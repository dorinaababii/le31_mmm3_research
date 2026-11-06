# Feature 444 — `le31-order-item-unit-price-is-mutable-in-place-with-no-trace`

> **Pick A of Daily Research 2026-11-06 (84th pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, the two price columns, verbatim:
>
> ```python
> class MenuItem(SQLModel, table=True):
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)
>
> class OrderItem(SQLModel, table=True):
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)
> ```
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite DB, then real inserts and real `UPDATE`s):
>
> ```
>   line created at 2.50, qty 2  ->  line total 5.00
>   UPDATE order_item SET unit_price = 1.00 WHERE id = :id
>   ACCEPTED (no error, no constraint, no trigger)
>   line price after the overwrite        -> 1.00
>   line total after the overwrite        -> 2.00   (was 5.00)
>   audit rows written by the overwrite   -> 0
>   original 2.50 recoverable from schema -> false
>   menu price (unchanged by the line)   -> 2.50
>   UPDATE menu_item SET unit_price = 99.00  -> ACCEPTED silently
> ```
>
> **The full schema, enumerated by execution** — `app_user, batch, bill, derived_tip, menu_item, order_item, shift, stock_entry, table_, visit` — contains **no price-change table, no audit table and no history table of any kind.** The ten tables are the entire database.
>
> **Evidence class: OBSERVED** (every claim below is a reproducible execution against LE31's own schema). **Confidence: high** — the defect is a missing column and a missing table, not an inference.
>
> **Bucket: v1.** **Build verdict: `build`.**

## Goal

Make an order line's price **a fact that can be explained after the fact**, instead of a mutable column whose earlier value is gone forever.

Concretely, three things:

1. **An append-only record of every price change** — what the price was, what it became, who changed it, and when.
2. **A price change that is a first-class operation**, not an `UPDATE` — the write path that changes a line's price writes a record.
3. **A current price that is unambiguous** — the line's price is always the current price, and its history is always available.

**No change to the shape of `OrderItem.unit_price`.** It stays a `Decimal` snapshot of what the line was sold at. This feature adds the *history* that makes the snapshot trustworthy.

## Scope

- Add an **append-only price-change record** to the schema.
- Add the **one helper** that changes an order line's price, and make it the **only** supported way to do so.
- Record, for every change: the order line, the previous price, the new price, the actor, and the instant.
- Add the **read path** that answers *"what did this line cost, and when did it change?"*.
- A **regression test** for each scenario in the table below.

## Out of scope (v1)

- **Discounts, promo codes, and comps as a separate model.** A discount is not a rewritten price — it is a discount with its own reason. Feature **05** owns the discount vocabulary; this feature records the *price change*, whatever the caller called it. **A caller that wants a discount must eventually write a `Discount` row; this contract does not introduce one.**
- **The bill-close route.** Feature **415** owns `backend/app/routers/bills.py` and the bill-closes-visit edge.
- **The bill's membership of lines.** Feature **435** owns *which lines a bill charged*; this feature owns the *history of each line's price*.
- **The tip formula and the money rules.** Features **408** (tax rate home), **410** (two rule sources), **411** (Decimal guard) and **420** (tendered vs received) are all unaffected and are read, not changed.
- **`OrderItem` *status* transitions.** Feature **379** owns the transition log and its actor; a status change and a price change are **two different events** and get **two different records**.
- **The menu price's own history.** The menu is *configuration*; a changed menu price is a catalogue edit, and the catalogue has no write path today. This feature records the **line's** price. (The menu-price overwrite is recorded below as an adjacent observation, not a pick.)
- **Any guest identity.** The actor is a **staff** member (`app_user`), never a guest. This is consistent with charter §3.1 (v1 stores counts, not guest identities).
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the defect

LE31 has **two** price columns and they mean different things:

- `MenuItem.unit_price` — the **current catalogue price**. Configuration.
- `OrderItem.unit_price` — the **price this line was sold at**. A snapshot, and the input to the bill total that feature 415 derives as `SUM(order_item.unit_price * order_item.qty)`.

The snapshot behaviour is correct and it is **not** the defect. Executed: the menu price moved from 2.50 to 3.00 and the line kept 2.50 — exactly right.

**The defect is that the snapshot has no writer that is safe.** The line's price is a plain mutable column. A `UPDATE` against it is accepted, unlogged and unrecoverable — and the bill is derived from whatever the number is at the moment it is derived.

### Why "the line snapshots the price" is the plausible wrong answer

This is **the** quiet wrong answer, and it is worth stating precisely because it is true:

> *"The line snapshots the price, so the price cannot drift."*

**True today** — and **silently irrelevant the moment anyone changes the line's price.** The snapshot protects against a **later change to the menu**. It says **nothing** about a change to the **line itself**. The two events are different, and only one of them is defended:

| Event | Defended today? | Evidence |
|---|---|---|
| Menu price changes after the line was taken | **Yes** | the line keeps the old value |
| Line's own price is changed | **No** | `UPDATE` accepted, no record, old value gone |

And the events are **not** hypothetical for a small restaurant. A comp, a correction, a price the waiter typed wrong, a goodwill round-down on a long tab, a partial refund that re-prices the line — **every one of them rewrites the number**, and **every one of them is silent**.

### The cost of getting it wrong

The bill is a **derivation**, not a record. Feature 415 computes `subtotal_items` from the lines and **forbids the caller from setting it**. That is the right design — and it means the **lines are the only place the money is written down**. So a wrong line price is:

- **not** an error at bill time — the bill faithfully derives a wrong total;
- **not** detectable later — there is no history to compare against;
- **not** attributable — there is no record of who did it.

A restaurant that discovers a mispriced bill has **no way to answer** *"was this a comp, a typo, or a mistake?"* — and, having no history, **has no way to correct the record either** without overwriting the evidence.

### The third-party instrument

`yixin-lot/posd` (Apache-2.0 ✓ §3.2, Go + SQLite, created **and** pushed 2026-11-05/2026-11-06 — **in-window by both fields**, ★0/⑂0, 755 KB, `archived=false`, `fork=false`; all fields read from a direct `GET /repos/`). Its README, verbatim (`readme/yixin-lot__posd.md`):

> `| 订单 | 挂单取单、抹零、改价（审计）、按件退款、整单作废、退款原路 |`
> (*order* column: *hold-order/pick-up, round-down, **price change (audited)**, per-item refund, whole-order void, refund to original route*)

**The vocabulary is the transfer, not the code.** `改价（审计）` — *price change, audited* — treats a price change as an **operation with a record**, not an edit. LE31's `UserRole` enum and SQLModel stack can express exactly that; the Go/SQLite implementation is irrelevant.

The same README's `后厨单不印价格` — *the kitchen ticket does not print prices* — is a **companion** observation recorded in *Adjacent evidence*, not part of this contract.

## Data model

**New table** — append-only, never updated, never deleted:

```python
class OrderItemPriceChange(SQLModel, table=True):
    """Append-only history of every change to an order line's price.

    The CURRENT price remains OrderItem.unit_price. This table is the history
    of how it got there. Never UPDATE or DELETE a row here.
    """
    __tablename__ = "order_item_price_change"

    id: int | None = Field(default=None, primary_key=True)
    order_item_id: int = Field(foreign_key="order_item.id", index=True)
    from_price: Decimal = Field(max_digits=10, decimal_places=2)
    to_price: Decimal = Field(max_digits=10, decimal_places=2)
    reason: PriceChangeReason
    by_user_id: int = Field(foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

**New enum** — deliberately small. The reason is a **label on an operation**, not a money rule:

```python
class PriceChangeReason(str, Enum):
    correction = "correction"   # the price was wrong and is being fixed
    comp        = "comp"         # goodwill, no charge
    discount    = "discount"     # a reduction was applied (feature 05 owns the discount model)
    round_down  = "round_down"   # a rounding adjustment
```

> **Open question, recorded not guessed:** whether `discount` belongs in this enum at all, given that feature 05 owns the discount model. The recommendation is to **include it as a label only** — the *discount itself* is feature 05's, and this enum says nothing about its amount or its eligibility.

**No change to `OrderItem`.** `unit_price` stays exactly as it is: a `Decimal` snapshot of the current price.

**No change to `MenuItem`, `Bill`, `DerivedTip`, `StockEntry` or `Visit`.**

**No `StockEntry` row is written by a price change.** The ledger records *quantity*, not price. A price change moves no stock. `test_price_change_writes_no_ledger_row` enforces it.

**Money is `Decimal`, never `float`,** per charter §7. The two price columns carry the same `max_digits=10, decimal_places=2` as every other money column in the schema.

## Implementation steps

Dependency-ordered; each task is independently verifiable.

1. **Model + migration.** Add `OrderItemPriceChange` and `PriceChangeReason` to `backend/app/models.py`. Register the new enum member set. **This step also depends on feature 446** (the schema-evolution mechanism) for anything beyond `create_all()` — see *Dependencies*.
2. **The one helper.** `backend/app/services/order_prices.py` (new module) with:
   ```python
   def change_order_item_price(
       session: Session,
       order_item: OrderItem,
       *,
       new_price: Decimal,
       reason: PriceChangeReason,
       by_user_id: int,
   ) -> OrderItemPriceChange:
       """The ONLY supported way to change an order line's price.

       Writes the append-only price-change row and sets order_item.unit_price
       in the SAME transaction. If either fails, neither happens.
       """
   ```
   It must: validate `new_price` is a non-negative `Decimal`; **reject a change where `new_price == order_item.unit_price`** (a no-op is not a change — it is a bug in the caller); write the history row; set `unit_price`; commit both together.
3. **A `Decimal` guard.** Reject a `float` argument explicitly. `Decimal` from a `float` silently carries the float's error, and this is money. Feature 411 owns the general `Decimal` precision guard — **read it, do not duplicate it**; this helper calls it if it exists, and asserts `isinstance(new_price, Decimal)` if it does not.
4. **The read path.** `GET /orders/{visit_id}/items/{item_id}/price-history` (or the equivalent service function if no order router exists yet — **see *Sequencing***), returning the line's current price and its ordered history.
5. **Tests.** One test per row of the table below, plus the two no-ledger-row tests.
6. **Documentation.** A short note in `backend/app/README.md` (or the module docstring) stating the rule in one line: **`OrderItem.unit_price` is changed only through `change_order_item_price`.**

### Sequencing — this must land WITH the first order write path

**There is no order-taking router today** (`backend/app/routers/` contains exactly `__init__.py` and `tables.py`). So **there is no write path that sets a line price** — which means this feature is currently **inert**: nothing can call the helper yet.

**That is the reason to land it now, not later.** The moment a write path that can set a line price exists, the price becomes mutable in place. The helper must be **the way that path is written**, or the guarantee is lost on day one.

### The scenario table (each row is a test)

| Scenario | Expected |
|---|---|
| A line is taken at 2.50; the menu price changes to 3.00 | the line stays **2.50**; **no** price-change row (the menu is not the line) |
| The line is changed from 2.50 to 1.00 with reason `correction` | one row: `from_price=2.50`, `to_price=1.00`, actor, timestamp; `order_item.unit_price == 1.00` |
| The line is changed twice | **two** rows, ordered; the first row's `to_price` equals the second's `from_price` |
| The change is attempted with `new_price == current price` | **rejected** — no row, no change |
| The change is attempted with a `float` | **rejected** — no row, no change |
| The change is attempted with a negative price | **rejected** — no row, no change |
| The change is attempted with a nonexistent actor | **rejected** — the FK protects it |
| The history is read for a never-changed line | the current price and an **empty** history — not an error |
| **A price change is performed** | **no `StockEntry` row is written** |
| **A price change is performed** | **no `Batch` row and no `Batch.qty_remaining` change** |
| The bill is derived after a price change (feature 415) | the bill uses the **new** price — the history does not change the derivation |
| A second user changes the same line | both changes are recorded, in order, with distinct actors |

## Telegram interaction if any

**None.** The price change is made on the **waiter web UI** (the surface the order is taken on). This feature adds a **server-side rule and a history**, not a Telegram surface.

**If** the cook bot ever needs to *see* the current price of a line, it reads `OrderItem.unit_price` as it does today — **unchanged**. **If** the cook bot ever needs to *change* a price, that is a **separate decision** and is explicitly not in this contract: a cook changing prices is a role-policy question (feature **403** owns role policy).

## Dependencies

- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — HARD dependency for the production database.** Adding a table works with `create_all()`; changing an existing table does not. **446 must land first**, or the new table must be created by hand on the production database (which is exactly the silent-no-op failure 446 exists to prevent).
- **Feature 415 (bill closes visit)** — reads the lines; **unaffected** by this feature, but the acceptance path for the bill row in the scenario table requires 415's derivation to exist.
- **Feature 435 (bill-line membership)** — unaffected; reads the lines.
- **Feature 379 (order-item transition actor)** — **adjacent, not a dependency.** 379 owns *status* transitions and their actor; this feature owns *price* changes and their actor. They may share a convention for "the actor of an order-line event", but **379 must not be modified by this feature** and this feature must not modify 379's log.
- **Feature 411 (Decimal precision guard)** — **read and reuse**; do not re-implement a second guard.
- **Feature 05 (payment / tip reconciliation)** — owns the discount *model*. This feature only labels a change `discount`.

## Open questions

1. **Is `discount` a member of `PriceChangeReason`, or should a discount take a completely separate path?** The recommendation is to include it as a **label only**, because feature 05 owns the discount model — but the owner should confirm that a `discount`-labelled price change is acceptable as an interim state, or whether feature 05 must land first.
2. **Who may change a price?** Every role? Only a manager? This feature **records** the actor but does **not** restrict who may act — that is feature **403**'s role policy. **Recorded as an owner decision, explicitly not made here.**
3. **Can a price be changed after the bill is paid?** The recommendation is **no** — a closed bill is a closed fact, and feature 415 owns the close. **Recorded as an open question because it is a money rule, and the money rules are the owner's.**
4. **Is `round_down` a distinct reason, or is it a `discount`?** It was observed in `posd`'s feature list as `抹零` alongside `改价（审计）`. The recommendation is to keep it distinct because it is the one rounding-shaped reason the charter's §7 "money rounding rules" mentions — but **the rounding mode itself is feature 408's.**
5. **Should the history be exposed on the waiter UI as well as the API?** The recommendation is API-only for v1.

## Why this matters

**Because the number the customer is charged comes from this column, and the column can be rewritten with nothing left behind.**

The bill in LE31 is a **derivation**, by design and correctly so — feature 415 forbids the caller from setting the subtotal, and computes it from the lines. **That design makes the lines the only place the money is written down.** It also means the line's price is the *single point of failure* for the whole money path, and it is a **plain mutable column with no writer and no history**.

The cost of the gap today is **zero**, because there is no order flow. The cost the day there is one is **permanent**: a wrong line price is **indistinguishable from a right one** once the bill closes, because the record of the change does not exist. This is the same shape as the defects the recent passes have been finding in the stock domain — **the ledger is append-only and audited; the price is not.** LE31's own `StockEntry` docstring says *"Never UPDATE or DELETE rows"*; `OrderItem.unit_price` says nothing and means the opposite.

**And it is cheap now.** One table, one helper, one call site — three to five hours. **Expensive after:** the first bill that closes over a rewritten price is indistinguishable from a correct one, forever, and the restaurant has no ground truth to audit against.

## Adjacent evidence

- **`yixin-lot/posd`** (Apache-2.0, Go + SQLite, in-window by both fields) — `改价（审计）`, the price-change-with-audit mechanism. **Vocabulary only; off-stack.**
- **`FreeOpenSourcePOS/FloCafe`** (MIT) — *"Granular roles & permissions: Owner, Manager, Cashier, Server, and Chef roles with context-aware access policies"* — the *who-may-change* question is recorded in *Open questions*, not answered here.
- **`asimhashmi47/DineSync`** — *"an audit log of sign-ins, voids, refunds, discounts, price changes, settings changes and exports"* — the same primitive, recorded in a peer.
- **`Raktim94/nodedr-restaurant-pos`** (AGPL-3.0 — licence-blocked) — *"Money balances are `set`, never `increment`"*, already filed as **feature 433**. **Not re-picked.** Its *"never blocks a sale on a stock shortfall"* rule concerns stock, not price.

## Adjacent work — recorded, NOT picked

- **The menu's own price has no history either.** Executed: `UPDATE menu_item SET unit_price = 99.00` was accepted silently. The menu is *configuration* and has no write path today, so this is a smaller problem than the line's price — but it is the same shape and it is **recorded here, not picked**.
- **`posd`'s `后厨单不印价格`** — *the kitchen ticket does not print prices*. LE31's cook bot receives an order; whether it shows the price is a **surface** question with a **privacy** dimension (a cook does not need the price to cook the dish). **Recorded, not picked — no ticket-printing surface exists.**
- **A `round_down` operation** — `posd`'s `抹零`. The rounding *mode* is feature 408's; the *operation* is not modelled in LE31. **Recorded, not picked.**
