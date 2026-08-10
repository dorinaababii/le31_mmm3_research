# zentra-offline-first-fb-pattern — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/53-zentra-offline-first-fb-pattern.md` before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `53`
- Slug: `zentra-offline-first-fb-pattern`
- Contract file: `features/53-zentra-offline-first-fb-pattern.md`
- Bucket: v2 owner-pains
- Linear parent: HMM-57 (Brainstorm 2026-08-10 — daily)
- Linear sub-issue: HMM-59 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "LE31 gate verdict per idea" → Pick B.
**Decision: build.** Evidence precondition: **observed** (anecdotal —
every small restaurant has wifi drops during Friday-night rush; the
cook's Telegram is more reliable than the restaurant's wifi because
Telegram runs over the cook's mobile data, but the FastAPI server is
on the restaurant's wifi and the waiter UI lives in the browser on the
same wifi). Confidence: **medium** for the wifi-drop frequency,
**low** for the *waiter-side offline-replay queue* as the right
solution. Today's `studionomadid/Zentra` is a cross-section pattern.

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

- `frontend/waiter/order-queue.js` (NEW) — the IndexedDB queue, the connection monitor, the flush logic, and the badge UI. ~150 lines of vanilla JS + IndexedDB.
- `frontend/waiter/order-queue.md` (NEW) — short doc explaining the algorithm and the runbook.
- `frontend/waiter/index.html` (existing) — wrap the "send to kitchen" button with the queue module; add the "queued (offline)" badge.
- `backend/app/routes/orders_replay.py` (NEW) — `POST /orders/replay` endpoint, idempotent on `client_uuid`.
- `backend/app/routes/replay_stats.py` (NEW) — `GET /replay/queue/stats` endpoint, owner-only.
- `backend/app/models/order.py` — add the `client_uuid` column (nullable VARCHAR(36)).
- `backend/app/migrations/versions/2026_08_10_add_client_uuid_to_order.py` (NEW) — Alembic migration adding the column + partial unique index.
- `backend/app/bot/commands/new_order.py` (existing) — add the `⏱ delayed <Xm Ys>` prefix when the order's `sent_at` is > 60 seconds in the past.
- `frontend/index.html` (existing owner mock-up) — add the "Replay queue" widget (60-second poll).
- `backend/tests/test_orders_replay.py` (NEW) — unit tests for the endpoint, the cook-bot prefix, the queue stats, and the idempotency rule.
- `frontend/tests/test_order_queue.js` (NEW) — E2E tests for the IndexedDB queue.
- `backend/app/main.py` — register the two new routes (2 lines).

## Endpoints and contracts added

**Two new HTTP endpoints:**

- `POST /orders/replay` — accepts `{orders: [{client_uuid, menu_item_id, qty, table_id, sent_at, client_cook_id}, ...]}`. Returns `{accepted: int, duplicates: int, conflicts: int}`. Cook-id allowlist check on the session cookie (same as existing `/orders`). Idempotent on `client_uuid` — duplicate posts return 409 (no duplicate `Order` row).
- `GET /replay/queue/stats` — returns `{pending_count: int, oldest_pending_at: str | null}`. Owner-only (same session cookie check as existing `/reports`).

## Telegram interaction

No new cook-bot commands. One change to the existing `new_order` cook-bot message:

- **Standard case** (gap ≤ 60s between `sent_at` and `now()`):
  `Table <n>: <qty>x <item1>, <qty>x <item2>, ...`
- **Delayed case** (gap > 60s):
  `⏱ delayed <Xm Ys>\nTable <n>: <qty>x <item1>, <qty>x <item2>, ...`

The cook sees the prefix and knows the order arrived late. The cook can still 86 the item if needed (the existing `/86` cook-bot command is unaffected).

No new waiter-side interaction. The waiter UI's "send to kitchen" button is unchanged from the waiter's perspective (only a "queued (offline)" badge appears below the button when there are pending orders).

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above.
2. **Migration**: `alembic upgrade head` on dev + staging — the
   `client_uuid` column and the partial unique index must be created
   without error.
3. **Unit tests**: `pytest backend/tests/test_orders_replay.py` —
   must pass all 8+ test cases (happy path + duplicate + conflict +
   idempotency + cook-bot prefix + queue stats).
4. **E2E test**: `npm test frontend/tests/test_order_queue.js` (or
   the existing `playwright` setup) — must pass all 4+ cases
   (offline → online → reconcile, FIFO order, debounce, idempotency
   on retry).
5. **Manual end-to-end**: in a browser, open the waiter UI, click
   "send to kitchen" with the FastAPI server stopped — the badge
   should show "queued (offline)". Restart the FastAPI server. The
   queue should flush automatically within 30 seconds. The cook bot
   should receive the message with the `⏱ delayed <Xm Ys>` prefix.
6. **Regression**: confirm features 02 (`order-taking`), 04
   (`menu-photo-bot`), 23 (`sse-cook-channel`), and 41
   (`telegram-msg-stock-update`) are unaffected by the new
   `client_uuid` column (the column is nullable; existing orders
   have `client_uuid=NULL`; the existing tests must still pass).

## Rollback / feature-removal path

- `alembic downgrade -1` — drops the `client_uuid` column and the
  partial unique index.
- Delete `frontend/waiter/order-queue.js`, `frontend/waiter/order-queue.md`,
  the two new endpoints, the migration, the test files.
- Revert the wrap on `frontend/waiter/index.html` (remove the queue
  module load + the badge).
- Revert the cook-bot prefix in `backend/app/bot/commands/new_order.py`.
- Revert the "Replay queue" widget from `frontend/index.html`.
- Remove the two new route registrations from `backend/app/main.py`.
- No data loss: the `client_uuid` column is additive; existing
  `Order` rows have `client_uuid=NULL` after rollback.
- No upstream feature broken by removing the queue.

## What remains safe if removed

- The "send to kitchen" button reverts to its pre-queue behavior
  (direct fetch to `/orders`, no IndexedDB queue, no badge).
- The cook bot reverts to its pre-prefix message format.
- The owner dashboard reverts to its pre-widget state.
- The privacy invariant is preserved (no guest identity, no LLM).
- No PII added; `client_uuid` is a uuid v4 generated on the
  waiter's tablet at click time.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-57)
back to the research-side Hermes before implementing. If they
conflict, **stop and ask** — do not silently rename.
