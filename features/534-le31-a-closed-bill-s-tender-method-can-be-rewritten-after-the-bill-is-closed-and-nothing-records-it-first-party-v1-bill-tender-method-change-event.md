# Feature 534 — A closed bill's tender method can be rewritten after the bill is closed, and nothing records it

> **Pick A of Daily Research 2026-11-27.** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
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
> **Nine columns record what a guest paid. Four of them are money. One of the remaining five says *how* the guest paid — and it is the one column on this row that no feature in the corpus protects.**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with a 4-seat table, one staff member, one visit, one order line and one bill with `payment_method=cash`, `total_paid=5.00`):
>
> ```
>   UPDATE bill SET payment_method = 'card'  ->  ACCEPTED
>   bill now: payment_method=card
> ```
>
> **A cash bill became a card bill, silently.** No error, no event, and **no consequence for any report that counts cash against card** — the owner's cash reconciliation reads `payment_method` to decide which side of the till a payment lands on.
>
> **⭐ AND THE CORPUS OWNS FOUR NEIGHBOURS AND EXPLICITLY DISCLAIMS THIS ONE.** A corpus-wide sweep over all **567** feature contracts and **520** HANDOFFs returns **zero hits** for a rule about the bill's tender method being written once or traced:
>
> | sweep | files |
> |---|---|
> | `payment_method.{0,120}(rewrit\|change event\|mutab\|flip\|immutab\|history)` | **0** |
> | `tender.{0,60}(method\|kind).{0,60}(rewrit\|chang\|mutab)` | **0** |
> | `payment.{0,30}method.{0,60}(chang\|rewrit\|overwrit)` | 1 (feature **449** — a *different* project's README quote about Indonesian payment methods) |
>
> **⭐ AND THE NEIGHBOURS SAY, IN THEIR OWN WORDS, THAT THIS COLUMN IS NOT THEIRS.**
>
> - **Feature 532** (the bill-money change event, filed 2026-11-26) writes, verbatim: *"**`bill` is otherwise untouched** — `visit_id`, **`payment_method`**, `paid_at`, `closed_by` and the unique constraint on `visit_id` are all unchanged."* **532 owns the four money columns and explicitly disclaims this one.**
> - **Feature 420** (tendered vs received) writes, verbatim, in its *Out of scope*: *"**Any change to `Bill.payment_method`** or to the `PaymentMethod` enum. Feature **442** owns the enum-membership constraint; feature **391** owns the payment row."*
> - **Feature 442** (enum membership) owns *"one `CHECK` constraint per enum column"* — *"the column may not hold a value outside the enum"*. **It says nothing about a value inside the enum changing after the write.**
> - **Feature 415** (the close route) owns the *write that creates* the bill. Its route *"accepts only `total_paid`, `payment_method` and `subtotal_tax`"* — **it refuses the caller at the door, and then stops.** Nothing downstream guards the stored column.
>
> **⭐ AND THE REPLACEMENT TECHNOLOGY IS ALREADY FILED — WHICH IS WHY THIS IS NOT A NEW IDEA.** Feature **391** owns the `Payment` table (feature 05's shape: `Payment (id, bill_id, amount, method, card_last4, by_user_id, at)` plus `shift_id`). **Once 391 lands, the tender method is a *row*, and a row that can be appended to cannot be edited.** This slice therefore has **two shapes**, and the implementer must implement **both**: the guard for today (a single mutable enum column) **and** the same rule expressed over 391's `Payment` rows when they exist. **The narrow form is not "wait for 391"** — because **until 391 lands, the column that decides cash-versus-card is a mutable string with no history**, and that is exactly the state the product is in today.
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a wrong tender method; the corpus confirms nobody owns the rule).

## Goal

Make a closed bill's tender method mean **one thing**: **the bill records how it was paid once, and afterwards that fact has a history.**

The concrete outcome: **a closed bill's `payment_method` cannot be rewritten silently**, and where the domain genuinely requires a correction, that correction is **a recorded event** carrying the old value, the new value, the actor and the time.

## Scope

**In scope (v1):**

1. **The write-path guard.** Once a bill is closed (`paid_at IS NOT NULL` — the bill is created already paid, so this is the *only* state a bill has today), the `payment_method` column is **written once**. A later write is refused unless it carries an event.
2. **A recorded tender-method change.** A change after the close is an **event**: the bill, the field that changed, the old value, the new value, the actor (`by_user_id`) and the time. The mechanism is a new append-only table, mirroring feature **532**'s bill-money change event and feature **533**'s visit-composition change event.
3. **The relation to feature 532, stated explicitly.** Feature 532 owns the **four money columns** (`subtotal_items`, `subtotal_tax`, `total_due`, `total_paid`) and **explicitly disclaims** `payment_method`. This slice owns **the tender method and the payment instant** — the two columns 532 names as *"otherwise untouched"*. **The two are compatible and must not be confused:** 532 says *how much* may not change; this slice says *how it was paid* may not change. **They share the same event-table shape and should land in one PR or in either order.**
4. **The relation to feature 442, stated explicitly.** Feature 442 constrains the column's **membership** — it may not hold a value outside `('cash','card')`. This slice constrains the column's **history** — it may not change at all after the close. **A membership constraint does not imply a write-once rule**: `cash → card` is a perfectly legal member-to-member transition, and 442's `CHECK` fires on neither end of it.
5. **The relation to feature 391, stated explicitly.** Feature 391 adds a `Payment` table whose rows carry `method`. **When 391 lands, the tender method is a row and the shape of the problem changes.** This slice's contract states the ordering: **391's payment rows are the mechanism for a legitimate post-close money movement; this slice's guard is the mechanism that says a post-close change of the tender method is an event, not a silent overwrite.** **This slice must not block 391**, and it must not be widened to redesign 391's table.
6. **The relation to feature 415, stated explicitly.** Feature 415 owns the **close route** — the write that creates the bill. This slice adds the guard that runs at the write site **and** the event table the guard consults. **If 415 has not landed, this slice's guard has no route to sit in** — recorded in *Dependencies*.
7. **A regression test** for each row of the scenario table below.

**Out of scope (v1):**

- **The four money columns.** That is **feature 532** — filed. This slice changes none of them and must not read them.
- **The `Payment` table and the `Shift`↔`Payment` money edge.** That is **feature 391** — filed.
- **What `total_paid` means (tendered vs received).** That is **feature 420** — filed. This slice does not touch the meaning of any money column.
- **The enum's membership and any `CHECK` constraint on it.** That is **feature 442** — filed.
- **The tip and the tip's formula.** That is **feature 457** (the formula) and feature **05** (the rule). This slice changes no formula and no `formula_version`.
- **The `Bill → order_item` edge and the derivation of `subtotal_items`.** That is **feature 435** — filed.
- **A refund.** That is **feature 450** — filed. **A refund is not a change of tender method**, and this slice must not be widened to cover one. (Feature 391's payment rows are where a refund's method lives.)
- **Split bills and split tender.** That is **feature 14** — filed. One bill, one tender method, is what today's schema can express.
- **The bill's human-facing identity / number.** That is **feature 448** — filed.
- **The currency of the money columns.** Feature **409** records it as an open owner question. This slice does not add a currency column.
- **Any change to `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan, menu or waiter-UI change.** The mock-up is `index.html`; feature **08**'s scope.
- **Alembic, or a migration framework.** §3.2's stated v1 policy is `init_db()`. **No `alembic.ini`, no `migrations/` directory, no `alembic` dependency.**
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the defect

A bill is the restaurant's record of a transaction. Nine columns. Four of them are money — and the corpus has filed **three separate features** to make the money columns stable (feature 532's write-once guard and event table, feature 457's tip formula enforcement, feature 411's `Decimal` precision guard). One column records **how** the money arrived. One records **when**. One records **who** closed it. One is the unique edge to the visit.

**`payment_method` is the column that decides which side of the till the money lands on, and it is the only one of the nine that no feature protects after the close.**

The corpus's own vocabulary for this already exists — feature 391's `Payment` row carries `method`, and the owner's cash reconciliation is defined over payments, not over a bill's mutable enum.

### What the corpus says, in its own words

This is the important part of the finding, because it is what makes the slice a *boundary* rather than an invention:

> **Feature 532**, *Out of scope / Data model*: *"**`bill` is otherwise untouched** — `visit_id`, **`payment_method`**, `paid_at`, `closed_by` and the unique constraint on `visit_id` are all unchanged."*

> **Feature 420**, *Out of scope*: *"**Any change to `Bill.payment_method`** or to the `PaymentMethod` enum. Feature **442** owns the enum-membership constraint; feature **391** owns the payment row."*

> **Feature 442**, *Scope*: *"One `CHECK` constraint per enum column, stating the membership: `bill.payment_method IN ('cash','card')` … The constraints are generated from the Python enum."*

**Read those three together and the gap is exact:** 442 says the column may not hold a value *outside* the enum; 420 says changing the column is nobody's business; 532 says the column is *not* one of the four it guards. **Nothing anywhere says the column may not change from `cash` to `card` after the bill is closed and paid.**

### ⭐ Why the plausible wrong answer is not the answer

Two wrong answers are available and both look right:

**Wrong answer 1 — *"the enum protects it."*** `PaymentMethod` is a `str, Enum` with two members, and `payment_method: PaymentMethod` is typed. **That is a Python type hint, not a runtime constraint.** SQLModel stores it as `VARCHAR` and the database accepts `'bitcoin'` — **feature 442 proved that by execution** and filed the fix. And even with 442 landed, `cash → card` is a member-to-member change that no `CHECK` can refuse: the constraint fires on the *value*, not on the *change*.

**Wrong answer 2 — *"415 refuses the caller, so the column is safe."*** Feature 415's route *"accepts only `total_paid`, `payment_method` and `subtotal_tax`"* and *"must not accept a caller-supplied `subtotal_items`, `total_due`, or a tip amount"*. **That is correct and it is filed — and it protects the create-write only.** It says nothing about the second write. **415 builds the door; nothing here builds the wall.** The stored column is exactly as mutable as it was before 415 landed.

### The two-numbers check

The defect is only meaningful if two numbers that should agree can diverge. **They can, and they do:**

| what | before | after |
|---|---|---|
| `bill.payment_method` | `cash` | `card` |
| the owner's cash reconciliation reads `payment_method` | counts this as **cash** | counts this as **card** |

**The bill still adds up to itself** — `total_paid` and `total_due` are untouched, the tip's formula still holds, the bill is internally consistent. **The inconsistency is between the bill and the day's cash reconciliation**, and nothing records that it happened. That is the same shape as feature 532's finding, on the one column 532 disclaimed.

### The cost of getting it wrong

- The owner counts the till at close and reconciles against a day's cash. A bill that was paid by card and now says cash **inflates** the counted cash; the reverse **deflates** it. Either way the variance is unexplained, and feature **391** (filed) is the feature that derives that variance.
- The owner's daily recap reports cash versus card. A rewritten method **silently changes yesterday's report**.
- Nothing anywhere will ever say *"this bill was cash and is now card"*, because **there is no record to say it with**.

## Data model

**No column is added to `bill`.** The bill keeps its nine columns; the history lives in the event table.

```python
# backend/app/models.py — NEW, appended after DerivedTip

class BillTenderMethodChange(SQLModel, table=True):
    """Append-only history of a closed bill's tender method changing.

    A bill records how it was paid ONCE. If that fact ever changes, the
    change is a fact of its own, not a silent overwrite.
    """
    __tablename__ = "bill_tender_method_change"

    id: int | None = Field(default=None, primary_key=True)
    bill_id: int = Field(foreign_key="bill.id", index=True)
    field: str = "payment_method"        # names the column that changed
    old_value: str
    new_value: str
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

| column | type | meaning |
|---|---|---|
| `id` | int PK | |
| `bill_id` | int FK → `bill.id`, indexed | the bill whose tender method changed |
| `field` | str | names the column that changed — `"payment_method"` today, `"paid_at"` if this slice is widened |
| `old_value` | str | the value before |
| `new_value` | str | the value after |
| `by_user_id` | int? FK → `app_user.id` | the actor — nullable, matching the corpus's actor convention |
| `at` | datetime (UTC) | when |

**The `field` column is what makes this table reusable and what makes it honest.** A bill's tender method and its payment instant are *the same kind of fact* — both are *"when and how this bill was settled"* — and both are disclaimed by 532. **Implementing one event table for both is cheaper than two, and the table's shape states the rule once.** The implementer must decide, and record the decision, whether `paid_at` is in scope. **Recorded default: `payment_method` only.** The `field` column exists so the *next* slice does not need a second table, and it does **not** widen this slice.

**Why a table and not a `previous_payment_method` column:** a `previous_*` column preserves one change and loses the second. Feature **523** states this rule for the menu price and it is the same rule here.

**Append-only.** Never updated, never deleted. It is a fact table.

## Implementation steps

1. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:

   | scenario | expected |
   |---|---|
   | the **close write** creates the bill with its `payment_method` | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `payment_method` on a closed bill, **no** event | **REFUSED**, stored value unchanged |
   | change `payment_method` on a closed bill **with** an event in the same transaction | **ACCEPTED**, event carries old value, new value, actor, time |
   | update or delete an event row | **REFUSED** |
   | the event history's last `new_value` and `bill.payment_method` | **must agree** — the two-numbers check |
   | change `payment_method` to a value outside the enum | **REFUSED** — feature **442**'s rule, unaffected and not re-implemented here |

2. **Add the event model** to `backend/app/models.py`, following the `StockEntry` / role-change-event / bill-money-event shape (an append-only fact with `by_user_id` and `at`). **No column is added to `bill`.**

3. **Add the guard** as a service helper, `backend/app/services/bills_service.py` (NEW): a single function that either refuses the change, or writes the event and the change in one transaction. **It does not rewrite the close route's semantics** — feature **415** owns that.

4. **Route the close write through the helper** if and only if the close route exists (feature 415). **If 415 has not landed, the helper stands alone and the route, when it lands, must call it.** **Record which of the two is true in the PR description.**

5. **Read feature 442 and 391 before writing the helper.** 442's `CHECK` must not be duplicated. 391's `Payment` table must not be redesigned. If 391 has landed, the helper's guard applies to the **`payment_method` column only** and the `Payment` rows are the mechanism for a legitimate second tender — **not** this slice's business.

6. **Add the two-numbers regression test** — after any accepted change, `bill.payment_method` and the event history's latest `new_value` must agree.

7. **Do not add a `CHECK` constraint** on `payment_method`. It already exists or will exist under feature 442, and it cannot express a history rule in any case.

## Telegram interaction if any

**None.** No bot command, no FSM state, no chat surface. This slice is a backend write-path guard on a column the waiter UI sets through the close route (feature 415).

## Dependencies

- **Feature 415 (`le31-bill-closes-visit`) — the route this slice's guard belongs to.** 415 owns the close write and **owns the route that does not exist yet.** This slice's guard must sit in that write path. **If 415 has not landed, this slice's rule has nowhere to live and must wait or must introduce the write path itself, which would duplicate 415.** Recorded explicitly, because *"the write path does not exist"* is the single most likely way for this slice to go wrong.
- **Feature 532 (`le31-bill-money-change-event`) — the sibling slice, and the reason this slice exists.** 532 owns the four money columns and **explicitly disclaims** `payment_method`. **The two are compatible and must not be confused.** 532's guard refuses a change to *how much*; this slice's guard refuses a change to *how it was paid*. **They share the event-table shape and should land together or in either order.** If 532 lands first, this slice's helper should be **written in the same service module** and the two guards should be **one transaction**.
- **Feature 442 (`le31-enum-columns-are-varchar-with-no-membership-constraint`) — read first.** 442 owns the membership `CHECK`. **This slice must not duplicate it.** Note that 442's constraint fires on the *value*, not on the *change*: `cash → card` is legal under 442 and is exactly what this slice refuses.
- **Feature 391 (`le31-shift-variance-stored-no-derivation-no-payment-table-shift-money-edge`) — the replacement technology.** 391 adds the `Payment` table. **When it lands, the tender method becomes a row and this slice's shape changes.** This slice must not block 391 and must not redesign it.
- **Feature 420 (`le31-total-paid-means-tendered-not-received`) — read first.** 420 owns the *meaning* of `total_paid`. This slice changes no money column and does not touch that meaning.
- **Feature 457 (`le31-derived-tip-formula-enforcement`) — unaffected.** 457 owns the tip's formula and its `formula_version`. This slice changes neither.
- **Feature 435 (`le31-bill-line-membership`) — unaffected.** 435 owns the `Bill → order_item` edge.
- **Feature 450 (`le31-a-refund-has-no-payment-to-be-capped-against`) — read first.** 450 owns refunds. **A refund is not a change of tender method**, and this slice must not be widened to cover one.
- **Feature 404 (`le31-money-precision`) — unaffected.**
- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — NOT a hard blocker for this slice.** This slice adds **one new table** and **no column to any existing table**. **It is recorded here so the implementer does not assume it is exempt for the wrong reason:** if the implementer *does* add a column (for example, a `tender_changed_at` marker on `bill`), **446 then blocks it.**
- **Alembic.** §3.2's stated v1 policy is `init_db()`. **Do not add `alembic`, an `alembic.ini`, a `migrations/` directory, a version table, or an `alembic` dependency.**

## Open questions

1. **What happens when the closed bill's tender method must legitimately change?** *Recorded default: **the change is an event, not a refusal.** The guard refuses a change that arrives **without** an event; a change that arrives **with** an event is **ACCEPTED.** Refusing every change would break the correction path and teach the operator that the field is frozen.*
2. **Should the event be allowed for a bill that has not been closed?** *Recorded default: **the guard only applies to a closed bill.** Today a bill is created already paid, so there is no open-bill state; if 415 later introduces one, the guard's condition must be re-read, not assumed.*
3. **Should `paid_at` be in the same slice?** *Recorded default: **no.** `paid_at` is the payment *instant* and `payment_method` is the payment *kind*; both are disclaimed by 532, but they are different facts and the implementer must not widen the slice to cover both. **The `field` column exists so the next slice does not need a second table.** Recorded, not decided.*
4. **When feature 391 lands, what happens to this guard?** *Recorded default: **the guard's condition moves to the `Payment` rows** — a bill's tender method is then a fact about a set of rows rather than a column — **and this slice's `bill`-column guard becomes a compatibility shim that refuses only the legacy single-column path.** **This is recorded as a follow-up obligation, not as work in this slice.**
5. **Who is the actor when the method is corrected by the owner at close?** *Recorded default: **`by_user_id` is nullable**, matching the corpus's actor convention (feature 417's). A correction made by the owner, outside a staff session, has no actor id, and the event must still be recordable.*

## Why this matters

**A bill is a legal record of what a guest paid.** The corpus says this in its own words — feature **435**'s contract: *"A bill is a legal record of what a guest paid."* And this slice's column is the one that says **how**.

**The gap is not that the column exists. The gap is that every other fact on the bill got a feature and this one did not.** The corpus filed: the money columns (532), the tip's formula (457), the money's precision (411), the lines a bill charged (435), the bill's identity (448), the tax's rate (408), what `total_paid` means (420), the bill's close edge (415), the enum's membership (442). **Nine features around this one row, and the tender method is the one column none of them reaches.**

**And the reason is visible in the corpus's own boundaries.** Feature 532 wrote the sentence *"**`bill` is otherwise untouched** — `visit_id`, **`payment_method`**, `paid_at`, `closed_by` … are all unchanged"* — **it was writing an accurate boundary statement, and the boundary it drew left this column unguarded.** Feature 420 wrote *"**Any change to `Bill.payment_method`**"* into its *Out of scope* list — **accurate, and it named the gap without closing it.** **Both slices were right. The gap is what is left between them.**

**This is the seventh shape the corpus has now found twice: a fact that is *owned* by nobody, sitting in a table where every neighbouring fact has an owner.** The fix is not new machinery — it is the corpus's own append-only-event shape, applied to the one column that was explicitly disclaimed.

**For the owner, the difference is the cash reconciliation.** Feature 391 derives the shift's variance from the payments. A bill whose tender method was rewritten silently changes what that derivation sees, and the day's cash will not balance — **and the owner will have no way to find out which bill caused it.**

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`Mindenry/tabletop`** — licence **`null`** (no SPDX id) → §3.2 strictly-incompatible → **vocabulary-only, the code-shape is NOT adopted**; ★0/⑂0, TypeScript, created **2026-11-26** and pushed **2026-11-26** = **in-window by both fields**, 7.8 MB; README at `gh/readme/Mindenry__tabletap.md`. Verbatim, **line 219**: *"**Prices come from the server. Client payloads carry item ids and quantities, never amounts.**"* — the same server-authoritative discipline, applied to money rather than to the tender method. Also verbatim, **line 89**: *"**Refunds do not move money. Recording one updates the ledger and the audit log.**"* — **the audit-log half is this slice's shape**: a post-close movement is *recorded*, not applied in place. The transfer is the **discipline**, not the code: this repository is TypeScript/SQLite and LE31's stack is Python 3.13/FastAPI/SQLModel/Postgres.
- **`ahmedshawky7/shifra-restaurant-platform`** — licence **`null`** → §3.2 strictly-incompatible → **vocabulary-only**; ★0/⑂0, Java/Spring Boot, created **2026-11-23** and pushed **2026-11-24** = **in-window by both fields**, 3.5 MB; README at `gh/readme/ahmedshawky7__shifra-restaurant-platform.md`. Verbatim, **line 29**: *"**Immutable Financial Audit Ledger: Append-only `audit_logs` table (`@Immutable` + `@PreUpdate`/`@PreRemove` guards) tracking bill closures, discounts, order cancellations, and menu price updates.**"* — **two properties of this slice appear in one sentence**: the *audit log* (this slice's event table) and the *`@PreUpdate`/`@PreRemove` guards* (this slice's refusal at the write path). **Recorded because it is a peer implementation of the mechanism — and because it is Java/Spring, off-stack, and unlicensed, so no code is adopted.**
- **`Simon-Keya/mekuin`** — licence **`null`** → §3.2 strictly-incompatible → **vocabulary-only**; ★0/⑂0, Go, created **2026-11-25** and pushed **2026-11-26** = **in-window by both fields**, 8.8 MB; README at `gh/readme/Simon-Keya__mekuin.md`. Verbatim, **line 90**: *"v52: authenticated provider reconciliation; **`provider_confirmed` is not settled**."* — **the distinction this slice protects**: a *provider's confirmation* is not the same fact as *settlement*. Verbatim, **line 130**: *"…branch-scoped operational alert inboxes for inventory thresholds, pending expense/supplier-invoice approvals and **cash variances**, plus acknowledgement/resolution history and an **immutable business audit ledger**."* — **the same two shapes**: an immutable ledger and an acknowledgement/resolution history, and the cash variance that 391 derives. **No code is adopted.**
- **`nishantmlad/Restaurant-POS`** — licence **AGPL-3.0** → §3.2 **strictly-incompatible** → **reference-only**; ★1/⑂0, TypeScript, created **2026-11-25** and pushed **2026-11-26** = **in-window by both fields**; README at `gh/readme/nishantmlad__Restaurant-POS.md`. Verbatim, **line 72**: *"**Server-authoritative money** — all pricing, tax, discount, and …"* — the same server-authoritative money discipline. **AGPL-3.0 is why no code is adopted.**

**Adjacent first-party work — recorded, NOT picked:**

- **The bill's four money columns being rewritten after the close** — **feature 532**, filed 2026-11-26. **Same table, adjacent columns, and the sibling of this slice.** 532 explicitly disclaims `payment_method`; this slice fills exactly that gap.
- **The order line's quantity being rewritten after the line exists** — **feature 531**, filed 2026-11-26. **Same family, different table.**
- **A seated visit's party size being rewritten after the party is seated** — **feature 533**, filed 2026-11-26. **Same family, different table.** **This slice is the fourth member of a family the corpus has now filed three times.**
- **The tip's formula and its `formula_version`** — **feature 457**, filed. **Read, not changed.**
- **The bill's `paid_at`** — recorded as *Open questions* 3 above. **Not in this slice.**
