# HANDOFF — le31-order-item-unit-price-is-mutable-in-place-with-no-trace

> **Slice contract for the coding agent.** Produced by the 84th LE31 daily-research pass (2026-11-06), Pick A.
>
> **Feature file**: `features/444-le31-order-item-unit-price-is-mutable-in-place-with-no-trace.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite DB, then `UPDATE order_item SET unit_price = 1.00 WHERE id = :id` → **ACCEPTED**; the line's total silently changed from **5.00** to **2.00**; **0** audit rows were written; the original **2.50** is **not recoverable**; and `UPDATE menu_item SET unit_price = 99.00` was **also accepted silently**. The full ten-table schema contains **no price-change table, no audit table and no history table**). All seven checks pass; see the feature file's *LE31 gate verdict* table in `/opt/data/le31-daily-research-2026-11-06.md` and the contract's *Description* / *Why this matters*.
>
> **Report**: `/opt/data/le31-daily-research-2026-11-06.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/444-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar: money is `Decimal` never `float`, append-only invariant, "reported, never repaired"), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Create `backend/app/services/order_prices.py`** with `change_order_item_price(session, order_item, *, new_price, reason, by_user_id) -> OrderItemPriceChange` — **one definition of "the price changed"**, and **the only supported way to change an order line's price**.
6. **Add `OrderItemPriceChange` and `PriceChangeReason`** to `backend/app/models.py` — an **append-only** history table. **Never UPDATE or DELETE a row in it.**
7. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_price_change_is_recorded_and_the_previous_price_is_recoverable` — it is what proves the history is not decorative.
8. **Read `features/446-le31-has-no-schema-evolution-mechanism` FIRST** and confirm the ordering described under *Frozen contract* below. **Feature 446 is about to write the pre-`create_all()` backup and the fail-closed rule; this slice adds a NEW TABLE, which `create_all()` can do — but only on a database where the schema can actually be applied.**
9. **Record the deferral-chain corrections** — one line each in the feature files this slice touches, saying *"the order line's price history is feature 444."*

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Create the order-taking router, or any write path that takes an order.** This slice ships the **helper and the history**; the call site belongs to the future order flow. **The commit message must say the call site is outstanding.**
- **Change `OrderItem.unit_price`'s type, its nullability, or its `max_digits`/`decimal_places`.** It stays exactly as it is: a `Decimal` snapshot of the current price.
- **Add a discount model, a promo-code model, a comp model, or a rounding rule.** A discount is **feature 05**; the tax rate and the rounding mode are **feature 408**; the money-rule reconciliation is **feature 410**; the Decimal precision guard is **feature 411**. This slice only **labels** a change `discount`.
- **Change `Bill`, `DerivedTip` or `Bill.visit_id`.** The bill-close route is **feature 415**; the bill-line membership is **feature 435**; the tip semantics are **feature 420**.
- **Add a status-transition log or touch `OrderItem.status`.** That is **feature 379**. A status change and a price change are **two different events** and get **two different records**. **Do not merge them and do not modify 379's log.**
- **Write a `StockEntry` row on a price change, or touch `Batch`.** A price change moves no stock. `Batch` is **feature 445**'s column.
- **Add a `MenuItem` price-history table, or change `MenuItem`.** The menu-price overwrite was observed and is recorded in the feature file's *Adjacent work — recorded, NOT picked*. **Do not widen into it.**
- **Add guest identity, a guest id, a guest name, or any guest contact field.** The actor is a **staff** member (`app_user`). Charter §3.1: v1 stores counts, not guest identities.
- **Restrict which roles may change a price.** Role policy is **feature 403**. This slice **records** the actor; it does not decide who may act. (The feature file's *Open questions* record this as an owner decision.)
- **Introduce Alembic, write a migration, or change `PROJECT_CHARTER.md`.** The charter is the owner's document. **Feature 446 owns the schema-evolution mechanism**; this slice must not invent its own.
- **Add a new pip dependency.** The whole slice uses SQLModel + the standard library.

**Disambiguation**: this slice is about **the history of an order line's price**. It is **not** about the bill's arithmetic (408/410/411/415/420/435), the line's status transitions (379), the line's allergens (439), the line's seat partition (440), the batch's provenance (385), the batch's preparer (445), the ledger's actor (417), the ledger's write path (421), or the role policy (403).

## Frozen contract

**The one thing this contract exists to make true:** *an order line's price can be changed, and the change is recorded, attributed, and reversible to understand — the previous price is never silently destroyed.*

Concretely, after this slice lands:

1. A line's price is changed through **one helper** — `change_order_item_price(...)` — and **nowhere else**.
2. Every change writes **exactly one** append-only `OrderItemPriceChange` row carrying `from_price`, `to_price`, `reason`, `by_user_id` and `at`.
3. The history row and the updated `order_item.unit_price` are written in **the same transaction** — if either fails, neither happens.
4. The **previous price is recoverable**: `SELECT ... FROM order_item_price_change WHERE order_item_id = ?` returns the price the line held before every change, in order.
5. A change to the **menu's** price does **not** write a price-change row — the menu is configuration, not the line.
6. A **no-op change** (`new_price == current price`) is **refused** — it is a caller bug, not a change.
7. A change with a **`float`** price is **refused** — money is `Decimal`, and `Decimal(float)` carries the float's error.
8. A change with a **negative** price is **refused**.
9. A change with a **nonexistent actor** is **refused** by the foreign key.
10. A price change writes **no `StockEntry` row** and **no `Batch` change**.

**The prohibition:** *an `UPDATE` against `order_item.unit_price` that does not go through the helper* — and *a price-change history that is not append-only.*

### The 446 ordering — resolve before writing code

| If | Then |
|---|---|
| **446 has not landed** (today's state) | 444 lands **alone** for the new table (`create_all()` creates a missing table). **But the commit message MUST state that the production database has no way to apply a schema change, and that this slice's table cannot be created on it without feature 446.** |
| **446 has landed** | 444 lands normally. `create_all()` on a differing schema now takes a backup first and **aborts if the backup fails**. |

**Either way, 444 must not introduce its own migration mechanism.** That is 446's job and widening into it is a defect.

### The sequencing constraint — this must land WITH the first order write path

There is **no order-taking router today** (`backend/app/routers/` contains exactly `__init__.py` and `tables.py`). So nothing can currently set a line price, and this feature is **inert** until an order flow exists.

**That is the reason to land it now.** The moment a write path that can set a line price exists, the price becomes mutable in place. **The helper must be the way that path is written, or the guarantee is lost on day one.** The commit message must say: *"the call site is outstanding; the first order write path MUST use `change_order_item_price`."*

## Files to touch

**Create:**

| Path | What |
|---|---|
| `backend/app/services/order_prices.py` | `change_order_item_price(...)` — the one helper — plus the price-change validation. |
| `backend/app/services/__init__.py` | **if it does not exist** — `backend/app/services/` is currently absent (`ls backend/app/` returns `bot/`, `routers/` and the module files). Feature 408's *Out of scope* already notes this directory does not exist. |
| `backend/tests/test_order_prices.py` | The regression tests (the repo's test layout — **check `backend/` for the existing test directory and follow it**; do not invent a second layout). |

**Modify:**

| Path | What |
|---|---|
| `backend/app/models.py` | Add `OrderItemPriceChange` and `PriceChangeReason`. **Change nothing else in this file.** |

**Read but do not modify:**

| Path | Why |
|---|---|
| `features/446-le31-has-no-schema-evolution-mechanism.md` | The ordering. |
| `features/415-…`, `features/435-…`, `features/420-…`, `features/408-…`, `features/410-…`, `features/411-…` | Boundaries — the money rules and the bill. |
| `features/379-…` | The sibling (status) log — **do not merge with it**. |
| `features/005-…` (payment / tip reconciliation) | The discount model. |
| `backend/app/models.py` — `OrderItem`, `Bill`, `DerivedTip`, `StockEntry`, `Batch` | The shapes you must not change. |

## Mandatory LE31 skill list

The external agent **must** load, in this order, before writing code:

1. **`le31-conventions`** — the seven-check gate, the hard invariants, §3.2 (fixed stack, no new dependency, `init_db()`-not-Alembic), §7 (the quality bar: money is `Decimal` never `float`; append-only; "reported, never repaired"), §4.1 (SQLite dev / Postgres prod — the **dev/prod divergence** trap), and the truth invariant (*never fabricate research results or execution output*).
2. **`le31-v1-feature-pattern`** — the canonical contract shape, the slicing rules (*model → domain operation → interface → realistic verification as one coherent slice*), and the *Definition of Done* (*"Done means the specified user completes the flow on the intended surface, resulting rows and derived values are inspected, forbidden and duplicate actions are safe, promised feedback appears, the regression gap was demonstrated where applicable, docs/status match reality, and the change is committed and pushed"*).
3. **`le31-feature-pipeline`** — where the artefacts land and the commit/push convention.
4. **`le31-handoff-spec`** — the frozen-contract discipline: *do not silently change the slice, scope, or verification path*.
5. **`development`** — the generic code pipeline (specify → plan → tasks → implement → independent review) for the implementation itself.

**Also read** `PROJECT_CHARTER.md` — §3.1 (in scope), §3.2 (out of scope for v1), §4.3 (the append-only ledger pattern), and §7 (the quality bar).

## Mandatory inputs

| Input | Path | Why |
|---|---|---|
| The feature contract | `features/444-le31-order-item-unit-price-is-mutable-in-place-with-no-trace.md` | The scope, the data model, the scenario table. |
| The research report | `/opt/data/le31-daily-research-2026-11-06.md` | The gate verdicts, the evidence, the duplicate sweep, and the *Adjacent evidence*. |
| The execution probe | `/tmp/le31-daily-2026-11-06/_parent_probe2.py` and `_parent_final.py` | **The parent-run probes that produced the evidence.** They import LE31's own `backend/app/models.py` and run against a throwaway SQLite DB. **Re-runnable.** The venv is at `/tmp/le31-daily-2026-11-06/.probe-venv` (`sqlmodel` 0.0.48 + `sqlalchemy` 2.0.57) — **if `/tmp` has been cleared, recreate it with `uv venv` + `uv pip install "sqlmodel>=0.0.42" "sqlalchemy<2.1"`.** |
| The raw fetches | `/tmp/le31-daily-2026-11-06/` | The third-party READMEs the evidence quotes come from (`readme/yixin-lot__posd.md` is the trigger). |
| The duplicate-sweep result | the feature file's *Adjacent work* + the report's *Duplicates skipped* | What is **already filed** and must not be re-picked. |

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases (from the feature file's scenario table)

| # | Case | Expected |
|---|---|---|
| 1 | Menu price changes 2.50 → 3.00 after the line is taken | line stays **2.50**; **no** price-change row |
| 2 | Line changed 2.50 → 1.00, reason `correction` | one row with `from_price=2.50`, `to_price=1.00`, actor, timestamp; `unit_price == 1.00` |
| 3 | Line changed twice | **two** rows, ordered; first `to_price` == second `from_price` |
| 4 | Change attempted with `new_price == current price` | **refused** — no row, no change |
| 5 | Change attempted with a `float` | **refused** — no row, no change |
| 6 | Change attempted with a negative price | **refused** — no row, no change |
| 7 | Change attempted with a nonexistent actor | **refused** by the FK |
| 8 | History read for a never-changed line | current price + **empty** history — **not an error** |
| 9 | A price change is performed | **no `StockEntry` row** |
| 10 | A price change is performed | **no `Batch` change** |
| 11 | The bill is derived after a price change (feature 415) | the bill uses the **new** price; the history does not change the derivation |
| 12 | A second user changes the same line | both changes recorded, in order, distinct actors |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Create a menu item, a table, a server, a visit and an order line **through the real ORM** (not raw SQL).
2. Change the line's price **through the helper**.
3. **Read the history back** and show the previous price is recoverable.
4. Show a **failed** change (case 4, 5 or 6) left **no row and no change**.
5. Show the **append-only** property: the history table's row count only ever **grows**.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (the price is overwritten and the history is empty), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

LE31's test suite runs on **SQLite**, while production is **Postgres** (charter §4.1). This slice adds **no column to an existing table** and **no constraint**, so there is **no dev/prod divergence risk** in the slice itself. **If the agent adds anything that Postgres would enforce differently — a `CHECK`, a `NOT NULL`, a length limit — that is a divergence and must be called out in the commit message.**

## Rollback path

| Aspect | Detail |
|---|---|
| **Revert** | `git revert` the commit. The new table is dropped with the model. |
| **Data at risk** | **None.** The new table holds only price-change history, which exists nowhere else. The `order_item.unit_price` column itself is **unchanged by this slice** — only the way it is set changes. |
| **Disable path** | Remove the single call site. The helper becomes unused; the history table goes stale but harmless. |
| **Migration / rollback cost** | **Zero** — the feature adds a table, and `create_all()` can create a table. **⚠️ But on a production database with no schema-evolution mechanism (feature 446 not landed), the table cannot be created there at all** — see the ordering table above. |
| **What remains safe if removed** | Everything. `OrderItem.unit_price` is unchanged and every existing behaviour keeps working. **The only loss is the history.** |
| **The one irreversible thing** | Nothing — **the history is append-only, but it is also new**. A wrongly-recorded price-change row is permanent by design (charter §4.3). That is the intended trade: **an append-only record of a mistake is recoverable by adding a correcting row; a mutable price is not recoverable at all.** |

## Sign-off gap

**What the agent must NOT decide:**

1. **Whether `discount` belongs in `PriceChangeReason`.** The recommendation is to include it as a **label only** (feature 05 owns the discount model). **The agent may implement the recommendation; the agent may NOT widen the enum beyond the five members listed in the feature file.**
2. **Who may change a price.** Role policy is **feature 403**. This slice records the actor, not who may act.
3. **Whether a price may be changed after the bill is paid.** A money rule, and the money rules are the owner's. **The recommendation is "no"; the agent may implement it if it is recorded as an owner decision, and must say so.**
4. **The four remaining `PriceChangeReason` members** — the feature file fixes the set. Adding a sixth is a scope creep, not an improvement.

**What the agent must report back:**

- The commit SHA and the push confirmation.
- The **failing-then-passing** output of the key regression test.
- The observed acceptance path (steps 1–5 above), with the actual rows shown.
- A statement of whether **feature 446** had landed when this was built, and what that means for the production database.
- A statement of whether the **call site is outstanding** (it is, today) — and that the first order write path must use the helper.
- Any deviation from this contract, stated explicitly rather than absorbed.

## Handoff summary

**One sentence:** *Give an order line's price a history — one append-only table, one helper, and the guarantee that a price change is recorded, attributed, and never silently destroys the previous value.*

**Three picks of the 84th daily-research pass (2026-11-06):**

| Pick | Slug | Gate | One line |
|---|---|---|---|
| **A** | `le31-order-item-unit-price-is-mutable-in-place-with-no-trace` | **build** | A line's price can be overwritten; the original is unrecoverable and the bill total silently changes. **This contract.** |
| **B** | `le31-batch-has-no-preparer` | **build** | `StockEntry.by_user_id` and `Shift.by_user_id` exist; `Batch` has no actor column, so the preparer of a batch is unknowable. |
| **C** | `le31-has-no-schema-evolution-mechanism` | **build (narrow form)** | `db.py` points at a directory that does not exist, and `create_all()` never alters an existing column. |

**Feature**: `features/444-le31-order-item-unit-price-is-mutable-in-place-with-no-trace.md`
**Report**: `/opt/data/le31-daily-research-2026-11-06.md`
**Bucket**: v1 · **Gate**: build · **Evidence**: OBSERVED (executed) · **Confidence**: high
