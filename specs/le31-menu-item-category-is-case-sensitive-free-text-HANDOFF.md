# HANDOFF — 431-le31-menu-item-category-is-case-sensitive-free-text

> **Slice contract for the coding agent.** Produced by the 97th LE31 daily-brainstorm pass (2026-11-03), Pick C.
>
> **Feature file**: `features/431-le31-menu-item-category-is-case-sensitive-free-text-first-party-three-spellings-of-one-category-are-three-categories-v1-category-canonicalisation.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: three `MenuItem` rows named `Tiramisu` with categories `"dessert"`, `"Desserts"` and `"dessert "` came back as **three distinct categories**). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod, same SQLModel code), §7 (the quality bar: *"No magic numbers"*, *"No dead code"*, *"End-to-end before commit"*), the truth invariant.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. **Read `features/386-…` FIRST.** It is the feature that **recorded this gap and did not pick it** — its *Adjacent evidence* says, verbatim: *"**The category-nesting gap (NOT this feature).** … `MenuItem.category` is a plain `str`. … **Recorded, not picked.**"* **This slice picks the *normalisation* half, not the *nesting* half.** The commit message must say so.
5. **Define the canonicalisation helper in one place** — `backend/app/services/` (new package; features 374 and 430 also expect it to exist) or `backend/app/config.py` — and apply it at every write site.
6. **Add the `CHECK` constraint** (option a or c) so an un-canonical value **cannot be stored**, and normalise the existing rows.
7. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_non_canonical_category_cannot_be_stored`: inserting `"Dessert"` directly, bypassing the helper, must be **rejected by the database**.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Design or add a category hierarchy / nesting.** Feature 386 explicitly recorded nesting as *"NOT this feature … Recorded, not picked."* **Nesting is a menu-structure question and is not this slice.**
- **Add a `menu_category` table** — *unless* the agent picks **option (b)** in the feature file, and **option (b) has a hard dependency on feature 427** (see *Frozen contract*).
- **Change `MenuItem.name`.** Names are **labels**, categories are **keys**. A dish legitimately has many names. **Do not normalise names.**
- **Change `MenuItem.unit`.** That is **features 386 / 392 / 407** — **filed**.
- **Change `MenuItem.is_prepared`.** That is **feature 398** — **filed**.
- **Answer charter §3.3's tax question** (*"Tax — flat 10%? Per-category? Per-item?"*). That is the **owner's** decision and is **features 408 / 409**'s territory. This slice only makes the `category` *string* trustworthy so that, if the owner later chooses per-category tax, the data supports it.
- **Implement the `/start_today` OCR flow, or write a menu router.** Charter P0 row 44 is a charter row with **no router today** — `backend/app/routers/` holds only `__init__.py` and `tables.py`. **This contract provides the helper; it does not create the OCR pipeline.**
- **Semantically merge categories** (`"Mains"` and `"Main Dishes"`). **Default recorded: normalise mechanically only** (`lower` + whitespace-collapse). **A semantic merge is an owner decision with a menu to hand.**
- **Introduce Alembic**, or add a foreign key. Charter §3.2 and **feature 427** respectively.

**Disambiguation**: this slice is about **the `category` string being canonical**. It is **not** about the *category tree* (386's deferral), the *unit* (386/392/407), the *prepared flag* (398), the *tax rate* (408/409), the *OCR flow* (charter P0 row 44), or the *timestamps* (429/430).

## Frozen contract

**The one thing this contract exists to make true:** *any two rows a human would call the same category land in the same category.*

Concretely, after this slice lands:

1. **One** canonicalisation function exists, defining the canonical form of a category (default recorded: whitespace-collapse + case-fold).
2. Every write site applies it.
3. **The database rejects an un-canonical value** — a `CHECK` constraint, so the rule holds for *every* path including one added in six months.
4. Existing rows are normalised.

**The prohibition:** *a normalisation rule that lives only in the application path* — a rule the next write path will forget — and *a category that can be spelled two ways and stored anyway*.

### The 427 dependency — only if option (b)

| Option | FK dependency | Status |
|---|---|---|
| **(a) canonicalise + `CHECK`** | **none** | **Recommended.** No schema change, no FK, identical behaviour in dev and prod for the mechanism that matters (the Python-side helper). |
| **(b) `menu_category` table + FK** | **hard dependency on feature 427** | LE31's `PRAGMA foreign_keys` is **off** in dev, so a new FK would be **unenforced in dev and enforced in prod** — exactly the divergence 427 exists to close. **If the agent picks (b), feature 427 must land first.** |
| **(c) canonicalise + `CHECK` + a fixed vocabulary in `config.py`** | none | Acceptable, but see the hazard below. |

**The option (c) hazard, stated so it is not discovered by accident:** a hard-coded category list in `config.py` must agree with what the OCR flow emits — **or the OCR flow will be rejected by the very constraint meant to protect it.** Option (c) is listed third for that reason.

### The load-bearing test, which must be written **before** the change and watched to fail

```python
def test_non_canonical_category_cannot_be_stored(session):
    """The database must reject an un-canonical category, not just the app."""
    mi = MenuItem(name="Tiramisu", category="Dessert", unit_price="8.80")
    session.add(mi)
    with pytest.raises(IntegrityError):
        session.commit()
```

**This test fails on the unfixed code** (today the row is simply accepted) and it is the test that distinguishes a real fix from a *helper-only* fix that a future write path could bypass.

**Three companion tests**, each equally load-bearing:

```python
def test_category_is_canonicalised():
    assert canonical_category("  Dessert ")  == "dessert"
    assert canonical_category("DESSERT")    == "dessert"
    assert canonical_category("Main   Dish") == "main dish"   # collapse, not just trim

def test_three_spellings_of_one_category_land_together(session):
    # three rows, three spellings -> ONE category when read back
    ...

def test_menu_item_name_is_not_canonicalised():
    """Names are labels; categories are keys. This guards the boundary."""
    assert MenuItem(name="Tiramisu", ...).name != MenuItem(name="tiramisu", ...).name
```

## Files to touch

| File | Change |
|---|---|
| `backend/app/models.py` | `class MenuItem` — option (a)/(c): add `__table_args__` with the `CHECK` constraint. Option (b): add `menu_category` + `category_id`. |
| `backend/app/services/category_service.py` *(new)* | The **single** definition of `canonical_category(raw)`. **One definition, used by every write site.** |
| `backend/app/services/__init__.py` *(new)* | Empty package marker. **Note: features 374 and 430 also expect `services/` to exist — three contracts creating the same package in one week is friction, not a conflict.** |
| `backend/app/db.py` | The `init_db()` path — **no Alembic**; the normalisation `UPDATE` for existing rows. |
| `backend/tests/test_menu_item_category.py` *(new)* | The four tests above. |

**Do not create** `backend/app/routers/menu.py` or a menu write path — there is none today and this contract does not add one.

## Mandatory LE31 skill list

The agent must load these **before** writing code:

- **`le31-conventions`** — the seven-check feature gate and the hard invariants (§3.2 the fixed stack and the `init_db()` policy; §4.1 the dialect rule; §7 the quality bar; the truth invariant; *Known conflicts*).
- **`le31-v1-feature-pattern`** — the canonical contract shape, the slicing rules, and the *Definition of Done* (which requires the **actual path** to be exercised, not merely a passing test).
- **`le31-handoff-spec`** — the frozen-contract discipline.
- **`le31-research`** — the source-of-truth discipline behind the quotes in the feature file.

The agent must **NOT** load `le31-feature-pipeline` — the slice is already in the pipeline.

**The mandatory reading list** (read; do **not** merge):

| Document | Why it must be read |
|---|---|
| `features/386-…-v1-menu-item-options.md` | **The nearest sibling — the feature that recorded this gap and did not pick it.** Its *Adjacent evidence* names the deferral verbatim. Read it so this slice does not silently open the nesting question. |
| `features/392-…-v1-menu-item-unit-meaning.md` and `features/407-…` | `MenuItem.unit`'s meaning — **the same pattern on a sibling column.** Read them so this slice does not duplicate a normalisation rule that already exists. |
| `features/398-…` | `MenuItem.is_prepared` has no consumer. Not touched, but read so the agent knows the sibling column is already owned. |
| `features/427-…-v1-sqlite-fk-enforcement.md` | **A hard prerequisite for option (b) only.** Option (a) has no such dependency. |
| `features/408-…` and `features/409-…` | The tax **rate** and its home. **This slice does not answer charter §3.3's tax question.** |
| `features/429-…` and `features/430-…` | This pass's other two contracts. **Independent** — one is about timestamps, one about a category string. |
| `PROJECT_CHARTER.md` §3.2, §3.3, §4.1, §7, §8 | The source of truth. **§3.3 is the open-questions list — read question 3 (tax) so you do not accidentally answer it.** |

## Mandatory inputs

- **The defect itself** — `class MenuItem` in `backend/app/models.py`, verbatim:

  ```python
  name: str
  category: str
  ```

  **No default, no length limit, no normalisation, no constraint, no lookup.**

- **The measured fact** — executed against LE31's real schema on 2026-11-03:

  ```
  category_variants_for_same_item   ["Desserts", "dessert", "dessert "]
  category_variants_count           3
  category_is_case_sensitive        true
  ```

  Three `MenuItem` rows, all named `Tiramisu`, all at `8.80`, in **three** categories.

- **The re-runnable probe** — `/opt/data/_bs_probe_body2_2026-11-03.py` builds LE31's schema and prints the same numbers. The agent may re-run it (it needs a venv with `sqlmodel`; one exists at `/opt/data/le31-verify-2026-10-27/.venv` — **reuse it, do not provision a new one**).

- **The corpus's own record of the gap** — feature 386's *Adjacent evidence*, verbatim:

  > *"**The category-nesting gap (NOT this feature).** — 'Category management with nesting' — `MenuItem.category` is a plain `str`. Nesting categories is a menu-structure question, not an option question. **Recorded, not picked.**"*

## Verification protocol reference

`PROJECT_CHARTER.md` §8 is the protocol; this slice's specific sequence is:

1. **Write the test first.** `test_non_canonical_category_cannot_be_stored` — watch it **FAIL** (today the row is accepted, so the test must fail before the constraint exists).
2. Apply the change (the helper, the constraint, the normalisation pass).
3. **Watch the test PASS.**
4. **Re-run the whole test suite** — this slice must not break another slice's test.
5. **Exercise the actual path**: start the app (`cd backend && uvicorn app.main:app --reload`), confirm `http://localhost:8000/docs` loads, and confirm the constraint is live in the running app's schema (`sqlite3 backend/restaurant.db ".schema"` — the `CHECK` must be visible).
6. **Verify the existing rows were normalised**: `sqlite3 backend/restaurant.db "select distinct category from menu_item;"` — the output must contain **no** category that differs from its own canonical form.
7. `git add -p && git commit -m "Feature 431: menu_item.category canonicalisation — <option (a)|(b)|(c)> (386 deferral: normalisation, not nesting)"` — **the commit message must name the option and state that this is the normalisation half, not the nesting half.**

**Manual verification is acceptable for v1** (charter §7) — **but** the regression tests in this contract **are** required: they are what makes the rule hold for a write path that does not exist yet.

## Rollback path

- **Option (a)/(c)**: drop the `CHECK` constraint (`__table_args__`) and delete the helper file. The `category` column is untouched and its data is unchanged.
- **Option (b)**: revert `MenuItem.category_id` → `category` and drop the `menu_category` table. **This is a larger rollback** and involves a data migration back — **which is why option (a) is recommended.**
- **The normalisation `UPDATE` is not reversible by re-running an inverse `UPDATE`** — `"Dessert"` becomes `"dessert"` and the original capitalisation is **not recoverable from the row alone.** It *is* recoverable from the source menu photograph. **This must be stated in the commit message**: the normalisation is a **one-way change to a display string**, and the owner should be told the menu's capitalisation will change.

**Note on the dev database**: charter §3.2 uses `init_db()`, so a dev database is disposable — drop and re-create. **Record the prod-migration step as known debt** in the commit message.

## Sign-off gap

- **⚠️ The canonical vocabulary is the owner's decision.** The *mechanical* rule (case-fold + whitespace-collapse) is implementation. *Which strings are the same category* is a judgement about this restaurant's menu. **Default recorded: normalise mechanically only** and **do not semantically merge** — `"Mains"` and `"Main Dishes"` stay distinct until the owner says otherwise.
- **⚠️ Should the vocabulary be fixed or open?** **Default recorded: open** (option a) — a restaurant that adds a "Kids" section should not need a code change. Option (c)'s fixed list carries the hazard noted above.
- **⚠️ Should categories be case-folded at all, or only whitespace-collapsed?** Case-folding loses display capitalisation. **Default recorded: store the canonical lower-case form**; if display capitalisation is wanted later, add a separate display name. **A key that must be displayed is a key that will be re-typed and will drift.**
- **⚠️ The empty string is currently accepted as a category.** **Default recorded: reject `""`** as part of the constraint — a small decision, recorded so it is not made by accident.
- **⚠️ The owner has not chosen option (a), (b) or (c).** **Default recorded: option (a)** — it satisfies the Goal with no schema change, no new dependency, and no FK-enforcement dependency. **But this is an owner decision and the agent should implement the default and say so clearly in the commit message.**
- **⚠️ The write path this protects does not exist yet.** The `/start_today` OCR flow is a charter P0 row with no router. The helper is therefore **unreferenced today** — the same honest position as feature 430's helper. **The agent should say so in the commit message** so a reviewer does not read it as dead code (charter §7): it is a specification, and the specification is the deliverable.

## Handoff summary

| | |
|---|---|
| **Feature** | 431 — `MenuItem.category` is case-sensitive free text |
| **Verdict** | `build` (OBSERVED — three spellings, three categories) |
| **Bucket** | v1 — schema hygiene on the table the P0 menu row depends on |
| **Files to touch** | `backend/app/models.py`, `backend/app/services/{__init__,category_service}.py` (new), `backend/app/db.py`, `backend/tests/test_menu_item_category.py` (new) |
| **New dependency** | none (option a); **feature 427 required first** if option b |
| **Reversible** | mostly — the constraint and helper are trivially removable; **the normalisation `UPDATE` is one-way** (recoverable only from the source menu photo) |
| **Hard prerequisite** | none under option (a); **feature 427** under option (b) |
| **Must not touch** | `MenuItem.name`, `MenuItem.unit`, `MenuItem.is_prepared`, the category *tree*, the OCR flow, the tax rate |
| **Known debt created** | the prod migration for the constraint and the normalisation pass (the standing `init_db()`-not-Alembic debt) |
