# Feature 290 — `AlvaroVerona/prime-cost` v1 restaurant-P&L-analytics-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue, or to `le31 Research` P-HMM-1 if v1 project is reserved for already-spec'd work — see pipeline note)
> **Date:** 2026-10-07
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/290-AlvaroVerona-prime-cost-mit-restaurant-p-l-menu-engineering-demand-forecast-staffing-optimization-monte-carlo-synthetic-madrid-wine-bar-v1-restaurant-p-l-analytics-vocab.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/290-AlvaroVerona-prime-cost-mit-restaurant-p-l-menu-engineering-demand-forecast-staffing-optimization-monte-carlo-synthetic-madrid-wine-bar-v1-restaurant-p-l-analytics-vocab-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-07.md` (pass 70, pick A)
> **Parent-verified via:** direct GitHub API GET `/repos/AlvaroVerona/prime-cost` at `/opt/data/le31-brainstorm-2026-10-07/verify_AlvaroVerona_prime-cost.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 owner-analytics reference is a future-extension signal)

## Goal

Surface a v1 owner-analytics vocabulary reference for **small-restaurant P&L + stock-reconciliation + menu-engineering + demand-forecast + staffing-and-purchasing-optimization + Monte-Carlo on a synthetic Madrid wine bar** as a forward-looking pattern for any future LE31 v1 surface that exposes owner-facing restaurant-economics analytics (food-cost per dish, weekly stock variance, menu mix, demand forecast, staffing optimization).

## Evidence / JTBD

**Evidence classification:** inferred. The *small-restaurant P&L + stock-reconciliation + menu-engineering + Monte-Carlo demand-forecast on synthetic data* discipline is forward-looking for any future LE31 v1 owner-analytics surface; no LE31 v1 surface today has owner-economics analytics. **Confidence: high** (0★/0⑂ + 1418 KB modest + Python on-stack ✓ + 10-topic array including `food-cost + menu-engineering + restaurant-analytics + demand-forecasting + monte-carlo + optimization + ortools + scikit-learn + streamlit + hospitality` + 0 customer-facing AI + in-window by BOTH fields = strongest v1 owner-analytics cross-section pick of the 70-pass series).

**When** the LE31 owner wants to understand where the restaurant makes and loses money — profitability per dish, stock-reconciliation variance, menu engineering, demand forecast, staffing optimization — **the owner wants to** see a clean dashboard with food-cost per dish, weekly stock variance, menu mix contribution margin, Monte-Carlo demand forecast, and a what-if simulator, **but struggles because** the existing `audit_logs` + `StockEntry` SQLModel tables are event-source ledgers with no P&L / no menu-engineering / no Monte-Carlo surface, **so that** the owner cannot answer "is this dish profitable?" / "what would staffing look like if I added a 7pm shift?" without an external spreadsheet. The *small-restaurant P&L + stock-reconciliation + menu-engineering + Monte-Carlo demand-forecast on synthetic data* discipline IS the *owner-facing-clarity + explicit-state-transition* charter §3.1 invariant applied to the *owner-economics* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *small-restaurant P&L + stock-reconciliation + menu-engineering + Monte-Carlo demand-forecast + staffing-and-purchasing-optimization* decuple-primitive as a candidate vocabulary for any future LE31 v1 owner-analytics surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive.
- Record the §3.1/§3.2/§3.3/§3.4/§3.7 alignment per `le31-conventions/SKILL.md`.
- Note the **synthetic Madrid wine bar** provenance (clearly labeled as synthetic data, not real restaurant data).

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No Streamlit dashboard integration; v1 owner-analytics is forward-looking.
- No menu-engineering / food-cost-per-dish computation on the existing `MenuItem` SQLModel table.
- No Monte-Carlo demand-forecast integration into the existing `Visit`/`OrderItem` SQLModel tables.

## Description

`AlvaroVerona/prime-cost` is a **small-restaurant P&L analytics reference** with the following properties:
- **Where does a small restaurant make and lose its money?** The repo's central question is the exact question a single-owner single-restaurant operator would ask.
- **Profitability, stock reconciliation, menu engineering, demand forecast, staffing and purchasing optimization and Monte Carlo** — eight distinct analytics primitives, all on a single synthetic Madrid wine bar.
- **scikit-learn + OR-tools + Streamlit** — on-Python-stack vocabulary (LE31 uses Python; scikit-learn is not in v1 stack but the discipline is).
- **Synthetic data** — clearly synthetic; no real restaurant data.
- **MIT permissive + 1418 KB modest** — small enough to be a vocabulary reference, not a production codebase.
- **10-topic array** including `demand-forecasting + food-cost + hospitality + menu-engineering + monte-carlo + optimization + ortools + restaurant-analytics + scikit-learn + streamlit` = the strongest v1 owner-analytics cross-section topic-coverage of the 70-pass series.

The vocabulary is a strong §3.4-alignment signal for any future LE31 v1 owner-analytics surface because:
- The *Monte-Carlo demand-forecast* IS the §3.1 *explicit-state-transition* charter invariant applied to the *demand-forecast* dimension.
- The *menu-engineering + food-cost-per-dish* IS the §3.6 *Money: never use binary floats* charter invariant applied to the *per-dish-margin* dimension.
- The *stock-reconciliation + weekly-variance* IS the §3.3 *append-only-ledger-as-audit-trail* charter invariant applied to the *stock-variance* dimension.
- The *staffing-and-purchasing-optimization* IS the §3.1 *explicit-operator-state-transition* charter invariant applied to the *staffing* dimension.

## Data model

```
MenuItem           (id, name, category, price_eur, food_cost_eur, contribution_margin_eur, prep_station)  # existing
RecipeIngredient   (id, menu_item_id, ingredient_id, quantity, unit)                                      # existing
StockEntry         (id, ingredient_id, quantity_delta, reason, created_at, created_by)                   # existing — append-only
DishProfitability  (id, menu_item_id, period_start, period_end, revenue_eur, food_cost_eur, gross_margin_eur, units_sold, computed_at)  # NEW — derived view, never updated, only inserted
DemandForecast     (id, menu_item_id, period_start, period_end, forecast_mean, forecast_p10, forecast_p90, monte_carlo_n, computed_at)  # NEW — derived view, never updated
StaffingPlan       (id, period_start, period_end, role, headcount_required, headcount_scheduled, optimizer_objective, computed_at)  # NEW — derived view
StockVariance      (id, ingredient_id, period_start, period_end, expected_quantity, actual_quantity, variance_pct, computed_at)  # NEW — derived view
```

The `DishProfitability + DemandForecast + StaffingPlan + StockVariance` tables are all **derived views** that compute from the existing `OrderItem + StockEntry + MenuItem` SQLModel tables and write a new row per period. They are append-only (the *period* is the primary-key component; recomputing a period writes a new row, never updates). The *Monte-Carlo demand-forecast* is deterministic given the same input data + the same random seed; the *staffing-and-purchasing-optimization* uses OR-tools with a fixed objective function (no learning, no surprise).

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v1 PR adopts the *small-restaurant P&L + menu-engineering + Monte-Carlo demand-forecast* discipline, the following files would be touched:

- `/opt/data/le31_mmm3_research_work/backend/app/models/owner_analytics.py` — new SQLModel `DishProfitability` + `DemandForecast` + `StaffingPlan` + `StockVariance` tables (append-only, §3.1 invariant).
- `/opt/data/le31_mmm3_research_work/backend/app/services/menu_engineering.py` — compute `DishProfitability` from `OrderItem` + `MenuItem` + `RecipeIngredient` SQLModel tables.
- `/opt/data/le31_mmm3_research_work/backend/app/services/demand_forecast.py` — Monte-Carlo demand-forecast using `numpy.random` with a fixed seed.
- `/opt/data/le31_mmm3_research_work/backend/app/services/staffing_optimizer.py` — OR-tools staffing-and-purchasing optimization with a fixed objective function.
- `/opt/data/le31_mmm3_research_work/backend/app/services/stock_variance.py` — compute `StockVariance` from `StockEntry` (existing) + supplier-order `expected_quantity` (existing).
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v1 build; vocabulary-only). If a future v1 owner-analytics surface is built, the owner-side Telegram bot could surface weekly recap events with their P&L / variance / forecast state (e.g., "Weekly recap: schnitzel €14.50 / food-cost €4.20 / margin €10.30 / units 87 / variance +0.3%. Monte-Carlo forecast next week: 90 units (p10-p90: 72-110)."). The recap is operator-facing per charter §3.4; not customer-facing.

## Dependencies

- **Charter §3.1 (explicit-state-transition)**: existing `OrderItem` + `Visit` SQLModel tables are the v1 precedent; the `DishProfitability` + `StockVariance` tables extend the same pattern to the *owner-economics* dimension with **append-only period-anchored derived views**.
- **Charter §3.3 (audit-log-immutability)**: existing `StockEntry` SQLModel table is the v1 append-only ledger; the `StockVariance` table is a derived view that never updates the underlying `StockEntry` rows.
- **Charter §3.4 (operator-facing)**: the *owner-analytics* surface is operator-tooling per charter §3.4 invariant; the *Monte-Carlo demand-forecast* is a deterministic computation primitive, not customer-facing AI; the *Streamlit dashboard* is the v1 reference for the owner-facing surface.
- **Charter §3.6 (Money: never use binary floats)**: the *food-cost per dish + weekly-variance* must use `Decimal` (Python `decimal.Decimal` or pydantic `condecimal`) per the existing v1 EUR convention. A future PR would need to specify the exact rounding rule (e.g., 2 decimal places for EUR, half-even rounding).
- **Stack note**: `scikit-learn + OR-tools` are not in the v1 stack; a future PR that adopts the *menu-engineering + Monte-Carlo demand-forecast + staffing-optimization* discipline would need to add them as dependencies (or substitute with a pure-Python equivalent). The vocabulary is informative; the stack addition is a charter decision.
- **No v1 dependencies today**: this is a v1 forward-looking surface; no v1 code depends on it.

## Open questions

1. **What is the period granularity?** The discipline uses *period_start + period_end* as the primary-key component (daily, weekly, monthly?). A future PR would need to specify the period granularity. A weekly recap is the most common in restaurant operations.
2. **What is the Monte-Carlo sample size?** The discipline uses `monte_carlo_n` as a column; a future PR would need to specify the sample size (e.g., 1000, 10000). A larger sample is more accurate but slower.
3. **What is the staffing-optimization objective?** The discipline uses OR-tools with an objective function; a future PR would need to specify the objective (e.g., minimize labor cost subject to minimum coverage, minimize understaffing subject to cost cap).
4. **What is the relationship between the v1 `MenuItem.food_cost_eur` field and the v1 derived `DishProfitability` table?** The v1 `MenuItem.food_cost_eur` is the *recipe-derived cost*; the v1 derived `DishProfitability.food_cost_eur` is the *actual cost including waste + supplier-price-variance*. A future PR would need to specify the relationship.
5. **What is the data freshness?** The discipline is a derived view; a future PR would need to specify the recompute policy (e.g., nightly, weekly, on-demand). A nightly recompute is the most common.

## Why this matters

This is the **strongest v1 owner-analytics cross-section pick of the 70-pass brainstorm series**. The *small-restaurant P&L + stock-reconciliation + menu-engineering + Monte-Carlo demand-forecast + staffing-and-purchasing-optimization + scikit-learn + OR-tools + Streamlit + 10-topic array* decuple-primitive maps 1:1 onto the *owner-facing-clarity* surface that a future v1 PR might add to extend the existing `audit_logs + StockEntry` SQLModel tables. The synthetic Madrid wine bar provenance is clearly labeled (no real-restaurant-data risk); the MIT permissive license + 1418 KB modest size + 0★/0⑂ + 10-topic array + in-window-by-both-fields = the cleanest v1 owner-analytics vocabulary reference of the 70-pass series.

The **Monte-Carlo demand-forecast** discipline extends the existing v1 event-sourcing pattern to the *demand-forecast* dimension with a deterministic computation (fixed seed = reproducible forecast). The **menu-engineering + food-cost-per-dish** discipline extends the v1 `MenuItem.food_cost_eur` field to the *actual-cost-including-waste* dimension. The **stock-reconciliation + weekly-variance** discipline extends the v1 `StockEntry` event-sourcing pattern to the *stock-variance* dimension. The **staffing-and-purchasing-optimization** discipline extends the v1 explicit-operator-state-transition pattern to the *staffing* dimension.

**Charter alignment summary:** §3.1 partial (P&L + menu-engineering + Monte-Carlo demand-forecast ✓; scikit-learn + OR-tools OFF-§3.1 = explicit charter-decision needed); §3.2 strictly-compatible (MIT permissive); §3.3 ✓ (append-only `DishProfitability + StockVariance` derived views = stronger than §3.3 raw `StockEntry`); §3.4 strong alignment (owner-facing analytics + deterministic Monte-Carlo + non-AI-fallback + observable-evidence); §3.6 ✓ (food-cost per dish = existing `MenuItem.food_cost_eur` precedent); §3.7 N/A.
