# Feature 31 — Peer Ledger Compare

> **Priority**: P2 · **Effort**: XS (≤ 1 day) · **Source**: daily-research
> 2026-08-05 (Pick B) · **Bucket**: v1 (research artefact + ≤ 1 column polish)
> **One-line**: Read `vanhamylly-api` + `branchbrew-cafe-erp` +
> `TidalBeast37/restaurant-inventory-rop`; produce a single-page comparison
> doc; name any narrow-`StockEntry` extension they motivate (none expected).

## Goal

Two in-window production-grade restaurant peers (`illustraton916/vanhamylly-api`
and `nkieu-config/branchbrew-cafe-erp`) both ship ledger patterns that are
adjacent to LE31's narrow append-only `StockEntry`. This feature produces a
single-page Markdown comparison at `research/13-peer-architecture-comparison.md`
that answers one question: **should LE31 widen its `StockEntry` to a true
general journal, or stay narrow?** It then optionally adds ≤ 1 nullable
column to `MenuItem` or `Batch` if the answer is "extend slightly".

## Scope

**In scope (v1):**
- New Markdown doc `research/13-peer-architecture-comparison.md`
  (≤ 1 page). Three sections:
  1. Peer ledger patterns observed (what each peer does).
  2. LE31's current `StockEntry` pattern restated (what charter §4.3 says).
  3. Verdict + optional ≤ 1 column on `MenuItem` or `Batch` if warranted
     (default verdict: "stay narrow, the `StockEntry` append-only ledger is
     sufficient for prepared-item stock; defer general-journal extensions
     to feature 16 supplier orders if it ever motivates").
- No new tables. No new endpoints. No new bot commands. No new dependency.
- ≤ 1 day total work (the doc is the dominant deliverable; the column is
  optional and trivial).

**Out of scope (v1):**
- Migrating `StockEntry` to a double-entry general journal. Charter §3.1
  explicitly chooses the narrow append-only pattern.
- Feature 16 (supplier orders) and feature 05 (payment + tip). Both
  already coexist with the narrow pattern.
- Reading the peers' source code (READMEs are sufficient for the
  architecture comparison).
- Any cross-restaurant or multi-tenancy implication.

## Description

LE31's `StockEntry` append-only ledger (charter §4.3) is the killer pattern.
Each row is a `qty_delta` event; current stock is `SUM(qty_delta)` per batch;
the ledger is never UPDATEd or DELETEd. This is a narrow primitive — it
captures prepared-item stock, not payments, not tips, not supplier invoices.

Today's two production peers each chose a slightly different primitive:

- **`illustraton916/vanhamylly-api`** — Node.js 20 + Express + PostgreSQL 16.
  Production restaurant backend (Vanha Mylly, Finland). Money is
  **integer cents only**; the server calculates all totals. There is no
  explicit general journal — totals are *derived*, not stored. Telegram bot
  is the sole admin panel; KDS over WebSocket at `/ws/kitchen`; ESC/POS
  receipt + SumUp card payments. ([https://github.com/illustraton916/vanhamylly-api](https://github.com/illustraton916/vanhamylly-api))
- **`nkieu-config/branchbrew-cafe-erp`** — NestJS + Next.js 16 + Prisma 7 +
  PostgreSQL. 43 pages, 23 modules, 131 endpoints, 41-table schema, 464
  tests, realtime kitchen display, **double-entry general journal**,
  load-tested to 150 orders/sec. ([https://github.com/nkieu-config/branchbrew-cafe-erp](https://github.com/nkieu-config/branchbrew-cafe-erp))
- **`TidalBeast37/restaurant-inventory-rop`** (carried over from yesterday's
  research, 2026-08-02) — Python; "Multi-location inventory tracking with
  automated Reorder Point calculations." ROP sits on a current-stock table,
  not an append-only ledger.

The narrow `StockEntry` is the right level for prepared-item stock. None of
the three peers forces LE31 to migrate. But the question deserves a written
answer so the next coding agent doesn't open it from scratch when extending
feature 03 (kitchen stock tracker) or designing feature 16 (supplier orders).

The output is a single-page doc with the three sections above. The optional
column extension (e.g. `MenuItem.last_reorder_at TIMESTAMPTZ NULL` to track
when ROP last fired per item — the most likely extension) is trivial and
nullable; removing it is one ALTER.

## Data model

No new tables. At most **one new nullable column** on `MenuItem` or `Batch`
if the comparison motivates it. The comparison doc will record the chosen
extension (or the explicit "no extension") in section 3.

Migration: `init_db()` adds the column if absent (existing pattern from
features 25, 26, 27).

## Implementation

1. **New Markdown doc** `research/13-peer-architecture-comparison.md` —
   copy the structure from `research/02-kitchen-display.md` and
   `research/03-inventory-stock.md` (existing in-repo research format).
   Fill the three sections.
2. **Optional column** — if section 3 motivates one, edit
   `backend/app/models.py` to add the nullable column and document the
   migration in the doc. Default: no column; verdict is "stay narrow".
3. **Manual verification**:
   - Read `features/03-kitchen-stock-tracker.md`, `features/26-reorder-point-on-stockentry.md`, and `charter/PROJECT_CHARTER.md` §4.3 to confirm the comparison doc's section 2 matches reality.
   - Open `https://github.com/illustraton916/vanhamylly-api`, scroll the
     README's "Architecture" and "Money" sections — confirm the
     "integer-cents, server-calculated totals" claim.
   - Open `https://github.com/nkieu-config/branchbrew-cafe-erp`, scroll
     the README — confirm the "double-entry general journal, 150 orders/sec"
     claim.
   - Confirm no `StockEntry` invariant is broken (no UPDATE or DELETE
     introduced). If section 3 motivates an extension, confirm the new
     column is nullable.
4. **Commit + push**: branch is `main`. Commit message:
   `Add research/13-peer-architecture-comparison.md (Pick B 2026-08-05)`.
   If the optional column is added, a second commit:
   `Feature 31: <column-name> on <table> (Pick B 2026-08-05)`.

## Telegram interaction

None. This feature produces a research artefact and possibly one nullable
column; neither is visible to the cook or the waiter.

## Dependencies

- [03-kitchen-stock-tracker.md](../features/03-kitchen-stock-tracker.md) —
  the `StockEntry` pattern being compared.
- [26-reorder-point-on-stockentry.md](../features/26-reorder-point-on-stockentry.md) —
  yesterday's Pick B; the ROP layer sits on top of `StockEntry`.
- Charter §3.1 (single-restaurant, money derived), §3.2 (no PII), §4.3
  (the `StockEntry` killer pattern).
- The two peers' READMEs (no API key, no auth required to read).

## Open questions

- Should the doc also compare to `TidalBeast37/restaurant-inventory-rop`
  even though that one is not a production restaurant system? Default:
  yes — it's the only Python ROP peer and is the most direct contrast to
  the append-only `StockEntry` pattern.
- Should the doc also mention `satisfecho/pos` and
  `KamerrEzz/odoo-x-restopro` from previous daily reports? Default: no —
  three peers is enough; keep the doc ≤ 1 page.
- Does `vanhamylly-api`'s server-calculated-totals pattern (vs general
  journal) suggest LE31 should keep money derivations in service layer
  rather than in models? Default: yes — charter §3.1 already says money is
  Decimal-derived not stored.
- Does `branchbrew-cafe-erp`'s double-entry pattern suggest LE31 should
  add a `JournalEntry` table for non-stock money flows (payments, tips,
  supplier orders)? Default: not in v1; defer to feature 16 (supplier
  orders) if it ever motivates.

## LE31 gate verdict

Run per `skills/le31-conventions/SKILL.md` — seven checks:

1. **JTBD** — When the operator considers LE31 vs `vanhamylly-api` /
   `branchbrew-cafe-erp`, the operator wants to know "is the LE31 ledger
   primitive the right one, or should we widen to a general journal?"; the
   comparison doc lets the operator answer the question without re-reading
   the peers' source.
2. **Viability** — ✅ owner-cook does not operate this artefact; consumed
   by the coding agent before extending feature 03.
3. **Practicability & confidence** — ✅ no new dependency; just a Markdown
   doc + optional column. Evidence strength: medium-high (two production
   peers in window with full READMEs).
4. **Conflict** — ⚠️ none if the comparison concludes "narrow append-only
   is right" (the most likely outcome). Conflict arises if the comparison
   concludes "general journal" — in that case, escalate to the user, do
   not silently widen `StockEntry`.
5. **Outcome & appetite** — v1 (≤ 1 day). Cut scope to "read two peers,
   name any extension" if it grows.
6. **Cost vs value** — low cost, high informational value (informs
   feature 16 supplier orders and future v2 extensions).
7. **Circuit breaker / reversibility** — ✅ document is deletable; any
   column added to `MenuItem`/`Batch` is nullable and removable.

**Decision: build** as a thin v1 research artefact + feature 03 polish.

## Why this matters

The narrow append-only `StockEntry` is LE31's defensible differentiator
(re-confirmed by 7 consecutive daily reports). Two production peers surface
today that both use slightly different primitives — neither forces LE31 to
change, but both deserve a written answer so the architecture decision is
documented. ≤ 1 day, no new dependency, no new endpoint.
