# void-rationale-ledger-field — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/37-void-rationale-ledger-field.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `37`
- Slug: `void-rationale-ledger-field`
- Contract file: `features/37-void-rationale-ledger-field.md`
- Bucket: v2 owner-pains (web-only + 2 new bot commands; no new client)
- Linear parent: HMM-40 (Brainstorm 2026-08-06 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: build.** No failed checks.

Evidence precondition: **reported** (2 in-window GitHub repos from outside
hospitality — `mazze93/stratum` pushed **today** 2026-08-06T06:48:55Z,
"S0tman/irp-capture" pushed 2026-08-01 — share the decision-rationale ledger
pattern). Confidence: **high**.

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
backend/app/models.py                          # add StockEntry.rationale column + Alembic migration
backend/app/services/stockentry_guard.py       # NEW: assert_rationale_if_negative()
backend/app/routers/stock_rationale.py         # NEW: GET /api/stock/rationale_search
backend/app/routers/orders.py                  # extend /api/orders/{id}/void to require rationale
backend/app/bot/cook_bot_void.py               # NEW: /void <item> <reason> + /86 <item> <reason>
backend/app/templates/waiter_void.html         # extend void modal with required <input>
backend/app/main.py                            # register the new router; extend SSE event payload
backend/app/events/stockentry_append_only.py   # extend listener to forbid UPDATE on rationale
backend/alembic/versions/<new>_rationale.py    # NEW migration: add column + backfill sentinel
backend/README.md                              # note the new column + manager search endpoint
```

No new pip dependencies. Alembic migration is required (the existing
`StockEntry` table needs the new column).

## Endpoints and contracts added

One new column on the existing `StockEntry` table:

```python
rationale: str | None = Field(default=None, max_length=240, index=True)
```

One new HTTP route:

- `GET /api/stock/rationale_search?q=<term>&limit=50` — manager-only
  (reuses the existing manager-cookie guard from feature 29). Returns
  the 50 most recent negative-delta `StockEntry` rows whose `rationale`
  matches `<term>` (case-insensitive `ILIKE %term%`). Returns
  `[{"id": ..., "menu_item_id": ..., "qty_delta": ..., "reason": ...,
    "rationale": ..., "source": ..., "created_at": "..."}]`.

One new model-layer guard:

```python
# backend/app/services/stockentry_guard.py
class RationaleRequiredError(ValueError):
    """Raised when a negative-delta StockEntry is written without a rationale."""

def assert_rationale_if_negative(stockentry: StockEntry) -> None:
    if stockentry.qty_delta < 0:
        if not stockentry.rationale or not stockentry.rationale.strip():
            raise RationaleRequiredError(
                f"rationale required for negative delta (item {stockentry.menu_item_id})"
            )
```

This guard is called from every existing negative-delta write path
inside the same SQLAlchemy session flush, before the row is inserted.

One new Alembic migration:

```python
# backend/alembic/versions/<new>_stockentry_rationale.py

def upgrade():
    op.add_column("stockentry", sa.Column("rationale", sa.String(240), nullable=True))
    op.create_index("ix_stockentry_rationale", "stockentry", ["rationale"])
    # Backfill: existing negative-delta rows get a sentinel rationale
    op.execute(
        "UPDATE stockentry SET rationale = '(legacy — no rationale recorded)' "
        "WHERE qty_delta < 0 AND rationale IS NULL"
    )

def downgrade():
    op.drop_index("ix_stockentry_rationale", table_name="stockentry")
    op.drop_column("stockentry", "rationale")
```

## New cook-bot commands

- `/void <item> <reason...>` — writes one `StockEntry` with
  `qty_delta = -1` (or the item's current batch quantity), `reason = "void"`,
  `rationale = <reason>`. Chat-id allowlisted same as feature 04.
- `/86 <item> <reason...>` — same shape, `reason = "86"`.

Both commands fail with "rationale required — try again" if `<reason>` is
empty (defence in depth — the model-layer guard would also catch it).

## Verification

Per `skills/le31-v1-feature-pattern/SKILL.md` "Definition of Done":

1. Migration runs cleanly on a fresh DB and on a DB with existing
   negative-delta rows (sentinel backfill).
2. `assert_rationale_if_negative` unit tests cover: cook `/void` with
   empty reason (raises), cook `/void` with reason (passes), waiter UI
   void without rationale (raises), waiter UI void with rationale
   (passes), manager comp without rationale (raises).
3. Cook bot end-to-end: `/86 lamb burned` → row written → row visible
   in DB → SSE event fires with `rationale` field.
4. Manager search end-to-end: write 3 negative rows with rationales,
   search for "burned", assert the right row returned.
5. Append-only invariant preserved: any `UPDATE stockentry SET
   rationale = ...` raises (test the SQLAlchemy listener).
6. Backwards-compat: a row with `rationale = "(legacy — no rationale
   recorded)"` is silently treated as "no rationale on file" by the
   search endpoint.

## Rollback path

Drop the `rationale` column. Migration downgrade is shipped alongside
the upgrade. Historical rows lose the column but `qty_delta` /
`reason` / `source` / `created_at` are unaffected. The model-layer
guard is removed in the same PR. The cook bot `/void` and `/86`
commands are removed in the same PR.

## Dependencies

- No new pip dependencies.
- Required upstream: none. This feature is independent.
- Required downstream: feature 39 (`owner-daily-recap-telegram`)
  reads `rationale` to summarise voids in the recap.