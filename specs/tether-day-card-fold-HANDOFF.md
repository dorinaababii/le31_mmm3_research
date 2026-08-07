# tether-day-card-fold — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/44-tether-day-card-fold.md` before touching any code. Do
> not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `44`
- Slug: `tether-day-card-fold`
- Contract file: `features/44-tether-day-card-fold.md`
- Bucket: v2 owner-pains (two new tables + two background tasks + two bot commands)
- Linear parent: HMM-49 (Brainstorm 2026-08-07 — daily, created by this run)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build.** (v2 owner-pains, ≤3 days.) No failed checks.

Evidence precondition: **observed** (1 in-window GitHub repo —
`SsssssSynqa/tether-agent-runtime` 7★, pushed 2026-08-05 — shares the
layered-memory-with-auto-folding pattern). Confidence: **medium**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/config.py                                # (no new fields)
backend/app/models.py                                # NEW: DayCard + DayCardLine SQLModel
backend/app/services/day_card.py                     # NEW: day_card_tick() + day_card_fold()
backend/app/services/date_parser.py                  # NEW: parse_relative_date(s) helper
backend/app/bot/cook_bot_day_card.py                 # NEW: /day, /shift command handlers
backend/app/routers/day_cards.py                     # NEW: GET /api/day-cards
backend/app/main.py                                  # NEW: APScheduler job registration (lifespan)
backend/app/events/daycard_append_only.py            # NEW: append-only listener for DayCard + DayCardLine
backend/alembic/versions/<new>_day_card.py            # NEW migration
backend/README.md                                    # note the new scheduler jobs + bot commands
```

No new pip dependencies. APScheduler is already imported.

## Endpoints and contracts added

**Two new SQLModel tables:**

```python
# backend/app/models.py
class DayCard(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    service_date: date = Field(unique=True, index=True)
    opened_at: datetime
    closed_at: datetime | None = Field(default=None)
    body_markdown: str | None = Field(default=None, max_length=8000)
    folded_at: datetime | None = Field(default=None)
    # Append-only on creation. folded_at / body_markdown transition
    # NULL → non-NULL at fold (idempotent).

class DayCardLine(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    day_card_id: int = Field(foreign_key="daycard.id", index=True)
    tick_at: datetime = Field(index=True)
    summary_text: str = Field(max_length=500)
    event_count: int = Field(default=0)
    # Append-only — rows are never updated.
```

**One new Alembic migration:**

```python
def upgrade():
    op.create_table(
        "daycard",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("service_date", sa.Date, nullable=False, unique=True),
        sa.Column("opened_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("closed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("body_markdown", sa.String(8000), nullable=True),
        sa.Column("folded_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_daycard_service_date", "daycard", ["service_date"], unique=True)

    op.create_table(
        "daycardline",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("day_card_id", sa.Integer, sa.ForeignKey("daycard.id"), nullable=False),
        sa.Column("tick_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("summary_text", sa.String(500), nullable=False),
        sa.Column("event_count", sa.Integer, nullable=False, server_default="0"),
    )
    op.create_index("ix_daycardline_day_card_id", "daycardline", ["day_card_id"])
    op.create_index("ix_daycardline_tick_at", "daycardline", ["tick_at"])

def downgrade():
    op.drop_index("ix_daycardline_tick_at", table_name="daycardline")
    op.drop_index("ix_daycardline_day_card_id", table_name="daycardline")
    op.drop_table("daycardline")
    op.drop_index("ix_daycard_service_date", table_name="daycard")
    op.drop_table("daycard")
```

**Two new APScheduler jobs registered in `backend/app/main.py` lifespan:**

```python
# backend/app/main.py
from apscheduler.triggers.cron import CronTrigger
from app.services.day_card import day_card_tick, day_card_fold

# Every 5 minutes — fires only while a DayCard row exists for today
scheduler.add_job(
    day_card_tick,
    CronTrigger(minute="*/5"),
    id="day_card_tick",
    replace_existing=True,
    misfire_grace_time=60,  # tolerate up to 1 min late firing
)

# Daily at 23:30 Europe/Paris — same time as feature 39's recap
scheduler.add_job(
    day_card_fold,
    CronTrigger(hour=23, minute=30, timezone="Europe/Paris"),
    id="day_card_fold",
    replace_existing=True,
    misfire_grace_time=300,  # tolerate up to 5 min late firing
)
```

**Two new bot commands (owner-only, reuse `OWNER_TELEGRAM_CHAT_IDS` from feature 39):**

- `/day [date_or_relative]` — parses date (YYYY-MM-DD, today,
  yesterday, last-saturday, last-sunday, N-days-ago). Replies with
  `DayCard.body_markdown`.
- `/shift [time] [date_or_relative]` — parses `HH:MM` + date.
  Replies with the matching `DayCardLine` one-line summary.

Both commands fail with "owner-only" if chat-id is not in
`OWNER_TELEGRAM_CHAT_IDS`.

**One new API endpoint:**

- `GET /api/day-cards?service_date=<YYYY-MM-DD>` — owner-only.
  Returns the `DayCard` row + all `DayCardLine` rows for the date.

**Date parser helper (`services/date_parser.py`):**

```python
def parse_relative_date(s: str) -> date:
    """Parse a relative date string into a date.

    Supports:
    - "today", "yesterday"
    - "last-saturday", "last-sunday", ..., "last-friday"
    - "N-days-ago" (e.g. "3-days-ago")
    - "YYYY-MM-DD" (ISO format)

    Returns the matching date in Europe/Paris timezone.
    Raises ValueError on unknown format.
    """
```

## Verification

1. `day_card_tick()` unit tests with mocked `CookChannel` SSE event
   log — verify one `DayCardLine` row is written per tick.
2. `day_card_fold()` unit tests with mocked `DayCardLine` rows —
   verify the folded body contains the four sections (covers /
   voids-with-reasons / top 3 movers / prep adherence).
3. End-to-end APScheduler test: fire `day_card_tick` at a fixed
   time, assert one `DayCardLine` row is written. Fire
   `day_card_fold` at 23:30 Europe/Paris, assert the folded body
   is non-empty.
4. Date parser tests: `parse_relative_date("today")` returns today;
   `parse_relative_date("yesterday")` returns yesterday;
   `parse_relative_date("last-saturday")` returns the most recent
   past Saturday; `parse_relative_date("3-days-ago")` returns
   3 days back; `parse_relative_date("2026-08-01")` returns
   2026-08-01. Unknown format raises `ValueError`.
5. Bot command tests: owner `/day yesterday` returns the folded
   body; owner `/shift 21:30 yesterday` returns the matching
   line; non-owner `/day yesterday` returns "owner-only".
6. No-card graceful fallback: owner `/day 2026-07-15` → bot replies
   "No card for 2026-07-15".
7. Cook / manager bot refuses owner-only command: cook types
   `/day yesterday` → bot replies "Owner-only command".
8. Append-only listener test: `UPDATE DayCardLine SET summary_text='x'
   WHERE id=1` raises `IntegrityError`. `DELETE FROM DayCardLine
   WHERE id=1` raises `IntegrityError`.
9. Idempotent fold: `day_card_fold` called twice for the same date
   → second call updates `folded_at` and `body_markdown` to the
   same values; no duplicate rows.
10. End-to-end observed: a 4-hour service runs → 48 `DayCardLine`
    rows written → fold at 23:30 → owner queries `/day yesterday`
    → folded body returned → owner queries `/shift 21:30 yesterday`
    → matching line returned.
11. DST transition test: at the spring-forward boundary (last Sunday
    of March), the 23:30 Europe/Paris `day_card_fold` job fires
    exactly once (not skipped, not duplicated).
12. Existing tests still green.

## Rollback path

Disable the `day_card_tick` and `day_card_fold` scheduler jobs in
one config line each. The tables stay but no new rows are written.
To fully rollback: drop the tables (migration downgrade), remove
the bot command handlers, remove the API router, remove the
scheduler job registration. No upstream feature is broken by
removing this.

## Dependencies

- No new pip dependencies.
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
