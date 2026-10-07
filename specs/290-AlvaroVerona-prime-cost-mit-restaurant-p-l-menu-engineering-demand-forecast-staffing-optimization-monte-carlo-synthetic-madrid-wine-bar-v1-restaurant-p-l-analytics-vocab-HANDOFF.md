# HANDOFF — 290-AlvaroVerona-prime-cost-v1-restaurant-p-l-analytics-vocab

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-07
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/290-AlvaroVerona-prime-cost-mit-restaurant-p-l-menu-engineering-demand-forecast-staffing-optimization-monte-carlo-synthetic-madrid-wine-bar-v1-restaurant-p-l-analytics-vocab.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 owner-analytics cross-section pick of the 70-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 owner-analytics vocabulary reference (`AlvaroVerona/prime-cost`, MIT, 0★/0⑂, 1418 KB modest, Python on-stack ✓, 10-topic array, in-window by BOTH fields) for the next time the LE31 owner opens a v1 owner-analytics surface window.

If the trigger condition (v1 owner-analytics surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `AlvaroVerona/prime-cost` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Implement the `DishProfitability + DemandForecast + StaffingPlan + StockVariance` SQLModel tables as described in the active feature's Data model section.
4. Implement the menu-engineering service (compute `DishProfitability` from `OrderItem + MenuItem + RecipeIngredient`).
5. Implement the Monte-Carlo demand-forecast service (using `numpy.random` with a fixed seed for reproducibility).
6. Implement the OR-tools staffing-and-purchasing-optimization service (with a fixed objective function).
7. Implement the stock-variance service (compute `StockVariance` from `StockEntry` + supplier-order `expected_quantity`).
8. Run the v1 test suite + the new v1 owner-analytics test suite.
9. Surface any test failures to the owner (LE31 v1 has no owner-analytics today; the test suite will be green if `OrderItem + StockEntry` are empty, but the deterministic Monte-Carlo must be verified against a synthetic seed scenario).
10. Verify the v1 `audit_logs + StockEntry` SQLModel tables are untouched (the v1 owner-analytics derived views are NEW tables, not a migration of v1 `audit_logs`).

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 owner-analytics surface window.

## Mandatory inputs

- **Active feature**: `features/290-AlvaroVerona-prime-cost-mit-restaurant-p-l-menu-engineering-demand-forecast-staffing-optimization-monte-carlo-synthetic-madrid-wine-bar-v1-restaurant-p-l-analytics-vocab.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-07.md` (pass 70, pick A)
- **Raw fetches**: `/opt/data/le31-brainstorm-2026-10-07/gh_hospitality_py_df.json` (parent re-fetched the productive query) and `/opt/data/le31-brainstorm-2026-10-07/verify_AlvaroVerona_prime-cost.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 70-pass series**:
  - **Feature 174 / 177 — `ilkinism/shiftwright`** — v2 owner-pains local-first-staff-rota
  - **Feature 246 — `mshykhov/expense-ledger-bot`** — v1 Telegram expense-ledger
  - **Feature 165 — `Ladle/restaurant-prep-forecasting`** — v1 food-cost-leak-detection
  - **Feature 218 — `LuisRG98/restaurant-saas-api`** — v1 production restaurant API reference

## Mandatory LE31 skill list

The external coding agent **MUST** load these skills before implementing:

- `le31-conventions` — charter invariants and the seven-check feature gate
- `le31-v1-feature-pattern` — v1 feature contract shape, slicing rules, and DoD
- `le31-handoff-spec` — frozen contract discipline and verification protocol
- `development` — generic coding pipeline (specify → plan → tasks → implement)
- `speckit-specify` — feature spec writer
- `speckit-plan` — implementation plan writer
- `speckit-tasks` — dependency-ordered task list writer

The external coding agent **MUST NOT**:

- Add `scikit-learn + OR-tools` to the v1 stack without an explicit charter decision.
- Update or delete any `StockEntry` or `audit_logs` rows (append-only §3.3 invariant).
- Send the `Monte-Carlo demand-forecast` results to diners (operator-facing §3.4 invariant).
- Use binary floats for `food_cost_eur` or `gross_margin_eur` (use `Decimal` per charter §3.6).

## Frozen contract

The active feature file is the frozen contract. Do not silently change the slice, scope, or verification path. If new evidence requires a contract change, surface it to the user and patch the package before re-sending.

## Verification protocol

The external coding agent verifies:

1. Its read of the contract matches the recorded contract fields (`Goal`, `Evidence`, `Scope`, `Description`, `Data model`, `Implementation steps`, `Telegram interaction`, `Dependencies`, `Open questions`, `Why this matters`).
2. The slice does not require another skill, model, or migration outside the package.
3. The end-to-end acceptance path is executable in the configured environment.
4. The rollback or feature-removal path is present and reversible.

End-to-end acceptance path (when triggered):
- Owner opens the v1 owner-analytics surface
- Owner sees weekly recap with `DishProfitability + StockVariance + DemandForecast + StaffingPlan` for the past 4 weeks
- Owner sees the Monte-Carlo forecast for next week with `forecast_mean + forecast_p10 + forecast_p90`
- Owner clicks a dish and sees the food-cost-per-dish + contribution-margin breakdown
- The synthetic seed test verifies the Monte-Carlo is deterministic (same seed = same forecast)

## Rollback path

- Delete the `DishProfitability + DemandForecast + StaffingPlan + StockVariance` SQLModel tables (drop + alembic downgrade).
- Delete the `owner_analytics.py + menu_engineering.py + demand_forecast.py + staffing_optimizer.py + stock_variance.py` service files.
- The v1 `audit_logs + StockEntry` SQLModel tables are untouched (NEW tables, not a migration).
- No data is lost (the derived views are computed from existing v1 data; deleting the derived views loses the cached views but not the source data).

## Sign-off gap

This is a defer artifact. The trigger condition is **the next time the LE31 owner opens a v1 owner-analytics surface window** (estimated Q1 2027 based on the v1 roadmap; no current commitment).

The external coding agent must mirror back the frozen contract before implementing and stop if it cannot.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial (P&L + menu-engineering + Monte-Carlo demand-forecast ✓; scikit-learn + OR-tools OFF-§3.1 = explicit charter-decision needed); §3.2 strictly-compatible (MIT permissive); §3.3 ✓ (append-only `DishProfitability + StockVariance` derived views); §3.4 strong alignment (owner-facing analytics + deterministic Monte-Carlo + non-AI-fallback + observable-evidence); §3.6 ✓ (food-cost per dish = existing `MenuItem.food_cost_eur` precedent); §3.7 N/A.
