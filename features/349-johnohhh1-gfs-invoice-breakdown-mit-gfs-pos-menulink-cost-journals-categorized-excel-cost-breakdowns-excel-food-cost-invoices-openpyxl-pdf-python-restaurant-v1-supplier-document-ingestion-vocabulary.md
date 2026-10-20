# Feature 349 — `johnohhh1-gfs-invoice-breakdown-mit-turn-gordon-food-service-pos-and-menulink-cost-journals-into-categorized-excel-cost-breakdowns-excel-food-cost-invoices-openpyxl-pdf-python-restaurant-v1-supplier-document-ingestion-vocabulary` (defer)

> **NEW observation (2026-10-20).** Documents in-window GitHub repo `johnohhh1/gfs-invoice-breakdown` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE** (the only pick with strict-permissive license; **code-shape adoptable per §3.2**), **0★/0⑂**, **18 KB tiny = THE SMALLEST pick of the 82-pass series** (vs pass-81 Pick B 2025 KB = 0.9% of pass-81's smallest pick), **Python ✓ ON-STACK** + openpyxl + pdf + excel + food-cost + invoices + restaurant, **pushed 2026-10-15T16:08:18Z AND created 2026-10-15T16:08:11Z = IN-WINDOW BY BOTH FIELDS** (~5-day-old repo; same-instant push), default_branch=undefined, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-20): *"Turn Gordon Food Service POs and MenuLink cost journals into categorized Excel cost breakdowns"*. Topics (verbatim, parent-verified, **7 topics**): `excel, food-cost, invoices, openpyxl, pdf, python, restaurant`. Bucket: **v1 (supplier-document-ingestion-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT-vocabulary)** — Pick C of Daily Brainstorm 2026-10-20. Build verdict: `defer` (parking-lot; **vocabulary reference**; **code-shape adoptable per §3.2** because MIT permissive).

## Goal

Retain the **vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT** vocabulary as a persistent cross-section reference for the LE31 v1 *supplier-document-ingestion + Italian-only-market-scope* wedge, and document the **vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT** primitive that an independent maintainer shipped in 2026 (the 7-topic array + the *parse-the-blob-then-categorise* posture IS the canonical §3.1 + §3.4 + §3.5 + §3.7 *no-account + upload-document-get-structured-sheet-back + zero-UI + deterministic kernel + Italian-only-market-scope + minimal-PII-only-aggregator-bridge* charter invariant applied to the *supplier-document-ingestion* dimension) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 *supplier-document-ingestion* gap-area. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT** 4-tuple-primitive: vendor-specific procurement artifacts (Gordon Food Service POs, MenuLink cost journals) normalised into a categorized Excel cost breakdown — the primitive is *PARSE-THE-BLOB-THEN-CATEGORISE*, at 18 KB, with zero UI. It is the **smallest example this pass of a complete inbound-artifact pipeline**: PDF in, openpyxl workbook out, MIT licensed. Transferable shape: **the operator pastes/uploads a supplier document and gets a structured sheet back, with no account, no dashboard, no session.** This is the canonical §3.1 + §3.4 + §3.5 + §3.7 *no-account + upload-document-get-structured-sheet-back + zero-UI + deterministic kernel + Italian-only-market-scope + minimal-PII-only-aggregator-bridge* invariant applied to the *supplier-document-ingestion* dimension.
- A written record of the **MIT STRICTLY-COMPATIBLE + 0★/0⑂ + 18 KB tiny + 7-topic array + Python ✓ ON-STACK + openpyxl + pdf + excel + food-cost + invoices + restaurant** stack-shape: this is the **FIRST *MIT-strictly-compatible-+-inbound-artifact-pipeline* pick of the 82-pass brainstorm series + the FIRST 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT vocabulary of the 82-pass brainstorm series**; the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI* posture IS the canonical §3.1 *no-account + upload-document-get-structured-sheet-back + zero-UI* invariant applied to the *LE31-v1-supplier-document-ingestion* dimension; the *parse-the-blob-then-categorise* posture IS the canonical §3.4 *deterministic kernel + openpyxl/PDF parse + no inference* invariant applied to the *LE31-v1-supplier-document-ingestion* dimension; the *MIT* license IS §3.2 STRICTLY-COMPATIBLE (code-shape adoptable); the *vendor-document-and-categories* posture IS the canonical §3.7 *minimal-PII-only-aggregator-bridge* invariant applied to the *LE31-v1-supplier-document-ingestion* dimension (the documents are vendor-side, not customer-PII).
- A written record of the **operator-facing vocabulary** discipline: the operator does NOT interact with a dashboard; the operator pastes/uploads a supplier document and gets a structured sheet back, with no account, no dashboard, no session; the *MIT* license IS §3.2 STRICTLY-COMPATIBLE (code-shape adoptable); the *parse-the-blob-then-categorise* posture IS the canonical *inbound-artifact-pipeline* stance. Sister-shape to feature 342 (`johnohhh1/restaurant-sales-forecast`, same author, in-window-pushed-TODAY, MIT, 18 KB, parse-the-blob) + features 290 (AlvaroVerona/prime-cost) + 225 (anugrhaswi/shop-ledger) + 298 (erhatechnologiesai/point-of-sale-system) — the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* posture IS the canonical v1 *supplier-document-ingestion-vocabulary* applied to the *LE31-v1-supplier-document-ingestion* dimension; the **7-topic + Python+food-cost-+-vendor-document-+-openpyxl-+-MIT cluster of the 82-pass series** = the **strongest single v1 supplier-document-ingestion day of the 82-pass series + the FIRST MIT-strictly-compatible-+-inbound-artifact-pipeline day of the 82-pass series**.
- A decision record: today's verdict is `defer` because (1) the v1 charter has *no supplier-document-ingestion surface* (LE31 v1 has HTMX-waiter + aiogram-cook-bot but no supplier-document-ingestion surface); (2) the *MIT* license IS §3.2 STRICTLY-COMPATIBLE (code-shape adoptable); (3) the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI* primitive IS portable to Italian suppliers (Caffe Borbone, Lavazza, etc.); (4) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's planned supplier-document-ingestion surface (LE31 has no spoken plan for supplier-document-ingestion today).
- Adoption of the gfs-invoice-breakdown codebase (MIT + 0★/0⑂ + Python + 5-day-old pushed-2026-Oct-15 repo) — even though MIT permissive, the *Gordon Food Service + MenuLink* vendor-specific postures are OFF-§3.5 unless §3.5 Italian-only-decision is made (the *parse-the-blob-then-categorise* primitive IS portable).
- Cross-pollination with the v1 charter §3.5 *Italian-only-market-scope* posture (the *Gordon Food Service + MenuLink* posture is OFF-§3.5; the *Italian-supplier (Caffe Borbone, Lavazza)* posture IS §3.5-aligned; the *parse-the-blob-then-categorise* primitive IS portable to Italian-supplier-document-ingestion).
- Cross-section candidate for v1 if LE31 ever adds a *supplier-document-ingestion + Italian-supplier + parse-the-blob-then-categorise* surface (charter §3.1 + §3.4 + §3.5 + §3.7 review required: the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* posture requires explicit §3.1 *no-account + upload-document-get-structured-sheet-back + zero-UI* + §3.4 *deterministic kernel + openpyxl/PDF parse + no inference* + §3.5 *Italian-only-market-scope + Italian-supplier* + §3.7 *minimal-PII-only-aggregator-bridge + vendor-document* scope before any v1 PR).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary reference + MIT code-shape adoptable**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v1 surface proposes "a supplier-document-ingestion + Italian-supplier + parse-the-blob-then-categorise surface (the operator does NOT interact with a dashboard; the operator pastes/uploads a supplier document and gets a structured sheet back, with no account, no dashboard, no session; MIT permissive; Italian-supplier)", the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT posture AND it's the 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT vocabulary of the 82-pass series"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `excel, food-cost, invoices, openpyxl, pdf, python, restaurant` + *"Turn Gordon Food Service POs and MenuLink cost journals into categorized Excel cost breakdowns"*).
- **Confidence**: medium-high for the vocabulary match (the verbatim description + topics name the 4-tuple-primitive set + the *vendor-specific-PDF/Excel-in* posture + the *openpyxl-workbook-out* posture + the *zero-UI* posture + the *MIT* posture); high for transferability (the *parse-the-blob-then-categorise* primitive IS portable to Italian-supplier-document-ingestion; the *MIT* license IS §3.2 STRICTLY-COMPATIBLE).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has HTMX-waiter + aiogram-cook-bot but no supplier-document-ingestion surface; today the LE31 v1 is HTMX-waiter + aiogram-cook-bot + minimal-Italian-operator-driven, no *vendor-document-ingestion*); the value is the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* vocabulary — when the first v1 PR that adopts *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* lands, the gfs-invoice-breakdown pattern is a ready-made *named primitive* (AND it's the 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT vocabulary of the 82-pass series).

## Description

GitHub `johnohhh1/gfs-invoice-breakdown` (MIT ✓ STRICTLY-COMPATIBLE, 0★/0⑂, 18 KB tiny, Python ✓ ON-STACK + openpyxl + pdf + excel + food-cost + invoices + restaurant, pushed 2026-10-15T16:08:18Z AND created 2026-10-15T16:08:11Z, default_branch=undefined, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-20): *"Turn Gordon Food Service POs and MenuLink cost journals into categorized Excel cost breakdowns"*.

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v1 surface:

1. **Vendor-specific-PDF/Excel-in** — the system ingests vendor-specific PDFs/Excels (Gordon Food Service POs, MenuLink cost journals). The *vendor-specific-PDF/Excel-in* posture IS the canonical §3.1 *upload-document-get-structured-sheet-back* invariant applied to the *supplier-document-ingestion* dimension.
2. **Openpyxl-workbook-out** — the system produces an openpyxl workbook as the output. The *openpyxl-workbook-out* posture IS the canonical §3.4 *deterministic kernel + openpyxl-workbook-out* invariant applied to the *supplier-document-ingestion* dimension.
3. **Zero-UI** — the system has zero UI (no dashboard, no settings page, no login). The *zero-UI* posture IS the canonical §3.1 *no-account + no-dashboard + no-session* invariant applied to the *supplier-document-ingestion* dimension.
4. **MIT** — the system is MIT-licensed. The *MIT* posture IS the canonical §3.2 STRICTLY-COMPATIBLE invariant applied to the *supplier-document-ingestion* dimension (code-shape adoptable).
5. **Parse-the-blob-then-categorise** — the primitive is *PARSE-THE-BLOB-THEN-CATEGORISE*. The *parse-the-blob-then-categorise* posture IS the canonical *inbound-artifact-pipeline* stance.
6. **Vendor-document-and-categories** — the documents are vendor-side (Gordon Food Service, MenuLink); the categories are pre-defined (food-cost, invoices). The *vendor-document-and-categories* posture IS the canonical §3.7 *minimal-PII-only-aggregator-bridge* invariant (the documents are vendor-side, not customer-PII).
7. **Python + openpyxl + pdf + excel + food-cost + invoices + restaurant** — the system is built on Python + openpyxl + pdf + excel + food-cost + invoices + restaurant. The *Python + openpyxl + pdf + excel* posture IS portable to LE31 v1 (LE31 v1 uses FastAPI + SQLModel + Postgres, but the *Python-on-stack + openpyxl-on-stack + pdf-on-stack* discipline is portable).
8. **Gordon Food Service + MenuLink** — the system targets Gordon Food Service + MenuLink (US suppliers). The *Gordon Food Service + MenuLink* posture IS OFF-§3.5 unless §3.5 Italian-only-decision is made; the *Italian-supplier (Caffe Borbone, Lavazza)* posture IS §3.5-aligned.
9. **Smallest-stack-profile** — the system is 18 KB with 7 topics. The *smallest-stack-profile* posture IS the canonical §3.5 *single-binary-install-on-Italian-desktop-laptop* invariant.
10. **Same-author-+-same-week-+-MIT-+-18KB-+-parse-the-blob** — the system shares an author (johnohhh1) + week (2026-10-15) + license (MIT) + size (18 KB) + primitive (parse-the-blob) with feature 342 (`johnohhh1/restaurant-sales-forecast`). The *same-author-+-same-week-+-MIT-+-18KB-+-parse-the-blob* discipline IS the canonical *small-footprint-+-MIT-+-parse-the-blob* cluster.

The defer artifact retains the **4-tuple-primitive** (vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT) as a persistent cross-section reference.

## Data model

N/A (defer artifact; vocabulary-only; no schema today).

When the first v1 PR that adopts the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline lands, the schema is:

```sql
-- Supplier document is parsed into a categorized Excel breakdown.
CREATE TABLE supplier_document (
    id BIGSERIAL PRIMARY KEY,
    supplier_name TEXT NOT NULL,           -- 'Gordon Food Service' / 'MenuLink' / 'Caffe Borbone' / 'Lavazza'
    document_type TEXT NOT NULL,            -- 'PO' / 'cost_journal' / 'invoice'
    raw_pdf BYTEA,                          -- raw PDF blob (if applicable)
    raw_excel BYTEA,                        -- raw Excel blob (if applicable)
    parsed_json JSONB NOT NULL,             -- parsed-then-categorised structure
    output_workbook BYTEA NOT NULL,         -- openpyxl workbook output
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Parse-the-blob-then-categorise view (the operator-facing surface).
CREATE VIEW categorized_cost_breakdown AS
    SELECT
        supplier_name,
        document_type,
        parsed_json,
        created_at
    FROM supplier_document
    ORDER BY created_at DESC;
```

## Implementation steps

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline lands, the implementation is:

1. Add `SupplierDocument` table with `raw_pdf` BYTEA + `raw_excel` BYTEA + `parsed_json` JSONB + `output_workbook` BYTEA columns.
2. Add `categorized_cost_breakdown` view as the operator-facing surface.
3. Add `pdfplumber` + `openpyxl` libraries for parse-the-blob.
4. Add zero-UI posture (single binary + on-premise-installer; no dashboard, no settings page, no login).
5. Add MIT permissive license posture (LE31 v1 is already MIT-compatible; the *vendor-document-and-categories* posture IS portable).
6. Add Italian-supplier adapter (Caffe Borbone, Lavazza, etc.) for §3.5 Italian-only-market-scope.
7. Add unit + integration tests for the *parse-the-blob-then-categorise* posture.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline lands, the Telegram interaction is:

- Cook bot (aiogram v3) sends a Telegram message to the owner when a supplier document is parsed-and-categorised (with attachment: the openpyxl workbook output).
- Waiter bot (aiogram v3 or HTMX-waiter) sends a Telegram message to the owner when the categorized_cost_breakdown view updates.
- The *parse-the-blob-then-categorise + openpyxl-workbook-out + zero-UI + MIT* posture IS the canonical *upload-document-get-structured-sheet-back-via-Telegram-message* invariant.

## Open questions

- **Does the v1 charter ever adopt *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline?** Today no. **Decision pending** — when the first v1 PR that proposes *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* lands, the gfs-invoice-breakdown pattern is a ready-made *named primitive*.
- **What is the Italian-only-market-scope decision?** Today the *Gordon Food Service + MenuLink* posture is OFF-§3.5; the *Italian-supplier (Caffe Borbone, Lavazza)* posture IS §3.5-aligned. **Decision pending**.
- **What is the LE31 v1 stance on supplier-document-ingestion?** Today LE31 v1 has no supplier-document-ingestion surface; the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* posture IS the canonical §3.1 *upload-document-get-structured-sheet-back* invariant. **Decision pending**.

## Why this matters

The *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* posture IS the canonical §3.1 + §3.4 + §3.5 + §3.7 *no-account + upload-document-get-structured-sheet-back + zero-UI + deterministic kernel + Italian-only-market-scope + minimal-PII-only-aggregator-bridge* charter invariant applied to the *LE31-v1-supplier-document-ingestion* dimension. The *parse-the-blob-then-categorise* posture IS portable to LE31 v1 (the operator does NOT interact with a dashboard; the operator pastes/uploads a supplier document and gets a structured sheet back, with no account, no dashboard, no session). The vocabulary reference is the value, not the code-adoption opportunity.

When the first v1 PR that adopts the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline lands, the gfs-invoice-breakdown pattern is a ready-made *named primitive* (AND it's the 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT vocabulary of the 82-pass series + the **FIRST 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT vocabulary of the 82-pass brainstorm series + the FIRST MIT-strictly-compatible-+-inbound-artifact-pipeline pick of the 82-pass brainstorm series**).

## Cross-section references

- **Sister-shape** to feature 342 (`johnohhh1/restaurant-sales-forecast`, same author, in-window-pushed-TODAY, MIT, 18 KB, parse-the-blob) + features 290 (AlvaroVerona/prime-cost) + 225 (anugrhaswi/shop-ledger) + 298 (erhatechnologiesai/point-of-sale-system) = the persistent *Python+food-cost-+-vendor-document-+-openpyxl-+-MIT* cluster.
- **Vocab-cluster** of the 82-pass brainstorm series: the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline IS the canonical §3.1 + §3.4 + §3.5 + §3.7 *no-account + upload-document-get-structured-sheet-back + zero-UI + deterministic kernel + Italian-only-market-scope + minimal-PII-only-aggregator-bridge* invariant applied to the *LE31-v1-supplier-document-ingestion* dimension.
- **Cross-section candidate** for v1 if LE31 ever adds a *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* surface (charter §3.1 + §3.4 + §3.5 + §3.7 review required: the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* posture requires explicit §3.1 *no-account + upload-document-get-structured-sheet-back + zero-UI* + §3.4 *deterministic kernel + openpyxl/PDF parse + no inference* + §3.5 *Italian-only-market-scope + Italian-supplier* + §3.7 *minimal-PII-only-aggregator-bridge + vendor-document* scope before any v1 PR).

## License caveat

**MIT ✓ §3.2 STRICTLY-COMPATIBLE.** The license is permissive; the code-shape IS adoptable per §3.2. The *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI* vocabulary IS portable to Italian-supplier-document-ingestion (Caffe Borbone, Lavazza); the *Gordon Food Service + MenuLink* vendor-specific code IS OFF-§3.5 unless §3.5 Italian-only-decision is made (the *parse-the-blob-then-categorise* primitive IS portable). The defer artifact is a *vocabulary reference + MIT code-shape adoptable*. The **FIRST MIT-strictly-compatible-+-inbound-artifact-pipeline pick of the 82-pass brainstorm series**.