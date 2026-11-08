# Feature 458 — Two dishes may share the one name the waiter says out loud

> **Pick C of Daily Research 2026-11-08 (86th daily-research pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class MenuItem`, verbatim (lines 82–92):
>
> ```python
> class MenuItem(SQLModel, table=True):
>     __tablename__ = "menu_item"
>
>     id: int | None = Field(default=None, primary_key=True)
>     name: str
>     category: str
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)
>     unit: str = "piece"
>     is_prepared: bool = True    # if True, sales decrement a Batch
>     photo_url: str | None = None
> ```
>
> **`name` is a bare `str` with no constraint.** It is the only column on `MenuItem` that a human would ever say out loud.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then real inserts):
>
> ```
>   MenuItem(name='Tiramisu', category='dessert',  unit_price=6.00) -> ACCEPTED id=1
>   MenuItem(name='Tiramisu', category='desserts', unit_price=6.50) -> ACCEPTED id=2
>   MenuItem(name='Tiramisu', category='Dessert',  unit_price=7.00) -> ACCEPTED id=3
>
>   SELECT COUNT(*) FROM menu_item WHERE name='Tiramisu'  ->  3
>
>   distinct prices among them     -> 6.00, 6.50, 7.00
>   distinct categories among them -> dessert, desserts, Dessert
> ```
>
> **Three dishes, one name, three prices, three categories.** Which one is the tiramisu? **Nothing in the schema can answer.**
>
> **⭐ AND NO FEATURE OWNS IT.** A sweep over all **941** feature contracts and HANDOFFs in `features/` + `specs/` returns **zero hits** for a dish-name uniqueness rule — the searches `menu_item.{0,30}name.{0,30}unique`, `duplicate dish` and `two dishes.{0,20}name` all return **0**.
>
> **⭐ AND THE CORPUS ALREADY OWNS THE *OTHER* SPOKEN IDENTIFIERS — AND HALF OF THIS ONE.** Feature **455** (filed yesterday) owns **`Table.label`**, on the explicit argument that *"the label is the one identifier the operator speaks"* and that **a table's name must be unambiguous**. Feature **448** owns `Bill.bill_number`. Feature **433** owns the menu **category** normalisation. **Nobody owns the dish's name.** **This is the same defect shape as 455, on the other spoken identifier** — and the corpus normalised the *category* while leaving the *name*.
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **medium** for the demand (no operator has reported a duplicate dish name; the corpus confirms nobody owns the rule). The honest framing: **the schema permits two dishes to answer to one name — at different prices.**

## Goal

Make the dish name **mean one thing**: **exactly one dish per name**, so that when the waiter says *"tiramisu"* there is exactly one tiramisu, at exactly one price.

The concrete outcome: **the database refuses a second dish with an existing name**, and the name a waiter says is unambiguous by construction.

## Scope

**In scope (v1):**

- **A uniqueness rule on `MenuItem.name`** — a `UniqueConstraint` (or an equivalent unique index plus a guarded write path), so that **two dishes cannot carry the same name**.
- **One decision about the scope of the uniqueness** — globally unique, or unique per category. *Recorded default: **globally unique**.* **The implementer must record the choice** (see *Open questions* 1); the reason the default is global is that the waiter says *"tiramisu"* and **does not say "the tiramisu in the desserts category"** — the category is a screen-sorting concept, not part of the spoken name.
- **One decision about case sensitivity** — *Recorded default: **case-insensitive uniqueness** (i.e. `"Tiramisu"` and `"tiramisu"` are the same dish).* **The implementer must record the choice** (see *Open questions* 2); **the reason for this default is that a case-sensitive rule produces a constraint whose behaviour differs between SQLite and Postgres** — the exact defect class feature **453** filed about timezones.
- **A regression test** that fails on today's code and passes on the fixed code: inserting a second dish with an existing name is **refused**.
- **A rule for what happens when a dish is renamed** — whether the old name is released or kept as a tombstone. *Recorded default: the old name is released.* **This is the implementer's call to record**, per the corpus's established precedent (feature **455** recorded the same decision for the table label).
- **One line in `features/02-order-taking.md`** — the menu is read on the order-taking surface — so the contract and the schema agree on the rule.

## Out of scope (v1)

- **The menu *category* normalisation.** That is **feature 433** — filed, `build`. 433 proved by execution that `"dessert"`, `"Desserts"` and `"dessert "` are three distinct categories for one dish, and it owns the **normalisation** half. **This slice is the **name** half** — the half the operator speaks, as against the half the screen sorts by. **They are complementary and must not be merged.**
- **`Table.label` uniqueness.** That is **feature 455** — filed. **Same shape, different table.** 455 owns the table's spoken name; this slice owns the dish's. **A reviewer must be able to check each on its own.**
- **`Bill.bill_number` uniqueness.** That is **feature 448** — filed. The third spoken identifier.
- **`OrderItem.unit_price` mutability.** That is **feature 449** — filed.
- **A dish *variant* or *modifier* model** (a "tiramisu" and a "tiramisu of the day" as two products with one base name). That is a **product decision the owner has not made**, and it would need a new column and a new concept. **Not decided here — see *Open questions* 3.**
- **A `CHECK` constraint or `STRICT` tables.** That is **feature 404** — filed. **This slice adds a `UniqueConstraint`; 404 adds a `CHECK`. Separate slices with separate precedents.**
- **The schema-evolution mechanism.** That is **feature 446** — filed. **This slice DEPENDS on 446** — a `UniqueConstraint` is a table-level change and `create_all()` cannot alter an existing table. **See *Dependencies*.**
- **Any change to `Visit`, `OrderItem`, `Bill`, `StockEntry`, `Batch`, `Table` or `Shift`.**
- **Renaming the existing dishes.** If a live database already holds two tiramisus, the constraint cannot be added until one is renamed — **that is an operational cleanup for the owner, not a migration this slice performs.** Recorded in *Open questions* 4.
- **A menu UI change.** The mock-up is `index.html`; feature 08's scope. This slice does not restyle it.
- **Alembic.**

## Description

### The defect, as observed in LE31's own code on 2026-11-08

`MenuItem.name` is `name: str` — no `max_length`, no constraint, no index, and **not even a `Field()`**: it is a bare annotation, so SQLModel gives it the default `VARCHAR` with no length.

**Executed — the live DDL, read back from the created database:**

```sql
CREATE TABLE menu_item (
    id INTEGER NOT NULL,
    name VARCHAR NOT NULL,          <- NOT NULL, but no UNIQUE, no index
    category VARCHAR NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    unit VARCHAR NOT NULL,
    is_prepared BOOLEAN NOT NULL,
    photo_url VARCHAR,
    PRIMARY KEY (id)
)
```

**Executed — three dishes, one name:**

```
  MenuItem(name='Tiramisu', category='dessert',  unit_price=6.00) -> ACCEPTED id=1
  MenuItem(name='Tiramisu', category='desserts', unit_price=6.50) -> ACCEPTED id=2
  MenuItem(name='Tiramisu', category='Dessert',  unit_price=7.00) -> ACCEPTED id=3

  SELECT COUNT(*) FROM menu_item WHERE name='Tiramisu'  ->  3
  distinct prices     -> 6.00, 6.50, 7.00
  distinct categories -> dessert, desserts, Dessert
```

**And the whole schema's constraint census:**

```
  TOTAL CHECK constraints across 10 tables: 0
  UNIQUE constraints: bill -> ['visit_id']   (and nothing else)
  UNIQUE indexes:     {}
```

### ⭐ Why this is a first-party defect and not a nitpick

**1. The dish name is the operator's vocabulary, and it is the ONLY identifier a waiter uses.**

The waiter says *"tiramisu"*. Every surface that shows the menu shows the **name**. The `id` is a surrogate integer that is **never spoken** and is **not stable across a restore** — feature **448** makes exactly this point for bills (*"`Bill.id` is an auto-increment integer that is **never shown to a human**, is **not stable across a restore**"*). **The name is therefore load-bearing in a way `id` is not**, and it is the one field with no constraint.

**2. Two dishes with one name makes the menu ambiguous exactly where the money is decided.**

The waiter opens the menu and taps "tiramisu". **Which of the three?** The kitchen hears *"tiramisu"*. The bill line that gets created references a `menu_item_id`, so **the *data* is fine** — the party is attached to the right row. **The ambiguity is in everything that reads the menu by name**, which is where the wrong dish, the wrong price and the wrong batch get attached to each other in the operator's head — and **the operator is the only human check in the system.**

**3. The failure is silent and it lands in the money.**

`OrderItem.unit_price` is a **snapshot** written on the line — feature **449** owns that column and its mutability. So the price that lands on the bill is **whatever `unit_price` the chosen row carried**. **Two tiramisus at 6.00 and 7.00 means the customer can be charged either, and nothing in the schema can say which was intended.** The difference — 1.00 € here, more on a wine pairing — is exactly the kind of amount that is too small to be argued about and too large to be ignored over a year.

**4. LE31's charter names the dish as the thing the waiter says, and the schema does not back it up.**

Feature **02** is *Order Taking (Dining/Service Side)*; the waiter selects dishes **by name** from the menu. Feature **04** is the *Menu Photo Bot* — a photo becomes a dish, and the dish's name is what the owner types and what the waiter then selects. Feature **19** (*Menu Engineering & Item Profitability*) and feature **07** (*Demand Estimation*) both compute per-dish quantities from the order lines, keyed by the dish. **A duplicated name splits every one of those reports.**

### ⭐ The corroboration is inside the corpus already

**Feature 455** (filed yesterday, 2026-11-07) is the **exact same argument about a different table**, and it says so in its own words:

> *"**`Table.label` exists.** A table has a name the operator says out loud ("table 4", "the corner one")."*

**455 also says this:**

> *"⭐ AND THE LABEL IS THE ONLY THING THAT MAKES A TABLE FINDABLE BY A HUMAN."*

**That argument is stronger for the menu than for the floor.** On the floor, a table has a physical position (the `x`/`y` columns) that the waiter can also use. **On the menu, the name is the whole identifier.** And 455's own corollary applies: **the system that names its dishes does not guarantee that two dishes cannot share a name** — and unlike the floor, **there is no second handle to disambiguate with.**

**⭐ AND THE CORPUS ALREADY KNOWS THAT LE31 HAS NO CONSTRAINTS AT ALL.** Feature **404** states it verbatim: *"**Not one declared type is enforced by the database.** `grep -rn 'Constraint' backend/` returns **no output** — there is no `CHECK`, no `UniqueConstraint` beyond primary keys, and no `STRICT`."* **This slice adds one of the first `UniqueConstraint`s in LE31's schema.**

**⭐ AND THE CATEGORY HALF OF THIS PROBLEM IS ALREADY FILED.** Feature **433** proved by execution that `"dessert"`, `"Desserts"` and `"dessert "` are **three distinct categories** for the same dish. **The corpus normalised the category and left the name.** That is the *same* normalisation problem with the two halves split across two features — **and the name is the half the operator speaks.**

### Why it lands before the menu-management route ships

The cheapest moment to add a uniqueness constraint is **before any row exists**. Today the shipped backend has **one router** (`backend/app/routers/tables.py` — `list_tables`, `seat_party`) and **no menu route at all**: `features/04-menu-photo-bot.md` describes the intended flow and the code does not exist. So **the constraint is free today, and becomes a data-migration problem the moment the first menu-creation route ships** — because a `UniqueConstraint` cannot be added to a table that already holds a duplicate name, and a `create_all()`-only deployment would never add it to a live table anyway.

## Data model

**One constraint. No new table. No new column.**

```
  BEFORE (today)
    menu_item
      id        INTEGER  primary key
      name      VARCHAR          <- nothing says this is unique
      ...

  AFTER (this slice)
    menu_item
      id        INTEGER  primary key
      name      VARCHAR   NOT NULL
                                   UNIQUE            <- or UNIQUE(name) in __table_args__
      ...
```

**Two acceptable implementations, both satisfying the contract:**

1. **`__table_args__ = (UniqueConstraint("name", name="uq_menu_item_name"),)`** on `class MenuItem` — declarative, enforced by the database on both SQLite and Postgres, and **the same shape feature 455 uses for `Table.label`** — which means **one precedent, not two.**
2. **A unique index** (`CREATE UNIQUE INDEX ... ON menu_item(name)`) created by the same change — equivalent enforcement, different mechanism. **Recorded as a choice for the implementer.**

**The contract's requirement, whichever is chosen:**

- **The database refuses a second dish with an existing name.** Not the application — the database.
- **The refusal is an `IntegrityError` the write path handles**, and the error **names the dish**, so the operator is told *"tiramisu already exists"* rather than getting a stack trace.
- **Two dishes with different names are still accepted.** The constraint does not restrict the set of names — only their uniqueness.
- **A rename releases the old name.** *Recorded default.*

**⭐ The case-sensitivity question is not a detail — it is the difference between a rule that works and a rule that only works on one engine.**

SQLite's default collation for `VARCHAR` is `BINARY` — `"Tiramisu"` and `"tiramisu"` are **different strings**. Postgres's default collation depends on the database's locale and is **case-sensitive in the common configurations but not universally**. **A `UNIQUE` constraint that behaves differently in dev (SQLite) and prod (Postgres) is exactly the class of defect feature 453 filed about timezones** — *"dev and prod disagree"*, verbatim in 453's own title.

**The contract therefore requires the implementer to make the behaviour explicit on BOTH engines:**

- **If case-insensitive uniqueness is chosen** (the recorded default), the implementation must be explicit — a functional/expression index (`LOWER(name)`) or a normalised stored column — **and it must be verified on both SQLite and Postgres.** A plain `UNIQUE(name)` on a case-sensitive collation does **not** implement a case-insensitive rule, and **a plain `UNIQUE(name)` on a case-*sensitive* collation would be a silently different rule from the one the contract states.**
- **If case-sensitive uniqueness is chosen**, that must be **recorded explicitly and tested on both engines**, and the contract must say that `"Tiramisu"` and `"tiramisu"` are two dishes.

**Whichever is chosen, the choice must be recorded, tested on both engines, and written into the contract.** "It depends on the database" is not a recorded decision.

**Precedent for the enforcement shape:** feature **404** records that LE31 has **no** `CHECK`, no `UniqueConstraint` beyond primary keys and no `STRICT`; feature **455** adds the first `UniqueConstraint` on `Table.label`. **This slice adds one on `MenuItem.name`** — **the same mechanism, the same shape, a second table.** **That consistency is the point: 455 and this slice together establish that a spoken identifier in LE31 is unique, and a reviewer should be able to check both by the same standard.**

## Implementation steps

1. **Write the failing test first.** A test that inserts two dishes with the same name and asserts the second is refused. **On today's code the insert simply SUCCEEDS** — show it succeeding, then show it failing after the fix. **A test that only ever passed proves nothing.**
2. **Decide and record the scope of the uniqueness** — global, or per category. *Recorded default: **global**.* **Record the choice in the code.**
3. **Decide and record the case-sensitivity behaviour** — *recorded default: **case-insensitive**.* **Verify the behaviour on BOTH SQLite and Postgres** — this is not optional, and the test must assert it. **See *Data model*.**
4. **Add the constraint** to `class MenuItem` via `__table_args__`, or add the unique index. **Use the same shape as feature 455** so there is one precedent.
5. **Handle the `IntegrityError` in the menu write path** — with a message naming the conflicting dish. **There is no menu route today** (`backend/app/routers/` contains only `tables.py`); if one is being added in the same PR, it must handle it. **If no route exists, the constraint still lands and the handling is deferred to the route's own feature — recorded.**
6. **Update `features/02-order-taking.md`**'s data-model line to state the constraint, so the contract and the schema agree.
7. **Add the tests:**
   - a second dish with the same name is **refused**;
   - two dishes with **different** names are accepted;
   - the same name in **different categories** — accepted or refused, **according to the recorded scope decision**;
   - the case behaviour — `"Tiramisu"` and `"tiramisu"` — **asserted on both engines**;
   - the error message **names the dish**;
   - **a raw `INSERT` through the SQLAlchemy core is refused** — proving the constraint is enforced by the **database**, not only by the application. **This is the test that distinguishes a real constraint from a model-level validator**, and it is the test that makes this slice worth doing.
8. **Record the precedent.** A note that this is **the second `UniqueConstraint` in LE31's schema**, following feature **455** on `Table.label`, with a pointer to feature **404** (which owns the `CHECK`/`STRICT` family) so the three do not contradict each other.

## Telegram interaction if any

**None.** This slice touches no bot command and no handler.

**The one relationship worth stating:** feature **04** (the *Menu Photo Bot*) creates dishes from a photo, and **the name it produces is the name the owner typed**. **A bot that creates a dish whose name already exists is a bot that creates a second tiramisu** — and the cook, who sees the name on the ticket, cannot tell them apart either. **That is a consequence of the defect, not a separate scope, and no bot change is proposed here.**

## Dependencies

- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — this slice is BLOCKED on it.** A `UniqueConstraint` is a **table-level change that `create_all()` cannot make on an existing table** — it creates missing tables and never alters an existing one. **446 must land first, or this slice must land in the same PR, or the constraint will be written, merged, deployed, pass its tests, and not exist in the running database.** **446's own contract names features 408, 415, 420, 421, 435, 438, 439, 442, 443 and 445 as blocked on it — **this feature must be added to that list.**
- **Feature 455 (`le31-two-tables-can-carry-the-same-label`) — adjacent, not blocking, and the closest in shape.** 455 adds the first `UniqueConstraint` on `Table.label`. **This slice adds one on `MenuItem.name`, using the same mechanism.** **They must not be merged** — a reviewer must be able to check each on its own — but **455's scope decision is the precedent for this slice's**, and this slice's case-sensitivity decision is, in turn, the precedent 455 should point back at. **One of the two contracts must reference the other; both must not silently assume the other's decision.**
- **Feature 433 (`le31-menu-item-category-is-case-sensitive-free-text`) — adjacent, not blocking, and the closest in substance.** 433 owns the **category** normalisation. **This slice owns the **name** uniqueness.** **They are the two halves of one normalisation problem.** **Not merged** — but **when both land, the menu must be checked for the case where a name is duplicated *and* a category is duplicated at once**, and the two features must not each assume the other has covered it.
- **Feature 448 (`le31-a-bill-has-no-human-facing-identity`) — adjacent, not blocking.** 448 proposes a `UniqueConstraint` on a **new** `bill_number`. **This slice proposes one on an **existing** column.** They are independent. 448's reasoning about **global** uniqueness (*"the number is unique **globally**, not per day"*) is **a useful precedent for this slice's scope decision** — record it as such.
- **Feature 449 (`le31-order-item-unit-price-is-mutable-in-place-with-no-trace`) — a consequence, not a dependency.** 449 owns the line's price snapshot. **With a unique dish name, the price the waiter picks is unambiguous** — but 449's column still needs its own fix, and **this slice does not make 449's problem go away.**
- **Feature 404 (`le31-sqlite-tables-not-strict`) — adjacent, not blocking.** 404 owns the `CHECK`-constraint family and the `STRICT` tables. **This slice adds a `UniqueConstraint`; 404 adds a `CHECK`.** They are separate slices and **must not be merged** — a reviewer must be able to check each on its own. **The precedent this slice sets (the second constraint of any kind) must be recorded so 404's contract can reference it.**
- **Feature 02 / feature 04 — consumers, not dependencies.** 02 reads the menu by name on the order surface; 04 creates dishes from photos. **Neither needs a change** — the constraint makes both unambiguous.

## Open questions

1. **Globally unique, or unique per category?** *Recorded default: **globally unique**.* The waiter says *"tiramisu"* and **not** *"the tiramisu in the desserts"*. The category exists for the screen, not for speech. **The implementer must record the choice.** (If per-category is chosen, the constraint is `UniqueConstraint("category", "name")` — and **the spoken ambiguity remains**, which is the reason the default is global.)
2. **Is the uniqueness case-sensitive?** *Recorded default: **case-insensitive** ("Tiramisu" and "tiramisu" are one dish).* **This is not a detail** — a plain `UNIQUE(name)` is case-sensitive on SQLite's default `BINARY` collation, and **a rule that differs between SQLite and Postgres is the defect class feature 453 filed.** **The behaviour must be made explicit and verified on both engines, and recorded.** **The implementer must confirm the choice against the charter** — the charter does not speak to it.
3. **What if the owner genuinely runs two products under one name** (a "tiramisu" and a "tiramisu of the day")? *Recorded default: **the owner renames one of them** — a "tiramisu of the day" is a different product and deserves a different name. **The alternative (a variant column) is a schema and product decision that has not been made, and it is recorded here as a future option rather than decided.** **This is the honest cost of the slice, and it must be said out loud rather than designed around silently.**
4. **What happens to existing duplicate names?** *Recorded default: **this slice does not migrate data.** The charter's v1 policy is `init_db()`, and **there is no menu-management route in the shipped backend**, so no duplicate names can exist in a database this code created. **If a live database does hold duplicates, they must be renamed by the owner before the constraint is added** — and that is **an operational cleanup, not a migration this slice performs.** **Recorded so a later pass does not mistake the omission for an oversight.**
5. **Can a dish be renamed, and does the old name stay reserved?** *Recorded default: the old name is released — a rename frees the old name.* The alternative (keeping the old name as a tombstone, so a waiter who says the old name gets *"that dish was renamed"*) is **better for the operator and worse for the schema** — it needs a tombstone table or a status. **Owner decision; the implementer records it.** **Feature 455 recorded the same decision for the table label.**
6. **Should the name have a format?** *Recorded default: **no format constraint**.* A regex on dish names is a product decision the owner has not made, and **a wrong regex is a rejection at the worst moment.** **Not decided here.**

## Why this matters

**Because a restaurant's menu is addressed by name, and LE31 lets two dishes share a name.**

Every other identifier in the system is a surrogate integer that the operator never sees. The **name is the opposite**: it is the only identifier the operator *speaks*. And it is the only one with no constraint. The gap is not stylistic — **the system that names its dishes does not guarantee that the dishes have distinct names**, and the operator is the only human check that exists.

**The cost of the defect is not a crash.** It is a customer charged 7.00 for the tiramisu the waiter meant at 6.00, a kitchen call that could go to the wrong dish, and an owner who cannot tell which of two identical dishes sold more — **because nothing in the schema can tell them either.** The order line is attached to the right row; only the *name* is ambiguous; and the name is what every human surface uses.

**The cost of the fix is one constraint.** One `UniqueConstraint`, one error message, one test that proves the *database* refuses it. **And today it is free**, because **no route creates a dish** — the constraint can be added before the first dish is ever written. **After the menu route ships, it becomes a data-migration problem.** The whole value of this slice is that it is cheap **now** and expensive later.

**⭐ And it is the second spoken identifier to be made unique, which makes it a precedent rather than a one-off.** Feature 455 did the same for `Table.label` yesterday. Feature 448 proposes it for a bill number. **Three features, three spoken identifiers, one rule each: the thing the operator says must identify exactly one thing.** **This slice is the menu's turn — and it is the one where the operator says the name most often of all.**

**It also completes a normalisation the corpus already half-did.** Feature 433 proved that three spellings of one category are three categories, and fixed the category. **This slice fixes the name.** A menu whose categories are normalised but whose dish names are not is **a menu that is half-right** — and the half that is wrong is the half the waiter reads.

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`Ifazawezk/dukkan`** — MIT ✓ §3.2 strictly-compatible, **★1 / ⑂0 = NO traction evidence in either direction**, 1,732 KB, **Python ✓ on-stack** (FastAPI + SQLAlchemy 2), created **2026-11-01** and pushed **2026-11-05** = **in-window by both fields**, README read in full. Its stated design, verbatim: *"**Every change to stock is a row in a ledger**, so the number on the screen can always be explained line by line."* **Recorded because the surrounding sentence is the reason a duplicate name is dangerous in a POS:** *"so the owner finds out an item ran out when a customer asks for it."* **A product whose name can be shared is a product whose stock-out is invisible** — the same reasoning that makes 433's category normalisation matter. **Already filed by the 2026-11-06 pass; recorded here as converging evidence, not re-picked.**
- **`Apurba94/shopdesk`** — MIT ✓, **★0 / ⑂0 = NO traction evidence**, 15 KB, Python (on-stack), created and pushed **2026-11-04** = in-window by both fields, README read in full. Verbatim: *"**Bills** with discounts, and loose quantities such as 1.5 kg. Stock falls by itself, and **you cannot sell more than you hold**"* and *"**Slow stock:** money tied up in goods that are not selling"*. **Recorded because "you cannot sell more than you hold" is a product-identity rule as much as a quantity rule** — a product you cannot distinguish from another product is a product whose stock you cannot count. **No code is adopted** (whole-paisa money is a deferred v2 representation decision; feature 404 records it).
- **`kitsboy/slip`** — MIT ✓, **★0 / ⑂0 = NO traction evidence**, 151,716 KB, TypeScript (off-stack), created and pushed in-window. Verbatim: *"| Index discipline | reserve at invoice creation, release on cancel, burn on display, gap-limit scan (`src/core/indexes.ts`) |"* — the "gap-limit scan" is the closest analogue to this slice: **a product identity checked before it is used.** **Recorded as vocabulary only** — crypto domain, off-stack, no traction.

**Adjacent first-party work — recorded, NOT picked:**

| Feature | Why it is adjacent and NOT picked |
|---|---|
| **455** `le31-two-tables-can-carry-the-same-label` | Owns `Table.label` uniqueness. **The identical argument, on a different table. This slice is the second `UniqueConstraint` and must be separately reviewable.** |
| **448** `le31-a-bill-has-no-human-facing-identity` | Owns a `UniqueConstraint` on a **new** `bill_number`. **This slice's is on an existing column.** Independent. |
| **433** `le31-menu-item-category-is-case-sensitive-free-text` | Owns the menu **category** normalisation. **This slice owns the menu **name** uniqueness.** **The two halves of one problem — not merged.** |
| **404** `le31-sqlite-tables-not-strict` | Owns the `CHECK` / `STRICT` family. **This slice adds a `UniqueConstraint`; 404 adds a `CHECK`.** Not merged. |
| **446** `le31-has-no-schema-evolution-mechanism` | **This slice is BLOCKED on it** — a constraint on an existing table is exactly the change `create_all()` cannot make. |
| **449** `le31-order-item-unit-price-is-mutable-in-place-with-no-trace` | Owns the line's price snapshot. **A consequence of this slice, not a dependency.** |
| **02 / 04** | **Consumers** of the menu by name. **No change proposed to either.** |

**External source families fetched this pass (all raw, all re-derived from disk by the parent):**

- **GitHub Search** — 14 date-filtered queries + a 4-request qualifier probe, **18/18 HTTP 200**; aggregate `total_count` = **19,648**; **zero** 73-byte or 6-byte stubs; the **correct `pushed:>=` qualifier** was used and the **dead `pushed_at:>=` qualifier was proved dead by a paired probe** (`topic:restaurant` → 2,972; `pushed_at:>=2026-11-01` → **0**; `pushed:>=2026-11-01` → **169**; `created:>=2026-11-01` → **45**). **The restaurant-shaped cluster is ALIVE.** **30 candidates verified by a direct `GET /repos/{owner}/{repo}`** plus a README fetch: **10 permissive / 20 licence-incompatible**, **30/30 in-window by BOTH `created_at` AND `pushed_at`**, and **every permissive candidate carries ★0 or ★1 and ⒂0 — NO traction in either direction.**
- **HN Algolia** — 10 queries, 10/10 HTTP 200, **30 hits**, `title: null` = **0**; **4 of 10 queries returned `nbHits = 0`** and are reported as counts. **All 30 hits read; 0 promoted to a signal** — the largest bucket (`point of sale`, 17 hits) holds **zero POS items**, and the nearest misses are *"Waiter Making 75K in NJ"* (a person, not software) and a **Roblox food-delivery game**.
- **OpenAlex** — 9 queries, 9/9 HTTP 200, `meta.count` = **611 / 626 / 886 / 56 / 66 / 29 / 57 / 3,113** — distinct; a nonsense-term control returned **0**, proving the filter is live. Abstracts carried as **raw `abstract_inverted_index` dumps**, never paraphrased. **0 papers promoted to a signal** — the family is **soft this pass**.
- **PyPI** — 10/10 HTTP 200; **4 in-window releases** (`fastapi` 0.162.1/0.162.2, `sqlalchemy` 2.0.56/2.1.7/2.0.57/2.1.8, `pydantic` 2.14.3); `sqlmodel`, `aiogram`, `uvicorn`, `alembic`, `httpx` = **0 in-window**. **No pin-bump proposed** — a pin bump needs a CHANGELOG read this pass did not perform, and the `sqlmodel` 0.0.42 → 0.0.48 gap is **unchanged since 2026-10-05**.
- **GitHub `release.atom`** — 9/10 HTTP 200, **90 `<entry>` elements**; `sqlmodel/sqlmodel` = **0 entries** (valid empty feed); `python-telegram/bot` = **HTTP 404** (9 B) — **the repository path is wrong; the feed does not exist there.**
- **EU** — 5/5 HTTP 200; ECB daily XML `time='2026-11-06'`, **USD = 1.1165**; ECB Data API CSV with 5 daily rows; CNIL EN/FR RSS with 10 items each; **EUR-Lex ELI = HTTP 200 with the real GDPR document — clearing the 2026-11-06 pass's EUR-Lex blocker on the ELI path.**
- **ScienceDirect** — **NOT RETRIEVABLE** (blocked on this VPS; not attempted).
