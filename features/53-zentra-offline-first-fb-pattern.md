# Feature 53 — Zentra Offline-First Waiter Replay Queue

> **Priority**: P2 · **Effort**: M (≤1.5 days) · **Source**: brainstorm 2026-08-10 (cross-section pick B) · **Bucket**: v2 owner-pains
> **One-line**: Add an **offline-first replay queue** to the waiter UI so that "send to kitchen" still works when the restaurant's wifi drops during a Friday-night rush — orders are buffered locally in IndexedDB on the waiter's tablet and flush to the cook bot automatically when the connection comes back, with a one-tap conflict resolution and a "delayed by X minutes" tag on each Telegram message.

## Goal

The existing waiter → cook surface assumes the FastAPI server is reachable (the waiter's tablet talks to FastAPI over the restaurant's wifi; the FastAPI server pushes to the cook bot via Telegram's webhook). What happens when the wifi drops? Today: the waiter's "send to kitchen" button fails silently, the order is lost, and the waiter falls back to telling the cook verbally. The cook then has to remember the order *and* remember to enter it into the system later, which never happens reliably. The operator loses revenue and the cook loses trust in the system.

`studionomadid/Zentra` (pushed 2026-08-10T06:58:48Z, 0★, "Offline-first POS app for small F&B businesses — built with Kotlin & Jetpack Compose. Keep selling, even without internet.") is the *offline-first small-F&B POS* primitive from the Kotlin/Compose world. The exact same problem — *what happens to orders when the wifi drops?* — is solved by buffering locally and reconciling on reconnect. Translated to LE31, this is the missing **waiter-side offline-replay queue** (server-side replay is already covered by the existing `sse-replay-buffer` HANDOFF in `specs/`; this is the *client-side* piece).

Distinct from feature 28 (`owner-no-account-live-floor-link`) because 28 is the *no-account floor-link* (the owner's ephemeral share link); this is the *offline-resilient order-send* (the waiter's local-first queue). Distinct from feature 23 (`sse-cook-channel`) because 23 is the *server-side* SSE channel for cook-bot events; this is the *client-side* queue that survives the SSE channel being unreachable.

## Evidence / JTBD

When the restaurant's wifi drops during a Friday-night rush and the waiter's tablet can't reach the FastAPI server, the waiter wants to keep sending orders to the kitchen without interruption, but currently the "send to kitchen" button fails silently (the SSE channel can't open), so that the waiter's "send to kitchen" button writes to a local IndexedDB queue when the FastAPI server is unreachable, and the queue flushes automatically when the connection comes back, with each Telegram message tagged "delayed by X minutes" so the cook knows the order arrived late and can re-86 anything that's already been 86'd by the verbal fallback.

## Scope

**In scope (v2):**
- One new JavaScript module: `frontend/waiter/order-queue.js` (NEW) — wraps the existing "send to kitchen" button (today's fetch to `/orders`) with an IndexedDB-backed queue. When the fetch fails (network error, 5xx, timeout), the order is written to IndexedDB and the UI shows a small "queued (offline)" badge. When the fetch succeeds, the queue is flushed in FIFO order (with a debounce to avoid stampeding the server when the connection comes back).
- One new FastAPI endpoint: `POST /orders/replay` (NEW) — accepts an array of buffered orders `{orders: [{client_uuid: str, menu_item_id: int, qty: int, table_id: int, sent_at: str, client_cook_id: str}, ...]}` and writes them to the existing `Order` + `StockEntry` tables. Returns `{accepted: int, duplicates: int, conflicts: int}` with per-order status. Conflict resolution: if a `client_uuid` is already in `Order`, the replay is a no-op for that item (idempotent — re-running the replay queue is safe).
- One new cook-bot tag: when an order arrives via `/orders/replay` and the `sent_at` is more than 60 seconds in the past, the cook-bot message gets a prefix `⏱ delayed <Xm Ys>` so the cook sees the delay. Existing orders (sent within 60 seconds) get no prefix.
- One new owner dashboard panel: a "Replay queue" widget on the existing `index.html` mock-up showing the current queue depth (read from a new `GET /replay/queue/stats` endpoint that returns the count of pending orders across all waiters — operator-visible, not cook-visible).
- One new unit test: `backend/tests/test_orders_replay.py` (NEW) — covers the endpoint (happy path + duplicate + conflict + idempotency), the cook-bot message prefix (delayed vs not), and the queue stats endpoint.
- One new E2E test: `frontend/tests/test_order_queue.js` (NEW) — covers the IndexedDB queue (offline → online → reconcile, FIFO order, debounce, idempotency on retry).
- One new short doc: `frontend/waiter/order-queue.md` (50 lines) — explains the algorithm, the IndexedDB schema, the conflict-resolution rule (first-write-wins by `client_uuid`), and the runbook for "what to do if the queue is stuck".

**Out of scope (v2):**
- No LLM dependency. The queue is pure JavaScript + IndexedDB.
- No automatic conflict resolution on simultaneous writes from two waiters' tablets to the same `table_id`. The first-write-wins rule (by `client_uuid`) covers the same-order-twice case; two different waiters ordering on the same table at the same time is an operator problem, not a queue problem.
- No offline-replay for *voids* or *payments*. Voids and payments stay online-only (the operator can always verbal-void and reconcile later; voids are reversible, unlike a missed order).
- No offline-replay for the cook bot's outbound messages. The cook's `/done` ack arrives via Telegram's webhook, which is on the cook's mobile data, not the restaurant's wifi. The cook side is *more* reliable than the waiter side, not less.
- No offline-replay for the owner's reports. The owner reads reports from the FastAPI server; if the wifi is down, the owner waits. (The owner can also read the existing `print-fallback-floor-sheet` from feature 45, which is a static HTML page that doesn't need the server.)
- No automatic retry with backoff. The queue flushes once when the connection comes back, then waits for the next button press.
- No new authentication on `/orders/replay`. The endpoint is operator-internal (no public access). The waiter tablet has the existing session cookie; the cook bot uses `TELEGRAM_ALLOWED_USERS`.

## Description

The offline-replay queue is the smallest primitive that turns "wifi down = orders lost" into "wifi down = orders buffered". The algorithm:

1. **Local queue (IndexedDB)**: when the waiter clicks "send to kitchen", the frontend first attempts the existing fetch to `/orders` with a 5-second timeout. If the fetch succeeds, no queue — the order is written to the server. If the fetch fails (network error, 5xx, timeout), the order is written to a local IndexedDB store `orderQueue` with the schema `{client_uuid: str (uuid v4 generated on click), menu_item_id: int, qty: int, table_id: int, sent_at: str (ISO-8601 UTC), client_cook_id: str, status: "pending" | "sending" | "acked" | "duplicate"}`.

2. **Connection monitor**: a small `navigator.onLine` + `fetch('/health')` heartbeat (every 30 seconds) tracks the connection state. When the state transitions from `offline` to `online`, the queue starts flushing.

3. **Flush**: in FIFO order (sorted by `sent_at`), the frontend POSTs each pending order to `/orders/replay`. The server is idempotent on `client_uuid` — a duplicate post is a no-op. The frontend marks each order `acked` on a 2xx response or `duplicate` on a 409 (the server already has it). The batch is debounced (one flush per 2 seconds) to avoid stampeding the server when the connection comes back.

4. **Cook-bot prefix**: when the cook bot fires the existing "new order" Telegram message, the bot checks the order's `sent_at` vs `now()`. If the gap is > 60 seconds, the message gets a `⏱ delayed <Xm Ys>` prefix. The cook sees "⏱ delayed 2m 13s — table 5: 2x lasagna, 1x salad" and knows the order arrived late. The cook can still 86 the item if it's already been verbally-ordered by the waiter in the meantime.

5. **Owner visibility**: a small widget on the existing `index.html` mock-up polls `GET /replay/queue/stats` (every 60 seconds) and shows the current queue depth across all waiters. The widget is operator-visible only (the cook doesn't see it).

The IndexedDB queue is invisible to the waiter — the "send to kitchen" button still says "send to kitchen" and still shows the existing spinner. The only difference is a small "queued (offline)" badge that appears below the button when there are pending orders, and the badge disappears when the queue is flushed.

## Data model

```sql
-- No new SQL tables. Reuses the existing `Order` and `StockEntry` tables.
-- The `client_uuid` field is added to `Order` for idempotency:
ALTER TABLE "order" ADD COLUMN client_uuid VARCHAR(36);
CREATE UNIQUE INDEX ix_order_client_uuid ON "order" (client_uuid) WHERE client_uuid IS NOT NULL;
```

The `client_uuid` is a uuid v4 generated on the waiter's tablet at click time. The unique index makes the replay idempotent — the server returns 409 on a duplicate post. The nullable column is backward-compatible with existing orders (which have `client_uuid=NULL`).

```javascript
// IndexedDB schema (frontend/waiter/order-queue.js)
{
  name: "orderQueue",
  keyPath: "client_uuid",
  autoIncrement: false,
  indexes: [
    { name: "by_status", keyPath: ["status", "sent_at"] },
    { name: "by_table", keyPath: ["table_id", "sent_at"] }
  ]
}
```

The compound index `[status, sent_at]` makes the FIFO flush query O(N) on the pending subset only.

## Implementation steps

1. **New file**: `frontend/waiter/order-queue.js` (NEW) — the IndexedDB queue, the connection monitor, the flush logic, and the badge UI. ~150 lines of vanilla JS + IndexedDB (no new dependencies; the existing `index.html` mock-up includes the necessary browser APIs).
2. **New file**: `frontend/waiter/order-queue.md` (NEW) — short doc explaining the algorithm, the IndexedDB schema, the conflict-resolution rule, and the runbook.
3. **Refactor**: `frontend/waiter/index.html` (existing) — wrap the "send to kitchen" button with the queue module; add the "queued (offline)" badge.
4. **New endpoint**: `backend/app/routes/orders_replay.py` (NEW) — `POST /orders/replay` accepting `{orders: [...]}` and returning `{accepted, duplicates, conflicts}`. Cook-id allowlist check on the session cookie (same as existing `/orders`).
5. **New endpoint**: `backend/app/routes/replay_stats.py` (NEW) — `GET /replay/queue/stats` returning `{pending_count: int, oldest_pending_at: str | null}`. Owner-only (same session cookie check as existing `/reports`).
6. **Refactor**: `backend/app/models/order.py` — add the `client_uuid` column (nullable VARCHAR(36)).
7. **New migration**: `backend/app/migrations/versions/2026_08_10_add_client_uuid_to_order.py` (NEW) — Alembic migration adding the `client_uuid` column and the partial unique index.
8. **Refactor**: `backend/app/bot/commands/new_order.py` (existing) — add the `⏱ delayed <Xm Ys>` prefix when the order's `sent_at` is more than 60 seconds in the past.
9. **Refactor**: `frontend/index.html` (existing owner mock-up) — add the "Replay queue" widget (60-second poll).
10. **New file**: `backend/tests/test_orders_replay.py` (NEW) — unit tests for the endpoint, the cook-bot prefix, the queue stats, and the idempotency rule.
11. **New file**: `frontend/tests/test_order_queue.js` (NEW) — E2E tests for the IndexedDB queue (offline → online → reconcile, FIFO order, debounce, idempotency on retry). Uses the existing `playwright` setup if available; otherwise a stub.
12. **Wire-up**: register the new endpoints in `backend/app/main.py` (two routes).
13. **Verify**: `pytest backend/tests/test_orders_replay.py` passes; the E2E test passes (offline → online → cook bot sees the delayed prefix); the owner dashboard widget shows the queue depth.

## Telegram interaction

No new cook-bot commands. One change to an existing command:

- **`new_order` (cook-only, automatic)** — when the order arrives via `/orders/replay` and the gap between `sent_at` and `now()` is > 60 seconds, the message gets a prefix:
  - Standard case (gap ≤ 60s): `Table <n>: <qty>x <item1>, <qty>x <item2>, ...`
  - Delayed case (gap > 60s): `⏱ delayed <Xm Ys>\nTable <n>: <qty>x <item1>, <qty>x <item2>, ...`

The cook sees the prefix and knows the order arrived late. The cook can still 86 the item if needed (the existing `/86` cook-bot command is unaffected).

No new waiter-side interaction. The waiter UI's "send to kitchen" button is unchanged from the waiter's perspective.

## Dependencies

- Existing `sqlmodel` (already a dep).
- Existing `sqlalchemy` (already a dep).
- Existing `pydantic` v2 (already a dep).
- Existing `pytest` (already a dep).
- Existing `alembic` (already a dep).
- Existing `aiogram` v3 (already a dep).
- Browser-side `IndexedDB` (always available in the existing waiter UI's target browsers — Chrome, Safari, Firefox, Edge).
- Browser-side `navigator.onLine` (always available).
- **No new packages.**

## Failure / recovery

- **If the IndexedDB queue fills up** (browser storage quota, ~50 MB on most browsers; ~10k small orders): the queue evicts the oldest `acked` or `duplicate` entries first; if all entries are `pending`, the queue rejects new entries and the waiter sees a "queue full — please wait for reconnect" badge. The operator is notified via the dashboard widget ("Replay queue at capacity — 10000 pending orders").
- **If the IndexedDB queue is corrupted** (browser crash mid-write, schema mismatch after a menu update): the queue is wiped on schema mismatch (the IndexedDB `versionchange` event fires; the frontend re-creates the store). The operator is notified via the dashboard widget ("Replay queue reset — N orders lost on wipe"). The waiter is asked to re-send the in-flight orders verbally as a fallback.
- **If the server is reachable but rejects the replay** (operator de-provisioned the cook bot, or the menu was changed and the `menu_item_id` no longer exists): the server returns 422 for the specific item; the frontend marks that item `duplicate` (with the server's error message in the queue entry) and continues flushing the rest. The waiter sees the badge update to "1 order needs attention" and can re-send manually after fixing the menu mismatch.
- **If the queue is stuck** (the connection came back but the flush never started): the `navigator.onLine` event is flaky on some browsers; the 30-second heartbeat is the fallback. If the heartbeat says online but the flush never started, the waiter can click the "send to kitchen" button manually — the click handler detects the pending queue and triggers a flush.

## Definition of done

- The waiter UI's "send to kitchen" button writes to IndexedDB when the FastAPI server is unreachable.
- The queue flushes automatically when the connection comes back, in FIFO order, debounced at 2 seconds per batch.
- The cook bot tags late-arriving orders with `⏱ delayed <Xm Ys>` when the gap is > 60 seconds.
- The `/orders/replay` endpoint is idempotent on `client_uuid` (duplicate posts return 409, not a duplicate `Order` row).
- The owner dashboard shows the current queue depth (polled every 60 seconds).
- `pytest backend/tests/test_orders_replay.py` passes (8+ test cases).
- `frontend/tests/test_order_queue.js` passes (4+ E2E cases: offline → online → reconcile, FIFO, debounce, idempotency on retry).
- The `order-queue.md` doc is in the repo.
- The change is committed and pushed to `main`.

## Open questions

1. **Should the queue also buffer *edits* to existing orders (e.g. "table 5 changed from 2x lasagna to 1x lasagna")?** Lean: as a follow-up, not in this feature. Edits are rare compared to new orders; the verbal-edit fallback covers them. Defer to v3 if the operator reports it as a problem.
2. **Should the queue also buffer *voids*?** Lean: no — voids are reversible and the verbal-void fallback covers them. The operator can always reconcile voids later. Including voids in the queue would double the IndexedDB schema complexity for marginal value.
3. **Should the `client_uuid` be a uuid v4 or a shorter token?** Lean: uuid v4 (36 chars including hyphens). The unique index fits comfortably; the collision probability is negligible. A shorter token saves 30 bytes per order but adds operator confusion if two waiters' tablets somehow generate the same token.
4. **Should the connection monitor poll every 30 seconds, or use the `online` / `offline` window events directly?** Lean: both — the window events are immediate on most browsers; the 30-second heartbeat is a fallback for browsers where the events don't fire (rare, but happens). Both run; the heartbeat is just slower.
5. **Should the queue also surface a "delayed" badge in the waiter UI for orders the waiter already knows are delayed?** Lean: yes — the existing "sent to kitchen" timestamp on the table view can show a small clock icon if the order's `sent_at` is > 60 seconds old. This is a 5-line UI change; deferred to a UI polish pass.
6. **Should the queue stats endpoint also report per-table queue depth?** Lean: yes, but as a follow-up. The current endpoint reports total depth; per-table depth is useful for the operator to see which tables have queued orders. Deferred to a dashboard polish pass.

## Why this matters

LE31's existing moat is the **per-batch append-only `StockEntry` ledger paired with a Telegram cook surface** (feature 03 + 04). The cook side is *more* reliable than the waiter side (Telegram runs over the cook's mobile data, not the restaurant's wifi), but the waiter side has a *fragility* that the operator notices immediately when the wifi drops during a rush. Today's `Zentra` is the cross-section proof that the *offline-first + reconcile-on-reconnect* pattern is the canonical answer for a small F&B POS — and LE31 is *exactly* the small-F&B POS where this matters most.

The operational value is concrete: when the wifi drops during a Friday-night rush, the waiter keeps clicking "send to kitchen" and the orders keep flowing (just buffered locally). When the wifi comes back, the queue flushes automatically and the cook sees `⏱ delayed 2m 13s — table 5: 2x lasagna, 1x salad`. The cook knows the order is late, can 86 anything that's already been verbally-ordered, and the operator never loses an order.

This complements feature 23 (`sse-cook-channel`) which handles server-side cook-bot reconnects; the existing `sse-replay-buffer` HANDOFF which handles server-side event replay; and feature 28 (`owner-no-account-live-floor-link`) which extends the no-account philosophy to the offline mode. Together, the four features give the operator *server-side replay* (existing), *client-side replay* (this feature), *no-account floor link* (feature 28), and *the cook surface that always works* (feature 04). Four small primitives, one resilient order-send surface.
