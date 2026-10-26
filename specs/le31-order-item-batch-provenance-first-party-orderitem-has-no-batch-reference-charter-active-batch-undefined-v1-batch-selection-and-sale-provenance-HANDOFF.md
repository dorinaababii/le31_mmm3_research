# HANDOFF — Feature 385: make the order line name the batch it consumed (`OrderItem.batch_id`) and decide what "the active batch" means

**This is the third `build` pick of the 88-pass series, and the third first-party defect found in three passes.** It is a gap in LE31's own code, not a reference to someone else's. **Do not defer it.**

**Discovery chain:** Daily Brainstorm 2026-10-26 → the parent read the README of the in-window repo `kodlyft/xpos` (MIT, ★51), whose Inventory section says *"**Batch & serial tracking** – Select specific batch/serial numbers during sale or return"* — a POS that lets the operator choose the batch at sale time has had to answer *"what if there are two batches?"* in its data model → the parent went and read LE31's own `backend/app/models.py` for the third time in three passes → found that **`OrderItem` has no `batch_id` at all**, while `StockEntry` carries **both** `batch_id` (line 121) and `ref_order_item_id` (line 124) — so the ledger knows which batch it hit and which order line caused it, and **the order line does not know which batch it came from** — and that **"active batch" is used five times across the repo and defined zero times** (the only candidate rule lives in feature 03's *Open questions* section, i.e. it is undecided).

**Full evidence record: `features/385-le31-order-item-batch-provenance-first-party-orderitem-has-no-batch-reference-charter-active-batch-undefined-v1-batch-selection-and-sale-provenance.md`**

## Active feature path

`features/385-le31-order-item-batch-provenance-first-party-orderitem-has-no-batch-reference-charter-active-batch-undefined-v1-batch-selection-and-sale-provenance.md` — **build** (Pick A of Daily Brainstorm 2026-10-26).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When a sale is recorded, the owner wants to be able to trace which batch of stock it consumed, but the order line records no batch and "the active batch" is never defined, so the sale and the stock movement cannot be reconciled from the order side.* The pain is **not inferred** — it is **observable in LE31's own schema**. The charter's own P0 acceptance criterion demands it: *"order a tiramisu → stock goes 8 → 7 → ledger has one entry"* (`PROJECT_CHARTER.md` §2) — a criterion that today can only be checked **backwards**, by scanning the ledger for a row whose `ref_order_item_id` matches. Evidence class: **OBSERVED** — parent-run greps, re-runnable in five commands (below). |
| 2 | Viability | ✓ | Small and wholly internal: one nullable FK column, one written rule, one test file. No third-party dependency, no licence question, no traction question (**the subject is LE31's own code**). |
| 3 | Practicability and confidence | ✓ | On-stack: `backend/app/models.py` is SQLModel; `Batch` and `StockEntry.batch_id` already exist, so there is no new design to invent — only a new column on a class whose sibling columns are right there. **Confidence: high** — the gap is directly observable and the required rule (FIFO) is already stated in feature 03. **Named rabbit hole:** the `qty_start` vs `initial`-entry opening-balance question — see Open questions 3. |
| 4 | Conflict | ✓ | **No conflict — the change restores an existing LE31 invariant and makes a real phrase mean something.** §4.3 already says the sale decrements *"its active batch"*. Today the phrase has no referent. **Adjacent tensions to respect, not to resolve here:** (a) the oversell/shortfall policy is feature 373's open question and feature 382's subject — **this feature does not decide whether the sale is allowed, only which batch it names**; (b) the `qty_start` vs `initial` opening-balance question is feature 374's — **not bundled**; (c) "operator chooses the batch" (as `xpos` does) would be a §3.1 surface question — **out of scope, FIFO instead**. |
| 5 | Outcome + appetite + scope | ✓ | Maps to a v1 correctness fix. Maximum time worth spending: **2–4 hours including the column, the charter paragraph and the regression test.** Scope is deliberately: one column, one paragraph, one test file. **Explicitly NOT in scope:** removing `Batch.qty_remaining` (feature 374), any `StockEntry` write path, any selling endpoint, any inventory router, any `/sold_out` command, any Telegram command, any `Option` model (features 386/387). |
| 6 | Cost to operational value | ✓ | High, and **the value rises with time.** Value today: the sale and the stock movement are provably the same event. Value in six months if deferred: **a silent historical mis-attribution** — see the gate's circuit-breaker note, this is the sharpest asymmetry of the three first-party defects. Features 03, 04, 26, 34 and 45 all plan to write to `Batch`/`StockEntry`; the selling path is the first thing v1 will build. Cost: under half a day, no new surface, no new dependency. |
| 7 | Circuit breaker + reversibility | ✓ | **Fully reversible: drop the column.** No existing data is affected, because no code writes `OrderItem` rows today (parent-verified). **The only irreversible part is if a selling path lands first** — the batch each historical sale consumed **cannot be reconstructed retroactively**, because the information was never written. **That is exactly why this is `build` and not `defer`.** **Stop evidence:** if the pre-flight below shows `OrderItem` already has a batch reference, **stop and re-read the contract.** **Review point:** after the first real sale is recorded, confirm `order_item.batch_id == stock_entry.batch_id` for that line — the mismatch is the whole failure mode this feature prevents. |

**Gate verdict: `build`** — check 1 passes on **observed** evidence, the same standard the 85th-pass first-party pick (feature 374) established.

## Bucket

**v1 (stock-deduction provenance — a core operational-correctness invariant)** — Pick A of Daily Brainstorm 2026-10-26. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — the parent confirmed on 2026-10-26 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that `le31 v2 owner-pains` / `le31 v2-AI` do **not** exist. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — 39th consecutive day), the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload, and that is the only project that exists for the write.

## Files to touch

**The change itself (ordered — the rule must be written down before the column is added, so the column has a defined meaning):**

- `PROJECT_CHARTER.md` — **ADD** a short paragraph to **§4.3** stating the batch-selection rule as a **decided** rule: oldest open batch first (FIFO by `prepared_at`); the batch consumed is recorded on the order line (`OrderItem.batch_id`) and named by the ledger entry (`StockEntry.batch_id`); the two must agree; a line whose item is not prepared carries no batch. **Read §4.3 first — do not paraphrase the existing insert-path list, extend it.** Also add a pointer to this feature. **Do not renumber or restructure §4.3.**
- `backend/app/models.py` — **ADD** `batch_id: int | None = Field(default=None, foreign_key="batch.id", index=True)` to `class OrderItem` (line 142), immediately after `menu_item_id`. **DO NOT** change `Batch`, `MenuItem`, `StockEntry`, `Visit`, `Bill`, `Shift`, `DerivedTip`, `ItemStatus` or any timestamp field. **DO NOT** touch `Batch.qty_remaining` — that is feature 374.
- `tests/test_order_item_batch_provenance.py` — **NEW.** The load-bearing tests (below).
- `features/03-kitchen-stock-tracker.md`, `features/26-reorder-point-on-stockentry.md`, `features/34-stockout-prep-board-snapshot.md` — **ADD one line each**, noting that the sale's `StockEntry` must name the **same batch** as the order line's `batch_id`. **Do not otherwise edit these contracts.**

**Do NOT touch (out of scope, explicitly):**

- `backend/app/routers/` — **do not add an orders router, a selling endpoint, or an inventory endpoint.** No selling path is in scope (`backend/app/routers/` holds only `__init__.py` and `tables.py`).
- `backend/app/services/` — **do not create it.** This feature adds no service function; the write path does not exist yet and inventing one is feature 03's job. **If you find yourself wanting to create a service layer, stop — that is scope creep.**
- `backend/app/bot/cook_bot.py` — **no new command, no new output.** The `/status` command already reads active batches.
- `backend/app/db.py` — **verify** that `init_db()` creates the altered table via SQLModel `create_all`; **do not assume.** Per §3.2, v1 uses `init_db()`, not Alembic; `backend/requirements.txt` already pins `alembic>=1.13` but **do not silently introduce Alembic** — follow §3.2's stated v1 policy and record the prod-migration step as known debt.
- `backend/requirements.txt` — **no dependency change.**
- Any `Option` / `Modifier` / `Variant` model — features 386 and 387.
- `Batch.qty_remaining` — feature 374.

## The load-bearing tests

`tests/test_order_item_batch_provenance.py` must contain, at minimum:

1. **The order line names a batch, and it is the batch the ledger hit** — create a batch, record a sale, assert `order_item.batch_id == stock_entry.batch_id`. **This is the test that makes the defect impossible to reintroduce silently.**
2. **The link is not decorative** — assert that pointing the order line's `batch_id` at a *different* batch makes the test fail. Without this, a test that only asserts non-null would pass against a broken implementation.
3. **A non-prepared item carries no batch** — `batch_id` is `None` for an item with `is_prepared=False`.
4. **The column is genuinely nullable** — a row created without `batch_id` persists and reads back `None`. **This is the backward-compatibility guard**: a nullable column accidentally declared `NOT NULL` is a classic silent migration failure that only shows up in production.
5. **The FK is enforced** — a `batch_id` pointing at a non-existent batch must be rejected (or must fail the test's insert). Do not rely on SQLModel alone to give you this.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. The observable behaviour here is **a number that can be reconciled in a running system**: record a sale, then read the order line and the ledger row and confirm they name the same batch.

**The pre-flight that must be re-run before starting (parent-run on 2026-10-26; re-run it — the answer is the whole point of this feature):**

```bash
cd /opt/data/le31_mmm3_research_work
sed -n '/^class OrderItem/,/^class Bill/p' backend/app/models.py
# expect: NO batch_id, NO batch reference of any kind
grep -n "batch" backend/app/models.py
# expect: the batch table, StockEntry.batch_id (line 121), the StockEntry docstring — and NOTHING on OrderItem
grep -rn "active batch\|active_batch" --include=*.py --include=*.md . | grep -v "^./features/\|^./specs/"
# expect: 5 hits (PROJECT_CHARTER.md:45, PROJECT_CHARTER.md:152, research/03-inventory-stock.md:40,
#         research/13-peer-architecture-comparison.md:141, coding-agent/skills/le31-cook-bot-ux/SKILL.md:65)
#         — five USES and zero DEFINITIONS
grep -rn "record.*batch\|which batch was\|sold.*batch" features/03-*.md features/26-*.md features/34-*.md
# expect: NO output — no existing feature records the batch on the sale
ls backend/app/services/ backend/app/routers/
# expect: services/ DOES NOT EXIST; routers/ holds only __init__.py and tables.py
```

If the second command now shows a batch reference on `OrderItem`, **the gap has already been closed by someone else — stop and re-read the feature contract before implementing.**

**Post-implementation, the same commands must show: a `batch_id` on `OrderItem`; the charter §4.3 paragraph; and the fourth grep still returning no output** (no existing feature records the batch on the sale — that is what the forward-pointers are for). That inversion is the proof of the change.

**The four-command "stock goes 8 → 7" rehearsal** — the charter's own acceptance criterion, runnable against a real database, not a mocked one: create a batch, insert `initial +8`, `sale -1`, `sale -1`, `waste -2`, read back `4`, and confirm the `sale` entries' `batch_id` equals the order line's `batch_id`. **Do this in a running system, not only in a unit test.**

## Rollback path

`git revert` the commit, or drop the column and the charter paragraph. **No existing data is affected on revert**, because no code writes `OrderItem` rows today (parent-verified). If a selling path lands before this feature, the rollback becomes an impossible backfill — **the batch each historical sale consumed was never written, and it cannot be recovered** — which is the entire reason this is `build` and not `defer`.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *State* rule first, then *Data*) **— this is the invariant being restored**
- `le31-data` — append-only rules and the derive-never-store discipline (the reason `StockEntry` is the source of truth and `OrderItem.batch_id` is a *pointer*, not a second copy of the quantity)
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants (§3.2 migrations via `init_db()`, §4.2 schema overview, §4.3 the killer pattern — **the paragraph you add goes here**)

## Open questions carried into any future build

1. **Should `batch_id` be `NOT NULL` for prepared items?** Enforced at the database level it would need a partial index or a check constraint that knows `menu_item.is_prepared` — which crosses a table. **Recommended: nullable at the DB level, enforced in the layer that writes sales, plus the regression test asserting the invariant.** The parent has not decided; the implementer should pick and **record the choice in the code**.
2. **What if the chosen batch has zero remaining?** That is the oversell/shortfall question — feature 373's open question and feature 382's subject. **Not answered here.** This feature's job is to *record* the batch, not to decide whether the sale is allowed.
3. **The `qty_start` vs `initial`-entry opening-balance question.** Feature 374's open question: is the opening balance a column (`qty_start`) or the `initial` `StockEntry`? **§4.3's own insert-path wording points at the `initial` entry.** **Do not resolve it here** — but note that this feature's `batch_id` makes it *answerable* later, which is itself a point in the feature's favour.
4. **Does the waiter ever need to see which batch an order line came from?** Probably not in v1. **Recorded as unknown**, not as "no" — the answer changes if a dish is prepared in two ways (a base tiramisu and a variant).
5. **Should a restock create a new batch or a `restock` entry on the existing one?** §4.3's insert-path list has `restock → qty_delta = +N, reason = 'restock'`, which implies the **same** batch. If a restock instead creates a *new* batch, the FIFO order changes. **Not decided here.**
6. **Does this interact with Feature 379?** Both add a column to `OrderItem` — 379 adds `by_user_id` (and a transition table), this adds `batch_id`. **They do not conflict** (one records *who*, the other records *what was consumed*), but **both touch the same class, so the second one to land must re-read the file.**
