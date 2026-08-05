# stockout-prep-board-snapshot — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/34-stockout-prep-board-snapshot.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `34`
- Slug: `stockout-prep-board-snapshot`
- Contract file: `features/34-stockout-prep-board-snapshot.md`
- Bucket: v2 owner-pains (web-only; no new client)
- Linear parent: HMM-32 (Brainstorm 2026-08-05 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: build.** No failed checks.

Evidence precondition: **inferred** (HN no-build-htmx cluster —
objectIDs 44774780 *Team Timezone Wall*, 44723744 *Interactive Data Viz*,
44592468 *templUI Pro* — share the pattern; 1,258 `topic:real-time` repos
in window validate SSE; no LE31-specific peer for thermal-print prep
specifically). Confidence: **medium**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/services/prep_board.py               # NEW: build_prep_board_state() joining MenuItem + active Batch + StockEntry + reorder_point/par_level
backend/app/routers/prep_board.py                # NEW: GET /prep/board, GET /api/prep/board/state
backend/app/templates/prep_board.html            # NEW: single-screen glanceable page with SSE subscribe + HTMX auto-swap
backend/app/static/css/print-prep.css            # NEW or extend (shared with feature 32): 80mm thermal receipt layout
backend/app/static/js/cook_channel.js            # reuse existing SSE client (from feature 23)
backend/app/main.py                              # register prep_board router
backend/README.md                                # note the new route + print stylesheet
```

No new dependencies (HTMX, Jinja2, FastAPI all already present).
No Alembic migration (no new tables). No new tables — reuses
`MenuItem`, `Batch`, `StockEntry`, and the `reorder_point` / `par_level`
columns added by feature 26.

## Endpoints and contracts added

Two new routes:

- `GET /prep/board` — renders `prep_board.html`. No auth required in
  v1 (kitchen-local network); add IP-allowlist or shared-secret header
  if exposed outside the kitchen.
- `GET /api/prep/board/state` — returns JSON: `{items: [{menu_item_id,
  name, qty_remaining, reorder_point, par_level, prep_now: bool,
  expires_at, last_event_at}]}`. Sorted by `prep_now DESC, qty_remaining
  ASC`.

No new tables. No new config fields.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn pins from features 25 + 27 resolve.
3. **Schema**: no schema changes; `init_db()` is a no-op for this
   feature.
4. **Run**: `uvicorn app.main:app --reload`; confirm the existing
   flows still respond.
5. **Initial render**: navigate to `http://localhost:8000/prep/board`
   in a browser at 1280×800 → page renders the 80/20 prep list with
   each item's `qty_remaining`, `par_level`, `reorder_point`. Items
   at or below `reorder_point` show a big *PREP NOW* badge.
6. **Print preview**: in the same browser, `Ctrl+P` → print preview
   shows the page on an 80mm thermal layout (monospace font, single
   column, no background colors).
7. **SSE update**: with the page open, write a `StockEntry(qty_delta =
   -1, reason='sale', ...)` row via the existing order-close flow →
   the page auto-refreshes the relevant item's `<li>` block within
   1s. The *PREP NOW* badge appears when `qty_remaining` drops to
   or below `reorder_point`.
8. **No events**: with the page open and no events firing for 60s,
   confirm the page remains stable (no auto-refresh storm; the SSE
   connection stays open).
9. **Sold-out display**: write a `StockEntry(reason='sold_out',
   qty_delta = -(remaining))` row → the page shows *SOLD OUT* with
   a red badge instead of disappearing.
10. **JSON contract**: `curl http://localhost:8000/api/prep/board/state`
    → JSON payload has the expected shape; sort order matches the
    contract.
11. **Regression**: confirm existing flows still work; confirm the
    append-only `StockEntry` ledger is unaffected.

## Rollback / feature-removal path

- Remove `prep_board.router` from `backend/app/main.py`.
- Delete `backend/app/routers/prep_board.py`,
  `backend/app/services/prep_board.py`, and
  `backend/app/templates/prep_board.html`.
- No data migration needed; no data retention — the page is a read-only
  view over existing tables.

## What remains safe if removed

- No customer data, no historical state.
- The append-only `StockEntry` ledger is unaffected (the prep board is
  a read-only view over `Batch` + `StockEntry`; never writes).
- The cook can simply stop opening `/prep/board` and the system behaves
  exactly as before. Feature 23 (`sse-cook-channel`) still serves the
  Telegram bot with the same live updates.
- No new client, no new infra, no new LE31 invariant violation.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-32)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.
