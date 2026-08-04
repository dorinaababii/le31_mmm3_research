# Feature 26 — Reorder Point on StockEntry

## Goal

Add a per-menu-item **reorder point** (`reorder_point` + `par_level`) on top of the
existing append-only `StockEntry` ledger so the owner gets an actionable "X items
hit reorder today" signal at end of service — without breaking the append-only
invariant or introducing a separate supplier-orders workflow.

## Scope

**In scope (v1):**
- New nullable columns on `MenuItem` (or `Batch`): `reorder_point INTEGER`,
  `par_level INTEGER`. Default `NULL` (feature off per item).
- New cook-bot command `/reorder` that returns the items whose active batch's
  `SUM(qty_delta)` is at or below `reorder_point`.
- New owner-only summary line in the existing cook `/end_of_day` output:
  "3 items need reorder" with the item names.
- A `GET /api/inventory/reorder` endpoint returning the same list as JSON,
  guarded by the existing role check.
- One new file `backend/app/routers/inventory_reorder.py`; no new tables.

**Out of scope (v1):**
- Automated supplier orders (feature 16 territory) — out of scope; this
  contract stops at the "needs reorder" signal.
- Multi-restaurant reorder rules.
- Email/SMS alerts to suppliers.
- A history of "when reorder last fired" — derived from `StockEntry` if ever
  needed in v2.
- Auto-reorder via webhook to any supplier.

## Description

The current `Batch` model (charter §3.1) tracks `qty_remaining` via the
append-only `StockEntry` ledger — `qty_remaining = SUM(StockEntry.qty_delta)`
per active batch. The model is operationally truthful but does not tell the
owner *when to buy*. `TidalBeast37/restaurant-inventory-rop` (pushed
2026-08-02; see `/opt/data/le31-daily-research-2026-08-04.md`) is the first
in-window peer implementing automated Reorder Point calculations for
restaurant inventory.

This contract closes that next layer with the smallest possible change:

- Add `reorder_point` + `par_level` to the existing table (nullable).
- Derive "needs reorder" by computing `SUM(qty_delta)` over active `StockEntry`
  rows for each `MenuItem` and comparing to `reorder_point`. Default-off per
  item means no behaviour change for items the owner hasn't tuned.
- Surface the signal through one new cook-bot command and one new GET
  endpoint.

The `StockEntry` ledger remains append-only. ROP is a *read* over the ledger.
The explicit-state rule is unaffected (no `OrderItem` transition is automated).

## Data model

No new tables. Two nullable columns on the existing `MenuItem` table:

```
MenuItem   (existing) — new cols: reorder_point INTEGER NULL, par_level INTEGER NULL
Batch      (existing) — unchanged; qty_remaining still derived from StockEntry
StockEntry (existing) — append-only ledger; ROP only reads it
```

Migration: `init_db()` adds the two columns if absent (existing pattern).

## Implementation

1. **Schema migration** — extend `backend/app/models.py` `MenuItem` with
   `reorder_point: Optional[int]` and `par_level: Optional[int]`.
2. **New router** `backend/app/routers/inventory_reorder.py`:
   - `GET /api/inventory/reorder` → returns `[{menu_item_id, name,
     current_remaining, reorder_point, par_level}]` for items where
     `current_remaining <= reorder_point`.
   - Query is `SELECT MenuItem, SUM(StockEntry.qty_delta) FROM MenuItem LEFT
     JOIN Batch ON ... LEFT JOIN StockEntry ON ... WHERE active=1 GROUP BY
     ...`.
3. **Wire into `app/main.py`** — include the new router.
4. **Cook bot** — extend `backend/app/bot/cook_bot.py` with `/reorder` command
   (chat-id-allowlisted, same as `/start_today`).
5. **EOD summary line** — extend the existing `/end_of_day` handler to call
   the new endpoint and append "N items need reorder" + names.
6. **Manual verification**:
   - `cd backend && uvicorn app.main:app --reload`
   - In Telegram (cook role): `/start_today` → set `reorder_point = 2` on
     tiramisu via a new `/set_reorder tiramisu 2` admin command (out of v1
     slice — pre-seed via direct DB or `init_db` fixture for verification).
   - Sell 6 of 8 tiramisu slices (so 2 remain) → `current_remaining == 2 ==
     reorder_point` → `/reorder` lists tiramisu; `/end_of_day` shows "1 item
     needs reorder: tiramisu".
   - Sell one more → `current_remaining == 1 < reorder_point` → still
     listed; first time the threshold was crossed, also log a one-line
     `info` in the cook-bot transcript.
   - Repeat with `reorder_point = NULL` (default) → item never appears in
     reorder list (proves the feature is opt-in per item).

## Telegram interaction

- New command `/reorder` — returns the current reorder list (plain text).
- Existing `/end_of_day` — extended with the reorder line.
- **No new cook input surface beyond these two commands.**

## Dependencies

- [03-kitchen-stock-tracker.md](../features/03-kitchen-stock-tracker.md) —
  `StockEntry` ledger is the source of truth that ROP reads; append-only
  invariant preserved.
- [04-menu-photo-bot.md](../features/04-menu-photo-bot.md) — defines the
  `Batch` lifecycle and active-batch semantics that ROP depends on.
- [16-supplier-orders.md](../features/16-supplier-orders.md) — explicit
  upstream of this contract; this is the v1 *signal*; feature 16 is the
  v2 *action*.

## Open questions

- Should the reorder line appear in `/start_today` output (morning pre-prep)
  as well as `/end_of_day`? Pro: helps the cook decide what to bake; con:
  scope creep. Default: `/end_of_day` only; revisit after first live trial.
- Reorder firing cadence — once-per-day at EOD, or every time a `StockEntry`
  row commits? Default: EOD only; live-streaming is a v2 polish (would
  piggy-back on feature 23 SSE).
- Owner-only vs cook-only visibility — both roles currently have access to
  the same bot via the chat-id allowlist; the `/reorder` command is safe
  for both.

## Why this matters

The killer pattern is the append-only `StockEntry` ledger. Every restaurant
op who looks at it asks the next question: "OK, I can see the truth — but
when do I need to reorder?" This contract answers that question with a
nullable, opt-in column on the existing model. It is the smallest, safest
step toward feature 16 (supplier orders), which is too large for v1.

Externally primed by `TidalBeast37/restaurant-inventory-rop` (2026-08-02):
**first explicit ROP-on-restaurant-inventory peer observed in daily
research.** None of the in-window Python POS repos implement ROP on a true
append-only ledger; LE31's position remains defensible.