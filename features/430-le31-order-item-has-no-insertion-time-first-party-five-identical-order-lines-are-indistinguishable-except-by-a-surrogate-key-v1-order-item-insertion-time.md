# Feature 430 — `order_item` cannot record **when a line was added**: five identical lines are indistinguishable except by a surrogate key

> **Pick B of Daily Brainstorm 2026-11-03 (97th pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proven by EXECUTION, not by reading.**
>
> `backend/app/models.py`, `class OrderItem` (lines 142-155), verbatim:
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
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then five real inserts through SQLModel):
>
> ```
>   orderitem_columns            [id, visit_id, menu_item_id, qty, unit_price,
>                                course, status, notes, fired_at, ready_at, served_at]
>   orderitem_has_insertion_time False
>   orderitem_timestamps         [fired_at, ready_at, served_at]
>
>   five identical order lines:
>     {"id":1,"qty":1,"unit_price":"8.80","notes":null,"course":null,"status":"ItemStatus.new","fired_at":"None"}
>     {"id":2,"qty":1,"unit_price":"8.80","notes":null,"course":null,"status":"ItemStatus.new","fired_at":"None"}
>     {"id":3,"qty":1,"unit_price":"8.80","notes":null,"course":null,"status":"ItemStatus.new","fired_at":"None"}
>     {"id":4,"qty":1,"unit_price":"8.80","notes":null,"course":null,"status":"ItemStatus.new","fired_at":"None"}
>     {"id":5,"qty":1,"unit_price":"8.80","notes":null,"course":null,"status":"ItemStatus.new","fired_at":"None"}
>
>   distinct_row_ids     5
>   distinct_payloads    1      <-- every line has the SAME content
>   per_line_timestamps  all three of fired_at/ready_at/served_at = None
> ```
>
> **The three timestamps `order_item` does have are null until the line has been fired.** They record *kitchen* milestones, not *insertion*. A waiter who adds a line and the cook who receives it are two different moments, and LE31 keeps only the second.

## Goal

**Give `order_item` a truthful, non-nullable record of when the line was added to the visit — and make the derivation of the bill's line order stop depending on a surrogate key.**

Concretely: `order_item` gains one insertion-time column, and the code that lists a visit's lines in the order they were added can do so **without** relying on `id` being monotonic.

## Scope

- **`backend/app/models.py` — `class OrderItem`:** add an insertion-time column.
- **Any code that orders a visit's lines.** As of this pass, `backend/app/routers/` contains only `__init__.py` and `tables.py`, and `backend/app/bot/` contains only `cook_bot.py` — **no orders router exists yet**, so there is currently no production ordering site to change. This contract therefore creates the column and the **helper** the future router will use; it does not invent a router.
- **The `fired_at` / `ready_at` / `served_at` trio is NOT touched.** They remain the kitchen's milestones.
- The **relationship between this contract and feature 429** is load-bearing and is stated in *Dependencies* and in the Open questions: **429 owns the schema-wide `created_at` convention; 430 owns the *meaning* of an order line's insertion time.** If 429 lands first and adds `created_at` to `order_item`, **430 must not add a second, competing column** — it must decide whether `created_at` *is* the answer.

## Out of scope (v1)

- **Adding an `order_items` router, or any write path.** There is none today. **This contract adds a column and a helper; it does not create the feature that would fill it.** Creating the router is a separate contract.
- **Firing, readying or serving a line.** That is **feature 379** (order-item transition attribution) and the `ItemStatus` transition family.
- **Changing `ItemStatus`**, its five members, or the fact that `status` defaults to `new`.
- **A course/sequencing model.** `OrderItem.course` exists as a free-text column but **the charter never mentions "course" at all** — sequencing is out of scope by the charter's silence, and is deliberately **not** picked.
- **Any `created_at`/`updated_at` on the other nine tables.** That is **feature 429**.
- **Any change to `Bill`, `Bill.total_due`, or how the bill is derived.** The bill's derivation is **feature 05 / feature 415**'s territory.
- **Backdating existing rows.** No historical insertion times exist.

## Description

### What the schema actually is

`order_item` is the **line** on a visit. It has eleven columns:

| Column | Meaning | Set when |
|---|---|---|
| `id` | autoincrement surrogate key | insert |
| `visit_id` | FK → `visit.id` | insert |
| `menu_item_id` | FK → `menu_item.id` | insert |
| `qty` | how many | insert |
| `unit_price` | the price charged | insert |
| `course` | free text (`appetizer / main / dessert`) | insert (nullable) |
| `status` | `ItemStatus` enum, defaults `new` | insert (default) |
| `notes` | free text | insert (nullable) |
| `fired_at` | the kitchen milestone | **later — null until fired** |
| `ready_at` | the kitchen milestone | **later — null until ready** |
| `served_at` | the kitchen milestone | **later — null until served** |

**There is no column that records the moment the line was added.** The three nullable timestamps are all *downstream* of the line's life and all start at `None`.

### The specific harm: two lines differing only in *when* are the same row

The execution above inserted five lines with identical content — same item, same quantity, same price, same null notes, same null course, same default status — and got back **five distinct ids and exactly one distinct payload**. There is nothing in the row that says *"this one was added first."*

The only thing that separates them is `id`, and `id` is a **surrogate key**:

- It is **not a business fact.** It says nothing about when the guest asked for the tiramisu.
- It is **not guaranteed monotonic.** A Postgres sequence reset, a restore from backup, or a bulk data migration can renumber rows. A sequence is an allocation counter, not a clock.
- It is **not unique to the visit.** `id` is global; the ordering a waiter needs is *within one visit*.

So the ordering of a visit's lines is, today, **an accident of allocation order**. For the first five lines of a visit, that accident is usually right. It is right *by luck*, not by construction — and it is exactly the kind of luck that survives until the first backup-restore, then silently changes the order of a guest's courses.

### The business consequence

Three concrete things LE31 cannot answer today:

1. **The bill's line order.** `Bill.subtotal_items` is a total, not a sequence — but a receipt, a kitchen ticket and a "what did we serve, in what order" question all need the sequence. `bill_has_no_link_to_order_items` = **true** (proved by execution): the bill does not reference its lines at all, so the link must be made through `visit_id`, and the *order* within it must come from a column that does not exist.
2. **"Which line was this waiter looking at a moment ago?"** The waiter surface polls (§3.2 defers WebSockets). Between polls, a line can be added and fired. Without an insertion time, the kitchen's `fired_at` and the waiter's add-moment are on different scales and cannot be reconciled.
3. **The kitchen's "what's oldest?" queue.** A cook looking at a screen wants the *oldest unfired line first*. Today the only ordering available is `id` — see above.

### The sibling finding this is *not*

**Feature 392** made the same *shape* of point on a **different axis**: two order lines for the same item, one sold by slice and one by tray, are **indistinguishable** because `OrderItem` records no unit. That is the **quantity** axis.

**This contract is the TIME axis.** They are complementary, not duplicate: a line can be perfectly distinguishable by unit (feature 392's fix) and still be unorderable by time (this one). Feature 392's contract states the fix is *`MenuItem.unit` meaning*, not an `order_item` column — so the two do not collide.

### The third-party instrument

`Damar2121/laravel-pos-booking` (NexPOS) (MIT ✓ §3.2, ★2/⑂0 — **no traction evidence**, PHP/Laravel 12 + Filament — **off-stack**, created 2026-11-01 **AND** pushed 2026-11-01 = **IN-WINDOW BY BOTH FIELDS**, 136 KB, all fields parent-verified via direct `GET /repos/`). Its README, verbatim:

> *"Displays store details, **transaction timestamp**, cashier name, customer name, **line item subtotals**, tax/discounts, and change returned."*

The transferable observation is narrow and precise: **a receipt prints a transaction timestamp.** A receipt is, among other things, a *record of when each line was added* — the guest's experience of the meal has an order, and the artefact that survives the meal preserves that order. LE31's `order_item` is the row that receipt is built from, and it keeps no time.

The same README states, verbatim: *"**Inventory Safety Checks:** Prevents overselling by automatically validating warehouse physical stock."* That is the **read-side** counterpart to the ledger: validate before you sell. LE31's own answer to that is **feature 404** (null-safe active-batch predicate) and **feature 417** (the actor FK) — **both filed.**

## Data model

```python
class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"

    id: int | None = Field(default=None, primary_key=True)
    visit_id: int = Field(foreign_key="visit.id", index=True)
    menu_item_id: int = Field(foreign_key="menu_item.id")
    qty: int = 1
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    course: str | None = None  # appetizer / main / dessert
    status: ItemStatus = ItemStatus.new
    notes: str | None = None
    added_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
    fired_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    ready_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    served_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
```

**`added_at` is the column this contract exists to create.** It is:

- **non-nullable**, `default_factory=utcnow`, `DateTime(timezone=True)` — matching the file's existing timestamp wiring exactly (`batch.prepared_at`, `visit.opened_at`, `stock_entry.at`);
- **UTC**, per the file's own line 8 convention and charter §7 (*"Time is UTC"*);
- **distinct in meaning from `fired_at`**: `added_at` is when the guest asked; `fired_at` is when the kitchen started it. **Both are facts and both are kept.**

### The relationship to feature 429 — decide once, record it

| If | Then |
|---|---|
| **429 lands first** and adds `created_at` to every table | **430 must NOT add `added_at`.** `created_at` **is** the insertion time; 430's remaining work is the **helper** below and a note that `order_item.created_at` is the ordering column. |
| **430 lands first** | 430 adds `added_at`. 429 must then **not** add `created_at` to `order_item`, and must name `order_item` as an exception in the docstring — or, better, **429 adopts `added_at` as `order_item`'s creation time** and the docstring says *"tables carry `created_at` except `order_item`, which uses `added_at`."* |

**Whichever lands first, the second one must be adjusted.** Two competing insertion-time columns on one table is a defect, not a redundancy.

### The ordering helper

Because there is no orders router yet, this contract ships the **helper** the future one will use, so the ordering rule is written down once and in one place:

```python
# backend/app/services/order_service.py   (new)
def lines_for_visit(session, visit_id) -> list[OrderItem]:
    """The visit's lines in the order they were added."""
    return list(session.exec(
        select(OrderItem)
        .where(OrderItem.visit_id == visit_id)
        .order_by(OrderItem.added_at, OrderItem.id)   # id is the TIE-BREAK, not the order
    ))
```

**The tie-break is the point.** `added_at` orders the lines; `id` only breaks ties between lines added in the same instant. **A single-column order by `id` is what this contract replaces.** Note that `backend/app/services/` **does not exist yet** in this repo — creating it is part of this contract (feature 374 also expects a `services/` directory to appear; that is fine, they can share the package).

## Implementation steps

1. **Resolve the 429/430 ordering first** — read `features/429-…` and decide which column ends up on `order_item`. **Record the decision in the commit message.** Do not end up with both `created_at` and `added_at` on `order_item`.
2. Add the insertion-time column to `class OrderItem` in `backend/app/models.py`, following the file's existing timestamp pattern.
3. Create `backend/app/services/__init__.py` and `backend/app/services/order_service.py` with the `lines_for_visit` helper above.
4. Per charter §3.2, v1 uses **`init_db()`**, **not** Alembic. For an existing dev database, drop and re-create; record the prod-migration step as **known debt**.
5. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:
   - `test_order_item_records_an_insertion_time` — a newly inserted line has a non-null insertion time, and it is **UTC**.
   - `test_order_item_insertion_time_is_independent_of_id_order` — insert three lines **with explicit, deliberately reversed** insertion times and assert the helper returns them in **insertion-time order, not id order**. **This is the test that would have caught the bug**, and it must fail on the unfixed code.
   - `test_order_item_has_no_second_insertion_timestamp` — assert `order_item` does **not** carry both `created_at` and `added_at`. (This is the guard against the 429/430 collision.)
6. **Do not** add an orders router, and do not write any `OrderItem` row outside the existing test path — there is no production write path today and this contract does not create one.

## Telegram interaction if any

**None.** The column is written by whatever writes an order line; the waiter's *"add to order"* gesture already implies the moment. **No new command, no new button.** The kitchen surface's *"oldest first"* ordering (a future feature) is the **consumer** of this column, not part of this contract.

## Dependencies

- **Charter §7** — *"Time is UTC. `datetime.now(timezone.utc)` everywhere."*
- **Charter §3.2** — `init_db()` for v1; **no Alembic**; no new dependency.
- **`le31-conventions`** — the seven-check feature gate and the hard invariants.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done*.
- **`le31-handoff-spec`** — the frozen-contract discipline.

**Nearest siblings — read these so this slice does not open them:**

- **`features/429-…-v1-schema-creation-timestamp-convention.md`** — **the closest sibling in the whole corpus; it touches the same table.** Read it first; the two must not both add a creation-time column to `order_item`.
- **`features/379-…-v1-order-item-transition-attribution.md`** — owns the **state transition** and the missing actor field on the transition. `fired_at` and `status` are **its** territory; this contract adds only the insertion time and does not move the transition.
- **`features/392-…-v1-menu-item-unit-meaning.md`** — the sibling finding on the **quantity** axis. Complementary, not duplicate.
- **`features/385-…-v1-batch-selection-and-sale-provenance.md`** — owns the **batch** reference from an order line (`StockEntry.ref_order_item_id`). It quotes `order_item`'s exact column list; read it so the column list stays consistent.
- **`features/404-…`** and **`features/417-…`** — the ledger-side counterparts (null-safe active batch, actor FK). **Filed.**
- **`features/415-…-v1-bill-closes-visit-edge.md`** — owns the bill ↔ visit edge and the missing `bills.py`. This contract does **not** touch the bill path.

## Open questions

1. **Should the column be named `added_at` or should `created_at` (feature 429's convention) serve?** **Default recorded: `added_at`**, because the name carries the *meaning* — a guest's add-moment is not a row's creation moment, and the distinction matters when the two are eventually written by different code paths (e.g. a retroactive order entered by a manager). **The alternative — `created_at` — is acceptable if 429 lands first and 430 adjusts.**
2. **What is the tie-break when two lines share an insertion instant?** Two lines added in the same millisecond are plausible on a fast tap. **Default recorded: `added_at, id`** — a deterministic, stable order. The helper already does this.
3. **Does a line added and then removed need an insertion time?** LE31 has no order-line deletion (charter §4.3 makes the *stock ledger* append-only; nothing says order lines are). **Default recorded: this contract does not decide that.** If a line can be removed, its *removal* time is a separate question — and a separate contract. **Recorded, not answered.**
4. **Should `course` become a real ordering dimension?** It is free text today and the charter never mentions it. **Default recorded: no — out of scope by the charter's silence.** Recorded here so a later pass does not re-litigate it inside this slice.

## Why this matters

**⭐ The thing a guest actually notices about a meal is its order, and LE31 cannot record it.**

Five identical lines produce five identical rows. The only thing that orders them is an autoincrement counter that happens to increment. On a quiet Tuesday that is always right. **On the first restore-from-backup, the first sequence reset, or the first data migration, the order of a guest's courses can change without a single error being raised** — and the receipt will print the courses in the wrong order with total confidence.

**⭐ This is the same class of defect LE31 already found twice, on a third axis.** Feature 392 found that two lines differing only in **unit** are indistinguishable. Feature 385 found that a line has no **batch** reference, so the sale cannot be traced to what it consumed. This pass finds that two lines differing only in **time** are indistinguishable. The pattern is worth naming because it is a property of the schema, not of any one feature: **`OrderItem` records what the line *is*, and has never recorded *when it happened*.** The kitchen timestamps (`fired_at`, `ready_at`, `served_at`) are the closest thing, and they are **half the story** — they start at `None` and only fill in once the line reaches the kitchen, which is precisely the window in which the ordering question is most urgent.

**⭐ And the fix is one column plus one helper — the smallest possible change that makes a real fact true.** One non-nullable UTC column, populated by the database, and a helper whose ordering rule is `added_at` with `id` only as a tie-break. **The tie-break is the contract:** it states that the ordering comes from a *fact about the business* and not from an *accident of allocation*. That single change converts an implicit assumption into a guaranteed property, which is what the rest of LE31's schema — the ledger, the FKs, the `Decimal` money — is built to do.

## Adjacent evidence

**Third-party instrument — `Damar2121/laravel-pos-booking` (NexPOS)** (MIT ✓ §3.2 STRICTLY-COMPATIBLE, ★2/⑂0 — **NO traction evidence in either direction**, 136 KB, **PHP/Laravel ✗ OFF-STACK** (Laravel 12 + Filament + Livewire + `spatie/laravel-permission`), created 2026-11-01 **AND** pushed 2026-11-01 = **IN-WINDOW BY BOTH FIELDS**, `default_branch=main`, `archived=false`, `fork=false`; all fields **parent-verified via direct `GET /repos/`**; README read in full, 10,102 bytes).

Its README, verbatim:

> *"**Print-Ready Thermal Receipt Generator** — Displays store details, **transaction timestamp**, cashier name, customer name, line item subtotals, tax/discounts, and change returned."*

> *"**Inventory Safety Checks:** Prevents overselling by automatically validating warehouse physical stock."*

**Le31-side gap this names (proven by EXECUTION):** `orderitem_has_insertion_time` = **false**; `distinct_payloads` = **1** across five real inserts; `bill_has_no_link_to_order_items` = **true** (the bill does not reference its lines, so ordering must be recovered through `visit_id` and a column that does not exist). The receipt prints a *transaction timestamp*; the row the receipt is built from keeps no time.

**⚠️ The repo's own test claim is NOT verified.** Its README states *"All 4 test suites pass with 100% assertions covering routing, redirects, permissions, and booking-to-order creation."* That is the **repo author's own marketing claim**, was **not independently verified** by this pass, and is **not** used as evidence for anything in this contract. (Per the standing rule: repo self-reported metrics are labelled unverified, never restated as fact.)

**Recorded, not picked (each verified by a corpus-wide grep, not by memory):**

| Rule from the source | LE31 analogue | Disposition |
|---|---|---|
| *"Inventory Safety Checks: Prevents overselling by automatically validating warehouse physical stock"* | validate stock before selling | **Feature 404** (null-safe active-batch predicate) + **feature 417** (actor FK) — **filed** |
| *"RBAC powered by `spatie/laravel-permission`"* | per-command authorisation | **COVERED (10)** — features 28-, 379; §3.1's chat_id allowlist is a **shape mismatch** already filed in the 91st pass |
| *"Split-screen reactive catalog, dynamic cart stepper, customer selector, checkout modal"* | the waiter surface | **COVERED (200)** — the customer-facing-ordering family |
| *"Print-Ready Thermal Receipt"* | the receipt | **COVERED (59)** — features 06-, 123 and the receipt family |
| *"Appointment & Reservation Management"* | reservations | **Out of scope** — §3.2 explicitly excludes *"Online ordering, delivery, reservations."* |
| *"Low-Stock Sentinel: automatic warning for products with ≤10 items in stock"* | low-stock thresholds | **COVERED** — the stock-threshold family (features 28-, 34) |

**Boundary — what this feature does NOT own:** the *order-item state transition* and its actor (379), the *`order_item` unit* (392), the *batch provenance* (385), the *bill ↔ visit edge* (415), the *schema-wide `created_at` convention* (429), the *`menu_item.category` normalisation* (431), the *ledger derivation* (374), the *null-safe active batch* (404), the *actor FK* (417).

**Fully reversible.** The column is additive and defaults to the insert instant; the helper is new and unreferenced until a router calls it. No existing row changes meaning.
