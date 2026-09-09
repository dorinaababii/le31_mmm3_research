# 2026-09-09 — `ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/159-ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment.md` (defer artifact; **no code today**).

Bucket: **v1 architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v1 is deployed to production, the operator wants *a ready-made FastAPI+PostgreSQL deployment pattern*, but struggles because *the current deployment is undocumented*, so that *a future operator has a defensible production deployment pattern*." **PASS** (zero-pain today; the codebase is small enough that the deployment is trivial; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 2 KB? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the stack match (FastAPI + PostgreSQL = exact LE31 v1 stack). MIT license permits documentation reference. **PASS**. |
| 4 | **Conflict** | None. The ledger-api *"append-only ledger"* pattern *is* the LE31 §3.1 *every prepared-item quantity change is a new `StockEntry`* invariant; the *"double-entry"* discipline is non-standard for a restaurant but the deployment pattern is portable. **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2 KB description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2 KB is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-09-ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment-HANDOFF.md` and `features/159-ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v1 production-deployment moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a Dockerfile or docker-compose.yml for production deployment, Terraform configuration, CI/CD pipeline, or cloud-provider deployment):

- `Dockerfile` — possibly add (depends on the v1 deployment decision).
- `docker-compose.yml` — possibly add (depends on the v1 deployment decision).
- `terraform/` — possibly add (depends on the v1 deployment decision; GCP, AWS, Azure, or on-prem).
- `.github/workflows/` — possibly add (depends on the v1 deployment decision).
- `app/main.py` — possibly modify for production deployment (env vars, logging, health checks).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/159-ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment.md` exists and is read back by the parent.
- [ ] `specs/2026-09-09-ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The ledger-api description is quoted verbatim (2 KB repo).
- [ ] The 1:1 mapping onto LE31 v1 architecture is documented (FastAPI + PostgreSQL stack match).
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a Dockerfile, Terraform configuration, CI/CD pipeline, or cloud-provider deployment lands):**
- [ ] The PR is read back by the parent.
- [ ] The ledger-api deployment pattern is evaluated against the PR's changes: does the change use FastAPI+PostgreSQL (the exact LE31 v1 stack)? Does the change use a serverless compute platform? Does the change use a managed Postgres? Does the change use infrastructure-as-code? Does the change use CI/CD?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new Dockerfile + Terraform + CI/CD; restore the original single-process deployment.
- Migration cost: depends on the v1 deployment decision; the ledger-api pattern's *append-only* implies *no data migrations* (the deployment doesn't change the data model).
- Retained data: the `StockEntry` table retains all rows (charter §3.1); the deployment is a *new infrastructure* surface, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.

## 7. Handoff summary

| Field | Value |
|---|---|
| Feature ID | 159 |
| Slug | `ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment` |
| Bucket | v1 architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `Dockerfile` (possibly) + `docker-compose.yml` (possibly) + `terraform/` (possibly) + `.github/workflows/` (possibly) + `app/main.py` (possibly) |
| Trigger condition | First v1 PR that adds a Dockerfile or docker-compose.yml for production deployment, Terraform configuration, CI/CD pipeline, or cloud-provider deployment |
| Verification protocol | Does the change use FastAPI+PostgreSQL (the exact LE31 v1 stack)? Does it use a serverless compute platform? Does it use a managed Postgres? Does it use infrastructure-as-code? Does it use CI/CD? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-222 |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `abdullahabduljabbarab/ledger-api` (MIT, 0★, pushed 2026-09-08T18:46:17Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v1 trigger sign-off gap** (when the first v1 PR that adds a Dockerfile, Terraform configuration, CI/CD pipeline, or cloud-provider deployment lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the ledger-api deployment pattern is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v1 surface that adds a Dockerfile, Terraform configuration, CI/CD pipeline, or cloud-provider deployment will append a row here with: PR number, the ledger-api deployment pattern evaluated, the evaluation result, and the operator's sign-off.)*
