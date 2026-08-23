# Slice Handoff — `mainstreet-in-browser-pos-kpi-forecaster`

> **Pick**: 103-mainstreet-in-browser-pos-kpi-forecaster (defer, watch-list)
> **Source brainstorm**: 2026-08-23 (Pick B)
> **Generated**: 2026-08-23 by daily-brainstorm cron

## Active feature path

- `features/103-mainstreet-in-browser-pos-kpi-forecaster.md`
- This `specs/mainstreet-in-browser-pos-kpi-forecaster-HANDOFF.md`

## Seven-check gate verdict

**Decision: defer, watch-list (≥5★ OR 2+ independent repos threshold).** The cross-section informs feature 07 (guest-analytics) v2 iteration without changing the v1 roadmap. No code today.

**Gate summary**:
1. **JTBD**: When the LE31 owner wants to see a next-week action plan derived from the POS data, knowing that a zero-backend in-browser tool can answer the question informs feature 07 v2 architectural choice. Defer (no owner has asked for this today).
2. **Viability**: n/a (no new feature to operate). The pattern informs existing feature 07 v2 iteration.
3. **Practicability + confidence**: medium (peer repo 1★ + MIT + HTML + in-browser-only; architecture straightforward). Low confidence in LE31-specific urgency (1★ = no observed market validation).
4. **Conflict**: none. Pattern aligns with charter §3.9 (privacy) and §3.5 (no recurring specialist help).
5. **Outcome, appetite, scope**: v2 owner-pains watch-list. S effort. ≤1 day. Defer.
6. **Cost to operational value**: zero implementation cost; pure pattern-record artifact.
7. **Circuit breaker + reversibility**: fully reversible. Watch-list artifact; can be deleted without consequence.

## Files to touch

**ZERO files in LE31 source tree.** This is a research-only artifact.

If the slice is ever un-deferred (i.e., when the peer crosses ≥5★ OR 2+ independent repos converge on the in-browser-only POS-analytics pattern), the slice will become an **input to feature 07 v2 iteration**, which will touch:
- `backend/app/analytics/export.py` (modify) — emit a `stock.csv` + `orders.csv` + `prices.csv` bundle.
- `frontend/static/analytics.html` (new file) — single HTML file with in-browser KPI/forecast/action-plan logic.
- `specs/feature-07-guest-analytics-v2.md` (new file) — v2 iteration spec.

These files do **not exist today** and **will not be created by this slice**.

## Verification protocol reference

- **Today**: verify that this `HANDOFF.md` exists + `features/103-mainstreet-in-browser-pos-kpi-forecaster.md` exists + the `INDEX.md` row was added + the `le31_daily_brainstorm_2026_08_23` Linear issue (HMM-133) was created with the parent body.
- **Daily (next 7 days)**: track `tabassum-begum/mainstreet-metrics` star velocity via `GET https://api.github.com/repos/tabassum-begum/mainstreet-metrics` (via `$HERMES_GITHUB_TOKEN`).
- **Re-check threshold**: if stars ≥5 OR ≥2 independent repos in the same `topic:small-business` cluster ship with the same in-browser-only POS-analytics pattern, the slice is un-deferred and the pattern becomes feature 07 v2 iteration input.

## Rollback path

**Fully reversible.** Delete `features/103-mainstreet-in-browser-pos-kpi-forecaster.md` + this `HANDOFF.md` + the `INDEX.md` row + the `le31_daily_brainstorm_2026_08_23` sub-issue + the `le31_v1_core_mvp` Linear sub-issue. Zero risk of code regression (no code changed).

## Mandatory LE31 skill list

Before resuming this slice, load:
- `le31-conventions` — verify no charter violation (especially §3.9 privacy + §3.5 no recurring specialist help).
- `le31-feature-pipeline` — verify the contract is up-to-date.
- `le31-v1-feature-pattern` — confirm the v1 contract template format.
- `le31-coding-agent-brief` — generate the paste-in prompt only if the slice is un-deferred.

If any skill is updated during the lifetime of this slice, patch it via `skill_manage(action='patch')` and re-verify before proceeding.
