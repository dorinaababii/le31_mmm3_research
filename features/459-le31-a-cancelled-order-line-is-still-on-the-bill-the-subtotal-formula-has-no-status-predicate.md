# Feature 459 — A cancelled order line is still on the bill: the subtotal formula has no status predicate

> **Pick A of Daily Brainstorm 2026-11-08 (99th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class OrderItem`, verbatim (lines 142–155):
>
> ```python
> class OrderItem(SQLModel, table=True):
>     __tablename__ = "order_item"
>
>     id: int | None = Field(default=None, primary_key=True)
>     visit_id: int = Field(foreign_key="visit.id", index=True)
>     menu_item_id: int = Field(foreign_key="menu_item.id")
>     qty: int = 1
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)
>     course: str | None = None  # appetizer / main / dessert
>     status: ItemStatus = ItemStatus.new
>     notes: str | None = None
>     fired_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     ready_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     served_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
> ```
>
> `ItemStatus` (lines 35–40) has **five** members: `new`, `preparing`, `ready`, `served`, **`cancelled`**.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then real inserts), applying **feature 415's formula verbatim**:
>
> ```
>   visit with 2 x Espresso @ 2.50  and  1 x Tiramisu @ 6.00
>
>   415's formula over the visit                              -> 11.00
>   ... then the Tiramisu line is set to status='cancelled'
>
>   A) 415's formula, verbatim, over ALL order_items          -> 11.00
>   B) the same sum, excluding status='cancelled'              ->  5.00
>   DIVERGENCE = 6.00
>
>   the guest paid 5.00 for the espresso. 415 would charge 11.00.
>   the derived tip (total_paid=5.00, tax=0.50) would be        ->  -6.50
>   ... with the CORRECT subtotal (5.00) the tip would be      ->  -0.50
> ```
>
> **The same query has two answers and nothing in LE31 says which one the bill uses.**
>
> **⭐ THE CORPUS ALREADY KNOWS THIS IS THE MOST CONSEQUENTIAL UNDECIDED QUESTION IN THE MONEY DOMAIN — AND DELIBERATELY DID NOT DECIDE IT.** Feature **435** (`le31-bill-records-no-which-lines-it-charged`) states, verbatim, in its *Open questions* 1:
>
> > *"Which `OrderItem.status` values may be billed? This is the **most consequential** open question and it is **deliberately not decided here**. `ItemStatus` has five members (`new`, `preparing`, `ready`, `served`, `cancelled`). **A `cancelled` line must obviously not be charged.** Must a line reach `served` before it can be billed? **Default recorded: a bill may charge lines in `new`, `preparing`, `ready` or `served`, and must NOT charge `cancelled` lines.**"*
>
> **The default was RECORDED. It was never IMPLEMENTED.** Feature 435's *Scope* puts *"Which statuses a bill may charge — see the open question, which is **deliberately not decided here**"* on the **`OrderItem` side** of the boundary — i.e. **435 owns the MEMBERSHIP (a `bill_line` table) and explicitly disclaims the PREDICATE.**
>
> **⭐ AND THE FORMULA THAT WOULD CONSUME THE PREDICATE HAS NO PREDICATE IN IT.** Feature **415** (`le31-bill-closes-visit`) writes the derivation, verbatim, at line 141:
>
> > ```
> > subtotal_items  = SUM(order_item.unit_price * order_item.qty)   # for the visit's open items
> > ```
>
> **"the visit's open items"** — but **`OrderItem` has no open/closed concept.** `OrderItem` has no `closed_at`, no `voided_at`, no `deleted_at`. The only status-like field is `ItemStatus`, and its one "not charged" member is `cancelled`. **A `CHECK`, a `WHERE` clause or a derivation site cannot be attached to a phrase the schema does not express.**
>
> **⭐ THIS IS THE UPSTREAM-OF-FILED-WORK CONDITION, AND IT IS THE STRONGEST FORM OF IT SEEN IN THIS SERIES.** Feature 415 is filed as **`build`**, it *names* `routers/bills.py` as the file it creates, and its implementation steps say *"**Derive `subtotal_items` from the visit's order items** — `SUM(order_item.unit_price * order_item.qty)`"*. **415 will implement the formula exactly as written, and the formula as written charges cancelled lines.** Feature 435 lands a `bill_line` table *around* that formula and *explicitly declines to state the predicate*. **Between them they admit a bill that charges a cancelled line, and neither owns the fix.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect (a corpus-wide sweep finds **zero** hits for `cancelled.{0,60}subtotal` and zero for `subtotal.{0,60}cancelled` across **947** feature contracts and HANDOFFs); **medium** for the demand framing (no operator has reported a wrong bill — but **no bill has ever been closed by shipped code**, so there is no report to have been made).
>
> **The honest framing: the schema permits a cancelled dish to be charged, and the two filed features that touch this formula have, between them, written the rule down and then deliberately not implemented it.**

## Goal

Make the bill's subtotal **count only the lines the guest is actually paying for**, so that a cancelled dish is never charged and the tip derived from it is never wrong.

**The single sentence this feature exists to make true:** *a bill charges the lines that were not cancelled, and the predicate that says so is written down in one place and used by the derivation.*

Two concrete outcomes:

1. **One written predicate, one home.** A named constant or helper — e.g. `BILLABLE_ITEM_STATUSES = {new, preparing, ready, served}` — stating exactly which `ItemStatus` values a bill may charge, with **`cancelled` excluded**, and **`served` explicitly NOT required** (a guest does not wait for the kitchen to mark a dish served before paying).
2. **The derivation uses it.** The subtotal is computed over the billable lines and over nothing else, and the bill records **which** lines it charged (feature 435's `bill_line` membership) **or**, until 435 lands, the derivation is at least *predicate-filtered* so the number is right even if the membership is not yet recorded.

## Scope

**In scope (v1):**

- **One written rule** — the set of `ItemStatus` values a bill may charge — **in one place** (a module-level constant in `backend/app/models.py` or a small service module, following the precedent of feature 432's sign matrix and feature 404's constraint family).
- **The rule applied to the subtotal derivation**, so a `cancelled` line contributes **0.00** to `subtotal_items`.
- **A regression test** that fails on today's code and passes on the fixed code: a visit with one `cancelled` line and one live line yields the subtotal of the live line only.
- **A regression test for the tip**, proving the derived tip is not dragged negative by a cancelled line.
- **The recorded decision** on the two open sub-questions below — *must a line reach `served` before it can be billed?* and *may a `new` line be billed?* — **recorded, not guessed.**

## Out of scope (v1)

- **The `bill_line` membership table.** That is **feature 435** — filed. This slice supplies **the predicate**; 435 supplies **the membership**. **They are complementary and must not be merged.** 435's own scope puts the predicate on the `OrderItem` side of the boundary — *"Which statuses a bill may charge — see the open question, which is deliberately not decided here"* — so **this slice is filling 435's recorded gap, not overlapping 435's work.**
- **The subtotal's derivation site and the bill-closing route.** That is **feature 415** — filed. This slice supplies the **predicate the derivation must use**; it does not write `routers/bills.py`. **See *Ordering*.**
- **The tip formula.** That is **features 05 / 415 / 420 / 457**. This slice does not change `tip = total_paid − (subtotal_items + subtotal_tax)`; it makes `subtotal_items` mean what it says.
- **The tax rate.** Feature **408**.
- **The money-precision guard.** Feature **411**.
- **The `OrderItem.status` transition table and its actor.** Features **379** and **394** own the *transition*; this slice owns *which terminal statuses a bill may charge*. **A cancelled line's transition history is 379's, not this slice's.**
- **A `cancelled_at` / `cancelled_by` column.** Feature **379**'s `OrderItemTransition` table records who cancelled and when. This slice adds **no column** and **no table**.
- **The negative-quantity rule.** Feature **456** owns `OrderItem.qty`'s sign and size — a *different* rule on a *different* column. **A line with `qty = -5` is 456's problem; a line with `qty = 2` and `status = 'cancelled'` is this slice's.**
- **Restoring stock when a sale is cancelled.** That is a separate defect and it is **not filed** — see *Adjacent evidence*.
- **Any `CHECK` constraint or `STRICT` table.** Feature **404** owns that family. **A `CHECK` could not express this rule anyway** (it spans rows via a `SUM`), which is exactly why this is an application-level predicate.
- **Alembic.** §3.2's stated v1 policy is `init_db()`.

## Description

### The defect, as observed in LE31's own code on 2026-11-08

`ItemStatus.cancelled` exists. `OrderItem.status` can hold it. **Nothing consumes it.**

The three places a bill's money is decided — feature 415's formula, feature 435's membership, and the charter's own P0 row 47 — each look at the order lines and **none of them mentions `status`.**

- Feature 415's formula: `SUM(order_item.unit_price * order_item.qty)` — **no `WHERE`.**
- Feature 435's recorded default: *"a bill may charge lines in `new`, `preparing`, `ready` or `served`, and must NOT charge `cancelled` lines"* — **recorded as a default, not built as a predicate.**
- The charter's P0 row 47: *"Waiter can close a bill; tip is **derived** as `total_paid − subtotal_items − subtotal_tax`"* — **the subtotal's membership is undefined.**

**So the corpus contains the rule in prose, in the file of the feature that owns the membership — and the feature that owns the derivation does not have it.**

### Why a cancelled line is not an edge case

A cancelled line is **the normal output of a service**, not a corruption:

- The guest changes their mind about the tiramisu.
- The kitchen drops the dish because the order was a mistake.
- The waiter mis-keys the order and cancels it.
- The manager voids a comp.

In every one of those cases, **the line stays in `order_item` with `status = 'cancelled'`** — which is exactly what feature 379's transition model implies (a *transition*, recorded in a log, with the current status as a cache). **The line is not deleted; the status is the record of what happened.**

**Which is why deleting the line is not an available answer.** The corpus already decided that the ledger is append-only and the transition log is the history (features 379, 394, 421, 432). **The bill must therefore exclude by predicate, because the line itself cannot go away.**

### The quiet wrong answer

The plausible wrong answer is *"the bill sums the lines the guest ordered, and a cancelled line is not one of them."* **That is true and it is silently irrelevant**, for two reasons:

1. **The formula has no predicate to carry it.** A `SUM` over `order_item` for a visit has no way to exclude a row *unless someone writes the `WHERE`*. **The code that does not exist cannot carry the rule.**
2. **The plausible wrong answer about the tip is worse.** Feature 415 derives `tip = total_paid − (subtotal_items + subtotal_tax)`. With the cancelled line counted, a guest who paid **5.00** for an espresso is recorded as owing **11.00**, and the tip becomes **−6.50** — **a negative tip on a paid bill.** Feature 415's own guard (*feature 05's* "tip > 50% of subtotal: ask") **does not fire** on a *negative* tip: the rule tests for a tip that is too LARGE. **A negative tip passes it silently.**

### The divergence is permanent once the bill closes

Executed, in the same probe: after the bill is written with `subtotal_items = 11.00`, cancelling the line afterwards leaves the **stored** `bill.subtotal_items` at **11.00** while the visit's live lines now sum to **5.00**.

**The bill and the visit now disagree, permanently.** And there is no `bill_line` table to say which lines the bill actually charged (feature **435**, not yet landed) — so **nothing can reconstruct the truth after the fact.**

### The instance sweep, not the concept sweep

A corpus-wide sweep over **947** feature contracts and HANDOFFs:

| pattern | hits |
|---|---|
| `cancelled.{0,60}subtotal` | **0** |
| `subtotal.{0,60}cancelled` | **0** |
| `excluded from the subtotal` | **0** |
| `billable` | 2 (feature 388's table-state wording; feature 408's *"billable items"* — **neither is about an order line's status**) |
| `which.{0,30}status.{0,40}billed` | 2 (feature **435** — the recorded open question) |

**The concept is covered (feature 435 knows the question exists). The INSTANCE is uncovered: nobody implements the predicate.**

## Data model

**No schema change.** This feature adds **no column, no table, no constraint, no index.**

```python
# backend/app/models.py — the ONE place the rule lives
class ItemStatus(str, Enum):
    new        = "new"
    preparing  = "preparing"
    ready      = "ready"
    served     = "served"
    cancelled  = "cancelled"


# The rule, named, in one place.
#
# A bill may charge a line that was ordered and not cancelled.  A line does
# NOT have to reach 'served' first: a guest does not wait for the kitchen to
# mark a dish served before paying.
#
# 'cancelled' is the ONLY excluded member.  See Open questions 1 and 2.
BILLABLE_ITEM_STATUSES: frozenset[ItemStatus] = frozenset({
    ItemStatus.new,
    ItemStatus.preparing,
    ItemStatus.ready,
    ItemStatus.served,
})
```

The derivation site (which **feature 415** writes) consumes it:

```python
from sqlmodel import select

def billable_lines(session: Session, visit_id: int) -> list[OrderItem]:
    """The lines a bill may charge.  ONE definition; used by the derivation."""
    return [
        line for line in session.exec(
            select(OrderItem).where(OrderItem.visit_id == visit_id)
        ).all()
        if line.status in BILLABLE_ITEM_STATUSES
    ]


def subtotal_items_derived(session: Session, visit_id: int) -> Decimal:
    """subtotal_items = SUM(unit_price * qty) over the BILLABLE lines only."""
    return sum(
        (Decimal(str(line.unit_price)) * line.qty for line in billable_lines(session, visit_id)),
        Decimal("0.00"),
    )
```

**Notes for the implementer:**

- **The comparison must be in Python on the enum, not in SQL.** `ItemStatus` is a `str` Enum, so `line.status in BILLABLE_ITEM_STATUSES` works on the Python value. **Do not** write a SQL `WHERE status IN ('new','preparing','ready','served')` — **feature 442** records that the enum columns are `VARCHAR` with **no membership constraint**, so the SQL spelling is a duplicated string list that can drift from the enum. **One definition, in Python.**
- **The money arithmetic stays `Decimal`.** Feature **411** proved that `Decimal` is a Python-side guarantee the storage layer does not enforce, and that **Postgres rounds where SQLite does not**. The sum is computed in Python, on `Decimal`, before the write — never as a SQL `SUM` against the stored column. **This matches feature 415's own recorded obligation.**
- **The empty sum is 0.00, not `None`.** `sum(..., Decimal("0.00"))` — a `Decimal("0.00")` seed, so a visit with no billable lines yields `Decimal("0.00")` rather than an integer `0` or a `None`.
- **The status is a cache, not the history.** Feature 379 makes `OrderItem.status` a *cache* of the transition log. **This predicate reads the cache.** That is acceptable **because the cache is what the bill is computed from at close time**, and because 379 guarantees the transition write and the status update happen together. **If 379 has not landed, `status` is still the only signal available** — and this slice does not depend on 379 landing first.

## Implementation steps

1. **Add `BILLABLE_ITEM_STATUSES`** to `backend/app/models.py`, immediately after `class ItemStatus`, with the comment block above. **One definition.**
2. **Add a `billable_lines(session, visit_id)` helper** and a `subtotal_items_derived(session, visit_id)` helper. **Two functions, one home** — put them in `backend/app/models.py` if no service directory exists yet, or in `backend/app/services/` if feature 374's `stock_service.py` has by then created that directory. **Record which path was chosen.**
3. **Wire feature 415's derivation to use `subtotal_items_derived`** instead of a bare `SUM`. **If 415 has not landed, this step is deferred to 415** — but the helper exists and is tested either way, so the fix cannot be lost.
4. **Write the regression test**: a visit with one live line (2 × 2.50) and one `cancelled` line (1 × 6.00) ⇒ `subtotal_items_derived(...) == Decimal("5.00")`. **This test fails on today's code** (there is no helper, and a bare `SUM` returns `11.00`) and passes after the fix.
5. **Write the tip regression test**: with `total_paid = Decimal("5.00")` and `subtotal_tax = Decimal("0.50")`, the derived tip is `Decimal("-0.50")` — **not** `Decimal("-6.50")`. **Note that a negative tip is still possible** (the guest underpaid, or feature 420's tendered-vs-received question is unresolved); **this feature makes the tip reflect the *right* lines**, it does not make tips non-negative. **Feature 05's "tip > 50%: ask" guard and feature 420 own the tip's own rules.**
6. **Record the two open decisions** (below) in the code comment and in the feature's own *Open questions* answer.
7. **Amend feature 435's recorded default** to point at this constant, so the two files cannot drift. **One line.**
8. **Amend feature 415's formula line** to say *"over the billable lines (see feature 459)"* so the formula's comment stops claiming a filter it does not have. **One line.** **Do not otherwise change 415's implementation** — 415 owns the route.

## Telegram interaction if any

**None.** This feature has **no Telegram surface**. It changes what a bill charges, and it changes nothing about how the operator or the cook interacts with the bot.

**One consequence must be recorded for the operator, though:** when the waiter cancels a dish, **the bill no longer includes it** — which is the point. **If a cancellation is made *after* the bill is closed, this feature does not retroactively change the closed bill** (feature 450 owns refunds against a *paid* bill). **The implementer must not add a "reopen the bill" path** — see *Open questions* 3.

## Dependencies

| Feature | Relationship | Why it matters |
|---|---|---|
| **435** (`bill-line membership`) | **Sibling — and this slice fills a gap 435 explicitly left open** | 435 owns *which lines the bill charged* (the membership table). It **explicitly disclaims** *which statuses may be billed*. **Without this slice, 435's table will faithfully record a cancelled line as a charged line.** |
| **415** (`bill-closes-visit`) | **UPSTREAM — this slice must land first, or in the same PR** | 415 is about to write the derivation. Its plausible implementation is `SUM(unit_price*qty)` with **no `WHERE`** — exactly the defect this feature proves. **415 must consume `BILLABLE_ITEM_STATUSES`, not a bare sum.** |
| **379** (`order-item transition actor`) | **Prerequisite of the *cache*, not of this feature** | 379 makes `status` a cache of an append-only transition log. This slice reads the cache. **379 is not a blocker** — `status` is already the only signal available. |
| **394** (guarded transition primitive) | **Adjacent** | Owns *how* a transition is written safely. |
| **456** (`OrderItem.qty` sign/size) | **Adjacent, different column** | 456 owns the **quantity** rule; this slice owns the **status** rule. **A line with `qty = -5` is 456's; a line with `qty = 2, status = 'cancelled'` is this slice's.** **Do not merge.** |
| **452** (`status` vs timestamps) | **Adjacent** | Owns that `status` and `fired_at`/`ready_at`/`served_at` are uncoupled. |
| **432** (`StockReason` sign coherence) | **Precedent for the shape** | 432's *sign matrix* is the precedent for a **named, table-shaped rule in one place**. **This slice's `BILLABLE_ITEM_STATUSES` is the same shape, on a different column.** |
| **442** (enum columns are VARCHAR) | **Reason the predicate is in Python** | 442 records that enum columns are `VARCHAR` with **no membership constraint** — so a SQL `WHERE status IN (...)` would duplicate the enum as a string list. |
| **404** (CHECK / STRICT family) | **Why there is no CHECK here** | A `CHECK` may only reference the **same row's** columns; this rule is over a **set**. |
| **05 / 415 / 420 / 457** (tip) | **Owners of the tip** | This slice makes `subtotal_items` right. It does not change the tip formula. |
| **450** (refund a paid bill) | **Owns money-back** | A cancellation *after* close is 450's territory. |
| **446** (schema evolution) | **No dependency** | This slice adds **no column and no table**. |

## Open questions

1. **Must a line reach `served` before it can be billed?** *Recorded default: **no** — a bill may charge a line in `new`, `preparing`, `ready` or `served`.* The reason: **a restaurant bills what was ordered and not cancelled; the guest does not wait for the kitchen to mark a dish served before paying.** This default is inherited verbatim from feature **435**'s recorded default, **which this slice now implements** — so the two cannot disagree. **The owner may change it; if the owner changes it, this constant is the one place to change it.**
2. **May a `new` line be billed?** *Recorded default: **yes**.* A line the waiter has just added and the guest has not yet changed is billable. **This is the same default as 435's**, for the same reason.
3. **What happens when a line is cancelled *after* the bill is closed?** *Recorded default: **the closed bill does not change.*** Feature **450** owns refunds against a paid bill; a cancellation of an unbilled line before close is exactly what this slice fixes. **The implementer must NOT add a "reopen and recompute the bill" path** — that is a money-movement decision (a refund, a part-payment, a split) and it belongs to features **14** (split bills), **450** (refund) and **457** (the tip formula's enforcement). **Recorded so a later pass does not read the omission as an oversight.**
4. **Should `BILLABLE_ITEM_STATUSES` live in `models.py` or in a service module?** *Recorded default: **`models.py`**, immediately after `ItemStatus`, because the rule is a property of the enum and it must be importable by feature 415's route without creating a new import cycle.* **If feature 374's `backend/app/services/` directory exists by then, moving it there is acceptable — but it must move as ONE definition, not a copy.**
5. **Should the rule also exclude a line whose `menu_item` has been deleted?** *Out of scope.* Feature **427** owns the FK-enforcement story on SQLite. **A dangling `menu_item_id` is 427's defect, not this one's.**

## Why this matters

**Because LE31's two most important money features have, between them, written down the rule that a cancelled dish must not be charged — and then not implemented it, while the feature that will write the derivation has no predicate in its formula to implement.**

The charter's P0 row 47 says the tip is *derived* and *never manually entered*. **A derived number is only as good as the set it is derived over**, and LE31's set is undefined: the corpus contains the answer in a *comment* in feature 435's open-questions list, and the formula in feature 415 that consumes it has no `WHERE`.

**What this costs when it is wrong:**

- **A cancelled dish is charged.** The guest sees a line they cancelled on the bill.
- **The tip is wrong, and wrong in the direction nobody checks.** With `total_paid` below `subtotal_items`, the tip goes **negative** — and feature 05's guard tests for a tip that is **too large**, so it **does not fire**. **The guard is on the wrong side of zero.**
- **The wrongness is permanent.** After the bill closes, `bill.subtotal_items` is stored, and (until feature 435 lands) **no membership record exists** to say which lines were charged. **The bill cannot be audited against the visit**, and the visit's lines may change afterwards. Feature **435** states this exact failure in its own words: *"The only way to reconstruct is to re-sum the visit's order items **at dispute time**, which is **not the same set** as the lines that were billed (a line can have been cancelled after the bill…)."*

**Why it is cheap today and expensive later:**

- **Cheap today**: one constant, two helpers, two tests. **No schema change, no column, no table, no migration, no backfill.**
- **Expensive later**: **no bill has ever been closed by shipped code** — there is no `bills.py` router, so the defect is currently inert. **The moment feature 415 lands, every bill in every deployment charges cancelled lines.** And because the wrong subtotal is **stored**, the first restaurant to use it will have **bills that cannot be reconstructed** — the wrong number is not a bug report, it is a fact in the database.

**Why it must land before feature 415:**

**Because 415 is about to write the derivation, and it will write it faithfully — including the omission.** The gap is not that 415 is wrong; 415 is right about everything it says. **The gap is that the rule 415 needs is recorded in a *different* feature's open-questions list and never implemented.** That is the upstream-of-filed-work condition in its sharpest form: **the pipeline will faithfully ship the defect, because the defect is written down as a *default* and the default was never turned into code.**

## Adjacent evidence

**Third-party, in-window, permissive licences, no code adopted.** All fields parent-verified via a direct `GET /repos/{owner}/{repo}` on 2026-11-08 (stars/forks/licence/`created_at`/`pushed_at` read from the API, **never** from search-result numbers) and **README read in full**.

- **`AlgoVyn/bikri`** (MIT ✓ §3.2, **★1 / ⑂0 = NO traction evidence in either direction**, TypeScript, 14,238 KB, created **2026-10-26** AND pushed **2026-11-08** = **in-window by BOTH fields**) — README, verbatim: *"**Stock and suppliers** — deliveries, supplier returns and **ledger**, stock adjustments, weighted-average cost…"*. **The transferable item is the vocabulary of a *correcting* ledger entry** — a cancellation in a POS is an adjustment, not an edit. **This repo is the trigger for the *adjacent* defect recorded below** (a cancelled sale leaves its `-1` row in the append-only ledger); it is **not** the trigger for this feature's predicate. **Already cited by features 455, 454 and 447** — recorded so a later pass does not re-derive it as a fresh trigger.
- **`baba-dev/menuminute`** (MIT ✓ §3.2, **★1 / ⑂0**, TypeScript, 92,690 KB, created **2026-10-13** AND pushed **2026-11-08** = **in-window by both fields**) — README, verbatim: *"**Cancelling**, refunds and big discounts stay owner-only"* (from `manoranjan2050/RestoPro-ERP-Web`, MIT ✓, **★1 / ⑂0**, created 2026-11-04, pushed 2026-11-05) and *"(from the Famalth suite)"* — **"**Immutable order snapshots**"* (menuminute, README line 89: *"Dine-in, table and pickup orders with a mobile cart and staff acceptance. **Immutable order snapshots.**"*). **The transferable primitive is "the snapshot is immutable; a cancellation is a separate act"** — which is LE31's own append-only discipline applied to the *bill* side rather than the ledger side. **Already cited by feature 443.**

**Repo self-reported metrics are labelled unverified.** Neither README states a test count or a coverage figure that this contract relies on; nothing here needs an unverified number.

**The adjacent defect this feature must NOT swallow.** The corpus has **one** other place where a cancellation meets the money, and it is **not filed**: a `cancelled` order line leaves its `StockEntry(qty_delta=-1, reason='sale')` row in the append-only ledger, and **the stock is never restored** — feature **400** names the missing `StockReason` reversal member verbatim (*"void restores stock … `StockReason` has **no reversal member**"*) but **does not own the fix**. **A corpus-wide sweep for `reversal`/`reversed`/`cancelled_sale`/`restore the stock` across `features/` and `specs/` returns only third-party vocabulary references (features 303, 390) and feature 400's observation — no LE31 feature owns the rule.** **That is a separate, separately-filed defect and it must not be merged with this one: this slice owns *the bill*; the other owns *the stock ledger*.** It is recorded here so that a later pass does not read this slice's silence about stock as an oversight.

## Verification protocol

The pre-flight for this feature is **four commands**, all re-runnable, all offline:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The predicate exists and has exactly one definition.
grep -rn "BILLABLE_ITEM_STATUSES" backend/ features/ specs/ | wc -l   # >= 3 (def + import + test)

# 2. The rule EXCLUDES 'cancelled'.  (must print exactly one match)
grep -rn "BILLABLE_ITEM_STATUSES" backend/ -A 12 | grep -c "ItemStatus.cancelled"

# 3. There is no bare SUM left in the derivation.
grep -rn "SUM(order_item.unit_price" backend/   # must print nothing

# 4. The corpus agrees: the predicate is now implemented, not just recorded.
grep -rn "cancelled.{0,60}subtotal" features/   # must now hit 459
```

Plus the **executed** regression test, which must **fail on today's code** and pass after the fix — see *Implementation steps* 4 and 5.

**The negative control**: reinject the defect by changing `BILLABLE_ITEM_STATUSES` back to `frozenset(ItemStatus)` (i.e. re-admit `cancelled`), and confirm the regression test **fails**. A test that only ever passed proves nothing.

## Rollback path

**Fully reversible in one step.** Revert the constant and the two helpers; the behaviour returns to today's. **No data is at risk** — no bill has ever been closed by shipped code, so no `bill.subtotal_items` was ever computed with the defect. **No column, no table, no migration, no backfill.**
