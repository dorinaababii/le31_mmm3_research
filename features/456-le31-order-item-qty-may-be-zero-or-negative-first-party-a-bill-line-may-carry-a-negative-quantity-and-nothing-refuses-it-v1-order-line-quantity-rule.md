# Feature 456 — An order line may carry a quantity of zero or negative, and nothing refuses it

> **Pick A of Daily Research 2026-11-08 (86th daily-research pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
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
> **`qty` is a bare `int` with a default of `1` and no constraint.** It is the column that turns an order line into money.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then real inserts):
>
> ```
>   OrderItem(qty=0,  unit_price=10.00)  -> ACCEPTED   id=1
>   OrderItem(qty=-5, unit_price=10.00)  -> ACCEPTED   id=2
>   OrderItem(qty=3,  unit_price=10.00)  -> ACCEPTED   id=3
>
>   qty(-5) * unit_price(10.00) = -50.00     <- a negative money value on a bill line
>   qty( 0) * unit_price(10.00) =   0.00     <- a line that contributes nothing but occupies a row
> ```
>
> **And the constraint census of the whole live schema, read back from the created database:**
>
> ```
>   TOTAL CHECK constraints across 10 tables: 0
>   UNIQUE constraints: bill -> ['visit_id']   (and nothing else)
>   UNIQUE indexes:     {}
> ```
>
> **⭐ AND NO FEATURE OWNS IT.** A sweep over all **941** feature contracts and HANDOFFs in `features/` + `specs/` returns **zero hits** for a bill-line quantity sign or size rule — the searches `order_item.{0,40}qty.{0,30}(negative|zero|<= *0)`, `(negative|zero).{0,30}(qty|quantity).{0,30}line` and `qty.{0,20}must be.{0,10}(positive|greater)` all return **0**. The concept "stock quantity" and the concept "money precision" are both heavily covered; **the specific rule "a bill line carries a positive quantity" is not.**
>
> **⭐ AND THE CORPUS ALREADY KNOWS THE ADJACENT RULE.** Feature **449** owns the order line's `unit_price` being mutable in place with no trace. Feature **452** owns an order line's `status` disagreeing with its timestamps. Feature **450** owns the absence of a refund concept. **Three features own three neighbouring columns and rules on the same table — and the one column that turns the line into money is unconstrained.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a bad quantity; the corpus confirms nobody owns the rule). The honest framing: **the schema permits a bill line to subtract money.**

## Goal

Make a bill line's quantity **mean one thing**: **a line carries a positive quantity of something**, so that when the bill is closed its subtotal can only ever be a sum of real things.

The concrete outcome: **the database refuses an order line whose quantity is zero or negative**, and the write path names the offending dish.

## Scope

**In scope (v1):**

- **A rule that `order_item.qty` is strictly positive** — a `CHECK (qty > 0)` constraint, enforced by the database on both SQLite and Postgres.
- **A decision about whether zero is allowed** — *Recorded default: **zero is NOT allowed**; the rule is `qty > 0`.* **The implementer must record the choice** (see *Open questions* 1). **The reason the default excludes zero** is that a line with `qty = 0` contributes `0.00` to the subtotal while still occupying a row, appearing on the bill, appearing in the kitchen ticket, and appearing in every per-dish sales report as a dish that was ordered — **a zero-quantity line is a line that says "the guest ordered this" and means "the guest ordered none of this."**
- **A regression test** that fails on today's code and passes on the fixed code: inserting an order line with `qty <= 0` is **refused**.
- **A rule for what the write path does with the refusal** — an `IntegrityError` handled into an operator-readable message naming the dish and the offending quantity.
- **One line in `features/02-order-taking.md`**, whose data model lists `OrderItem (…, qty, …)`, so the contract and the schema agree on the rule.

## Out of scope (v1)

- **A refund mechanism.** That is **feature 450** — filed, `build`. This slice does **not** create a refund, a credit line, or a negative-quantity path. **The point of this slice is the opposite: to make the absence of a refund mechanism visible rather than to fill it.**
- **A `CHECK` constraint on the money columns' shape.** That is **feature 404** — filed. 404 owns `round(x, 2)` and `typeof(x) = 'integer'` — the *shape* of a value. **This slice owns the *size and sign* of a quantity.** They are separate slices and **must not be merged** — a reviewer must be able to check each on its own.
- **`OrderItem.unit_price` and its mutability.** That is **feature 449** — filed. Same table, adjacent column.
- **`OrderItem.status` versus its timestamps.** That is **feature 452** — filed. Same table again.
- **A `CHECK` on `StockEntry.qty_delta`.** That is feature 404's territory, on a **different table** — the *ledger's* quantity, not the *bill line's*. **A negative ledger delta is legitimate** (a sale consumes stock); **a negative bill line is not.** **The two must never be conflated.**
- **`Batch.qty_remaining` versus `Batch.qty_start`.** That is **feature 374** — filed. A different table, a different question.
- **The derivation of `Bill.subtotal_items` from the order lines.** That is **feature 435** — filed. **435 owns the missing `Bill → order_item` edge; this slice owns the shape of one line.** They are complementary and must not be merged.
- **Any change to `Visit`, `Bill`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan or menu UI change.** The mock-up is `index.html`; feature 08's scope.
- **Alembic.**

## Description

### The defect, as observed in LE31's own code on 2026-11-08

`OrderItem.qty` is `qty: int = 1` — a bare annotation with a default. SQLModel gives it `INTEGER NOT NULL` and **nothing else**. There is no `CHECK`, no minimum, no maximum, no relationship to `unit_price`.

**Executed — the live DDL, read back from the created database:**

```sql
CREATE TABLE order_item (
    id INTEGER NOT NULL,
    visit_id INTEGER NOT NULL,
    menu_item_id INTEGER NOT NULL,
    qty INTEGER NOT NULL,          <- NOT NULL, but no CHECK, no UNIQUE, no index
    unit_price NUMERIC(10, 2) NOT NULL,
    course VARCHAR,
    status VARCHAR(9) NOT NULL,
    notes VARCHAR,
    fired_at DATETIME,
    ready_at DATETIME,
    served_at DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY(visit_id) REFERENCES visit (id),
    FOREIGN KEY(menu_item_id) REFERENCES menu_item (id)
)
```

**Executed — the whole schema's constraint census:**

```
  TOTAL CHECK constraints across 10 tables: 0
  UNIQUE constraints: bill -> ['visit_id']   (and nothing else)
  UNIQUE indexes:     {}
```

**The only rule LE31's storage layer enforces about a quantity is `NOT NULL`.** For an order line, "not null" is a statement about the *shape of the request*, not about the *meaning of the line*.

### ⭐ Why this is a first-party defect and not a nitpick

**1. A negative quantity is a negative money value, and money is the thing LE31 is most careful about.**

`qty(-5) * unit_price(10.00) = -50.00`. The charter's quality bar says *"Money is `Decimal`, never `float`"* and *"Money sums use `Decimal` arithmetic"* — the whole apparatus exists to make money exact. **But the precision of `-50.00` is not the problem; the sign is.** Feature **411** already proved that LE31's `Decimal` guarantee is a Python-side guarantee the storage layer does not enforce. **This slice is a different failure of the same family, and a cheaper one:** the value is perfectly precise and perfectly wrong.

**2. LE31 has no refund concept, so a negative line is indistinguishable from an unauthorised refund.**

Feature **450** filed, on 2026-11-07, that *"a refund has no payment to be capped against"* — **the refund does not exist.** That is a deliberate gap with a filed plan. **But here is the consequence that the corpus has not recorded:** until 450 lands, **a negative order line is the only way to take money off a bill in LE31**, and it is **completely indistinguishable from an unauthorised refund.** Both are `qty < 0` on an order line. **The system cannot tell the owner which happened.** A defect that removes the boundary between "a mistake" and "an unauthorised transaction" is a money defect.

**3. The charter's P0 promise is a *derived* tip, and a negative line makes the derivation wrong in a direction the operator cannot see.**

The charter's P0 acceptance criterion is that *"tip is **derived** as `total_paid − subtotal_items − subtotal_tax`"*. A subtotal that includes `-50.00` is wrong, and **it is wrong in the direction that makes the bill look smaller** — the direction a human skimming a bill is least likely to catch, and the direction a tipped-over till is most likely to produce. **The owner is the only human check in the system, and this defect is designed to get past them.**

**4. A zero-quantity line is a line that lies.**

`qty = 0` contributes `0.00` to the subtotal and **still** occupies a row, appears on the bill, appears on the kitchen ticket, and appears in every per-dish sales report as **a dish that was ordered**. Feature **19** (menu engineering) and feature **07** (demand estimation) both read order lines to compute per-dish quantities. **A zero line is a phantom sale**: it says the guest ordered the tiramisu, in every report, and contributes nothing to the money.

### ⭐ The corroboration is inside the corpus already

- **Feature 449** — *"the order line's price is mutable in place with no trace"* — owns the column **next to** this one. Its whole argument is that the order line's contents must be traceable and constrained. **The quantity is the other half of the line's value and has neither.**
- **Feature 452** — *"an order line can be served and still say it is new"* — owns the line's `status` against its timestamps. **Again, the same table, the same class of "the line says something untrue".**
- **Feature 449 / 452 / 450 / 456** are, together, **a pattern**: the order line is LE31's central record and **four separate features have been needed to constrain it**. **This one is the fourth.** A reviewer should read them as a family.
- **Feature 404** proves the storage layer enforces **nothing** about values: *"Not one declared type is enforced by the database."* **This slice adds one of the first value rules.**

### Why it lands before the order route ships

The cheapest moment to add a constraint on a column is **before any row exists**. Today the shipped backend has **exactly one router** (`backend/app/routers/tables.py`, with `list_tables` and `seat_party`) and **no order-taking route at all** — `features/02-order-taking.md` describes the intended flow, and the code does not exist. **So the constraint is free today, and becomes a data-migration problem the moment the first order route ships** — because a `CHECK` cannot be added to a table that already holds a zero-quantity row, and a `create_all()`-only deployment would never add it to a live table anyway.

## Data model

**One constraint. No new table. No new column.**

```
  BEFORE (today)
    order_item
      id        INTEGER  primary key
      qty       INTEGER  NOT NULL        <- nothing says this is positive
      ...

  AFTER (this slice)
    order_item
      id        INTEGER  primary key
      qty       INTEGER  NOT NULL
                                     CHECK (qty > 0)     <- or CHECK (qty >= 1)
      ...
```

**Two acceptable implementations, both satisfying the contract:**

1. **`__table_args__ = (CheckConstraint("qty > 0", name="uq_order_item_qty_positive"),)`** on `class OrderItem` — declarative, enforced by the database on both SQLite and Postgres.
2. **A table-level `CHECK` written into the model's `__table_args__` as a raw expression** — equivalent enforcement, same mechanism.

**The contract's requirement, whichever is chosen:**

- **The database refuses an order line whose quantity is zero or negative.** Not the application — the database.
- **The refusal is an `IntegrityError` the write path handles**, and the error **names the dish and the quantity**: *"cannot order tiramisu with quantity -5"* — not a stack trace.
- **A positive quantity is still accepted**, and so is a **large** quantity (there is no upper bound proposed; see *Open questions* 2).
- **No new column is added.** The rule constrains an existing column.

**⭐ The `CHECK` must be a table-level constraint, not a column-level `Field` constraint, and the reason is the 446 problem.** SQLModel's `Field(gt=0)` produces a **Pydantic** validator — it is enforced **in Python, at the model boundary, and only when the model is validated**. It is **not** a database constraint. The charter's truth invariant and feature **404**'s lesson are the same: **a rule enforced only in the application is not enforced against a direct `INSERT`, a migration, a seed script, or a future service.** Feature 455 records the precedent for the declarative form — `__table_args__ = (UniqueConstraint(...),)` — **and this slice uses the same shape with a `CheckConstraint`.**

**Precedent for the enforcement shape:** feature **404** records that LE31 has **no** `CHECK`, no `UniqueConstraint` beyond primary keys and no `STRICT`; feature **455** adds the first `UniqueConstraint`. **This slice adds one of the first `CHECK`s. The precedent must be recorded so 404's contract can point at it** — exactly as feature 400 recorded the same fact.

## Implementation steps

1. **Write the failing test first.** A test that inserts an order line with `qty = 0` and one with `qty = -5`, and asserts each is refused. **On today's code both inserts SUCCEED** — show it succeeding, then show it failing after the fix. **A test that only ever passed proves nothing.**
2. **Decide and record whether zero is allowed** — *recorded default: **not allowed** (`qty > 0`)*. **Record the choice in the code.**
3. **Add the `CHECK` constraint** to `class OrderItem` via `__table_args__` — a `CheckConstraint("qty > 0", …)`. **Do not use `Field(gt=0)` alone**: that is a Python-side validator, not a database constraint. **If a `Field` validator is added as well, it is for a nicer message, not for the rule.**
4. **Handle the `IntegrityError` in the order write path** — with a message naming the dish and the offending quantity. **There is no order route today** (`backend/app/routers/` contains only `tables.py`); if one is being added in the same PR, it must handle it. **If no route exists, the constraint still lands and the handling is deferred to the route's own feature — recorded.**
5. **Update `features/02-order-taking.md`**'s data-model line to state the rule, so the contract and the schema agree.
6. **Add the tests:**
   - `qty = 0` is **refused**;
   - `qty = -5` is **refused**;
   - `qty = 1` is accepted (the default);
   - `qty = 100` is accepted (**no upper bound**);
   - the error message **names the dish and the quantity**;
   - **the constraint is enforced by the database, not only by the model** — a test that issues a **raw `INSERT`** through the SQLAlchemy core and asserts the database refuses it. **This test is the one that distinguishes a real constraint from a Pydantic validator**, and it is the test that makes this slice worth doing.
7. **Record the precedent.** A note that this is **one of the first value-level `CHECK` constraints in LE31's schema**, with a pointer to feature **404** (which owns the `CHECK`/`STRICT` family) and to feature **455** (the first `UniqueConstraint`) so the three do not contradict each other.

## Telegram interaction if any

**None.** This slice touches no bot command and no handler. The cook bot has no order-entry surface — orders are entered by the waiter.

**The one relationship worth stating:** a positive-quantity rule means the kitchen ticket can only carry real dishes. **A zero-quantity line that reaches the cook is a ticket for nothing**, and a negative one is a ticket telling the kitchen to make *minus five* tiramisus. **The bot is the surface that would have to interpret such a line, and it cannot.** **That is a consequence of the defect, not a separate scope, and no bot change is proposed here.**

## Dependencies

- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — this slice is BLOCKED on it.** A `CHECK` constraint is a **table-level change that `create_all()` cannot make on an existing table** — it creates missing tables and never alters an existing one. **446 must land first, or this slice must land in the same PR, or the constraint will be written, merged, deployed, pass its tests, and not exist in the running database.** **This is the upstream-of-filed-work condition in its clearest form**, and 446's own contract names features 408, 415, 420, 421, 435, 438, 439, 442, 443 and 445 as blocked on it — **this feature must be added to that list.**
- **Feature 449 (`le31-order-item-unit-price-is-mutable-in-place-with-no-trace`) — adjacent, not blocking.** It owns `unit_price`. **If 449 and this slice land together, they touch the same class and the same file but different columns** — the two must remain separately reviewable.
- **Feature 452 (`le31-an-order-line-can-be-served-and-still-say-it-is-new`) — adjacent, not blocking.** It owns `status` against the timestamps.
- **Feature 450 (`le31-a-refund-has-no-payment-to-be-capped-against`) — adjacent, not blocking, and the closest in spirit.** 450 owns the *refund concept*. **This slice owns the *absence of ambiguity* between a negative line and a refund.** **They must not be merged** — 450 is about a payment to cap against; this slice is about a quantity that must be positive. **When 450 lands, this constraint must be revisited:** if refunds are modelled as negative order lines, this rule would block them. **That interaction must be recorded when 450 is implemented, and it is a reason to land 450's design first if it is close.**
- **Feature 404 (`le31-sqlite-tables-not-strict`) — adjacent, not blocking.** 404 owns the *shape* checks; this slice owns a *value* check. **They are separate slices.**
- **Feature 435 (`le31-bill-records-no-which-lines-it-charged`) — a consumer, not a dependency.** 435 will compute `subtotal_items` from the lines. **This slice makes each line's quantity well-formed; 435 makes the subtotal auditable.** Both are needed; neither replaces the other.
- **Feature 411 (`le31-money-precision-declared-not-enforced`) — adjacent, not blocking.** 411 owns the *precision* of money; this slice owns the *sign* of a quantity. **A value can be perfectly precise and perfectly wrong** — `999.00` passes 411's rule and is still the wrong tip (that is feature 457).

## Open questions

1. **Is zero allowed?** *Recorded default: **no** — the rule is `qty > 0`.* The argument for excluding zero is that a zero-quantity line occupies a row, appears on the bill and on the kitchen ticket, and contributes nothing to the money — **it is a line that says "ordered" and means "none".** The argument for allowing zero is that *"we will decide the quantity at the table"* is a real hospitality pattern for tasting portions. **Owner decision; the implementer records it.**
2. **Is there an upper bound on a single line's quantity?** *Recorded default: **no**.* A table might order 60 covers of the same dish. **A maximum would need to be a product decision and a wrong maximum would refuse a legitimate large order.** **Not decided here.**
3. **Does the rule apply to a `cancelled` line?** *Recorded default: the rule applies to every row, regardless of `status`.* A cancelled line should be **removed or zeroed by the cancellation path**, not left with a negative quantity — **and the cancellation path is not in scope here.** **Recorded so a later pass does not read the omission as an oversight.** Feature **37** owns the void-rationale concept.
4. **Should the constraint be a `CHECK` on `qty` alone, or should it also relate to the line's total?** *Recorded default: `qty` alone.* The line's total is `qty * unit_price`, which is a **derived** value — **and `unit_price` is mutable in place (feature 449)**, so a constraint relating two mutable quantities would be false as soon as either moved. **Feature 449 owns that column.**
5. **Does the constraint apply to the ledger?** *Recorded default: **no**.* `StockEntry.qty_delta` is **legitimately negative** — a sale consumes stock. **Do not add a sign constraint to the ledger.** **This is the single most likely way for this slice to be implemented wrongly, and it is called out here on purpose.**

## Why this matters

**Because a restaurant's bill is a promise about what was ordered, and LE31 lets the system promise less than nothing.**

Every other rule in LE31 about a quantity is about the *stock ledger*, where a negative delta is meaningful and correct. **The bill line is the opposite: a negative quantity there is not a semantic, it is a subtraction from what the guest owes** — and LE31 has no way to tell it apart from an unauthorised refund, because the refund does not exist yet.

**The cost of the defect is not a crash.** It is a bill that is wrong in the direction that looks smallest, a kitchen ticket for a dish nobody ordered, and a per-dish sales report that counts a dish as sold when the guest took none of it. **The line is silent.** And the owner — the only human check — reads bills quickly and from the total, where a `-50.00` line is one line among several.

**The cost of the fix is one `CHECK`.** One constraint, one error message, one test that proves the *database* refuses it rather than the application. **And today it is free**, because **no order route exists** — the constraint can be added before the first order line is ever written. **After the order route ships, it becomes a data-migration problem.** The whole value of this slice is that it is cheap **now** and expensive later.

**It is also the fourth rule on the same table.** Features 449, 452, 450 and 456 between them constrain what an order line may say. **That is not four unrelated problems — it is one table that was never given a contract.** This slice adds the piece that makes the line's *value* well-formed, next to the pieces that make its *price*, its *state* and its *refunds* well-formed.

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`Apurba94/shopdesk`** — MIT ✓ §3.2 strictly-compatible, **★0 / ⒂0 = NO traction evidence in either direction**, **15 KB**, Python (on-stack language), created **2026-11-04** and pushed **2026-11-04** = **in-window by both fields**, README read in full. Its stated rules, verbatim:
  > *"**Bills** with discounts, and loose quantities such as 1.5 kg. Stock falls by itself, and **you cannot sell more than you hold**"*
  > *"App tests run a sale end to end and **confirm that a failed sale changes nothing**, and that **a customer cannot pay more than they owe**."*

  **Recorded because it states the rule this slice is about, in the vocabulary of a small-shop POS that is on LE31's stack**: a quantity that cannot exceed what exists, and a customer who cannot pay more than they owe. **Both are *value* rules enforced at write time, not *shape* rules — exactly the class of rule feature 404 does not cover.**

  **The transferable idea is the discipline of refusing at write time and proving it end-to-end.** **No code is adopted**, and the reason is recorded plainly: its money is held as **whole paisa**, which is a **v2 representation decision LE31 has explicitly deferred** (feature 404 records it), and **★0 / ⒂0 is no traction in either direction.**

- **`kitsboy/slip`** — MIT ✓, **★0 / ⒂0 = NO traction evidence**, 151,716 KB, TypeScript (off-stack), created and pushed in-window. Its README documents an index discipline, verbatim: *"| Index discipline | reserve at invoice creation, release on cancel, burn on display, gap-limit scan (`src/core/indexes.ts`) |"* — **the reserve/release/burn shape is LE31's batch lifecycle**, and **the "gap-limit scan" is the closest analogue to this slice: a quantity checked against a limit before it is used.** **Recorded as vocabulary only; crypto domain, off-stack, no traction.**

**Adjacent first-party work — recorded, NOT picked:**

| Feature | Why it is adjacent and NOT picked |
|---|---|
| **449** `le31-order-item-unit-price-is-mutable-in-place-with-no-trace` | Owns `OrderItem.unit_price`. **Same table, adjacent column, separate slice.** |
| **452** `le31-an-order-line-can-be-served-and-still-say-it-is-new` | Owns the line's `status` vs its timestamps. **Same table again.** |
| **450** `le31-a-refund-has-no-payment-to-be-capped-against` | Owns the refund concept. **This slice makes the absence of refunds visible; it does not fill it.** |
| **404** `le31-sqlite-tables-not-strict` | Owns `CHECK`/`STRICT` — the *shape* family. **This slice owns a *value* rule.** |
| **411** `le31-money-precision-declared-not-enforced` | Owns money *precision*. **This slice owns a quantity's *sign*.** |
| **435** `le31-bill-records-no-which-lines-it-charged` | Owns the missing `Bill → order_item` edge. **This slice owns the shape of one line.** |
| **374** (batch `qty_remaining`) | Owns the derived stock quantity. **A different table, a different question.** |
| **446** `le31-has-no-schema-evolution-mechanism` | **This slice is BLOCKED on it** — a `CHECK` on an existing table is exactly the change `create_all()` cannot make. |

**External source families fetched this pass (all raw, all re-derived from disk by the parent):**

- **GitHub Search** — 14 date-filtered queries + a 4-request qualifier probe, **18/18 HTTP 200**; aggregate `total_count` = **19,648**; **zero** 73-byte or 6-byte stubs; the **correct `pushed:>=` qualifier** was used and the **dead `pushed_at:>=` qualifier was proved dead by a paired probe** (`topic:restaurant` → 2,972; `pushed_at:>=2026-11-01` → **0**; `pushed:>=2026-11-01` → **169**; `created:>=2026-11-01` → **45**). **The restaurant-shaped cluster is ALIVE.** **30 candidates were verified by a direct `GET /repos/{owner}/{repo}`** plus a README fetch: **10 permissive / 20 licence-incompatible**, **30/30 in-window by BOTH `created_at` AND `pushed_at`**, and **every one of the ten permissive candidates carries ★0 or ★1 and ⒂0 — NO traction evidence in either direction.**
- **HN Algolia** — 10 queries, 10/10 HTTP 200, **30 hits**, `title: null` = **0**. **4 of 10 queries genuinely returned `nbHits = 0`** and are reported as counts, not failures. **All 30 hits were read; 0 were promoted to a signal** — the largest bucket (`point of sale`, 17 hits) contains **zero POS items**, and the nearest misses are *"Waiter Making 75K in NJ"* (a person, not software) and a **Roblox food-delivery game**.
- **OpenAlex** — 9 queries, 9/9 HTTP 200, `meta.count` = **611 / 626 / 886 / 56 / 66 / 29 / 57 / 3,113** — **distinct** and none near corpus scale; a diagnostic control query for a nonsense term returned **0**, proving the filter is live. Abstracts were carried as **raw `abstract_inverted_index` dumps**, **never paraphrased**. **0 papers were promoted to a signal** — the family is **soft this pass**.
- **PyPI** — 10/10 HTTP 200; **4 in-window releases** (`fastapi` 0.162.1/0.162.2, `sqlalchemy` 2.0.56/2.1.7/2.0.57/2.1.8, `pydantic` 2.14.3); `sqlmodel`, `aiogram`, `uvicorn`, `alembic`, `httpx` = **0 in-window**. **No pin-bump proposed** — a pin bump needs a CHANGELOG read this pass did not perform.
- **GitHub `release.atom`** — 9/10 HTTP 200, **90 `<entry>` elements**; `sqlmodel/sqlmodel` = **0 entries** (valid empty feed); `python-telegram/bot` = **HTTP 404** (9 B).
- **EU** — 5/5 HTTP 200; ECB daily XML `time='2026-11-06'`, **USD = 1.1165**; CNIL EN/FR RSS 10 items each; **EUR-Lex ELI = HTTP 200 with the real GDPR document**.
- **ScienceDirect** — **NOT RETRIEVABLE** (blocked on this VPS; not attempted).
