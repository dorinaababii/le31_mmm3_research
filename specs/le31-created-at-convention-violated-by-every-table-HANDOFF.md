# HANDOFF — 429-le31-created-at-convention-violated-by-every-table

> **Slice contract for the coding agent.** Produced by the 97th LE31 daily-brainstorm pass (2026-11-03), Pick A.
>
> **Feature file**: `features/429-le31-created-at-convention-violated-by-every-table-first-party-the-module-docstring-says-all-tables-have-created-at-and-not-one-table-does-v1-schema-creation-timestamp-convention.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema, built with `SQLModel.metadata.create_all` on a throwaway SQLite file and inspected with `sqlalchemy.inspect`). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod, same SQLModel code), §7 (the quality bar: *"Time is UTC"*, *"No magic numbers"*, *"No dead code"*, *"End-to-end before commit"*), the truth invariant.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done* (which requires the **actual path** to be exercised, not merely a passing test).
4. **Read `features/430-…` FIRST** and resolve the `created_at` / `added_at` collision described under *Frozen contract* below. **Do not ship both a `created_at` and an `added_at` on `order_item`.**
5. **Decide option (a) or option (b)** — add the columns, or correct the docstring — and **record the choice in the commit message**.
6. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_docstring_convention_matches_schema`: it parses the module docstring and asserts that if the docstring claims *"All tables have created_at"*, then every table does.
7. **Not touch** the stock ledger, the tip formula, the bill path, the shift path, or any other contract's territory.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Add `created_at` or `updated_at` to `stock_entry`.** Charter §4.3: *"EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE."* An `updated_at` on an append-only table is a contradiction. **That is feature 421's** territory (the append-only linter rule).
- **Add a `business_date` / `service_date` column.** That is **feature 405**.
- **Add an insertion-time column to `order_item`.** That is **feature 430** — and adding *both* is the specific collision this handoff exists to prevent.
- **Change `Batch.expires_at`, `Visit.closed_at`, `Bill.paid_at`, `Shift.opened_at` or `Shift.closed_at`.** This slice adds a column; it does not redefine an existing business timestamp.
- **Backdate existing rows with invented timestamps.** No historical insertion times exist; the migration instant is the honest answer and must be recorded.
- **Introduce Alembic.** `alembic>=1.13` is already in `requirements.txt` — **do not silently activate it.** Charter §3.2: *"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)."*
- **Enable `PRAGMA foreign_keys`** or add a foreign key. That is **feature 427**.
- **Change `MenuItem.category`.** That is **feature 431**.
- **Derive `created_at` from `id`.** They are different facts. `id` is a surrogate key.

**Disambiguation**: this slice is about **the schema-wide convention that every table records when its row was created**. It is **not** about the *service day* (405), **not** about the *order line's* insertion time (430), **not** about the *ledger* (374, 421), and **not** about the *menu category* (431).

## Frozen contract

**The one thing this contract exists to make true:** *`backend/app/models.py` must not state a convention that its own schema contradicts.*

Concretely, after this slice lands, one of these is true — and the commit message says which:

- **(a) Honour it.** Every one of the ten tables carries `created_at`, and the mutable ones carry `updated_at`. The docstring at line 10 is then true.
- **(b) Correct it.** The docstring at line 10 is amended to describe what the schema actually does, naming the exceptions (`stock_entry` uses `at`; business events use their own columns). Nothing else changes.

**The prohibition:** *the docstring must not continue to claim a convention the schema does not follow.* Leaving the contradiction in place is the failure this contract exists to prevent.

**The load-bearing test**, which must be written **before** the change and watched to fail:

```python
def test_docstring_convention_matches_schema():
    """If models.py claims every table has created_at, every table must have it."""
    src = open(MODELS, encoding="utf-8").read()
    doc = src.split('"""')[1]              # module docstring
    claims = "all tables have created_at" in doc.lower()
    tables = inspect(engine).get_table_names()
    with_created = [t for t in tables if "created_at" in cols_of(t)]
    if claims:
        assert len(with_created) == len(tables), (
            "docstring claims every table has created_at; "
            f"{len(tables) - len(with_created)} of {len(tables)} do not: "
            f"{sorted(set(tables) - set(with_created))}")
```

**This test is worth more than the migration.** Without it, the contradiction returns the next time someone adds a table.

## Files to touch

| File | Change |
|---|---|
| `backend/app/models.py` | Option (a): add `created_at` (+ `updated_at` where mutable) to the ten classes, following the file's existing `Column(DateTime(timezone=True))` pattern. Option (b): amend the `Conventions:` block at line 10 **only**. |
| `backend/app/db.py` | The `init_db()` path — **no Alembic**. Option (a) only. |
| `backend/tests/test_created_at_convention.py` *(new)* | The three tests: the convention test above, `test_every_table_has_created_at`, `test_no_table_has_unexpected_updated_at` (asserts `stock_entry` does **not** have `updated_at`). |

**Do not create** a `backend/app/services/` package in this slice — **feature 430** and **feature 374** expect one to exist, and three contracts creating the same package in one week is friction. If option (a) needs a helper, put it in `backend/app/config.py` or inline it in the model module.

## Mandatory LE31 skill list

The agent must load these **before** writing code:

- **`le31-conventions`** — the seven-check feature gate and the hard invariants (§3.2 the fixed stack and the `init_db()` policy; §4.1 the dialect rule; §7 the quality bar; the truth invariant; *Known conflicts*).
- **`le31-v1-feature-pattern`** — the canonical contract shape, the slicing rules, and the *Definition of Done* (which requires the **actual path** to be exercised, not merely a passing test).
- **`le31-handoff-spec`** — the frozen-contract discipline.
- **`le31-research`** — the source-of-truth discipline behind the quotes in the feature file.

The agent must **NOT** load `le31-feature-pipeline` — the slice is already in the pipeline.

**The mandatory reading list** (read; do **not** merge):

| Document | Why it must be read |
|---|---|
| `features/430-…-v1-order-item-insertion-time.md` | **The nearest sibling in the whole corpus, and it touches the same table.** It decides whether `order_item`'s creation time is `created_at` or `added_at`. |
| `features/405-…-v1-service-day-boundary-and-business-date.md` | Owns the *business* date. Read it so this slice does not open it. |
| `features/421-…-v1-ledger-append-only-mechanism.md` | Owns `stock_entry`'s append-only status. Read it so this slice does not add `updated_at` to an append-only table. |
| `features/427-…-v1-sqlite-fk-enforcement.md` and `features/426-…` | Schema-level work on the same file. Neither owns timestamps. |
| `features/431-…-v1-category-canonicalisation.md` | This pass's other contract. Independent — but read it so the two do not drift in style. |
| `PROJECT_CHARTER.md` §3.2, §4.1, §4.3, §7, §8 | The source of truth. |
| `backend/app/models.py` lines 1-25 | **The docstring this contract is about.** Read it verbatim before changing anything in that file. |

## Mandatory inputs

- **The defect itself** — the docstring at `backend/app/models.py` line 10, verbatim:

  ```
  - All tables have created_at; only mutable ones get updated_at.
  ```

- **The measured fact** — executed against LE31's real schema on 2026-11-03:

  ```
  tables_total              10
  tables_with_created_at    []
  tables_with_updated_at    []
  tables_with_NO_timestamp_at_all  ["app_user", "derived_tip", "menu_item", "table_"]
  convention_fully_honoured false
  ```

- **The re-runnable probe** — `/opt/data/_bs_probe_body2_2026-11-03.py` builds LE31's schema, inspects it, and prints the same numbers. The agent may re-run it (it needs a venv with `sqlmodel`; one exists at `/opt/data/le31-verify-2026-10-27/.venv` — **reuse it, do not provision a new one**).

## Verification protocol reference

`PROJECT_CHARTER.md` §8 is the protocol; this slice's specific sequence is:

1. **Write the test first.** `test_docstring_convention_matches_schema` — watch it **FAIL** (it must fail on the unfixed code; a test that only ever passed proves nothing).
2. Apply the change (option a or b).
3. **Watch the test PASS.**
4. **Re-run the whole test suite** — this slice must not break another slice's test.
5. **Exercise the actual path**: start the app (`cd backend && uvicorn app.main:app --reload`), confirm `http://localhost:8000/docs` loads, and confirm the schema in the running app has the columns (`sqlite3 backend/restaurant.db ".schema"`).
6. **Re-run the probe** and confirm `tables_with_created_at` is `[]`-or-complete according to the option chosen, and that `convention_fully_honoured` is `true` under option (a).
7. `git add -p && git commit -m "Feature 429: <option (a) or (b)> — <one line>"` — **the commit message must name the option.**

**Manual verification is acceptable for v1** (charter §7: *"Tests are not required for v1. Manual verification via curl + the mock-up is acceptable."*) — **but** the regression test in this contract **is** required, because it is the thing that stops the contradiction returning. The charter's exemption is about proving a feature works, not about skipping a test that guards a stated invariant.

## Rollback path

- **Option (a)**: drop the added columns. **No data is lost** — the columns were added empty and populated by default; removing them restores the previous schema exactly. On an existing dev database, drop and re-create (`init_db()`); on prod, the reverse migration is a `DROP COLUMN`.
- **Option (b)**: revert the docstring change. One line. **Nothing else changes.**
- **Either way**: the change is confined to `backend/app/models.py` (+ `db.py` + a test file). **No router, no bot handler, no UI, no external call.** The blast radius is the schema and one test file.

**Note on the dev database**: charter §3.2 uses `init_db()`, so a dev database is disposable — drop and re-create. **Record the prod-migration step as known debt** in the commit message; it is the standing debt of the v1 `init_db()` policy, not a new debt introduced here.

## Sign-off gap

- **⚠️ The owner has not chosen option (a) or option (b).** Both are correct; they differ in cost (nine-to-seventeen columns and a migration vs. one line of docstring). **Default recorded: option (a)** — honour the convention — because the convention is right and the schema should catch up. **But this is an owner decision and the agent should implement the default and say so clearly in the commit message.**
- **⚠️ `app_user`'s mutability is undecided** (default recorded: give it both `created_at` and `updated_at`).
- **⚠️ `derived_tip`'s redundancy is undecided** (default recorded: give it `created_at` anyway; one column, and the convention stays true without an exception clause).
- **⚠️ Existing rows get the migration instant, not their true insertion time.** No historical data exists to reconstruct it. **This must be stated in the commit message** — a reader must not later mistake the migration instant for a business fact.
- **⚠️ The 429/430 collision is unresolved until one of them lands.** If both land in the same week, the second must be adjusted. **The agent must read 430 before writing code.**

## Handoff summary

| | |
|---|---|
| **Feature** | 429 — the `created_at` convention, violated by all ten tables |
| **Verdict** | `build` (OBSERVED — executed against LE31's real schema) |
| **Bucket** | v1 — schema hygiene, on the path to the first working slice |
| **Files to touch** | `backend/app/models.py`, `backend/app/db.py`, `backend/tests/test_created_at_convention.py` (new) |
| **New dependency** | none |
| **Reversible** | yes — additive columns, or a one-line docstring amendment |
| **Hard prerequisite** | none — but **read feature 430 first** to resolve the `order_item` column collision |
| **Must not touch** | `stock_entry` (append-only), `Batch.expires_at`, `Visit.closed_at`, `Bill.paid_at`, the bill path, the shift path, `MenuItem.category` |
| **Known debt created** | the prod migration for the added columns (the standing `init_db()`-not-Alembic debt) |
