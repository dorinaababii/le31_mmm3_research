# Feature 522 — A menu item can be deleted while its batches and its order lines still point at it: the catalogue has no delete path, no tombstone and no referential guard

> **Pick A of Daily Brainstorm 2026-11-24 (107th daily-brainstorm pass).** **Bucket: v1.** **Verdict: `build` — first-party, proven by execution, and recorded UNOWNED by the corpus itself (twice).**
>
> **Evidence class: FIRST-PARTY, PROVEN BY EXECUTION.** The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-24-scripts/probe_schema.py`.
>
> **The single sentence this feature exists to make true:** *a menu item that has been ordered from is never removed from the catalogue — it is retired, and the history that points at it stays readable.*

## Goal

Make the **catalogue's** delete path mean **one thing**: a dish that appears in money or in stock history is not deleted; it is retired, and everything that referenced it still resolves.

Concretely, three things:

1. **A delete must be refused when the item has history.** `DELETE FROM menu_item` is accepted today even when a `Batch` and an `OrderItem` still point at the deleted row.
2. **A retirement must exist for the case the delete is refusing.** Feature **438** already owns the *flag* that says "we stopped serving this dish" (`is_active` semantics — retired is permanent, sold-out is temporary). What does not exist is the **rule that the flag is the only way to take a dish off the menu**, and the **guard that makes the flag path the only way**.
3. **A price change must not be a silent rewrite.** See the second half of the corpus's own recorded observation: `UPDATE menu_item.unit_price` is accepted silently today. **That is a separate pick** (feature **523**) and this slice does not swallow it.

**The charter rows this supports, verbatim** (`PROJECT_CHARTER.md`):

> | **P0** | Waiter can browse today's menu and add items to the active visit. | `POST /api/visits/{id}/items` works; menu hides sold-out items. |

and the module docstring's own claim, verbatim from `backend/app/models.py`:

> ```
> # ───── Tables ─────
> ```

and — the load-bearing one — the schema's own intent for the ledger, verbatim from `StockEntry`'s docstring:

> ```
> Append-only ledger. Never UPDATE or DELETE rows.
> ```

**The catalogue has no such claim, and no such guard.** The stock story is protected by a docstring plus feature **421**'s triggers. The catalogue story is protected by nothing.

## Scope

**In scope (v1):**

- **A delete path for `MenuItem` that is refused when the item has history** — specifically when a `Batch` row references it (`Batch.menu_item_id`) or an `OrderItem` row references it (`OrderItem.menu_item_id`).
- **A retirement write path that is the sanctioned alternative**: retire a dish, keep the row, keep its price and its history.
- **A referential guard** so that the reference cannot be created broken in the first place — the `ON DELETE` clause the schema has nowhere, or an equivalent rule enforced at the write path.
- **A regression check** that fails on today's shape and passes on the fixed one: deleting a dish with history is refused; deleting a dish with no history is still possible or is also refused by an explicit decision.
- **A cleanup note for the owner** if a live database already holds orphaned rows — **this slice does not delete a row to make the guard apply.**

**Explicitly NOT in scope:**

- **The availability flag itself.** Feature **438** owns `is_active` / the retired-vs-sold-out distinction, its write path and its restore path. **This slice owns the rule that the catalogue is not deletable and the guard that enforces it.** **438's own text is the boundary**: *"Deleting a dish preserves the money and loses the thing the customer ordered. A retired dish preserves both, because the row stays and the retirement is a flag."*
- **The sold-out state.** Feature **397** owns it (per-day, derived, stock-driven). **Sold-out is temporary and does not un-stock; retired is permanent and does not touch the ledger at all.** The two must never be merged into one column.
- **The catalogue's own price history.** Feature **523** owns it. **444** owns the *order line's* price and explicitly puts *"the menu price's own history"* out of scope.
- **The FK-enforcement story on SQLite.** Feature **427** owns `PRAGMA foreign_keys = 0` and the dev/prod divergence. **This slice does not enable the pragma and does not fix it**; it adds the `ON DELETE` semantics that the pragma, once 427 lands, will actually enforce.
- **Any change to `Batch`, `OrderItem`, `Bill` or `StockEntry`.**
- **Any router, any endpoint, any Python file beyond `models.py`, any new dependency.** — *(the route that 438 adds is the route; this slice may add the guard beside it)*
- **Deleting or renumbering a menu item, a batch or an order line.** **The guard may fail to apply to an existing database; resolving that is an operational step for the owner, and this slice must not destroy data to make it apply.**
- **Any change to `index.html`** — the twelve-way collision zone belongs to features 465/466/467/474/475/476/484/487/489/509/511/516.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The defect, as executed

`backend/app/models.py`, verbatim — the catalogue and the two tables that point at it:

```python
class MenuItem(SQLModel, table=True):
    __tablename__ = "menu_item"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    category: str
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    unit: str = "piece"
    is_prepared: bool = True    # if True, sales decrement a Batch
    photo_url: str | None = None
```

```python
class Batch(SQLModel, table=True):
    __tablename__ = "batch"
    ...
    menu_item_id: int = Field(foreign_key="menu_item.id")
```

```python
class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"
    ...
    menu_item_id: int = Field(foreign_key="menu_item.id")
```

**Neither foreign key carries an `ON DELETE` clause** — proven by execution, enumerating every `ForeignKey` on every table in LE31's real schema:

```text
PROBE D — schema-level guard census
  app_user       unique=[] check=[]
  batch          unique=[] check=[]
                 fk menu_item.id ondelete=None
  bill           unique=[None] check=[]
                 fk visit.id ondelete=None
                 fk app_user.id ondelete=None
  derived_tip    unique=[] check=[]
                 fk bill.id ondelete=None
  menu_item      unique=[] check=[]
  order_item     unique=[] check=[]
                 fk visit.id ondelete=None
                 fk menu_item.id ondelete=None
  shift          unique=[] check=[]
                 fk app_user.id ondelete=None
  stock_entry    unique=[] check=[]
                 fk batch.id ondelete=None
  table_         unique=[] check=[]
  visit          unique=[] check=[]
                 fk table_.id ondelete=None
                 fk app_user.id ondelete=None
```

**Every `ondelete` in LE31's schema is `None`.** There is no `RESTRICT`, no `CASCADE`, no `SET NULL` anywhere.

And the mutation itself, executed against LE31's **real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one menu item, one batch and one order line that both point at it):

```text
PROBE B — the catalogue can be deleted and its children survive
  DELETE FROM menu_item WHERE id=<menu_item>                 ACCEPTED
  batches still pointing at the deleted menu_item : 1
  order_lines still pointing at the deleted item   : 1
  DELETE FROM batch WHERE id=<batch>                         ACCEPTED
```

**The delete was accepted. Two rows now point at a row that does not exist.** The `Batch` still says "8 tiramisu prepared today" about a dish that is gone; the `OrderItem` still says "the guest ordered a Schnitzel at €11.50" — and `OrderItem` carries its **own** `unit_price`, so the money on the line survives; what is lost is the **dish**: the name, the category, the unit, the photo, and the price the menu shows today.

That is the shape feature **438** names verbatim: *"Deleting a dish preserves the money and loses the thing the customer ordered."*

### The corpus already recorded this gap and left it open — twice

**Feature 470**, in its *Adjacent evidence*, verbatim:

> - **`DELETE menu_item` was also ACCEPTED**, and the `batch` rows that referenced it **survived** (1 batch still points at the deleted menu item) — because the FK pragma is off in dev (feature 427) and **no FK in the schema carries an `ON DELETE` clause**. **The catalogue's delete/retire path is owned by no feature** and is recorded as adjacent evidence in the 2026-11-12 report, not filed here.

**Feature 471**, in its *Adjacent evidence*, verbatim — the same finding, recorded a second time, on a different day, by a different pass:

> - **`DELETE menu_item` was ACCEPTED** and the referencing `batch` rows survived. **No feature owns the catalogue's delete/retire path.** Recorded, not filed.

**Both passes said "recorded, not filed" and neither filed it.** That is an explicit, twice-repeated invitation — the sixth instrument's shape: *a feature that found a defect, did not own it, and said so.*

**The corpus sweep confirms it is still unowned.** Over all **555** feature contracts and **511** HANDOFFs:

| pattern | hits | what they are |
|---|---|---|
| `menu_item.{0,30}(delete\|deleted)` | 1 | feature **459**, which says *"A dangling `menu_item_id` is 427's defect, not this one's"* |
| `delete.{0,20}menu_item` | 3 | features **470** and **471** (the two recordings) + 470's HANDOFF |
| `catalogue.{0,30}(delete\|retire)` | 2 | the same two recordings |
| `orphaned? (menu\|batch\|order)` | **0** | — |

**Feature 459's own words point the defect elsewhere**, which is exactly the "covered concept, uncovered instance" shape: 459 owns the *bill's subtotal predicate*, and it says a dangling `menu_item_id` is **427's** defect (the SQLite FK pragma). **427 is about the pragma being off in dev; it is not about what a delete should do.** The instance this slice takes is: *the catalogue has no delete rule at all* — which neither 427 nor 459 nor 438 states.

### What 438 already owns, and why this is not 438

Feature **438** is the retirement feature. It owns the flag, the write path, the restore path and the two read filters. **Its own text is what makes this slice necessary**, verbatim:

> **Deleting a dish preserves the money and loses the thing the customer ordered.** A retired dish preserves both, because the row stays and the retirement is a flag.

**438 assumes the flag is the only way to take a dish off the menu.** Today it is not: `DELETE FROM menu_item` still works, so there are **two** ways to take a dish off the menu and only one of them is safe. **This slice closes the second one.** The mechanisms are disjoint — 438's is a boolean column and its filters; this slice's is the absence of a delete path and the `ON DELETE` semantics.

## Data model

**No new table. No new column. One clause and one rule.**

```python
class Batch(SQLModel, table=True):
    ...
    # RESTRICT is the default in both SQLite and Postgres; stating it makes
    # the rule legible instead of implied.
    menu_item_id: int = Field(foreign_key="menu_item.id", ondelete="RESTRICT")
```

```python
class OrderItem(SQLModel, table=True):
    ...
    menu_item_id: int = Field(foreign_key="menu_item.id", ondelete="RESTRICT")
```

**Why `RESTRICT` and not `CASCADE`:**

- **`CASCADE` would delete the batch rows and the order lines** — that is precisely the data loss the charter's append-only discipline exists to prevent. `StockEntry` rows reference `batch.id`; cascading a batch away would cascade away the ledger. **Unacceptable.**
- **`SET NULL` is impossible here** — both columns are `NOT NULL`.
- **`RESTRICT`** refuses the delete and leaves every row intact. **It is the default in both engines**, so stating it changes no behaviour on a healthy database and makes the intent readable in the schema — which is the whole point of this slice.

**The rule, stated once:** *a `MenuItem` row with history is not deletable; it is retired (feature 438).*

**The dev/prod caveat, stated honestly:** SQLite's foreign keys are **off** by default, and feature **427** owns that. `PRAGMA foreign_keys = 0` means **`RESTRICT` does not fire in dev** until 427 lands. **This slice must therefore add the rule at the write path as well, not only in the DDL** — the write-path rule is the one that works today, and the DDL clause is the one that survives into production.

## Implementation

**Files to touch:**

| file | change |
|---|---|
| `backend/app/models.py` | `ondelete="RESTRICT"` on `Batch.menu_item_id` and `OrderItem.menu_item_id` |
| `backend/app/services/catalogue_service.py` *(new)* | one function: `retire_menu_item(session, menu_item_id, by_user_id)` and one function: `delete_menu_item(session, menu_item_id)` that **raises** when history exists |
| `backend/app/routers/menu.py` *(new or existing)* | the delete route — refuse with **409** when the item has history |
| tests | a regression test that fails on today's schema |

**Order of work:**

1. **Write the guard as a function first.** `delete_menu_item(session, menu_item_id)` raises when a `Batch` or an `OrderItem` references the item. **It raises; it never deletes.**
2. **Add the DDL clause.** `ondelete="RESTRICT"` on both foreign keys. **This needs the migration path feature **446** owns** — `create_all()` cannot alter an existing table. **446 must land first, or this lands in the same PR.**
3. **Add the route**, refusing with **409** and the reason.
4. **Point the existing retirement route (438) at the same service module**, so there is one place that knows the catalogue's rules.
5. **Write the regression test.**

**The regression test, specified:**

```python
def test_delete_is_refused_when_the_item_has_history(...):
    # a menu item with a batch and an order line
    with pytest.raises(...):
        delete_menu_item(session, menu_item_id)
    # and the rows are still there
    assert session.get(Batch, batch_id) is not None
    assert session.get(OrderItem, order_item_id) is not None
```

**The negative control (the check must be able to fail):** the same test with the guard removed **must fail**. If it passes without the guard, the test proves nothing.

## Telegram interaction

**None.** This slice changes no bot command, no FSM state and no chat surface. **Charter §3.1** keeps the Telegram surface to the cook and the manager; a catalogue delete is a manager action, and if the owner wants it in the bot it is a separate feature that cites this one.

## Dependencies

- **Feature 446** (the migration path) — **must land first, or in the same PR**, because `create_all()` cannot alter an existing table's foreign keys. **This is the upstream-of-filed-work condition, and it is named here with its number.**
- **Feature 438** (retirement flag) — **adjacent, not a dependency.** 438 owns the flag and its filters; this slice owns the absence of a delete path. **If 438 has not landed, the sanctioned alternative does not exist yet** — so the delete must be refused outright in the meantime, and the contract says so.
- **Feature 427** (SQLite FK enforcement) — **not a dependency.** When it lands, `RESTRICT` starts firing in dev too. **This slice does not wait for it** and does not enable the pragma.
- **Feature 470** (ledger delete guard) — **adjacent.** 470 protects `stock_entry`. This slice protects `menu_item`. **470's own text says the catalogue's path *"is owned by no feature"* — this slice is that missing slice.**
- **Feature 471** (stored `qty_remaining`) — **adjacent.** 471 records the same catalogue finding a second time.
- **Feature 459** (bill subtotal predicate) — **adjacent.** 459 defers the dangling-`menu_item_id` question to 427; this slice answers the different question (what a delete *does*).

## Open questions

1. **Should a dish with no history at all still be deletable?** The recommendation is **yes** — a dish created by mistake and never ordered has no history and no money attached, and refusing the delete leaves the owner with no way to correct a typo. **Recorded default: a dish with no `Batch` and no `OrderItem` is deletable; one with either is not.** **The owner may decide otherwise, and the decision is one line.**
2. **Should retirement be reversible?** Feature **438** owns the restore path and says the restore is in scope there. **This slice does not change that.**
3. **Should the delete be refused with 409 or 404?** **Recorded default: 409** — the item exists, the *state* forbids the operation. A 404 would hide a dish that is still on the menu.
4. **What about a soft-delete that keeps the row forever?** Retirement (438) is exactly that, and it is the better shape. **A separate `deleted_at` column would be a third way to take a dish off the menu — the very thing this slice removes.**
5. **Should the guard also cover `Bill`?** A bill references a visit, and a visit references a table — **not a menu item.** The `order_item → menu_item` edge is the one that matters. **Not decided here; recorded so the implementer does not widen the guard by reflex.**
6. **Does the existing live database already hold orphans?** The parent cannot know without reading the owner's database. **The contract requires the implementer to check and to report the count, and forbids deleting rows to make the count zero.**

## Why this matters

**Because a restaurant forgets what it used to serve, and LE31 forgets it the wrong way.**

The failure mode is quiet and it is not a crash. Nothing breaks. A dish is deleted — by a migration script, by an admin tool, by a mistake at 2 a.m. — and the database accepts it. The kitchen's prep board for today still says **8 tiramisu**. The bill from last Friday still says the guest ordered a **Schnitzel at €11.50**, and the line's own price survives, so **the money is right and the dish is gone**. The owner's daily report shows a dish that no longer exists with a price that no longer applies. The order history cannot be read back in the one way a restaurant reads history — by name.

**And the guard that would catch it is exactly the guard the schema does not have.** Every foreign key in LE31's schema carries `ondelete=None`. There is no `RESTRICT`, no `CASCADE`, no `SET NULL` — ten tables, ten foreign keys, **no clause**. The stock ledger is protected by a docstring and feature 421's triggers; the catalogue is protected by **nothing at all**, while carrying **two** inbound references and a **name** that the business speaks out loud.

**The corpus knew.** Twice, on two different days, two different passes wrote *"The catalogue's delete/retire path is owned by no feature"* and *"recorded, not filed"*. Those two lines are the reason this contract exists. **A finding that is recorded twice and filed never is a finding that will be rediscovered forever** — so this pass files it.

## Out of scope

*(Repeated at the end deliberately: the boundary is the point.)*

- **The retirement flag, its write path, its restore path and its read filters** — **feature 438**. This slice makes the flag the *only* way to take a dish off the menu; it does not build the flag.
- **The sold-out state** — **feature 397**.
- **The catalogue's own price history** — **feature 523**. Feature 444 owns the order line's price and explicitly defers the catalogue's.
- **The SQLite foreign-key pragma** and the dev/prod divergence — **feature 427**. This slice adds the clause; it does not enable the pragma.
- **The migration mechanism** — **feature 446**. 446 must land first, or in the same PR.
- **Any change to `Batch`, `OrderItem`, `Bill`, `StockEntry` or `Visit`.**
- **Any router beyond the catalogue delete route**, any new dependency, any Python file beyond `models.py` and the catalogue service.
- **Deleting or renumbering any existing row** — the guard may fail to apply to a live database, and that is the owner's operational step, not this slice's.
- **Any change to `index.html`** — the twelve-way collision zone.
- **Any change to `PROJECT_CHARTER.md`.**
