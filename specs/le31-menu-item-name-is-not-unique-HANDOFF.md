# HANDOFF — le31-menu-item-name-is-not-unique

> **Slice contract for the coding agent.** Produced by the 86th LE31 daily-research pass (2026-11-08), Pick C.
>
> **Feature file**: `features/458-le31-menu-item-name-is-not-unique-first-party-two-dishes-may-share-the-one-name-the-waiter-says-out-loud-v1-menu-item-name-uniqueness.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then three inserts — `MenuItem(name='Tiramisu', category='dessert', unit_price=6.00)`, `MenuItem(name='Tiramisu', category='desserts', unit_price=6.50)`, `MenuItem(name='Tiramisu', category='Dessert', unit_price=7.00)` — **all ACCEPTED**; `SELECT COUNT(*) FROM menu_item WHERE name='Tiramisu'` → **3**; the three carry **three distinct prices** (6.00 / 6.50 / 7.00) and **three distinct categories** (dessert / desserts / Dessert); the live DDL shows `name VARCHAR NOT NULL` with **no UNIQUE and no index**; and the constraint census over the whole schema reads **0 CHECK constraints across 10 tables**, the only UNIQUE being `bill.visit_id`). All seven checks pass; check 1's **demand** is classed **INFERRED** — **no operator has reported a duplicate dish name**, and the corpus confirms nobody owns the rule (a sweep over **941** feature/spec files returns **zero** hits for a dish-name uniqueness rule) — which is why this contract is deliberately **one constraint, one error message, six tests** and adds **no** route and **no** surface. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-daily-research-2026-11-08.md`.
>
> **Report**: `/opt/data/le31-daily-research-2026-11-08.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/458-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/446-le31-has-no-schema-evolution-mechanism` FIRST and confirm the ordering described under *Frozen contract* below.** **This slice is BLOCKED on 446** — a `UniqueConstraint` on an existing table is exactly the change `create_all()` cannot make.
6. **Read `features/455-le31-two-tables-can-carry-the-same-label`** — it adds the **first** `UniqueConstraint` in LE31's schema, on `Table.label`, and **it is the precedent this slice follows**: same declarative shape, same error-message discipline, same rename-semantics decision to record.
7. **Read `features/448-le31-a-bill-has-no-human-facing-identity`** — the uniqueness-scope precedent (*"the number is unique **globally**, not per day"*).
8. **Read `features/433-le31-menu-item-category-is-case-sensitive-free-text`** — the **category** half of the same normalisation problem. **Not merged with this one** — but see the case-sensitivity note below.
9. **Decide and RECORD the scope of the uniqueness** — global, or per category. *Recorded default: **globally unique*** (feature *Open questions* 1).
10. **Decide and RECORD the case-sensitivity behaviour** — *recorded default: **case-insensitive*** (feature *Open questions* 2) — **and make it explicit on BOTH engines.**
11. **Add the constraint** in the same change, using the **same shape as feature 455** so there is one precedent, not two.
12. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_second_dish_with_the_same_name_is_refused` — on today's code the insert simply **succeeds**.
13. **Add the raw-`INSERT` test** — the one that distinguishes a real database constraint from a model-level validator.
14. **Update `features/02-order-taking.md`**'s data-model line so the contract and the schema agree.
15. **Record the precedent** — this is **the second `UniqueConstraint` in LE31's schema**, following 455 — and point at features 404 and 455 so the three do not contradict each other.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Normalise, canonicalise, or re-spell the menu `category`.** Feature **433** owns that. **This slice owns the **name**.** They are the two halves of one problem and **must not be merged.**
- **Add a `UniqueConstraint` on `table_.label`, or change `Table` in any way.** Feature **455** owns that — on a different table, a different slice.
- **Add a bill number, a bill identity, or a `UniqueConstraint` on a bill.** Feature **448** owns that — on a **new** column; this slice's is on an **existing** one. **They are independent.**
- **Add a `CHECK` constraint or make the tables `STRICT`.** Feature **404** owns that family. **This slice adds a `UniqueConstraint`; 404 adds a `CHECK`.** Separate slices with separate precedents.
- **Add a dish-variant, a modifier, or a "product family" column.** That is a product decision the owner has not made. *Open questions* 3 records the option and **the default is that the owner renames one of the two dishes.** **Not decided here.**
- **Add a `CHECK` on `order_item.qty` or a tip derivation.** Features **456** and **457** own those.
- **Change `OrderItem.unit_price`.** Feature **449** owns it. **With a unique dish name the price the waiter picks is unambiguous, but 449's column still needs its own fix — this slice does not make 449's problem go away.**
- **Migrate, backfill, or rename existing dishes.** If a live database holds two tiramisus, **the owner renames one** — an operational cleanup, **not this slice's work.**
- **Add a name format regex, a length limit, or a naming convention.** *Open questions* 6 records *"no format constraint"* as the default, and **a wrong regex is a rejection at the worst moment.**
- **Change the menu UI or the floor-plan UI.** The mock-up is `index.html`; feature 08's scope.
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**
- **Add a router or a Telegram command.** The slice ships the constraint. **Surfaces are a later feature.**

**Disambiguation**: this slice is about **the dish's name being unique**. It is **not** about the dish's category (433), the table's label (455), the bill's number (448), the menu's shape checks (404), the order line's quantity (456) or price (449), the tip (457), or the schema-evolution mechanism (446).

## Frozen contract

**The one thing this contract exists to make true:** *exactly one dish per name — the name the waiter says out loud.*

Concretely, after this slice lands:

1. **The DATABASE refuses a second dish with an existing name.** Not the application — the database. A `UniqueConstraint` in `__table_args__`, or an equivalent unique index — **the same shape feature 455 uses for `Table.label`.**
2. **The uniqueness scope is recorded by the implementer** — global, or per category. *Recorded default: **global***, because the waiter says *"tiramisu"* and **not** *"the tiramisu in the desserts"*.
3. **The case-sensitivity behaviour is recorded by the implementer** — *recorded default: **case-insensitive** ("Tiramisu" and "tiramisu" are one dish)* — **and it must be made EXPLICIT and verified on BOTH SQLite and Postgres.** See below.
4. **The refusal is an `IntegrityError` the write path handles**, and the error **names the dish**: *"tiramisu already exists"* — not a stack trace.
5. **Two dishes with different names are still accepted.** The constraint does not restrict the set of names — only their uniqueness.
6. **A rename releases the old name.** *Recorded default.* The alternative (a tombstone) is an owner decision; *Open questions* 5.
7. **No dish is renamed, migrated or backfilled by this slice.**
8. **No new column is added.** The rule constrains an existing column. **No new table is added.**
9. **The dish's other columns are untouched** — `category`, `unit_price`, `unit`, `is_prepared`, `photo_url`.

### ⭐ The case-sensitivity rule — this is the part that is easy to get wrong

**SQLite's default collation for `VARCHAR` is `BINARY`** — `"Tiramisu"` and `"tiramisu"` are **different strings**. **Postgres's default collation depends on the database's locale** and is case-sensitive in the common configurations but **not universally**.

**A `UNIQUE` constraint whose behaviour differs between dev (SQLite) and prod (Postgres) is exactly the defect class feature 453 filed** — its own title ends *"and dev and prod disagree"*.

**The contract therefore requires the implementer to make the behaviour explicit on both engines:**

- **If case-insensitive uniqueness is chosen** (the recorded default), the implementation must be explicit — **a functional/expression index on `LOWER(name)`**, or a normalised stored column — **and it must be verified on both SQLite and Postgres.** **A plain `UNIQUE(name)` on a case-sensitive collation does NOT implement a case-insensitive rule**, and **a plain `UNIQUE(name)` would be a silently different rule from the one this contract states.**
- **If case-sensitive uniqueness is chosen**, that must be **recorded explicitly and tested on both engines**, and the contract must state that `"Tiramisu"` and `"tiramisu"` are **two dishes**.

**Whichever is chosen, it must be recorded, tested on both engines, and written into the contract.** **"It depends on the database" is not a recorded decision.**

**⭐ And the interaction with feature 433 must be recorded.** 433 owns the **category** normalisation, and it proved that `"dessert"`, `"Desserts"` and `"dessert "` are three categories for one dish. **If this slice's case-sensitivity decision is "case-insensitive" and 433's category normalisation is also case-insensitive, the two together define one dish-lookup rule across both columns — and that interaction must be written down, not left implicit.** **Neither slice may assume the other has covered it.**

### The 446 ordering — this slice is BLOCKED on it

**446 must land first, or in the same PR as this slice.**

Feature 446 proved, by execution, that `create_all()`:

> *"**adds missing tables but NEVER alters, renames, drops or retypes an existing column** — a changed column is **silently ignored** and the old column keeps serving, so **a feature that adds a column lands, merges, deploys, passes its tests, and the column does not exist in the running database.**"*

**The same failure applies verbatim to a `UniqueConstraint` on an existing table.** Without 446, this slice would land, merge, deploy, pass its tests — **and the constraint would not exist in the running database.**

**446's own contract names the features it blocks** (408, 415, 420, 421, 435, 438, 439, 442, 443, 445). **This feature must be added to that list, and the PR description must name 446.**

**This slice does NOT introduce Alembic.** §3.2 forbids it in v1. It **depends on 446** and adds nothing further.

### The 455 relationship — one precedent, two contracts

**455** adds the **first** `UniqueConstraint` in LE31's schema on `Table.label`, and its contract records the same three decisions this slice must record: the **scope** (global vs per-section — 455's default is *global*), the **rename semantics** (the old label is released), and the **error-message discipline** (the message names the conflicting label). **This slice's defaults are the same in each case, and for the same reason: a spoken identifier is one thing.**

**The two must not be merged** — a reviewer must be able to check each on its own — **but they must not also drift apart.** **One of the two contracts must reference the other.** 455's contract is the older one and its scope decision is the precedent; **the implementer of this slice must cite it, and — if 455's scope decision is changed later — the two must be re-read together.** **This is recorded because the precedent for "a spoken identifier is unique" is now spread across two files, and a future third (448, for the bill) must find both.**

### The 433 relationship — the two halves of one normalisation

**433** owns the menu **category**; **this slice** owns the menu **name**. **They are complementary and must not be merged.** **When both land, the menu must be checked for the case where a name is duplicated *and* a category is duplicated at once** — and **neither feature may assume the other has covered it.**

## Files to touch

**Create:**

- `backend/tests/test_menu_item_name_is_unique.py` — the regression tests.

**Modify:**

- `backend/app/models.py` — **only** `class MenuItem`: the `__table_args__` (or the unique index). **Nothing else in this file changes.**
- `features/02-order-taking.md` — **one line**: the data-model line, to state the constraint.

**Read but do not modify:**

- `features/446-le31-has-no-schema-evolution-mechanism.md` — **the hard dependency.**
- `features/455-le31-two-tables-can-carry-the-same-label.md` — **the sibling constraint and the precedent.**
- `features/433-le31-menu-item-category-is-case-sensitive-free-text-…md` — **the sibling normalisation, on the same table.**
- `features/448-le31-a-bill-has-no-human-facing-identity.md` — the uniqueness-scope precedent.
- `features/404-le31-sqlite-tables-not-strict-…md` — the adjacent constraint family; the first-constraint precedent.
- `features/453-le31-sqlite-silently-drops-the-utc-offset-…md` — **the dev/prod-disagreement precedent that the case decision must not repeat.**
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
- The case-sensitivity decision — **recorded, not assumed**, and verified on both engines.
- The rename semantics — **recorded, not assumed**.
- Feature 446's status — **it must have landed, or must land in this PR.**

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases

| # | Case | Expected |
|---|---|---|
| 1 | insert two dishes with the **same** name | the second is **REFUSED** |
| 2 | insert two dishes with **different** names | both **ACCEPTED** |
| 3 | the **same name in different categories** | accepted or refused **according to the recorded scope decision** — and the test must assert **that** decision, not a guess |
| 4 | `"Tiramisu"` and `"tiramisu"` | the behaviour of the **recorded case decision** — **asserted explicitly** |
| 5 | the error message | **names the dish** |
| 6 | a **raw `INSERT`** through the SQLAlchemy core | **REFUSED by the database** — *this is the test that proves the rule is a constraint and not a validator* |
| 7 | the constraint's **scope in the DDL** | matches the recorded decision — `uq_menu_item_name` vs a composite `(category, name)`, and the case strategy is visible in the DDL |
| 8 | a **rename** | the **old name is released** (per the recorded decision) and a new dish may take it |
| 9 | the constraint on **Postgres** (if a test DB is available) | the same refusal **and the same case behaviour** — **and record what was actually run** |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Build a throwaway SQLite DB from LE31's own `models.py`.
2. Insert `MenuItem(name="Tiramisu", category="dessert", unit_price=Decimal("6.00"))` → **accepted**.
3. Insert a second `MenuItem(name="Tiramisu", …)` → **show the refusal**, with the message naming `"Tiramisu"`.
4. Insert `MenuItem(name="Tiramisu of the day", …)` → **accepted**.
5. Show `SELECT COUNT(*) FROM menu_item WHERE name='Tiramisu'` → **1**.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code the second insert **succeeds** — there is no constraint at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

The verification venv from prior passes can be reused: **`/tmp/le31-daily-2026-11-06/.probe-venv`** (SQLModel + SQLAlchemy + SQLite) — the same venv this pass's probes used. **`/opt/data/le31-verify-2026-10-27/.venv`** is the older equivalent. **Do not provision a new venv if one of these works.** If a Postgres test DB is **not** available, **say so plainly and record what was actually verified on SQLite** — do not claim the Postgres row was tested. **In particular, if the Postgres case-sensitivity row was not tested, that gap must be stated in the PR** — it is the row most likely to be silently wrong.

## Rollback path

**Fully reversible in one step.**

- **Revert the commit** and the constraint is gone.
- **No data is at risk**: **no menu-management route exists in the shipped backend**, so no dish row can have been created by shipped code — and therefore **no duplicate name can exist** in a database this code built. *(Recorded, and it is the reason this slice is free today and expensive later.)*
- **The one caveat**: if a live database **did** acquire duplicate names through another path, removing the constraint restores the old behaviour and **the duplicates stay** — they are not repaired by a rollback, and **this slice does not repair them.**

## Sign-off gap

**What the agent MUST NOT decide:**

- **Whether the uniqueness is global or per category** — recorded default: **global**. **Owner decision; the implementer records it.**
- **Whether the uniqueness is case-sensitive** — recorded default: **case-insensitive**. **Owner decision; the implementer records it and verifies it on both engines.**
- **Can a dish be renamed and whether the old name is reserved** — recorded default: the old name is released. **Owner decision.**
- **Whether the owner may run two products under one name** — recorded default: **the owner renames one of them**; a variant column is a **v2 product decision**. **Not decided here.**
- **What to do about existing duplicate names in a live database** — an **operational cleanup for the owner**, explicitly out of scope here.
- **Whether the name has a format, a length limit, or a naming convention** — recorded default: **no format constraint**. **Owner decision.**
- **Anything about the menu category (433), the table label (455), the bill identity (448), the order line (449 / 456), the tip (457), or the schema-evolution mechanism (446).**

**What the agent must report back:**

- The **two inserts** before and after, as observed.
- The **scope decision**, the **case decision** and the **rename decision**, as recorded in the code.
- The **DDL** the constraint produced — **so a reviewer can check the scope and the case strategy against the recorded decisions.**
- **The case behaviour as actually observed on SQLite**, and **on Postgres if a test DB was available** — **and if it was not, that must be said plainly.**
- **Whether 446 had landed**, and if not, **what happens on a database where `menu_item` already exists** — the constraint will **not** be created by `create_all()` on an existing table.
- **Whether feature 433's category normalisation and this slice's name uniqueness have been read together**, and what the combined behaviour is.

## Handoff summary

**One sentence:** *Make a dish's name mean one thing — one `UniqueConstraint`, one explicit case rule verified on both engines, one error message — and do it now, while no route creates a dish and the constraint is still free.*
