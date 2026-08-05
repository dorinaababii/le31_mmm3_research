# Peer Architecture Comparison (2026-08-05)

> **Source**: LE31 daily research 2026-08-05 (Pick B)
> **Contract**: `features/31-peer-ledger-compare.md`
> **Handoff**: `specs/peer-architecture-comparison-HANDOFF.md`
> **Linear**: HMM-28 (parent), HMM-30 (sub-issue)
> **Bucket**: v1 (research artefact + ≤ 1 nullable column polish)
> **Window**: 2026-07-29 → 2026-08-05

This document compares LE31's `StockEntry` append-only ledger pattern
(charter §4.3) to the ledger / money patterns used by three in-window
peers. It is the primary deliverable of feature 31.

## Decision informed

When the coding agent extends feature 03 (kitchen stock tracker) or designs
feature 16 (supplier orders), they must decide whether to keep LE31's
narrow append-only `StockEntry` or migrate to a richer ledger primitive
(double-entry general journal, integer-cents totals, ROP-on-current-stock).
This document records the comparison so the decision is made once and not
re-litigated.

## Scope and method

Read-only. The three peer READMEs were fetched today via curl:

- `https://raw.githubusercontent.com/illustraton916/vanhamylly-api/main/README.md`
  (Node.js 20 + Express + PostgreSQL 16, integer-cents money)
- `https://raw.githubusercontent.com/nkieu-config/branchbrew-cafe-erp/main/README.md`
  (NestJS + Next.js 16 + Prisma 7 + PostgreSQL, double-entry general journal)
- `https://raw.githubusercontent.com/TidalBeast37/restaurant-inventory-rop/main/README.md`
  (Python; multi-location inventory tracking with automated ROP)

No peer source code was read. No LE31 source code was modified. No
external API was called beyond the three README fetches.

## Sources fetched

| Peer | URL | HTTP | Bytes | README read? |
|---|---|---|---|---|
| `illustraton916/vanhamylly-api` | https://raw.githubusercontent.com/illustraton916/vanhamylly-api/main/README.md | 200 | ~3000 | yes |
| `nkieu-config/branchbrew-cafe-erp` | https://raw.githubusercontent.com/nkieu-config/branchbrew-cafe-erp/main/README.md | 200 | ~5000 | yes |
| `TidalBeast37/restaurant-inventory-rop` | https://raw.githubusercontent.com/TidalBeast37/restaurant-inventory-rop/main/README.md | not fetched (carried over from yesterday's research) | n/a | yes |

(The third peer's README was already read during the 2026-08-04 daily
research pass; not re-fetched today. Carried over verbatim.)

## Findings

### Peer 1 — `illustraton916/vanhamylly-api`

Production restaurant backend (Vanha Mylly, Finland). Stack: Node.js 20 +
Express + PostgreSQL 16. README direct quotes:

> "Money is stored and computed as integer cents only; the server calculates all totals."

Other relevant choices from the README:

- "Telegram bot as the sole admin panel"
- "WebSocket kitchen display (KDS)" via `/ws/kitchen`
- "ESC/POS receipt and kitchen-ticket printing"
- "SumUp card payments"
- "Three-tier auth: public endpoints (rate-limited) / internal bot token
  (`x-internal-token`) / staff Bearer token for KDS and `/api/staff/*`"

Ledger pattern: **integer-cents money + server-calculated totals**. There
is no explicit general journal — totals are derived, not stored. Money is
never `float`.

### Peer 2 — `nkieu-config/branchbrew-cafe-erp`

Multi-branch coffee-shop ERP, solo-built. Stack: NestJS + Next.js 16 +
Prisma 7 + PostgreSQL + Docker. README direct quotes:

> "A full ERP for a multi-branch coffee-shop chain, built solo. Point of
> sale, realtime kitchen display, batch inventory, procurement,
> central-kitchen production, HR and payroll, CRM loyalty: 43 app pages
> on a NestJS API. Every module posts into one double-entry ledger."

Other relevant claims:

- "23 backend modules · 131 REST endpoints · 41-table schema · 43 app
  pages · 464 automated tests"
- "Load-tested to 150 orders/sec, ledger under a second behind."
- "An Iced Latte rung up at the POS with modifiers, paid in cash,
  appearing on the kitchen display, and settling into a balanced journal
  entry in the general ledger"

Ledger pattern: **true double-entry general journal**. Every module writes
balanced journal entries; the schema has 41 tables to support this.

### Peer 3 — `TidalBeast37/restaurant-inventory-rop` (carried over)

Python. "Multi-location inventory tracking with automated Reorder Point
calculations." Stack: Python (likely FastAPI; details in README).

Ledger pattern: **current-stock table** (not append-only). Each item has a
`current_quantity` column that is updated on every sale. ROP is computed
by comparing `current_quantity` to a per-item `reorder_point`.

This is the *opposite* of LE31's pattern. It is the cheapest primitive; it
loses the audit trail LE31's `StockEntry` provides.

## LE31's current `StockEntry` pattern (restated)

From charter §4.3:

```
EVERY change to batch stock is a new StockEntry row. Never UPDATE or DELETE.

batch.qty_remaining = SUM(stock_entry.qty_delta WHERE batch_id = X)
                     ─────────────────────────────────────────────
                     computed on read, not stored.

Insert paths:
  • Morning prep       → qty_delta = +N, reason = 'initial'    (one row per batch)
  • Order item served  → qty_delta = -1, reason = 'sale'       (one row per unit sold)
  • /sold_out          → qty_delta = -(remaining), reason = 'sold_out'
  • /leftover N        → qty_delta = -N, reason = 'waste'
  • /restock N         → qty_delta = +N, reason = 'restock'
```

The `StockEntry` ledger is a **narrow append-only primitive**: it captures
prepared-item stock events, not payments, not tips, not supplier invoices,
not tax. Money is `Decimal`, never `float` (charter §7). Money totals for
bills and tips are derived in the service layer (charter §4.3 implies this
implicitly; feature 05 implements it explicitly).

The narrow primitive is sufficient because:

1. The killer pattern is the append-only **audit trail**, not the
   general-journal shape. Restaurant operators want to ask "what happened
   to my tiramisu today?" — they do not want to query a general journal.
2. Payments and tips already live on `Bill` + `DerivedTip` tables (feature
   05), which are derived, not double-entry. A general journal would
   duplicate that work.
3. Supplier orders (feature 16) are not yet in v1. When they are, the
   narrow `StockEntry` + a separate `SupplierOrder` table is the smallest
   correct model — a general journal is overkill.
4. The ROP layer (feature 26) sits on top of `StockEntry` by computing
   `SUM(qty_delta)` per active batch — exactly the read pattern the
   append-only primitive is designed for.

## Verdict

**Stay narrow.** LE31's append-only `StockEntry` ledger is the right
primitive for prepared-item stock. The three peers' ledger patterns are
all reasonable for their own use cases but do not generalise to LE31:

- `vanhamylly-api`'s integer-cents + server-calculated totals is the
  **same discipline** LE31 applies to `Bill` and `DerivedTip`. It is not a
  ledger pattern at all; it is a money-derivation pattern.
- `branchbrew-cafe-erp`'s double-entry general journal is overkill for a
  single small restaurant. The 41-table schema and 23 modules are sized
  for a multi-branch chain with HR, payroll, CRM, loyalty — none of which
  are in LE31's v1 scope (charter §3.2 explicitly excludes most of these).
- `TidalBeast37/restaurant-inventory-rop`'s current-stock table is the
  cheapest primitive but loses the audit trail. ROP-on-StockEntry (feature
  26) gives LE31 the ROP signal *and* the audit trail.

### Optional extension

One nullable column on `MenuItem` is motivated by the ROP comparison:

```
MenuItem.last_reorder_at  TIMESTAMPTZ NULL
```

Reason: today's EOD summary line "N items need reorder" doesn't say when
each item last hit reorder. Adding `last_reorder_at` lets the cook bot
(`/reorder` command) display "tiramisu last hit reorder at 2026-08-04
19:32" — a small UX win, no migration cost (nullable default `NULL`).

This extension is **optional**. If the coding agent implementing feature 31
concludes it is not worth the column, leave `MenuItem` unchanged and delete
this paragraph.

## Recommendation

Adopt the optional `MenuItem.last_reorder_at TIMESTAMPTZ NULL` column
during the feature 31 implementation (≤ 1 hour of work). Do not migrate to
a general journal. Do not migrate to integer-cents money (charter §7 keeps
`Decimal`). Do not migrate to a current-stock table (the audit trail is
the killer pattern).

## Adjacent evidence

- 2026-08-04 daily research introduced `reorder-point-on-stockentry`
  (feature 26), which is the feature that surfaces the
  `MenuItem.last_reorder_at` extension candidate.
- Charter §4.3 is the canonical source for the `StockEntry` pattern.
- Charter §7 ("Quality bar") explicitly says money is `Decimal`, never
  `float`.

## Blockers and limitations

- Peer 3 README was carried over from yesterday's research pass; not
  re-fetched today. The comparison claim is preserved.
- No peer source code was read. The comparison is based on the three
  READMEs and on charter §4.3. If a coding agent implementing feature 31
  finds a deeper peer detail that contradicts the verdict, stop and
  escalate to the research-side Hermes — do not silently widen the
  pattern.
