# Feature 449 — `le31-an-order-line-may-carry-any-price-it-likes`

> **Pick C of Daily Brainstorm 2026-11-06 (99th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, two verbatim fragments:
>
> ```python
> class MenuItem(SQLModel, table=True):
>     __tablename__ = "menu_item"
>
>     id: int | None = Field(default=None, primary_key=True)
>     name: str
>     category: str
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)   # the catalogue price
>     unit: str = "piece"
>     is_prepared: bool = True
>     photo_url: str | None = None
>
>
> class OrderItem(SQLModel, table=True):
>     __tablename__ = "order_item"
>
>     id: int | None = Field(default=None, primary_key=True)
>     visit_id: int = Field(foreign_key="visit.id", index=True)
>     menu_item_id: int = Field(foreign_key="menu_item.id")
>     qty: int = 1
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)   # the line price -- INDEPENDENT
>     course: str | None = None
>     status: ItemStatus = ItemStatus.new
>     notes: str | None = None
>     fired_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     ready_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     served_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
> ```
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite DB, then real inserts):
>
> ```
>   menu_item.unit_price = 2.50
>   order_item.unit_price = 99.00   (the line says 99.00, the menu says 2.50)
>   TWO NUMBERS: menu price = 2.50 ; line price = 99.00 ; ratio = 39.6x
> ```
>
> **The line was ACCEPTED.** There is no rule connecting them, no default, and no derivation.
>
> **Evidence class: OBSERVED** (every claim below is a reproducible execution against LE31's own schema). **Confidence: high** for the gap; **medium** for the operational pain (see *Evidence* in the gate verdict and *Open questions*).
>
> **Bucket: v1.** **Build verdict: `build`.**

## Goal

Make an order line's price **come from the menu**, and make any departure from the menu price **an explicit, deliberate act**.

One helper, one call site, one question answered: **"why is this line not at the menu price?"**

## Scope

- Add **one helper** that produces an order line's price — **from the menu**, by default.
- Call it from **the one path that writes an order line**.
- Make the **deliberate** departures explicit: a caller that wants a different price must **say so**, and the reason must be **named**.
- Keep the line's price **a snapshot** — feature **444**'s property, unchanged.

## Out of scope (v1)

- **The price-change TRACE.** Feature **444** owns *a change to a line's price is recorded and reversible*. **This feature owns where a line's price comes from.** The two are adjacent and **must not be merged**: 444's contract says verbatim that `unit_price` *"stays a `Decimal` snapshot of what the line was sold at"* — this feature is what decides **what "sold at" means**.
- **Discounts, promo codes, and comps as a separate model.** Feature **444**'s own out-of-scope says verbatim: *"A discount is not a rewritten price — it is a discount with its own shape."* **Same boundary here.**
- **The menu price's own history.** The menu is *configuration*; a changed menu price is a catalogue edit. **Feature 444 explicitly excludes it.**
- **The bill-close route** — feature **415**.
- **The bill's membership of lines** — feature **435**.
- **The tax rate home** — feature **408**. **The tax is computed on a line's price, so this feature must not touch it.**
- **The tip formula and the money rules** — features **408**, **410**, **411**, **420**.
- **`MenuItem.is_prepared`** — feature **398**. **`MenuItem.unit`** — feature **392**.
- **A `menu_item_id`-less order line** (a free-text item, a daily special, a comp). **The line's `menu_item_id` is NOT NULL today and stays that way.**
- **Any new table.** The reason is **recorded on the line**, not in a new model.
- **Alembic, a migration, or any change to `PROJECT_CHARTER.md`.**
- **Any new pip dependency.**

## Description

### What LE31 already believes

LE31 has two prices, and they are related in the business but unrelated in the schema:

- `MenuItem.unit_price` — **the catalogue price**, what the item costs today;
- `OrderItem.unit_price` — **the line price**, what this guest is being charged.

The relationship between them is *snapshotting*: **the line remembers the price at the moment the guest ordered it**, so a later menu change does not retroactively alter a bill already taken. That is a sound design and it is what feature **444** preserves.

### The gap is the step before the snapshot

A snapshot is only meaningful if there is a thing to snapshot **from**. Today there is no such rule:

- the line's price is **not** defaulted from the menu (SQLModel will not do it, and a `default=` on a non-constant is not possible);
- it is **not** derived from the menu by any helper;
- it is **not** validated against the menu by any check.

So the "snapshot" is not a snapshot of anything. **It is a number the caller typed**, and `menu_item_id` is a *reference*, not a *constraint*. Two rows can point at the same menu item and carry prices that differ by **39.6×**, and the database is perfectly happy.

### The direction of the asymmetry matters

This is the same shape as the defect family LE31's audit has now found repeatedly: **a fact the business knows, with no mechanism that carries it.**

The asymmetry is precise:

- `MenuItem.unit_price` is **the** price. It is the number the menu shows, the number the kitchen works to, the number the owner set deliberately.
- `OrderItem.unit_price` is **a** price. It has no relationship to the first one.

And the direction of the error matters. The line price can be:
- **too high** — the guest is overcharged;
- **too low** — the guest is undercharged and the restaurant quietly loses the difference;
- **wildly wrong** — the 39.6× case above.

**All three are accepted, and none of them is visible.** There is no audit row (feature **444**'s gap), no flag, no exception.

### Why the plausible wrong answer is the quiet one

The plausible wrong answer is *"the line snapshots the menu price."*

That answer is **true of what the schema stores** and **silent about how it got there.** The snapshot defends against a **later menu change**; it says **nothing** about a **wrong price typed at order time**. Those are different failures, and the second one is unguarded.

The second plausible wrong answer is *"the waiter types the price, so it is the waiter's job."*

That is true of a **deliberate** price and false of an **accidental** one, and **the schema cannot tell them apart.** A waiter who enters `9.00` for a `2.50` espresso because they were rushing is **indistinguishable from** a manager applying a promotion. **Both produce a row that looks identical.** The only way to tell them apart is to have made the distinction *at the moment of writing* — which is exactly what this feature does.

### The evidence class is important here — and it cuts both ways

- **The gap is OBSERVED** — an order line was written at 39.6× the menu price and accepted.
- **The pain is INFERRED.** No owner has reported a mispriced bill. There is no complaint, because **there is no order-taking write path** — the parent verified by execution that `grep -rn 'OrderItem(' backend/` returns **exactly one hit**, the class declaration. **No order line has ever been taken.**

This is why the contract is deliberately small: **one helper, one call site, one named reason.** It is not a feature that adds a surface; it is a rule that has to exist before the surface that would violate it.

## Data model

**One added column, and it is the reason — not a second price.**

```python
class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"

    ...
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    price_reason: str | None = None       # NEW — NULL means "the menu price, unchanged"
    ...
```

**Why `price_reason` is a string and not an enum.** An enum here would be a new membership constraint on a column nobody has written yet, and feature **442** just established that LE31's enums are bare `VARCHAR` with no membership constraint — so an enum would need **the same generated-constraint work** before it could be trusted. A `str` with a **named set of allowed values checked in the application helper** is smaller, and it can carry a value the business has not thought of yet without a schema change.

**Why `NULL` means "the menu price, unchanged."** That is the only default that is safe: a line with no reason recorded is a line at the catalogue price. **A line with a reason recorded is a line somebody deliberately departed from the catalogue**, and the reason says which kind of departure.

**The allowed reasons — a named set, checked in the helper, not in the schema:**

| reason | meaning | who |
|---|---|---|
| `NULL` | the menu price, unchanged | the default |
| `manager_override` | the manager changed it | a manager |
| `comp` | the guest is not paying for it | a manager |
| `promo` | a promotion applied | whoever applies promotions |
| `happy_hour` | a time-bounded price | whoever sets happy hour |
| `correction` | the menu price was wrong and the guest was told the real one | a manager |

**The rule this feature adds is not "the price must equal the menu price."** It is:

> **The line's price is the menu price, unless a reason is recorded.**

That is deliberately weaker than a `CHECK` constraint and it is the right shape, because the business **does** have legitimate reasons to sell at a different price — and a schema that forbids them would push the behaviour into the data (the waiter would type a fake price and leave the reason blank, and "no reason" would stop meaning anything).

**Why no `CHECK` constraint.** It would span two tables (`menu_item` and `order_item`), and a SQLite `CHECK` may only reference the row's own table. A trigger would reintroduce a **dev/prod divergence** (feature **413**). **The rule belongs in the application helper.**

## Implementation steps

1. **Write the regression test FIRST, and watch it fail.** The test that matters most is `test_line_price_defaults_to_the_menu_price`.
2. **Add `price_reason: str | None = None` to `class OrderItem`** — **nullable**, so it does not need a backfill. **There are no `OrderItem` rows** (no order write path exists), so the migration question is moot — say so in the PR.
3. **Create `backend/app/services/ordering.py`** with:
   ```python
   def price_for(session, menu_item: MenuItem, *, price: Decimal | None = None,
                 reason: str | None = None) -> tuple[Decimal, str | None]:
       """Return (unit_price, price_reason) for a new order line.

       No explicit price -> the MENU price, and no reason.
       An explicit price -> it, and it MUST come with a reason.
       """
       if price is None:
           if reason is not None:
               raise ValueError("a reason was given without a price")
           return menu_item.unit_price, None
       if reason is None:
           raise ValueError("an order line price that differs from the menu price "
                            "must record a reason")
       if reason not in ALLOWED_PRICE_REASONS:
           raise ValueError("unknown price reason: %r" % (reason,))
       if price < 0:
           raise ValueError("an order line price may not be negative")
       return price, reason
   ```
4. **Call it from the one path that writes an order line.** **If no such path exists yet, provide the helper and a thin `create_order_item(...)` that the future route will call** — and **do not write the route**; that is feature **02**'s territory.
5. **Do not write the line price from the request body.** The request may name a `menu_item_id`; **the price comes from the menu**, and the request may only *override* it **with a reason**. This is the whole point of the slice.
6. **Keep the line's price a snapshot.** The helper reads `menu_item.unit_price` **at write time** and stores the resulting number on the line. Feature **444**'s property is preserved unchanged.
7. **Do not touch `MenuItem.unit_price`**, and do not add a price history to the menu (feature **444** excludes it explicitly).
8. **Do not implement discounts or comps as a model.** The reason string records that a comp happened; the comp's own accounting (who ate it, was it a stock draw) is feature **444**'s and the wider money features' business.

### The scenario table (each row is a test)

| # | Menu price | Call | Expected |
|---|---|---|---|
| 1 | `2.50` | no price, no reason | line price **`2.50`**, reason **`NULL`** |
| 2 | `2.50` | price `1.00`, reason `manager_override` | line price `1.00`, reason `manager_override` — **ACCEPTED** |
| 3 | `2.50` | price `1.00`, **no reason** | **REFUSED** — a departure needs a reason |
| 4 | `2.50` | **no price**, reason `comp` | **REFUSED** — a reason without a price is incoherent |
| 5 | `2.50` | price `1.00`, reason `not_a_reason` | **REFUSED** — unknown reason |
| 6 | `2.50` | price `-1.00`, reason `comp` | **REFUSED** — a negative price is not a comp |
| 7 | `2.50` | price `2.50`, reason `manager_override` | **ACCEPTED** — a redundant reason is allowed (it records that someone looked) |
| 8 | menu price later changes to `3.00` | the existing line is unchanged | the line keeps `2.50` — **the snapshot property, preserved** |
| 9 | `2.50` | price `99.00`, reason `correction` | **ACCEPTED** — the slice does not cap the departure; **it requires the departure to be named** |

**Row 9 is the honest limit of this contract, and it is stated rather than hidden.** A named reason does not make a 39.6× price *correct*. It makes it **visible**: the row now says a manager did this on purpose. **Whether a reason is enough, or whether some reasons should carry their own bound, is an owner question** (see *Open questions*), and this contract does not decide it.

## Telegram interaction if any

**None in this slice.** The slice ships the helper and the reason vocabulary.

The operator surface (a waiter seeing *"this item's price was changed by a manager"*, a manager being asked for a reason when they override) is a **later feature**, and it needs the order-taking path that does not exist yet.

## Dependencies

- **Feature 444** (`le31-order-item-unit-price-is-mutable-in-place-with-no-trace`) — **ADJACENT AND MUST NOT CONFLICT.** 444 owns the *change* and the *trace*; this feature owns the *source*. 444's contract states verbatim that the column *"stays a `Decimal` snapshot of what the line was sold at"* — **this feature is what decides what "sold at" means.** **444 must land first, or in the same PR**, because 444's helper is the thing that *changes* a price, and a change to a price whose origin was never recorded is a change to an unknown baseline.
- **Feature 446** (`le31-has-no-schema-evolution-mechanism`) — **HARD dependency.** This slice **adds a column to an existing table**, which is exactly the operation `create_all()` cannot perform. **446 must land first, or in the same PR.**
- **Feature 442** (`le31-enum-columns-are-varchar-with-no-membership-constraint`) — **adjacent.** It establishes that a new `VARCHAR` membership must be **checked in the application**, which is why `price_reason` is a validated `str` and not a new enum column. **Do not modify 442's work.**
- **Feature 411** (`le31-money-precision-declared-not-enforced`) — owns the `Decimal` precision guard on money columns. **This feature must not weaken it; the helper's negative-price check complements it.**
- **Feature 435** — owns which lines a bill charged. **Adjacent.**
- **Feature 415** — owns the bill-close route, which reads the lines' prices. **Adjacent.**
- **Feature 408** — owns the tax rate home; the tax is computed on a line's price. **Adjacent, not owned here.**
- **Feature 02** (`order-taking`) — owns the order-taking flow. **This feature provides the helper; it does not write the route.**

## Open questions

1. **Should some reasons carry their own bound?** A `manager_override` of `99.00` on a `2.50` item is *named* by this contract but is not obviously *sane*. **A per-reason bound is an owner decision and is not made here.** The reason exists so that the question can be asked later, without re-interpreting existing rows.
2. **Is `happy_hour` a price or a schedule?** It is recorded here as a price with a reason. **If it becomes a time-window on the menu item, that is a different concept** and belongs to a different feature.
3. **Should the reason be free text as well as a code?** A code plus an optional note is the richer shape; a code alone is the smaller one. **This contract implements the code alone.** A note is a later addition.
4. **Who is allowed to use `manager_override` and `comp`?** **Feature 403** owns the role policy. **This contract checks the reason's membership, not the actor's role** — that is 403's, and doing it here would duplicate it.
5. **What happens to a line whose menu item is later deleted?** The line's price is a snapshot, so it survives; **the menu item is not deletable today** and this contract does not change that.
6. **Does a comp consume stock?** A compped dish is still prepared and still consumes a batch. **The stock side of a comp is feature 441**'s and the wider stock features' business; this contract only records that the price was zeroed on purpose.

## Why this matters

A mispriced line is **permanent**. The bill is a **derivation** — feature **415** computes the subtotal from the lines and forbids the caller from setting it — so **the lines are the only place the money is written down.** A wrong line price is indistinguishable from a right one once the bill closes, and it is indistinguishable from a right one *in the database* at every point before that too.

And the failure has no shape. An overcharge is a customer complaint and a refund. An undercharge is a small, invisible loss on every transaction. A 39.6× error is one of the two, or neither, depending on the digit.

**The cheapest possible prevention is a rule that makes the wrong price hard to write by accident:** the price comes from the menu, and any departure must be named. **One helper, one call site, one nullable column, no rows to backfill** (no order line has ever been written). It must land **before** the order-taking path, because after the order-taking path exists, the price will be typed from a request body and the menu will be a suggestion.

## Adjacent evidence

- **Trigger source**: `stdevMac/payverge` — **Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **★1/⑂1**, Go + Next.js, created **2026-10-07** (in-window by both `created_at` and `pushed_at`; `pushed_at` 2026-11-05), README read in full (17,497 B). Verbatim, lines 93–95:
  > *"The AI features ran against real service, so they are built around one rule: **the model never decides a fact, a price or an action on its own. Prices come from the menu snapshot**, tool calls are validated server-side, director changes are previewed and can be undone, and every AI feature has a daily budget and a no-model fallback."*
  **What transfers: the rule itself — the price has a SOURCE, and the source is the menu, not the actor.** LE31's case is narrower and stronger than the source's: there is no AI in LE31's v1, so the "actor who might get the price wrong" is **a human typing into a request body**, and the same rule applies — **the price comes from the menu.** Note also the source's phrase *"tool calls are validated server-side"*: that is a **server-side validation** rule, which is exactly the shape of this contract's helper.
  **What does not transfer: the AI surfaces, the undo log, the budgets, the director console.** LE31 v1 has no AI (charter §3.2), and this contract adds none.
- **Corroborating source**: `indraaryaLabs/coffeeshop-pos` — **MIT ✓ §3.2**, **★0/⑂0**, TypeScript, created **2026-11-05** + pushed **2026-11-05** (in-window by both fields), README read in full (6,655 B). Verbatim: *"**POS screen** — category-filtered product grid, cart, three payment methods (Tunai / Kartu / QRIS), **quick-cash with change preview, discount input**, …"* and *"**Settings** — shop profile (name, address, phone, receipt footer, **tax toggle**) rendered on receipts"*. **The corroboration is the discount input: a POS that lets the cashier type a different price at checkout must therefore have a place to record WHY** — otherwise the price and its justification are the same silent field. LE31 has neither.
- **The corpus probe**: a corpus-wide sweep of all **480 feature contracts** and **446 HANDOFFs** for `price-at-order-time`, `order_item.unit_price`, `line price source`, `price at the time of the order` and `menu price` returned **no feature owning the SOURCE of a line's price**. The four features that mention `order_item.unit_price` — **415**, **418**, **435**, **444** — treat it as a *number that exists*: the bill's input (415), a cross-check input (418), a membership input (435), and a *change* target (444). **None of them says where it comes from.**

## Adjacent work — recorded, NOT picked

- **The price-change trace and the reversibility of a change** — feature **444**.
- **Discounts and comps as a model** — feature **444**'s explicit exclusion; the money rules in features **408**, **410**, **411**, **420**.
- **The menu price's own history** — feature **444**'s explicit exclusion.
- **The role policy for who may override** — feature **403**.
- **The tax rate home** — feature **408**.
- **The bill's membership of lines** — feature **435**.
- **The bill-close route** — feature **415**.
- **The order-taking route** — feature **02**.
- **`MenuItem.is_prepared`** — feature **398**; **`MenuItem.unit`** — feature **392**.
- **Stock consumed by a compped dish** — feature **441** and the wider stock features.
