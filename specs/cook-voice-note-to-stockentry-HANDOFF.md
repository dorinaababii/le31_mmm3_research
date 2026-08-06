# cook-voice-note-to-stockentry — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/38-cook-voice-note-to-stockentry.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `38`
- Slug: `cook-voice-note-to-stockentry`
- Contract file: `features/38-cook-voice-note-to-stockentry.md`
- Bucket: v2-AI (Whisper.cpp local install + new bot flow)
- Linear parent: HMM-40 (Brainstorm 2026-08-06 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: experiment.** (Start with one cook during one lunch rush,
measure time-to-86 with vs without voice.)

Evidence precondition: **inferred** (2 well-starred in-window GitHub
repos from hands-busy / accessibility voice tooling — `C-Loftus/sight-free-talon`
24★, `LeonardNJU/CaveBridge` 30★ — share the voice-as-typed-input
pattern). Confidence: **medium**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/config.py                            # NEW: VOICE_ENABLED (bool, default False), WHISPER_MODEL_PATH
backend/app/models.py                            # NEW: VoiceTranscript SQLModel
backend/app/services/voice_transcribe.py           # NEW: transcribe_ogg(path) wrapper
backend/app/bot/cook_bot_voice86.py              # NEW: voice message handler + confirmation keyboard
backend/app/main.py                              # NEW: lifespan smoke test for whisper binary
backend/app/events/stockentry_append_only.py     # extend listener to cover VoiceTranscript
backend/alembic/versions/<new>_voice_transcript.py   # NEW migration
backend/README.md                                # note the whisper install + model download
```

**System-level dependencies (NOT pip)**:

```
# whisper.cpp binary — MIT, build from source
git clone https://github.com/ggerganov/whisper.cpp /opt/whisper.cpp
cd /opt/whisper.cpp && make -j

# Model — whisper.cpp-tiny.en (English-only, ~39 MB, MIT)
mkdir -p /opt/data/le31-whisper/models
curl -L -o /opt/data/le31-whisper/models/ggml-tiny.en.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.en.bin
```

The Python `transcribe_ogg()` wrapper calls the binary via
`subprocess.run(["/opt/whisper.cpp/build/bin/whisper-cli", "-m",
WHISPER_MODEL_PATH, "-f", temp_path, "--no-timestamps", "--language",
"en", "--output-file", temp_out])` — same pattern as the existing
OCR adapter in feature 04.

## Endpoints and contracts added

No new HTTP routes. All logic lives in the bot webhook.

One new bot message handler:

- `voice` content type → routes to the `/voice86` flow. Handler:
  1. Download the voice note from Telegram to a temp `.ogg`.
  2. Call `transcribe_ogg(temp_path)` (sub-200 ms).
  3. Parse the transcript with the same regex as typed `/86`.
  4. Reply with the confirmation keyboard (3 buttons).
  5. On `Confirm` callback: write `StockEntry` with
     `source="telegram:cook-voice"` and `rationale=<transcript>`, write
     one `VoiceTranscript` row, delete the temp `.ogg`.
  6. On `Re-record` callback: ask for new voice note.
  7. On `Edit (typed)` callback: prompt for typed input.

One new SQLModel table:

```python
# backend/app/models.py
class VoiceTranscript(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transcript: str = Field(max_length=240)
    source: str = Field(max_length=40)
    stock_entry_id: int = Field(foreign_key="stockentry.id", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
```

Append-only (extended `stockentry_append_only` listener).

One new Alembic migration:

```python
def upgrade():
    op.create_table(
        "voicetranscript",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("transcript", sa.String(240), nullable=False),
        sa.Column("source", sa.String(40), nullable=False),
        sa.Column("stock_entry_id", sa.Integer, sa.ForeignKey("stockentry.id"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_voicetranscript_stock_entry_id", "voicetranscript", ["stock_entry_id"])

def downgrade():
    op.drop_index("ix_voicetranscript_stock_entry_id", table_name="voicetranscript")
    op.drop_table("voicetranscript")
```

## Verification

1. Whisper.cpp binary smoke test passes on a fresh install.
2. `transcribe_ogg()` unit tests (mocked subprocess) + integration
   test against a 5-second sample `.ogg` recording.
3. End-to-end voice flow: cook sends voice note → bot transcribes →
   confirmation keyboard appears → cook taps Confirm → `StockEntry`
   written with `rationale` populated → `VoiceTranscript` written →
   SSE event fires → temp `.ogg` deleted.
4. Re-record + Edit (typed) confirmation paths observed working.
5. Failure paths observed: missing binary → typed fallback; bad audio
   → typed fallback; unparseable transcript → typed fallback.
6. No audio files retained after transcription (verify temp dir is
   empty after the round-trip).
7. Existing tests still green (feature 37's `/86` typed command must
   continue to work unchanged).

## Rollback path

Set `VOICE_ENABLED = False` in config and restart — voice command is
silently refused, typed `/86` (feature 37) keeps working. To fully
rollback: drop the `VoiceTranscript` table (migration downgrade),
remove the new files, remove the bot message handler. Feature 37's
typed `/86` is unaffected.

## Dependencies

- New system dependency: `whisper.cpp` binary on the host. MIT. Build
  with `make -j` from the upstream repo.
- New file: `whisper.cpp-tiny.en.bin` model (~39 MB) downloaded once
  to `/opt/data/le31-whisper/models/`. Path is config-driven via
  `WHISPER_MODEL_PATH`.
- **Required upstream features**:
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column and the model-layer guard.
  - feature 04 (cook Telegram bot) — supplies the webhook primitive.
- **Required downstream features**: none.