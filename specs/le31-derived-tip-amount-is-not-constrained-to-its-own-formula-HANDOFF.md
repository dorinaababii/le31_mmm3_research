# HANDOFF — le31-derived-tip-amount-is-not-constrained-to-its-own-formula

> **Slice contract for the coding agent.** Produced by the 86th LE31 daily-research pass (2026-11-08), Pick B.
>
> **Feature file**: `features/457-le31-derived-tip-amount-is-not-constrained-to-its-own-formula-first-party-the-row-that-is-documented-as-computed-is-a-free-standing-number-v1-derived-tip-formula-enforcement.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then a bill with `total_paid=25.00, subtotal_items=20.00, subtotal_tax=2.00` — the class docstring's formula gives **3.00** — and `DerivedTip(bill_id=1, amount=999.00)` → **ACCEPTED**; on a second, underpaid bill (`total_paid=10.00` against `22.00` of items+tax, formula gives **-12.00**) a tip of **-12.00** → **ACCEPTED**; and the live DDL shows `amount NUMERIC(10, 2) NOT NULL` with **no CHECK, no default, no derivation**). All seven checks pass; check 1's **demand** is classed **REPORTED** — **the charter's P0 says the tip is *derived* and *never manually entered*, and the schema contradicts it** — and check 3 records the one real constraint on the implementation: **a plain SQL `CHECK` cannot express a rule over another table's columns**, so the enforcement must live in the write path. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-daily-research-2026-11-08.md`.
>
> **Report**: `/opt/data/le31-daily-research-2026-11-08.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/457-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/420-le31-total-paid-means-tendered-not-received` FIRST.** It establishes what `total_paid` means, and therefore **what the formula yields.** **This slice depends on it.** If 420 has not landed, **record which meaning was used and that the derived values will change when 420 lands.**
6. **Read `features/410-le31-two-money-rule-sources`** for the money **rounding rule**. **Do not invent a third rule.** If 410 has not landed, **record the rule used and why.**
7. **Read `features/415-le31-bill-closes-visit`** — **it owns the bill-closing write path, and that route does not exist yet.** See *Frozen contract* for the ordering requirement.
8. **Implement the derivation** as a small pure function in the service layer, returning the amount **and** the `formula_version` it used.
9. **Refuse a caller-supplied `amount`** that disagrees with the derivation, with a message naming the bill and both figures. **A supplied amount that agrees is accepted.**
10. **Write the failing test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_a_tip_that_disagrees_with_the_formula_is_refused` — on today's code the wrong amount is **ACCEPTED**.
11. **Update `features/05-payment-tip-reconciliation.md`**'s data-model line so the contract and the schema agree that `amount` is derived.
12. **Record the precedent** — LE31 now has **a derived money value**, and `derived_tip` is the first table whose value is computed rather than supplied.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Change what `total_paid` means.** Feature **420** owns it. **Read it; do not re-implement it.**
- **Add a tax rate, a tax rounding rule, or a third money rule.** Feature **408** owns the rate; feature **410** owns the rule reconciliation. **Use the recorded rule; do not invent one.**
- **Add a `CHECK` constraint on `derived_tip.amount`'s shape, or make the tables `STRICT`.** Feature **404** owns that family. **This slice owns the value's *meaning*, not its shape.**
- **Add a `CHECK` constraint claiming to enforce the formula.** **A plain SQL `CHECK` may only reference columns of the same row** — it cannot reference `bill.total_paid`. **An agent that writes one is writing a rule that does not say what the contract says.**
- **Add the `Bill → order_item` edge, or derive `subtotal_items` from the lines.** Feature **435** owns that. **This slice uses the bill's stored columns as they are.**
- **Add the bill-closing route itself.** Feature **415** owns it. **See *Frozen contract* — this slice's rule has nowhere to live until that route exists.**
- **Change the formula itself.** That is feature 420's and feature 408's business. **This slice makes the tip equal the formula; it does not decide what the formula is.**
- **Resolve the split-bill case.** Feature **14** owns it. **See *Frozen contract*.**
- **Add a refund, or change what a refund does to the tip.** Feature **450** owns refunds.
- **Add a `CHECK` on `order_item.qty` or a `UniqueConstraint` on `menu_item.name`.** Features **456** and **458** own those.
- **Add a tip-correction / supersession mechanism** (a second tip row, a tombstone, a `superseded_by` column). **This is a v2 shape — it would change `derived_tip`'s primary key — and it is explicitly out of scope.** *The adjacent evidence records it as a real tension; recording it is not resolving it.*
- **Migrate, backfill, or re-derive existing tip rows.**
- **Change the owner-recap bot or the reconciliation UI.** Feature 39 and feature 05 own those; **this slice does not change them.**
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**
- **Add a Telegram command.** The slice ships the derivation. **Surfaces are a later feature.**

**Disambiguation**: this slice is about **the tip row equalling the formula over the bill it points at**. It is **not** about the meaning of `total_paid` (420), the money rounding rule (410), the tax rate (408), the shape of the money columns (404 / 411), where the subtotal comes from (435), the bill-closing route (415), split bills (14), or refunds (450).

## Frozen contract

**The one thing this contract exists to make true:** *the tip on a bill is the number LE31's own formula produces for that bill — derived, never taken from a caller.*

Concretely, after this slice lands:

1. **`DerivedTip.amount` is computed from the bill**, as `total_paid − (subtotal_items + subtotal_tax)`, in **`Decimal` arithmetic**, using the **recorded rounding rule** (feature 410 — or the rule the implementer records).
2. **A caller-supplied `amount` that disagrees with the derivation is REFUSED**, with a message naming the bill, the supplied figure and the derived figure. **A caller-supplied amount that AGREES is accepted** — *Open questions* 5; refusing every supplied amount would break a round-trip and teach the caller the rule is hostile.
3. **`formula_version` is written by the derivation**, not by the caller — and it must refer to something. *Recorded default: the implementer defines `v1` as a single named constant the derivation uses, and the stored value is that constant's value.* **A bare literal default with no referent is feature 448's shape and must not be reproduced.**
4. **One tip row per bill** — already true, because `bill_id` is the primary key, and **this slice must not weaken it.**
5. **A negative derived tip is NOT refused** — *recorded default* (feature *Open questions* 1). **The bill being underpaid is a fact about the bill, not an error in the tip.** Refusing the write would leave the bill closed with **no tip row at all**, which is worse.
6. **The derivation uses `Decimal` end to end and does NOT round-trip through `float`.** Feature 411 proved `Decimal` is a Python-side guarantee the storage layer does not enforce — **this slice is on the Python side, so this is the one place the guarantee can actually be kept.**
7. **No new table and no new column.** The rule changes the **write path**, not the schema.
8. **No existing tip row is re-derived, backfilled or deleted** by this slice.
9. **The tip is stored, not computed on read.** The charter's P0 says *"`tip` field appears on `DerivedTip` row"*; the table already exists. **A computed-on-read tip would remove the column rather than constrain it — a v2 decision, not this slice's.**

### ⭐ The enforcement shape — a `CHECK` cannot do this, and the contract says so

**A plain SQL `CHECK` constraint may only reference columns of the same row.** `amount` depends on `bill.total_paid`, `bill.subtotal_items` and `bill.subtotal_tax` — **three columns of another table.** There is no portable `CHECK` that expresses *"this number equals that formula over there"*, and there is no portable trigger that would keep it true across SQLite and Postgres without duplicating business logic into the database.

**Therefore the enforcement is in the write path.** A `CHECK` on `amount` could only assert something about `amount` alone (`amount = round(amount, 2)`) — **which is feature 404's shape check and does not enforce the formula.** A tip of 999.00 passes it perfectly.

**Why the write path and not a trigger or a view:** the trigger puts business logic in the database, where LE31's other rules live in Python and would need to be duplicated per engine; a view would not protect the stored value. **The write path is where LE31's other invariants already live** — feature 452's "a served line must not still say it is new" is enforced there too. **One place, one rule.**

### ⭐ The 415 ordering — this slice's rule has nowhere to live until the bill route exists

**There is no bill-closing route in the shipped backend.** `backend/app/routers/` contains only `tables.py` (`list_tables`, `seat_party`). Feature **415** records this verbatim: *"no bills router exists and nothing ties a paid bill to a closed visit."*

**The tip is computed at bill close.** So this slice has two honest options, and **the implementer must record which one they took:**

- **(a) Land 415 (or the bill-closing route) first, and put the derivation in that route.** *Recorded default — this is the cleaner option and the one this contract expects.*
- **(b) Land this slice together with the route**, in the same PR. **If the agent does this, they must not re-implement 415's edge** — the route must be 415's route, with the derivation added to it.

**What the agent must NOT do is invent a third thing:** a *separate* tip-writing path that bypasses the bill-closing route. **Two write paths for a derived value is how the value drifts.**

### ⭐ The 420 dependency — read first, and record the order

**Feature 420 establishes that `total_paid` means *tendered*, not *received*, so the change is booked as tip.** **That changes what the formula yields.** The two features are **dependent, not conflicting** — 420 owns the *input*, this slice owns the *output*.

**If 420 lands after this slice, the derived values change and this slice's tests must be updated.** The implementer must say **which order was used and why.**

### ⭐ The 14 tension — the split-bill case is a real rabbit hole, and it is NOT this slice's to solve

**On a split bill (feature 14) there are several tenders, so there is no single `total_paid`, so the derivation has no single answer.** The tip on a split bill must either be allocated across the splits or booked against the whole bill.

**This slice must not resolve it and must not be widened to.** It is recorded in feature *Open questions* 2 as an **open design question for feature 14**. **If 14 has landed, this slice must read it before implementing the derivation.** **If 14 has not landed, the implementer must record that the derivation is currently defined for a single-tender bill and that it will need revisiting.**

## Files to touch

**Create:**

- `backend/tests/test_derived_tip_is_derived.py` — the regression tests.

**Modify:**

- `backend/app/services/tips.py` — **create** if absent (or the service module where the bill-closing logic lives): the pure derivation function and the formula-version constant. **If the bill-closing route does not exist yet, see the 415 ordering in *Frozen contract* — do not create a parallel write path.**
- the bill-closing write path — the refusal of a disagreeing caller-supplied amount, and the writing of `formula_version`. **Only if that path exists; see the 415 ordering.**
- `features/05-payment-tip-reconciliation.md` — **one line**: the data-model line, to state that `amount` is derived.

**Read but do not modify:**

- `features/420-le31-total-paid-means-tendered-not-received-…md` — **the input dependency; read first.**
- `features/410-le31-two-money-rule-sources-…md` — **the rounding rule.**
- `features/415-le31-bill-closes-visit-…md` — **the route this slice's rule lives in.**
- `features/14-split-bills.md` — **the open tension.**
- `features/404-le31-sqlite-tables-not-strict-…md` — the adjacent shape family.
- `features/411-le31-money-precision-declared-not-enforced-…md` — the adjacent precision family.
- `features/408-le31-tax-rate-has-no-home-…md` — the adjacent rate.
- `PROJECT_CHARTER.md` — §3.2, §4.1, §7, and the P0 acceptance criterion (line 47).

## Mandatory LE31 skill list

- **`le31-conventions`** — §3.2, §4.1, §7, the truth invariant, the seven-check gate.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done*.
- **`le31-feature-pipeline`** — where the artefacts land.
- **`le31-handoff-spec`** — the slice-contract shape.
- **`le31-backend`** — the FastAPI/SQLModel layering and the session boundary.

**Also read** `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), and **the P0 acceptance criterion at line 47**, which is the rule this slice enforces.

## Mandatory inputs

- The **rounding rule** — recorded (from feature 410, or the implementer's recorded choice).
- The **meaning of `total_paid`** in the version being implemented — recorded (from feature 420, or the implementer's recorded note).
- Feature **415**'s status — **recorded, because the rule has nowhere to live until the route exists.**
- The **negative-tip** decision — recorded default: **not refused**.

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases

| # | Case | Expected |
|---|---|---|
| 1 | close a normally-paid bill | the tip equals `total_paid − (subtotal_items + subtotal_tax)` exactly |
| 2 | supply an amount that **agrees** with the formula | **ACCEPTED** — *a rule that only ever refuses is a bad rule* |
| 3 | supply an amount that **disagrees** | **REFUSED**, and the message names the bill and both figures |
| 4 | write a **second** tip row for the same bill | **REFUSED** (the primary key must survive) |
| 5 | the derivation's return type | `isinstance(result, Decimal)` — **and it must not round-trip through `float`** |
| 6 | a bill whose items+tax exceed `total_paid` | the tip is **negative** and the write is **NOT refused** |
| 7 | `formula_version` on the written row | **the derivation's version**, not a caller-supplied string |
| 8 | the derivation on **Postgres** (if a test DB is available) | the same value — **and record what was actually run** |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Build a throwaway SQLite DB from LE31's own `models.py`.
2. Create a bill with `total_paid=25.00`, `subtotal_items=20.00`, `subtotal_tax=2.00`.
3. Close it → **show the tip row**: `amount = 3.00`.
4. Attempt to close a bill with a supplied tip of `999.00` → **show the refusal**, with both figures in the message.
5. Create an underpaid bill (`total_paid=10.00` against `22.00`) → **show the tip is `-12.00` and the write was not refused.**

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code the wrong amount is **ACCEPTED** — there is no rule at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

The verification venv from prior passes can be reused: **`/tmp/le31-daily-2026-11-06/.probe-venv`** (SQLModel + SQLAlchemy + SQLite) — the same venv this pass's probes used. **`/opt/data/le31-verify-2026-10-27/.venv`** is the older equivalent. **Do not provision a new venv if one of these works.** If a Postgres test DB is **not** available, **say so plainly and record what was actually verified on SQLite** — do not claim the Postgres row was tested.

## Rollback path

**Fully reversible in one step.**

- **Revert the commit** and the derivation is gone; the write path accepts a caller-supplied amount again.
- **No schema change, so no data migration and no data at risk.** The rule is **code, not DDL** — which is one of the reasons this slice is cheaper than features 456 and 458.
- **No existing tip row is re-derived or deleted by the rollback**, and **none is repaired by it.**
- **The one caveat**: if a live database **did** acquire a wrong tip through another path, reverting restores the old behaviour and **the wrong row stays** — this slice does not repair it.

## Sign-off gap

**What the agent MUST NOT decide:**

- **What happens on a split bill** — feature **14** owns it. **This slice must not resolve it and must not be widened to.** *Recorded default: the derivation is defined for a single-tender bill.*
- **The rounding rule**, if feature 410 has not landed — *the implementer records the rule used and why.*
- **What `formula_version = "v1"` refers to, in detail** — *the implementer defines it as a named constant and records it; the **semantics** of a future `v2` are not this slice's.*
- **Whether a wrong tip can be corrected afterwards** — **a supersession mechanism is a v2 shape** (it would change `derived_tip`'s primary key). **Out of scope, and recorded as an open question.**
- **Whether the tip row should be stored at all** — *recorded default: **stored**, because the charter's P0 says so and the table exists.* **Removing the column is a v2 decision.**
- **Anything about refunds (450), the tax rate (408), the subtotal's derivation (435), or the bill-closing route itself (415).**

**What the agent must report back:**

- The **three derivations** (normal, agreeing-supplied, disagreeing-supplied) as observed.
- The **underpaid-bill case** as observed — the negative tip and the non-refusal.
- The **rounding rule** used, and where it came from.
- **Which meaning of `total_paid`** was used, and whether 420 had landed.
- **Whether 415 had landed**, and **which of the two ordering options in *Frozen contract* was taken** — **and, if the route did not exist, what the agent did and why.**
- The **DDL of `derived_tip` before and after**, to show it did **not** change — unless the agent added a column, in which case **446 blocks it and that must be reported.**

## Handoff summary

**One sentence:** *Make the tip mean one thing — compute it from the bill in the write path, refuse a caller-supplied amount that disagrees, and do it now, while no bill has ever been closed and the rule is still free.*
