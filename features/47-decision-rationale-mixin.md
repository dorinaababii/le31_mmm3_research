# Feature 47 — Decision Rationale Mixin

> **Priority**: P2 · **Effort**: XS (≤1 day) · **Source**: brainstorm 2026-08-08 (cross-section pick B) · **Bucket**: v2 (utility)
> **One-line**: A new `DecisionRationaleMixin` (Python SQLAlchemy declarative mixin) + matching Alembic migration helper that any future append-only entity can mix in to get the `rationale` / `rationale_set_at` / `rationale_set_by_chat_id` audit chain that feature 37 hand-rolled for `StockEntry`.

## Goal

Today the "decision rationale" pattern is hand-rolled in feature 37 (`void-rationale-ledger-field`) for `StockEntry` only:

```python
class StockEntry(SQLModel, table=True):
    ...
    rationale: Optional[str] = Field(default=None, max_length=500)
    rationale_set_at: Optional[datetime] = Field(default=None)
    rationale_set_by_chat_id: Optional[int] = Field(default=None)
    via: str = Field(default="manual")  # enum: manual|void|comp|substitution|...
```

The same pattern is needed for comps, supplier-order cancellations (feature 16), inventory variances (feature 15), and any future append-only entity that needs a "why" field. Today each feature would hand-roll the same three columns + the same SQLAlchemy listener + the same prompt wording. A new `DecisionRationaleMixin` (Python SQLAlchemy declarative mixin) + matching Alembic migration helper captures the recurring shape so any feature can `class SupplierOrder(DecisionRationaleMixin, SQLModel, table=True): ...` and inherit the column + prompt + audit chain.

Inspired by today's brainstorm: GitHub `topic:append-only` repo `S0tman/irp-capture` (pushed 2026-08-01T17:24:01Z, **3★**, "An append-only ledger that records why decisions were made"). The repo comes from the *general programming / project-management* world — completely outside hospitality — and shares the same primitive: a *generic* decision-rationale template that any append-only entity can use. Translated to LE31, this is the missing *abstraction* that lets all future features reuse the same field+prompt+audit chain.

Distinct from feature 37 (`void-rationale-ledger-field`) because 37 is the *first user* of the rationale pattern (for `StockEntry` voids); this is the *abstraction* that lets feature 16, feature 15, and any future append-only entity reuse it without re-inventing the pattern.

## Evidence / JTBD

When the implementer adds a new feature that needs an append-only `Why` field, the implementer wants to reuse the rationale pattern instead of inventing it fresh, but currently there's no shared pattern, so that a `DecisionRationaleMixin` SQLAlchemy helper + Alembic migration template is the contract — any future entity can mix in the rationale pattern in 5 minutes instead of re-implementing the same three columns.

## Scope

**In scope (v2 utility):**
- A new Python file `backend/app/models/mixins.py` defining `class DecisionRationaleMixin`:
  - 3 SQLModel columns: `rationale: Optional[str] = Field(default=None, max_length=500)`, `rationale_set_at: Optional[datetime] = Field(default=None)`, `rationale_set_by_chat_id: Optional[int] = Field(default=None)`.
  - 1 helper method: `def set_rationale(self, rationale: str, *, by_chat_id: int | None = None) -> None` that sets all three fields atomically.
  - 1 class-level discriminator: `__rationale_required__: bool = False` (default `False`; subclasses can override) — used by the validator below.
  - 1 Pydantic validator: `validate_rationale_required` that raises `ValueError` on insert if `__rationale_required__ is True and rationale is None`.
- A new Alembic migration helper `backend/app/migrations/templates/decision_rationale_mixin.py` — a string template that can be included in any future migration to add the three columns.
- A new short doc `backend/app/models/mixins/README.md` — 50 lines explaining the pattern, when to use it, and how to migrate from the existing hand-rolled `StockEntry.rationale` field.
- A new unit test `backend/tests/test_decision_rationale_mixin.py` — covers the helper method, the validator, and the migration template.
- A backward-compatibility shim: feature 37's `StockEntry` is updated to inherit from `DecisionRationaleMixin` (no schema change; the columns were already there). This is a 5-line refactor.

**Out of scope (v2 utility):**
- Backporting `DecisionRationaleMixin` to features 15, 16, 22, 25, 28, 31, 33, 39 etc. — each is a separate feature that can opt in *if* the implementer wants the rationale audit chain. The mixin is just the primitive; the opt-in is per-feature.
- A new "rationale view" or "rationale API" — the v1 form is the column + the helper. Surfacing rationale in `/notes` or `/recap` is per-feature.
- A change to `StockEntry.via` semantics — the existing `via` enum stays in feature 37. The mixin only adds the three columns + the helper.
- LLM-based rationale generation — no LLM. The mixin is pure data.

## Description

The rationale pattern is a recurring shape: every *append-only* entity that affects money or stock needs a `rationale` field that is *required* under certain conditions (e.g. negative deltas, cancellations, variances) and *optional* otherwise. The pattern also needs a `rationale_set_at` timestamp and a `rationale_set_by_chat_id` audit chain (the same author tracking pattern as feature 37's `void-rationale-ledger-field`).

The mixin is the smallest abstraction that captures this shape without imposing semantics. The semantics (whether `rationale` is required, whether the prompt is "OK ✓ <reason> for <entity> logged") are per-feature opt-in via `__rationale_required__` and the existing feature's bot prompt.

## Data model

The mixin adds 3 columns to whatever table inherits it:

```sql
ALTER TABLE <table> ADD COLUMN rationale VARCHAR(500);
ALTER TABLE <table> ADD COLUMN rationale_set_at TIMESTAMPTZ;
ALTER TABLE <table> ADD COLUMN rationale_set_by_chat_id BIGINT;
```

The Alembic migration helper creates the three columns + the same `before_update` SQLAlchemy listener that feature 37 has on `StockEntry` (immutability: once set, the `rationale` and the two metadata fields are not updated).

## Implementation steps

1. **New file**: `backend/app/models/mixins.py` — defines `DecisionRationaleMixin` as described above. Pydantic v2 validator pattern (same as `StockEntry`).
2. **New file**: `backend/app/migrations/templates/decision_rationale_mixin.py` — Alembic migration template that adds the three columns + the immutability listener to a target table.
3. **New file**: `backend/app/models/mixins/README.md` — short doc.
4. **New file**: `backend/tests/test_decision_rationale_mixin.py` — unit tests.
5. **Refactor**: `backend/app/models/stock_entry.py` — `class StockEntry(DecisionRationaleMixin, SQLModel, table=True): ...` (5-line refactor, no schema change).
6. **Verify**: `pytest backend/tests/test_decision_rationale_mixin.py` passes; `pytest backend/tests/test_stock_entry.py` still passes (backward-compat).

## Telegram interaction

No new bot commands. The mixin is a back-end primitive; the bot commands that *use* the rationale field are per-feature (e.g. feature 37's "OK ✓ void logged" for `StockEntry`, feature 16's "OK ✓ delivery cancelled" for `SupplierOrderDelivery`).

## Dependencies

- Existing `sqlmodel` (already a dep).
- Existing `pydantic` v2 (already a dep).
- Existing `alembic` (already a dep).
- Existing `pytest` (already a dep).
- **No new packages.**

## Open questions

1. **Should the mixin also include `rationale_author_role`** (cook / owner / system)? Lean: yes, but as text not enum (keep the mixin interface minimal). Deferred to feature 46 (havemind-decision-notes) which already adds `author_role` to `DecisionNote`. The two primitives are complementary.
2. **Should the migration helper be opt-in or auto-applied** to all future append-only entities? Lean: opt-in (the implementer adds `from app.models.mixins import DecisionRationaleMixin` when the feature needs it). Auto-apply is invasive.
3. **Should the mixin also include `rationale_tags`** (free-text tags)? Lean: no — feature 46's `DecisionNote` already has `tags_csv`. The mixin is the smallest primitive; tags are per-feature.
4. **Should the immutability listener be opt-in or always-on**? Lean: always-on. The mixin is rationale *audit*; immutability is the core of audit.

## Why this matters

The LE31 cookbook will grow from 45 features to ~100 over the next 18 months. Roughly 30 of those will be *append-only entities* (stock entries, comps, delivery receipts, inventory variances, gift-card transactions, reservation deposits, supplier orders, etc.). Each one will need a *why* field. Without the mixin, each feature hand-rolls the same three columns + the same SQLAlchemy listener + the same prompt wording. With the mixin, each new feature is one line: `class SupplierOrderDelivery(DecisionRationaleMixin, SQLModel, table=True): ...`. Total implementation cost: 1 day, 1 new file, 1 migration template, 50-line doc, 1 backward-compat refactor. Total operational value: ~30 future features get the rationale audit chain for free, in 5 minutes instead of 1 day. This is documentation-as-code: the rationale pattern is captured once, written once, and reused forever.
