# Feature 455 — Two tables can carry the same label, and the label is the only name a waiter says out loud

> **Pick A of Daily Brainstorm 2026-11-07 (100th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Table`, verbatim (lines 64–71):
>
> ```python
> class Table(SQLModel, table=True):
>     __tablename__ = "table_"  # 'table' is a SQL reserved word
>
>     id: int | None = Field(default=None, primary_key=True)
>     label: str
>     section: str = "main"
>     seats: int = 4
>     x: int = 0        # for floor map coords
>     y: int = 0
> ```
>
> **`label` is a bare `str` with no constraint.** It is the only column on `Table` that a human would ever say out loud.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then real inserts):
>
> ```
>   Table(label="T1", section="main", seats=4)   -> ACCEPTED   id=1
>   Table(label="T1", section="main", seats=4)   -> ACCEPTED   id=2
>
>   SELECT COUNT(*) FROM table_ WHERE label = 'T1'   ->  2
>
>   two tables, one label.
> ```
>
> **⭐ AND THE LABEL IS THE ONLY THING THAT MAKES A TABLE FINDABLE BY A HUMAN.** Feature 448 — filed on 2026-11-06 — says, verbatim:
>
> > *"And note the neighbouring contrast: **`Table.label` exists.** A table has a name the operator says out loud ("table 4", "the corner one"). A bill — the thing that represents money received — does not. **The system that names its furniture does not name its receipts.**"*
>
> **That contrast is exactly right, and it is why this defect matters: the label is the table's entire human identity, and it is not unique.** Feature 448 used `Table.label` as the *example of a good practice* without asking whether the example holds. **It does not.**
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all feature contracts returns **zero** hits for a uniqueness rule on `Table.label`; the only two features that mention a `UniqueConstraint` at all are **448** (on a *new* `bill_number` column it proposes) and **404** (which notes that *"there is no `CHECK`, no `UniqueConstraint` beyond primary keys"*). **Nothing proposes one for the label that already exists.**
>
> **⭐ AND THE CORPUS ALREADY KNOWS THAT LE31 HAS NO CONSTRAINTS AT ALL.** Feature 404 states it verbatim: *"**Not one declared type is enforced by the database.** `grep -rn 'Constraint' backend/` returns **no output** — there is no `CHECK`, no `UniqueConstraint` beyond primary keys, and no `STRICT`."* **This slice adds the first one, on the column that carries the operator's vocabulary.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a duplicate label — the corpus confirms it, and feature 414 records that the table-capacity rule is likewise **defensive rather than reactive**). The honest framing: **the schema permits two objects to share the one name the operator uses to refer to them.**

## Goal

Make the label **mean one thing**: **exactly one table per label**, so that when the waiter says *"table 4"* there is exactly one table 4.

The concrete outcome: **the database refuses a second table with an existing label**, and the label a waiter says is unambiguous by construction.

## Scope

**In scope (v1):**

- **A uniqueness rule on `Table.label`** — a `UniqueConstraint` (or an equivalent index plus a guarded write path), so that **two tables cannot carry the same label**.
- **One decision about the scope of the uniqueness** — globally unique, or unique **per section**. *Recorded default: **globally unique**.* **The implementer must record the choice** (see *Open questions* 1); the reason the default is global is that the waiter says *"table 4"* and **does not say "table 4 in the terrace"** — the section is a floor-plan concept, not part of the spoken name.
- **A regression test** that fails on today's code and passes on the fixed code: inserting a second table with an existing label is **refused**.
- **A rule for what happens when a table is renamed** — whether the old label is released or kept as a tombstone. *Recorded default: the old label is released.* **This is the implementer's call to record**, per the corpus's established precedent.
- **One line in `features/01-table-management.md`**, whose data model line reads `Table (id, label, section, seats, x, y)`, so the contract and the schema agree on the constraint.

## Out of scope (v1)

- **`Table.status`, the double-seating guard, and the release path.** That is **feature 388** — filed, `build`. This slice does not add a status column and does not add or modify a route.
- **The table-capacity rule** (`party_size` vs `seats`). That is **feature 414** — filed. This slice does not compare a party to a table.
- **The bill's human-facing identity.** That is **feature 448** — filed. **448 proposes a `UniqueConstraint` on a `bill_number` column that does not exist yet; this slice proposes one on a column that does.** **The two are independent and must not be merged.**
- **A `CHECK` constraint or `STRICT` tables.** That is **feature 404** — filed. **This slice adds the first `UniqueConstraint`; 404 adds the first `CHECK`. They are separate slices with separate precedents.**
- **The schema-evolution mechanism.** That is **feature 446** — filed. **This slice DOES depend on 446**: a `UniqueConstraint` is a table-level change and `create_all()` cannot alter an existing table. **See *Dependencies*.**
- **Any change to `Visit`, `OrderItem`, `Bill`, `StockEntry`, `Batch`, `MenuItem` or `Shift`.**
- **Renaming the existing tables.** If a live database already holds two tables labelled "T1", the constraint cannot be added until they are renamed — **that is an operational cleanup for the owner, not a migration this slice performs.** Recorded in *Open questions* 2.
- **A floor-plan UI change.** The mock-up is `index.html`; feature 01's scope. This slice does not restyle it.
- **Alembic.**

## Description

### The defect, as observed in LE31's own code on 2026-11-07

`Table.label` is `str` — no `max_length`, no constraint, no index, and **not even a `Field()`**: it is a bare annotation, so SQLModel gives it the default `VARCHAR` with no length.

**Executed:**

```
  Table(label="T1", section="main", seats=4)   -> ACCEPTED   id=1
  Table(label="T1", section="main", seats=4)   -> ACCEPTED   id=2

  SELECT COUNT(*) FROM table_ WHERE label = 'T1'   ->  2
```

**Executed — the column's declared shape:**

```
  PRAGMA table_info(table_)
    id      INTEGER  primary key
    label   VARCHAR          <- no NOT NULL, no UNIQUE, no index
    section VARCHAR
    seats   INTEGER
    x       INTEGER
    y       INTEGER
```

### ⭐ Why this is a first-party defect and not a nitpick

**1. The label is the operator's vocabulary, and it is the ONLY identifier a waiter uses.**

LE31's floor is a set of tables. The waiter says *"table 4"*. Every surface that shows the room shows the **label**. The `id` is a surrogate integer that is **never spoken** and is **not stable across a restore** — feature 448 makes exactly this point for bills (*"`Bill.id` is an auto-increment integer that is **never shown to a human**, is **not stable across a restore**"*). **The label is therefore load-bearing in a way `id` is not**, and it is the one field with no constraint.

**2. Two tables with one label makes the room ambiguous exactly where it must not be.**

A party is seated at table 1; the waiter looks up "table 1" and gets **two rows**. Which one has the party? **Nothing in the schema can answer**, because the two rows are identical in every field a waiter sees. The floor grid shows two tiles with the same name, and the order screen shows two visits.

**3. The failure is silent and it lands in the money.**

**A visit is bound to a `table_id`, not to a label** — `Visit.table_id: int = Field(foreign_key="table_.id")`. So the *data* is fine: the party is attached to the right row. **The ambiguity is in everything that reads the floor by name.** That is where the wrong party, the wrong bill and the wrong table get attached to each other in the operator's head — and the operator is the only human check in the system.

**4. LE31's charter names the label as the operator's handle, and the schema does not back it up.**

`features/01-table-management.md`'s own Description reads: *"Tap a **free** table → 'Seat party' → enter `party_size`, `adults`, `children` → confirm."* — **the tap is on a named tile.** Feature 24 (`visual-table-layout-v2`) lists `Table (existing) — id, label, section, seats, x, y` and builds the floor map from the label. **The label is the floor map's own identity.**

### ⭐ The corroboration is inside the corpus already

**Feature 448** (filed yesterday, 2026-11-06) uses `Table.label` as the exemplar of a well-named entity:

> *"**`Table.label` exists.** A table has a name the operator says out loud ("table 4", "the corner one")."*

**Feature 414** (the table-capacity rule) writes its test fixture as:

```python
table = Table(label="T1", section="main", seats=4, x=0, y=0)
```

— i.e. **the corpus itself treats "T1" as *the* name of *the* table.**

**Neither feature asks whether the label can be shared.** A concept sweep for *"is a table's name ambiguous"* returns **zero** hits, because the *concept* ("table identity") is covered — by 388, by 448, by 414 — while the *instance* (**the label is not unique**) is not.

**This is the *seventh* finding shape: a covered concept with an uncovered instance.** The corpus knows what a table is called. It has never checked whether two tables can be called the same thing.

### Why this lands before the floor map is built

The cheapest moment to add a uniqueness constraint is **before any row exists**. Today there is **one write path for a `Table` in the whole backend** — `features/01-table-management.md` describes it and the router file `tables.py` has only `list_tables` and `seat_party`; **there is no route that creates a table at all.** So the constraint is free today, and **becomes a data-migration problem the moment the first table-creation route ships.**

## Data model

**One constraint. No new table. No new column.**

```
  BEFORE (today)
    table_
      id      INTEGER  primary key
      label   VARCHAR          <- nothing says this is unique
      ...

  AFTER (this slice)
    table_
      id      INTEGER  primary key
      label   VARCHAR   NOT NULL
                        UNIQUE            <- or UNIQUE(label) in __table_args__
      ...
```

**Two acceptable implementations, both satisfying the contract:**

1. **`__table_args__ = (UniqueConstraint("label", name="uq_table_label"),)`** on `class Table` — declarative, enforced by the database on both SQLite and Postgres, and the **first constraint of any kind in LE31's schema** (feature 404 records that `grep -rn 'Constraint' backend/` currently returns no output).
2. **A unique index** (`CREATE UNIQUE INDEX ... ON table_(label)`) created by the same change — equivalent enforcement, different mechanism. **Recorded as a choice for the implementer.**

**The contract's requirement, whichever is chosen:**

- **The database refuses a second table with an existing label.** Not the application — the database.
- **The refusal is an `IntegrityError` the write path handles**, and the error names the label, so the operator is told *"table T1 already exists"* rather than getting a stack trace.
- **`label` becomes `NOT NULL`.** A table with no name cannot be referred to by a waiter, and a null label in a unique column is a hole in the rule (SQLite and Postgres both allow **multiple NULLs** in a unique column — **so a nullable label would defeat the constraint entirely**).

**⭐ The `NOT NULL` is not a detail — it is half the rule.** Executed consideration: a `UniqueConstraint` over a **nullable** column permits any number of rows whose label is `NULL`, because `NULL != NULL` in SQL. **A table with a null label would be a table with no name, and there could be many of them.** The constraint must be `NOT NULL` + `UNIQUE`.

**Precedent for the enforcement shape:** feature 404 records that LE31 has **no** `CHECK`, no `UniqueConstraint` beyond primary keys and no `STRICT`. **This slice adds the first `UniqueConstraint`; the precedent it sets must be recorded** — exactly as feature 400 did when it noted that *"A `UniqueConstraint` **would be the first constraint of any kind in LE31's schema**"*.

## Implementation steps

1. **Write the failing test first.** A test that inserts two tables with the same label and asserts the second is refused. **On today's code it PASSES the insert** — show it succeeding, then show it failing after the fix. **A test that only ever passed proves nothing.**
2. **Decide and record the scope of the uniqueness** — global, or per section. *Recorded default: global.* **Record the choice in the code.**
3. **Add the constraint** to `class Table` via `__table_args__`, or add the unique index. **Add `NOT NULL` to `label` in the same change** — see *Data model* for why the two are one rule.
4. **Handle the `IntegrityError` in the table-creation write path** — with a message naming the conflicting label. **There is no such route today**; if one is being added in the same PR, it must handle it. **If no route exists, the constraint still lands and the handling is deferred to the route's own feature — recorded.**
5. **Update `features/01-table-management.md`**'s data-model line to state the constraint, so the contract and the schema agree — **the same one-line edit feature 388 makes for its status column.**
6. **Add the tests:**
   - a second table with the same label is **refused**;
   - a table with a **null label** is refused (the `NOT NULL` half);
   - two tables with **different** labels are accepted;
   - the same label in **different sections** — accepted or refused, **according to the recorded scope decision**;
   - the error message **names the label**.
7. **Record the precedent.** A note that this is **the first `UniqueConstraint` in LE31's schema**, and a pointer to feature 404 (which owns the `CHECK`/`STRICT` family) so the two do not contradict each other.

## Telegram interaction if any

**None.** This slice touches no bot command and no handler. The cook bot has no table concept at all — the floor is the waiter's surface.

**The one relationship worth stating:** a unique label makes the waiter's spoken reference unambiguous, and **the waiter's spoken reference is what the cook hears when an order is called** ("table 4, two tiramisu"). **A duplicate label makes the kitchen call ambiguous too.** **That is the reason this is more than a tidiness rule — but it is a consequence, not a separate scope, and no bot change is proposed here.**

## Dependencies

- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — this slice is BLOCKED on it.** A `UniqueConstraint` (and a `NOT NULL` on an existing column) is a **table-level change that `create_all()` cannot make on an existing table** — it creates missing tables and never alters an existing one. **446 must land first, or this slice must land in the same PR, or the constraint will be written, merged, deployed, pass its tests, and not exist in the running database.** **This is the upstream-of-filed-work condition in its clearest form**, and 446's own contract names features 408, 415, 420, 421, 435, 438, 439, 442, 443 and 445 as blocked on it — **this feature must be added to that list.**
- **Feature 388 (`le31-table-state-machine`) — adjacent, not blocking.** 388 adds a `status` column to `Table` and does **one edit to `features/01-table-management.md`**. **If 388 and this slice land together, they must both edit that file — the edits must not conflict.** 388 does not add a uniqueness rule and this slice does not add a status column.
- **Feature 404 (`le31-sqlite-tables-not-strict`) — adjacent, not blocking.** 404 owns the `CHECK`-constraint family and the `STRICT` tables. **This slice adds the first `UniqueConstraint`; 404 adds the first `CHECK`.** They are separate slices and **must not be merged** — a reviewer must be able to check each on its own. **The precedent this slice sets (the first constraint of any kind) must be recorded so 404's contract can reference it.**
- **Feature 414 (`le31-table-capacity`) — adjacent, not blocking.** 414 owns `party_size` vs `seats`. It writes a fixture `Table(label="T1", ...)` — **that fixture remains valid under this slice** (one table, one label). **No conflict.**
- **Feature 448 (`le31-a-bill-has-no-human-facing-identity`) — adjacent, not blocking.** 448 proposes a `UniqueConstraint` on a **new** `bill_number`. **This slice proposes one on an **existing** column. They are independent.** 448's reasoning about *global* uniqueness (*"the number is unique **globally**, not per day"*) is a **useful precedent for this slice's scope decision** — record it as such.
- **Feature 24 (`visual-table-layout-v2`) — a consumer, not a dependency.** It reads the label to draw the floor map. **With a unique label, the map is unambiguous.** **No change to 24 is proposed.**

## Open questions

1. **Globally unique, or unique per section?** **Recorded default: globally unique.** The waiter says *"table 4"* and **not** *"table 4 in the terrace"*. The section exists for the floor plan, not for speech. **The implementer must record the choice.** (If per-section is chosen, the constraint is `UniqueConstraint("section", "label")` — and **the spoken ambiguity remains**, which is the reason the default is global.)
2. **What happens to existing duplicate labels?** **Recorded default: this slice does not migrate data.** The charter's v1 policy is `init_db()`, and **there is no table-creation route in the shipped backend**, so no duplicate labels can exist in a database this code created. **If a live database does hold duplicates, they must be renamed by the owner before the constraint is added** — and that is **an operational cleanup, not a migration this slice performs.** **Recorded so a later pass does not mistake the omission for an oversight.**
3. **Can a table be renamed, and does the old label stay reserved?** **Recorded default: the old label is released** — a rename frees the old name. **The alternative** (keeping the old label as a tombstone, so a waiter who says the old name gets *"that table was renamed"*) is **better for the operator and worse for the schema** (it needs a tombstone table or a status). **Owner decision; the implementer records it.**
4. **Should the label have a format?** *Recorded default: **no format constraint**.* A regex on table names is a product decision the owner has not made, and **a wrong regex is a rejection at the worst moment.** **Not decided here.**
5. **Is the constraint on `label` alone, or on `(section, label)`?** **Same question as 1, stated in DDL terms.** Recorded once and answered once.

## Why this matters

**Because a restaurant's floor is addressed by name, and LE31 lets two tables share a name.**

Every other identifier in the system is a surrogate integer that the operator never sees. The **label is the opposite**: it is the only identifier the operator *speaks*. And it is the only one with no constraint. The gap is not stylistic — **the system that names its furniture does not guarantee that the furniture has distinct names**, and the operator is the only human check that exists.

**The cost of the defect is not a crash.** It is a floor where "table 4" is ambiguous, a kitchen call that could go to the wrong table, and an operator who cannot tell which of two identical tiles holds the party — **because nothing in the schema can tell them either.** The visit is attached to the right row; only the *name* is ambiguous; and the name is what every human surface uses.

**The cost of the fix is one constraint.** One `UniqueConstraint`, one `NOT NULL`, one error message. **And today it is free**, because **no route creates a table** — the constraint can be added before the first table is ever written. **After the floor-map route ships, it becomes a data-migration problem.** The whole value of this slice is that it is cheap **now** and expensive later.

**It is the cheapest possible first constraint, and it sets the precedent.** Feature 404 records that LE31's storage layer enforces **nothing** — *"Not one declared type is enforced by the database."* This slice adds the **first** one, on the **one column that carries the operator's vocabulary**. **A later feature that adds a `CHECK` will be able to point at a precedent** — and a reviewer will be able to check that the precedent was deliberate.

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`DonnC/dura-pos`** — MIT ✓ §3.2 strictly-compatible, **★0 / ⒂0 = NO traction evidence in either direction**, 10,967 B README, Python (on-stack language), created in-window. Its glossary states, verbatim: *"**Event** | One recorded fact, such as `sale.completed`. It has a stable ID and is never edited. A correction is a new linked event."* **Recorded because a system that names every business object by a stable identity — and never edits it — is the discipline LE31's `label` lacks.**
- **`AlgoVyn/bikri`** — MIT ✓, ★1 / ⒂0 = **NO traction evidence**, 13,320 KB, TypeScript (off-stack). Its data model declares, verbatim: *"Every tenant-scoped D1 table starts with `tenant_id TEXT NOT NULL REFERENCES tenants(id)` and has **`PRIMARY KEY (tenant_id, id)`**; every reference to another tenant-scoped row is a **composite foreign key** … every UNIQUE rule and every index starts with `tenant_id`."* **The transferable idea is the *discipline of naming every rule and every index*, and of making the scope of uniqueness explicit rather than implicit.** **No code is adopted.**
- **`Famalth/lynx-pos`** (`famalthtechnologies/famalth-lynx-pos`) — Apache-2.0 ✓, ★3 / ⒂0 = **NO traction evidence**, 28,659 KB, JavaScript (off-stack), created **2026-10-21** = in-window. **Recorded as a lower-tier POS whose README is dominated by an installer, with its real content in a separate `WIKI.md`.** **Its relevance is bounded and stated plainly: it contributes no verified claim here, and that is recorded rather than dressed up.**

**Adjacent first-party work — recorded, NOT picked:**

| Feature | Why it is adjacent and NOT picked |
|---|---|
| **388** `le31-table-state-machine` | Owns `Table.status` and the double-seating guard. **Edits the same `features/01-table-management.md` line** — the two edits must not conflict. |
| **414** `le31-table-capacity` | Owns `party_size` vs `seats`. **Its fixture remains valid.** |
| **448** `le31-a-bill-has-no-human-facing-identity` | Owns a `UniqueConstraint` on a **new** `bill_number`. **This slice owns one on an existing column.** 448's *global* uniqueness reasoning is the precedent for *Open questions* 1. |
| **404** `le31-sqlite-tables-not-strict` | Owns the `CHECK` / `STRICT` family. **This slice adds the first `UniqueConstraint`; 404 adds the first `CHECK`. Not merged.** |
| **446** `le31-has-no-schema-evolution-mechanism` | **This slice is BLOCKED on it** — a constraint on an existing table is exactly the change `create_all()` cannot make. |
| **24** `visual-table-layout-v2` | **A consumer** of the label, not a dependency. |

**External source families fetched this pass (all raw, all re-derived from disk by the parent):**

- **GitHub Search** — 17 date-filtered queries + a 4-request qualifier probe, **21/21 HTTP 200**; aggregate `total_count` = **72,050**; **zero** 73-byte or 6-byte stubs; the **correct `pushed:>=` qualifier** was used and the **dead `pushed_at:>=` qualifier was proved dead by a paired probe** (`topic:restaurant` → 2,963; `pushed_at:>=2026-10-08` → **0**; `pushed:>=2026-10-08` → **583**; `created:>=` → 230). **The restaurant-shaped cluster is ALIVE.** Pipeline: **903 unique repos → 864 in-window → 285 created in-window (fresh) → 393 permissive**; **579 in-window repos were created BEFORE the window start** and are labelled as such.
- **HN Algolia** — 8 queries, 8/8 HTTP 200, **21 hits**, `title: null` = **0**. **4 of 8 queries genuinely returned `nbHits=0`** and are reported as counts, not failures. **0 HN items were promoted to a signal** — the "phone-first POS" query returned 12 hits, **none of them restaurant-related**.
- **OpenAlex** — 3 queries, 3/3 HTTP 200, `meta.count` = **4,076 / 5 / 0** — **distinct** (the filter was applied) and **none near corpus scale**; a diagnostic query for a nonsense term returned **0**, proving the filter is live. Abstracts were carried as **raw `abstract_inverted_index` dumps**, **never paraphrased**. **0 papers were promoted to a signal** — the family is **soft this pass**.
- **ProductHunt** — HTTP 200, 44,100 B (soft source; **not used for a pick**).
- **ScienceDirect** — **NOT RETRIEVABLE** (blocked on this VPS; not attempted).
