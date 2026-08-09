# Feature 50 — Lifecycle Citation Mixin (`lifecycle_state` + `superseded_by_id` chain on `StockEntry`)

> **Priority**: P2 · **Effort**: S (≤1 day) · **Source**: brainstorm 2026-08-09 (cross-section pick B) · **Bucket**: v2 (state machine)
> **One-line**: Add a `LifecycleState` enum + `LifecycleCitationMixin` SQLModel mixin that gives any append-only entity a first-class `lifecycle_state` (`entered/active/superseded/voided`), a `superseded_by_id` chain, an `audit_citation` free-text field, and a new cook-bot `/void` and `/reweigh` command pair — so the *what replaced what* audit is a first-class graph edge, not a free-text footnote.

## Goal

The existing `StockEntry` row has `entered` (row created) → `consumed` (cook decrements via a later row) → `voided` (row written with negative delta + rationale from feature 37). What it does NOT have is a first-class *superseded* state — when the cook re-weighs a batch and discovers the original count was wrong (e.g. the original 4 kg of ricotta turns out to be 3.6 kg after the cook tips out the water), today the original row stays at its old value with a free-text `notes` field pointing at the replacement; the *link* between the two rows is implicit and the operator has to read both rows to discover the relationship.

`paragon-ux/UCF-RS` (pushed 2026-07-31T18:43:32Z, 0★, "Local, source-clean **citation tracking** for code — attach durable, **auditable citations** to file/line ranges without touching source, with explicit **lifecycle states**, offline sync, and deterministic exports. Python stdlib only.") is a *citation-tracking* primitive that solves the same problem in code: "explicit **lifecycle states**, auditable citations without touching source". Translated to LE31, this is a small `LifecycleState` enum + `LifecycleCitationMixin` SQLModel mixin: `lifecycle_state: Literal["entered","active","superseded","voided"]`, `superseded_by_id: int | None`, `superseded_reason: str`, `audit_citation: str | None` (free-text, e.g. "voided per /void command at 21:14 by cook_id=42"). Reuses the rationale pattern from feature 47 (now ~1 day of work instead of half a day) and extends it to cover *supersession*, the one state machine the operator actually needs.

Inspired by today's brainstorm: GitHub `topic:append-only` repo `paragon-ux/UCF-RS` (pushed 2026-07-31T18:43:32Z, 0★, "Local, source-clean citation tracking for code — attach durable, auditable citations to file/line ranges without touching source, with explicit lifecycle states, offline sync, and deterministic exports. Python stdlib only."). The repo comes from the *developer-tools / code-citation-tracking* world — completely outside hospitality — and shares the LE31 *append-only ledger* primitive, but adds *explicit lifecycle states*. Translated to LE31, this is the missing *lifecycle-state machine* layer on top of `StockEntry`.

Distinct from feature 30 (`append-only-audit-redirect`) because 30 is the *redirect*; this is the *state machine*. Distinct from feature 37 (`void-rationale-ledger-field`) because 37 is the *per-event rationale* on voids; this is the *state transition* (entered → superseded → voided) between rows. Distinct from feature 47 (`decision-rationale-mixin`) because 47 is the *rationale field*; this is the *lifecycle state* + the *supersession chain*. **None** of the three model *state transitions* between rows — Pick B does.

## Evidence / JTBD

When the cook voids a batch or re-weighs it (the original count was wrong), the owner wants to see *what replaced what* in the audit log, but currently the voided row stays at its old value with no link to the replacement, so that an explicit `lifecycle_state` (`entered/active/superseded/voided`) + `superseded_by_id` chain on `StockEntry` makes the supersession a first-class audit row, not a free-text footnote.

## Scope

**In scope (v2):**
- A new `LifecycleState` enum in `backend/app/models/lifecycle_state.py`: `class LifecycleState(str, Enum): ENTERED = "entered"; ACTIVE = "active"; SUPERSEDED = "superseded"; VOIDED = "voided"`.
- A new `LifecycleCitationMixin` SQLModel mixin in `backend/app/models/mixins/lifecycle_citation.py`:
  - 4 SQLModel columns: `lifecycle_state: LifecycleState = Field(default=LifecycleState.ENTERED)`, `superseded_by_id: Optional[int] = Field(default=None)`, `superseded_reason: Optional[str] = Field(default=None, max_length=500)`, `audit_citation: Optional[str] = Field(default=None, max_length=500)`.
  - 1 helper method: `def mark_superseded(self, by_id: int, reason: str) -> None` that sets `lifecycle_state = SUPERSEDED`, `superseded_by_id = by_id`, `superseded_reason = reason`, and `audit_citation = f"superseded by row {by_id} ({reason})"`. (The new row is the *replacement* and is itself an `ENTERED` row.)
  - 1 helper method: `def mark_voided(self, reason: str) -> None` that sets `lifecycle_state = VOIDED`, `audit_citation = f"voided ({reason})"`. (The void is recorded on the *new* row with negative `delta_qty`; the existing row is left at its current state. The chain is: original row stays `ACTIVE`, void row is `ENTERED` then `VOIDED` — but the convention is that the void row's `audit_citation` points at the original row.)
  - 1 Pydantic validator: `validate_lifecycle_consistency` that raises `ValueError` if `lifecycle_state == SUPERSEDED` and `superseded_by_id is None`, or if `lifecycle_state == ACTIVE` and `superseded_by_id is not None`.
- A new Alembic migration: `add_lifecycle_columns_to_stockentry` — adds the four columns to `StockEntry` (nullable for back-fill).
- A new back-fill script: `backend/scripts/backfill_stockentry_lifecycle.py` — for every existing `StockEntry` row, sets `lifecycle_state = ENTERED` if no subsequent `void` row references it, `ACTIVE` if subsequent rows reference it, `VOIDED` if the row has `via = "void"`. Idempotent.
- Two new cook-bot commands:
  - `/void <entry_id> [reason]` — writes a new `StockEntry` row with `delta_qty = -1 * (existing_row.delta_qty)`, `via = "void"`, `lifecycle_state = VOIDED`, `audit_citation = f"voided per /void command at <HH:MM> by cook_id={chat_id} (reason: {reason})"`. The original row is left at `lifecycle_state = ACTIVE` (it is *referenced* by the void row, not *superseded*).
  - `/reweigh <entry_id> <new_qty> [reason]` — writes a new `StockEntry` row with `delta_qty = new_qty - existing_row.delta_qty` (the *delta*, not the absolute), `via = "correction"`, `lifecycle_state = ENTERED`, then calls `mark_superseded(by_id=new_row_id, reason=reason)` on the original row. The chain is: original row `ACTIVE → SUPERSEDED`, new row `ENTERED`. (The new row is the *replacement*.)
- One new query command: `/lifecycle <entry_id>` — returns the full lifecycle graph for the row: "Row <id>: <state>. Superseded by row <N> (reason: ...). Voided by row <N> (reason: ...). <N> rows reference this row." (One line, no follow-up.)
- One new unit test: `backend/tests/test_lifecycle_citation_mixin.py` — covers the mixin, the migration, the back-fill script, the two new bot commands, and the query command. Includes a state-machine test (try an invalid transition like `ENTERED → SUPERSEDED` and assert the validator raises).
- One new short doc: `backend/app/models/mixins/lifecycle_citation/README.md` — 50 lines explaining the state machine, the valid transitions, the difference between `VOIDED` (a *negative* correction) and `SUPERSEDED` (a *positive* replacement), and the runbook for "what to do if a row is in the wrong state".

**Out of scope (v2):**
- No LLM dependency. The state machine is pure Python + Pydantic.
- No retroactive supersession on existing rows. Existing `void` rows get back-filled as `VOIDED`; existing non-void rows get back-filled as `ENTERED` (or `ACTIVE` if a later void row references them). The back-fill is conservative — it never promotes `ENTERED` to `SUPERSEDED` automatically (because the original `notes` field is free-text and we cannot reliably parse it).
- No LLM-based state inference. The state transitions are explicit user actions — `/void` and `/reweigh` are the only paths.
- No change to the `via` enum semantics — but a new `via = "correction"` value is added to support `/reweigh`.
- No change to feature 49 (`postledger-tamper-evident-hash`) — the hash chain covers the new rows the same way it covers the old rows. The state machine is a *logical* layer; the hash chain is a *cryptographic* layer.

## Description

The state machine is a 4-state directed graph:

```
              ┌─────────────┐
              │   ENTERED   │  (default state on row creation)
              └──────┬──────┘
                     │ (no automatic transition — row is "active in the ledger" the moment it's written)
                     ▼
              ┌─────────────┐
              │    ACTIVE   │  (the row is in the live ledger; subsequent rows may reference it)
              └──────┬──────┘
                     │ /reweigh writes a new row and marks this one
                     ▼
              ┌─────────────┐
              │ SUPERSEDED  │  (this row was replaced by row N; the replacement is the truth)
              └─────────────┘

              ┌─────────────┐
              │   VOIDED   │  (this row is a void row; the original row it voids is left as ACTIVE)
              └─────────────┘
```

The state machine is intentionally **not** an automatic state machine — the transitions are explicit user actions (`/reweigh`, `/void`) or the back-fill script. The operator never sees an unexpected state change.

The supersession chain is a *graph*, not a *list*: a row can be superseded by exactly one row, but a row can be the *target* of multiple supersessions (if the cook re-weighs the same batch twice). The query command `/lifecycle <id>` walks the graph in both directions and returns the full picture.

## Data model

```sql
ALTER TABLE stockentry ADD COLUMN lifecycle_state VARCHAR(16) NOT NULL DEFAULT 'entered';
ALTER TABLE stockentry ADD COLUMN superseded_by_id BIGINT;
ALTER TABLE stockentry ADD COLUMN superseded_reason VARCHAR(500);
ALTER TABLE stockentry ADD COLUMN audit_citation VARCHAR(500);
CREATE INDEX ix_stockentry_lifecycle_state ON stockentry (lifecycle_state);
CREATE INDEX ix_stockentry_superseded_by_id ON stockentry (superseded_by_id);
```

The two new indexes are the fast-path for the `/lifecycle` query (find all rows in a given state, find all rows superseded by a given row).

The `via` enum is extended with `"correction"` to support `/reweigh`. The back-fill script sets `lifecycle_state = "entered"` for existing rows (the conservative default — see Open Questions).

## Implementation steps

1. **New file**: `backend/app/models/lifecycle_state.py` — `LifecycleState` enum.
2. **New file**: `backend/app/models/mixins/lifecycle_citation.py` — `LifecycleCitationMixin` SQLModel mixin with the four columns, the two helper methods, and the validator.
3. **New file**: `backend/app/models/mixins/lifecycle_citation/README.md` — short doc.
4. **New file**: `backend/app/migrations/versions/2026_08_09_add_lifecycle_columns_to_stockentry.py` — Alembic migration that adds the four columns + the two indexes + extends the `via` enum.
5. **New file**: `backend/scripts/backfill_stockentry_lifecycle.py` — back-fill script.
6. **New file**: `backend/app/bot/commands/void.py` — `/void <entry_id> [reason]` command.
7. **New file**: `backend/app/bot/commands/reweigh.py` — `/reweigh <entry_id> <new_qty> [reason]` command.
8. **New file**: `backend/app/bot/commands/lifecycle.py` — `/lifecycle <entry_id>` query command.
9. **New file**: `backend/tests/test_lifecycle_citation_mixin.py` — unit tests.
10. **Refactor**: `backend/app/models/stockentry.py` — `class StockEntry(LifecycleCitationMixin, DecisionRationaleMixin, SQLModel, table=True): ...` (one-line refactor; no schema change for the rationale columns).
11. **Verify**: `pytest backend/tests/test_lifecycle_citation_mixin.py` passes; the cook-bot commands work end-to-end on a fresh dev DB.

## Telegram interaction

Three new cook-bot commands:
- `/void <entry_id> [reason]` (cook-only). Writes the void row and replies: `OK ✓ voided row <id> via row <N> (reason: <reason>).` (One line.)
- `/reweigh <entry_id> <new_qty> [reason]` (cook-only). Writes the correction row, marks the original as SUPERSEDED, and replies: `OK ✓ row <id> superseded by row <N> (new qty: <new_qty>, reason: <reason>).` (One line.)
- `/lifecycle <entry_id>` (cook-only). Returns the full lifecycle graph. (One line, formatted as "Row <id>: <state>. Superseded by row <N> (reason: ...). <N> rows reference this row." If the row has no supersession, the second sentence is omitted.)

No new waiter-side interaction. The state machine is cook-only — the waiter doesn't void or reweigh; the waiter just *sells* (which decrements existing rows via a later `consumed` row).

## Dependencies

- Existing `sqlmodel` (already a dep).
- Existing `pydantic` v2 (already a dep).
- Existing `alembic` (already a dep).
- Existing `pytest` (already a dep).
- Existing `aiogram` v3 (already a dep).
- **No new packages.**

## Failure / recovery

- **If a row is in the wrong state** (e.g. an existing `void` row was back-filled as `ENTERED`): the operator runs the back-fill script again with `--force` to re-classify. The script is idempotent.
- **If `/reweigh` is called with a `new_qty` that's the same as the existing `delta_qty`**: the bot replies `No change — new_qty matches existing row.` and writes no row.
- **If `/reweigh` is called on a row that's already `SUPERSEDED`**: the bot replies `Row <id> is already superseded by row <N>. Void the replacement instead?` and writes no row. (The operator can then `/void` the replacement.)
- **If `/void` is called on a row that's already `SUPERSEDED`**: the bot replies `Row <id> is superseded by row <N>. Void the replacement instead?` and writes no row.
- **If the `via` enum extension breaks an existing row**: the Alembic migration uses `ALTER TYPE ... ADD VALUE 'correction'` (Postgres) which is non-blocking. The migration is reversible.

## Definition of done

- `StockEntry` has the four new columns + the two new indexes + the `via = "correction"` enum value.
- The `LifecycleCitationMixin` is wired into `StockEntry`.
- The three new bot commands work end-to-end on a fresh dev DB.
- The back-fill script runs on production and exits 0.
- The unit test suite passes (including the state-machine test that tries an invalid transition).
- The `lifecycle_citation/README.md` doc is in the repo.
- The change is committed and pushed to `main`.

## Open questions

1. **Should the back-fill script try to parse existing `notes` fields to detect past supersessions?** Lean: no. Existing `notes` is free-text and the parse-error rate would be high. The conservative `ENTERED` default is the right call; the operator can re-classify rows manually via a future `/lifecycle` admin command.
2. **Should `/reweigh` accept a negative `new_qty` (i.e. *reduce* the batch)?** Lean: no. `/reweigh` is for corrections to a positive count; reductions go through `/void` + a fresh `prep` row.
3. **Should the state machine also include `CANCELED` (the row was never real, e.g. a misclick)?** Lean: no for v2. CANCELED is a `void` with a different `via` value; adding it as a state would be premature.
4. **Should the supersession chain be traversable in the manager dashboard (the existing `index.html` reports view)?** Lean: as a follow-up. The `/lifecycle` cook-bot command is the v2 path; the manager dashboard is a v3 enhancement.
5. **Should feature 49's `prev_hash` / `row_hash` chain include the `lifecycle_state` field in the canonical JSON?** Lean: yes. The lifecycle state is part of the row's truth. The canonical JSON in feature 49 is updated to include `lifecycle_state` (and the new `superseded_by_id` and `superseded_reason` and `audit_citation` fields). The hash chain is therefore aware of the state machine.

## Why this matters

LE31's existing `StockEntry` ledger is a *list* — every row is a flat fact, and the *relationship* between rows is implicit in the `delta_qty` sign and the `via` enum. Adding a `lifecycle_state` + `superseded_by_id` chain turns the list into a *graph* with explicit parent-child edges.

The supersession edge is the most-cited *correction* scenario: the cook re-weighs a batch and discovers the original count was wrong. Today the operator has to read both rows (the original and the correction) to discover the relationship. With the lifecycle chain, the `/lifecycle <id>` query returns the full graph in one line. With the supersession edge in the canonical JSON, feature 49's hash chain also protects the *state* of every row, not just its contents.

The cost is one new mixin + one migration + three new bot commands + one test suite — about 1 day of work. The benefit is that the owner can answer "what is the current state of this batch?" in one command, and the answer is *a graph edge*, not "I trust the cook's notes".
