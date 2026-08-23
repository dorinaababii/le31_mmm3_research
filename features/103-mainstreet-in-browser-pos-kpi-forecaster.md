# Feature 103 — Mainstreet In-Browser POS-Export-to-KPI Forecaster (Watch-list)

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-23 (Pick B, **defer**) · **Bucket**: v2 owner-pains (analytics surface)
> **One-line**: A research-only watch-list artifact that records the in-window `tabassum-begum/mainstreet-metrics` cross-section peer (1★ MIT HTML) — a **zero-backend in-browser POS-export-to-KPI/forecast/action-plan tool**. The pattern informs feature 07 (guest-analytics) v2 iteration: **the owner-analytics surface should be privacy-preserving and infra-free**. **No code today; deferred indefinitely until either (a) the peer crosses ≥5★ and validates the pattern as a market, or (b) ≥2 independent repos converge on the in-browser-only POS-analytics pattern.**

## Goal

The 2026-08-23 brainstorm scan surfaced `tabassum-begum/mainstreet-metrics` (1★, MIT, HTML, pushed 2026-08-19T08:35:05Z, https://github.com/tabassum-begum/mainstreet-metrics) — a single HTML file that "turns any POS export into KPIs, forecasts, dollar-quantified action plan. 100% in-browser." The cross-section insight: **zero-backend, browser-only, no telemetry** is a novel owner-analytics UX pattern that aligns with LE31 charter §3.9 (privacy) and §3.5 (no recurring specialist help).

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2 owner-pains passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 owner wants to see a next-week action plan derived from the POS data, the owner wants to know whether a zero-backend in-browser tool can answer the question, so that LE31 stays privacy-preserving and infra-free.

**Why this is a fresh cross-section signal today**: `tabassum-begum/mainstreet-metrics` is the **first in-window repo to surface the "POS export → in-browser KPI/forecast/action plan" zero-backend pattern**. The prior LE31 owner-analytics surface (feature 07 guest-analytics, feature 39 owner-daily-recap-telegram, feature 57 owner-recap-export, features 74/75 per-recipe-cost + day-part-margin) is all server-side rendered; this peer shows that the browser-only pattern is technically viable. The privacy-preservation alignment with charter §3.9 (privacy) and §3.5 (no recurring specialist help) makes the pattern directionally consistent with LE31's value proposition.

## Scope

**In scope (v2 owner-pains, S effort, ≤1 day, defer — feature 07 v2 iteration input):**
- Daily direct-repo `GET https://api.github.com/repos/tabassum-begum/mainstreet-metrics` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `tabassum-begum/mainstreet-metrics` HTML source + commit history in the next daily-research pass to confirm the in-browser-only architecture (READ ONLY — no import).
- Tracking star velocity + push activity on `tabassum-begum/mainstreet-metrics`.
- Documenting the in-browser-only owner-analytics pattern in the LE31 research notes (this artifact is the document).

**Out of scope (no new LE31 implementation):**
- An `tabassum-begum/mainstreet-metrics` import. The repo is 1★ + single-HTML + unproven.
- A new in-browser owner-analytics surface. Feature 07 v2 iteration is the correct bucket; this artifact is the input to that work.
- Any new feature based on the `mainstreet-metrics` code surface.

## Description

**Evidence precondition:** observed (GitHub `tabassum-begum/mainstreet-metrics` 1★ + MIT + HTML + in-browser-only + 2026-08-19 push + clear description cross-section with LE31 feature 07 v2 iteration). Confidence: **medium** for the architectural pattern (the description is explicit and the repo is single-HTML); **low** for LE31-specific pain (1★ = no observed market validation; no LE31 owner has asked for this).

### `tabassum-begum/mainstreet-metrics`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-23 (this pass) | **1★** | (track) | 2026-08-19T08:35:05Z | MIT | HTML |

**Direct repo URL**: https://github.com/tabassum-begum/mainstreet-metrics

**Verbatim description** (from GitHub API):
> Turn any POS export into KPIs, forecasts, dollar-quantified action plan. 100% in-browser.

**Why this is the cross-section peer of the day:**

1. **The architectural pattern is novel among LE31 peers.** Every other in-window peer in the `restaurant+python` + `topic:small-business` cluster is server-side rendered (FastAPI/MySQL/Docker), an n8n-workflow glue (`Akshay-ALLAM/restaurant-ai-telegram-chat-agent`), or an Electron desktop app (`PplCallMeSk-15/Grocery-Pos-Desktop`). `mainstreet-metrics` is the **only in-window peer that ships zero-backend + browser-only + single-HTML**. The privacy-preservation consequence is unique: the owner can run the tool offline, no infra cost, no telemetry, no auth.
2. **The pattern alignment is direct with LE31 charter.** Charter §3.9 (privacy: store only data needed for restaurant operations) + §3.5 (no recurring specialist help) — the in-browser-only pattern removes the need for a separate analytics service, removes the telemetry surface, and keeps the data on the owner's machine.
3. **The cross-section to feature 07 (guest-analytics) is direct.** Feature 07 is the LE31 v2 owner-pains analytics surface (counting guest demographics, no identity/contact data per charter §3.9). The in-browser pattern from `mainstreet-metrics` would let feature 07 ship as a single-HTML file rather than a server-side dashboard.

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 owner wants to see a next-week action plan derived from the POS data, the owner wants to know whether a zero-backend in-browser tool can answer the question, so that LE31 stays privacy-preserving and infra-free. Plausible but not currently blocking (no owner has asked for this today).
2. **Viability**: No new feature to operate; the pattern informs existing feature 07 v2. No new viability required.
3. **Practicability and confidence**: The peer repo is 1★ + MIT + HTML + in-browser-only; architecture is straightforward (single HTML + JavaScript); high confidence in the pattern (description is explicit). Low confidence in LE31-specific urgency (1★ = no observed market validation).
4. **Conflict**: No invariant conflict. The pattern aligns with charter §3.9 (privacy) and §3.5 (no recurring specialist help).
5. **Outcome, appetite, scope**: v2 owner-pains watch-list. S effort. ≤1 day. **Defer** — feature 07 v2 iteration is the correct bucket; this artifact records the architectural pattern as input.
6. **Cost to operational value**: Zero implementation cost; pure pattern-record artifact. High upside (privacy-preserving owner-analytics) at zero downside.
7. **Circuit breaker and reversibility**: Fully reversible. Watch-list artifact; can be deleted without consequence.

## Data model

**No schema changes.** Watch-list artifact only.

## Implementation steps

**None** — research-only artifact. The slice ships this Markdown file + a one-row `INDEX.md` update + a `*-HANDOFF.md` slice contract for the coding agent (which records the same non-action: "do not implement today; read the mainstreet-metrics HTML on next pass; surface as feature 07 v2 input when ≥5★ validation OR 2+ independent repos converge on the pattern"). The slice hand-off is a no-op directive to the coding agent.

## Telegram interaction if any

**None** — the artifact does not interact with the LE31 Telegram-bot surface. The cross-section is observational only.

## Dependencies

- **No code dependencies** (research-only artifact).
- **External data dependency**: `tabassum-begum/mainstreet-metrics` HTML source + commit history — to be read in the next daily-research pass (carry-over to 2026-08-24).
- **Watch-list add to `le31-daily-research-2026-08-24` pass**: include `tabassum-begum/mainstreet-metrics` in the 5-repo watch list to track star velocity + push activity.
- **Feature 07 (guest-analytics) v2 iteration**: this artifact is the architectural input.

## Open questions

1. **Does `tabassum-begum/mainstreet-metrics` actually work?** The repo is 1★ and the description is plausible but unproven. The next daily-research pass should clone the HTML and verify the KPI/forecast/action-plan pipeline.
2. **What CSV format does it accept?** The description says "POS export" without specifying schema. The cross-section to LE31's POS export (feature 57) requires schema alignment.
3. **What KPI/forecast libraries does it use?** If it uses a server-side forecasting library, the in-browser-only claim is incorrect. The next pass should check the `<script>` tags.
4. **What is the dollar-quantified action-plan algorithm?** Without reading the source, the cross-section to LE31's owner-recap surface (feature 39/57/69) is speculative.

## Why this matters

The 2026-08-23 brainstorm pass surfaces `tabassum-begum/mainstreet-metrics` as the first in-window peer to surface the "POS export → in-browser KPI/forecast/action plan" zero-backend pattern. The pattern informs feature 07 (guest-analytics) v2 iteration: **the owner-analytics surface should be privacy-preserving and infra-free**. Today the LE31 owner-recap surface (feature 39/57/69) is server-side rendered; this artifact records that the in-browser-only pattern is technically viable for future v2 iteration, without changing the v1 roadmap.

**Cross-section with existing LE31 features**:
- Feature 07 (guest-analytics) → v2 iteration input.
- Features 21 (stockout-prep-board-snapshot) + 39 (owner-daily-recap-telegram) + 57 (owner-recap-export) + 74/75 (per-recipe-cost + day-part-margin) → all server-side today; this artifact is the architectural pattern for the browser-only variant.

**Why defer, not build**: 1★ = no observed market validation; no LE31 owner has asked for this; feature 07 v2 iteration is the correct bucket for the pattern, not a separate feature. The artifact is a research-note that records the pattern for future v2 owner-pains iteration.
