# HANDOFF — le31-sqlite-silently-drops-the-utc-offset

> **Slice contract for the coding agent.** Produced by the 100th LE31 daily-brainstorm pass (2026-11-07), Pick C.
>
> **Feature file**: `features/453-le31-sqlite-silently-drops-the-utc-offset-time-is-utc-is-not-enforced-and-dev-and-prod-disagree.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then `Batch(prepared_at=utcnow())` written and **read back as `tzinfo=None`** — a naive datetime; a Paris-local value stored as `'2026-11-07 23:30:00.000000'` against a true instant of `2026-11-07T22:30:00+00:00`, i.e. **−3600 s**; a read-back value compared with `now()` **raising `TypeError`**; and feature **405's own specified guard** (`raise` on naive input) **raising on every value read from SQLite**). All seven checks pass; check 1's **demand** is classed INFERRED — the corpus confirms *"the LE31 owner has never complained about a wrong day"* (feature 405) — which is why this contract is deliberately **one storage type, one helper, eight column declarations, five tests** and adds **no** surface, **no** column and **no** table. See the feature file's *Description* / *Why this matters* and the gate table in `/opt/data/le31-brainstorm-2026-11-07.md`.
>
> **Report**: `/opt/data/le31-brainstorm-2026-11-07.md`

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/453-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §3.5 (**"Time is UTC"** — the rule this slice makes true), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Read `features/405-le31-service-day-boundary` FIRST and confirm the ordering described under *Frozen contract* below.** **405's central helper is un-callable on SQLite until this slice lands — this slice MUST land first, or in the same PR.**
6. **Read `features/411-le31-money-precision-declared-not-enforced` before starting.** It is the **precedent**: the identical *"declared, not enforced, and dev/prod disagree"* shape, already proved for money. **Reuse its vocabulary and its discipline.**
7. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_timestamp_read_back_is_timezone_aware` — on today's code it **fails**.
8. **Add the storage type and the helper** exactly as specified in the feature file's *Data model* — one `TypeDecorator` (or the equivalent alias + helper), applied to **all eight** `datetime` columns.
9. **Grep the file; do not eyeball the column list.** A missed column is a silent hole.
10. **Record the two decisions** — *naive value: refuse or assume UTC?* and *`TypeDecorator` or alias + helper?* — in the code, per *Open questions* 1 and 2.
11. **Correct the `coding-agent/checklist.md` line** — *"Every timestamp is `TIMESTAMPTZ`."* — which feature 410 already flagged as wrong for SQLite. **Coordinate with feature 405** so the two do not contradict.

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Decide what a service day is.** Feature **405** owns the business-date column and its semantics. **Do not add a business-date column, do not name a day, and do not change what "today" means.** This slice makes the *input* to 405's decision trustworthy — it does not make the decision.
- **Change `Batch.expires_at`'s nullability, or change the active-batch predicate.** Feature **404** owns both. **Do not "fix" the NULL case.**
- **Change `Batch.qty_remaining`.** Feature **374** owns it (derive, don't store).
- **Touch any money column, `Payment`, `Shift.variance`, or the cash-reconciliation derivation.** Features **391** and **426** own those. **Feature 411 owns the money-precision guard.**
- **Add a `CHECK` constraint or make the tables `STRICT`.** Feature **404** owns that family. **This slice adds the storage type for time only.**
- **Introduce Alembic, write a migration, add an `alembic` dependency, an `alembic.ini`, or a `migrations/` directory**, or change `PROJECT_CHARTER.md`.
- **Add a new pip dependency.**
- **Add a router, an endpoint, or a Telegram command.** The slice ships the type and the helper. **Surfaces are a later feature.**
- **Add a column or a table.** This slice adds **no** column and **no** table. *(Changing a column's *type* is not adding one — but see the 446 note below.)*
- **Assume UTC for a naive value without recording the decision.** The recorded default is **refuse**. Silently assuming UTC is the exact failure this slice removes.

**Disambiguation**: this slice is about **making a stored timestamp be an instant on every read, on every database**. It is **not** about the service day (405), the expiry predicate (404), the remaining quantity (374), money precision (411), the money-rule reconciliation (410), the `CHECK`/`STRICT` family (404), the schema-evolution mechanism (446), or the ledger's append-only discipline (421).

## Frozen contract

**The one thing this contract exists to make true:** *every `datetime` column in LE31 stores and returns a timezone-aware UTC instant, and a naive value cannot be written.*

Concretely, after this slice lands:

1. **Every value read from the database is tz-aware.** `read.tzinfo is not None` for every `datetime` column, on SQLite **and** Postgres.
2. **Every value written is converted to UTC first.** A Paris-local `23:30+01:00` is stored as `22:30Z` — **not** as `23:30`.
3. **A naive value is REFUSED at the write boundary**, with an error naming the column. **Recorded default: refuse** (feature file *Open questions* 1). **If the implementer chooses "assume UTC", that choice must be recorded in the code** — but **the recommended and recorded default is to refuse.**
4. **A read-back value is comparable with `now()` without raising.** `value > utcnow()` must not raise `TypeError`.
5. **Feature 405's specified guard accepts a value read from the database.** `business_date()` must not raise on a value that came from a `SELECT`. **This is the test that proves the collision is closed** — it is the whole reason this slice exists.
6. **Feature 404's expiry predicate, written in Python, evaluates without raising.** (`expires_at is None or expires_at > utcnow()`.)
7. **All eight columns are covered** — `batch.prepared_at`, `batch.expires_at`, `stock_entry.at`, `visit.opened_at`, `visit.closed_at`, `bill.paid_at`, `shift.opened_at`, `shift.closed_at`. **Grep, do not eyeball.**
8. **There is exactly ONE conversion implementation.** Not two. If the implementer chooses the alias + helper shape over the `TypeDecorator`, **the read boundary must be centralised** — a second inline conversion is a defect.
9. **No column is added and no table is added.** The change is to the *type* of the existing columns and to the values they accept.
10. **No existing behaviour changes.** The stored wall-clock for a `utcnow()`-written value is **unchanged** — it was already correct. **Only the type on read, and the refusal of a non-UTC write, change.**
11. **The Postgres side is not touched.** `DateTime(timezone=True)` already renders `timestamptz` there. **Do not add a Postgres-specific type** — §3.2 forbids it.
12. **`utcnow()`'s contract is unchanged.** It is correct today; it stays correct.

### The 405 ordering — resolve before writing code

**405 must land first, or in the same PR as this slice.**

Feature 405 specifies a `business_date()` helper that **raises on a naive input**:

```python
if instant.tzinfo is None:
    raise ValueError("business_date() requires a timezone-aware instant; ...")
```

On SQLite **every value read back is naive**. So on the charter's dev database, **405's central helper raises on every query it is given.**

This is the **upstream-of-filed-work** condition in its sharpest form: **a filed feature would implement a guard that fails closed on every real call.** A coding agent implementing 405 today, faithfully, would either ship a helper that always raises, or "fix" it by deleting the guard. **Both outcomes are worse than the defect 405 was filed to fix.**

**Do not implement 405's business-date column here. Do not decide what a service day is.** This slice makes 405's helper *callable*; 405 decides what it *answers*.

### The 411 precedent — reuse it, do not reinvent it

Feature 411 already proved, for money, the identical shape:

> *"money is `Decimal`, never `float`"* is **declared and not enforced**, and **SQLite and Postgres disagree** about it.

**This slice is the same finding for time**: *"Time is UTC"* is **declared and not enforced**, and **SQLite and Postgres disagree** about it — with a `TypeError` instead of a wrong number.

**Read 411 before writing code.** It establishes the corpus's vocabulary for *"declared, not enforced"* and for the dev/prod split. **Reuse that vocabulary in the code comments and in the PR description.**

### The 410 checklist line — coordinate, do not contradict

Feature 410's Open Question 4 asks: *"Is `TIMESTAMPTZ` a checklist error or a Postgres-only note?"*

**The answer this slice supplies: it is a Postgres-only note — and the SQLite behaviour is worse than a note, because it is a *type* change.** Qualify the `coding-agent/checklist.md` line to name the real behaviour, and **coordinate with 405** so the checklist, 405's contract and this one do not say three different things.

### The 446 note — why there is no dependency here

Most slices that touch `models.py` depend on feature **446** (`le31-has-no-schema-evolution-mechanism`), because `create_all()` cannot add a column to an existing table. **This slice adds no column and no table**, so **it does not depend on 446** — the column *types* are declared in the model and are created with the table.

**Recorded explicitly so it is not mistaken for an oversight.** If the implementer's chosen shape does end up requiring a schema change (for example, if a `TypeDecorator` forces a type change on an existing table), **446 becomes a dependency and the PR must say so.**

## Files to touch

**Create:**

- `backend/app/types.py` (or `backend/app/db_types.py`) — the storage type and the one normalisation helper. **One file, one conversion.**
- `backend/tests/test_timestamps_are_instants.py` — the regression tests.

**Modify:**

- `backend/app/models.py` — apply the new type to **all eight** `datetime` columns. **Grep for `DateTime(` and confirm the count is zero afterwards.**
- `coding-agent/checklist.md` — qualify the *"Every timestamp is `TIMESTAMPTZ`."* line.

**Read but do not modify:**

- `features/405-le31-service-day-boundary-…md` — the dependent; its helper must become callable.
- `features/411-le31-money-precision-declared-not-enforced-…md` — the precedent.
- `features/404-le31-active-batch-rule-…md` — the adjacent predicate; its SQL form must keep working unchanged.
- `features/410-le31-two-money-rule-sources-…md` — the checklist-line owner.
- `PROJECT_CHARTER.md` — §3.5 (*"Time is UTC"*), §3.2 (out of scope), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar).

## Mandatory LE31 skill list

- **`le31-conventions`** — §3.2, §3.5, §4.1, §7, the truth invariant, the seven-check gate.
- **`le31-v1-feature-pattern`** — the contract shape and the *Definition of Done*.
- **`le31-feature-pipeline`** — where the artefacts land.
- **`le31-handoff-spec`** — the slice-contract shape.
- **`le31-backend`** — the FastAPI/SQLModel layering and the session boundary.

**Also read** `PROJECT_CHARTER.md` — §3.5 (*"Time is UTC. `datetime.now(timezone.utc)` everywhere."*), §3.2 (out of scope for v1), §4.1 (SQLite dev / Postgres prod), and §7 (the quality bar).

## Mandatory inputs

- The eight column names, listed in *Frozen contract* item 7. **Do not rely on a hand-written list — grep.**
- Feature 405's exact guard text, so the compatibility test is written against **the real helper**, not a paraphrase.
- The `coding-agent/checklist.md` line to qualify.

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases

| # | Case | Expected |
|---|---|---|
| 1 | write `Batch(prepared_at=utcnow())`, read it back | `tzinfo is not None` |
| 2 | write a **Paris-local** aware value (`23:30+01:00`), read it back | the value is `22:30Z` — **not** `23:30` |
| 3 | write a **naive** value | **refused**, error names the column |
| 4 | read a value back, compare with `utcnow()` | **no `TypeError`** |
| 5 | pass a **read-back** value to feature 405's `business_date()` | **does not raise** |
| 6 | evaluate feature 404's expiry predicate **in Python** on a read-back value | **no `TypeError`** |
| 7 | `grep -c 'DateTime(' backend/app/models.py` | **0** (every column uses the new type) |
| 8 | the same test on **Postgres** (if a test DB is available) | the value is **tz-aware** — **and record what was actually run** |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Start the app against a throwaway SQLite DB (`init_db()`).
2. Write a `Batch` through the ORM and **read it back**.
3. **Show the read-back value's `tzinfo`** and show it is `timezone.utc`.
4. Show the comparison with `now()` succeeding.
5. Show feature 405's guard accepting it.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (on the unfixed code the read-back value is naive, so the test fails), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

The verification venv from prior passes can be reused: **`/opt/data/le31-verify-2026-10-27/.venv`** (SQLModel + FastAPI + SQLite). **Do not provision a new venv if this one works.** If a Postgres test DB is **not** available, **say so plainly and record what was actually verified on SQLite** — do not claim the Postgres row was tested.

## Rollback path

**Fully reversible in one step.** The slice adds **no column, no table, and no constraint** — it changes the *type* of eight existing columns and adds one helper.

- **Revert the commit** and the columns return to `DateTime(timezone=True)`.
- **No data is at risk**: no `Batch`, `Bill`, `StockEntry` or `Shift` row has ever been written by any shipped code path (the only `Visit` write in the whole backend is `backend/app/routers/tables.py` line 51). **Recorded, and it is the reason this slice is cheap.**
- **The ledger is append-only by charter**, and this slice never writes to it.
- **The one thing a rollback loses**: any value written *under the new type* by a future code path would still be readable — the stored wall-clock is unchanged — so **a rollback does not corrupt data**.

## Sign-off gap

**What the agent MUST NOT decide:**

- **What a service day is** (405). **When a service day starts** (405). **Whether business dates are stored or derived** (405).
- **Whether the naive-value policy is refuse or assume-UTC** — the **recorded default is refuse**; if the implementer overrides it, they must record it and say why.
- **Whether a `TypeDecorator` or an alias + helper** is the shape — the implementer records the choice; **both are acceptable** as long as the guarantee holds and there is **exactly one** conversion implementation.
- **Anything about the business-day column, the checklist's business rules, or the Postgres migration story** (446).

**What the agent must report back:**

- The **read-back `tzinfo`** before and after, as observed.
- The **Paris-local write** result — the stored value and the true instant.
- Whether **feature 405's guard** accepts a read-back value.
- The **`grep` count** of remaining `DateTime(` occurrences.
- **What was actually run on Postgres**, or an explicit statement that Postgres was **not** available and only SQLite was verified.

## Handoff summary

**One sentence:** *Make every stored timestamp an instant on every read — one storage type, one helper, eight columns, five tests — so that "Time is UTC" is enforced by the database instead of trusted, and so that feature 405's own guard becomes callable on the charter's own dev database.*

**Three picks of the 100th daily-brainstorm pass (2026-11-07):**

- **Pick A (this one):** `le31-two-tables-can-carry-the-same-label` — **feature 455**.
- **Pick B:** `le31-a-visit-may-be-closed-with-order-lines-and-no-bill` — **feature 454**.
- **Pick C:** `le31-sqlite-silently-drops-the-utc-offset` — **feature 453** *(this contract)*.

**Feature**: `features/453-le31-sqlite-silently-drops-the-utc-offset-time-is-utc-is-not-enforced-and-dev-and-prod-disagree.md`
**Report**: `/opt/data/le31-brainstorm-2026-11-07.md`
