# 228 — QuentinFuxa/WhisperLiveKit v2-streaming-real-time-architecture-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 streaming/real-time/WebSocket question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/228-QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible.md` (defer artifact; **no code today**).

Bucket: **v2 streaming/real-time-architecture-reference (FastAPI + WebSocket + real-time + streaming + local-ASR + speaker-diarization + translation + OpenAI/Deepgram-compatible-APIs, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a streaming/real-time/WebSocket surface (a voice-input to the cook-bot, a bi-directional DOM-diffs to the waiter web UI, an OpenAI/Deepgram-compatible-API surface for vendor-agnostic speech-to-text integration, or any streaming/real-time route beyond feature 23's SSE cook-channel), what is the *FastAPI + WebSocket + real-time + streaming + local-ASR + OpenAI/Deepgram-compatible-API* vocabulary that preserves the existing v1 SSE cook-channel posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 43.8 KB with 11097★/1140⑂ + Apache-2.0 permissive license + 12 topics + in-window-by-pushed_at-only is shipping the *FastAPI + WebSocket + real-time + streaming + local-ASR + OpenAI/Deepgram-compatible-API* primitive as the v2 streaming/real-time-architecture discipline*, but struggles because *v1 has no documented WebSocket + local-ASR + OpenAI-compatible-API primitive in the charter*, so that *v2 can introduce the WebSocket + local-ASR + OpenAI-compatible-API vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no WebSocket+ voice-input trigger; the JTBD is primitive vocabulary extension + WebSocket + local-ASR + OpenAI-compatible-API documentation, not a build-need; **cross-section JTBD value is moderate** — the highest-star-count in-window 2026 Python candidate of the 57-pass brainstorm series = the *FastAPI + WebSocket + real-time + streaming* vocabulary reference, but the *speech-recognition* itself is off-pattern for LE31 v1 today). |
| 2 | **Viability** | Maintainer can read 43.8 KB repo description + 12-topic vocabulary + FastAPI + WebSocket + real-time + streaming + local-ASR + speaker-diarization + translation + OpenAI/Deepgram-compatible-APIs octuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *WebSocket + local-ASR + OpenAI-compatible-API* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + SSE cook-channel stack, not imported from the Apache-2.0-permissive code; LE31 v1 has no WebSocket + voice-input surface today). Confidence: medium for the *WebSocket + local-ASR + OpenAI-compatible-API* vocabulary (11097★/1140⑂ + Apache-2.0 permissive license + 12 topics + in-window-by-pushed_at-only + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *FastAPI + WebSocket + real-time + streaming* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the streaming-stateful-connection dimension*; the *local-ASR + OpenAI-compatible-API* discipline IS the *vendor-agnostic-API + on-device-inference posture* applied to the voice-input dimension). Stack: FastAPI + SQLModel + PostgreSQL backend = on-pattern for v1 primitives (matches v1 charter §3.2 baseline); WebSocket = off-pattern for v1 (LE31 v1 uses SSE per feature 23); local-ASR = off-pattern for v1 (LE31 v1 cook-bot is text-only per charter §3.1); speaker-diarization = off-pattern for v1 (LE31 v1 has no voice-input today); translation = off-pattern for v1 (LE31 v1 is single-language today); OpenAI/Deepgram-compatible-APIs = off-pattern for v1 (LE31 v1 has zero external-API integration today); Apache-2.0 permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *WebSocket + local-ASR + OpenAI-compatible-API* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the streaming-stateful-connection dimension* (every state transition is an explicit SQLModel row; no silent transition; the *SSE-cook-channel* pattern IS the *streaming* primitive). Charter §3.1 alignment (the *WebSocket + local-ASR + OpenAI-compatible-API* discipline IS the *explicit-state-transition* applied to the streaming-stateful-connection dimension); §3.2 STRICTLY-COMPATIBLE (Apache-2.0 permissive); **§3.4 NOT triggered** (WhisperLiveKit is *operator-tooling* — voice input from the cook to the cook-bot, NOT customer-facing-AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 streaming/real-time-architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 43.8 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours with caveat: 43.8 KB modest-repo size limits inspection depth). **Cost-to-value ratio: moderate** (the *FastAPI + WebSocket + real-time + streaming + local-ASR + OpenAI/Deepgram-compatible-APIs* octuple + the highest-star-count signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/228-QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible-HANDOFF.md` and `features/228-QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + WebSocket + local-ASR + OpenAI-compatible-API documentation for the next v2 streaming/real-time-architecture review moment; **cross-section JTBD value is moderate, the highest-star-count in-window 2026 Python candidate of the 57-pass brainstorm series = the *FastAPI + WebSocket + real-time + streaming* vocabulary reference, but the *speech-recognition* itself is off-pattern for LE31 v1 today**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a voice-input surface to the cook-Telegram-bot, a WebSocket route to the waiter web UI, a streaming/real-time route beyond feature 23's SSE cook-channel, or an OpenAI/Deepgram-compatible API surface):

- `app/voice_input/` — possibly add (the voice-input module; depends on the v2 change).
- `app/voice_input/asr.py` — possibly add (the local-ASR execution handler; depends on the v2 change).
- `app/voice_input/transcript.py` — possibly add (the transcript-routing handler; depends on the v2 change).
- `app/voice_input/speaker.py` — possibly add (the speaker-diarization handler; depends on the v2 change).
- `app/voice_input/translation.py` — possibly add (the translation handler; depends on the v2 change).
- `app/streaming/` — possibly add (the WebSocket streaming module; depends on the v2 change).
- `app/streaming/websocket.py` — possibly add (the WebSocket route; depends on the v2 change).
- `app/external_apis/` — possibly add (the OpenAI/Deepgram-compatible-API layer; depends on the v2 change).
- `app/models/voice_transcript.py` — possibly add (the `voice_transcript` SQLModel table; depends on the v2 change).
- `app/models/speaker.py` — possibly add (the `speaker` SQLModel table; depends on the v2 change).
- `tests/test_voice_input.py` + `tests/test_streaming.py` + `tests/test_external_apis.py` — possibly add (the integration tests for the voice-input + streaming + external-API surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no voice-input surface added, no WebSocket route added, no OpenAI/Deepgram-compatible-API surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/228-QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible.md` exists and is read back by the parent.
- [ ] `specs/228-QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `QuentinFuxa/WhisperLiveKit` description is quoted verbatim (43.8 KB repo).
- [ ] The 11097★/1140⑂ + Apache-2.0 permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + in-window-by-pushed_at-only + 12 topics + description *"Real-time, local speech-to-text with streaming ASR, speaker diarization, translation, and OpenAI/Deepgram-compatible APIs."* is documented.
- [ ] The charter §3.1 alignment via *WebSocket + local-ASR + OpenAI-compatible-API = explicit-state-transition discipline applied to streaming-stateful-connection* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (Apache-2.0 permissive) is documented.
- [ ] The charter §3.4 NOT-triggered (WhisperLiveKit is operator-tooling, NOT customer-facing-AI) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a voice-input surface to the cook-Telegram-bot, a WebSocket route to the waiter web UI, a streaming/real-time route beyond feature 23's SSE cook-channel, or an OpenAI/Deepgram-compatible API surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `QuentinFuxa/WhisperLiveKit` *FastAPI + WebSocket + real-time + streaming + local-ASR + OpenAI/Deepgram-compatible-APIs* vocabulary is evaluated against the PR's changes: does the change address the *streaming-stateful-connection* discipline? does the change preserve the *local-ASR* primitive? does the change preserve the *OpenAI-compatible-API* posture? does the change preserve the *charter §3.1 explicit-state-transition* pattern? does the change preserve the *charter §3.4 operator-tooling boundary*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

Fully reversible. Delete `specs/228-QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible-HANDOFF.md` and `features/228-QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible.md`. The git revert path is `git revert HEAD~0 -- features/228-...md specs/228-...-HANDOFF.md` (or whichever commit introduced the files). No retained data; no safe-failure-mode concern; no operator-visible behavior change.

## 6. Mandatory LE31 skill list

The coding agent MUST load and follow these skills before starting work on this HANDOFF (per `le31-coding-agent-brief/SKILL.md`):

- `le31-conventions/SKILL.md` — the canonical seven-check feature gate + the v1/v2/v2-AI bucket taxonomy.
- `le31-daily-brainstorm/SKILL.md` — the parent context for cross-section picks + the daily-brainstorm-no-fabrication-canary.
- `le31-daily-research/SKILL.md` — the sister daily-research skill for source-family coverage.
- `le31-feature-pipeline/SKILL.md` — the immediate parent skill for this HANDOFF.
- `le31-verification-protocol/SKILL.md` — the verification protocol referenced in §4.
- `le31-coding-agent-brief/SKILL.md` — the skill that produces the paste-in prompt-in prompt automatically from this slice contract; do not paste chat excerpts.
- `le31-handoff-spec/SKILL.md` — the skill that defines this HANDOFF format.
- `le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern reference.

**Do not start any code work today.** The HANDOFF is documentation-only.

## 7. Honest disclosure

- The 11097★/1140⑂ is explicitly NOT offered as evidence of *LE31 needing speech-recognition*; the 11097★/1140⑂ is for the *speech-recognition domain*, not for the *FastAPI + WebSocket + real-time + streaming* primitive. The transferable item is the *technique* (FastAPI + WebSocket + real-time + streaming + OpenAI-compatible-API), not the *speech-recognition* itself.
- LE31 v1 today does not need a *speech-recognition* primitive (the cook-bot is text-only per charter §3.1), but v2's *voice-input-to-cook-bot* surface would inherit the *FastAPI + WebSocket + real-time ASR* primitive.
- The 43.8 KB size is modest; source-code inspection depth is limited; the *vocabulary* is high-value, the *code* is reference-only.
- Charter §3.4 NOT triggered because WhisperLiveKit is operator-tooling (voice input from cook to cook-bot), NOT customer-facing-AI.