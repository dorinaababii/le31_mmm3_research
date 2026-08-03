# sse-cook-channel — HANDOFF

> **Slice for the coding agent.** Read this *and* `features/23-sse-cook-channel.md`
> before touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `23`
- Slug: `sse-cook-channel`
- Contract file: `features/23-sse-cook-channel.md`
- Bucket: v1 (thin slice inside feature 04 — extends, does not replace)
- Linear parent: HMM-16 (Research 2026-08-03 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "LE31 gate verdict". **Decision: build.** No failed checks.

Evidence precondition: **inferred** (FastAPI SSE fixes + competitor KDS
activity → cook wants a live screen). Confidence: **medium**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be
   sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the
research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/main.py                      # include the new router
backend/app/routers/cook_stream.py       # NEW — GET /api/cook/stream
backend/app/services/event_bus.py        # NEW — in-process pub/sub + after_commit hook
backend/app/services/__init__.py         # export event_bus
backend/app/models.py                    # touch OrderItem.status update path; no schema change
backend/app/requirements.txt             # pin fastapi>=0.141.0 (feature 25 prerequisite)
backend/README.md                        # document the SSE endpoint
index.html                               # NEW <section id="cook-screen"> + EventSource JS
```

## Endpoints and contracts added

- `GET /api/cook/stream` — returns `text/event-stream` (FastAPI
  `StreamingResponse`). Emits one JSON event per line, prefixed `data: `.
  - `ticket_new` — payload `{order_item_id, table_id, item_name, qty}`
  - `ticket_done` — payload `{order_item_id, table_id, served_at}`
  - `stock_low` — payload `{batch_id, menu_item_id, remaining}`
  - `stock_soldout` — payload `{menu_item_id, sold_out_at}`

No new tables, no new columns, no new migration.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions behave
as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -r requirements.txt` — confirm
   `fastapi>=0.141.0` resolves.
3. **Schema**: nothing to migrate; `init_db()` still works.
4. **Run**: `uvicorn app.main:app --reload`; open
   `http://localhost:8000/docs` and confirm `GET /api/cook/stream` appears.
5. **Smoke**: `curl -N http://localhost:8000/api/cook/stream` and confirm
   the heartbeat `:` line arrives within 15s.
6. **Two-tab test**: open `/` in two browser tabs (one as cook, one as
   waiter). Waiter seats a party, adds two `OrderItem` rows → cook tab
   shows `ticket_new` twice within 200ms.
7. **Cook-state test**: mark an item `served` → cook tab shows
   `ticket_done`. If it's a prepared item and the batch is now low, also
   show `stock_low`.
8. **Sold-out test**: sell the last prepared item → cook tab shows
   `stock_soldout`; the existing Telegram bot alert still fires (no
   double-alert regression).
9. **Reconnect test**: kill uvicorn mid-session and restart → cook tab
   reconnects via `EventSource` auto-retry within ~3s.
10. **Regression**: confirm existing flows (seat, order, serve, bill, tip)
    still work and that `StockEntry` rows are append-only.

## Rollback / feature-removal path

- Delete `backend/app/routers/cook_stream.py` and remove its `include_router`
  from `main.py`.
- Delete `backend/app/services/event_bus.py`.
- Revert the `index.html` cook-screen pane.
- No data migration, no data retention — SSE emits derived events only; no
  rows were added.

## What remains safe if removed

- No customer data, no historical state.
- The append-only `StockEntry` ledger is unaffected (SSE observes commits;
  it never writes).
- The explicit-state rule is unaffected (no `OrderItem` transition is
  automated by the SSE channel).

## Sign-off gap

External coding agent must mirror the five frozen identifiers (Feature ID,
slug, contract file path, bucket, Linear parent HMM-16) back to the
research-side Hermes before implementing. If any of these conflict with what
the agent sees locally, **stop and ask** — do not silently rename.