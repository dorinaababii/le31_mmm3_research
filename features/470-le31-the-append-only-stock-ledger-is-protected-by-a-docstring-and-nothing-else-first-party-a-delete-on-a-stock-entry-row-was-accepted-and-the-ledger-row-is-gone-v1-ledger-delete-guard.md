# Feature 470 — The append-only stock ledger is protected by a docstring and nothing else: a `DELETE` on a `StockEntry` was accepted and the ledger row is gone

> **Pick B of Daily Research 2026-11-12 (89th pass).** **FIRST-PARTY.** The defect is in LE31's own schema and LE31's own deployment posture. **Evidence class OBSERVED** — reproduced by execution against the real `backend/app/models.py`; the transcript is re-runnable.
>
> **Executed against LE31's real schema (2026-11-12):**
>
> ```
> seeded menu_item id=2, batch id=2, stock_entry id=2
> DELETE menu_item   -> ACCEPTED
>   batches still referencing it: 1
> DELETE stock_entry -> ACCEPTED (the append-only ledger row is gone)
>   stock_entry rows now: 1
> sqlite PRAGMA foreign_keys = 0
> ```
>
> And separately:
>
> ```
> UPDATE stock_entry.qty_delta -> -99 ACCEPTED (reads back -99)
> ```
>
> **The whole schema's constraint census, executed:** `CheckConstraint` instances across all ten tables → **`[]` — not one**. `SQLModel` creates **no triggers**. The `StockEntry` model carries this docstring (`backend/app/models.py:113-118`):
>
> ```python
> class StockEntry(SQLModel, table=True):
>     """Append-only ledger. Never UPDATE or DELETE rows.
>
>     Current stock for a batch = SUM(qty_delta) WHERE batch_id = X.
>     """
> ```
>
> **⭐ THE FINDING IS THE GAP BETWEEN THE WORDING AND THE ENFORCEMENT.** The docstring says *"Never UPDATE or DELETE rows."* The database says *"sure."* The only thing standing between LE31's central ledger invariant and a silent rewrite is a Python comment in a class body.
>
> **⭐ WHY THIS IS NOT A DUPLICATE OF FEATURE 421 — the boundary is exact.** Feature **421** owns **a lint rule**: *"Add a lint rule that rejects an UPDATE or DELETE on StockEntry"*, plus the single write path and a `StockReason` reversal member. That is a **static-analysis** mechanism — and 421's own words describe its guarantee precisely: *"so that the guarantee is checkable by a machine rather than upheld by the fact that nobody has written the mutating code yet."* **The guarantee 421 buys is a Python-code guarantee.** A lint rule does **not** run against a direct database session, a `psql` shell, a migration script, a `sqlite3` CLI, or any process that never goes through the linted Python path. **This feature buys a database guarantee**, and the two are **complementary**: 421 makes the *application* refuse; this makes the *database* refuse.
>
> **The corpus gate:** a sweep for `linter.{0,120}(update|delete).{0,40}stockentry` over all 966 corpus files returns **0 hits** — no feature pairs the lint rule with a database-level guard.

## Goal

Make the ledger's append-only invariant **enforced by the database**, so that a `StockEntry` row cannot be updated or deleted **by any process** — not just by Python code that passed the linter.

The concrete outcome:

1. **A `DELETE` on `stock_entry` is refused by Postgres**, with an error that names the invariant.
2. **An `UPDATE` on `stock_entry` is refused by Postgres**, with the same treatment.
3. **The Postgres role that owns the application cannot perform those statements** — the refusal is not merely a trigger that a sufficiently-privileged role could disable.
4. **The guard is declared in the repository** — a SQL migration file that any operator can apply — **not only in a chat message**.
5. **The development database is honest about its own weaker guarantee.** SQLite has no triggers, so the dev guard is a **lint rule plus a documented limitation**, not a false claim of parity.

**The single sentence this feature exists to make true:** *LE31's stock ledger cannot be rewritten by anyone, including the database administrator's application role.*

## Scope

**In scope (v1):**

- **One Postgres trigger function + two triggers** on `stock_entry`: one `BEFORE UPDATE`, one `BEFORE DELETE`, both raising an exception that names the append-only invariant and the charter section it comes from.
- **One SQL file** in the repository that creates them, applied in the documented order.
- **A privilege statement** that revokes `UPDATE` and `DELETE` on `stock_entry` from the application's runtime role, **with a documented note** that the migration/owner role retains them (otherwise the owner could never run a legitimate correction — and feature **421** owns the *append-a-correction* path, not an edit).
- **One regression test** that runs against **Postgres** and asserts both statements are refused. **This test must be skipped, not silently passed, when no Postgres is available** (see *Implementation steps*, step 6).
- **One documentation note** in `backend/README.md` recording: *what the trigger does, that it is Postgres-only, and that SQLite (dev) is guarded by lint alone.*
- **A decision note** recording the owner's position on who may perform a legitimate correction — **recorded, not guessed.**

**Explicitly NOT in scope (v1):**

- **The lint rule.** Feature **421** owns it, together with the single write path and the `StockReason` reversal member. **This feature does not add a lint rule, does not add a write path, and does not add an enum member.** The two features are complementary and **must not be merged**.
- **Any schema change to `stock_entry`.** No column, no type change, no new table, no index. **This feature adds triggers and a privilege statement only.**
- **Postgres triggers for any other table.** Feature **413** owns the trigger vocabulary broadly; this feature applies it to exactly one table.
- **`CHECK` constraints and `STRICT` tables.** Feature **404** owns that family. **A `CHECK` cannot express "this table may not be deleted from"** — it is a row constraint, and append-only is a *mutation* rule.
- **The `StockEntry` actor foreign key.** Feature **417** owns `by_user_id` → `app_user.id`.
- **`StockEntry.ref_order_item_id`.** Feature **426** owns that FK.
- **The SQLite foreign-key pragma.** Feature **427** owns it. **A different mechanism entirely** — FKs govern *references*, not *mutability*. **Do not touch `PRAGMA foreign_keys` here.**
- **`Batch.qty_remaining`.** Feature **374** owns the derived-not-stored contradiction; feature **470's sibling** (the consistency slice) covers the write-path side. **Neither is touched here.**
- **Tamper-evidence or hash-chaining.** Features 49, 141, 151, 245, 300 and feature 379's cross-section note all place that elsewhere (*"do not bundle it here"*).
- **Postgres in general, or a migration framework.** §3.2 says *"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)"* — **this feature does not add Alembic, does not add a migrations directory, and does not add a dependency.** The trigger is one hand-written SQL file, applied by hand, and recorded.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.
- **A hard delete for a GDPR/erasure request.** The ledger's append-only nature conflicts with erasure; feature **464** records that conflict and escalates it. **This feature does not resolve it and does not weaken the invariant for it.**

## Description

LE31's product claim is narrower and stronger than most POS systems': **the stock ledger is append-only**. Every stock movement is a new `StockEntry` row; the current quantity is derived by summing them. The charter states it twice, and the corpus has built an entire vocabulary on it — feature **141** is literally titled *"five invariants — append-only — audit proof"*, feature **379** records the *"charter explicit user action vs. schema no actor field"* asymmetry, feature **400** describes *"void restores stock"*, and feature **421** exists precisely because the charter names a linter rule that nobody had built.

**What the enforcement actually is today: a comment.**

```python
class StockEntry(SQLModel, table=True):
    """Append-only ledger. Never UPDATE or DELETE rows.
    ...
    """
```

The database has **no opinion**. Executed against the real schema:

- `UPDATE stock_entry.qty_delta -> -99` → **ACCEPTED**, reads back `-99`.
- `DELETE` → **ACCEPTED**, the row is gone, and the ledger's sum changes with no trace.

There are **zero** `CheckConstraint`s in the whole schema, and SQLModel emits **no triggers**.

### ⭐ Why this is not "421, but at the database level"

This needs stating precisely, because 421 is the obvious neighbour and a reviewer will ask.

**Feature 421 builds a lint rule.** A lint rule is a **static-analysis** check over the **Python source**. It catches `session.delete(stock_entry)` and `stock_entry.qty_delta = ...` **in code that is committed to the repository**.

**It catches none of these:**

- `psql -c "DELETE FROM stock_entry WHERE id = 1"` — the operator's own shell.
- A `psycopg` script run by an operator, a migration, or a one-off script.
- Any process using the application's **own database credentials** outside the linted package.
- The `sqlite3` CLI against the dev database.

**Feature 421's goal statement is itself the proof that this is a different thing.** It says the point of the lint rule is *"so that the guarantee is checkable by a machine rather than upheld by the fact that nobody has written the mutating code yet."* **That is a guarantee about the application code.** The guarantee LE31's product claim needs is about the **data**, and the data does not live in the application code.

**The two features together give two different refusals:**

| | Feature 421 (lint rule) | This feature (database trigger + privilege) |
|---|---|---|
| Refuses a mutating write from committed Python | **Yes** | Yes (defence in depth) |
| Refuses a mutating write from a shell / script / migration | **No** | **Yes** |
| Refuses a mutating write by the app's DB role | **No** | **Yes** |
| Works identically on SQLite and Postgres | Yes | **No** — Postgres only |
| Catches the *first* attempt, before the statement runs | Yes | Yes (BEFORE trigger) |
| Needs a schema/migration change | No | Yes — **one SQL file, applied by hand** |

**Neither substitutes for the other.** 421 alone leaves the database writable. This alone leaves the Python code unlinted.

### The honest limitation, stated rather than hidden

**SQLite has no triggers.** The development database — the one LE31 develops and tests against — cannot enforce this at the database level. This is the same class of dev/prod divergence that feature **427** records for foreign keys, and feature **453** records for timestamps: **the database LE31 tests against is not the database LE31 runs against.**

This feature therefore does **two** things and is honest about the split:

1. **Postgres gets the real guarantee** (triggers + privilege).
2. **SQLite gets an explicit statement** — the lint rule (feature **421**) is the only guard in dev, and the README says so in those words.

**A false claim of parity would be worse than no guard.** The implementer must **not** write a test that asserts SQLite refuses the delete and passes it by skipping silently. The test must be **explicitly skipped with a reason** when Postgres is unavailable, and the skip must be **visible in the CI output**.

### The cost of leaving it

The ledger is LE31's one irreducible asset. If a stock row can be rewritten, then *"the ledger is append-only"* is a **claim about the code**, not a **property of the data** — and every feature in the corpus that reasons from the ledger (features 03, 04, 26, 34, 374, 382, 385, 400, 417, 421, 432, 437) reasons from a property that is currently enforced by a comment.

## Data model

**No schema change. No column. No table. No index. No new model class.**

The feature adds **two database objects**:

```sql
-- 1. The refusal function.
CREATE OR REPLACE FUNCTION stock_entry_is_append_only()
RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION
        'stock_entry is append-only (PROJECT_CHARTER.md 4.3): % is forbidden. '
        'Record a new StockEntry row instead of modifying history.',
        TG_OP
        USING ERRCODE = 'restrict_violation';
END;
$$ LANGUAGE plpgsql;

-- 2. The two triggers.
CREATE TRIGGER stock_entry_no_update
    BEFORE UPDATE ON stock_entry
    FOR EACH ROW EXECUTE FUNCTION stock_entry_is_append_only();

CREATE TRIGGER stock_entry_no_delete
    BEFORE DELETE ON stock_entry
    FOR EACH ROW EXECUTE FUNCTION stock_entry_is_append_only();
```

**And one privilege statement:**

```sql
REVOKE UPDATE, DELETE ON stock_entry FROM le31_app;
```

**Why the trigger alone is not enough:** a trigger can be dropped by its owner, and a role with table-ownership can `ALTER TABLE ... DISABLE TRIGGER`. The privilege statement is the layer that holds when the trigger is disabled. **The application role must therefore be a non-owner role** — if the app connects as the table's owner, the privilege statement is a no-op and the guarantee is a fiction. **This is the load-bearing deployment requirement and it must be stated in the README.**

**Why `USING ERRCODE = 'restrict_violation'`:** it makes the refusal **machine-classifiable**. A caller can distinguish *"you tried to rewrite history"* from *"your query was malformed"*. An arbitrary SQLSTATE makes the refusal indistinguishable from any other database error, and a client that catches-and-retries will retry a statement that must never succeed.

**The trigger fires `BEFORE`, not `AFTER`.** A `BEFORE` trigger refuses the statement **before** the row is touched; an `AFTER` trigger would roll back afterwards, which still protects the data but wastes the work and produces a different error surface. **`BEFORE` is the correct choice and the implementer must not "simplify" it to `AFTER`.**

**The exception message names the charter section.** An error that says *"`stock_entry` is append-only (PROJECT_CHARTER.md §4.3): DELETE is forbidden"* tells the person who hit it what to do next. An error that says `permission denied` does not.

## Implementation steps

Each step is independently verifiable. **Do not begin step 3 before step 2's test fails.**

1. **Write the SQL file** at `backend/app/sql/0001_stock_entry_append_only.sql` (create the `sql/` directory). It contains the function, both triggers, and the privilege statement — **each in its own clearly-labelled statement**, with a comment saying it is applied by hand.
2. **Write the failing Postgres test first.** It connects to a Postgres instance, creates the schema via `SQLModel.metadata.create_all()`, applies the SQL file, inserts one `StockEntry`, and then asserts:
   - `UPDATE stock_entry SET qty_delta = -99 WHERE id = ...` raises, and
   - `DELETE FROM stock_entry WHERE id = ...` raises.
   **On a Postgres without the trigger this test FAILS.** Record the failure output.
3. **Apply the SQL file** to the development Postgres and re-run the test. **It must now pass.**
4. **Add the privilege test**: connect **as the application role** (not the owner) and assert both statements are refused. **If the app role is the owner, this test fails — that failure is the point.** Record it.
5. **Write the README note** in `backend/README.md`: what the trigger does, the requirement that the app role is **not** the owner, that the SQL file is applied by hand, and that **SQLite is guarded by lint only** (feature 421).
6. **Add the explicit Postgres-availability skip** to the test module:
   ```python
   pytestmark = pytest.mark.skipif(
       not os.getenv("LE31_TEST_POSTGRES_URL"),
       reason="No Postgres configured: the append-only trigger is a Postgres-only "
              "mechanism and SQLite cannot enforce it. The dev guard is feature "
              "421's lint rule. This skip is NOT a pass.",
   )
   ```
   **The skip reason must say this is not a pass.** A silent skip would let a green CI run be read as "the ledger is protected" when it was never exercised.
7. **Record the decision note** (see *Open questions*) — who may perform a legitimate correction, and in what form.
8. **Run the whole test suite** and confirm nothing else changed. In particular, `init_db()`/`create_all()` must still work on a fresh SQLite database — **the trigger file is Postgres-only and must not be executed by `init_db()`**.

## Telegram interaction if any

**None.** This feature touches no bot handler and no command. The cook bot's stock vocabulary (feature 03, "kitchen stock tracker") writes ledger rows through the application; **this feature does not change what the bot writes — it changes what the database will tolerate.** A bot that tried to *edit* a ledger row would start failing loudly instead of silently corrupting history, which is the intended behaviour.

**Note for the implementer:** do **not** add a "force edit" Telegram command. **The append-only invariant has no override** — that is the point. A legitimate correction is a **new row**, and feature **421** owns the `StockReason` member that expresses it.

## Dependencies

- **Feature 421 (the append-only linter rule) — COMPLEMENTARY, NOT a dependency.** 421 owns the Python-code guard, the single write path and the `StockReason` reversal member. **This feature owns the database guard.** **They must not be merged.** The implementer of 470 **must not** add a lint rule, a write path, or an enum member — **and the implementer of 421 must not** add a trigger.
- **Feature 427 (SQLite FK enforcement) — adjacent, DIFFERENT mechanism.** 427 makes declared FKs enforced in dev; it has nothing to do with *mutability*. A FK constrains references; a trigger constrains mutations. **Do not bundle.**
- **Feature 404 (CHECK constraints / STRICT tables) — adjacent, different mechanism, and 470 does not touch it.** 404 owns row-value constraints; 470 owns mutation refusal. **Note for 404's owner, not an edit to 404.**
- **Feature 413 (database triggers) — the vocabulary reference, and the owner of the general question.** 413 owns the trigger vocabulary and records the dev/prod divergence. **This feature applies that vocabulary to exactly one table.** It does not extend 413's scope.
- **Feature 417 (`StockEntry.by_user_id` FK) and 426 (`ref_order_item_id` FK) — adjacent.** Both add FKs to `stock_entry`. **Both are blocked on 427** and neither is touched here. **The trigger must not prevent those FKs from being added** — adding a column is an `ALTER TABLE`, not an `UPDATE`, so the `BEFORE UPDATE` trigger does not fire on it. **The implementer must verify this**, because a trigger that accidentally blocked `ALTER TABLE` would block the whole corpus.
- **Feature 374 (`Batch.qty_remaining` derived) — adjacent.** 374 removes the column; 470's sibling covers the write-path consistency. **Neither is touched here.**
- **Feature 464 (staff deactivation) and the erasure conflict — adjacent.** 464 records that a hard delete conflicts with the append-only invariant and **escalates** it rather than resolving it. **This feature does not resolve it and does not weaken the invariant for it.** The trigger makes the conflict *louder*, which is the correct direction.
- **No Alembic, no `migrations/` directory, no new dependency.** §3.2's v1 posture is `init_db()`. **One hand-written SQL file, applied by hand, documented.**

## Open questions

1. **Who may perform a legitimate correction, and in what form?** The trigger refuses all `UPDATE`/`DELETE`, including the owner's. **The owner's answer determines whether the privilege statement should also revoke them from the owner role.** **Recorded default: the owner role retains them, and every legitimate correction is recorded as a **new** `StockEntry` row** — which is feature **421**'s `StockReason` reversal member, and **this feature must not invent that member.** **The implementer must not guess; the decision is recorded and escalated.**
2. **Should the trigger be `BEFORE` or `AFTER`?** **`BEFORE` is correct** (refuse before the row is touched) and this contract specifies it. The question is recorded because it is the kind of detail a future reader may "fix" incorrectly.
3. **What happens to a database restore or a data migration that legitimately rewrites rows?** A trigger is bypassed by `COPY` in some configurations and by a superuser. **Recorded default: the trigger is a guard against *application and operator* mistakes, not against a superuser.** The owner should know the boundary.
4. **Should the SQLite side get anything beyond the lint rule?** SQLite has no triggers. The options are a **file-permission** discipline or accepting the divergence. **Recorded default: accept the divergence and document it** — feature **427** and feature **453** already establish that SQLite/Postgres divergence is a known, recorded pattern in this codebase, not a surprise.
5. **Is `le31_app` the real role name?** The implementation uses it as a placeholder in the SQL. **The implementer must use the actual deployment role name, or leave the statement clearly marked as a template.** **No role may be created by this feature.**

## Why this matters

Every product promise LE31 makes about stock rests on one sentence: **the ledger is append-only**. That sentence is what lets the owner trust a number; it is what lets the corpus derive `qty_remaining` from the ledger rather than storing it (feature 374); it is what makes "void restores stock" (feature 400) an append rather than an edit; it is what lets feature **141** call append-only one of the five invariants it audits.

**Today that sentence is enforced by a comment in a Python file.** Any process with the application's database credentials can rewrite the restaurant's stock history, and the rewrite is silent — there is no error, no row count change in any audit table (there are none), and no way to notice afterwards.

The corpus already knows this. Feature **421** exists because the charter *names* a linter rule and nobody built it. Feature **413** records the trigger vocabulary. Feature **427** records that dev and prod disagree about foreign keys. **What the corpus does not have is the layer that makes the claim true of the data rather than of the code** — and that layer is small: **one function, two triggers, one privilege statement, one hand-written SQL file.**

**It is the cheapest pick in this pass with the highest blast radius of being wrong if omitted.** The cost is a few hours and a documented manual step. The cost of leaving it is that LE31's central claim is a convention.

## Adjacent evidence

- **`DELETE menu_item` was also ACCEPTED**, and the `batch` rows that referenced it **survived** (1 batch still points at the deleted menu item) — because the FK pragma is off in dev (feature 427) and **no FK in the schema carries an `ON DELETE` clause**. **The catalogue's delete/retire path is owned by no feature** and is recorded as adjacent evidence in the 2026-11-12 report, not filed here.
- **`UPDATE batch.qty_remaining -> 999` was ACCEPTED.** A third mutation surface on the stock story, distinct from the ledger row and the catalogue price. **Feature 374 removes the column**; until then it is writable. Recorded, not filed.
- **`UPDATE app_user.role server->manager` was ACCEPTED**, and `UPDATE app_user.name` was ACCEPTED. The corpus sweep for `appuser.{0,30}role.{0,30}(update|change|mutable)` returns **0 hits** — **no feature owns the staff-role change event.** Recorded, not filed.
- **`UPDATE order_item.qty -> 99` was ACCEPTED.** Feature **456** owns the sign and size rule; feature **444** owns the unit price; **neither owns the quantity changing after the line exists.** Recorded, not filed.
- **The whole schema has zero `CheckConstraint`s** and no triggers. This feature is the first trigger LE31 owns.
- **`PRAGMA foreign_keys = 0`** was confirmed on the dev connection — feature **427**'s finding, re-confirmed on 2026-11-12.

## Verification protocol

The implementer must run these and record the actual output. **A skipped Postgres test is not a pass and must be reported as a skip, never as a success.**

```bash
# 1. The contract file exists and is parseable.
python3 - <<'PY'
import pathlib
p = pathlib.Path("features/470-le31-the-append-only-stock-ledger-is-protected-by-a-docstring-and-nothing-else-first-party-a-delete-on-a-stock-entry-row-was-accepted-and-the-ledger-row-is-gone-v1-ledger-delete-guard.md")
assert p.exists(), "contract file missing"
txt = p.read_text()
for h in ("## Goal", "## Scope", "## Description", "## Data model",
          "## Implementation steps", "## Telegram interaction if any",
          "## Dependencies", "## Open questions", "## Why this matters"):
    assert h in txt, f"missing section {h}"
print("PASS contract sections")
PY

# 2. THE load-bearing check — against POSTGRES. Requires LE31_TEST_POSTGRES_URL.
#    This test is EXPLICITLY SKIPPED without Postgres; a skip is NOT a pass.
python3 - <<'PY'
import os, pytest
from sqlmodel import SQLModel, Session, create_engine
from app import models

url = os.getenv("LE31_TEST_POSTGRES_URL")
if not url:
    pytest.skip("No Postgres configured: the append-only trigger is a Postgres-only "
                "mechanism and SQLite cannot enforce it. The dev guard is feature "
                "421's lint rule. THIS SKIP IS NOT A PASS.")
engine = create_engine(url)
SQLModel.metadata.create_all(engine)
# apply backend/app/sql/0001_stock_entry_append_only.sql
with engine.begin() as c:
    c.exec_driver_sql(open("backend/app/sql/0001_stock_entry_append_only.sql").read())
with Session(engine) as s:
    e = models.StockEntry(batch_id=1, qty_delta=-1, reason=models.StockReason.sale)
    s.add(e); s.commit(); s.refresh(e)
    eid = e.id
for stmt in (f"UPDATE stock_entry SET qty_delta = -99 WHERE id = {eid}",
             f"DELETE FROM stock_entry WHERE id = {eid}"):
    try:
        with engine.begin() as c:
            c.exec_driver_sql(stmt)
    except Exception as ex:
        print("refused:", stmt.split()[0], "->", type(ex).__name__)
    else:
        raise AssertionError(f"FAIL: {stmt.split()[0]} was NOT refused")
print("PASS both mutations refused")
PY

# 3. The row is still there after the refusals.
#    -> asserts: SELECT COUNT(*) FROM stock_entry WHERE id = <id>  == 1

# 4. The application role (NOT the owner) is refused.
#    -> connects with the app role's credentials and repeats step 2

# 5. The trigger is BEFORE, not AFTER.
grep -n "BEFORE UPDATE\|BEFORE DELETE" backend/app/sql/0001_stock_entry_append_only.sql
#    -> asserts: both are BEFORE; neither is AFTER

# 6. The error is machine-classifiable.
#    -> asserts: the raised SQLSTATE is 'restrict_violation' (23514 in Postgres)

# 7. No lint rule, write path or enum member was added here.
#    (those belong to feature 421)
grep -rn "StockReason" backend/app/models.py | grep -i "revers\|correct"
#    -> asserts: no new enum member appears in this feature's diff

# 8. The trigger does not block ALTER TABLE (features 417 and 426 depend on this).
#    -> ALTER TABLE stock_entry ADD COLUMN ... must succeed with the trigger installed

# 9. init_db() still works on a fresh SQLite database.
python3 -c "
from sqlmodel import SQLModel
from app import models
from sqlmodel import create_engine
SQLModel.metadata.create_all(create_engine('sqlite:///:memory:'))
print('PASS create_all still works')"

# 10. Nothing but the named files changed.
git status --short
#    -> asserts: only backend/app/sql/0001_*.sql, backend/README.md,
#                the test file, this feature file and the HANDOFF changed
```

## Rollback path

**One command per object, all reversible:**

```sql
DROP TRIGGER IF EXISTS stock_entry_no_delete ON stock_entry;
DROP TRIGGER IF EXISTS stock_entry_no_update ON stock_entry;
DROP FUNCTION IF EXISTS stock_entry_is_append_only();
GRANT UPDATE, DELETE ON stock_entry TO le31_app;   -- if the privilege was revoked
```

- **No data is at risk.** The trigger refuses mutations; it never modifies a row. Dropping it cannot lose anything.
- **No schema change.** No column, no table, no index, no migration state.
- **The ledger is untouched** by the rollback — a trigger cannot alter history, and neither can dropping one.
- **The test suite's other checks are unaffected.** The SQLite path never ran the trigger, so the dev experience is unchanged by the rollback.
- **The privilege statement is the only part with a blast radius**: if the revoke is in place and the trigger is dropped, the app role may still be unable to write. **The rollback order matters — drop the triggers first, then re-grant.** The implementer must record the order they used.
