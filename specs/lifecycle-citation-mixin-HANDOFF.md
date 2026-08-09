# lifecycle-citation-mixin — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/50-lifecycle-citation-mixin.md` before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `50`
- Slug: `lifecycle-citation-mixin`
- Contract file: `features/50-lifecycle-citation-mixin.md`
- Bucket: v2 (state machine)
- Linear parent: HMM-52 (Brainstorm 2026-08-09 — daily) [predicted; will be confirmed on issue creation]
- Linear sub-issue: HMM-54 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "LE31 gate verdict per idea" → Pick B.
**Decision: build.** Evidence precondition: **observed** (1 in-window GitHub
repo — `paragon-ux/UCF-RS` 0★, pushed 2026-07-31T18:43:32Z — documents the
explicit-lifecycle-states + auditable-citations pattern). Confidence:
**medium** for the pattern, **low** for "we need to migrate today" —
but the cost is tiny (~1 day, reuses feature 47's `DecisionRationaleMixin`
pattern) so the build is justified.

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

- `backend/app/models/lifecycle_state.py` (NEW) — `LifecycleState` enum.
- `backend/app/models/mixins/lifecycle_citation.py` (NEW) — `LifecycleCitationMixin` SQLModel mixin (4 columns, 2 helpers, 1 validator).
- `backend/app/models/mixins/lifecycle_citation/README.md` (NEW) — short doc.
- `backend/app/models/stockentry.py` — `class StockEntry(LifecycleCitationMixin, DecisionRationaleMixin, SQLModel, table=True): ...` (one-line refactor).
- `backend/app/migrations/versions/2026_08_09_add_lifecycle_columns_to_stockentry.py` (NEW) — Alembic migration adding 4 columns + 2 indexes + extending `via` enum with `"correction"`.
- `backend/scripts/backfill_stockentry_lifecycle.py` (NEW) — back-fill script.
- `backend/app/bot/commands/void.py` (NEW) — `/void <entry_id> [reason]` command.
- `backend/app/bot/commands/reweigh.py` (NEW) — `/reweigh <entry_id> <new_qty> [reason]` command.
- `backend/app/bot/commands/lifecycle.py` (NEW) — `/lifecycle <entry_id>` query command.
- `backend/tests/test_lifecycle_citation_mixin.py` (NEW) — unit tests (mixin + migration + back-fill + 3 bot commands + state-machine test).

## Endpoints and contracts added

**No new HTTP endpoints.** No new SQLModel tables. The state machine is
additive on the existing `StockEntry` table.

**New bot commands** (cook-only):
- `/void <entry_id> [reason]` — writes a `StockEntry` with `via = "void"`, `lifecycle_state = VOIDED`, `audit_citation` set, `delta_qty = -1 * existing_row.delta_qty`. Reply: `OK ✓ voided row <id> via row <N> (reason: <reason>).`
- `/reweigh <entry_id> <new_qty> [reason]` — writes a `StockEntry` with `via = "correction"`, `lifecycle_state = ENTERED`, `delta_qty = new_qty - existing_row.delta_qty`, then marks the original row as `SUPERSEDED` pointing at the new row. Reply: `OK ✓ row <id> superseded by row <N> (new qty: <new_qty>, reason: <reason>).`
- `/lifecycle <entry_id>` — returns the full lifecycle graph. Reply: `Row <id>: <state>. Superseded by row <N> (reason: ...). <N> rows reference this row.` (omit the second sentence if no supersession; omit the third if no referencing rows).

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above.
2. **Migration**: `alembic upgrade head` on dev + staging — the 4 new
   columns, 2 new indexes, and the `via` enum extension must be
   created without error.
3. **Back-fill**: `python -m backend.scripts.backfill_stockentry_lifecycle`
   on dev — the script must commit every 1000 rows in a transaction
   and exit 0 with "Lifecycle back-fill complete (<N> rows classified:
   <E> entered, <A> active, <V> voided, <S> superseded)".
4. **State machine test**: `pytest backend/tests/test_lifecycle_citation_mixin.py::test_state_machine` — must pass (the test tries `ENTERED → SUPERSEDED` without `superseded_by_id` and asserts the validator raises).
5. **Bot commands**:
   - `/void 42 "dropped on floor"` (cook chat-id) — must write the void row and reply `OK ✓ voided row 42 via row <N> (reason: dropped on floor).`
   - `/reweigh 42 3.6 "re-weighed after tipping out water"` — must write the correction row, mark the original as SUPERSEDED, and reply `OK ✓ row 42 superseded by row <N> (new qty: 3.6, reason: re-weighed after tipping out water).`
   - `/lifecycle 42` — must reply `Row 42: superseded. Superseded by row <N> (reason: re-weighed after tipping out water). 0 rows reference this row.`
6. **Regression**: confirm features 03 (`kitchen-stock-tracker`), 37
   (`void-rationale-ledger-field`), 47 (`decision-rationale-mixin`), and
   49 (`postledger-tamper-evident-hash`) are unaffected by the new
   columns. The hash chain in feature 49 is updated to include the
   lifecycle state in the canonical JSON — verify the existing
   `test_stockentry_hash_chain` still passes after the update.

## Rollback / feature-removal path

- `alembic downgrade -1` — drops the 4 columns and 2 indexes, removes the `via = "correction"` enum value.
- Delete `backend/app/models/lifecycle_state.py`, the mixin file, the migration, the back-fill script, the 3 bot commands, the test, and the doc.
- Revert the `StockEntry` class to drop the mixin inheritance.
- No data loss: the 4 columns are additive; existing `StockEntry`
  rows are unaffected (their `lifecycle_state` defaults to `ENTERED`
  after rollback).
- No upstream feature broken by removing the state machine.

## What remains safe if removed

- Feature 49's hash chain is unaffected (the canonical JSON update
  is a no-op if the new columns are dropped — the chain will simply
  not include them).
- Feature 47's `DecisionRationaleMixin` is unaffected.
- Feature 37's `rationale` field is unaffected.
- The Telegram cook surface is unaffected (the 3 new commands are
  removed, the existing commands are unchanged).
- The privacy invariant is preserved (no guest identity, no LLM).

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-52)
back to the research-side Hermes before implementing. If they
conflict, **stop and ask** — do not silently rename.
