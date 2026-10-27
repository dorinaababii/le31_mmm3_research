# HANDOFF — Feature 388: give `Table` a stored status so a second seat is refused instead of opening a second `Visit`

**This is the only `build` pick of the 89-pass series, and the only first-party finding in four passes that is reachable in the shipped code today.** It was **reproduced by execution** on 2026-10-27, not inferred from reading code. **Do not defer it.**

**Discovery chain:** Daily Research 2026-10-27 → the parent read the README of the in-window repo `adil-alzhan-dev/kumo-qr-ordering` (null licence, ★0, created 2026-10-24) whose Features section says *"A lost connection never creates a duplicate order: each order carries a key"* — and the same day's OpenAlex sweep surfaced *"A Reliable Event-Reconciliation Framework for Real-Time Restaurant Order and Inventory Synchronization"* (2026-10-23, DOI `10.5281/zenodo.23572532`), whose abstract prescribes *"**order-state validation**"* and *"duplicate-event detection"* as distinct concerns → that is the **third** independent arrival at the duplicate-event family (after yesterday's `dc-tech-inc/dotnet-pos-integration` ADR-0001 and `kumo-qr-ordering`'s key) → the parent therefore went and read LE31's own `backend/app/routers/tables.py` → found `# TODO: reject if table is not FREE (need TableStatus column on Table)` on **line 50** → and then **ran the real router against a throwaway SQLite DB**: two identical `POST /api/tables/1/seat` requests, **both HTTP 200**, **two open `Visit` rows** (`ids [1, 2]`), and the floor grid still showing a single `"seated"` tile.

**Full evidence record: `features/388-le31-table-state-machine-first-party-table-has-no-status-column-so-a-second-seat-opens-a-second-visit-v1-table-state-validation-and-seat-idempotency-vocabulary.md`**

## Active feature path

`features/388-le31-table-state-machine-first-party-table-has-no-status-column-so-a-second-seat-opens-a-second-visit-v1-table-state-validation-and-seat-idempotency-vocabulary.md` — **build** (Pick A of Daily Research 2026-10-27).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When the waiter taps "Seat party" on a tablet — and the connection hiccups, or the waiter taps twice — the waiter wants one party at one table, but struggles because the endpoint does not check whether the table is free, so that the floor's view of the room stays true.* Links to existing feature **01 (Table Management)**, whose Description says *"Tap a **free** table"*. **Pass on OBSERVED evidence** — the pain was **executed**, not inferred: HTTP 200 twice, two `Visit` rows, one tile on the floor. |
| 2 | Viability | ✓ | One column, one guard, one release primitive, one test. **No new role, no new surface, no admin.** The waiter recovers by seeing a 409 with the existing `visit_id`; the owner recovers by seeing one `Visit` instead of two. **Pass.** |
| 3 | Practicability and confidence | ✓ | Exactly on-stack: `backend/app/models.py` is SQLModel, `TableStatus` **already exists** (line 27) and is **already imported** by `routers/tables.py` (line 10). **No new design to invent — only a new column on a class whose sibling columns are right there.** **Confidence: high** for the defect (reproduced), **medium** for the fix shape (two shapes are available: a stored column vs a derived-uniqueness constraint; the charter does not choose — see Open questions). **Named rabbit hole:** the spec/implementation divergence — feature 01's data model omits the column, so **the contract must be corrected, not only the code**. |
| 4 | Conflict | ✓ | **No conflict — the change enforces an existing LE31 invariant.** §3.1 *"Operational transitions are explicit user actions"* is **strengthened**: a seat on an already-seated table is not a legal transition and must be refused. **Adjacent tensions to respect, not to resolve here:** (a) the oversell/shortfall policy is feature 382's subject — **this feature does not decide whether a sale is allowed**; (b) `Batch.qty_remaining` is feature 374's; (c) `OrderItem.batch_id` is feature 385's; (d) the ledger-write idempotency rule is feature 382's. **All four are open and NONE is bundled here.** |
| 5 | Outcome + appetite + scope | ✓ | v1 Core MVP correctness fix (feature 01 is P0: *"Waiter can seat a party at any free table"*). **Maximum time worth spending: one focused slice** — the column, the guard, the release primitive, the test, the one-line contract fix. **Explicitly NOT in scope:** the full five-state machine as transitions (only `free ⇄ seated` is wired), any change to `Visit`/`OrderItem`/`StockEntry`/`Bill`, any waiter-UI restyle, any Telegram change, any auth work (the `server_id` TODO stays), any reconciliation of pre-existing duplicate `Visit` rows. |
| 6 | Cost to operational value | ✓ | The pain is **a real party seated, eating, and un-billed** — high severity; frequency unknown (one restaurant, no traffic yet) and **not claimed**. Cost: under half a day, no new surface, no new dependency, no third-party licence question. ICE/RICE as vocabulary only, no fabricated arithmetic. **The asymmetry that decides the ordering: cheap now, expensive later, because a party with no bill cannot be reconstructed after the fact without an audit that has no ground truth.** |
| 7 | Circuit breaker + reversibility | ✓ | **Fully reversible: drop the column and the guard.** No existing data is destroyed — no code writes `Visit` rows outside the seat route, and the new column is additive with a default. **Stop evidence:** the pre-flight below shows `Table` already has a status column → **stop and re-read the contract.** **Review point:** after the guard lands, re-run the two-POST observation and confirm the second returns 409 and the open-`Visit` count stays at 1. **Pre-mortem (the most likely failure):** the stored status and the currently-derived status disagree, so the UI shows `seated` while the column says `free` — **this is why the contract fixes ONE source of truth (the stored column) and demotes the derived helper to a test assertion only.** |

**Gate verdict: `build`** — check 1 passes on **observed, executed** evidence.

## Bucket

**v1 (table-state correctness — a core operational invariant)** — Pick A of Daily Research 2026-10-27. Per `le31-feature-pipeline/SKILL.md` step 4 the matching project is **`le31 v1 — Core MVP` (P-HMM-3)**. Per `le31-feature-pipeline/SKILL.md` line 33, the parent confirmed with `list_projects` on 2026-10-27 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that **`le31 v2 owner-pains` / `le31 v2-AI` do not exist**. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — **40th consecutive day**), the sub-issue has no parent to hang under — it is routed to `le31 v1 — Core MVP` (P-HMM-3) in the fallback payload as the correct bucket, and **no project attachment actually occurred**.

## Files to touch

**The change itself (ordered — the contract is corrected before the column, and the column before the guard):**

- `features/01-table-management.md` — **EDIT** the Data model block: `Table (id, label, section, seats, x, y)` → add `status`. **ADD** one sentence to the Description stating that seating a non-free table is refused (HTTP 409) and carries the existing `visit_id`. **Do not restructure the feature, do not renumber it, do not add the other three states as transitions.**
- `backend/app/models.py` — **ADD** `status: TableStatus = TableStatus.free` to `class Table` (line 64). `TableStatus` is already defined at line 27 — **no new enum, no new import**. **DO NOT** change any other class, field or timestamp.
- `backend/app/routers/tables.py` — **EDIT** `seat_party` (line 33): after the existing 404/400 checks, refuse with **HTTP 409** when `table.status` is not `free`, and include the open `visit_id` in the response body; on success set `table.status = TableStatus.seated` **in the same transaction** as the `Visit` insert, with **one** `session.commit()`. **EDIT** `_table_status` (line 64) to return the **stored** `table.status` — **keep the function** (the JSON shape depends on the `status` key), change only its body. **ADD** the release path (see below).
- `tests/test_table_seat_guard.py` — **NEW.** The load-bearing tests (below).
- `backend/app/db.py` — **VERIFY** that `init_db()` creates the altered table via SQLModel `create_all`; **do not assume.** Per §3.2, v1 uses `init_db()`, not Alembic; `backend/requirements.txt` already pins `alembic>=1.13` but **do not silently introduce Alembic** — follow §3.2's stated v1 policy and record the prod-migration step as known debt.

**The release path — read this before you write it.** The table must be returnable to `free`, or it becomes permanently unseatable. Parent-verified 2026-10-27: `backend/app/routers/` contains **only** `__init__.py` and `tables.py`, and **`Visit.closed_at` is set nowhere in the shipped code**. So:

- If a visit-closing path exists by the time you build, hook the release into it.
- If it does not, expose a **minimal** `POST /api/tables/{id}/release` that closes the open visit and frees the table, and record in the contract that the billing flow (features 05/14) will call it.
- **If you find yourself writing a bill-closing endpoint, STOP — that is feature 14's job.** Scope creep here fails the gate.

**Do NOT touch (out of scope, explicitly):**

- `backend/app/models.py` — **any class other than `Table`.** Not `Visit`, `OrderItem`, `StockEntry`, `Bill`, `DerivedTip`, `Shift`, `Batch`, `MenuItem`, `ItemStatus`.
- `backend/app/routers/` — **do not add an orders router, an inventory router, or a selling endpoint.**
- `backend/app/services/` — **do not create it.** This slice adds no service layer; if you want one, stop.
- `backend/app/bot/cook_bot.py` — **no new command, no new output.**
- `backend/app/routers/tables.py` line 39 — the `# TODO: from auth token` comment **stays**.
- `backend/requirements.txt` — **no dependency change.**
- `PROJECT_CHARTER.md` — **no change required.** If you touch it, the only permitted edit is a pointer to this feature. **Do not** add a table-state machine to the charter in this slice.
- Any `Option`/`Modifier`/`Variant` model — features 386/387.
- `Batch.qty_remaining` — feature 374. `OrderItem.batch_id` — feature 385. Idempotency-key semantics — feature 382.

## The load-bearing tests

`tests/test_table_seat_guard.py` must contain, at minimum:

1. **The defect is impossible to reintroduce** — seat a table twice; assert the **second call returns 409** and that the number of **open** `Visit` rows for that table is **exactly 1**. **This is the test that makes the defect impossible to reintroduce silently.**
2. **The refusal is not decorative** — assert the 409 body carries the **existing** `visit_id`, and that it equals the id returned by the first successful seat. A 409 with no id would let the UI recover badly.
3. **A refusal creates nothing** — assert the second call did **not** add a `Visit` row, and did **not** change the table's status.
4. **The state transition is atomic** — after a successful seat, assert `table.status == TableStatus.seated` **and** an open `Visit` exists. (If these could diverge, the feature has not fixed the inconsistency it was written for.)
5. **The release path frees the table** — release, then assert `table.status == TableStatus.free`, the visit is closed, and **a subsequent seat succeeds** (HTTP 200, new `visit_id`). Without this the table is permanently bricked — a bug worse than the original.
6. **The status is genuinely stored, not derived** — assert `Table` has a `status` column in `SQLModel.metadata` and that two tables with different stored statuses report different values from `GET /api/tables`. This is the **single-source-of-truth guard** the pre-mortem names.
7. **The column is backward-compatible** — a `Table` row created without an explicit status persists and reads back `free`. **This is the migration guard**: a column accidentally declared NOT NULL is a classic silent migration failure that only appears in production.
8. **The status is a string column, not a native DB ENUM** — assert the stored value round-trips on **SQLite** (dev) and would on Postgres. §3.1 requires one schema across both; a native ENUM does not port.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. **The observable behaviour here is a row count and an HTTP status in a running system.**

**The pre-flight that must be re-run before starting** (parent-run on 2026-10-27; **re-run it — the answer is the whole point of this feature**):

```bash
cd /opt/data/le31_mmm3_research_work

# 1. the missing column
sed -n '/^class Table(/,/^class AppUser/p' backend/app/models.py
# expect: id, label, section, seats, x, y — and NO status field

# 2. the enum exists but is not stored
grep -n "status" backend/app/models.py
# expect: EXACTLY ONE hit — OrderItem.status (line 151). Table has no status.

# 3. the developer's own note
grep -n "TODO: reject if table is not FREE" backend/app/routers/tables.py
# expect: line 50

# 4. the spec/implementation divergence
grep -n "Table " features/01-table-management.md
# expect: "Table          (id, label, section, seats, x, y)"  — NO status
grep -n "Tap a free table" features/01-table-management.md
# expect: a hit — the Description REQUIRES a free table, the data model cannot express one

# 5. LE31's own cited reference disagrees with LE31's own contract
grep -n "Table (id, seats, section" research/01-pos-systems.md
# expect: a hit — the peer model HAS a status column

# 6. the shipped backend is a skeleton (context for scope)
grep -c "@app\." backend/app/main.py
# expect: 3   (/api/health, /, and the startup hook)
ls backend/app/routers/
# expect: __init__.py  tables.py
```

**And the reproduction — run it before and after.** The parent-observed transcript is the contract's evidence; **re-run it to see the fix change the answer**:

```bash
cd /opt/data/le31-verify-2026-10-27
.venv/bin/python observe_seat.py
# BEFORE the fix: second POST returns HTTP 200; "open Visits after 2nd POST: 2 -> ids [1, 2]"
# AFTER the fix:  second POST returns HTTP 409; "open Visits after 2nd POST: 1 -> ids [1]"
# VERDICT line flips from DEFECT_REPRODUCED to NO_DEFECT
```

**After the fix, the observable behaviour to exercise:** seat a table, seat it again, and confirm the floor grid shows **one** yellow tile, **one** open visit, and that the waiter is told which party is already there. **Then release it and seat a new party** — the table must be usable again.

## Rollback path

- **Drop the column and the guard.** The feature is additive: `status` has a default, and no pre-existing row has a meaningful value beyond `free`/`seated`.
- **No data migration is required for rollback** — the column can be dropped.
- **Existing duplicate `Visit` rows are NOT touched by this feature, in either direction.** A live DB could already contain two open visits for one table; this feature prevents **new** duplicates and does **not** merge, close or delete existing ones — that is a data migration with product judgement in it and it is explicitly out of scope. **Recorded in the feature's Open questions.**
- **If the release path turns out to conflict with the eventual billing flow (features 05/14), the release primitive is the piece to re-wire** — it is deliberately small and isolated for exactly this reason.
- **Known debt to record, not to fix:** the prod migration for the added column (v1 uses `init_db()`, per §3.2, not Alembic).

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — **read first.** The seven-check gate, the hard invariants, and the source-of-truth order.
- `development` — the generic coding pipeline (specify → plan → tasks → implement → independent review). **Do not skip to implementation.**
- `test-driven-development` — **RED-GREEN-REFACTOR.** The regression test must **fail on today's code** and pass after the fix. Write it first and **watch it fail** — a test that only ever passed proves nothing.
- `systematic-debugging` — the root cause is known here, but the discipline still applies to anything you hit.
- `pre-merge-review` — **an independent non-author review is required before this merges.** This is product code.
- `spckit-specify` / `spckit-plan` / `spckit-tasks` — if the change grows beyond the slice described above, stop and re-specify rather than expanding in place.
- `verify-before-fixing` — **do not "fix" a failing check by weakening it.** This series has recorded five separate occasions where the *checker* was the bug (see `le31-cron-infra` §17). Read the failing output, triage it, and only then touch an artefact.
- `raw-api-web-research` — not needed for this slice; the research is already done and filed.

## Open questions carried into any future build

1. **Stored column vs database-level uniqueness.** This slice decides **stored column + application guard**. The stronger alternative — a partial unique index on `(table_id) WHERE closed_at IS NULL` — makes the *database* refuse the second row, but is **not portable to SQLite** the way §3.1 requires, and a partial index is a different schema object to migrate. **Decided here: stored column.** The database-level constraint is future work. **Do not implement it in this slice.**
2. **What to do about duplicate `Visit` rows that already exist.** **Decided: out of scope, explicitly.** The guard prevents new duplicates; existing ones are an operational cleanup the owner must confirm. **Do not auto-merge them.**
3. **Who calls the release.** The bill (features 05/14) is the eventual caller. **Decided: provide the release primitive; do not build the bill.**
4. **Does the 409 body carry the existing `visit_id`?** **Decided: yes.** The waiter needs to know *which* party is already there; a bare 409 makes the UI's recovery worse, not better. This is the one decision here that changes the API's usefulness to the operator.
5. **Does a future feature need the `ordered` / `billed` / `dirty` states as real transitions?** **Not decided.** Only `free ⇄ seated` is wired here. The other three enum values exist and are unused — **do not wire them in this slice.**

---

**Bottom line for the coding agent:** this is a **small, well-understood, reproduced** defect. The evidence is executed, not inferred; the fix is one column, one guard, one release primitive, one test file; and the pre-mortem has already named the one way this could go wrong (two sources of truth). **Read `features/388-…md` in full before you start — it contains the reproduction transcript and the exact expectations.**
