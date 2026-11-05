# HANDOFF — le31-stockentry-may-name-a-batch-and-an-order-line-for-different-dishes

> **Slice contract for the coding agent.** Produced by the 98th LE31 daily-brainstorm pass (2026-11-05), Pick A.
>
> **Feature file**: `features/441-le31-stockentry-may-name-a-batch-and-an-order-line-for-different-dishes.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then two raw inserts — `StockEntry(batch_id=<batch of item 2>, qty_delta=-1, reason='sale', ref_order_item_id=<order line for item 1>)` and `StockEntry(batch_id=<batch of item 1>, qty_delta=-7, reason='sale', ref_order_item_id=<order line with qty=2>)` — **both ACCEPTED**). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod, same SQLModel code), §7 (the quality bar: *"Time is UTC"*, *"No magic numbers"*, *"No dead code"*, *"End-to-end before commit"*), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. **Read `features/421-…` FIRST** and confirm the ordering described under *Frozen contract* below. **Feature 421 is about to build the single `StockEntry` write path, and it places the business rules out of scope. If 421 lands without this rule, it will implement the defect faithfully.**
5. **Create `backend/app/services/__init__.py` and `backend/app/services/stock_rules.py`** with `assert_ledger_row_is_coherent(se)` — **one definition of the rule, imported by every caller.** The helper reads `batch.menu_item_id` and `order_item.menu_item_id` / `order_item.qty` and raises `ValueError` when they disagree.
6. **Apply the helper at the write path** — feature 421's single write path if it exists; **otherwise expose the helper and leave the call site, recording that in the commit message.**
7. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_ledger_row_naming_a_different_dish_is_refused` — it is what proves the two pointers are mutually coherent.
8. **Record the deferral-chain correction** — one line in `features/421-…` *Adjacent work* and one in `features/385-…`, saying *"the coherence rule between the two pointers is feature 441."*

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Add the `ref_order_item_id` foreign key.** That is **feature 426**. **⚠️ ORDERING: 426 must land first, or in the same PR.** **This feature does not add an FK.**
- **Enable `PRAGMA foreign_keys` on SQLite.** That is **feature 427**. **⚠️ ORDERING: 427 must land first, or in the same PR**, or every FK in the table stays decorative. **This feature does not enable the pragma.**
- **Create the single `StockEntry` write path, the lint rule, or the `StockReason` reversal member.** That is **feature 421**. **This feature supplies a rule and a helper; 421 supplies the place the rule is called from.**
- **Add `OrderItem.batch_id`.** That is **feature 385** — the *forward* pointer. **This feature does not add it.**
- **Constrain the SIGN of `qty_delta` against its `reason`.** That is **feature 432**. **Different axis: 432 is about `reason`, this is about the order line.** **The two may share a PR, but they must be two separate rules in separate code.**
- **Add the `StockEntry.by_user_id` foreign key.** That is **feature 417**.
- **Change `Batch.qty_remaining`, or derive it.** That is **feature 374**.
- **Add `CHECK` constraints to `stock_entry`.** That is **feature 404** (and feature **404** owns the mechanism generally). **This feature's rule is an application-layer invariant, not a constraint.** It is **expressible** as a composite FK, but **that is not this slice** — see *Open questions* 4 in the feature file.
- **Change the `sold_out` withdrawal semantics.** That is **feature 419**.
- **Write a `StockEntry` row.** No ledger row has ever been written outside its class declaration — `grep -rn "StockEntry(" backend/` returns exactly **one** hit. **This feature adds a rule; it does not create a ledger.**
- **Create `backend/app/routers/inventory.py` or any selling endpoint.** Out of scope. **There is no selling path today.**
- **Change the `qty_delta` column type.** That is **feature 437**.
- **Decide the multi-batch sale case.** See *Open questions* 1 in the feature file. **The recommended starting position is to ship the COHERENCE rule and defer the MAGNITUDE rule until the FIFO question (feature 03's open question + feature 385) is answered** — but that is a recommendation, and the agent must **record which of the two it implemented.**
- **Introduce Alembic**, or write a migration. Charter §3.2: `init_db()` is the v1 policy. **No historical rows exist to migrate.**
- **Change `PROJECT_CHARTER.md`.** The charter is the owner's document.

**Disambiguation**: this slice is about **whether a ledger row's two pointers agree with each other and with the order line they name**. It is **not** about whether the pointers *exist* (426), about the forward pointer (385), about the sign (432), about the actor (417), about the quantity derivation (374), or about where the write path lives (421).

## Frozen contract

**The one thing this contract exists to make true:** *a ledger row that says "this dish was consumed because of that order line" is a claim the database can check — and LE31 currently cannot check at all.*

Concretely, after this slice lands:

1. A `StockEntry` with `reason='sale'` whose `batch_id` resolves to a **different** `menu_item_id` than its `ref_order_item_id` is **refused**.
2. A `StockEntry` with `reason='sale'` whose `ABS(qty_delta)` **does not equal** the referenced order line's `qty` is **refused** — *if the magnitude rule is in scope for this slice; see the boundary table below.*
3. A `StockEntry` with `reason='sale'` naming the **same** dish and the **same** quantity is **accepted**.
4. A `StockEntry` with `reason='initial'`, `'restock'` or `'waste'` and `ref_order_item_id = NULL` is **accepted** — **those reasons are not constrained by this rule.**
5. **No schema change.** The rule is an application-layer invariant, enforced by one helper.

**The prohibition:** *writing a ledger row whose two pointers disagree, or whose magnitude contradicts the order line it names.*

### The 421/426/427 ordering — resolve before writing code

| If | Then |
|---|---|
| **421 has not landed** (today's state) | 441 lands alone. The helper is created and **exported**; the call site is left to 421. **The commit message must say so.** |
| **421 has landed first** | 441's helper **must** be called from 421's write path. **If 421's write path does not call it, this slice has failed** — a rule nobody calls is not a rule. |
| **426 has not landed** | The rule **still works**, because the helper reads `order_item` **by id** and the order line it finds is read fresh from the table. **But the back-pointer can name a nonexistent row**, so the helper must treat *"the order line does not exist"* as **its own error**, distinct from *"it is about a different dish."* **Record which behaviour you implemented.** |
| **426 has landed** | The helper's "does not exist" branch becomes **unreachable in production** (the FK refuses first) and stays reachable in dev (the pragma is off until 427). **Keep the branch.** |

**Either way: 421 is the one that matters.** Its write path is where the rule must be called.

### Why the coherence rule and not a `CHECK` constraint

A `CHECK` constraint **cannot** express this rule: it would have to compare a column in `stock_entry` with a column in `batch` and a column in `order_item`, and SQLite `CHECK` constraints may only reference columns of the row's own table. **A composite foreign key** could express the *dish* half (`(batch_id, menu_item_id) → batch(batch_id, menu_item_id)`) but would require a `UNIQUE` index on `batch(batch_id, menu_item_id)`, which does not exist — **that is a schema change and is deliberately not in this slice.**

**So: one helper, called at the write path.** The **database** backstop is feature **413**'s territory (triggers) and is **recorded, not adopted** — and feature 413 has already recorded that **triggers exist in Postgres and not in SQLite**, so a trigger would reintroduce a dev/prod divergence.

### Why the helper is the enforcement and not the ORM

SQLModel does **not** validate a field against a `str, Enum` annotation on write, and it certainly does not validate a cross-table relation. **The helper is the only thing standing between a caller and a wrong row.** It must be called from the write path, and the regression test must assert the helper raises — **not** that some future caller remembers to call it.

## Files to touch

| File | Action | Notes |
|---|---|---|
| `backend/app/services/__init__.py` | **create** | `backend/app/services/` **does not exist today.** |
| `backend/app/services/stock_rules.py` | **create** | `assert_ledger_row_is_coherent(se)` — the one definition of the rule. Plus the small resolvers it needs. |
| `backend/app/services/stock_writer.py` | **create or modify** | Feature 421's single write path, **if it exists**. **If it does not exist, do NOT create it** — leave the helper exported and record that. |
| `backend/tests/test_stock_ledger_coherence.py` | **create** | The five regression tests listed below. **Confirm the project's test path before assuming this one.** |
| `features/421-le31-stockentry-append-only-linter-rule…` | **modify** | One line in *Adjacent work*: the coherence rule between the two pointers is feature 441. |
| `features/385-le31-order-item-batch-provenance…` | **modify** | One line in *Adjacent work*: the coherence rule between the two pointers is feature 441. |

**Not touched:** `backend/app/models.py` (no schema change), `backend/app/routers/tables.py`, `backend/app/db.py`, `backend/app/bot/`, `backend/app/config.py`, `index.html`, `PROJECT_CHARTER.md`, every other model.

**⚠️ If feature 442 has landed**, `backend/app/models.py` **will** carry `CHECK` constraints on the enum columns — **this feature does not touch them, and does not add one for `reason`.** 442 owns the *membership* of `reason`; 432 owns its *sign*; **this feature owns the relation between the pointers.**

## Mandatory LE31 skill list

The coding agent **must** load these before writing code. They are in the project repo at `skills/`, and on this VPS they are **not** in the standard `skills_list` index — read them from disk:

- **`le31-conventions`** — `skills/le31-conventions/SKILL.md`. **The fixed stack, the hard invariants, and the seven-check gate.**
- **`le31-v1-feature-pattern`** — `skills/le31-v1-feature-pattern/SKILL.md`. **The contract shape and the Definition of Done.**
- **`development`** → `speckit-specify` / `speckit-plan` / `speckit-tasks` / `speckit-implement`. **Product behaviour changes go through the development pipeline.**
- **`pre-merge-review`** — **product code does not merge on the author's say-so.** An independent reviewer must sign off.

**Also read (not skills, but mandatory context):** `features/421-…` (the write path and the append-only rule), `features/426-…` (the back-pointer FK), `features/427-…` (the pragma), `features/385-…` (the forward pointer), `features/432-…` (the sign rule), `features/374-…` (the quantity derivation), `features/417-…` (the actor FK), `features/404-…` (the `CHECK` mechanism), and `PROJECT_CHARTER.md` §3.3 and §4.3.

## Mandatory inputs

| Input | Where | Why |
|---|---|---|
| `PROJECT_CHARTER.md` §3.3 (the derivation invariant), §4.3 (the insert-path table) | repo root | **§4.3 names the sign for every reason** — feature 432's territory. **§3.3 says current stock is derived from entries**, which is why a wrong entry is a wrong number. |
| `features/421-…` (append-only + the single write path) | `features/` | **The ordering dependency.** Read it first. |
| `features/426-…` (the back-pointer FK) | `features/` | The ordering dependency, and the boundary. |
| `features/427-…` (the pragma) | `features/` | The ordering dependency. |
| `features/385-…` (the forward pointer) | `features/` | The boundary. |
| `features/432-…` (the sign rule) | `features/` | The nearest sibling. **Different axis.** |
| `features/374-…` (the `qty_remaining` derivation) | `features/` | **Different fact: the derivation vs the row.** |
| The parent's proof script | `/opt/data/le31-brainstorm-2026-11-05-scripts/audit_lifecycle3.py` | **The parent's execution transcript for this finding** (probe G). Run it with `/opt/data/le31-verify-2026-10-27/.venv/bin/python` — that venv has `sqlmodel`/`fastapi`/`pydantic` installed; **the system Python does not have `sqlmodel`.** |
| The pass report | `/opt/data/le31-brainstorm-2026-11-05.md` | The pass, the evidence, and the rejected alternatives. |

## Verification protocol reference

**Reference**: `skills/le31-research-workflow/SKILL.md` (the curl-only anti-fabrication and signed-delta discipline) and `skills/le31-first-party-defect-proving/SKILL.md` (the execution-proof method). **Read `le31-first-party-defect-proving` — this feature was proven that way and the agent must preserve that property in its own tests.**

**The five required regression tests** (all in `backend/tests/test_stock_ledger_coherence.py`):

1. `test_ledger_row_naming_a_different_dish_is_refused` — **the boundary test.** A sale row whose `batch_id` names a batch of a **different** `menu_item_id` than its `ref_order_item_id` → **raises**.
2. `test_ledger_row_with_wrong_magnitude_is_refused` — a sale row whose `ABS(qty_delta)` is **not** the order line's `qty` → **raises**. *Skip and record if the magnitude rule is deferred per *Open questions* 1.*
3. `test_coherent_sale_row_is_accepted` — a sale row naming the **same** dish and the **same** quantity → **no raise**.
4. `test_non_sale_rows_with_null_ref_are_accepted` — an `initial` row and a `waste` row with `ref_order_item_id = NULL` → **no raise**.
5. `test_sale_row_naming_a_nonexistent_order_line_is_refused` — **if feature 426 has not landed**, the helper must still refuse it rather than raising `AttributeError`.

**Method — the one that matters:** **write the tests first, watch them fail against the current code, then apply the change and watch them pass.** A test that only ever passed proves nothing, and this feature's entire value is the *distinction*, which is exactly the kind of thing a test that never failed cannot certify.

**End-to-end before commit** (charter §7): run the actual write path — **or, if no write path exists, the actual helper** — against a real database and observe the behaviour change. **Do not declare done from a diff or from green tests alone.**

**Anti-fabrication:** every claim in the PR description must be traceable to a command you ran and its output. **No number, no status code and no test count that you did not observe.**

## Rollback path

**Fully reversible, and deliberately so.**

- **The code rollback:** delete `services/stock_rules.py`, delete the test file, revert the two one-line notes in `features/421-…` and `features/385-…`, and remove the helper call from the write path. **Nothing today reads a field that does not exist yet, so no existing behaviour can regress.**
- **The data rollback:** **there is nothing to roll back.** No `StockEntry` row has ever been written (`grep -rn "StockEntry(" backend/` returns exactly one hit — the class declaration). **The ledger is empty.**
- **The migration rollback:** LE31 uses `init_db()` (charter §3.2 — **Alembic is a non-goal for v1**), so there is no migration file to revert. **If a migration file is created anyway, that is a scope violation of this contract.**
- **The one irreversible thing:** **if a ledger row is written under the wrong rule while this feature is in flight, it is permanent.** The ledger is append-only **by charter** — that is a feature, and it is exactly why this rule must land before the write path. **That asymmetry is the reason this contract exists.**

**Rollback cost:** minutes. **No data is at risk.**

## Sign-off gap

**What this contract does NOT establish, and the agent must not assume:**

- **That a `StockEntry` write path exists.** It does not. **If 421 has not landed, this slice creates a rule and a helper with no caller** — which is a **legitimate, recorded** outcome, but it means **the rule is not yet enforced**. **Say so in the PR description.**
- **That feature 426's foreign key will be enforced.** It will not, until feature 427 enables the pragma. **The helper's "order line does not exist" branch is therefore still reachable in dev.**
- **That the multi-batch sale case is settled.** It is not. See *Open questions* 1.
- **That the ledger's `reason` values are constrained.** They are not, until feature 442 lands. **A row with `reason='gift'` would pass feature 432's sign check and this feature's coherence check** — because the coherence check compares *pointers*, not *reason membership*. **That is feature 442's job and it is recorded, not adopted here.**
- **That the `qty_remaining` derivation is correct.** It is not — feature 374 owns that. **This feature does not fix it.**
- **Any owner decision about the permitted sale semantics.** See *Open questions* 1 in the feature file. **The agent is not authorised to make it.**

## Handoff summary

One helper, one call site (or one exported helper with no caller), one test file, two one-line notes in other feature files. **Two to five hours.**

The gap was **proven by execution**, not inferred: LE31's `StockEntry` carries **two** pointers that both name what was affected — `batch_id` and `ref_order_item_id` — and **nothing in the schema says they must be talking about the same dish**. The parent wrote a ledger row naming the **cake's** batch against the **soup's** order line and the database **accepted it**. A second row claimed **7** units consumed against an order line of **2**.

**The one boundary that must not be crossed:** feature **421** owns *where a ledger row may be written*; this feature owns *what a ledger row may say*. **And the ordering is the sharpest point: 421 is about to build the one and only function through which every `StockEntry` in LE31 will ever be written, and it has already decided that business rules are somebody else's job.** **If this rule is not in place when 421 lands, the wrong rule becomes permanent at the moment the right rule becomes cheap.**

**The one thing that must not happen:** a ledger row whose two pointers disagree. **The ledger is append-only. A wrong row is forever.**
