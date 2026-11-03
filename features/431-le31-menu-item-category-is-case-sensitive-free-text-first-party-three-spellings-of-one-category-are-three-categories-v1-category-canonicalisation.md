# Feature 431 — `MenuItem.category` is free text: `"dessert"`, `"Desserts"` and `"dessert "` are three different categories for the same dish

> **Pick C of Daily Brainstorm 2026-11-03 (97th pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proven by EXECUTION, not by reading.**
>
> `backend/app/models.py`, `class MenuItem` (lines 84-93), verbatim:
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
> **`category: str`.** No normalisation, no lookup table, no constraint, no default.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then three real inserts through SQLModel):
>
> ```
>   category_variants_for_same_item   ["Desserts", "dessert", "dessert "]
>   category_variants_count           3
>   category_is_case_sensitive        true
> ```
>
> **Three `MenuItem` rows, all named `Tiramisu`, all at `8.80`, ended up in three different categories** — because `"dessert"`, `"Desserts"` and `"dessert "` are three distinct strings.
>
> **⭐ The corpus already knows this gap exists and has never filed it.** Feature 386 (`mighty840/kitchenasty`, the menu-variant feature) states, verbatim, in its *Adjacent evidence* section:
>
> > *"**The category-nesting gap (NOT this feature).** — 'Category management with nesting' — `MenuItem.category` is a plain `str`. Nesting categories is a menu-structure question, not an option question. **Recorded, not picked.**"*
>
> **So the gap is known, explicitly deferred, and still open.** This contract picks it up — but note carefully: it picks the **normalisation** defect, **not** the nesting one. They are different problems with different fixes.

## Goal

**Make `MenuItem.category` mean exactly one thing per dish.**

Any two rows that a human would call the same category must land in the same category. A dish must not be split across the menu by a stray capital letter or a trailing space.

## Scope

- **`backend/app/models.py` — `class MenuItem.category`.** Make it **canonical**, and make it **constrained** so an un-canonical value cannot be written.
- **The write path for a `MenuItem`** — chiefly the **menu OCR flow** (`/start_today`, charter P0 row 44: *"Cook can upload a menu photo via Telegram, confirm parsed items, set per-item prep quantities, and the system creates batches"*), because that is where a model's free-text output becomes a `category` string.
- **The existing rows.** A normalisation pass over whatever categories already exist.
- **The category vocabulary itself** — where the canonical set comes from. See the Open questions; this is the one genuinely open decision.

## Out of scope (v1)

- **A category hierarchy / nesting.** Feature 386 explicitly recorded the nesting gap as *"NOT this feature … Recorded, not picked."* **Nesting is a menu-structure question and it is not this contract.** If the owner wants a tree, that is a separate feature.
- **A `Category` table with a foreign key.** A `menu_category` table is one way to do this, but it is **not the only way** and it is **not required** — see *Data model*. **This contract's requirement is *canonicalisation and a constraint*, not a normalised schema.**
- **Any change to `MenuItem.unit`.** That is **feature 386 / 392 / 407**'s territory — **filed**.
- **`MenuItem.is_prepared`.** That is **feature 398**'s territory (the rule with no consumer) — **filed**.
- **`MenuItem.name`.** Names are free text and should stay so; a dish legitimately has many names across languages.
- **Any change to the charter's tax question.** Charter §3.3 Open Question 3 asks *"**Tax** — flat 10%? Per-category? Per-item?"* — **this contract does not answer it.** It only makes the `category` *string* trustworthy so that, if the owner later chooses per-category tax, the data supports it. **Answering the tax question is the owner's, and features 408/409 own it.**
- **Menu ordering, menu publishing, the QR menu.** **Out of scope** — the category is a grouping attribute, and how the menu is presented is a separate concern.

## Description

### What the schema actually is

`MenuItem` has seven columns: `id`, `name`, `category`, `unit_price`, `unit`, `is_prepared`, `photo_url`. It has **no foreign keys at all** — it is a standalone leaf table. `category` is a bare `str` with:

- **no default** (so it is required — but required is not the same as canonical),
- **no length limit** (a 4 KB category is accepted),
- **no normalisation** (no strip, no case-fold, no whitespace collapse),
- **no constraint** (any string is accepted),
- **no lookup** (nothing to check the value against).

### Why this is a defect and not a nitpick

Three reasons, in increasing order of weight:

1. **A category is a *key*, and LE31 stores keys as free text.** `category` is used to group the menu — by the waiter browsing today's menu (charter P0 row 43), by the kitchen display, by the forecast (charter P1 row 50). A grouping key that can be spelled two ways is not a key.
2. **The OCR path makes the split reachable by accident, not by malice.** The `/start_today` flow parses a menu photo and writes `MenuItem` rows from a model's output. A model that writes `"Dessert"` for the tiramisu row and `"dessert"` for the espresso row — **which is entirely normal LLM behaviour** — silently creates two categories. **No error is raised anywhere.** The failure is invisible at write time and visible only when the guest cannot find the tiramisu on the menu.
3. **The same dish, split three ways, splits three ways everywhere.** A "desserts" group now holds one of the three, and the other two appear under a near-identical heading. Any grouping, any count, any report splits along the same wrong line — and the count is *wrong*, not just ugly: the owner sees three categories where there is one, and the menu shows three "Dessert" headings to the guest.

**⚠️ The sibling risk, stated plainly: `MenuItem.name` is *also* free text, and that is correct.** The same dish legitimately has different names ("Tiramisu", "Tiramisu classico", "Tiramisu à la maison"). **Names are labels; categories are keys.** This contract must not be read as "normalise all strings on `MenuItem`" — it is specifically about the *grouping key*.

### What feature 386 recorded, and what this contract does about it

Feature 386's note is about **nesting**: *"Category management with nesting"*. Nesting asks *"is Dessert under Food, and is Food under Everything?"* — a **menu-structure** question that needs a tree, a parent pointer, and a decision about how deep the menu goes. **That is not this contract.**

This contract is about the **string**: *does `"Dessert"` and `"dessert"` mean the same category?* The answer must be yes, and today it is no, **proven by execution**.

### The third-party instrument

`Ifazawezk/dukkan` (MIT ✓ §3.2, ★1/⑂0 — no traction, FastAPI + SQLAlchemy 2, created **and** pushed 2026-11-01, **in-window by both fields**, 1,719 KB, all fields parent-verified via direct `GET /repos/`). Its README, verbatim:

> *"**Exact money.** Amounts are stored as whole dirhams (1 QAR = 100 dirhams) and are `Decimal` in Python, so no floating point touches a price. **An order discount is split across lines with the largest remainder method, so the shares always add up to the discount exactly.** The browser runs the same rules for the live total, and **the server recalculates everything at checkout.**"*

> *"**Refund that add up.** A return pays back the line's share of **what the customer actually paid**. When the last unit of a line comes back, the refund is **whatever is left of that line**, so rounding can never leak a dirham."*

The transferable idea is the one stated in the middle: **the shares must add up to the discount exactly — and the way a system guarantees that is by *defining the canonical form of a value and computing it the same way on both sides*.** dukkan guarantees it with the **largest remainder method**, which is only correct because the *set of categories* is fixed and the *rule for splitting* is deterministic.

LE31 has the same structural need for `category` and no such guarantee: **two write paths (the OCR flow and, later, a hand-entered menu) can spell the same category differently, and nothing reconciles them.** The fix is the same discipline in a smaller place: **define the canonical form, and enforce it at write time.**

## Data model

**Three options. All three satisfy the Goal. The implementer picks one and records it in the commit message.**

### Option (a) — canonicalise on write + a `CHECK` constraint (recommended, smallest)

```python
class MenuItem(SQLModel, table=True):
    __tablename__ = "menu_item"
    __table_args__ = (
        CheckConstraint(
            "category = lower(trim(category))",
            name="ck_menu_item_category_canonical",
        ),
    )
    ...
    category: str
```

**Plus** a single canonicalisation helper applied at every write site:

```python
def canonical_category(raw: str) -> str:
    """'  Dessert ' -> 'dessert'. The one rule, applied everywhere."""
    return " ".join(raw.split()).lower()
```

- The **`CHECK` constraint** is the enforcement — it makes an un-canonical value **impossible to store**, not merely unlikely.
- The helper is the **definition** — it is the single place the rule lives, so the OCR path and any hand-entered path cannot diverge.
- **No new table, no new dependency, no FK.**

**Note the SQLite/Postgres asymmetry** — and it is a real one, so it is stated: SQLite's `lower()`/`trim()` are ASCII-only, Postgres's `lower()`/`trim()` are locale-aware. For a menu category in one restaurant's language this is immaterial, but it is **not identical behaviour across the two databases**, and the charter commits LE31 to *"SQLite for dev, Postgres for prod. Same SQLModel code for both."* **The canonicalisation helper (Python-side) IS identical across both** — which is why the helper is the primary mechanism and the `CHECK` is the backstop.

### Option (b) — a `menu_category` table with a foreign key

```python
class MenuCategory(SQLModel, table=True):
    __tablename__ = "menu_category"
    id: int | None = Field(default=None, primary_key=True)
    name: str            # canonical, unique
    sort_order: int = 0
```

with `MenuItem.category_id: int = Field(foreign_key="menu_category.id")`.

- **Pros:** the vocabulary is visible, sortable and extensible; typos become impossible; a category can be renamed in one place.
- **Cons:** **a schema change on `MenuItem` that touches the OCR write path, the menu list, the kitchen display and the forecast** — and it makes **nesting** tempting, which is **explicitly not this contract's job**.
- **⚠️ This option must land together with an FK-enforcement story.** LE31's `PRAGMA foreign_keys` is **off** in dev (**feature 427** — filed) — so a new FK would be **unenforced in dev and enforced in prod**, which is exactly the divergence feature 427 exists to close. **Option (b) therefore has a hard dependency on feature 427 landing first.**

### Option (c) — a `category` lookup by name, no new table

Keep `MenuItem.category: str` and enforce canonicality with the option (a) helper + `CHECK`, **plus** a canonical vocabulary maintained in `config.py` (e.g. `MENU_CATEGORIES: list[str]`).

- **Pros:** no schema change at all; the vocabulary is one config list; the `CHECK` can also assert membership in the list (`category IN ('drinks','mains','desserts',…)`).
- **Cons:** the vocabulary is hard-coded and must be edited when the menu changes — which, for a restaurant whose menu changes, is friction. **And a hard-coded list in `config.py` must be consistent with what the OCR flow emits, or the OCR flow will be rejected by the very constraint meant to protect it.** That last point is a genuine hazard and is why option (c) is listed third.

**Recommendation: option (a)** — it satisfies the Goal with no schema change, no new dependency, no FK-enforcement dependency, and identical behaviour in dev and prod for the mechanism that actually matters (the Python-side helper).

### The normalisation pass for existing rows

Whichever option is chosen, existing rows must be brought into canonical form:

```sql
-- before: 'Dessert', 'dessert', 'dessert '
-- after:  'dessert', 'dessert', 'dessert'
UPDATE menu_item SET category = lower(trim(category));
```

**⚠️ Note what this does NOT do:** it does not merge categories that are *semantically* different but *spelled* the same way. `"Mains"` and `"main"` merge; `"Mains"` and `"Main Dishes"` do **not** — that is a **vocabulary decision**, and it is the owner's. See Open question 1.

## Implementation steps

1. **Pick option (a), (b) or (c)** and record the choice in the commit message.
2. **Define the canonicalisation helper** in one place — `backend/app/services/` (new package; feature 374 and feature 430 also expect it to exist) or `backend/app/config.py`. **One definition, used by every write site.**
3. **Apply the helper at every `MenuItem` write site.** As of this pass, `backend/app/routers/` contains only `__init__.py` and `tables.py` and `backend/app/bot/` only `cook_bot.py` — **there is no menu write path implemented yet.** The `/start_today` OCR flow is a **charter P0 row that has no router**. **So this contract's write-site work is: provide the helper, and apply it wherever a write site exists — which today means the tests and any future call site.**
4. **Add the `CHECK` constraint** (option a or c). Per charter §3.2, v1 uses **`init_db()`**, **not** Alembic. **Note the SQLite/Postgres `lower()`/`trim()` asymmetry** — the Python-side helper is the portable guarantee; the constraint is the backstop.
5. **Normalise existing rows** (the `UPDATE` above) as part of the `init_db()` / migration step.
6. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:
   - `test_category_is_canonicalised` — `"  Dessert "` → `"dessert"`; `"DESSERT"` → `"dessert"`; `"Main   Dish"` → `"main dish"` (whitespace collapsed, not just trimmed).
   - `test_non_canonical_category_cannot_be_stored` — inserting `"Dessert"` directly (bypassing the helper) is **rejected by the constraint**. **This test must fail on the unfixed code.**
   - `test_three_spellings_of_one_category_land_together` — three `MenuItem` rows written through the helper with three spellings group into **one** category when read back.
   - `test_menu_item_name_is_not_canonicalised` — `"Tiramisu"` and `"tiramisu"` remain **distinct names**. This test guards the boundary: *names are labels, categories are keys.*
7. **Do not** add a category tree, a `menu_category` table (unless option b), a foreign key on `category`, or any menu-publishing behaviour.

## Telegram interaction if any

**None new.** The `/start_today` flow already exists as a charter P0 row; this contract changes **what value it writes** into `category`, not what the cook sees or types. **No new command, no new button.**

## Dependencies

- **Charter P0 row 44** — the `/start_today` flow that creates `MenuItem` rows (the write path this contract protects).
- **Charter P0 row 43** — *"Waiter can browse today's menu and add items to the active visit … menu hides sold-out items"* (the **consumer** whose grouping breaks).
- **Charter P1 row 50** — the `/forecast` per-item (a second consumer of the grouping).
- **Charter §3.2** — `init_db()` for v1; **no Alembic**; no new dependency.
- **Charter §7** — *"No magic numbers"*; *"End-to-end before commit."*
- **`le31-conventions`** — the seven-check feature gate and the hard invariants.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done*.
- **`le31-handoff-spec`** — the frozen-contract discipline.

**Nearest siblings — read these so this slice does not open them:**

- **`features/386-…-v1-menu-item-options.md`** — **the nearest sibling, and the one that recorded this gap.** Read it first; it explicitly says *"NOT this feature … Recorded, not picked"* about the *nesting* half. **This contract picks the *normalisation* half and must say so in the commit message.**
- **`features/392-…-v1-menu-item-unit-meaning.md`** and **`features/407-…`** — `MenuItem.unit`'s meaning and its free-text problem. **Filed.** This contract does **not** touch `unit` — but it is the **same pattern on a sibling column**, so read them to be sure you are not duplicating a normalisation rule that already exists.
- **`features/398-…`** — `MenuItem.is_prepared` has no consumer. **Filed.** Not touched.
- **`features/427-…-v1-sqlite-fk-enforcement.md`** — **a hard prerequisite for option (b) only.** A new FK would be unenforced in dev and enforced in prod without it. **Option (a) has no such dependency.**
- **`features/408-…`** and **`features/409-…`** — the tax **rate** and its home. **Filed.** This contract does not answer charter §3.3's tax question; it only makes `category` trustworthy.
- **`features/429-…`** and **`features/430-…`** — this pass's other two contracts. **Independent** (one is about timestamps, one about a category string); none of the three touches another's column.

## Open questions

1. **What is the canonical vocabulary?** This is an **owner decision, not an implementation detail.** The canonicalisation rule (case-fold + whitespace-collapse) is mechanical, but *which strings are the same category* is a judgement about the restaurant's menu. **Default recorded: normalise mechanically only** (`lower` + whitespace-collapse) and **do not attempt semantic merging** — `"Mains"` and `"Main Dishes"` stay distinct until the owner says otherwise. **A semantic merge is a data-migration decision with a menu to hand, and it is not this contract's call.**
2. **Should the category vocabulary be fixed or open?** Option (c) fixes it in `config.py`; option (a) leaves it open (any canonical string). **Default recorded: option (a) — open.** A restaurant that adds a "Kids" section should not need a code change. **But see the hazard noted in option (c): a fixed list must agree with what the OCR flow emits.**
3. **Should the categories be case-folded at all, or only whitespace-collapsed?** Lower-casing loses the *display* capitalisation an owner may want ("Desserts" in the UI). **Default recorded: store the canonical lower-case form and, if display capitalisation is wanted, add a separate display name later.** A v1 menu can render `"desserts"` without harm, and **a key that must be displayed is a key that will be re-typed and will drift.**
4. **Is `category` ever empty or missing?** Today it is a required `str` with no default, so an empty string is the only "missing" value and it is **accepted** (`""` is a valid canonical string). **Default recorded: reject the empty string** as part of the constraint. **This is a small decision and it is recorded so it is not made by accident.**
5. **What happens to the existing rows' *display* if they were hand-capitalised ("Desserts")?** **Default recorded: they become `desserts`.** The owner should be told this in the commit message, because it is a **visible change to the menu**, even though it is not a visible change to the data's meaning.

## Why this matters

**⭐ LE31's menu is written by a language model, and nothing checks what it writes.**

Charter P0 row 44 is *"Cook can upload a menu photo via Telegram, confirm parsed items, set per-item prep quantities, and the system creates batches."* The parse is a **model's free-text output**, and the model's output for a category label is `"Dessert"` as often as `"dessert"` — for the same photograph, on the same day, in the same language. **Those two strings are two different categories in LE31's schema today, and the split happens silently at write time and surfaces to the guest as a menu with three "Dessert" headings.**

**⭐ And this is a defect the corpus has already seen and set aside.** Feature 386 read a third-party README about *"Category management with nesting"*, correctly identified that LE31's `category` is *"a plain `str`"*, correctly decided that *nesting* was not its subject, and wrote the gap down as *"Recorded, not picked."* **It was then never picked up by anyone.** That is exactly the failure mode this pass's coverage sweep was built to detect — and it is why the sweep for *this* concept (`menu_item.category` free text) returned **exactly one** hit (feature 386's own deferral note) and no filed feature.

**⭐ The fix is small and it is the right shape.** One canonicalisation function, defined once and applied at every write site, plus a database constraint that makes an un-canonical value **impossible to store** rather than merely unlikely. **That second half is what matters.** A normalisation rule applied only in the write path is a rule the next write path will forget; a `CHECK` constraint is a rule the database enforces for **every** path, including the one somebody adds in six months. LE31's charter already demands exactly this kind of enforcement for money — *"Money is `Decimal`, never `float`"* is a *type-level* guarantee, not a convention — and category is the same kind of guarantee: **a grouping key should be a constrained value, not a free-text label.**

**⭐ And the boundary is worth protecting explicitly.** `MenuItem.name` is *also* free text, and that is **correct** — a dish legitimately has many names. **The lesson is not "normalise all strings"; it is "know which of your strings are keys and which are labels."** LE31's schema today does not distinguish them, and this contract draws that line for one column, in one file, with a test that says so.

## Adjacent evidence

**Third-party instrument — `Ifazawezk/dukkan`** (MIT ✓ §3.2 STRICTLY-COMPATIBLE, ★1/⑂0 — **NO traction evidence in either direction**, 1,719 KB, **Python ✓ ON-STACK** (FastAPI + SQLAlchemy 2 + Pydantic v2), created 2026-11-01 **AND** pushed 2026-11-01 = **IN-WINDOW BY BOTH FIELDS**, `default_branch=main`, `archived=false`, `fork=false`; all fields **parent-verified via direct `GET /repos/`**; README read in full, 14,693 bytes).

Its README, verbatim:

> *"**Exact money.** Amounts are stored as whole dirhams (1 QAR = 100 dirhams) and are `Decimal` in Python, so no floating point touches a price. **An order discount is split across lines with the largest remainder method, so the shares always add up to the discount exactly.** The browser runs the same rules for the live total, and **the server recalculates everything at checkout.**"*

**Le31-side gap this names (proven by EXECUTION):** `category_variants_for_same_item` = `["Desserts", "dessert", "dessert "]` — **three** categories for one dish; `category_is_case_sensitive` = `true`. The transferable primitive is the one dukkan makes explicit for money: **a system that guarantees "the shares always add up to the discount exactly" does it by defining the canonical form of a value and computing it the same way on both sides.** LE31's `category` has no canonical form and two prospective write paths (the OCR flow and a future hand-entered menu).

**Recorded, not picked (each verified by a corpus-wide grep, not by memory):**

| Rule from the source | LE31 analogue | Disposition |
|---|---|---|
| *"Roles, branches and JWT login"* / *"Owner, manager and cashier roles, with costs hidden from cashiers"* | per-role authorisation and cost visibility | **COVERED (8)** — features 393, 403, 406, 413. §3.1's *"role-based via chat_id allowlist"* is a **shape mismatch**, filed in the 91st pass |
| *"Stock per branch, low stock thresholds and an append-only movement ledger"* | the ledger + thresholds | **COVERED** — features 374, 421, 404 |
| *"Suppliers, and purchase orders from draft to ordered to received"* | supplier / PO | **COVERED (71)** — features 03, 121 |
| *"Split payments across cash, card and wallet, with change given from cash only"* | multiple tenders on one bill | **Feature 14** + **feature 420** — **filed** |
| *"CSV export of every table report, which opens in Excel with Arabic intact"* | report export | **COVERED** — the reporting family |
| *"Two views of returns (a cash view … a product view)"* | cash vs accrual reporting | **NOT COVERED** — **recorded here, deliberately not picked**; it is a *reporting* concept, and features 06/08 are briefs rather than contracts |
| *"Items sold by weight"* — on dukkan's **unbuilt** roadmap | `MenuItem.unit` | **Features 386 / 392 / 407** — **filed** |
| *"Cash drawer sessions with end of day counts"* — on dukkan's **unbuilt** roadmap | the shift close | **Feature 426** — **filed** |

**Boundary — what this feature does NOT own:** the *category hierarchy* (386's recorded-not-picked note), `MenuItem.unit`'s meaning (386/392/407), `MenuItem.is_prepared`'s consumer (398), the *tax rate* (408/409), the *`created_at` convention* (429), the *`order_item` insertion time* (430), the *OCR parse flow itself* (charter P0 row 44, no router exists).

**Fully reversible.** Under option (a) nothing structural changes: the column stays a `str`, the constraint is additive, and the normalisation pass is a one-way `UPDATE` whose original values are recoverable from the model's own source rows (the menu photo). Under option (b) the change is larger and is recorded as such.
