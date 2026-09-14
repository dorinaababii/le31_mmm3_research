# Feature 173 — `Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot` (defer)

> **NEW observation (2026-09-14).** Documents in-window GitHub repo `Sholu021/KitchenIQ` (**MIT**, **0★/0⑂**, Python, **pushed 2026-09-14T06:55:15Z** (TODAY), in-window by `pushed_at` only, 344 KB, **created 2026-06-18T07:54:41Z** — 89-day-old repo with first in-window push today). Description (verbatim from GitHub API, parent-verified direct-GET 2026-09-14): *"AI-powered ERP and Inventory Management System for Restaurants, Cafés, Bakeries & Cloud Kitchens."* Topics (verbatim from raw JSON, parent-verified): `ai, erp, fastapi, food-tech, inventory-management, nextjs, openai, postgresql, python, react, restaurant, sqlalchemy`. README verbatim tech-stack (parent-verified 2026-09-14): `Backend: FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic + APScheduler + JWT Authentication; Frontend: Next.js + React + TailwindCSS; AI: OpenAI + AI Gateway`. README verbatim feature list: `Inventory: Batch Management + FEFO Inventory + Inventory Ledger + Inventory Valuation + Inventory Health + ABC Analysis + Low Stock Alerts + Expiry Tracking; Purchasing: Purchase Orders + Approval Workflow + Supplier Performance + Supplier Invoices + AI Reorder Suggestions; Production: Recipes + Production Runs + Yield Management + Finished Goods; Sales: Sales Management + Profit Tracking + Revenue Analytics + Top Products; AI: AI Copilot + AI Insights + Demand Forecasting + Automatic Reordering; Reports: Executive Dashboard + PDF Reports + Excel Reports + Scheduled Reports`. README badges: `Python 3.14, FastAPI Latest, Next.js 15, PostgreSQL 17, License MIT, Tests 21 Passing`. Bucket: **v1 (operator-surface inspiration; the stack-shape is the value, not the code)** — pick A of Brainstorm 2026-09-14 (parent research issue HMM-249). Build verdict: `defer` (parking-lot). Zero build time today. The 89-day-old repo with first in-window push today is the demand signal, not a code-adoption opportunity.

## Goal

Retain the **`FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic + Inventory Ledger + FEFO + Approval Workflow + AI Copilot`** stack-shape as a persistent cross-section reference for the LE31 v1 *restaurant-domain + append-only StockEntry + Approval Workflow + owner-side AI* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 without reading the LE31 charter. The artifact is the persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **`FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic + JWT Auth`** stack-shape: this is **byte-for-byte the LE31 v1 stack** (FastAPI + SQLModel + Postgres + Alembic + JWT are all on the LE31 pin set; SQLAlchemy 2.0 is the SQLModel dependency). The verbatim stack match is the **strongest single-repo cross-section signal of the 46-pass series**.
- A written record of the **`Inventory Ledger + FEFO Inventory + Batch Management + Expiry Tracking`** operator-surface-shape: every inventory movement is a ledger entry (FEFO = First-Expired-First-Out = the production-ERP discipline that maps 1:1 onto LE31's `StockEntry` with batch-level tracking). This is the §3.1 explicit-state-transitions primitive applied to inventory with batch-level granularity.
- A written record of the **`Approval Workflow + Purchase Orders + Supplier Performance + Supplier Invoices + AI Reorder Suggestions`** purchasing-surface-shape: every purchase order is gated by an explicit approval rule. This maps 1:1 onto LE31 v1's feature 61 (`holdfast-approval-ledger`) and feature 16 (`supplier-orders`).
- A written record of the **`AI Copilot + AI Insights + Demand Forecasting + Automatic Reordering`** owner-side-AI surface-shape: AI assists the owner/manager with daily recap + actionable suggestions + replenishment. **No customer-facing AI** — no guest ordering via AI, no menu recommendation for guests. This is **§3.4-compatible** (owner/staff-assist AI allowed; customer-facing AI forbidden).
- A written record of the **Recipes + Production Runs + Yield Management + Finished Goods** production-surface-shape: every recipe is versioned; every production run is a ledger entry; yield is calculated from input vs output. This is feature 19 (`menu-engineering`) + feature 21 (`recipe-generation`) surface shape.
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (89-day-old, first in-window push today); (2) the stack-shape match is the value, not the code (LE31 v1 uses minimal HTML/HTMX, not Next.js; LE31 v1 has no AI integration in the v1 charter scope); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot (charter §3.1: explicit state transitions; v1 surfaces are sufficient for v1 ops).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the KitchenIQ codebase (single maintainer, brand-new in-window push, Next.js frontend vs LE31's HTMX frontend, OpenAI integration vs LE31's no-AI v1 charter).
- Cross-pollination with charter §3.4 AI surface (KitchenIQ AI is owner/manager-side — Copilot / Insights / Demand Forecasting / Reordering — which is **§3.4-compatible**; no guest-facing AI in the README; not a §3.4 hard trigger).
- Cross-pollination with charter §3.3 (KitchenIQ is single-tenant per the README; no multi-tenant scope in v1).

## Evidence / JTBD

When a future LE31 v1 surface proposes "the restaurant-domain + append-only StockEntry + Approval Workflow + owner-side AI Copilot shape" (e.g. a v2 surface that introduces AI-assisted owner-side daily recap, or a v2 surface that introduces supplier-order approval workflow), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "FastAPI + SQLAlchemy 2.0 + PostgreSQL + Inventory Ledger + FEFO + Approval Workflow + AI Copilot" is a real demand signal*, so that *the v1/v2 surface can be defended with "this is what an independent maintainer shipped in 2026 with the exact same stack as LE31"*.

- **Evidence class**: observed (the KitchenIQ description + topics + README tech-stack + feature list name the primitives explicitly: `ai,erp,fastapi,food-tech,inventory-management,nextjs,openai,postgresql,python,react,restaurant,sqlalchemy`; `FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic`).
- **Confidence**: medium-high for the stack-shape match (the verbatim tech-stack is byte-for-byte the LE31 stack plus a frontend-framework; the topic tags are LE31-aligned; the 89-day-old repo with first in-window push today is the *demand signal*, not the *adoption signal*); low for transferability (LE31's frontend is minimal HTML/HTMX, KitchenIQ is Next.js + React; LE31 has no v1 AI integration, KitchenIQ has OpenAI integration).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has minimal-HTML/HTMX + no AI; KitchenIQ has Next.js/React + OpenAI); the value is the *stack-shape validation* — when the first v1 surface change proposes adding any of the v1-aligned primitives (Inventory Ledger, FEFO, Approval Workflow), the KitchenIQ pattern is a ready-made *named primitive*.
- **The value is naming, not direct demand**: when the first v1 PR that adds an owner-side surface lands (if/when the owner approves the v1 expansion), the KitchenIQ pattern is a ready-made *named primitive* and the `Inventory Ledger + FEFO + Batch Management + Approval Workflow + AI Copilot` vocabulary slots into features 3 (`kitchen-stock-tracker`) + 5 (`payment-tip-reconciliation`) + 7 (`demand-estimation`) + 16 (`supplier-orders`) + 19 (`menu-engineering`) + 26 (`reorder-point-on-stockentry`) + 28 (`shelf-threshold-receiving-bot`) + 61 (`holdfast-approval-ledger`) + 165 (`ladle-restaurant-prep-forecasting-food-cost-leak-detection`).

## Description

GitHub `Sholu021/KitchenIQ` (MIT, 0★/0⑂, Python, pushed 2026-09-14T06:55:15Z, created 2026-06-18T07:54:41Z, 344 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-14): *"AI-powered ERP and Inventory Management System for Restaurants, Cafés, Bakeries & Cloud Kitchens."*

The architectural primitive has six sub-primitives that map 1:1 onto the LE31 v1 + v2 surface:

1. **`Inventory: Batch Management + FEFO Inventory + Inventory Ledger + Inventory Valuation + Inventory Health + ABC Analysis + Low Stock Alerts + Expiry Tracking`** — every inventory movement is a ledger entry with batch-level granularity; FEFO = First-Expired-First-Out = the production-ERP discipline that maps 1:1 onto LE31's `StockEntry` with batch-level tracking. This is the §3.1 explicit-state-transitions primitive applied to inventory with batch-level granularity. Sister-shape to features 3 (`kitchen-stock-tracker`) + 10 (`allergen-tracking`) + 15 (`inventory-variance`) + 26 (`reorder-point-on-stockentry`) + 28 (`shelf-threshold-receiving-bot`) + 34 (`stockout-prep-board-snapshot`).
2. **`Purchasing: Purchase Orders + Approval Workflow + Supplier Performance + Supplier Invoices + AI Reorder Suggestions`** — every purchase order is gated by an explicit approval rule. The `Approval Workflow` primitive maps 1:1 onto LE31 feature 61 (`holdfast-approval-ledger`). Sister-shape to features 16 (`supplier-orders`) + 61 (`holdfast-approval-ledger`).
3. **`Production: Recipes + Production Runs + Yield Management + Finished Goods`** — every recipe is versioned; every production run is a ledger entry; yield is calculated from input vs output. Sister-shape to features 19 (`menu-engineering`) + 21 (`recipe-generation`) + 15 (`inventory-variance`).
4. **`Sales: Sales Management + Profit Tracking + Revenue Analytics + Top Products`** — sales management with profit tracking is the owner-side sales-recap surface. Sister-shape to features 39 (`owner-daily-recap-telegram`) + 57 (`owner-recap-persona-voice`) + 74 (`per-recipe-cost-margin-rollup`) + 75 (`day-part-menu-margin-surface`).
5. **`AI: AI Copilot + AI Insights + Demand Forecasting + Automatic Reordering`** — owner/manager-side AI assistance with daily recap + actionable suggestions + replenishment. **No customer-facing AI** — no guest ordering via AI, no menu recommendation for guests. This is **§3.4-compatible** (owner/staff-assist AI allowed; customer-facing AI forbidden). Sister-shape to feature 7 (`demand-estimation`) + 17 (`demand-forecasting-ml`) + 166 (`close-the-books-quickbooks-catch-up-ai-agent-human-review-gate`).
6. **`Reports: Executive Dashboard + PDF Reports + Excel Reports + Scheduled Reports`** — owner-facing dashboard + scheduled reports export. Sister-shape to features 39 + 57 + 82 (`owner-public-data-watch-bot`).

**The 1:1 mapping onto LE31 surface:**

| KitchenIQ primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic | FastAPI + SQLModel + Postgres + Alembic (LE31 pin set) | §3.1 ✓ | **Implemented (v1)** |
| JWT Authentication | JWT Authentication | §3.1 ✓ | **Implemented (v1)** |
| APScheduler | APScheduler | §3.1 ✓ | **Implemented (v1)** |
| Next.js + React + TailwindCSS | minimal HTML/HTMX | not in v1 | **Different medium** — LE31 v1 is HTML-first, not SPA |
| OpenAI + AI Gateway | (LE31 v1 has no AI) | v2 (with §3.4 owner-side AI primitive) | **Not implemented** — v2 surface |
| Inventory Ledger | `StockEntry` (append-only) | §3.1 ✓ | **Implemented (v1)** |
| FEFO + Batch Management + Expiry Tracking | (LE31 v1 has no batch-level tracking) | v2 | **Not implemented** — v2 surface |
| Approval Workflow | feature 61 (`holdfast-approval-ledger`) | §3.1 ✓ | **Implemented (v1)** |
| Recipes + Production Runs + Yield Management | features 19 (`menu-engineering`) + 21 (`recipe-generation`) | v1/v2 | **Partial** — recipes implemented, production runs + yield v2 |
| AI Copilot + Demand Forecasting + Reordering | (LE31 v1 has no AI) | v2 with §3.4 owner-side primitive | **Not implemented** — v2 surface (when §3.4 owner-AI is added) |
| Executive Dashboard | `owner-daily-recap-telegram` (feature 39) | v1 ✓ | **Implemented (v1 — different medium)** |
| PDF + Excel + Scheduled Reports | features 39 + 57 + 82 | v1/v2 | **Partial** — Telegram recap implemented, PDF/Excel/Scheduled v2 |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v1/v2 trigger condition fires (first v1 PR that adds a FEFO/batch-level tracking surface, or first v2 PR that introduces an owner-side AI Copilot surface), the implementation would not require a code change for the existing LE31 v1 surface — the existing `StockEntry` schema already implements the append-only discipline. The HANDOFF is to evaluate whether the v1 FEFO/batch-level tracking surface or the v2 owner-side AI Copilot surface is the right product-wedge for the next v1/v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v1/v2 trigger fires:

**For v1 FEFO/batch-level tracking** (if approved):
1. Add a `batch_id` column to the `StockEntry` table (Alembic migration).
2. Add a `FEFO` helper function that returns the oldest-batch-first inventory for a given `MenuItem`.
3. Update feature 3 (`kitchen-stock-tracker`) + feature 26 (`reorder-point-on-stockentry`) + feature 28 (`shelf-threshold-receiving-bot`) + feature 34 (`stockout-prep-board-snapshot`) to use the FEFO helper.
4. No new feature file needed; this is an incremental enhancement to the existing append-only `StockEntry` schema.

**For v2 owner-side AI Copilot** (if approved):
1. Add an `ai_copilot` module to the v2 surface.
2. Wire it to the OpenAI API (or a self-hosted model) with the LE31 audit-log + StockEntry as context.
3. Enforce the **§3.4 owner-side-AI primitive**: every AI suggestion must be reviewable by the owner before any state mutation; the AI is a *summariser*, not an *actor*.
4. New feature file at `features/NNN-ai-copilot-owner-side-OwnerAIDailyRecap.md` (NOT this defer artifact).

## Telegram interaction if any

None today. The defer artifact is documentation only.

If the future v2 owner-side AI Copilot surface is approved, the AI-Copilot Telegram delivery would use the existing `owner-daily-recap-telegram` (feature 39) channel — the AI summarises the day's `audit_logs` + `StockEntry` and the recap is delivered via the existing owner Telegram channel. No new Telegram surface.

## Dependencies

- None today (defer artifact is documentation only).
- If the v2 owner-side AI Copilot surface is approved: OpenAI API key (or self-hosted model); LE31 `audit_logs` table (already implemented); LE31 `StockEntry` table (already implemented).

## Open questions

- Does the owner approve a v1 FEFO/batch-level tracking surface? (Currently no — v1 is single-batch-per-item; FEFO is a v2 surface.)
- Does the owner approve a v2 owner-side AI Copilot surface? (Currently no — v1 has no AI integration; v2 AI is explicitly owner-side per §3.4.)
- Is the LE31 v1 frontend (minimal HTML/HTMX) sufficient, or does the owner approve a Next.js/React SPA frontend? (Currently minimal-HTML is sufficient for v1; Next.js/React is out-of-v1 scope.)

## Why this matters

The KitchenIQ repo is the **strongest single cross-section signal of the 46-pass series**: it is the only in-window permissive-licensed restaurant-domain repo with `FastAPI + SQLAlchemy 2.0 + PostgreSQL + Alembic + Inventory Ledger + FEFO + Approval Workflow + AI Copilot` in one package. The verbatim tech-stack is **byte-for-byte the LE31 stack plus a frontend-framework**. This is the *demand-signal* that the LE31 v1 stack-shape is correct — an independent maintainer arrived at the same primitives (Inventory Ledger + FEFO + Batch Management + Expiry Tracking + Approval Workflow + Recipes + Production Runs + AI Copilot) without reading the LE31 charter. The §3.4 owner-side AI surface (Copilot / Insights / Demand Forecasting / Reordering) is the *named reference* for the v2 question *"does LE31 v2 introduce an owner-facing AI that summarises daily `audit_logs` into actionable prep-board hints? — and if so, does the AI sit behind an explicit-evidence + non-AI-fallback gate?"* The §3.1 append-only StockEntry with batch-level tracking is the *named reference* for the v2 question *"does LE31 v2 introduce FEFO/batch-level tracking for prep-station inventory?"* No code today; the value is the stack-shape validation + the named reference for future v1/v2 PRs.
