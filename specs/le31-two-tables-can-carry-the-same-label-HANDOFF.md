# HANDOFF — le31-two-tables-can-carry-the-same-label

> **Slice contract for the coding agent.** Produced by the 100th LE31 daily-brainstorm pass (2026-11-07), Pick A.
>
> **Feature file**: `features/455-le31-two-tables-can-carry-the-same-label.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then `Table(label="T1", ...)` inserted **twice** — **ACCEPTED**; `SELECT COUNT(*) FROM table_ WHERE label='T1'` → **2**; `PRAGMA table_info(table_)` shows `label VARCHAR` with **no NOT NULL and no UNIQUE**). All seven checks pass; check 1's **demand** is classed INFERRED — **no operator has reported a duplicate label**, and feature 414 records the same "defensive rather than reactive" framing for the table-capacity rule — which is why this contract is deliberately **one constraint, one `NOT NULL`, one error message, five tests** and adds **no** route and **no** surface. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-brainstorm-2026-11-07.md`.
>
> **Report**: `/opt/data/le31-brainstorm-2026-11-07.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/455-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/446-le31-has-no-schema-evolution-mechanism` FIRST and confirm the ordering described under *Frozen contract* below.** **This slice is BLOCKED on 446** — a constraint on an existing table is exactly the change `create_all()` cannot make.
6. **Read `features/448-le31-a-bill-has-no-human-facing-identity` for the uniqueness-scope precedent** (its Open Question / Scope records *"the number is unique **globally**, not per day"*).
7. **Decide and RECORD the scope of the uniqueness** — global, or per section. *Recorded default: **globally unique*** (feature *Open questions* 1).
8. **Add the constraint and the `NOT NULL`** in the same change.
9. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_second_table_with_the_same_label_is_refused` — on today's code the insert simply **succeeds**.
10. **Update `features/01-table-management.md`'s data-model line** so the contract and the schema agree.
11. **Record the precedent** — this is the **first constraint of any kind in LE31's schema** — and point at feature 404 so the two do not contradict.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Add a `status` column to `Table`, a double-seating guard, or a release route.** Feature **388** owns those. **This slice adds one constraint and nothing else about the table's lifecycle.**
- **Compare `party_size` to `seats`.** Feature **414** owns the table-capacity rule.
- **Add a bill number, a bill identity, or a `UniqueConstraint` on a bill.** Feature **448** owns that — on a **new** column. **This slice's constraint is on an existing column and the two are independent.**
- **Add a `CHECK` constraint or make the tables `STRICT`.** Feature **404** owns that family. **This slice adds the first `UniqueConstraint`; 404 adds the first `CHECK`. They must not be merged** — a reviewer must be able to check each on its own.
- **Migrate, backfill, or rename existing tables.** **No table-creation route exists in the shipped backend**, so no duplicate labels can exist in a database this code created. **If a live database holds duplicates, the owner renames them** — that is an operational cleanup, **not this slice's work**.
- **Add a label format regex, a length limit, or a naming convention.** That is an owner decision; *Open questions* 4 records "no format constraint" as the default, and **a wrong regex is a rejection at the worst moment.**
- **Change the floor-map UI.** The mock-up is `index.html`; feature 01's scope; feature **24** owns the visual layout. **Do not restyle anything.**
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**
- **Add a router or a Telegram command.** The slice ships the constraint. **Surfaces are a later feature.**

**Disambiguation**: this slice is about **a table's label being unique**. It is **not** about the table's status (388), its capacity (414), the bill's identity (448), the `CHECK`/`STRICT` family (404), or the schema-evolution mechanism (446).

## Frozen contract

**The one thing this contract exists to make true:** *exactly one table per label — the label the waiter says out loud.*

Concretely, after this slice lands:

1. **The DATABASE refuses a second table with an existing label.** Not the application — the database. A `UniqueConstraint` in `__table_args__`, or an equivalent unique index.
2. **`label` is `NOT NULL`.** **This is half the rule, not a detail.** A `UniqueConstraint` over a **nullable** column permits any number of rows whose label is `NULL` (SQLite and Postgres both allow multiple NULLs in a unique column), so a nullable label would leave a hole exactly where the operator needs a name. **A table with a null label is a table with no name.**
3. **The uniqueness scope is recorded by the implementer** — global, or per section. *Recorded default: **global***, because the waiter says *"table 4"* and **not** *"table 4 in the terrace"*.
4. **The refusal is an `IntegrityError` the write path handles**, and the error **names the conflicting label**. The operator is told *"table T1 already exists"*, not shown a stack trace.
5. **Two tables with different labels are still accepted.** The constraint does not restrict the set of labels — only their uniqueness.
6. **A rename releases the old label.** *Recorded default.* The alternative (a tombstone) is an owner decision; *Open questions* 3.
7. **No table is renamed, migrated or backfilled by this slice.**
8. **No new column is added.** The `NOT NULL` tightens an existing column; it is not a new column. **No new table is added.**
9. **The table's other columns are untouched** — `section`, `seats`, `x`, `y`.
10. **Feature 388's `status` column, if it lands in the same PR, is a separate change** and the two must be independently reviewable.
11. **The constraint is the FIRST of its kind in LE31's schema** and that fact must be **recorded** — exactly as feature 400 recorded the same fact when it contemplated a `UniqueConstraint`. Feature **404** records the current state verbatim: *"there is no `CHECK`, no `UniqueConstraint` beyond primary keys, and no `STRICT`."*

### The 446 ordering — this slice is BLOCKED on it

**446 must land first, or in the same PR as this slice.**

Feature 446 proved, by execution, that `create_all()`:

> *"**adds missing tables but NEVER alters, renames, drops or retypes an existing column** — a changed column is **silently ignored** and the old column keeps serving, so **a feature that adds a column lands, merges, deploys, passes its tests, and the column does not exist in the running database.**"*

**The same failure applies verbatim to a constraint and to a `NOT NULL` tightening on an existing table.** Without 446, this slice would land, merge, deploy, pass its tests — **and the constraint would not exist in the running database.**

**446's own contract names the features it blocks** (408, 415, 420, 421, 435, 438, 439, 442, 443, 445). **This feature must be added to that list, and the PR description must name 446.**

**This slice does NOT introduce Alembic.** §3.2 forbids it in v1. It **depends on 446** and adds nothing further.

### The 388 collision — two edits to one file

Feature 388 adds a `status` column to `Table` and makes **one edit** to `features/01-table-management.md`'s data-model line. **This slice makes one edit to the same line.**

**If both land in the same PR, the edits must not conflict** — the line must end up stating **both** the status column and the label constraint. **If they land in separate PRs, one will conflict with the other and must be rebased, not dropped.** Flag this in the PR description.

**388 does not add a uniqueness rule and this slice does not add a status column.** The two are independent and must remain separately reviewable.

### The 448 precedent — the scope decision, already argued once

Feature 448 proposes `UniqueConstraint("bill_number")` and reasons, verbatim:

> *"**Uniqueness.** `UniqueConstraint("bill_number")` — the number is unique **globally**, not per day, because the service day is already inside the number. A per-day unique constraint would allow two bills to share `2026-11-06-0007` if one of them was allocated against the wrong day. **One number, one bill, everywhere.**"*

**That is the precedent for *Frozen contract* item 3**: the default is global, and the reason is that **the spoken reference does not carry the qualifier.** Cite 448 in the PR description — **this scope question has already been argued once in the corpus, and the answer is recorded.**

## Files to touch

**Create:**

- `backend/tests/test_table_label_is_unique.py` — the regression tests.

**Modify:**

- `backend/app/models.py` — **only** `class Table`: the `label` declaration and the `__table_args__` (or the unique index). **Nothing else in this file changes.**
- `features/01-table-management.md` — **one line**: the data-model line, to state the constraint.

**Read but do not modify:**

- `features/446-le31-has-no-schema-evolution-mechanism.md` — **the hard dependency.**
- `features/388-le31-table-state-machine-…md` — the sibling that edits the same line.
- `features/448-le31-a-bill-has-no-human-facing-identity.md` — the uniqueness-scope precedent.
- `features/404-le31-sqlite-tables-not-strict-…md` — the adjacent constraint family; the first-constraint precedent.
- `features/414-le31-table-capacity-…md` — the adjacent table rule; its fixture stays valid.
- `PROJECT_CHARTER.md` — §3.2, §4.1, §7.

## Mandatory LE31 skill list

- **`le31-conventions`** — §3.2, §4.1, §7, the truth invariant, the seven-check gate.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done*.
- **`le31-feature-pipeline`** — where the artefacts land.
- **`le31-handoff-spec`** — the slice-contract shape.
- **`le31-backend`** — the FastAPI/SQLModel layering and the session boundary.

**Also read** `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §4.1 (SQLite dev / Postgres prod), and §7 (the quality bar).

## Mandatory inputs

- The uniqueness scope decision — **recorded, not assumed**.
- The rename semantics — **recorded, not assumed**.
- Feature 446's status — **it must have landed, or must land in this PR.**

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases

| # | Case | Expected |
|---|---|---|
| 1 | insert two tables with the **same** label | the second is **REFUSED** |
| 2 | insert a table with a **null label** | **REFUSED** (the `NOT NULL` half) |
| 3 | insert two tables with **different** labels | both **ACCEPTED** |
| 4 | the **same label in different sections** | accepted or refused **according to the recorded scope decision** — and the test must assert **that** decision, not a guess |
| 5 | the error message | **names the label** |
| 6 | the constraint's **scope in the DDL** | matches the recorded decision — `uq_table_label` vs a composite `(section, label)` |
| 7 | a **rename** | the **old label is released** (per the recorded decision) and a new table may take it |
| 8 | the constraint on **Postgres** (if a test DB is available) | the same refusal — **and record what was actually run** |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Build a throwaway SQLite DB from LE31's own `models.py`.
2. Insert `Table(label="T1", ...)` → **accepted**.
3. Insert a second `Table(label="T1", ...)` → **show the refusal**, with the message naming `"T1"`.
4. Insert `Table(label="T2", ...)` → **accepted**.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code the second insert **succeeds** — there is no constraint at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

The verification venv from prior passes can be reused: **`/opt/data/le31-verify-2026-10-27/.venv`** (SQLModel + FastAPI + SQLite). **Do not provision a new venv if this one works.** If a Postgres test DB is **not** available, **say so plainly and record what was actually verified on SQLite** — do not claim the Postgres row was tested.

## Rollback path

**Fully reversible in one step.**

- **Revert the commit** and the constraint is gone.
- **No data is at risk**: **no table-creation route exists in the shipped backend**, so no table row can have been created by shipped code — and therefore **no duplicate label can exist** in a database this code built. *(Recorded, and it is the reason this slice is free today and expensive later.)*
- **The one caveat**: if a live database **did** acquire duplicate labels through another path, removing the constraint restores the old behaviour and **the duplicates stay** — they are not repaired by a rollback, and **this slice does not repair them.**

## Sign-off gap

**What the agent MUST NOT decide:**

- **Whether a table may be renamed and whether the old label is reserved** — recorded default: the old label is released. **Owner decision.**
- **Whether the label has a format, a length limit, or a naming convention** — recorded default: **no format constraint**. **Owner decision.**
- **Whether the uniqueness is global or per section** — recorded default: **global**. **Owner decision; the implementer records it.**
- **What to do about existing duplicate labels in a live database** — an **operational cleanup for the owner**, explicitly out of scope here.
- **Anything about the table's status (388), capacity (414), or the bill's identity (448).**

**What the agent must report back:**

- The **two inserts** before and after, as observed.
- The **scope decision** and the **rename decision**, as recorded in the code.
- The **DDL** the constraint produced, so a reviewer can check the scope against the recorded decision.
- **Whether 446 had landed**, and if not, **what happens on a database where `table_` already exists** — the constraint will **not** be created by `create_all()` on an existing table.

## Handoff summary

**One sentence:** *Make a table's name mean one thing — one `UniqueConstraint`, one `NOT NULL`, one error message — and do it now, while no route creates a table and the constraint is still free.*

**Three picks of the 100th daily-brainstorm pass (2026-11-07):**

- **Pick A (this one):** `le31-two-tables-can-carry-the-same-label` — **feature 455**.
- **Pick B:** `le31-a-visit-may-be-closed-with-order-lines-and-no-bill` — **feature 454**.
- **Pick C:** `le31-sqlite-silently-drops-the-utc-offset` — **feature 453**.

**Feature**: `features/455-le31-two-tables-can-carry-the-same-label.md`
**Report**: `/opt/data/le31-brainstorm-2026-11-07.md`
