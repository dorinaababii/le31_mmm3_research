# Feature 146 — slashbooks AI-bookkeeper QuickBooks-replacement cross-section (defer)

> **NEW observation (2026-09-05).** Documents in-window GitHub repository `giltotherescue/slashbooks` (32★/4 forks, Apache-2.0, Python, pushed **2026-08-24T22:40:20Z**, in-window by push only): *"Replace QuickBooks and your outsourced bookkeeper with an AI agent you control."* Plain-text accounting, claude-code, local-first. **Highest-stars net-new Python repo in the 30-day window** across all 8 GitHub queries; **first surface of this repo in the 37-pass series** (parent-verified by ripgrep against all features 1–143 + all brainstorm reports 2026-08-18..2026-09-04). Bucket: **v2 owner-pains (cross-section competitive signal)** — watch-list defer. Zero build time today.

## Goal

Retain the **"replace outsourced bookkeeper" JTBD framing** as the **architectural signal** that the v2 owner-facing month-end-books-reconciliation surface is being addressed by credible independent maintainers in 2026. The artifact is the persistent cross-section reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the slashbooks primitive: plain-text accounting + AI agent + claude-code + local-first; addresses the "replace outsourced bookkeeper" JTBD that LE31 v2 owner-facing surface might also address.
- A decision record: today's verdict is `defer` because LE31 v1 has no owner-facing month-end-books-reconciliation surface today; the defer surfaces the JTBD framing for the next v2 surface that might.
- A cross-section reference with feature 119 BalanceDesk (`Ritchalison/BalanceDesk`, a different repo) — same shape (bookkeeping surface for solo operators), different mechanism (text-ledger + AI agent vs. local-first desktop reconciliation terminal).

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `audit_logs` schema.
- Any user-facing owner-facing month-end-books-reconciliation surface (no owner-facing query today).
- Adoption of the slashbooks code — LE31 has no AI-agent surface today (charter §3.4 forbids customer-facing AI; v1 has no AI at all).

## Evidence / JTBD

When a future LE31 v2 owner wants to verify *month-end books against `audit_logs`*, the owner wants *a JTBD framing that maps cleanly to the existing append-only `audit_logs` discipline*, but struggles because *the "replace outsourced bookkeeper" framing has not been validated for LE31's specific operator shape*, so that *the v2 owner-facing surface has independent evidence that the JTBD is real and being addressed by credible maintainers*.

- **Evidence class**: observed (32★ + 4 forks + Apache-2.0 + in-window push on a small-operator-bookkeeping framing = credible-maintainer validation of the JTBD).
- **Confidence**: medium-high (JTBD validation) / low (mechanism transferability).
- **Real observed LE31 JTBD**: none directly, but **charter §3.1's "Money: never use binary floats. Preserve exact EUR values and explicit tax/tip derivations."** is the *operational discipline* that any v2 owner-facing books-reconciliation surface would inherit.
- **The value is JTBD validation**, not direct demand: when the question is eventually asked, the JTBD has been validated by independent maintainers.

## Description

GitHub `giltotherescue/slashbooks` (32★/4 forks, Apache-2.0, Python, pushed 2026-08-24T22:40:20Z, in-window by push only) — *"Replace QuickBooks and your outsourced bookkeeper with an AI agent you control."* Plain-text accounting, claude-code, local-first.

The transferable primitive is the **JTBD framing**: *"replace outsourced bookkeeper"* is the exact framing that a future LE31 v2 owner-facing month-end-books-reconciliation surface would address. The mechanism (plain-text accounting + claude-code + local-first) is *not* what LE31 would build (LE31's `audit_logs` per mutation is the right substrate, not a parallel text-ledger), but the **framing** is signal that the JTBD is real.

**Cross-section with LE31 charter §3.1** (Money: never use binary floats. Preserve exact EUR values):

| Charter invariant | v1 status | Slashbooks cross-section |
|---|---|---|
| **Money: never use binary floats. Preserve exact EUR values** (charter §3.1) | **Satisfied** — `Decimal` everywhere, `max_digits=10, decimal_places=2` SQLModel fields. | Slashbooks' *"plain-text accounting"* is the opposite approach (text-ledger, no SQL); LE31 v1's SQL + `Decimal` discipline is the more rigorous path. |
| **Tip derived from total_paid − items_consumed − tax** (charter §3.1) | **Satisfied** — `DerivedTip` model never manually entered. | Slashbooks does not address tips specifically; the *"replace outsourced bookkeeper"* JTBD is broader. |
| **End-of-shift cash reconciliation computes expected vs counted cash** (charter §3.1) | **Satisfied** — `POST /api/shifts/{id}/close` returns variance. | Slashbooks is the **month-end** JTBD; LE31's shift-close is the **shift-end** JTBD. Same family, different time scale. |
| **Privacy: store only data needed for restaurant operations** (charter §3.2) | **Satisfied** — v1 stores counts, no identity or contact data. | Slashbooks' *"AI agent you control"* + *"local-first"* is the privacy-friendly framing that LE31 v2 would inherit. |

**Cross-section with feature 119 BalanceDesk** (`Ritchalison/BalanceDesk`):

| Dimension | Slashbooks | BalanceDesk | LE31 v1 |
|---|---|---|---|
| **JTBD** | Replace outsourced bookkeeper | Local-first reconciliation terminal | (shift-end reconciliation only) |
| **Mechanism** | Plain-text accounting + claude-code + local-first | Local-first Windows-desktop offline app | SQLModel + Postgres + FastAPI |
| **Stars** | 32★ | 1★ | n/a |
| **License** | Apache-2.0 | NOASSERTION | n/a |
| **Stack match** | None (text-ledger, no SQL) | None (CSS desktop app) | Full (SQLModel + Postgres) |
| **LE31 importable?** | Yes (Apache-2.0) | No (NOASSERTION, CSS not Python) | n/a |

Slashbooks and BalanceDesk address the same JTBD (bookkeeping surface for solo operators) with **opposite mechanisms**: Slashbooks is *AI-driven text-ledger*, BalanceDesk is *local-first desktop reconciliation terminal*. LE31 v1 has neither; the v2 owner-facing month-end-books-reconciliation surface would address the same JTBD with a third mechanism: *SQLModel + Postgres + audit_logs per mutation*.

**Cross-section with prior picks:**

- **Feature 49 Postledger Tamper-Evident Hash** (2026-08-06) — *double-entry-bookkeeping "assumes the bookkeeper is not trustworthy"*. Slashbooks is the *opposite* assumption: the bookkeeper is the *owner*, controlled locally. Same append-only primitive, opposite threat model.
- **Feature 119 BalanceDesk** (2026-08-26) — *local-first reconciliation terminal*. Same JTBD, opposite mechanism, same charter §3.1 privacy-friendly framing.
- **Feature 132 sqlmodel 0.0.42 pin-track** (2026-08-29) — *LE31's pinned SQLModel version*. Slashbooks does not use SQLModel; the cross-section is on the JTBD, not on the stack.
- **Feature 141 KRINEIA five invariants** (2026-09-04) — *proof/record distinction*. Slashbooks' *"local-first"* framing is the privacy-friendly cousin of KRINEIA's `trust-root separation` invariant: the owner's local text-ledger is the trust root for the owner's books.
- **Feature 144 silphe** (2026-09-05) — *local-only pointer-movement biometric*. Slashbooks is a different local-first framing: local-first *bookkeeping*, not local-first *operator-identity*. Same privacy-friendly posture, different primitive.

LE31 v1 currently has no owner-facing month-end-books-reconciliation surface; the defer surfaces the slashbooks JTBD framing for future use. The value is **JTBD validation**, not *implementation*.

## Data model

No schema change today. The defer artifact documents that the future slashbooks-cross-section-instantiation would have:

- **Monthly-reconciliation query** (future): a thin SQLModel query that joins `audit_logs` + `stock_entry` + `bill` + `shift` tables for a given calendar month and returns a per-category total that maps onto a bookkeeper's chart-of-accounts. **Not built today.**
- **CSV export extension** (future): an extension of the existing `GET /api/reports/today.csv` that returns the monthly-reconciliation query as a text/csv the owner can hand to a human bookkeeper. **Not built today.**
- **Chart-of-accounts mapping** (future): a `chart_of_accounts` table that maps LE31's table names to bookkeeper category names (e.g., `Bill.method = 'cash'` → "Cash on hand"). **Not built today.**

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to build this in v2, the implementation steps would be:

1. Add a `LE31_BOOKS_RECONCILIATION_ENABLED` env flag (default off).
2. Implement the monthly-reconciliation query above.
3. Add a CSV export endpoint `GET /api/reports/month/{YYYY-MM}.csv` that returns the monthly-reconciliation query as text/csv.
4. Add a one-page owner-facing reconciliation surface at `/owner/reports/monthly` that displays the monthly totals per chart-of-accounts category.
5. **Out of scope for v1**: any chart-of-accounts customization; any AI-agent loop integration (charter §3.4 forbids customer-facing AI; staff-facing AI is allowed but not in v1); any third-party bookkeeper integration (the CSV export is the integration boundary).
6. **Out of scope for v1**: any QuickBooks-format export; any tax-jurisdiction-aware derivation.

## Telegram interaction if any

None. Slashbooks is a cross-section competitive-signal artifact; no cook-facing Telegram surface today. If the LE31 owner decides to build the v2 owner-facing month-end-books-reconciliation surface, it would be a *web UI*, not a Telegram surface.

## Dependencies

- **GitHub**: `giltotherescue/slashbooks` (32★/4 forks, Apache-2.0, Python, pushed 2026-08-24T22:40:20Z, in-window by push only).
- **Charter §3.1 (Money: never use binary floats. Preserve exact EUR values and explicit tax/tip derivations)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (Privacy: counts not identity)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Companion artifacts**: features 49 / 119 / 132 / 141 / 144 (ripgrep-verified distinct).
- **Stack**: existing SQLModel + Postgres + FastAPI + aiogram v3 — no new dependency.
- **Licence**: Apache-2.0 — importable but not proposed as a v2 dependency (LE31 has no AI-agent surface today). README contents not read in this pass (parent relied on the GitHub Search `description` field). The 32★ + 4 forks + in-window push is the strongest single-maintainer validation of the "small-operator bookkeeping" JTBD in the 37-pass series.

## Open questions

1. **Who would invoke the monthly-reconciliation view on a v2 LE31 surface?** LE31 has one stakeholder (the owner). The CSV export is *useful* even for one stakeholder (the owner can hand the CSV to a human bookkeeper), so the marginal value is non-zero even with one stakeholder. Different from features 121 / 141 / 144 / 145, where the marginal value of one-stakeholder-only surfaces is *unproven*. Recommendation: when v2 owner-facing surface is considered, the CSV export is the cheapest first step (1-2 days of work; no AI integration; no new dependencies).
2. **Does charter §3.1 need an explicit `month-end-books-reconciliation` clause?** Today, no. A future v2 surface that adds the monthly-reconciliation endpoint would make this explicit. Recommendation: not a v1 question; revisit when v2 owner-facing surface is considered.
3. **Is the chart-of-accounts mapping stable across LE31 versions?** Today: unknown; LE31 v1 has no chart-of-accounts table. The mapping would need to be designed when v2 is considered. Recommendation: not a v1 question; revisit when v2 is considered.
4. **Does slashbooks' claude-code + plain-text mechanism offer any transferable primitive?** Maybe: the *plain-text-as-source-of-truth* discipline is the inverse of LE31's *SQL-as-source-of-truth* discipline. The transferable item is the **owner-facing view** that exposes the underlying records in a human-readable format; LE31's existing `GET /api/reports/today.csv` already does this for the daily level. Recommendation: when v2 is considered, the monthly CSV export is the natural extension.

## Why this matters

LE31 charter §3.1 has been **operationalizing explicit-money-discipline** for 37 passes without ever surfacing the *"replace outsourced bookkeeper" JTBD framing*. Slashbooks is the **first repo in the 37-pass series** that explicitly states the JTBD the way a small-operator LE31 owner would state it: *"I want to stop paying my bookkeeper"*. The value is not implementation today — LE31 v1 has no owner-facing month-end-books-reconciliation surface. The value is **JTBD validation**: any future v2 owner-facing surface can now point to a credible-maintainer, high-star, in-window repo that addresses the same JTBD. The **32★ + 4 forks + Apache-2.0 + in-window push** is the strongest single JTBD-validation data point of the 37-pass series for the small-operator-bookkeeping surface. Combined with feature 119 BalanceDesk (same JTBD, opposite mechanism), the JTBD has **two independent credible-maintainer data points** — a JTBD pattern, not a single data point.

The defer is fully reversible: if the LE31 owner decides the JTBD framing is not worth carrying, the file can be deleted with no operational impact. The framing is contained in the file, not in the codebase.