# POS Systems (Point of Sale)

Researched July 2026. Sources: GitHub REST API + raw README fetches.

## Top projects

| # | Project | Repo | ⭐ | Last push | License | Stack |
|---|---|---|---|---|---|---|
| 1 | **TastyIgniter** | https://github.com/tastyigniter/TastyIgniter | 3,670 | 2026-07-21 | MIT | PHP/Laravel + Twig, MySQL |
| 2 | **URY (ury-erp/ury)** | https://github.com/ury-erp/ury | 318 | 2026-07-15 | AGPL-3.0 | Vue + ERPNext/Frappe + Python |
| 3 | **evan361425/flutter-pos-system** | https://github.com/evan361425/flutter-pos-system | 488 | 2026-07-12 | Apache-2.0 | Dart/Flutter (mobile POS) |
| 4 | **RestoPOS** | https://github.com/faizaldevs/RestoPOS | 100 | 2025-03-10 | MIT | Laravel + Vue, multi-tenant SaaS |
| 5 | **Mausam5055/Restraunt-Management-System** | https://github.com/Mausam5055/Restraunt-Management-System | (small) | n/a | n/a | (older Java) |

## Notable patterns

- **Two-table layout**: `orders` (open tickets) and `order_items` (line items).
  Items carry `menu_item_id`, `qty`, `unit_price`, `modifiers`, `notes`.
- **Table state machine**: `free → seated → ordered → billed → paid → free`.
- **Modifier / variant model**: each menu item has a list of modifier groups
  (e.g. "size", "extras"); a line item carries the chosen modifier values.
- **Course sequencing**: appetizer/main/dessert sent to kitchen in waves.

## Common data models (synthesized from READMEs)

- `Menu` → `Category` → `MenuItem` (price, image, allergens, available_from/until)
- `Table` (id, seats, section, status)
- `Order` (table_id, server_id, opened_at, closed_at, status, total)
- `OrderItem` (order_id, menu_item_id, qty, unit_price, modifiers_json, notes, course, status)
- `Bill` (order_id, subtotal, tax, tip, discount, total_paid, payment_method)
- `User` (role: server | kitchen | manager | admin; pin_hash)

## Integration points

- **KDS / kitchen printer**: order_items with `status='new'` flow out as tickets
- **Payment terminal**: bill → charge → total_paid
- **Inventory**: line-item sale triggers `StockEntry(-qty)` against batch
- **CRM / loyalty**: customer_id on Order enables repeat-visit analytics

## Takeaway for the user's app

None of these fit the spec cleanly. TastyIgniter is the most mature but requires
Laravel + MySQL + a separate theme installation; overkill for one restaurant
and zero support for Telegram-driven kitchen.

**Recommendation**: do **not** fork a POS. Instead model the dining-service side
fresh in a thin Python/FastAPI app. See [../features/02-order-taking.md](../features/02-order-taking.md).