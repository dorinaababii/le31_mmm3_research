# Feature 446 — `le31-has-no-schema-evolution-mechanism`

> **Pick C of Daily Research 2026-11-06 (84th pass).** **FIRST-PARTY — the defect is in LE31's own source code, and it is proved by EXECUTION against LE31's own schema** plus a reading of the repository's own directory listing.
>
> `backend/app/db.py`, `init_db()`, **verbatim**:
>
> ```python
> def init_db() -> None:
>     """Create all tables. For real schema evolution use Alembic (see /db/migrations/)."""
>     # Import models so SQLModel.metadata is populated before create_all.
>     from . import models  # noqa: F401
>     SQLModel.metadata.create_all(engine)
> ```
>
> `backend/app/main.py`, **verbatim**:
>
> ```python
> """Create DB tables on startup. Replace with Alembic for prod."""
> ```
>
> **The directory `/db/migrations/` does not exist.** The repository's own listing, executed:
>
> ```
>   backend/ contains exactly: ['.env.example', 'README.md', 'app', 'requirements.txt']
>   alembic.ini exists                 -> false
>   backend/db/migrations exists        -> false
> ```
>
> **And `create_all()` is not a substitute — proved by execution.** `SQLModel.metadata.create_all(engine)` **adds missing tables** but **never alters, renames, drops or retypes an existing column.** A changed column is **silently ignored**, and the old column keeps serving.
>
> **Evidence class: OBSERVED** (the docstrings, the missing directory and the no-op behaviour are all reproducible). **Confidence: high.**
>
> **Bucket: v1, NARROW FORM ONLY.** **Build verdict: `build` for the narrow form (a backup before `create_all()`, plus recording the owner decision).** **The broad form — introducing Alembic — is `defer`, because `PROJECT_CHARTER.md` line 86 puts it out of scope for v1.** That conflict is surfaced, not guessed through.

## Goal

Make it **impossible for a schema change to be silently ignored** — and make the one decision the charter is waiting on explicit rather than implied.

Concretely, two things:

1. **A backup before `create_all()` runs.** The old schema is preserved before the new one is applied, so the change can be verified and, if it went wrong, reverted.
2. **A recorded owner decision on the migration mechanism**, so the charter's deferral becomes an answer instead of a standing ambiguity.

**This contract does not introduce a migration framework.** That is the owner's decision, and the charter has already deferred it.

## Scope

- **A timestamped backup** taken immediately **before** `create_all()` runs, on every startup that would create or alter tables.
- **A clear failure** if the backup cannot be taken — **fail closed**, never proceed silently.
- **A record of the backup's location** so a rollback is a documented operation, not an archaeology exercise.
- **A short note** recording the owner decision on the migration mechanism, at the point where the decision lives (see *The owner decision* below).
- A **regression test** for each scenario in the table below.

## Out of scope (v1)

- **Introducing Alembic.** The charter explicitly defers it. **This contract must not add `alembic`, an `alembic.ini`, a `migrations/` directory, a version table, or a `alembic` dependency.** The decision is recorded, not made.
- **A general migration framework of any kind.** No `schema_version` table, no hand-rolled migration runner, no DDL-diff tool.
- **Converting the existing schema to any migration tool.** There is no production data to convert.
- **Any change to the models.** This feature changes **how the schema is applied**, not **what the schema is**.
- **Any change to `PROJECT_CHARTER.md` itself.** The charter is the owner's document; the recommendation goes *to* the owner.
- **Docker, Kubernetes, or deployment tooling.** A charter §3.2 non-goal.
- **Backups of the application data outside the database.** This is a **pre-schema-change** backup, not a data-retention programme.
- **Any new pip dependency.** The backup is a file copy using the standard library.

## Description

### The defect is the code pointing at a directory that does not exist

This is not a missing feature in the abstract. **LE31's own source code names the missing thing, in two places, and points at a path that is not there.** That is a defect with a very specific shape: the repository contains an instruction that cannot be followed, and the fallback it names (`create_all()`) does not do what the surrounding code implies it does.

The two docstrings are not comments about a future plan. They are **instructions to the next person who changes the schema**, and they are **wrong as written** — there is no `/db/migrations/` to use.

### Why `create_all()` is not a substitute — proved by execution

This is the part that matters, because `create_all()` *looks* like a schema mechanism. It is not.

`SQLModel.metadata.create_all(engine)` **issues `CREATE TABLE` for tables that do not exist** and **does nothing at all for tables that do**. It has no notion of:

- adding a column to an existing table,
- changing a column's type, nullability or default,
- renaming a table or a column,
- dropping anything,
- recording which version is deployed.

**The consequence is the quiet one, and it is the whole reason this feature exists:** a feature that adds a column **lands in the code, merges, deploys, and its tests pass** — and **the column does not exist in the running database.** Nothing errors. Nothing warns. The application then reads and writes against a schema that is not the one the code was written against, and the behaviour is whatever the *old* column's definition happens to be.

### The scale of the exposure

This is not a hypothetical. **The corpus contains at least ten filed features whose entire deliverable is a column or a table.** From the current `features/` directory:

| Feature | What it adds |
|---|---|
| **408** | the tax rate and the rounding mode in `config.py` |
| **415** | `Bill.amount_tendered`, `Bill.amount_received` (via 420) and the bills router |
| **420** | `Bill.amount_tendered`, `Bill.amount_received` |
| **421** | the `StockEntry` write-path rule (a linter/checklist mechanism) |
| **435** | the bill→line membership edge |
| **438** | `MenuItem.is_active` |
| **439** | the line-level allergen field |
| **442** | the generated `CHECK` constraints |
| **443** | the bill-close role rule |
| **444** (this pass, Pick A) | the `OrderItemPriceChange` table |
| **445** (this pass, Pick B) | `Batch.by_user_id` |
| **446** (this pass, Pick C) | this contract |

**Every one of them assumes a mechanism that does not exist.** Not one of them is wrong about its own defect; they are all *blocked on this one*, and they are blocked **silently**, which is the worst way to be blocked.

### The plausible wrong answer — and it is a good one

> *"`create_all()` is fine for v1 — the schema will not change before production."*

**This is a reasonable position, and it is the one the charter takes.** It is also **falsifiable**, and today it is **false in the only sense that matters**: the schema **has** changed — repeatedly — and the features that change it are **already written**. The deferral is not "before the schema changes"; it is "before the schema changes **and someone notices**". The noticing is the thing that is missing.

The honest counter-argument, which is why this contract proposes the **narrow** form: **a full Alembic introduction is not what the charter is waiting for.** It is a per-change discipline, an operational burden, and a thing to learn — and the charter's §3.2 lists it as a v1 non-goal. **A backup before `create_all()` is not that.** It is a file copy.

### The peer instrument

`FreeOpenSourcePOS/FloCafe` (MIT ✓ §3.2, TypeScript off-stack, ★168/⑂80, pushed 2026-11-05), README verbatim:

> *"- **Pre-migration backups:** FloCafe automatically creates a **timestamped database backup before running schema migrations**."*

> *"- **Automated database backups:** Pre-migration automatic snapshots, manual exports, and optional Google Drive sync."*

FloCafe is a **desktop, single-machine** app whose database is a SQLite file in the user's data directory — so a file copy is both possible and sufficient there. **LE31 is a server with Postgres in production**, so **the portable primitive is not "copy the file" but "take a timestamped backup before the schema changes, and fail closed if it cannot be taken."** The mechanism differs; the rule does not.

## Data model

**No new table. No new column. No new model.**

This is a **mechanism** feature, not a schema feature.

The backup artefact itself is **not a table** — it is a file, on the server, outside the database. Its location must be **recorded somewhere durable**, and the two candidates are:

- **Option (a) — a log line.** The backup path is written to the application log on every startup that takes one. Simple, no schema change, and the log is already where operational events go. **The recommendation.**
- **Option (b) — a `schema_change` table.** Durable and queryable, but it is a **new table** — which is precisely the thing this feature exists to make safe, and it would need its own backup. **Rejected as circular.**

**The decision rule, stated as a rule:**

```
Before create_all() is executed:
  1. Determine whether the schema on disk differs from the schema in the models.
  2. If it does NOT differ  -> nothing to back up; create_all() is a no-op; proceed.
  3. If it DOES differ       -> take a timestamped backup; verify it is non-empty;
                               write the backup path to the log; then create_all().
  4. If the backup FAILS     -> log the failure and ABORT startup. Do not create_all().
```

**Step 4 is the load-bearing one.** A backup that fails but is tolerated is **worse than no backup**, because it creates the *appearance* of safety. **Fail closed.**

**Step 1 is how the feature knows whether it is doing anything.** The simplest honest implementation: compare the set of table names and column names in `SQLModel.metadata` against the live database, and treat a difference as "the schema differs". A full DDL diff is out of scope; **a name-and-column comparison is enough to decide "this is a schema-changing startup, back up first."**

## Implementation steps

Dependency-ordered; each task is independently verifiable.

1. **A backup helper.** A new module, e.g. `backend/app/backup.py`:
   ```python
   def take_pre_schema_backup(engine: Engine, *, now: datetime) -> Path:
       """Take a timestamped backup of the database and return its path.

       Raises on failure. The caller must abort startup; a tolerated backup
       failure is worse than no backup at all.
       """
   ```
   For **SQLite** (dev): copy the database file, WAL and SHM safely — **the copy must be taken through the database's own backup facility (sqlite3's `.backup()` API), not a raw file copy**, because a raw copy of a WAL-mode database can be torn.
   For **Postgres** (prod): `pg_dump` — **the question of whether `pg_dump` is available on the production host is an open question, recorded below.**
2. **A schema-difference check.** `schema_differs(engine) -> bool`, comparing table and column names in `SQLModel.metadata` against the live database. **Name-level only.** A full DDL diff is out of scope.
3. **Wire it into `init_db()`.** `backend/app/db.py` becomes:
   ```python
   def init_db() -> None:
       """Create all tables.

       A timestamped backup is taken first whenever the live schema differs from
       the models, and startup aborts if that backup fails. See feature 446.
       """
       from . import models  # noqa: F401
       from .backup import take_pre_schema_backup
       from .schema_diff import schema_differs

       if schema_differs(engine):
           path = take_pre_schema_backup(engine, now=utcnow())
           logger.info("pre-schema-change backup written to %s", path)

       SQLModel.metadata.create_all(engine)
   ```
   **The existing behaviour of `create_all()` is unchanged** — it still runs, it still creates missing tables. **What is new is the backup before it and the abort on failure.**
4. **Update the two docstrings.** `db.py`'s `"""Create all tables. For real schema evolution use Alembic (see /db/migrations/)."""` **must change**, because it points at a directory that does not exist. The replacement must say what is true: the backup behaviour, and the fact that **`create_all()` cannot alter an existing column**.
5. **The owner-decision note.** A short file — `docs/decisions/schema-evolution.md` (or the equivalent) — recording: the charter's current position (line 86, verbatim), what `create_all()` can and cannot do, what the narrow form does, and **the question for the owner**: *does LE31 adopt Alembic before production, or does it keep `create_all()` plus backups as the v1 mechanism?* **The note states the question. It does not answer it.**
6. **Tests.** One test per row of the table below.

### The scenario table (each row is a test)

| Scenario | Expected |
|---|---|
| The live schema **matches** the models | **no backup is taken**; `create_all()` runs; startup succeeds |
| The live schema **differs** from the models (a column is missing) | a **timestamped backup is taken**; its path is logged; `create_all()` then runs |
| The live schema differs **and the backup fails** | **startup ABORTS** — `create_all()` does **not** run. **Fail closed.** |
| The backup file is written but is **empty** | treated as a **failure** — startup aborts |
| Two schema-changing startups on the same day | **two distinct backups** — the timestamp includes enough resolution to avoid a collision, or a counter disambiguates |
| The backup completes | the **old schema is still intact** in the backup file — verified by opening it and reading the table list |
| A rollback is performed from a backup | **documented** — the backup path from the log is used to restore. The restore procedure itself is a **runbook**, not automated code (see *Out of scope*) |
| `init_db()` is called on a fresh empty database | no backup needed; tables are created; **the existing behaviour is unchanged** |

## Telegram interaction if any

**None.** This is a server-side startup mechanism. **There is no Telegram surface, and none should be added** — a backup is an operational event, and the charter's surfaces are the waiter web UI and the cook Telegram bot.

**The only user-visible effect** is that a schema-changing deploy may **take slightly longer** (the backup) and, if the backup fails, **refuses to start** rather than starting with a stale schema. **That refusal is the feature working correctly**, and it must be in the runbook so nobody "fixes" it by disabling the backup.

## Dependencies

- **No upstream dependency.** This feature **unblocks** others; nothing blocks it.
- **It is a dependency of every feature that changes an existing table**, including this pass's Pick A (444, a new table — `create_all()` handles a new table, so 444 is *not* strictly blocked) and Pick B (445, a new **column** — **strictly blocked**), plus features 408, 415, 420, 435, 438, 439, 442 and 443.
- **The `PROJECT_CHARTER.md` decision** — the broad form is blocked by the charter's §3.2 line 86. **The narrow form is not blocked**, because a backup is not a migration mechanism.
- **The production host's tooling** — whether `pg_dump` is installed on the production VPS is an open question (see below). **This is the one practical risk in this feature.**

## Open questions

1. **Is `pg_dump` available on the production host, and is it the right tool?** The narrow form assumes a mechanism to take a Postgres backup. `pg_dump` is the standard answer and is **not** in `backend/requirements.txt` (it is a system package, not a Python one). **If `pg_dump` is unavailable, the options are a managed snapshot, a `COPY`-based export, or a VPS-level snapshot — and the owner should choose.** **This is the one question that could change the implementation, and it is recorded rather than assumed.**
2. **Should the backup be kept, and for how long?** The recommendation is to keep the **most recent N** (N = 5) and prune older ones, and **never** to delete the one the running schema was deployed with. **An owner decision, recorded not made.**
3. **Should the backup live on the same disk as the database?** The recommendation is **yes for v1** (it is a safety net against a *schema* mistake, not against a disk failure) — but the owner should know that it does **not** protect against a disk failure. **Recorded.**
4. **Does the owner adopt Alembic before production?** **This is the charter question, and the deliverable of this contract is that the question gets asked and recorded, not that it gets answered here.** The charter currently says: *"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)."*
5. **Should `init_db()` still be called on every startup?** The recommendation is yes — it is idempotent for a matching schema — **but** with the backup guard it is now *meaningfully* different on a mismatching schema. **Recorded.**
6. **Is a name-level schema comparison enough?** A column **type** change with the same name would not be detected by a name-only diff. The recommendation is **yes for v1** — a type change is a charter-decision-scale event and the backup still happens when the *set* differs. **But a same-name type change on an otherwise identical schema would be missed**, and that limitation should be written down rather than left implied. **Recorded.**

## Why this matters

**Because the failure mode is the worst kind there is: a change that lands, merges, deploys, passes its tests, and does nothing.**

Every other first-party defect in this corpus has a shape: a wrong value is accepted, a rule is not enforced, a record is missing. **This one is different — the defect is that the *mechanism to apply the fix* does not exist.** A feature that adds a column is not a feature until the column is in the database, and in LE31 today **the column would not be.**

And **the evidence that this is not hypothetical is the corpus itself.** Eleven filed features — including this pass's Pick A and Pick B — add a column or a table. **Not one of them is wrong about its own defect. All of them are blocked on this one**, and they would be blocked **silently**, because `create_all()` does not raise when it cannot do the job.

**This is also the cheapest fix in the corpus**, and the only one with a **zero-regression** profile: the backup is a file copy, `create_all()`'s behaviour is unchanged, and the failure mode it introduces (refusing to start) is the correct behaviour. Two to four hours.

**And it is the decision with the widest blast radius.** The charter's line 86 has deferred Alembic since before the first feature was written. Every week it stays open, another column lands in a contract and not in a database. **Putting the question to the owner is the deliverable; answering it is not this contract's job.**

## Adjacent evidence

- **`FreeOpenSourcePOS/FloCafe`** (MIT ✓ §3.2, TypeScript off-stack) — *"FloCafe automatically creates a timestamped database backup before running schema migrations."* The portable primitive.
- **`yixin-lot/posd`** (Apache-2.0, in-window by both fields) — *"自动备份到 \`backups/\`（默认保留 7 份）"* — *automatic backup to `backups/` (7 kept by default)*. **The retention-count shape** is a useful precedent for *Open question 2*.
- **`Raktim94/nodedr-restaurant-pos`** (AGPL-3.0 — licence-blocked) — *"Pre-migration automatic snapshots, manual exports"* is also stated there; the same rule in a second peer. **Not picked (licence).**

## Adjacent work — recorded, NOT picked

- **Feature 429 (`created_at` convention)** — *every* table lacks the timestamps the module docstring promises. Adding ten columns is the **largest** schema change in the corpus, and it is **the reason the narrow form must exist before it**. **Recorded, not picked** — 429 is a first-party defect with its own contract; this feature is the mechanism that makes it applicable.
- **A `schema_version` table** — the conventional answer to "what version is deployed?". It is a new table, and it is out of scope here. **Recorded, not picked.**
- **The `alembic 1.20.1` release** — PyPI, uploaded **2026-10-22**, **outside this window**. It is the tool the charter names, and its availability is not a reason to pick it. **A pin-bump decision, not a research-pass decision** — deliberately **not** picked.
- **The production deployment story** — systemd unit, single VPS, no Docker. A charter §3.2 non-goal, and not this contract's business.
