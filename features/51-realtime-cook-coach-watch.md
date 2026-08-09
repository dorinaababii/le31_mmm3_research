# Feature 51 — Realtime Cook Coach Watch (parking-lot)

> **Priority**: P3 · **Effort**: parking-lot (no build) · **Source**: brainstorm 2026-08-09 (cross-section pick C) · **Bucket**: parking-lot
> **One-line**: A paper artifact that documents the real-time-mid-task-AI-coach category watch — if feature 38 (`cook-voice-note-to-stockentry`) is reported as choppy and the operator wants a *real-time conversational* Q&A on the live ledger ("how much ricotta do I have left?"), the strongest in-window OSS reference is `pathorsAI/parley` (13★, pushed 2026-08-09T06:30:31Z). No build, no commit, no `features/52` follow-up.

## Goal

Today feature 38 (`cook-voice-note-to-stockentry`) is a *choppy* one-shot upload-the-audio pattern: the cook records a voice note in Telegram, the bot downloads it, transcribes via local Whisper.cpp, asks "confirm: 86 lamb", then writes a `StockEntry` with the transcript as the rationale. This works but is a *batch* interaction (one audio file per note).

`pathorsAI/parley` (pushed 2026-08-09T06:30:31Z, **13★** — the strongest in-window star count of the pass that is non-filed and not already on the watch list, "Real-time AI coaching for sales & negotiation calls — live suggestions while you talk, voice translation into the meeting, deep debrief after. Local-first macOS app, bring your own keys.") is the strongest new in-window *category signal* for a *real-time mid-task AI coach* primitive — different from feature 48's `pipecat-ai/pipecat` (which is the *infrastructure* — the voice-agent framework), and different from feature 38 (which is the *choppy upload pattern*). Parley is the *use-case* (real-time conversational Q&A on a live task).

Translated to LE31, a v3 follow-up to feature 38 could be a real-time cook coach: the cook is mid-service, asks "how much ricotta do I have left?" and the bot answers within 200 ms from the live `StockEntry` + `PrepSheet` + recipe tables, without uploading a voice note first. The cook then says "void 2 kg, I just dropped it" and the bot writes a `StockEntry` with the rationale "cook dropped 2 kg of ricotta". The interaction is conversational, mid-task, and ends with a confirmation step (the LE31 *AI invariant*).

This feature is a **parking-lot paper artifact**: no build, no commit, no `features/52` follow-up. The artifact exists so when the operator does report the choppy pattern is a problem (or the cook asks for a conversational Q&A), the path is documented and not a fresh research effort.

Inspired by today's brainstorm: GitHub `topic:real-time` repo `pathorsAI/parley` (pushed 2026-08-09T06:30:31Z, 13★, "Real-time AI coaching for sales & negotiation calls — live suggestions while you talk, voice translation into the meeting, deep debrief after. Local-first macOS app, bring your own keys."). The repo comes from the *sales-tech / AI-coaching* world — completely outside hospitality — and shares the LE31 *cook-as-operator* primitive, but reframes it as a *real-time mid-task AI coach* (live voice translation + post-call debrief).

Distinct from feature 38 (`cook-voice-note-to-stockentry`) because 38 is *upload-the-audio → write one row*; this is *use-case* (conversational Q&A on the live ledger). Distinct from feature 48 (`pipecat-voice-watch`) because 48 is *infrastructure* (the voice-agent framework), not *use-case*; this is *use-case* (real-time conversational Q&A on the live ledger).

## Evidence / JTBD

When LE31 considers replacing feature 38's choppy cook voice with a real-time conversational Q&A on the live ledger, the implementer wants to know the OSS options, but the operator reports no current pain, so the watch is documented and the build is deferred.

## Scope

**In scope (parking-lot):**
- This feature file only.
- A one-paragraph note in the §"Why this matters" section documenting the migration path.
- A pointer to `pathorsAI/parley` and the broader real-time-mid-task-AI-coach category (e.g. `pathorsAI/parley`, `pipecat-ai/pipecat` for the infrastructure, `livekit/agents`, `moshi`, `ultravox` for adjacent voice-agent primitives).

**Out of scope (parking-lot):**
- No code. No migration. No new feature file follow-up.
- No LLM dependency added to LE31.
- No schema change.
- No new infrastructure.
- No competitive analysis (parley is one of several in the category; a full comparison is a v3 effort).

## Why this matters

The real-time-mid-task-AI-coach OSS category has matured in 2026; `pathorsAI/parley` at 13★ (pushed 2026-08-09T06:30:31Z) is the strongest in-window non-filed hit, sitting alongside the prior voice-agent watch (feature 48 — `pipecat-ai/pipecat` 13991★). The two artifacts together tell the same story: the *infrastructure* (pipecat) and the *use-case* (parley) are both production-ready.

LE31's feature 38 is a *batch* choppy pattern — works fine but is not the future-path. The future-path is *real-time conversational Q&A* on the live ledger, with a confirmation step before any state change. If the operator reports "the choppy pattern is annoying because I want to interrupt mid-note", or "the choppy pattern misses overlapping voices during service rush", or "I want to ask the bot how much ricotta I have left without typing", then feature 38 should be revisited.

When feature 38 is revisited, the migration path is:

1. Stand up a `pathorsAI/parley`-style real-time voice agent as a sidecar service (FastAPI + the parley pattern + local Whisper.cpp + Qwen2.5-3B for NLU). The exact stack is open — parley is macOS local-first, but the *pattern* (real-time stream + local LLM + post-task debrief) is what matters.
2. Replace the Telegram `voice` upload handler with a *streaming* voice handler. The cook's voice is transcribed as it arrives; partial transcripts are matched against the live `StockEntry` + `PrepSheet` + recipe tables.
3. Keep the *confirmation* step (the cook says "confirm 86 lamb" before the `StockEntry` is written) — this is the LE31 *AI invariant* (no silent auto-state-transition).
4. Add a *non-LLM fallback* path: if Qwen2.5-3B is down, fall back to the existing feature 38 choppy pattern. This is the LE31 *circuit breaker*.
5. Add a *post-task debrief* (the parley pattern): at the end of service, the bot sends the cook a 30-second summary of the Q&A interactions (e.g. "you asked 14 questions today, 11 were answered from the live ledger, 3 required a human review").

Estimated effort: 5-7 days for the migration (parallel to building feature 38 was 3 days). The LE31 code is mostly the same; the wrapper changes.

This file exists so the implementer has the path on file. **No build today.** Revisit only if feature 38 is reported as a problem or the operator asks for a conversational Q&A on the live ledger.
