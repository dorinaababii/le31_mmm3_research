# Kitchen Display Systems (KDS)

A KDS replaces paper kitchen tickets with a screen showing active orders.
For our app, this overlaps heavily with the kitchen-side Telegram bot.

## Top projects

| # | Project | Repo | ⭐ | Last push | License | Stack |
|---|---|---|---|---|---|---|
| 1 | **URY Mosaic** | https://github.com/ury-erp/mosaic | 45 | 2025-11-04 | AGPL-3.0 | Python (Frappe) + JS UI |
| 2 | **CampusBites** | https://github.com/Pxrvn07/CampusBites | 15 | 2026-03-29 | MIT | TypeScript full-stack |
| 3 | **FoodStreams** | https://github.com/calvincchong/FoodStreams | 13 | 2023-10-08 | none | JS MVP |
| 4 | **OpenKDS** | https://github.com/BenClementt/OpenKDS | 11 | 2023-03-23 | GPL-3.0 | Node.js + EJS |

## Notable patterns

- **Order ticket lifecycle**: `new → preparing → ready → served → bumped`.
  Status changes carry timestamps; time-in-stage analytics are core.
- **Course bucketing**: appetizers / mains / desserts shown on separate screens
  or color-banded.
- **Item modifiers visible inline**: "Burger — no onions, extra cheese".
- **Bump bar**: cook taps to mark ready; ticket slides off the screen.

## Common data models

- `OrderTicket` (id, table_or_order_id, opened_at, course, station, status)
- `TicketItem` (ticket_id, menu_item_name, qty, modifiers, notes, status, started_at, ready_at)
- `Station` (grill | fryer | salad | bar | dessert) — routes items to the right screen
- `BumpLog` (ticket_id, item_id, by_user, at) — audit / analytics

## Why none of these are a great fork target

- All couple tightly to a parent POS (URY Mosaic → ERPNext; CampusBites → its own POS).
- None support **Telegram as the KDS** (the user wants the cook to use a phone).
- All assume kitchen hardware (mounted screens) rather than a phone in a pocket.

## Recommendation

For our app, the **Telegram bot IS the KDS**. The cook gets:
- A daily menu message each morning (with stock counts)
- A `Bump <order_item_id>` command when an item is plated
- Auto-decrement of stock on bump
- An end-of-day report: sold vs wasted, leftovers for tomorrow's planning

See [../features/03-kitchen-stock-tracker.md](../features/03-kitchen-stock-tracker.md).