# HANDOFF — Feature 349: `johnohhh1-gfs-invoice-breakdown-mit-gfs-pos-menulink-cost-journals-categorized-excel-cost-breakdowns-excel-food-cost-invoices-openpyxl-pdf-python-restaurant-v1-supplier-document-ingestion-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/349-johnohhh1-gfs-invoice-breakdown-mit-gfs-pos-menulink-cost-journals-categorized-excel-cost-breakdowns-excel-food-cost-invoices-openpyxl-pdf-python-restaurant-v1-supplier-document-ingestion-vocabulary.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-20).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes a *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT primitive*, the owner wants *evidence that this supplier-document-ingestion-vocabulary exists in 2026 with the same vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT posture AND the 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT posture*, but struggles because *LE31 has no documented v1 supplier-document-ingestion-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT posture AND it's the 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT vocabulary of the 82-pass series"*. |
| 2 | Viability | ✓ | The owner/staff can understand the supplier-document-ingestion vocabulary (vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT) without specialist help. The **7-topic + 0★/0⑂ + Python ✓ ON-STACK + 18 KB tiny + MIT ✓ STRICTLY-COMPATIBLE + 5-day-old pushed-2026-10-15 repo** makes vocabulary viable AND code adoption viable (MIT permissive per §3.2). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + openpyxl ✓ ON-PATTERN (the §3.4 deterministic-kernel + openpyxl-workbook-out posture is portable) + pdf ✓ ON-PATTERN (the *pdfplumber* library is MIT-licensed and IS adoptable per §3.2) + excel ✓ ON-PATTERN + food-cost ✓ ON-PATTERN (the §3.7 minimal-PII-only-aggregator-bridge posture is portable; the documents are vendor-side, not customer-PII) + invoices ✓ ON-PATTERN + restaurant ✓ ON-PATTERN. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX + aiogram v3 + openpyxl + pdfplumber (MIT). Evidence strength: medium-high for vocabulary; **high for transferability** (the *parse-the-blob-then-categorise* primitive IS portable to Italian-supplier-document-ingestion; the *MIT* license IS §3.2 STRICTLY-COMPATIBLE). |
| 4 | Conflict | ✓ | Does not violate any invariant. The *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* primitives are §3.1 + §3.4 + §3.5 + §3.7-aligned (no-account + upload-document-get-structured-sheet-back + deterministic kernel + Italian-only-market-scope + minimal-PII-only-aggregator-bridge). The *vendor-document-and-categories* posture IS the canonical §3.7 *minimal-PII-only-aggregator-bridge* invariant (the documents are vendor-side, not customer-PII). No §3.5 conflict (the *Gordon Food Service + MenuLink* vendor-specific code IS OFF-§3.5 unless §3.5 Italian-only-decision is made; the *parse-the-blob-then-categorise* primitive IS portable to Italian-supplier-document-ingestion with Caffe Borbone + Lavazza adapters). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 defer outcome (vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT surface for the LE31 v1 supplier-document-ingestion). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (planned supplier-document-ingestion + Italian-only-market-scope + Italian-supplier) may adopt the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline; the reference is *naming*, not new build. The **7-topic + 0★/0⑂ + Python ✓ ON-STACK + 18 KB tiny + MIT ✓ STRICTLY-COMPATIBLE** makes this the strongest possible vocabulary reference for v1 supplier-document-ingestion (the FIRST 7-topic + supplier-document-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT vocabulary of the 82-pass brainstorm series + the FIRST MIT-strictly-compatible-+-inbound-artifact-pipeline pick of the 82-pass brainstorm series). |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because there is no v1 charter surface for supplier-document-ingestion today (LE31 v1 is HTMX-waiter + aiogram-cook-bot + minimal-Italian-operator-driven; no *vendor-document-ingestion*). The vocabulary IS portable AND the **7-topic + 0★/0⑂ + Python ✓ ON-STACK + 18 KB tiny + MIT ✓ STRICTLY-COMPATIBLE** makes this the strongest possible vocabulary reference for v1 supplier-document-ingestion (the FIRST MIT-strictly-compatible-+-inbound-artifact-pipeline pick of the 82-pass brainstorm series).

## Bucket

**v1 (supplier-document-ingestion-+-vendor-specific-PDF/Excel-in-+-openpyxl-workbook-out-+-zero-UI-+-MIT-+-Gordon-Food-Service-+-MenuLink-+-Italian-supplier-portable-vocabulary)** — the *vocabulary* IS the value AND the *MIT license* IS code-shape adoptable per §3.2 (the vendor-specific posture IS portable to Italian-supplier-document-ingestion with Caffe Borbone + Lavazza adapters). The verbatim description + topics name the 4-tuple-primitive set (vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT) + the tech-stack (Python ✓ ON-STACK + openpyxl + pdf + excel + food-cost + invoices + restaurant).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `supplier_document` table with `raw_pdf` BYTEA + `raw_excel` BYTEA + `parsed_json` JSONB + `output_workbook` BYTEA columns.
- `backend/alembic/versions/` — add migration for `categorized_cost_breakdown` view as the operator-facing surface.
- `backend/services/supplier_document_service.py` — new file with `SupplierDocumentService` class (charter §3.1 *upload-document-get-structured-sheet-back + no-account + zero-UI* posture).
- `backend/services/parse_blob_service.py` — new file with `ParseBlobService` class (charter §3.4 *parse-the-blob-then-categorise + openpyxl/PDF parse + no inference* posture).
- `backend/services/categorize_service.py` — new file with `CategorizeService` class (charter §3.7 *vendor-document-and-categories + minimal-PII-only-aggregator-bridge* posture).
- `backend/main.py` — wire the new sub-apps into the parent uvicorn app.
- `backend/requirements.txt` — add `openpyxl` + `pdfplumber` (both MIT-licensed; compatible per §3.2).
- `backend/adapters/caffe_borbone.py` — new file with `CaffeBorboneAdapter` class (charter §3.5 *Italian-only-market-scope + Italian-supplier* posture).
- `backend/adapters/lavazza.py` — new file with `LavazzaAdapter` class (charter §3.5 *Italian-only-market-scope + Italian-supplier* posture).
- `frontend/templates/categorized-cost-breakdown.html` — new minimal-HTML/HTMX template for the operator-facing-categorized-cost-breakdown.
- `tests/test_supplier_document_service.py` — new unit test for `SupplierDocumentService`.
- `tests/test_parse_blob_service.py` — new unit test for `ParseBlobService`.
- `tests/test_categorize_service.py` — new unit test for `CategorizeService`.
- `tests/integration/test_supplier_document_to_categorize.py` — new integration test for `SupplierDocumentService` → `ParseBlobService` → `CategorizeService` (verify the *parse-the-blob-then-categorise* posture).

## Verification protocol reference

See `/opt/data/le31_mmm3_research_work/skills/le31-v1-feature-pattern/SKILL.md` for the canonical v1 verification protocol.

## Rollback path

`git rm features/349-...md specs/349-...-HANDOFF.md` — single-file revert.

## Mandatory LE31 skill list

When the first v1 PR that adopts the *vendor-specific-PDF/Excel-in + openpyxl-workbook-out + zero-UI + MIT* discipline lands, the coding agent must load these skills before starting:

- `le31-conventions` — for the canonical §3.1 + §3.4 + §3.5 + §3.7 charter-invariant review.
- `le31-v1-feature-pattern` — for the canonical v1 feature pattern (HTMX-waiter + aiogram-cook-bot + append-only-StockEntry + Postgres + FastAPI + SQLModel).
- `le31-backend` — for the canonical FastAPI + SQLModel + Postgres + Alembic + append-only-ledger pattern.
- `le31-frontend` — for the canonical minimal-HTML/HTMX + minimal-JS pattern.
- `le31-handoff-spec` — for the canonical HANDOFF-spec format.
- `le31-coding-agent-brief` — for the canonical paste-in-prompt format.