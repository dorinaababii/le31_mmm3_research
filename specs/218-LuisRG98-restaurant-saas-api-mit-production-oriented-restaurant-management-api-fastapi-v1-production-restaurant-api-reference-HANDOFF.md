# 218 — LuisRG98-restaurant-saas-api-mit-production-oriented-restaurant-management-api-fastapi-v1-production-restaurant-api-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v1 maintenance surface becomes buildable. **Do not implement today.** Source-code inspection follow-up required (32 KB small-repo size + 0 topics + no source-code inspection = the repo may be a scaffold/template rather than a real implementation).

## 1. Active feature path

`features/218-LuisRG98-restaurant-saas-api-mit-production-oriented-restaurant-management-api-fastapi-v1-production-restaurant-api-reference.md` (defer artifact; **no code today**).

Bucket: **v1 production-restaurant-API-reference (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + §3.2 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v1 maintenance PR adds a production-grade primitive (error-handling + observability + authentication + deployment-ready Dockerfile), the owner wants *a comparison baseline against another production-grade FastAPI + Python + restaurant-management-API reference*, but struggles because *LE31 v1 is small enough that no in-repo comparison baseline exists*, so that *v1 maintenance can ship production-grade primitives with reference evidence*." **PASS** (zero-pain today; v1 is small enough that the comparison baseline is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-low for the architectural match (the *Python + FastAPI + restaurant-management-API + production-oriented* primitive set is well-established in the GitHub 0★-community-adoption cluster; the 32 KB small-repo size + 0 topics + no source-code inspection is a caveat — the repo may be a scaffold/template rather than a real implementation; **source-code inspection required before any deeper claim**). MIT license is charter-compatible per §3.2. **PASS** (with caveat). |
| 4 | **Conflict** | None. The *Python + FastAPI + restaurant-management-API + production-oriented* primitive set is charter §3.1 + §3.2 invariant-compatible (Python 3.13 + FastAPI + SQLModel + Postgres match LE31 v1 stack exactly). **PASS** (charter §3.1 + §3.2 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 production-restaurant-API-reference (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation + a source-code-inspection follow-up). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours). **Cost-to-value ratio: high** (small artifact is already tight; source-code inspection is the value-multiplier). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/218-LuisRG98-restaurant-saas-api-mit-production-oriented-restaurant-management-api-fastapi-v1-production-restaurant-api-reference-HANDOFF.md` and `features/218-LuisRG98-restaurant-saas-api-mit-production-oriented-restaurant-management-api-fastapi-v1-production-restaurant-api-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference + the source-code-inspection follow-up task).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 maintenance trigger condition fires (first v1 PR that adds a production-grade primitive to the waiter/cook surface):

- `app/models/api_surface_endpoints.py` — possibly add an `api_surface_endpoints` SQLModel table (route_id, method, path, handler, auth_required, recorded_at).
- `app/models/observability_metrics.py` — possibly add an `observability_metrics` SQLModel table (metric_id, route_id, latency_ms, status_code, recorded_at).
- `app/models/auth_tokens.py` — possibly add an `auth_tokens` SQLModel table (token_id, user_id, expires_at, scopes).
- `deploy/Dockerfile` — possibly add a `deploy_dockerfile` that pins the LE31 v1 deployable to a container image.
- `deploy/docker-compose.yml` — possibly add a `deploy_compose` that orchestrates the LE31 v1 deployable.
- `app/bot/obs_today.py` — possibly add a Telegram-bot command for the cook to view the *observability summary* (e.g., `/obs today`).
- `app/bot/tokens.py` — possibly add a Telegram-bot command for the owner to view the *auth-tokens-active* list (e.g., `/tokens`).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [x] `features/218-LuisRG98-restaurant-saas-api-mit-production-oriented-restaurant-management-api-fastapi-v1-production-restaurant-api-reference.md` exists and is read back by the parent.
- [x] `specs/218-LuisRG98-restaurant-saas-api-mit-production-oriented-restaurant-management-api-fastapi-v1-production-restaurant-api-reference-HANDOFF.md` (this file) exists and is read back by the parent.
- [x] The GitHub repo description is quoted verbatim: *"Production-oriented restaurant management API built with Python and FastAPI."*
- [x] The MIT permissive license is documented.
- [x] The *Python + FastAPI + restaurant-management-API + production-oriented* primitive set is documented.
- [x] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/` + INDEX.md row + parent research report file.

**Future v1 maintenance trigger (when the first v1 PR that adds a production-grade primitive to the waiter/cook surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The *Python + FastAPI + restaurant-management-API + production-oriented* primitive set is evaluated against the PR's changes: does the change add a FastAPI route that matches `restaurant-management-API` semantics? Does the change add an observability primitive? Does the change add an authentication primitive? Does the change add a deployment-ready Dockerfile?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 maintenance surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `api_surface_endpoints` table; remove the new `observability_metrics` table; remove the new `auth_tokens` table; restore the original schema.
- Migration cost: depends on the v1 maintenance change; the *Python + FastAPI + restaurant-management-API + production-oriented* primitive set's design implies *additive schema* (the new tables are additive on top of the existing append-only log).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

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

This is the **54th-pass daily-research Pick A** (2026-09-23). Bucket: **v1 production-restaurant-API-reference**. Build verdict: **`defer`** (parking-lot, vocabulary-only artifact). The cross-section reference is the artifact. No code today. The future v1 maintenance trigger condition is *first v1 PR that adds a production-grade primitive to the waiter/cook surface*. Sister-picks today: feature 219 (Mormolykos/epcore v2-AI deterministic-licensing-kernel), feature 220 (Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger). Source-code inspection follow-up required for `LuisRG98/restaurant-saas-api` (32 KB small-repo caveat).

## 8. Trigger condition for re-evaluation

The artifact is *re-evaluable* when:
- A v1 PR lands that adds a production-grade primitive to the waiter/cook surface (observability / authentication / deployment-ready Dockerfile).
- A v1 PR lands that adds an API-only surface (the *restaurant-management-API* vocabulary).
- The source-code inspection of `LuisRG98/restaurant-saas-api` reveals a real implementation (vs scaffold/template).

When any of these trigger conditions fires, the coding agent should:
1. Re-read the GitHub repo structure of `LuisRG98/restaurant-saas-api`.
2. Compare against LE31 v1's actual waiter/cook surface.
3. Identify the transferable architectural primitives.
4. Apply the LE31 seven-check gate from `le31-conventions/SKILL.md`.

## 9. Sign-off gap

The artifact is vocabulary-only; no end-to-end behavior is built today. The verification protocol section's "Future v1 maintenance trigger" checklist is the placeholder for the next coding-agent reviewer.

---

**Linear sub-issue (intended, blocked):** HMM-299 in `le31 v1 — Core MVP` (parent: HMM-298 in `le31 Research`); fallback at `/opt/data/le31-daily-research-2026-09-23.linear-fallback.json` (Linear MCP write endpoint BLOCKED by workspace plan-limit).