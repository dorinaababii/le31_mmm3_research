# Feature 531 — An order line's quantity can be rewritten after the line exists, and nothing records it

> **Pick A of Daily Brainstorm 2026-11-26 (108th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class OrderItem`, verbatim (lines 142–156):
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
> **`qty` is a bare `int` with a default of `1`, no constraint, and no history.** Feature **456** owns *what a quantity may be* (the sign and the size). This feature owns *when a quantity may change*.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one menu item, one batch, one visit and one order line):
>
> ```
>   UPDATE order_item SET qty=99 WHERE id=1      ->  ACCEPTED   (the line was already status=served)
>   UPDATE order_item SET qty=1  WHERE id=1      ->  ACCEPTED   (the bill was already closed and paid)
>
>   SUM(order_item.qty * order_item.unit_price)  =  6.50
>   bill.total_due                               = 14.30
>   bill.subtotal_items                          = 13.00
>   SUM(stock_entry.qty_delta) for batch 1        = -2      <- the ledger says two sold; the order says one
> ```
>
> **⭐ TWO NUMBERS THAT SHOULD AGREE, DISAGREEING — after the bill is closed and paid.** The order says the visit is worth €6.50. The closed, paid bill says €14.30. **Nothing raised an error, and nothing was written to the append-only ledger.**
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **564** feature contracts and **517** HANDOFFs returns **zero hits** for a rule about *when* a line's quantity may change:
>
> | sweep | files | hits |
> |---|---|---|
> | `order_item.{0,50}qty.{0,60}(after\|once\|post\|already).{0,50}(exist\|order\|serv\|fired\|bill)` | 0 | 0 |
> | `order.{0,20}line.{0,40}(quantity\|qty).{0,40}(immutable\|fixed\|frozen\|locked)` | 0 | 0 |
> | `order_item.{0,40}qty.{0,30}(update\|change\|mutab)` | 0 | 0 |
> | `qty.{0,40}(after\|once).{0,40}(line\|exists\|order)` | 0 | 0 |
> | `line.{0,20}qty.{0,30}(mutable\|change\|rewrite)` | 0 | 0 |
>
> **⭐ AND THE CORPUS RECORDED IT TWICE AND FILED IT NEVER.** Feature **470** wrote, verbatim: *"`UPDATE order_item.qty -> 99` was ACCEPTED. Feature **456** owns the sign and size rule; feature **444** owns the unit price; **neither owns the quantity changing after the line exists.** Recorded, not filed."* Feature **471** wrote the same sentence the same day. Two passes, two days, two records — and no contract. **That is the sixth instrument's shape: a feature that found a defect, did not own it, and said so.** This contract is the slice the corpus asked for.
>
> **⭐ AND THE NEIGHBOURS DISCLOSE IT EXPLICITLY.** Feature **456**'s own *Out of scope* says: *"`OrderItem.unit_price` and its mutability — that is **feature 449**. Same table, adjacent column"* — **the price, not the quantity**. Feature **444** owns *the history of the line's price* and says the line's `status` transitions are **379**'s. Feature **452** owns *status versus timestamps* and says the transition log is **379**'s. Feature **430** owns *insertion time* and says the bill's derivation is **05 / 415**'s. **Four features own four neighbouring columns and rules on the same table — and the column that decides *how much food* is unconstrained and untraced.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a wrong quantity; the corpus confirms nobody owns the rule).

## Goal

Make an order line's quantity mean **one thing at every point in the line's life**: **a quantity may be set while the line is still the waiter's to change, and after that it is a fact with a history.**

The concrete outcome: **the quantity of a line that has left the waiter's hands cannot be rewritten silently**, and if a quantity does change after the line has been fired, the change is a **recorded event** that names the old quantity, the new quantity, who made it and when.

## Scope

**In scope (v1):**

1. **The timing rule on `OrderItem.qty`.** A line's quantity may be changed only while the line is in a state where the quantity is still the waiter's to set. The states are LE31's own `ItemStatus` enum: `new`, `preparing`, `ready`, `served`, `cancelled`.
2. **A recorded quantity change.** A quantity change after the line has been fired is an **event**: the old quantity, the new quantity, the actor and the time. The mechanism is a new append-only table, mirroring the ledger's discipline.
3. **The write-path guard.** The check lives at the write site, **not only** as a database constraint, because `PRAGMA foreign_keys` is off by default in SQLite (feature **427** owns the pragma; feature **522** records that `ON DELETE` clauses do not fire in dev until 427 lands — the same reasoning applies here).
4. **The relation to the bill.** A line whose quantity changed after the bill was closed must not be able to make the closed bill's stored subtotal wrong **silently**. The contract states the ordering rule: **this slice does not recompute a closed bill** (feature **415** owns the bill-close write and the derivation), but it **does** guarantee that the quantity-change event exists so that the bill's history is reconstructible.

**Out of scope (v1):**

- **The sign and size of a quantity.** That is **feature 456** — filed, `build`. 456 owns *what* a quantity may be (zero and negative are refused); this feature owns *when* it may change. **They are two different rules with two different mechanisms.**
- **The unit price's mutability and history.** That is **feature 444** — filed. 444 owns the *trace* of a price change; this feature owns the *trace* of a quantity change. **Same table, adjacent column, separate slices.**
- **`OrderItem.status` transitions and their timestamps.** That is **feature 452** and feature **379** — filed. This feature does not add a status, change a status, or own the transition log.
- **The order-line's insertion order.** That is **feature 430** — filed.
- **The derivation of `Bill.subtotal_items` and the `Bill → order_item` edge.** That is **feature 435** (the edge) and **feature 415** (the close write and the derivation). This slice creates the event that makes the derivation *auditable*; it does not change the derivation.
- **The tip formula.** Feature **05** owns the rule; features **408**, **410**, **411**, **420**, **457** own its inputs and shape. Unaffected, and read, not changed.
- **A refund, a credit line, or a negative-quantity path.** That is **feature 450** — filed. This slice does the opposite: it makes the quantity of an existing line a traced fact.
- **The stock ledger's write path.** That is **feature 421** — filed.
- **Any change to `Bill`, `Visit`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan, menu or waiter-UI change.** The mock-up is `index.html`; feature **08**'s scope.
- **Alembic.**
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the defect

LE31's schema has **ten tables** and, as feature **470** proved by execution, **no `CHECK` constraint on any of them** and **exactly one `UNIQUE` constraint in the whole database** (`bill.visit_id`). The order line is where the business decides *how much food* and, through `qty × unit_price`, *how much money*. Today **the value of that decision can be replaced at any moment, silently, and the only trace of the original decision is whatever a reader remembers.**

The defect is not that `qty` is an `int`. It is that `qty` is a **barely-typed number with no lifecycle**.

### Why "the value" is not the defect

Feature **456** already filed the sign and the size: a line may carry `qty=0` or `qty=-5`, and the database accepts both. That is a *value* defect. This slice is a *time* defect: **the same value, written at a moment when it can no longer mean what it meant.**

### The execution, in full

```
=== LIFECYCLE 1: order a line, fire it, SERVE it, then change its qty ===
  status -> served: ACCEPTED
  UPDATE order_item SET qty=99 on a SERVED line -> ACCEPTED, qty now 99

=== LIFECYCLE 2: the bill's stored subtotal vs SUM(order_item) ===
  bill.subtotal_items stored = 13.00
  SUM(order_item.qty * unit_price) = 643.50

=== LIFECYCLE 3: change the qty AFTER the bill is closed and paid ===
  bill.subtotal_items = 13.00   bill.total_due = 14.30   bill.total_paid = 14.30   paid_at set
  SUM(order_item.qty * unit_price) NOW = 6.50
  derived_tip.amount = 0.00 (computed from total_paid, unchanged by the line edit)

=== LIFECYCLE 6: does the qty rewrite touch the stock ledger? ===
  SUM(stock_entry.qty_delta) for batch 1 = -2 (unchanged by the qty 2->99->1 rewrites)
```

**Read those four blocks together — they are the finding:**

1. **The quantity of a served dish became 99 and then became 1.** The kitchen was told nothing; the guest's bill was never recomputed.
2. **The order and the bill now disagree** — €6.50 of food against a €14.30 bill — and both numbers are in the database, in a table with no constraint connecting them.
3. **The tip did not move.** `DerivedTip.amount` is derived from `total_paid`, not from the lines, so a silent quantity edit leaves the tip **exactly where it was** — a tip that is arithmetically self-consistent and semantically wrong, with no field that ever moved. **This is the honest limit of the finding: the tip does not expose the edit. The bill's `subtotal_items` does, and only by being compared against the lines by hand.**
4. **The append-only ledger recorded nothing.** `SUM(stock_entry.qty_delta)` stayed at `-2` while the order line's quantity went `2 → 99 → 1`. **The ledger is the one part of LE31 that is append-only, and it did not see this event at all** — because a quantity edit is not a stock event, and there is no event table for it.

### The rule this slice files

> **A quantity is set while the line is `new`. After the line has been fired, the quantity is a fact: it changes only through a recorded event that carries the old quantity, the new quantity, the actor and the time.**

The `ItemStatus` ladder is LE31's own (`new → preparing → ready → served`, with `cancelled` off to the side), and the existing timestamps (`fired_at`, `ready_at`, `served_at`) already mark the moment the line left the waiter's hands. **The boundary this slice needs is therefore already present in the schema** — it is `fired_at`.

### Why an event table and not a column

A `previous_qty` column preserves **one** change and loses the second. The corpus has already learned this twice: feature **470** (the ledger's delete) and feature **523** (the catalogue's price history) both chose a table over a column, and **523** states the reason verbatim: *"Implemented as a TABLE, not a column — a `previous_price` column preserves one change and loses the second."* **The same reasoning applies here, and the same precedent is available.**

### The mechanism, stated as the implementer must write it

1. **A new append-only table** — the quantity-change event: the line it belongs to, the old quantity, the new quantity, the actor (`by_user_id`), and the time. It is written **only** by the write path, and it is never updated or deleted.
2. **A guard at the write site.** Any code that changes a line's quantity after the line is fired must write the event **in the same transaction** as the change. If it cannot, it must refuse.
3. **A refusal.** A quantity change on a fired line that arrives **without** an event is refused, the same way feature **456** refuses a non-positive quantity: **the write is refused and nothing is written.**
4. **The bill's relation is stated, not silently inherited.** Feature **415** computes `subtotal_items` from the lines at close time. This slice does not change that computation. What this slice guarantees is that **after the close, a quantity change is a recorded event** — so the pair (*the closed bill*, *the line as it stands now*) is reconstructible, and the question *"why does the order say €6.50 and the bill say €14.30?"* has an answer. **Without this slice the question has no answer at all, because the edit left no trace.**

## Data model

**New table — the quantity-change event.** Naming follows LE31's own conventions (an append-only fact table with an actor and a timestamp, like `stock_entry`):

| column | type | meaning |
|---|---|---|
| `id` | int PK | |
| `order_item_id` | int FK → `order_item.id`, indexed | the line whose quantity changed |
| `old_qty` | int | the quantity before the change |
| `new_qty` | int | the quantity after the change |
| `by_user_id` | int FK → `app_user.id` | who made the change |
| `at` | datetime (UTC) | when |

**Rules the table carries:**

- **Append-only.** Never updated, never deleted. It is a fact table.
- **`old_qty` is the quantity as it stood immediately before this event.** The chain of events reconstructs the line's quantity history; `old_qty` of the first event equals the quantity the line was created with.
- **No `CHECK` on the table is required by this slice** — the write-path guard is the mechanism. (Feature **404** owns the *shape* of money columns and feature **456** owns the *shape* of a quantity; this slice adds no new shape rule.)

**No column is added to `order_item`.** The line keeps its single `qty`, which stays the current quantity. **The history lives in the event table.** This is the same discipline as feature **470**'s ledger and feature **523**'s price history.

**`order_item` is otherwise untouched.** Its `qty` column, its type and its default do not change.

## Implementation

1. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:
   - a quantity change on a `new` line with **no** event is **ACCEPTED** (the waiter is still setting the quantity);
   - a quantity change on a line with `fired_at` set and **no** event is **REFUSED**, and the stored quantity is unchanged;
   - a quantity change on a fired line **with** an event in the same transaction is **ACCEPTED**, and the event carries the old and new quantities, the actor and the time;
   - the event table rejects an update and a delete;
   - **the two-numbers check:** after any accepted quantity change, `SUM(order_item.qty * order_item.unit_price)` for the visit and the line's own event history agree on the current quantity.
2. **Add the event model** to `backend/app/models.py`, following the `StockEntry` shape (an append-only fact with `by_user_id` and `at`).
3. **Add the write-path guard** in the place that changes a line's quantity. **Today there is no such place** — the backend has no orders router — so this slice adds the **helper** the future router will use, exactly as feature **430** does, and it does **not** invent a router. **The helper's signature must make the safe path the only one the type system permits**: a quantity change takes the line, the new quantity and the actor, and it either writes the event and the change together or refuses.
4. **The guard must not depend on a database constraint alone.** SQLite does not enforce `CHECK` at the schema level in the way Postgres does, and the write path is the only place that can also write the event. **Both** the write-path guard and (later) a database-level rule must carry it.
5. **State the ordering against the filed work explicitly** — see *Dependencies*.
6. **Do not modify `index.html`.** The shipped waiter screen is a twelve-way collision zone (features 465, 466, 467, 474, 475, 476, 484, 487, 489, 509, 511, 516). This slice is server-side and schema-side.

## Telegram interaction

**None.** This slice adds no Telegram command, no bot handler and no message. The kitchen is not told, because the kitchen does not need to be told — **the change is a fact about the order, and the fact is recorded.**

## Dependencies

**⭐ THE UPSTREAM-OF-FILED-WORK RULE — THIS SLICE IS UPSTREAM OF A FILED FEATURE AND MUST SAY SO.**

- **Feature 415** implements the bill-close write and computes `subtotal_items = SUM(order_item.unit_price * order_item.qty)`. **It is unaffected by this slice** — it reads the lines and closes the bill. **But** 415's derivation becomes *reconstructible* only once the quantity-change event exists. **415 does not need to wait for this slice; this slice must not contradict 415.**
- **Feature 379** owns the order-line transition log and its actor. **This slice creates a second, adjacent log** — for the quantity, not the status. **The two must share the same actor convention** (a staff `app_user`), and 379's rule that *"no other code path may set `status` directly"* is the precedent this slice follows for `qty`.
- **Feature 452** owns status versus timestamps. **This slice reads `fired_at`** to decide the boundary and changes nothing about it.
- **Feature 444** owns the line price's history; **feature 456** owns the quantity's sign and size. **Both are unaffected.** This slice is the **quantity's history and timing** — the third rule on the same table.
- **Feature 427** owns the SQLite foreign-key pragma. **A `CHECK` constraint is not what carries this rule**, so 427 is not a prerequisite; it is noted because the same dev/prod divergence argument applies.
- **Feature 421** owns the ledger's write path. The event table this slice adds is **not** a ledger row: a quantity change moves no stock. **452** says so verbatim: *"A transition moves no stock."* The same holds here.
- **Feature 446** owns the migration path, if the event table needs one for an existing deployment. `create_all()` cannot alter an existing table, and this slice **adds** a table, which `create_all()` handles — so 446 is relevant only if the implementer also adds a `CHECK` to `order_item` in the same PR.

## Open questions

1. **Should the boundary be `status` or `fired_at`?** The status ladder and the timestamps are two views of the same moment, and feature **452** owns the rule that they agree. **Recommendation: use `fired_at`** — it is a fact about the line, not a state that can be set out of order, and 452 already owns making them agree. **But the choice belongs to the implementer, and it must be stated.**
2. **Should a `cancelled` line's quantity be writable?** Recommendation: **no** — a cancelled line is a fact too. **But a cancellation that is itself reversed (feature **452**'s concern) is a different event.**
3. **Should the event table be the *only* way a quantity changes, or should the quantity be *immutable* after firing with the event recording a *correction*?** The first is a lifecycle rule; the second is a correction rule. **The first is what the corpus's own words support** ("neither owns the quantity changing after the line exists"). **The second is a strictly larger design and is not filed here.**
4. **What happens to the bill when a quantity changes after the close?** Recommendation: **the bill is not recomputed** — a closed bill is a fact (415) — and the event is what makes the discrepancy *visible*. **But a rule that says "a quantity change after the close raises a flag on the bill" is a plausible alternative and is not decided here.**
5. **Is the event table a `StockEntry`-shaped table or a first-class entity with its own `created_at`?** Recommendation: `StockEntry`-shaped (an `at` column, no `created_at`), because that is the append-only precedent. **Not decided here.**

## Why this matters

**LE31's schema has one append-only ledger and nine ordinary tables, and the ordinary tables are where the money is.**

The `StockEntry` docstring says, verbatim: *"Append-only ledger. Never UPDATE or DELETE rows."* The order line — **the table that decides how much food and, through `qty × unit_price`, how much money** — has no such sentence, no such mechanism and no such history. The corpus has been closing this family of gaps one column at a time: **444** gave the line's *price* a history, **456** gave the *quantity* a valid range, **452** gave the *status* a rule, **471** gave the *batch's remaining quantity* a derivation, **522** gave the *catalogue's delete* a guard, **523** gave the *catalogue's price* a history, **524** gave the *staff role* an event. **Each of those closed one door and left the quantity's door open.**

**And the corpus said so, twice, on two different days.** Feature **470**: *"neither owns the quantity changing after the line exists. Recorded, not filed."* Feature **471**, the same day: *"nobody owns the quantity changing after the line exists. Recorded, not filed."* **A finding that is recorded twice and filed never is a finding that will be rediscovered forever.** This contract is the door, closed.

**The operational shape of the defect.** A guest orders two tiramisu. The kitchen serves them. The waiter notices the second was not plated and goes back to the terminal to "fix the line". **Nothing asks whether the line may still be fixed, nothing records that it was, the kitchen is not told, the ledger is not told, and the bill — if it has already been closed and paid — is not revisited.** The next person to look at the database sees an order for one tiramisu, a ledger entry for two, and a bill for two. **Nothing in the data says what happened.** A restaurant cannot answer "why does the order and the bill disagree" because the disagreement was never recorded as an event — it was recorded as *nothing at all*.

**Why this is a `build` and not a `defer`.** The change is small (one table, one helper, one guard) and the schema it lands on is LE31's own. The demand is not evidenced by an operator complaint — **the honest framing is that this is a schema-integrity defect, not a reported incident** — but it is the same class of defect the corpus has filed seven times in this family, and the charter's **P0** row 43 (*"Waiter can browse today's menu and add items to the active visit"*) and row 45 (*"Selling a prepared item decrements its active batch's `qty_remaining` and writes a `StockEntry(-1, reason='sale')` row"*) both assume that an order line's quantity and the ledger's record of it **agree**. **Today nothing makes them agree, and nothing notices when they stop.**

## Out of scope (v1)

- **The sign and size of a quantity** — **feature 456**, filed. This slice owns *when* a quantity may change, not *what* it may be.
- **The unit price's mutability and history** — **feature 444**, filed. Same table, adjacent column, separate slice.
- **`OrderItem.status` transitions, the transition log and their timestamps** — **features 452, 379**, filed.
- **The line's insertion order** — **feature 430**, filed.
- **`Bill.subtotal_items`' derivation and the `Bill → order_item` edge** — **features 435, 415**, filed. This slice makes the derivation *auditable*; it does not change it.
- **Recomputing a closed bill** — **feature 415** owns the bill-close write.
- **The tip formula and its inputs** — **features 05, 408, 410, 411, 420, 457**, filed.
- **A refund, a credit or a negative-quantity path** — **feature 450**, filed.
- **The stock ledger's write path and `Batch.qty_remaining`** — **features 421, 374, 471**, filed. **A quantity change moves no stock** (452's own words).
- **Any change to `Bill`, `Visit`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan, menu or waiter-UI change** — `index.html` is feature **08**'s scope and a twelve-way collision zone.
- **Alembic**, except as noted in *Dependencies* for feature 446.
- **Any change to `PROJECT_CHARTER.md`.**
