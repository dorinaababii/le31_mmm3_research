# append-only-audit-redirect — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/30-append-only-audit-redirect.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `30`
- Slug: `append-only-audit-redirect`
- Contract file: `features/30-append-only-audit-redirect.md`
- Bucket: v2 owner-pains (integrity check; stdlib-only)
- Linear parent: HMM-24 (Brainstorm 2026-08-04 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build (hard-scoped to 5 tables).** No failed checks.

Evidence precondition: **inferred** (HN `append-only-ledger` returned
**0 hits** in the 30-day window — recorded honestly; GitHub
`topic:append-only` surfaced multiple repos; OpenAlex "Digital innovation
strategy" paper in window). Confidence: **medium**.

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
backend/app/main.py                          # nothing (audit hook is in db.py)
backend/app/models.py                        # new OwnerAuditEvent SQLModel
backend/app/audit.py                         # NEW — canonical_json, compute_hash, make_event, verify_chain
backend/app/db.py                            # extend with after_flush hook on operational models
backend/app/bot/cook_bot.py                  # add /audit [days] command
backend/app/bot/cook_bot_audit.py            # NEW — /audit handler
backend/app/templates/owner.html             # if feature 29 is shipped; show chain badge
backend/README.md                            # note the new command
```

No new dependencies (uses only `hashlib` from stdlib). No Alembic
migration (charter §3.2 — `init_db()` for v1).

## Endpoints and contracts added

No new HTTP endpoints. One new cook-bot command:

- `/audit [days]` — default 7, max 30. Single-line reply:
  - `audit OK: N events, chain valid (last event <ts>)` on success
  - `audit BROKEN: chain break at event <id> (<ts>): expected
    prev_hash=<a>, got <b>` on failure

One new table:

```
OwnerAuditEvent  (id, event_type TEXT, source_table TEXT, source_id BIGINT,
                  payload_json TEXT NOT NULL, prev_hash TEXT NULL,
                  this_hash TEXT NOT NULL, created_at TIMESTAMPTZ NOT NULL
                  DEFAULT now())
```

Audited tables (writes only): `Visit`, `Order`, `OrderItem`, `Bill`,
`StockEntry`. Other tables (`MenuItem`, `Table`, `Batch`, etc.) are
excluded by design.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn pins from features 25 + 27 resolve.
3. **Schema**: `init_db()` creates the `OwnerAuditEvent` table if
   absent.
4. **Run**: `uvicorn app.main:app --reload`.
5. **Trigger writes**: seat a party (`POST /api/visits`), add an
   item, bill it, write a `StockEntry`. Each commit must produce one
   corresponding `OwnerAuditEvent` row.
6. **Initial audit**: in Telegram (cook role), `/audit 7` → "audit
   OK: N events, chain valid".
7. **Tamper**: open psql → `UPDATE stockentry SET qty_delta = 999
   WHERE id = 1;`.
8. **Detect**: `/audit 7` → "audit BROKEN: chain break at event <id>
   (<ts>): expected prev_hash=<a>, got <b>".
9. **Restore**: roll back the tamper → `/audit 7` → STILL BROKEN (the
   chain detects payload edits to the audit row, not just the source
   row). This is correct behaviour.
10. **Reset (manual)**: operator may `TRUNCATE ownerauditevent RESTART
    IDENTITY` to start a fresh chain; the chain id starts at 1 again
    and the next `/audit` reports "audit OK".
11. **Regression**: confirm existing flows (seat, order, serve, bill,
    tip) still work, that no operational model is broken, and that
    the `after_flush` hook does not introduce measurable latency
    (< 5 ms per commit is the budget).

## Rollback / feature-removal path

- Drop the `OwnerAuditEvent` table from `backend/app/models.py`.
- Delete `backend/app/audit.py`.
- Remove the `after_flush` hook from `backend/app/db.py`.
- Remove the `/audit` command from `backend/app/bot/cook_bot.py`.
- No data migration needed; no data retention — `OwnerAuditEvent`
  rows are throwaway.

## What remains safe if removed

- No customer data, no historical state. The `OwnerAuditEvent` table
  contains only SHA-256 hashes and JSON payloads of operational
  events — no PII.
- The append-only `StockEntry` ledger is unaffected.
- The explicit-state rule is unaffected.
- The owner can simply stop issuing `/audit` and the system behaves
  exactly as before; the hook still writes audit rows, but no one
  reads them.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-24)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.