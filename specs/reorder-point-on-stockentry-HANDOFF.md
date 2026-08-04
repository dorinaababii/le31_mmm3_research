# reorder-point-on-stockentry — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/26-reorder-point-on-stockentry.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `26`
- Slug: `reorder-point-on-stockentry`
- Contract file: `features/26-reorder-point-on-stockentry.md`
- Bucket: v1 (schema + cook-bot summary; opt-in per item)
- Linear parent: HMM-20 (Research 2026-08-04 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "LE31 gate verdict". **Decision: build.** No failed
checks.

Evidence precondition: **inferred** (single in-window peer
`TidalBeast37/restaurant-inventory-rop`, no other signal). Confidence:
**medium**. Becomes an experiment (single menu item with ROP turned on)
rather than a system-wide rollout if no further evidence lands within two
weeks.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/main.py                            # include the new router
backend/app/models.py                          # add reorder_point + par_level columns to MenuItem
backend/app/routers/inventory_reorder.py       # NEW — GET /api/inventory/reorder
backend/app/bot/cook_bot.py                    # add /reorder + extend /end_of_day
backend/README.md                              # note the new endpoint
```

No new tables. No Alembic migration (charter §3.2 — `init_db()` for v1).

## Endpoints and contracts added

- `GET /api/inventory/reorder` — returns
  `[{menu_item_id, name, current_remaining, reorder_point, par_level}]`
  for items where `current_remaining <= reorder_point` (and
  `reorder_point IS NOT NULL`). Auth: same role check as `/api/tables`.
- Cook bot `/reorder` — plain text reply listing the same items.
- Cook bot `/end_of_day` — extended summary line: "N items need reorder"
  + names.

No writes to `StockEntry`. No new schema. No new dependency.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn pins from features 25 + 27 resolve.
3. **Schema**: nothing to migrate; `init_db()` adds the two nullable
   columns to `MenuItem` if absent.
4. **Run**: `uvicorn app.main:app --reload`; open
   `http://localhost:8000/docs` and confirm `GET
   /api/inventory/reorder` appears.
5. **Seed**: set `reorder_point = 2` on tiramisu directly via a small
   admin script or a temporary `/set_reorder` admin command (the latter
   is acceptable as a v1 verification aid; flag it for cleanup before
   the slice ships).
6. **Threshold test**: sell 6 of 8 tiramisu slices → remaining == 2 ==
   `reorder_point` → `/reorder` lists tiramisu; `/end_of_day` shows
   "1 item needs reorder: tiramisu".
7. **Below-threshold test**: sell one more → remaining == 1 <
   `reorder_point` → still listed.
8. **Opt-out test**: set `reorder_point = NULL` on tiramisu → item
   no longer appears in `/reorder` output (proves the feature is
   opt-in per item).
9. **No-ROP test**: items where `reorder_point` was never set → never
   appear (default off).
10. **Regression**: confirm existing flows (seat, order, serve, bill,
    tip) still work and that `StockEntry` rows remain append-only
    (no UPDATE/DELETE introduced by this slice).

## Rollback / feature-removal path

- Drop the two nullable columns from `MenuItem` in
  `backend/app/models.py`.
- Delete `backend/app/routers/inventory_reorder.py` and remove its
  `include_router` from `main.py`.
- Revert the `/reorder` command and the `/end_of_day` extension in
  `backend/app/bot/cook_bot.py`.
- No data migration, no data retention — ROP is a *read* over the
  ledger; no rows were added.

## What remains safe if removed

- No customer data, no historical state.
- The append-only `StockEntry` ledger is unaffected (ROP only reads
  commits; it never writes).
- The explicit-state rule is unaffected (no `OrderItem` transition is
  automated by ROP).
- The owner can leave `reorder_point = NULL` on all items and the
  system behaves exactly as before.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-20)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.