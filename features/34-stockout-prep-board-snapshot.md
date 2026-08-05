# Feature 34 — Stockout Prep Board Snapshot

> **Priority**: P1 · **Effort**: S–M (≤4 days) · **Source**: brainstorm 2026-08-05
> (cross-section pick C) · **Bucket**: v2 owner-pains
> **One-line**: A single FastAPI route (`/prep/board`) returns a thermal-printer-
> friendly HTML page that auto-refreshes from the existing `CookChannel` SSE
> stream and renders the 80/20 stockout + prep list with a big *PREP NOW*
> badge for items at or below `reorder_point`.

## Goal

The LE31 cook doesn't need a "kitchen display system" — they need a
*printed* prep list that auto-refreshes when a 86 fires. Today's cook
surface is the Telegram bot (feature 04), which works well for one-off
events but does not give the cook a glanceable *wall* they can read in
two seconds between tickets. A second screen (kitchen tablet, wall
monitor) costs €300–800 and is overkill for ≤40 seats.

The fix is a single FastAPI route that returns a thermal-printer-grade
HTML page. The cook opens it on any laptop / phone in the kitchen, hits
`Ctrl+P`, and the same page renders on a €60 thermal receipt printer or
on a wall-mounted tablet. The page auto-refreshes from the existing
`CookChannel` SSE stream (feature 23), so when a `StockEntry` writes
"86 tiramisu" the page redraws.

Inspired by HN no-build-htmx cluster (objectIDs 44774780 *Team Timezone
Wall — 100% offline, single file*, 44723744 *Interactive Data Viz*,
44592468 *templUI Pro*) — three threads in the 30-day window that
explicitly share the *single-file, glanceable, print-grade* pattern.
Translated to LE31, the cook needs a print-grade static surface, not an
SPA.

## Scope

**In scope (v2 owner-pains):**
- A new route `GET /prep/board` in a new router
  `backend/app/routers/prep_board.py`. Returns the new
  `templates/prep_board.html` page.
- A new `GET /api/prep/board/state` endpoint that returns the JSON
  payload: list of items with `qty_remaining`, `par_level`,
  `reorder_point`, and a derived `prep_now` boolean.
- A new template `backend/app/templates/prep_board.html` — minimal
  Jinja2 page. One big block per item. Subscribes to `CookChannel` SSE.
  Reuses the print-stylesheet from feature 32 (shared
  `static/css/print-prep.css`).
- One new file `backend/app/services/prep_board.py` — composes the
  state payload from existing `StockEntry` + `Batch` + `MenuItem` +
  `reorder_point` queries. No new tables.
- Reuses `CookChannel` SSE (feature 23) and the
  `reorder_point` / `par_level` columns (feature 26).

**Out of scope (v2 owner-pains):**
- Order counts, tip totals, manager KPIs — those live on the manager
  dashboard (feature 06).
- Multi-page board (split by station) — single page in v1; per-station
  split is a v2-AI polish.
- Drag-to-reorder — fixed order (by `reorder_point` desc, then by name).
- Voice readout — out of scope, would be v2-AI.
- Customer-facing prep board — privacy invariant forbids the cook's prep
  data crossing to the customer surface; that's the QR customer menu
  (feature 11) territory.

## Description

The page is intentionally single-screen:

```
/prep/board
  ├─ /api/prep/board/state  (initial render)
  └─ CookChannel SSE  (live updates)
       └─ on each event:
            ├─ recompute prep_now flags
            └─ HTMX swap the relevant <li> blocks
```

The print-stylesheet (`@media print`) makes the page fit a 80mm thermal
receipt printer: monospace font, no background colors, no JS, single
column. On screen it adds a big *PREP NOW* badge for items at or below
`reorder_point`.

## Data model

No new tables. Reuses:

```
MenuItem (existing)         — name, category, is_prepared
Batch (existing)            — qty_start, qty_remaining, prepared_at
StockEntry (existing)       — append-only ledger, drives qty_remaining
reorder_point (existing,    — feature 26; per-menu-item threshold
             feature 26)
par_level (existing,        — feature 26; per-menu-item par
         feature 26)
```

Derived (computed on read in `services/prep_board.py`):

```
qty_remaining = SUM(stock_entry.qty_delta) per active_batch
prep_now      = qty_remaining <= reorder_point
sort          = reorder by prep_now DESC, then qty_remaining ASC
```

## Implementation

1. **Service**: `backend/app/services/prep_board.py` with
   `build_prep_board_state() -> list[PrepBoardItem]`. Joins `MenuItem`
   with active `Batch`es, sums `StockEntry.qty_delta`, joins
   `reorder_point` / `par_level` from feature 26, sorts per above.
2. **Router**: `backend/app/routers/prep_board.py` with:
   - `GET /prep/board` — renders the template.
   - `GET /api/prep/board/state` — returns the JSON payload.
3. **Template**: `backend/app/templates/prep_board.html` — Jinja2.
   Subscribes to `CookChannel` SSE (reuse the existing client in
   `static/js/cook_channel.js`). HTMX auto-swaps per-item blocks.
   Print-stylesheet included.
4. **Print stylesheet**: `static/css/print-prep.css` — shared with
   feature 32's owner PIN page. Defines the 80mm thermal layout (mono
   font, no JS, single column).
5. **Mount**: `app.include_router(prep_board.router)` in
   `backend/app/main.py`.
6. **Wire-up verification**: spin up `uvicorn app.main:app --reload`,
   navigate to `/prep/board` in a browser at 1280×800 (screen layout)
   and at print preview (80mm thermal layout). Confirm SSE updates
   trigger HTMX swaps when a `StockEntry` is written.

## Telegram interaction

**None.** This feature is web-only. The cook bot is unchanged; the prep
board is a passive glanceable surface, not a push surface.

## Dependencies

- **Hard**:
  - [feature 23 — sse-cook-channel](23-sse-cook-channel.md) — SSE stream.
  - [feature 26 — reorder-point-on-stockentry](26-reorder-point-on-stockentry.md) — threshold + par columns.
  - [feature 03 — kitchen-stock-tracker](03-kitchen-stock-tracker.md) — `StockEntry` append-only ledger.
- **Soft**:
  - [feature 32 — solo-operator-floor-pin](32-solo-operator-floor-pin.md) — shares the print-stylesheet.

## Open questions

1. **Auto-refresh interval**: SSE is event-driven, but if no events fire
   for 30+ minutes the cook might miss a manual change. Mitigation:
   fallback HTMX poll every 60s on top of SSE. Decide at code-review.
2. **Per-station split**: bar / kitchen / pastry — single page in v1 of
   this feature; per-station split in v2 once we see real kitchen
   topology.
3. **What counts as "active batch"?** Same as feature 03's FIFO rule:
   oldest `Batch` consumed first; a batch is active while
   `SUM(qty_delta) > 0` and `expires_at > now()`. Confirm at
   code-review.
4. **Do we hide items with `qty_remaining == 0`?** No — they should
   still show as *SOLD OUT* with a red badge, so the cook sees the 86
   status. Confirm at code-review.
5. **Print on auto-fire?**: should the page auto-print when an item
   hits `reorder_point`? No — `Ctrl+P` is manual. Auto-print burns
   paper and surprises the cook. Defer.

## Why this matters

Closes the gap between the existing live cook channel (feature 23,
Telegram-bot-only) and the operator-pain "I keep losing track of what's
at reorder" complaint in the research. Reuses every primitive that
already exists: `CookChannel` SSE, `StockEntry` ledger, `reorder_point` /
`par_level` from feature 26. ~150 lines + a CSS file. No new client, no
new infra, no new LE31 invariant violation.

Cross-section because: HN no-build-htmx threads (44774780, 44723744,
44592468) share the *single-file, glanceable, print-grade* pattern —
a surface the cook can put on the wall or print on a thermal printer
without buying another device. Translated to LE31, the cook doesn't
need a "kitchen display system" — they need a printed prep list that
auto-refreshes when a 86 fires.
