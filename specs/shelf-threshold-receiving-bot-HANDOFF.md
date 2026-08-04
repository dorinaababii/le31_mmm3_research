# shelf-threshold-receiving-bot — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/28-shelf-threshold-receiving-bot.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `28`
- Slug: `shelf-threshold-receiving-bot`
- Contract file: `features/28-shelf-threshold-receiving-bot.md`
- Bucket: v2 owner-pains (cook-bot surface only; no new client)
- Linear parent: HMM-24 (Brainstorm 2026-08-04 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report. **Decision:
build (experiment).** No failed checks.

Evidence precondition: **observed** (one in-window peer
`Sreenivas-Sadhu-Prabhakara/shelftrack`, pushed today; topic `small-business`).
Confidence: **medium**. Becomes a 2-week experiment on a single supplier /
single menu item if no further evidence lands within two weeks.

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
backend/app/main.py                          # register cook_bot_receiving
backend/app/models.py                        # add StockEntry.reason; new ExpectedDelivery model
backend/app/bot/cook_bot.py                  # extend dispatcher with new handlers
backend/app/bot/cook_bot_receiving.py        # NEW — /expected + /received handlers
backend/README.md                            # note the new commands
```

No new dependencies. No Alembic migration (charter §3.2 — `init_db()` for
v1).

## Endpoints and contracts added

No new HTTP endpoints. Two new cook-bot commands:

- `/expected <supplier> <item>=<qty>...` — records an expected delivery.
- `/received` (followed by a photo) — OCRs the photo, writes `StockEntry`
  rows with `reason='receiving:<supplier>'`, returns reorder summary.

One new table:

```
ExpectedDelivery  (id, supplier_name, menu_item_id, expected_qty,
                   expected_at, fulfilled_at NULL)
```

One new nullable column:

```
StockEntry.reason TEXT NULL DEFAULT NULL
```

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn pins from features 25 + 27 resolve.
3. **Schema**: `init_db()` adds the `StockEntry.reason` column and
   creates the `ExpectedDelivery` table if absent.
4. **Run**: `uvicorn app.main:app --reload`; confirm cook bot starts
   and the existing commands still respond.
5. **Expected**: in Telegram (cook role), `/expected butcher ribeye=2
   1kg=1` → bot replies "expected 2 ribeye, 1 1kg-pack from butcher".
6. **Received**: send a photo of a slip reading "ribeye 2 / 1kg-pack 1"
   with the caption `/received` → bot replies with the reorder summary
   ("0 items need reorder" if feature 26 is enabled and `reorder_point`
   is unset, else the actual list).
7. **Ledger check**: open psql → `SELECT reason, qty_delta FROM
   stockentry ORDER BY id DESC LIMIT 2` → both rows have `reason =
   'receiving:butcher'`.
8. **Short delivery**: repeat with a photo showing "ribeye 1" → confirm
   `StockEntry.qty_delta = -1` and the ledger row's `reason` is set.
9. **OCR failure**: send a deliberately blurry photo with the caption
   `/received` → bot replies "could not read items; please retype
   quantities" and no `StockEntry` is written.
10. **Regression**: confirm existing flows (seat, order, serve, bill,
    tip) still work and that `StockEntry` rows from cooking/selling
    remain append-only.

## Rollback / feature-removal path

- Drop the `StockEntry.reason` column from `backend/app/models.py`.
- Drop the `ExpectedDelivery` table.
- Remove `cook_bot_receiving.py` and unregister its handlers from
  `cook_bot.py`.
- No data migration needed; no data retention — the `StockEntry` rows
  remain valid with `reason = NULL`.

## What remains safe if removed

- No customer data, no historical state.
- The append-only `StockEntry` ledger is unaffected (the receiving
  writes are themselves append-only `StockEntry` rows; nothing
  retroactively changes).
- The explicit-state rule is unaffected (the cook's `/received` photo
  is an explicit action).
- The owner can simply stop issuing `/expected` / `/received` and the
  system behaves exactly as before.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-24)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.