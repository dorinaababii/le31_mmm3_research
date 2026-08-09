# havemind-decision-notes — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/46-havemind-decision-notes.md` before touching any code. Do
> not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `46`
- Slug: `havemind-decision-notes`
- Contract file: `features/46-havemind-decision-notes.md`
- Bucket: v2-AI (no-LLM core, optional LLM digest in v3)
- Linear parent: HMM-50 (Brainstorm 2026-08-08 — daily)
- Linear sub-issue: HMM-51 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build (v2-AI, no-LLM core).** No failed checks.

Evidence precondition: **observed** (1 in-window GitHub repo —
`MikolajSapek/havemind` pushed 2026-08-07T19:47:12Z — shares the
shared-audit-trail-for-team-and-AI pattern). Confidence: **medium**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/main.py                                  # include the new router; register the new bot commands
backend/app/models/decision_note.py                  # NEW — DecisionNote SQLModel
backend/app/models/__init__.py                       # re-export DecisionNote
backend/app/models/mixins.py                         # import here for sibling-feature reuse (or rely on feature 47)
backend/app/services/decisions.py                    # NEW — compute_decision_digest, insert/list helpers
backend/app/routers/decisions.py                     # NEW — GET /api/decisions/list + /api/decisions/week
backend/app/bot/commands.py                          # add cmd_note, cmd_notes_list, cmd_notes_tag, cmd_notes_week
backend/app/bot/startup.py                           # add _maybe_send_start_of_service_digest
backend/app/scheduler.py                             # add weekly_decision_digest cron
backend/app/templates/notes.md.j2                    # NEW — Jinja2 markdown digest template
alembic/versions/2026_08_08_havemind_decision_notes.py   # NEW — creates decision_note table
backend/tests/test_decisions.py                      # NEW — append-only, /note roundtrip, /notes list filter, /notes week, start-of-service hook
backend/README.md                                    # note the new endpoints + bot commands
```

No new dependencies. `apscheduler` is already a dep (feature 39);
`uuid4` is stdlib.

## Endpoints and contracts added

- `GET /api/decisions/list?date=YYYY-MM-DD` (owner-only, via `require_user`).
  Returns JSON: `{"date": "...", "notes": [{"decision_id": "...", "body": "...", "author_chat_id": ..., "author_role": "cook|owner", "effective_from": "...", "expires_at": "...", "tags": ["..."]}]}`.
- `GET /api/decisions/week` (owner-only). Returns the 7-day digest.
- Cook-bot `/note <body>` — chat-id in `TELEGRAM_ALLOWED_USERS`.
  Bot writes one `DecisionNote` row with `effective_from=now()`, `expires_at=now()+24h` (default), `author_role=cook|owner` (inferred from chat-id), and replies "OK ✓ note <head> logged as <decision_id>".
- Cook-bot `/note <body> keep` — same but `expires_at=NULL` (persistent).
- Cook-bot `/note <body> 7d` — same but `expires_at=now()+7d`.
- Cook-bot `/note <body> #tag1 #tag2` — regex-parses tags, stores `tags_csv="#tag1 #tag2"`.
- Cook-bot `/notes` — list today's notes.
- Cook-bot `/notes YYYY-MM-DD` — list notes for that date.
- Cook-bot `/notes tag:<tag>` — filter by tag.
- Cook-bot `/notes week` — owner-only weekly digest.

One new table:

```sql
CREATE TABLE decision_note (
  id              BIGSERIAL PRIMARY KEY,
  decision_id     UUID NOT NULL UNIQUE,
  body            TEXT NOT NULL,
  author_chat_id  BIGINT NOT NULL,
  author_role     TEXT NOT NULL CHECK (author_role IN ('cook','owner')),
  effective_from  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  expires_at      TIMESTAMPTZ,
  tags_csv        TEXT NOT NULL DEFAULT '',
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_decision_note_effective_from ON decision_note (effective_from);
CREATE INDEX idx_decision_note_tags ON decision_note USING gin (string_to_array(tags_csv, ' ') array_ops);
```

Append-only invariant: SQLAlchemy `@event.listens_for` `before_update` and `before_delete` raise `RuntimeError` on the `DecisionNote` table. The only mutable fields are `effective_from` and `expires_at` at insertion time (set explicitly via the `insert` helper).

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn + apscheduler pins resolve.
3. **Schema**: `alembic upgrade head` applies the new migration; `init_db()` creates the `decision_note` table if absent.
4. **Run**: `uvicorn app.main:app --reload`.
5. **Cook writes**: in Telegram (cook role), `/note we 86 the lamb on slow days` → "OK ✓ note d-7f3a1c logged. Expires in 24h."
6. **Cook lists**: `/notes` → "Today's notes (1): <NN:MM> cook: we 86 the lamb on slow days".
7. **Owner writes**: in Telegram (owner role), `/note Tuesdays we open at 18:00 not 18:30 #schedule keep` → "OK ✓ note d-7f3a1d logged. Tags: schedule. Persistent."
8. **Owner lists weekly**: `/notes week` → "Last week's notes (2): ...".
9. **Start-of-service hook**: send any message as cook after 06:00 Europe/Paris → bot auto-replies "Today's notes (N): <one-line per body>".
10. **Append-only**: in a Python REPL, attempt `session.execute(update(DecisionNote).values(body='hacked'))` → expect `RuntimeError: append-only invariant`.
11. **Weekly cron**: trigger the cron job manually (`apscheduler.run_job('weekly_decision_digest')`) → owner chat-id receives the digest.
12. **Regression**: confirm existing flows (seat, order, serve, bill, void, prep) still work and that the existing role checks still gate the cook bot.

## Rollback / feature-removal path

- Drop the `decision_note` table from the database (`alembic downgrade -1`).
- Delete `backend/app/models/decision_note.py` and remove the import from `models/__init__.py`.
- Delete `backend/app/services/decisions.py`.
- Delete `backend/app/routers/decisions.py` and remove its `include_router` from `main.py`.
- Delete `backend/app/templates/notes.md.j2`.
- Remove the new bot commands from `backend/app/bot/commands.py`.
- Remove the start-of-service hook from `backend/app/bot/startup.py`.
- Remove the weekly cron from `backend/app/scheduler.py`.
- Delete `backend/tests/test_decisions.py`.
- No data migration needed; no data retention — `DecisionNote` rows are throwaway.

## What remains safe if removed

- The append-only `StockEntry` ledger is unaffected.
- The bot still works for any existing command.
- The existing waiter UI and cook bot are unaffected.
- The privacy invariant is preserved: `DecisionNote` stores no guest identity, no PII.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-50)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.
