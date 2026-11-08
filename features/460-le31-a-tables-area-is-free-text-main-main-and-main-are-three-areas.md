# Feature 460 — A table's area is free text: "Main", "main" and "MAIN" are three areas

> **Pick B of Daily Brainstorm 2026-11-08 (99th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Table`, verbatim (lines 64–72):
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
> `section` is a bare `str` with a **default of `"main"`** and **no constraint, no index and no `Field()`**.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then real inserts):
>
> ```
>   Table(label="B1", section="Main", seats=2, x=1, y=1)  ACCEPTED
>   Table(label="B2", section="main", seats=2, x=2, y=2)  ACCEPTED
>
>   SELECT DISTINCT section FROM table_   ->  ['Main', 'main']
>
>   PRAGMA table_info(table_) for `section`  ->  VARCHAR, notnull=0, no UNIQUE, no index
>   PRAGMA index_list(table_)              ->  []          (no index at all on the table)
> ```
>
> **Two sections that are the same word in different case. Nothing can tell them apart.**
>
> **⭐ THE CORPUS ALREADY OWNS THE *IDENTICAL* DEFECT ON THE *SIBLING* COLUMNS — AND NOBODY OWNED THE THIRD ONE.** Feature **431** (`le31-menu-item-category-is-case-sensitive-free-text`) proved by execution that `"dessert"`, `"Desserts"` and `"dessert "` are **three distinct categories** for one dish, and filed the canonicalisation rule. Feature **455** (`le31-two-tables-can-carry-the-same-label`) proved that **two tables may carry the same label** — *"the label is the one field the operator speaks and the one field with no constraint"* — and filed the uniqueness rule. **`Table.section` is the third free-text identifier on the same table, and it is owned by nobody.**
>
> **A corpus-wide sweep over 947 feature contracts and HANDOFFs** finds **zero** hits for a rule on `Table.section`:
>
> | pattern | hits |
> |---|---|
> | `Table.section` / `section:` outside cross-section prose | **0** (the only hits are feature 388's and 455's *code block quoting the model*, and feature 08's mock-up data) |
> | `floor.{0,30}collision` | **0** |
> | `coordinate.{0,40}unique` | **0** |
> | `overlapping table` | **0** |
>
> **Bucket: v1.** Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect (three columns, two filed, one not); **medium** for the demand framing (no operator has reported a broken floor plan — but **no route in the shipped backend creates a table at all**, so there is no report to have been made).

## Goal

Make **a table's area mean one thing**, so that the floor map can group tables by area and a query for *"the terrace"* returns the terrace and not a half of it.

**The single sentence this feature exists to make true:** *a table's area is one of a known set of areas, written one way.*

**Two concrete outcomes**, and the implementer must decide which combination is right — see *Open questions*:

1. **One spelling per area.** `"Main"`, `"main"` and `"MAIN"` are **one** area, not three. The mechanism is either **a canonicalisation rule** (feature 431's shape) **or a fixed vocabulary** (feature 431's option (c)), and **the implementer must record which**.
2. **One home for the vocabulary.** If the vocabulary is fixed, it lives in **one** place — `backend/app/config.py` — and **not** in a `CHECK` constraint string, which would duplicate it in the schema and in the code.

## Scope

**In scope (v1):**

- **One decision about the mechanism**: canonicalise-on-write (feature 431's shape — a helper that normalises a section string before it is stored) **or** a fixed vocabulary (a list in `config.py` plus a validation), **or both**. *Recorded default: **canonicalise-on-write plus an open vocabulary**, i.e. feature 431's option (a)* — the reason is stated in *Open questions* 1.
- **One helper** that normalises a section string, and **one place** it is called.
- **A regression test** that fails on today's code and passes after the fix: writing `"Main"` and `"main"` leaves **one** area, not two.
- **The recorded decision** on *whether the vocabulary is fixed or open* and *on case handling* — **recorded, not guessed.**
- **A one-line amendment to feature 431** so the two canonicalisation rules do not drift apart — 431 owns `MenuItem.category`, this slice owns `Table.section`, and **the helper should be shared if the mechanism matches**.

## Out of scope (v1)

- **`MenuItem.category`.** That is **feature 431** — filed, `build`. 431 proved by execution that `"dessert"`, `"Desserts"` and `"dessert "` are three distinct categories. **Same shape, different column. They must not be merged** — 431 owns the *menu*, this slice owns the *floor*. **If the two mechanisms are identical, they should share one helper**; that is a *shared implementation*, not a merged contract.
- **`Table.label` uniqueness.** That is **feature 455** — filed. Same table, **different column**: 455 owns the table's *name* (a `UniqueConstraint`); this slice owns the table's *area* (a normalisation/vocabulary rule). **455 adds the first `UniqueConstraint`; this slice adds no constraint at all.** They are independent and a reviewer must be able to check each on its own.
- **`Table.x` / `Table.y` uniqueness.** The floor-map coordinates are **also unconstrained** — two tables may sit at the same `(x, y)` (executed: `SELECT COUNT(*) FROM table_ WHERE x=3 AND y=7` → **2**). **That is a *different* rule with a *different* mechanism** (a `UniqueConstraint` over a coordinate pair, not a spelling rule), and **it is not owned by any feature either.** **It is recorded here so a later pass can file it — it is NOT taken by this slice**, because a coordinate constraint and a spelling rule are separate changes and this slice's mechanism (normalise the string) cannot express either.
- **`Table.status`.** Feature **388** owns the status column and the double-seating guard.
- **`Table.seats` vs `Visit.party_size`.** Feature **414** owns the capacity rule.
- **A menu UI change.** The mock-up is `index.html`; feature 08's scope. This slice does not restyle it.
- **A `CHECK` constraint or `STRICT` tables.** Feature **404** owns that family. **Note**: a `CHECK (section IN (...))` **would** express a fixed vocabulary — but it would put the vocabulary in **the schema**, duplicating whatever `config.py` says, and it would be **unenforced on SQLite** (feature 427's finding: SQLite never enables `PRAGMA foreign_keys`, and a `CHECK` on a non-`STRICT` table is only as strong as the table). **Recorded, not decided here.**
- **Alembic / schema evolution.** Feature **446** owns that. **This slice needs no column, so it does not need 446** — unless the implementer chooses a `CHECK` constraint, in which case **446 becomes a dependency**.
- **A floor-map drag-and-drop editor.** Feature **01** and feature **24** own the UI.

## Description

### The defect, as observed in LE31's own code on 2026-11-08

`Table.section` is `section: str = "main"` — a bare annotation with a default, so SQLModel gives it a plain `VARCHAR` with **no length, no NOT NULL, no UNIQUE, and no index** (`PRAGMA index_list(table_)` → `[]`).

The floor map is **the surface this column exists for.** Feature **01** specifies `Table (id, label, section, seats, x, y) -- x/y for floor map`, and feature **24** is *"Visual table layout v2"*, whose stated rationale is *"Operators want a floor map, not a list"*. **A floor map is grouped by area**: the terrace, the bar, the main room, the patio. **`section` is the only column that can group them.**

**So the one column that makes the floor map a floor map is the one column whose value space is unbounded free text.**

### Why "Main" and "main" is a real defect and not a cosmetic one

The failure mode is the one the corpus has already learned to look for — **a plausible business number instead of an error**:

- The floor map groups tables by `section`. A query for the main room is `WHERE section = ?`.
- With `"Main"` and `"main"` both present, **the operator asks for the main room and gets half of it.** The other half is still on the floor, still seated, still waiting — and it is **invisible to the query**.
- **Nothing errors.** The query returns a plausible set of tables. A manager checking "how many are in the main room" gets a number, and the number is wrong.

**And the direction is the quiet one.** A table in `"Main"` and a table in `"main"` are **the same area spelled two ways**, so the error is a **split**, not an extra. The count is *smaller* than reality, and the missing tables are the ones the waiter seated most recently. **A capacity check or a "which tables are free" query built on `section` would leave the newest table invisible.**

### The third instance of a shape the corpus has already filed twice

| Column | Table | Owner | Status |
|---|---|---|---|
| `MenuItem.category` | `menu_item` | feature **431** | filed, `build` — three spellings of one category proved by execution |
| `Table.label` | `table_` | feature **455** | filed, `build` — two tables, one label proved by execution |
| **`Table.section`** | **`table_`** | **nobody** | **this feature** |

**Feature 455 is the closest sibling and it states the argument this slice needs, in its own words:** *"the label is the one field the operator speaks and the one field with no constraint."* **`section` is spoken too** — *"table 4 in the terrace", "the corner one in the bar"* — and it is the field the floor map **groups by**, which is a stronger claim than being spoken.

**And the corpus has already noticed the *pattern* without noticing this instance.** Feature **431** records, verbatim: *"**⭐ The corpus already knows this gap exists and has never filed it.**"* — it found that the corpus normalised the *category* and left the *name*. **The same corpus, the same pass family, normalised the *menu category* and the *table label* and left the *table's area*.**

### The instance sweep, not the concept sweep

A corpus-wide sweep over **947** feature contracts and HANDOFFs:

| pattern | hits |
|---|---|
| `floor.{0,30}collision` | **0** |
| `coordinate.{0,40}unique` | **0** |
| `overlapping table` | **0** |
| `same position` | 7 — all in **HANDOFF** prose about unrelated "same position" topics, none about floor coordinates |
| `Table.section` outside model-quoting code blocks | **0** |

**The concept is covered (the corpus knows free-text identifiers are a problem). The INSTANCE is uncovered: nobody owns the table's area.**

## Data model

**No schema change is required by the recorded default.** The canonicalisation is an **application-level** rule, for the same reason feature **411**'s money guard is application-level and feature **404**'s `CHECK` family is *belt-and-braces*: **a `CHECK` on a non-`STRICT` SQLite table is not a portable constraint, and a vocabulary duplicated into a DDL string is a second copy to drift.**

```python
# backend/app/config.py — ONE home for the vocabulary (if the vocabulary is fixed)
#
# Recorded default: the vocabulary is OPEN (any string a restaurant wants),
# and the canonical form is lower-cased and stripped.
#
# A restaurant that adds a "Kids" section should not need a code change.
# See Open questions 1 and 2.
SECTION_CANONICAL_CASE = "lower"


# backend/app/services/tables_service.py  (or models.py if no services dir yet)
def canonical_section(raw: str | None) -> str:
    """The ONE spelling of a table's area.

    Feature 460: "Main", "main" and "MAIN" are one area.
    Feature 431 owns the SAME shape for MenuItem.category -- if the two
    mechanisms end up identical, they should share ONE helper, not two
    copies.  Record which was chosen.
    """
    if raw is None:
        return "main"
    return raw.strip().lower()
```

**Notes for the implementer:**

- **The default value in the model is `"main"` — lower-case.** That is the canonical spelling, and it is already correct. **The defect is not the default; it is that nothing constrains a *write* to match it.** Feature 431's finding generalises: a default value on a free-text column is **a starting value, not a constraint**.
- **Do NOT put the vocabulary in a `CHECK` constraint string.** Two copies — `config.py` and the DDL — will drift, and feature **442** has already recorded that LE31's enum columns are `VARCHAR` with **no membership constraint**. **If the owner chooses a fixed vocabulary, put it in `config.py` and validate in the application; a `CHECK` is optional reinforcement only** (feature 411's precedent).
- **Case handling is a decision, and the two databases do not agree by default.** SQLite's default collation is `BINARY`; Postgres's default collation does **not** agree with it on `"Main"` vs `"main"`. **Feature 453** filed exactly this class of defect (*"a constraint that differs between dev and prod"*). **Recorded default: normalise in Python to lower-case on write**, so the stored value is canonical and the comparison is a plain `=`. **The implementer must record the choice** — see *Open questions* 2.
- **This slice adds no index.** If the implementer adds one for the floor-map query, that is a **performance** decision, not a correctness one, and it must be recorded separately.

## Implementation steps

1. **Decide the mechanism** (canonicalise-on-write / fixed vocabulary / both) and **record the decision** in `config.py` and in *Open questions* below. **Do not start implementing before the decision is recorded** — feature 431's precedent is that the recorded decision is what stops the next pass from re-deriving it.
2. **Add `canonical_section()`** — one helper, one home.
3. **Call it at the write path**: wherever a `Table` row is created or its `section` is updated. **There is currently no route that creates a table** (the shipped backend's `routers/` contains only `tables.py`, and it has no create route) — **so the helper may have no call site today.** **That is fine and it is also the point: the rule must exist before the first table is written, exactly as feature 455 argues for the label.** **Record the intended call site in the HANDOFF.**
4. **Write the regression test**: insert two tables with `section="Main"` and `section="main"`, and assert `SELECT DISTINCT section FROM table_` returns **one** value. **This test fails on today's code** (two values) and passes after the fix.
5. **Add a one-line amendment to feature 431** naming this feature, so the two canonicalisation rules do not drift — 431 owns `MenuItem.category`, this owns `Table.section`, and **if the mechanisms match they should share one helper**.
6. **Record the decision** about whether the vocabulary is open or fixed, and the case rule, in the code comment and in the HANDOFF.

## Telegram interaction if any

**None.** This feature has **no Telegram surface.** It constrains a value that is written by an operator on the floor-map surface (feature 01 / 24's UI), not by the cook bot.

**One consequence must be recorded for the owner, though:** if the restaurant already has tables whose sections are spelled inconsistently, **the canonicalisation helper does not rewrite them.** Existing rows keep their spelling until someone edits them. **The implementer must NOT write a migration that rewrites existing rows** — that is a data migration, and feature **446** owns the schema-evolution mechanism and feature **409** owns the open-decisions register. **Recorded in *Open questions* 3.**

## Dependencies

| Feature | Relationship | Why it matters |
|---|---|---|
| **431** (`MenuItem.category` canonicalisation) | **Sibling — and the source of the mechanism** | 431 owns the **identical shape** on the menu. **If the mechanism matches, they should share one helper.** This slice must not re-invent 431's mechanism under a different name. |
| **455** (`Table.label` uniqueness) | **Sibling — same table, different column** | 455 owns the table's **name** (a `UniqueConstraint`). This slice owns the table's **area** (a spelling rule). **455 adds the first `UniqueConstraint`; this adds no constraint.** Independent. |
| **404** (CHECK / STRICT family) | **Why the rule is in the application** | A `CHECK` on a non-`STRICT` SQLite table is not portable, and a vocabulary in DDL is a second copy. |
| **442** (enum columns are VARCHAR) | **Precedent** | Enum columns carry no membership constraint — so a free-text column needs an application rule. |
| **453** (SQLite vs Postgres collation) | **Why the case rule is decided in Python** | The two engines do not agree on `"Main"` vs `"main"`. Normalising on write makes the comparison plain `=`. |
| **411** (money precision) | **Precedent for the shape** | Application-level guard primary, DB constraint optional. |
| **01 / 24** (floor map UI) | **Downstream consumers** | The floor map groups by `section`; this slice makes the grouping total. |
| **388** (table status) | **Adjacent** | Owns the status column. |
| **414** (table capacity) | **Adjacent** | Owns `seats` vs `party_size`. |
| **446** (schema evolution) | **No dependency** *unless* the implementer adds a `CHECK`*, in which case it becomes one. |
| **409** (open-decisions register) | **Where the mechanism decision is recorded** | 409 owns the register of open decisions. |

## Open questions

1. **Is the section vocabulary fixed or open?** *Recorded default: **open** — any string a restaurant wants, canonicalised to lower case.* The reason is inherited from feature **431**'s recorded option (a): *"A restaurant that adds a 'Kids' section should not need a code change."* **A fixed list is defensible** — it catches typos like `"mainn"` at the boundary — but it must then live in **one** place (`config.py`) and be validated in the application, and the owner must accept that adding an area is a code change. **The implementer must record the choice.** **This is the decision that most changes the shape of the code, so it is recorded first.**
2. **Case-sensitive or case-insensitive?** *Recorded default: **case-insensitive** — the stored value is lower-cased, so `"Main"` and `"main"` are one area.* The reason: **SQLite's `BINARY` collation and Postgres's default collation do not agree**, and a rule that differs between dev and prod is exactly the defect class feature **453** filed. **The implementer must record the choice.**
3. **What happens to the tables already in the database with inconsistent spellings?** *Recorded default: **nothing is rewritten.** The helper affects writes only.* The reason: **a data migration is feature 446's territory** and the owner has not asked for one. **Recorded so a later pass does not read the omission as an oversight.**
4. **Should `section` also be `NOT NULL`?** *Recorded default: **yes** — a table with no area is a table the floor map cannot place, and the model already gives it a default of `"main"`.* **Note**: a `NOT NULL` is a **table-level change** on an existing column and is therefore **blocked on feature 446** in the same way feature **455**'s `NOT NULL` is. **If the implementer wants to avoid a 446 dependency, leave the nullability alone — a `NULL` section canonicalises to `"main"` anyway.** **The implementer must record the choice.**
5. **Should the floor-map coordinates `(x, y)` be unique too?** *Out of scope — and NOT decided here.* Two tables may currently sit at the same `(x, y)` (executed: **2** rows at `(3, 7)`). **That is a `UniqueConstraint` over a coordinate pair — a different mechanism from a spelling rule — and it is unowned by any feature.** **Recorded here so the next pass files it as its own slice rather than bolting it on here.** Feature **440** mentions the floor-map coordinates only to say the floor map is out of its scope.

## Why this matters

**Because the one column that turns LE31's table list into a floor map is the one column whose value space is unbounded free text — and the corpus has already filed this exact defect on the two sibling columns.**

**What this costs when it is wrong:**

- **The floor map shows half a room.** The manager asks for the main room and gets a subset. **No error, no warning, a plausible number.**
- **The missing tables are the newest ones**, because the newest spelling is whatever the last person typed. **A "which tables are free" query, a capacity check, or a section-scoped report would leave the most recently seated table invisible.**
- **The count is wrong in the quiet direction.** A split produces a *smaller* number than reality, and a smaller number is what a manager reads as "quiet". **The system is wrong in the way that looks right.**
- **It compounds with the floor map's own existence.** Feature **24**'s stated rationale is *"Operators want a floor map, not a list"* — the value of the floor map is entirely in **grouping by area**, and grouping by an area whose value space is unbounded is grouping by a typo.

**Why it is cheap today and expensive later:**

- **Cheap today**: one helper, one decision, one test. **No schema change under the recorded default, no column, no table, no migration.**
- **Expensive later**: **the shipped backend has no route that creates a table** (`routers/` contains only `tables.py`, with no create route). So **no inconsistent section can exist in a database this code built — yet.** The moment the table-creation route ships, the inconsistency can start. **And unlike a label typo, a section typo is invisible on the floor**: the table is *there*, in the right place, with the right number of seats — it is just in a group the query did not return. **A typo in `label` is visible to the waiter; a typo in `section` is visible to nobody until a query runs.**

**Why this is a `build` and not a `defer`:**

**Because it is the same shape as two filed features and the corpus explicitly warns that finding the *shape* is not the same as finding the *instance*.** Feature 431's own text: *"The corpus already knows this gap exists and has never filed it."* **The corpus knows free-text identifiers are a defect class; it normalised the category, it constrained the label, and it never looked at the area.** The rule is one helper and one decision. **The only thing standing between this and a filed contract is that nobody asked.**

## Adjacent evidence

**Third-party, in-window, permissive licences, no code adopted.** All fields parent-verified via a direct `GET /repos/{owner}/{repo}` on 2026-11-08 and **README read in full**.

- **`famalthtechnologies/famalth-lynx-pos`** (Apache-2.0 ✓ §3.2, **★3 / ⑂2**, JavaScript, 26,777 KB, created **2026-10-21** AND pushed **2026-11-07** = **in-window by BOTH fields**) — README, verbatim: *"**Interactive Floor & Table Management**: Live visual floor plan, table reservations, occupancy status, and quick table transfers or bill merging."* **The transferable observation: a mature floor plan treats the floor plan as a first-class object with a *management* surface — which is exactly the surface that needs a well-defined set of areas.** **The README does not state how it constrains its area names** — this is recorded as an **absence**, and the absence is the observation. **No code adopted.**
- **`AlgoVyn/bikri`** (MIT ✓ §3.2, **★1 / ⑂0 = NO traction evidence in either direction**, TypeScript, 14,238 KB, created **2026-10-26** AND pushed **2026-11-08** = **in-window by both fields**) — README, verbatim: *"It runs many independent shops on one Cloudflare deployment; **every shop's data is isolated**"*, and the repository layout names *"**`packages/core` | Pure business and money rules, shared table/op metadata**"* and *"**`packages/db` | D1 SQL migrations, Dexie schema, table metadata**"*. **The transferable primitive is "the metadata is a shared, versioned artefact, not a per-row string"** — which is the vocabulary a fixed-vocabulary decision (Open questions 1) would use. **Already cited by features 455, 454 and 447** — recorded so a later pass does not re-derive it as a fresh trigger.

**Repo self-reported metrics are labelled unverified.** Neither README states a test count or coverage figure that this contract relies on; **nothing here needs an unverified number.**

**The adjacent defect this feature must NOT swallow.** The floor-map coordinates `(x, y)` are **also unconstrained** — two tables may sit at the same spot (executed: **2** rows at `(3, 7)`), and `PRAGMA index_list(table_)` is `[]`. **That is a `UniqueConstraint` over a coordinate pair, a different mechanism from a spelling rule, and it is owned by no feature either** (sweep: `floor.{0,30}collision` → **0**, `overlapping table` → **0**, `coordinate.{0,40}unique` → **0**). **It is recorded in *Open questions* 5 so the next pass files it as its own slice.** This slice's mechanism (normalise a string) **cannot express it**, and bolting a second rule onto one contract would make both harder to review.

## Verification protocol

Four commands, all re-runnable, all offline:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The helper exists and has exactly ONE definition.
grep -rn "def canonical_section" backend/ | wc -l        # must be 1

# 2. It is called somewhere (the write path).
grep -rn "canonical_section(" backend/ | wc -l           # >= 2 (def + call site)

# 3. There is no SECOND copy of the vocabulary in a DDL string.
grep -rn "CHECK" backend/app/models.py | grep -i section  # must print nothing

# 4. The corpus agrees: the area rule is now owned.
grep -rn "Table.section" features/ | wc -l                # must now hit 460
```

Plus the **executed** regression test: two tables with `"Main"` and `"main"` must yield **one** distinct `section`.

**The negative control**: remove the canonicalisation call from the write path (or make `canonical_section` return its input unchanged) and confirm the regression test **fails**. A test that only ever passed proves nothing.

## Rollback path

**Fully reversible in one step.** Remove the helper and the call; behaviour returns to today's. **No data is at risk** — no route creates a table today, so no `section` value was ever written by this code. **No column, no table, no migration, no backfill** under the recorded default.
