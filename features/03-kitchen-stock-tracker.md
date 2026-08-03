# Feature 03 — Kitchen Stock Tracker (Prepared Items)

## Goal

The kitchen tells the system "today we have 8 pieces of cake" and the system
keeps a live ledger — each slice sold decrements the count, when it hits 0 the
menu item is hidden from waiters, and the cook gets a Telegram alert.

## Scope

**In scope (v1):**
- Create a `Batch` for a prepared item with starting quantity.
- Decrement on sale (triggered by order close).
- Mark sold-out (auto or manual via `/sold_out`).
- End-of-day waste logging.
- Daily summary report sent to cook via Telegram.

**Out of scope (v1):**
- Recipe / BOM (auto-deduct ingredient stock when prep happens).
- Supplier integration / purchase orders.
- Expiry alerting (we'll record expiry but not notify).

## Description

A `Batch` is a concrete instance of a prepared item: "8 pieces of Tiramisu,
prepared 09:00 today, expires 22:00". Every sale of that menu item writes
a `StockEntry(qty_delta = -1, reason = 'sale', ref_order_item_id = ...)`
row. Sum across the ledger gives current remaining stock.

When `qty_remaining = 0`:
- Item marked `sold_out` for the day.
- Menu auto-hides for waiters.
- Cook gets a Telegram message: "Tiramisu is sold out."

## Data model

```
MenuItem       (id, name, unit, unit_price, is_prepared, category)
Batch          (id, menu_item_id, qty_start, qty_remaining,
                prepared_at, expires_at, photo_url, notes)
StockEntry     (id, batch_id, qty_delta, reason, ref_order_item_id,
                by_user_id, at)
```

The `StockEntry` table is an **append-only ledger**. Never `UPDATE` or `DELETE`.
Current stock = `SUM(qty_delta)` filtered by batch.

## Triggers

| Event | Effect |
|---|---|
| Cook uploads menu photo → item created with batch | `StockEntry(reason='initial', qty_delta = qty_start)` |
| OrderItem status → `served` and menu_item.is_prepared | `StockEntry(reason='sale', qty_delta = -1)` for active batch |
| Cook `/sold_out <item>` | `StockEntry(reason='sold_out', qty_delta = -(remaining))` |
| Cook `/leftover <item> <qty>` (EOD) | `StockEntry(reason='waste', qty_delta = -qty)` |
| Cook `/restock <item> <qty>` | `StockEntry(reason='restock', qty_delta = +qty)` |

## Dependencies

- [02-order-taking.md](02-order-taking.md) — sales come from order close.
- [04-menu-photo-bot.md](04-menu-photo-bot.md) — batches are born from the
  daily menu photo + cook's per-item quantity replies.

## Open questions

- What happens if two batches of the same item are active (e.g. cook made more
  tiramisu at 3pm)? Use FIFO — oldest batch consumed first.
- Should we auto-mark `sold_out` at expiry time? (Yes seems obvious but needs
  a periodic job.)
- Should the menu hide sold-out items for *today only* or until cook re-stocks?

## Why this matters

This is the **core differentiator**. No existing open-source POS handles
"prepared item with finite, per-piece stock" as a first-class concept.
URY/ERPNext can do it via the Batch module but requires the full ERP stack.
We can do it in ~150 lines of Python + 4 SQL tables.