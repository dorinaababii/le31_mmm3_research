# HANDOFF — le31-has-no-schema-evolution-mechanism

> **Slice contract for the coding agent.** Produced by the 84th LE31 daily-research pass (2026-11-06), Pick C.
>
> **Feature file**: `features/446-le31-has-no-schema-evolution-mechanism.md`
>
> **LE31 feature gate verdict**: **build — NARROW FORM ONLY.** Evidence class **OBSERVED** (executed + read from the repository's own tree): `backend/app/db.py`'s `init_db()` docstring says, verbatim, *"Create all tables. For real schema evolution use Alembic (see /db/migrations/)."*; `backend/app/main.py` says *"Create DB tables on startup. Replace with Alembic for prod."*; **`backend/db/migrations/` does not exist** — `backend/` contains exactly `['.env.example', 'README.md', 'app', 'requirements.txt']`, there is no `alembic.ini`, and there is no version table anywhere. And `create_all()` is **not** a substitute — proved by execution: it **adds missing tables** but **never alters, renames, drops or retypes an existing column**, so a changed column is **silently ignored** and the old column keeps serving.
>
> **⚠️ THE HARD CONSTRAINT ON THIS SLICE:** `PROJECT_CHARTER.md` line 86 lists, under **out of scope for v1**, verbatim: *"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)."* **The broad form — introducing Alembic — is therefore BLOCKED and is `defer`. This contract proposes only the narrow form: a timestamped backup before `create_all()`, plus recording the owner decision. The agent MUST NOT add `alembic`, an `alembic.ini`, a `migrations/` directory, a version table, or an `alembic` dependency.**
>
> **Report**: `/opt/data/le31-daily-research-2026-11-06.md`

## Trigger policy

This is a **`build`** contract, **narrow form only**. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file (`features/446-…`) and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, **`init_db()`-not-Alembic**, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. Load **`le31-feature-pipeline`** and **`le31-handoff-spec`** — this is a `v1` bucket slice and the artefacts must land where the pipeline expects them.
5. **Create `backend/app/backup.py`** with `take_pre_schema_backup(engine, *, now) -> Path` — **raises on failure**; the caller must abort startup. **A tolerated backup failure is worse than no backup at all**, because it creates the appearance of safety.
6. **Create `backend/app/schema_diff.py`** (or an equivalent) with `schema_differs(engine) -> bool` — a **name-level** comparison of tables and columns between `SQLModel.metadata` and the live database. **A full DDL diff is out of scope** and must not be attempted.
7. **Wire it into `init_db()`** in `backend/app/db.py` — take a backup when the schema differs, log its path, then run `create_all()` as before. **Fail closed: if the backup fails, startup aborts and `create_all()` does not run.**
8. **Update the two docstrings** that point at the non-existent `/db/migrations/` — `db.py` and `main.py` — so they state what is true: what the backup does, and that **`create_all()` cannot alter an existing column**.
9. **Write the decision note** at `docs/decisions/schema-evolution.md` (or the repo's equivalent location) — recording the charter's verbatim position, what `create_all()` can and cannot do, what the narrow form does, and **the question for the owner**. **The note states the question. It does not answer it.**
10. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_schema_change_with_failing_backup_aborts_startup` — it is what proves the fail-closed rule is not decorative.

**What the agent MUST NOT do** — each of these is a defect, not initiative:

- **⚠️ Add `alembic` to `backend/requirements.txt`, create an `alembic.ini`, create a `migrations/` directory, add a version table, or write a migration.** **The charter defers Alembic. The broad form is `defer`, and the agent may NOT implement it.**
- **Hand-write an `ALTER TABLE`**, or any ad-hoc DDL, to work around the missing mechanism. **That is precisely the silent-no-op class this feature exists to prevent.**
- **Create a general migration framework of any kind** — no `schema_version` table, no hand-rolled migration runner, no DDL-diff tool.
- **Change any model.** This feature changes **how the schema is applied**, not **what the schema is**. If the agent believes a model change is needed, it must record that as a deviation.
- **Change the behaviour of `create_all()`** — it still creates missing tables. What is new is the backup **before** it and the abort **on failure**.
- **Tolerate a failed backup.** Startup **must** abort. **A startup that logs a warning and continues is the defect, not a fix.**
- **Change `PROJECT_CHARTER.md`.** The charter is the owner's document. The recommendation goes *to* the owner; the agent must not edit the charter.
- **Add a Docker, Kubernetes, or deployment story.** A charter §3.2 non-goal.
- **Add a new pip dependency.** The backup uses the standard library plus whatever system tools are already present (see *Open questions* 1).
- **Back up anything other than the database.** This is a **pre-schema-change** backup, not a data-retention programme.
- **Automate the restore.** The restore is a **documented runbook step**, not code. See *Out of scope* in the feature file.

**Disambiguation**: this slice is about **how the schema is applied, safely**. It is **not** about any specific column or table (that is 444, 445, 408, 415, 420, 435, 438, 439, 442, 443), **not** about the backup of business data, and **not** about the deployment story.

## Frozen contract

**The one thing this contract exists to make true:** *a schema change can never be silently ignored — and the one decision the charter has been deferring is recorded rather than left open.*

Concretely, after this slice lands:

1. **The live schema matches the models** → **no backup is taken**; `create_all()` runs; startup succeeds. **The existing behaviour is unchanged.**
2. **The live schema differs from the models** → a **timestamped backup is taken**; its path is **logged**; `create_all()` then runs.
3. **The backup fails, or produces an empty file** → **startup ABORTS** and `create_all()` **does not run**. **Fail closed.**
4. Two schema-changing startups on the same day produce **two distinct backups** — the timestamp must have enough resolution, or a counter must disambiguate.
5. The backup **contains the old schema** — verified by opening it and reading its table list.
6. **Both docstrings** that pointed at `/db/migrations/` now state what is true.
7. **The decision note exists**, quotes the charter verbatim, and **asks the owner the Alembic question without answering it**.
8. **`create_all()`'s own behaviour is unchanged** — it still creates missing tables.

**The prohibition:** *a startup that proceeds with a changed schema after a failed backup* — and *any form of Alembic introduction.*

### The narrow-form boundary — the line the agent must not cross

| | In scope (this slice) | **Out of scope (`defer`)** |
|---|---|---|
| **What** | A timestamped backup taken **before** `create_all()`, and a fail-closed abort | Alembic, `alembic.ini`, a `migrations/` directory, a version table, a migration runner |
| **Why in/out** | It does **not** conflict with the charter: a backup is not a migration mechanism | The charter's §3.2 lists it as out of scope for v1. **An owner decision, explicitly not made here** |
| **Charter impact** | **None** | Would require a charter change |

**The agent's job is to make the question askable, not to answer it.** If the owner later decides Alembic, this slice is **not** invalidated — the backup still protects the first Alembic migration.

### The ordering this slice creates

**This slice is upstream of every feature that changes an existing table.** Today that is at least:

| Feature | What it changes |
|---|---|
| **445** (this pass, Pick B) | `Batch.by_user_id` — **a new column on an existing table** |
| **408** | the tax rate and the rounding mode in `config.py` |
| **415** | the bills router and the bill-close edge |
| **420** | `Bill.amount_tendered`, `Bill.amount_received` |
| **421** | the `StockEntry` write-path rule |
| **435** | the bill→line membership edge |
| **438** | `MenuItem.is_active` |
| **439** | the line-level allergen field |
| **442** | the generated `CHECK` constraints |
| **443** | the bill-close role rule |
| **429** | ten `created_at` / `updated_at` columns — **the largest schema change in the corpus** |

**Pick A (444) is the one exception**: it adds a **new table**, and `create_all()` can create a table — so 444 is **not** strictly blocked. **That asymmetry is worth stating precisely**, because it is the reason 444 can land while 445 cannot.

## Files to touch

**Create:**

| Path | What |
|---|---|
| `backend/app/backup.py` | `take_pre_schema_backup(engine, *, now) -> Path`. **Raises on failure.** For **SQLite**: use the database's own backup facility (`sqlite3`'s `.backup()`), **not a raw file copy** — a raw copy of a WAL-mode database can be torn. For **Postgres**: `pg_dump` — **see *Open questions* 1; if it is unavailable on the production host, STOP and report it rather than substituting a weaker mechanism.** |
| `backend/app/schema_diff.py` | `schema_differs(engine) -> bool` — **name-level only**. A full DDL diff is out of scope. |
| `docs/decisions/schema-evolution.md` | The owner-decision note. **If `docs/` does not exist, follow the repository's existing convention for notes** — check before creating a new top-level directory. |
| `backend/tests/test_schema_evolution.py` | The regression tests (the repo's test layout — **check `backend/` for the existing test directory and follow it**; do not invent a second layout). |

**Modify:**

| Path | What |
|---|---|
| `backend/app/db.py` | `init_db()` — the backup-before-`create_all()` guard and the fail-closed abort. **And the docstring**, which currently points at a directory that does not exist. |
| `backend/app/main.py` | **The docstring only** — *"Create DB tables on startup. Replace with Alembic for prod."* must state what is true. **Do not change the startup behaviour itself in this file** — the guard belongs in `init_db()`. |

**Read but do not modify:**

| Path | Why |
|---|---|
| `PROJECT_CHARTER.md` (line 86) | The verbatim position this slice must respect and record. **Do not edit it.** |
| `backend/app/models.py` | The schema this slice must **not** change. |
| `backend/requirements.txt` | To confirm the dependency set is unchanged. |

## Mandatory LE31 skill list

The external agent **must** load, in this order, before writing code:

1. **`le31-conventions`** — the seven-check gate, the hard invariants, §3.2 (**`init_db()`-not-Alembic**, fixed stack, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), and the truth invariant.
2. **`le31-v1-feature-pattern`** — the canonical contract shape, the slicing rules, and the *Definition of Done*.
3. **`le31-feature-pipeline`** — where the artefacts land and the commit/push convention.
4. **`le31-handoff-spec`** — the frozen-contract discipline: *do not silently change the slice, scope, or verification path*.
5. **`development`** — the generic code pipeline (specify → plan → tasks → implement → independent review) for the implementation itself.

**Also read** `PROJECT_CHARTER.md` — §3.2 in full (the out-of-scope list this slice lives inside), §3.3 (the open scope questions — **this slice's decision note belongs in that conversation**), and §7 (the quality bar).

## Mandatory inputs

| Input | Path | Why |
|---|---|---|
| The feature contract | `features/446-le31-has-no-schema-evolution-mechanism.md` | The scope, the decision rule, the scenario table, the open questions. |
| The research report | `/opt/data/le31-daily-research-2026-11-06.md` | The gate verdicts, the evidence, the duplicate sweep. |
| The execution probe | `/tmp/le31-daily-2026-11-06/_parent_final.py` (section `C`) | **The parent-run probe that produced the evidence** — it imports LE31's own `backend/app/models.py`, runs against a throwaway SQLite DB, and shows `create_all()` is a no-op on an existing table. **Re-runnable.** The venv is at `/tmp/le31-daily-2026-11-06/.probe-venv` (`sqlmodel` 0.0.48 + `sqlalchemy` 2.0.57) — **if `/tmp` has been cleared, recreate it with `uv venv` + `uv pip install "sqlmodel>=0.0.42" "sqlalchemy<2.1"`.** |
| The raw fetches | `/tmp/le31-daily-2026-11-06/` | The third-party READMEs the evidence quotes come from (`readme/FreeOpenSourcePOS__FloCafe.md` is the trigger). |
| The duplicate-sweep result | the feature file's *Adjacent work* + the report's *Duplicates skipped* | What is **already filed** and must not be re-picked. |

## Verification protocol reference

**The agent must mirror back these fields before implementing, and stop if it cannot.**

### Verification cases (from the feature file's scenario table)

| # | Case | Expected |
|---|---|---|
| 1 | The live schema **matches** the models | **no backup**; `create_all()` runs; startup succeeds |
| 2 | The live schema **differs** (a column is missing) | a **timestamped backup** is taken; its path is logged; `create_all()` then runs |
| 3 | The live schema differs **and the backup fails** | **startup ABORTS** — `create_all()` does **not** run. **Fail closed.** |
| 4 | The backup file is written but is **empty** | treated as a **failure** — startup aborts |
| 5 | Two schema-changing startups on the same day | **two distinct backups** |
| 6 | The backup completes | the **old schema is intact** in the backup file — verified by opening it and reading the table list |
| 7 | A rollback is performed from a backup | **documented** — the path from the log is used to restore. The restore is a **runbook step**, not automated code |
| 8 | `init_db()` on a fresh empty database | no backup needed; tables created; **the existing behaviour is unchanged** |

### The acceptance path the agent must OBSERVE

**Do not stop at "the tests pass".** Per `le31-v1-feature-pattern`, done means the flow was exercised. The minimum observable path:

1. Create a **fresh** database and run `init_db()` → **no backup**, tables created.
2. **Add a column** to the live database (or to the model) so the schema **differs**, run `init_db()` again → **a backup file appears**, its **path is in the log**, and `create_all()` then runs.
3. **Open the backup file** and show the **old** table list is in it.
4. **Break the backup** (point the path at an unwritable location, or stub the helper to raise) → show **startup aborts** and that **`create_all()` did not run**. **This is the case that proves the feature is not decorative.**
5. Show the **two docstrings** now say what is true and **no longer** reference `/db/migrations/`.
6. Show the **decision note** exists, quotes the charter verbatim, and **asks** the Alembic question.

### The regression-gap demonstration

**The agent must write the test first, run it against the unfixed code, and show it FAILING** (there is no backup and no abort today — a failing backup is simply impossible because there is no backup), **then apply the fix and show it PASSING.** A test that only ever passed proves nothing.

### The environment note

LE31's test suite runs on **SQLite**, while production is **Postgres** (charter §4.1). **This slice touches both engines**, and they back up differently:

- **SQLite (dev):** use the database's own backup facility (`sqlite3`'s `.backup()`) — a **raw file copy of a WAL-mode database can be torn**.
- **Postgres (prod):** `pg_dump`.

**The agent must test both paths if both are reachable.** If `pg_dump` is **not** available in the environment, the agent must **say so in the commit message** rather than shipping an untested Postgres path — **and must not silently substitute a weaker mechanism.** This is *Open questions* 1 and it is the one practical risk in this slice.

## Rollback path

| Aspect | Detail |
|---|---|
| **Revert** | `git revert` the commit. The two new modules are removed and `init_db()` returns to its original body. |
| **Data at risk** | **None.** The backup is a **copy**; the original database is untouched by taking it. |
| **Disable path** | Remove the guard block from `init_db()`. Startup reverts to plain `create_all()`. **⚠️ Note that disabling this restores the silent-no-op behaviour — the runbook must say so.** |
| **Migration / rollback cost** | **Zero** — the slice adds **no table and no column**. It is the only slice in this pass that needs no schema change of its own. |
| **What remains safe if removed** | Everything. `create_all()`'s behaviour was never changed. |
| **The one irreversible thing** | Nothing. **The backup file is written *before* the change, so the old state is always preserved.** The restore path is: read the path from the log, restore the file. |
| **Operational risk to name in the runbook** | **A startup that aborts is the feature working.** Someone under pressure may "fix" it by disabling the backup. **The runbook must say: do not disable the backup; fix the backup's target or the disk, then restart.** |

## Sign-off gap

**What the agent MUST NOT decide:**

1. **⚠️ Whether LE31 adopts Alembic before production.** **This is the charter's question, not the agent's.** The deliverable is that the question is **recorded and asked**, not answered. The charter currently says, verbatim: *"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)."* **The agent may implement the narrow form; the agent may NOT implement the broad form.**
2. **How many backups to keep.** The recommendation is **the most recent N (N = 5)** with older ones pruned, never deleting the one the running schema was deployed with. **An owner decision.**
3. **Where the backups live.** The recommendation is **the same disk as the database** for v1 — which protects against a *schema* mistake, **not** against a disk failure. **An owner decision, and the limitation must be written down.**
4. **Whether `init_db()` should still run on every startup.** The recommendation is **yes** — it is idempotent for a matching schema. **Recorded.**
5. **Whether a name-level schema comparison is enough.** It is **not** sufficient to detect a same-name column *type* change. The recommendation is **yes for v1**, **with the limitation written into the decision note** rather than left implied.

**What the agent must report back:**

- The commit SHA and the push confirmation.
- The **failing-then-passing** output of the key regression test.
- The observed acceptance path (steps 1–6 above), with the actual files and log lines shown.
- **A statement of whether `pg_dump` is available on the production host**, and whether the Postgres path was tested. **This is the single most important line in the report.**
- The exact wording of the **two updated docstrings**, and the path to the **decision note**.
- Any deviation from this contract, stated explicitly rather than absorbed.

## Handoff summary

**One sentence:** *Make a schema change impossible to apply silently — take a timestamped backup before `create_all()`, fail closed if it cannot, and put the charter's deferred Alembic question to the owner without answering it.*

**Three picks of the 84th daily-research pass (2026-11-06):**

| Pick | Slug | Gate | One line |
|---|---|---|---|
| **A** | `le31-order-item-unit-price-is-mutable-in-place-with-no-trace` | **build** | A line's price can be overwritten; the original is unrecoverable and the bill total silently changes. |
| **B** | `le31-batch-has-no-preparer` | **build** | `StockEntry.by_user_id` and `Shift.by_user_id` exist; `Batch` has no actor column, so the preparer of a batch is unknowable. **Blocked on this slice** — a new column cannot reach a live database without it. |
| **C** | `le31-has-no-schema-evolution-mechanism` | **build (narrow form)** | `db.py` points at a directory that does not exist, and `create_all()` never alters an existing column. **This contract.** |

**Feature**: `features/446-le31-has-no-schema-evolution-mechanism.md`
**Report**: `/opt/data/le31-daily-research-2026-11-06.md`
**Bucket**: v1 · **Gate**: build (narrow form) · **Evidence**: OBSERVED (executed) · **Confidence**: high
