# HANDOFF — 325-AlexisLD-DEV-qramen

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today) — **OFF-STACK flag — UX-pattern vocabulary only; the n8n + Airtable + vanilla-JS codebase is NOT adopted; a future v1 PR would re-implement the QR-code-table-ordering UX pattern in Python+FastAPI+HTMX**
**Date**: 2026-10-15
**Active feature path**: `/opt/data/le31_mmm3_research/features/325-AlexisLD-DEV-qramen-mit-qr-code-table-ordering-demonstration-mobile-page-cuisine-screen-n8n-airtable-tickets-addition-pdf-v1-qr-code-table-ordering-ux-vocabulary-reference.md`
**LE31 feature gate verdict**: defer (LE31 v1 does not need to *use* `AlexisLD-DEV/qramen`; the LE31 v1 surface has features 02 (waiter order-taking) + 03 (kitchen stock tracker) + 05 (payment-tip-reconciliation) for the relevant operator surfaces, but no *QR-code-table-ordering-for-the-diner* surface today; the peer value is *v1 cross-section UX-pattern vocabulary for a future v1 PR that adds a QR-code-table-ordering surface*, not *adoption*; the UX pattern is the vocabulary, the n8n+Airtable+vanilla-JS codebase is OFF-STACK and explicitly NOT adopted.)

## Trigger policy

This is a **defer artifact (parking-lot, UX-pattern vocabulary only)** — a watch-list entry. It does not start a build. It surfaces the `AlexisLD-DEV/qramen` GitHub repo (MIT, **0★ / 0⑂**, **267756 KB substantial** (large because of asset files), language=`Python` per GitHub metadata — **OFF-STACK actual implementation is n8n + Airtable + vanilla-JS, NOT Python+FastAPI+SQLModel+Postgres+HTMX** per `le31-daily-brainstorm/SKILL.md` hard rule line 65 (the GitHub `language:` qualifier does not guarantee the language of returned repos), **pushed 2026-10-15T02:21:56Z AND created 2026-10-13T19:01:38Z = IN-WINDOW BY BOTH FIELDS** = 2-day-old repo with TODAY push) as a dated, in-window **UX-pattern vocabulary peer** for LE31's potential v1 *QR-code-table-ordering-for-the-diner* surface.

If the trigger condition (LE31 first proposes a v1 surface that wants *QR-code-table-ordering-for-the-diner* OR *mobile-page-no-app-install-ordering* OR *kitchen-screen-via-Web-push* OR *tickets-PDF-output-for-kitchen* OR *bill-PDF-output-for-diner* primitives, OR a future owner decision questions whether feature 02 `order-taking` should be extended to cover the *diner-self-orders-via-QR-code* dimension) is met, the external coding agent should:

1. Load this artifact and the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-15.md`).
2. Load the `qramen` repo: `https://github.com/AlexisLD-DEV/qramen` — README + screenshots if available; **the codebase is OFF-STACK and NOT adopted — the UX-pattern is the vocabulary**.
3. Load the companion features 02 (waiter order-taking) + 03 (kitchen stock tracker) + 05 (payment-tip-reconciliation) + 13 (reservations deposits) + 28 (visual table layout); the *QR-code-table-ordering* UX pattern re-implements these in a diner-self-service fashion.
4. **Re-implement in Python+FastAPI+HTMX+SQLModel — NOT n8n+Airtable+vanilla-JS**. The transferable items are: (a) the *QR-code-at-the-table* UX pattern; (b) the *mobile-page-ordering-no-app-install* UX pattern; (c) the *kitchen-screen-via-Web-push* UX pattern; (d) the *tickets-PDF-output-for-kitchen* UX pattern; (e) the *bill-PDF-output-for-diner* UX pattern. Each is a *feature* in LE31's v1 charter, not a *code dependency*.
5. Re-run the LE31 feature gate with the re-implementation in mind.
6. **Decide whether the proposed v1 surface benefits from the QR-code-table-ordering UX pattern**. If the v1 surface wants *diner-self-ordering* OR *per-table-QR-code-stickers*, the `qramen` pattern is purpose-built for that use case (re-implement in Python+FastAPI+HTMX). If the v1 surface only wants to extend the existing feature 02 waiter-tip-capture, `qramen` adds no value.
7. **If the QR-code-table-ordering UX pattern is proposed for adoption**: do NOT add `qramen` to `requirements-qramen.txt`; instead, design the v1 surface as a fresh Python+FastAPI+HTMX implementation that captures the UX pattern. Add to `requirements-new-v1-qrcode.txt` only the new dependencies (e.g., `qrcode[pil]` for QR-code generation, `weasyprint` for PDF generation, `reportlab` for tickets-PDF). Add a single test QR-code-redirect call against a single `Visit` from the LE31 owner-side. Compare against the existing waiter-side order-taking UX. If the test QR-code-redirect adds diner-self-ordering-value, propose a v1 extension as feature 02X; if not, document the comparison and defer.
8. **If the QR-code-table-ordering UX pattern is not adopted**: document the comparison and defer. No charter §3.1 change is needed.
9. **Pilot on one real-Visit first**. Do not ship the QR-code-table-ordering surface project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/325-AlexisLD-DEV-qramen-...md`
- **Parent daily-brainstorm report**: `/opt/data/le31-brainstorm-2026-10-15.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-15/gh_sanity_restaurant_python.json` (where `AlexisLD-DEV/qramen` is listed; parent-verified raw JSON has `stargazers_count=0`, `forks_count=0`, `license.spdx_id=MIT`, `pushed_at=2026-10-15T02:21:56Z`, `created_at=2026-10-13T19:01:38Z`, `description="Commande à table par QR code (démonstration) : page mobile, écran cuisine, automatisations n8n, base Airtable, tickets et addition en PDF."`, `size=267756`, `topics=[airtable, automation, n8n, qr-code, restaurant, self-hosted, vanilla-js]`)
- **`qramen` repo**: `https://github.com/AlexisLD-DEV/qramen` (parent-fetched 2026-10-15 metadata; verify-via-direct-GitHub-API-GET at `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_AlexisLD-DEV_qramen.json` — **for UX-pattern reference only, NOT for code adoption**)
- **Companion artifacts**:
  - `features/02-order-taking.md` (the existing v1 waiter-side ordering surface that the QR-code-table-ordering pattern would parallel for diner-self-ordering)
  - `features/03-kitchen-stock-tracker.md` (the stop-list-item event already implemented as a `StockEntry` schema)
  - `features/05-payment-tip-reconciliation.md` (the bill-PDF would extend the existing bill-receipt surface)
  - `features/13-reservations-deposits.md` (the QR-code pattern could double for the reservation check-in flow)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.6 money-invariants + integer-minor-units + per-order-attribution).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

**OFF-STACK reminder**: The `qramen` repo's actual implementation is n8n + Airtable + vanilla-JS, NOT Python+FastAPI+SQLModel+Postgres+HTMX. The codebase is **NOT adopted**; only the UX-pattern is the vocabulary. A future v1 PR would re-implement the UX pattern in Python+FastAPI+HTMX from scratch, NOT add `qramen` to the requirements file.

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-brainstorm-2026-10-15/gh_sanity_restaurant_python.json` JSON to confirm `full_name=AlexisLD-DEV/qramen` + `stargazers_count=0` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-15T02:21:56Z` + `created_at=2026-10-13T19:01:38Z` + `description = "Commande à table par QR code (démonstration) : page mobile, écran cuisine, automatisations n8n, base Airtable, tickets et addition en PDF."` + `size=267756` + `topics=[airtable, automation, n8n, qr-code, restaurant, self-hosted, vanilla-js]`. **OFF-STACK flag**: `language=Python` is the GitHub metadata, but the actual implementation is n8n + Airtable + vanilla-JS per `le31-daily-brainstorm/SKILL.md` hard rule line 65.
- **GitHub canonical read**: GET `https://api.github.com/repos/AlexisLD-DEV/qramen` (HTTP 200; parent-verified 2026-10-15; raw JSON at `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_AlexisLD-DEV_qramen.json`).
- **Anti-fabrication canary**: `grep -lF 'AlexisLD-DEV/qramen'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `qramen` against features 1–324 = only this feature 325.
- **OFF-STACK validation**: verify the actual implementation is n8n + Airtable + vanilla-JS by reading the repo's package.json + workflows directory + any n8n-workflow files; the codebase has NO Python source files beyond optional glue.

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/325-AlexisLD-DEV-qramen-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/325-AlexisLD-DEV-qramen-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).
- **No n8n / Airtable / vanilla-JS dependencies were added** (the codebase is OFF-STACK and explicitly NOT adopted).
