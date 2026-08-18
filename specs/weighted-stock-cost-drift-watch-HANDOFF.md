# weighted-stock-cost-drift-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/83-weighted-stock-cost-drift-watch.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `83`
- Slug: `weighted-stock-cost-drift-watch`
- Contract file: `features/83-weighted-stock-cost-drift-watch.md`
- Bucket: **v2 owner-pains** — experiment (1-week measurement required before build)
- Linear parent: `HMM-99` (Brainstorm 2026-08-18 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft cost-drift experiment artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (in-window GitHub `topic:small-business` cluster — `TMBeaver/openstock` 3★ Python, 157KB, in-window push 2026-07-21T16:34:41Z, "Self-hosted warehouse and invoicing system for small manufacturers. Multi-location stock, weighted-average costing, VAT invoices, production BOMs, quotes, and role-based access").

**Confidence:** **medium** for the JTBD pull (weighted-average inventory valuation is a standard accounting method; restaurant ingredient cost basis is a real owner question), **low** for the immediate-build peer signal (3★ is the lowest-confidence anchor of the 3 picks; the pattern is real but the peer evidence is thin).

**Decision: experiment.** Run a 1-week measurement BEFORE any build commitment. Capture supplier-invoice unit_cost_eur on every `receive` StockEntry for 7 days, compute weighted_avg_cost per MenuItem at end-of-day, and report the distribution of week-over-week cost drift. If >20% of menu items show >10% drift, status becomes build-candidate. If <5% drift is common, status becomes reject.

**Failed checks:**
- **Practicability**: prerequisite features 03 (Kitchen Stock Tracker) + 15 (Inventory Variance) + 26 (Reorder Point on StockEntry) need to be in a stable shipped state before adding cost-drift on top.
- **Charter §3.2 money**: `weighted_avg_cost` must be Decimal, EUR, with explicit rounding rule (4 decimal places); the experiment will verify the rounding rule works on real data.
- **Cost-to-value**: requires 1-week measurement of actual cost-basis volatility before build. The value of the feature depends on the real drift distribution; the experiment is the gate.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate; especially §3.2 money Decimal invariant).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-18).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after the experiment runs and prerequisites ship).
6. `le31-research` (for the cross-section evidence base).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice will touch (when re-elevated to build, post-experiment)

```
features/83-weighted-stock-cost-drift-watch.md            # NEW (this artifact)
specs/weighted-stock-cost-drift-watch-HANDOFF.md         # NEW (this file)
INDEX.md                                                  # EDIT: append one row to "Active feature pipeline" table
agent/services/cost_basis.py                              # NEW (weighted_avg_cost function; Decimal, EUR, 4-decimal rounding)
agent/services/cost_drift.py                              # NEW (cost_drift_report function)
cook_bot/handlers/cost_drift.py                           # NEW (aiogram v3 /cost-drift handler)
cook_bot/handlers/receive_cost.py                         # NEW (aiogram v3 /receive-cost handler)
alembic/versions/xxx_add_stock_entry_unit_cost.py         # NEW (Alembic migration: ADD COLUMN unit_cost_eur NUMERIC(10,4))
agent/tests/test_cost_drift.py                            # NEW (6 acceptance tests)
```

One Alembic migration (`ADD COLUMN unit_cost_eur NUMERIC(10,4)` to `stock_entry`). **Zero schema impact on `Visit`, `Order`, `OrderItem`, `Bill`, `Payment`.** `weighted_avg_cost` is **derived, not persisted** (charter §3.2 "current stock is derived from entries"; same pattern). Zero new pip dependencies.

## Verification protocol

After the artifact ships (post-experiment + post-prerequisites):

1. **Run the 1-week experiment FIRST**: capture supplier-invoice unit_cost_eur on every `receive` StockEntry for 7 days (manual via cook-bot `/receive-cost <entry_id> <cost_eur> <unit>`). Compute weighted_avg_cost per MenuItem at end-of-day. Report the distribution. If >20% of menu items show >10% drift, proceed to build; if <5%, reject and close the artifact.
2. **Read back** `features/83-weighted-stock-cost-drift-watch.md` and confirm it matches the daily-brainstorm report's "83-weighted-stock-cost-drift-watch" pick description.
3. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-18), pick slug, feature path, and Linear sub-issue ID.
4. **Run the 6 acceptance tests** in `agent/tests/test_cost_drift.py`:
   - empty StockEntry → "no ingredient data, no drift"
   - 30 days of stable cost → "0 menu items with >10% drift"
   - 1 ingredient cost spike 18% → that menu item surfaces in drift report
   - Decimal rounding (4 decimal places) → verify no float drift
   - legacy rows with NULL unit_cost_eur → excluded from projection (not included in divisor)
   - threshold_pct configurable → `/cost-drift 25` returns only >25% drift
5. **Run the LE31 test suite** (`pytest` or equivalent) and confirm it still passes.
6. **Hand-test on the cook bot**: trigger `/cost-drift` in a test chat; verify the drift report renders within the 4096-char Telegram limit.
7. **On a future daily-brainstorm pass**: re-query the GitHub `topic:small-business` cluster for new in-window small-business cost-drift alert patterns. If a new ≥10★ peer surfaces, escalate evidence and re-evaluate.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`.

- Title: `Feature 83 — weighted-stock-cost-drift-watch`.
- Body: short summary + the file path to `features/83-weighted-stock-cost-drift-watch.md` (≤1500 chars).
- Parent: `HMM-99` (Brainstorm 2026-08-18 — daily).
- Status: `Backlog` (experiment; run 1-week measurement first).

## Rollback path

Delete `features/83-weighted-stock-cost-drift-watch.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. Remove `agent/services/cost_basis.py`, `agent/services/cost_drift.py`, `cook_bot/handlers/cost_drift.py`, `cook_bot/handlers/receive_cost.py`, the Alembic migration, and the test file. Revert the Alembic migration (`alembic downgrade -1`). No data loss to revert (the new column is NULL-able and not yet populated at the defer state).

## Why this matters (for the coding agent)

The owner of a single small restaurant is cost-exposed: ingredient prices move weekly, menu prices move quarterly (because of menu-printing cycles). Without a weighted-average cost basis projection, the owner learns about cost drift only when the margin collapses at end-of-month reconciliation. With `/cost-drift`, the owner gets a weekly plain-language summary of which menu items have ingredient cost basis that moved >10%, on the surface they already use (Telegram), with the current vs. prior-week values to inform the menu-price decision. The cross-section pattern (weighted-average cost basis + owner-visible drift alert) is observed in the in-window `TMBeaver/openstock` at 3★ + 157KB + in-window push 2026-07-21.

**Distinct from feature 74 (Per-Recipe Cost Margin Rollup) and feature 75 (Day-Part Menu Margin Surface)**: feature 74 computes recipe margin = menu_price - ingredient_cost; feature 75 computes day-part × menu margin; this feature computes ingredient_cost itself (the foundation feature 74 then uses). Different cost surface, different JTBD owner question.

**Status: experiment.** Run 1-week measurement before build. Re-evaluate based on actual cost-basis volatility distribution. Charter §3.2 "Money: never use binary floats" applies — `weighted_avg_cost` MUST be Decimal, EUR, 4-decimal rounding.
