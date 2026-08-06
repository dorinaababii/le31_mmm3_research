# Feature 38 — Cook Voice Note to StockEntry

> **Priority**: P2 · **Effort**: M (≤5 days) · **Source**: brainstorm 2026-08-06
> (cross-section pick B) · **Bucket**: v2-AI
> **One-line**: Cook sends a Telegram voice note ("we're out of lamb,
> eighty-six it"); bot transcribes via local Whisper.cpp, asks "confirm: 86
> lamb", then writes a `StockEntry` with the transcript as the new
> `rationale` column (from feature 37) and the negative delta for the item.
> The typed variant (`/86 <item> <reason>`) is always available as the
> non-AI fallback.

## Goal

Move the cook surface's input modality from typed-Telegram-only to
voice-or-typed-Telegram. The cook's hands are greasy and the cook can't
stop to type during service; the cook should be able to 86 an item with
one tap of a voice note, get a one-tap confirmation, and have the
`StockEntry` row written in <10 seconds. The typed variant stays the
default for cooks who prefer it and as the always-on non-AI fallback
(charter §3.3: "AI may assist owner/staff, with observable evidence and a
non-AI fallback").

Inspired by today's brainstorm: GitHub `topic:hci` repos
`C-Loftus/sight-free-talon` (24★, "Integrate Talon voice dictation
commands with TTS, screen readers, braille, and more!") and
`LeonardNJU/CaveBridge` (30★, "Play the 1977 classic Colossal Cave
Adventure by just talking — in any language your LLM speaks. An LLM
Dungeon Master turns free-form voice into typed adventure commands.").
Both come from the hands-busy accessibility / hobbyist voice tooling
world — not from any POS — and translate directly to the cook's
greasy-hands / can't-stop-to-type pain. Voice is the missing modality for
the cook surface.

This feature is a thin layer on top of feature 37 (`void-rationale-ledger-field`).
The cook's voice note supplies the rationale; the model-layer guard from
feature 37 then refuses to write a negative-delta `StockEntry` without
a `rationale`. Same `StockEntry` row, same append-only invariant, same
`CookChannel` SSE event — only the input modality changes.

## Evidence / JTBD

When the cook 86s an item mid-service, the cook wants to record the 86 and
the reason, but struggles because the cook station's hands are greasy and
the cook can't stop to type a `/86 lamb` command, so that a one-tap voice
note → transcribed confirm → appended `StockEntry` writes the 86 in
<10 seconds.

## Scope

**In scope (v2-AI):**
- New local install of Whisper.cpp on the same box as the FastAPI server
  (small model, `whisper.cpp-tiny.en` — English-only, ~39 MB, MIT, sub-200
  ms latency on a modern CPU). No cloud API, no API key, no PII leaving
  the device.
- New Python wrapper `backend/app/services/voice_transcribe.py` exposing
  one function `transcribe_ogg(path: Path) -> str` that runs the whisper
  binary against the supplied audio file and returns the plaintext
  transcript.
- New cook-bot command `/voice86` (audio-message trigger): bot downloads
  the incoming voice note from Telegram (already supported by aiogram),
  writes it to a temp `.ogg`, calls `transcribe_ogg`, parses the
  transcript with the same regex used by the typed `/86` command
  (`/86 <item> <reason>`), and shows the cook a confirmation keyboard
  with three buttons: `Confirm`, `Re-record`, `Edit (typed)`.
- On `Confirm` tap: bot writes one `StockEntry` with `qty_delta = -<batch>`
  (same logic as typed `/86`), `reason = "86"`, `rationale = <transcript>`,
  `source = "telegram:cook-voice"`.
- On `Re-record` tap: bot sends "Send the new voice note" and re-enters
  the flow.
- On `Edit (typed)` tap: bot sends "Type the 86 command now (e.g.
  `/86 lamb burned`)" and re-enters via the typed path (feature 37's
  command).
- A config field `VOICE_ENABLED: bool = False` (default off) in
  `backend/app/config.py`. The cook bot refuses `/voice86` with "voice
  input disabled by config" if False.
- A new `VoiceTranscript` SQLModel table (append-only) recording
  `(id, transcript, source, created_at, stock_entry_id)` for audit. The
  transcript is the new `rationale` value; the `VoiceTranscript` row is
  the durable record of the audio-as-text path. Same append-only invariant.
- A startup-time smoke test in `backend/app/main.py` that, if
  `VOICE_ENABLED = True`, checks the whisper binary is on PATH and the
  model file is present, otherwise logs a clear error at boot and disables
  voice input for the lifetime of the process.

**Out of scope (v2-AI):**
- Multi-item voice notes ("86 lamb and salmon, we're out of both") —
  single-item only in v1. Multi-item is a v3 problem.
- Voice for any other bot command (`/void`, `/cook`, `/receive`, etc.) —
  only `/voice86` in v1; extending to other commands is a follow-up.
- Speaker diarisation or multi-language detection — single-language
  English-only in v1 (`whisper.cpp-tiny.en`).
- Voice notes longer than 30 seconds — Telegram voice notes are typically
  <30 s; longer notes are clipped with a bot reply "voice note too long,
  keep under 30 s".
- Auto-86 without cook confirmation — explicit confirmation button is
  always required (charter §3.2: explicit operational transitions only).
- Cloud speech-to-text APIs (Google / Whisper hosted / Deepgram) —
  explicit decision to stay local because (a) cook voice notes may
  contain guest PII, (b) no new operational cost, (c) no API key
  management.

## User flow

**Cook — 86 with a voice note:**

1. Cook taps-and-holds the Telegram mic, says "we're out of lamb,
   eighty-six it", releases.
2. Telegram delivers the voice note to the existing cook-bot webhook.
3. Bot replies immediately with "🎙️ Got it — transcribing…" (loading
   indicator).
4. Bot calls `transcribe_ogg(temp_path)` — sub-200 ms on a modern CPU.
5. Bot replies with the parsed interpretation:
   ```
   I heard:
   > "we're out of lamb eighty-six it"

   Confirm 86 lamb?
   [✅ Confirm] [🎙️ Re-record] [⌨️ Edit typed]
   ```
6. Cook taps `✅ Confirm`.
7. Bot writes one `StockEntry` row with `qty_delta=-<batch>`,
   `reason="86"`, `rationale="we're out of lamb eighty-six it"`,
   `source="telegram:cook-voice"`. Also writes one `VoiceTranscript` row
   linking to the new `StockEntry`.
8. Bot replies with one line: "86 lamb written. Rationale: we ran out of
   lamb. (StockEntry #1234)" and pushes to `CookChannel` SSE.
9. Bot deletes the temp audio file (no PII retention).

**Cook — re-records after a mis-transcription:**

1. ...same as steps 1–5 above...
2. Cook taps `🎙️ Re-record`.
3. Bot replies "Send the new voice note".
4. Cook sends a new voice note.
5. ...back to step 4 above.

**Cook — falls back to typed input when voice is disabled or fails:**

1. Cook sends `/86 lamb burned the second batch` (typed).
2. Same as feature 37's typed path. `source="telegram:cook"` (typed, not
   voice).

## Data model

Two changes to existing models, one new table:

```python
# backend/app/models.py (additive patch)

class StockEntry(SQLModel, table=True):
    # ... all existing fields ...
    rationale: str | None = Field(default=None, max_length=240, index=True)
    # NEW: which source channel the rationale came from; defaults to
    # the value of `source`; the voice path appends ":voice" suffix.
    # Used for analytics only; not a control field.

# NEW table: durable record of audio → text path
class VoiceTranscript(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transcript: str = Field(max_length=240)
    source: str = Field(max_length=40)         # e.g. "telegram:cook"
    stock_entry_id: int = Field(foreign_key="stockentry.id", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
```

`VoiceTranscript` is itself append-only (same SQLAlchemy listener as
`StockEntry` and `OwnerAuditEvent`).

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04 + feature 37):**
- New message handler for `voice` content type → routes to
  `/voice86` flow.
- Confirmation keyboard uses `aiogram.types.InlineKeyboardMarkup` with
  three `InlineKeyboardButton`s with `callback_data`:
  - `voice86:confirm:<transcript>:<item>`
  - `voice86:rerecord:<transcript>:<item>`
  - `voice86:edit:<transcript>:<item>`
- The `/voice86` command is chat-id allowlisted same as feature 04.
- Disabled state (`VOICE_ENABLED = False`): bot replies "voice input
  disabled by config — use typed `/86 <item> <reason>` instead".

**API (FastAPI):**
- No new HTTP routes. All logic lives in the bot webhook. The
  `VoiceTranscript` table is internal to the bot; the existing
  `/api/stock/rationale_search` (feature 37) automatically picks up
  voice-originated rationales because it reads `StockEntry.rationale`.

**UI:**
- No new UI surfaces. The cook's UI is the existing Telegram chat.
  The waiter's UI is unchanged. The manager's UI is unchanged.

## Dependencies

- **New system dependency**: `whisper.cpp` binary on the host
  (build with `make` from the upstream repo, MIT). On Ubuntu 24.04:
  `apt install -y build-essential && git clone https://github.com/ggerganov/whisper.cpp && cd whisper.cpp && make -j`. No new Python pip package needed —
  `transcribe_ogg` calls the binary via `subprocess.run` (existing
  pattern from the OCR adapter in feature 04).
- **New file**: `whisper.cpp-tiny.en.bin` model (~39 MB) downloaded
  once at install time to `/opt/data/le31-whisper/models/`. Path is
  config-driven via `WHISPER_MODEL_PATH`.
- **Required upstream features**:
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column and the model-layer guard that prevents silent
    negative-delta writes.
  - feature 04 (cook Telegram bot) — supplies the webhook primitive.
- **Required downstream features**: none.

## Failure / recovery

- **Whisper binary missing at startup**: `VOICE_ENABLED` auto-flips to
  False for the lifetime of the process; clear log entry at boot. Cook
  bot replies with the disabled message; typed `/86` still works.
- **Transcription fails (audio too quiet / unsupported codec)**:
  bot replies "Couldn't transcribe — try again or type the command".
  No `StockEntry` written.
- **Cook taps `Confirm` after re-recording too many times (3)**: bot
  replies "Please type the command instead" and stops accepting
  `/voice86` from that chat for 60 seconds.
- **Transcript contains no parseable item**: bot replies "I didn't catch
  the item name — try again or type `/86 <item> <reason>`". No write.
- **Audio file retention**: temp `.ogg` is deleted immediately after
  `transcribe_ogg` returns (try/finally). The `VoiceTranscript` table
  stores only the *transcript text*, never the audio.

## Definition of done

- [ ] Whisper.cpp binary installed on the host; `whisper.cpp-tiny.en.bin`
      model downloaded.
- [ ] `transcribe_ogg()` Python wrapper ships with unit tests (mocked
      binary subprocess) and an integration test against a 5-second
      sample `.ogg`.
- [ ] `/voice86` cook-bot flow ships; end-to-end observed (cook sends
      voice note → bot transcribes → confirmation keyboard → cook taps
      Confirm → `StockEntry` written with `rationale` populated →
      `CookChannel` SSE event fires).
- [ ] `VoiceTranscript` table added; `append-only` listener extended.
- [ ] `VOICE_ENABLED` config flag shipped (off by default); boot-time
      smoke test runs and flips off if binary missing.
- [ ] Re-record + Edit (typed) confirmation paths observed working.
- [ ] Failure paths observed: missing binary → typed fallback; bad
      audio → typed fallback; unparseable transcript → typed fallback.
- [ ] No audio files retained after transcription.
- [ ] Existing tests still green.
- [ ] End-to-end acceptance: a single 86-from-voice round-trip completes
      in <10 seconds wall-clock from voice-note-sent to `StockEntry`
      written, on a pilot-grade VPS.

## Open questions

- Should the voice variant record the raw transcript or a cleaned-up
  version (e.g. strip filler words like "um", "uh", repeated words)?
  Decision: store the raw transcript as `rationale`; the owner can
  always read the cook's actual words. Cleaning is a v3 polish.
- Should the cook bot push the SSE event as the typed variant
  (`source="telegram:cook"`) or differentiate (`source="telegram:cook-voice"`)?
  Decision: differentiate — the analytics on `source` field then
  answers "how often is the cook using voice vs typed?" without extra
  instrumentation.
- Whisper.cpp CPU vs GPU? Decision: CPU only for v1; GPU is overkill
  for the latency target and adds a CUDA dep. Re-evaluate if a future
  restaurant pilots a multi-cook station and latency becomes the
  bottleneck.

## Why this matters

Voice is the missing input modality for the cook surface. The two
real-world in-window peers (`C-Loftus/sight-free-talon` 24★,
`LeonardNJU/CaveBridge` 30★) come from the hands-busy accessibility /
hobbyist voice tooling world — completely outside hospitality — and
translate directly to the cook's greasy-hands / can't-stop-to-type pain.

This feature is a thin layer on top of feature 37's rationale column —
the cook's voice note supplies the rationale that feature 37's
model-layer guard requires. Same `StockEntry` row, same append-only
invariant, same `CookChannel` SSE event. The non-AI typed fallback is
always available (charter §3.3). No cloud API, no PII leaving the device
(Whisper.cpp is local). Medium cost, high value if the cook surface is
the dominant friction in any LE31 pilot (it almost certainly is).