# Feature 342 — `johnohhh1-restaurant-sales-forecast-mit-zero-shot-daily-restaurant-sales-forecasting-with-timesfm-2-5-p10-p50-p90-bands-and-4-week-period-rollups-v1-foundation-model-restaurant-sales-forecasting-vocabulary` (defer)

> **NEW observation (2026-10-18).** Documents in-window GitHub repo `johnohhh1/restaurant-sales-forecast` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **Python ✓ ON-STACK** + TimesFM 2.5 + forecasting + restaurant + sales + time-series, **pushed 2026-10-15T16:08:27Z AND created 2026-10-15T16:08:20Z = IN-WINDOW BY BOTH FIELDS** (3-day-old repo; both fields in window, ~7-second gap between `created_at` and `pushed_at` = same-instant push), **10 KB tiny = 2nd-smallest in-window brainstorm-vocabulary pick of the 80-pass series** (vs 2026-10-17 Pick B at 5 KB = 2x larger than today's; the smallest in-window brainstorm-vocabulary pick of the 80-pass series is still 2026-10-17 Pick B), default_branch=`main`, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-18): *"Zero-shot daily restaurant sales forecasting with TimesFM 2.5: P10/P50/P90 bands and 4-week period rollups"*. Topics (verbatim, parent-verified, **6 topics**): `forecasting, python, restaurant, sales, time-series, timesfm`. Bucket: **v1 (foundation-model-restaurant-sales-forecasting-vocabulary)** — Pick B of Daily Brainstorm 2026-10-18. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **zero-shot-daily-restaurant-sales-forecasting + TimesFM-2.5 + P10/P50/P90-bands + 4-week-period-rollups + restaurant + sales + time-series + forecasting + python** 9-tuple-primitive as a persistent cross-section reference for the LE31 v1 *foundation-model-restaurant-sales-forecasting* wedge, and document the **zero-shot-daily-restaurant-sales-forecasting + TimesFM-2.5 + P10/P50/P90-bands + 4-week-period-rollups** primitive that an independent maintainer shipped in 2026 (3-day-old repo; same-instant push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 *demand-estimation* gap-area. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **zero-shot-daily-restaurant-sales-forecasting + TimesFM-2.5 + P10/P50/P90-bands + 4-week-period-rollups + restaurant + sales + time-series + forecasting + python** 9-tuple-primitive: a foundation-model-based zero-shot daily restaurant sales forecaster that produces P10/P50/P90 uncertainty bands and 4-week period rollups; the forecaster uses TimesFM 2.5 (Google's time-series foundation model); no training data is required; the model is zero-shot. This is the §3.1 *explicit-state-transitions* + §3.7 *forecast-uncertainty-bands* invariant applied to the *foundation-model-restaurant-sales-forecasting* dimension.
- A written record of the **MIT + 0★/0⑨ + 10 KB tiny + 6-topic array + Python ✓ ON-STACK + TimesFM-2.5 + restaurant + sales + time-series** stack-shape: this is the **first zero-shot-foundation-model-restaurant-sales-forecasting-vocabulary of the 80-pass brainstorm series**; the *TimesFM-2.5 + zero-shot + P10/P50/P90-bands + 4-week-period-rollups* discipline IS the canonical §3.4 *no-AI-by-default + non-AI-fallback + observable-evidence* + §3.7 *forecast-uncertainty-bands* invariant applied to the *foundation-model-restaurant-sales-forecasting* dimension.
- A written record of the **operator-facing vocabulary** discipline: the operator does not interact with the model directly; the operator consumes the P10/P50/P90 bands and the 4-week-period rollups via the owner-daily-recap surface; the P10 band is the worst-case scenario; the P50 band is the median scenario; the P90 band is the best-case scenario; the 4-week-period rollups show the week-over-week + month-over-month trends. Sister-shape to today's research PICK C `donaldrichard19-LVD/pattern-mcp` (TypeScript pattern-mining-for-restaurant) + features 07 (`demand-estimation`) + 39 (`owner-daily-recap-telegram`) + 314 (`Samarty-1/payout-recon`) + 315 (`Samarty-1/fairshift` for sick-call-replanning) — the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* posture IS the canonical v1 *foundation-model-restaurant-sales-forecasting-vocabulary* applied to the *LE31-v1-demand-estimation* dimension.
- A decision record: today's verdict is `defer` because (1) the v1 charter has *no foundation-model-restaurant-sales-forecasting surface* (LE31 v1 has feature 07 `demand-estimation` but it is feature-class-b as a v1 polish gap-area, not a foundation-model-forecaster); (2) the stack-shape match is the value, not the code (LE31 v1 uses Python + FastAPI + Postgres + aiogram v3 + minimal-HTML/HTMX, not TimesFM 2.5 + zero-shot-forecaster); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the restaurant-sales-forecast codebase (MIT + 0★/0⑨ + 3-day-old repo; same-instant push).
- Cross-pollination with the v1 charter §3.4 *no-AI-by-default + non-AI-fallback + observable-evidence* posture (the *zero-shot-foundation-model-forecaster + P10/P50/P90-bands + 4-week-period-rollups* discipline IS the §3.4 invariant; the *foundation-model-as-forecaster* posture IS OFF-§3.4 — a foundation model is *not* an LLM intent-parser, but a time-series-forecaster; explicit charter-decision needed for any v1 PR that adopts this discipline).
- Any vendor-relationship with Google / TimesFM (LE31 v1 has no foundation-model-forecaster integration today; v1 uses Python + FastAPI + Postgres + aiogram v3 + minimal-HTML/HTMX, not TimesFM 2.5).
- Cross-section candidate for v1 if LE31 ever adds a foundation-model-forecaster surface (charter §3.4 review required: the *foundation-model-as-forecaster + P10/P50/P90-bands* posture requires explicit non-AI-fallback and explicit forecast-uncertainty-bands-scope before any v1 PR).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "a zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups primitive" (e.g., a v1 surface that adds a foundation-model-based demand-estimator to the existing feature 07 `demand-estimation`; the foundation-model-forecaster produces P10/P50/P90 uncertainty bands and 4-week-period rollups; the owner-daily-recap surface consumes the P50 band as the expected-demand-scenario and the P10/P90 bands as the worst-/best-case-scenarios), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups posture"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `forecasting, python, restaurant, sales, time-series, timesfm` + *"Zero-shot daily restaurant sales forecasting with TimesFM 2.5: P10/P50/P90 bands and 4-week period rollups"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + topics name the 9-tuple-primitive set + the zero-shot-foundation-model-forecaster posture + the P10/P50/P90-bands posture + the 4-week-period-rollups posture); low for transferability (LE31 v1 has feature 07 `demand-estimation` but it is feature-class-b as a v1 polish gap-area; a foundation-model-forecaster is OFF-§3.4 unless explicit charter-decision is made).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has feature 07 `demand-estimation` as a v1 polish gap-area, but no foundation-model-forecaster surface); the value is the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* vocabulary — when the first v1 PR that adopts a foundation-model-forecaster surface lands, the restaurant-sales-forecast pattern is a ready-made *named primitive*.

## Description

GitHub `johnohhh1/restaurant-sales-forecast` (MIT, 0★/0⑨, Python, pushed 2026-10-15T16:08:27Z, created 2026-10-15T16:08:20Z, 10 KB tiny, default_branch=`main`, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-18): *"Zero-shot daily restaurant sales forecasting with TimesFM 2.5: P10/P50/P90 bands and 4-week period rollups"*.

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Zero-shot-daily-restaurant-sales-forecasting** — the operator picks a target restaurant; the foundation-model-forecaster produces a P10/P50/P90-band forecast for the next N days without any training data; the forecaster is zero-shot. The *zero-shot-foundation-model-forecaster* primitive maps 1:1 onto any future v1 surface that needs a foundation-model-based demand-estimator for the LE31 feature 07 `demand-estimation`.
2. **TimesFM-2.5** — Google's time-series foundation model. The *TimesFM-2.5* posture IS the §3.4 *foundation-model-as-forecaster* posture (a foundation model is *not* an LLM intent-parser, but a time-series-forecaster; charter-decision needed for a v1 PR that adopts this discipline).
3. **P10/P50/P90-bands** — the uncertainty bands (P10 = 10th percentile = worst-case scenario; P50 = 50th percentile = median scenario; P90 = 90th percentile = best-case scenario). The *P10/P50/P90-bands* posture IS the §3.7 *forecast-uncertainty-bands* charter invariant applied to the *demand-estimation-uncertainty* dimension.
4. **4-week-period-rollups** — the weekly + monthly rollups (week-over-week + month-over-month trends). The *4-week-period-rollups* posture IS the §3.7 *forecast-period-rollups* charter invariant applied to the *demand-estimation-period* dimension.
5. **Restaurant + sales + time-series** — the domain + the metric + the time-series. The *restaurant + sales + time-series* posture IS the §3.1 *explicit-state-transitions* charter invariant applied to the *restaurant-sales-forecasting* dimension.
6. **Forecasting + python** — the technique + the language. The *forecasting + python* posture IS the §3.1 *Python-as-forecasting-language* charter invariant applied to the *foundation-model-forecaster* dimension.

The defer artifact retains the **9-tuple-primitive** (zero-shot-daily-restaurant-sales-forecasting + TimesFM-2.5 + P10/P50/P90-bands + 4-week-period-rollups + restaurant + sales + time-series + forecasting + python) as a persistent cross-section reference.

## Data model

None today. The defer artifact is documentation only.

When the first v1 PR that adopts the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* discipline lands, the data model is:

```sql
-- hypothetical future v1 surface (NOT IMPLEMENTED TODAY)
CREATE TABLE forecast_run (
    id SERIAL PRIMARY KEY,
    run_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    forecast_horizon_days INT NOT NULL,
    model TEXT NOT NULL,                   -- 'timesfm-2.5' | 'chronos-bolt' | 'moirai-2.0' | ...
    target_date DATE NOT NULL,
    p10_sales_eur NUMERIC(10, 2) NOT NULL,
    p50_sales_eur NUMERIC(10, 2) NOT NULL,
    p90_sales_eur NUMERIC(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE forecast_period_rollup (
    id SERIAL PRIMARY KEY,
    forecast_run_id INT NOT NULL REFERENCES forecast_run(id),
    period_type TEXT NOT NULL,             -- 'week' | 'month' | '4-week'
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    p10_total_sales_eur NUMERIC(10, 2) NOT NULL,
    p50_total_sales_eur NUMERIC(10, 2) NOT NULL,
    p90_total_sales_eur NUMERIC(10, 2) NOT NULL,
    wow_change_pct NUMERIC(5, 2),          -- week-over-week change (period_type='week' only)
    mom_change_pct NUMERIC(5, 2),          -- month-over-month change (period_type='month' only)
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- append-only forecast event log (the §3.3 append-only-ledger invariant)
CREATE TABLE forecast_event (
    id BIGSERIAL PRIMARY KEY,
    forecast_run_id INT NOT NULL REFERENCES forecast_run(id),
    event_type TEXT NOT NULL,             -- 'forecast_requested' | 'forecast_completed' | 'forecast_failed' | 'forecast_consumed' | ...
    payload JSON NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Implementation steps

None today. The defer artifact is documentation only.

When the first v1 PR that adopts the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* discipline lands, the implementation steps are:

1. Add Alembic migration for `ForecastRun`, `ForecastPeriodRollup`, `ForecastEvent` tables.
2. Add `backend/services/forecast_runner.py` with `ForecastRunner` class (wraps TimesFM 2.5; produces P10/P50/P90 bands; supports 4-week-period rollups).
3. Add `backend/services/forecast_period_rollup.py` with `ForecastPeriodRollup` class (weekly + monthly + 4-week rollups; wow + mom change percentages).
4. Wire the new service into the existing feature 07 `demand-estimation` surface.
5. Add `frontend/templates/forecast-dashboard.html` minimal-HTML/HTMX template for the P10/P50/P90 dashboard.
6. Add `cron/forecast_overnight.py` for the overnight zero-shot-forecast run.
7. Add `tests/test_forecast_runner.py` + `tests/test_forecast_period_rollup.py`.

## Telegram interaction if any

The owner Telegram bot's daily-recap surface consumes the P50 band as the expected-demand-scenario and the P10/P90 bands as the worst-/best-case-scenarios. The P50 band is shown as *"Today's expected sales: €X (P50)"* + *"Worst case (P10): €X" + *"Best case (P90): €X"*. The 4-week-period-rollups are shown in the weekly-owner-recap as *"This week vs last week: +X% (P50)"*. No new Telegram-bot surface today.

## Dependencies

When the first v1 PR that adopts the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* discipline lands, the dependencies are:

- `timesfm` (Google's time-series foundation model; torch-based; charter-decision needed for v1)
- `pandas` + `numpy` (data manipulation; already in the LE31 v1 stack)
- Existing LE31 v1 stack: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX

## Open questions

- **§3.4 foundation-model-as-forecaster review**: a foundation model is *not* an LLM intent-parser, but a time-series-forecaster. The charter §3.4 *no-AI-by-default* review is required before any v1 PR that adopts this discipline lands.
- **§3.7 forecast-uncertainty-bands review**: the *P10/P50/P90-bands* posture is the §3.7 invariant; explicit charter-decision needed for a v1 PR that adopts this discipline.
- **TimesFM 2.5 vs alternatives**: today's pick is TimesFM-2.5-specific. The transferable discipline is the *zero-shot-foundation-model-forecaster + P10/P50/P90-bands + 4-week-period-rollups* posture, not the TimesFM 2.5 API surface. The first v1 PR must decide whether to abstract over multiple foundation models (TimesFM 2.5 + Chronos-Bolt + Moirai 2.0 + ...) or to start with a single foundation model (TimesFM 2.5).
- **Zero-shot vs fine-tuned**: today's pick is zero-shot-specific. The transferable discipline is the *foundation-model-forecaster + P10/P50/P90-bands + 4-week-period-rollups* posture, not the zero-shot discipline. The first v1 PR must decide whether to ship zero-shot (no training data) or fine-tuned (training data required; charter §3.4 review).

## Why this matters

The *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* primitive is the **canonical v1 foundation-model-restaurant-sales-forecasting-vocabulary of the 80-pass brainstorm series**. The verbatim description + topics name the 9-tuple-primitive set explicitly. The vocabulary is the value, not the code (LE31 v1 has feature 07 `demand-estimation` as a v1 polish gap-area but no foundation-model-forecaster surface). When the first v1 PR that adopts a foundation-model-forecaster surface lands, the restaurant-sales-forecast pattern is a ready-made *named primitive*. Sister-shape to features 07 (`demand-estimation`) + 39 (`owner-daily-recap-telegram`) + 314 (`Samarty-1/payout-recon`) + 315 (`Samarty-1/fairshift` for sick-call-replanning).

The transferable items are:

1. The *zero-shot-foundation-model-restaurant-sales-forecasting* primitive (the §3.4 *foundation-model-as-forecaster* posture; charter-decision needed for v1).
2. The *TimesFM-2.5* posture (Google's time-series foundation model; OFF-§3.4 unless explicit charter-decision is made).
3. The *P10/P50/P90-bands* posture (the §3.7 *forecast-uncertainty-bands* invariant applied to demand-estimation-uncertainty).
4. The *4-week-period-rollups* posture (the §3.7 *forecast-period-rollups* invariant applied to demand-estimation-period).
5. The *restaurant + sales + time-series* posture (the §3.1 *explicit-state-transitions* invariant applied to restaurant-sales-forecasting).
6. The *forecasting + python* posture (the §3.1 *Python-as-forecasting-language* invariant applied to foundation-model-forecaster).

The defer artifact is **fully reversible** (vocabulary-only). No code today.