# Feature 171 — `bamideleadedeji-hybrid-inventory-restock-spreadsheet` (parking-lot)

> **NEW observation (2026-09-13).** Documents in-window GitHub repo `bamideleadedeji/Hybrid_Inventory_Restock_Master.xlsx` (note `.xlsx` extension in repo name; **0★/0⑂**, **MIT**, Python per `language` field, **pushed 2026-09-12T13:37:02Z**, in-window by create+push, 10 KB, **created 2026-09-12T13:24:52Z — 12-minute-old repo at push time**). Description (verbatim from GitHub API, parent-verified direct-GET 2026-09-13): *"Automate multi-department stock control with the International Hybrid Retail, Pharmacy & Restaurant Inventory Suite. Built for mini-marts, pharmacy outlets, boutiques, and supermarket-bistros, this mobile Google Sheets & Excel template tracks retail units, pharmacy batch expiry, kitchen raw materials, and triggers stockout alerts."* Topics (verbatim from raw JSON, parent-verified): `[]` (none). Bucket: **new (meta-brainstorm — questioning the v1 architecture choice via the existence of this repo)** — pick B of Brainstorm 2026-09-13. Build verdict: **parking-lot**. Zero build time today. The artifact is the *named architectural question* ("what does LE31 add that earns its way OFF Google Sheets?"), not a code-adoption opportunity.

## Goal

Retain the **"lowest-effort-UX operator surface is a Google Sheets template, not a web app"** observation as a persistent meta-brainstorm on the LE31 v1 product wedge, and document the *what-LE31-earns-its-way-OFF-spreadsheets* question as a discrete architecture decision the v1 product owner must answer. The artifact is the persistent cross-section reference + a meta-brainstorm on the v1 architecture choice. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"lowest-effort-UX operator surface"** observation: for "small restaurant with no IT", the operator surface that wins today is a Google Sheets template, not a web app. The Hybrid_Inventory_Restock_Master.xlsx pattern is the *de-facto incumbent* for the operator surface that LE31 v1 proposes to replace.
- A written record of the **"what does LE31 add that earns its way OFF Google Sheets?"** product-wedge question. The candidate answers (any of which could be the v1 product-wedge answer):
  - **Multi-user concurrency** (Sheets has it but version conflicts are brutal — last-writer-wins loses data)
  - **Structured audit log** (`audit_logs` table, not formula history)
  - **Telegram-cook channel** (Sheets doesn't speak Telegram; the cook-facing surface is a different medium)
  - **Owner-recap export** (Sheets has it but it's read-only; LE31 can push daily recaps)
  - **Append-only StockEntry** (Sheets has it but the user can break the append-only discipline by editing a cell; LE31 enforces it at the DB layer)
- A written record of the **"multi-industry scope (retail + pharmacy + restaurant)"** dilution: the repo serves four industries, which means the restaurant-specific features are watered down. LE31 v1's wedge is the *restaurant-specific* surface, not the multi-industry surface.
- A decision record: today's verdict is `parking-lot` because (1) the repo is 0★ with single-maintainer cadence; (2) the actual logic is in a spreadsheet, not in Python (despite `language:Python` in the GitHub-search qualifier); (3) the *insight* — that spreadsheets-as-LE31 is the de-facto incumbent — is the value, not the code.

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot (charter §3.1: explicit state transitions; v1 surfaces are sufficient for v1 ops).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the spreadsheet template (the artifact is in `.xlsx` format, not Python; the maintainer may have a Python script that generates the spreadsheet, but the *logic* is in spreadsheet formulas).
- Cross-pollination with charter §3.4 AI surface (the spreadsheet template has zero AI — pure formula-driven; §3.4 compatible).
- Cross-pollination with charter §3.3 (the spreadsheet is single-user; multi-tenant is not in scope).

## Evidence / JTBD

When the LE31 v1 product owner asks *"is there demand for an offline-first restaurant-POS?"*, the answer is yes (feature 170 / ShopDesk proves it). When the owner asks the deeper question *"is there demand for a *web app* in the same space as the spreadsheet alternative?"*, the answer is more nuanced: the spreadsheet already serves the low-end operator (single-user, no IT, multi-industry). LE31 v1's wedge is the *restaurant-specific, multi-user, audit-logged, Telegram-integrated* surface — the four things the spreadsheet *cannot* do. The brainstorm writes the test; LE31 v1 design must answer it.

- **Evidence class**: observed (the Hybrid_Inventory_Restock_Master.xlsx description + filename `.xlsx` extension signal the spreadsheet-template pattern explicitly).
- **Confidence**: medium for the demand signal (the description is direct; the spreadsheet-template market is well-established; the LE31 owner has likely already considered this trade-off); low for the *meta-brainstorm value* (the brainstorm value is the *naming* of the wedge question, not the answer).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is web-first, not spreadsheet-first); the value is the *naming of the wedge question*.
- **The value is naming, not direct demand**: when the first v1 PR lands that proposes a v1 surface for the offline-first / single-shop / no-IT operator, the Hybrid_Inventory_Restock_Master.xlsx pattern is a ready-made *named counter-example* + the *naming of the four candidate wedge answers* (multi-user concurrency / structured audit log / Telegram-cook channel / owner-recap export).

## Description

GitHub `bamideleadedeji/Hybrid_Inventory_Restock_Master.xlsx` (MIT, 0★/0⑂, Python per `language` field, pushed 2026-09-12T13:37:02Z, created 2026-09-12T13:24:52Z, 10 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-13): *"Automate multi-department stock control with the International Hybrid Retail, Pharmacy & Restaurant Inventory Suite. Built for mini-marts, pharmacy outlets, boutiques, and supermarket-bistros, this mobile Google Sheets & Excel template tracks retail units, pharmacy batch expiry, kitchen raw materials, and triggers stockout alerts."*

The architectural pattern has one core observation and four sub-observations:

1. **"Lowest-effort-UX is a Google Sheets template"** — for "small restaurant with no IT", the operator surface that wins today is a Google Sheets template (or Excel spreadsheet) — *not* a web app, *not* a mobile app, *not* a desktop app. The reasoning: zero install, zero IT setup, zero vendor lock-in, free.
2. **"Multi-department stock control with stockout alerts"** — the spreadsheet tracks (a) retail units, (b) pharmacy batch expiry, (c) kitchen raw materials, (d) stockout triggers. The features are *aggregated*, not restaurant-specific.
3. **"Mobile Google Sheets & Excel"** — the spreadsheet is designed for mobile access (Google Sheets mobile app, Excel mobile app), not for desktop. The mobile-first design is consistent with the LE31 phone-first posture.
4. **"Multi-industry scope (retail + pharmacy + restaurant)"** — the spreadsheet serves four industries, which means the restaurant-specific features are watered down. LE31 v1's wedge is the *restaurant-specific* surface, not the multi-industry surface.

**The 1:1 mapping onto LE31 v1 architecture (offline-first wedge):**

| Hybrid_Inventory_Restock_Master.xlsx primitive | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| Multi-department stock control | `StockEntry` per department | §3.1 ✓ | **Implemented (v1)** |
| Pharmacy batch expiry | (LE31 v1 has no batch expiry surface; would require an `expires_at` field on `StockEntry`) | not in v1 | **Not implemented** — cross-section with feature 153 `sausageos-production-erp-append-only-stock-fefo-versioned-recipes` |
| Kitchen raw materials | `StockEntry` for kitchen raw materials | §3.1 ✓ | **Implemented (v1)** |
| Stockout triggers | `reorder-point-on-stockentry` (feature 26) + `shelf-threshold-receiving-bot` (feature 28) | v1 ✓ | **Implemented (v1)** |
| Mobile-first spreadsheet | Phone-first web UI | §3.1 ✓ | **Implemented (v1 but different medium)** |
| Multi-user concurrency (last-writer-wins) | (LE31 v1 has row-level locking + audit log; spreadsheet loses data on concurrent edits) | §3.1 ✓ | **Implemented (v1 wins over spreadsheet)** |
| Structured audit log | `audit_logs` (append-only) | §3.1 ✓ | **Implemented (v1 wins over spreadsheet)** |
| Telegram-cook channel | (LE31 v1 cook Telegram bot; spreadsheet doesn't speak Telegram) | §3.1 ✓ | **Implemented (v1 wins over spreadsheet)** |
| Append-only discipline (enforced) | (LE31 v1 enforces at DB layer; spreadsheet user can break it by editing a cell) | §3.1 ✓ | **Implemented (v1 wins over spreadsheet)** |
| Single-user | (LE31 v1 supports multi-user with audit log; spreadsheet is single-user) | §3.1 ✓ | **Implemented (v1 wins over spreadsheet)** |

The mapping table makes the case: **LE31 v1's wedge is the *structured audit log + multi-user concurrency + Telegram-cook channel* set** — the four things the spreadsheet *cannot* do. The spreadsheet is the *minimum-viable operator surface*; LE31 v1 is the *restaurant-specific, multi-user, audit-logged, Telegram-integrated* surface.

## Data model

**No schema change today.** The defer artifact is documentation only.

The pattern itself does not require a schema change — the LE31 v1 schema already implements the *restaurant-specific, multi-user, audit-logged* surface.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v1 implementation would include:
1. None — the v1 surface is already implemented. The Hybrid_Inventory_Restock_Master.xlsx pattern is the *naming of the wedge question*, not a code-adoption opportunity.

**No existing code change today.**

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

Future v1: if the owner approves a feature that adds a *spreadsheet-export* surface (e.g. an "Export to Google Sheets" button on the owner-recap), the spreadsheet pattern becomes a *named companion surface*. The owner-recap export (feature 39 `owner-daily-recap-telegram`) is the LE31-native operator-surface-shape; the spreadsheet export would be a *secondary* surface for operators who prefer spreadsheets.

## Dependencies

- **LE31 v1 status**: append-only StockEntry implemented (feature 3), multi-user concurrency implemented (row-level locking on `StockEntry` + `audit_logs`), structured audit log implemented (`audit_logs` table), Telegram-cook channel implemented (feature 33 `telegram-walkin-pin`), owner-recap implemented (feature 39 `owner-daily-recap-telegram`), reorder-point implemented (feature 26 `reorder-point-on-stockentry`), shelf-threshold implemented (feature 28 `shelf-threshold-receiving-bot`).
- **External**: Google Sheets API, Excel file format (the libraries the spreadsheet template likely uses — not adopted, just referenced for the meta-brainstorm narrative).
- **Charter**: §3.1 + §3.2 + §3.3 + §3.4 all compatible (zero AI, single-restaurant scope).

## Open questions

1. **Is the spreadsheet-template market a real threat to LE31 v1 adoption?** — if the operator can use a free Google Sheets template, why would they pay for LE31 v1? The answer is the four wedge answers above (multi-user / audit log / Telegram / append-only-enforced), but the operator may not realize they need those features until they hit the limitation. The owner decision is whether to add a *spreadsheet-import* surface (so a Sheets-using operator can migrate to LE31) or to *not address* the spreadsheet market.
2. **Should LE31 v1 add a spreadsheet-export surface?** — the operator-recap could be exported to Google Sheets for the operator who wants to analyze the data in a spreadsheet. This is a v2 surface (LE31 v1 is web-first; the spreadsheet export is an optional secondary surface). Decision deferred.
3. **Should LE31 v1 add a spreadsheet-import surface?** — an operator who is currently using a Google Sheets template could migrate to LE31 v1 by importing the spreadsheet. This is a v2 surface. Decision deferred.

## Why this matters

The Hybrid_Inventory_Restock_Master.xlsx pattern is the **meta-brainstorm** on the LE31 v1 architecture choice. The question is not *"is there demand for offline-first restaurant-POS?"* (ShopDesk / feature 170 answers yes), it is *"is there demand for a *web app* in the same space as the spreadsheet alternative?"* The spreadsheet is the *de-facto incumbent*; LE31 v1 is the *wedge* that adds the four things the spreadsheet *cannot* do (multi-user / audit log / Telegram / append-only-enforced). The brainstorm writes the test; the LE31 v1 design must answer it. The 0★ is a popularity signal (§3.2 note: stars are not need-validation), not a negation. The stakeholder reasoning: if LE31 v1 ever proposes a v1 surface that competes with the spreadsheet alternative, the Hybrid_Inventory_Restock_Master.xlsx pattern is a *named counter-example* + the *naming of the four candidate wedge answers*.

## Distinct from existing features

Ripgrep-verified unique vs features/ 1–169 (2026-09-13). Sister-shape references:
- `03-kitchen-stock-tracker` — stock-tracking surface (LE31 v1 implements this already)
- `15-inventory-variance` — multi-department variance (LE31 v1 implements this already)
- `16-supplier-orders` — restock workflow (LE31 v1 implements this already)
- `26-reorder-point-on-stockentry` — reorder triggers (LE31 v1 implements this already)
- `28-shelf-threshold-receiving-bot` — stockout-alert pattern (LE31 v1 implements this already)
- `34-stockout-prep-board-snapshot` — stockout surfacing (LE31 v1 implements this already)
- `65-cook-photo-stock-list-pwa` — operator-side stock list (LE31 v1 implements this already)
- `66-offline-first-pwa-transactional-arch` — offline-first pattern (LE31 v1 implements this already)
- `153-sausageos-production-erp-append-only-stock-fefo-versioned-recipes` — production ERP with FEFO + versioned recipes (cross-section on the *batch expiry* primitive)

The Hybrid_Inventory_Restock_Master.xlsx pattern is the **named counter-example** to LE31 v1 — the spreadsheet is the *minimum-viable operator surface*; LE31 v1 is the *restaurant-specific, multi-user, audit-logged, Telegram-integrated* wedge that adds the four things the spreadsheet *cannot* do.

---

**End of feature contract.**
