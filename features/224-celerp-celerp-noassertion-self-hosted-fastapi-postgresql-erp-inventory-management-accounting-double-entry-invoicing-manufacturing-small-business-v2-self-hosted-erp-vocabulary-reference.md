# Feature 224 — celerp-celerp-noassertion-self-hosted-fastapi-postgresql-erp-inventory-management-accounting-double-entry-invoicing-manufacturing-small-business-v2-self-hosted-erp-vocabulary-reference (defer)

> **NEW observation (2026-09-24).** Documents in-window GitHub Search `topic:small-business+language:python` query result: `celerp/celerp` (**NOASSERTION (`spdx_id: 'NOASSERTION'` in raw JSON — §3.2 BLOCKER for code adoption → vocabulary-only artifact; description hints "MIT modules"), 31★/8⑂ = +8★/24h star-inflow = the strongest single-day star-inflow delta on this repo in the 57-pass series' history, Python, pushed 2026-09-24T07:09:14Z = TODAY, created 2026-04-16T16:14:34Z, IN-WINDOW BY BOTH FIELDS, 20843 KB substantial repo, default_branch=`main`**). Topics (verbatim from raw JSON, **10 topics**): `accounting`, `double-entry-accounting`, `erp`, `fastapi`, `inventory-management`, `invoicing`, `manufacturing`, `postgresql`, `self-hosted`, `small-business`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-24): *"Downloadable, self-hosted desktop ERP for business operations. Modular, source-available core, MIT modules, no cloud required."* **The only 2026-09-24 in-window v2 self-hosted-ERP-vocabulary-reference that pins all 10 of `accounting + double-entry-accounting + erp + fastapi + inventory-management + invoicing + manufacturing + postgresql + self-hosted + small-business` in the topic array** = **8/10 LE31-relevant topics** = the **strongest self-hosted-FastAPI-Postgres-ERP stack-shape of the 57-pass brainstorm series** = **the only of today's 3 picks with +8★/24h star-inflow delta**. Bucket: **v2 self-hosted-ERP-vocabulary-reference (defer, parking-lot)** — watch-list entry, zero build time today. **HONEST DISCLOSURE**: this repo was previously surfaced in `/opt/data/le31-brainstorm-2026-09-12.md` and `/opt/data/le31-brainstorm-2026-09-14.md` (carry-over mentions in features 90/94) as a NOT-picked watch-list-only candidate — parent explicitly declined it twice because the topic-overlap score was below threshold; the subagent surfaced it again today and parent re-evaluates positively based on the *8/10 topic-overlap score + 31★ + TODAY push + NOASSERTION-with-MIT-modules-description* combined signal, but the **§3.2 NOASSERTION blocker means this pick is vocabulary-only — no code adoption is possible without author negotiation**; same prior-rejection-then-promotion pattern as yesterday's Pick B `donbarbos/telegram-bot-template` and 09-21's Pick C `penguineer/PingBoardDaemon`.

## Goal

Retain the **"Downloadable, self-hosted desktop ERP for business operations. Modular, source-available core, MIT modules, no cloud required."** + **"accounting + double-entry-accounting + erp + fastapi + inventory-management + invoicing + manufacturing + postgresql + self-hosted + small-business"** decuple-primitive as a persistent cross-section reference for any future LE31 v2 expansion that needs a *self-hosted-FastAPI-ERP + PostgreSQL + double-entry-accounting + inventory-management + manufacturing + invoicing + small-business* baseline to compare against. The artifact is the persistent cross-section reference + the ten named architectural primitives (accounting, double-entry-accounting, erp, fastapi, inventory-management, invoicing, manufacturing, postgresql, self-hosted, small-business). No code today (NOASSERTION license blocks code adoption; vocabulary-only artifact today; description hints "MIT modules" but the GitHub-level `spdx_id` is NOASSERTION; 20843 KB substantial-repo size makes source-code inspection immediately productive if author grants re-license).

## Scope

**In scope (defer artifact):**
- A written record of the **self-hosted + single-tenant + on-premise** discipline: the *single-tenant-deployment* posture (LE31 v1 today is single-tenant + on-premise per charter §3.1; the *self-hosted* discipline IS the *single-tenant-deployment* posture applied to the *integrated-business-process-management* dimension).
- A written record of the **FastAPI + PostgreSQL** discipline: the *direct LE31 v1 backend stack match* (charter §3.2: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres) — today's pick pins both `fastapi` + `postgresql` as topics, the only 2026-09-24 GitHub Search candidate that does so simultaneously with `erp + double-entry-accounting + manufacturing`.
- A written record of the **ERP + accounting + double-entry-accounting + invoicing** discipline: the *integrated-business-process-management* cluster (finance + inventory + orders + reporting in one system; the *double-entry-accounting* discipline IS the *every-transaction-has-two-legs* pattern; the *invoicing* discipline IS the *customer-facing-receivable-tracking* primitive).
- A written record of the **inventory-management + manufacturing** discipline: the *inventory-and-production* cluster (the *inventory-management* primitive IS the *what-stocks-do-we-have-and-what-do-we-need-to-reorder* query; the *manufacturing* primitive IS the *production-process-tracking* discipline).
- A written record of the **small-business** discipline: the *small-business-software* category (LE31 v1 is one-small-restaurant = small-business).
- A written record of the **MIT-modules hint** in the description: the *some-modules-are-MIT-permissive* discipline (the *core* is *source-available* but the description says "MIT modules"; this is a hopeful signal for re-license possibility but not a license).
- A decision record: today's verdict is `defer` because (a) the NOASSERTION license blocks code adoption and (b) LE31 v2 is not built today; the comparison baseline is informative, not a build-trigger.
- A cross-section reference with the prior v2 self-hosted-ERP stack-shape cluster: features 90/94 (the prior carry-over watch-list-only mentions), 152 (`lattice-governance-first-authorized-ai-architecture`), 195 (`skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management` Frappe-ERPNext-cloud-kitchen), 223 (`psb684-sketch-athena` ERP-inventory-management-small-business-SQLite from 09-23). The *transferable insight* is the **self-hosted + FastAPI + PostgreSQL + ERP + inventory-management + accounting + double-entry-accounting + invoicing + manufacturing + small-business** decuple-primitive.

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
- Any code-adoption from this repo (NOASSERTION §3.2 BLOCKER; vocabulary-only artifact; code adoption would require author re-license negotiation).

## Description

GitHub Search `topic:small-business+language:python` query (parent re-fetched live, see `/tmp/le31-brainstorm-2026-09-24/gh/gh_01_topic-small-business.json`) returned 77 total / 50 retrieved candidates; `celerp/celerp` is one of the 30 net-new in-window candidates. It is the **only 2026-09-24 in-window v2 self-hosted-ERP-vocabulary-reference that pins all 10 of `accounting + double-entry-accounting + erp + fastapi + inventory-management + invoicing + manufacturing + postgresql + self-hosted + small-business` in the topic array**.

The `celerp/celerp` repo's architectural pattern has ten core sub-primitives:

1. **Self-hosted + single-tenant + on-premise** — the *single-tenant-deployment* posture. The phrase *"Downloadable, self-hosted"* explicitly names the *single-tenant + no-cloud* posture (matches LE31 v1's *single-tenant + on-premise* posture per charter §3.1); *"no cloud required"* explicitly names the *no-cloud-dependency* discipline.

3. **FastAPI + PostgreSQL** — direct LE31 v1 backend stack match. The *FastAPI + PostgreSQL* posture is exactly the LE31 v1 backend stack (charter §3.2: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres). LE31 v1 today uses FastAPI + SQLModel + Postgres; the *celerp/celerp* repo confirms the *FastAPI + PostgreSQL + self-hosted-ERP* posture is achievable in 20843 KB (note: substantial-repo size; source-code inspection immediately productive if author grants re-license).

5. **ERP + accounting + double-entry-accounting + invoicing** — the *integrated-business-process-management* cluster. The *ERP* discipline IS the *integrated-business-process-management* pattern: finance + inventory + orders + reporting in one system; the *accounting + double-entry-accounting* discipline IS the *every-transaction-has-two-legs* pattern; the *invoicing* discipline IS the *customer-facing-receivable-tracking* primitive.

7. **Inventory-management + manufacturing** — the *inventory-and-production* cluster. The *inventory-management* primitive IS the *what-stocks-do-we-have-and-what-do-we-need-to-reorder* query; charter §3.2 baseline = StockEntry-append-only (every prepared-item quantity change is a new `StockEntry`; never update or delete ledger events; current stock is derived from entries); the *manufacturing* primitive IS the *production-process-tracking* discipline (LE31 v1 today does not have manufacturing; the *manufacturing* discipline IS the *batch-production + multi-stage-production-process* pattern applied to the integrated-business-process-management dimension).

9. **Small-business** — the *small-business-software* category. LE31 v1 is one-small-restaurant = small-business; the *small-business* vocabulary IS the *single-owner-single-operator* posture.

11. **MIT-modules hint** — the *some-modules-are-MIT-permissive* discipline. The description says *"Modular, source-available core, MIT modules, no cloud required."* This is a hopeful signal that *some modules* may be MIT-permissive even though the GitHub-level `spdx_id` is NOASSERTION; the **description is informational but the license is the spdx_id field**; vocabulary-only artifact today.

The LE31 relevance is the **self-hosted + FastAPI + PostgreSQL + ERP + inventory-management + accounting + double-entry-accounting + invoicing + manufacturing + small-business** decuple-primitive. LE31 v1 today has working single-restaurant-vertical product; the question this repo answers is "what does a self-hosted-FastAPI-Postgres-ERP + double-entry + manufacturing baseline look like in 2026?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2 expansion trigger condition (if the first v2 PR that adds a self-hosted-ERP-horizontal surface to the LE31 v2 operator surface lands):** potential schema additions (depending on the v2 surface):
- `app/erp_modules/` — possibly add (the self-hosted-ERP module directory; depends on the v2 change).
- `app/erp_modules/accounting.py` — possibly add (the double-entry-accounting handler; depends on the v2 change).
- `app/erp_modules/inventory.py` — possibly add (the inventory-management handler; depends on the v2 change).
- `app/erp_modules/invoicing.py` — possibly add (the invoicing handler; depends on the v2 change).
- `app/models/erp_accounts.py` — possibly add (the `erp_accounts` SQLModel table; double-entry-accounting ledger; depends on the v2 change).
- `app/models/erp_invoices.py` — possibly add (the `erp_invoices` SQLModel table; depends on the v2 change).
- `app/models/erp_manufacturing.py` — possibly add (the `erp_manufacturing` SQLModel table; depends on the v2 change).
- `tests/test_erp_modules.py` + `tests/test_erp_accounts.py` + `tests/test_erp_invoices.py` + `tests/test_erp_manufacturing.py` — possibly add (the integration tests for the self-hosted-ERP + double-entry-accounting + invoicing + manufacturing surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no self-hosted-ERP-horizontal-expansion surface added.

## Implementation steps

**NONE today.** The defer artifact is documentation only. Implementation steps if the future v2 trigger condition fires:

1. **Negotiate re-license with `celerp/celerp` author** — the *MIT modules* descriptor in the description is a hopeful signal; the LE31 v2 maintainer should contact the author to ask for explicit MIT-permissive licensing of the relevant modules (likely `accounting`, `inventory-management`, `invoicing`). This is the prerequisite for any code adoption.
2. **Read the `celerp/celerp` source** (20843 KB substantial-repo size) — identify the *self-hosted + single-tenant + no-cloud* primitives; identify the *FastAPI + PostgreSQL* stack-match patterns; identify the *double-entry-accounting* ledger-discipline; identify the *inventory-management* StockEntry-append-only pattern; identify the *invoicing + manufacturing* surface primitives.
3. **Adapt the vocabulary to LE31 v2's existing schema** (no direct import due to NOASSERTION license; vocabulary + architecture-reference adoption only) — re-implement the *self-hosted-FastAPI-ERP + double-entry + inventory-management + manufacturing + invoicing* primitive against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack.
4. **Document the cross-section** in `specs/` (the present HANDOFF.md) — record the *self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing + small-business* decuple-primitive as a persistent cross-section reference for future v2 self-hosted-ERP-horizontal-expansion reviews.
5. **Verify the cross-section** by reading at least 3 of the 10 LE31-relevant-topic primitives in source code (accounting + inventory-management + invoicing are the three most transferable).
6. **Update the LE31 v2 horizontal-expansion roadmap** to reflect the *self-hosted-FastAPI-ERP* vocabulary primitive as a future-build option.

**No code today.**

## Telegram interaction if any

None today. The defer artifact is documentation only; no Telegram operator surface changes.

## Dependencies

- **No new dependencies today.** The defer artifact is documentation only.
- **Future v2 dependencies (if the v2 trigger condition fires and author re-license is granted):** `fastapi` (already in LE31 v1 stack per charter §3.2), `sqlalchemy` (already in LE31 v1 stack via SQLModel per charter §3.2), `postgresql` (already in LE31 v1 stack per charter §3.2). No new Python packages required.

## Open questions

- **Does LE31 v2 ever need a self-hosted-ERP horizontal-expansion surface?** Today no; v1 is single-restaurant-vertical. If v2 ever expands to multiple vertical-business-types, the *self-hosted + FastAPI + PostgreSQL + ERP* primitive is the cleanest cross-section reference. **Status: parking-lot until v2 expansion is on the roadmap.**
- **Would `celerp/celerp`'s author grant a re-license for the relevant parts (accounting + inventory-management + invoicing)?** The *MIT modules* descriptor in the description is a hopeful signal but not a license. **Status: unknown; would require author contact.**
- **Is the *+8★/24h star-inflow* delta sustainable or a one-off?** Today is the first time this repo has shown a TODAY push in the 57-pass series; the +8★ delta is the largest single-day star-inflow on record for this repo. **Status: observation only; will re-check next pass.**
- **Is `celerp/celerp` actually a *desktop* ERP or a *web* ERP?** The description says *"Downloadable, self-hosted desktop ERP"* — but the topics include `fastapi + postgresql` which is the web-stack primitive. The *"desktop"* in the description likely means *desktop-deployment* (i.e. self-hosted on a desktop machine, not *desktop-UI*). **Status: observation only; would require source-code inspection to confirm.**

## Why this matters

The *self-hosted + FastAPI + PostgreSQL + ERP + inventory-management + accounting + double-entry-accounting + invoicing + manufacturing + small-business* decuple-primitive is the **strongest v2-self-hosted-ERP-vocabulary reference of the 57-pass series**. LE31 v1 today is single-restaurant-vertical; the v2 horizontal-expansion question is *"if v2 ever needs to support multiple vertical-business-types (restaurants + cafes + bars + retail + small-business-ERP), what does the *self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing* vocabulary look like in 2026?"* Today's pick documents that vocabulary with the **only 2026-09-24 GitHub Search candidate that pins all of `fastapi + postgresql + erp + double-entry-accounting + manufacturing` simultaneously** = the closest LE31-stack-shape match for the *self-hosted-FastAPI-ERP + double-entry + manufacturing + invoicing + small-business* quintuple-primitive. The **+8★/24h star-inflow** is the strongest single-day star-inflow signal on this repo in the 57-pass series' history, suggesting *celerp/celerp* is gaining adoption as the *self-hosted-FastAPI-ERP* reference of choice in 2026 — the vocabulary reference is becoming more credible as the reference ecosystem grows.

Without this artifact, a future LE31 v2 maintainer facing the *self-hosted-FastAPI-ERP horizontal-expansion* question would have to discover the *self-hosted + FastAPI + PostgreSQL + ERP + double-entry + manufacturing + invoicing + small-business* vocabulary from scratch; with this artifact, the vocabulary is documented as a persistent cross-section reference with the *8/10 topic-overlap score + 31★ + 20843 KB substantial-repo size + IN-WINDOW BY BOTH FIELDS* combined signal.