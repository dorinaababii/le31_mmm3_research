# HANDOFF — 427-le31-sqlite-never-enables-pragma-foreign-keys

**Status**: **build** (v1, first-party — **the defect is in LE31's own code and is proven by execution**)
**Date**: 2026-11-02
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/427-le31-sqlite-never-enables-pragma-foreign-keys-first-party-every-declared-fk-is-unenforced-in-dev-while-postgres-enforces-it-in-prod-v1-sqlite-fk-enforcement.md`
**LE31 feature gate verdict**: **build** — gate check 1 (**demand**) is **OBSERVED**: the charter's P1 row *"SQLite for dev, Postgres for prod. Same SQLModel code for both"* is **false today** on the referential-integrity axis, and every manual test in §2 runs on the database that accepts rows Postgres would reject. Gate check 2 (**evidence**) is **OBSERVED by EXECUTION**: `PRAGMA foreign_keys` returned **0** on a stock SQLite connection; `backend/app/db.py` contains **no** `foreign_keys` pragma; the *same* dangling insert that SQLite accepted with the pragma off was **rejected with `IntegrityError`** with the pragma on. Gate check 3 (**practicability**) is **PASS**: one event listener, no schema change, no new dependency (`sqlalchemy.event` ships with SQLAlchemy). Gate check 4 (**scope**) is **PASS**: no router, no bot command, no behaviour change beyond making declared constraints bite. Gate check 5 (**consistency**) is **PASS**: this feature is the **prerequisite** for features **417** and **426**, and its own contract names them.

## Trigger policy

This is a **`build`** contract. The external coding agent **SHOULD** enable SQLite's foreign-key enforcement on every application connection, write the regression tests, and document the dialect difference.

**⏱️ ORDERING — THIS IS THE FIRST SLICE.** This feature is the **prerequisite** for two other filed features:

- **Feature 417** (`le31-stockentry-actor-foreign-key`) adds a foreign key to `StockEntry.by_user_id`.
- **Feature 426** (`le31-stockentry-ref-order-item-id-foreign-key`) adds a foreign key to `StockEntry.ref_order_item_id`.

**Without this feature, both of those are decorations** — declared constraints that SQLite will not enforce. Their contracts name this feature as a "must land first, or in the same PR" dependency. **Land this first.**

**What the agent MAY do:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the out-of-scope list, including *"Alembic migrations"*); §3.5 (the explicit-state invariant — a constraint that is declared but not carried is exactly the kind of *unwritten state* this project distrusts); the truth invariant.
3. Load **features 404, 417, 426, 411, 421** — the contracts that surround this mechanism — **and read what each reserves.**
4. **Add one event listener** to `backend/app/db.py`.
5. **Write the three regression tests.**
6. **Document the dialect difference** in `backend/README.md` (one or two sentences).
7. **Inspect every existing test fixture that fails** — and **report each one**, rather than blanket-fixing it.

**What the agent MUST NOT do:**

- **Do not add any foreign key.** The schema already declares ten. This feature changes the **mechanism**, not the schema.
- **Do not add `CHECK` constraints or `STRICT` tables.** That is **feature 404** — a different mechanism, and `CHECK` constraints in SQLite are honoured independently of the foreign-key pragma.
- **Do not implement features 417 or 426** in this slice. **Verify** they have landed; if they have not, that is fine — this feature is their prerequisite, not their dependant.
- **Do not decide `ON DELETE` / `ON UPDATE` semantics.** This feature enforces constraints **as declared**. `ON DELETE` appears in 2 feature contracts in the corpus; this is not one of them.
- **Do not add WAL mode, a busy timeout, or any other pragma.** Not this feature's business.
- **Do not make the pragma configurable.** A flag that can switch off the enforcement this feature exists to enable is a footgun.
- **Do not enable the pragma inside `init_db()` as well.** The event listener covers every connection the application opens, including `init_db()`'s. **One place, not two.**
- **Do not change the database technology.** §3.1 keeps SQLite for dev and Postgres for prod; this closes the *behavioural* gap between them, it does not change the decision.
- **Do not blanket-fix failing fixtures.** A fixture that was writing a dangling reference was carrying an undeclared assumption — **inspect each one and report it.**

**Disambiguation**: this slice is about **the mechanism that makes declared foreign keys enforced**. It is **not** about adding a foreign key (features 417, 426), **not** about `CHECK` constraints (feature 404), **not** about money precision (feature 411 — the *sibling pattern* on a different axis), and **not** about the charter's §7 linter rule (feature 421 — an app-layer instrument, not a data-layer one).

## Frozen contract

**The one thing this contract exists to make true:** *the database LE31 tests against enforces the same rules the database LE31 runs against.*

**The rule, as it would be recorded:**

> **SQLite enforces foreign keys in LE31's development environment.** SQLite does not enable foreign-key enforcement unless `PRAGMA foreign_keys = ON` is set **on every connection**, and its default is **OFF**. LE31's engine sets the pragma on every SQLite connection it opens. Postgres enforces foreign keys by default, so the pragma is a no-op there — but the behaviour is identical on both engines, which is what "same SQLModel code for both" means in practice rather than in aspiration.

**Why the rule is a *mechanism* rule and not a *schema* rule:** LE31's schema already states the constraints — ten foreign keys, correctly declared. **The gap is between what the schema says and what the database does.** Ten declared constraints and zero enforced ones is not a schema problem; there is nothing to add to the schema. It is a **configuration** problem, and that is why the fix is one function.

**Anti-goals, stated so they are not drifted into:**

- **Not a schema slice.** No column, no table, no constraint.
- **Not a general SQLite hardening slice.** No WAL, no busy timeout, no `legacy_alter_table`.
- **Not a migration slice.** §3.2's v1 policy is `init_db()`.
- **Not a cascade-policy slice.** Enforcement is enabled; *what should happen on delete* is not decided.
- **Not a "make the tests pass" slice.** Fixtures that break are **findings**, and each must be reported.

**The asymmetry, stated precisely — this is the shape of the defect:**

| | SQLite (dev) | Postgres (prod) |
|---|---|---|
| Foreign keys declared in the schema? | yes | yes |
| Foreign keys **enforced** by the database? | **NO** (pragma off) | **yes** (on by default) |
| A dangling reference is | **stored silently** | **rejected** |

**A bug that writes a dangling reference passes every development test and fails in production.** That is the same *class* of defect as feature 411 (money precision: *"`Decimal("12.345")` is silently coerced"*) — declared but not enforced — but on the referential-integrity axis, and it has not been filed.

## Files to touch

| File | Change |
|---|---|
| `backend/app/db.py` | **ADD** one `event.listens_for(engine, "connect")` listener that executes `PRAGMA foreign_keys=ON` for SQLite connections. **Plus one import (`from sqlalchemy import event`). Nothing else changes** — not `init_db()`, not `get_session()`, not the `create_engine` arguments. |
| `backend/tests/` (or the repo's existing test location) | **ADD** three tests: the pragma is on for an application connection; a dangling foreign key is **rejected**; a `NULL` foreign key is **still accepted**. |
| `backend/README.md` | **AMEND** with one or two sentences: SQLite requires the pragma per connection, Postgres enforces foreign keys by default, and LE31's dev engine enables it in `backend/app/db.py`. |
| `features/427-…md` | **VERIFY** the dialect table and the *Dependencies* section name features 417, 426, 404, 411 and 421 correctly. **Amend only if a name is wrong.** |
| `INDEX.md` | **ADD** one row to the "Active feature pipeline" table. |

**Any other file is out of scope.** If the agent believes another file must change, that is a **new finding** — surface it, do not silently widen the slice.

**Explicitly NOT to be touched:** `backend/app/models.py` (**no column changes — that is features 417 and 426**), `backend/app/routers/` (no route), `backend/app/bot/` (no command), `backend/app/services/` (does not exist yet), `features/404-…` (the `CHECK`-constraint slice), `features/417-…` (the sibling FK), `features/426-…` (the sibling FK), `features/421-…` (the linter rule).

## Mandatory LE31 skill list

The external coding agent must load:

- **`le31-conventions`** — the seven-check feature gate and the hard invariants (§3.2 the out-of-scope list, including *"Alembic migrations"*; §3.5 the explicit-state invariant — a declared-but-unenforced constraint is an unwritten state; the truth invariant).
- **`le31-v1-feature-pattern`** — the canonical contract shape and the slicing rules.
- **`le31-research`** — the source-of-truth discipline behind the artifact quote.
- **`le31-handoff-spec`** — the frozen-contract discipline.
- **`le31-data`** — the append-only-ledger discipline and the storage-layer rules; this feature is the storage layer's contract with the schema.

The agent must **NOT** load `le31-feature-pipeline` — the slice is already in the pipeline.

## Mandatory inputs

- **Active feature**: `features/427-le31-sqlite-never-enables-pragma-foreign-keys-first-party-every-declared-fk-is-unenforced-in-dev-while-postgres-enforces-it-in-prod-v1-sqlite-fk-enforcement.md`
- **Execution proof** (re-runnable): `/opt/data/le31_mmm3_research_work/_exec_proof_2026_11_02.py` — run with `/opt/data/le31-verify-2026-10-27/.venv/bin/python`. Probe 3 (`PRAGMA foreign_keys = 0`), Probe 3b (with the pragma ON, the dangling insert raises `IntegrityError`), Probe 5 (`db.py` contains no `foreign_keys`).
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-11-02.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-11-02/`

## Verification protocol reference

**Reference**: `coding-agent/skills/le31-verification-protocol` and `PROJECT_CHARTER.md` §8.

1. **Re-run the execution proof** and confirm Probe 3 now returns **`1`** and Probe 5 now reports that `db.py` **does** mention `foreign_keys`. **The proof must flip, not merely pass.**
2. **Confirm the pragma is on for an application connection** — open a session via LE31's own `get_session()` and assert `PRAGMA foreign_keys` returns `1`. **Do not assert it on a hand-rolled connection** — the whole defect is that the application connection did not have it.
3. **Run the three regression tests.** The dangling-reference test must fail **before** the change and pass after.
4. **Confirm the nullable case still works** — a `NULL` foreign key is **accepted**. **Enabling enforcement must not turn nullable columns into required ones.**
5. **Inspect every failing fixture individually.** For each one, determine whether it was (a) writing a dangling reference, which is a **real latent bug now exposed** and must be reported, or (b) relying on the pragma being off for some other reason. **Report the list. Do not blanket-fix.**
6. **Confirm nothing else changed** — `git diff --stat` must show only the files in *Files to touch*. **In particular, `backend/app/models.py` must be untouched.**
7. **Confirm the listener is scoped to SQLite** — the `settings.database_url` guard must be present, so the Postgres path is unaffected.
8. **Confirm `init_db()` was not also changed** — the pragma is enabled in exactly **one** place.

## Rollback path

**Trivially reversible. The slice changes no schema and writes no data.**

1. **Revert the commit.** `git revert` removes the listener.
2. **No data loss.** There are no `StockEntry` rows, and no ledger write path exists (`StockEntry(` is constructed **zero** times outside its own class declaration, verified 2026-11-02).
3. **What remains safe if removed:** every existing behaviour — and, precisely, the current behaviour of accepting dangling references. **This is the state LE31 is in today, and the reason the defect is filed rather than deferred.**
4. **Retained data:** none. The slice **writes no rows and reads no rows**.
5. **⚠️ Rollback interaction:** if this is rolled back **after** features 417 or 426 have landed, those features' foreign keys become declared-and-unenforced. **That is not a regression** — it is exactly the state LE31's other eight foreign keys are in today — but it must be **recorded**, because it silently removes the guarantee those features were filed to create.

## Sign-off gap

**Four owner decisions are open. None blocks the fix; each is recorded so the next pass does not re-open it.**

1. **Should the pragma be enabled in `init_db()` as well, or only on the event listener?** **Recorded default: the listener alone.** `init_db()` uses the same engine, so the listener fires for it too. A second `PRAGMA` would create a second place to forget to update.
2. **What about `PRAGMA foreign_keys` and table rebuilds?** SQLite's documented quirk: the pragma is a **no-op inside a transaction**, and altering a table with foreign keys enabled requires care. **Recorded default: defer.** LE31 uses `init_db()` (no migrations) per §3.2, so no table is rebuilt today. **When Alembic arrives post-v1, this must be revisited** — recorded as known debt.
3. **Should the pragma be configurable?** **Recorded default: no.** A flag that can switch off the enforcement this feature exists to enable is a footgun; if a test needs to bypass it, it can open its own connection.
4. **Does this change what feature 404's `CHECK`-constraint work must do?** SQLite honours `CHECK` constraints independently of the foreign-key pragma, so **no** — but this is recorded so the two implementers do not assume a dependency that does not exist, and do not bundle the two slices.

**The agent must not widen any of these decisions.** If the configuration seems to require a different answer, that is a **finding to surface**, not a choice to make.

## Handoff summary

LE31's `backend/app/db.py` builds its engine in five lines and **never enables `PRAGMA foreign_keys`**. The parent proved the consequence by **executing against LE31's real schema**: on a stock SQLite connection the pragma reads **`0`** — SQLite's default is **OFF** — and the *same* dangling insert that SQLite happily stored was **rejected with `IntegrityError`** once the pragma was turned on. **The constraint exists and the mechanism is switched off.**

The consequence is that **ten declared foreign keys are enforced on none of them in development.** `batch_id`, `menu_item_id`, `visit_id`, `table_id`, `server_id`, `closed_by`, `bill_id`, `by_user_id` — every one of them declared in `backend/app/models.py`, every one of them inert on the database the team tests against. Postgres enforces foreign keys by default, so **the production database refuses rows the development database accepts.** A bug that writes a dangling reference passes every development test and fails in production — and the charter's P0 acceptance criterion (*"the ledger has one entry"*) is a manual test that runs on the permissive one.

**This is the cheapest defect in the series and the prerequisite for two others.** Features **417** and **426** both add foreign keys to LE31's ledger; **without this feature they add decorations.** And it is cheap precisely *now*: the ledger has **zero** construction sites, `backend/app/routers/` holds only `__init__.py` and `tables.py`, and the natural next piece of work is the stock-writing router. **Before that router lands, this is a configuration nicety; after it lands, this is the difference between the development database and the production database having the same rules.**

The third-party instrument (`Raktim94/nodedr-restaurant-pos`, AGPL-3.0, off-stack — **vocabulary only, no code adopted**) supplies the discipline this fix embodies: its README states that the full rationale for *"**why Postgres over the originally-specced SQLite**"* is written down — because the two dialects are not the same, and *"a SQLite edition"* is on its not-yet-built list. LE31's charter says *"Same SQLModel code for both."* **This feature is where that sentence stops being aspirational.**
