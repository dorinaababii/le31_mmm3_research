# Feature 24 — Visual Table Layout v2

## Goal

Upgrade the existing `index.html` floor grid (feature 01) into a true visual
layout — drag-to-reorder tables within a section, persistent section dividers
("patio", "main hall", "bar"), and a "waiter currently at" badge — so a busy
waiter can recognize the floor in 1 second instead of scanning a list.

## Scope

**In scope (v1):**
- Drag-to-reorder tables **within** a section at runtime (purely visual, not
  persisted — see Out of scope).
- Section dividers ("patio" / "main hall" / "bar") rendered as horizontal
  bands in the grid.
- A small badge on each table card showing the assigned waiter's initials
  (derived from `Visit.server_id` → `app_user.display_name`).
- Color rules preserved from feature 01: green = free, yellow = seated, orange =
  ordered, red = billed, gray = dirty.
- All changes live in `index.html` only; no backend changes, no new endpoints.

**Out of scope (v1):**
- Drag-and-drop table *editor* (admin-only layout authoring) — explicitly
  forbidden by charter §3.2.
- Persisting the runtime reorder across reloads — the layout is derived from
  `Table.x, Table.y` server-side; runtime drag is a display-only convenience.
- Real-time sync of drag actions across waiters — not a v1 concern.
- Adding new sections via UI — sections are configured in `backend/app/config.py`
  as a hard-coded list.

## Description

The current `index.html` mock-up renders tables in a fixed order. Feature 01's
contract is satisfied by this; feature 24 is the polish layer that makes the
grid feel native to a restaurant floor:

- The waiter opens `/` on a tablet, sees the floor.
- Section dividers ("patio", "main hall") separate the rows.
- Each table card is colored by its `Visit` state (existing logic) **plus** a
  small badge in the corner showing the initials of the assigned waiter (e.g.
  "JD" for Juan David — derived from `Visit.server_id`).
- During service the waiter can long-press a table card and drag it to a new
  spot **within the same section**; the move is local-only and resets on
  reload (acceptable because the grid is small and reordering is rare).
- A tap on a free table still opens the "Seat party" flow (feature 01
  behavior).

## Data model

No new tables. No new columns. Reuses:

```
Table       (existing) — id, label, section, seats, x, y
Visit       (existing) — server_id, status, opened_at, ...
app_user    (existing) — display_name (initials derived client-side)
```

## Implementation

1. **Section list** — add `SECTIONS = ["main", "patio", "bar"]` (or whatever
   the user has configured) to `backend/app/config.py`. Read by
   `/api/tables` and exposed in the existing floor endpoint.
2. **`/api/tables` extension** — return `sections: ["main", "patio", "bar"]`
   plus each table's `section`. No new endpoint needed.
3. **`index.html` rewrite of the floor grid**:
   - Replace the single `<div class="floor">` with one `<section class="floor-section">`
     per configured section.
   - Each table card stays a `<button class="table-card" data-id="...">` with
     the existing color states.
   - Add a `<span class="waiter-badge">` per card; populated client-side from
     `/api/visits/active` (existing endpoint) by joining on `table_id`.
   - Add a small drag handle (CSS `cursor: grab` on hover) and a tiny vanilla JS
     reorder using `dragstart` / `dragover` / `drop`. No external library.
4. **Manual verification**:
   - Open `/` on desktop and tablet.
   - Confirm section dividers render.
   - Confirm waiter badge appears on tables that have a `Visit` with a
     `server_id`.
   - Confirm drag-to-reorder within a section works and resets on reload.
   - Confirm a tap on a free table still opens the seat-party modal (regression).

## Telegram interaction

None. The cook screen is unrelated; this is purely a waiter-side polish.

## Dependencies

- [01-table-management.md](../features/01-table-management.md) — extends the
  existing grid; the `Table` schema is unchanged.
- [02-order-taking.md](../features/02-order-taking.md) — provides the active
  visit data the waiter badge reads.
- `backend/app/config.py` — new `SECTIONS` constant (one line).
- `backend/app/routers/tables.py` — extend `/api/tables` response to include
  `sections` list (already returning tables; just add a sibling key).

## Open questions

- How many sections does a real LE31 restaurant have? Default 3 (main / patio
  / bar). Configurable via `config.SECTIONS`.
- Is "waiter initials" the right badge or should it be a color per waiter
  (so a waiter can be colorblind-friendly identified)? Default initials; color
  is a v2 polish.
- Should the long-press reorder also work on touch devices? Default yes —
  pointer events handle both.
- Drag handle discoverability — a small "≡" icon vs. the whole card being
  draggable. Default: whole card on desktop, long-press handle on touch
  (detected via `matchMedia('(pointer: coarse)')`).

## Why this matters

The active frontier in the 2026-07-27..08-03 window includes `KamerrEzz/odoo-x-restopro`'s
`restopro_tables` (visual table management) and `Rajathtuesday/restaurant-pos`'s
KOT routing. Operators want a floor map, not a list — this was already noted in
`research/08-deep-dive-top-5.md`. Feature 24 turns the existing mock-up into
that floor map at near-zero cost (one config constant + one HTML/JS pass),
without violating the charter §3.2 prohibition on a v1 table-layout *editor*.
It's the highest perceived-polish-per-hour feature in today's research batch
and reuses the existing `/api/tables` endpoint, so it can ship independent of
features 23 and 25.