# Inventory & Finite-Stock Tracking

This is the **single most important category** for the user's spec — they
specifically called out the case "kitchen prepared a cake today, 8 pieces; if
some customer buys then stock decreases by -1". That is **finite stock of
prepared/cooked items, decremented per unit sold**.

## Top projects

| # | Project | Repo | ⭐ | Last push | License | Stack |
|---|---|---|---|---|---|---|
| 1 | **Nishiki** | https://github.com/nishiki-tech/nishiki-frontend | 24 | 2024-11-01 | MIT | TypeScript + React Native |
| 2 | **harismuneer/Restaurant-Management-System** | https://github.com/harismuneer/Restaurant-Management-System | 346 | 2025-01-30 | MIT | Java + Android |
| 3 | **URY** (uses ERPNext Stock module) | https://github.com/ury-erp/ury | 318 | 2026-07-15 | AGPL-3.0 | Python + Frappe |
| 4 | **RestoPOS** | https://github.com/faizaldevs/RestoPOS | 100 | 2025-03-10 | MIT | Laravel + Vue |

## Notable patterns

- **Batch / Lot model** (used by ERPNext and Nishiki): an item is a *recipe*,
  a *batch* is a concrete preparation ("8 cakes, baked 09:00 today"). Sales
  decrement batch quantity. When `qty ≤ 0` the item auto-hides from the menu.
- **Stock-entry ledger**: never delete; append a `StockEntry(qty ±, reason,
  ref)` row. Sum the ledger to get current stock. This is the pattern used by
  every serious inventory system.
- **Recipe / BOM (Bill of Materials)**: the parent menu item expands to
  ingredient children (1 cake = 200g flour + 150g sugar + …). When a batch is
  created, ingredients are deducted from raw stock.

## Recommended data model for our app

```
Item          (id, name, unit, category, is_prepared, perishable)
Batch         (id, item_id, qty_start, qty_remaining, prepared_at, expires_at, photo_url)
StockEntry    (id, batch_id, qty_delta, reason, ref_order_item_id, by_user, at)
Recipe        (id, parent_item_id, ingredient_item_id, qty_per_unit)
RecipeBatch   (batch_id, ingredient_batch_id, qty_consumed)  -- snapshot at prep time
```

When an `OrderItem` is closed (paid):
1. Look up the menu item → if `is_prepared`, decrement the active batch's
   `qty_remaining` and write a `StockEntry(reason='sale')`.
2. If `qty_remaining = 0`, mark item as `sold_out` and notify kitchen via Telegram.
3. If the item is ingredient-based (e.g. a cocktail), consume from ingredient
   batches instead.

## Gaps & opportunities

- **ERY/Nishiki are desktop/mobile apps** with their own UI; integrating our
  Telegram-driven flow is awkward.
- **ERPNext Batch system is overkill** — full WMS, requires Postgres + Redis + Frappe.
- No open-source project handles **"I baked 8 cakes at 9am"** with a Telegram
  command + photo upload. **This is a real gap and the user's killer feature.**

## Recommendation

Implement the Batch + StockEntry pattern ourselves in our own schema; it's
~150 lines of SQL + a thin CRUD layer. Do not adopt ERPNext just for this.

See [../features/03-kitchen-stock-tracker.md](../features/03-kitchen-stock-tracker.md)
and [../features/04-menu-photo-bot.md](../features/04-menu-photo-bot.md).