# HANDOFF — 426-le31-stockentry-ref-order-item-id-foreign-key

**Status**: **build** (v1, first-party — **the defect is in LE31's own schema and is proven by execution**)
**Date**: 2026-11-02
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/426-le31-stockentry-ref-order-item-id-has-no-foreign-key-first-party-the-ledger-accepts-a-reference-to-an-order-line-that-does-not-exist-v1-stockentry-order-reference-foreign-key.md`
**LE31 feature gate verdict**: **build** — gate check 1 (**demand**) is **OBSERVED**: the charter's P0 acceptance criterion *"order a tiramisu → stock goes 8 → 7 → ledger has one entry"* depends on the ledger row naming the order line that caused it, and that name is currently unconstrained. Gate check 2 (**evidence**) is **OBSERVED by EXECUTION**: a `StockEntry` naming `order_item 999999` was **accepted and stored** against LE31's own schema, and the referenced order item was **absent** — a dangling reference, absorbed silently by the ledger's own `SUM(qty_delta)` derivation. Gate check 3 (**practicability**) is **PASS**: one column, one `Field(...)` argument, three assertions. Gate check 4 (**scope**) is **PASS**: no runtime flow changes — `StockEntry(` is constructed **zero** times today. Gate check 5 (**consistency**) is **PASS** with one stated dependency: the same column's sibling (`by_user_id`) is feature **417**, and the *enforcement mechanism* is feature **427**.

## Trigger policy

This is a **`build`** contract. The external coding agent **SHOULD** add the foreign key to `StockEntry.ref_order_item_id`, write the regression test, and amend the deferral note in feature 404.

**⏱️ ORDERING — READ FIRST.** This slice is **inert** unless feature **427** (`le31-sqlite-never-enables-pragma-foreign-keys`) has landed. SQLite's `PRAGMA foreign_keys` defaults to **OFF**, so until 427 enables it, the foreign key added here is **declared and unenforced** — exactly the state LE31's eight existing foreign keys are in today. **Feature 427 must land first, or in the same PR.** If 427 is not yet landed, **stop and say so** rather than landing a decoration.

**What the agent MAY do:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the out-of-scope list, including *"Alembic migrations"*); §3.6 (the money-is-`Decimal` rule, for context on the other schema-contract feature); the truth invariant (*"the ledger looks perfectly well-formed"* is the failure this feature removes).
3. Load **features 417, 404, 385, 427** — the four contracts that surround this column — **and read what each reserves.**
4. **Change one line** in `backend/app/models.py`.
5. **Write the three regression tests.**
6. **Amend feature 404's deferral note** (a one-line amendment — see *Files to touch*).
7. **Record the sibling relationships** in the feature file (already done — verify, do not re-derive).

**What the agent MUST NOT do:**

- **Do not touch `StockEntry.by_user_id`.** That is **feature 417**. Different column, different defect. **If both land in one PR, they must be separate commits with separate tests.**
- **Do not add `OrderItem.batch_id`.** That is **feature 385** (the *forward* pointer). This feature constrains the *back* pointer.
- **Do not enable `PRAGMA foreign_keys`.** That is **feature 427**. **Do not implement 427 here** — but do verify it has landed, and if it has not, say so.
- **Do not add `CHECK` constraints or `STRICT` tables.** That is **feature 404**.
- **Do not make `ref_order_item_id` NOT NULL.** `NULL` is correct for `initial`, `restock`, `waste` and `sold_out` rows.
- **Do not add `ON DELETE` semantics.** The delete policy is an open question in the feature file; it is **not decided**.
- **Do not add an index** to `ref_order_item_id` — the recorded default is no index.
- **Do not write a `StockEntry` write path, a selling endpoint, or an inventory router.** None exists; this slice changes the schema shape only.
- **Do not implement feature 421's linter rule** — a linter rule and a database constraint are different instruments.

**Disambiguation**: this slice is about **the ledger's back-pointer to the order line**. It is **not** about the actor FK (feature 417), **not** about the order's forward pointer to the batch (feature 385), **not** about the FK *enforcement mechanism* (feature 427), **not** about `CHECK` constraints (feature 404), and **not** about the `qty_remaining` derivation (feature 374).

## Frozen contract

**The one thing this contract exists to make true:** *the ledger's back-pointer to the order line is exactly as trustworthy as its forward-pointer to the batch.*

**The rule, as it would be recorded:**

> **A `StockEntry` that names an order line names an order line that exists.** `StockEntry.ref_order_item_id` carries a foreign key to `order_item.id`. A ledger row whose reference is `NULL` is a row not caused by an order line — morning prep, restock, waste, withdrawal — and that is the **only** legitimate use of `NULL`. A ledger row that names an order line which does not exist is **rejected by the database at write time**, because the ledger is append-only and can never be corrected afterwards.

**Why the rule must exist as a *database* constraint and not as application code:** the ledger has no `UPDATE` path, no `DELETE` path and no `void` concept (§4.3: *"EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE."*). **Write-time validation is the only validation the ledger will ever get.** An application-layer check can be skipped by a second code path, a script, or a retry; a foreign key cannot.

**Anti-goals, stated so they are not drifted into:**

- **Not a general "add foreign keys everywhere" slice.** One column.
- **Not a write-path slice.** No router, no service, no bot command.
- **Not a data migration.** §3.2's v1 policy is `init_db()`. There are no rows to migrate.
- **Not a policy decision about `ON DELETE`.** Recorded as open.

**The deferral chain that this slice closes — and that is itself part of the finding.** Feature 404 states, verbatim: *"note that `StockEntry.ref_order_item_id` has no FK at all, which is **feature 385's** subject, not this one."* But feature 385's Goal is *"one nullable foreign key on `OrderItem`"* — the forward pointer — and it **never** adds a foreign key to `ref_order_item_id`. The chain is **404 → 385 → (nothing)**, and the back-pointer is owned by no feature. **The corpus's own cross-references were load-bearing and one link was missing.** The amendment in *Files to touch* closes it so the next pass does not re-derive this and file a duplicate.

## Files to touch

| File | Change |
|---|---|
| `backend/app/models.py` | **ONE LINE.** In `class StockEntry`: `ref_order_item_id: int \| None = None` → `ref_order_item_id: int \| None = Field(default=None, foreign_key="order_item.id")`. **Nothing else in this file changes.** |
| `backend/tests/` (or the repo's existing test location) | **ADD** three tests: a dangling reference is **rejected**; a `NULL` reference with `reason='initial'` is **accepted**; a valid reference is **accepted**. |
| `features/404-le31-sqlite-tables-not-strict-…md` | **AMEND** the deferral note about `ref_order_item_id` so it points at **feature 426** instead of feature 385. **A one-line amendment. Do not rewrite 404's scope, and do not touch 404's own subject.** |
| `features/426-…md` | **VERIFY** the sibling-relationship table and the *Dependencies* section already name features 417, 427, 385, 404 and 421 correctly. **Amend only if a name is wrong.** |
| `INDEX.md` | **ADD** one row to the "Active feature pipeline" table. |

**Any other file is out of scope.** If the agent believes another file must change, that is a **new finding** — surface it, do not silently widen the slice.

**Explicitly NOT to be touched:** `backend/app/db.py` (that is feature **427**), `backend/app/routers/` (no route exists), `backend/app/bot/` (no command), `features/417-…` (the sibling column), `features/385-…` (the forward pointer), `features/404-…` (beyond the one-line amendment), `features/421-…` (the linter rule), `features/374-…` (the derivation).

## Mandatory LE31 skill list

The external coding agent must load:

- **`le31-conventions`** — the seven-check feature gate and the hard invariants (§3.2 the out-of-scope list, including *"Alembic migrations"*; §3.6 the money-is-`Decimal` rule; the truth invariant — *"the ledger looks perfectly well-formed"* is the failure mode this feature removes).
- **`le31-v1-feature-pattern`** — the canonical contract shape and the slicing rules.
- **`le31-research`** — the source-of-truth discipline behind the artifact quote.
- **`le31-handoff-spec`** — the frozen-contract discipline.
- **`le31-data`** — the append-only-ledger discipline; the ledger's *no-update, no-delete* invariant is the reason this constraint must live in the database.

The agent must **NOT** load `le31-feature-pipeline` — the slice is already in the pipeline.

## Mandatory inputs

- **Active feature**: `features/426-le31-stockentry-ref-order-item-id-has-no-foreign-key-first-party-the-ledger-accepts-a-reference-to-an-order-line-that-does-not-exist-v1-stockentry-order-reference-foreign-key.md`
- **Execution proof** (re-runnable): `/opt/data/le31_mmm3_research_work/_exec_proof_2026_11_02.py` — run with `/opt/data/le31-verify-2026-10-27/.venv/bin/python`. Probe 1a/1b are the defect; Probe 3/3b are the contrast (the pragma is off by default; with it on, the same class of dangling insert raises `IntegrityError`).
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-11-02.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-11-02/`

## Verification protocol reference

**Reference**: `coding-agent/skills/le31-verification-protocol` and `PROJECT_CHARTER.md` §8.

1. **Re-run the execution proof** and confirm Probe 1a now **fails** — i.e. the dangling reference is **rejected**, not stored. This is the load-bearing check: the proof must flip, not merely pass.
2. **Confirm the DDL** carries the constraint: `sqlite3 backend/restaurant.db ".schema stock_entry"` must show `FOREIGN KEY(ref_order_item_id) REFERENCES order_item (id)`.
3. **Confirm the pragma is on** (feature 427 landed): `PRAGMA foreign_keys` must return `1` on a connection from `get_session()`. **If it returns `0`, stop — the foreign key is a decoration and the slice is not complete.**
4. **Run the three regression tests.** The dangling-reference test must fail **before** the change and pass after. **A test that only ever passed proves nothing.**
5. **Confirm the nullable case still works** — a `StockEntry` with `reason='initial'` and `ref_order_item_id=NULL` is accepted. **A foreign key must not turn a nullable column into a required one.**
6. **Confirm feature 404's amendment** is a one-line change and that 404's own scope is untouched.
7. **Confirm nothing else changed** — `git diff --stat` must show only the files in *Files to touch*. **In particular, `backend/app/db.py` must be untouched** (that is 427's file).
8. **Confirm the sibling column is untouched** — `git diff backend/app/models.py` must show **exactly one** changed line, and it must be the `ref_order_item_id` line. **`by_user_id` must not appear in the diff.**

## Rollback path

**Trivially reversible. The slice changes one column declaration and adds tests.**

1. **Revert the commit.** `git revert` restores the previous declaration.
2. **No data loss.** There are no `StockEntry` rows: `StockEntry(` is constructed **zero** times outside its own class declaration (verified by execution, 2026-11-02), so there is nothing to migrate back.
3. **What remains safe if removed:** every existing behaviour. The slice is **inert by construction** — the constraint only ever fires on a write that does not happen today.
4. **Retained data:** none. The slice **writes no rows and reads no rows**.
5. **If 427 is rolled back after this lands:** the foreign key becomes declared-but-unenforced — i.e. the state LE31 is in today for its other eight foreign keys. **That is a known condition, not a regression**, and it is the reason 427 must land first.

## Sign-off gap

**Two owner decisions are open. Neither blocks the fix; both are recorded so the next pass does not re-open them.**

1. **Should `ref_order_item_id` become NOT NULL for `reason='sale'` rows specifically?** A `CHECK` constraint of the form `CHECK (reason <> 'sale' OR ref_order_item_id IS NOT NULL)` would enforce the pairing. **Recorded default: defer** — it is a different mechanism, it belongs with feature 404's `CHECK`-constraint work, and the foreign key alone already removes the dangerous case (a *dangling* reference). **Not decided.**
2. **What should happen to a sale whose order line was legitimately deleted?** §3.2 has no "void an order line" concept and the append-only rule applies to the *ledger*, not to `OrderItem`. **Recorded default: `OrderItem` rows are not deleted in v1**, so the question is theoretical today. If voiding is ever added it needs `ON DELETE` semantics — **not decided here.**
3. **Should the foreign key be indexed?** **Recorded default: no.** `batch_id` carries `index=True`; `ref_order_item_id` does not. The lookup direction that matters (`batch_id` → ledger rows) is already indexed, and there is no read path yet to justify a second index.

**The agent must not widen any of these decisions.** If the schema seems to require a different answer, that is a **finding to surface**, not a choice to make.

## Handoff summary

`StockEntry.ref_order_item_id` is declared as a bare `int | None = None` in LE31's own `backend/app/models.py` — **no foreign key**, while its sibling `batch_id` has one. The parent proved the consequence by **executing against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file): a `StockEntry` naming `order_item 999999` — which does not exist — was **ACCEPTED and STORED**, and LE31's own ledger derivation (`SUM(qty_delta) WHERE batch_id = X`) was **completely unaffected**, because a wrong *reference* is not a wrong *value*. The corruption is **absorbed**.

That is the shape this audit instrument calls a **corruption sink**: the system's own derivation returns a plausible business number rather than an error, and there is no ground truth to audit against. It matters more here than elsewhere because the charter's §4.3 makes the ledger **append-only with no `UPDATE` and no `DELETE` path** — so write-time validation is the only validation the ledger will ever get, and a dangling reference, once written, is **permanent**.

**And the corpus already knew the column was unconstrained — but nobody owned it.** Feature 404's deferral note says `ref_order_item_id` "is feature 385's subject"; feature 385's Goal is *"one nullable foreign key on `OrderItem`"* — the forward pointer — and never constrains the back-pointer. The chain was **404 → 385 → (nothing)**. Feature 417 covered the *actor* field (`by_user_id`) and was literally right to call it "the only actor field without a foreign key" — `ref_order_item_id` is a *reference* field, so 417's title is true and its scope is correct, and **the second unconstrained column fell between two features that each believed the other owned it.**

**The fix is one line**, the regression test is three assertions, and the risk of not fixing it grows with every feature that touches the ledger. The third-party instrument (`Raktim94/nodedr-restaurant-pos`, AGPL-3.0, off-stack — **vocabulary only, no code adopted**) supplies the discipline this fix embodies: *why Postgres over the originally-specced SQLite* is a question worth writing down, and the dialect answer is not the same on both sides.
