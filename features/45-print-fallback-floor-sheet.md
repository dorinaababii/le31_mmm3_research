# Feature 45 — Print Fallback Floor Sheet

> **Priority**: P2 · **Effort**: S (≤1 day) · **Source**: brainstorm 2026-08-07
> (cross-section pick C) · **Bucket**: v2 owner-pains
> **One-line**: A new `GET /floor/sheet` route returns a one-page
> printable HTML page that shows the current table states (from
> feature 01), the prep board (from feature 34), and the void-reason
> roll-up (from feature 37) — all in a single 80-column-wide
> print-grade layout suitable for an A4 thermal printer or a
> wall-mounted tablet in kiosk mode. The route requires no login and
> is **stateless** — no token, no cookie, no account — so the owner
> can hang a tablet by the espresso machine and the page is always
> there, refreshed every 5 seconds via the existing `CookChannel` SSE
> stream (feature 23).

## Goal

The LE31 owner's most-cited *mid-service* friction is "my phone is wet
and I need the floor state now" — currently unanswerable because
logging into the full web app costs ~15 seconds of attention and the
owner is mid-service. A printable no-account floor sheet hanging by
the espresso machine answers "table 5 paid?" in <3 seconds.

Inspired by today's brainstorm: GitHub `topic:small-business` cluster
of 3 same-author in-window repos pushed **today** (2026-08-07) —
`Sreenivas-Sadhu-Prabhakara/shelftrack` ("Photo-first stock list for a
tiny shop — 100% offline, nothing leaves your device"),
`Sreenivas-Sadhu-Prabhakara/slotone` ("A private, offline appointment
day-book for a one-person business. No accounts, no network"),
`Sreenivas-Sadhu-Prabhakara/slipbook` ("Free invoice & receipt maker,
no sign-up. Private, offline, nothing leaves your device."). All three
come from the indie-developer / micro-SaaS world — completely outside
hospitality — and share the *private, offline, nothing leaves your
device, no-account* primitive. Translated to LE31, this is the missing
surface for the busiest moments of service when the owner's hands are
wet and the phone is in the apron.

Distinct from feature 34 (`stockout-prep-board-snapshot`) because 34
is the cook-facing prep list, while this is the owner-facing floor
status. Distinct from feature 29 (`owner-no-account-live-floor-link`)
because 29 is a *live phone link with rotating token*, while this is
a *static no-account print-grade sheet* that any browser can hit at
any time.

## Evidence / JTBD

When the owner is mid-service and their phone is wet or in their apron,
the owner wants to know the current table states and prep board, but
struggles because logging into the full web app costs ~15 seconds of
attention and the owner is busy, so that a printable no-account floor
sheet hanging by the espresso machine answers "table 5 paid?" in
<3 seconds.

## Scope

**In scope (v2 owner-pains):**
- A new route `GET /floor/sheet` in a new router
  `backend/app/routers/floor_sheet.py`. Returns the new
  `templates/floor_sheet.html` page.
- A new route `GET /api/floor/sheet/state` (no auth) that returns
  the JSON payload: list of tables with their states (free / seated
  / ordered / billed / dirty — from feature 01), the prep-board
  summary (from feature 34), and the today's-voids summary with
  reasons (from feature 37).
- A new template `backend/app/templates/floor_sheet.html` — minimal
  Jinja2 page. **No login form, no auth guard, no cookie set, no
  token required.** Subscribes to `CookChannel` SSE (feature 23) for
  live updates; re-renders the body of the page every 5 seconds
  without a full reload. One big block per table. Reuses the
  print-stylesheet from feature 32 (shared `static/css/print-prep.css`).
- A new file `backend/app/services/floor_sheet.py` — composes the
  state payload from existing `Table`, `Visit`, `MenuItem`,
  `StockEntry` (with `rationale` from feature 37), and the
  prep-board query from feature 34. No new tables.
- A new file `backend/app/static/css/print-floor.css` — minimal
  print-grade CSS for 80-column-wide A4 / thermal-printer layouts.
  Black text on white, 14px base font, no images, no JS framework.
- A new file `backend/app/static/js/floor-sheet.js` — small vanilla
  JS that subscribes to `/api/cook/channel` (the existing SSE
  endpoint from feature 23) and re-fetches
  `/api/floor/sheet/state` on every event.

**Out of scope (v2 owner-pains):**
- Wall-display / kiosk-mode config (auto-fullscreen, auto-reload,
  screen-saver disable) — v1 is a regular browser tab the owner
  pins. Kiosk-mode is a v3 follow-up.
- Auth-protected variant — v1 is *deliberately* no-auth. If the
  restaurant needs a gated version, that is a follow-up feature.
- Mobile-native print dialog wiring — v1 uses the browser's
  built-in `Ctrl+P`. Native print dialog is a v3 follow-up.
- Order placement / voiding from the sheet — v1 is read-only.
  Two-way interaction is a v3 follow-up.

## User flow

**Owner — mid-service floor status glance:**

1. Owner glances at the tablet pinned by the espresso machine. The
   browser tab is at `https://le31.local/floor/sheet` (or whatever
   the deployment URL is).
2. The page renders:
   ```
   LE31 — Floor Sheet — 2026-08-07 19:42
   
   Tables (12)
   T1  🟢 free
   T2  🟡 seated — party 4 — opened 19:30 — server Anna
   T3  🟠 ordered — 3 items — opened 19:35 — server Marco
   T4  🔴 billed — €42.00 — server Anna
   T5  ⚫ dirty
   
   Prep board (3 at reorder point)
   • flour — at reorder (5 kg remaining)
   • eggs — below reorder (12 u remaining)
   • basil — at reorder (1 bunch remaining)
   
   Voids today (2)
   • lamb — 86 — "we ran out" — 19:15
   • focaccia — comp — "guest comp — birthday" — 20:30
   ```
3. The page refreshes every 5 seconds via SSE. New voids and prep
   status updates appear automatically.

**Owner — wet-hands, no-phone needed:**

1. Owner has both hands in dough. Glances at the wall tablet.
2. Reads "T2 🟡 seated — server Anna" and confirms Anna has table 2.
   No phone, no login, no touch.

**Cook / waiter — same view from the kitchen:**

1. Cook opens the same URL on the kitchen tablet. Same view, no
   auth, no account.
2. The cook uses this view as a *secondary* surface to the existing
   prep board (feature 34); the floor sheet shows tables + prep,
   the prep board shows prep only.

## Data model

**No new tables.** This feature is a read-only view layer that
composes existing data:

- `Table` + `Visit` (feature 01) — for table states.
- `MenuItem` — for prep-board labels.
- `StockEntry` with `rationale` (feature 37) — for today's voids.
- The prep-board query from feature 34 (`services/prep_board.py`) —
  for items at-or-below `reorder_point` (feature 26).

The state payload is computed on read in `services/floor_sheet.py`
(≤200 ms for a typical 12-table service).

## API / bot / UI contract

**API (FastAPI):**

- New `GET /floor/sheet` — **no auth**. Returns the HTML page
  rendered by `templates/floor_sheet.html`.
- New `GET /api/floor/sheet/state` — **no auth**. Returns the JSON
  payload: `{tables: [...], prep_board: [...], voids_today: [...],
  generated_at: "<ISO timestamp>"}`. Used by the page's SSE-driven
  refresh.
- The existing `GET /api/cook/channel` (from feature 23) is the
  SSE endpoint the page subscribes to for live updates.
- No new HTTP routes beyond the two above. No new POST / PATCH /
  DELETE endpoints.

**UI (HTML template):**

- One HTML file `backend/app/templates/floor_sheet.html` — minimal
  Jinja2. Subscribes to `/api/cook/channel` via vanilla JS EventSource.
  On every SSE event, re-fetches `/api/floor/sheet/state` and
  re-renders the body. No build step, no framework.
- One CSS file `backend/app/static/css/print-floor.css` — print-grade
  stylesheet. 80-column-wide A4 / thermal-printer friendly.
- One JS file `backend/app/static/js/floor-sheet.js` — vanilla JS
  EventSource subscriber + DOM update logic.
- No images, no fonts, no external dependencies.

**Bot:**

- No bot commands. This is a web-only surface.

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
    `static/css/print-prep.css` stylesheet (reused).
  - feature 34 (`stockout-prep-board-snapshot`) — supplies the
    prep-board state query.
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column on `StockEntry` that feeds the voids
    section.
- **Required downstream features**: none.

## Failure / recovery

- **SSE endpoint unavailable** — the page falls back to polling
  `/api/floor/sheet/state` every 30 seconds. The page still
  renders; updates are slower but functional.
- **State query fails (DB error / transient)** — the page renders
  the last known state with a small "stale — <HH:MM>" footer.
  No silent failure; the operator can see the staleness.
- **Tablet loses power / browser tab closes** — owner reopens
  the URL on next glance. No state to recover; the page is
  stateless.
- **Restaurant has no tablet** — owner can print the page via
  `Ctrl+P` once at start of service and re-print on demand.
  The print-grade CSS makes both A4 and thermal-printer
  outputs work.
- **No `PrepTask` rows for today (feature 43 not yet shipped)** —
  the prep-board section renders from feature 34's data only
  (items at-or-below `reorder_point`). The voids section renders
  from feature 37's data. Both are independent of feature 43.

## Definition of done

- [ ] `GET /floor/sheet` route shipped; returns the HTML page
      without auth.
- [ ] `GET /api/floor/sheet/state` endpoint shipped; returns the
      JSON payload without auth.
- [ ] `floor_sheet.html` template shipped; subscribes to
      `/api/cook/channel` SSE; re-renders on every event.
- [ ] `print-floor.css` shipped; renders correctly on A4 and
      thermal-printer paper.
- [ ] `floor-sheet.js` shipped; vanilla JS EventSource subscriber.
- [ ] End-to-end observed: a 12-table service runs for 4 hours →
      owner opens `/floor/sheet` on a tablet → page renders all
      12 tables with correct states → SSE event fires → page
      re-renders within 1 second with updated state.
- [ ] Print test: owner hits `Ctrl+P` on the page → A4 print
      preview shows correct layout, 80-column-wide, 14px font,
      black on white, no images.
- [ ] No-auth guarantee: opening `/floor/sheet` in a private /
      incognito browser window renders the page (no login form,
      no redirect, no token required).
- [ ] Existing tests still green.
- [ ] Manual acceptance: in a 7-day pilot, the owner references
      the floor sheet ≥5 times during service and finds the
      answer in <3 seconds each time.

## Open questions

- Should the page also show the per-cook adherence score (from
  feature 43) when available? Decision: no — v1 shows
  tables + prep + voids only. Adherence is a v3 follow-up.
- Should the page support a `/floor/sheet?table=<id>` deep-link
  for kitchen printer routing? Decision: no — v1 is the
  single-page view. Deep-link is a v3 follow-up.
- Should the page auto-reload on browser visibility change
  (when owner tabs back to it)? Decision: no — SSE keeps the
  page current. Browser visibility is a v3 follow-up.

## Why this matters

LE31's solo operator is also the cook, the manager, and the owner.
The operator's most-cited *mid-service* friction is "my phone is wet
and I need the floor state now" — currently unanswerable because
logging into the full web app costs ~15 seconds of attention and the
owner is busy.

The in-window peer cluster (`Sreenivas-Sadhu-Prabhakara/shelftrack/
slotone/slipbook`, all pushed **today** 2026-08-07, all by the same
single-author indie-developer) shares the *private, offline, nothing
leaves your device, no-account* primitive. Translated to LE31, this
is the missing surface for the busiest moments of service when the
owner's hands are wet and the phone is in the apron.

Tiny cost (one new route + one new API endpoint + one new template +
one new CSS file + one new JS file + one new service module), high
value (the operator's most-cited *mid-service* friction). Reuses the
existing SSE stream, the existing prep-board query, the existing
`rationale` column, and the existing print-stylesheet primitive.
