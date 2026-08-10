# drailver-handoff-protocol — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/52-drailver-handoff-protocol.md` before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `52`
- Slug: `drailver-handoff-protocol`
- Contract file: `features/52-drailver-handoff-protocol.md`
- Bucket: v2 owner-pains
- Linear parent: HMM-57 (Brainstorm 2026-08-10 — daily)
- Linear sub-issue: HMM-58 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "LE31 gate verdict per idea" → Pick A.
**Decision: build.** Evidence precondition: **inferred** (the shift-change
context-loss pain is universal in single-restaurant operations; today's
`Dawil/draiver` documents the cross-section pattern). Confidence:
**medium** for the pattern, **low** for the specific solution shape.
The cost is tiny (~1 day, mostly reusing feature 49's primitives) so the
build is justified.

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

- `backend/app/models/stockentry.py` — add 3 new columns (`is_shift_anchor`, `prev_anchor_hash`, `anchor_hash`).
- `backend/app/models/shift_anchor.py` (NEW) — `to_anchor_canonical_json`, `compute_anchor_hash`, `verify_shift_anchors`, `VerifyResult` dataclass.
- `backend/app/models/shift_anchor_listener.py` (NEW) — `@event.listens_for(StockEntry, "before_insert")` that fires only when `is_shift_anchor=true` and calls `compute_anchor_hash`. Coexists with feature 49's row-hash listener.
- `backend/app/models/shift_metadata.py` (NEW) — `compute_shift_metadata(session, from_dt, to_dt) -> dict` — pure Python SQL queries for voids, 86's, top movers, prep shortfalls.
- `backend/app/migrations/versions/2026_08_10_add_shift_anchor_columns_to_stockentry.py` (NEW) — Alembic migration adding 3 columns + 1 partial unique index + 1 CHECK constraint.
- `backend/app/bot/commands/shift_close.py` (NEW) — `/shift close [cook_id]` cook-bot command.
- `backend/app/bot/commands/shift_open.py` (NEW) — `/shift open <cook_id>` cook-bot command.
- `backend/app/bot/commands/verify_shifts.py` (NEW) — `/verify shifts [from_date] [to_date]` cook-bot command.
- `backend/scripts/verify_shift_anchors.py` (NEW) — CLI verifier.
- `backend/tests/test_shift_anchor_chain.py` (NEW) — unit tests (listener + metadata + bot commands + verifier + tamper test).
- `backend/app/models/shift_anchor.md` (NEW) — short doc.
- `backend/app/main.py` — register the new listener on app startup (1 line, alongside feature 49's row-hash listener).

## Endpoints and contracts added

**No new HTTP endpoints.** No new SQLModel tables. The shift-anchor chain is
additive on the existing `StockEntry` table.

**New bot commands** (cook-only, chat-id in `TELEGRAM_ALLOWED_USERS`):
- `/shift close [cook_id]` — outgoing cook. Writes an anchor row, replies with the shift recap.
- `/shift open <cook_id>` — incoming cook. Reads the previous anchor's `anchor_hash`, writes the new anchor, replies with the previous shift's recap.
- `/verify shifts [from_date] [to_date]` — runs the chain verifier. Replies "OK ✓ <N> anchors verified" or "✗ BROKEN at anchor row <id>".

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above.
2. **Migration**: `alembic upgrade head` on dev + staging — the new
   columns, the partial unique index, and the CHECK constraint must be
   created without error.
3. **Round-trip close/open smoke**: in the cook bot, run
   `/shift close cook-A` then `/shift open cook-B` — both must succeed
   and reply with the expected recap.
4. **Verify**: run `/verify shifts` — must reply "OK ✓ <N> anchors
   verified".
5. **CLI**: `python -m backend.scripts.verify_shift_anchors` — must
   exit 0 with "Chain OK (<N> anchors verified)".
6. **Tamper test**: in a test DB, manually edit an anchor row's
   `void_count` and run the verifier — must report BROKEN with the
   anchor row id, the expected `anchor_hash`, and the recomputed
   `anchor_hash`. The unit test `test_tamper_detection` covers this.
7. **Regression**: confirm features 03 (`kitchen-stock-tracker`), 37
   (`void-rationale-ledger-field`), 47 (`decision-rationale-mixin`),
   and 49 (`postledger-tamper-evident-hash`) are unaffected by the new
   columns (the new listener fires only when `is_shift_anchor=true`;
   feature 49's listener still fires on every row; the existing tests
   must still pass).

## Rollback / feature-removal path

- `alembic downgrade -1` — drops the three columns, the partial unique
  index, and the CHECK constraint.
- Delete `backend/app/models/shift_anchor.py`, `shift_anchor_listener.py`,
  `shift_metadata.py`, the migration, the three bot commands, the CLI,
  the test, and the doc.
- Remove the listener registration from `backend/app/main.py`.
- No data loss: the three columns are additive; existing `StockEntry`
  rows are unaffected (their `is_shift_anchor` is `false` after rollback,
  but the original row contents are unchanged).
- No upstream feature broken by removing the shift chain.

## What remains safe if removed

- The append-only `StockEntry` invariant is enforced by convention
  (no UPDATE/DELETE statements in the codebase) — the shift chain was
  additive, not foundational.
- Feature 37's `rationale` field is unaffected.
- Feature 47's `DecisionRationaleMixin` is unaffected.
- Feature 49's row-hash chain is unaffected (the row-hash listener
  fires independently of the shift-anchor listener).
- The Telegram cook surface is unaffected.
- The privacy invariant is preserved (no guest identity, no LLM).

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-57)
back to the research-side Hermes before implementing. If they
conflict, **stop and ask** — do not silently rename.
