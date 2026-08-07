# Feature 44 — Tether Day Card Fold

> **Priority**: P2 · **Effort**: M (≤3 days) · **Source**: brainstorm 2026-08-07
> (cross-section pick B) · **Bucket**: v2 owner-pains
> **One-line**: A new `DayCard` and `DayCardLine` append-only SQLModel
> tables store a time-indexed memory of each service. During service a
> background task listens on the existing `CookChannel` SSE stream
> (feature 23) and appends a one-line summary every 5 minutes. At
> end-of-service the daily card is **folded**: per-5-minute detail is
> collapsed into a single 4-section body (covers, voids-with-reasons
> from feature 37, top 3 movers, prep adherence from feature 43). The
> owner can query any past service moment at any time via
> `/day [date]` or `/shift [time]` Telegram commands.

## Goal

The LE31 owner's second-most-cited follow-up question after service is
"what happened at <specific moment> in a past service?" — currently
unanswerable because the existing recap (feature 39) is a *single push
at end of day* with no time-indexed detail, and the manager dashboard
requires login + manual date navigation. A time-indexed per-shift
memory card that auto-folds raw detail at close gives the owner
`/day last-saturday` and `/shift 21:30 last-saturday` without leaving
Telegram.

Inspired by today's brainstorm: GitHub `topic:append-only` repo
`SsssssSynqa/tether-agent-runtime` (pushed 2026-08-05, **7★** — the
strongest in-window star count of the pass outside the volume-leaders,
"Give an API-only agent real continuity: live on Telegram and your
terminal with built-in layered memory (auto-folding + day/week cards)
and a local memory console"). The repo comes from the AI-agent /
developer-tools world — completely outside hospitality — and shares
the *auto-folding + day/week cards* layered memory primitive.
Translated to LE31, this is the missing layer between the live link
(feature 29 — pull, owner goes to it) and the end-of-day recap
(feature 39 — push at 23:30).

Distinct from feature 39 because 39 is a *push at end of day*; this
is a *persistent, queryable memory* the owner can interrogate at any
time. Distinct from feature 29 because 29 is *live (current
state)*; this is *historical (any past service)*.

## Evidence / JTBD

When the owner is reviewing the books at home 3 days after a service,
the owner wants to know what happened at a specific moment ("did we 86
the lamb at 21:30 last Saturday?"), but struggles because the existing
recap (feature 39) is a single push at end of day with no
time-indexed detail, so that a queryable per-shift card that auto-folds
raw detail at close gives the owner `/day last-saturday` and
`/shift 21:30 last-saturday` without leaving Telegram.

## Scope

**In scope (v2 owner-pains):**
- A new `DayCard` append-only SQLModel table (one row per service):
  `(id, service_date, opened_at, closed_at, body_markdown,
  folded_at)`. `folded_at` is `NULL` while the card is live; set to
  `NOW()` at end-of-service fold. The only mutable column is
  `folded_at` (NULL → non-NULL).
- A new `DayCardLine` append-only SQLModel table (one row per
  5-minute summary tick during service):
  `(id, day_card_id, tick_at, summary_text, event_count)`.
  Append-only — rows are never updated.
- A new background task `day_card_tick()` in
  `backend/app/services/day_card.py` that runs every 5 minutes via
  APScheduler (already imported for features 39 and the price-update
  task). The task:
  1. Reads the latest 5-minute window of events from the existing
     `CookChannel` SSE stream's backing log (feature 23 already
     publishes events to a per-service log table).
  2. Composes a one-line summary (e.g. `4 covers open · 2 new orders
     · lamb 86ed · focaccia comp`).
  3. Writes one `DayCardLine` row with `tick_at=NOW()`.
- A new background task `day_card_fold()` in
  `backend/app/services/day_card.py` that runs at 23:30 Europe/Paris
  (same time as feature 39's recap). The task:
  1. Reads all `DayCardLine` rows for the current `DayCard`.
  2. Composes a 4-section folded body: covers, voids-with-reasons
     (from feature 37), top 3 movers, prep adherence (from feature 43,
     when available — falls back gracefully if no `PrepTask` rows
     exist).
  3. Writes the folded body to `DayCard.body_markdown` and sets
     `folded_at=NOW()`.
- A new bot command `/day [date_or_relative]` — owner-only (chat-id
  in `OWNER_TELEGRAM_CHAT_IDS` from feature 39). Bot parses the date
  (supports `YYYY-MM-DD`, `today`, `yesterday`, `last-saturday`,
  `last-sunday`, etc. via small date math). Replies with the matching
  `DayCard.body_markdown`. Falls back to "No card for <date>" if no
  `DayCard` row exists.
- A new bot command `/shift [time] [date_or_relative]` — owner-only.
  Bot parses the time + date, finds the matching `DayCardLine` row
  (or interpolates from the nearest two ticks), replies with the
  one-line summary at that moment. Falls back to "No card for
  <time> <date>" if no `DayCard` row exists.

**Out of scope (v2 owner-pains):**
- Weekly / monthly auto-folding cards — the v1 fold runs at
  end-of-service only. Weekly card folding is a v3 follow-up.
- Trend analysis ("how does this Saturday compare to last Saturday?")
  — the v1 card is a single-service artifact. Trend is a v3
  follow-up.
- NLU / fuzzy time parsing (`/shift around nine-thirty yesterday
  evening`) — the v1 commands accept strict `HH:MM` + standard date
  formats. NLU is forbidden on the owner surface per charter §3.3
  (AI may assist with non-AI fallback).
- Multi-restaurant / multi-tenant cards — the v1 card is per-single
  restaurant. Multi-tenant is a v3 follow-up.

## User flow

**Owner — query a past service day:**

1. Owner types `/day last-saturday` in the existing owner Telegram chat.
2. Bot parses "last-saturday" → `2026-08-01` (assuming today is
   2026-08-07), looks up `DayCard` row for that date.
3. Bot reads `body_markdown` (already folded) and replies with the
   4-section card:
   ```
   📅 2026-08-01 (Sat) — folded 23:30

   💰 Covers: 52 orders · €1,456.78
   🚫 Voids with reasons (2):
     • lamb — 86 — "we ran out"
     • focaccia — comp — "guest comp — birthday"
   🏆 Top 3 movers:
     1. tagliatelle al ragù — 22 orders · €264.00
     2. tiramisu — 18 orders · €108.00
     3. panna cotta — 15 orders · €90.00
   ✅ Prep adherence: 4/5 done (80%), 1 skipped

   Reply `/shift HH:MM last-saturday` for a per-moment summary.
   ```
4. The folded card is also written to `DayCard.body_markdown` so it
   can be queried at any future time without re-folding.

**Owner — query a specific moment:**

1. Owner types `/shift 21:30 last-saturday`.
2. Bot parses "21:30 last-saturday" → looks up `DayCardLine` rows
   for `2026-08-01` with `tick_at` between `21:25` and `21:35`.
3. Bot replies with the matching one-line summary:
   ```
   🕒 2026-08-01 21:30 — 6 covers open · 3 new orders in last 5min ·
   lamb 86ed · focaccia comp · 0 prep tasks skipped
   ```

**Owner — query a date that has no card:**

1. Owner types `/day 2026-07-15`.
2. Bot looks up `DayCard` row for `2026-07-15`, finds none.
3. Bot replies: "No card for 2026-07-15. Reply `/day today` or
   `/day yesterday` for the latest cards."

**Cook / manager — bot refuses owner-only command:**

1. Cook types `/day yesterday` in the cook chat.
2. Bot validates chat-id is not in `OWNER_TELEGRAM_CHAT_IDS`,
   replies: "Owner-only command. Reply `/prep list` for prep status."

## Data model

Two new tables:

```python
# backend/app/models.py (additive)

class DayCard(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    service_date: date = Field(unique=True, index=True)
    opened_at: datetime  # first DayCardLine tick_at for this date
    closed_at: datetime | None = Field(default=None)  # set at fold
    body_markdown: str | None = Field(default=None, max_length=8000)  # set at fold
    folded_at: datetime | None = Field(default=None)  # NULL → live; non-NULL → folded
    # Append-only on creation. The only mutable column is folded_at
    # (NULL → non-NULL at fold) and body_markdown (NULL → non-NULL).

class DayCardLine(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    day_card_id: int = Field(foreign_key="daycard.id", index=True)
    tick_at: datetime = Field(index=True)
    summary_text: str = Field(max_length=500)
    event_count: int = Field(default=0)
    # Append-only — rows are never updated.
```

Both tables are append-only (same SQLAlchemy listener pattern as
`StockEntry` and `OwnerAuditEvent`). `DayCard` allows the one-shot
transition `folded_at: NULL → non-NULL` and `body_markdown: NULL →
non-NULL` at fold time (idempotent — re-folding is safe).

No changes to existing models. Reuses:
- `CookChannel` SSE stream (feature 23) — provides the live event log.
- `TELEGRAM_ALLOWED_USERS` (cook/manager allowlist) — unchanged.
- `OWNER_TELEGRAM_CHAT_IDS` (owner allowlist from feature 39) — reused
  for the `/day` and `/shift` commands (no new config).
- APScheduler (already imported) — new jobs `day_card_tick` (every 5
  min) and `day_card_fold` (daily at 23:30 Europe/Paris).

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**

- New command: `/day [date_or_relative]` — owner-only (chat-id in
  `OWNER_TELEGRAM_CHAT_IDS`). Parses date (YYYY-MM-DD, today,
  yesterday, last-saturday, last-sunday, N-days-ago). Replies with
  folded `DayCard.body_markdown`.
- New command: `/shift [time] [date_or_relative]` — owner-only.
  Parses `HH:MM` + date. Replies with the matching `DayCardLine`
  one-line summary.
- Owner-only guard reuses `OWNER_TELEGRAM_CHAT_IDS` allowlist from
  feature 39 (no new config).

**API (FastAPI):**

- New `GET /api/day-cards?service_date=<YYYY-MM-DD>` — owner-only.
  Returns the `DayCard` row + all `DayCardLine` rows for the date.
- Existing routes unchanged. Existing manager dashboard can be
  extended later to render `DayCard` rows for read-only history
  (out of scope).

**Scheduler:**

- APScheduler job `day_card_tick` registered with
  `CronTrigger(minute='*/5')` (every 5 minutes) — fires only while
  a `DayCard` row exists for today (`folded_at IS NULL`).
- APScheduler job `day_card_fold` registered with
  `CronTrigger(hour=23, minute=30, timezone='Europe/Paris')` — same
  time as feature 39's recap. Idempotent — re-folding is safe.

## Dependencies

- **No new pip dependencies.** APScheduler is already imported.
- **Required upstream features**:
  - feature 23 (`sse-cook-channel`) — supplies the `CookChannel`
    SSE stream that the per-5-minute tick reads from.
  - feature 39 (`owner-daily-recap-telegram`) — supplies
    `OWNER_TELEGRAM_CHAT_IDS` allowlist and the Europe/Paris
    CronTrigger pattern.
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column on `StockEntry` that feeds the
    voids-with-reasons section of the folded card.
  - feature 43 (`telegram-prep-checkoff-adherence`) — supplies
    the prep-adherence section of the folded card (graceful
    fallback if not yet shipped).
- **Required downstream features**: none.

## Failure / recovery

- **Background task fails (DB error / transient)** — APScheduler logs
  the exception and retries on the next scheduled tick (5 min). No
  silent failure; no row written. Re-running the tick writes the
  missing summary; the audit chain is preserved because each
  `DayCardLine` row has its own `tick_at` timestamp.
- **Fold runs before any tick has fired (e.g. early close)** — the
  folded body is composed from whatever `DayCardLine` rows exist
  (possibly zero); falls back gracefully. The owner sees a thin
  card with a "(no live ticks recorded)" footer.
- **Bot can't reach the owner (network blip)** — bot retries once
  after 60s; if still failing, the `DayCard` row is unaffected.
  The owner can re-query at any later time.
- **Date parse error** — bot replies with usage hint:
  "Usage: `/day [today|yesterday|last-saturday|YYYY-MM-DD|N-days-ago]`.
  Example: `/day yesterday`."
- **Time parse error** — bot replies with usage hint:
  "Usage: `/shift HH:MM [date_or_relative]`. Example:
  `/shift 21:30 last-saturday`."
- **5-minute tick during folded card** — the task checks
  `DayCard.folded_at IS NULL` before writing a new line. Post-fold
  ticks are no-ops.

## Definition of done

- [ ] `DayCard` and `DayCardLine` SQLModel tables added; append-only
      listener extended.
- [ ] Alembic migration for the two tables.
- [ ] `day_card_tick()` background task registered with
      `CronTrigger(minute='*/5')`; verified by unit test that fires
      the job at a fixed time and asserts one `DayCardLine` row is
      written.
- [ ] `day_card_fold()` background task registered at 23:30
      Europe/Paris; verified by unit test that fires the job at a
      fixed time and asserts the folded body contains the four
      sections (covers / voids-with-reasons / top 3 movers /
      prep adherence).
- [ ] Bot commands `/day [date]` and `/shift [time] [date]`
      shipped; owner-only allowlist enforced.
- [ ] Date parser handles `today`, `yesterday`, `last-saturday`,
      `last-sunday`, `N-days-ago`, `YYYY-MM-DD`.
- [ ] Time parser handles strict `HH:MM` 24-hour format.
- [ ] End-to-end observed: service runs for 4 hours → 48
      `DayCardLine` rows written → fold at 23:30 → owner queries
      `/day yesterday` → folded body returned → owner queries
      `/shift 21:30 yesterday` → matching line returned.
- [ ] No-card graceful fallback: owner queries `/day 2026-07-15` →
      bot replies "No card for 2026-07-15".
- [ ] Cook / manager bot refuses owner-only command: cook types
      `/day yesterday` → bot replies "Owner-only command".
- [ ] Existing tests still green.
- [ ] Manual acceptance: in a 7-day pilot, the owner queries
      `/day` and `/shift` for past services ≥3 times and finds
      the answers they expect.

## Open questions

- Should the fold also include the prep-adherence section when
  `PrepTask` rows exist but feature 43 hasn't shipped yet? Decision:
  no — feature 43 ships first; this contract references feature 43
  as a prerequisite for the prep-adherence section. Without 43,
  the fold omits the prep-adherence line cleanly.
- Should the card auto-fold on `cook_end_of_service` event from
  feature 23, or only at 23:30 Europe/Paris? Decision: 23:30 only
  in v1. Auto-fold on event is a v3 follow-up.
- Should the bot support `/week` (queries the weekly auto-fold)?
  Decision: no — v1 is `/day` and `/shift` only. Weekly fold is
  a v3 follow-up.

## Why this matters

LE31's solo operator is also the cook, the manager, and the owner.
The operator's most-cited follow-up question after a few days is
"what happened at <moment> in <past service>?" — currently
unanswerable because the existing recap is a single push at end of
day, and the manager dashboard requires login + manual date
navigation.

The in-window peer (`SsssssSynqa/tether-agent-runtime`, pushed
2026-08-05, **7★** — the strongest in-window star count of the pass
outside the volume-leaders) shares the *auto-folding + day/week
cards* layered memory primitive. Translated to LE31, this is the
missing layer between the live link (feature 29 — pull, owner goes
to it) and the end-of-day recap (feature 39 — push at 23:30). The
owner can interrogate any past service moment at any time.

Medium cost (two new tables + two new bot commands + two new
background tasks + one new API endpoint + one date parser), high
value (the operator's most-cited historical-moment follow-up
question).
