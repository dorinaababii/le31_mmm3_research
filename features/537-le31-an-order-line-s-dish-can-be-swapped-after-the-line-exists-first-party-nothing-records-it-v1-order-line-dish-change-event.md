# Feature 537 — An order line's dish can be swapped after the line exists, and the price and the ledger keep pointing at the old one

> **Pick A of Daily Brainstorm 2026-11-27 (109th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
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
>     fired_at: datetime | None = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     ready_at: datetime | None = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     served_at: datetime | None = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
> ```
>
> **`menu_item_id` is a bare foreign key with no constraint, no history, and no write-path rule.** Feature **456** owns *what a quantity may be*. Feature **444** owns *the history of the line's price*. Feature **441** owns *the rule that a ledger row's batch and its order line name the same dish*. **Nobody owns the line's dish being changed after the line exists.**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with two dishes — Schnitzel at €14.00 and Margherita at €9.00 — one batch of Schnitzel, one visit, one served order line at qty 2, one `StockEntry(-2, reason='sale')`, and one paid bill):
>
> ```
>   UPDATE order_item SET menu_item_id = <margherita> WHERE id = 1   ->  ACCEPTED
>
>   the line's dish          = 2   (was 1)              <- says MARGHERITA
>   the line's unit_price    = 14                      <- the SCHNITZEL's price
>   the new dish's price     = 9
>   SUM(stock_entry.qty_delta) for the schnitzel batch = -2   <- two SCHNITZEL were sold
>   batch.menu_item_id       = 1                      <- the batch is still schnitzel's
> ```
>
> **⭐ THREE NUMBERS THAT SHOULD AGREE, ALL THREE DISAGREE.** The line says **Margherita**. The line's price says **Schnitzel at €14.00**. The ledger says **two Schnitzel were sold**. A guest who ordered Schnitzel is billed the Schnitzel price, the kitchen was told to plate Schnitzel, and the stock ledger consumed Schnitzel — while the order line says Margherita.
>
> **⭐ AND THE REWRITE DEFEATS A FILED FEATURE'S OWN RULE.** Feature **441** ("a `StockEntry` may name a batch and an order line for different dishes") specifies the rule *"`batch.menu_item_id == order_item.menu_item_id`"*, and its own text says it *"reads `menu_item_id` **through** the order line"*. That rule is enforced **at the write path, at the moment the ledger row is written** — so it was true when the row was written. **It is not true afterwards.** A later rewrite of the line's `menu_item_id` makes the ledger row permanently, silently incoherent, and the ledger is append-only by charter, so the wrong row can never be corrected: **feature 441's coherence check becomes a check of a value that has since moved.**
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **570** feature contracts and **525** HANDOFFs (1,093 files) returns **zero hits** for a rule about the line's *dish* changing after the line exists:
>
> | sweep | files | hits |
> |---|---|---|
> | `order_item.{0,50}menu_item_id.{0,60}(update\|rewrite\|mutab\|swapp?ed\|chang(e\|ing))` | 0 | 0 |
> | `(line\|order line).{0,50}(dish\|menu_item).{0,50}(rewrite\|mutab\|swapp?ed)` | 0 | 0 |
> | `menu_item_id.{0,60}(rewritten\|swapped\|mutab)` | 0 | 0 |
>
> **95** corpus files mention `menu_item_id` — the column is well discussed. **Not one of them is about the column changing.** The nearest neighbours each own a *different* half:
>
> | rule | mechanism | owner |
> |---|---|---|
> | what a line's **quantity** may be (no `0`, no `-5`) | a value check at the write site | **feature 456** |
> | the **price**'s mutability and history | history table | **feature 444** |
> | the line's **status** transition log and its actor | append-only transition table | **features 379, 452** |
> | the line's **insertion** order | an `added_at` column | **feature 430** |
> | a ledger row's batch and line must name the **same dish** | a write-path coherence rule | **feature 441** — **read-side, at write time** |
> | **the line's dish changing after the line exists** | **event table + write-path guard** | **THIS SLICE** |
>
> **⭐ AND 441 IS UPSTREAM-OF-FILED-WORK.** Feature **441**'s own *Out of scope* says: *"**Any write path.** This feature supplies the **rule** and the **helper**; feature **421** supplies the **single write path** the helper is called from."* And feature **421**'s own scope places *"the business rules"* out of scope. **If the line's dish can be rewritten after the sale row is written, 421 and 441 will faithfully implement a rule that a later mutation can defeat.** **This contract therefore states the ordering explicitly: this lands FIRST, or in the same PR as 421 and 441.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a swapped dish; no code path changes `menu_item_id` today — there is no orders router).
>
> The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`.

## Goal

Make an order line's **dish** mean one thing at every point in the line's life: **a line names the dish the guest ordered, and that is a fact with a history.**

The concrete outcome: **the dish on a line that has left the waiter's hands cannot be rewritten silently**, and where the domain genuinely requires a change (a mis-keyed line, a wrong dish rung in), that change is **a recorded event** carrying the old dish, the new dish, the actor and the time — and the **price travels with the dish** or the line is refused.

The single sentence this feature exists to make true: *a line's dish is set when the line is created; after that it is a fact with a history, and the line's price is the price of the dish it names.*

## Scope

- **One new table** — `OrderItemDishChange` — recording `order_item_id`, `from_menu_item_id`, `to_menu_item_id`, `from_unit_price`, `to_unit_price`, `by_user_id`, `at`.
- **One write-path rule**: the dish of a line may be changed only while the line is in `ItemStatus.new` — the waiter's own draft state — and only through a helper that writes the change event and moves the line's `unit_price` to the new dish's price in the same transaction.
- **A refusal** for the case the domain genuinely has: changing the dish of a line that has already been **fired** (`preparing` / `ready` / `served`) is refused by the write path, because the kitchen has already acted on it. A `cancelled` line's dish is never changed.
- **A read-side consistency assertion**: for any line that carries a dish change, `unit_price` equals the **new** dish's price at the time of the change and is not re-derived later — the line's price is a **snapshot**, exactly as feature **444** already established for the line's price itself.
- **A regression test** that asserts the swap of a fired line's dish is refused, and that a permitted swap on a `new` line writes one change row with the old dish, the new dish, the actor and both prices.

**The dish change is recorded in an event table, not by a `previous_*` column.** A column preserves one change and loses the second; the corpus already established that shape for the menu price (feature **523**: *"Implemented as a TABLE, not a column — a `previous_price` column preserves one change and loses the second."*).

## Out of scope

- **The line's quantity.** Feature **456** owns the sign and the size; feature **531** owns *when* the quantity may change. **This slice does not change `qty` and does not add a quantity event.**
- **The line's price's own history.** Feature **444** owns it, and feature **523** owns the **catalogue's** price history. This slice does not touch either feature's table, its event shape, or its write path.
- **The line's status transition log.** Features **379** and **452** own it. A dish change and a status change are **two different events** and get **two different records** — feature 444's own *Out of scope* states this rule for its own event, and it applies here verbatim.
- **The ledger coherence rule** (`batch.menu_item_id == order_item.menu_item_id`). Feature **441** owns it. This slice does not add it, does not re-implement it, and does not add a write path — but **this slice must land before or with it**, because a mutable dish makes 441's rule defeatable after the fact.
- **The single `StockEntry` write path.** Feature **421** owns it.
- **`StockEntry.ref_order_item_id`'s foreign key.** Feature **426**.
- **Any delete of a menu item.** Feature **522** owns the catalogue's delete/retire guard. This slice does not change it — but it records the interaction in *Dependencies*, because a retired dish and a changed dish are different questions.
- **The menu catalogue's own fields.** `MenuItem.name`, `category`, `unit` — feature **431** owns the category's spelling, feature **458** owns the name's uniqueness. **This slice does not touch them.**
- **Any change to `Visit`, `Bill`, `Table`, `Batch`, `Shift`, `DerivedTip` or `StockEntry`.**
- **A floor-plan, menu or waiter-UI change.** `index.html` is feature **08**'s scope and a thirteen-way collision zone (features 465/466/467/474/475/476/484/487/489/509/511/516 and this corpus's other UI owners).
- **Alembic**, except as noted in *Dependencies* for feature **446**.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.
- **Any change to `ItemStatus`'s enum values or the order of transitions** — feature 379's own rule.

## Description

### The defect, as executed

The schema declares `menu_item_id` as a bare foreign key. There is no `UniqueConstraint`, no `CheckConstraint`, no `ondelete` clause, and **no write path exists** that could enforce anything about it. The line therefore names a dish, and nothing stops that name from changing.

The executed probe seeded a coherent world and then made one change:

```
  dish 1 = Schnitzel   unit_price 14.00
  dish 2 = Margherita  unit_price  9.00
  order_item(id=1, menu_item_id=1, qty=2, unit_price=14.00, status='served')
  batch(id=1, menu_item_id=1, qty_start=10)          # a batch of schnitzel
  stock_entry(id=1, batch_id=1, qty_delta=-2, reason='sale')
  bill(id=1, subtotal_items=28.00, subtotal_tax=5.60, total_due=33.60, total_paid=33.60)

  UPDATE order_item SET menu_item_id = 2 WHERE id = 1;      ->  ACCEPTED
```

and then read back the three things that must agree:

| what | value after the rewrite | what it should say |
|---|---|---|
| `order_item.menu_item_id` | **2** (Margherita) | 1 (Schnitzel) — the guest ordered Schnitzel |
| `order_item.unit_price` | **14.00** | 9.00 — the price of the dish the line now names |
| `SUM(stock_entry.qty_delta)` for batch 1 | **-2** | -2 — **two Schnitzel**, and the line now says Margherita |

**Nothing raised. Nothing was written to any log. The bill still says €33.60 and its `subtotal_items` still says €28.00 — the bill remains internally consistent and globally wrong.**

### Why the "three numbers" shape is the tell

The charter's own P0 row 45 says: *"Selling a prepared item decrements its active batch's `qty_remaining` and writes a `StockEntry(-1, reason='sale')` row."* The acceptance criterion is *"Manual test: order a tiramisu → stock goes 8 → 7 → ledger has one entry."*

That criterion is **only checkable if the line, the price and the ledger continue to name the same dish.** The rewrite breaks exactly that: the ledger is right about Schnitzel, the line is wrong, and the price is right about Schnitzel. **A single number would never show this.** The tell is the *disagreement between three numbers that are each individually plausible*.

### Why feature 441's rule is defeated by this, specifically

Feature 441's rule, in its own words, is: *"**COHERENCE:** `batch.menu_item_id == order_item.menu_item_id`"*, and it obtains the line's dish by *reading `menu_item_id` **through** the order line*. It is enforced at the write path, at the moment the ledger row is written.

That is a **read-side rule over a mutable value**. It is true at write time and it is false after a later rewrite. Because the ledger is append-only by charter (§4.3, *"EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE."*), **the wrong row is permanent**: a correction must be a *new* ledger row, and the audit trail will show a sale of Schnitzel pointing at a line that says Margherita, with nothing to explain the gap.

**This is not a duplicate of 441. It is the missing half of it.** 441 owns *the rule at the write path*. This slice owns *the value the rule reads*. One without the other is a guarantee over a number that can move.

### Why the fix is an event table and not a guard alone

A guard that refuses a fired line's dish change is necessary but not sufficient:

1. A line that is still `new` **may** legitimately be corrected — the waiter rang it wrong. The rule must permit that.
2. When it is permitted, the change must be **visible afterwards**: which dish was rung, which dish it became, who changed it and when.
3. The line's `unit_price` must move with the dish **in the same transaction**, or the line will name Margherita at Schnitzel's price — which is the corruption this feature exists to remove.
4. The price that travels is a **snapshot** of the new dish's price at the moment of the change — feature **444** already established that a line's price is a snapshot and not a live join to the catalogue, and that must not change.

A `previous_menu_item_id` column would satisfy (1)–(3) once and fail on the second change: it preserves one change and loses the second. The corpus has already made this argument for the catalogue's price in feature **523**; the same argument applies here.

### The refusal, stated precisely

The domain's rule, which the contract does not invent:

> **A dish may be corrected only before the kitchen has been told.** A line that has been fired (`preparing`, `ready`, `served`) names a dish the kitchen has already acted on, and changing it would make the ticket and the plate disagree. A `cancelled` line's dish is never changed either — the line's own price is already on the bill.

The refusal message must say **which** dish the line names and **which** dish was refused, so the waiter can correct the order by cancelling and re-ringing, which is the operation the domain already has.

### The read-side consistency assertion

For every row in `OrderItemDishChange`, the line's `unit_price` must equal that row's `to_unit_price`, and the line's `menu_item_id` must equal that row's `to_menu_item_id`. If a later change exists, the *latest* change's `to_*` values are the ones that must match. This assertion is a **test**, not a second source of truth: the change event is the record, and the line's columns are its current projection.

### The actor

The actor is a **staff** member (`app_user`), never a guest — consistent with charter §3.1 (v1 stores counts, not guest identities) and with feature **379**'s actor convention, which this slice follows rather than reinvents. The convention is recorded in feature **417**'s schema note: *"every actor field carries a foreign key."*

## Data model

```python
# backend/app/models.py — ADD, do not modify any existing class

class OrderItemDishChange(SQLModel, table=True):
    """The dish on an order line changed. Append-only."""
    __tablename__ = "order_item_dish_change"

    id: int | None = Field(default=None, primary_key=True)
    order_item_id: int = Field(foreign_key="order_item.id", index=True)
    from_menu_item_id: int = Field(foreign_key="menu_item.id")
    to_menu_item_id: int = Field(foreign_key="menu_item.id")
    from_unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    to_unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

Notes the implementer must honour:

- The class name and table name follow the corpus's convention: **`order_item_dish_change`**, in the pluralised snake style of `stock_entry` and `order_item`.
- `by_user_id` is **nullable** with a foreign key, exactly the form feature **379** specifies for `OrderItemTransition.by_user_id` and feature **417** specifies for `StockEntry.by_user_id` — the corpus's actor convention, applied a fourth time.
- `from_unit_price` / `to_unit_price` are **snapshots**, not joins. Feature **444**'s rule, applied to the dish change.
- **Do not add a `UniqueConstraint`** on any pair here. A line may be corrected more than once; the constraint would forbid the second correction.

**Migration path.** `PROJECT_CHARTER.md` §3.2 says v1 uses `init_db()` rather than Alembic, and `create_all()` **cannot alter an existing table** — but this slice **adds** a table and **changes no existing column**, so `create_all()` is sufficient for a fresh database. **If the deployment has an existing database, feature **446** owns the migration path and this slice must not invent one.** The `out of scope` section says so, and it is repeated here because it is the single most common way a slice like this goes wrong.

## Implementation

1. **`backend/app/models.py`** — add `class OrderItemDishChange` exactly as specified above. **Do not touch `OrderItem`, `MenuItem`, `Batch`, `StockEntry`, `Visit`, `Bill`, `Shift` or `DerivedTip`.**
2. **`backend/app/services/order_line_service.py`** (new file — or the equivalent service package the repo grows; see *Dependencies*) — one helper, `change_order_line_dish(session, order_item_id, to_menu_item_id, actor_id)`, which:
   - loads the line and the target dish;
   - **refuses** when `line.status` is not `ItemStatus.new`, raising a legible error naming the current dish, the requested dish and the line's status;
   - writes **one** `OrderItemDishChange` row carrying both dishes and both prices;
   - sets `line.menu_item_id = to_menu_item_id` **and** `line.unit_price = <the target dish's price>`;
   - commits **once**.
3. **The helper is the only writer of `order_item.menu_item_id` after the line's creation.** A grep for `menu_item_id =` under `backend/` must return the creation path and this helper, and nothing else. **Record the grep output in the PR description** — a rule with two writers is not a rule.
4. **The consistency assertion** — a test that, for every `OrderItemDishChange`, asserts `line.menu_item_id == change.to_menu_item_id` and `line.unit_price == change.to_unit_price`, using the **latest** change per line.
5. **Regression tests** — at minimum:
   - a dish change on a **`served`** line is **refused**, and the line is unchanged;
   - a dish change on a **`new`** line is **accepted**, writes exactly **one** change row with the correct `from_*`/`to_*` values and the actor, and sets `unit_price` to the new dish's price;
   - a dish change on a **`cancelled`** line is **refused**;
   - a **second** dish change on the same line is accepted and produces a **second** row — this is the case a `previous_*` column would have lost.
6. **The docs** — a short note in the repository's own data-model documentation that a line's dish is a fact with a history, and that the price is a snapshot of the dish's price at the moment of the change.

**The implementer must not guess at step 2's package location.** LE31 has **no `services/` package** today (`backend/app/` holds `models.py`, `main.py`, `routers/`, `bot/`). Feature **441** says it *"supplies the rule and the helper"* and feature **421** supplies *"the single write path"*; whichever of the two lands first **creates** the package. **If `backend/app/services/` does not exist when you start, create it — and say so in the PR.** Do not put the helper in `routers/`: it is not a route, and feature 441's own *Out of scope* draws that line.

## Telegram interaction

**None.** The waiter UI is `index.html`, feature **08**'s scope and a thirteen-way collision zone. This slice changes **no** surface. The refusal is raised at the write path and reaches whichever surface eventually calls the helper — and **the helper's error must be legible**, because a surface that cannot express the refusal will swallow it. That is feature **486**'s problem (the surface's capacity display), not this slice's, and it is recorded in *Dependencies*.

The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched. A dish change is a waiter's correction; the cook's photo flow is feature **469**'s and feature **380**'s territory.

## Dependencies

- **Feature 421 (the single `StockEntry` write path) — ⭐ THIS SLICE MUST LAND FIRST, or in the same PR.** 421 owns where ledger rows are written and, in its own words, places *"the business rules"* out of scope. **If this slice has not landed, 421 will implement a write path that lets the line's dish be rewritten afterwards — and 441's coherence rule, which 421's path enforces, will then be defeatable after the fact.**
- **Feature 441 (the ledger coherence rule) — ⭐ THIS SLICE MUST LAND FIRST, or in the same PR.** 441's rule is *read-side over `order_item.menu_item_id`* and is enforced at the write path. **A mutable dish makes 441's guarantee defeatable after the fact, and the ledger is append-only, so the wrong row is permanent.** 441's own *Out of scope* says it supplies *"the rule and the helper"* — this slice supplies the *value the rule reads*. **The two must not be merged, and the implementer of 441 must not add a dish-change guard and the implementer of this slice must not add the coherence rule.**
- **Feature 444 (the line's price history) — adjacent, not blocking.** 444 owns the *price's* history and says the line's price is a snapshot. This slice moves the price **when the dish changes**, and records both prices in the change row. **444's table and 444's event shape are untouched.**
- **Feature 531 (the line's quantity change event) — adjacent, same table, may land in either order.** 531 owns `order_item.qty`. **This slice must not add a quantity event, must not touch `qty`, and must not reuse 531's table.** If both land in one PR, keep the two event tables separate.
- **Feature 456 (the sign and size of a quantity) — untouched.** A different column, a different rule.
- **Feature 379 / 452 (the status transition log) — adjacent, same table, different event.** A dish change and a status change get two different records.
- **Feature 446 (the migration path) — needed only if the deployment already has a database.** This slice **adds** a table and changes no existing column, so `create_all()` suffices for a fresh database. **If an existing database must be migrated, 446 owns the mechanism and this slice must not invent one.**
- **Feature 522 (the catalogue's delete/retire guard) — adjacent.** 522 owns `DELETE FROM menu_item`. This slice's `from_menu_item_id` / `to_menu_item_id` are foreign keys to `menu_item.id`; while the pragma is off (feature **427**) they are **declared but unenforced**, so a change row may name a retired dish. **That is 522's and 427's question, not this slice's** — and it is why the change row's dish ids are snapshots of *ids*, not of names.
- **Feature 427 (the SQLite FK pragma) — adjacent.** The pragma is off by default in SQLite (`PRAGMA foreign_keys = 0` — proved by execution), so the foreign keys on this new table are enforced in Postgres and not in SQLite. **The write-path rule does not depend on them**, and the implementer must not write a test that passes only because SQLite ignores a foreign key.

## Open questions

1. **May a dish be corrected on a line that is `preparing`?** The contract refuses anything not `new`. **The domain may disagree**: a kitchen that rings *"wrong dish"* mid-preparation is a real event. **Recorded default: refuse — the kitchen has been told, and the correction route is cancel-and-re-ring.** **The implementer must not guess; the decision is recorded and escalated.**
2. **Does the correction create a new line instead of changing the old one?** A cancel-and-re-ring model would sidestep the event table entirely, at the cost of the guest's line history. **Recorded default: change in place, with the event.** **The implementer must not build the cancel-and-re-ring flow — that is a product decision, not an implementation detail.**
3. **What is the correction's effect on the bill?** If the bill is already closed, the price moved after the money was taken. **Feature **532** owns the bill's money columns and feature **415** owns the close write — this slice does not decide.** **Recorded: the change is recorded with both prices, and the bill's arithmetic is 532's and 415's question.**
4. **Is the actor required?** `by_user_id` is nullable, matching the corpus's convention for `StockEntry.by_user_id` and `OrderItemTransition.by_user_id`. **Recorded default: nullable — a correction made by an unauthenticated path is still a correction, and a missing actor is visible as a missing actor.** **The implementer must not make it non-nullable without a decision.**
5. **Does the same rule apply to `course`?** `OrderItem.course` is the other free-text field on the line (appetizer / main / dessert) and is equally rewritable. **It is a different question — a course is a routing hint, not an identity — and it is recorded here so the next pass files it or discards it deliberately. It is NOT taken by this slice.**

## Why this matters

**The order line is the atom of LE31's money.** Every number the restaurant reports — the bill, the tip, the covers, the top-items list — is a sum over `order_item` rows. A line whose dish disagrees with its price and with the ledger is a row that is *individually plausible and collectively wrong*, which is the hardest class of defect to catch: nothing raises, nothing looks broken, and every report derived from it is quietly off.

**And the disagreement is permanent in one direction.** The ledger is append-only by charter. A line whose dish was swapped after the sale row was written leaves a permanent audit artefact saying Schnitzel was sold for a line that says Margherita. **The correction is a new row, so the trail shows both facts and nothing that connects them.** The rule this slice adds is what makes that trail readable.

**It is the same shape as three defects the corpus has already filed** — features **531** (the quantity), **532** (the bill's money), **533** (the party's composition), **534** (the tender method), **535** (the tip's formula version) and **536** (the shift's opening float) — and it is the one column of the same table that the corpus sweep returned **zero** hits for. **Six sibling columns have a rule; the seventh does not.** That is not a coincidence: it is the shape of a defect that is only visible when you execute the update rather than read the schema.

**It is also the cheapest possible fix at the right moment.** There is **no orders router today** — `backend/app/routers/` holds only `__init__.py` and `tables.py` — so **no code path changes `menu_item_id`**, and the defect is **latent, not corrupting data**. That is exactly the moment to add the rule: before the first write path exists, not after. Feature 414's own audit note states the generalisable form of this lesson: *"when an audit domain stops yielding, the next untouched domain is where the next defect is."*

**The demand is INFERRED and the contract says so.** No operator has reported a swapped dish, because there is no surface that can swap one. **The evidence for the defect is OBSERVED — executed, re-runnable, with the numbers in this contract — and the evidence for the priority is INFERRED.** Those are different claims and the gate asks for both.

## Adjacent evidence

- **Feature 441** (`le31-stockentry-may-name-a-batch-and-an-order-line-for-different-dishes`) — the rule this slice protects. Its own words: *"the cross-item rule reads `menu_item_id` **through** the order line"*, and *"**COHERENCE:** `batch.menu_item_id == order_item.menu_item_id`"*.
- **Feature 421** (`le31-stockentry-append-only-linter-rule-…`) — *"the single write path"*; its own scope places *"the business rules"* out of scope, which is why this slice must land first.
- **Feature 444** (`le31-order-item-unit-price-is-mutable-in-place-with-no-trace`) — the line's price is a **snapshot**; the dish change moves the snapshot and records both.
- **Feature 523** (`le31-the-catalogue-s-own-price-can-be-rewritten-with-no-trace`) — *"Implemented as a TABLE, not a column — a `previous_price` column preserves one change and loses the second."* **The same argument, applied to the dish.**
- **Feature 531 / 532 / 533 / 534 / 535 / 536** — the six sibling change-event contracts on the same codebase. **This slice is the seventh, and the one column the sweep left uncovered.**
- **Feature 531's own evidence is the precedent for the mechanism** — an append-only event table carrying the old value, the new value, the actor and the time, plus a write-path guard.
- **Charter P0 row 45** — *"Selling a prepared item decrements its active batch's `qty_remaining` and writes a `StockEntry(-1, reason='sale')` row."* **The acceptance criterion is only checkable if the line, the price and the ledger keep naming the same dish.**
- **Feature 427** — the SQLite FK pragma, proved by execution (`PRAGMA foreign_keys = 0`), which is why this slice's rule lives at the write path and not only in the foreign keys.

## Verification protocol

**Re-run the probe.** `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py` builds LE31's real schema on a throwaway SQLite file and executes the rewrite. **Its output, before the fix, is `ACCEPTED`.** After the fix, the same probe must show the fired-line dish change **refused**.

**The negative control is load-bearing.** A test that asserts "the dish change is refused" **must fail** when the guard is removed — assert that by commenting out the refusal and watching the test go red. **A test that passes both with and without the guard proves nothing.**

**The assertions, in order:**

1. `UPDATE order_item SET menu_item_id` on a **served** line is **refused**; the line's `menu_item_id` and `unit_price` are unchanged; **zero** `OrderItemDishChange` rows exist.
2. `change_order_line_dish(..., status='new')` is **accepted**; exactly **one** change row exists with `from_menu_item_id`, `to_menu_item_id`, `from_unit_price`, `to_unit_price`, `by_user_id` and `at` correct; `line.menu_item_id` and `line.unit_price` both moved.
3. A **second** change on the same line produces a **second** row (the case a `previous_*` column loses).
4. A change on a **`cancelled`** line is refused.
5. The consistency assertion holds for every change row: `line.menu_item_id == latest_change.to_menu_item_id` and `line.unit_price == latest_change.to_unit_price`.
6. A dish change on a `new` line **does not** write a `StockEntry` row and **does not** touch `batch.qty_remaining` — the ledger is untouched by a dish correction.
7. `grep -rn "menu_item_id = " backend/` returns the creation path and the helper, **and nothing else**.

**A note on the numbers in this contract.** Every number quoted here was produced by execution against LE31's real schema on 2026-11-27, by the parent, with the probe in the `scripts/` directory named above. **They are not transcribed from a subagent's prose.** Where a claim is not proved by execution — Postgres behaviour, the UI's reaction, the operational demand — this contract says so explicitly, in the *Evidence class* line, in the *Open questions*, and in *Why this matters*.
