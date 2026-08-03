# Feature 23 — SSE Cook Channel

## Goal

Give the cook a live, read-only "tickets waiting" and "stock running low" surface
served from FastAPI's Server-Sent Events, alongside the existing aiogram Telegram
input channel — so the kitchen display becomes a real product surface (validated
by `satisfecho/pos` and `KamerrEzz/odoo-x-restopro` shipping a KDS) without
abandoning the append-only `StockEntry` invariant or the explicit-state rule.

## Scope

**In scope (v1):**
- New FastAPI endpoint `GET /api/cook/stream` that returns `text/event-stream`
  using `StreamingResponse`.
- Event types: `ticket_new`, `ticket_done`, `stock_low`, `stock_soldout`.
- Events are derived from existing `OrderItem`, `Batch`, and `StockEntry` rows;
  no new tables, no new columns.
- A small "Cook screen" pane in `index.html` that subscribes via `EventSource`
  and renders the four event types.
- Optional: a backpressure-safe in-process pub/sub keyed off existing SQLModel
  session commits (see Implementation).

**Out of scope (v1):**
- WebSockets (charter §3.2 explicitly excludes real-time push for v1 — SSE is
  the chosen substitute because FastAPI `0.140.13/0.140.12/0.141.1` made it
  first-class).
- New state fields on `OrderItem` or `Batch`.
- Replacing the aiogram bot — SSE is a read-only companion, aiogram remains the
  cook's input channel.
- Customer-facing SSE (charter §3.2 forbids it anyway).

## Description

The cook currently interacts with the system only via aiogram (`/start_today`,
`/sold_out`, `/leftover`). When service is busy, the cook has no passive view of
"what's waiting / what's running out" except by re-reading bot history or
asking the waiter. SSE adds a second surface that streams four event types
derived from existing data:

- `ticket_new` — fired when a new `OrderItem` row is committed and its parent
  `Visit` is in state `seated` or `ordered`.
- `ticket_done` — fired when an `OrderItem` transitions to `served` (the same
  transition that already writes `StockEntry(reason='sale')` for prepared
  items; see feature 03).
- `stock_low` — fired when `SUM(StockEntry.qty_delta)` for an active batch
  drops below a configurable threshold (default: 2 units). One-shot per batch
  per service, matching the existing "sold out" alert discipline in feature 03.
- `stock_soldout` — fired when `SUM(...)` reaches 0 (already covered by the
  existing Telegram alert in feature 03, but surfaced on the cook screen too).

The SSE endpoint is read-only and emits JSON payloads. It does not own any new
state — every event is derived from a row commit that already happened, so the
append-only ledger invariant and the explicit-state rule are unaffected.

## Data model

No new tables. No new columns.

```
OrderItem   (existing) — fires ticket_new on insert, ticket_done on status='served'
Batch       (existing) — fires stock_low when SUM(qty_delta) crosses threshold
StockEntry  (existing) — append-only ledger; SSE events derive from new commits
```

In-process pub/sub uses a small `asyncio.Queue` per connected client,
populated by a single subscriber hooked into the SQLModel `after_commit` event.

## Implementation

1. **Pre-requisite** — adopt FastAPI `>=0.141.0` in `backend/requirements.txt`
   (covered by feature 25 / Pick C of today's research). Verifies the SSE fixes
   in `0.140.13 / 0.140.12` and the new `app.frontend(check_dir='auto')`
   convenience.
2. **New router** `backend/app/routers/cook_stream.py`:
   - `GET /api/cook/stream` → `StreamingResponse(generator(), media_type='text/event-stream')`
   - Generator reads from `asyncio.Queue`, formats as `data: {json}\n\n`.
   - Heartbeat comment every 15s to keep proxies alive.
3. **In-process broker** `backend/app/services/event_bus.py`:
   - `subscribe() -> asyncio.Queue`
   - `publish(event_type: str, payload: dict)`
   - Hooked into SQLModel `event.listens_for(Session, 'after_commit')` — fires
     `ticket_new` on `OrderItem` insert, `ticket_done` on `OrderItem.status` update,
     `stock_low` / `stock_soldout` from `StockEntry` rows by checking the
     resulting `SUM(qty_delta)` per active batch.
4. **Wire into `app/main.py`** — include the router; ensure the SSE route is
   registered before any auth middleware that's added in v2 (v1 has no per-user
   auth, per charter §3.2).
5. **HTML pane** in `index.html`:
   - Add a `<section id="cook-screen">` hidden by default, toggleable from the
     top nav for the cook role.
   - JS `EventSource('/api/cook/stream')` with reconnect on close.
   - Render the four event types in a fixed-position bottom-right toast column.
6. **Manual verification**:
   - `cd backend && uvicorn app.main:app --reload`
   - Open `/` in two browser tabs (cook + waiter).
   - Waiter seats a party, adds two order items → cook tab shows `ticket_new`
     twice within 200ms.
   - Mark one item `served` → cook tab shows `ticket_done` and (if a prepared
     item) the corresponding `stock_low` if the batch is now below threshold.
   - Sell the last prepared item → cook tab shows `stock_soldout`; Telegram
     bot already shows the existing alert (no double-alert bug because the
     Telegram path is unchanged).

## Telegram interaction

**None added.** The aiogram bot remains the cook's *input* surface; the SSE
cook channel is a *read-only output*. The existing `/sold_out` and `/leftover`
flows are unchanged. No new bot command is introduced.

## Dependencies

- `backend/requirements.txt` — pin `fastapi>=0.141.0` (feature 25 prerequisite).
- [02-order-taking.md](../features/02-order-taking.md) — `OrderItem` insert is
  the source of `ticket_new` events.
- [03-kitchen-stock-tracker.md](../features/03-kitchen-stock-tracker.md) —
  `StockEntry` commits are the source of `stock_low` / `stock_soldout`; the
  append-only ledger rule is preserved.
- [04-menu-photo-bot.md](../features/04-menu-photo-bot.md) — defines the
  active-batch lifecycle that SSE events reference.
- [25-fastapi-frontend-dev-loop.md](../features/25-fastapi-frontend-dev-loop.md)
  — prerequisite for adopting `app.frontend(check_dir='auto')`.

## Open questions

- Threshold for `stock_low` — default 2 units per batch; expose as
  `config.py:COOK_LOW_STOCK_THRESHOLD` so owner-cook can tune per item.
- Heartbeat interval — 15s default; configurable via `COOK_SSE_HEARTBEAT_S`.
- Reconnect policy — `EventSource` auto-reconnects with last-event-id; we
  need to assign monotonically increasing event ids so a reconnect can replay
  the last few events from a 60-second ring buffer (out of scope for v1 —
  record as a v2 polish).
- Multi-restaurant tenancy is explicitly out (charter §3.2). If it becomes a
  v2 ask, the SSE channel needs `server_id` filtering.

## Why this matters

Two of the in-window Python POS competitors (`satisfecho/pos`,
`KamerrEzz/odoo-x-restopro`) ship a dedicated KDS as a first-class product
surface. LE31's research (`02-kitchen-display.md`, v2 feature 09 Kitchen Delay
Visibility) already flagged this as the validated active frontier. SSE is the
cheapest way to get a KDS-shaped surface inside the LE31 fixed stack (no new
dependency beyond `fastapi>=0.141.0`'s native `StreamingResponse`) without
violating the append-only ledger invariant, the explicit-state rule, or the
charter §3.2 prohibition on WebSockets. It also unlocks v2 feature 09 by
proving the streaming path before that feature commits to a fuller data
model.