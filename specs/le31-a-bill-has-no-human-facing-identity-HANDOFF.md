# HANDOFF — le31-a-bill-has-no-human-facing-identity

> **Slice contract for the coding agent.** Produced by the 99th LE31 daily-brainstorm pass (2026-11-06), Pick B.
>
> **Feature file**: `features/448-le31-a-bill-has-no-human-facing-identity.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite DB, then three bills on one table with identical totals — **bills on table 1 = 3 ; DISTINCT total_due among them = 1** — and a `PRAGMA table_info(bill)` returning `False` for `number`, `no`, `receipt`, `code`, `reference` and `label`: the only identity a bill has is `Bill.id`, an auto-increment integer that is never shown to a human, is not stable across a restore, and carries no service day). All seven checks pass; check 1's **demand** is classed INFERRED, which is why this contract is deliberately **one column, one allocator, one uniqueness constraint** and adds no printing surface. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-brainstorm-2026-11-06.md`.
>
> **Report**: `/opt/data/le31-brainstorm-2026-11-06.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/448-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/446-le31-has-no-schema-evolution-mechanism` FIRST** and confirm the ordering described under *Frozen contract* below. **This slice adds a COLUMN to an existing table — which is exactly the operation `create_all()` cannot perform. 446 is a HARD dependency.**
6. **Read `features/405-le31-service-day-boundary` and confirm the ordering described under *Frozen contract*.** **405 owns which business day a bill belongs to, and the allocator must call 405's service-day helper — not `date.today()`.**
7. **Add `bill_number: str` to `class Bill`** — **non-null**, **indexed**, with a `UniqueConstraint("bill_number")`.
8. **Create `backend/app/services/billing.py`** with `next_bill_number(session, service_day)` exactly as specified in the feature file's *Data model*, including the **collision retry**.
9. **Provide the write path** — if feature 415's bill-close route exists, call the allocator from it; if it does not, provide a thin `create_bill(...)` helper the future route will call. **Do not write the route; that is 415's.**
10. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_two_bills_in_one_day_get_different_numbers`.
11. **Record the allocator vocabulary** — one line in `features/415-…` saying that the bill number is feature 448's.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Re-derive the service-day boundary.** Feature **405** owns it. **Do not call `date.today()`** and do not decide whether a bill belongs to the calendar day or the service day — **call 405's helper.**
- **Write the bill-close route.** Feature **415** owns `backend/app/routers/bills.py` and the bill→visit edge.
- **Change `Bill.visit_id`'s `unique=True`.** Feature **14** (`split-bills`) owns the split concept; a split is **not** representable as two bills on one visit today, and **this slice does not change that.**
- **Change `Bill.id`, remove it, or rename it.** It stays the primary key and the FK target for `DerivedTip.bill_id`. **The id does not go away — it simply stops being the only identity.**
- **Add a currency column, or decide the currency.** Feature **409** records it as an open owner question; the charter fixes EUR.
- **Add a receipt printer, a receipt template, a PDF invoice, a "private bill link", or any printing surface.** Features **362** and **353** are the adjacent vocabulary references. **This slice ships the identifier, not the paper.**
- **Implement split bills, a void policy, a reprint policy, or a fiscal/legal invoice number.** Features **14**, **37**, and **131** respectively.
- **Change the money columns, the tax, or the tip formula.** Features **408**, **410**, **411**, **420**.
- **Change which lines a bill charged.** Feature **435**.
- **Add a `Payment` table or a `Shift`↔`Bill` edge.** Feature **391**.
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**
- **Add a per-day counter TABLE.** The `MAX()+1` + constraint + retry is the chosen form; the counter-row alternative is **recorded as an open question, not decided here.**

**Disambiguation**: this slice is about **a bill's human-facing identity**. It is **not** about the bill's membership of lines (435), the bill-close route (415), the tip formula (420), the tax rate (408), the money precision (411), the shift money edge (391), split bills (14), the currency (409), fiscal numbering (131), the service day (405), or the schema-evolution mechanism (446).

## Frozen contract

**The one thing this contract exists to make true:** *every bill carries a number a human can read out loud and a person can point at.*

Concretely, after this slice lands:

1. `Bill` has **exactly one** new column: `bill_number: str`, **non-null**, **indexed**.
2. `Bill` has **exactly one** new constraint: `UniqueConstraint("bill_number")` — **globally** unique, not per-day, because the service day is already inside the number.
3. The number's shape is **`<service-day>-<4-digit sequence>`**, e.g. `2026-11-06-0007`.
4. The sequence is **zero-padded to 4 digits**, so it sorts correctly **as a string**.
5. The sequence **restarts at `0001` for each service day**.
6. The number contains **no character that needs shell, URL or filename escaping** — in particular **no slash** (note: the trigger source uses `2026-27/0001`; the slash is a UI convenience and an escaping hazard, and this contract deliberately differs).
7. The service day comes from **feature 405's helper**, never from `date.today()`.
8. Two bills closed concurrently get **two different numbers** — the second insert **retries**, and the retry is **not** swallowed.
9. `Bill.id` is **unchanged** — still the primary key, still the FK target for `DerivedTip.bill_id`.
10. `bill_number` is **returned wherever a bill is returned**, and is **included in the bill-close response**.
11. **No rows are backfilled** — no bill has ever been written, so there is nothing to reconcile. **The PR must say so explicitly.**
12. **No existing number is renumbered, reordered or reformatted.**
13. The number is a **`str`**, not an integer — the artefact that gets printed is a string with a date and a zero-padded sequence in it.

**The prohibition:** *catching the `IntegrityError` and continuing anyway.* A duplicate bill number is worse than a failed bill close, because a failed close is **visible** and a duplicate number is **not**. The retry must be bounded and must **fail loudly** past the bound.

### The 446 ordering — resolve before writing code

This slice **adds a column to an existing table**, and `create_all()` **adds missing tables but never alters, renames or retypes an existing column**. A changed column is silently ignored and the old column keeps serving — so a feature that adds a column lands, merges, deploys, passes its tests, and **the column does not exist in the running database**.

**446 must land first, or in the same PR.** Read `features/446-le31-has-no-schema-evolution-mechanism` and follow its backup-before-`create_all()` behaviour. **Do not hand-write an `ALTER TABLE`** — that is 446's job, and hand-writing one is exactly the thing 446 exists to prevent.

### The 405 ordering — resolve before writing code

The number embeds the service day, and the service day is **feature 405's** business (charter §3.5 says UTC while the linear project says Paris time). **405 must land first, or in the same PR.**

**A documented UTC-calendar-date fallback is allowed only as an interim**, and it must be replaced when 405 lands. **Do not quietly ship `date.today()` and call it done** — that is the failure mode 405 exists to prevent, and it would be invisible until a late-night close landed on the wrong day.

### The per-day-vs-continuous counter — an owner decision, recorded not guessed

The contract chooses **per-day** numbering (the day is inside the number, so it is self-describing). **A continuous counter is the alternative.** The owner's answer determines whether the shape changes, and it should be asked **before the first bill is written, not after** — after, the numbers exist and the shape is a migration.

**The agent may implement the per-day form.** The agent may **not** implement a continuous counter, a per-day counter *table*, or a renumbering migration.

## Files to touch

**Create:**

- `backend/app/services/billing.py` — `next_bill_number(session, service_day)` and, if feature 415's route does not exist, a thin `create_bill(...)`.
- `backend/tests/test_bill_number.py` — the scenario table from the feature file, as eight tests.

**Modify:**

- `backend/app/models.py` — **class `Bill` only.** Add `bill_number: str = Field(index=True)` and `__table_args__` with `UniqueConstraint("bill_number")`.
- `features/415-le31-bill-closes-visit-…md` — **one line only**, recording that the bill number is feature 448's. **Do not change 415's route.**

**Read but do not modify:**

- `features/446-le31-has-no-schema-evolution-mechanism.md` — the hard dependency.
- `features/405-le31-service-day-boundary-…md` — the hard dependency for the allocator.
- `features/415-le31-bill-closes-visit-…md` — the route this slice's allocator feeds.
- `features/435-le31-bill-records-no-which-lines-it-charged-…md` — the bill's membership.
- `features/391-le31-shift-variance-stored-no-derivation-…md` — the `Payment` table and the shift edge.
- `features/14-split-bills.md` — the split concept; `Bill.visit_id` stays `unique=True`.
- `features/409-le31-open-questions-register-…md` — the currency question.
- `features/131-puntovivo-…md` — the deferred fiscal-numbering artifact. **Recorded, not adopted.**
- `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §3.5 (time is UTC), §3.6 (money is `Decimal`, never `float`), §7 (the quality bar).

## Mandatory LE31 skill list

The agent **must** load, in order:

1. `le31-conventions` — §3.2, §4.1, §3.5, §3.6, §7, the truth invariant, the seven-check feature gate.
2. `le31-v1-feature-pattern` — the contract shape and the *Definition of Done*.
3. `le31-feature-pipeline` — where the artefacts must land.
4. `le31-handoff-spec` — this file's obligations.
5. `le31-backend` — the service-layer conventions.
6. `le31-data` — the data-model conventions (the `Decimal` rules).

**Also read** `PROJECT_CHARTER.md` — §3.2 (out of scope for v1), §3.5 (time is UTC), §3.6 (money is `Decimal`, never `float`), and §7 (the quality bar).

## Mandatory inputs

- The active feature file: `features/448-le31-a-bill-has-no-human-facing-identity.md`
- This handoff: `specs/le31-a-bill-has-no-human-facing-identity-HANDOFF.md`
- Feature 405's service-day helper (or its recorded decision)
- Feature 446's backup-before-`create_all()` behaviour
- The charter's §3.6 money rules

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases (from the feature file's scenario table)

| # | Situation | Expected |
|---|---|---|
| 1 | First bill of service day `2026-11-06` | `2026-11-06-0001` |
| 2 | Second bill of the same day | `2026-11-06-0002` |
| 3 | First bill of service day `2026-11-07` | `2026-11-07-0001` — the sequence restarts, the day does not |
| 4 | Ten bills in one day | `…-0010` — zero-padded, sorts as a string |
| 5 | Two bills closed concurrently | two different numbers — one insert retries |
| 6 | The same number allocated twice | the second insert raises `IntegrityError` — never two rows |
| 7 | A bill closed just before midnight | allocated against the service day, not the wall clock (405) |
| 8 | The number as rendered | contains the service day and a zero-padded sequence, and no shell/URL/filename-escaping character |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Allocate and store a first bill number. **Observe** `…-0001`.
2. Allocate a second. **Observe** `…-0002` and **that it sorts after `0001` as a string** (compare `sorted(["…-0010", "…-0009"])`).
3. Allocate on the next service day. **Observe** the sequence restarting and the day changing.
4. **Force the collision** — allocate the same number twice — and **observe** the `IntegrityError` and the retry producing a different number.
5. **Observe** that `Bill.id` is unchanged and still the `DerivedTip` FK target.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code there is no `bill_number` column at all), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

Use the **existing verification venv** rather than provisioning a new one: `/opt/data/le31-verify-2026-10-27/.venv` (`sqlmodel` 0.0.48, `sqlalchemy` 2.1.6). `python3` on the host has **no `pip` module** (PEP 668); do not try to install into the system interpreter.

## Rollback path

**Mostly reversible; the one irreversible part is stated plainly.**

- **Reversible:** remove the `bill_number` column and the `UniqueConstraint` from `models.py`; delete `backend/app/services/billing.py`; remove the allocator call site.
- **The one-way door:** if any bill has been written with a number, **the numbers stay**. This is the point — a number that is quoted by a guest is a fact, and facts do not get renumbered. **Because no bill has ever been written, the rollback is currently clean. After the first bill is closed, it is not.**
- **The schema change needs 446's mechanism.** `create_all()` cannot drop a column either. **If the column must be removed after bills exist, that is a migration decision, and 446's mechanism is the only sanctioned path.**

**No data is at risk today:** there is no bill-close route and therefore **no `Bill` row exists** to be affected.

## Sign-off gap

**What the agent MUST NOT decide:**

- whether the number restarts each service day or runs continuously (per-day is implemented; the alternative is **not**);
- whether a per-day counter table is worth it (the `MAX()+1` + constraint + retry form is implemented; the counter row is **not**);
- what the number looks like on the guest's receipt (the shape is implemented; the printing is **not**);
- whether a voided or reopened bill keeps or consumes a number;
- whether the number should appear on the kitchen ticket as well as the receipt;
- whether the number leaks volume (it does; that is **recorded**, not designed around);
- the currency of the money columns (feature 409's open question).

**What the agent must report back:**

- the eight scenario results, **one row each, with the observed outcome**;
- the **failing-then-passing** proof for `test_two_bills_in_one_day_get_different_numbers`;
- the **forced-collision** observation — the `IntegrityError`, and the number the retry produced;
- the **string-sort** observation for the zero-padding;
- confirmation that **no rows were backfilled** and **no number was renumbered**;
- a `git diff` on `models.py` showing **exactly** the one column and the one constraint;
- confirmation that features **446** and **405** were read and that the ordering is satisfied or explicitly flagged as pending.

## Handoff summary

**One sentence:** *Give every bill a name a human can say out loud — one column, one allocator, one uniqueness constraint, and no rows to backfill because no bill has ever been written.*

**Three picks of the 99th daily-brainstorm pass (2026-11-06):**

| | Pick | Feature | Gate | Evidence |
|---|---|---|---|---|
| A | an expired batch can still be sold from | `features/447-le31-an-expired-batch-can-still-be-sold-from.md` | **build** | OBSERVED (executed) |
| B | a bill has no human-facing identity | `features/448-le31-a-bill-has-no-human-facing-identity.md` | **build** | OBSERVED (executed) |
| C | an order line may carry any price it likes | `features/449-le31-an-order-line-may-carry-any-price-it-likes.md` | **build** | OBSERVED (executed) |

**Feature**: `features/448-le31-a-bill-has-no-human-facing-identity.md`
**Report**: `/opt/data/le31-brainstorm-2026-11-06.md`
**Bucket**: v1 · **Gate**: build · **Evidence**: OBSERVED (executed) · **Confidence**: high (gap) / medium (demand)
