# owner-daily-recap-telegram — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/39-owner-daily-recap-telegram.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `39`
- Slug: `owner-daily-recap-telegram`
- Contract file: `features/39-owner-daily-recap-telegram.md`
- Bucket: v2 owner-pains (recurring push, no new client)
- Linear parent: HMM-40 (Brainstorm 2026-08-06 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: build.** (with feature 37 `void-rationale-ledger-field` as a
prerequisite.) No failed checks.

Evidence precondition: **observed** (HN objectID 49181766 *Ask HN: Show
your micro-SaaS / MRR updates (August 2026)* 7 pts; the monthly-recap
transparency thread is recurring and live in 2026-08). Confidence: **high**.

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
backend/app/config.py                            # NEW: OWNER_TELEGRAM_CHAT_IDS, OWNER_RECAP_HOUR, OWNER_RECAP_MINUTE
backend/app/models.py                            # NEW: OwnerRecap SQLModel
backend/app/services/recap.py                    # NEW: build_daily_recap() function
backend/app/bot/cook_bot_recap.py                # NEW: /ack + /explain <N> command handlers
backend/app/main.py                              # NEW: APScheduler job registration (lifespan)
backend/app/events/ownerrecap_append_only.py     # NEW: append-only listener for OwnerRecap
backend/alembic/versions/<new>_owner_recap.py    # NEW migration
backend/README.md                                # note the new scheduler job + env vars
```

No new pip dependencies. APScheduler is already imported for the
existing price-update task.

## Endpoints and contracts added

No new HTTP routes. All logic lives in the scheduler + bot webhook.

One new SQLModel table:

```python
# backend/app/models.py
class OwnerRecap(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sent_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    chat_id: int | None = Field(default=None, index=True)
    body_markdown: str = Field(max_length=4000)
    acked_at: datetime | None = Field(default=None)
    acked_by_chat_id: int | None = Field(default=None)
```

Append-only (new `ownerrecap_append_only.py` listener — only column
ever updated is `acked_at`, only ever `NULL → non-NULL`).

One new Alembic migration:

```python
def upgrade():
    op.create_table(
        "ownerrecap",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("sent_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("chat_id", sa.BigInteger, nullable=True),
        sa.Column("body_markdown", sa.String(4000), nullable=False),
        sa.Column("acked_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("acked_by_chat_id", sa.BigInteger, nullable=True),
    )
    op.create_index("ix_ownerrecap_chat_id", "ownerrecap", ["chat_id"])
    op.create_index("ix_ownerrecap_sent_at", "ownerrecap", ["sent_at"])

def downgrade():
    op.drop_index("ix_ownerrecap_sent_at", table_name="ownerrecap")
    op.drop_index("ix_ownerrecap_chat_id", table_name="ownerrecap")
    op.drop_table("ownerrecap")
```

One new config block:

```python
# backend/app/config.py
OWNER_TELEGRAM_CHAT_IDS: list[int] = Field(default_factory=list)  # loaded from .env
OWNER_RECAP_HOUR: int = 23                                        # default 23:00 Paris
OWNER_RECAP_MINUTE: int = 30                                      # default :30 → 23:30 Paris
```

`.env` keys:

```
OWNER_TELEGRAM_CHAT_IDS=8930997623  # comma-separated chat ids
OWNER_RECAP_HOUR=23
OWNER_RECAP_MINUTE=30
```

One new APScheduler job registered in the FastAPI lifespan:

```python
# backend/app/main.py
from apscheduler.triggers.cron import CronTrigger
from app.services.recap import build_daily_recap

scheduler.add_job(
    build_daily_recap,
    CronTrigger(hour=OWNER_RECAP_HOUR, minute=OWNER_RECAP_MINUTE, timezone="Europe/Paris"),
    id="daily_recap",
    replace_existing=True,
    misfire_grace_time=300,  # tolerate up to 5 min late firing
)
```

Two new bot commands (owner-only, separate allowlist from
`TELEGRAM_ALLOWED_USERS`):

- `/ack` — owner replies this to dismiss the recap. Bot sets
  `OwnerRecap.acked_at = NOW()` on the most recent row for that chat id.
- `/explain <line_number>` — owner replies this to drill in. Bot parses
  `<N>` against the most recent recap's body, fetches the matching
  `StockEntry` or `OrderItem` row, and replies with full context.

Both commands fail with "owner-only" if the chat id is not in
`OWNER_TELEGRAM_CHAT_IDS`.

## Verification

1. `build_daily_recap()` unit tests with mocked `Order` / `OrderItem` /
   `StockEntry` queries — verify the four sections appear in the right
   order with the right totals.
2. End-to-end APScheduler test: fire at a fixed time (e.g. set
   `OWNER_RECAP_HOUR=15`, `OWNER_RECAP_MINUTE=30`, wait for the next
   15:30 Paris, assert the message was sent and `OwnerRecap` row was
   written).
3. DST transition test: at the spring-forward boundary (last Sunday of
   March), the 23:30 Europe/Paris job fires exactly once (not skipped,
   not duplicated).
4. `/ack` end-to-end: owner replies `/ack` → `OwnerRecap.acked_at` set
   → bot replies "Acknowledged".
5. `/explain <N>` end-to-end: write a recap with 3 voids → owner replies
   `/explain 2` → bot replies with the full `StockEntry` + linked
   `Order` + linked `OrderItem`.
6. Disabled-state test: `OWNER_TELEGRAM_CHAT_IDS=` empty → scheduler
   still fires `build_daily_recap()` (cheap) but sends to zero chat
   ids. `OwnerRecap` row is written with `chat_id = NULL`.
7. Recap on a closed day: zero `Order` rows → recap body is "Closed
   today — see you tomorrow." No noise.
8. Existing tests still green.

## Rollback path

Set `OWNER_TELEGRAM_CHAT_IDS=` (empty) in `.env` and restart — scheduler
still fires `build_daily_recap()` (cheap, single SELECT) but the bot
sends to zero chat ids. To fully rollback: drop the `OwnerRecap` table
(migration downgrade), remove the new files, remove the scheduler job
registration. No upstream feature is broken by removing this.

## Dependencies

- No new pip dependencies.
- **Required upstream features**:
  - feature 37 (`void-rationale-ledger-field`) — supplies the
    `rationale` column on `StockEntry`. Without 37, the recap's
    "Voids with reasons" section degrades to "(legacy — no rationale
    recorded)" for every row. This contract **lists 37 as a
    prerequisite and will refuse to ship without it**.
  - feature 04 (cook Telegram bot) — supplies the bot instance +
    `bot.send_message()` primitive.
  - feature 26 (`reorder-point-on-stockentry`) — supplies the
    tomorrow's-prep-alerts query.
- **Required downstream features**: none.