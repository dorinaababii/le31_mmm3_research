# Feature 374 — Derive `Batch.qty_remaining` from `StockEntry` (charter §4.3 says "computed on read, not stored"; the schema stores it) (build — v1)

> **NEW observation (2026-10-24, parent-verified first-party).** This is **not** a third-party reference. It is a **contradiction inside LE31's own repository**, found by the parent while reading an external project's README during the Daily Brainstorm 2026-10-24 pass (see Feature 373, `ramaraihan12/warung-pos`, whose README states *"Stock is never a stored number"*). LE31's `PROJECT_CHARTER.md` §4.3 and the `StockEntry` docstring both state the same rule — and `backend/app/models.py` **does not obey it**.
>
> **The evidence, all parent-run on 2026-10-24 (commands and outputs in the HANDOFF, and re-runnable):**
> 1. `backend/app/models.py:106` — `qty_remaining: int` is a **persisted column** on `class Batch(SQLModel, table=True)`. It is declared exactly like `qty_start: int` on line 105. It is not a computed field, not a `@property`, not a hybrid.
> 2. `grep -rn "qty_remaining" . --include=*.py --include=*.html --include=*.md --include=*.sql` across the whole repository returns **exactly one code hit** — the declaration itself. There is **no derivation site, no read path, no writer, and no test** anywhere in the codebase.
> 3. `backend/app/services/` **does not exist** (`backend/app/` contains only `__init__.py`, `bot/`, `config.py`, `db.py`, `main.py`, `models.py`, `routers/`). The directory the Spoolman HANDOFF (feature 371) refers to as `backend/services/stock_service.py` — and therefore where a derivation would naturally live — has never been created.
> 4. `backend/app/routers/` contains **only** `__init__.py` and `tables.py`. There is no `inventory` router. No code path currently sells an item or decrements a batch.
> 5. **Four prior feature contracts describe the derivation as if it exists**: feature 26 (`"qty_remaining still derived from StockEntry"`), feature 34 (`"qty_remaining = SUM(stock_entry.qty_delta) per active_batch"`), feature 371 (`"batch.qty_remaining already *is* the derived projection"`), feature 372 (`"the same derive-never-store discipline as batch.qty_remaining"`). Features 34 and 371 also both name `backend/services/stock_service.py` as a file to touch — **a file that does not exist.**
> 6. `PROJECT_CHARTER.md` §4.3 — *"EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE. `batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)` — computed on read, not stored."*
> 7. `backend/app/models.py:113-118` — the `StockEntry` docstring repeats it: *"Append-only ledger. Never UPDATE or DELETE rows. Current stock for a batch = SUM(qty_delta) WHERE batch_id = X."*
>
> **The contradiction is between the specification and the schema, not between the specification and itself.** LE31 has been describing a derivation in prose for 87 passes without anyone checking whether the code had it. Because no selling path exists yet, the defect is **currently harmless** — but it is exactly the kind of defect that gets *frozen in* by the first feature that writes to `qty_remaining`, and features 03, 04, 26, 34 and 45 all plan to do exactly that.
>
> Bucket: **v1 (correctness of the core stock invariant)** — Pick B of Daily Brainstorm 2026-10-24. Build verdict: **`build`** — this is the only pick of the 87-pass series that is not a vocabulary reference. **Evidence class: OBSERVED** — every claim below was produced by a command the parent ran on 2026-10-24, and each is re-runnable in four commands (listed in the HANDOFF). This is the first pick of the series whose gate check 1 does not rest on an inference.

## Goal

Make `backend/app/models.py` obey `PROJECT_CHARTER.md` §4.3 by **removing the persisted `Batch.qty_remaining` column** and replacing every read of it with a **single, tested derivation** over the append-only `StockEntry` ledger.

**The invariant being restored:** current stock for a batch = `SUM(stock_entry.qty_delta WHERE batch_id = X)`, computed on read, never stored. One ledger, one source of truth, no second copy to drift.

**This is a correction, not a feature.** LE31 is not gaining a capability. LE31 is removing a way for its stock number to be wrong.

## Scope

**In scope (v1):**

- **Drop `Batch.qty_remaining` from the schema** and add a single derivation helper that computes it from `StockEntry`.
- **Audit every existing reader of `qty_remaining` and route it through the helper.** Parent-verified: there are currently **no code readers** — the only hits are the column declaration and prose in charter/research/feature files. So the audit surface is small *today*; the helper must exist before the first selling path lands.
- **A derivation service** at the path the existing HANDOFFs already name: `backend/app/services/stock_service.py` (the directory does not exist and must be created).
- **A test that fails if the column ever comes back** and a test that proves the derivation equals the ledger sum.
- **A migration** for the existing dev/prod databases, if any exist.

**Out of scope (v1):**

- **Any selling, ordering, or stock-movement write path.** LE31 has no router that sells an item today (§4.3's *Insert paths* are specified but not implemented). This feature makes the schema honest; it does not implement the flows.
- **The `sold_out` marking behaviour** in §4.3 (*"Mark menu_item as sold_out… Hide from waiter UI… Send Telegram alert to cook"*). That is a separate feature and it depends on this one being correct first.
- **Multi-location, multi-tenant, reservations, online ordering** — §3.2.
- **Any change to `StockEntry` itself.** It is already append-only by construction and its docstring is already correct.
- **`StockReason` extension** — no new reasons.
- **Caching.** The derivation is a `SUM` over an indexed `batch_id`; caching it would re-introduce a second copy. **No cache.** If it is later shown to be slow, the fix is an index, not a column.

## Description

LE31's charter §4.3 is unusually good. It names the killer pattern precisely: every change to batch stock is a new `StockEntry` row, never an update or a delete, and the current quantity is a *computation* over those rows. The `StockEntry` model carries the same sentence in its docstring. This is the right design, and it is the design the "append-only" name promises.

**The schema does not implement it.** `Batch` carries a persisted `qty_remaining: int` sitting next to `qty_start: int` — a plain column on a `table=True` SQLModel class, which means a real column in the real table. Nothing computes it, nothing writes it, nothing reads it. It is currently an inert, always-default-valued field. The reason this has gone unnoticed for 87 passes is that **no code path has ever moved stock**: with no selling router, no prep flow, and no `StockEntry` writer, there is nothing to be wrong *about* yet.

That is exactly why this has to be fixed now rather than later. Four prior contracts — features 03, 04, 26, 34, 45 — plan to write to this field. The moment the first of them lands, the schema will contain two representations of the same fact: the ledger (correct, append-only) and a mutable column (a cache with no invalidation strategy). From that moment on, "stock" has two answers, and the wrong one is the one a reader is likelier to trust, because it is a column.

**Why an external README is what surfaced this.** LE31's own prose had been internally consistent for 87 passes — the charter, the docstring and the feature contracts all agreed with each other, because they were all written from the same source. The contradiction only becomes visible against something external. Reading `ramaraihan12/warung-pos`'s README — a stranger's project that states *"Stock is never a stored number"* as a design decision, and separately states *"A sale is never refused for lack of stock"* and *"Money is integer rupiah everywhere… a guard that throws on a fractional value"* — made the parent go and read LE31's own `models.py` instead of another README. It found the column. **The external reference did not tell LE31 it was wrong; it told LE31 to go and check.** That is the reusable lesson of this pass and it is written up as Feature 373.

**The second, smaller finding, recorded here so it is not lost:** LE31's money fields are `Decimal = Field(max_digits=10, decimal_places=2)` — correct in type, but a `Decimal` write with a third decimal place will be *rounded*, not rejected, and `max_digits`/`decimal_places` in SQLModel/Pydantic constrain the *column*, not necessarily the *validator*. There is no guard that raises on a fractional value. The upstream reference has one. **That is a separate, smaller change and is not bundled into this feature** — it is recorded as an open question in Feature 373 and is filed here only as an adjacent observation.

## Data model

**Change to one table. One column removed. No table added.**

```
Batch (existing) — REMOVE the column:
    qty_remaining: int        # persisted today — violates §4.3

Batch (existing) — KEEP unchanged:
    id, menu_item_id, qty_start, prepared_at, expires_at, photo_url, notes

StockEntry (existing) — KEEP unchanged. Already append-only by construction:
    id, batch_id (indexed), qty_delta, reason, ref_order_item_id, by_user_id, at
```

**The derived quantity is not a column.** It is a value, computed by a helper:

```
batch.qty_remaining  →  SUM(stock_entry.qty_delta WHERE stock_entry.batch_id = X)
```

**Migration shape.** Because no code writes `qty_remaining` today, the migration is a **column drop, not a backfill** — there is no data to preserve in that column (it holds either a default or a value no code has ever read). The correct migration is therefore:

1. Create `backend/app/services/stock_service.py` with the derivation helper.
2. Add the test that asserts the column is absent.
3. Drop the column.

**Order matters.** The helper and the test come *first*; the drop comes last. Dropping first would leave a window where a reader expecting the column gets an `AttributeError` with no replacement in place. (The same ordering rule — *make the replacement exist before removing the thing it replaces* — is the discipline that makes this reversible and reviewable.)

**⚠️ The `qty_start` question is deliberately left open.** `qty_start` is also a persisted number, and it is *not* derivable from the ledger in the same way — it is the opening balance of a batch. Two defensible designs: (a) keep `qty_start` as a column and derive `remaining = qty_start + SUM(delta)`; (b) make the `initial` `StockEntry` row (reason=`'initial'`, `qty_delta=+N`) the sole source of the opening balance, exactly as §4.3's insert-path list already describes (*"Morning prep → qty_delta = +N, reason = 'initial' (one row per batch)"*) — in which case `qty_start` becomes a **duplicate** of that first entry and is also droppable. **§4.3's own insert-path wording already implies (b).** This feature implements (b) *only if* it is cheap; otherwise (a) with `qty_start` retained, and the choice is recorded in the code and the HANDOFF. **Either way, exactly one representation of the opening balance must survive.**

## Implementation steps

1. **Create `backend/app/services/__init__.py` and `backend/app/services/stock_service.py`.** One public function, e.g. `remaining_for_batch(session, batch_id) -> int`, returning `SUM(qty_delta)`. No caching, no ORM-attribute assignment, no write path.
2. **Add `tests/test_stock_derivation.py`** with, at minimum:
   - a test that the derivation equals the sum of `StockEntry.qty_delta` for that batch;
   - a test that inserting a `StockEntry` **changes** the derived value (proving it is derived, not cached);
   - a test that **`Batch` has no `qty_remaining` attribute / the `batch` table has no `qty_remaining` column** — this is the regression test that makes the defect impossible to reintroduce silently;
   - a test that the `initial` entry alone yields the opening balance (if design (b) is taken).
3. **Migrate** the `batch` table to drop `qty_remaining` (and `qty_start`, if design (b)). LE31 v1 uses `init_db()` rather than Alembic (§3.2: *"Alembic migrations (we use `init_db()` for v1; switch to Alembic before prod)"*), and `backend/requirements.txt` already pins `alembic>=1.13` — so this is the moment the §3.2 inconsistency becomes live. **Follow §3.2's stated v1 policy: update `init_db()` and the model, and record the prod-migration step as a known debt.** Do not silently introduce Alembic.
4. **Update the four contracts that assert the derivation already exists** (features 26, 34, 371, 372) so they no longer describe a helper that was never there. **Do not rewrite their history** — add a one-line forward-pointer to this feature.
5. **Update `PROJECT_CHARTER.md` §4.3** to point at the derivation helper by path, so the charter names the code that implements it. (The charter text is already correct; it just needs a pointer.)
6. **Add the regression test to the guard set** so a future PR that reintroduces a stored quantity fails CI, not review.

**Do NOT** add an `inventory` router, a selling endpoint, a `/sold_out` command, a `StockEntry` write path, or a Telegram alert. Those are separate features and they depend on this one.

## Telegram interaction if any

None today. This feature touches no bot command. The §4.3 behaviour it enables (*"Send Telegram alert to cook (one-shot, not on every order attempt)"*) belongs to the `sold_out` feature, not to this one. **Note the dependency explicitly in the HANDOFF: any future `sold_out` implementation must call the derivation helper and must not read a column.**

## Dependencies

- **No new packages.** Uses only SQLModel/SQLAlchemy already in `backend/requirements.txt`.
- **No new surfaces.** §3.1's two roles are unaffected.
- **No new infrastructure.** Single VPS + systemd unit (§3.2) is unaffected.
- **Migration tooling**: `init_db()` per §3.2's v1 policy. (`alembic>=1.13` is already a dependency but §3.2 defers it — see step 3.)
- **Blocker for downstream features:** features 03, 04, 26, 34, 45 all assume a writable `qty_remaining`. **This feature must land before any of them writes to it**, or they must be updated to use the helper.

## Open questions

1. **Design (a) or (b) for the opening balance?** Keep `qty_start` as a column and derive `remaining = qty_start + SUM(delta)`, or make the `initial` `StockEntry` the sole opening-balance source and drop `qty_start` too? §4.3's insert-path wording points at (b); (b) is cleaner but touches one more column. **The parent has not decided; the implementer should pick (b) if it lands without schema surprise, and record the choice in the code.**
2. **Is the derivation cheap enough at LE31's scale?** LE31's domain is one restaurant, one kitchen, a few hundred entries a day (§4.3's insert paths). A `SUM` over an indexed `batch_id` is trivially cheap. **This is a non-question at LE31's scale and should not be used to justify a cached column.** Answered for the record: yes, it is cheap enough.
3. **Should `qty_remaining` remain as a *read-only* property for convenience?** A `@property` on the model that queries would be a second, subtler trap (it hides a query inside attribute access and can go stale within a session). **Recommendation: no — the helper is the only accessor.** Unmade, but the recommendation is strong.
4. **Does the fractional-money guard belong here?** No — it is a different invariant (§3.6, money) and a different failure mode. It is recorded in Feature 373's open questions and should be its own small feature. **Do not bundle it.**

## Why this matters

Because **LE31's stock number is currently fiction, and four contracts describe it as if it were real.** §4.3 is the single most important rule in LE31's charter — the append-only ledger is the design that makes the whole system auditable — and the code does not implement it. Every guarantee the charter makes about stock ("current stock is derived from entries", "never update or delete ledger events") is currently backed by a *column* that nothing maintains. It reads `0`, or `qty_start`, or whatever a future writer last put there. There is no code path that can make it correct.

The stakes are asymmetric. If this is found now, it costs a column drop and a helper. If it is found after the first selling feature lands, it costs a backfill of every historical batch, an audit of every number the owner was ever shown, and — the real cost — a loss of trust in a system whose entire pitch is that the number is derived and therefore correct. **A restaurant owner's confidence in LE31's stock number is the product.** A cached, un-derived, silently-drifting stock column is the one thing that would break it.

And there is a second-order point worth making, because it generalises beyond this bug: **87 passes of external-arrival references were all read as evidence about LE31's rules, and not one of them was read as evidence about LE31's code.** They were filed as citations. Feature 373's README was finally used as an *instrument* — a prompt to go and check — and it found a defect in ninety seconds that ninety citations had not. The generalisable practice: **when an external artifact states an invariant you already claim to hold, the first thing to do is check whether your own implementation holds it, and file what you find.** The reference is only worth what the check is worth.

## Cross-section

Features 03 (`kitchen-stock-tracker`), 04 (`menu-photo-bot` — *"a `Batch` is created with `qty_remaining = qty_start`"*), 15 (`inventory-variance`), 26 (`reorder-point-on-stockentry` — *"qty_remaining still derived from StockEntry"*), 34 (`stockout-prep-board-snapshot` — *"qty_remaining = SUM(stock_entry.qty_delta) per active_batch"*), 45 (`print-fallback-floor-sheet`), 259 (`CtrlAltDevelop/ledger-service` — transactional outbox), 370 (`jdmacleod/kitchen-erp` — "append-only facts"), 371 (`Donkie/Spoolman` — on-hand derived, never stored), 372 (`hitaishi2222/kinv` — expiry without valuation), 373 (`ramaraihan12/warung-pos` — the reference that surfaced this). **This feature is unique vs all 402 pre-existing feature files + 378 HANDOFFs** — it is the first to propose *changing LE31's own schema* to restore a charter invariant, rather than quoting an external project about it. Reversibility: **high** — the column drop is reversible by re-adding the column, and no data is lost because nothing ever wrote it.
