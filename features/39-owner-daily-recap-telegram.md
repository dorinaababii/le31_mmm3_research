# Feature 39 — Owner Daily Recap Telegram

> **Priority**: P1 · **Effort**: S (≤3 days) · **Source**: brainstorm 2026-08-06
> (cross-section pick C) · **Bucket**: v2 owner-pains
> **One-line**: Once per day at the owner's chosen close-of-shift time
> (default 23:30 Europe/Paris), the existing cook-bot webhook fires a
> single Telegram message to the owner with covers, voids-with-reasons
> (from feature 37), top 3 movers, and tomorrow's prep alerts at-or-below
> `reorder_point`. Owner can reply `/ack` to dismiss or `/explain <line>`
> to drill into a single row. Push, not pull — sits beside (not replaces)
> the no-account live floor link from feature 29.

## Goal

Add the missing *recurring push* for the solo-operator end-of-day ritual.
The solo-operator "I don't want to log in just to see how today went"
pain is *exactly* the indie-founder "monthly MRR-recap" pain: a single
push summarising what the operator needs to know, with a one-tap
acknowledge and a typed drill-in command. Distinct from feature 29
(`owner-no-account-live-floor-link`) because it is push (bot → owner),
not pull (owner → live link); distinct from feature 30
(`append-only-audit-redirect`) because it is summary-shaped, not
audit-chain-shaped.

Inspired by today's brainstorm: HN objectID **49181766** *Ask HN: Show
your micro-SaaS / MRR updates (August 2026)* (7 pts, in window) plus
objectIDs 49150870 *Need feedback: My first SaaS as a solo-founder* and
49107855 *Ventora Expands Its AI Business Builder to Help Solo
Founders*. The recurring UX primitive across these threads: a single
push notification to the founder once a month (or once a day for the
LE31 owner) summarising the numbers they care about, with a one-tap
acknowledge and a typed drill-in.

This feature **depends on feature 37 (`void-rationale-ledger-field`)** —
the recap's "voids with reasons" line is meaningless without the
`rationale` column. Without 37, the recap is just a count of voids; with
37, the recap is a list of *decisions*. This contract lists 37 as a
prerequisite and will refuse to ship without it.

## Evidence / JTBD

When the owner finishes the day's paperwork at home, the owner wants a
one-glance recap of what happened, but struggles because logging into the
full web app costs ~90 seconds of attention and the owner is already
tired, so that a single Telegram push at 23:30 Europe/Paris gives covers
/ voids-with-reasons / top 3 movers / tomorrow's prep alerts in
<30 seconds.

## Scope

**In scope (v2 owner-pains):**
- A new config field `OWNER_TELEGRAM_CHAT_IDS: list[int]` in
  `backend/app/config.py` (list of chat ids that receive the recap).
  Loaded from env var `OWNER_TELEGRAM_CHAT_IDS` (comma-separated). The
  existing `TELEGRAM_ALLOWED_USERS` config stays as the cook/manager
  allowlist; this is a separate, narrower allowlist for the recap push.
- A new config field `OWNER_RECAP_HOUR: int = 23` (default 23:00 Paris
  time) and `OWNER_RECAP_MINUTE: int = 30` (default :30 → recap fires
  at 23:30 Paris daily). Configurable per restaurant.
- A new background scheduler (APScheduler `AsyncIOScheduler` already
  imported for the existing price-update task) that runs a single daily
  job at `OWNER_RECAP_HOUR:OWNER_RECAP_MINUTE` Europe/Paris time. The
  job calls a new `build_daily_recap()` function and sends the result
  to every chat id in `OWNER_TELEGRAM_CHAT_IDS` via the existing
  aiogram bot instance.
- A new function `build_daily_recap() -> str` in
  `backend/app/services/recap.py` that builds the markdown message body
  with four sections:
  1. **Covers**: number of paid orders today + total EUR (uses
     `Order.total_eur` from existing schema; EUR invariant preserved).
  2. **Voids with reasons**: list of today's negative-delta
     `StockEntry` rows with `rationale` populated, grouped by
     `menu_item_id` (so "lamb was 86ed twice" appears as one line).
     If feature 37's `rationale` column is empty for a row, the recap
     shows "(legacy — no rationale recorded)" so the owner still sees
     the count.
  3. **Top 3 movers**: top 3 `menu_item`s by `qty` sold today, with
     EUR contribution (single SELECT against the existing `OrderItem`
     table).
  4. **Tomorrow's prep alerts**: items at-or-below `reorder_point`
     (the existing query from feature 26), formatted as a single bulleted
     list.
- A new bot command `/ack` (no args) — owner-only, chat-id in
  `OWNER_TELEGRAM_CHAT_IDS`; bot replies "Acknowledged. See you
  tomorrow." and writes one `OwnerRecapAck` row (append-only).
- A new bot command `/explain <line_number>` — owner-only; bot replies
  with the matching row from the recap (full `StockEntry` or `OrderItem`
  details), so the owner can drill in without leaving Telegram.
- A new append-only `OwnerRecap` SQLModel table (one row per recap
  sent) recording `(id, sent_at, chat_id, body_markdown,
  acked_at, acked_by_chat_id)` for audit.

**Out of scope (v2 owner-pains):**
- Live alerts during service — that lives on the live floor link
  (feature 29). The recap is end-of-day only.
- Weekly or monthly rollups — daily only in v1.
- Tips reconciliation or payout reports — feature 05 territory.
- Demand forecasting — feature 07 / 17 / 21 territory.
- Recap on days the restaurant was closed — the scheduler skips
  cleanly if there were zero `Order` rows that day (just sends a
  one-line "Closed today — see you tomorrow").
- Per-item revenue breakdown beyond top 3 — full report is one click
  away in the manager dashboard.

## User flow

**Owner — receives the 23:30 recap:**

1. At 23:30 Europe/Paris, the scheduler fires `build_daily_recap()`.
2. The function aggregates the four sections (covers, voids-with-reasons,
   top 3 movers, tomorrow's prep alerts) and returns a single markdown
   string.
3. The bot sends the message to every chat id in
   `OWNER_TELEGRAM_CHAT_IDS`. Message body example:
   ```
   📊 Daily recap — 2026-08-06

   💰 Covers: 47 orders · €1,234.56

   🚫 Voids with reasons (3):
   • lamb — 86 — "we ran out of lamb eighty-six it" (×2)
   • focaccia — comp — "guest comp — birthday"

   🏆 Top 3 movers:
   1. tagliatelle al ragù — 18 orders · €216.00
   2. tiramisu — 14 orders · €84.00
   3. panna cotta — 12 orders · €72.00

   ⚠️ Tomorrow's prep alerts (2):
   • flour — at reorder point (5 kg remaining)
   • eggs — below reorder point (12 u remaining)

   Reply `/ack` to dismiss, or `/explain <N>` to drill in.
   ```
4. The bot also writes one `OwnerRecap` row (append-only, never
   updated).

**Owner — dismisses:**

1. Owner replies `/ack`.
2. Bot replies "Acknowledged. See you tomorrow."
4. Bot sets `acked_at` on the latest `OwnerRecap` row.

**Owner — drills in on the focaccia comp:**

1. Owner replies `/explain 2`.
2. Bot looks up the recap's voids section, line 2 (focaccia comp), and
   replies with the full `StockEntry` row + the linked `OrderItem` and
   the `Order`:
   ```
   StockEntry #1234
   • focaccia — qty_delta = -1 — reason = comp
   • rationale = "guest comp — birthday"
   • source = web:waiter
   • created_at = 2026-08-06T21:14:33+02:00

   Linked Order #5678 (table 4, €42.00 paid, paid 21:14)
   Linked OrderItem: focaccia × 1, €8.00

   Reply `/explain <N>` for another row, or `/ack` to finish.
   ```

**Owner — disabled the recap and forgot:**

1. Owner sets `OWNER_TELEGRAM_CHAT_IDS=` (empty) in `.env` and restarts.
2. The scheduler still runs `build_daily_recap()` (cheap, single SELECT)
   but the bot sends to zero chat ids. The `OwnerRecap` row is written
   with `chat_id = NULL` so the audit chain stays complete.
3. Owner can manually trigger the recap from the manager dashboard
   (out of scope for this contract; deferred to a follow-up).

## Data model

One new table:

```python
# backend/app/models.py (additive)

class OwnerRecap(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sent_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    chat_id: int | None = Field(default=None, index=True)  # NULL if OWNER_TELEGRAM_CHAT_IDS is empty
    body_markdown: str = Field(max_length=4000)            # exact message body sent
    acked_at: datetime | None = Field(default=None)
    acked_by_chat_id: int | None = Field(default=None)
```

`OwnerRecap` is append-only (same SQLAlchemy listener as `StockEntry`
and `OwnerAuditEvent`). `acked_at` is the only mutable column, and is
only ever set from `NULL` to a non-NULL timestamp (idempotent — tapping
`/ack` twice is safe).

No changes to existing models. Reuses `StockEntry`, `Order`, `OrderItem`,
`MenuItem`, the `reorder_point` query from feature 26.

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**
- New command: `/ack` — owner-only (chat-id in `OWNER_TELEGRAM_CHAT_IDS`).
- New command: `/explain <line_number>` — owner-only; parses `<N>` and
  replies with the matching row from the most recent `OwnerRecap.body_markdown`.
- The recap itself is sent by the scheduler via `bot.send_message()`
  to each chat id (same primitive as the existing cook bot's replies).
- A new config-driven allowlist guard: bot refuses `/ack` and `/explain`
  from any chat id not in `OWNER_TELEGRAM_CHAT_IDS`. This is a separate
  allowlist from `TELEGRAM_ALLOWED_USERS` (which is cook/manager only).

**API (FastAPI):**
- No new HTTP routes. All logic lives in the scheduler + bot webhook.
- Existing routes unchanged. Existing manager dashboard can be extended
  later to render `OwnerRecap` rows for read-only history (out of scope).

**Scheduler:**
- APScheduler `AsyncIOScheduler` instance is created in
  `backend/app/main.py` lifespan (same pattern as the existing
  price-update cron task). New job `daily_recap` registered at
  `OWNER_RECAP_HOUR:OWNER_RECAP_MINUTE` Europe/Paris time. Uses
  `apscheduler.triggers.cron.CronTrigger` with `timezone="Europe/Paris"`.

## Dependencies

- **No new pip dependencies.** APScheduler is already imported for the
  existing price-update task.
- **Required upstream features**:
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column on `StockEntry`. Without 37, the recap's
    "Voids with reasons" section degrades to "(legacy — no rationale
    recorded)" for every row.
  - feature 04 (cook Telegram bot) — supplies the bot instance +
    `bot.send_message()` primitive.
  - feature 26 (`reorder-point-on-stockentry`) — supplies the
    tomorrow's-prep-alerts query.
- **Required downstream features**: none.

## Failure / recovery

- **Scheduler job fails (DB error / transient)**: APScheduler logs the
  exception and retries on the next scheduled run. No silent failure;
  the operator gets a clear log line. An optional one-line
  `Sentry.capture_exception()` is acceptable if the deployment uses
  Sentry.
- **Bot can't reach the owner (network blip / chat id wrong)**:
  APScheduler retries once after 60 seconds; if still failing, the
  `OwnerRecap` row is still written (with `chat_id` set) and the
  manager dashboard shows the recap row as "undelivered" (out of scope
  for v1).
- **Owner never `/ack`s**: the recap row stays with `acked_at = NULL`
  forever; the audit chain is unaffected (append-only). The next day's
  recap is independent.
- **Time zone misconfiguration**: the scheduler uses
  `CronTrigger(timezone="Europe/Paris")` explicitly, so DST transitions
  are handled by APScheduler; no manual offset math.
- **Cook bot is down / webhook broken**: this recap is independent of
  the cook bot's webhook for *receiving* commands; the scheduler still
  fires. If the bot *send* fails, the row is still written and the
  manager dashboard shows "undelivered" (out of scope for v1).

## Definition of done

- [ ] `OwnerRecap` table added; append-only listener extended.
- [ ] `OWNER_TELEGRAM_CHAT_IDS` and `OWNER_RECAP_HOUR` / `_MINUTE` config
      fields added to `backend/app/config.py`.
- [ ] `build_daily_recap()` function ships with the four sections
      (covers / voids-with-reasons / top 3 movers / tomorrow's prep alerts).
- [ ] APScheduler job registered at 23:30 Europe/Paris daily; verified
      with a unit test that fires the job at a fixed time and asserts the
      message body shape.
- [ ] Bot commands `/ack` and `/explain <N>` shipped; chat-id allowlist
      enforced.
- [ ] End-to-end observed: a 23:30 trigger fires → recap message body
      contains the four sections → owner receives the message → owner
      replies `/ack` → `OwnerRecap.acked_at` is set → owner replies
      `/explain 2` → bot replies with the focaccia comp details.
- [ ] DST transition test: at the spring-forward boundary (last Sunday
      of March), the 23:30 Europe/Paris job fires exactly once (not
      skipped, not duplicated).
- [ ] Existing tests still green.
- [ ] Manual acceptance: in a 7-day pilot, the recap fires daily at the
      configured time, the owner acknowledges every day, and zero
      unintended noise is sent (no recap on a closed day, no recap with
      missing rationale).

## Open questions

- Should the recap body be MarkdownV2 or plain text? Telegram Markdown
  is finicky about escaping. Decision: plain text with explicit emojis
  (📊 💰 🚫 🏆 ⚠️) for visual structure; no MarkdownV2 escape rules to
  worry about.
- Should the scheduler write a *predicted* `OwnerRecap` row before
  sending (for race-free idempotency if APScheduler retries)? Decision:
  no — the `id` is auto-generated and `sent_at` is set at send time;
  if APScheduler retries after a successful send, the second attempt
  writes a duplicate row. Mitigation: idempotency key = `(date, chat_id)`
  — if a row for today already exists for that chat id, skip the send.
  Add to Open Questions for v1 follow-up.
- Should the recap include a revenue breakdown by payment method
  (cash vs card vs other)? Decision: not for v1; out of scope. Could
  be a one-line addition later (uses the existing `Bill.payment_method`
  column from feature 05).

## Why this matters

LE31's solo operator is also the same person who runs the floor and
manages the books. The end-of-day paperwork is the friction the operator
cites most often in any pilot. The HN indie-SaaS MRR-thread pattern
(objectID 49181766, 7 pts, in window) is the same shape as a daily
owner recap: a single push summarising what the operator needs to know,
with a one-tap acknowledge and a typed drill-in command.

Translated to LE31, this is the missing layer between the live link
(feature 29 — pull, owner goes to it) and the manager dashboard
(feature 25 dev loop — full app, too heavy for end-of-day). Tiny cost
(one new table + one scheduler job + two bot commands + four SQL
aggregations), high value (the solo-operator's most-cited end-of-day
friction). Depends on feature 37's `rationale` column.