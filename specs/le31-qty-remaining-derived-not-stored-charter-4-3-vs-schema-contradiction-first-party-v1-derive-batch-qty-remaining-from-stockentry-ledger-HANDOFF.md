# HANDOFF — Feature 374: derive `Batch.qty_remaining` from `StockEntry` (charter §4.3 vs schema contradiction — FIRST-PARTY)

**This is the only `build` pick of the 87-pass series.** It is a defect in LE31's own code, not a reference to someone else's. **Do not defer it.**

**Discovery chain:** Daily Brainstorm 2026-10-24 → Pick A (`ramaraihan12/warung-pos`, feature 373) stated *"Stock is never a stored number"* in its README → the parent went and read LE31's own `backend/app/models.py` → found `qty_remaining: int` persisted on `Batch`, with **no derivation site anywhere in the repository**, while `PROJECT_CHARTER.md` §4.3 and the `StockEntry` docstring both say the quantity is *"computed on read, not stored"*.

**Full evidence record: `features/374-le31-qty-remaining-derived-not-stored-charter-4-3-vs-schema-contradiction-first-party-v1-derive-batch-qty-remaining-from-stockentry-ledger.md`**

## Active feature path

`features/374-le31-qty-remaining-derived-not-stored-charter-4-3-vs-schema-contradiction-first-party-v1-derive-batch-qty-remaining-from-stockentry-ledger.md` — **build** (Pick B of Daily Brainstorm 2026-10-24).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *This is the difference from every other pick of the series.* The job is not inferred. **The owner's own charter says the quantity is derived; the code says it is stored.** The job is to make the code say what the charter says. Evidence class: **OBSERVED** — parent-run greps, re-runnable in four commands (below). |
| 2 | Viability | ✓ | The change is small and wholly internal: drop one column, add one helper, add tests. No third-party dependency, no licence question, no traction question (**the subject is LE31's own code**). |
| 3 | Practicability and confidence | ✓ | On-stack: `backend/app/models.py` is SQLModel, the ledger is `StockEntry` with `batch_id` indexed. A `SUM` over an indexed `batch_id` is trivially cheap at LE31's scale (one restaurant, one kitchen, a few hundred entries a day). **Confidence: high** — the defect is directly observable, and §4.3 already specifies the fix exactly. |
| 4 | Conflict | ✓ | **No conflict — the change restores compliance with an existing charter rule.** §4.3 *requires* the derivation. The persisted column is the deviation, and it is the deviation being removed. The only genuine sub-question is whether `qty_start` also goes (design (a) vs (b)) — see Open questions. |
| 5 | Outcome + appetite + scope | ✓ | Maps to a v1 build. Maximum time worth spending: **2–3 hours including the migration and the regression test.** The scope is deliberately one column, one helper, one test file. |
| 6 | Cost to operational value | ✓ | High. The value is that LE31's stock number stops being a fiction and becomes a derivation — and that the four contracts describing it (26, 34, 371, 372) become true. No training, no maintenance, no new surface. |
| 7 | Circuit breaker + reversibility | ✓ | **Fully reversible: re-add the column.** No data is lost by the drop, because nothing has ever written it (parent-verified: no code reads or writes it anywhere). Rollback is `git revert` plus a re-add. **The only irreversible part is if a selling path lands first** — which is exactly why this is `build` and not `defer`. |

**Gate verdict: `build`** — check 1 passes on **observed** evidence. This is the first pick in the 87-pass series whose gate check 1 rests on something the parent *ran*, rather than something it inferred from an external description.

## Bucket

**v1 (correctness of the core stock invariant)** — Pick B of Daily Brainstorm 2026-10-24. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming. Because the **parent research issue for this pass also failed to create**, the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload, and that is the only project that exists for the write.

## Files to touch

**The change itself (ordered — the replacement must exist before the thing it replaces is removed):**

- `backend/app/services/__init__.py` — **NEW.** The directory does not exist today.
- `backend/app/services/stock_service.py` — **NEW.** One public helper, e.g. `remaining_for_batch(session, batch_id) -> int`, returning `SUM(stock_entry.qty_delta WHERE batch_id = X)`. **No caching. No assignment to a model attribute. No write path.** Note: features 34 and 371 already name this exact path — creating it makes those two contracts true.
- `backend/app/models.py` — **REMOVE** `qty_remaining: int` from `class Batch` (currently line 106). **Possibly also remove** `qty_start: int` (line 105) if design (b) is taken — see Open questions. `StockEntry` is **unchanged**.
- `tests/test_stock_derivation.py` — **NEW.** The load-bearing tests (below).
- `backend/app/db.py` (or wherever `init_db()` lives) — the v1 migration. **Per §3.2, v1 uses `init_db()`, not Alembic** (*"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)"*). `backend/requirements.txt` already pins `alembic>=1.13` — **do not silently introduce Alembic**; follow §3.2's stated v1 policy and record the prod-migration step as known debt.

**The documentation that currently describes a derivation that does not exist (forward-pointers only — do NOT rewrite their history):**

- `features/26-reorder-point-on-stockentry.md` — says *"qty_remaining still derived from StockEntry"*. Add a one-line pointer to feature 374.
- `features/34-stockout-prep-board-snapshot.md` — says *"qty_remaining = SUM(stock_entry.qty_delta) per active_batch"* and names `backend/services/stock_service.py`. Add a one-line pointer.
- `features/371-Donkie-Spoolman-...-vocabulary.md` — says *"batch.qty_remaining already is the derived projection"* and names `backend/services/stock_service.py` as a file to touch. Add a one-line pointer.
- `features/372-hitaishi2222-kinv-...-vocabulary.md` — says *"the same derive-never-store discipline as batch.qty_remaining"*. Add a one-line pointer.
- `PROJECT_CHARTER.md` §4.3 — the text is already **correct**; add a pointer to the helper's path so the charter names the code that implements it.

**Do NOT touch (out of scope, explicitly):**

- `backend/app/routers/` — **do not add an `inventory` router, a selling endpoint, or a `/sold_out` command.** No selling path is in scope.
- `backend/app/bot/cook_bot.py` — no Telegram behaviour changes.
- `StockEntry` — no new reasons, no schema change, no new columns.
- Any new table.

## The load-bearing tests

`tests/test_stock_derivation.py` must contain, at minimum:

1. **The derivation equals the ledger sum** — a batch with a set of `StockEntry` rows derives the expected quantity.
2. **Inserting an entry changes the value** — this is what proves it is *derived* and not *cached*. A cached implementation passes test 1 and fails this one.
3. **The column is gone** — assert that `Batch` exposes no `qty_remaining` attribute and that the `batch` table has no such column. **This is the regression test that makes the defect impossible to reintroduce silently.** Without it, the next contributor who reads §4.3 and sees the column in the schema will reasonably assume it is the derived value, cached.
4. **The opening balance** (if design (b) is taken) — the `initial` `StockEntry` alone yields the opening balance, and `qty_start` is absent.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. The observable behaviour here is **the derived number in a running system**: create a batch, add stock entries, and confirm the derived remaining quantity matches the ledger — through the actual code path, not only in a unit test. Concretely, a script or `init_db` + direct service call that inserts `initial +8`, `sale -1`, `sale -1`, `waste -2` and reads back `4`.

**The pre-flight that must be re-run before starting (parent-run on 2026-10-24; re-run it — the answer is the whole point of this feature):**

```bash
cd /opt/data/le31_mmm3_research_work
grep -n "qty_remaining" backend/app/models.py            # expect: one persisted column
grep -rn "qty_remaining" . --include=*.py --include=*.sql | grep -v "\.venv"   # expect: NO code hits besides the declaration
ls backend/app/services/ 2>&1                            # expect: No such file or directory
ls backend/app/routers/                                  # expect: only __init__.py and tables.py
```

If the second command now returns a **derivation site**, the defect has already been fixed by someone else — **stop and re-read the feature contract before implementing.**

**Post-implementation, the same command must return a hit inside `backend/app/services/stock_service.py` and the column must be gone from `models.py`.** That inversion is the proof of the change.

## Rollback path

`git revert` the commit, or re-add the column. **No data loss on revert**, because the column was never written by any code path (parent-verified). If a selling path lands before this feature, the rollback becomes a backfill of every historical batch and an audit of every number the owner was shown — **which is the entire reason this is `build` and not `defer`.**

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *Stock* rule first)
- `le31-data` — append-only ledger rules (`StockEntry`: never update or delete) **— read this one carefully, it is the invariant being restored**
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants (§3.2 migrations, §4.3 the append-only stock ledger)

## Open questions carried into any future build

1. **Design (a) or (b) for the opening balance?** (a) keep `qty_start` as a column, derive `remaining = qty_start + SUM(delta)`; or (b) make the `initial` `StockEntry` the sole opening-balance source and drop `qty_start` too. **§4.3's own insert-path wording ("Morning prep → qty_delta = +N, reason = 'initial' (one row per batch)") already implies (b).** The parent has not decided; (b) is cleaner if it lands without schema surprise, and **the choice must be recorded in the code and in this HANDOFF.** Either way, exactly one representation of the opening balance must survive.
2. **Should `qty_remaining` exist as a read-only `@property`?** **Recommendation: no.** A property that runs a query hides I/O inside attribute access and can go stale within a session. The helper is the only accessor.
3. **Does the fractional-money guard belong here?** **No.** It is a different invariant (§3.6, money) with a different failure mode. It is recorded in feature 373's open questions and should be its own small feature. **Do not bundle it.**
4. **Which downstream features must be updated to use the helper?** Features 03, 04, 26, 34 and 45 all plan to write to `qty_remaining`. **This feature must land before any of them writes to it**, or they must be updated to call the helper instead. The parent has not done a full audit of those five contracts; the coding agent should re-check them when it touches them.
