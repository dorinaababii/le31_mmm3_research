# telegram-prep-checkoff-adherence — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/43-telegram-prep-checkoff-adherence.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `43`
- Slug: `telegram-prep-checkoff-adherence`
- Contract file: `features/43-telegram-prep-checkoff-adherence.md`
- Bucket: v1 polish (extends existing cook bot + existing recap)
- Linear parent: HMM-49 (Brainstorm 2026-08-07 — daily, created by this run)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build.** (v1 polish, ≤1 day.) No failed checks.

Evidence precondition: **observed** (1 in-window GitHub repo —
`QuinnQuak/telegram-accountability-bot` pushed **today** 2026-08-07 —
shares the Telegram honor-system task accountability pattern).
Confidence: **medium-high**.

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
backend/app/models.py                                # NEW: PrepTask + PrepCheckoff SQLModel
backend/app/services/prep.py                         # NEW: compute_prep_adherence()
backend/app/services/recap.py                        # EXTEND: prep-adherence section in build_daily_recap()
backend/app/bot/cook_bot_prep.py                     # NEW: /done, /skipped, /prep list command handlers
backend/app/routers/prep.py                          # NEW: POST/GET/PATCH /api/prep/tasks
backend/app/main.py                                  # NEW: include_router(prep.router)
backend/app/events/prepcheckoff_append_only.py       # NEW: append-only listener for PrepCheckoff + PrepTask
backend/alembic/versions/<new>_prep_checkoff.py      # NEW migration
backend/README.md                                    # note the new bot commands + API endpoints
```

No new pip dependencies.

## Endpoints and contracts added

**Bot commands (cook-only, existing `TELEGRAM_ALLOWED_USERS` allowlist):**

- `/done <prep_task_id>[,<prep_task_id>...]` — parses comma-separated
  ids, writes one `PrepCheckoff` row per id with `via=done`.
- `/skipped <prep_task_id> <reason…>` — writes one `PrepCheckoff`
  row with `via=skipped, reason=<reason>`.
- `/prep list` — replies with today's `PrepTask` rows + status +
  adherence-so-far.

All three fail with "cook-only" if chat-id is not in
`TELEGRAM_ALLOWED_USERS`.

**API endpoints (owner-only):**

- `POST /api/prep/tasks` — body: `{service_date, name, deadline_at}`.
  Creates one `PrepTask` row.
- `GET /api/prep/tasks?service_date=<YYYY-MM-DD>` — returns the day's
  `PrepTask` rows + computed adherence score.
- `PATCH /api/prep/tasks/<id>` — body: `{name?, deadline_at?}`.
  Adjusts a task before its first check-off.

Both bot and API endpoints reuse the existing owner-only guard pattern
(chat-id check for bot, JWT check for API).

**Two new SQLModel tables:**

```python
# backend/app/models.py
class PrepTask(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    service_date: date = Field(index=True)
    name: str = Field(max_length=200)
    deadline_at: datetime
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    # Append-only on creation; mutable only on deadline_at (before first check-off).

class PrepCheckoff(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    prep_task_id: int = Field(foreign_key="preptask.id", index=True)
    checked_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    checked_by_chat_id: int = Field(index=True)
    via: str = Field(max_length=10)  # "done" | "skipped"
    reason: str | None = Field(default=None, max_length=500)
```

Append-only listener (`prepcheckoff_append_only.py`):
- `PrepCheckoff`: rejects any UPDATE or DELETE (raises
  `IntegrityError`); the table is fully immutable.
- `PrepTask`: rejects UPDATE on `service_date` or `name` after the
  first `PrepCheckoff` is written for that task; `deadline_at` is
  mutable only while no check-off exists.

**One new Alembic migration:**

```python
def upgrade():
    op.create_table(
        "preptask",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("service_date", sa.Date, nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("deadline_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_preptask_service_date", "preptask", ["service_date"])

    op.create_table(
        "prepcheckoff",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("prep_task_id", sa.Integer, sa.ForeignKey("preptask.id"), nullable=False),
        sa.Column("checked_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("checked_by_chat_id", sa.BigInteger, nullable=False),
        sa.Column("via", sa.String(10), nullable=False),
        sa.Column("reason", sa.String(500), nullable=True),
    )
    op.create_index("ix_prepcheckoff_prep_task_id", "prepcheckoff", ["prep_task_id"])
    op.create_index("ix_prepcheckoff_checked_by_chat_id", "prepcheckoff", ["checked_by_chat_id"])

def downgrade():
    op.drop_index("ix_prepcheckoff_checked_by_chat_id", table_name="prepcheckoff")
    op.drop_index("ix_prepcheckoff_prep_task_id", table_name="prepcheckoff")
    op.drop_table("prepcheckoff")
    op.drop_index("ix_preptask_service_date", table_name="preptask")
    op.drop_table("preptask")
```

**One new service function:**

```python
# backend/app/services/prep.py
def compute_prep_adherence(service_date: date) -> dict:
    """Return per-service adherence stats for the given date.

    Returns:
        {
            "service_date": <YYYY-MM-DD>,
            "total_tasks": <N>,
            "done_count": <M>,         # via=done with checked_at <= deadline_at
            "late_count": <K>,         # via=done with checked_at > deadline_at
            "skipped_count": <J>,      # via=skipped
            "pending_count": <N-M-K-J>,
            "on_time_pct": <float 0-100>,
        }
    """
```

**Recap extension (feature 39):**

The existing `build_daily_recap()` in `services/recap.py` is extended
with a new section inserted after "Voids with reasons":

```python
def build_daily_recap() -> str:
    # ... existing covers, voids, top 3 movers sections ...

    # NEW: prep adherence section
    adherence = compute_prep_adherence(date.today())
    if adherence["total_tasks"] > 0:
        body += (
            f"\n✅ Prep adherence: {adherence['done_count']}/{adherence['total_tasks']}"
            f" done ({adherence['on_time_pct']:.0f}%),"
            f" {adherence['skipped_count']} skipped:\n"
        )
        # List skipped tasks with reasons
        for task in fetch_skipped_tasks(date.today()):
            body += f"  • {task.name} — skipped — \"{task.reason}\"\n"

    # ... existing prep alerts section ...
```

The recap gracefully omits the prep-adherence section if no `PrepTask`
rows exist for the day.

## Verification

1. `compute_prep_adherence()` unit tests with mocked `PrepTask` +
   `PrepCheckoff` rows — verify on-time / late / skipped / pending
   counts and `on_time_pct`.
2. Bot command tests: `/done 1` writes one row with `via=done`;
   `/done 1,2,3` writes three rows; `/skipped 4 ran out` writes one
   row with `via=skipped`; `/prep list` returns today's tasks +
   status.
3. Cook-only allowlist test: a non-allowlisted chat-id hits `/done 1`
   → bot replies "cook-only"; no row written.
4. Idempotency test: `/done 1` twice for the same task → only one
   `PrepCheckoff` row written (the second is a no-op).
5. API endpoint tests: `POST /api/prep/tasks` creates a row;
   `GET /api/prep/tasks?service_date=2026-08-07` returns the day's
   tasks + adherence; `PATCH /api/prep/tasks/1` updates
   `deadline_at` (before any check-off).
6. Recap integration test: with `PrepTask` + `PrepCheckoff` rows in
   the DB, the recap body includes the prep-adherence section.
   Without those rows, the section is omitted cleanly.
7. Recovery path test: cook runs `/done 1,2,3` after service → 3
   rows written, adherence score reflects the audit chain.
8. Append-only listener test: `UPDATE PrepCheckoff SET reason='x'
   WHERE id=1` raises `IntegrityError`. `DELETE FROM PrepCheckoff
   WHERE id=1` raises `IntegrityError`.
9. End-to-end observed: a real service runs for 4 hours → cook
   uses `/done` and `/skipped` during service → owner receives
   recap at 23:30 with the prep-adherence section.
10. Existing tests still green.

## Rollback path

Drop the `PrepCheckoff` and `PrepTask` tables (migration downgrade),
remove the new bot command handlers, remove the new API router, remove
the recap extension. No upstream feature is broken by removing this.
The recap falls back to its pre-extension shape (no prep-adherence
section).

## Dependencies

- No new pip dependencies.
- **Required upstream features**:
  - feature 04 (cook Telegram bot) — supplies the bot instance +
    `TELEGRAM_ALLOWED_USERS` allowlist.
  - feature 39 (`owner-daily-recap-telegram`) — supplies the
    `build_daily_recap()` function that the prep-adherence section
    extends.
- **Required downstream features**: none.
