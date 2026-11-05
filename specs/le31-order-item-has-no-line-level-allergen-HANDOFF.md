# HANDOFF — 439-le31-order-item-has-no-line-level-allergen

> **Slice contract for the coding agent.** Produced by the 83rd LE31 daily-research pass (2026-11-05), Pick B.
>
> **Feature file**: `features/439-le31-order-item-has-no-line-level-allergen.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `OrderItem.model_fields` returned `['course','fired_at','id','menu_item_id','notes','qty','ready_at','served_at','status','unit_price','visit_id']` and `MenuItem.model_fields` returned `['category','id','is_prepared','name','photo_url','unit','unit_price']` — **neither carries an allergen field**, and `OrderItem.notes` is the only free-text channel, so "the dish contains nuts" and "the guest is allergic to nuts" are recorded identically). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking** — **subject to the stop condition below, which can only cancel this slice, never delay it.**

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §3.2's Privacy invariant, §4.1 (SQLite dev / Postgres prod, same SQLModel code), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. **⛔ EXECUTE THE STOP CONDITION FIRST** (see below). **If feature 10's implementation has already landed with a line-level allergen field, STOP and close this slice as a duplicate.**
5. **Read `features/10-…` FIRST** and reuse its 14-allergen vocabulary verbatim. **Do not re-derive, re-order or re-decide the list.**
6. **Add the `allergen_codes` column** to `class OrderItem` in `backend/app/models.py`, with the comment recording the vocabulary source and the `NULL` semantics.
7. **Create `backend/app/services/__init__.py` and `backend/app/services/allergens.py`** with `ALLERGEN_CODES`, `parse_allergens()` and `is_recorded()` — **one definition of the vocabulary**, shared by the write path and the read path.
8. **Implement `validate_codes(raw) -> str | None`** in the same module, with the unknown-code rejection and the canonical ordering. **This is the "never guess" rule: an unrecognised code is rejected at write time, never stored and later misread.**
9. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_allergens_are_snapshotted_onto_the_line` — it is what proves the line keeps the allergen set it was ordered under.
10. **Apply the flag to the cook's ticket surface** if that surface exists. **If it does not exist, record that in the PR description rather than creating it.**

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Re-implement any part of feature 10.** The dish-level allergen metadata, the 14-allergen list, the ingredient-level derivation, the substitutions table, the `/allergens` Telegram command and the menu badge are **all feature 10's**. **This feature owns the line, not the dish.** Duplicating any of it creates two sources of truth for the same fact.
- **Derive the line's allergens from ingredients.** **This feature states the flag; it does not compute it.** A derived value that can change after the fact is not a record.
- **Add a `/allergens` Telegram command, or any bot handler.** The command is **feature 10's** — its scope already names it. Feature 10's command answers *"what is in this dish?"*; this feature's flag answers *"what is on this order?"*. **Two questions, two surfaces, and feature 10 already owns one of them.**
- **Store guest identity, a guest id, a guest name, or an allergy profile.** **This is the charter's Privacy invariant and it is hard.** The flag is a property of the **plate and the order**, not of a person. **No guest table. No contact data. No per-person allergy record.**
- **Touch `MenuItem`.** It is **feature 10's** ground, and its schema is unchanged by this feature.
- **Create `backend/app/routers/orders.py`.** There is no orders router today — `backend/app/routers/` holds only `__init__.py` and `tables.py`. **This contract supplies the validation *function* and its tests; it does not build the router.** If feature 02's router has landed by the time you start, call `validate_codes()` from it; **if not, build the function and record in the PR description that feature 02's router must call it.**
- **Add an `OrderItem` mutation route.** The field is written at line creation and **not updated afterwards** in v1.
- **Touch `OrderItem.course`, `status`, `fired_at`, `ready_at`, `served_at`, `notes`, `qty` or `unit_price`.** `notes` in particular — **this feature adds a structured field so that facts stop hiding in free text; it does not remove or re-purpose `notes`.**
- **Touch `Bill`, `DerivedTip`, `Visit`, `Shift`, `Batch`, `StockEntry`, `Table` or `AppUser`.**
- **Introduce Alembic**, or add a foreign key or an index. That is **feature 427** for FKs; charter §3.2 for Alembic.
- **Build a customer-facing allergen surface** (QR menu quiz, receipt). Charter §3.2 non-goals; feature 10's own out-of-scope.
- **Build an allergen briefing.** That is **feature 12**.
- **Record a substitution on a line.** Feature 10 owns the substitutions table; the substitution sharp edge is recorded as a known limitation.
- **Change `PROJECT_CHARTER.md`.** The charter is the owner's document.

**Disambiguation**: this slice is about **the allergen state of one order line**. It is **not** about the dish's composition (10), briefings (12), customer-facing surfaces (11), order-line insertion time (430), transition attribution (379), batch provenance (385), the active-visit write guard (436), the bill (05/415), or guest identity (charter §3.2).

## ⛔ The stop condition — execute this BEFORE writing any code

> **If feature 10's implementation has already landed and it added a line-level allergen field to `OrderItem`, this feature is a DUPLICATE and must be CLOSED, not merged and not re-implemented.**
>
> The parent's corpus probe — `order item allergen`, `allergen on the line`, `per-line allergen`, `dietary flag`, `guest allergy on the line`, `line-level allergen` — returned **0 hits across all 471 feature files and all spec files**, with a **passing negative control** on the same corpus, so the zero is meaningful rather than a broken grep.
>
> **That establishes the gap as unfilled *in the corpus*. It does NOT establish it as unfilled *in an unmerged branch*.**
>
> **The agent's first actions, in order:**
> 1. `git log --all --oneline -- features/ | head -50` and `git branch -a` — look for an unmerged feature-10 implementation.
> 2. `grep -rn "allergen" backend/app/` — look for an existing allergen field anywhere in the code.
> 3. If **either** shows a line-level allergen field, **STOP**, write a PR that says *"duplicate of feature 10 — closing"*, and **do not write code**.
>
> **Feature 10 is filed but not implemented as of this contract.** If it lands first, this pick is closed with the reason recorded. **This is the only condition in this contract that can cancel the slice.**

## Frozen contract

**The one thing this contract exists to make true:** *the allergen facts attached to an order line are recorded as structured, readable facts — and they are a record of what was communicated at the moment the order was taken, not a value that can change afterwards.*

Concretely, after this slice lands:

1. `order_item` carries exactly one `allergen_codes: str | None` column.
2. The 14-allergen vocabulary has **exactly one definition**, shared by the write path and the read path.
3. An **unknown allergen code is rejected at write time** with an error naming the code. **It is never stored.**
4. Stored codes are in a **canonical order**, so `"nuts,milk"` and `"milk,nuts"` are the same stored value.
5. `NULL` means **not recorded**. It is **not** "allergen-free", and the two are **not** collapsed.
6. The line's allergens are a **snapshot**: changing the dish's own metadata afterwards does **not** change the line.

**The prohibition:** *guessing an allergen code, deriving it from a recipe that can change, and collapsing "not recorded" into "no allergens".*

### The snapshot rule — where it comes from and why it is load-bearing

`Jmonczewski-droid/kisnet-pos`, README L26, verbatim: *"**Price snapshots:** each item's name, price, and **recipe** are saved at the moment of sale, so changing the menu never rewrites past sales."*

**The line's allergen set is a snapshot.** It is what was true and communicated at the moment the order was taken. If the kitchen later changes the recipe, the historical line **keeps the allergen set it was ordered under** — and that is not a bug, it is the point: it is the record of what the guest was told. **The regression test `test_allergens_are_snapshotted_onto_the_line` is the enforcement.**

### The `NULL` semantics — why the default is not "no allergens"

`NULL` means *nothing was recorded*. `""` would mean *recorded, and nothing applies*. **The feature deliberately does not collapse those two**, because they are different facts: a line where the waiter said nothing about allergens is **not** a line that is safe to serve without asking.

**The `is_recorded()` helper exists precisely so that the distinction can be made at render time** — a line where nothing was recorded must render **differently** on the cook's ticket from a line recorded as "no allergens". **Otherwise the kitchen reads silence as safety.** That is the whole reason the helper is separate from `parse_allergens()`.

### The string-vs-join-table decision — recorded, not assumed

A `order_item_allergen(order_item_id, allergen)` join table is the textbook shape and is **deliberately not used**, for two recorded reasons:

1. **LE31 v1 has one restaurant and a small menu.** A join table for one row per order line is a second table to keep consistent for no query v1 needs to answer. **If a "lines involving nuts this month" query is ever needed, that is a separate change** — and it is the moment to revisit this decision.
2. **The snapshot property is easier to guarantee with one column.** A join table needs the same "insert rows, never update" discipline the ledger already has; a single column is simply written once at creation.

**The vocabulary check is what makes the string safe:** a code that is not one of the 14 is rejected at write time. **That is the "never guessed" rule from `YuxuanZHO/Canyon` applied to the field this feature adds.**

### The 10/439 boundary — resolve before writing code

| If | Then |
|---|---|
| **10 has not landed** (today's state) | 439 lands alone. The 14-allergen list is reused from **feature 10's specification** (`features/10-allergen-tracking.md`), which is written down even though it is not implemented. The line's flag is **stated by a person**, and the dish's metadata is read only if it exists. |
| **10 has landed first** | 439 reads 10's dish-level metadata and **snapshots it onto the line** at creation. 439 must **not** re-implement 10's derivation, and 10 must not be modified. |

**Either way: the dish's metadata and the line's snapshot are two different records, with different lifetimes.** The dish's composition does not change during service; a guest's requirement is a property of one visit and disappears when the visit closes.

## Files to touch

| File | Action | Notes |
|---|---|---|
| `backend/app/models.py` | **modify** | Add `allergen_codes: str \| None = None` to `class OrderItem`, with a comment recording the vocabulary source (feature 10) and the `NULL` semantics. **One line.** |
| `backend/app/services/__init__.py` | **create** | `backend/app/services/` **does not exist today.** |
| `backend/app/services/allergens.py` | **create** | `ALLERGEN_CODES`, `parse_allergens(raw)`, `is_recorded(item)`, `validate_codes(raw)`. **One definition of the vocabulary.** |
| `backend/tests/test_allergens.py` | **create** | The regression tests listed below. **Confirm the project's test path before assuming this one.** |
| `features/10-allergen-tracking.md` | **modify** | One line: feature 10 owns the dish, feature 439 owns the line. |
| `backend/app/routers/orders.py` | **modify — ONLY IF feature 02 has already landed it** | Call `validate_codes()` from the line-creation path and reject an unknown code with HTTP 422 naming the code. **If the router does not exist, DO NOT create it** — record in the PR description that feature 02's router must call `validate_codes()`. |

**Not touched:** `backend/app/routers/menu.py` (feature 438's), `backend/app/routers/tables.py`, `backend/app/db.py`, the bot module, `index.html`, `PROJECT_CHARTER.md`, `MenuItem` and every other model.

## Mandatory LE31 skill list

The coding agent **must** load these before writing code. They are in the project repo at `skills/`, and on this VPS they are **not** in the standard `skills_list` index — read them from disk:

- **`le31-conventions`** — `skills/le31-conventions/SKILL.md`. **The fixed stack, the hard invariants (especially the Privacy invariant), and the seven-check gate.**
- **`le31-v1-feature-pattern`** — `skills/le31-v1-feature-pattern/SKILL.md`. **The contract shape and the Definition of Done.**
- **`development`** → `speckit-specify` / `speckit-plan` / `speckit-tasks` / `speckit-implement`. **Product behaviour changes go through the development pipeline.**
- **`pre-merge-review`** — **product code does not merge on the author's say-so.** An independent reviewer must sign off.

**Also read (not skills, but mandatory context):** `features/10-…` (the vocabulary and the boundary), `features/12-…` (briefings), `features/431-…` (the canonicalisation pattern this feature mirrors), `features/430-…` (the same table, a different column), and `PROJECT_CHARTER.md` §3.2 and §3.4.

## Mandatory inputs

| Input | Where | Why |
|---|---|---|
| `PROJECT_CHARTER.md` §3.2 (non-goals, incl. **"Capture of guest gender, age, or any PII beyond counts"**), §3.4 (no customer-facing AI) | repo root | **The non-goals list is a hard filter.** The Privacy invariant is the reason this feature is about the *plate*, not the *person*. |
| `features/10-…` | `features/` | **The 14-allergen vocabulary, reused verbatim. And the boundary.** |
| `features/12-…` | `features/` | Pre-shift briefings — **out of scope here.** |
| `features/431-…` | `features/` | **The canonicalisation pattern this feature mirrors** (a free-text field carrying structured meaning). |
| `features/430-…` | `features/` | The same table, a different column. |
| The proof script | `/opt/data/le31_proof_picks_2026_11_05.py` | **The parent's execution transcript for this finding.** Run it with `/opt/data/le31-verify-2026-10-27/.venv/bin/python` — that venv has `sqlmodel`/`fastapi`/`pydantic`; **the system Python does not have `sqlmodel`.** |
| The research report | `/opt/data/le31-daily-research-2026-11-05.md` | The pass, the evidence, and the rejected alternatives. |
| The trigger README | `/tmp/le31-daily-2026-11-05/readme/readme_Jmonczewski-droid__kisnet-pos.md` | The snapshot rule, verbatim, at L26. |

## Verification protocol reference

**Reference**: `skills/le31-research-workflow/SKILL.md` (the curl-only anti-fabrication and signed-delta discipline) and `skills/le31-first-party-defect-proving/SKILL.md` (the execution-proof method). **Read `le31-first-party-defect-proving` — this feature was proven that way and the agent must preserve that property in its own tests.**

**The required regression tests** (all in `backend/tests/test_allergens.py`):

1. `test_line_reads_back_its_allergens` — a line created with allergens reads them back.
2. `test_line_without_allergens_is_empty_and_uninvented` — a line created **without** allergens reads back **empty** — **not `None`-as-default-and-not-invented**, and specifically **no default allergen set is fabricated**. (The precise assertion: `parse_allergens(None) == []` **and** `is_recorded(line) is False` — the two facts stay distinct.)
3. `test_allergens_are_snapshotted_onto_the_line` — **the snapshot test.** Change the dish's own allergen metadata afterwards; the line's recorded allergens are **unchanged**.
4. `test_unknown_allergen_code_is_rejected` — `validate_codes("nuts,unicorn")` raises / returns an error naming `unicorn`, and **nothing is stored**.
5. `test_allergen_codes_are_stored_in_canonical_order` — `"nuts,milk"` and `"milk,nuts"` produce the **same stored string**.
6. `test_ticket_read_renders_the_flag` — a line with allergens is rendered with the flag on the ticket read. **Only if a ticket surface exists**; **if it does not, record that in the PR description rather than creating the surface.**

**Method — the one that matters:** **write the tests first, watch them fail against the current code, then apply the change and watch them pass.** A test that only ever passed proves nothing, and this feature's entire value is the *distinction* between "not recorded" and "no allergens" — exactly the kind of thing a test that never failed cannot certify.

**End-to-end before commit** (charter §7): run the actual validation and the actual read path against a real database and observe the behaviour change. **Do not declare done from a diff or from green tests alone.**

**Anti-fabrication:** every claim in the PR description must be traceable to a command you ran and its output. **No number, no status code and no test count that you did not observe.**

## Rollback path

**Fully reversible, and deliberately so.**

- **The code rollback:** drop the column, drop `services/allergens.py`, drop the test file, revert the one-line note in `features/10-…`, and revert the router call if one was added. **Nothing today reads a field that does not exist yet, so no existing behaviour can regress.**
- **The data rollback:** `allergen_codes` defaults to `None`, so **every existing `OrderItem` row is unaffected** and the change is a no-op on existing data.
- **The migration rollback:** LE31 uses `init_db()` (charter §3.2 — **Alembic is a non-goal for v1**), so there is no migration file to revert. **If a migration file is created anyway, that is a scope violation of this contract.**
- **The one irreversible thing:** **if a customer was served something they were told was safe while this feature was in flight, that cannot be undone.** That is the whole argument for building it now rather than deferring it.

**Rollback cost:** minutes. **No data is at risk.**

## Sign-off gap

**What this contract does NOT establish, and the agent must not assume:**

- **That feature 10's implementation exists.** It does not, today. **This feature can ship ahead of it** — the vocabulary is specified in feature 10's contract even though it is not implemented. **But the agent must confirm the stop condition before starting.**
- **That the cook's ticket surface exists.** It may not. **Record it in the PR description if it does not — do not create it.**
- **That the order-taking router exists.** It does not, today. **Build `validate_codes()` and its tests; leave the router wiring to feature 02.**
- **That the line's allergens are ever rendered to anyone.** Without a ticket surface, the flag is recorded and unread. **That is the honest state of this slice, and it must be stated in the PR description rather than papered over with a new surface.**
- **That the dish's allergen metadata exists.** Feature 10 owns it. Until it lands, the line's flag is **stated by the waiter**, which is exactly what this feature specifies.
- **Any owner decision about substitutions.** The substitution sharp edge is recorded as a known limitation, not solved.

## Handoff summary

One column on `OrderItem`, one service module holding the 14-allergen vocabulary and two helpers plus the validation function, one line of wiring into feature 02's router **if it exists**, and the regression tests. **Four to six hours.**

The gap was **proven by execution**, not inferred: `OrderItem` and `MenuItem` **both carry no allergen field**, and `notes` is the only free-text channel — so *"the dish contains nuts"* and *"the guest is allergic to nuts"* are **recorded identically, with no way to query or render them differently.**

**The one boundary that must not be crossed:** feature **10** owns **the dish**; this feature owns **the line**. **10 answers "what is in this dish?"; 439 answers "what did we tell the kitchen about this plate?"** Both are needed; neither subsumes the other.

**The two rules that make the field safe:** an **unknown allergen code is rejected, never guessed** (from `YuxuanZHO/Canyon`'s never-guess rule), and **`NULL` means "not recorded", never "allergen-free"** — because a kitchen that reads silence as safety is the failure this feature exists to prevent.

**And the boundary that must not be crossed at all:** **no guest identity, no guest id, no name.** The flag is on the **plate**. That is what makes this feature compatible with LE31's rule that v1 stores counts, not identities.
