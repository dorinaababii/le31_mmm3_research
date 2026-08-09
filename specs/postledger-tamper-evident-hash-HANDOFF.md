# postledger-tamper-evident-hash — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/49-postledger-tamper-evident-hash.md` before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `49`
- Slug: `postledger-tamper-evident-hash`
- Contract file: `features/49-postledger-tamper-evident-hash.md`
- Bucket: v2 (audit)
- Linear parent: HMM-52 (Brainstorm 2026-08-09 — daily) [predicted; will be confirmed on issue creation]
- Linear sub-issue: HMM-53 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "LE31 gate verdict per idea" → Pick A.
**Decision: build.** Evidence precondition: **observed** (1 in-window GitHub
repo — `shuaige121/postledger` 0★, pushed 2026-08-08T18:22:04Z — documents the
tamper-evident-hash-chain pattern). Confidence: **medium** for the pattern
existence, **low** for "we need to migrate today" — but the cost is tiny
(~1 day) so the build is justified.

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

- `backend/app/models/stockentry.py` — add 2 nullable columns (`prev_hash`, `row_hash`).
- `backend/app/models/stockentry_hash.py` (NEW) — `to_canonical_json`, `compute_row_hash`, `verify_chain`, `VerifyResult` dataclass.
- `backend/app/models/stockentry_listeners.py` (NEW) — `@event.listens_for(StockEntry, "before_insert")` listener.
- `backend/app/migrations/versions/2026_08_09_add_prev_hash_row_hash_to_stockentry.py` (NEW) — Alembic migration adding 2 columns + 1 unique index.
- `backend/scripts/backfill_stockentry_hash.py` (NEW) — back-fill script.
- `backend/scripts/verify_stockentry_chain.py` (NEW) — CLI verifier.
- `backend/app/bot/commands/verify_ledger.py` (NEW) — `/verify ledger [date]` cook-bot command.
- `backend/tests/test_stockentry_hash_chain.py` (NEW) — unit tests (listener + back-fill + CLI + bot + tamper test).
- `backend/app/models/stockentry_hash.md` (NEW) — short doc.
- `backend/app/main.py` — register the listener on app startup (1 line).

## Endpoints and contracts added

**No new HTTP endpoints.** No new SQLModel tables. The hash chain is
additive on the existing `StockEntry` table.

**New bot command**: `/verify ledger [date]` (cook-only).
- Default date = today (Europe/Paris).
- OK reply: `OK ✓ <N> rows verified (<from_id>..<to_id>)` (one line, no follow-up).
- Broken reply: `✗ BROKEN at row <id> — expected <expected_short>, got <actual_short>. Investigate.` + a follow-up message with the full `VerifyResult` JSON.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above.
2. **Migration**: `alembic upgrade head` on dev + staging — the new
   columns and the unique index must be created without error.
3. **Back-fill**: `python -m backend.scripts.backfill_stockentry_hash`
   on dev — the script must commit every 1000 rows in a transaction
   and exit 0 with "Chain OK after back-fill (<N> rows hashed)".
4. **Verify**: `python -m backend.scripts.verify_stockentry_chain` —
   must exit 0 with "Chain OK (<N> rows verified)".
5. **Bot command**: send `/verify ledger today` in the cook bot (cook
   chat-id) — must reply `OK ✓ <N> rows verified`.
6. **Tamper test**: in a test DB, manually edit a `StockEntry` row's
   `delta_qty` and run the verifier — must report BROKEN with the row
   id, the expected `row_hash`, and the recomputed `row_hash`. The
   unit test `test_tamper_detection` covers this.
7. **Regression**: confirm features 03 (`kitchen-stock-tracker`), 37
   (`void-rationale-ledger-field`), and 47 (`decision-rationale-mixin`)
   are unaffected by the new columns (the listener fires on every
   insert; the existing tests must still pass).

## Rollback / feature-removal path

- `alembic downgrade -1` — drops the two columns and the unique index.
- Delete `backend/app/models/stockentry_hash.py`, `stockentry_listeners.py`, the migration, the two scripts, the bot command, the test, and the doc.
- Remove the listener registration from `backend/app/main.py`.
- No data loss: the two columns are additive; existing `StockEntry`
  rows are unaffected (their `row_hash` is NULL after rollback, but
  the original row contents are unchanged).
- No upstream feature broken by removing the hash chain.

## What remains safe if removed

- The append-only `StockEntry` invariant is enforced by convention
  (no UPDATE/DELETE statements in the codebase) — the hash chain was
  additive, not foundational.
- Feature 37's `rationale` field is unaffected.
- Feature 47's `DecisionRationaleMixin` is unaffected.
- The Telegram cook surface is unaffected.
- The privacy invariant is preserved (no guest identity, no LLM).

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-52)
back to the research-side Hermes before implementing. If they
conflict, **stop and ask** — do not silently rename.
