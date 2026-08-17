# Feature 80 — AI Voice Agent × Restaurant Menu Capability Cross-Section Watch

> **Priority**: P3 (parking-lot) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-17 (Pick C, **parking-lot**) · **Bucket**: new (out-of-scope v1; v2-AI candidate)
> **One-line**: A research-only watch-list artifact that records the **first in-window observation of AI menu-capability queries crossing the modality boundary (text → voice)** in 2026-08, via `csloki-ab/voice-caller` (0★, 212KB Python, 2026-08-17T02:50:39Z, "Outbound voice agent that phones restaurants and works out what a kitchen can make against a strict diet. Twilio, Deepgram, Claude, ElevenLabs, Pipecat, on Railway"). **No code today; parked indefinitely — charter-out-of-scope for v1, no observed owner pain, voice stack is not LE31-importable.**

## Goal

The 2026-08-17 brainstorm scan surfaced the first in-window repo that answers the exact menu-capability question LE31's cook bot answers ("what can the kitchen make against a strict diet?") — but inbound-via-text only in LE31's case, outbound-via-voice in `csloki-ab/voice-caller`'s case. If 2026-08 is the inflection month for AI menu-capability crossing modality, LE31's text-based cook bot may face a UX gap by 2027: a guest calling the restaurant to ask "what can you make for me if I'm vegan + gluten-free?" gets a faster answer from a voice agent than from a Telegram-only cook surface.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2-AI passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 team wants to confirm whether the AI menu-capability inflection point is crossing the text → voice modality boundary in 2026-08, the team wants to know whether independent developers are reaching for voice-driven menu-capability agents, so that the team can decide whether the LE31 strategic posture (text-based cook bot only) is at risk of a UX gap by 2027.

**Why this is a fresh cross-section signal today**: the GitHub `restaurant created:>2026-07-17 language:python` cluster (1319 repos) produced `csloki-ab/voice-caller` (0★ 2026-08-17T02:50:39Z), the first in-window repo that explicitly answers the menu-capability question via voice. The 0★ + first-push combination is not a market-validation signal, but the modality-crossing pattern is the first in 2026-08.

## Scope

**In scope (v2-AI, S effort, ≤1 day, parking-lot — charter-out-of-scope):**
- One source-file edit: this `features/80-voice-agent-menu-capability-watch.md` artifact (the watch-list record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (no new LE31 implementation):**
- A new Twilio voice telephony integration. Charter-out-of-scope for v1.
- A new Deepgram STT pipeline. Not LE31-importable.
- A new ElevenLabs TTS pipeline. Not LE31-importable.
- A new Pipecat voice agent framework. Not LE31-importable.
- A new Claude-as-menu-reasoning layer. Re-evaluate when feature 68 (cook-assistant-deterministic-gate) ships and the LLM-proposes / deterministic-gates-decide pattern is the proven LLM surface in LE31.

## Description

**Evidence precondition:** inferred (1 in-window 0★ repo, no observed pain, no owner survey). Confidence: **low** for the modality-crossing inflection (one repo is an observation, not a trend); **zero** for the LE31-specific pain (no observed pain at the LE31 owner-pain level; LE31 ships text + Telegram only).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: If 2026-08 is the inflection month for AI menu-capability crossing modality, LE31's text-based cook bot may face a UX gap by 2027. Plausible but not yet observed.
2. **Viability**: Twilio + Deepgram + ElevenLabs + Pipecat stack is not LE31-importable. The watch-list is parked until the charter is revised.
3. **Practicability and confidence**: LE31 ships text + Telegram only. Voice is charter-out-of-scope. Low confidence today.
4. **Conflict**: AI-related surface; charter §3.2 allows AI to assist owner/staff with observable evidence and a non-AI fallback. Voice-Twilio is not yet a charter surface.
5. **Outcome, appetite, scope**: v2-AI watch-list. S effort.
6. **Cost to operational value**: Cost is high (Twilio + Deepgram + ElevenLabs + Pipecat + Claude + Railway). Value is low (LE31's text cook bot already answers the question). Net: negative.
7. **Circuit breaker**: Delete this file + the corresponding `INDEX.md` row + the Linear sub-issue. No other code changes to revert.

**Decision: parking-lot (charter-out-of-scope, no observed pain).** Cargo-culted from feature 72's pattern.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline" table with date 2026-08-17, pick `voice-agent-menu-capability-watch`, feature path `features/80-voice-agent-menu-capability-watch.md`, Linear sub-issue ID (TBD), status "Parking-lot (charter-out-of-scope — Twilio + voice not in v1)".
2. **Re-check** on a future daily-research pass. If a future ≥10★ voice-restaurant repo validates the demand, OR if the LE31 owner surveys surface voice pain, OR if the charter is revised to include voice, the watch re-activates (re-evaluate the gate).

## Telegram interaction

None. The slice is a research artifact; no user-facing Telegram surface changes.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- The LE31 charter must be revised to include voice-telephony before the build can be evaluated.
- Feature 68 (cook-assistant-deterministic-gate) must ship to define the LLM-proposes / deterministic-gates-decide pattern that a voice surface would inherit.

No new pip dependencies. No new system dependencies. No new external services.

## Open questions

- **Q1: Will `csloki-ab/voice-caller` reach ≥10★ in the next 30 days?** Currently 0★ after 1 day. Watch-list dormant unless the repo grows past 10★.
- **Q2: Will a future ≥10★ voice-restaurant repo validate the demand?** Yes/no question; the watch-list re-evaluates when such a repo appears.
- **Q3: Will the LE31 owner survey surface voice pain?** No owner survey data today. The watch remains dormant until observed pain.
- **Q4: Will the charter be revised to include voice?** Unknown. The watch is parked until charter revision.

## Why this matters

The 2026-08-17 observation of `csloki-ab/voice-caller` is the **first in-window data point** that AI menu-capability is crossing the modality boundary (text → voice). If 2026-08 is the inflection month, LE31's text-based cook bot may face a UX gap by 2027. The watch-list is parked because the LE31 stack does not yet import voice; if the inflection becomes a trend, the LE31 charter must be revised to include voice.

**Risk of NOT tracking**: if the inflection becomes a trend in 2026-H2 and the watch-list is not in place, LE31 either re-derives the same conclusions (wasted cycles) or misses the inflection (strategic risk).

**Risk of over-tracking**: the inflection is observed at the repo level only (1 repo, 0★); the watch-list is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "parking-lot — charter-out-of-scope, no observed pain." Re-evaluate when (a) a future ≥10★ voice-restaurant repo validates the demand, (b) the LE31 owner surveys surface voice pain, or (c) the charter is revised to include voice.

## Status: parking-lot (charter-out-of-scope)

This file is a **parking-lot artifact (charter-out-of-scope)**. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. No code change today. The research-side subagent (Pass 18, 2026-08-17) records the watch as **parking-lot — Twilio + voice not in v1**.

## Cross-validation anchors

- **`csloki-ab/voice-caller`** (0★, 212KB Python, 2026-08-17T02:50:39Z, "Outbound voice agent that phones restaurants and works out what a kitchen can make against a strict diet. Twilio, Deepgram, Claude, ElevenLabs, Pipecat, on Railway", topics `apps` + `claude` + `elevenlabs` + `pipecat` + `twilio` + `voice-ai`) — the first in-window AI-voice-agent × restaurant-menu-capability cross-section signal.
- **Charter §3.2**: AI may assist owner/staff with observable evidence and a non-AI fallback. Voice telephony is not yet a charter surface.
- **Feature 68 (cook-assistant-deterministic-gate)** — the LLM-proposes / deterministic-gates-decide pattern. A future voice surface would inherit this pattern.
- **No HN / OpenAlex validating peer** — the GitHub `restaurant` cluster is the only in-window signal. No HN thread, no OpenAlex paper, no ProductHunt item validates the AI-voice-agent × restaurant-menu-capability cross-section.
