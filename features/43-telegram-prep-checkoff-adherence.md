# Feature 43 — Telegram Prep Checkoff Adherence

> **Priority**: P1 · **Effort**: S (≤1 day) · **Source**: brainstorm 2026-08-07
> (cross-section pick A) · **Bucket**: v1 polish
> **One-line**: The existing cook Telegram bot (feature 04) gets a new
> `/done <prep_task_id>` and `/skipped <task_id> <reason>` command plus a
> new append-only `PrepCheckoff` SQLModel table. The cook self-marks each
> prep task done (or skipped-with-reason) at the moment of completion;
> the bot records the timestamp. At end-of-service the owner gets a
> **per-service adherence score** (% of prep tasks marked done within
> their deadline window) alongside the existing recap (feature 39).

## Goal

The LE31 owner's most-cited follow-up question after service today is
"did the kitchen actually prep everything on time?" — currently
unanswerable because there is no per-prep-task audit chain, only the
cook's head and the existing prep board (feature 34, static display).
A simple `/done <task_id>` and `/skipped <task_id> <reason>` Telegram
command — paired with a small append-only `PrepCheckoff` table — turns
the prep ritual from "the cook's head" into a queryable audit chain,
and gives the owner a per-service adherence score they can review in
<10 seconds via the existing recap push (feature 39).

Inspired by today's brainstorm: GitHub `topic:telegram-bot` repo
`QuinnQuak/telegram-accountability-bot` (pushed **today** 2026-08-07,
FastAPI + Postgres, "Telegram bot for group task accountability — set
deadlines, mark tasks done on the honor system"). The repo comes from
the group-task / project-management world — completely outside
hospitality — and shares the same primitive: a Telegram bot that lets
the team self-mark tasks done and rolls up an adherence score.
Translated to LE31, this is the missing one-line check-off that turns
the prep ritual into a queryable audit chain.

Distinct from feature 34 (`stockout-prep-board-snapshot`) because 34
is a *static print-grade display*, while this is *interactive check-off
with adherence history*. Distinct from feature 39
(`owner-daily-recap-telegram`) because 39 is a single push at end of
day, while this is the data source for the prep-adherence section of
that recap.

## Evidence / JTBD

When the cook finishes a prep task mid-service, the cook wants to record
that the task is done, but struggles because the prep ritual happens in
30-second bursts between tickets and writing it down takes longer than
doing it, so that a single Telegram `/done <task_id>` from the same
phone the cook is already holding writes the timestamp and rolls up to
an adherence score for the owner.

## Scope

**In scope (v1 polish):**
- A new `PrepTask` SQLModel table (one row per prep task per service):
  `(id, service_date, name, deadline_at, created_at)`. Append-only —
  the only mutable column is `completed_at` and `completed_via`
  (set by `PrepCheckoff` insertion; never updated).
- A new append-only `PrepCheckoff` SQLModel table (one row per
  check-off event):
  `(id, prep_task_id, checked_at, checked_by_chat_id, via, reason)`.
  `via` is enum `done|skipped`. `reason` is required when `via=skipped`,
  optional when `via=done`.
- A new bot command `/done <prep_task_id>` — cook-only (chat-id in
  existing `TELEGRAM_ALLOWED_USERS`). Bot writes one `PrepCheckoff`
  row with `via=done`, replies "OK ✓ <task_name> done at <HH:MM>".
- A new bot command `/skipped <prep_task_id> <reason…>` — cook-only.
  Bot writes one `PrepCheckoff` row with `via=skipped`, replies
  "OK ✓ <task_name> skipped: <reason>".
- A new bot command `/prep list` — cook-only. Bot replies with the
  list of today's `PrepTask` rows + status (done / skipped / pending)
  + adherence-so-far (e.g. "3/5 done, 1 skipped, 1 pending").
- A new derived view `compute_prep_adherence(service_date) -> float`
  in `backend/app/services/prep.py` that returns the per-service
  adherence score: `% of PrepTask rows for that date that have a
  matching PrepCheckoff with via=done AND checked_at <= deadline_at`.
  Tasks with `via=skipped` count as "not done" but distinguished in
  the audit chain.
- An extension to the existing `build_daily_recap()` function (from
  feature 39) to include a new section: **Prep adherence** — the
  per-service score + list of skipped tasks with reasons. Falls back
  gracefully if no `PrepTask` rows exist for the day (omits the
  section cleanly).

**Out of scope (v1 polish):**
- Auto-creating `PrepTask` rows from a recipe / menu template —
  the operator creates them manually via the manager dashboard
  (out of scope, deferred to a follow-up).
- Push reminders when a task is approaching its deadline — the cook
  self-marks; reminders are a v3 follow-up.
- Per-cook adherence breakdown — the v1 score is per-service, not
  per-cook. Per-cook breakdown is a v3 follow-up.
- NLU parsing of free-form "done the lamb prep" text — the cook
  picks from the existing task list (`/prep list`). NLU is forbidden
  on the cook surface per charter §3.2 (no customer-facing AI) and
  §3.3 (AI may assist with non-AI fallback).

## User flow

**Cook — mid-service check-off:**

1. Cook finishes a prep task (e.g. "sauce reduced") and types
   `/done 3` in the existing cook Telegram bot chat.
2. Bot validates that task `3` exists for today's service and is
   not already done. Writes one `PrepCheckoff` row with
   `via=done, checked_at=NOW(), checked_by_chat_id=<cook>`.
3. Bot replies: "OK ✓ sauce reduced done at 19:42 (5 min early).
   2/5 done today. Reply `/prep list` for the full status."

**Cook — skipped with reason:**

1. Cook decides to skip a prep task (e.g. "we ran out of the herb,
   skipping the garnish") and types
   `/skipped 4 out of basil — skipping garnish`.
2. Bot writes one `PrepCheckoff` row with `via=skipped, reason="out of
   basil — skipping garnish"`, replies: "OK ✓ garnish prepped skipped:
   out of basil — skipping garnish. 2/5 done, 1 skipped, 2 pending."

**Owner — end-of-service recap:**

1. At 23:30 Europe/Paris the existing `build_daily_recap()` runs.
2. The recap body now includes a new "Prep adherence" section:
   ```
   ✅ Prep adherence: 4/5 done (80%), 1 skipped:
   • garnish prepped — skipped — "out of basil — skipping garnish"
   ```
3. The recap is sent to the owner via the existing feature 39 pipeline.

**Cook — recovery path (batch at end of service):**

1. Cook realises they did 3 prep tasks but forgot to mark any of them.
   Types `/done 1,2,3` (comma-separated task ids).
2. Bot writes 3 `PrepCheckoff` rows (one per id), all with
   `checked_at=NOW()`. Replies: "OK ✓ 3 tasks marked done: 1, 2, 3.
   5/5 done today."
3. The adherence score for the service is updated (a task marked done
   after its deadline counts as `late`, not `on-time`; the score
   reflects the audit chain truthfully).

## Data model

Two new tables:

```python
# backend/app/models.py (additive)

class PrepTask(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    service_date: date = Field(index=True)
    name: str = Field(max_length=200)
    deadline_at: datetime  # service-local deadline (e.g. 19:30 Europe/Paris)
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    # No updated_at — append-only on creation. completed_at is derived
    # from the latest matching PrepCheckoff row.

class PrepCheckoff(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    prep_task_id: int = Field(foreign_key="preptask.id", index=True)
    checked_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    checked_by_chat_id: int = Field(index=True)
    via: str = Field(max_length=10)  # "done" | "skipped"
    reason: str | None = Field(default=None, max_length=500)
```

`PrepCheckoff` is append-only (same SQLAlchemy listener pattern as
`StockEntry` and `OwnerAuditEvent`). `PrepTask` is append-only on
creation — the only mutable state is `deadline_at` (operator can adjust
before service starts; after the first check-off, deadline is frozen).

No changes to existing models. Reuses the existing
`TELEGRAM_ALLOWED_USERS` cook allowlist, the existing aiogram v3 bot
instance from feature 04, and the existing `build_daily_recap()` from
feature 39 (extended, not replaced).

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**

- New command: `/done <prep_task_id>[,<prep_task_id>...]` —
  cook-only (chat-id in `TELEGRAM_ALLOWED_USERS`). Parses
  comma-separated task ids; writes one `PrepCheckoff` row per id.
- New command: `/skipped <prep_task_id> <reason…>` — cook-only;
  writes one `PrepCheckoff` row with `via=skipped, reason=<reason>`.
- New command: `/prep list` — cook-only; replies with today's
  `PrepTask` rows + status + adherence-so-far.
- No changes to existing bot commands. Cook allowlist guard is the
  existing `TELEGRAM_ALLOWED_USERS` (no new config).

**API (FastAPI):**

- New `POST /api/prep/tasks` endpoint — owner-only. Body:
  `{service_date, name, deadline_at}`. Creates one `PrepTask` row.
- New `GET /api/prep/tasks?service_date=<YYYY-MM-DD>` — owner-only.
  Returns the day's `PrepTask` rows + computed adherence score.
- New `PATCH /api/prep/tasks/<id>` — owner-only. Body:
  `{name?, deadline_at?}`. Adjusts a task before its first check-off.
- Existing routes unchanged. Existing manager dashboard can be
  extended later to render `PrepTask` rows for create/edit (out of
  scope for this contract).

**Recap (extension to feature 39):**

- The existing `build_daily_recap()` function (from feature 39) is
  extended with a new section inserted after "Voids with reasons":
  **Prep adherence** — the per-service score + list of skipped tasks
  with reasons. Falls back gracefully if no `PrepTask` rows exist
  for the day (omits the section cleanly).

## Dependencies

- **No new pip dependencies.**
- **Required upstream features**:
  - feature 04 (cook Telegram bot) — supplies the bot instance +
    `TELEGRAM_ALLOWED_USERS` allowlist.
  - feature 39 (`owner-daily-recap-telegram`) — supplies the
    `build_daily_recap()` function that the prep-adherence section
    extends. The recap can ship without Pick A; Pick A adds the
    prep-adherence section once `PrepTask` + `PrepCheckoff` exist.
- **Required downstream features**: none.

## Failure / recovery

- **Bot command with unknown task id** — bot replies "Task <id> not
  found for today. Reply `/prep list` to see today's tasks." No row
  written.
- **Bot command for already-done task** — bot replies "Task <id>
  already marked done at <HH:MM>. Reply `/prep list` to see today's
  status." No duplicate row written (idempotent on `(prep_task_id,
  via=done)`).
- **Cook marks task done after deadline** — bot still writes the
  `PrepCheckoff` row with `checked_at=NOW()`; the adherence view
  flags it as `late` (counted in `done_count` but not in `on_time_count`).
  The audit chain is preserved — the timestamp speaks for itself.
- **Bot can't reach the cook (network blip)** — the `PrepCheckoff`
  row is not written; the cook retries when the bot is back. No
  silent failure.
- **Manager dashboard not yet wired for `PrepTask` CRUD** — the
  owner creates `PrepTask` rows via the API endpoint directly (curl
  or Postman) until the dashboard is extended. Deferred to a
  follow-up.
- **Recap runs but no `PrepTask` rows exist for the day** — the
  prep-adherence section is omitted cleanly. The owner sees no
  prep-adherence line; no error, no noise.

## Definition of done

- [ ] `PrepTask` and `PrepCheckoff` SQLModel tables added; append-only
      listener extended.
- [ ] Alembic migration for the two tables.
- [ ] Bot commands `/done`, `/skipped`, `/prep list` shipped;
      cook-only allowlist enforced.
- [ ] API endpoints `POST /api/prep/tasks`, `GET /api/prep/tasks`,
      `PATCH /api/prep/tasks/<id>` shipped.
- [ ] `compute_prep_adherence()` function shipped with on-time /
      late / skipped counts.
- [ ] `build_daily_recap()` extended with the prep-adherence section.
- [ ] End-to-end observed: cook runs `/done 3` → `PrepCheckoff` row
      written → bot replies with confirmation → owner receives recap
      at 23:30 with prep-adherence line.
- [ ] Recovery path: cook runs `/done 1,2,3` after service → 3 rows
      written → adherence score reflects the audit chain.
- [ ] No-task graceful fallback: recap on a day with zero `PrepTask`
      rows omits the prep-adherence section cleanly.
- [ ] Existing tests still green.
- [ ] Manual acceptance: in a 7-day pilot, the cook marks ≥80% of
      prep tasks done via `/done` and the owner reads the
      prep-adherence section daily.

## Open questions

- Should the prep-adherence score weight late vs missed? Decision:
  no — v1 score is binary `done|not_done`; a `late` flag is recorded
  on the `PrepCheckoff` row but not surfaced in the v1 score. Weight
  is a v3 follow-up.
- Should the `/prep list` command also show upcoming tasks for the
  next service? Decision: no — v1 is today-only. Tomorrow's tasks
  are a `/prep list tomorrow` follow-up.
- Should the cook see other cooks' check-offs in `/prep list`?
  Decision: yes — v1 shows all cook check-offs (the per-service
  score is shared). Per-cook breakdown is a v3 follow-up.

## Why this matters

LE31's solo operator is also the cook, the manager, and the owner. The
end-of-service paperwork is the friction the operator cites most often
in any pilot. The "did we prep everything on time?" question is the
operator's #1 follow-up after "did we lose money on voids?" — and both
questions get answered in one glance with feature 37's `rationale`
column + this feature's prep-adherence score.

The in-window peer (`QuinnQuak/telegram-accountability-bot`, pushed
**today** 2026-08-07) is the strongest fresh cross-section signal of
the pass: a FastAPI + Postgres Telegram bot for group-task
accountability with deadlines and self-marked done. Translated to
LE31, this is the missing one-line check-off that turns the prep
ritual into a queryable audit chain.

Tiny cost (two new tables + three bot commands + three API endpoints +
one derived view + one recap extension), high value (the operator's
most-cited end-of-service follow-up question). Reuses the existing
bot, the existing allowlist, the existing recap primitive, and the
existing append-only listener pattern.
