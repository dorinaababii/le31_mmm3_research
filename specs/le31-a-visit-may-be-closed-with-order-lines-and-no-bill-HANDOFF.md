# HANDOFF — le31-a-visit-may-be-closed-with-order-lines-and-no-bill

> **Slice contract for the coding agent.** Produced by the 100th LE31 daily-brainstorm pass (2026-11-07), Pick B.
>
> **Feature file**: `features/454-le31-a-visit-may-be-closed-with-order-lines-and-no-bill.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then a `Visit` with **one** `OrderItem` worth **16.00**, the visit closed with **no bill** — **ACCEPTED**; the table freed; the two kinds of closed visit **indistinguishable** to any plain query without a join to `bill`). **The two numbers: `SUM(order_item on the closed visit) = 16.00` vs `SUM(bill.total_due) = 0.00`.** All seven checks pass; check 1's **demand** is classed **medium** — a walk-out is a real restaurant event, but its *frequency* in this restaurant is not evidenced and is not claimed. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-brainstorm-2026-11-07.md`.
>
> **Report**: `/opt/data/le31-brainstorm-2026-11-07.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/454-…`) and this handoff.
2. Load **`le31-conventions`** — §3.1 (*"operational transitions are explicit user actions"*), §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §3.3 (the append-only discipline), §3.6 (money is `Decimal`, never `float`), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/415-le31-bill-closes-visit-edge` FIRST and confirm the ordering described under *Frozen contract* below.** 415 owns the *paid* close; this slice owns the *unpaid* close. **They are siblings and must land together.**
6. **Read `features/388-le31-table-state-machine` and confirm the ordering.** 388 supplies the release path that closes a visit; this slice supplies the rule that release must obey.
7. **Decide and RECORD the void's shape** — a nullable column on `Visit`, or a `visit_void` table — per *Frozen contract* item 4 and *Open questions* 1. **The choice must be recorded in the code.**
8. **Add the guard on the visit-close write** and the **void write**, in **one transaction**.
9. **Derive the void's amount from the visit's lines** — never from the request body.
10. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_closing_a_visit_with_lines_and_no_bill_is_refused` — on today's code the close simply **succeeds**.
11. **Answer feature 415's Open Question 3** in this contract, and add a one-line pointer in 415's Open questions.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Create `bills.py`, write a bill, or re-implement the tip derivation.** Feature **415** owns the bill route, the bill→visit edge, the tip derivation and the refusal rules. **This slice is 415's complement, not its replacement.**
- **Add a `status` column to `Table`, a double-seating guard, or a release endpoint.** Feature **388** owns those. **This slice supplies the rule the release path must obey** — it does not supply the release path.
- **Add a `bill_line` table, or re-sum the order lines to compute a money total.** Feature **435** owns the membership. **See the 435 ordering note below — this is the rule most likely to be got wrong.**
- **Add a write guard on `OrderItem`.** Feature **436** owns that (no line may be *created* against a dead visit). **This slice is about a visit being *closed* without an account.**
- **Implement refunds, partial refunds, or comped *items*.** Feature **450** owns refunding a **paid bill**; feature **05** owns the payment rules. **A voided visit has no bill to refund.**
- **Touch `Shift`, `Shift.variance`, or the cash reconciliation.** Features **391** and **426** own those.
- **Change the `DerivedTip` formula or its refusal rules.** Feature **05** owns the formula; feature **420** owns the negative-tip refusal.
- **Add a `CHECK` constraint, a `UniqueConstraint`, or make the tables `STRICT`.** Feature **404** owns that family.
- **Modify `UserRole`, or add a role policy.** Feature **403** owns the role policy. *Open questions* 4 records a manager-role question **as an owner decision, not a change here.**
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**
- **Add a Telegram command or a bot handler.** The void is a **waiter-side** action. **Do not add a bot surface.**
- **Accept the void's amount, the bill's total, or the tip from a request body.** Derive them.

**Disambiguation**: this slice is about **a visit that closes without the money being accounted for**. It is **not** about the bill→visit edge (415), the table status (388), the bill-line membership (435), the active-visit write guard (436), refunds (450), the role policy (403), the cash reconciliation (391/426), or the negative tip (420).

## Frozen contract

**The one thing this contract exists to make true:** *a visit may not close with order lines and no bill, unless the close is a recorded void/walk-out that accounts for the money.*

Concretely, after this slice lands:

1. **Closing a visit that has order lines and NO bill is REFUSED**, unless a void/walk-out is recorded in the same transaction.
2. **The refusal writes nothing** — no void row, no `closed_at`, no partial state. (Same discipline as feature 415: *"a refused bill closes nothing"*.)
3. **A void is a FACT, not an edit.** It does **not** UPDATE or DELETE the visit's order lines. The lines stay on the visit; the void sits beside them. *(The charter's append-only reasoning applies: a void that edits history destroys the very record the owner needs.)*
4. **The void's shape is recorded by the implementer** — a nullable column on `Visit`, or a `visit_void` table. **Either is acceptable.** The contract requires the facts to exist and the guard to enforce them; it does not mandate the storage.
5. **The void carries:** a **reason** (walk-out / comped / written off / error), an **actor** (who recorded it), and an **amount** (the money written off).
6. **The void's amount is DERIVED from the visit's lines**, never accepted from the request body. **Same rule as 415**: *"It must **not** accept `subtotal_items`, `total_due`, or a tip amount."*
7. **The void and the close are ONE transaction.** A void that can be written after the close is an edit to a closed visit and is forbidden. (Recorded default, feature *Open questions* 3.)
8. **The two numbers become comparable.** For every closed visit: `SUM(lines)` equals `bill.total_due`, **or** equals the void's amount plus a billed amount. **The reconciliation surface shows both numbers side by side.**
9. **The money is a `Decimal`, never a `float`** — and the guard is in code, because feature 411 proved the `Decimal` declaration is **not enforced** by the storage layer.
10. **The paid close is unaffected.** A visit with a bill closes exactly as feature 415 specifies. **This slice adds one precondition; it does not modify 415's rules.**
11. **No `OrderItem` row is ever deleted or modified.** The visit's lines are the record of what the party ate.
12. **A void is not a refund.** A voided visit has no bill; a refund needs a bill and a payment. **The two are different objects** and a reviewer must be able to check each on its own.

### The 415 ordering — resolve before writing code

**415 must land first, or in the same PR as this slice.**

Feature 415 owns the *paid* close and puts the `Visit.closed_at` write in the bill route, **in the same transaction** as the `Bill` and `DerivedTip` writes. It records, verbatim:

> *"**What closes a walk-out's visit is undecided.**"*

**This slice answers that question** — the walk-out's visit is closed by a **recorded void**, and 415's paid close is unchanged.

**But 415 alone will not see the hole.** 415 says the release route is 388's business, and 388 says *"**If you find yourself writing a bill-closing endpoint, stop — that is feature 14/05's job.**"* **So 415 implements the paid close faithfully and never notices that a second, unbilled close path exists.** That is the upstream-of-filed-work condition: **a filed feature would implement the defective shape faithfully.** Name 415 in the PR description.

**Do not implement 415's bill route here. Do not re-implement its tip derivation or its refusal rules.**

### The 388 ordering — resolve before writing code

Feature 388 supplies the release path — the route that closes the open visit and frees the table. **388 will close visits with money owed unless this rule exists.**

**388 and this slice must land together, or 388's release path must not ship until this slice lands.** **This slice does not add the release path and does not add a status column** — it supplies the rule the release path obeys.

### The 435 ordering — the rule most likely to be got wrong

The guard needs to know *whether the visit has order lines*. **Feature 435 states verbatim:**

> *"a reconciliation would have to re-sum the visit's lines, which is exactly what feature 435 says you must not do."*

**Therefore:**

- **If 435 has landed** — use its membership table. Do not re-sum.
- **If 435 has not landed** — the guard may answer the question by **counting** the visit's `order_item` rows (a yes/no, **not** a money derivation), and **must not compute a money total from them**.

**Whichever it does, the implementer must record which.** And note the consequence for *Frozen contract* item 6: **if 435 has not landed, the void's amount cannot be derived from a membership table** — so the void's amount derivation and 435's membership are genuinely coupled. **If the implementer cannot derive the amount without re-summing the lines, that is a reason to bring 435 into the same PR.** State it plainly in the PR description rather than quietly re-summing.

### The 446 dependency — it depends on the shape

- **Shape A (a nullable column on `Visit`)** — adds a column. **`create_all()` cannot add a column to an existing table**, so **feature 446 (`le31-has-no-schema-evolution-mechanism`) is a HARD dependency.** 446 must land first or in the same PR.
- **Shape B (a `visit_void` table)** — adds a table, which `create_all()` *can* create. **446 is not needed for the table itself**, though it remains the right place to record the prod-migration debt.

**The implementer must state which dependency applies.** If Shape A is chosen and 446 has not landed, **the column will be written, merged, deployed, pass its tests, and not exist in the running database.**

## Files to touch

**Create:**

- `backend/app/services/visit_service.py` (if it does not exist) — the close guard and the void write.
- `backend/tests/test_visit_close_requires_bill_or_void.py` — the regression tests.

**Modify:**

- `backend/app/models.py` — **only** the void's shape (Shape A: one nullable column on `Visit`; Shape B: one new table). **Nothing else in this file changes.**
- `features/415-le31-bill-closes-visit-edge-…md` — **one line** in its Open questions, recording that the walk-out question is answered by feature 454. **One line. Do not rewrite 415.**

**Read but do not modify:**

- `features/415-le31-bill-closes-visit-edge-…md` — the sibling; the paid close.
- `features/388-le31-table-state-machine-…md` — the sibling; the release path.
- `features/435-le31-bill-line-membership-…md` — the membership; the ordering constraint.
- `features/436-le31-charter-active-visit-is-undefined-…md` — the adjacent write guard.
- `features/450-le31-a-refund-has-no-payment-to-be-capped-against.md` — the adjacent, different object.
- `features/446-le31-has-no-schema-evolution-mechanism.md` — the dependency (Shape A).
- `PROJECT_CHARTER.md` — §3.1, §3.2, §3.3, §3.6, §4.1, §7.

## Mandatory LE31 skill list

- **`le31-conventions`** — §3.1, §3.2, §3.3, §3.6, §4.1, §7, the truth invariant, the seven-check gate.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done*.
- **`le31-feature-pipeline`** — where the artefacts land.
- **`le31-handoff-spec`** — the slice-contract shape.
- **`le31-backend`** — the FastAPI/SQLModel layering and the session/transaction boundary.

**Also read** `PROJECT_CHARTER.md` — §3.1 (*"operational transitions are explicit user actions"*), §3.2 (out of scope for v1), §3.3 (append-only ledger), §3.6 (money is `Decimal`, never `float`), §4.1 (SQLite dev / Postgres prod), and §7 (the quality bar).

## Mandatory inputs

- Feature 415's exact refusal vocabulary, so the two guards do not use two words for one rule.
- Feature 435's membership shape — **or** an explicit statement that it has not landed, with the consequence recorded.
- The **two numbers** to compare: the visit's line sum and the bill's total.

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases

| # | Case | Expected |
|---|---|---|
| 1 | close a visit with **one order line** and **no bill** | **REFUSED** |
| 2 | the refusal writes | **nothing** — no void, no `closed_at` |
| 3 | close the same visit **with a recorded void** | **ACCEPTED**, and the void's amount **equals the lines' sum** |
| 4 | close a visit that **has a bill** | **ACCEPTED** (415's path, unchanged) |
| 5 | a void recorded **after** the close | **REFUSED** (one transaction) |
| 6 | the void's amount **supplied by the caller** | **REFUSED** — it is derived, never accepted |
| 7 | the day's reconciliation | shows the lines' sum **and** the billed amount **and** the void, side by side |
| 8 | the order lines after a void | **unchanged** — not deleted, not modified |
| 9 | a `Decimal` check on the void's amount | it is a `Decimal`, **not** a `float` |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Build a throwaway SQLite DB from LE31's own `models.py`.
2. Seat a visit, add **one** order line worth **16.00**.
3. **Try to close it with no bill** → **show it refused.**
4. Record a void, close it → **show it accepted**, and the void's amount = **16.00**.
5. Show the reconciliation displaying the two numbers and the void.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code the close simply **succeeds** — there is no refusal at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

The verification venv from prior passes can be reused: **`/opt/data/le31-verify-2026-10-27/.venv`** (SQLModel + FastAPI + SQLite). **Do not provision a new venv if this one works.**

## Rollback path

**Reversible in one step, but the shape determines the cost.**

- **Shape A (a column on `Visit`)** — the column can be dropped. **Reversible.** *(A `NOT NULL` column with no default would not be droppable without a table rebuild — **do not make the column `NOT NULL`**; the void is optional and the guard enforces it.)*
- **Shape B (a table)** — the table can be dropped. **Reversible.** The order lines and any bills are untouched either way.
- **No data is at risk**: the state this feature forbids **has never been produced** — no bill has ever been closed by any shipped code (feature 415 proves the route does not exist), and the only `Visit` write in the whole backend is `backend/app/routers/tables.py` line 51.
- **The void, once written, is a fact.** Rolling back the code does not delete voids that were written under it. **Record this**: a rollback leaves historical voids in place, and the reconciliation must still display them. *(That is the intended behaviour — a void is a record of a real event — but it must be stated, not discovered.)*

## Sign-off gap

**What the agent MUST NOT decide:**

- **The void's storage shape** (column vs table) — the implementer **records** the choice; **both are acceptable**.
- **How much of a void is recoverable** — recorded default: the void records the amount written off; recovery is a separate fact and is **not modelled here**.
- **Whether a void requires a manager's role** — recorded default: yes, but **feature 403 owns the role policy** and this slice does not modify it. **Owner decision.**
- **Whether the void may be added after the close** — recorded default: **no**.
- **What a "service day" is** (405) and **what a "walk-out" costs the business** — the latter is an owner/accounting decision.
- **Anything about refunds** (450) or **comped items** (05).

**What the agent must report back:**

- The **two numbers** before and after the guard, as observed.
- The **shape chosen and why**, recorded in the code.
- Whether **435 had landed**, and if not, **which** question the guard answered by counting rather than by membership — and whether the void's amount therefore required 435.
- Whether **446** is a dependency under the chosen shape, and if Shape A, **what happens on a database where the table already exists**.

## Handoff summary

**One sentence:** *Stop a visit from closing with money owed and no bill — one guard, one recorded void, one reconciliation surface, and it must land with feature 415's paid close or that close will not see the hole.*

**Three picks of the 100th daily-brainstorm pass (2026-11-07):**

- **Pick A:** `le31-two-tables-can-carry-the-same-label` — **feature 455**.
- **Pick B (this one):** `le31-a-visit-may-be-closed-with-order-lines-and-no-bill` — **feature 454**.
- **Pick C:** `le31-sqlite-silently-drops-the-utc-offset` — **feature 453**.

**Feature**: `features/454-le31-a-visit-may-be-closed-with-order-lines-and-no-bill.md`
**Report**: `/opt/data/le31-brainstorm-2026-11-07.md`
