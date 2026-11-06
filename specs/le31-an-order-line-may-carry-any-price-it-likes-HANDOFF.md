# HANDOFF — le31-an-order-line-may-carry-any-price-it-likes

> **Slice contract for the coding agent.** Produced by the 99th LE31 daily-brainstorm pass (2026-11-06), Pick C.
>
> **Feature file**: `features/449-le31-an-order-line-may-carry-any-price-it-likes.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite DB, then a `MenuItem` with `unit_price = 2.50` and an `OrderItem` pointing at it with `unit_price = 99.00` — **ACCEPTED**; **menu price = 2.50 ; line price = 99.00 ; ratio = 39.6x**). There is no rule connecting them, no default, and no derivation: the "snapshot" is not a snapshot of anything, it is a number the caller typed). All seven checks pass; check 1's **demand** is classed INFERRED, which is why this contract is deliberately **one helper, one call site, one nullable reason column** and adds no surface. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-brainstorm-2026-11-06.md`.
>
> **Report**: `/opt/data/le31-brainstorm-2026-11-06.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/449-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §3.6 (money is `Decimal`, never `float`), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/444-le31-order-item-unit-price-is-mutable-in-place-with-no-trace` FIRST** and confirm the ordering described under *Frozen contract* below. **444 owns the CHANGE and the TRACE; this slice owns the SOURCE.** **444 must land first, or in the same PR.**
6. **Read `features/446-le31-has-no-schema-evolution-mechanism` and confirm the ordering described under *Frozen contract*.** **This slice adds a COLUMN to an existing table — which is exactly the operation `create_all()` cannot perform. 446 is a HARD dependency.**
7. **Add `price_reason: str | None = None` to `class OrderItem`** — **nullable**, so it needs no backfill.
8. **Create `backend/app/services/ordering.py`** with `price_for(...)` and `ALLOWED_PRICE_REASONS`, exactly as specified in the feature file's *Data model*.
9. **Provide the write path** — if feature 02's order-taking route exists, call `price_for` from it; if it does not, provide a thin `create_order_item(...)` helper the future route will call. **Do not write the route; that is 02's.**
10. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_line_price_defaults_to_the_menu_price`.
11. **Record the source vocabulary** — one line in `features/444-…` saying that the *source* of a line's price is feature 449's.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Change the price-change trace, the helper that changes a price, or the reversibility rule.** Feature **444** owns them. **Do not modify 444.**
- **Implement discounts, promo codes, or comps as a separate model.** Feature **444**'s own out-of-scope says verbatim: *"A discount is not a rewritten price — it is a discount with its own shape."* **Same boundary here.**
- **Add a price history to the menu.** The menu is *configuration*; **feature 444 explicitly excludes it.**
- **Check the actor's role against the reason.** Feature **403** owns the role policy. **This contract checks the reason's membership, not who may use it.**
- **Cap the departure, or add a per-reason bound.** The contract's rule is *"the price is the menu price unless a reason is recorded"* — **a named reason does not make a 39.6× price correct**, and that limit is **stated, not hidden**. A per-reason bound is an **owner decision**.
- **Allow a price without a reason, or a reason without a price.** Both are **REFUSED** — the first is the defect, the second is incoherent.
- **Allow a negative price.**
- **Write the line's price from the request body.** The request may name a `menu_item_id`; **the price comes from the menu**, and the request may only *override* it **with a reason**. **This is the whole point of the slice.**
- **Make `OrderItem.menu_item_id` nullable.** A free-text item, a daily special or a comp line is **not** representable in this slice.
- **Change the bill-close route, the tax, the tip formula, or the money columns.** Features **415**, **408**, **420**, **411**.
- **Decide whether a comp consumes stock.** Feature **441** and the wider stock features own that.
- **Add a router, an endpoint, or a Telegram command.** The slice ships the helper and the reason vocabulary. **Surfaces are a later feature.**
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**

**Disambiguation**: this slice is about **where an order line's price comes from**. It is **not** about the price-change trace (444), the bill's membership of lines (435), the bill-close route (415), the tax rate (408), the money precision (411), the tip formula (420), the order-taking route (02), the role policy (403), the enum membership constraint (442), `MenuItem.is_prepared` (398), `MenuItem.unit` (392), or stock consumed by a comp (441).

## Frozen contract

**The one thing this contract exists to make true:** *an order line's price is the menu price, unless a reason is recorded.*

Concretely, after this slice lands:

1. `OrderItem` has **exactly one** new column: `price_reason: str | None = None` — **nullable**, so it needs **no backfill**.
2. `price_reason IS NULL` means **"the menu price, unchanged"**.
3. `price_for(session, menu_item, price=None, reason=None)` returns **`(menu_item.unit_price, None)`** when no price is supplied.
4. A price supplied **without** a reason is **REFUSED** — `ValueError`.
5. A reason supplied **without** a price is **REFUSED** — `ValueError`.
6. An unknown reason is **REFUSED** — `ValueError`. The allowed set is checked **in the application helper**, not by a `CHECK` constraint.
7. A negative price is **REFUSED** — `ValueError`.
8. A price **equal** to the menu price **with** a reason is **ACCEPTED** — a redundant reason records that somebody looked.
9. The line's price is a **snapshot**: the helper reads `menu_item.unit_price` **at write time** and the stored number does not change when the menu price later changes. **Feature 444's property, preserved.**
10. `ALLOWED_PRICE_REASONS` is exactly: `manager_override`, `comp`, `promo`, `happy_hour`, `correction`.
11. The helper **does not mutate** `MenuItem.unit_price`, and **does not** write a menu price history.
12. **No new table.** The reason is on the line.

**The prohibition:** *catching the `ValueError` and falling back to the menu price.* A silent fallback makes the line's price right and the **record** wrong, and the record is the thing that is supposed to explain the money.

### The 444 ordering — resolve before writing code

Feature **444** owns *a change to a line's price is recorded and reversible*. This slice owns *where the line's price comes from*. 444's contract states verbatim that `unit_price` *"stays a `Decimal` snapshot of what the line was sold at"* — **this feature is what decides what "sold at" means.**

**444 must land first, or in the same PR.** A change to a price whose origin was never recorded is a change to an **unknown baseline**, and 444's whole value is that the previous value is recoverable. **Do not merge them and do not modify 444's work.**

### The 446 ordering — resolve before writing code

This slice **adds a column to an existing table**, and `create_all()` **adds missing tables but never alters, renames or retypes an existing column**. A changed column is silently ignored and the old column keeps serving — so a feature that adds a column lands, merges, deploys, passes its tests, and **the column does not exist in the running database**.

**446 must land first, or in the same PR.** Read `features/446-le31-has-no-schema-evolution-mechanism` and follow its backup-before-`create_all()` behaviour. **Do not hand-write an `ALTER TABLE`** — that is 446's job.

### The named-departure limit — stated, not hidden

A named reason makes a departure **visible**; it does not make it **correct**. A `manager_override` of `99.00` on a `2.50` item is named and, under this contract, accepted.

**The agent may implement the contract as written.** The agent may **not** add a per-reason bound, a percentage cap, or a maximum-departure rule — **those are owner decisions**, and the contract's value is precisely that the departure is *recorded* so the question can be asked later **without re-interpreting existing rows**.

## Files to touch

**Create:**

- `backend/app/services/ordering.py` — `ALLOWED_PRICE_REASONS` and `price_for(...)`, plus, if feature 02's route does not exist, a thin `create_order_item(...)`.
- `backend/tests/test_order_line_price_source.py` — the scenario table from the feature file, as nine tests.

**Modify:**

- `backend/app/models.py` — **class `OrderItem` only.** Add `price_reason: str | None = None`.
- `features/444-le31-order-item-unit-price-is-mutable-in-place-with-no-trace.md` — **one line only**, recording that the *source* of a line's price is feature 449's. **Do not change 444's trace.**

**Read but do not modify:**

- `features/444-le31-order-item-unit-price-is-mutable-in-place-with-no-trace.md` — the hard dependency and the adjacent owner.
- `features/446-le31-has-no-schema-evolution-mechanism.md` — the hard dependency.
- `features/442-le31-enum-columns-are-varchar-with-no-membership-constraint.md` — why the reason is a checked `str` and not a new enum column. **Do not modify 442's work.**
- `features/411-le31-money-precision-declared-not-enforced-…md` — the `Decimal` guard this slice complements.
- `features/435-le31-bill-records-no-which-lines-it-charged-…md` — the bill's membership.
- `features/415-le31-bill-closes-visit-…md` — the bill-close route that reads the lines' prices.
- `features/408-le31-tax-rate-has-no-home-…md` — the tax rate home.
- `features/403-…` — the role policy this slice does **not** implement.
- `features/02-order-taking.md` — the order-taking flow this slice feeds.
- `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §3.6 (money is `Decimal`, never `float`), §7 (the quality bar).

## Mandatory LE31 skill list

The agent **must** load, in order:

1. `le31-conventions` — §3.2, §3.6, §4.1, §7, the truth invariant, the seven-check feature gate.
2. `le31-v1-feature-pattern` — the contract shape and the *Definition of Done*.
3. `le31-feature-pipeline` — where the artefacts must land.
4. `le31-handoff-spec` — this file's obligations.
5. `le31-backend` — the service-layer conventions.
6. `le31-data` — the data-model conventions (the `Decimal` rules).

**Also read** `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §3.6 (money is `Decimal`, never `float`), and §7 (the quality bar).

## Mandatory inputs

- The active feature file: `features/449-le31-an-order-line-may-carry-any-price-it-likes.md`
- This handoff: `specs/le31-an-order-line-may-carry-any-price-it-likes-HANDOFF.md`
- Feature 444's trace contract (the change side)
- Feature 446's backup-before-`create_all()` behaviour
- Feature 442's membership-constraint rule (why the reason is checked in the application)
- The charter's §3.6 money rules

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases (from the feature file's scenario table)

| # | Menu price | Call | Expected |
|---|---|---|---|
| 1 | `2.50` | no price, no reason | line price **`2.50`**, reason **`NULL`** |
| 2 | `2.50` | price `1.00`, reason `manager_override` | line price `1.00`, reason `manager_override` — **ACCEPTED** |
| 3 | `2.50` | price `1.00`, **no reason** | **REFUSED** |
| 4 | `2.50` | **no price**, reason `comp` | **REFUSED** |
| 5 | `2.50` | price `1.00`, reason `not_a_reason` | **REFUSED** |
| 6 | `2.50` | price `-1.00`, reason `comp` | **REFUSED** |
| 7 | `2.50` | price `2.50`, reason `manager_override` | **ACCEPTED** |
| 8 | menu price later changes to `3.00` | the existing line is unchanged | the line keeps `2.50` — the snapshot property, preserved |
| 9 | `2.50` | price `99.00`, reason `correction` | **ACCEPTED** — the slice requires the departure to be *named*, not to be *sane* |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Create a `MenuItem` at `2.50`. Write an order line with **no** price argument. **Observe** the stored price is `2.50` and the reason is `NULL`.
2. Attempt a line with an explicit price and **no** reason. **Observe the refusal**, and that **no row was written**.
3. Attempt a line with a price and a valid reason. **Observe** acceptance and that the reason is stored.
4. Attempt a line with a price and an **invalid** reason. **Observe the refusal.**
5. Change the menu price to `3.00`. **Observe** that the existing line still reads `2.50` — the snapshot, preserved.
6. Show the **two numbers** side by side: the menu price and the line price, and the reason that explains any difference.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code a line may carry any price with no reason at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

Use the **existing verification venv** rather than provisioning a new one: `/opt/data/le31-verify-2026-10-27/.venv` (`sqlmodel` 0.0.48, `sqlalchemy` 2.1.6). `python3` on the host has **no `pip` module** (PEP 668); do not try to install into the system interpreter.

## Rollback path

**Mostly reversible; the one irreversible part is stated plainly.**

- **Reversible:** remove the `price_reason` column from `models.py`; delete `backend/app/services/ordering.py`; remove the helper call site.
- **The one-way door:** if any order line has been written with a reason recorded, **the reasons stay.** This is the point — a reason is a record of a deliberate act, and a record that can be rewritten is not a record.
- **The schema change needs 446's mechanism.** `create_all()` cannot drop a column either. **If the column must be removed after lines exist, that is a migration decision, and 446's mechanism is the only sanctioned path.**

**No data is at risk today:** there is no order-taking write path and therefore **no `OrderItem` row exists** to be affected.

## Sign-off gap

**What the agent MUST NOT decide:**

- whether some reasons should carry their own bound (the contract's rule is **visibility, not sanity**);
- whether `happy_hour` is a price or a schedule (if it becomes a time window on the menu item, **that is a different concept and a different feature**);
- whether the reason should carry an optional free-text note as well as a code (this contract implements **the code alone**);
- which roles may use `manager_override` or `comp` (feature 403's);
- whether a comp consumes stock (feature 441's and the wider stock features');
- what happens to a line whose menu item is later deleted (the snapshot survives; the menu item is not deletable today);
- the menu price's own history (feature 444 explicitly excludes it).

**What the agent must report back:**

- the nine scenario results, **one row each, with the observed outcome**;
- the **failing-then-passing** proof for `test_line_price_defaults_to_the_menu_price`;
- the **snapshot observation** — the menu price changed to `3.00` and the line still reads `2.50`;
- confirmation that **the price came from the menu**, not from the request body, in the write path the agent produced;
- a `git diff` on `models.py` showing **exactly** the one column;
- confirmation that **no rows were backfilled** and that **no order line was written** during the work;
- confirmation that features **444**, **446** and **442** were read and that the ordering is satisfied or explicitly flagged as pending.

## Handoff summary

**One sentence:** *Make an order line's price come from the menu, and make every departure from the menu a named, deliberate act — one helper, one call site, one nullable reason column, no rows to backfill because no order line has ever been written.*

**Three picks of the 99th daily-brainstorm pass (2026-11-06):**

| | Pick | Feature | Gate | Evidence |
|---|---|---|---|---|
| A | an expired batch can still be sold from | `features/447-le31-an-expired-batch-can-still-be-sold-from.md` | **build** | OBSERVED (executed) |
| B | a bill has no human-facing identity | `features/448-le31-a-bill-has-no-human-facing-identity.md` | **build** | OBSERVED (executed) |
| C | an order line may carry any price it likes | `features/449-le31-an-order-line-may-carry-any-price-it-likes.md` | **build** | OBSERVED (executed) |

**Feature**: `features/449-le31-an-order-line-may-carry-any-price-it-likes.md`
**Report**: `/opt/data/le31-brainstorm-2026-11-06.md`
**Bucket**: v1 · **Gate**: build · **Evidence**: OBSERVED (executed) · **Confidence**: high (gap) / medium (demand)
