# HANDOFF — 400-tws-manumaha-cafe-pos-v3

**Status**: defer (v1 vocabulary + one decision, no build today)
**Date**: 2026-10-29
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/400-tws-manumaha-cafe-pos-v3-mit-python-fastapi-sqlalchemy-restaurant-pos-escp-thermal-printing-split-bill-by-item-stock-take-with-variance-wastage-client-uuid-idempotent-offline-sync-void-restores-stock-v1-committed-vs-consumed-stock-vocabulary.md`
**LE31 feature gate verdict**: **defer** — vocabulary-only; no code is adopted. The gap is OBSERVED (parent-verified against `backend/app/models.py`); the demand is not.

## Trigger policy

This is a **defer artifact** — a vocabulary record plus three named decisions. It does **not** start a build.

It surfaces `tws-manumaha/cafe-pos-v3` (MIT, Python + FastAPI + SQLAlchemy, in-window by both `created_at` and `pushed_at`) as a dated, in-window reference for **three decisions LE31 must make before the first `StockEntry` write site exists**:

1. **Where the idempotency key is minted** (client-side vs server-side; one namespace shared by the waiter UI and the cook bot).
2. **The void/reversal event** — a new `StockReason` member, recorded as a **new `StockEntry`**, never as an update to `Batch.qty_remaining`.
3. **The variance record** — a counted quantity that disagrees with the derived balance, recorded as a **finding**, not silently reconciled.

**Trigger conditions** — if ANY of these is met, the external coding agent should:

1. Load this artifact, the linked feature file, and the raw README (`/tmp/le31-daily-2026-10-29/parent/tws-manumaha__cafe-pos-v3__README.md`).
2. Load the companion features **382** (stock-deduction idempotency — owns the idempotency write path), **374** (`qty_remaining` stored-vs-derived — owns the stored-number question) and **390** (`Pantry` snapshot — owns the reversal-adjacent question).
3. Load **feature 401** (the same window's pending-order reservation vocabulary) and **feature 402** (the same window's storage-layer permission rule).
4. Decide the three questions above **explicitly**, in writing, before writing any `StockEntry` write path.
5. If a decision is made, implement it **in the owning feature** (382 for the key, 374 for the variance), **not** in a new feature.
6. If no decision can be made, close this artifact and leave the ledger as-is.

**If the trigger condition is NOT met, do nothing.** In particular: **do not** add a `reserved` column, **do not** add an idempotency key column, and **do not** add a `StockReason` member — the whole point of the defer is that these are decisions, not defaults.

**Disambiguation**: this artifact is about the **ledger-side machinery** (key, reversal, variance). It is **not** about the pending-order reservation quantity (**feature 401**) and **not** about permission enforcement (**feature 402**). Three separate artifacts, one window, three different concepts — do not merge them.

## Mandatory inputs

- **Active feature**: `features/400-tws-manumaha-cafe-pos-v3-…-v1-committed-vs-consumed-stock-vocabulary.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-29.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-29/`
  - `parent/tws-manumaha__cafe-pos-v3__repo.json` — direct `GET /repos/`
  - `parent/tws-manumaha__cafe-pos-v3__README.md` — README, 4,938 B
  - `parent/tws-manumaha__cafe-pos-v3__tree.json` — file tree, 25 files
- **LE31 source of truth**: `backend/app/models.py`
  - `StockEntry` (lines 113–126) — no idempotency key; `at: datetime` is a wall-clock timestamp, not a monotonic cursor
  - `StockReason` (lines 54–60) — `initial`, `sale`, `waste`, `restock`, `sold_out`; **no reversal member**
  - `Batch.qty_remaining` (line 106) — a single stored number
  - `ItemStatus` (lines 35–40) — `new`, `preparing`, `ready`, `served`, `cancelled`
- **Charter §3.3** (append-only stock ledger), **§3.6** (exact EUR, never float) — `PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — the seven-check feature gate and the hard invariants (charter §3.3 append-only, §3.6 money, §3.4 AI-with-evidence).
- `le31-v1-feature-pattern` — the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — the source-of-truth discipline on the artifact's README quotes.
- `le31-handoff-spec` — the frozen-contract discipline.

The agent must **NOT** load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The three recorded primitives:

- **Idempotency key** — a caller-supplied value that makes a repeated write a **no-op** rather than a second event. LE31's equivalent, if adopted, is a new column on `StockEntry` with a `UniqueConstraint` where not null. **Note the precedent: that would be the first constraint of any kind in LE31's schema** (`grep -rn "Constraint" backend/` currently returns nothing).
- **Reversal** — an event that *undoes* a prior event's effect, recorded **as its own entry**, never as an edit of the original. LE31's equivalent, if adopted, is a new `StockReason` member; the `StockEntry` row itself mirrors the original entry's `qty_delta` and points at it via `ref_order_item_id`.
- **Variance** — the difference between a **counted** quantity and the **derived** quantity, recorded as a **finding**. LE31's equivalent, if adopted, is a `StockEntry` with a count/correction `StockReason`; the variance itself is **derived**, never stored as a mutable number.

**Anti-goals, stated so they are not drifted into:**

- **No `reserved` column.** "Committed" is a derivation, not a stored number (see feature 401). §3.3 forbids storing current stock.
- **No update to `Batch.qty_remaining`.** A void restores stock by **adding a new `StockEntry`**, never by editing the balance.
- **No stored-balance pattern.** The artifact's own *"stock history for every ingredient"* is a stored-balance model and **violates §3.3** — only the rule transfers.

## Files to touch (when the defer is promoted to build)

**None today.** When promoted, the changes belong to the **owning** features:

- `backend/app/models.py` — a new `StockReason` member (line 54–60 block), and possibly an idempotency-key column on `StockEntry` (line 113–126 block).
- A new alembic migration under `backend/migrations/versions/` — **note the charter's known unresolved migration-strategy inconsistency (§3.2 excludes Alembic for v1 while the codebase uses it); surface it, do not settle it by accident.**
- `backend/app/` — the write path itself, **which lives in feature 382**, not here.

## Verification protocol

When promoted, the external coding agent must verify:

1. **The frozen contract fields match the recorded fields** — `idem_key`, the reversal `StockReason` member, the count/correction `StockReason` member.
2. **A repeated write with the same idempotency key creates exactly one `StockEntry` row.** This must be tested at the **database** level, not the API level.
3. **A void creates a new `StockEntry`; it does not modify the original row and does not modify `Batch.qty_remaining`.** Assert both: the original row is byte-identical afterwards, and the derived balance moved by exactly the mirrored delta.
4. **A count that disagrees with the derived balance produces a variance record and does not silently change the balance.** The variance must be *reported*, not reconciled away.
5. **The end-to-end acceptance path is executable in the configured environment**: the cook bot receives the same order twice → exactly one stock deduction; a void → stock restored via a new entry; a count → a variance record appears.
6. **The rollback path is present and reversible**: drop the new column / revert the migration; the ledger rows written under the new scheme remain valid, or the write path is disabled cleanly.

## Rollback path

- Today: **nothing to roll back** — this defer writes **no** code, **no** schema, and **no** data.
- When promoted: revert the alembic migration; remove the new `StockReason` member(s) only if no production rows use them; disable the write path that depends on the new behaviour.
- **Ledger rows are never edited or deleted to roll back** (charter §3.3). A mistaken write is compensated by a **new compensating `StockEntry`**, not by an edit.

## Sign-off gap

No build today. This defer artifact does **not** require owner sign-off; it surfaces a dated, in-window reference and three open decisions.

**The open decisions DO require owner sign-off before they are implemented** — specifically the **key-minting location** (client-side vs server-side), because that decision determines whether the waiter UI and the cook bot share one key namespace. The external coding agent must mirror these three decisions back to the owner before implementing and **stop if it cannot**.
