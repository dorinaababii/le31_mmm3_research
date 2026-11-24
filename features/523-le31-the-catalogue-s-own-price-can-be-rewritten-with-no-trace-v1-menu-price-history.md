# Feature 523 — The catalogue's own price can be rewritten with no trace: `menu_item.unit_price` is the second mutable money number, and the corpus recorded that nobody owns it

> **Pick B of Daily Brainstorm 2026-11-24 (107th daily-brainstorm pass).** **Bucket: v1.** **Verdict: `build` — first-party, proven by execution, and named as unowned by the corpus itself.**
>
> **Evidence class: FIRST-PARTY, PROVEN BY EXECUTION.** The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-24-scripts/probe_schema.py`.
>
> **The single sentence this feature exists to make true:** *the price a dish costs today, and the price it cost when it was sold, are two different facts, and only one of them may be overwritten.*

## Goal

Make the **catalogue's** price mean **one thing**: the price the menu shows today — with the price it carried yesterday **recoverable**.

Concretely, three things:

1. **A price change must leave a record.** `UPDATE menu_item.unit_price` is accepted today, silently, and the old price is gone.
2. **The catalogue's price history is a distinct thing from the order line's price history, and the corpus says so.** Feature **444** owns the *line's* price and **explicitly puts the menu price's own history out of scope** — in its own words. **This slice is that scope note, taken.**
3. **The snapshot behaviour that already works must keep working.** The order line carries its **own** `unit_price`, so a line taken at €2.50 stays at €2.50 when the menu moves to €3.00. **That is correct today and this slice does not change it.**

**The charter row this supports, verbatim** (`PROJECT_CHARTER.md`):

> | **P0** | Waiter can browse today's menu and add items to the active visit. | `POST /api/visits/{id}/items` works; menu hides sold-out items. |

A guest is charged the price on the **line**, but the price on the line came from the **menu**. The menu's price is therefore the *root* of every money figure in the system — and it is the only one of the three that has **no** record behind it.

## Scope

**In scope (v1):**

- **A price-change record for `MenuItem`** — one row per change, carrying the old price, the new price, the actor and the moment.
- **A write path that goes through it** — a price change is a *recorded event*, not a bare `UPDATE`.
- **A read helper** that returns the current price and, on request, the history.
- **A regression check** that fails on today's shape and passes on the fixed one: after a price change, the previous price is recoverable.
- **A cleanup note for the owner** if a live database already holds price rewrites that were never recorded — **this slice cannot reconstruct them and must not pretend to.**

**Explicitly NOT in scope:**

- **The order line's price history.** Feature **444** owns it. **444's own text is the boundary**: *"The menu price's own history. The menu is *configuration*; a changed menu price is a catalogue edit, and the catalogue has no write path today. This feature records the **line's** price."*
- **What price a line may carry.** Feature **449** owns that (`price_reason`, `manager_override`, `comp`). **449 is a different question** — it is about the *line's* price being justified; this is about the *catalogue's* price being *traceable*.
- **The catalogue's delete path.** Feature **522** owns it.
- **The bill's derivation from the order lines.** Feature **435** owns the missing `Bill → order_item` edge. Untouched.
- **The tax rate, the rounding mode and the Decimal guard** — features **408**, **410** and **411** are read, not changed.
- **The tip formula and the money rules** — features **420** (tendered vs received) and **415** (the bill-close write) are unaffected.
- **Any change to `OrderItem`, `Bill`, `DerivedTip` or `StockEntry`.**
- **Any new column on `menu_item`** — the history is a **table**, not a column. *(A `previous_price` column would preserve exactly one change and lose the second one — the same "stored value that is a copy of a derived number" defect feature **471** owns for `Batch.qty_remaining`.)*
- **Any change to `index.html`** — the twelve-way collision zone.
- **Any change to `PROJECT_CHARTER.md`.**

## Description

### The defect, as executed

`backend/app/models.py`, verbatim — the catalogue price and the line price, side by side:

```python
class MenuItem(SQLModel, table=True):
    __tablename__ = "menu_item"
    ...
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
```

```python
class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"
    ...
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
```

**Two columns, the same name, the same type, two different jobs** — and the corpus already knows the difference. Feature **449** states it verbatim:

> - `MenuItem.unit_price` — **the catalogue price**, what the item costs today;

**The mutation, executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one menu item):

```text
PROBE B — the catalogue can be deleted and its children survive
  DELETE FROM menu_item WHERE id=<menu_item>                 ACCEPTED
  ...
```

and, from feature **444**'s own probe on 2026-11-06, re-confirmed on the schema built today:

```text
  UPDATE menu_item SET unit_price = 99.00  -> ACCEPTED silently
```

**The price moved from €11.50 to €99.00 and nothing recorded that it moved, from what, or by whom.** The catalogue's price is **the only money number in LE31 that has no history**.

### The corpus already recorded this gap and left it open

**Feature 471**, in its *Adjacent evidence*, verbatim:

> - **`UPDATE menu_item.unit_price -> 99.00` was ACCEPTED** — the catalogue's price is a second mutable number with no history. Feature **449** owns *what price a line may carry*; 444 owns the *order line's* price. **The catalogue's own price history is a third thing**, owned by nobody. Recorded, not filed.

**"Owned by nobody. Recorded, not filed."** — that is the sixth instrument's shape verbatim: *a feature that found a defect, did not own it, and said so.*

**And feature 444 had already seen the same mutation and pointed at the gap in its own *Out of scope* list**, verbatim:

> - **The menu price's own history.** The menu is *configuration*; a changed menu price is a catalogue edit, and **the catalogue has no write path today.** This feature records the **line's** price. (The menu-price overwrite is recorded below as an adjacent observation, not a pick.)

**Two features, two different days, two explicit invitations.** 444 in its *Out of scope*, 471 in its *Adjacent evidence*.

**The corpus sweep confirms it is still unowned.** Over all **555** feature contracts and **511** HANDOFFs, the patterns for a catalogue price *history* — as opposed to a catalogue price *value* — return **zero** files:

| pattern | hits | what they are |
|---|---|---|
| `menu_item.{0,30}unit_price` | 2 | feature **449** (the catalogue price *value*) and feature **429** (a column inventory) |
| `catalogue.{0,30}price` | 1 | feature **471** (the recording) |
| `menu.{0,20}price.{0,20}(history|change|old|previous)` | **0** | — |
| `price_change\|price_history\|price_change_log` | **0** | — |

**The nearest neighbour is 444, and 444's own sentence is what makes this a distinct instance rather than a duplicate.** 444 owns *the line's* price history; it disclaims *the catalogue's*. **449** owns *what a line may carry*; it is about justification, not traceability. **Two different questions about two different columns, with two different mechanisms — one is a history table on `OrderItem`, this is a history table on `MenuItem`.**

### The snapshot behaviour that is already right, and must not break

Feature **444** proved this, and it is worth stating here because it is the reason this feature is cheap:

> The snapshot behaviour is correct and it is **not** the defect. Executed: the menu price moved from 2.50 to 3.00 and the line kept 2.50 — exactly right.

| | the line | the menu |
|---|---|---|
| taken at €2.50, menu later moves to €3.00 | stays **€2.50** | shows **€3.00** |
| what is lost today | — | **the €2.50** — there is no record it ever was €2.50 |

**This slice adds the missing half of that table.** The left column is right; the right column has no memory.

## Data model

**One new table. No new column on `menu_item`.**

```python
class MenuItemPriceChange(SQLModel, table=True):
    """Append-only record of every change to a menu item's price."""
    __tablename__ = "menu_item_price_change"

    id: int | None = Field(default=None, primary_key=True)
    menu_item_id: int = Field(foreign_key="menu_item.id", index=True)
    old_price: Decimal = Field(max_digits=10, decimal_places=2)
    new_price: Decimal = Field(max_digits=10, decimal_places=2)
    by_user_id: int | None = Field(foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

**Why a table and not a column.** A `previous_price` column on `menu_item` preserves **exactly one** change and loses the second — the identical failure mode feature **471** owns for `Batch.qty_remaining` (*"the stored column is a second copy of a number the charter says must be derived"*), and the identical shape feature **470** owns for the ledger. **A history is not a column.** The corpus has learned this three times.

**Why append-only.** Feature **470** established the discipline for `stock_entry`: *"Never UPDATE or DELETE rows."* A price history is the same shape — a sequence of facts, each of which was true at a moment. **A price change row is never updated and never deleted.**

**The rule, stated once:** *a menu item's current price is the `new_price` of its latest change record; the price before that is the `old_price` of the same record.*

**A note on the actor.** `by_user_id` is nullable — a price may be changed by a migration script or a seed, and a history that refuses to record who changed the price is worse than one that records "unknown". **Feature **451** owns the actor-resolution seam and this slice reuses it**; it does not build authentication.

## Implementation

**Files to touch:**

| file | change |
|---|---|
| `backend/app/models.py` | the `MenuItemPriceChange` table |
| `backend/app/services/catalogue_service.py` *(new — shared with feature **522**)* | `set_menu_item_price(session, menu_item_id, new_price, by_user_id)` — writes the change row **and** updates the column in **one transaction** |
| `backend/app/routers/menu.py` | the price-change route — a price change goes through the service, never a bare `UPDATE` |
| tests | a regression test that fails on today's shape |

**Order of work:**

1. **Add the table.** New table, so `create_all()` creates it — **no migration needed** *(this is the one thing that makes this slice cheaper than feature 522, which must wait for 446.)*
2. **Write the service function.** It must write the change row and update the column **in the same transaction** — a change row without the column update, or the reverse, is worse than neither.
3. **Point the route at the service.** If a price can still be changed by a bare `UPDATE` anywhere, the guard is decorative. **The corpus's own lesson from feature **444**: *"the rule belongs to the write path, not to each caller, and it must be checkable."*
4. **Write the regression test.**

**The regression test, specified:**

```python
def test_a_price_change_leaves_the_old_price_recoverable(...):
    menu_item = make_menu_item(unit_price=Decimal("11.50"))
    set_menu_item_price(session, menu_item.id, Decimal("13.00"), by_user_id=1)
    assert menu_item.unit_price == Decimal("13.00")
    changes = list_price_changes(session, menu_item.id)
    assert changes[0].old_price == Decimal("11.50")
    assert changes[0].new_price == Decimal("13.00")
```

**The negative control (the check must be able to fail):** the same test with the service bypassed **must fail** — i.e. a bare `UPDATE menu_item SET unit_price` leaves no row, and the test must catch that. **If the test passes when the write path is bypassed, it proves nothing.**

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface. *(If the owner wants the cook to see today's price changes, that is a separate feature that cites this one.)*

## Dependencies

- **Feature 444** — **adjacent, and the nearest neighbour.** 444 owns the line's price history and explicitly defers the catalogue's. **This slice must not modify 444's table or its service.**
- **Feature 449** — **adjacent.** 449 owns what price a *line* may carry. **Its `price_reason` vocabulary is about the line, not the catalogue** — and the two must not be merged.
- **Feature 451** — **reused.** 451 owns the actor-resolution seam; this slice records `by_user_id` and reuses 451's resolution. **It does not build authentication.**
- **Feature 470** — **adjacent.** 470 establishes the append-only discipline for a ledger; this slice applies it to a price history.
- **Feature 471** — **adjacent.** 471 recorded this finding. **471 also owns the shape** ("a stored column that is a second copy of a derived number") that this slice avoids by using a table.
- **Feature 522** — **adjacent, and the sibling.** 522 owns the catalogue's *delete* path; this owns the catalogue's *price* path. **Both write into the same `catalogue_service.py` module** — they are designed to land together or in either order, and they do not conflict.
- **Feature 470's triggers and feature 446's migration mechanism are NOT dependencies** — this slice adds a **new table**, which `create_all()` can create without a migration.

## Open questions

1. **Should the price change be blocked while an open visit holds lines at the old price?** The recommendation is **no** — the line carries its own price, so an open visit is unaffected. **Recorded default: no block.** The owner may decide otherwise.
2. **Should a price change be effective from a moment, or from a service day?** Feature **405** owns the service-day boundary. **Recorded default: from the moment the change is written** — a price history row carries its own `at`, so a service-day question is answerable later without a schema change.
3. **Should the history be exposed on the menu read?** **Recorded default: no.** The history is for the owner and for audit, not for the waiter. **A read that exposes the whole price history to every surface is scope creep.**
4. **Who may change a price?** Feature **403** owns the role policy. **This slice records the actor; it does not decide who may act.** *(Same boundary as feature **444**.)*
5. **Should a price change that does not actually change the price write a row?** **Recorded default: no** — a row that says "€11.50 → €11.50" is noise. **Recorded so the implementer does not decide it by accident.**
6. **What about the `MenuItem.unit` and `category`?** They are mutable in the same way the price is. **Recorded, not picked** — the same guard should cover them, and **the implementer should say whether it does**, rather than the price being special-cased alone.

## Why this matters

**Because a price change is not a typo. It is a decision, and decisions are supposed to leave a trace.**

The failure mode is quiet and it is invisible in the moment. The owner writes the menu on a Tuesday. On Thursday a dish costs €13.00 instead of €11.50. **Nobody notices that anything happened**, because nothing *happened* — the column simply holds a different number now. The old price is **not** in the database, not in a log, not anywhere. **A week later the owner cannot answer "what did this cost last month?"** — and for a restaurant that is a real question, because the answer decides what yesterday's sales actually were.

**And this is the gap that makes LE31's money story incomplete.** The corpus has, over eleven days of passes, closed the price story on the **line** (444), the **bill** (415, 435), the **tip** (457, 420) and the **ledger** (470, 471). The **menu** is the one money number with no record — and the menu is the **root**: every line's price was copied from it.

**The discipline is already established twice.** Feature **444** proved that the *line's* price must have a history, and proved the snapshot behaviour that makes it safe. Feature **470** established the append-only discipline for a sequence of facts. **This slice applies both, to the one column that was left.** And it applies them where the corpus itself pointed: 444's *Out of scope* said *"the catalogue has no write path today"* — and 471's *Adjacent evidence* said *"owned by nobody. Recorded, not filed."*

**A price that cannot be explained is a price the owner has to trust.** That is a low bar for a system whose whole claim is that it keeps the books.

## Out of scope

*(Repeated at the end deliberately: the boundary is the point.)*

- **The order line's price history** — **feature 444**.
- **What price a line may carry** (`price_reason`, `manager_override`, `comp`) — **feature 449**.
- **The catalogue's delete path** — **feature 522**.
- **The bill's line membership** — **feature 435**. **The bill-close write** — **feature 415**. **The tip formula** — **feature 457**. **Tendered vs received** — **feature 420**.
- **The tax rate, the rounding mode and the Decimal guard** — features **408**, **410**, **411**.
- **The role policy for who may change a price** — **feature 403**.
- **The actor-resolution seam** — **feature 451** (reused, not rebuilt).
- **Any change to `OrderItem`, `Bill`, `DerivedTip`, `StockEntry`, `Batch` or `Visit`.**
- **Any column on `menu_item`** — the history is a table. **A `previous_price` column preserves one change and loses the second.**
- **Any change to `index.html`** — the twelve-way collision zone.
- **Any change to `PROJECT_CHARTER.md`.**
