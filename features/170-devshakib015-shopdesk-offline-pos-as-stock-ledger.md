# Feature 170 — `devShakib015-shopdesk-offline-pos-as-stock-ledger` (defer)

> **NEW observation (2026-09-13).** Documents in-window GitHub repo `devShakib015/BusinessMonitoringApp` (ShopDesk, **0★/0⑂**, **MIT**, Python, **pushed 2026-09-02T14:19:28Z**, in-window by push, 3.3 MB, **created 2020-08-05T19:06:46Z — 5-year-old repo with single recent re-activation push**). Description (verbatim from GitHub API, parent-verified direct-GET 2026-09-13): *"ShopDesk — a free, offline point-of-sale for a small shop: barcode selling, stock as a ledger, customer credit, thermal receipts and day-close reports. The data never leaves the counter."* Topics (verbatim from raw JSON, parent-verified): `barcode, inventory, offline, open-source, point-of-sale, pos, python, receipt-printer, retail, shop-management, small-business, sqlite, windows`. Bucket: **v1 (operator-surface inspiration)** — pick A of Brainstorm 2026-09-13. Build verdict: `defer` (parking-lot). Zero build time today. The 5-year-old repo with a single re-activation push is the demand signal, not a code-adoption opportunity.

## Goal

Retain the **"stock as a ledger in an offline single-shop POS"** primitive as a persistent cross-section reference for the LE31 v1 *offline-first + append-only StockEntry + no-cloud* wedge, and document the **operator-surface-shape** that an independent maintainer arrived at in 2026 without reading the LE31 charter. The artifact is the persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"stock as a ledger"** primitive: every sale reduces inventory by inserting a row into a ledger table (not by mutating a counter). This is the load-bearing primitive for any LE31 v1 surface that ships offline-first + append-only StockEntry (§3.1).
- A written record of the **"data never leaves the counter"** framing: SQLite as the canonical store; no cloud sync; no vendor lock-in. This is the LE31 phone-first operator posture (§3.1, §3.2).
- A written record of the **"barcode selling + thermal receipts + day-close reports"** operator-surface-shape: the operator's daily workflow is *scan → confirm → receipt → close*, with the day-close report as the recap export. This is the LE31 v1 surface shape that maps to features 5 (`payment-tip-reconciliation`) + 27 (`reorder-point-on-stockentry`) + 33 (`telegram-walkin-pin`) + 39 (`owner-daily-recap-telegram`).
- A written record of the **"5-year-old repo with single re-activation push"** signal: the maintainer independently arrived at the same primitives (barcode + ledger + offline + day-close), but the repo hasn't shipped in 5 years before this single push. The signal is *demand*, not *adoption*. Sister-shape to feature 40 (`satisfecho/python-pos-watch` — AGPL-3.0 blocked by §3.2; ShopDesk is the MIT alternative shape) and feature 54 (`corner-mart-pos-double-entry`).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence; (2) the stack is desktop-Windows-Sqlite, not LE31's phone-first-web-FastAPI-SSE; (3) the *demand-signal* is the value, not the code.

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot (charter §3.1: explicit state transitions; v1 surfaces are sufficient for v1 ops).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the ShopDesk codebase (single maintainer, 5-year-old repo, Windows-desktop-POS stack — no overlap with LE31's FastAPI+SSE+Postgres+aiogram stack).
- Cross-pollination with charter §3.4 AI surface (ShopDesk has zero AI; the operator-facing surface is deterministic barcode-driven — §3.4 compatible).
- Cross-pollination with charter §3.3 (ShopDesk is single-shop, not multi-tenant).

## Evidence / JTBD

When a future LE31 v1 surface proposes "the offline-first single-shop POS shape" (e.g. a beta operator wants to run the v1 surface on a counter PC without internet), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "stock as a ledger + offline + day-close reports" is a real demand*, so that *the v1 surface can be defended with "this is what an independent operator shipped in 2026"*.

- **Evidence class**: observed (the ShopDesk description + topics name the primitive explicitly: `barcode, inventory, offline, point-of-sale, sqlite, receipt-printer`).
- **Confidence**: medium-high for the demand signal (the description is direct; the topic tags are LE31-aligned; the "5-year-old repo with single re-activation push" is the *demand signal*, not the *adoption signal*); low for transferability (LE31's stack is web/SSE, ShopDesk is Windows desktop).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is web-first, not Windows-desktop); the value is the *demand-signal* for the offline-first wedge.
- **The value is naming, not direct demand**: when the first v1 offline-first PR lands (if/when the owner approves the offline-first wedge), the ShopDesk pattern is a ready-made *named primitive* and the *barcode + stock-as-ledger + offline + day-close* vocabulary slots into features 3 (`kitchen-stock-tracker`) + 5 (`payment-tip-reconciliation`) + 26 (`reorder-point-on-stockentry`) + 27 (`uvicorn-0-52-pin`) + 34 (`stockout-prep-board-snapshot`) + 39 (`owner-daily-recap-telegram`) + 40 (`satisfecho-python-pos-watch`) + 54 (`corner-mart-pos-double-entry`) + 131 (`puntovivo-fiscal-native-local-first-pos-cross-section`) + 165 (`ladle-restaurant-prep-forecasting-food-cost-leak-detection`).

## Description

GitHub `devShakib015/BusinessMonitoringApp` (ShopDesk, MIT, 0★/0⑂, Python, pushed 2026-09-02T14:19:28Z, created 2020-08-05T19:06:46Z, 3.3 MB). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-13): *"ShopDesk — a free, offline point-of-sale for a small shop: barcode selling, stock as a ledger, customer credit, thermal receipts and day-close reports. The data never leaves the counter."*

The architectural primitive has one core principle and four sub-primitives:

1. **"Stock as a ledger"** — every sale reduces inventory by inserting a row into a ledger table (not by mutating a counter). Append-only discipline, no mutable fields. This is the §3.1 explicit-state-transitions primitive.
2. **"The data never leaves the counter"** — SQLite as the canonical store; no cloud sync; no vendor lock-in; the operator owns the data. This is the §3.1 phone-first operator posture + the §3.2 permissive-license posture.
3. **"Barcode selling + thermal receipts + day-close reports"** — the operator's daily workflow is *scan → confirm → receipt → close*, with the day-close report as the recap export. The day-close report is the operator-facing recap pattern that maps to features 39 (`owner-daily-recap-telegram`) + 57 (`owner-recap-persona-voice`).
4. **"Customer credit"** — the customer-credit workflow is the *accounts-receivable* surface that LE31 v1 explicitly defers (LE31 v1 is *cash-only*; customer-credit is a v2 surface). The fact that ShopDesk ships customer-credit is a *demand signal* for a v2 LE31 surface, not a v1 surface.

**The 1:1 mapping onto LE31 v1 surface (offline-first wedge):**

| ShopDesk primitive | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| Stock as a ledger | `StockEntry` (append-only) | §3.1 ✓ | **Implemented (v1)** |
| The data never leaves the counter | Phone-first operator web UI, no cloud by default | §3.1, §3.2 ✓ | **Implemented (v1)** |
| Barcode selling | (LE31 v1 has no barcode surface; waiter enters order manually on phone) | not in v1 | **Not implemented** — out of v1 scope |
| Thermal receipts | (LE31 v1 has no receipt-printer surface) | not in v1 | **Not implemented** — out of v1 scope |
| Day-close reports | `owner-daily-recap-telegram` (feature 39) | v1 ✓ | **Implemented (v1 — different medium)** |
| SQLite as canonical store | SQLite + Alembic migrations | v1 ✓ | **Implemented (v1)** |
| Customer credit | (LE31 v1 is cash-only) | v2 | **Not implemented** — deferred to v2 |
| Windows desktop | (LE31 v1 is web-first) | not in v1 | **Not implemented** — different stack |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds an offline-first wedge surface), the v1 schema migration would not require any change — the `StockEntry` + `audit_logs` table pair already implements the *append-only ledger* primitive.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v1 implementation would include:
1. None — the v1 surface is already implemented. The ShopDesk pattern is the *demand-signal* for an offline-first wedge that LE31 v1 already partially supports.

**No existing code change today.**

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

Future v1: if the owner approves an offline-first wedge, the day-close report could be pushed to the owner via the existing cook-Telegram-bot channel (feature 33 `telegram-walkin-pin`) + the owner-recap export (feature 39 `owner-daily-recap-telegram`). The operator-facing recap export is the cross-section primitive.

## Dependencies

- **LE31 v1 status**: append-only StockEntry implemented (feature 3), owner-recap implemented (feature 39), cook Telegram bot implemented (feature 33). The ShopDesk pattern is the *demand-signal* for an offline-first wedge that LE31 v1 already partially supports.
- **External**: SQLite 3.x, python-barcode, python-escpos (the libraries ShopDesk likely uses — not adopted, just referenced for the demand-signal narrative).
- **Charter**: §3.1 + §3.2 compatible; §3.4 not triggered (zero AI); §3.3 not triggered (single-shop).

## Open questions

1. **Is the "5-year-old repo with single re-activation push" pattern a demand signal or a maintainer signal?** — the maintainer `devShakib015` may have re-pushed the repo for personal reasons (e.g. fixing a CV, archiving an old project), not because of a market event. The next pass should check `devShakib015`'s other repos for sustained maintenance cadence to disambiguate.
2. **Should LE31 v1 add a barcode surface?** — the ShopDesk pattern implies demand for barcode-driven order entry. LE31 v1's phone-first posture assumes the waiter scans + confirms on the phone, not on a dedicated barcode scanner. The owner decision is whether to add a barcode-scanner surface to the v1 waiter UI (decision deferred to first v1 PR that touches the order-entry surface).
3. **Should LE31 v1 add a thermal-receipt-printer surface?** — ShopDesk's thermal-receipts surface is a *demand-signal* for a v1 surface that prints a customer-facing receipt. LE31 v1's cook Telegram bot prints cook-facing order summaries, not customer-facing receipts. The owner decision is whether to add a customer-facing receipt surface (decision deferred to first v1 PR that touches the customer-experience surface).

## Why this matters

The ShopDesk pattern is the **demand-signal** for the LE31 v1 offline-first wedge. An independent maintainer in 2026 independently arrived at (stock as a ledger + SQLite + offline + barcode + day-close reports) as the *minimum-viable operator surface* — without reading the LE31 charter, without the LE31 §3.1/§3.2/§3.4 framework, without any of the 169 existing LE31 features. The pattern's contribution is the *demand-signal*: there is at least one independent operator in 2026 who wants the LE31 v1 surface shape (or something close to it). The 0★ is a popularity signal (§3.2 note: stars are not need-validation), not a negation. The stakeholder reasoning: if LE31 v1 ever proposes an offline-first wedge, the ShopDesk pattern is a *named architectural reference* + a *demand-signal* for the wedge.

## Distinct from existing features

Ripgrep-verified unique vs features/ 1–169 (2026-09-13). Sister-shape references:
- `03-kitchen-stock-tracker` — stock-tracking surface (LE31 v1 implements this already)
- `05-payment-tip-reconciliation` — payment surface (LE31 v1 implements this already)
- `26-reorder-point-on-stockentry` — reorder triggers (LE31 v1 implements this already)
- `34-stockout-prep-board-snapshot` — stockout surfacing (LE31 v1 implements this already)
- `40-satisfecho-python-pos-watch` — Python POS watch (AGPL-3.0 blocked; ShopDesk is the MIT alternative shape)
- `54-corner-mart-pos-double-entry` — small-shop POS pattern
- `69-owner-no-account-shift-recap-link` — operator-side recap (= "day-close reports")
- `131-puntovivo-fiscal-native-local-first-pos-cross-section` — offline-first POS pattern
- `165-ladle-restaurant-prep-forecasting-food-cost-leak-detection` — restaurant stock + recipe surface

The ShopDesk pattern is the **MIT-permissive, offline-first, single-shop, day-close-report surface** that complements the existing features. It is the demand-signal for the *offline-first wedge* that LE31 v1 already partially supports.

---

**End of feature contract.**
