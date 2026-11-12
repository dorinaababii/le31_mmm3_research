# HANDOFF — Feature 470: the append-only stock ledger is protected by a docstring and nothing else

> **Slice contract for an external coding agent.** Read this file and the feature contract it names; you should need nothing else. **Do not paste chat excerpts.** If anything here is ambiguous, stop and say so — do not invent product behaviour.
>
> **Pick B of Daily Research 2026-11-12 (89th pass). FIRST-PARTY, execution-proven.** Bucket: **v1**. Gate verdict: **`build`**.

## 1. The active feature path

```
features/470-le31-the-append-only-stock-ledger-is-protected-by-a-docstring-and-nothing-else-first-party-a-delete-on-a-stock-entry-row-was-accepted-and-the-ledger-row-is-gone-v1-ledger-delete-guard.md
```

**The one-sentence claim:** LE31's append-only ledger invariant is a docstring; the database accepted a `DELETE` on a `StockEntry` and the ledger row is gone.

**The one sentence this feature exists to make true:** *LE31's stock ledger cannot be rewritten by anyone, including the database administrator's application role.*

**The executed evidence (re-run it; do not trust this paragraph):**

```
seeded menu_item id=2, batch id=2, stock_entry id=2
DELETE menu_item   -> ACCEPTED
  batches still referencing it: 1
DELETE stock_entry -> ACCEPTED (the append-only ledger row is gone)
  stock_entry rows now: 1
sqlite PRAGMA foreign_keys = 0

UPDATE stock_entry.qty_delta -> -99 ACCEPTED (reads back -99)

CheckConstraint instances in the whole schema: []
Triggers on stock_entry: none (SQLModel creates no triggers)
```

**The invariant, as a comment — `backend/app/models.py:113-118`:**

```python
class StockEntry(SQLModel, table=True):
    """Append-only ledger. Never UPDATE or DELETE rows.

    Current stock for a batch = SUM(qty_delta) WHERE batch_id = X.
    """
```

## 2. The seven-check gate verdict

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | When the next code path touches the ledger, it can `UPDATE` or `DELETE` a row and the database will not object, so the one number LE31 promises never changes is one a `psql` session can change. |
| 2 | Viability | **Yes** — one trigger function, two triggers, one privilege statement, one SQL file. |
| 3 | Practicability & confidence | **Yes** — Postgres triggers are standard; SQLite has none. **Rabbit hole: the trigger must not block `ALTER TABLE` (features 417 and 426 depend on that) and must not block the owner's legitimate corrections.** |
| 4 | Conflict | **No invariant violated** — it *upholds* the append-only invariant the charter already declares. |
| 5 | Outcome / appetite / scope | **v1** — 2–4 hours. Scope fixed: **one trigger + the privilege grant**. |
| 6 | Cost to operational value | **High** — a silently rewritten ledger row is the most expensive class of defect in LE31, because the product's whole claim is that the ledger is append-only. |
| 7 | Circuit breaker & reversibility | **Stop evidence:** a test asserting `DELETE` on `stock_entry` is refused on Postgres. **Rollback:** drop the trigger. |
| — | **Decision** | **`build`** |

**Evidence class:** **observed**. Confidence: **high** for the mutation; **medium** for the Postgres behaviour, because **Postgres was NOT exercised on this VPS** (`psycopg` is not importable in the probe venv). **Your first job is to run the Postgres test for real.**

## 3. Files to touch

**Exactly these, and no others:**

| File | Change |
|---|---|
| `backend/app/sql/0001_stock_entry_append_only.sql` | **Create** the directory and the file: the function, both triggers, the privilege statement. |
| `backend/README.md` | **Add** a note: what the trigger does, the requirement that the app role is **not** the owner, that the SQL is applied by hand, and that **SQLite is guarded by lint only (feature 421)**. |
| `backend/tests/test_stock_entry_append_only.py` (or the repo's existing test location) | **Add** the Postgres regression test **with an explicit skip**. |
| `features/470-…md` | The contract. Read-only for you except for fixing a typo. |
| `specs/le31-the-append-only-stock-ledger-is-protected-by-a-docstring-and-nothing-else-first-party-a-delete-on-a-stock-entry-row-was-accepted-and-the-ledger-row-is-gone-v1-ledger-delete-guard-HANDOFF.md` | This file. |

**Files you must NOT touch:** `backend/app/models.py` (no enum member, no column), `backend/app/db.py` (no Alembic, no migrations directory, no `init_db()` change), `backend/app/routers/**` (no router), `backend/app/bot/cook_bot.py`, `backend/app/config.py`, anything under `features/` other than 470, anything under `specs/` other than this one, `PROJECT_CHARTER.md`, `INDEX.md` (the parent owns the INDEX rows).

## 4. The implementation, in order

1. **Write the SQL file** at `backend/app/sql/0001_stock_entry_append_only.sql`. **Each statement separately labelled.** The content is given verbatim in the feature contract's *Data model* section — **use it exactly**, including `USING ERRCODE = 'restrict_violation'` and `BEFORE` (not `AFTER`).
2. **Write the failing Postgres test first.** It creates the schema via `SQLModel.metadata.create_all()`, applies the SQL file, inserts one `StockEntry`, then asserts that `UPDATE` and `DELETE` are both refused. **Against a Postgres without the trigger this test FAILS — record the failure output.**
3. **Apply the SQL file** to the development Postgres and re-run. **It must now pass.**
4. **Add the privilege test**: connect **as the application role** (not the owner) and assert both statements are refused. **If the app role is the owner, this test fails — that failure is the point.**
5. **Write the README note.**
6. **Add the explicit Postgres-availability skip** to the test module:
   ```python
   pytestmark = pytest.mark.skipif(
       not os.getenv("LE31_TEST_POSTGRES_URL"),
       reason="No Postgres configured: the append-only trigger is a Postgres-only "
              "mechanism and SQLite cannot enforce it. The dev guard is feature "
              "421's lint rule. This skip is NOT a pass.",
   )
   ```
   **The skip reason must say this is not a pass.** A silent skip lets a green CI run be read as "the ledger is protected" when it was never exercised.
7. **Record the decision note** for Open question 1 (who may perform a legitimate correction).
8. **Run the whole test suite.** `init_db()` / `create_all()` must still work on a fresh SQLite database — **the trigger file is Postgres-only and must never be executed by `init_db()`.**

## 5. The five things that will go wrong if nobody tells you

1. **⚠️ You will be tempted to add the lint rule.** Do not. **Feature 421 owns it**, together with the single write path and the `StockReason` reversal member. 421 is a **Python-code** guarantee; this feature is a **database** guarantee. **They are complementary and must not be merged.** If you find yourself writing a lint rule, you have crossed the boundary.
2. **⚠️ You will be tempted to use `AFTER` instead of `BEFORE`.** `BEFORE` refuses the statement **before the row is touched**. `AFTER` rolls back afterwards — it still protects the data but wastes the work and produces a different error surface. **The contract specifies `BEFORE`.**
3. **⚠️ You will be tempted to drop the privilege statement** because the trigger already refuses the statements. **The trigger can be dropped by its owner, and a role with table-ownership can `ALTER TABLE ... DISABLE TRIGGER`.** The privilege statement is the layer that holds when the trigger is disabled. **And it only works if the app role is NOT the owner** — that is the load-bearing deployment requirement.
4. **⚠️ You will be tempted to add Alembic or a `migrations/` directory.** Do not. §3.2 says *"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)"*. **One hand-written SQL file, applied by hand, documented.** No new dependency, no `alembic.ini`, no version table.
5. **⚠️ You will be tempted to write a test that skips silently, or to assert parity with SQLite.** SQLite has **no triggers**. **A false claim of parity is worse than no guard.** The test must be explicitly skipped with a reason that says *"THIS SKIP IS NOT A PASS"*.

## 6. Verification protocol

Run each of these and record the **actual output**. **A skipped Postgres test is not a pass and must be reported as a skip, never as a success.**

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
from sqlmodel import SQLModel, create_engine
from app import models
SQLModel.metadata.create_all(create_engine('sqlite:///:memory:'))
print('PASS create_all still works')"

# 10. Nothing but the named files changed.
git status --short
#    -> asserts: only backend/app/sql/0001_*.sql, backend/README.md,
#                the test file, this feature file and this HANDOFF
```

## 7. Rollback path

**One command per object, all reversible. Order matters.**

```sql
DROP TRIGGER IF EXISTS stock_entry_no_delete ON stock_entry;
DROP TRIGGER IF EXISTS stock_entry_no_update ON stock_entry;
DROP FUNCTION IF EXISTS stock_entry_is_append_only();
GRANT UPDATE, DELETE ON stock_entry TO le31_app;   -- if the privilege was revoked
```

- **No data is at risk.** The trigger refuses mutations; it never modifies a row. Dropping it cannot lose anything.
- **No schema change.** No column, no table, no index, no migration state.
- **The ledger is untouched by the rollback** — a trigger cannot alter history, and neither can dropping one.
- **⚠️ The privilege statement is the only part with a blast radius.** If the revoke is in place and the trigger is dropped, the app role may still be unable to write. **Drop the triggers first, then re-grant. Record the order you used.**

## 8. The mandatory LE31 skill list

**Load these before you write code. In this order:**

1. `le31-conventions` — the seven-check gate, the hard invariants, and §3.2's non-goals. **This is why you are not adding Alembic.**
2. `le31-v1-feature-pattern` — the contract shape, the slicing rules, and the definition of done.
3. `le31-handoff-spec` — the frozen-contract discipline: **do not silently change the slice, the scope or the verification path.** If something must change, **surface it and stop.**
4. `development` — the generic pipeline: specify → plan → tasks → implement → **independent review**.
5. `speckit-specify`, `speckit-plan`, `speckit-tasks` — as `development` directs.
6. `pre-merge-review` — **product code does not merge on your own say-so.** It merges on green checks **and** a review from an agent or person who did not author the change.
7. `verify-before-fixing` — when a check fails, **fix what it is flagging. Never weaken a check to make it pass.**

**The project skills live in the repository** at `skills/<name>/SKILL.md`. If the Hermes loader cannot find one by name, **read the file directly** — do not proceed without it.

## 9. The one thing that matters

**LE31's product claim is one sentence: the ledger is append-only.** Today that sentence is enforced by a comment in a Python file, and the database will happily `DELETE` a ledger row while you watch.

**Your job is not to make the application well-behaved — feature 421 does that. Your job is to make the *database* refuse.** That is the difference between a convention and a property, and it is the difference between "our code does not do that" and "that cannot happen".

Two things you must carry out of this slice:

- **A skipped Postgres test is a skip, not a pass.** Say so in your report.
- **The trigger and the privilege are two layers for one reason.** The trigger can be disabled by its owner; the privilege cannot be evaded by a disabled trigger — **as long as the application role is not the table's owner.** Check that. If it is, the guarantee is a fiction and you must say so.
