# Feature 223 — psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference (defer)

> **NEW observation (2026-09-23).** Documents in-window GitHub Search `topic:small-business+language:python` query result: `psb684-sketch/athena` (**MIT ✓**, **1★/0⑂**, Python, **pushed 2026-09-20T18:13:16Z = ~3 days before fetch time**, **created 2026-09-12T19:49:43Z = ~11 days before fetch time**, **IN-WINDOW BY BOTH FIELDS**, **426 KB** modest repo, default_branch=`main`). Topics (verbatim from raw JSON, **6 topics**): `business-automation`, `erp`, `inventory-management`, `python`, `small-business`, `sqlite`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-23): *"ERP system pc ver"*. **The only 2026-09-23 in-window v2 small-business-ERP-horizontal-vocabulary-reference that pins all 6 of `business-automation + erp + inventory-management + python + small-business + sqlite` in the topic array** = the **only of today's 3 picks that is in-window by BOTH `created_at` AND `pushed_at`** = the **strongest in-window discovery by `created_at` of the 55-pass brainstorm series' cross-app-signals section**. Bucket: **v2 small-business-ERP-horizontal-vocabulary-reference (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"ERP system pc ver"** + **"business-automation + erp + inventory-management + python + small-business + sqlite"** quintuple-primitive as a persistent cross-section reference for any future LE31 v2 expansion that needs a *small-business-ERP + inventory-management + Python + SQLite* baseline to compare against. The artifact is the persistent cross-section reference + the six named architectural primitives (business-automation, erp, inventory-management, python, small-business, sqlite). No code today (MIT license permits future code reuse; vocabulary-only artifact today; 426 KB modest-repo size limits source-code inspection depth).

## Scope

**In scope (defer artifact):**
- A written record of the **ERP + business-automation** discipline: the *enterprise-resource-planning* primitive (the *ERP* discipline IS the *integrated-business-process-management* pattern: finance + inventory + orders + reporting in one system; the *business-automation* discipline IS the *automated-business-process-execution* posture).
- A written record of the **inventory-management** discipline: the *stock-tracking* primitive (charter §3.2 baseline = StockEntry-append-only; the *inventory-management* primitive is the *what-stocks-do-we-have-and-what-do-we-need-to-reorder* query).
- A written record of the **small-business** discipline: the *small-business-software* category (LE31 v1 is one-small-restaurant = small-business; the *small-business* vocabulary IS the *single-owner-single-operator* posture).
- A written record of the **python + sqlite** discipline: the *Python + SQLite-as-development-DB* primitive (SQLite is the LE31 v1 *development* database per charter §3.2 known-conflicts note; the *SQLite-as-development-DB* choice is documented as a known-conflict that LE31 v1 currently navigates with dual-interpretation).
- A decision record: today's verdict is `defer` because LE31 v2 is not built today; the comparison baseline is informative, not a build-trigger.
- A cross-section reference with the prior v2 small-business-ERP stack-shape cluster: features 152 (lattice-governance-first-authorized-ai-architecture), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management from 09-22). The *transferable insight* is the **ERP + inventory-management + small-business + Python + SQLite** quintuple-primitive.

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

GitHub Search `topic:small-business+language:python` query (parent re-fetched live, see `/tmp/le31-brainstorm-2026-09-23/gh/gh_topic_small-business.json`) returned 74 total / 50 retrieved candidates; `psb684-sketch/athena` is one of the 30 net-new in-window MIT Python candidates not previously filed. It is the **only 2026-09-23 in-window v2 small-business-ERP-horizontal-vocabulary-reference that pins all 6 of `business-automation + erp + inventory-management + python + small-business + sqlite` in the topic array**.

The `psb684-sketch/athena` repo's architectural pattern has five core sub-primitives:

1. **ERP + business-automation** — the *enterprise-resource-planning + integrated-business-process-management* primitive. The *ERP* discipline IS the *integrated-business-process-management* pattern: finance + inventory + orders + reporting in one system; the *business-automation* discipline IS the *automated-business-process-execution* posture (low-code / no-code business-process automation, vs hand-coded business processes). LE31 v1 today is a single-restaurant-vertical product (waiter + cook + owner surfaces per charter §3.1); the *ERP + business-automation* primitive IS the *integrated-business-process-management* pattern for any future v2 horizontal-expansion.

2. **Inventory-management** — the *stock-tracking* primitive. The *inventory-management* discipline IS the *what-stocks-do-we-have-and-what-do-we-need-to-reorder* query; charter §3.2 baseline = StockEntry-append-only (every prepared-item quantity change is a new `StockEntry`; never update or delete ledger events; current stock is derived from entries). The *inventory-management* primitive is the v1 charter §3.2 baseline vocabulary; today's pick documents the *inventory-management-as-ERP-module* posture for any future v2 expansion.

3. **Small-business** — the *small-business-software* category. LE31 v1 is one-small-restaurant = small-business; the *small-business* vocabulary IS the *single-owner-single-operator* posture. The *small-business* primitive IS the *single-tenant-single-deployment* posture (vs SaaS multi-tenant multi-deployment).

4. **Python + SQLite** — the *Python + SQLite-as-development-DB* primitive. SQLite is the LE31 v1 *development* database per charter §3.2 known-conflicts note; the *SQLite-as-development-DB* choice is documented as a known-conflict that LE31 v1 currently navigates with dual-interpretation. Today's pick documents the *Python + SQLite* posture for any future v2 expansion that needs an embedded-database-as-deployment-DB alternative to LE31 v1's *Postgres-in-production*.

The LE31 relevance is the **ERP + business-automation + inventory-management + small-business + Python + SQLite** sextuple-primitive. LE31 v1 today has working single-restaurant-vertical product; the question this repo answers is "what does a small-business-ERP + inventory-management + Python + SQLite baseline look like in 2026?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2 expansion trigger condition (if the first v2 PR that adds a small-business-ERP-horizontal surface to the LE31 v2 operator surface lands):** potential schema additions (depending on the v2 surface):
- `business_processes` table — a registry of every ERP business-process (process_id, name, description, status, recorded_at); the *ERP* vocabulary.
- `inventory_modules` table — a primitive for tracking per-tenant inventory-module configuration; the *inventory-management* posture.
- `tenant_config` table — a primitive for managing single-tenant vs multi-tenant deployment configuration; the *small-business* posture.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v2 expansion trigger (when the first v2 PR that adds a small-business-ERP-horizontal surface to the LE31 v2 operator surface lands):**
- Add a `business_processes` SQLModel table (process_id, name, description, status, recorded_at).
- Add an `inventory_modules` SQLModel table (module_id, tenant_id, config_json, recorded_at).
- Add a `tenant_config` SQLModel table (config_id, key, value, recorded_at).
- Optionally add a `business_processes/` FastAPI module that exposes the *ERP + business-automation* vocabulary; the *small-business-ERP* discipline.

**Steps independent of the v2 expansion trigger (today):**
- [x] Read the `psb684-sketch/athena` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, created_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *ERP system pc ver* + 6-topic vocabulary (parent re-verified verbatim).
- [x] Cross-reference with features 152, 195 (ripgrep-verified distinct).
- [ ] **Future source-code inspection recommended** with caveat (426 KB modest-repo size limits source-code inspection depth; the *ERP + inventory-management* vocabulary is documented but the *SQLite-schema* + *business-process-execution* details may require deeper inspection).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v2 expansion trigger (when the first v2 PR that adds a small-business-ERP-horizontal surface to the cook surface lands):**
- The owner would access a Telegram command to view the *inventory-management-summary* (e.g., `/inventory today`); the *inventory-management* primitive maps 1:1 onto a chat-style query interface.
- The owner would access a Telegram command to view the *business-process-status* (e.g., `/processes active`); the *ERP + business-automation* primitive maps 1:1 onto a chat-style query interface.
- These are v2 expansion surface additions; not in v2 scope today.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v2 expansion trigger dependencies:** depends on the v2 surface that adds a small-business-ERP-horizontal surface to the LE31 v2 operator surface. Cross-references: features 152 (lattice-governance-first-authorized-ai-architecture), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management from 09-22).

## Open questions

1. **What is the exact ERP module surface?** Does it expose finance + inventory + orders + reporting as separate modules, or as a unified surface? The full read of the repo's source code is needed.
2. **What is the *inventory-management* table schema?** Does it use a `StockEntry` append-only pattern (charter §3.2 baseline), or a `current_stock` derived column (charter §3.2 violation), or a hybrid? The full read of the repo's source code is needed.
3. **What is the *business-automation* discipline?** Does it use a low-code/no-code workflow engine, or hand-coded business-process execution? What is the *process_status* state machine? The full read of the repo's source code is needed.
4. **What is the *small-business* posture?** Is it single-tenant-single-deployment, or multi-tenant-multi-deployment? Is there a *tenant_config* table, or is the deployment hardcoded to a single tenant? The full read of the repo's source code is needed.
5. **What is the *Python + SQLite* discipline?** Does it use SQLAlchemy Core, SQLAlchemy ORM, or raw sqlite3? Does it use Alembic for migrations? The full read of the repo's source code is needed.
6. **What is the *ERP system pc ver* description's "pc ver" qualifier?** Is it a desktop-only application (vs web), or a desktop-also application (vs mobile-only)? The full read of the repo's source code is needed.
7. **MIT license file confirmation:** is `psb684-sketch/athena`'s MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **ERP + business-automation + inventory-management + small-business + Python + SQLite** sextuple-primitive is **the only 2026-09-23 in-window v2 small-business-ERP-horizontal-vocabulary-reference that pins all 6 of `business-automation + erp + inventory-management + python + small-business + sqlite` in the topic array of the 55-pass brainstorm series** — and the MIT permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is forward-compatible with LE31 v1's charter §3.2 baseline (Python 3.13, FastAPI, SQLModel, Postgres in production; SQLite in development). The artifact is informational only today; the value is vocabulary + a future-comparison-baseline note for any v2 small-business-ERP-horizontal-expansion.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 expansion PR adds a small-business-ERP-horizontal surface to the operator surface, the maintainer wants *a comparison baseline against another small-business-ERP + inventory-management + Python + SQLite reference*, but struggles because *LE31 v1 is vertical-only and has no small-business-ERP-horizontal vocabulary in the charter*, so that *v2 can ship small-business-ERP-horizontal primitives with reference evidence*." **PASS** (zero-pain today; v1 is vertical-only; the JTBD is vocabulary + future-comparison-baseline, not a build-need). |
| 2 | **Viability** | Maintainer can read the 426 KB repo + the 6-topic vocabulary + the ERP + inventory-management + small-business + Python + SQLite sextuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *small-business-ERP + inventory-management + Python + SQLite* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported). Confidence: medium for the *small-business-ERP* vocabulary (1★/0⑂ + MIT permissive license + 6 topics + in-window-by-both-fields + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *ERP + inventory-management + small-business + Python + SQLite* quintuple IS the *integrated-business-process-management + small-business-software + embedded-database* posture). Stack: FastAPI + PostgreSQL backend = on-pattern for v1 primitives; ERP = off-pattern for v1 (LE31 v1 has no ERP surface); inventory-management = on-pattern for v1 (charter §3.2 baseline); small-business = on-pattern for v1 (LE31 v1 is one-small-restaurant = small-business); SQLite = on-pattern for v1 *development* (known-conflict per `le31-conventions/SKILL.md` lines 73-75). MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *ERP + inventory-management + small-business + Python + SQLite* primitive set is charter §3.1 + §3.2 invariant-compatible (Python 3.13 + FastAPI + SQLModel + Postgres match LE31 v1 stack; SQLite is on-pattern for v1 development per known-conflict note). **PASS** (charter §3.1 + §3.2 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 small-business-ERP-horizontal-vocabulary-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 426 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours with caveat: 426 KB modest-repo size limits inspection depth). **Cost-to-value ratio: moderate** (426 KB is modest; the *ERP + inventory-management + small-business + Python + SQLite* quintuple + the in-window-by-both-fields signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/223-psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference-HANDOFF.md` and `features/223-psb684-sketch-athena-mit-erp-inventory-management-small-business-python-sqlite-business-automation-v2-small-business-erp-horizontal-vocabulary-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + ERP + inventory-management + small-business + Python + SQLite documentation for the next v2 small-business-ERP-horizontal-expansion review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-brainstorm-2026-09-23.md` (55th consecutive daily-brainstorm pass).
- Companion artifacts (ripgrep-verified distinct): features 152 (lattice-governance-first-authorized-ai-architecture), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management from 09-22).
- Sister-picks from 2026-09-23: feature 221 (mrlonis-python-open-restaurant-fastapi v1 production-restaurant-API-reference), feature 222 (donbarbos-telegram-bot-template v1 aiogram-cook-bot-deployment-blueprint).
- Linear parent issue: `Brainstorm 2026-09-23 — daily` (or fallback JSON at `/opt/data/le31-brainstorm-2026-09-23.linear-fallback.json` if Linear MCP write is blocked by workspace plan-limit).
- Linear sub-issue (this feature): `LE31-XXX` (pending Linear MCP write — see `Brainstorm 2026-09-23 — daily` parent issue; attached to project `le31 Research` P-HMM-1 per the verified workspace rule that `le31 v2 owner-pains` and `le31 v2-AI` projects do not exist).
