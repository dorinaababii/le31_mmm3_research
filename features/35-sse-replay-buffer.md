# Feature 35 — SSE Replay Buffer

## Goal

Make the SSE cook-channel (feature 23) refresh-safe: when the waiter's
browser tab reconnects (refresh, network blip, rolling uvicorn reload),
the connecting client replays the last few events from a 60-second
in-process ring buffer keyed on a monotonic event id, so the cook's screen
does not go blank at the worst moment of service.

## Scope

**In scope (v1 polish):**
- A monotonic event-id counter on the in-process broker added by feature 23
  (`backend/app/services/event_bus.py`).
- A 60-second ring buffer of the most recent ~256 events, keyed on event id.
- Honour the SSE `Last-Event-ID` header on reconnect: read the buffer from
  the requested id forward; if the id is older than the buffer's head, emit a
  synthetic `replay_overflow` event so the client knows to re-render from
  scratch instead of waiting for events that no longer exist.
- One small library: `backend/app/services/event_ring.py` (~120 LOC).
- Update `backend/app/routers/cook_stream.py` (from feature 23) to
  register the `Last-Event-ID` reader.

**Out of scope (v1):**
- Persisted event log (would duplicate the `StockEntry` ledger; charter
  §3.1 forbids silent duplication of stock state).
- Cross-process / multi-worker ring buffer sharing (LE31 v1 runs a single
  uvicorn process per charter §4.1; if/when LE31 grows multi-worker,
  feature 35 will need a Redis-backed ring or a sticky-session routing
  rule — recorded as a v2 polish).
- Authentication of the SSE channel (charter §3.2 forbids per-user auth in
  v1; the cook-screen pane is reachable by anyone who can open the page).
- Resume across uvicorn restarts (the ring buffer is in-process; a restart
  loses the ring, which is acceptable because uvicorn restarts happen
  during deploy windows, not during service).

## Description

Feature 23 (`sse-cook-channel.md`) ships a read-only SSE endpoint that
streams `ticket_new`, `ticket_done`, `stock_low`, `stock_soldout` events
to the cook screen. The endpoint is correct as designed, but its Open
Questions section currently records:

> Reconnect policy — `EventSource` auto-reconnects with last-event-id;
> we need to assign monotonically increasing event ids so a reconnect can
> replay the last few events from a 60-second ring buffer (out of scope
> for v1 — record as a v2 polish).

Today's daily research (2026-08-06) surfaced
[`ofershap/fastapi-resumable-stream`](https://github.com/ofershap/fastapi-resumable-stream)
(2026-08-06, Python, single-file, "Resumable SSE streams for FastAPI —
survive refresh, reconnects, and rolling deploys"). That peer is a
direct, MIT-licensed reference implementation of exactly the problem
feature 23 defers to v2. Reading it shifts the cost/value calculation:
the cost is ≤ 2 days of work and ~120 LOC of pure Python; the value is
that the cook's screen survives the one event that matters most during
service — the waiter's browser refreshing because the iPad ran out of
memory.

This feature ships that promotion. The implementation is small, the
dependencies are unchanged, and the append-only `StockEntry` invariant
is unaffected (events are derived from `StockEntry` commits, never the
other way around).

## Data model

No new tables. No new columns. The ring buffer lives entirely in
process memory; it is not persisted.

```
class EventRingBuffer:
    capacity: int = 256          # ~60 seconds at 4 events/sec
    ttl_seconds: float = 60.0
    events: Deque[(int, float, str, dict)]  # (event_id, ts, type, payload)
    next_id: int = 0
```

The ring is fed by `event_bus.publish()` (from feature 23) and drained
by `cook_stream.py` when a reconnect request carries a `Last-Event-ID`.

## Implementation

1. **Read `ofershap/fastapi-resumable-stream`** — confirm the approach
   matches the SSE Last-Event-ID protocol; check the licence is MIT.
2. **New file** `backend/app/services/event_ring.py`:
   - `EventRingBuffer` class with `append(event_type, payload) -> int`,
     `read_from(event_id) -> list[event]` (returns empty if the id is
     older than the buffer head, signalling `replay_overflow`), and a
     background async task that evicts entries older than
     `ttl_seconds`.
   - Wrap the existing `event_bus.publish()` to also call
     `ring.append()` so the ring stays in sync with the live stream.
3. **Update `backend/app/routers/cook_stream.py`**:
   - Read the `Last-Event-ID` header from the incoming request.
   - If present and ≥ ring head, drain `ring.read_from(id + 1)` and
     emit those events before the live stream starts.
   - If present and < ring head, emit one synthetic
     `{"type": "replay_overflow", "since": id}` event so the client
     re-renders from the current state.
4. **Update the cook-screen JS** in `index.html` (feature 23's pane):
   - `EventSource` already auto-sends `Last-Event-ID` on reconnect.
   - Handle the `replay_overflow` event type by re-rendering the
     pane from `/api/cook/snapshot` (a tiny read-only endpoint that
     returns the current "tickets waiting" + "low-stock" list — out of
     scope to build today but trivial to add; if it isn't built, the
     pane just clears on overflow which is acceptable for v1).
5. **Manual verification**:
   - `cd backend && uvicorn app.main:app --reload`
   - Open `/` in two browser tabs (cook + waiter).
   - Waiter seats a party, adds 3 order items → cook tab shows 3
     `ticket_new` events.
   - Refresh the cook tab → browser auto-sends `Last-Event-ID: 3`;
     cook tab re-receives the last 3 events within 200ms, screen
     state preserved.
   - Wait 90 seconds, refresh again → cook tab receives
     `replay_overflow`, pane clears (acceptable for v1; the snapshot
     endpoint is a v2 polish).

## Telegram interaction

None. This is a server-side polish on feature 23's SSE endpoint. No
new bot command, no new Telegram surface.

## Dependencies

- [23-sse-cook-channel.md](../features/23-sse-cook-channel.md) — the
  SSE endpoint, in-process broker, and cook-screen pane that this
  feature extends.
- `backend/requirements.txt` — FastAPI `>=0.141.0` and uvicorn
  `>=0.52.0` already pinned by features 25 and 27. No new dep.

## Open questions

- Ring capacity 256 vs. 512 — default 256 (~60 seconds at 4 events/sec
  is fine; bump to 512 if the operator wants 2 minutes of buffer).
- Ring TTL 60 seconds — is 60 enough? Default yes; bump via
  `config.py:SSE_REPLAY_TTL_S` if the operator wants 5 minutes.
- Should the synthetic `replay_overflow` event also include a
  `/api/cook/snapshot` URL? If yes, that endpoint needs to ship too;
  if no, the client clears the pane which is acceptable for v1.
- Cross-worker ring sharing — out of scope for v1 (single uvicorn
  process); recorded as v2 polish for when LE31 grows multi-worker.

## Why this matters

Without this feature, the cook's SSE screen goes blank every time the
waiter's browser refreshes (which happens during the busiest minute of
service). With this feature, the screen is refresh-safe, reconnect-safe,
and rolling-deploy-safe. The reference implementation is small, MIT, and
Python-only — there is no remaining reason to defer it to v2.
