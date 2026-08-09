# Feature 48 — Pipecat Voice Watch (parking-lot)

> **Priority**: P3 · **Effort**: parking-lot (no build) · **Source**: brainstorm 2026-08-08 (cross-section pick C) · **Bucket**: parking-lot
> **One-line**: A paper artifact that documents the voice-agent category watch — if feature 38's choppy cook-voice note-to-StockEntry is reported as a problem, the migration path is `pipecat-ai/pipecat` (13991★, pushed 2026-08-08) and its derivatives. No build, no commit, no `features/49` follow-up.

## Goal

Today feature 38 (`cook-voice-note-to-stockentry`) is a *choppy* one-shot upload-the-audio pattern: the cook records a voice note in Telegram, the bot downloads it, transcribes via local Whisper.cpp, asks "confirm: 86 lamb", then writes a `StockEntry` with the transcript as the rationale. This works but is a *batch* interaction (one audio file per note).

`pipecat-ai/pipecat` (pushed 2026-08-08T04:00:13Z, **13991★** — the strongest in-window star count of the pass, "Open Source framework for voice agents, multimodal apps, and realtime AI. Maintained by Daily and the community") is the strongest new in-window *category signal* for a *real-time streamed voice agent* pattern. A v3 follow-up to feature 38 could replace the choppy pattern with a pipecat pipeline if the LLM dependency is acceptable.

This feature is a **parking-lot paper artifact**: no build, no commit, no `features/49` follow-up. The artifact exists so when the operator does report the choppy pattern is a problem, the path is documented and not a fresh research effort.

Inspired by today's brainstorm: GitHub `topic:real-time` repo `pipecat-ai/pipecat` (pushed 2026-08-08T04:00:13Z, 13991★). The repo comes from the *AI-agent / developer-tools* world — completely outside hospitality — and shares the *real-time voice agent pipeline* primitive. Translated to LE31, this is the missing *category watch* — the future-path for feature 38.

Distinct from feature 38 (`cook-voice-note-to-stockentry`) because 38 is a one-shot choppy pattern; this is a watch for *if/when* 38 is reported as a problem.

## Evidence / JTBD

When LE31 considers replacing feature 38's choppy cook voice with a real-time voice agent, the implementer wants to know the OSS options, but the operator reports no current pain, so the watch is documented and the build is deferred.

## Scope

**In scope (parking-lot):**
- This feature file only.
- A one-paragraph note in the §"Why this matters" section documenting the migration path.
- A pointer to `pipecat-ai/pipecat` and the broader voice-agent category (e.g. `pipecat-ai/pipecat`, `livekit/agents`, `moshi`, `ultravox`).

**Out of scope (parking-lot):**
- No code. No migration. No new feature file follow-up.
- No LLM dependency added to LE31.
- No schema change.
- No new infrastructure.

## Why this matters

The voice-agent OSS category has matured in 2026; `pipecat-ai/pipecat` consolidating at 13991★ is the strongest single signal that the real-time streamed-voice pattern is production-ready. LE31's feature 38 is a *batch* choppy pattern — works fine but is not the future-path. The future-path is real-time streaming. If the operator reports "the choppy pattern is annoying because I want to interrupt mid-note", or "the choppy pattern misses overlapping voices during service rush", then feature 38 should be revisited.

When feature 38 is revisited, the migration path is:

1. Stand up a `pipecat` pipeline as a sidecar service (FastAPI + pipecat + local Whisper.cpp + Qwen2.5-3B for NLU).
2. Replace the Telegram `voice` upload handler with a `pipecat` WebSocket bridge.
3. Keep the *confirmation* step (cook says "confirm 86 lamb" before the StockEntry is written) — this is the LE31 *AI invariant* (no silent auto-state-transition).
4. Add a *non-LLM fallback* path: if Qwen2.5-3B is down, fall back to the existing feature 38 choppy pattern. This is the LE31 *circuit breaker*.

Estimated effort: 5-7 days for the migration (parallel to building feature 38 was 3 days). The LE31 code is mostly the same; the wrapper changes.

This file exists so the implementer has the path on file. **No build today.** Revisit only if feature 38 is reported as a problem.
