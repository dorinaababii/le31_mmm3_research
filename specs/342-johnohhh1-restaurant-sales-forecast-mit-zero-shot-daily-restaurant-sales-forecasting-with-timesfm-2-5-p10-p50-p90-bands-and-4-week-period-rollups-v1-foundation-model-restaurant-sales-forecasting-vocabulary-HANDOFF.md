# HANDOFF — Feature 342: `johnohhh1-restaurant-sales-forecast-mit-zero-shot-daily-restaurant-sales-forecasting-with-timesfm-2-5-p10-p50-p90-bands-and-4-week-period-rollups-v1-foundation-model-restaurant-sales-forecasting-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/342-johnohhh1-restaurant-sales-forecast-mit-zero-shot-daily-restaurant-sales-forecasting-with-timesfm-2-5-p10-p50-p90-bands-and-4-week-period-rollups-v1-foundation-model-restaurant-sales-forecasting-vocabulary.md` — defer/parking-lot (Pick B of Daily Brainstorm 2026-10-18).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups primitive*, the owner wants *evidence that this foundation-model-restaurant-sales-forecasting-vocabulary exists in 2026 with the same zero-shot + P10/P50/P90-bands + 4-week-period-rollups posture*, but struggles because *LE31 has no documented v1 foundation-model-restaurant-sales-forecasting-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups) without specialist help. The 0★/0⑨ with maintainer activity (created 2026-10-15 + pushed 2026-10-15 = IN-WINDOW BY BOTH FIELDS, ~3-day-old repo; same-instant push) makes vocabulary viable, but code adoption is not viable (the TimesFM-2.5 + zero-shot-forecaster stack is off-§3.4 unless explicit charter-decision is made; LE31 v1 has no foundation-model-forecaster surface). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + TimesFM-2.5 OFF-§3.4 (foundation-model-forecaster charter-decision needed for v1) + forecasting ✓ ON-PATTERN + restaurant ✓ ON-STACK + sales ✓ ON-STACK + time-series ✓ ON-PATTERN. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX + timesfm (Google's time-series foundation model). Rabbit hole: the *TimesFM-2.5 + zero-shot + P10/P50/P90-bands + 4-week-period-rollups* stack is off-§3.4 unless explicit charter-decision is made. Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* primitives are §3.7-aligned (forecast-uncertainty-bands + forecast-period-rollups). The *P10/P50/P90-bands + 4-week-period-rollups* posture IS the §3.7 *forecast-uncertainty-bands + forecast-period-rollups* charter invariant. No §3.4 customer-facing AI (a foundation model is a time-series-forecaster, not an LLM intent-parser; charter-decision needed for v1). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (foundation-model-based demand-estimator for the LE31 feature 07 `demand-estimation`). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (feature 07 `demand-estimation` + feature 39 `owner-daily-recap-telegram`) may adopt the *foundation-model-forecaster + P10/P50/P90-bands* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (TimesFM-2.5 + zero-shot-forecaster stack off-§3.4 unless explicit charter-decision is made + no v1 foundation-model-forecaster surface in v1 charter).

## Bucket

**v1** (foundation-model-restaurant-sales-forecasting-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 9-tuple-primitive set (zero-shot-daily-restaurant-sales-forecasting + TimesFM-2.5 + P10/P50/P90-bands + 4-week-period-rollups + restaurant + sales + time-series + forecasting + python) + the tech-stack (Python + TimesFM-2.5 + forecasting + restaurant + sales + time-series).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `ForecastRun`, `ForecastPeriodRollup`, `ForecastEvent` tables.
- `backend/services/forecast_runner.py` — new file with `ForecastRunner` class (wraps TimesFM 2.5; produces P10/P50/P90 bands; supports 4-week-period rollups).
- `backend/services/forecast_period_rollup.py` — new file with `ForecastPeriodRollup` class (weekly + monthly + 4-week rollups; wow + mom change percentages).
- `backend/main.py` — wire the new service into the existing feature 07 `demand-estimation` surface.
- `frontend/templates/forecast-dashboard.html` — new minimal-HTML/HTMX template for the P10/P50/P90 dashboard.
- `cron/forecast_overnight.py` — new cron entry for the overnight zero-shot-forecast run.
- `tests/test_forecast_runner.py` — new unit test for `ForecastRunner`.
- `tests/test_forecast_period_rollup.py` — new unit test for `ForecastPeriodRollup`.

## Verification protocol reference

When the first v1 PR that adopts the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* discipline lands, the verification protocol is:

1. Run `pytest tests/test_forecast_runner.py` and verify the `ForecastRunner` produces valid P10/P50/P90 bands for the existing LE31 daily sales.
2. Run `pytest tests/test_forecast_period_rollup.py` and verify the `ForecastPeriodRollup` produces valid weekly + monthly + 4-week rollups with wow + mom change percentages.
3. Run `uvicorn backend.main:app` and curl the forecast endpoint to verify the P50 band matches the median scenario.
4. Open `frontend/templates/forecast-dashboard.html` in a browser and verify the P10/P50/P90 dashboard renders correctly.
5. Run the `cron/forecast_overnight.py` overnight run and verify the `ForecastRun` table is populated.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the three tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.
5. Remove the `cron/forecast_overnight.py` entry from the cron schedule.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules.
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `skills/le31-frontend/SKILL.md` — for the frontend conventions (if applicable).
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v1 PR that adds a foundation-model-forecaster surface to the LE31 feature 07 `demand-estimation`** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which foundation model (TimesFM 2.5, Chronos-Bolt, Moirai 2.0) becomes the first `ForecastRunner`.
3. Decide whether to ship zero-shot (no training data) or fine-tuned (training data required; charter §3.4 review).
4. Adopt the *zero-shot-foundation-model-restaurant-sales-forecasting + P10/P50/P90-bands + 4-week-period-rollups* discipline on the feature 07 `demand-estimation` surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.