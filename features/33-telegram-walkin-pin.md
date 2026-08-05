# Feature 33 — Telegram Walk-in PIN

> **Priority**: P2 · **Effort**: M (≤5 days) · **Source**: brainstorm 2026-08-05
> (cross-section pick B) · **Bucket**: new (owner-facing, additive)
> **One-line**: When a walk-in party is added to the queue and remains
> un-seated for >2 minutes, a Telegram push with *Seat me / Wait 10 /
> No-show* buttons is sent to the host/owner chat-id; tapping any button
> writes an append-only `WalkinEvent` row and resolves the queue entry.

## Goal

Stop losing walk-in revenue to paper-and-memory. The LE31 host is also the
owner during a rush; today, when a walk-in party arrives, the host adds
them to a paper list (or remembers them mentally) and tries to find a
table in their head. If the host gets pulled to the floor to seat a
different party, the walk-in walks out — and there's no record of the
missed revenue.

The fix is a Telegram push with three buttons. The host/owner carries
Telegram in their pocket; a one-tap resolution takes <5 seconds, even
with a tray in the other hand.

Inspired by GitHub `topic:telegram-bot` — 3,050 repos pushed in the
30-day window — confirming that the creator / gig / host / driver
economies consistently pick Telegram as the lowest-friction "owner gets
one decisive push and acts with one tap" surface. Translated to LE31,
the host/owner is a one-person ops team for walk-ins.

## Scope

**In scope (new, owner-facing, additive):**
- A new table `WalkinEvent` (see Data Model) — append-only ledger, same
  pattern as `StockEntry`. One row per state change.
- A new `POST /api/walkin/` route that:
  - Records a `WalkinEvent(reason='arrived', party_size, by_user_id)` row.
  - Starts a background timer (default 2 minutes, configurable) that sends
    the Telegram push if the entry is still un-seated.
- A new cook-bot webhook handler in `backend/app/bot/walkin_bot.py` that:
  - Receives Telegram `callback_query` events for the *Seat me / Wait 10 /
    No-show* inline buttons.
  - Writes a `WalkinEvent(reason='seat_me' | 'wait_10' | 'no_show', ...)`
    row.
  - Acknowledges with a one-line message ("Walk-in seated" or similar).
- A new chat-id allowlist `WALKIN_BOT_ALLOWED_USERS` in
  `backend/app/config.py` — separate from the cook bot's allowlist. Empty
  by default; owner/host opt-in.
- A new "Telegram walk-in bot" token in `.env` (can reuse the cook bot
  token if the owner prefers one bot; documented in `backend/README.md`).
- A new host-station UI panel that:
  - Lists active walk-ins (party_size, arrived_at, age).
  - Has a "Send PIN push now" button per walk-in (manual override).
- One new file `backend/app/routers/walkin.py`. Reuses the existing
  Telegram webhook primitive from feature 04 (cook bot).

**Out of scope (new):**
- Reservations, deposit handling — feature 13 territory.
- Customer-facing waitlist / no-show fee — privacy invariant forbids
  customer identity.
- SMS push — Telegram only in v1 of this feature.
- Multi-language button labels — single language in v1.

## Description

The Telegram flow:

```
Walk-in arrives at host station
  └─ Host clicks "+ Walk-in" in the panel, picks party size 1–8
       └─ POST /api/walkin/ → writes WalkinEvent('arrived')
            └─ Background timer (2 min default) starts
                 └─ on fire: POST to Telegram Bot API
                      message: "Walk-in 4p, 2m waiting"
                      inline_keyboard: [Seat me] [Wait 10] [No-show]
                 └─ on callback_query:
                      ├─ Seat me → WalkinEvent('seat_me') + resolves entry
                      ├─ Wait 10 → WalkinEvent('wait_10') + resets timer
                      └─ No-show → WalkinEvent('no_show') + resolves entry
```

The `WalkinEvent` table is the same shape as `StockEntry`: append-only,
no UPDATE, no DELETE. The current state of a walk-in is derived from the
last `WalkinEvent` per walk-in-id.

## Data model

New table (SQLModel):

```
WalkinEvent
  id              int PK
  walkin_id       uuid       # one walk-in party = one walkin_id
  reason          str        # 'arrived' | 'seat_me' | 'wait_10' | 'no_show'
  party_size      int        # 1..8
  by_user_id      int FK     # who logged it (host / manager)
  telegram_msg_id int nullable  # for dedupe on Telegram retries
  at              datetime   # UTC, tz-aware
```

Derived (computed on read): `current_state = WalkinEvent
  .where(walkin_id=X)
  .order_by(at.desc())
  .first()
  .reason`.

## Implementation

1. **Model**: add `WalkinEvent` class to `backend/app/models.py` (table=True).
2. **Router**: create `backend/app/routers/walkin.py` with:
   - `POST /api/walkin/` — body `{party_size, by_user_id}`,
     writes `WalkinEvent('arrived')`, starts the background timer
     (asyncio task in `app.main.lifespan`).
   - `GET /api/walkin/active` — returns the live list (joins latest event
     per walkin_id).
   - `POST /api/walkin/<id>/seat` — manual host-station override, writes
     `WalkinEvent('seat_me')`.
3. **Bot webhook**: add inline button handler in
   `backend/app/bot/walkin_bot.py` (or extend existing `cook_bot.py` if
   sharing the token). On callback: write `WalkinEvent` row, answer the
   callback with a one-line ack.
4. **Config**: add `WALKIN_BOT_ALLOWED_USERS` (list[int]) and
   `WALKIN_PUSH_DELAY_SECONDS` (int, default 120) to
   `backend/app/config.py`.
5. **Mount**: `app.include_router(walkin.router)` in `backend/app/main.py`.
6. **Host UI panel**: extend `templates/_host_panel.html` with a
   walk-in list (HTMX-driven). Add a "Send push now" button per row that
   posts to `/api/walkin/<id>/push` (skips the timer).
7. **Append-only hook**: same hook pattern used for `StockEntry` (see
   `backend/app/services/stock_audit.py` or equivalent) — verify no
   code path does `UPDATE` or `DELETE` on `WalkinEvent`.
8. **Wire-up verification**: start bot, simulate a walk-in via
   `curl -X POST /api/walkin/ -d '{"party_size": 4}'`, confirm Telegram
   message arrives in the test chat-id, tap *Seat me*, confirm
   `WalkinEvent` row written and active-list returns the seated state.

## Telegram interaction

**All Telegram interactions** for this feature:

- **Outbound**: one push per walk-in after `WALKIN_PUSH_DELAY_SECONDS`,
  with three inline buttons: *Seat me*, *Wait 10*, *No-show*.
- **Inbound**: callback_query events from those three buttons. Each is
  answered with a short ack (no further bot interaction).
- **Auth**: chat-id must be in `WALKIN_BOT_ALLOWED_USERS`. Unknown
  chat-ids are silently dropped (same pattern as feature 04).
- **Quiet hours**: respect `config.QUIET_HOURS_START` /
  `QUIET_HOURS_END` (already exists for the cook bot) — during quiet
  hours, the push is suppressed and the walk-in only appears on the host
  panel.

## Dependencies

- **Hard**:
  - Feature 04 — Telegram bot primitive (token, webhook, allowlist).
  - Feature 23 — SSE stream for live updates (host panel auto-refresh).
- **Soft**:
  - Feature 16 — supplier orders / receiving (uses the same append-only
    ledger pattern for `ExpectedDelivery` rows).

## Open questions

1. **Bot token reuse vs separate token**: simpler to share the cook bot
   token + a separate `WALKIN_BOT_ALLOWED_USERS` list; cleaner ops
   posture is a separate token. Decide at code-review.
2. **Walk-in dedupe**: if the host clicks "+ Walk-in" twice, do we
   create two walk-in rows or merge? Resolve: each click = a row
   (append-only invariant), but the host UI groups by party_size +
   arrived_at window (default: 30s).
3. **Push on a 1-top walk-in**: skip the push if the host is actively
   seating (heuristic: any `WalkinEvent('seat_me')` in the last 60s)?
   Defer — manual override button covers the case.
4. **Multi-language**: deferred; document the i18n boundary so a v2
   translation doesn't require restructuring.
5. **No-show analytics**: a daily count of `WalkinEvent('no_show')`
   rows could feed the demand forecast (feature 17). Defer; the data
   shape is already correct.

## Why this matters

Removes the most-lost revenue in any small-restaurant pilot: walk-in
no-shows. A typical 30-cover restaurant loses 2–4 walk-in covers per
lunch rush to paper-and-memory drift. At an average ticket of €18, that's
€36–72/day — €900–1,800/month per location.

The fix reuses primitives that already exist (Telegram webhook from
feature 04, append-only ledger pattern from `StockEntry`, SSE from
feature 23) and adds one new table. No new client, no new infra
dependency, no new LE31 invariant violation. Explicit-state rule is
preserved (each button press is an explicit action writing a row).

Cross-section because: the 3,050 in-window repos under
`topic:telegram-bot` show the creator / gig / host / driver economies
consistently pick Telegram as the lowest-friction owner surface.
Translated to LE31, the host/owner is a one-person ops team for
walk-ins — currently losing revenue to a paper-and-memory loop.

Experiment-only because: Telegram introduces one new external
dependency surface; ship on a single 30-minute lunch rush for a fixed
window before deciding to keep the feature on by default.
