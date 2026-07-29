# Feature 09 — Slow-Kitchen Visibility (Ticket-Time Tracking)

> **Priority**: P1 · **Effort**: M (5–8 days) · **Source of recommendation**: owner-pains
> research + our existing order timestamps.
> **One-line**: Tell waiters honestly "kitchen is X minutes behind" before guests ask.

## Why this is the top v2 feature

The owner-pains research showed: **"Slow kitchen / ticket time visibility"**
is among the most-requested features across Capterra, G2, and owner forums.
Restaurants that ship this save real money because:
- Servers stop guessing and over-promising ETA to guests.
- Managers stop firefighting — they see exceptions pushed to them.
- Kitchen gets feedback on its own pacing.

Best part for us: **we already have the data**. The order timestamps exist
in our `order_item` model (`fired_at`, `ready_at`, `served_at`). We just need
to compute rolling stats and surface them.

## Goal

Real-time visibility into kitchen performance:
- Per-item average prep time (by station, daypart, item).
- Traffic-light status on every active order: 🟢 on time · 🟡 watch · 🔴 delayed.
- "Kitchen is X minutes behind" banner on the waiter UI.
- Telegram alert when kitchen exceeds its own historical norm.

## Scope

**In scope (v1 of this feature):**
- Compute prep-time stats from existing `order_item` timestamps.
- Compute a "normal range" per item (rolling 14-day median + stddev).
- Add `kitchen_status` field to each open `order_item` in the API.
- Add a Telegram bot command `/kitchen_status` showing current state.
- Manager dashboard tile: "X items delayed, Y items on time".
- Cook sees aggregate delays via Telegram (per shift summary).

**Out of scope:**
- Computer-vision station load detection.
- Predictive delays (ML-based).
- Course pacing optimisation.
- Per-station displays (we keep the Telegram + waiter UI surfaces).

## Description

Each `order_item` already has `fired_at` (when sent to kitchen), `ready_at`
(when cook marked ready), and `served_at` (when waiter delivered). We compute
`prep_seconds = ready_at - fired_at` for served items.

Every 14 days we recompute per-item normal range:
- `normal_median = median(prep_seconds over last 14 days)`
- `normal_p95 = 95th percentile`
- `normal_max = max` (a hard ceiling — anything longer is an outlier)

For each open (not yet ready) `order_item`:
```
seconds_since_fired = now - fired_at
status = 'on_time'   if seconds_since_fired < normal_median
       | 'watch'     if normal_median ≤ seconds_since_fired < normal_p95
       | 'delayed'   if seconds_since_fired ≥ normal_p95
```

When a manager / waiter hits `/api/visits?status=open` (or the equivalent),
each visit's items carry this status. The waiter UI shows traffic-light pills.

## Data model (no schema change required)

We use existing `order_item` timestamps. Add one new table for computed stats
(so we don't recompute on every request):

```
KitchenItemStats
  menu_item_id    FK
  window_start    DATE       (e.g. rolling 14-day window start)
  window_end      DATE
  prep_median_sec INT
  prep_p95_sec    INT
  prep_max_sec    INT
  sample_size     INT
```

Recomputed nightly by a background job (apscheduler or cron).

## Implementation

1. **Add timestamps** to `OrderItem` lifecycle: set `fired_at` on `new → preparing`,
   `ready_at` on `preparing → ready`. (Already in our schema; just wire the
   transitions in the order router.)
2. **Background job** (`backend/app/services/kitchen_stats.py`):
   nightly SQL aggregate → upsert into `KitchenItemStats`.
3. **API enrichment**: `GET /api/visits?status=open` includes a `kitchen_status`
   field per item.
4. **Telegram command** in `cook_bot.py`: `/kitchen_status` returns a
   formatted summary of currently delayed items.
5. **Manager dashboard tile** on the Reports view (extend `index.html`).

## Dependencies

- [02-order-taking.md](02-order-taking.md) — needs `fired_at` / `ready_at` set on transitions.
- [06-guest-demographics.md](06-guest-demographics.md) — Reports router powers the tile.
- aiogram already in stack — no new deps.

## Open questions

- 14-day window or 30-day? (14-day adapts faster to seasonal menu changes.)
- Should the cook see *other cooks'* delays? (Probably yes — they shift change.)
- Should we alert via Telegram only when delayed, or also when "watch"?
- Do we need a station model? (For now, no — one kitchen.)

## Why this matters

This is the **cheapest high-impact** extension. No new external integrations,
no ML, no payment certification. Pure derived views over existing data.

In the owner-pains research, kitchen delays were called out as the
**#1 feature that saves owner-hours per week**.