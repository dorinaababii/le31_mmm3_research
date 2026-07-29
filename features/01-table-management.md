# Feature 01 — Table Management

## Goal

Let staff see the floor at a glance, seat parties at tables, and track which
tables are open / seated / ordered / billed.

## Scope

**In scope (v1):**
- Visual table grid (rows = sections, columns = tables in section).
- States: `free`, `seated`, `ordered`, `billed`, `dirty`.
- Seat a party → opens a `Visit` (see feature 02).
- Mark table `dirty` after bill paid (manual or auto).
- Print / view floor plan from `index.html`.

**Out of scope (v1):**
- Drag-and-drop table layout editor (use a hard-coded floor map for now).
- Reservations (later).
- Waiter assignment queues (later).

## Description

The dining room has a small number of tables. The waiter app shows a colored
grid (green = free, yellow = seated, orange = ordered, red = billed, gray = dirty).
Tap a free table → "Seat party" → enter `party_size`, `adults`, `children` → confirm.
A `Visit` row is created with that data and `opened_at = now()`.

## Data model

```
Table          (id, label, section, seats, x, y)         -- x/y for floor map
Visit          (id, table_id, server_id, opened_at, closed_at,
                party_size, adults, children)
```

## Dependencies

- [02-order-taking.md](02-order-taking.md) — every seated visit becomes an order.
- [../research/01-pos-systems.md](../research/01-pos-systems.md) — TastyIgniter's
  table state machine as a reference.

## Open questions

- How many tables in total? (Affects UI density and whether we need pagination.)
- Are tables fixed-position (have x/y coords) or freely arranged?
- Sections? (e.g. "patio", "main hall", "bar") — yes/no?

## Mock-up sketch (`index.html`)

```
┌──────────────────────────────────────────┐
│  Floor — Friday 24 Jul                   │
├──────────────────────────────────────────┤
│                                          │
│   [T1 🟢]  [T2 🟡 party 4]  [T3 🔴 bill] │
│                                          │
│   [T4 ⚫ dirty]  [T5 🟢]  [T6 🟠 ord.] │
│                                          │
│   ─── patio ───                          │
│   [P1 🟢]  [P2 🟢]                       │
│                                          │
│  [+ Add table]                           │
└──────────────────────────────────────────┘
```