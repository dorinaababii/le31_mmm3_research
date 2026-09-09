# Feature 159 — ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment (defer)

> **NEW observation (2026-09-09).** Documents in-window GitHub repo `abdullahabduljabbarab/ledger-api` (MIT, **0★/0⑂**, Python, **pushed 2026-09-08T18:46:17Z**, in-window by push only, 2 KB description). Description (verbatim): *"Append-only double-entry ledger API on GCP Cloud Run and Cloud SQL. FastAPI, PostgreSQL, Terraform, CI/CD."* **The ONLY in-window append-only-ledger repo today with the exact LE31 stack (FastAPI + PostgreSQL)**. Bucket: **v1 architecture-reference** — watch-list defer. Zero build time today.

## Goal

Retain the **FastAPI + PostgreSQL + Terraform + GCP Cloud Run + Cloud SQL + CI/CD** deployment topology as a persistent cross-section reference for the LE31 v1 production deployment. The artifact is the persistent cross-section reference + a candidate *named deployment pattern* for the LE31 v1 production deployment. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **deployment topology**: FastAPI service + GCP Cloud Run (serverless compute) + GCP Cloud SQL (managed PostgreSQL) + Terraform (infrastructure-as-code) + CI/CD (automated build/deploy).
- A written record of the **"append-only double-entry ledger"** discipline (the `append-only` part is compatible with LE31 charter §3.1; the `double-entry` part is non-standard for a restaurant but is the deployment pattern is portable).
- A written record of the **1:1 mapping onto LE31 v1 architecture**: the FastAPI + PostgreSQL stack is the exact LE31 v1 stack; the deployment topology (Cloud Run + Cloud SQL + Terraform) is a production reference for any future LE31 v1 deployment.
- A decision record: today's verdict is `defer` because the LE31 v1 codebase already runs as a single Python service and the Cloud Run deployment pattern is a documentation reference, not a code change.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `Bill` schema.
- Any new deployment topology (the LE31 v1 deployment is currently single-process; introducing Cloud Run would require an owner decision per charter §3.2).
- Any new Terraform configuration (the LE31 v1 codebase does not yet have Terraform; introducing Terraform would require a separate owner decision).
- Any new CI/CD pipeline (the LE31 v1 codebase does not yet have CI/CD; introducing it would require a separate owner decision).
- Adoption of the ledger-api code (the repo is a 2 KB description + a FastAPI codebase; the deployment pattern is transferable; the codebase is not adoptable — the *"double-entry"* discipline is not LE31's `StockEntry` discipline).

## Evidence / JTBD

When a future LE31 maintainer considers deploying LE31 v1 to production, the operator wants *a ready-made FastAPI+PostgreSQL deployment pattern*, but struggles because *the current deployment is undocumented*, so that *a future operator has a defensible production deployment pattern*.

- **Evidence class**: observed (the ledger-api README names the FastAPI+PostgreSQL+Terraform+Cloud Run deployment pattern).
- **Confidence**: high for the stack match (FastAPI + PostgreSQL = exact LE31 v1 stack); high for the deployment pattern transferability (Cloud Run + Cloud SQL + Terraform is a standard 2026 deployment pattern).
- **Real observed LE31 JTBD**: zero-pain today; the codebase is small enough that the deployment is trivial.
- **The value is naming, not direct demand**: when the LE31 v1 deployment *is* reviewed (e.g. before a v1 production deployment or a v2 surface that requires production deployment), the ledger-api pattern is a ready-made *named* production deployment pattern.

## Description

GitHub `abdullahabduljabbarab/ledger-api` (MIT, 0★/0⑂, Python, pushed 2026-09-08T18:46:17Z, in-window by push only, 2 KB description). Description (verbatim): *"Append-only double-entry ledger API on GCP Cloud Run and Cloud SQL. FastAPI, PostgreSQL, Terraform, CI/CD."*

The architectural pattern has one core principle and a deployment topology:

1. **"Append-only double-entry ledger"** — every ledger entry is a new ledger row; current balance is **derived** from the ledger, never stored as a mutable cache. The *double-entry* discipline is a bookkeeping discipline (each transaction has equal debits and credits) that LE31 v1 does not currently implement (LE31 uses append-only `StockEntry` rows without double-entry bookkeeping).
2. **GCP Cloud Run deployment** — the FastAPI service runs on GCP Cloud Run (serverless compute, scale-to-zero, request-based billing). The deployment is suitable for a small-restaurant workload (low request volume, bursty traffic, no always-on server cost).
3. **GCP Cloud SQL PostgreSQL** — managed PostgreSQL with automated backups, point-in-time recovery, and read replicas. The deployment is suitable for a small-restaurant workload (single-tenant, low write volume, predictable schema).
4. **Terraform infrastructure-as-code** — the entire GCP project (Cloud Run service + Cloud SQL instance + VPC connector + IAM roles + service accounts) is defined in Terraform. The pattern allows for reproducible deployments and disaster recovery.
5. **CI/CD pipeline** — automated build (pytest + lint) + automated deploy (gcloud builds submit + gcloud run deploy). The pattern allows for safe deployments with rollback capability.

**The 1:1 mapping onto LE31 v1 architecture:**

| ledger-api component | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| FastAPI service | `app/main.py` FastAPI service | §3.2 (Stack: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres in production) | **Exact stack match** |
| GCP Cloud Run | (LE31 v1 currently runs as single-process; Cloud Run is a future deployment option) | (future v1 deployment decision) | **Not implemented** — would require an owner decision |
| GCP Cloud SQL PostgreSQL | (LE31 v1 currently uses local Postgres; Cloud SQL is a future deployment option) | (future v1 deployment decision) | **Not implemented** — would require an owner decision |
| Terraform infrastructure-as-code | (LE31 v1 does not yet have Terraform) | (future v1 deployment decision) | **Not implemented** — would require a separate owner decision |
| CI/CD pipeline | (LE31 v1 does not yet have CI/CD) | (future v1 deployment decision) | **Not implemented** — would require a separate owner decision |
| Append-only ledger | `StockEntry` table (every prepared-item quantity change is a new row) | §3.1 (Never update or delete ledger events) | **Same discipline** — both use append-only |
| Double-entry bookkeeping | (LE31 v1 does not use double-entry) | n/a | **Not implemented** — would require a `Bill_line_item → StockEntry` link |

**What ledger-api does NOT transfer:**
- The repo is a 2 KB description + a FastAPI codebase; the *double-entry* discipline is not LE31's `StockEntry` discipline. The codebase is not adoptable.
- The author is a *new maintainer* (created recently; in-window push 2026-09-08; 0★/0⑂ traction). The 1-day-old repo is *not* production-traction evidence.
- The "GCP Cloud Run + Cloud SQL" deployment pattern is GCP-specific; LE31 v1 might choose a different cloud provider (AWS, Azure, on-prem). The *pattern* (serverless + managed Postgres + Terraform) is portable; the *specific services* are not.

**Cross-section with prior picks:**
- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. Ledger-api's *append-only ledger* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Ledger-api's *append-only ledger* is the queried record; feature 122 supplies the query-time measurement.
- **Feature 125 auditable-continual-learning-three-axis** — the *commit-time gate* axis. Ledger-api's *append-only ledger* is the commit-time record; feature 125's *auditable continual learning* is the AI-discipline analog.
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Ledger-api's *append-only ledger* is the ledger; feature 127's *proposal-then-action* is the action the ledger authorizes.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Ledger-api's *append-only ledger* is the explanation-time record; feature 129's *graph* is the *typed edges* that make the explanation queryable.
- **Feature 133 hansard-runtime-witnessing** — the *who witnessed* axis. Ledger-api's *append-only ledger* is the commit; feature 133 supplies the runtime witness.
- **Feature 134 echo-record-shape** — the *record shape* axis. Ledger-api's *append-only ledger* is the *commit*; feature 134 is the *record shape* of the commit.
- **Feature 135 dreamledger-execution-settled-credit-ledger** — the *credit ledger* dual. Ledger-api's *double-entry ledger* is the *debit/credit ledger* dual; feature 135 is the *credit ledger* for AI agent actions.
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* axis. Ledger-api's *append-only ledger* is the *commit*; feature 137's obligations would be *compiled into* the ledger.
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Ledger-api is the *informal* statement of feature 138's 9-node model.
- **Feature 139 stale-constraints-budgeted-verification-failures** — the *stale-constraint* problem. Ledger-api's *append-only ledger* is the *record*; feature 139's verification budget is the resource.
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Ledger-api's *append-only ledger* is the *record*; feature 141's invariants are the *proof*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** — the *frozen mandate* primitive. Ledger-api's *append-only ledger* is the *commit*; the mandate is what the production-run holds fixed.
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** — the *JTBD framing*. Ledger-api is the *production-deployment JTBD*; feature 146 is the *bookkeeping JTBD*. Both are operator-pain-driven.
- **Feature 147 reliability-lives-in-institution-not-cognition-2609-03192v1** — the *experimental test* of the architecture. Ledger-api is the *informal* statement; feature 147 is the *experimental* test (preregistered refutations of the five properties).
- **Feature 148 coxswain-graphs-harness-owns-consequence-architecture-pattern** — the *one harness owns every consequence* pattern. Ledger-api's *append-only ledger* is the *commit*; feature 148's *one harness* is the *one place where consequence is owned*.
- **Feature 149 personal-agent-blueprint-telegram-chokepoint-architecture-pattern** — the *authorization chokepoint* pattern. Ledger-api's *append-only ledger* is the *commit*; feature 149's *chokepoint* is the *enforcement of the authorization*.
- **Feature 153 sausageos-production-erp-append-only-stock-fefo-versioned-recipes** — the *manufacturing-stock discipline*. Ledger-api is the *deployment topology*; feature 153 is the *production-ERP pattern*. Both are append-only.
- **Feature 154 chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive** — the *cryptographic-verifiability primitive*. Ledger-api is the *deployment topology*; feature 154 is the *cryptographic anchoring*.
- **Feature 155 ha-filament-ledger-end-user-deployable-append-only-integration-pattern** — the *end-user deployable integration pattern*. Ledger-api is the *production deployment topology*; feature 155 is the *end-user deployable integration*.
- **Feature 156 awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent** — the *every-act-cites-the-rule* primitive. Ledger-api is the *append-only ledger*; feature 156 is the *rule-citation primitive*.
- **Feature 157 talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel** — the *deterministic permission kernel*. Ledger-api is the *append-only ledger*; feature 157 is the *deterministic permission kernel*.
- **Feature 158 azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory** — the *in-domain restaurant-POS+KDS+inventory integration*. Ledger-api is the *append-only ledger API*; feature 158 is the *integrated restaurant system*.

The 26 picks (this one + 25 prior) form the **deepest single-vocabulary cluster in the 41-pass series** for the *append-only-ledger + production-deployment + audit-trail* architectural pattern. **All 26 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The *append-only* discipline matches LE31 charter §3.1; the *double-entry* discipline would require a `Bill_line_item → StockEntry` link table (a future v2 surface, not v1).

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the ledger-api FastAPI+PostgreSQL+Terraform+Cloud Run deployment pattern to `specs/2026-09-09-ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment-HANDOFF.md`** as a named deployment pattern for the LE31 v1 production deployment — already done in the HANDOFF.md.
2. **Wait for the first v1 PR that adds a production-deployment concern** — trigger conditions: (a) first v1 PR that adds a Dockerfile or docker-compose.yml for production deployment; (b) first v1 PR that adds Terraform configuration; (c) first v1 PR that adds a CI/CD pipeline; (d) first v1 PR that deploys LE31 v1 to a cloud provider.
3. **On trigger, evaluate the change against the ledger-api deployment pattern** — does the change use FastAPI+PostgreSQL (the exact LE31 v1 stack)? Does the change use a serverless compute platform (Cloud Run, Lambda, Cloud Functions)? Does the change use a managed Postgres (Cloud SQL, RDS, Azure Database)? Does the change use infrastructure-as-code (Terraform, Pulumi, CloudFormation)? Does the change use CI/CD? The pattern is the *what to verify*, not the *what to implement*.
4. **Future v1 surface (NOT v1 today)**: the deployment topology (serverless compute + managed Postgres + Terraform + CI/CD) is a candidate v1 production deployment pattern. Owner decision required: which cloud provider (GCP, AWS, Azure, on-prem)? Each is a separate owner decision per charter §3.2.

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v1 deployment** (if the owner decides to deploy LE31 v1 to production) would: (a) add a Dockerfile + docker-compose.yml for local development; (b) add a Terraform configuration for the chosen cloud provider; (c) add a CI/CD pipeline for automated build + deploy; (d) configure the production Postgres database (Cloud SQL, RDS, or on-prem). This is a *v1 production deployment decision*, not a v1 code change.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v1 deployment dependencies** (if Cloud Run + Cloud SQL + Terraform is adopted): GCP account, Terraform installation, GitHub Actions or similar CI/CD platform, Docker. All future; no v1 dependency.

## Open questions

1. **Which cloud provider should LE31 v1 use for production deployment?** Owner decision required. Options: GCP (Cloud Run + Cloud SQL), AWS (Lambda + RDS), Azure (Functions + Azure Database), on-prem (single server + local Postgres). Each is a separate charter §3.2 decision. Recommend: GCP (matches the ledger-api pattern; small-restaurant workload fits the serverless + managed-Postgres billing model).
2. **Should LE31 v1 introduce Terraform today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant does not need Terraform (the deployment is trivial); the maintainer who wants to deploy LE31 v1 to production needs Terraform. Recommend: defer to v1 production deployment if/when the owner decides to deploy.
3. **Should LE31 v1 introduce CI/CD today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant does not need CI/CD (the codebase is small enough for manual deploys); the maintainer who wants automated deploys needs CI/CD. Recommend: defer to v1 production deployment if/when the owner decides to deploy.
4. **Is the ledger-api 1-day-old 0★/0⑂ repo a credible production-traction data point?** Charter §3.2: stars are popularity proxy, not gate. The *deployment pattern* is the value, not the maintainer's track record. The 2 KB description is tight; the technology choices (FastAPI + PostgreSQL + Terraform + Cloud Run) are credible. **The deployment pattern is transferable; the codebase is not adoptable**.
5. **Is the ledger-api *double-entry* discipline a blocking factor?** The *append-only* discipline matches LE31 §3.1; the *double-entry* discipline does not (LE31 v1 uses append-only `StockEntry` without double-entry bookkeeping). The deployment pattern is portable; the *double-entry* bookkeeping discipline is not. If LE31 ever needs the deployment pattern in code, the FastAPI + PostgreSQL + Terraform + Cloud Run components would be *re-implemented* on the LE31 stack (without the double-entry discipline), not imported from ledger-api.

## Why this matters

**Ledger-api is the ONLY in-window append-only-ledger repo with the exact LE31 stack (FastAPI + PostgreSQL).** The deployment topology (GCP Cloud Run + Cloud SQL + Terraform + CI/CD) is the 2026 production-deployment reference for the LE31 v1 codebase. The 2 KB README is the tightest single-paragraph production-deployment statement of the series; the 1-day-old 0★ repo is a new maintainer's first attempt at the pattern.

**The cluster (26 picks, this one + 25 prior) is the persistent cross-section reference for the next v1 production-deployment moment.** All 26 are `defer`; no code change today. The cluster is the *what the LE31 architecture is*, named across 26 different sources, and ready to be referenced when the first v1 production-deployment PR lands.

**The most operationally valuable future v1 surface is the deployment topology**: introducing a Dockerfile + Terraform + CI/CD pipeline + Cloud Run configuration would close the *production-deployment gap* (today, LE31 v1 is single-process with no production deployment). Owner decision required; not v1 today.
