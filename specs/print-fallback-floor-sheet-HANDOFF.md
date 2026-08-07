# print-fallback-floor-sheet — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/45-print-fallback-floor-sheet.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `45`
- Slug: `print-fallback-floor-sheet`
- Contract file: `features/45-print-fallback-floor-sheet.md`
- Bucket: v2 owner-pains (read-only view layer, no new tables)
- Linear parent: HMM-49 (Brainstorm 2026-08-07 — daily, created by this run)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build.** (v2 owner-pains, ≤1 day.) No failed checks.

Evidence precondition: **observed** (3 in-window GitHub repos —
`Sreenivas-Sadhu-Prabhakara/shelftrack/slotone/slipbook` pushed **today**
2026-08-07 — share the no-account offline tiny-shop pattern).
Confidence: **high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/routers/floor_sheet.py                   # NEW: GET /floor/sheet + GET /api/floor/sheet/state
backend/app/services/floor_sheet.py                  # NEW: build_floor_sheet_state() function
backend/app/templates/floor_sheet.html               # NEW: minimal Jinja2 page (no auth, no JS framework)
backend/app/static/css/print-floor.css               # NEW: print-grade CSS (A4 / thermal friendly)
backend/app/static/js/floor-sheet.js                 # NEW: vanilla JS EventSource subscriber
backend/app/main.py                                  # NEW: include_router(floor_sheet.router)
backend/README.md                                    # note the new route + no-auth design
```

**No new pip dependencies. No new SQLModel tables. No new bot commands.**
This feature is a read-only view layer that composes existing data.

## Endpoints and contracts added

**Two new routes (no auth — stateless, no token, no cookie, no account):**

- `GET /floor/sheet` — returns the HTML page rendered by
  `templates/floor_sheet.html`. **No login form, no auth guard, no
  redirect.** Any browser can hit this URL.
- `GET /api/floor/sheet/state` — returns the JSON payload:
  `{tables: [...], prep_board: [...], voids_today: [...],
  generated_at: "<ISO timestamp>"}`. **No auth.** Used by the
  page's SSE-driven refresh.

**One new HTML template:**

```html
<!-- backend/app/templates/floor_sheet.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>LE31 — Floor Sheet</title>
  <link rel="stylesheet" href="/static/css/print-floor.css">
</head>
<body>
  <h1>LE31 — Floor Sheet — <span id="generated-at">…</span></h1>
  <section id="tables"><h2>Tables</h2><ul id="tables-list">…</ul></section>
  <section id="prep-board"><h2>Prep board</h2><ul id="prep-list">…</ul></section>
  <section id="voids"><h2>Voids today</h2><ul id="voids-list">…</ul></section>
  <script src="/static/js/floor-sheet.js"></script>
</body>
</html>
```

**One new CSS file:**

```css
/* backend/app/static/css/print-floor.css */
@media print {
  body { font-family: monospace; font-size: 14px; color: #000; background: #fff; }
  section { page-break-inside: avoid; }
  ul { list-style: none; padding: 0; }
  li { margin-bottom: 0.5em; }
}
@media screen {
  body { font-family: system-ui; font-size: 16px; max-width: 800px; margin: 2em auto; }
}
```

**One new JS file:**

```javascript
// backend/app/static/js/floor-sheet.js
const es = new EventSource('/api/cook/channel');
es.onmessage = async (event) => {
  // Re-fetch state on every SSE event
  const res = await fetch('/api/floor/sheet/state');
  const state = await res.json();
  render(state);
};

async function render(state) {
  document.getElementById('generated-at').textContent = state.generated_at;
  // Render tables, prep_board, voids_today sections
  // (full DOM update logic in this file)
}

// Initial fetch
(async () => {
  const res = await fetch('/api/floor/sheet/state');
  const state = await res.json();
  render(state);
})();
```

**One new service function:**

```python
# backend/app/services/floor_sheet.py
def build_floor_sheet_state() -> dict:
    """Compose the floor sheet state payload from existing data.

    Returns:
        {
            "tables": [
                {"label": "T1", "state": "free", "server": None, "opened_at": None, ...},
                {"label": "T2", "state": "seated", "server": "Anna", "opened_at": "2026-08-07T19:30:00+02:00", ...},
                ...
            ],
            "prep_board": [
                {"menu_item_name": "flour", "qty_remaining": 5.0, "reorder_point": 5.0, "status": "at_reorder"},
                ...
            ],
            "voids_today": [
                {"menu_item_name": "lamb", "rationale": "we ran out", "checked_at": "2026-08-07T19:15:00+02:00"},
                ...
            ],
            "generated_at": "<ISO timestamp Europe/Paris>",
        }
    """
```

Reuses:
- `Table` + `Visit` queries (feature 01) — for table states.
- `MenuItem` + `StockEntry` (with `rationale` from feature 37) — for
  prep-board and voids.
- The prep-board query from `services/prep_board.py` (feature 34) —
  for items at-or-below `reorder_point`.

No new SQLModel tables. No new migration.

## Verification

1. `build_floor_sheet_state()` unit tests with mocked `Table`,
   `Visit`, `MenuItem`, `StockEntry` rows — verify the four
   sections render with the right data.
2. `GET /floor/sheet` returns 200 with `Content-Type: text/html`
   in a test browser / curl without auth headers.
3. `GET /api/floor/sheet/state` returns 200 with `Content-Type:
   application/json` in a curl without auth headers.
4. SSE integration test: open `EventSource('/api/cook/channel')` in
   the page, fire a `StockEntry` write, assert the page re-fetches
   `/api/floor/sheet/state` within 1 second.
5. Print test: open `/floor/sheet` in a browser, hit `Ctrl+P`, verify
   the A4 print preview shows correct layout (80-column-wide, 14px
   font, black on white, no images).
6. No-auth guarantee: open `/floor/sheet` in an incognito / private
   browser window → page renders without any login form or redirect.
7. End-to-end observed: a 12-table service runs for 4 hours →
   owner opens `/floor/sheet` on a tablet → page renders all 12
   tables with correct states → SSE event fires → page re-renders
   within 1 second with updated state.
8. Existing tests still green.

## Rollback path

Remove the `floor_sheet` router from `main.py`. Delete the
`templates/floor_sheet.html`, `static/css/print-floor.css`, and
`static/js/floor-sheet.js` files. Delete the
`services/floor_sheet.py` module. No upstream feature is broken
by removing this — the route simply stops existing.

## Dependencies

- **No new pip dependencies.**
- **Required upstream features**:
  - feature 01 (`table-management`) — supplies the `Table` +
    `Visit` schema.
  - feature 23 (`sse-cook-channel`) — supplies the SSE endpoint
    `/api/cook/channel` that the page subscribes to.
  - feature 26 (`reorder-point-on-stockentry`) — supplies the
    `reorder_point` query for the prep-board section.
  - feature 32 (`solo-operator-floor-pin`) — supplies the
    `static/css/print-prep.css` stylesheet (reused; the new
    `print-floor.css` extends it).
  - feature 34 (`stockout-prep-board-snapshot`) — supplies the
    prep-board state query.
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column on `StockEntry` that feeds the voids
    section.
- **Required downstream features**: none.
