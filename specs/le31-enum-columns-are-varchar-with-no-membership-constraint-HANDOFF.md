# HANDOFF — le31-enum-columns-are-varchar-with-no-membership-constraint

> **Slice contract for the coding agent.** Produced by the 98th LE31 daily-brainstorm pass (2026-11-05), Pick B.
>
> **Feature file**: `features/442-le31-enum-columns-are-varchar-with-no-membership-constraint.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then four raw inserts — `bill.payment_method='bitcoin'`, `order_item.status='cooked'`, `stock_entry.reason='gift'`, `app_user.role='owner'` — **all four ACCEPTED and stored**; the `CHECK`-constraint count is **0** on every one of the four tables; and the ORM write `Bill(payment_method="bitcoin")` was **also accepted**). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod, same SQLModel code), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. **Read `features/404-…` FIRST** and confirm the boundary described under *Frozen contract* below. **Feature 404 owns the `CHECK`-constraint mechanism and explicitly excludes the `VARCHAR` columns** — this slice is that excluded problem.
5. **Add `enum_check(column, enum_cls, name)`** to `backend/app/models.py` (or a small `backend/app/enums.py`) — **a helper that builds the `CHECK` constraint from the enum's MEMBERS**, so the constraint and the enum cannot drift.
6. **Attach `__table_args__`** to `Bill`, `OrderItem`, `StockEntry` and `AppUser` — **one constraint each.**
7. **Add the application-layer validator** `validate_enum(column, value, enum_cls)` for a useful error message, and call it at the seat endpoint's write path and at whatever ledger write path exists.
8. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_invalid_payment_method_is_rejected_by_the_database` — it must assert the **database** refused the write, not an application-level check.
9. **Record the divergence closure** — one line in `features/404-…` *Adjacent work*, saying *"the `VARCHAR` enum columns are constrained by feature 442."*

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Add, rename or remove any enum member.** Adding `StockReason.correction` is **feature 421**'s business; the `sold_out` withdrawal semantics is **feature 419**'s. **This slice constrains the columns to the members that exist today.** **The whole point of the generated constraint is that it follows a member change automatically — so a hand-edited literal is a defect.**
- **Add `CHECK` constraints on `qty_delta` or on any money column.** That is **feature 404**. **This slice does not touch a single numeric column.**
- **Change `qty_delta`'s type.** That is **feature 437**.
- **Add the `reason`/`qty_delta` sign rule.** That is **feature 432**. **Different rule, same column; same PR is fine, but keep them separate in code.**
- **Add the `StockEntry.by_user_id` foreign key.** That is **feature 417**.
- **Add the role capability map, or a `BotChat` table.** That is **feature 403**. **This slice does not add a read site for `UserRole` and does not decide any policy.**
- **Add a `status` column to `table_`.** That is **feature 388**. **⚠️ `TableStatus` has no column today** — this slice does **not** add one. **When 388 lands, the generated constraint attaches in one line** — see the boundary table below.
- **Widen `bill.payment_method` to fit `'wallet'`.** That is an **owner decision** (feature file *Open questions* 2). **The agent is not authorised to make it.** The recorded position: constrain to the members that exist.
- **Use a native SQL `ENUM` type.** `sa_column=Column(Enum(PaymentMethod, native_enum=False))` renders as a native `ENUM` on Postgres and as `VARCHAR` + `CHECK` on SQLite — **which reintroduces a dev/prod divergence of its own.** **Use a `CHECK`.**
- **Add a `CHECK` on `DerivedTip.formula_version`.** It is a **version string**, not an enum; the set of future versions is open. **Recorded, not in scope.**
- **Introduce Alembic**, or write a migration. Charter §3.2: `init_db()` is the v1 policy. **There is no historical data to migrate.**
- **Change `PROJECT_CHARTER.md`.** The charter is the owner's document.

**Disambiguation**: this slice is about **whether a column's value is one of its enum's members**. It is **not** about the *type* of a number (404, 437), the *sign* of a delta (432), the *existence* of an actor (417), the *policy* of a role (403), or the *presence* of a status column (388).

## Frozen contract

**The one thing this contract exists to make true:** *a column declared as an enum is a column whose value set is known — and LE31's database does not know it.*

Concretely, after this slice lands:

1. `bill.payment_method` accepts **only** `'cash'` and `'card'`.
2. `order_item.status` accepts **only** `'new'`, `'preparing'`, `'ready'`, `'served'`, `'cancelled'`.
3. `stock_entry.reason` accepts **only** `'initial'`, `'sale'`, `'waste'`, `'restock'`, `'sold_out'`.
4. `app_user.role` accepts **only** `'server'`, `'cook'`, `'manager'`.
5. **The constraint is GENERATED from the Python enum**, so adding a member changes the constraint with **no other edit**. **The literal `IN ('cash','card')` string must NOT appear in the source.**
6. **SQLite and Postgres agree.** A value that one refuses, the other refuses, **for the same reason** — the membership set, not the column width.

**The prohibition:** *a hand-written constraint literal*, and *an enum column that accepts a value outside its enum.*

### The 404/421/388 ordering — resolve before writing code

| If | Then |
|---|---|
| **404 has not landed** (today's state) | 442 lands alone. The `CHECK` constraints are the **only** ones on those columns. **Record that in the PR description.** |
| **404 has landed first** | 404's constraints are on the **numeric** columns (`qty_delta` and the money columns). 442's are on the **enum** columns. **They are disjoint sets on disjoint columns and must not be merged or confused.** **The four `CHECK` sets on a table must be separately named.** |
| **421 has landed first** | 421 adds a `StockReason` member. **Because the constraint is generated, it follows automatically.** **If the constraint were hand-written, 421 and 442 would conflict — and that is exactly why the generation mechanism is in scope.** **Verify this by adding the member in a scratch branch and confirming the generated `CHECK` changes.** |
| **421 lands later** | Same, in the other direction: the generated constraint follows 421's new member when 421 lands. **No action needed from this slice.** |
| **388 has not landed** | `table_` has **no** `status` column. **442 does not add one.** When 388 lands, 442's author (or 388's) attaches the generated constraint in one line. **Record this in feature 388's *Adjacent work*.** |
| **442 lands after 388** | Both `__table_args__` entries must be present on `Table` — 388's own constraint (if any) and 442's generated one. **They compose as a tuple, not a replacement.** |

### Why the constraint must be **generated**, not written

**The failure mode this feature exists to prevent is a constraint that drifts from its enum.** Feature **421** is about to add a `StockReason` member. If the `CHECK` is a hand-written string, then adding `correction = "correction"` to `StockReason` without editing the `CHECK` produces a schema where **the valid member is the invalid one** — and 421's whole point is to add a member.

```python
# backend/app/models.py
from sqlalchemy import CheckConstraint

def enum_check(column: str, enum_cls, name: str) -> CheckConstraint:
    """Build a CHECK constraint from an enum's MEMBERS, so the two cannot drift."""
    members = ", ".join("'%s'" % m.value for m in enum_cls)
    return CheckConstraint("%s IN (%s)" % (column, members), name=name)
```

**The one-line proof that the two cannot drift:** `grep -c "IN ('cash','card')" backend/app/models.py` → **0**. The literal never appears in source.

### Why a `CHECK` and not a native `ENUM`

`sa_column=Column(Enum(PaymentMethod, native_enum=False))` renders **differently** on the two engines: a native `ENUM` type on Postgres, `VARCHAR` + `CHECK` on SQLite. **That reintroduces a dev/prod divergence** — the exact class of defect this slice closes. **A plain `CHECK` constraint is portable and behaves identically on both.**

### Why the application-layer validator exists alongside it

The `CHECK` is the **enforcement**. The validator is the **ergonomics**: it gives the caller a readable error instead of an `IntegrityError`. **Both are wanted — and the PR description must state which one actually fires in each regression test**, because a test that asserts "it raised" without saying *what* raised it can pass for the wrong reason.

## Files to touch

| File | Action | Notes |
|---|---|---|
| `backend/app/models.py` | **modify** | Add `enum_check()` and attach `__table_args__` to `Bill`, `OrderItem`, `StockEntry`, `AppUser`. **Four constraints.** |
| `backend/app/enums.py` | **create (optional)** | If `enum_check()` is kept out of `models.py`. **Either location is fine; pick one and record it.** |
| `backend/app/services/validation.py` | **create** | `validate_enum(column, value, enum_cls)` — the application-layer twin. **`backend/app/services/` does not exist today**; creating it here is fine **only if** it does not collide with features 421/441/443, which also want to create it. **⚠️ If 421 or 441 has landed, put this helper in the file they created and record it.** |
| `backend/app/routers/tables.py` | **modify** | Call `validate_enum` on the values the seat endpoint writes. **The endpoint's existing two checks (feature 423) stay as they are** — they are readable and they are 423's. **The `CHECK` is the backstop behind them.** |
| `backend/tests/test_enum_membership.py` | **create** | The six regression tests listed below. **Confirm the project's test path before assuming this one.** |
| `features/404-le31-sqlite-tables-not-strict…` | **modify** | One line in *Adjacent work*: the `VARCHAR` enum columns are constrained by feature 442. |
| `features/388-le31-table-state-machine…` | **modify** | One line in *Adjacent work*: `TableStatus` has no column yet; when feature 388 adds it, the generated constraint attaches in one line. |

**Not touched:** `backend/app/db.py`, `backend/app/bot/`, `backend/app/config.py`, `index.html`, `PROJECT_CHARTER.md`, every other model, **and every numeric column**.

## Mandatory LE31 skill list

The coding agent **must** load these before writing code. They are in the project repo at `skills/`, and on this VPS they are **not** in the standard `skills_list` index — read them from disk:

- **`le31-conventions`** — `skills/le31-conventions/SKILL.md`. **The fixed stack, the hard invariants, and the seven-check gate.**
- **`le31-v1-feature-pattern`** — `skills/le31-v1-feature-pattern/SKILL.md`. **The contract shape and the Definition of Done.**
- **`development`** → `speckit-specify` / `speckit-plan` / `speckit-tasks` / `speckit-implement`. **Product behaviour changes go through the development pipeline.**
- **`pre-merge-review`** — **product code does not merge on the author's say-so.** An independent reviewer must sign off.

**Also read (not skills, but mandatory context):** `features/404-…` (the `CHECK` mechanism and the dev/prod-divergence theme), `features/421-…` (the forthcoming enum member), `features/432-…` (the sign rule), `features/437-…` (the quantity type), `features/417-…` (the actor FK), `features/403-…` (the role policy), `features/388-…` (the table status column), and `PROJECT_CHARTER.md` §3.1, §3.6 and §4.1.

## Mandatory inputs

| Input | Where | Why |
|---|---|---|
| `PROJECT_CHARTER.md` §3.1 (role-based access), §3.6 (money is `Decimal`), §4.1 (SQLite dev / Postgres prod) | repo root | **§4.1 is the reason this slice exists** — the same SQLModel code must behave the same on both engines. |
| `features/404-…` (`CHECK` constraints, dev/prod divergence) | `features/` | **The boundary** — and the sibling that owns the mechanism. |
| `features/421-…` (the append-only linter + the forthcoming `StockReason` member) | `features/` | **Why the constraint must be generated.** |
| `features/432-…` (the sign rule) | `features/` | The nearest sibling on the same column. |
| `features/403-…` (the role allowlist) | `features/` | The role *policy* — which this slice does **not** decide. |
| `features/388-…` (the table state machine) | `features/` | `TableStatus` has no column yet. |
| The parent's proof script | `/opt/data/le31-brainstorm-2026-11-05-scripts/audit_lifecycle5.py` | **The parent's execution transcript for this finding** (probe Q). Run it with `/opt/data/le31-verify-2026-10-27/.venv/bin/python` — that venv has `sqlmodel`/`fastapi`/`pydantic` installed; **the system Python does not have `sqlmodel`.** |
| The pass report | `/opt/data/le31-brainstorm-2026-11-05.md` | The pass, the evidence, and the rejected alternatives. |

## Verification protocol reference

**Reference**: `skills/le31-research-workflow/SKILL.md` (the curl-only anti-fabrication and signed-delta discipline) and `skills/le31-first-party-defect-proving/SKILL.md` (the execution-proof method). **Read `le31-first-party-defect-proving` — this feature was proven that way and the agent must preserve that property in its own tests.**

**The six required regression tests** (all in `backend/tests/test_enum_membership.py`):

1. `test_invalid_payment_method_is_rejected_by_the_database` — `Bill(payment_method='bitcoin')` → **the DATABASE refused it.** **Assert the `IntegrityError`, not an application-level `ValueError`.**
2. `test_invalid_order_item_status_is_rejected` — `status='cooked'` → **rejected**.
3. `test_invalid_stock_reason_is_rejected` — `reason='gift'` → **rejected**.
4. `test_invalid_app_user_role_is_rejected` — `role='owner'` → **rejected**.
5. `test_valid_enum_values_are_accepted` — `payment_method='cash'`, `status='new'`, `reason='initial'`, `role='server'` → **all accepted**.
6. `test_constraint_is_generated_from_the_enum` — **the drift test.** Assert the literal `IN ('cash','card')` does **not** appear in `backend/app/models.py`, and that `enum_check('payment_method', PaymentMethod, 'x')` produces a constraint whose SQL contains `'cash'` and `'card'`. **Optionally: add a member to a scratch copy of the enum and assert the generated constraint changes.** ⚠️ **This is the test that proves the feature's central claim.**

**Method — the one that matters:** **write the tests first, watch them fail against the current code, then apply the change and watch them pass.** A test that only ever passed proves nothing.

**A specific warning about test 1.** The parent's execution found that **the ORM accepts a bare `str` for an enum-annotated field** (`Bill(payment_method="bitcoin")` was committed and stored). **If the agent's test passes because SQLModel validated the value on the way in, the test has passed for the wrong reason and the database is still unguarded.** **The assertion must be on the `IntegrityError` raised by the database, and the agent must verify that the constraint is present in the created schema** (`sqlite_master.sql`, or `PRAGMA table_info` + the `CREATE TABLE` text).

**End-to-end before commit** (charter §7): run the actual seat endpoint against a real database and observe the behaviour change. **Do not declare done from a diff or from green tests alone.**

**Anti-fabrication:** every claim in the PR description must be traceable to a command you ran and its output. **No number, no status code and no test count that you did not observe.**

## Rollback path

**Fully reversible, and deliberately so.**

- **The code rollback:** remove the four `__table_args__` entries and the `enum_check()` helper; delete the validator; delete the test file; revert the two one-line notes. **Nothing today writes an invalid enum value, so no existing behaviour can regress.**
- **The data rollback:** **there is nothing to roll back.** No `StockEntry` write path exists, the only `Visit` write is the seat endpoint, and the seat endpoint's own checks already refuse the values the ORM would reject. **The columns hold only valid members today.**
- **The migration rollback:** LE31 uses `init_db()` (charter §3.2 — **Alembic is a non-goal for v1**), so there is no migration file to revert. **If a migration file is created anyway, that is a scope violation of this contract.**
- **The one semi-irreversible thing:** **if a row with an invalid enum value is written while this feature is in flight** — and it can be, because the ORM accepts it — **then dropping the constraint later leaves the bad row in place**, and `init_db()` will not fix it. **This is the reason the slice lands before any write path exists.**

**Rollback cost:** minutes. **No data is at risk.**

## Sign-off gap

**What this contract does NOT establish, and the agent must not assume:**

- **That `TableStatus` is constrained.** It is not — `table_` has **no** `status` column. **Feature 388 owns adding it.** **Record this.**
- **That the enum's *members* are right.** They are not: `UserRole` has no `waiter` member although the charter's P0 row 47 says *"Waiter can close a bill"*. **That naming mismatch is feature 443's *Open questions* 5, and it is not this slice's to fix.** **Adding a member is feature 421/403's business.**
- **That `payment_method` should have more members.** `AlgoVyn/bikri` (in-window, MIT, README read in full) lists *"take cash/card/wallet/udhaar"* — and `'wallet'` is **6 characters**, which does not fit `VARCHAR(4)`. **That is an owner decision (feature file *Open questions* 2) and the agent is not authorised to make it.**
- **That the constraint survives a schema rebuild.** **It does — `init_db()` recreates it.** But if the project later adopts Alembic, the constraint must be carried into the migration. **Not this slice.**
- **That the `CHECK` is enforced in production.** It is — a `CHECK` constraint behaves identically on SQLite and Postgres. **That is the point of this slice.** But the *narrow* `VARCHAR` width is **not** portable, and the slice deliberately does not rely on it.

## Handoff summary

One helper, four `__table_args__` lines, one application-level validator, one test file, two one-line notes. **Two to four hours.**

The gap was **proven by execution**, not inferred: LE31 has **five** enums and **every one of them is a bare `VARCHAR` with no membership constraint** — `CHECK`-constraint count **0** on all four tables that carry one. The parent wrote `'bitcoin'`, `'cooked'`, `'gift'` and `'owner'` into the four enum columns and **the database accepted all four**, and the ORM accepted a bare `str` too.

**And the dev/prod divergence is the severe part:** `payment_method` is `VARCHAR(4)` and `'bitcoin'` is **7 characters** — **SQLite accepted it and stored it whole; Postgres would reject it with `ERROR 22001`.** The same code path succeeds in development and fails in production, and the test suite runs on SQLite. **Feature 411 already established that this divergence is a first-class finding; this is the same finding on a column nobody has looked at.**

**The one thing that must not happen:** a hand-written constraint literal. **The constraint is generated from the enum precisely so that feature 421's forthcoming `StockReason` member cannot break it.** A literal would have created a conflict between this slice and 421 within the same week.
