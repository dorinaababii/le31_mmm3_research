# Feature 438 — `le31-menu-item-has-no-availability-flag`

> **Pick A of Daily Research 2026-11-05 (83rd pass).** **FIRST-PARTY, and the gap was PROVEN BY EXECUTION on 2026-11-05 — not inferred from reading code.**
>
> LE31's own `backend/app/models.py` declares:
>
> ```python
> class MenuItem(SQLModel, table=True):
>     __tablename__ = "menu_item"
>     id: int | None = Field(default=None, primary_key=True)
>     name: str
>     category: str
>     unit_price: Decimal = Field(max_digits=10, decimal_places=2)
>     unit: str = "piece"
>     is_prepared: bool = True    # if True, sales decrement a Batch
>     photo_url: str | None = None
> ```
>
> The parent enumerated the model's fields **by execution** — building a real SQLite database from LE31's own models via `SQLModel.metadata.create_all` and reading `MenuItem.model_fields` — and got:
>
> ```
> ['category', 'id', 'is_prepared', 'name', 'photo_url', 'unit', 'unit_price']
> ```
>
> **There is no availability field of any kind.** Not `is_active`, not `enabled`, not `is_available`, not `retired_at`, not `sold_out_today`. The parent's probe for *any* field whose name contains `active`, `availab`, `sold`, `enable`, `retir` or `hidden` returned **the empty list**.
>
> **The consequence, also proven by execution.** The parent inserted two `MenuItem` rows and one `Batch`:
>
> ```
> tiramisu    (id=1) — batch created, 8 units prepped, all 8 sold   → derived stock = -8
> panna cotta (id=2) — no batch row at all                         → derived stock =  0
> ```
>
> **Both rows carry identical field values for every field `MenuItem` actually has.** The one difference — *is this dish sold out right now?* — lives entirely in the `Batch`/`StockEntry` tables, which is the correct place for it. The difference the schema **cannot** express — *is this dish being served at all?* — has nowhere to live.
>
> **Why this matters concretely.** LE31 can say "this batch sold out" and "this item is not prepared". It **cannot** say "we stopped serving the tiramisu". A retired dish and a dish that simply has no batch today are the same row with the same field values. The two available workarounds are both wrong:
>
> - **Delete the row.** Then every historical `OrderItem` that references it points at nothing — and `OrderItem.menu_item_id` has a foreign key, so either the sale history is destroyed or the delete is refused.
> - **Leave it.** Then the waiter keeps offering a dish the kitchen no longer makes, and the cook has to remember to filter the menu mentally.
>
> **The external trigger (in-window, read in full).** `YuxuanZHO/Canyon` (Python + Flet + SQLite, created 2026-11-02, pushed 2026-11-04, ★0, licence-null), from `readme/readme_YuxuanZHO__Canyon.md` lines 32-33, verbatim:
>
> > *"Create, edit, enable/disable and delete dishes; **delete is refused while an order references the dish (disable instead)**."*
>
> That is the whole rule, in one line, and it is exactly the distinction LE31's schema cannot express. The same README adds a third distinction worth recording: *"Categories: create, rename, reorder, **activate/deactivate**, delete with reassignment."* — **the category has an activation state; the dish does not.**
>
> **Boundary — this feature must NOT be confused with feature 397.** Feature 397 owns the **sold-out** state: a per-day, **derived**, stock-derived availability record (`sold_out_today`), which the charter names at §4.3 and which the cook sets with `/sold_out`. **Sold-out is temporary and un-stocks; retired is permanent and does not touch the ledger at all.** A dish that is sold out comes back tomorrow. A retired dish does not. The two states must never be merged into one column, because merging them would mean a sold-out dish could be permanently withdrawn, and a restock could silently un-retire a dish.
>
> **Corroboration from a second in-window source (not picked).** `rkevrellan/ComandaPOS` (Python/Flask desktop POS for Panama, created 2026-11-05, licence-null) separates *removing a record* from *taking it out of service* in its catalogue administration, and refuses a **discount above a threshold unless a supervisor authorises it** — the same shape of rule: **the action that changes the operational state is not the action that changes the data.** Recorded as adjacent evidence.

## Goal

Make LE31 able to say **"we are not serving this dish"** as a fact it can read, filter on, and keep — without deleting the dish, and without touching the stock ledger.

Today a retired dish is indistinguishable from a dish that was never prepped. The goal is one stored representation of *retirement*, one write path that sets it, one read helper that every surface filters on, and one regression test that pins the distinction.

The concrete outcome: after the owner retires the seasonal soup, **the waiter's menu no longer shows it**, **the cook's prep board no longer offers it**, and **every historical `OrderItem` for it still renders correctly** — all three at once, which is impossible today.

## Scope

**In scope (v1):**

- **One stored column on `MenuItem`** recording retirement. The shape is a **boolean** (`is_active: bool = True`) rather than a timestamp, because LE31 v1 has no menu-versioning concept and a timestamp implies a history the schema does not keep. **The implementer records this choice in the code.**
- **The write path** — one service function and one route that retires a dish and one that restores it. **The restore path is in scope** because a boolean without an inverse is a one-way door, and the gate's reversibility check requires the disable path.
- **The read helper** — one function answering *"is this dish currently being served?"*, in a place every surface can import it. **The helper has exactly one definition** and no surface re-implements the rule.
- **One filter applied to the waiter menu surface** and **one to the cook's prep-board surface**, so that the retired dish is actually hidden rather than merely recorded.
- **A regression test** with three assertions, because the failure this feature prevents is a *confusion*, and a test that only checks "retired is hidden" would pass even if sold-out and retired were the same field:
  1. a retired dish is absent from the menu read;
  2. a **sold-out** dish is **still present** in the menu read (it is unavailable *today*, not retired — feature 397's ground, and this test proves the two states did not merge);
  3. a dish retired **after** being sold still has its historical `OrderItem` rows resolvable.
- **A one-line note in `features/03-kitchen-stock-tracker.md`** recording that retirement is **not** a ledger event, so a future implementer does not reach for `StockEntry`.

**Explicitly NOT in scope:**

- **The sold-out state.** Feature **397** owns it — the per-day derived availability record and the `/sold_out` command. **This feature does not read, write, derive or duplicate it.** The only relationship is a **negative assertion** (test 2 above).
- **`StockEntry` / `Batch` / the append-only ledger.** A retirement writes **no** ledger row. **The ledger is the source of truth for quantity; this column is the source of truth for *whether the dish is on the menu at all*.** They are different facts and the charter's append-only rule is untouched by this feature.
- **`MenuItem.is_prepared`.** Feature **398** owns it (*"the rule with no consumer"*). **This feature does not read it, change it, or give it a consumer.** Retirement is orthogonal to whether a dish is prepared.
- **`MenuItem.category`.** Feature **431** owns its canonicalisation. **This feature does not normalise, validate or constrain it.**
- **Any menu-management UI.** The write path is an API; the screen is not built here.
- **Any `MenuItem` deletion.** **The rule is the opposite of deletion** — deletion remains refused while an order references the dish, and that refusal is *why* this column exists.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.
- **A history of retirements.** v1 has no menu-versioning; `is_active` is the current state and nothing else. **A dish retired and restored leaves no trace**, and that limitation is stated rather than hidden.
- **Anything on the order-taking path.** No `OrderItem` is written or validated by this feature.

## Description

### The gap, precisely

LE31 currently has **two** independent "can I have this?" questions and **can answer only one of them**:

| Question | Where it lives today | Owned by |
|---|---|---|
| *Is there stock of it right now?* | `Batch` + `StockEntry` — `SUM(qty_delta)` per batch | feature 374 (derivation), feature 397 (availability state) |
| *Is it prepared at all?* | `MenuItem.is_prepared: bool` | feature 398 |
| ***Are we serving it at all?*** | **nowhere** | **this feature** |

The third question is what an owner asks when a dish leaves the menu — *"we don't do the soup in summer any more"* — and it is not a stock question and not a preparation question. **It is a question about the menu.**

### Why "just delete the row" is the wrong answer

The parent checked the schema for the consequence of deletion:

- `OrderItem.menu_item_id: int = Field(foreign_key="menu_item.id")` — **a sale references the dish.** Deleting the dish either orphans the sale or is refused.
- `OrderItem.unit_price` is a **snapshot** — feature 386 records that *"each item's name, price, and recipe are saved at the moment of sale"*. So the *price* survives a deletion. **The item's *name* does not** — `OrderItem` has `menu_item_id`, not a `name` snapshot.

That asymmetry is the crux. **Deleting a dish preserves the money and loses the thing the customer ordered.** A retired dish preserves both, because the row stays and the retirement is a flag.

### Why "just set the price to 0" is worse

A zero-priced dish is indistinguishable from a genuinely free item, corrupts the revenue report, and turns every average-price computation wrong. **Not proposed.**

### The shape

```python
class MenuItem(SQLModel, table=True):
    ...
    is_prepared: bool = True    # if True, sales decrement a Batch
    is_active: bool = True      # if False, the dish is retired: hidden from the menu,
                                # but its history stays readable
```

**Why a boolean and not `retired_at: datetime | None`:** a timestamp would allow "when was it retired and when was it restored", which v1 has nowhere to show and no requirement to record. LE31's `Batch` has `expires_at` because batches genuinely expire; a menu decision does not have an expiry. **A boolean is the smallest representation that makes the distinction, and it is honest about what it does not record.**

**Why it is on `MenuItem` and not a separate table:** a `retired_menu_item(menu_item_id, date)` table would be the right shape *if* retirement were per-day (that is feature 397's shape, and the reason it needs its own table). **Retirement is not per-day — it is a property of the dish until it is changed.** A separate table would add a join to every menu read to answer a boolean question.

### The read helper — one definition

```python
# backend/app/services/menu.py
def is_served(item: MenuItem) -> bool:
    """Is this dish currently on the menu?

    Retirement is a stored fact. This helper deliberately does NOT consult
    StockEntry or Batch: sold-out availability is feature 397's derivation
    and is composed by the caller, not re-derived here.
    """
    return item.is_active
```

**The helper is a pure function of the `MenuItem` row, and it says so in its docstring.** The reason for that discipline is specific: a helper that also computed sold-out would silently become a second implementation of feature 397's derivation, and the two would drift. **The composition of "retired AND not sold out" belongs to the caller, and that composition is where feature 397's rule is applied.**

### The write path

```python
@router.post("/{item_id}/retire")
def retire_item(item_id: int, session: Session = Depends(get_session)) -> dict:
    """Take a dish off the menu. Writes no StockEntry — the ledger records
    quantity, and this records availability. Refuses to retire a dish that
    is not on the menu already."""
```

**Two refusal rules, both explicit:**

1. **Retiring an already-retired dish is refused** (409), so the endpoint is not a silent no-op.
2. **No ledger write happens.** A test asserts that `StockEntry` row count is **unchanged** across a retirement. **This is the assertion that keeps the feature from leaking into the append-only ledger.**

**And the restore path**, because a boolean without an inverse is a one-way door:

```python
@router.post("/{item_id}/restore")
```

**`restore` is a separate explicit action, not an automatic consequence.** The charter's invariant is that *operational transitions are explicit user actions* — and a dish re-appearing on the menu without anyone deciding it should is exactly the silent transition the charter forbids. **A `/restock` must not un-retire a dish, and a sale must not un-retire a dish.**

### The data flow

```
owner: "we're not doing the soup this week"
   │
   ├─► POST /api/menu/{id}/retire
   │      └─► MenuItem.is_active = False      (ONE write; NO StockEntry row)
   │
   ├─► waiter menu read ─► filter(is_served) ─► soup ABSENT
   ├─► cook prep board   ─► filter(is_served) ─► soup ABSENT
   └─► historical OrderItem for the soup ─► STILL RENDERS (row intact)
```

## Data model

**Schema change — exactly one column:**

| Table | Column | Type | Default | Notes |
|---|---|---|---|---|
| `menu_item` | `is_active` | `bool` | `True` | `False` = retired. Not nullable. |

**No new tables. No new indexes required** (the menu read is a full scan of a small table; LE31 v1 has one restaurant's menu).

**No change to:** `OrderItem`, `Bill`, `DerivedTip`, `Shift`, `Batch`, `StockEntry`, `Visit`, `Table`, `AppUser`.

**Why the history survives:** `OrderItem.menu_item_id` remains a valid foreign key because the `MenuItem` row is **never deleted**. Retirement is a flag on the row, not a removal of the row. **This is the entire point of the feature, and it is what makes it different from deletion.**

**Interaction with feature 431 (category canonicalisation):** none. **Interaction with feature 398 (`is_prepared`):** none — `is_prepared` is *whether this dish decrements a batch*, `is_active` is *whether it is on the menu*. **A retired prepared dish still decrements its batch if an order line for it already exists** (the sale happened before the retirement). A retired dish that is *not* prepared is still retired.

**Data retention:** the `is_active` flag is part of the `menu_item` row. **Restoring sets it back to `True`; there is no tombstone and no history.** Stated plainly as a v1 limitation.

## Implementation steps

1. **Add the column** to `class MenuItem` in `backend/app/models.py`:
   ```python
   is_active: bool = True      # if False, retired: hidden from the menu, history kept
   ```
   **One line.** Record the choice and its rationale in a comment on the line.
2. **Create `backend/app/services/menu.py`** with `__init__.py`. **The directory does not exist today** (`backend/app/` contains only `models.py`, `db.py`, `routers/`, and the bot modules — the parent verified this). Put `is_served(item)` there.
   - **The point of the module is that the rule has exactly one definition** and every caller imports it. A surface that re-implements `item.is_active` inline is a defect even though it produces the same result — the day the rule grows a condition, one surface will have been missed.
3. **Create `backend/app/routers/menu.py`** with:
   - `GET /api/menu` — the waiter-facing menu read, **filtered by `is_served`**. This router does not exist today; create it. **Do not build a full menu CRUD API** — this slice adds the read and the two write routes only.
   - `POST /api/menu/{item_id}/retire`
   - `POST /api/menu/{item_id}/restore`
   - **Both write routes: no `StockEntry` write, and no `Batch` write.** A comment on each route states that the ledger is untouched, because a future implementer adding "also mark the stock sold out" would be silently breaking the append-only rule.
4. **Apply the filter on the cook's prep-board surface.** Locate the existing prep-board read and add the same `is_served` filter. **If the prep-board surface does not exist yet, record that in the PR description rather than creating it** — the waiter surface and the helper are the contract; the prep board is a caller that lands when it lands.
5. **Do NOT delete any `MenuItem` row** as part of this slice. **Do not add a delete route.**
6. **Write the regression test** — `backend/tests/test_menu_availability.py`:
   - `test_retired_item_is_absent_from_menu` — retire a dish, read the menu, assert it is absent.
   - `test_sold_out_item_is_still_present` — **the boundary test.** Create a dish with a fully-consumed batch (feature 397's state) and assert it is **still in the menu read** and that **`is_served` returns `True` for it**. **This test is what proves retirement and sold-out did not merge.**
   - `test_retirement_writes_no_ledger_row` — count `StockEntry` rows before and after a retirement; assert **unchanged**.
   - `test_retired_item_history_still_resolves` — retire a dish that has a historical `OrderItem`; assert the `OrderItem` still loads and its `menu_item_id` still resolves to a readable `MenuItem` row.
   - `test_restore_brings_the_dish_back` — retire then restore; assert it is present again.
   - `test_double_retire_is_refused` — retire twice; assert the second is refused with 409.
7. **Add the one-line note** to `features/03-kitchen-stock-tracker.md`: retirement is not a ledger event; see feature 438.
8. **Do not touch `PROJECT_CHARTER.md`.**

## Telegram interaction if any

**None in this slice, and that is deliberate.**

The cook's Telegram bot already has `/sold_out` — **and that command belongs to feature 397, not to this feature.** Adding a `/retire` command here would put two availability concepts behind one surface and would make the sold-out/retired distinction harder to see, not easier.

**The owner retires a dish from the waiter surface.** The owner is the only person who decides what the menu is; the cook does not. The cook's existing `/sold_out` continues to mean exactly what it means today, and **the two commands must never be conflated** — `/sold_out` means "we have none right now", and "retire" means "we do not do this".

**Recorded as an explicit non-goal with its reason:** if the owner later wants the cook to retire a dish from Telegram, that is a **separate feature** with its own gate, and it must not be smuggled in here.

## Dependencies

**Must exist before this feature can land:**

- `backend/app/models.py` — the `MenuItem` class. **Exists.**
- `backend/app/db.py` — the session dependency. **Exists.**
- `backend/app/routers/` — a package with `__init__.py`. **Exists** (it contains only `__init__.py` and `tables.py`).
- A test harness. **Exists** — feature 414's proof built a throwaway SQLite DB with `SQLModel.metadata.create_all` and the parent re-used that pattern today. **Confirm the project's test layout before assuming a path.**

**Must NOT be implemented by this feature, and the boundaries are load-bearing:**

| Ground | Owner | Why this feature cannot touch it |
|---|---|---|
| Sold-out availability state | **397** | This feature's whole point is that they are **different** states. Merging them is the failure this feature prevents. |
| `qty_remaining` derivation | **374** | Different fact: quantity vs. availability. |
| `StockEntry` append-only rule | **421** | **A retirement writes no ledger row.** Feature 421 owns the single write path; this feature adds no write path to the ledger at all. |
| `MenuItem.is_prepared` | **398** | Orthogonal: "is it prepared" vs "is it served". **This feature does not give `is_prepared` a consumer.** |
| `MenuItem.category` | **431** | Orthogonal. **This feature does not normalise or constrain the category.** |
| `MenuItem.unit` | **386 / 392 / 407** | Orthogonal. |
| Order taking | **02** | **No `OrderItem` is written or validated here.** |
| Bill / derived tip | **05 / 415** | Untouched. |
| The waiter UI surface | **02** | This feature supplies the **filter**; the screen belongs to the order-taking feature. |

**Soft dependency (read before writing, not a blocker):** feature **397**'s sold-out derivation, if it has landed. If it has, the menu read should compose `is_served(item) AND not sold_out(item)` — **calling 397's helper, never re-implementing it.** If 397 has not landed, this feature lands alone and the composition is left to whoever lands 397.

**Nothing here depends on a feature that is still open in a way that blocks this slice.** Every item above is a *boundary*, not a *prerequisite* — with one exception: if feature **421** lands first and introduces the single ledger write path, this feature must still **not** write to it. **The dependency is a prohibition, not a sequencing requirement.**

## Open questions

1. **Should retirement be per-day rather than permanent?** A restaurant may serve the soup in winter only. The boolean cannot express "retired until 1 March". **The answer this feature records: no, a boolean — v1 has one menu and a boolean is the smallest representation that makes the distinction.** **If the owner says the menu changes seasonally, this feature becomes the wrong shape and must be re-specified**, not patched. **This is the single decision most likely to invalidate the slice.**
2. **Should a dish with open orders be retirable at all?** The current rule retires unconditionally and keeps the history. The alternative is to refuse retirement while the dish has un-served `OrderItem`s. **Recorded default: allow it** — the waiter may have already taken the order, and refusing would create a worse failure (a stuck open order) than the one being prevented.
3. **Should the QR menu (feature 11) honour retirement too?** Almost certainly yes, and **the helper is written so that answering this is a one-line change** — but the QR menu surface belongs to feature 11 and this feature does not modify it. **Recorded as a follow-up pointer, not a scope item.**
4. **Should a retired dish still be selectable by the waiter for an existing open visit?** Same reasoning as question 2. **Recorded default: yes, it stays orderable for a visit that began before the retirement** — because a table that already ordered the soup is still going to receive it.
5. **Who may retire a dish?** The owner. **Auth is a separate, open problem in LE31** (`server_id: int = 1,  # TODO: from auth token` is still in the code — feature 426's ground). **This feature does not implement auth and does not pretend to.**

## Why this matters

A menu is the thing the owner changes most often, and it is the one thing the schema cannot change. Every other thing LE31 records — stock, orders, bills, shifts — has a place to go. The menu does not.

The failure this prevents is not hypothetical and not dramatic: it is a waiter offering the soup on a day the kitchen stopped making it, and then the owner explaining to a customer why the thing they ordered is not on the menu. That is a small, embarrassing, entirely avoidable failure, and the schema currently makes it **inevitable** — because the only available actions are *leave it on the menu* or *destroy the history*.

**The cost side is the reason this is a `build` and not a `defer`.** One boolean column, one service module, two routes, one filter, one test file. **Three to five hours.** No training, no new surface, no new dependency, no new router family beyond the one this creates. Compare that to the alternative the owner currently has: **mentally filtering the menu**, forever.

**And it is reversible.** Drop the column and the routes; nothing today reads a field that does not exist yet. **The only irreversible thing would be if a dish were deleted under the current schema in the meantime** — which is precisely the loss this feature exists to prevent, and which makes the column's value *rise* with time rather than fall.

## Adjacent evidence

- **`YuxuanZHO/Canyon`** (Python + Flet + SQLite, created 2026-11-02, pushed 2026-11-04, ★0/⑂0, licence-null, **in-window by both `created_at` and `pushed_at`**): **the trigger.** README L32-33 verbatim: *"Create, edit, enable/disable and delete dishes; delete is refused while an order references the dish (disable instead)."* Also L34: *"Categories: create, rename, reorder, activate/deactivate, delete with reassignment."* **Recorded as vocabulary; no code is adopted** (the licence is null and the stack — Flet — is off-charter).
- **`rkevrellan/ComandaPOS`** (Python/Flask, Panama, created 2026-11-05, ★0, licence-null): separates catalogue removal from operational deactivation, and refuses a **discount above a threshold unless a supervisor authorises it**. **Off-stack and jurisdiction-specific; recorded as adjacent evidence, not picked.**
- **`Jmonczewski-droid/kisnet-pos`** (FastAPI + SQLAlchemy 2.0, ★0, licence-null, created 2026-11-03): the *menu/recipe snapshot* half — *"each item's name, price, and recipe are saved at the moment of sale, so changing the menu never rewrites past sales."* **This is the same principle applied to a different field**: changing the menu must not rewrite the past. **Feature 386 already records that `OrderItem.unit_price` is a snapshot**, so the *price* half is owned. **This feature extends the principle to the *dish's existence*.**
- **Feature 397** (sold-out availability state) — **the adjacent pair, not a duplicate.** 397 owns *"is it available **today**"* (derived, per-day, from the ledger); this feature owns *"is it on the menu **at all**"* (stored, until changed). **The two must be composed by the caller and never merged into one column.**
- **Feature 431** (category canonicalisation) — the *same table, a different field*. **Evidence that the `MenuItem` row has been audited field-by-field before, and that this field was not.**
- **Feature 398** (`is_prepared` — "the rule with no consumer") — **the closest structural analogue in LE31**: a boolean on `MenuItem` that nothing reads. **This feature is the second such boolean, and it is read.** *Recorded as an observation, not a dependency.*
