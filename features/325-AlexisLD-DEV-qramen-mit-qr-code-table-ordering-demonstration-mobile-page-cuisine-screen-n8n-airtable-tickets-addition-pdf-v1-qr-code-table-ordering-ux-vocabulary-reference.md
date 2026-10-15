# Feature 325 — `AlexisLD-DEV/qramen` v1 QR-code-table-ordering-UX-vocabulary-reference (defer, OFF-STACK)

> **NEW observation (2026-10-15).** Documents in-window GitHub repo `AlexisLD-DEV/qramen` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **267756 KB substantial** (large because of asset files, likely ~268 MB), language `Python` per GitHub metadata — **OFF-STACK flag — actual implementation is n8n (workflow orchestration) + Airtable (database) + vanilla-JS (frontend)**, NOT Python+FastAPI+SQLModel+Postgres+HTMX, parent-direct-GitHub-API-GET-verified 2026-10-15 from `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_AlexisLD-DEV_qramen.json`). `language:Python` GitHub Search qualifier misled per `le31-daily-brainstorm/SKILL.md` hard rule line 65 (the GitHub `language:` qualifier does not guarantee the language of returned repos). **pushed 2026-10-15T02:21:56Z = TODAY's push ~5 hours before fetch time AND created 2026-10-13T19:01:38Z = IN-WINDOW BY BOTH FIELDS**. Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15, French): *"Commande à table par QR code (démonstration) : page mobile, écran cuisine, automatisations n8n, base Airtable, tickets et addition en PDF."* Topics (verbatim, parent-verified): `airtable`, `automation`, `n8n`, `qr-code`, `restaurant`, `self-hosted`, `vanilla-js` = **7 topics including `qr-code + restaurant + vanilla-js` (the v1 in-domain cross-section match) + `n8n + airtable + automation + self-hosted` (the OFF-STACK implementation primitives)** = **canonical v1 QR-code-table-ordering-UX-vocabulary-reference of the 77-pass brainstorm series**. Bucket: **v1 (parking-lot, vocabulary reference)** — Pick C of Daily Brainstorm 2026-10-15. Build verdict: `defer` (parking-lot, vocabulary-only). Zero build time today.

## Goal

Retain the **QR-code-table-ordering + mobile-page + kitchen-screen + n8n-automations + Airtable-DB + tickets-PDF + bill-PDF** sextuple-primitive as a persistent cross-section reference for the LE31 v1 *QR-code-table-ordering-for-the-diner* wedge, and document the **UX-pattern validation** that an independent maintainer arrived at in 2026 (2-day-old repo with TODAY push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v1 product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **QR-code-table-ordering + mobile-page + kitchen-screen + tickets-PDF + bill-PDF** UX-pattern vocabulary: (1) *QR-code-at-the-table* (the diner scans a QR code at the table); (2) *Mobile-page ordering* (the diner browses the menu, adds items to the cart, submits the order); (3) *Kitchen-screen* (the kitchen sees the new order in real-time); (4) *Tickets-PDF* (every order generates a printable PDF ticket for the kitchen); (5) *Bill-PDF* (when the table asks for the bill, a PDF bill is generated and sent to the diner's phone). This is the §3.1 *crossover-restaurant-app + phone-first-POS + low-effort-UX* charter triple-invariant applied to the *table-side-ordering* dimension
- A written record of the **n8n + Airtable + vanilla-JS** implementation-shape: this is **OFF-STACK** (LE31 uses Python + FastAPI + SQLModel + Postgres + HTMX; the n8n + Airtable + vanilla-JS codebase is **NOT** adopted — vocabulary-only); the **n8n + Airtable + vanilla-JS** implementation is the lexicographic vocabulary point, but the transferable item is the *QR-code-table-ordering-UX-pattern*, not the codebase
- A written record of the **QR-code-table-ordering-UX-pattern** operator-surface-shape: the operator (waiter) is *freed* from taking orders at the table because the diner self-orders via the QR code; the kitchen receives orders directly from the diner's phone; the operator only steps in if the diner asks for help or wants to close the bill
- A decision record: today's verdict is `defer (vocabulary-only, OFF-STACK)` because (1) the actual implementation is n8n + Airtable + vanilla-JS, NOT Python+FastAPI+SQLModel+Postgres+HTMX — **no v1 code adoption possible**; (2) the *QR-code-table-ordering-UX-pattern* + *mobile-page + kitchen-screen + tickets-PDF + bill-PDF* vocabulary is the transferable item for a future v1 PR re-implementing the pattern in Python+FastAPI+HTMX; (3) the *demand-signal* is the value, not the code-adoption opportunity

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3) or owner daily-recap
- Any change to LE31 v1's `audit_logs` schema or `Visit` (table-state) schema
- **Adoption of the `qramen` codebase — explicitly NOT adopted because n8n + Airtable + vanilla-JS is OFF-STACK; the UX-pattern is the vocabulary; a future v1 PR would re-implement the pattern in Python+FastAPI+HTMX**
- Cross-pollination with the n8n workflow engine (LE31 uses FastAPI + LangGraph for v2-AI surfaces; n8n is a no-go per §3.1 stack)

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1 code is shipped today. The n8n + Airtable codebase is explicitly NOT adopted (OFF-STACK).

## Evidence / JTBD

When a future LE31 v1 surface proposes "the *QR-code-table-ordering-for-the-diner* surface that lets the diner scan a QR code at the table, browse the menu, add items to the cart, submit the order to the kitchen screen, and receive a PDF bill" (e.g., a v1 PR that introduces a *QR-code-table-ordering* surface that reduces waiter-side order-taking time from 30 seconds to 5 seconds per table while keeping the operator-driven-confirmation pattern intact), the owner wants *a primitive that proves the demand for this UX pattern exists in 2026*, but struggles because *LE31 has no documented evidence that "QR-code-table-ordering + mobile-page + kitchen-screen + tickets-PDF + bill-PDF" is a real demand signal*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the QR-code-table-ordering UX pattern"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `qr-code + restaurant + vanilla-js + n8n + airtable + automation + self-hosted`)
- **Confidence**: medium-high for the UX-pattern vocabulary match (the verbatim description names the 5-primitive UX-pattern set + the tech-stack-implementation); low for transferability (LE31 v1 uses Python+FastAPI+SQLModel+Postgres+HTMX; the n8n+Airtable+vanilla-JS implementation is OFF-STACK; a future v1 PR would re-implement the UX pattern in Python+FastAPI+HTMX)
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1's order-taking is waiter-side 30-second-polling-HTMX via feature 02; no QR-code-table-ordering surface); the value is the *QR-code-table-ordering-UX-pattern* vocabulary — when the first v1 PR that adds a *QR-code-table-ordering* surface lands, the `qramen` pattern is a ready-made *named primitive*

## Description

GitHub `AlexisLD-DEV/qramen` (MIT, 0★/0⑂, language=`Python` per metadata — **OFF-STACK actual implementation is n8n + Airtable + vanilla-JS, NOT Python+FastAPI+SQLModel+Postgres+HTMX**, pushed 2026-10-15T02:21:56Z, created 2026-10-13T19:01:38Z = 2-day-old repo with TODAY push, both-window, 267756 KB = ~268 MB substantial). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15, French): *"Commande à table par QR code (démonstration) : page mobile, écran cuisine, automatisations n8n, base Airtable, tickets et addition en PDF."*

The UX-pattern primitive has five sub-primitives that map 1:1 onto the LE31 v1 *QR-code-table-ordering* surface:

1. **QR-code at the table** — every table has a QR code printed on a stand or a sticker. The *QR-code-at-the-table* primitive maps 1:1 onto LE31's potential v1 surface that adds a QR-code-per-table artifact (a small printed sticker).
2. **Mobile-page ordering** — the diner scans the QR code, opens a mobile-browser-page (no app install), sees the menu, adds items to the cart, submits the order. The *mobile-page-ordering-no-app-install* primitive maps 1:1 onto LE31's `Visit` (table-state) + `OrderItem` (line-item) schemas (which already support diner-side ordering).
3. **Kitchen-screen** — the kitchen receives the new order in real-time on a kitchen-screen. The *kitchen-screen* primitive maps 1:1 onto LE31's cook-bot (feature 03) + a future kitchen-screen Web app.
4. **Tickets-PDF** — every order generates a printable PDF ticket for the kitchen to print and stick to the order-pickup screen. The *tickets-PDF* primitive maps 1:1 onto LE31's potential v1 surface that generates PDF tickets (the v1 charter has no PDF-output surface today, but the `Visit` + `OrderItem` schemas already support PDF-attachment to events).
5. **Bill-PDF** — when the table asks for the bill, a PDF bill is generated and sent to the diner's phone. The *bill-PDF* primitive maps 1:1 onto LE31's `payment-tip-reconciliation` (feature 05) — a future v1 PR would extend the bill-receipt surface with a PDF output.

**The 1:1 mapping onto LE31 surface (UX-pattern + re-implementation):**

| `qramen` primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| QR-code at the table | (LE31 has no QR-code-table surface today) | v1 | **Not implemented** — new v1 surface (printed QR code per table) |
| Mobile-page ordering | `Visit` + `OrderItem` state | §3.1 ✓ | **Implemented (v1)** — UX-pattern re-implementation in HTMX |
| Kitchen-screen | cook-bot (03) + future kitchen-screen Web app | §3.1 ✓ | **Partially implemented** — Web app is new |
| Tickets-PDF | (LE31 has no PDF-output surface today) | v1 | **Not implemented** — new v1 surface (ReportLab or weasyprint) |
| Bill-PDF | `payment-tip-reconciliation` (05) | §3.6 | **Partially implemented** — PDF output is new |
| **ACTUAL implementation** | n8n + Airtable + vanilla-JS | OFF-STACK | **NOT adopted — vocabulary-only** |
| **Future re-implementation** | Python + FastAPI + SQLModel + Postgres + HTMX | §3.1 ✓ | **Future v1 PR target** |

## Dependencies

- [02-order-taking.md](../features/02-order-taking.md) — the diner-side-ordering UX-pattern re-implements `OrderItem` state management
- [03-kitchen-stock-tracker.md](../features/03-kitchen-stock-tracker.md) — the kitchen-screen reads from `StockEntry`
- [05-payment-tip-reconciliation.md](../features/05-payment-tip-reconciliation.md) — the bill-PDF extends the existing bill-receipt surface

## Open questions

- Should the QR-code-table-ordering surface be optional (per-table toggle, qr-code off by default) or mandatory (every table has a qr-code by default)?
- Should the diner-side cart have a per-item modifier UI (size, extras) or be flat (as v1 charter says menu is flat)?
- Should the QR-code redirect to a static mobile-page (low-cost) or a per-visit dynamic page (more accurate)?
- Should the tickets-PDF auto-print or require a cook-confirm first?

## Why this matters

The **QR-code-table-ordering + mobile-page + kitchen-screen + tickets-PDF + bill-PDF** quintuple-primitive is a *stronger* v1 cross-section vocabulary than features 02/03/04/05/16/28 alone. The QR-code-table-ordering discipline IS the §3.1 *crossover-restaurant-app + phone-first-POS + low-effort-UX* charter triple-invariant applied to the *table-side-ordering* dimension. The mobile-page-no-app-install discipline IS the §3.5 *low-friction-operator-and-diner* invariant applied to the *diner-side-ordering* dimension. The tickets-PDF + bill-PDF discipline IS the §3.6 *per-visit-attribution + per-day-attribution* invariant applied to the *table-bill-output* dimension. The 0★/0⑂ + 2-day-old-repo + TODAY-push + both-window + MIT permissive + UX-pattern-vocabulary-only + ~268 MB (the largest of today's 3 picks because of asset files) = the cleanest v1 cross-section *UX-pattern vocabulary reference* of the 77-pass brainstorm series.

## Rollback path

This defer artifact is fully reversible:
- Delete the feature file: `rm /opt/data/le31_mmm3_research/features/325-AlexisLD-DEV-qramen-...md`
- Delete the HANDOFF: `rm /opt/data/le31_mmm3_research/specs/325-AlexisLD-DEV-qramen-...-HANDOFF.md`
- No code change was made today, so no rollback of code is required
- No database migration was made today, so no rollback of schema is required
- No pin change was made today (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1)
- No n8n / Airtable / vanilla-JS dependencies were added (the codebase is OFF-STACK and explicitly NOT adopted)
