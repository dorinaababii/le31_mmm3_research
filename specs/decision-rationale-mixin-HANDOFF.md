# decision-rationale-mixin — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/47-decision-rationale-mixin.md` before touching any code. Do
> not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `47`
- Slug: `decision-rationale-mixin`
- Contract file: `features/47-decision-rationale-mixin.md`
- Bucket: v2 (utility)
- Linear parent: HMM-50 (Brainstorm 2026-08-08 — daily)
- Linear sub-issue: HMM-52 (created, status Backlog, label `Feature`, project `le31 v1 — Core MVP`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build (v2 utility).** No failed checks.

Evidence precondition: **observed** (1 in-window GitHub repo —
`S0tman/irp-capture` 3★, pushed 2026-08-01T17:24:01Z — shares the
reusable decision-rationale template pattern). Confidence: **medium**.

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
backend/app/models/mixins.py                                          # NEW — DecisionRationaleMixin
backend/app/models/mixins/README.md                                   # NEW — 50-line doc
backend/app/models/stock_entry.py                                     # refactor: inherit from DecisionRationaleMixin (no schema change)
backend/app/migrations/templates/decision_rationale_mixin.py          # NEW — Alembic migration template
backend/app/migrations/README.md                                      # note the new template
backend/tests/test_decision_rationale_mixin.py                        # NEW — unit tests
backend/README.md                                                    # note the new mixin
```

No new dependencies. All deps already in `requirements.txt`.

## Endpoints and contracts added

- **No new endpoints.** The mixin is a back-end model primitive only.
- **No new bot commands.** Features that use the mixin add their own bot commands per their scope.
- **No new schema** for the existing `stock_entry` table (the columns were already there from feature 37; the refactor is a 5-line change of the parent class).

One new file with the mixin shape:

```python
# backend/app/models/mixins.py
from datetime import datetime
from typing import Optional
from pydantic import field_validator
from sqlmodel import Field, SQLModel


class DecisionRationaleMixin(SQLModel):
    rationale: Optional[str] = Field(default=None, max_length=500)
    rationale_set_at: Optional[datetime] = Field(default=None)
    rationale_set_by_chat_id: Optional[int] = Field(default=None)

    # Subclasses may set this to True to require rationale on insert.
    __rationale_required__: bool = False

    @field_validator("rationale", mode="before")
    @classmethod
    def _validate_required(cls, v, info):
        # If the subclass declared the rationale field required, raise on None.
        if info.data.get("__rationale_required__") and v is None:
            raise ValueError("rationale is required for this entity")
        return v

    def set_rationale(self, rationale: str, *, by_chat_id: int | None = None) -> None:
        """Set rationale + metadata atomically. Idempotent for same rationale."""
        self.rationale = rationale
        self.rationale_set_at = datetime.utcnow()
        if by_chat_id is not None:
            self.rationale_set_by_chat_id = by_chat_id
```

One new migration template:

```python
# backend/app/migrations/templates/decision_rationale_mixin.py
"""Alembic migration template for the DecisionRationaleMixin.

Usage in a future migration:

    from app.migrations.templates.decision_rationale_mixin import add_decision_rationale_columns

    def upgrade():
        add_decision_rationale_columns(op, "<table_name>")

    def downgrade():
        op.drop_column("<table_name>", "rationale_set_by_chat_id")
        op.drop_column("<table_name>", "rationale_set_at")
        op.drop_column("<table_name>", "rationale")
"""
from alembic import op
import sqlalchemy as sa


def add_decision_rationale_columns(op, table_name: str) -> None:
    op.add_column(table_name, sa.Column("rationale", sa.String(500), nullable=True))
    op.add_column(table_name, sa.Column("rationale_set_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column(table_name, sa.Column("rationale_set_by_chat_id", sa.BigInteger, nullable=True))
```

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm sqlmodel + pydantic v2 + alembic pins resolve.
3. **Refactor**: `git diff backend/app/models/stock_entry.py` — confirm
   the change is exactly 5 lines: `class StockEntry(DecisionRationaleMixin, SQLModel, table=True): ...` and the three hand-rolled
   `rationale*` fields are removed.
4. **Run**: `uvicorn app.main:app --reload` — confirm the app starts
   without an OperationalError on the `stock_entry` table.
5. **Backward-compat**: `pytest backend/tests/test_stock_entry.py` — all
   existing tests pass. The rationale field is still on `StockEntry`,
   still optional, still recorded by the existing bot command (feature 37).
6. **Mixin unit tests**: `pytest backend/tests/test_decision_rationale_mixin.py` — all new tests pass:
   - `set_rationale` sets all three fields atomically.
   - `__rationale_required__=True` subclasses raise `ValueError` on insert with `rationale=None`.
   - The Alembic migration template can be applied to a test table.
7. **Subclass opt-in**: write a one-off test that defines `class DummyComp(DecisionRationaleMixin, SQLModel, table=True): __rationale_required__ = True` and inserts `DummyComp(rationale=None)` → expect `ValueError`.
8. **Migration template**: write a one-off test that runs `add_decision_rationale_columns(op, "_test_decision_rationale")` on a SQLite in-memory engine, then drops the table; expect no errors.
9. **Regression**: confirm existing flows (seat, order, serve, bill, void) still work and that the existing rationale prompt (feature 37) still records `rationale` on `StockEntry`.

## Rollback / feature-removal path

- Delete `backend/app/models/mixins.py` and `backend/app/models/mixins/README.md`.
- Delete `backend/app/migrations/templates/decision_rationale_mixin.py`.
- Delete `backend/tests/test_decision_rationale_mixin.py`.
- Revert the 5-line refactor in `backend/app/models/stock_entry.py` (re-add the three hand-rolled `rationale*` fields).
- No data migration needed; no schema change. `StockEntry` rows are unaffected.

## What remains safe if removed

- The `stock_entry.rationale` field is unaffected (the columns were already there).
- The existing bot command (feature 37) still records rationale.
- No new endpoints means no new API surface to deprecate.
- The privacy invariant is preserved: the mixin adds no PII columns.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-50)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.
