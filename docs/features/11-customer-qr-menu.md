# Feature 11 — QR-Code / Customer-Facing Digital Menu

> **Priority**: P1 · **Effort**: S–M (3–6 days) · **Source**: owner-pains research
> + adjacent OSS category A (QR / digital menus).
> **One-line**: Customer scans QR at table → sees the live menu (filtered by
> allergens/diet) → can place their own order or just browse.

## Goal

Let guests self-serve: see the menu, filter by their dietary needs, and
optionally order from their phone. The waiter no longer has to read out the
menu or run to the kitchen for special requests.

## Scope

**In scope (v1 of this feature):**
- Static QR codes generated per table (one QR per `Table`).
- Customer lands on `/menu/<table_id>` — a clean, mobile-first menu page.
- Menu shows: name, description, price, photo (if any), allergen badges,
  dietary badges, current stock (`5 left` / `sold out`).
- Filters: vegetarian, vegan, gluten-free, lactose-free, spicy.
- "Order to this table" button — drops items into the table's current visit.
- No customer identity required (no name, phone, account). v1 is anonymous.
- 100 % responsive — designed mobile-first.

**Out of scope:**
- Customer accounts / login.
- Saved payment methods (skip — order-to-table is paid by the existing visit).
- Per-customer order history.
- Multi-language (in v1; v2 with [feature 13](#)).

## Description

The cook (or manager) prints a QR code sticker for each table, sticks it on
the table. Guest scans → phone opens the menu for that specific table.
Filters work live (V / GF / LF badges), sold-out items show "Sold out" and
can't be ordered.

If the guest taps "Add to my order", the item is appended to the table's
current `Visit` (assuming one is open). The waiter sees it appear in their
order panel; they don't need to take the order verbally.

If no visit is open (rare — guest arrives before being seated), the customer
can browse but not order. They get a message: "Your server will be with you
shortly."

## Data model (no schema change required)

Uses existing `menu_item`, `batch`, `order_item`, `visit`. The QR code URL
is just `/menu/<table_id>`.

Optional addition: a `Table.qr_token` column for short, non-sequential
URLs (e.g. `/menu/T5-7af2`) so customers can't enumerate all tables.

## Implementation

1. **Generate QR** — `qrcode` Python lib; render on demand in the manager UI
   for printing; store PNG per table.
2. **New route** `/menu/<table_id_or_token>` in FastAPI — serves a static
   HTML page with the menu data injected.
3. **Customer menu page** — a separate `customer_menu.html` template with
   a different visual style (no admin chrome; warm and welcoming).
4. **Live updates** — server-side events or simple polling every 5s for
   stock changes (sold out / restocked).
5. **Order endpoint** `POST /api/visits/<id>/items` already exists (feature 02);
   reuse it with a `source='qr_menu'` flag on `order_item`.

## Security / abuse

- The QR token is a guessable URL. Mitigation: use a long random token, not
  the integer table id.
- Customers could spam-add items. Mitigation: rate-limit by IP; cap daily
  items per table; manager can disable ordering on a table ("order via server only").
- Customers can't see other tables' orders (they only see their own table's
  menu, not its order history).

## Customer menu mock-up

```
┌─────────────────────────────────────┐
│  🍽 Bistro                       🔍  │
│  Table 5 · Friday evening          │
│─────────────────────────────────────│
│  Filters: [V] [VG] [GF] [Spicy]   │
│─────────────────────────────────────│
│  Mains                              │
│  ─────                              │
│  🍖 Schnitzel        14 €  [+]    │
│     Breaded veal cutlet             │
│     🌾 🥛  · 18 left                │
│                                     │
│  🥗 Caesar Salad      9 €  SOLD OUT │
│     Romaine, anchovy, parmesan      │
│                                     │
│  🍔 Burger          12 €  [+]      │
│     Beef patty, brioche bun         │
│     🌾 🥛 🥚  · 15 left             │
│                                     │
│  Desserts                           │
│  ─────                              │
│  🍰 Tiramisu         6 €  [+]      │
│     Classic Italian                 │
│     🌾 🥛 🥚  · 6 left              │
│                                     │
│  Your order so far: 14 €           │
│  [Add to my order]                  │
└─────────────────────────────────────┘
```

## Dependencies

- [02-order-taking.md](02-order-taking.md) — order endpoint reused.
- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — live stock display.
- [10-allergen-tracking.md](10-allergen-tracking.md) — allergen/dietary badges.

## Open questions

- Should customers see prices? (Common practice: yes in EU, US often hides.)
- Should ordering be enabled by default, or opt-in per table?
- Should we include a "call the waiter" button? (Yes — easy add: a Telegram ping to manager.)
- Daily QR tokens (rotate at midnight) vs permanent? (Recommend permanent + per-table token.)

## Why this matters

- Reduces server workload (no menu reading for every new table).
- Speeds up orders during rush.
- Frees the waiter to focus on hospitality, not logistics.
- Differentiator: a **stock-aware** customer menu (shows "5 left") — most
  restaurant QR menus don't.