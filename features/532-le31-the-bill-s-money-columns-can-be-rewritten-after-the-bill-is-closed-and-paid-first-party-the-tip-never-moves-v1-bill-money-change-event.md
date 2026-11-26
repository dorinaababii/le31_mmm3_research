# Feature 532 — The bill's money columns can be rewritten after the bill is closed and paid, and the tip never moves

> **Pick B of Daily Brainstorm 2026-11-26 (108th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Bill`, verbatim (lines 158–169):
>
> ```python
> class Bill(SQLModel, table=True):
>     __tablename__ = "bill"
>
>     id: int | None = Field(default=None, primary_key=True)
>     visit_id: int = Field(foreign_key="visit.id", unique=True)
>     subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
>     subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)
>     total_due: Decimal = Field(max_digits=10, decimal_places=2)
>     total_paid: Decimal = Field(max_digits=10, decimal_places=2)
>     payment_method: PaymentMethod
>     paid_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     closed_by: int = Field(foreign_key="app_user.id")
> ```
>
> **Four `Decimal` columns holding the money, and not one of them has a history, a constraint, or a rule that says it may not change.**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one menu item, one batch, one visit, one order line and one bill):
>
> ```
>   UPDATE bill SET subtotal_items=0.01, subtotal_tax=0.00, total_due=0.01  ->  ACCEPTED
>   UPDATE bill SET total_paid=100.00                                        ->  ACCEPTED
>
>   bill.total_due                =  0.01
>   SUM(order_item.qty * unit_price) = 13.00     <- the real subtotal
>
>   derived_tip.amount (stored)   =  0.00
>   recomputed tip from the stored total_paid = 85.70
> ```
>
> **⭐ TWO NUMBERS THAT SHOULD AGREE, DISAGREEING — on the table the charter calls the record of what a guest paid.** The stored tip says €0.00. The tip the bill's own `total_paid` implies says **€85.70**. **Both are in the database. Nothing raised an error.**
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **564** feature contracts and **517** HANDOFFs returns **one** hit for a rule about the bill's money columns being immutable or traced — and that one hit is a **remark inside another feature's prose**, not a contract:
>
> | sweep | files | hits |
> |---|---|---|
> | `bill.{0,40}(subtotal_items\|total_due\|total_paid).{0,50}(immutable\|frozen\|rewrite\|mutable\|history)` | 1 | 1 |
> | `bill.{0,30}(recompute\|re-derive).{0,40}(on read\|always)` | 0 | 0 |
> | `bill.{0,40}(snapshot\|copy).{0,30}(subtotal\|total)` | 0 | 0 |
> | `derived_tip.{0,40}(formula_version\|amount).{0,40}(immutable\|frozen\|rewrite)` | 0 | 0 |
> | `tip.{0,30}amount.{0,40}(rewrite\|mutable\|history)` | 0 | 0 |
>
> The single hit is feature **450**, and it is the reason this slice is not owned: **450 says, verbatim, "`Bill.total_paid` stays exactly as it is."** 450's job is to make `total_paid` a *sum of payment rows* so a refund can be capped against a payment — **it explicitly leaves the column alone, and its own words are the reason the column's mutability is still unowned.**
>
> **⭐ AND THE NEIGHBOURS DISCLOSE IT.** Feature **415** owns the bill-close *route* and says the route's body *"must not accept a caller-supplied `subtotal_items` or tip"* — **that is a rule about the write, not about the stored value afterwards.** Feature **457** owns the tip's *formula* and says the tip is derived from *"the bill's own four money columns"* — **it constrains the formula, not the columns.** Feature **435** owns the `Bill → order_item` edge. Feature **448** owns the bill's human-facing identity. **None of them says a closed, paid bill's money may not be rewritten.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a wrong bill; the corpus confirms nobody owns the rule).

## Goal

Make a closed, paid bill mean **one thing**: **the money on a bill is what the guest paid, it is written once, and it cannot be quietly replaced.**

The concrete outcome: **a bill's money columns cannot be rewritten in place after the bill is closed**, and where the domain genuinely requires a change after the close (a refund, a correction, a service charge), that change is **a recorded event against the bill** — never a silent overwrite of a number.

## Scope

**In scope (v1):**

1. **The write-path guard.** Once a bill is closed (`closed` / `paid`), the money columns — `subtotal_items`, `subtotal_tax`, `total_due`, `total_paid` — are **written once**. Any later write is refused.
2. **The recorded correction.** A correction to a closed bill's money is an **event** carrying the bill, the column or the field that changed, the old value, the new value, the actor and the time. The mechanism is a new append-only table, mirroring feature **523**'s price-history table and feature **524**'s role-change event.
3. **The relation to the tip, stated explicitly.** Feature **457** owns the tip's formula. This slice does not change the formula. What this slice guarantees is that **the inputs the formula reads cannot change after the fact** — so the tip recorded against a bill and the tip that bill's columns imply **cannot drift apart**, and the €0.00-vs-€85.70 divergence above becomes impossible.
4. **The relation to the refund, stated explicitly.** Feature **450** owns refunds and will make `total_paid` a *sum of payment rows*. **This slice must not block that.** The contract states the ordering: **450's payment rows are the mechanism that records a refund; this slice's guard is the mechanism that says a refund is not an overwrite of `total_paid`.**

**Out of scope (v1):**

- **The tip formula itself.** That is **feature 05** (the rule) and **feature 457** (the formula's enforcement and its `formula_version`). This slice changes no formula and no `formula_version`.
- **The `Bill → order_item` edge and the derivation of `subtotal_items`.** That is **feature 435** (the edge) and **feature 415** (the close write and the derivation). This slice makes the derivation's *result* immutable; it does not change how it is derived.
- **The bill-close route.** That is **feature 415** — filed. This slice adds the guard that runs at the write site and the event table the guard consults.
- **The refund, the payment row and the refund cap.** That is **feature 450** — filed. **450 says "`Bill.total_paid` stays exactly as it is"**, and this slice does not contradict it: this slice says a closed bill's money is **written once**, and 450's payment rows are how a *legitimate* post-close money movement is recorded.
- **The tax rate and the meaning of `subtotal_tax`.** That is **feature 408** — filed. 408 owns the *rate*; this slice owns the *mutability*.
- **The `Decimal` arithmetic guarantee.** That is **feature 411** — filed. Unaffected, and read, not changed.
- **The meaning of `total_paid` (tendered vs received).** That is **feature 420** — filed.
- **Split bills.** That is **feature 14** — filed.
- **The bill's human-facing identity / number.** That is **feature 448** — filed.
- **The currency of the money columns.** Feature **409** records it as an open owner question. This slice does not add a currency column.
- **`Shift` and the `Shift ↔ Bill` money edge.** That is **feature 391** — filed.
- **Any change to `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan, menu or waiter-UI change.** The mock-up is `index.html`; feature **08**'s scope.
- **Alembic.**
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the defect

LE31's charter **P0** row 47 reads, verbatim:

> *"Waiter can close a bill; tip is **derived** as `total_paid − subtotal_items − subtotal_tax`."*
>
> *Acceptance criterion: "`tip` field appears on `DerivedTip` row; **never manually entered**."*

**That row is satisfied by the shape of the code and broken by the shape of the schema.** Feature **415** implements the route correctly: its request body *"accepts only `total_paid`, `payment_method` and `subtotal_tax`"*, and it *"must not accept a caller-supplied `subtotal_items`, `total_due`, or a tip amount"* — **415 refuses the caller at the door.** That is the right rule and it is filed.

**But the door is not the wall.** Once the row exists, the four money columns are four ordinary `Decimal` columns with no history and no constraint, and **the same process that was refused at the door can rewrite them directly.** The route's refusal is a property of *one function's argument parser*; the schema's mutability is a property of *the table*.

**And the charter's own acceptance criterion is silent on it.** *"never manually entered"* describes the **tip**. It says nothing about the four inputs the tip is derived from. A bill whose `total_paid` is rewritten after the close produces a tip that was **never manually entered** — and is now wrong.

### The execution, in full

```
=== F: bill's STORED derived columns rewritten in place ===
  UPDATE bill SET subtotal_items=0.01, total_due=0.01 -> ACCEPTED
  bill now: subtotal_items=0.01 subtotal_tax=0.00 total_due=0.01 total_paid=14.30
  SUM(order_item.qty*unit_price) = 13.00   <- the real subtotal

=== G: Bill.total_paid (money received) rewritten after payment ===
  UPDATE bill SET total_paid=100.00 -> ACCEPTED
  derived_tip.amount (stored) = 0.00
  recomputed tip = total_paid - (subtotal_items+subtotal_tax) = 85.70
```

**Read those two blocks together — they are the finding:**

1. **The bill's stored money was replaced with a number that has no relationship to the visit** — `total_due = 0.01` against a visit whose lines total €13.00. **The bill still adds up to itself** (`0.01 + 0.00 = 0.01`), which is exactly why it is dangerous: **a bill that is internally consistent and globally wrong passes every arithmetic check a reader would run.**
2. **The tip did not move.** `DerivedTip.amount` is a stored row; it is not recomputed when `total_paid` changes. The stored tip says **€0.00**; the tip the bill's own `total_paid` implies says **€85.70**. **The record of what the guest tipped and the record of what the guest paid now contradict each other, and both are on the same bill.** The formula was never violated — **it was simply never run again.**

### The rule this slice files

> **A closed bill's money is written once. A change to a closed bill's money is a recorded event carrying the old value, the new value, the actor and the time — and the bill's stored columns keep the value that was written at the close.**

**This is the second half of the seventh finding shape** — *a covered concept, an uncovered instance*. The concept *"the bill's money is a fact"* is covered: feature **457** owns the tip's formula, feature **415** owns the close write, feature **411** owns the `Decimal` guarantee, feature **420** owns the meaning of `total_paid`, feature **448** owns the bill's identity, feature **450** owns refunds. **Six features own six facets of the bill's money. The facet none of them owns is that the money cannot be quietly replaced after the fact.**

### Why an event table and not a column

The same precedent the corpus has already established twice, in the same family: feature **523** (the catalogue's price history) states it verbatim — *"Implemented as a TABLE, not a column — a `previous_price` column preserves one change and loses the second"* — and feature **524** (the role-change event) ships an event table for the same reason. **A `previous_total_paid` column would preserve one overwrite and lose the second.**

### The mechanism, stated as the implementer must write it

1. **A new append-only table** — the bill-money correction event: the bill, the field that changed, the old value, the new value, the actor (`by_user_id`) and the time. Never updated, never deleted.
2. **A guard at the write site.** A write that changes any of the four money columns on a **closed** bill is refused, unless the same transaction writes the corresponding event. **A write that changes them on an *open* bill is accepted** — the close write itself is one such write and must not be refused.
3. **The tip is not recomputed by this slice.** Feature **457** owns the formula and `formula_version`. **What this slice guarantees is that the formula's inputs are stable**, so the recorded tip and the bill's money cannot drift.
4. **The refund path is not blocked.** Feature **450** will make `total_paid` a sum over payment rows. **The guard must be written so that 450's rows are the mechanism for a legitimate post-close money movement, not a violation of it.** This is an explicit, named dependency, not a hope.

## Data model

**New table — the bill-money correction event.** Following the shape of feature **524**'s role-change event and feature **523**'s price history:

| column | type | meaning |
|---|---|---|
| `id` | int PK | |
| `bill_id` | int FK → `bill.id`, indexed | the bill whose money changed |
| `field` | str | which money column changed (`subtotal_items`, `subtotal_tax`, `total_due`, `total_paid`) |
| `old_value` | Decimal(10,2) | the value before the change |
| `new_value` | Decimal(10,2) | the value after the change |
| `by_user_id` | int FK → `app_user.id` | who made the change |
| `at` | datetime (UTC) | when |

**Rules the table carries:**

- **Append-only.** Never updated, never deleted. It is a fact table.
- **`field` names the column that changed**, so a bill's money history is one ordered list of `(field, old, new, who, when)`. **The list reconstructs the bill's money as it stood at any moment.**
- **The decimal *shape* is not this slice's rule.** Feature **404** owns `round(x, 2)` and `typeof(x) = 'integer'`; this slice owns *when a value may change*, not what a value may look like.

**No column is added to `bill`.** The bill keeps its four money columns; the history lives in the event table.

**`bill` is otherwise untouched** — `visit_id`, `payment_method`, `paid_at`, `closed_by` and the unique constraint on `visit_id` are all unchanged.

## Implementation

1. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:
   - the **close** write itself sets the money columns and is **ACCEPTED** (the guard must not block the legitimate write);
   - a write that changes `total_paid` on a **closed** bill with **no** event is **REFUSED**, and the stored value is unchanged;
   - a write that changes `total_paid` on a **closed** bill **with** an event in the same transaction is **ACCEPTED**, and the event carries the old value, the new value, the actor and the time;
   - a write that changes `total_paid` on an **open** bill is **ACCEPTED** with no event;
   - the event table rejects an update and a delete;
   - **the two-numbers check:** after any accepted change, the tip implied by the bill's money and the `DerivedTip` row stored against it **agree** — *or* the difference is exactly accounted for by a recorded event.
2. **Add the event model** to `backend/app/models.py`, following the `StockEntry` / role-change-event shape (an append-only fact with `by_user_id` and `at`).
3. **Add the write-path guard** where a bill's money is written. **Today the close write does not exist** — there is no bills router — so this slice adds the **helper** the future router will use and does **not** invent a router (the same discipline as feature **430** and feature **415**). **The helper's signature must make the safe path the only one the type system permits**: it either refuses, or it writes the event and the change together.
4. **Do not depend on a database constraint alone.** A `CHECK` cannot express "this value may not change after the close" — the database has no notion of a row's history. **The write path is the mechanism**; a trigger is possible but is feature **421**'s territory for the ledger and is **not** claimed here.
5. **State the ordering against the filed work explicitly** — see *Dependencies*.
6. **Do not modify `index.html`.**

## Telegram interaction

**None.** This slice adds no Telegram command, no bot handler and no message. **A manager approving a correction is a real workflow and is deliberately NOT designed here** — see *Open questions* 3.

## Dependencies

**⭐ THE UPSTREAM-OF-FILED-WORK RULE — TWO FILED FEATURES SIT ON TOP OF THIS ONE.**

- **Feature 415** implements the bill-close write and computes `subtotal_items` from the lines. **415 must land first, or in the same PR** — otherwise 415 ships a close write with **no guard behind it**, and the guard this slice adds would have to be retrofitted onto a route that already exists. **415 is unaffected by this slice's semantics** (it writes an *open* bill's money, which the guard permits) and the two are compatible.
- **Feature 450** makes `total_paid` a sum over payment rows and will own refunds. **450 says "`Bill.total_paid` stays exactly as it is"** — and 450's own words are why this slice is not owned by it. **The two must be designed together, not sequenced blindly:** 450's payment rows are *how* a legitimate post-close money movement is recorded; this slice's guard is *that a movement is never an overwrite of the stored column*. **If 450 lands first, this slice's guard must be written against 450's model, not against the current single-column model.**
- **Feature 457** owns the tip's formula and `formula_version`. **Unaffected** — this slice changes no formula. **What this slice adds is the stability of the formula's inputs**, which 457's own text identifies as *"the bill's own four money c[olumns]"*.
- **Feature 435** owns the `Bill → order_item` edge. Unaffected; read, not changed.
- **Feature 420** owns the meaning of `total_paid` (tendered vs received). **Read, not changed** — but note the interaction: a rewrite of `total_paid` after the close **changes what the tip means**, which is why the correction is an event rather than a silent overwrite.
- **Feature 404** owns the *shape* of money columns; **feature 411** owns the `Decimal` guarantee; **feature 408** owns the tax rate. All unaffected, all read.
- **Feature 446** owns the migration path. This slice **adds** a table, which `create_all()` handles; 446 becomes relevant only if the implementer also adds a `CHECK` in the same PR.
- **Feature 379** owns the actor convention for order-line transitions. **This slice uses the same convention** (a staff `app_user`) so that one actor model serves the whole ledger.

## Open questions

1. **What exactly marks a bill as "closed" for the guard's purposes?** LE31's `Bill` has no status column — closure is implied by the row's existence (and `visit.closed_at`, owned by feature **388**'s edge work). **Recommendation: treat the bill's existence as closed**, because the close write creates the row with its money. **But an explicit `closed_at` on `bill` may be the better shape and is not decided here.**
2. **Should the event table carry one row per changed field, or one row per correction carrying all four old and new values?** The former is simpler to write and to query; the latter makes a correction atomic. **Recommendation: one row per changed field** — a correction that changes two fields is two facts, and the event table is a fact table. **Not decided here.**
3. **Should a manager approval be part of this?** The charter has no approval workflow for money, and feature **403**'s manager-PIN work (*"Manager approval by PIN for voids, large discounts and refunds"*) would be the natural owner. **Recommendation: this slice refuses and records; the approval policy is 403's.** **Not decided here.**
4. **Does a refund (450) count as a "change to a closed bill's money"?** Recommendation: **no** — a refund is a *new fact about a payment*, recorded as a payment row, not an overwrite of `total_paid`. **The guard must be written so 450's rows are not refused.** **This is the single most important open question, because 450 is filed and this slice must not block it.**
5. **Should the bill's money be re-derived on read instead of stored?** Recommendation: **no** — the charter's **P0** row 47 names the fields as the derivation's inputs, and feature **415** writes them. **Re-deriving on read is a different design and is not claimed here.**

## Why this matters

**The bill is the only record LE31 has of what a guest paid, and its four money columns are the only money in the business that is neither append-only nor derived.**

Feature **450** put the observation in the corpus's own words: *"the ledger is append-only and audited; the money side is not. LE31's own `StockEntry` docstring says 'Never UPDATE or DELETE rows'; `Bill.total_paid` says nothing and means the opposite: a single mutable number that can be set to **anything**."* **450 then fixed the *refund* problem and explicitly left the column alone.** The mutability itself remained unowned — and a corpus-wide sweep finds exactly one mention of it, in that same sentence.

**The operational shape of the defect.** A bill is closed and paid. The guest's card statement says €47.50. LE31 says €14.30, and the tip LE31 recorded is €0.00 while the tip the same bill's `total_paid` implies is €85.70. **Nobody can tell which is right**, because the number can be replaced without a trace — and the tip, being a stored row, is simply never recomputed. **The charter's P0 acceptance criterion is satisfied throughout**: the tip *was* derived, and it *was* never manually entered. **It is still wrong.**

**Why this is a `build` and not a `defer`.** The change is one table and one guard, on LE31's own schema, and it makes the charter's central money fact — *"the tip is derived from the bill"* — actually hold. **The honest framing: this is a schema-integrity defect, not a reported incident**; no operator has complained about a wrong bill. **But the bill is where the business's money lives, and the defect is that the business's own record of money can be replaced without saying so.** The corpus has filed this family seven times in eight days — 444, 456, 470, 471, 522, 523, 524 — and each of those closed one door on this same schema. **This closes the bill's.**

## Out of scope

- **The tip formula, `formula_version` and the tip's enforcement** — **features 05, 457**, filed.
- **`Bill → order_item` and the derivation of `subtotal_items`** — **features 435, 415**, filed.
- **The bill-close route** — **feature 415**, filed.
- **The refund, the payment row and the refund cap** — **feature 450**, filed.
- **The tax rate** — **feature 408**, filed. **The `Decimal` guarantee** — **feature 411**, filed. **The meaning of `total_paid`** — **feature 420**, filed. **The currency** — **feature 409** (open owner question). **Split bills** — **feature 14**, filed. **The bill's number** — **feature 448**, filed. **`Shift` and the `Shift ↔ Bill` edge** — **feature 391**, filed.
- **Any change to `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan, menu or waiter-UI change** — `index.html` is feature **08**'s scope.
- **Alembic**, except as noted in *Dependencies** for feature 446.
- **Any change to `PROJECT_CHARTER.md`.**
