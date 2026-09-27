# Feature 238 — acardozos-skardex-mit-kardex-web-application-materials-supplies-small-businesses-startups-simple-v2-small-business-inventory-vocabulary-reference (defer)

> **NEW observation (2026-09-27).** Documents in-window GitHub Search `small+business+ERP` query result: `acardozos/skardex` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂** (early-traction, no community adoption yet), Python, **pushed 2026-09-23T05:18:19Z** (in-window by `pushed_at` only — *4 days before fetch time*), **created 2026-09-20T15:21:13Z** (~7-day-old repo with in-window `pushed_at`; `created_at` is IN-WINDOW by ~7 days), **367 KB modest repo**, `default_branch=main`, archived=`False`). **No topics** (parent-verified from raw JSON: `"topics": []`). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-27): *"Simple Kardex: web application for managing materials and supplies in small businesses or startups. Its fundamental principle is simplicity."* The **simple + kardex + small-business + materials + supplies + web-application** sextuple-primitive + the *simple* discipline (the fundamental principle is simplicity) = the **strongest single v2 small-business-inventory-vertical vocabulary of the 58-pass series** (in the g7 small+business+ERP cluster which today returned only 1 in-window candidate). Bucket: **v2 small-business-inventory (parking-lot, future-v2-horizontal-expansion-vocabulary-reference)** — watch-list entry, zero build time today. **The 0★/0⑂ is explicitly NOT offered as evidence of restaurant need; the transferable item is the *simple-kardex* vocabulary**, not the *kardex* itself.

## Goal

Retain the **simple + kardex + small-business + materials + supplies + web-application** sextuple-primitive as a persistent cross-section reference for any future LE31 v2 surface that introduces (a) **simple** (the fundamental principle is simplicity), (b) **kardex** (a kardex-style FIFO/LIFO accounting layer for raw materials), (c) **small-business** (the target audience is small businesses, not enterprises), (d) **materials** (the inventory is materials, not finished goods), (e) **supplies** (the inventory is supplies, not merchandise), and (f) **web-application** (the surface is a web app, not a CLI or Telegram bot). The artifact is the persistent cross-section reference + the verbatim description. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 367 KB modest-repo size is comfortably readable).

## Scope

**In scope (defer artifact):**
- A written record of the **simple** discipline: the *simple-fundamental-principle* primitive (the fundamental principle of the vocabulary is simplicity; this is the *minimal-surface* posture applied to the small-business-inventory dimension; LE31 v1 already follows the *minimal-surface* discipline per charter §3.1, but the *kardex* surface has not been adopted yet).
- A written record of the **kardex** discipline: the *kardex-accounting* primitive (a kardex-style FIFO/LIFO accounting layer for raw materials; this is the *inventory-accounting* posture applied to the small-business-inventory dimension; LE31 v1's `StockEntry` schema tracks only *prepared-item quantities* but does NOT track *raw materials* + does NOT implement a kardex-style FIFO/LIFO accounting layer — the *kardex-accounting* discipline is a v2 future reference).
- A written record of the **small-business** discipline: the *small-business-vertical* primitive (the target audience is small businesses, not enterprises; this is the *single-tenant + small-footprint* posture applied to the inventory dimension; LE31 v1's charter §3.1 already follows the *single-restaurant-vertical* discipline but the *small-business-horizontal-expansion* posture is a v2 future reference).
- A written record of the **materials + supplies** discipline: the *materials-and-supplies* primitive (the inventory is materials + supplies, not finished goods; this is the *raw-inputs* posture applied to the inventory dimension; LE31 v1's `StockEntry` schema tracks *prepared-item quantities* but does NOT track *raw materials + supplies* — the *materials-and-supplies* layer is a v2 future reference).
- A written record of the **web-application** discipline: the *web-application* primitive (the surface is a web app, not a CLI or Telegram bot; this is the *browser-accessible* posture applied to the inventory dimension; LE31 v1 already follows the *waiter-web-UI + cook-Telegram-bot* discipline per charter §3.1, but the *owner-web-UI-for-kardex* surface has not been adopted yet).
- A decision record: today's verdict is `defer` because LE31 v1 has no inventory-of-raw-materials surface (charter §3.1 single-restaurant-vertical discipline); the cross-section reference is informative, not a v2 build-trigger.
- A cross-section reference with the prior v2 small-business-inventory + small-business-ERP + small-business-ledger cluster: features 170 (`devShakib015/ShopDesk` offline-POS-as-stock-ledger) + 172 (`bamideleadedeji-hybrid-inventory-restock-spreadsheet`) + 223 (`psb684/sketch-athena` ERP-inventory-management-small-business-SQLite from 09-23) + 224 (`celerp/celerp` NOASSERTION self-hosted FastAPI PostgreSQL ERP inventory management) + 225 (`anugrhaswi/shop-ledger` MIT self-hosted bookkeeping for small shops). The *transferable insight* is the **simple + kardex + small-business + materials + supplies + web-application** sextuple-primitive.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2 horizontal-expansion surface in v2 (charter §3.1 + §3.2 invariant: v2 surface expansion is the next boundary; this is a vocabulary reference, not a v2 expansion trigger).
- Any v2 raw-materials-inventory implementation in v2 (the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off).
- Any kardex-FIFO/LIFO accounting layer in v1 (LE31 v1 has no raw-materials-inventory surface; the *kardex-FIFO/LIFO* discipline is a v2 future reference).
- Any owner-web-UI-for-kardex surface in v1 (LE31 v1's owner surface is the existing waiter-web-UI + cook-Telegram-bot; the *owner-web-UI-for-kardex* surface is a v2 future reference).

## Description

The pick is **`acardozos/skardex`** — a Python + MIT + simple + kardex + small-business + materials + supplies + web-application vocabulary artifact. Charter §3.4 NOT triggered because the artifact has no AI surface at all (the *kardex* is a deterministic-inventory discipline, not an AI discipline). The *simple-kardex* is a vocabulary reference for the *raw-materials-inventory + small-business-inventory* dimensions; LE31 v1 has no `StockEntry` schema for raw materials + supplies today, but the *kardex* discipline is a plausible future v2 horizontal-expansion surface if the owner ever asks for raw-materials-inventory tracking. The artifact is the persistent cross-section reference for the verbatim description + the 6 named primitives.

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v2 surface that adopts the *kardex* primitive would extend the LE31 v1 data model with appropriate new tables (e.g., a `kardex_entry` table with `kardex_id, material_id, quantity, unit, fifo_lifo_flag, recorded_at, parent_kardex_id`; a `material` table with `material_id, material_name, material_category, unit, reorder_threshold, current_quantity`; a `supplier` table with `supplier_id, supplier_name, contact_info, last_order_date`). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v2 PR is triggered by the trigger condition below, the implementation would:
1. Read the `acardozos/skardex` README at https://github.com/acardozos/skardex for the *simple + kardex + small-business + materials + supplies + web-application* sextuple-primitive.
2. Cross-reference with LE31 v1's `StockEntry` schema to identify the *delta* (the *delta* = `acardozos/skardex` introduces kardex-style FIFO/LIFO accounting + raw-materials tracking + supplier tracking + reorder thresholds that LE31 v1's `StockEntry` schema does not have; LE31 v1's `StockEntry` schema tracks *prepared-item quantities* but does NOT track *raw materials + supplies* + does NOT implement FIFO/LIFO accounting).
3. Apply charter §3.1 *single-restaurant-vertical + small-footprint* review to the *delta* (any new v2 surface requires explicit owner/charter sign-off; the *kardex* surface is a hypothetical v2 horizontal-expansion that the owner may or may not request).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the `acardozos/skardex` reference is the *vocabulary* for *simple + kardex + small-business + materials + supplies + web-application*, NOT for *kardex replacement*.

## Telegram interaction

Zero new Telegram interaction today. Future v2 PR that adopts the *kardex* primitive would extend the existing aiogram-bot (cook-bot per charter §3.1) with a *kardex-status* command set that allows the operator to query kardex status (e.g., `/kardex list` → list of materials with current quantities; `/kardex show <material_id>` → show a material with its reorder threshold; `/kardex receive <material_id> <quantity>` → record a material receipt). The *kardex-status* discipline is *operator-tooling* (operator queries the kardex status), NOT customer-facing-AI; charter §3.4 is NOT triggered.

## Dependencies

- LE31 charter §3.1 surface-expansion review (for any v2 surface adoption).
- LE31 charter §3.2 surface-expansion review (for any v2 surface adoption).
- LE31 charter §3.2 license-compatible (MIT permissive; future code adoption is possible).
- Features 170, 172, 223, 224, 225.
- Cross-section reference `acardozos/skardex` at https://github.com/acardozos/skardex (MIT, 0★/0⑂, Python, simple + kardex + small-business + materials + supplies + web-application).

## Open questions

- Will LE31 v2 ever introduce a raw-materials-inventory surface? If yes, `acardozos/skardex` is the vocabulary reference.
- Will LE31 v2 ever introduce a kardex-style FIFO/LIFO accounting layer (vs the current `StockEntry` schema which tracks *prepared-item quantities* but not *raw materials + FIFO/LIFO*)? If yes, `acardozos/skardex` is the vocabulary reference.
- Will LE31 v2 ever introduce a small-business-horizontal-expansion surface (vs the current charter §3.1 single-restaurant-vertical discipline)? If yes, `acardozos/skardex` is the vocabulary reference.
- Will LE31 v2 ever introduce an owner-web-UI-for-kardex surface (vs the current waiter-web-UI + cook-Telegram-bot + existing owner surfaces)? If yes, `acardozos/skardex` is the vocabulary reference.
- The 0★/0⑂ is explicitly NOT offered as evidence of *LE31 needing a kardex*; the 0★/0⑂ is for the *kardex domain*, not for the *LE31 operational* primitive. The transferable item is the *technique* (simple + kardex + small-business + materials + supplies + web-application), not the *kardex* itself.
- **Open question that may kill any future PR**: does the LE31 owner want raw-materials-inventory tracking? Charter §3.1 single-restaurant-vertical discipline is silent on this; the owner has not requested it in any of the 58 daily-research passes. The *kardex* surface may never be built because the operational need may not exist.
- **Open question that may kill any future PR**: would LE31 v2 adopt the *simple* discipline at the cost of feature richness? The *simple* posture may be too restrictive for the v2 horizontal-expansion surface if the owner wants rich inventory analytics.

## Why this matters

The verbatim description in `acardozos/skardex` is the **canonical v2 small-business-inventory-vertical vocabulary** that LE31 v1's `StockEntry` (feature/charter §3.1) and v2's future raw-materials-inventory surface would inherit. Specifically: (i) **simple** (the *simple-fundamental-principle* primitive) is the *minimal-surface* posture; (ii) **kardex** (the *kardex-accounting* primitive) is the *inventory-accounting* posture; (iii) **small-business** (the *small-business-vertical* primitive) is the *single-tenant + small-footprint* posture; (iv) **materials + supplies** (the *materials-and-supplies* primitive) is the *raw-inputs* posture; (v) **web-application** (the *web-application* primitive) is the *browser-accessible* posture. When v2 introduces any of these 6 primitives, `acardozos/skardex` is the vocabulary reference. **HONEST DISCLOSURE**: `acardozos/skardex`'s 0★/0⑂ is for the *kardex domain*, not for the *LE31 operational* primitive; the 0★/0⑂ is explicitly NOT offered as evidence of LE31's need for the kardex. **WEAK SIGNAL**: the 0★/0⑂ + the ~7-day-old repo + the small (367 KB) size = the *weakest* of today's 3 picks; the verdict is `defer, parking-lot` with the explicit understanding that the owner has not requested this surface and the operational need is hypothetical.