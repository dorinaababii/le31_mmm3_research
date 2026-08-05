# telegram-walkin-pin — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/33-telegram-walkin-pin.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `33`
- Slug: `telegram-walkin-pin`
- Contract file: `features/33-telegram-walkin-pin.md`
- Bucket: new (owner-facing, additive; no existing client replaced)
- Linear parent: HMM-32 (Brainstorm 2026-08-05 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: experiment** (start with a single 30-minute lunch rush).
No failed checks.

Evidence precondition: **inferred** (GitHub `topic:telegram-bot` — 3,050
repos pushed in the 30-day window — validates the pattern; no
LE31-specific peer in window). Confidence: **medium**.

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
backend/app/models.py                            # NEW: WalkinEvent SQLModel
backend/app/routers/walkin.py                    # NEW: POST /api/walkin/, GET /api/walkin/active, POST /api/walkin/<id>/seat
backend/app/bot/walkin_bot.py                    # NEW: callback_query handler (or extend cook_bot.py if sharing token)
backend/app/bot/cook_bot.py                      # dispatcher may need to route walkin callbacks here
backend/app/config.py                            # NEW: WALKIN_BOT_ALLOWED_USERS, WALKIN_PUSH_DELAY_SECONDS
backend/app/main.py                              # register walkin router; lifespan registers background timers
backend/app/templates/_host_panel.html           # NEW or extend: walk-in list with "+ Walk-in" button
backend/app/static/css/host-panel.css            # NEW: walk-in row styling
backend/README.md                                # note the new walk-in bot commands + allowlist env var
```

No new dependencies (Telegram Bot API is curl-friendly; reuse the existing
Telegram webhook primitive from feature 04). No Alembic migration (charter
§3.2 — `init_db()` for v1).

## Endpoints and contracts added

Three new routes:

- `POST /api/walkin/` — body `{party_size, by_user_id}`; writes a
  `WalkinEvent('arrived')` row; starts a background timer (default
  `WALKIN_PUSH_DELAY_SECONDS = 120`) that sends the Telegram push if the
  entry is still un-seated.
- `GET /api/walkin/active` — returns the live list: per walk-in-id, the
  latest `WalkinEvent` row joined with `WalkinEvent('arrived')` for
  party_size + arrived_at.
- `POST /api/walkin/<id>/seat` — manual host-station override; writes a
  `WalkinEvent('seat_me')` row.

One new table:

```
WalkinEvent
  id              int PK
  walkin_id       uuid       # one walk-in party = one walkin_id
  reason          str        # 'arrived' | 'seat_me' | 'wait_10' | 'no_show'
  party_size      int        # 1..8
  by_user_id      int FK
  telegram_msg_id int NULL   # for dedupe on Telegram retries
  at              datetime   # UTC, tz-aware
```

Append-only invariant: same hook pattern as `StockEntry` — verify no code
path does `UPDATE` or `DELETE` on `WalkinEvent`. Current state derived on
read from the latest row per `walkin_id`.

## Telegram interaction (outbound + inbound)

**Outbound** (bot → owner):

```
Walk-in 4p, 2m waiting
[ Seat me ] [ Wait 10 ] [ No-show ]
```

Sent via Telegram Bot API `sendMessage` with `reply_markup=inline_keyboard`.
Only fires when the background timer expires AND the entry is still
un-seated. Suppressed during `QUIET_HOURS_START`..`QUIET_HOURS_END`.

**Inbound** (owner → bot): `callback_query` events for the three buttons.
Each handler:

1. Writes a `WalkinEvent` row with the corresponding `reason`.
2. Answers the callback with a one-line ack ("Walk-in seated" / "Wait
   timer reset" / "Marked no-show") via Telegram Bot API
   `answerCallbackQuery`.
3. If reason is `wait_10`, resets the background timer for the same
   walk-in-id.

**Auth**: chat-id must be in `WALKIN_BOT_ALLOWED_USERS`. Unknown
chat-ids are silently dropped (same pattern as feature 04).

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn pins from features 25 + 27 resolve.
3. **Schema**: `init_db()` creates the `WalkinEvent` table if absent.
4. **Config**: set `WALKIN_BOT_ALLOWED_USERS` to the test chat-id.
   Set `WALKIN_PUSH_DELAY_SECONDS=10` (short for testing).
5. **Run**: `uvicorn app.main:app --reload`; confirm cook bot starts
   and the existing commands still respond.
6. **Walk-in creation**: `curl -X POST /api/walkin/ -d
   '{"party_size": 4, "by_user_id": 1}' -H "Content-Type: application/json"`
   → response confirms `walkin_id` and a `WalkinEvent('arrived')` row
   written.
7. **Telegram push**: after `WALKIN_PUSH_DELAY_SECONDS`, the bot sends
   a message to the test chat-id with the three inline buttons.
   Confirm the message arrives.
8. **Seat me**: tap *Seat me* in the Telegram client → `WalkinEvent
   ('seat_me')` row written; `GET /api/walkin/active` no longer lists
   this walk-in-id; bot answers the callback with "Walk-in seated".
9. **Wait 10**: repeat step 6; tap *Wait 10* → `WalkinEvent('wait_10')`
   row written; timer reset; the walk-in stays in `/active`; after
   the second delay, a fresh Telegram push fires.
10. **No-show**: tap *No-show* → `WalkinEvent('no_show')` row written;
    walk-in removed from `/active`; bot answers the callback with
    "Marked no-show".
11. **Auth**: send a callback from a chat-id NOT in
    `WALKIN_BOT_ALLOWED_USERS` → no `WalkinEvent` row written; bot
    silently drops the callback.
12. **Append-only check**: `SELECT * FROM walkinevent ORDER BY id` → all
    rows present, none deleted/updated. `grep -r "UPDATE walkinevent"
    backend/` → no matches. `grep -r "DELETE FROM walkinevent"
    backend/` → no matches.
13. **Regression**: confirm existing flows still work; confirm the
    append-only `StockEntry` ledger is unaffected.

## Rollback / feature-removal path

- Remove `walkin.router` from `backend/app/main.py`.
- Delete `backend/app/routers/walkin.py` and
  `backend/app/bot/walkin_bot.py`.
- Drop the `WalkinEvent` model from `backend/app/models.py`.
- Unset `WALKIN_BOT_ALLOWED_USERS` and `WALKIN_PUSH_DELAY_SECONDS` from
  `backend/app/config.py`.
- No data migration needed; no data retention — the `WalkinEvent` rows
  remain valid (read-only after rollback).

## What remains safe if removed

- No customer data, no historical state.
- The append-only `WalkinEvent` table is itself append-only, so the new
  table reinforces the invariant it relies on.
- The explicit-state rule is preserved (each Telegram button press is
  an explicit action writing a row).
- The privacy invariant holds (no customer identity is created — only
  party_size and arrival time).
- The host station panel still works (the walk-in list is a UI on top
  of `WalkinEvent`; the data shape is preserved across rollback).
- The owner can simply unset `WALKIN_BOT_ALLOWED_USERS` and the system
  behaves exactly as before — no pushes, no callbacks, no writes.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-32)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.
