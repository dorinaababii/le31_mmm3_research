# Feature 113 — restaurant-voice-ai deterministic-state-machine voice-ordering

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-25 (Pick B, **defer**) · **Bucket**: v2 owner-pains (parking-lot, future-voice-cook-bot-architecture)
> **One-line**: A research-only watch-list artifact that records the in-window `arushahmd/restaurant-voice-ai` cross-section peer (1★ MIT Python, pushed 2026-08-19) — **a direct FastAPI-stack LE31 cross-section with "deterministic state-machine orchestration" phrasing that mirrors LE31 charter §3.1** — as a future reference for LE31 v2 cook-bot/voice extensions (features 41 + 65 v2 extension). **No code today; deferred indefinitely until either (a) LE31 v2 explicitly opens the voice-input cook-bot question (charter §3.5 AI non-customer-facing rule applies — voice-input must be gated on deterministic state transitions, not free-form LLM calls), or (b) the `restaurant-voice-ai` peer gains a community-traction signal (>=50★ or >=3 independent FastAPI+state-machine voice peers with similar positioning).**

## Goal

The 2026-08-25 brainstorm scan surfaced `arushahmd/restaurant-voice-ai` (1★ MIT Python, pushed 2026-08-19T17:09:21Z, https://github.com/arushahmd/restaurant-voice-ai). Description verbatim: *"Real-time AI voice ordering system using FastAPI, Twilio Media Streams, Deepgram STT/TTS, Redis, custom NLU, and deterministic state-machine orchestration."*

The cross-section insight: **LE31's voice-input cook-bot extensions have a direct FastAPI-stack reference peer with deterministic state-machine orchestration phrasing that mirrors charter §3.1 deterministic-gate language**. Twilio + Deepgram + Redis components are individually familiar from feature 13 (Twilio SMS) and feature 38 (Deepgram alternative for voice notes); the *deterministic state-machine orchestration* + voice-ordering is the fresh signal — a voice-ordering surface that gates on deterministic state transitions, applicable to LE31 v2 cook-bot/voice extensions.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 v2 team considers adding a voice-input mode to the cook-bot surface (features 41 + 65 v2 extension), the team wants to know whether a working FastAPI-stack peer documents the deterministic-state-machine voice-ordering architecture, so that the voice-input design is informed by a working peer and not invented from scratch.

**Why this is a fresh cross-section signal today**: `arushahmd/restaurant-voice-ai` is the **only in-window FastAPI-stack voice-ordering peer that explicitly names "deterministic state-machine orchestration."** The other in-window voice/cook-bot peers are:
- `justinmichaelvieira/ezdmb` 25★ LGPL-3.0 Python — display menu board, not voice-ordering (covered by feature 91).
- `Eigensu/RestoBuzz` 1★ MIT Python — WhatsApp bulk-messaging + restaurant CRM, not voice-ordering (mention-only).
- `nematjon555/telegram-restaurant-delivery-bot` 0★ Python — Telegram restaurant delivery bot, not voice-ordering (covered by feature 110).

None of the above ship a FastAPI + voice-ordering + deterministic-state-machine architecture. `restaurant-voice-ai` is the unique pattern-record candidate.

## Scope

**In scope (v2 owner-pains, S effort, ≤1 day, defer — LE31 v1 doesn't ship a voice-input cook-bot surface):**
- Daily direct-repo `GET https://api.github.com/repos/arushahmd/restaurant-voice-ai` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `restaurant-voice-ai` README + architecture documentation in the next daily-research pass to confirm the deterministic-state-machine voice-ordering architecture (READ ONLY — no import).
- Tracking star velocity + push activity on `restaurant-voice-ai`.
- Documenting the deterministic-state-machine voice-ordering architecture pattern in the LE31 research notes (this artifact is the document).

**Out of scope (no new LE31 implementation):**
- A new voice-ordering surface. LE31 v1 doesn't ship one; the v2 extension is a future-tense concern.
- A `restaurant-voice-ai` import. MIT permissive license means code-borrow is permitted, but no borrow is needed today; the architectural pattern is informational only.
- A Twilio / Deepgram / Redis dependency. Adding these would expand LE31's dependency surface; the artifact is informational only.
- Any new feature based on the `restaurant-voice-ai` code surface.
- Any schema changes; any new dependencies; any source-file edits outside this artifact.

## Description

**Evidence precondition:** observed (GitHub `arushahmd/restaurant-voice-ai` 1★ + MIT + Python + FastAPI + Twilio + Deepgram + Redis + deterministic state-machine orchestration + in-window push on 2026-08-19). Confidence: **high** for the cross-section pattern (the FastAPI + deterministic-state-machine voice-ordering architecture is documented in the repo description); **low** for LE31-specific urgency (LE31 v1 doesn't ship a voice-input cook-bot surface; the v2 extension is a future-tense concern; charter §3.5 AI non-customer-facing rule applies — voice-input must be gated on deterministic state transitions, not free-form LLM calls).

### `arushahmd/restaurant-voice-ai`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-25 (this pass) | **1★** | 0 | 2026-08-19T17:09:21Z | MIT | Python |

**Direct repo URL**: https://github.com/arushahmd/restaurant-voice-ai

**Verbatim description** (from GitHub API):
> Real-time AI voice ordering system using FastAPI, Twilio Media Streams, Deepgram STT/TTS, Redis, custom NLU, and deterministic state-machine orchestration.

**Why this is the cross-section peer of the day:**

1. **Direct FastAPI-stack LE31 cross-section.** LE31 v1 uses FastAPI as the HTTP API layer. The peer's FastAPI + Twilio Media Streams + Deepgram STT/TTS + Redis + custom NLU + deterministic state-machine orchestration stack is a direct reference for any future LE31 v2 voice-input cook-bot extension.
2. **Deterministic state-machine orchestration phrasing mirrors charter §3.1.** The peer's "deterministic state-machine orchestration" phrasing directly mirrors LE31 charter §3.1 (operational transitions are explicit user actions; do not silently send, serve, close, or reconcile an order). When LE31 v2 considers adding voice-input to the cook-bot surface, the deterministic-state-machine gating ensures voice-input follows charter §3.1 explicit-action rules (the cook must explicitly accept the voice-input before any `StockEntry` write).
3. **Twilio + Deepgram + Redis components are individually familiar from feature 13 + 38.** The peer's component stack is well-known in the LE31 v2 extension context; the fresh signal is the **deterministic-state-machine orchestration** + voice-ordering integration, not the components themselves.
4. **MIT permissive license.** No contagion if any spec or pattern is borrowed; the pattern is reusable without license concerns.

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 v2 team considers adding voice-input to the cook-bot surface, the team wants to know whether a FastAPI-stack peer documents the deterministic-state-machine voice-ordering architecture, so that the voice-input design is informed by a peer. Plausible but not currently blocking.
2. **Viability**: No new feature to operate; the pattern informs a future v2 surface decision. No new viability required. **Note**: charter §3.5 (AI non-customer-facing) applies — voice-input must be gated on deterministic state transitions, not free-form LLM calls.
3. **Practicability and confidence**: The peer repo is 1★ + MIT + Python + FastAPI + Twilio + Deepgram + Redis + deterministic state-machine orchestration; high confidence in the pattern (the architecture is documented in the repo description). Low confidence in LE31-specific urgency (no owner signal of "I want voice-input for the cook-bot" today).
4. **Conflict**: No invariant conflict. The pattern is informational and does not change LE31 v1 behavior. **Note**: charter §3.5 (AI non-customer-facing) is preserved by the deterministic-state-machine gating pattern.
5. **Outcome, appetite, scope**: v2 owner-pains parking-lot. S effort. ≤1 day. **Defer** — LE31 v1 doesn't ship a voice-input cook-bot surface; this artifact records the deterministic-state-machine voice-ordering architecture for future v2 iteration.
6. **Cost to operational value**: Zero implementation cost; pure pattern-record artifact. High upside (voice-input cook-bot surface for v2) at zero downside.
7. **Circuit breaker and reversibility**: Fully reversible. Watch-list artifact; can be deleted without consequence.

## Data model

**No schema changes.** Watch-list artifact only.

## Implementation steps

**None** — research-only artifact. The slice ships this Markdown file + a one-row `INDEX.md` update + a `*-HANDOFF.md` slice contract for the coding agent (which records the same non-action: "do not implement today; read `restaurant-voice-ai` README on next pass"). The slice hand-off is a no-op directive to the coding agent.

## Telegram interaction if any

**None today.** The artifact does not interact with the LE31 Telegram-bot surface. The cross-section is observational only. **If/when the slice is un-deferred** (v2 owner-pains extension), the voice-input cook-bot surface would be a **voice-input mode for the existing cook-bot** (features 41 + 65 v2 extension) gated on deterministic-state-machine transitions, not free-form LLM calls — preserving charter §3.1 + §3.5.

## Dependencies

- **No code dependencies** (research-only artifact).
- **External data dependency**: `arushahmd/restaurant-voice-ai` README + architecture documentation — to be read in the next daily-research pass (carry-over to 2026-08-26).
- **Watch-list add to `le31-daily-research-2026-08-26` pass**: include `arushahmd/restaurant-voice-ai` in the 5-repo watch list to track star velocity + push activity.

## Open questions

1. **What is the exact deterministic-state-machine pattern in `restaurant-voice-ai`?** Is it an explicit state-machine library (e.g., `transitions`, `python-statemachine`) or an implicit state-transition table? The answer determines how transferable the pattern is to LE31 v2.
2. **Is the 1★ count maintained over the next 7 days?** Velocity will inform whether the pattern is gaining traction or is a niche positioning.
3. **Does `restaurant-voice-ai` use custom NLU or an LLM?** The answer informs whether the pattern is compatible with charter §3.5 (AI non-customer-facing) — if the NLU is an LLM call, the pattern would need to be re-gated to ensure no customer-facing AI exposure.
4. **Does the LE31 owner actually want voice-input cook-bot?** This is a charter-level question that the artifact defers. The current charter (PROJECT_CHARTER.md §3) does not mention voice-input; features 41 + 65 v2 extension would need explicit charter approval.

## Why this matters

The 2026-08-25 brainstorm pass surfaces `arushahmd/restaurant-voice-ai` as the **only in-window FastAPI-stack voice-ordering peer that explicitly names "deterministic state-machine orchestration."** The cross-section insight: **LE31's cook-bot voice-input extension (features 41 + 65 v2) has a direct FastAPI-stack reference peer with deterministic-state-machine gating that preserves charter §3.1 + §3.5.** MIT permissive license means any spec or pattern is reusable without license concerns for future v2 owner-pains extension.

**Cross-section with existing LE31 features**:
- Features 41 (telegram-msg-stock-update) + 65 (cook-photo-stock-list-pwa) + 38 (cook-voice-note-to-stockentry) → these are the cook-bot message-input surfaces; this artifact strengthens the voice-input layer with a deterministic-state-machine reference.
- Features 13 (Twilio SMS) + 38 (Deepgram alternative) → these are the component-level references; the fresh signal is the deterministic-state-machine gating pattern.
- Features 67 (solo-operator-shift-journal-pwa) + 68 (cook-assistant-deterministic-gate) + 90 (pronto-cafe-telegram-reminders-cross-section) → these are the deterministic-gate + solo-operator cook-bot cross-section siblings; this artifact (feature 113) is the FastAPI-stack voice-ordering sibling.

**Why defer, not build**: zero observed pain at the LE31-owner level (no signal that the owner wants voice-input for the cook-bot today); LE31 v1 doesn't ship one; the v2 extension is a future-tense concern; charter §3.5 AI non-customer-facing rule applies — voice-input must be gated on deterministic state transitions, not free-form LLM calls. The artifact is a research-note that records the deterministic-state-machine voice-ordering architecture for future v2 iteration.