# Feature 02 — Order Taking (Dining/Service Side)

## Goal

A waiter at a table can browse today's available menu, add items to the table's
order, fire them to the kitchen, and track which items are still being prepared
vs. ready to serve.

## Scope

**In scope (v1):**
- Browse menu by category.
- Add item to a `Visit` (one tap = one quantity).
- Add notes per item ("no onions", "allergic to nuts").
- Mark item status (`new → preparing → ready → served`) — kitchen bumps it.
- Send "fire course" trigger (e.g. send all mains now, hold desserts).

**Out of scope (v1):**
- Item modifiers UI (size, extras) — v1 menu is flat.
- Combo / set menus — later.
- Split-bill UI — bill is per-visit (paid by one tender or split into 2 payments).

## Description

After seating a party (feature 01), the waiter opens the table's order screen.
Left side: today's menu grouped by category. Right side: current items for this
visit with status pills. Tap an item on the left → adds with qty=1 to the right.
Tap an item on the right → cycle status (kitchen can also bump via Telegram).

## Data model

```
OrderItem  (id, visit_id, menu_item_id, qty, unit_price, course,
            status, notes, fired_at, ready_at, served_at)
```

Status lifecycle:
```
new ──(cook bumps on Telegram)──► preparing ──(cook bumps again)──► ready ──(waiter)──► served
                                                                                       │
                                                              cancelled ◄──(anytime)────┘
```

When an `OrderItem` moves to `preparing`, the kitchen gets a Telegram message.
When it moves to `ready`, the cook bumps again (or waiter gets a "ready!" alert
on their UI).

## Dependencies

- [01-table-management.md](01-table-management.md) — orders belong to a visit.
- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — selling an
  `is_prepared` item decrements a batch.

## Open questions

- Should the waiter app run on a tablet (big buttons, no keyboard) or a phone?
- Should the kitchen get one Telegram message per item, or one batched
  message per course fire?
- Multi-language menu? (Affects UI string handling.)

## Mock-up sketch (`index.html`)

```
┌────────────────────────────────────────────┐
│ Table 2 — party 4 (3 adults, 1 child)     │
├────────────────┬───────────────────────────┤
│ Menu (today)   │ Current order             │
│                │                           │
│ ▾ Mains        │ • Schnitzel     preparing │
│  Schnitzel 14€ │ • Fries         ready     │
│  Burger   12€  │ • Coke          new       │
│  Salad    9€   │ • Tiramisu      new       │
│                │                           │
│ ▾ Drinks       │ Subtotal: 39€             │
│  Coke      3€  │                           │
│  Wine      5€  │ [Fire mains] [Fire all]   │
│                │ [Bill] [Close visit]      │
└────────────────┴───────────────────────────┘
```