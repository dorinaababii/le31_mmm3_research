# Feature 15 — Inventory Variance & Waste Tracking

> **Priority**: P2 · **Effort**: L (10–20 days) · **Source**: owner-pains
> research — #9 most-requested feature with "very common" frequency:
> "Theoretical stock says 40 portions; we have 25. Was it waste, over-portioning,
> bad receiving, or theft?"
> **One-line**: Per-item variance reporting — what the books say vs. what's actually
> on the shelf — broken down by reason (waste, comp, receiving, theft signal).

## Goal

Give the owner real visibility into where stock goes. Today most small
restaurants either (a) don't track inventory at all (gut feel only) or
(b) use a commercial system like MarketMan / MarginEdge at $200-500/mo.

We extend our existing append-only `StockEntry` ledger (already from feature 03)
to add **theoretical vs actual** counting + variance analysis.

## Scope

**In scope (v1 of this feature):**
- Periodic stock count (cook counts what's on the shelf, enters in Telegram).
- Computes "theoretical" stock = `qty_start + sum(purchases) − sum(sales) − sum(waste_log)`.
- Variance = actual − theoretical (positive = over, negative = under).
- Variance report per item, per shift, per week.
- Waste reasons enum: `prep_error`, `spoiled`, `customer_return`, `staff_meal`, `comp`, `other`.
- Comp / void tracking: waiter marks item as `comp` with a reason; contributes to variance.
- Manager dashboard tile: top 5 items by variance this week.

**Out of scope:**
- Theft detection algorithms (variance is shown; interpretation is human).
- Supplier integration / automatic purchase orders.
- Bar inventory (liquor bottles, wine bottles — different units).
- Perpetual vs periodic inventory (we do periodic; perpetual is for chains).

## Description

Our existing `StockEntry` ledger already tracks every stock change. The
variance feature adds:

1. **Theoretical stock** at any moment:
   ```
   theoretical = SUM(qty_delta)
                 WHERE batch_id IN (active batches of menu_item X)
   ```

2. **Actual stock** from a count event:
   ```
   CountEvent.item_id, count_qty, counted_at, by_user_id
   ```

3. **Variance** = `actual − theoretical`.

The variance report then attributes the gap to plausible reasons:
- High `waste` stock entries → likely waste / spoilage.
- Many `comp` order_items → comps.
- Mismatch with `purchase` stock entries → receiving error.

We can't **prove** theft — but we can **show the manager where to look**.

## Data model

```
StockEntry       (existing — extends with new reasons)
PurchaseOrder
  id              PK
  supplier        TEXT
  ordered_at      DATETIME
  received_at     DATETIME NULL
  status          Enum (draft | ordered | partial | received | cancelled)

PurchaseLine
  id              PK
  purchase_order_id FK
  ingredient_id   FK
  qty_ordered     Decimal
  qty_received    Decimal NULL
  unit_cost       Decimal

CountEvent
  id              PK
  ingredient_id   FK  (or batch_id for prepared items)
  count_qty       Decimal
  counted_at      DATETIME
  by_user_id      FK
  notes           TEXT NULL

WasteLog         -- could be derived from StockEntry(reason='waste'); explicit table optional
  id              PK
  stock_entry_id  FK
  waste_reason    Enum (prep_error | spoiled | customer_return | staff_meal | comp | other)
  by_user_id      FK
  at              DATETIME
```

## Implementation

1. **Extend `StockEntry.reason` enum** to add `purchase`, `comp`, `count_adjustment`.
2. **Add `PurchaseOrder` + `PurchaseLine` + `CountEvent`** tables.
3. **Theoretical computation** as a SQL view or stored procedure.
4. **Count flow** — cook runs `/count` in Telegram; bot walks through items,
   waits for numbers, writes `CountEvent` rows.
5. **Variance report** — `GET /api/reports/variance?from=...&to=...` returns
   per-item variance + breakdown.

## Telegram interaction

```
Cook: /count
Bot:  Let's count today's prepared items.

       Schnitzel — theoretical: 7 — actual? [___]
       Burger    — theoretical: 4 — actual? [___]
       Tiramisu  — theoretical: 0 — actual? [___] (sold out)
       ...

Cook: 6 / 4 / 0
Bot:  Variance:

       Schnitzel: -1 (under by 1) — likely waste
       Burger:    0 ✓
       Tiramisu:  0 ✓

       Save these counts? [Yes] [Re-enter]
```

```
Manager: /variance_week
Bot:     This week's variance:

         Item            Theo  Actual  Δ     Likely cause
         Schnitzel         142    138  -4   waste (3) + comp (1)
         Burger             98     96  -2   waste
         Tiramisu           42     40  -2   waste
         ...
         Total loss: €87.40

         Top concern: Schnitzel — 4% variance. Investigate.
```

## Dependencies

- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — the existing ledger is the foundation.
- [10-allergen-tracking.md](10-allergen-tracking.md) — `Ingredient` table is the unit of measure.
- [16-supplier-orders.md](16-supplier-orders.md) — PurchaseOrder for receiving.

## Open questions

- Should the count be done daily, weekly, or on-demand? (Default: weekly + on-demand.)
- Do we need bar/liquor tracking? (Common in restaurants but adds a new unit system.)
- Should the cook see their own variance, or only the manager? (Both, but manager sees dollar values.)

## Why this matters

Per the owner-pains research, inventory variance is in the **top 3 features
by direct financial impact** — a 5% shrinkage rate is typical in small
restaurants, representing thousands of euros per year. The catch is data
discipline: variance reports are only as good as the counts that go in.

Recommend building this **after** the cook is in the habit of using the
existing stock tracker (feature 03) — typically 2-4 weeks of usage.