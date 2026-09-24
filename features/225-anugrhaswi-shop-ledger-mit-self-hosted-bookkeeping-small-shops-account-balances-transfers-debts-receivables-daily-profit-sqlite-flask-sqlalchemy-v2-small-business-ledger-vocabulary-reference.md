# Feature 225 — anugrhaswi-shop-ledger-mit-self-hosted-bookkeeping-small-shops-account-balances-transfers-debts-receivables-daily-profit-sqlite-flask-sqlalchemy-v2-small-business-ledger-vocabulary-reference (defer)

> **NEW observation (2026-09-24).** Documents in-window GitHub Search `topic:small-business+language:python` query result: `anugrhaswi/shop-ledger` (**MIT ✓**, **0★/0⑂** (fresh discovery, 0★ = no traction yet), Python (Flask framework), **pushed 2026-09-24T02:19:45Z = TODAY** (FRESH PUSH TODAY; in-window by `pushed_at`), **created 2026-07-01T19:03:59Z** (~3-month-old repo with in-window `pushed_at`; **IN-WINDOW BY PUSH ONLY**; `created_at` is OUT-OF-WINDOW by ~2 months), **148 KB** modest repo, default_branch=`main`). Topics (verbatim from raw JSON, **9 topics**): `accounting`, `bookkeeping`, `finance`, `flask`, `ledger`, `python`, `small-business`, `sqlalchemy`, `sqlite`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-24): *"Simple self-hosted bookkeeping for small shops. Track account balances, transfers, debts, receivables, and daily profit - everything stored locally in one SQLite file."* **The only 2026-09-24 in-window v2 small-business-ledger-vocabulary-reference that pins all 9 of `accounting + bookkeeping + finance + flask + ledger + python + small-business + sqlalchemy + sqlite` in the topic array** = **9/9 LE31-relevant topics** = **100% topic-overlap score** = **the first 100% topic-overlap score of any 2026-09 GitHub Search candidate**. Bucket: **v2 small-business-ledger-vocabulary-reference (defer, parking-lot)** — watch-list entry, zero build time today. **HONEST DISCLOSURE**: this repo was not previously surfaced in any prior brainstorm report — the FRESH PUSH TODAY is the first in-window event for this repo in the 57-pass series; the 9/9 topic-overlap score + FRESH PUSH TODAY combination is the strongest cross-section JTBD signal of today's 3 picks; same fresh-discovery pattern as 09-22's Pick C `penguineer/PingBoardDaemon` (also a fresh-discovery-then-promotion).

## Goal

Retain the **"Simple self-hosted bookkeeping for small shops. Track account balances, transfers, debts, receivables, and daily profit - everything stored locally in one SQLite file."** + **"accounting + bookkeeping + finance + flask + ledger + python + small-business + sqlalchemy + sqlite"** nonuple-primitive as a persistent cross-section reference for any future LE31 v2 expansion that needs a *self-hosted-bookkeeping + small-shops + double-entry-accounting + daily-profit + Flask + SQLAlchemy + SQLite* baseline to compare against. The artifact is the persistent cross-section reference + the nine named architectural primitives (accounting, bookkeeping, finance, flask, ledger, python, small-business, sqlalchemy, sqlite). No code today (MIT license permits future code reuse; vocabulary-only artifact today; 148 KB modest-repo size makes source-code inspection immediately productive for the v2 maintainer).

## Scope

**In scope (defer artifact):**
- A written record of the **self-hosted + single-tenant + on-premise** discipline: the *single-tenant-deployment* posture (LE31 v1 today is single-tenant + on-premise per charter §3.1; the *self-hosted* discipline IS the *single-tenant-deployment* posture applied to the *bookkeeping* dimension).
- A written record of the **Flask + SQLAlchemy + SQLite** discipline: the *Python + SQLite-as-deployment-DB* primitive (LE31 v1 uses FastAPI + SQLModel + PostgreSQL per charter §3.2; the *Flask + SQLAlchemy + SQLite* posture is a *sister-stack* discipline; the *flask* vs *fastapi* difference is sister-shape not off-stack; the *SQLite-as-deployment-DB* primitive is a known-conflict per `le31-conventions/SKILL.md` lines 73-75 that LE31 v1 currently navigates with dual-interpretation).
- A written record of the **bookkeeping + accounting + finance** discipline: the *small-business-bookkeeping* vocabulary (the *bookkeeping* primitive IS the *every-transaction-recorded-as-a-double-entry* discipline; the *accounting* primitive IS the *financial-statement-generation* discipline; the *finance* primitive IS the *capital-management* discipline).
- A written record of the **ledger** discipline: the *small-business-ledger* vocabulary (the *ledger* primitive IS the *append-only-transaction-log* discipline; charter §3.2 baseline = StockEntry-append-only; the *small-business-ledger* vocabulary IS the *append-only-ledger* applied to the *small-business-bookkeeping* dimension).
- A written record of the **small-business** discipline: the *small-business-software* category (LE31 v1 is one-small-restaurant = small-business).
- A written record of the **daily-profit** surface: the *daily-P&L-calculation* primitive (the *what-was-today's-profit* query is the simplest business-intelligence primitive; today's pick documents the *daily-profit-as-bookkeeping-output* posture for any future v2 expansion).
- A written record of the **account-balances + transfers + debts + receivables** discipline: the *double-entry-accounting-modules* vocabulary (the *account-balances* primitive IS the *current-balance-per-account* query; the *transfers* primitive IS the *inter-account-money-movement* discipline; the *debts* primitive IS the *payable-tracking* primitive; the *receivables* primitive IS the *receivable-tracking* primitive).
- A decision record: today's verdict is `defer` because LE31 v2 is not built today; the comparison baseline is informative, not a build-trigger.
- A cross-section reference with the prior v2 small-business-ledger stack-shape cluster: features 170 (`devShakib015/ShopDesk` offline-POS-as-stock-ledger from 09-12), 172 (`bamideleadedeji-hybrid-inventory-restock-spreadsheet` from 09-12), 223 (`psb684-sketch-athena` ERP-inventory-management-small-business-SQLite from 09-23). The *transferable insight* is the **self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite** octuple-primitive.

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

## Description

GitHub Search `topic:small-business+language:python` query (parent re-fetched live, see `/tmp/le31-brainstorm-2026-09-24/gh/gh_01_topic-small-business.json`) returned 77 total / 50 retrieved candidates; `anugrhaswi/shop-ledger` is one of the 30 net-new in-window candidates. It is the **only 2026-09-24 in-window v2 small-business-ledger-vocabulary-reference that pins all 9 of `accounting + bookkeeping + finance + flask + ledger + python + small-business + sqlalchemy + sqlite` in the topic array** = **9/9 LE31-relevant topics** = **100% topic-overlap score**.

The `anugrhaswi/shop-ledger` repo's architectural pattern has nine core sub-primitives:

1. **Self-hosted + single-tenant + on-premise** — the *single-tenant-deployment* posture. The phrase *"Simple self-hosted"* explicitly names the *single-tenant + no-cloud* posture (matches LE31 v1's *single-tenant + on-premise* posture per charter §3.1); *"everything stored locally in one SQLite file"* explicitly names the *embedded-database-as-deployment-DB* posture.

3. **Flask + SQLAlchemy + SQLite** — the *Python + SQLite-as-deployment-DB* stack. The *Flask* framework is sister-shape to LE31 v1's FastAPI (both are Python web frameworks with route-handler + blueprint-architecture patterns); the *SQLAlchemy* ORM is sister-shape to LE31 v1's SQLModel (SQLModel IS SQLAlchemy + Pydantic, so the *SQLAlchemy* primitive transfers); the *SQLite* database is the *embedded-database-as-deployment-DB* primitive (LE31 v1 today uses SQLite for *development* but Postgres for *production* per charter §3.2; the *SQLite-as-deployment-DB* posture is the more aggressive option).

5. **Bookkeeping + accounting + finance** — the *small-business-bookkeeping* vocabulary. The *bookkeeping* primitive IS the *every-transaction-recorded-as-a-double-entry* discipline; the *accounting* primitive IS the *financial-statement-generation* discipline (income-statement + balance-sheet + cash-flow-statement); the *finance* primitive IS the *capital-management* discipline (cash-on-hand + working-capital + capital-efficiency).

7. **Ledger** — the *small-business-ledger* vocabulary. The *ledger* primitive IS the *append-only-transaction-log* discipline; charter §3.2 baseline = StockEntry-append-only (every prepared-item quantity change is a new `StockEntry`; never update or delete ledger events; current stock is derived from entries). Today's pick documents the *small-business-ledger* vocabulary as a sister-shape to LE31 v1's *StockEntry-append-only* ledger.

9. **Small-business** — the *small-business-software* category. LE31 v1 is one-small-restaurant = small-business; the *small-business* vocabulary IS the *single-owner-single-operator* posture.

11. **Daily-profit** — the *daily-P&L-calculation* primitive. The *daily-profit* view shows the operator today's P&L at a glance; the *daily-profit* primitive IS the *summarize-today's-transactions* discipline applied to the *small-business-bookkeeping* dimension.

13. **Account-balances + transfers + debts + receivables** — the *double-entry-accounting-modules* vocabulary. The *account-balances* primitive IS the *current-balance-per-account* query; the *transfers* primitive IS the *inter-account-money-movement* discipline; the *debts* primitive IS the *payable-tracking* primitive; the *receivables* primitive IS the *receivable-tracking* primitive.

The LE31 relevance is the **self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite** octuple-primitive. LE31 v1 today has working single-restaurant-vertical product; the question this repo answers is "what does a small-business-bookkeeping + double-entry-accounting + daily-P&L baseline look like in 2026?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2 expansion trigger condition (if the first v2 PR that adds a small-business-ledger-horizontal surface to the LE31 v2 operator surface lands):** potential schema additions (depending on the v2 surface):
- `app/bookkeeping/` — possibly add (the small-business-bookkeeping module directory; depends on the v2 change).
- `app/bookkeeping/ledger.py` — possibly add (the double-entry-accounting ledger handler; depends on the v2 change).
- `app/bookkeeping/daily_pnl.py` — possibly add (the daily-P&L-calculation handler; depends on the v2 change).
- `app/bookkeeping/balances.py` — possibly add (the account-balances query handler; depends on the v2 change).
- `app/models/bookkeeping_accounts.py` — possibly add (the `bookkeeping_accounts` SQLModel table; depends on the v2 change).
- `app/models/bookkeeping_transactions.py` — possibly add (the `bookkeeping_transactions` SQLModel table; double-entry ledger; depends on the v2 change).
- `app/models/bookkeeping_daily_pnl.py` — possibly add (the `bookkeeping_daily_pnl` SQLModel table; depends on the v2 change).
- `tests/test_bookkeeping.py` + `tests/test_bookkeeping_ledger.py` + `tests/test_bookkeeping_daily_pnl.py` — possibly add (the integration tests for the small-business-bookkeeping + double-entry + daily-P&L surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no small-business-ledger-horizontal-expansion surface added.

## Implementation steps

**NONE today.** The defer artifact is documentation only. Implementation steps if the future v2 trigger condition fires:

1. **Read the `anugrhaswi/shop-ledger` source** (148 KB modest-repo size) — identify the *self-hosted + single-tenant + no-cloud* primitives; identify the *Flask + SQLAlchemy + SQLite* stack patterns; identify the *bookkeeping + accounting + finance + ledger* disciplines; identify the *daily-profit + account-balances + transfers + debts + receivables* surfaces.
2. **Adapt the vocabulary to LE31 v2's existing schema** — re-implement the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* primitive against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack (note: LE31 v1 uses Postgres in production; the *SQLite-as-deployment-DB* posture would be a v2 expansion question).
3. **Document the cross-section** in `specs/` (the present HANDOFF.md) — record the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* octuple-primitive as a persistent cross-section reference for future v2 small-business-ledger-horizontal-expansion reviews.
4. **Verify the cross-section** by reading all 9 of the 9 LE31-relevant-topic primitives in source code (every topic in the topic array maps to an LE31-relevant keyword — this is the strongest topic-overlap signal of the 57-pass series).
5. **Update the LE31 v2 horizontal-expansion roadmap** to reflect the *small-business-bookkeeping + double-entry + daily-profit + SQLite* vocabulary primitive as a future-build option.

**No code today.**

## Telegram interaction if any

None today. The defer artifact is documentation only; no Telegram operator surface changes.

## Dependencies

- **No new dependencies today.** The defer artifact is documentation only.
- **Future v2 dependencies (if the v2 trigger condition fires):** `fastapi` (already in LE31 v1 stack per charter §3.2), `sqlalchemy` (already in LE31 v1 stack via SQLModel per charter §3.2). No new Python packages required.
- **Optional future v2 dependency**: `sqlite` (LE31 v1 today uses SQLite for development but not for production; the *SQLite-as-deployment-DB* posture would require schema-validation + migration-discipline that LE31 v1 does not currently have).

## Open questions

- **Does LE31 v2 ever need a small-business-ledger horizontal-expansion surface?** Today no; v1 is single-restaurant-vertical. If v2 ever expands to multiple vertical-business-types, the *self-hosted-bookkeeping + double-entry + daily-profit + SQLite* primitive is the cleanest cross-section reference. **Status: parking-lot until v2 expansion is on the roadmap.**
- **Does LE31 v1 need a daily-P&L surface today?** Today's pick documents the *daily-profit-as-bookkeeping-output* posture, but v1 currently does not have a daily-P&L surface. **Status: parking-lot until v1 daily-P&L surface is on the roadmap (could be a future v1 maintenance question if owner asks for daily-profit visibility).**
- **Is the *sqlite-as-deployment-DB* posture applicable to LE31 v1?** Today no; v1 uses Postgres in production per charter §3.2. The known-conflict note in `le31-conventions/SKILL.md` lines 73-75 documents the dual-interpretation that LE31 v1 currently navigates. **Status: known-conflict; future v2 question.**
- **Would the *account-balances + transfers + debts + receivables* primitives apply to LE31 v2?** Today no; v1 does not have these surfaces. **Status: parking-lot until v2 expansion is on the roadmap.**

## Why this matters

The *self-hosted-bookkeeping + small-shops + account-balances + transfers + debts + receivables + daily-profit + SQLite* octuple-primitive is the **cleanest small-business-ledger primitive of the 57-pass series**. LE31 v1 today is single-restaurant-vertical; the v2 horizontal-expansion question is *"if v2 ever needs to support multiple vertical-business-types (restaurants + cafes + bars + retail + small-business-ledger), what does the *self-hosted-bookkeeping + double-entry + daily-profit + SQLite* vocabulary look like in 2026?"* Today's pick documents that vocabulary with the **only 2026-09-24 GitHub Search candidate that pins 9/9 LE31-relevant topics** = the **first 100% topic-overlap score of any 2026-09 GitHub Search candidate** = the closest LE31-stack-shape match for the *small-business-ledger + double-entry + daily-profit* triple-primitive. The **FRESH PUSH TODAY** is the first in-window event for this repo in the 57-pass series; the **MIT permissive license + 148 KB modest-repo size + FRESH PUSH TODAY** combination is the strongest cross-section JTBD signal of today's 3 picks.

Without this artifact, a future LE31 v2 maintainer facing the *small-business-ledger horizontal-expansion* question would have to discover the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* vocabulary from scratch; with this artifact, the vocabulary is documented as a persistent cross-section reference with the *9/9 topic-overlap score + 0★/0⑂ + MIT permissive + 148 KB modest-repo size + FRESH PUSH TODAY + IN-WINDOW BY PUSH ONLY* combined signal.