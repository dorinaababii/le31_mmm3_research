# Feature 228 — QuentinFuxa-WhisperLiveKit-apache-2-0-fastapi-websocket-real-time-streaming-asr-speaker-diarization-translation-openai-deepgram-compatible (defer)

> **NEW observation (2026-09-25).** Documents in-window GitHub Search `topic:real-time+language:python` query result: `QuentinFuxa/WhisperLiveKit` (**Apache-2.0 ✓**, **11097★/1140⑂** = the **highest-star-count in-window 2026 Python candidate of the 57-pass brainstorm series**; 4× higher star count than feature 222 `donbarbos/telegram-bot-template`'s 476★; parent-direct-GET confirms; subagent scored stars=`None` from search-result JSON), Python, **pushed 2026-09-21T04:36:02Z** (in-window by `pushed_at` only — *4 days before fetch time*), **created 2024-12-19T10:49:09Z** (~21-month-old repo with in-window `pushed_at` — `created_at` is OUT-OF-WINDOW by ~20 months), **43.8 KB** modest repo, `default_branch=main`, archived=`False`). **12 topics** (verbatim from raw JSON): `automatic-speech-recognition`, `fastapi`, `python`, `pytorch`, `real-time`, `speaker-diarization`, `speech-recognition`, `speech-to-text`, `streaming`, `translation`, `websocket`, `whisper`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-25): *"Real-time, local speech-to-text with streaming ASR, speaker diarization, translation, and OpenAI/Deepgram-compatible APIs."* The **FastAPI + WebSocket + real-time + streaming + local-ASR + speaker-diarization + translation + OpenAI/Deepgram-compatible-APIs** octuple primitive. Bucket: **v2 streaming/real-time-architecture-reference (parking-lot, future-voice-input-vocabulary-reference)** — watch-list entry, zero build time today.

## Goal

Retain the **FastAPI + WebSocket + real-time + streaming + local-ASR + speaker-diarization + translation + OpenAI/Deepgram-compatible-APIs** octuple-primitive as a persistent cross-section reference for any future LE31 v2 expansion that introduces a streaming/real-time/WebSocket surface (e.g., voice-input to the cook-bot; bi-directional DOM-diffs to the waiter web UI; any OpenAI/Deepgram-compatible-API surface). The artifact is the persistent cross-section reference + the 8 named architectural primitives. No code today (Apache-2.0 license permits future code reuse; vocabulary-only artifact today; 43.8 KB modest-repo size limits source-code inspection depth — the *vocabulary* is high-value, the *code* is reference-only).

## Scope

**In scope (defer artifact):**
- A written record of the **FastAPI + WebSocket + real-time + streaming** discipline: the *streaming-stateful-connection* primitive (LE31 v1's `sse-cook-channel` (feature 23) uses SSE; WebSocket is the bi-directional sibling; the *streaming + WebSocket + real-time + FastAPI* posture IS the *canonical v2 streaming/real-time-architecture vocabulary*).
- A written record of the **local-ASR** discipline: the *on-device-automatic-speech-recognition* primitive (the *local-ASR* discipline IS the *no-cloud-required-for-speech-to-text* posture; LE31 v1 today does not need a *speech-recognition* primitive, but v2's *voice-input-to-cook-bot* surface would inherit the *local-ASR* primitive).
- A written record of the **speaker-diarization** discipline: the *who-is-speaking* primitive (the *speaker-diarization* discipline IS the *multi-speaker-identification* posture; relevant for any v2 voice-input surface that needs to distinguish between cook-voice and owner-voice).
- A written record of the **translation** discipline: the *real-time-translation* primitive (the *translation* discipline IS the *automatic-language-translation* posture; LE31 v1 is Switzerland-Europe + multi-language; the *translation* discipline may be relevant for any v2 voice-input surface that needs to handle French/German/Italian/English).
- A written record of the **OpenAI/Deepgram-compatible-APIs** discipline: the *drop-in-replacement-API* primitive (the *OpenAI-compatible-API* pattern IS the *vendor-agnostic-API* posture; any v2 surface that integrates with an external speech-to-text provider should adopt the *OpenAI-compatible-API* pattern for vendor-agnosticism).
- A decision record: today's verdict is `defer` because LE31 v1 is not built today and v2 streaming/real-time-architecture surface expansion is not in scope; the cross-section reference is informative, not a build-trigger.
- A cross-section reference with the prior v2 streaming/real-time cluster: features 23 (`sse-cook-channel`), 25 (`fastapi-frontend-dev-loop`), 142 (`feldroy-air-fastapi-htmx-ai-write-framework`), 143 (`volfpeter-fasthx-htmx-fastapi-declarative-ssr`), 210 (`duckframework-duck-server-side-reactive-web-no-frontend-framework-no-javascript-stack`). The *transferable insight* is the **FastAPI + WebSocket + real-time + streaming** discipline shared by all 6 features.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2 horizontal-expansion surface in v2 (charter §3.1 + §3.2 invariant: v2 surface expansion is the next boundary; this is a vocabulary reference, not a v2 expansion trigger).
- Any voice-input surface in v1 (LE31 v1 cook-bot is text-only per charter §3.1; voice-input is a v2 expansion candidate).
- Any WebSocket surface in v1 (LE31 v1 uses SSE per feature 23; WebSocket is a v2 expansion candidate).
- Any OpenAI/Deepgram-compatible-API surface in v1 (LE31 v1 has no external-API integration today; the *OpenAI-compatible-API* pattern is a v2 expansion candidate).

## Description

The pick is **QuentinFuxa/WhisperLiveKit** — a Python + FastAPI + WebSocket + real-time + streaming + local-ASR + speaker-diarization + translation + OpenAI/Deepgram-compatible-APIs real-time local speech-to-text system. Charter §3.4 NOT triggered because WhisperLiveKit is operator-tooling (voice input from cook to cook-bot), NOT customer-facing-AI. The *speech-recognition* is a tool for the *cook/staff*, not a tool that interacts with restaurant diners. The artifact is the persistent cross-section reference for the 8 named primitives.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v2 surface that adopts any of the 8 primitives would extend the LE31 v1 data model with appropriate new tables (e.g., a `VoiceTranscript` table for the local-ASR primitive; a `Speaker` table for the speaker-diarization primitive; a `Translation` table for the translation primitive; a `StreamingSession` table for the WebSocket primitive). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v2 PR is triggered by the trigger condition below, the implementation would:
1. Read the WhisperLiveKit README at https://github.com/QuentinFuxa/WhisperLiveKit for the *FastAPI + WebSocket + real-time + streaming + local-ASR + speaker-diarization + translation + OpenAI/Deepgram-compatible-APIs* architecture pattern.
2. Cross-reference with LE31 v1's *FastAPI + SSE + Postgres + aiogram* stack to identify the *delta* (the *delta* = WhisperLiveKit uses WebSocket instead of SSE; WhisperLiveKit adds local-ASR + speaker-diarization + translation + OpenAI-compatible-API).
3. Apply charter §3.1 surface-expansion review to the *delta* (any new v2 surface requires explicit owner/charter sign-off; the voice-input delta is the most charter-sensitive because of charter §3.1 *operator-surface-only* boundary).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the WhisperLiveKit reference is the *vocabulary*, not the *code*.

## Telegram interaction

Zero new Telegram interaction today. Future v2 PR that adopts the *voice-input-to-cook-bot* primitive would extend the existing aiogram-bot (cook-bot per charter §3.1) with a voice-message handler that transcribes the audio via WhisperLiveKit and routes the transcript through the existing deterministic-template-renderer (the same pattern as chatty's *capture buy milk* deterministic-intercept). The *voice-input* primitive is *operator-tooling* (cook → cook-bot), NOT customer-facing-AI; charter §3.4 is NOT triggered.

## Dependencies

- LE31 charter §3.1 surface-expansion review (for any v2 surface adoption).
- LE31 charter §3.4 operator-tooling boundary (for any voice-input surface adoption; WhisperLiveKit's *operator-tooling* posture confirms NOT triggered today).
- LE31 charter §3.2 license-compatible (Apache-2.0 permissive; future code adoption is possible).
- Features 23 (`sse-cook-channel`), 25 (`fastapi-frontend-dev-loop`), 142 (`feldroy-air-fastapi-htmx-ai-write-framework`), 143 (`volfpeter-fasthx-htmx-fastapi-declarative-ssr`), 210 (`duckframework-duck-server-side-reactive-web-no-frontend-framework-no-javascript-stack-http2-websocket-reverse-proxy`).
- Cross-section reference `QuentinFuxa/WhisperLiveKit` at https://github.com/QuentinFuxa/WhisperLiveKit (Apache-2.0, 11097★/1140⑂, Python, FastAPI + WebSocket + real-time + streaming + local-ASR + speaker-diarization + translation + OpenAI/Deepgram-compatible-APIs).

## Open questions

- Will LE31 v2 ever introduce a voice-input surface to the cook-Telegram-bot? If yes, WhisperLiveKit is the vocabulary reference.
- Will LE31 v2 ever introduce a WebSocket route to the waiter web UI (replacing or supplementing the SSE cook-channel)? If yes, WhisperLiveKit is the vocabulary reference.
- Will LE31 v2 ever introduce a streaming/real-time route beyond feature 23's SSE cook-channel? If yes, WhisperLiveKit is the vocabulary reference.
- Will LE31 v2 ever introduce an OpenAI/Deepgram-compatible API surface for vendor-agnostic speech-to-text integration? If yes, WhisperLiveKit is the vocabulary reference.
- Will LE31 v2 ever introduce a multi-language voice-input surface (French/German/Italian/English translation)? If yes, WhisperLiveKit is the vocabulary reference.
- Will LE31 v2 ever introduce a speaker-diarization primitive (multi-speaker identification in voice-input)? If yes, WhisperLiveKit is the vocabulary reference.
- The 11097★/1140⑂ is explicitly NOT offered as evidence of *LE31 needing speech-recognition*; the 11097★/1140⑂ is for the *speech-recognition domain*, not for the *FastAPI + WebSocket + real-time + streaming* primitive. The transferable item is the *technique* (FastAPI + WebSocket + real-time + streaming + OpenAI-compatible-API), not the *speech-recognition* itself.

## Why this matters

The 8 primitives in WhisperLiveKit are the **canonical v2 streaming/real-time-architecture vocabulary** that LE31 v1's `sse-cook-channel` (feature 23) and v2's future voice-input surface would inherit. Specifically: (i) **FastAPI + WebSocket + real-time + streaming** (the *streaming-stateful-connection* discipline) is the *bi-directional sibling* of LE31 v1's SSE; (ii) **local-ASR** (the *on-device-automatic-speech-recognition* primitive) is the *no-cloud-required-for-speech-to-text* posture; (iii) **speaker-diarization** is the *multi-speaker-identification* posture; (iv) **translation** is the *automatic-language-translation* posture; (v) **OpenAI/Deepgram-compatible-APIs** is the *drop-in-replacement-API* posture. When v2 introduces any of these 5 primitives, WhisperLiveKit is the vocabulary reference. **HONEST DISCLOSURE**: WhisperLiveKit's 11097★ is for the *speech-recognition domain*, not for the *FastAPI + WebSocket + real-time + streaming* primitive; the 11097★ is explicitly NOT offered as evidence of LE31's need for the speech-recognition primitive.