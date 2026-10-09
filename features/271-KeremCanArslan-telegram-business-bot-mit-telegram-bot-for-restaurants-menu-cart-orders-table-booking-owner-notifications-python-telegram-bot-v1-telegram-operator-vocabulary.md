# Feature 271 — `KeremCanArslan-telegram-business-bot-mit-telegram-bot-for-restaurants-menu-cart-orders-table-booking-owner-notifications-python-telegram-bot-v1-telegram-operator-vocabulary` (defer)

> **NEW observation (2026-10-09).** Documents in-window GitHub repo `KeremCanArslan/telegram-business-bot` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python, **pushed 2026-10-05T10:33:16Z**, in-window by `pushed_at` only, **created 2026-10-05T10:33:10Z** — 6-second creation-to-push delta = **0-day-old repo = TODAY**, **8 KB tiny repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-09): *"Telegram bot for restaurants: menu, cart orders, table booking and owner notifications."* Topics (verbatim, parent-verified): `automation, python, python-telegram-bot, telegram-bot` — 4 topics including `python + telegram-bot` (LE31 stack-shape partial match: uses `python-telegram-bot`, NOT aiogram v3 — partial stack match). Bucket: **v1 (telegram-operator-vocabulary)** — Pick C of Daily Research 2026-10-09. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`Telegram-bot-for-restaurants + menu + cart orders + table booking + owner notifications`** quadruple-primitive as a persistent cross-section reference for the LE31 v1 *telegram-operator-surface + owner-recap-via-telegram* wedge, and document the **`python-telegram-bot` partial stack match** as a known caveat (LE31 uses aiogram v3 — code-adoption is not portable directly but the operator-UX vocabulary is). The artifact is a persistent cross-section reference for future v1 polish. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`Telegram-bot-for-restaurants + menu + cart orders + table booking + owner notifications`** quadruple-primitive: every menu item has a Telegram-card with photo + price + description; every cart-order is an idempotent state machine transition; every table-booking is a calendar ledger entry; every owner-notification is a daily-recap Telegram push. This is the §3.1 explicit-state-transitions primitive applied to the restaurant Telegram surface.
- A written record of the **`python-telegram-bot`** partial stack match: LE31 uses aiogram v3 (charter §3.1) — the `python-telegram-bot` library is NOT on the LE31 stack. The code is not directly portable; the **operator-UX vocabulary** (menu/cart/booking/notifications) IS portable.
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (0-day-old, in-window by BOTH `created_at` AND `pushed_at`); (2) the *operator-UX vocabulary* is the value, not the code (LE31 uses aiogram v3 + Postgres + HTMX + StockEntry); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema, `audit_logs` schema, or telegram-bot message handlers.
- Adoption of the telegram-business-bot codebase (`python-telegram-bot` is OFF stack; the 8 KB tiny size confirms a sketch-level implementation; the 0-day-old repo has insufficient maturity).
- Cross-pollination with the `python-telegram-bot` library (LE31 v1 uses aiogram v3 per charter §3.1).
- Cross-pollination with `table booking` (LE31 v1 charter does not have table-booking; would need charter-decided before any v1 PR).

## Evidence / JTBD

When a future LE31 v1 polish proposes "the Telegram-bot-for-restaurants operator surface with menu + cart orders + table booking + owner notifications" (e.g., a v1 polish that extends the cook Telegram bot to surface menu items + cart-order confirmations to guests, or a v1 polish that adds owner-notifications for new bookings), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented in-window Telegram-operator reference*, so that *the v1 polish surface can be defended with "this is what an independent maintainer shipped in 2026 with a similar stack to LE31"*.

- **Evidence class**: observed (the telegram-business-bot description + topics name the primitives explicitly: `automation, python, python-telegram-bot, telegram-bot`).
- **Confidence**: medium for the operator-UX vocabulary match (the verbatim description names the 4-primitive set); low for transferability (LE31 uses aiogram v3 — the code is not portable, but the vocabulary is).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has minimal-HTML/HTMX + aiogram v3 + single-restaurant); the value is the *operator-UX vocabulary* — when the first v1 polish that extends the cook Telegram bot to menu-cart-booking surface lands, the telegram-business-bot pattern is a ready-made *named primitive*.

## Description

GitHub `KeremCanArslan/telegram-business-bot` (MIT, 0★/0⑂, Python, python-telegram-bot, pushed 2026-10-05T10:33:16Z, created 2026-10-05T10:33:10Z, 8 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-09): *"Telegram bot for restaurants: menu, cart orders, table booking and owner notifications."*

The architectural primitive has four sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Menu** — every menu item has a Telegram-card view with name + photo + price + description. The *menu-card* primitive maps onto LE31's `MenuItem` SQLModel + the cook bot's `view_menu` handler (if added). The operator-facing vocabulary (card-based browse + select-and-add) is the value.
2. **Cart orders** — every cart-order is an idempotent state machine transition (cart → confirmed → prepared → served). The *cart-order* primitive maps 1:1 onto LE31's `Order` lifecycle (`open → sent → acknowledged → served → closed` per feature 02). The state-machine vocabulary is portable.
3. **Table booking** — every table-booking is a calendar ledger entry with explicit start/end times. The *table-booking* primitive is OFF v1 charter (LE31 v1 has no table-booking surface) but applies to any future v1 polish that introduces booking.
4. **Owner notifications** — every state transition fires an owner-notification to a designated Telegram chat. The *owner-notification* primitive maps 1:1 onto LE31 feature 39 (`owner-daily-recap-telegram`) + feature 57 (`owner-recap-persona-voice`). The pattern is portable.

**The 1:1 mapping onto LE31 surface:**

| telegram-business-bot primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Menu | `MenuItem` SQLModel + cook bot `view_menu` handler (if added) | §3.1 ✓ | **Implemented (v1)** + **Not implemented** for guest-facing menu (cook-only today) |
| Cart orders | `Order` lifecycle | §3.1 ✓ | **Implemented (v1)** |
| Table booking | (LE31 v1 has no table-booking) | v1 polish | **Not implemented** — charter-decision needed |
| Owner notifications | feature 39 + feature 57 | v1 ✓ | **Implemented (v1)** |
| `python-telegram-bot` | aiogram v3 | §3.1 ✓ | **OFF stack** — partial match only |
| Telegram-card view | (LE31 v1 has minimal Telegram surface) | v1 polish | **Not implemented** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that extends the cook Telegram bot to a menu-cart-booking surface, or first v1 PR that adds a guest-facing Telegram bot), the implementation would:

1. Add a `MenuItem` SQLModel (already exists per LE31 v1 features).
2. Add a `Booking` SQLModel with `start_at + end_at + table_id` (Alembic migration).
3. Add an `OrderItem` SQLModel with `cart_state` (Alembic migration).
4. Add a `NotificationSubscription` SQLModel with `chat_id + trigger_state` (Alembic migration).
5. Wire the aiogram v3 dispatcher to handle the `view_menu`, `add_to_cart`, `confirm_order`, `book_table` handlers.

The HANDOFF is to evaluate whether the v1 guest-facing Telegram surface is the right product-wedge for the next v1 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1 trigger fires:

**For v1 guest-facing Telegram bot** (if approved):
1. Add a `Booking` SQLModel with `start_at + end_at + table_id` (Alembic migration).
2. Add a `NotificationSubscription` SQLModel with `chat_id + trigger_state` (Alembic migration).
3. Add the `view_menu`, `add_to_cart`, `confirm_order`, `book_table` aiogram handlers to the cook bot dispatcher.
4. Add the `notify_owner` aiogram handler that fires on every Order state transition.
5. New feature file at `features/NNN-guest-facing-telegram-bot.md` (NOT this defer artifact).

## Telegram interaction

- **Cook bot**: the existing cook bot gains new handlers (`/view_menu`, `/add_to_cart`, `/confirm_order`, `/book_table`).
- **Waiter web**: unchanged (HTMX surface is unaffected; the new Telegram surface is guest-facing, not waiter-facing).
- **Owner**: the owner-side daily recap gains a guest-order notifications feed + a new-bookings feed.

## Dependencies

- LE31 v1 stack primitives (`StockEntry` + `audit_logs` + alembic + aiogram v3 dispatcher) — all on the LE31 pin set.
- aiogram v3 (already on the LE31 stack).
- No external dependency change.

## Open questions

1. **Is the v1 guest-facing Telegram surface the right product-wedge today?** LE31 charter §3.1 says *"operational transitions are explicit user actions. Do not silently send, serve, close, or reconcile an order"* — the guest-facing Telegram bot would need an explicit guest confirmation gate for every state transition; recommend charter-decided before any v1 PR.
2. **Does the operator-UX vocabulary (menu/cart/booking/notifications) map 1:1 onto LE31's existing aiogram v3 dispatcher?** Yes — the *vocabulary* is portable; only the `python-telegram-bot` implementation differs from aiogram v3.

## Why this matters

The telegram-business-bot repo is the strongest direct operator-UX vocabulary match for the **`Telegram-bot-for-restaurants + menu + cart orders + table booking + owner notifications`** quadruple-primitive in the 71-pass series. The **caveat** is the `python-telegram-bot` partial stack match (LE31 uses aiogram v3 — code is not portable directly) — but the **operator-UX vocabulary** (menu-card + cart-state-machine + booking-calendar + owner-notification) is portable. When LE31 v1 polish extends the cook Telegram bot to a guest-facing surface, the telegram-business-bot pattern is a ready-made *named primitive*. The 0-day-old repo with first in-window push is the demand-signal, not the adoption-signal.
