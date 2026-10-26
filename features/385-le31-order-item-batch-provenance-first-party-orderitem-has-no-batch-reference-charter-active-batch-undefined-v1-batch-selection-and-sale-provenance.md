# Feature 385 — `OrderItem` records no batch provenance: the charter's "active batch" is undefined and the sale cannot be traced back to the batch it consumed

> **NEW observation (2026-10-26).** Surfaced by reading the README of in-window GitHub repo `kodlyft/xpos` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE in principle**, but **TypeScript/Vue on Frappe+ERPNext ✗ OFF-STACK** for LE31's Python 3.13 / FastAPI / SQLModel / Postgres stack), **★51/⑂44**, **9,316 KB**, `default_branch=main`, `archived=false`, created **2026-02-26T00:00:00Z** and pushed **2026-10-25T00:00:00Z** = **in-window by `pushed_at` ONLY** (created 7 months before the 2026-09-26..2026-10-26 window start — **this is not a fresh discovery**). All field values read from a **direct `/repos/` GET** by the parent on 2026-10-26, never from search-result numbers. Description (verbatim from GitHub API): *"A lightweight, fast, and advanced POS for ERPNext"*.
>
> Bucket: **v1 (stock-deduction provenance — the third first-party defect of the series)** — Pick A of Daily Brainstorm 2026-10-26. Build verdict: **`build`** (first-party fix: one nullable FK column + one decision record + one regression test).

## Goal

Make LE31 able to answer, from the **order side** alone, the question the charter's own acceptance criterion asks:

> *"Manual test: order a tiramisu → stock goes 8 → 7 → ledger has one entry."* — `PROJECT_CHARTER.md` §2, P0 row.

Today LE31 can answer that question **only backwards**, by finding the `StockEntry` row that points back at the order item. It cannot answer it forwards: **nothing on the order records which batch was consumed.**

The fix is one nullable foreign key on `OrderItem`, one written-down rule for choosing the batch when more than one is active, and one regression test that the two agree.

## Scope

**In scope (v1):**
- Add `OrderItem.batch_id: int | None` (FK to `batch.id`) — the batch this line was drawn from.
- Write down the **batch-selection rule** as a decided rule (not an open question) in the charter §4.3 vicinity, so "its active batch" stops being an undefined phrase.
- One regression test that ties the two facts together: the batch named on the order line is the batch the ledger entry hit.
- A **forward-pointer line** in the existing `StockEntry` write path description (feature 03) noting that the sale and the order line must name the same batch.

## Out of scope (v1)

- **Any `StockEntry` write path, selling endpoint, inventory router, `/sold_out` command, or Telegram alert.** None of those exist yet (`backend/app/routers/` holds only `__init__.py` and `tables.py`; `backend/app/services/` does not exist). This feature changes the **schema shape** and the **written rule**, not the runtime behaviour of a selling flow that does not yet exist.
- **Removing `Batch.qty_remaining`.** That is **feature 374** (`le31-qty-remaining-derived-not-stored`), still open. This feature does not touch it and must not be bundled with it — two different defects with two different failure modes.
- **The `qty_start` vs `initial`-entry opening-balance question.** Also feature 374's open question. **Not resolved here.**
- **The oversell / shortfall / negative-stock policy.** That is feature 373's open question and today's research cron's pick (`dc-tech-inc/dotnet-pos-integration`, feature 382). **Not resolved here.**
- **Any `Option` / `Modifier` / `Variant` model.** See feature 386 and feature 387 — the option concept is a separate gap with a separate pick.
- **Any change to `Batch`, `MenuItem`, `Visit`, `Bill`, `Shift`, or `DerivedTip`.**
- **Alembic.** §3.2's stated v1 policy is `init_db()`. Follow it and record the prod-migration step as known debt.
- **A backfill of existing rows.** There is no selling path, so no `OrderItem` rows exist to backfill.

## Description

### The defect, as observed in LE31's own code on 2026-10-26

Parent-verified, all re-runnable:

1. `backend/app/models.py` — `class OrderItem` (line 142) declares:
   `id, visit_id, menu_item_id, qty, unit_price, course, status, notes, fired_at, ready_at, served_at`.
   **There is no `batch_id`.** `grep -n "batch" backend/app/models.py` returns the `batch` table, the `batch_id` column on `StockEntry` (line 121) and the docstring on line 116 — **and nothing on `OrderItem`.**
2. `backend/app/models.py` — `class StockEntry` (line 113) has **both** `batch_id` (line 121) **and** `ref_order_item_id` (line 124). The ledger records which batch it hit *and* which order line caused it.
3. **The link is therefore one-directional.** `StockEntry → (batch_id, ref_order_item_id)` is a full cross-reference. `OrderItem → batch` **does not exist**. The only way to learn which batch a sale consumed is to scan the ledger for the row whose `ref_order_item_id` matches — which is a *backwards* lookup, and it silently yields nothing if the ledger row is absent, is mis-linked, or if the sale was recorded against a batch that a later restock superseded.
4. **"Active batch" is used five times and defined zero times.** `grep -rn "active batch" --include=*.py --include=*.md` (excluding `features/` and `specs/`) returns:
   - `PROJECT_CHARTER.md:45` — *"Selling a prepared item decrements its active batch's `qty_remaining` and writes a `StockEntry(-1, reason='sale')` row."*
   - `PROJECT_CHARTER.md:152` — *"When SUM(qty_delta) ≤ 0 for an active batch: …"*
   - `research/03-inventory-stock.md:40` — *"Look up the menu item → if `is_prepared`, decrement the active batch's …"*
   - `research/13-peer-architecture-comparison.md:141` — *"`SUM(qty_delta)` per active batch — exactly the read pattern the …"*
   - `coding-agent/skills/le31-cook-bot-ux/SKILL.md:65` — *"`/status` shows every active batch in compact form, refreshed on demand."*
   **No file anywhere states what "active" means.** The only candidate rule in the repo is an **open question** in feature 03: *"What happens if two batches of the same item are active (e.g. cook made more tiramisu at 3pm)? Use FIFO — oldest batch consumed first."* — stated in the **Open questions** section of a feature contract, which is where an **undecided** thing goes.
5. **No existing feature records the batch on the sale.** `grep -rn "record.*batch\|which batch was\|sold.*batch" features/03-*.md features/26-*.md features/34-*.md` returns **no matches**. Feature 34 defers to feature 03's FIFO rule; feature 03's FIFO rule is an open question; nothing anywhere adds a batch reference to the order line.

### Why an external artifact was the trigger

`kodlyft/xpos` is an ERPNext/Frappe POS. Its README, read raw by the parent on 2026-10-26, states under **Inventory & Purchasing**:

> *"**Batch & serial tracking** – Select specific batch/serial numbers during sale or return"*
> *"**Real-time stock display** – Actual quantities per warehouse"*

A POS that lets the operator **select which batch** at the moment of sale is a POS that has had to answer the question *"what if there are two batches?"* — and has answered it **in the data model**, not in a comment. That is what made the parent go and read LE31's own `models.py` for the third time in three passes.

**This is the third time in three passes that an external README produced a first-party finding** (after `ramaraihan12/warung-pos` → feature 374, and `sajeercherukottayil/Ordova` → feature 379). The pattern is stable enough to name as a method: *when an external artifact states an invariant LE31 claims to hold, check whether LE31's own implementation holds it, and file what you find.* Ninety citations had not found the `qty_remaining` defect; a `grep` and ninety seconds did.

### Why this matters more than the `qty_remaining` defect

Feature 374's defect is **inert**: a stored column nothing maintains. This one is worse, because **the design rule it violates is the rule the feature pipeline is about to write code against.**

The moment a selling path lands, it must answer "which batch?" — and it will answer it **by whatever the implementer happened to assume**. The plausible wrong assumption is the quiet one: *"there is only one active batch per item today, so the batch is unambiguous."* That assumption is **true today and will not stay true**: the moment the cook makes more tiramisu at 3pm, there are two, and the sale silently picks one.

The consequence is not a crash. It is that **the ledger and the order disagree and nobody can tell which is right.** A stock number that is wrong by one tiramisu is a number the owner will never audit, because the ledger looks perfectly well-formed: it has a `batch_id` and a `ref_order_item_id`, both non-null, both pointing at real rows.

**The asymmetry is the argument.** Today: one column, one rule, one test. After the first selling feature lands and a second batch becomes possible: a **historical audit** — every sale ever made against the wrong batch, with no way to tell which ones — plus a **silent** corruption, because the ledger's own structure looks intact. Cheap now, expensive after.

## Data model

**One column added to `OrderItem`:**

```python
class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"

    id: int | None = Field(default=None, primary_key=True)
    visit_id: int = Field(foreign_key="visit.id", index=True)
    menu_item_id: int = Field(foreign_key="menu_item.id")
    batch_id: int | None = Field(default=None, foreign_key="batch.id", index=True)
    # ^^^ NEW: the batch this line was drawn from. Nullable because
    #     (a) non-prepared items (`is_prepared=False`) have no batch, and
    #     (b) existing rows predate this feature.
    qty: int = 1
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    # ... unchanged ...
```

**Nothing else changes.** No new table. No new column on `StockEntry` (it already has both references). No change to `Batch`, `MenuItem`, `Visit`, `Bill`, `Shift`, `DerivedTip`.

**Migration:** per §3.2's stated v1 policy, `init_db()` — **not** Alembic. `backend/requirements.txt` already pins `alembic>=1.13`, so this is the moment the §3.2 inconsistency becomes live; record the prod-migration step as known debt rather than silently introducing Alembic.

## Implementation steps

1. **Write the rule down first, then encode it.** Add to `PROJECT_CHARTER.md` §4.3 a short paragraph stating the batch-selection rule as a **decided** rule. Recommended wording (the implementer may refine the prose but must not leave it undecided):

   > *When a prepared menu item has more than one open batch, the sale is drawn from the **oldest open batch first** (FIFO by `prepared_at`). The batch consumed is recorded on the order line (`OrderItem.batch_id`) and named by the ledger entry (`StockEntry.batch_id`); the two must agree. A line whose item is not prepared carries no batch.*

   **Why FIFO and not "newest" or "let the operator choose":** FIFO needs no operator input, which matters on a hands-busy surface (§3.1); it is deterministic, so the same inputs always produce the same ledger; and it needs no new UI. **Operator-chosen batch selection is explicitly out of scope for v1** — `xpos` offers it, but a choice presented to a waiter mid-service is a §3.1 surface question, and LE31's waiter surface is already minimal.

2. **Add the column.** `backend/app/models.py` → `class OrderItem` → one line, as above.

3. **Add the regression test.** `tests/test_order_item_batch_provenance.py`. The load-bearing assertions:
   - **The order line names a batch, and it is the batch the ledger hit.** Create a batch, record a sale, assert `order_item.batch_id == stock_entry.batch_id`.
   - **The link is not decorative.** Assert that changing the order line's `batch_id` to a *different* batch makes the test fail — i.e. the test is actually comparing the two, not just checking non-null.
   - **A non-prepared item carries no batch** and `batch_id` is `None`.
   - **The nullable column is nullable** — a row created without `batch_id` persists and reads back `None` (this is the backward-compatibility guard; `Nullable` columns that are accidentally `NOT NULL` are a classic silent migration failure).

4. **Forward-pointers.** Add one line each to `features/03-kitchen-stock-tracker.md`, `features/26-reorder-point-on-stockentry.md` and `features/34-stockout-prep-board-snapshot.md` noting that the sale's `StockEntry` must name the **same batch** as the order line's `batch_id`. **Do not otherwise edit those contracts.**

5. **Record the decision where it will be found.** The charter paragraph from step 1, plus a pointer to this feature in §4.3.

## Telegram interaction if any

**None.** The cook bot's `/status` command already reads "every active batch" (`coding-agent/skills/le31-cook-bot-ux/SKILL.md:65`). This feature adds **no** command, **no** output, and **no** prompt. It changes what a stored fact *is*, not what anyone sees.

**This is deliberate and is the point.** Feature 379 (the `OrderItem` actor defect) needed a transition-history table and a write path; this one needs a column and a rule. Both are inert until the selling path lands. **That inertness is the argument for doing them now** — see "Why this matters".

## Dependencies

- **Feature 374** (`le31-qty-remaining-derived-not-stored`) — **the load-bearing sibling.** It removes `Batch.qty_remaining` and derives it from the ledger. This feature does **not** depend on it and does not wait for it, but the two must land in a compatible order: 374 changes how *stock* is derived, this changes *which batch* a sale names. A sale names a batch; a batch has a derived remaining. These compose cleanly. **If 374 lands first, `StockEntry.batch_id` becomes even more load-bearing — it is then the only place the batch identity lives.** Do not let 374's implementer delete `StockEntry.batch_id` under a "the sum is all we need" reading; the sum is per-batch and the batch identity is what links a sale to it.
- **Feature 379** (`le31-order-item-transition-actor-attribution`) — **the sibling defect on the same table.** 379 adds a `by_user_id` to `OrderItem` and an `OrderItemTransition` table. This feature adds a `batch_id` to `OrderItem`. **Both touch the same class; both must be re-read before the second one lands.** They do not conflict — one records *who*, the other records *what was consumed*.
- **Feature 03** (`kitchen-stock-tracker`) — owns the `StockEntry` write path and is where the forward-pointer from step 4 goes.
- **Feature 04** (`menu-photo-bot`) — creates the batches this feature's FK points at.
- **Feature 382** (`dc-tech-inc/dotnet-pos-integration`, filed today by the research cron) — owns the **oversell/shortfall** policy. **Explicitly not bundled** with this feature: 382 is about *how much* to deduct when stock is short; this is about *which batch* the deduction came from. **They are different questions and must not be answered in one PR.**

## Open questions

- **Should `batch_id` be `NOT NULL` for prepared items?** Enforced at the database level it would need a partial-index or a check constraint that knows `menu_item.is_prepared` — which crosses a table. **Recommended: nullable at the DB level, enforced in the service layer** that writes sales, plus the regression test asserting the invariant. **This is the implementer's call and must be recorded in the code.**
- **What if the chosen batch has zero remaining?** That is the oversell question — feature 373's open question and feature 382's subject. **Not answered here.** This feature's job is to *record* the batch, not to decide whether the sale is allowed.
- **Does the waiter ever need to see which batch an order line came from?** Probably not in v1. Recorded as **unknown**, not as "no" — the answer changes if a dish is prepared in two ways (e.g. a base tiramisu and a variant).
- **Should a restock create a new batch or a `restock` entry on the existing one?** §4.3's insert-path list has `restock → qty_delta = +N, reason = 'restock'`, which implies the **same** batch. If a restock instead creates a *new* batch, the FIFO order changes. **Not decided here**; note that this feature's `batch_id` makes the question answerable later, which is itself a point in its favour.

## Why this matters

**LE31's stock number is the product.** An owner's confidence in it is the whole reason to keep using LE31. Today the charter promises a derivation from an append-only ledger, and the ledger — as feature 374 found — is not actually connected to anything. This feature addresses the *second* half of that promise: even once the sum is derived correctly, **the sum is per-batch, and nothing says which batch a given sale hit.**

Without it, three facts are true at once and mutually inconsistent:

1. The ledger says *which batch* was decremented.
2. The order says *what was sold*.
3. Nothing says these are the same event.

Any of the three can be wrong independently, and a reader cannot tell which. Today that is inert. **It stops being inert the moment the first selling feature lands** — and the selling feature is the first thing the v1 pipeline will build.

**And the failure is silent in the worst way.** There is no error, no constraint violation, no crash. A sale is decremented from a valid batch and recorded against a valid order line, and the two are connected only by a convention nobody wrote down. The owner's stock number drifts by one unit, the ledger looks well-formed, and there is no way to find out which sale was wrong.

**That is the whole argument.** The fix is one nullable column, one paragraph, and one test — against a failure that costs a full historical audit once the selling path exists. **Do this one before any selling feature lands.**
