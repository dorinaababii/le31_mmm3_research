# Feature 439 — `le31-order-item-has-no-line-level-allergen`

> **Pick B of Daily Research 2026-11-05 (83rd pass).** **FIRST-PARTY, and the gap was PROVEN BY EXECUTION on 2026-11-05.**
>
> LE31's own `backend/app/models.py` declares:
>
> ```python
> class OrderItem(SQLModel, table=True):
>     __tablename__ = "order_item"
>     id: int | None = Field(default=None, primary_key=True)
>     visit_id: int = Field(foreign_key="visit.id", index=True)
>     menu_item_id: int = Field(foreign_key="menu_item.id")
>     qty: int = 1
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)
>     course: str | None = None  # appetizer / main / dessert
>     status: ItemStatus = ItemStatus.new
>     notes: str | None = None
>     fired_at: datetime | None = None
>     ready_at: datetime | None = None
>     served_at: datetime | None = None
> ```
>
> The parent enumerated the fields **by execution** — building a real SQLite database from LE31's own models via `SQLModel.metadata.create_all` and reading `OrderItem.model_fields`:
>
> ```
> ['course', 'fired_at', 'id', 'menu_item_id', 'notes', 'qty',
>  'ready_at', 'served_at', 'status', 'unit_price', 'visit_id']
> ```
>
> **No allergen field. No dietary field. No allergy flag.** And `MenuItem.model_fields` came back as:
>
> ```
> ['category', 'id', 'is_prepared', 'name', 'photo_url', 'unit', 'unit_price']
> ```
>
> **Also no allergen field.** The parent's probe for any field named `allergens`, `allergen`, `contains` or `dietary` on either model returned **nothing**.
>
> **The consequence, stated exactly.** `OrderItem.notes: str | None` is a free-text column. **It is the only place either of these two facts can live today**, and it carries them **without distinguishing them**:
>
> - *"dish contains nuts"* (a property of the **dish**)
> - *"guest is allergic to nuts"* (a property of the **guest at this table**)
>
> **The two are recorded identically, in the same column, with the same syntax.** Nothing in the schema separates what the kitchen must *avoid* from what one guest must *be told*.
>
> **Why the gap is real but not feature 10.** Feature 10 (`features/10-allergen-tracking.md`) owns **per-dish** allergen and dietary metadata — the 14 EUFIC allergens as *tags on a menu item*, plus dietary tags, plus a `/allergens <item>` bot command and a waiter-UI badge on each menu item. **Feature 10 does not own the line.** Its own scope says *"Per-menu-item metadata; per-ingredient metadata; auto-derivation"* — **every one of those is a property of the dish.** The line — the thing the cook actually prepares, on a specific table, for a specific guest on a specific visit — carries nothing, and **no feature in the 471-file corpus owns it**: the parent's probe for `order item allergen`, `allergen on the line`, `per-line allergen`, `dietary flag`, `guest allergy on the line` and `line-level allergen` returned **0 hits across all 471 feature files and all spec files**, with a passing negative control on the same corpus.
>
> **The boundary, stated precisely.** Feature 10 owns **what is in the dish**. This feature owns **what the line is about, given who ordered it**. Those are different facts with different lifetimes: a dish's composition does not change during service; a guest's requirement is a property of one visit and disappears when that visit closes. **Merging them would be wrong, and putting the line's flag on `MenuItem` would be a category error.**
>
> **The external trigger (in-window).** `Jmonczewski-droid/kisnet-pos` (Python 3.12 + FastAPI + SQLAlchemy 2.0 + Alembic + Pydantic, 98 pytest tests, created 2026-11-03, pushed 2026-11-03, ★0, licence-null), README L26, verbatim:
>
> > *"**Price snapshots:** each item's name, price, and **recipe** are saved at the moment of sale, so changing the menu never rewrites past sales."*
>
> The word that matters is **recipe**: the kitchen ticket carries *what went into the dish*, at the moment of sale, on the line. **That is the line-level fact this feature is about** — the record that answers "what did I just tell the kitchen about this specific plate". Its station model places that record on the **kitchen ticket**, which is LE31's cook surface.
>
> **Corroboration from a second in-window source (not picked).** `YuxuanZHO/Canyon` (Python + Flet + SQLite, created 2026-11-02, pushed 2026-11-04) documents a paste-import path whose *"ambiguous prices (`12/18元`, `10-20元`) are flagged 'needs confirmation' and never guessed"*. **The transferable rule is not the price — it is the refusal to guess.** An ambiguous allergen is exactly this: the parser must not guess it, and the kitchen must not act on a guess.

## Goal

Let LE31 record, **on the order line**, the allergen facts that are true *for that line* — and let the cook see them — without turning a free-text note into the safety system.

The concrete outcome: when the waiter takes an order at a table where someone asks "does this contain nuts?", **the answer and the flag live in the same record**, and **the cook's ticket shows the flag** — so the answer is not something the waiter has to remember, and not something the kitchen has to infer from a note.

## Scope

**In scope (v1):**

- **One column on `OrderItem`** carrying the line's allergen state. **The shape is a free-text string of allergen codes, not a boolean** — because the question is never binary ("is this line dangerous?") but *"which of the 14 allergens does this line involve?"*. **The implementer records the choice and the vocabulary source in the code.**
- **The vocabulary: the 14 EUFIC allergens**, as the codes feature 10 already names (*cereals, crustaceans, eggs, fish, peanuts, soybeans, milk, nuts, celery, mustard, sesame, sulphites, lupin, molluscs*). **This feature does not re-derive or re-decide that list** — feature 10 owns it, and reusing it is the point.
- **One write path** — the field is set when the order line is created, by the **waiter's surface**, and it is **explicitly set by a person**. **It is never inferred, never defaulted, and never guessed.**
- **One read helper** — a function that returns the allergens for a line, so the cook's ticket and the waiter's screen render the same thing.
- **One rendering of the flag on the cook's ticket surface**, so the fact reaches the kitchen. **The surface belongs to the kitchen/cook feature; this feature supplies the flag and the helper, and applies it where that surface already reads order lines.**
- **One regression test** with four assertions:
  1. a line created with allergens reads them back;
  2. a line created **without** allergens reads back **empty** — **not `None`, and not a default** — so "no allergens" and "not recorded" are the same thing on a line, and neither is invented;
  3. **the allergen set is snapshotted onto the line** — changing the dish's own metadata afterwards does **not** change the line's recorded allergens (this is the `kisnet-pos` rule: *"the recipe are saved at the moment of sale"*);
  4. a line with allergens renders the flag on the ticket read.
- **A one-line note in `features/10-allergen-tracking.md`** recording the division of labour: feature 10 owns the dish, this feature owns the line.

**Explicitly NOT in scope:**

- **The dish-level allergen metadata itself.** Feature **10** owns it — the `MenuItem` tags, the 14-allergen list, the `/allergens` command, the menu badge, the substitutions table. **This feature reads what feature 10 provides and does not re-implement any of it.**
- **Any new allergen vocabulary, and any new taxonomy.** The 14 EUFIC allergens are reused verbatim.
- **Ingredient-level allergen derivation** (feature 10's *"per-ingredient metadata; auto-derivation"*). **This feature does not build a recipe graph, does not compute allergens from ingredients, and does not write a derivation.** The line's flag is **stated by a person**.
- **Per-guest identity, per-guest allergen records, or any PII.** **This is a hard boundary and it is the charter's Privacy invariant.** The flag is on the **order line**, not on a person. LE31 v1 guest demographics are **counts, not identity or contact data** (charter §3.2). **No guest table, no guest id, no allergy profile attached to a person, and no contact data of any kind.**
- **Any customer-facing surface.** The charter's §3.2 non-goals exclude customer-facing receipts and the QR menu's allergen quiz is feature 10's own out-of-scope. **This is a staff-facing record.**
- **Ingredient substitution recording.** Feature 10 owns the substitutions table. **This feature does not extend a line into a substitution record.**
- **Allergen briefings.** Feature **12** owns pre-shift briefings. **This feature does not build a briefing.**
- **Any change to `MenuItem`.** Untouched — feature 10's ground.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The gap, precisely

Three questions a kitchen must answer at the pass, and where each one lives:

| Question | Where it lives today | Owner |
|---|---|---|
| *What allergens does this dish contain?* | **Nowhere in the schema** — feature 10 specifies it but it is not implemented | feature 10 |
| *Does **this line** involve any allergen?* | **Nowhere.** Only `notes`, which cannot distinguish it from a guest's requirement | **this feature** |
| *Does **this guest** have an allergy?* | **Nowhere, and it should not be anywhere** — v1 stores counts, not identity | **deliberately not stored** |

### Why `notes` is not an answer

The parent's execution confirmed `notes: str | None` is the **only** free-text channel on the line. A note reading *"no nuts"* and a note reading *"guest is allergic to nuts"* are **the same string to every query, every renderer and every kitchen screen.** There is no way to ask "show me the lines with nuts" without matching free text, and there is no way to render a badge that means exactly one thing.

**This is the same class of defect as feature 431** (free-text `MenuItem.category` producing three spellings of one category) and feature 430 (five identical order lines that are indistinguishable except by a surrogate key) — **a field that looks free but is actually carrying structured meaning.**

### Why the flag is stated, not derived

Feature 10 owns the derivation from ingredients. Deriving the line's allergens at write time would mean the line's value depends on a recipe graph that does not exist yet, and would make the *recorded past* change when the *recipe* changes.

**The rule this feature records, taken from `kisnet-pos`:** *"each item's name, price, and **recipe** are saved at the moment of sale, so changing the menu never rewrites past sales."*

**A line's allergen set is a snapshot.** It is what was true and communicated at the moment the order was taken. If the kitchen later changes the recipe, **the historical line keeps the allergen set it was ordered under** — and that is not a bug, it is the point: it is the record of what the guest was told.

### The shape

```python
class OrderItem(SQLModel, table=True):
    ...
    allergen_codes: str | None = None   # free-text codes from the 14-allergen
                                        # vocabulary, snapshot at order time.
                                        # NULL = nothing was recorded (NOT "allergen-free").
```

**Why `str` and not a normalised table.** A `order_item_allergen(order_item_id, allergen)` join table is the textbook shape and it is **deliberately not used**, for two reasons, both recorded rather than assumed:

1. **LE31 v1 has one restaurant and a small menu.** A join table for one row per order line is a second table to keep consistent for no query that v1 needs to answer. **If a query ever needs "how many lines involved nuts this month", the string is answerable with a `LIKE` and the join table is answerable with a `GROUP BY` — and the string's failure mode (a typo in a code) is caught by the vocabulary check below.**
2. **The snapshot property is easier to guarantee with one column.** A join table needs the same "insert rows, never update" discipline the ledger already has; a single column is simply written once at creation.

**The vocabulary check is what makes the string safe.** A code that is not one of the 14 is **rejected at write time**, with a recorded error. **This is the "never guessed" rule from `YuxuanZHO/Canyon` applied to the field this feature adds**: an unrecognised allergen code must fail loudly, not be stored and later misread.

**Why `NULL` and not `""`.** `NULL` means *nothing was recorded*. `""` would mean *recorded, and nothing applies*. **The feature deliberately does not collapse those two**, because they are different facts: a line where the waiter said nothing about allergens is **not** a line that is safe to serve without asking. The regression test asserts that a line created without allergens reads back **empty and un-invented**, and the *read helper* is what decides how to present that to the kitchen.

### The read helper — one definition

```python
# backend/app/services/allergens.py
ALLERGEN_CODES = ("cereals", "crustaceans", "eggs", "fish", "peanuts",
                  "soybeans", "milk", "nuts", "celery", "mustard",
                  "sesame", "sulphites", "lupin", "molluscs")

def parse_allergens(raw: str | None) -> list[str]:
    """Parse a stored allergen string into codes. Unknown codes are IGNORED
    here and REJECTED at write time — this function never raises on data
    written before the vocabulary check existed."""

def is_recorded(item: OrderItem) -> bool:
    """Was any allergen recorded for this line? Distinct from 'no allergens'."""
    return item.allergen_codes is not None
```

**Two functions, two questions.** `parse_allergens` answers *"which?"*; `is_recorded` answers *"was anything said at all?"*. **The second question is the one that matters operationally**, and it is exactly the one a bare `notes` string cannot answer. **A line where nothing was recorded must render differently on the ticket from a line recorded as "no allergens"** — otherwise the kitchen reads silence as safety.

### The write path

```python
# the waiter surface, when creating an order line
allergen_codes: str | None = validated_codes   # None means "not recorded"
```

**The validation is explicit and total:**

- A submitted code that is not in the 14-vocabulary is **rejected** with a recorded error naming the unknown code. **Never stored.**
- The codes are **normalised to a canonical order** before storage, so `"nuts,milk"` and `"milk,nuts"` are the same stored value — the same canonicalisation discipline feature 431 applies to `category`, and the same one feature 434 records as *normalise-on-read*.
- **The write happens once, at line creation.** The field is not updated afterwards by this feature. **A later change to the line's allergens is a new fact and is not modelled in v1** — stated plainly rather than left as a surprise.

**The default is `None`, not "no allergens".** That is the single most important line in this feature.

## Data model

**Schema change — exactly one column:**

| Table | Column | Type | Default | Notes |
|---|---|---|---|---|
| `order_item` | `allergen_codes` | `str \| None` | `None` | Comma-separated canonical codes from the 14-allergen vocabulary. `NULL` = not recorded. Snapshot at order time. |

**No new tables.** **No new indexes required** for v1 (no "lines by allergen" query exists yet; **if one is needed later, that is a separate change** and this feature's string-vs-join-table decision is the thing to revisit then).

**No change to:** `MenuItem` (feature 10's ground), `Visit`, `Bill`, `DerivedTip`, `Shift`, `Batch`, `StockEntry`, `Table`, `AppUser`.

**Interaction with feature 10 (the dish's own metadata):** **read-only, one-directional.** Feature 10 provides the dish's allergens; this feature snapshots them onto the line at order time. **The line never reads the dish's metadata after creation.** That is what makes the snapshot property hold.

**Interaction with feature 10's substitutions table:** none in v1. **A substituted line's allergen set is the set that was ordered**, not the set of the substitute. **Recorded as a v1 limitation and a known sharp edge** — see Open question 3.

**Data retention:** the line's allergen codes live on the line and are never updated by this feature. **They persist for the life of the line**, which is the correct lifetime for the fact *"this is what the guest was told"*.

**Privacy:** **the column records a property of the dish and the order, not of a person.** It is stored on the order line, which already exists and already belongs to a visit. **No new identifying data is stored, no guest table is created, and no allergy profile is attached to anything that could be read as a person.** The charter's Privacy invariant is satisfied *because* the field is about the plate, not the patron.

## Implementation steps

1. **Add the column** to `class OrderItem` in `backend/app/models.py`:
   ```python
   allergen_codes: str | None = None   # canonical codes from the 14-allergen vocabulary;
                                       # snapshot at order time; NULL = not recorded
   ```
   **One line.** The comment records the vocabulary source (feature 10) and the NULL semantics.
2. **Create `backend/app/services/allergens.py`** with `__init__.py`. **The `services/` directory does not exist today** (the parent verified this — `backend/app/` contains only `models.py`, `db.py`, `routers/` and the bot modules). Put `ALLERGEN_CODES`, `parse_allergens()` and `is_recorded()` there.
   - **The point of the module is that the vocabulary has exactly one definition** and that the write path and the read path cannot disagree about it. A renderer that hard-codes the 14 codes inline is a defect even when it prints the same thing today.
3. **Add the write-time validation** to wherever order lines are created. **Note: `backend/app/routers/orders.py` does not exist today** — feature 02 owns it and it has not landed. **So this step has two possible shapes, and the implementer must pick honestly:**
   - **If the orders router does not exist yet (today's state):** implement the validation as a **service function** in `backend/app/services/allergens.py` — `validate_codes(raw) -> str | None` — with its own unit test, and **record in the PR description that feature 02's router must call it.** **Do not create `routers/orders.py` in this slice** — that is feature 02's work and creating it would be scope creep into another feature's file.
   - **If feature 02 has landed by then:** call `validate_codes()` from the router's line-creation path, and reject an unknown code with HTTP 422 naming the code.
   **Either way the validation itself is built and tested here.**
4. **Apply the flag on the cook's ticket surface.** Locate the existing kitchen-ticket read and render the line's allergens from `parse_allergens()`. **If no ticket surface exists yet, record that in the PR description rather than creating it** — the flag, the helper and the read are the contract; the surface is a caller that lands when it lands.
5. **Add the one-line note** to `features/10-allergen-tracking.md`: feature 10 owns the dish, feature 439 owns the line.
6. **Do NOT add an `OrderItem` mutation route** in this slice. **The field is written at line creation and not updated afterwards.**
7. **Do not touch `MenuItem`.**
8. **Do not touch `PROJECT_CHARTER.md`.**

## Telegram interaction if any

**None in this slice, and the reason is worth recording.**

The cook's Telegram bot is where an allergen flag would matter most — the kitchen is the last place a mistake is caught. **But the bot's command surface belongs to feature 04 / the cook-bot features, and this feature is about the record, not the surface.**

**Specifically:**
- **No `/allergens` command is added.** That command is **feature 10's** — its scope already names *"Cook gets a `/allergens <item>` Telegram command"*, and **this feature must not take it over.** Feature 10's command answers *"what is in this dish?"*; a line-level flag answers *"what is on this specific order?"*. **Two different questions, two different surfaces, and feature 10 already owns one of them.**
- **No bot handler reads the flag yet.** The bot has no order-line surface today; the flag reaches the kitchen through whichever surface displays tickets.

**Recorded as an explicit non-goal with its reason:** if the owner wants the flag on the Telegram ticket, that is a **separate feature** whose gate must consider the bot's own constraints — and it must not be smuggled in here.

## Dependencies

**Must exist before this feature can land:**

- `backend/app/models.py` — the `OrderItem` class. **Exists.**
- `backend/app/db.py` — the session dependency. **Exists.**
- `backend/app/routers/` — a package with `__init__.py`. **Exists.**
- A test harness. **Exists** — the parent re-used the `SQLModel.metadata.create_all` throwaway-SQLite pattern today.

**Soft dependency (read before writing, not a blocker):** feature **10**. **This feature does not require feature 10 to have landed** — it can ship the column, the vocabulary and the validation ahead of it, because the 14-allergen list is already *specified* in `features/10-allergen-tracking.md` even though it is not implemented. **But the implementer must read feature 10 first**, and there is one hard stop condition below.

**⛔ THE STOP CONDITION — read this before writing any code:**

> **If feature 10's implementation has already landed and it added a line-level allergen field to `OrderItem`, this feature is a DUPLICATE and must be closed, not merged and not re-implemented.**
>
> The parent's corpus probe (`order item allergen`, `allergen on the line`, `per-line allergen`, `dietary flag`, `guest allergy on the line`, `line-level allergen`) returned **0 hits across all 471 feature files and all spec files** — with a **passing negative control** on the same corpus, so the zero is meaningful rather than a broken grep. **That establishes the gap as unfilled *in the corpus*.** It does **not** establish it as unfilled *in a branch that has not been merged*. **The implementer must check the working tree and `git log` for an unmerged feature-10 implementation before starting.** Feature 10 is filed but not implemented; **if it lands first, this pick is closed with the reason recorded.**

**Must NOT be implemented by this feature, and the boundaries are load-bearing:**

| Ground | Owner | Why this feature cannot touch it |
|---|---|---|
| Dish-level allergen metadata, the 14-allergen list, the substitutions table, the `/allergens` command, the menu badge | **10** | **This feature owns the line, not the dish.** Duplicating any of it creates two sources of truth for the same fact. |
| Ingredient-level derivation from a recipe graph | **10** | **This feature states the flag; it does not compute it.** A derived value that can change after the fact is not a record. |
| Pre-shift allergen briefings | **12** | Different surface, different trigger. |
| Customer-facing allergen surfaces (QR menu quiz, receipts) | **§3.2 non-goal / 10 / 11** | **Staff-facing only.** |
| `OrderItem` insertion time, transition attribution, batch provenance, active-visit write guard | **430 / 379 / 385 / 436** | **Unrelated fields on the same row.** This feature adds one column and touches nothing else on `OrderItem`. |
| Guest identity, guest demographics, allergy profiles | **charter §3.2 Privacy invariant** | **Not stored, at any level.** |
| The order-taking router itself | **02** | This feature supplies the validation *function*; it does not build `routers/orders.py`. |

**Nothing here blocks on an open feature.** Every dependency above is a **boundary or a stop condition**, not a sequencing requirement — with the single exception of the **stop condition**, which can only *cancel* this feature, never delay it.

## Open questions

1. **Does the waiter actually need to set this per line, or is a per-visit flag enough?** A table of four ordering together may have one allergy at the table. **Per-line is the more precise answer and the more expensive one; per-visit is the opposite.** **The recorded default is per-line**, because the line is what the kitchen prepares — but **this is the one decision most likely to change the slice's shape.** If the owner says "we just flag the table", this feature becomes a `Visit` column instead and the contract must be re-written, not patched.
2. **What is the value when the waiter knows the dish is allergen-free and the guest has no allergy?** **The recorded default: `None` — not recorded.** The alternative (writing "none") creates a distinction the kitchen must honour ("written as safe" vs "never mentioned") and that distinction is a **liability if the two are ever rendered identically**. **The `is_recorded()` helper exists so the distinction can be made later without a migration.**
3. **What happens to the line's allergens when the dish is substituted?** Not modelled in v1. **The recorded default: the line keeps the allergen set it was ordered under.** This is correct as a *record of what was told* and is **wrong as a record of what was served** — and the gap between those two is a known sharp edge. **Recorded, not solved.**
4. **Should the flag be visible to the customer on a QR menu?** The charter's §3.2 non-goals exclude customer-facing receipts; feature 11 owns the QR menu. **Out of scope here.**
5. **Should this be a `bool` "has any allergen" instead of a code list?** The parent's execution shows the line-level question is never binary, and the 14-allergen vocabulary already exists. **Recorded default: the code list.**
6. **What is the write path today, given `routers/orders.py` does not exist?** **The recorded answer: implement the validation as a service function with its own tests, and leave the router wiring to feature 02 — or to whoever lands the router next.** **This is deliberately the awkward shape and it is stated rather than hidden.**

## Why this matters

"Of course it doesn't contain nuts" is a sentence a waiter says, from memory, under time pressure, about a dish they did not cook. **LE31 today has nowhere to record that the sentence was said, and nowhere to record whether it was true.**

The failure this prevents is not a usability annoyance. **It is a customer with an allergy being served something they were told was safe.** That is the single highest-consequence defect class in a restaurant system, and LE31's schema currently makes the *only* mitigation — a human's memory and a free-text note — the *entire* mitigation.

**The cost side is what makes this a `build` rather than a `defer`.** One column, one service module, one validation function, one test file. **Four to six hours.** No new surface, no new dependency, no training beyond "tick the allergens when the guest asks". The vocabulary is already written down in feature 10; **this feature does not have to invent anything.**

**And it is reversible.** Drop the column and the module; nothing today reads a field that does not exist yet. The only irreversible thing would be if a guest were harmed in the meantime — **which is exactly the argument for building it now rather than deferring it.**

**One thing this feature is deliberately not:** it is **not** a guest-allergy system. LE31 v1 stores counts, not identities, and that is correct. **The allergen fact belongs to the plate.** Putting it there is what makes the feature both safe to build and safe to keep.

## Adjacent evidence

- **`Jmonczewski-droid/kisnet-pos`** (Python 3.12 + FastAPI + SQLAlchemy 2.0 + Alembic + Pydantic, 98 pytest tests, ★0/⑂0, licence-null, created 2026-11-03, pushed 2026-11-03): **the trigger.** README L26 verbatim: *"**Price snapshots:** each item's name, price, and **recipe** are saved at the moment of sale, so changing the menu never rewrites past sales."* **The transferable rule is the snapshot property, applied to the recipe/allergen fact rather than the price.** Its five-station model places the record on the kitchen ticket — LE31's cook surface. **Recorded as vocabulary; no code adopted** (licence-null).
- **`YuxuanZHO/Canyon`** (Python + Flet + SQLite, ★0, licence-null, created 2026-11-02): the **never-guess** rule — *"Ambiguous or unknown names are reported and never added silently"* and ambiguous prices are *"flagged 'needs confirmation' and never guessed"*. **The transferable rule is the refusal to guess**, applied here to an unrecognised allergen code: **it is rejected at write time, not stored and later misread.**
- **`ANOUARLEK2026/RestaurantOS`** (local-first, ★0, licence-null): its *"Admin staff account creation with role selection"* and *"Audit log"* are adjacent but **not** about allergens. **Recorded, not picked.**
- **Feature 10** (allergen & dietary tracking, **P1**) — **the adjacent pair, not a duplicate.** 10 owns **the dish** (per-item tags, 14 EUFIC allergens, ingredient derivation, substitutions, `/allergens` command, menu badge). 439 owns **the line** (what was ordered under, at a visit, recorded on the order line). **The division is: 10 answers "what is in this dish?", 439 answers "what did we tell the kitchen about this plate?"** Both are needed; neither subsumes the other.
- **Feature 431** (category canonicalisation) — **the same class of defect**: a free-text field that is actually carrying structured meaning. **Recorded as a pattern, not a dependency.**
- **Feature 430** (order-item insertion time) — **the same table, a different column**, and a reminder that `OrderItem` is being audited field-by-field. **This feature is the allergen column in that series.**
- **Charter §3.2** — *"Capture of guest gender, age, or any PII beyond counts."* **This feature is the reason that rule is not violated by a feature about allergies: the flag is on the plate, not the person.**
