# Feature 83 — Weighted Stock Cost Drift Watch

> **Priority**: P2 · **Effort**: M (3–5 days) · **Source**: brainstorm 2026-08-18 (cross-section pick C) · **Bucket**: v2 owner-pains
> **One-line**: A `weighted_avg_cost` Decimal field per `MenuItem` (derived from per-ingredient per-batch `StockEntry` unit-cost rows) plus a `/cost-drift` cook-bot command that surfaces menu items whose weighted-average ingredient cost has moved >10% week-over-week.

## Goal

The owner of a single small restaurant does not have time to compute the current weighted-average cost basis for each menu item after every supplier delivery. But the question is real and frequent: "my ragù's tomato cost basis moved 18% week-over-week — should I raise the menu price?" The cross-section pattern (append-only `StockEntry` ledger + unit-cost column + weighted-average projection + owner-visible drift alert) is observed in `TMBeaver/openstock` (3★ Python, 157KB, in-window push 2026-07-21T16:34:41Z, "Self-hosted warehouse and invoicing system for small manufacturers. Multi-location stock, weighted-average costing, VAT invoices, production BOMs, quotes, and role-based access").

## Scope

**In scope (v2 owner-pains):**
- Add a `unit_cost_eur` Decimal column to `StockEntry` (NULL allowed for legacy rows; populated on every new `receive` StockEntry with the supplier invoice unit price).
- Add a `weighted_avg_cost` Decimal field per `MenuItem`, derived from the unit_cost_eur of all `StockEntry` rows tagged with that ingredient (`MenuItemIngredient` join) within the last 30 days (configurable window).
- Add a `/cost-drift` cook-bot command that returns the menu items whose `weighted_avg_cost` has moved >10% (configurable threshold) week-over-week.
- Plain-language report: "tomato sauce (menu item 7): cost basis +18% week-over-week, current €2.84/kg, last week €2.40/kg — review menu price?".
- 1-week **experiment** measurement run before any build commitment (see `Why experiment` below).

**Out of scope (v2 owner-pains):**
- Recipe-cost margin rollup (covered by feature 74; this feature is the **ingredient** cost basis, not the **recipe** margin).
- Day-part menu margin surface (covered by feature 75; different direction — menu price × sold quantity, not ingredient cost).
- Recipe BOM maintenance (the menu-recipe link `MenuItemIngredient` already exists in feature 03; this feature adds the unit_cost capture, not the BOM itself).
- Auto menu-price recommendation (v3 territory + AI; charter §3.2 "AI may assist owner/staff, with observable evidence and a non-AI fallback" — defer).

## Description

Today the `StockEntry` table captures `{id, at, menu_item_id, qty, via, rationale, actor_user_id}` for every prepared-item quantity change. The `qty` is EUR-quantity for prepared items (e.g., 2.5 servings of ragù), but it does NOT capture the **cost of the ingredients that went into those servings**. The supplier invoice arrives separately (paper or email) and the owner mentally tracks the per-ingredient cost basis.

This feature adds a `unit_cost_eur` Decimal column to `StockEntry` (NULL for legacy rows; populated for every new `receive` StockEntry by the supplier-invoice capture flow — TBD; for v1, capture is via a new `/receive-cost <entry_id> <cost_eur> <unit>` cook-bot command, OR by extending the existing photo-stock-list flow to include the supplier invoice line items). The weighted-average cost for each `MenuItem` is computed on demand: sum of `qty × unit_cost_eur` across all `StockEntry` rows tagged with that ingredient in the last 30 days, divided by sum of `qty` across the same rows.

The `/cost-drift` command returns the menu items whose weighted-average cost has moved >10% week-over-week, with the current vs. prior-week values, in plain language. The owner decides whether to raise the menu price (separate decision, not in scope).

## Data model

```sql
-- Migration: add unit_cost_eur to StockEntry
ALTER TABLE stock_entry ADD COLUMN unit_cost_eur NUMERIC(10,4);  -- EUR per unit; NULL allowed for legacy rows

-- New derived field on MenuItem (not persisted; computed on demand)
-- MenuItem.weighted_avg_cost = SUM(StockEntry.qty * StockEntry.unit_cost_eur) / SUM(StockEntry.qty)
--   over StockEntry rows tagged with this MenuItem via MenuItemIngredient
--   within the last 30 days
```

The `weighted_avg_cost` is **derived, not persisted** (charter §3.2 "current stock is derived from entries"; same pattern). The drift detection compares the current derived value to the value 7 days ago (also derived, using a 30-day window ending 7 days ago).

## Implementation steps

1. **EXPERIMENT FIRST**: before any build, run a 1-week measurement. For 7 days, log every `StockEntry` `receive` row with its supplier-invoice unit_cost_eur (manual capture via cook-bot command), and compute the weighted_avg_cost for each MenuItem at end-of-day. Report: (a) the distribution of week-over-week cost drift across the menu; (b) the percentage of menu items with >10% drift; (c) the percentage with >25% drift. If >10% drift is common (>20% of menu items), the feature is build-candidate. If <5% drift is common, the feature is rejected (low value).
2. **Prerequisite**: ship feature 03 (Kitchen Stock Tracker) + feature 15 (Inventory Variance) + feature 26 (Reorder Point on StockEntry) to a stable baseline.
3. Add Alembic migration: `ALTER TABLE stock_entry ADD COLUMN unit_cost_eur NUMERIC(10,4)`.
4. Add `agent/services/cost_basis.py` with `weighted_avg_cost(menu_item_id, window_days=30) -> Decimal` function (Decimal, EUR, explicit rounding).
5. Add `agent/services/cost_drift.py` with `cost_drift_report(threshold_pct=10) -> list[DriftItem]` function.
6. Add `cook_bot/handlers/cost_drift.py` aiogram v3 handler bound to `/cost-drift` (owner chat id).
7. Add `cook_bot/handlers/receive_cost.py` for `/receive-cost <entry_id> <cost_eur> <unit>` (cook bot).
8. Write 6 acceptance tests in `agent/tests/test_cost_drift.py`:
   - empty StockEntry → "no ingredient data, no drift"
   - 30 days of stable cost → "0 menu items with >10% drift"
   - 1 ingredient cost spike 18% → that menu item surfaces in drift report
   - Decimal rounding (4 decimal places) → verify no float drift
   - legacy rows with NULL unit_cost_eur → excluded from projection (not included in divisor)
   - threshold_pct configurable → `/cost-drift 25` returns only >25% drift
9. Run the experiment + the tests; commit + push.

## Telegram interaction if any

- `/cost-drift` (owner) — returns the drift report inline as a Telegram message (max 4096 chars; truncate + "..." for very long reports).
- `/cost-drift <pct>` (owner) — same with custom threshold.
- `/receive-cost <entry_id> <cost_eur> <unit>` (cook) — captures supplier-invoice cost basis on a `receive` StockEntry.

## Dependencies

- **[feature 03] Kitchen Stock Tracker** — `StockEntry` schema + receive StockEntry workflow.
- **[feature 15] Inventory Variance** — adjacent but not a prerequisite. Variance is qty-based; cost-drift is EUR-based.
- **[feature 26] Reorder Point on StockEntry** — adjacent but not a prerequisite. Reorder is qty-threshold-based; cost-drift is EUR-velocity-based.
- **[feature 74] Per-Recipe Cost Margin Rollup** — adjacent but not a prerequisite. Feature 74 is the **recipe margin** direction (menu price × sold quantity); this feature is the **ingredient cost basis** direction.
- **[feature 75] Day-Part Menu Margin Surface** — adjacent but not a prerequisite. Feature 75 is day-part × menu price; this feature is week-over-week × ingredient cost.
- `agent/services/cost_basis.py` — new module.
- `agent/services/cost_drift.py` — new module.
- `cook_bot/handlers/cost_drift.py` — new aiogram v3 handler.
- `cook_bot/handlers/receive_cost.py` — new aiogram v3 handler.

## Open questions

- Should `unit_cost_eur` capture include the **delivery fee / packaging cost** or just the per-unit food cost? Charter §3.2 "Money: never use binary floats. Preserve exact EUR values and explicit tax/tip derivations" — capture exactly what the supplier invoices; let the projection sum it.
- Should the weighted-average window be **rolling 30 days** or **since last count**? Rolling 30 days is simpler; since-last-count is more accurate but requires a count event marker. Recommend rolling 30 days for v1.
- Should `/cost-drift` also surface **supplier concentration risk** (e.g., "tomatoes: 90% from one supplier, consider a backup")? Out of scope for v1; v3 territory.
- Should the experiment measurement capture be **automatic** (parse supplier invoices via OCR) or **manual** (cook types `/receive-cost`)? Manual for v1; auto via OCR is v3 territory.

## Why this matters

The owner of a single small restaurant is cost-exposed: ingredient prices move weekly, menu prices move quarterly (because of menu-printing cycles). Without a weighted-average cost basis projection, the owner learns about cost drift only when the margin collapses at end-of-month reconciliation. With `/cost-drift`, the owner gets a weekly plain-language summary of which menu items have ingredient cost basis that moved >10%, on the surface they already use (Telegram), with the current vs. prior-week values to inform the menu-price decision. The cross-section pattern (weighted-average cost basis + owner-visible drift alert) is observed in the in-window `TMBeaver/openstock` at 3★ + 157KB + in-window push 2026-07-21. **The experiment is the right gate here**: run the measurement for 1 week before committing to build, and reject the slice if the drift distribution shows <5% week-over-week movement.

## Distinct from existing features

- **Feature 03 (Kitchen Stock Tracker)** is the **qty** ledger. This feature adds the **cost basis** projection on top of the existing qty ledger.
- **Feature 15 (Inventory Variance)** detects qty variance between expected and counted stock. This feature detects EUR variance between current and prior-week ingredient cost basis.
- **Feature 16 (Supplier Orders)** captures supplier orders. This feature captures the **unit cost** of each receive StockEntry.
- **Feature 26 (Reorder Point on StockEntry)** triggers reorder when qty drops below threshold. This feature surfaces **cost drift** when ingredient unit cost moves >10%.
- **Feature 74 (Per-Recipe Cost Margin Rollup)** computes recipe margin = menu_price - ingredient_cost. This feature computes ingredient_cost itself; feature 74 then uses it.
- **Feature 75 (Day-Part Menu Margin Surface)** computes day-part × menu margin. This feature is week-over-week × ingredient cost; different axes.

## Cross-section evidence

- **Anchor**: [TMBeaver/openstock](https://github.com/TMBeaver/openstock) — 3★ Python, 157KB, pushed 2026-07-21T16:34:41Z. "Self-hosted warehouse and invoicing system for small manufacturers. Multi-location stock, weighted-average costing, VAT invoices, production BOMs, quotes, and role-based access. Python, Flask, SQLite; no build step."
- **Adjacent (in-window)**: `RippleCheck/Ripple-Lead-Finder` (4★, Python, 2026-08-07) — local-business finder + outreach; not cost-related but small-business JTBD.
- **Adjacent (carry-over)**: `ifrederico/forkluck` (0★, Python, AGPL recipe costing workbench — pattern-only, not importable per charter §3.2 AGPL-incompatibility).
- **Academic backdrop**: standard accounting methods (FIFO / LIFO / weighted-average) are well-established inventory valuation methods; this feature implements the weighted-average variant for restaurant ingredient cost basis.

## Why experiment (not build or reject)

- **Experiment gate**: the value of this feature depends on the actual week-over-week cost drift distribution in the LE31 owner's data. If real cost drift is <5% week-over-week in 90% of cases, the feature is low-value (`reject`). If real cost drift is ≥10% in ≥20% of cases, the feature is build-candidate. **Run the experiment before committing.**
- **Prerequisite gate**: feature 03 + feature 15 + feature 26 need to be in a stable shipped state before adding cost-drift on top.
- **Charter §3.2 money**: `weighted_avg_cost` must be Decimal, EUR, with explicit rounding rule (4 decimal places); the experiment will verify the rounding rule works on real data.
- **Scope creep risk**: cost drift could expand into "recipe margin optimization" or "menu price recommender" which crosses into v2-AI territory. Stay narrow on cost basis + drift alert only.

## Re-evaluation trigger

- 1-week experiment measurement complete → if >20% of menu items show >10% drift, status becomes build-candidate; if <5%, status becomes reject.
- An in-window ≥10★ peer surfaces with a small-business cost-drift alert pattern → escalates evidence to high.
- The LE31 owner explicitly asks for it → status becomes build (skip experiment).

## Status

**experiment** — gate verdict from brainstorm 2026-08-18 (HMM-99). Run 1-week measurement first; re-evaluate based on actual cost drift distribution. Prerequisites (features 03/15/26) not in stable shipped state.
