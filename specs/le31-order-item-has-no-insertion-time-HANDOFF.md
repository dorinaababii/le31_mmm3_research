# HANDOFF — 430-le31-order-item-has-no-insertion-time

> **Slice contract for the coding agent.** Produced by the 97th LE31 daily-brainstorm pass (2026-11-03), Pick B.
>
> **Feature file**: `features/430-le31-order-item-has-no-insertion-time-first-party-five-identical-order-lines-are-indistinguishable-except-by-a-surrogate-key-v1-order-item-insertion-time.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: five real inserts through SQLModel returned five distinct ids and **one** distinct payload, with every per-line timestamp `None`). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod, same SQLModel code), §7 (the quality bar: *"Time is UTC"*, *"No magic numbers"*, *"No dead code"*, *"End-to-end before commit"*), the truth invariant.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. **Read `features/429-…` FIRST** and resolve the `created_at` / `added_at` collision described under *Frozen contract* below. **Do not ship both a `created_at` and an `added_at` on `order_item`.**
5. **Add the insertion-time column** to `class OrderItem`, following the file's existing `Column(DateTime(timezone=True))` pattern exactly (`batch.prepared_at`, `visit.opened_at`, `stock_entry.at`).
6. **Create `backend/app/services/__init__.py` and `backend/app/services/order_service.py`** with the `lines_for_visit` helper — ordering by the insertion time with `id` **only** as the tie-break.
7. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_order_item_insertion_time_is_independent_of_id_order`: insert three lines with **deliberately reversed** insertion times and assert the helper returns them in **insertion-time order, not id order**.
8. **Not create** an orders router, and **not** write any `OrderItem` row from production code.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Add a second creation-time column to `order_item`.** The 429/430 collision — see *Frozen contract*. **Exactly one** insertion-time column on `order_item`.
- **Create an `order_items` router, or write any production write path for `OrderItem`.** There is no orders router today — `backend/app/routers/` holds only `__init__.py` and `tables.py`. **This contract adds a column and a helper; it does not create the feature that would fill the column.**
- **Change `ItemStatus`, its five members, or the fact that `status` defaults to `new`.**
- **Touch `fired_at`, `ready_at` or `served_at`.** They are the kitchen's milestones and are **feature 379's** territory.
- **Add an actor field to the transition.** That is **feature 379** — *"Order-item transition actor attribution"*.
- **Add a `unit` column to `OrderItem`, or change `MenuItem.unit`.** That is **features 386 / 392 / 407**.
- **Add a batch reference to `OrderItem`.** That is **feature 385**.
- **Add or change `Bill`, `Bill.total_due`, or any bill derivation.** That is **features 05 / 415**.
- **Introduce Alembic**, or add a foreign key. That is **feature 427** for FKs; charter §3.2 for Alembic.
- **Design a course/sequencing model.** `OrderItem.course` is free text and **the charter never mentions "course"** — sequencing is out of scope by the charter's silence.
- **Order by `id` alone.** That is the defect this contract fixes. `id` is a surrogate key and may be renumbered by a sequence reset, a restore from backup, or a data migration.

**Disambiguation**: this slice is about **when an order line was added to a visit**. It is **not** about the line's *state* (379), its *unit* (392), its *batch provenance* (385), the *bill* (415), the *service day* (405), or the *schema-wide creation-timestamp convention* (429).

## Frozen contract

**The one thing this contract exists to make true:** *the order in which a visit's lines were added must be recorded as a fact, not inferred from a surrogate key.*

Concretely, after this slice lands:

1. `order_item` carries **exactly one** non-nullable UTC insertion-time column.
2. A helper returns a visit's lines **ordered by that column**, with `id` **only** as a tie-break between lines added in the same instant.
3. **The ordering rule exists in exactly one place**, so the future orders router cannot get it wrong.

**The prohibition:** *two competing insertion-time columns on `order_item`, and an ordering that depends on `id` alone.*

### The 429/430 collision — resolve before writing code

| If | Then |
|---|---|
| **429 lands first** and adds `created_at` to every table | **430 must NOT add `added_at`.** `created_at` **is** the insertion time; 430's remaining work is the helper and the tests. |
| **430 lands first** | 430 adds `added_at`. 429 must then **not** add `created_at` to `order_item`, and must amend its docstring to name the exception — or adopt `added_at` as `order_item`'s creation time. |

**Whichever lands first, the second must be adjusted.** The agent's **first action** is to read `features/429-…` and determine which case applies — and **the commit message must state the resolution.**

**The load-bearing test**, which must be written **before** the change and watched to fail:

```python
def test_order_item_insertion_time_is_independent_of_id_order(session):
    """Three lines added out of id order must be returned in insertion order."""
    t0 = datetime(2026, 11, 3, 12, 0, 0, tzinfo=timezone.utc)
    t1 = t0 + timedelta(seconds=1)
    t2 = t0 + timedelta(seconds=2)
    # insert deliberately REVERSED: the newest gets the smallest id
    newest = make_line(at=t2)   # id 1
    middle = make_line(at=t1)   # id 2
    oldest = make_line(at=t0)   # id 3
    assert [o.id for o in lines_for_visit(session, visit_id)] == [oldest.id, middle.id, newest.id]
```

**This test fails on the unfixed code** (which has no insertion time at all) and it fails on a *wrong* fix that orders by `id` alone. **It is the test that distinguishes a real fix from a plausible one.**

**A second test is equally load-bearing**, because it guards the collision:

```python
def test_order_item_has_no_second_insertion_timestamp():
    cols = [c["name"] for c in inspect(engine).get_columns("order_item")]
    assert not ("created_at" in cols and "added_at" in cols), (
        "order_item must carry exactly ONE insertion-time column")
```

## Files to touch

| File | Change |
|---|---|
| `backend/app/models.py` | `class OrderItem` — add the insertion-time column. **Exactly one.** |
| `backend/app/services/__init__.py` *(new)* | Empty package marker. **Note: features 374 and 429 also expect `services/` to exist — three contracts creating the same package in one week is friction, not a conflict.** |
| `backend/app/services/order_service.py` *(new)* | `lines_for_visit(session, visit_id) -> list[OrderItem]`, ordered by the insertion time with `id` as the tie-break. |
| `backend/app/db.py` | The `init_db()` path — **no Alembic**. |
| `backend/tests/test_order_item_insertion_time.py` *(new)* | The three tests: `test_order_item_records_an_insertion_time`, `test_order_item_insertion_time_is_independent_of_id_order`, `test_order_item_has_no_second_insertion_timestamp`. |

**Do not create** `backend/app/routers/orders.py` — there is no orders router and this contract does not add one.

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
| `features/429-…-v1-schema-creation-timestamp-convention.md` | **The nearest sibling in the whole corpus; it touches the same table.** It decides whether `order_item`'s creation time is `created_at` or `added_at`. |
| `features/379-…-v1-order-item-transition-attribution.md` | Owns the **state transition** and the missing actor field. `fired_at` and `status` are its territory — this slice adds only the insertion time and does not move the transition. |
| `features/392-…-v1-menu-item-unit-meaning.md` | The sibling finding on the **quantity** axis — *complementary, not duplicate*. Read it so the two do not collide. |
| `features/385-…-v1-batch-selection-and-sale-provenance.md` | Owns the **batch** reference from an order line. It quotes `order_item`'s exact column list; read it so the column list stays consistent. |
| `features/415-…-v1-bill-closes-visit-edge.md` | Owns the bill ↔ visit edge and the missing `bills.py`. This slice does **not** touch the bill path. |
| `features/405-…-v1-service-day-boundary-and-business-date.md` | Owns the *business* date. Read it so this slice does not open it. |
| `PROJECT_CHARTER.md` §3.2, §4.1, §7, §8 | The source of truth. |
| `backend/app/models.py` lines 129-156 | The `Visit` and `OrderItem` classes this slice touches. |

## Mandatory inputs

- **The defect itself** — `class OrderItem`'s column list, verbatim from `backend/app/models.py`:

  ```
  id, visit_id, menu_item_id, qty, unit_price, course, status, notes,
  fired_at, ready_at, served_at
  ```

  **There is no insertion-time column.** The three timestamps are all `None` until the line is fired.

- **The measured fact** — executed against LE31's real schema on 2026-11-03:

  ```
  orderitem_has_insertion_time   False
  orderitem_timestamps            [fired_at, ready_at, served_at]

  five identical lines inserted:
    id=1..5, qty=1, unit_price=8.80, notes=null, course=null,
    status=ItemStatus.new, fired_at=None

  distinct_row_ids      5
  distinct_payloads     1        <-- every line has the SAME content
  per_line_timestamps   fired_at=None for all five
  ```

- **The re-runnable probe** — `/opt/data/_bs_probe_body_2026-11-03.py` builds LE31's schema and prints the same numbers. The agent may re-run it (it needs a venv with `sqlmodel`; one exists at `/opt/data/le31-verify-2026-10-27/.venv` — **reuse it, do not provision a new one**).

## Verification protocol reference

`PROJECT_CHARTER.md` §8 is the protocol; this slice's specific sequence is:

1. **Write the test first.** `test_order_item_insertion_time_is_independent_of_id_order` — watch it **FAIL**. **A test that only ever passed proves nothing**; the failure is the evidence the test can fail.
2. Apply the change (the column + the helper).
3. **Watch the test PASS.**
4. **Re-run the whole test suite** — this slice must not break another slice's test.
5. **Exercise the actual path**: start the app (`cd backend && uvicorn app.main:app --reload`), confirm `http://localhost:8000/docs` loads, and confirm the schema in the running app has the column (`sqlite3 backend/restaurant.db ".schema"`).
6. **Re-run the probe** and confirm `orderitem_has_insertion_time` is now `true`.
7. `git add -p && git commit -m "Feature 430: order_item insertion time — <created_at | added_at> (429 resolved: <how>)"` — **the commit message must name the column and the 429 resolution.**

**Manual verification is acceptable for v1** (charter §7) — **but** the regression tests in this contract **are** required: they are what distinguishes a real fix from a plausible one.

## Rollback path

- **Drop the column.** The column is additive and default-populated; removing it restores the previous schema exactly. On an existing dev database, drop and re-create (`init_db()`); on prod, the reverse migration is a `DROP COLUMN`.
- **Delete the helper.** `backend/app/services/order_service.py` is new and unreferenced until a router calls it, so removing it breaks nothing.
- **Either way**: the change is confined to `backend/app/models.py` (+ a new `services/` package + a test file). **No router, no bot handler, no UI, no external call.** No existing row changes meaning, because nothing reads the column yet.

**Note on the dev database**: charter §3.2 uses `init_db()`, so a dev database is disposable — drop and re-create. **Record the prod-migration step as known debt** in the commit message.

## Sign-off gap

- **⚠️ The column name is undecided.** Default recorded: **`added_at`**, because it carries the *meaning* (a guest's add-moment) rather than the mechanism (a row's creation moment) — and the two will eventually be written by different code paths. **Alternative: `created_at`**, acceptable if feature 429 lands first and this slice adjusts.
- **⚠️ The tie-break is undecided.** Default recorded: **`added_at, id`** — deterministic and stable. The helper already does this.
- **⚠️ The removal of an order line is undecided — and deliberately not decided here.** If a line can be removed, its *removal* time is a separate question and a separate contract. **Recorded, not answered.**
- **⚠️ The 429/430 collision is unresolved until one of them lands.** The agent must read 429 before writing code, and the commit message must state the resolution.
- **⚠️ Existing rows get the migration instant, not their true insertion time.** No historical insertion times exist. **This must be stated in the commit message.**
- **⚠️ The helper has no production caller.** This is honest and expected: there is no orders router. The helper is the **single definition** of the ordering rule, written down before the router that will use it exists. **The agent should say so in the commit message** so a reviewer does not read an unreferenced helper as dead code (charter §7: *"No dead code"*) — it is a specification, and the specification is the deliverable.

## Handoff summary

| | |
|---|---|
| **Feature** | 430 — `order_item` cannot record when a line was added |
| **Verdict** | `build` (OBSERVED — five identical payloads, no per-line timestamp) |
| **Bucket** | v1 — schema hygiene on the table the P0 order rows depend on |
| **Files to touch** | `backend/app/models.py`, `backend/app/services/{__init__,order_service}.py` (new), `backend/app/db.py`, `backend/tests/test_order_item_insertion_time.py` (new) |
| **New dependency** | none |
| **Reversible** | yes — an additive column plus a new unreferenced helper |
| **Hard prerequisite** | none — but **read feature 429 first** to resolve the `order_item` column collision |
| **Must not touch** | `fired_at`/`ready_at`/`served_at`, `ItemStatus`, `Bill`, the bill path, `MenuItem.unit`, the batch reference, any FK |
| **Known debt created** | the prod migration for the added column (the standing `init_db()`-not-Alembic debt) |
