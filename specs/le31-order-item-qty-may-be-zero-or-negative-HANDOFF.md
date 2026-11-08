# HANDOFF — le31-order-item-qty-may-be-zero-or-negative

> **Slice contract for the coding agent.** Produced by the 86th LE31 daily-research pass (2026-11-08), Pick A.
>
> **Feature file**: `features/456-le31-order-item-qty-may-be-zero-or-negative-first-party-a-bill-line-may-carry-a-negative-quantity-and-nothing-refuses-it-v1-order-line-quantity-rule.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then `OrderItem(qty=0, …)` inserted → **ACCEPTED**; `OrderItem(qty=-5, …)` → **ACCEPTED**; `qty(-5) * unit_price(10.00) = -50.00`; the live DDL shows `qty INTEGER NOT NULL` with **no CHECK, no UNIQUE, no index**; and the constraint census over the whole schema reads **0 CHECK constraints across 10 tables**, the only UNIQUE being `bill.visit_id`). All seven checks pass; check 1's **demand** is classed **INFERRED** — **no operator has reported a bad quantity**, and the corpus confirms nobody owns the rule (a sweep over **941** feature/spec files returns **zero** hits for a bill-line quantity sign or size rule) — which is why this contract is deliberately **one constraint, one error message, six tests** and adds **no** route and **no** surface. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-daily-research-2026-11-08.md`.
>
> **Report**: `/opt/data/le31-daily-research-2026-11-08.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/456-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/446-le31-has-no-schema-evolution-mechanism` FIRST and confirm the ordering described under *Frozen contract* below.** **This slice is BLOCKED on 446** — a `CHECK` on an existing table is exactly the change `create_all()` cannot make.
6. **Read `features/449-le31-order-item-unit-price-is-mutable-in-place-with-no-trace` and `features/452-le31-an-order-line-can-be-served-and-still-say-it-is-new`** — the two sibling features that own the **other** columns of the same table. **They must not be merged with this one.**
7. **Read `features/450-le31-a-refund-has-no-payment-to-be-capped-against`** — the closest feature in spirit, and the one whose design must be reconciled with this constraint (see *Frozen contract*).
8. **Decide and RECORD whether zero is allowed** — *recorded default: **zero is NOT allowed**; the rule is `qty > 0`* (feature *Open questions* 1).
9. **Add the `CHECK` constraint** in the same change, using the **database-level** mechanism (see *Frozen contract*).
10. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_order_line_with_non_positive_quantity_is_refused` — on today's code the insert simply **succeeds**.
11. **Add the raw-`INSERT` test** — the one that distinguishes a real database constraint from a model-level validator.
12. **Update `features/02-order-taking.md`**'s data-model line so the contract and the schema agree.
13. **Record the precedent** — this is **one of the first value-level `CHECK` constraints in LE31's schema** — and point at features 404 and 455 so the three do not contradict each other.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Add a refund, a credit line, or a negative-quantity path.** Feature **450** owns that. **This slice's whole purpose is to make the absence of a refund mechanism visible rather than to fill it.**
- **Add a `CHECK` constraint on any money column, on `stock_entry.qty_delta`, or make the tables `STRICT`.** Feature **404** owns that family. **This slice adds one value check on one quantity column.**
- **Add a sign constraint to the ledger.** `StockEntry.qty_delta` is **legitimately negative** — a sale consumes stock. **This is the single most likely way for this slice to be implemented wrongly, and it is called out on purpose.**
- **Change `OrderItem.unit_price`, or add any trace of it.** Feature **449** owns it.
- **Change `OrderItem.status`, `fired_at`, `ready_at` or `served_at`.** Feature **452** owns the status/timestamp disagreement.
- **Change `Batch.qty_remaining` or `Batch.qty_start`.** Feature **374** owns the derived stock quantity, on a different table.
- **Add the missing `Bill → order_item` edge, or derive `Bill.subtotal_items` from the lines.** Feature **435** owns that. **This slice owns the shape of one line.**
- **Add a `CHECK` on `menu_item.name` or any `MenuItem` change.** Feature **458** owns the dish-name uniqueness — a different table, a different slice.
- **Add a `UniqueConstraint` on `table_.label`.** Feature **455** owns that.
- **Derive or constrain `DerivedTip.amount`.** Feature **457** owns that.
- **Migrate, backfill, or rename existing order lines.**
- **Add a maximum quantity, a quantity format, or a category rule.** The upper bound is *Open questions* 2 and is explicitly **not decided here**.
- **Change the menu UI or the floor-plan UI.** The mock-up is `index.html`; feature 08's scope.
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**
- **Add a router or a Telegram command.** The slice ships the constraint. **Surfaces are a later feature.**

**Disambiguation**: this slice is about **the sign and size of one order line's quantity**. It is **not** about the ledger's quantity (404 / 374), the line's price (449), the line's status (452), refunds (450), the bill's line membership (435), the dish's name (458), the tip's derivation (457), or the schema-evolution mechanism (446).

## Frozen contract

**The one thing this contract exists to make true:** *a bill line carries a positive quantity of something — so the subtotal can only ever be a sum of real things.*

Concretely, after this slice lands:

1. **The DATABASE refuses an order line whose quantity is zero or negative.** Not the application — the database.
2. **The rule is `qty > 0`** — *recorded default*. **The implementer must record the choice** (feature *Open questions* 1). **The reason zero is excluded** is that a zero-quantity line occupies a row, appears on the bill, appears on the kitchen ticket, and appears in every per-dish sales report as a dish that was ordered — **a line that says "ordered" and means "none".**
3. **The refusal is an `IntegrityError` the write path handles**, and the error **names the dish and the quantity**: *"cannot order tiramisu with quantity -5"* — not a stack trace.
4. **A positive quantity is still accepted**, and so is a **large** quantity — **there is no upper bound** (feature *Open questions* 2).
5. **The constraint is enforced by the DATABASE, not by a Pydantic validator.** **A `Field(gt=0)` is a Python-side check at the model boundary and is NOT a database constraint** — it does not fire on a direct `INSERT`, a seed script, a migration, or a future service. **The contract requires a table-level `CheckConstraint` in `__table_args__`.** A `Field` validator may be added *in addition*, for a nicer message — **but it must not be the rule.**
6. **No new column is added and no new table is added.** The rule constrains an existing column.
7. **The rule applies to every row regardless of `status`** — *recorded default*. A cancelled line is removed or zeroed by the cancellation path, not left with a negative quantity; **the cancellation path is not in scope here.**
8. **The line's total is NOT constrained.** The rule is on `qty` alone. **The line's total is `qty * unit_price`, and `unit_price` is mutable in place (feature 449)** — a constraint relating two mutable quantities would be false as soon as either moved.
9. **No existing order line is renamed, migrated or backfilled.** There is no order route today, so no order line can exist in a database this code built.
10. **The ledger is untouched.** `StockEntry.qty_delta` may be negative and always will be.

### The 446 ordering — this slice is BLOCKED on it

**446 must land first, or in the same PR as this slice.**

Feature 446 proved, by execution, that `create_all()`:

> *"**adds missing tables but NEVER alters, renames, drops or retypes an existing column** — a changed column is **silently ignored** and the old column keeps serving, so **a feature that adds a column lands, merges, deploys, passes its tests, and the column does not exist in the running database.**"*

**The same failure applies verbatim to a `CHECK` constraint.** Without 446, this slice would land, merge, deploy, pass its tests — **and the constraint would not exist in the running database.**

**446's own contract names the features it blocks** (408, 415, 420, 421, 435, 438, 439, 442, 443, 445). **This feature must be added to that list, and the PR description must name 446.**

**This slice does NOT introduce Alembic.** §3.2 forbids it in v1. It **depends on 446** and adds nothing further.

### The 450 interaction — a rule that will need revisiting, and that is recorded now

**Feature 450 owns the missing refund concept.** Until 450 lands, **a negative order line is the only way to take money off a bill in LE31**, and it is **indistinguishable from an unauthorised refund** — both are `qty < 0` on an order line.

**This constraint will therefore block 450's implementation if 450 models a refund as a negative order line.** That is the correct outcome for now (an unauthorised negative line must not be possible), but **the interaction must be recorded when 450 is implemented.** **If 450's design is close to landing, read 450 first and record which order was used.**

### The 456/449/452 collision — three features, one table

**449** owns `unit_price`; **452** owns `status` against the timestamps; **456** owns `qty`. **All three touch `class OrderItem` in `backend/app/models.py`.** If they land in separate PRs, they will conflict on the class body and must be **rebased, not dropped**. If they land in the same PR, **each must remain independently reviewable** — a reviewer must be able to check the `qty` constraint on its own. **Flag this in the PR description.**

## Files to touch

**Create:**

- `backend/tests/test_order_item_qty_is_positive.py` — the regression tests.

**Modify:**

- `backend/app/models.py` — **only** `class OrderItem`: add `__table_args__` with the `CheckConstraint`. **Nothing else in this file changes.**
- `features/02-order-taking.md` — **one line**: the data-model line, to state the rule.

**Read but do not modify:**

- `features/446-le31-has-no-schema-evolution-mechanism.md` — **the hard dependency.**
- `features/450-le31-a-refund-has-no-payment-to-be-capped-against.md` — the interaction to record.
- `features/449-le31-order-item-unit-price-is-mutable-in-place-with-no-trace.md` — the sibling on the same class.
- `features/452-le31-an-order-line-can-be-served-and-still-say-it-is-new.md` — the sibling on the same class.
- `features/404-le31-sqlite-tables-not-strict-…md` — the adjacent constraint family; the first-constraint precedent.
- `features/435-le31-bill-records-no-which-lines-it-charged-…md` — the adjacent bill rule.
- `PROJECT_CHARTER.md` — §3.2, §4.1, §7.

## Mandatory LE31 skill list

- **`le31-conventions`** — §3.2, §4.1, §7, the truth invariant, the seven-check gate.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done*.
- **`le31-feature-pipeline`** — where the artefacts land.
- **`le31-handoff-spec`** — the slice-contract shape.
- **`le31-backend`** — the FastAPI/SQLModel layering and the session boundary.

**Also read** `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §4.1 (SQLite dev / Postgres prod), and §7 (the quality bar).

## Mandatory inputs

- The zero-allowed decision — **recorded, not assumed**.
- Feature 446's status — **it must have landed, or must land in this PR.**
- Feature 450's status — **recorded so the interaction with the refund concept is not lost.**

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases

| # | Case | Expected |
|---|---|---|
| 1 | insert an order line with `qty = 0` | **REFUSED** |
| 2 | insert an order line with `qty = -5` | **REFUSED** |
| 3 | insert an order line with `qty = 1` | **ACCEPTED** (the default) |
| 4 | insert an order line with `qty = 100` | **ACCEPTED** — **no upper bound** |
| 5 | the error message | **names the dish and the quantity** |
| 6 | a **raw `INSERT`** through the SQLAlchemy core | **REFUSED by the database** — *this is the test that proves the rule is a constraint and not a validator* |
| 7 | the constraint's **presence in the DDL** | `CHECK (qty > 0)` present on `order_item` |
| 8 | the constraint on **Postgres** (if a test DB is available) | the same refusal — **and record what was actually run** |
| 9 | `StockEntry(qty_delta=-1)` | **ACCEPTED** — *the ledger is unaffected* |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Build a throwaway SQLite DB from LE31's own `models.py`.
2. Insert `OrderItem(qty=3, unit_price=Decimal("10.00"))` → **accepted**.
3. Insert `OrderItem(qty=0, …)` → **show the refusal**.
4. Insert `OrderItem(qty=-5, …)` → **show the refusal**, with the message naming the dish and the quantity.
5. Show `qty(-5) * unit_price(10.00) = -50.00` is now **unreachable**, and that a positive line still totals `30.00`.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code the zero and negative inserts **succeed** — there is no constraint at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

The verification venv from prior passes can be reused: **`/tmp/le31-daily-2026-11-06/.probe-venv`** (SQLModel + SQLAlchemy + SQLite) — the same venv this pass's probes used. **`/opt/data/le31-verify-2026-10-27/.venv`** is the older equivalent. **Do not provision a new venv if one of these works.** If a Postgres test DB is **not** available, **say so plainly and record what was actually verified on SQLite** — do not claim the Postgres row was tested.

## Rollback path

**Fully reversible in one step.**

- **Revert the commit** and the constraint is gone.
- **No data is at risk**: **no order-taking route exists in the shipped backend** (`backend/app/routers/` contains only `tables.py`), so no order line can have been created by shipped code — and therefore **no non-positive quantity can exist** in a database this code built. *(Recorded, and it is the reason this slice is free today and expensive later.)*
- **The one caveat**: if a live database **did** acquire a non-positive quantity through another path, removing the constraint restores the old behaviour and **the bad row stays** — it is not repaired by a rollback, and **this slice does not repair it.**

## Sign-off gap

**What the agent MUST NOT decide:**

- **Whether zero is allowed** — recorded default: **not allowed** (`qty > 0`). **Owner decision; the implementer records it.**
- **Whether there is an upper bound on a line's quantity** — recorded default: **no**. **Owner decision.**
- **How a cancelled line is represented** — recorded default: the rule applies to every row regardless of `status`; **the cancellation path is out of scope** (feature 37 owns the void-rationale concept).
- **What to do about existing non-positive quantities in a live database** — an **operational cleanup for the owner**, explicitly out of scope here.
- **Anything about refunds (450), the line's price (449), the line's status (452), the bill's line membership (435), the dish's name (458), the tip (457), or the ledger's quantity (404 / 374).**

**What the agent must report back:**

- The **zero and negative inserts** before and after, as observed.
- The **zero-allowed decision**, as recorded in the code.
- The **DDL** the constraint produced.
- **Whether the constraint is enforced by the database** — with the raw-`INSERT` result as evidence. **A `Field(gt=0)` alone does not satisfy this contract and must not be reported as if it did.**
- **Whether 446 had landed**, and if not, **what happens on a database where `order_item` already exists** — the constraint will **not** be created by `create_all()` on an existing table.

## Handoff summary

**One sentence:** *Make a bill line's quantity mean one thing — one database-level `CHECK`, one error message, one raw-`INSERT` test — and do it now, while no order route exists and the constraint is still free.*
