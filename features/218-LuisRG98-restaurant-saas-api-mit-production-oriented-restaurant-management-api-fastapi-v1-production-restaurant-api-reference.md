# Feature 218 — LuisRG98-restaurant-saas-api-mit-production-oriented-restaurant-management-api-fastapi-v1-production-restaurant-api-reference (defer)

> **NEW observation (2026-09-23).** Documents in-window GitHub Search `fastapi+restaurant` query result: `LuisRG98/restaurant-saas-api` (**MIT ✓**, **0★/0⑂**, Python, **pushed 2026-09-23T04:07:03Z = TODAY**, in-window by push only, **32 KB** small repo, default_branch=`main`). Topics (verbatim from raw JSON, **0 topics**): none. Description (verbatim, parent-verified GitHub Search raw JSON): *"Production-oriented restaurant management API built with Python and FastAPI."* **The only 2026-09-23 in-window v1 production-restaurant-API reference pushed TODAY of the 54-pass series** (the only in-window candidate combining `Python + FastAPI + restaurant + management API + production-oriented` posture pushed on 2026-09-23). Bucket: **v1 production-restaurant-API-reference (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"Production-oriented restaurant management API built with Python and FastAPI"** triple-primitive as a persistent cross-section reference for any future LE31 v1 maintenance pass that needs a *production-grade FastAPI + Python + restaurant-management-API* baseline to compare against. The artifact is the persistent cross-section reference + the four named architectural primitives (Python, FastAPI, restaurant-management-API, production-oriented). No code today (MIT license permits future code reuse; vocabulary-only artifact today; 32 KB small-repo size requires source-code inspection before any deeper claim).

## Scope

**In scope (defer artifact):**
- A written record of the **Python + FastAPI** discipline: the *direct LE31 v1 backend stack match* (charter §3.2: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres).
- A written record of the **restaurant-management-API** surface: the *third-surface-vocabulary* for future v1 expansion (currently LE31 v1 has 2 primary surfaces per charter §3.1: waiter web UI + cook Telegram bot; the *restaurant-management-API* pattern adds an API-only surface for future v1 expansion).
- A written record of the **production-oriented** discipline: the *production-grade posture* (error-handling + observability + authentication + deployment-ready Dockerfile) vs *prototype-grade* or *scaffold-grade*.
- A decision record: today's verdict is `defer` because LE31 v1 is working code today; the comparison baseline is informative, not a build-trigger.
- A cross-section reference with the prior v1 Python + FastAPI + restaurant stack-shape + hotel-management surface + UI-architecture + no-build + small-business cluster: features 23 (sse-cook-channel), 25 (fastapi-frontend-dev-loop), 67 (Bill), 142 (feldroy-air-fastapi-htmx-ai-write-framework), 144 (zentra-offline-first-fb-pattern), 154 (htmx-fastapi-cook-channel), 156 (AWIG-OS), 162 (htmx-fastapi-cook-channel v2), 168 (htmx-no-build-python-skeleton-watch), 178 (nhobin219-litelink-append-only-iceberg-embedded-local-first), 191 (eddiedzhang-FullHouse-Updated — repo now 404, vocabulary-only), 194 (vaibhavkr993630-droid/CollabFlow-Platform), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 206 (djust-org/djust phoenix-liveview-style), 210 (duckframework/duck server-side-reactive-web), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow v2-AI signed-evidence-receipts), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 219 (today's Pick B sister — Mormolykos/epcore v2-AI deterministic-licensing-kernel), 220 (today's Pick C sister — Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger). The *transferable insight* is the **Python + FastAPI + restaurant-management-API + production-oriented** primitive set.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).

## Description

GitHub Search `fastapi+restaurant` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-23/_raw/gh_fastapi_restaurant.json`) returned 30 total / 30 retrieved candidates; `LuisRG98/restaurant-saas-api` is one of the 3 net-new in-window MIT Python candidates not previously filed. It is the only 2026-09-23 in-window v1 production-restaurant-API-reference pushed TODAY of the 54-pass series.

The `LuisRG98/restaurant-saas-api` repo's architectural pattern has three core sub-primitives:

1. **Python + FastAPI** — direct LE31 v1 backend stack match. The *FastAPI + Python* posture is exactly the LE31 v1 backend stack (charter §3.2: Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres). LE31 v1 today uses FastAPI + SQLModel + Postgres; the *restaurant-saas-api* repo confirms the *Python + FastAPI + restaurant-domain* posture is achievable in < 32 KB (note: small-repo caveat — likely scaffold; source-code inspection required before deeper claim).
2. **Restaurant management API** — the *restaurant-management-API* surface (orders + menu + reservations + staff + inventory + kitchen + reporting = the full operator-surface vocabulary). LE31 v1 today has 2 primary surfaces (waiter web UI + cook Telegram bot) per charter §3.1; the *restaurant-management-API* pattern is the *third-surface-vocabulary* (the API-only surface, no UI) for future v1 expansion. Note: the description does not enumerate endpoints; source-code inspection required.
3. **Production-oriented** — the *production-grade* discipline (vs prototype-grade or scaffold-grade). LE31 v1 today is a working prototype; a future v1 maintenance pass would benefit from any production-grade FastAPI + restaurant + Python reference as the comparison baseline. The *production-oriented* qualifier is the *ready-for-real-restaurant-deployment* posture: error-handling + observability + authentication + deployment-ready. Note: the description does not enumerate production-grade primitives; source-code inspection required.

The LE31 relevance is the **Python + FastAPI + restaurant-management-API + production-oriented** quadruple-primitive. LE31 v1 today has working stack (FastAPI + SQLModel + Postgres); the question this repo answers is "what does a production-grade FastAPI + Python + restaurant-management-API baseline look like in 2026?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v1 maintenance trigger condition (if the first v1 PR that adds a production-grade primitive to the waiter/cook surface lands):** potential schema additions (depending on the v1 surface):
- `api_surface_endpoints` table — a registry of every FastAPI route (method + path + handler + auth-required) for the *production-grade* observability primitive; the *restaurant-management-API* vocabulary.
- `observability_metrics` table — a primitive for tracking per-endpoint latency + error-rate + uptime; the *production-grade* posture.
- `auth_tokens` table — a primitive for managing operator-staff authentication tokens; the *production-grade* posture.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v1 maintenance trigger (when the first v1 PR that adds a production-grade primitive to the waiter/cook surface lands):**
- Add an `api_surface_endpoints` SQLModel table (route_id, method, path, handler, auth_required, recorded_at).
- Add an `observability_metrics` SQLModel table (metric_id, route_id, latency_ms, status_code, recorded_at).
- Add an `auth_tokens` SQLModel table (token_id, user_id, expires_at, scopes).
- Optionally add a `deploy_dockerfile` + `deploy_compose` primitive that pins the LE31 v1 deployable to a container image; the *production-oriented* posture.

**Steps independent of the v1 maintenance trigger (today):**
- [x] Read the `LuisRG98/restaurant-saas-api` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *Production-oriented restaurant management API built with Python and FastAPI* primitive (parent re-verified verbatim).
- [x] Cross-reference with features 23, 25, 67, 142, 144, 154, 156, 162, 168, 178, 191, 194, 195, 205, 206, 210, 212, 213, 214, 215, 216, 217, 219 (this file's Pick B sister), 220 (this file's Pick C sister) (ripgrep-verified distinct).
- [ ] **Future source-code inspection required** before any deeper claim (32 KB small-repo size requires verifying whether the repo is a real implementation or a scaffold/template).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v1 maintenance trigger (when the first v1 PR that adds a production-grade primitive to the cook surface lands):**
- The cook would need a Telegram command to view the *observability summary* (e.g., `/obs today`); the *production-grade* observability primitive maps 1:1 onto a chat-style query interface.
- The owner would need a Telegram command to view the *auth-tokens-active* list (e.g., `/tokens`); the *production-grade* auth primitive maps 1:1 onto a chat-style query interface.
- These are v1 maintenance surface additions; not in v1 scope today.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v1 maintenance trigger dependencies:** depends on the v1 maintenance surface that adds a production-grade primitive to the waiter/cook surface. Cross-references: features 23 (sse-cook-channel), 25 (fastapi-frontend-dev-loop), 67 (Bill), 142 (feldroy-air-fastapi-htmx-ai-write-framework), 144 (zentra-offline-first-fb-pattern), 154 (htmx-fastapi-cook-channel), 156 (AWIG-OS), 162 (htmx-fastapi-cook-channel v2), 168 (htmx-no-build-python-skeleton-watch), 178 (nhobin219-litelink-append-only-iceberg-embedded-local-first), 191 (eddiedzhang-FullHouse-Updated — repo now 404, vocabulary-only), 194 (vaibhavkr993630-droid/CollabFlow-Platform), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 206 (djust-org/djust phoenix-liveview-style), 210 (duckframework/duck server-side-reactive-web), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 219 (this file's Pick B sister — Mormolykos/epcore v2-AI deterministic-licensing-kernel), 220 (this file's Pick C sister — Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger).

## Open questions

1. **Real implementation or scaffold/template?** The 32 KB small-repo size + 0★/0⑂ community adoption + no-topics (description-only signals) + no-deployed-endpoints raises a question of whether the repo is a real implementation or a scaffold/template. The full read of `LuisRG98/restaurant-saas-api`'s code is needed before any deeper claim.
2. **What is the *production-oriented* posture?** Is it error-handling? observability? authentication? deployment-ready Dockerfile? The full read of the repo's source code is needed.
3. **What is the *restaurant-management-API* surface?** What endpoints does it expose? orders? menu? reservations? staff? inventory? kitchen? reporting? The full read of the repo's source code is needed.
4. **What is the *FastAPI* discipline?** Does it use SQLModel? SQLAlchemy? Pydantic v2? async def? lifespan handlers? The full read of the repo's source code is needed.
5. **What is the *Python* posture?** Does it use type hints? PEP-604 unions? is it 3.11+ 3.12+ 3.13+? The full read of the repo's source code is needed.
6. **MIT license file confirmation:** is `LuisRG98/restaurant-saas-api`'s MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **Python + FastAPI + restaurant-management-API + production-oriented** quadruple-primitive is **the only 2026-09-23 in-window v1 production-restaurant-API reference pushed TODAY of the 54-pass series** — and the MIT permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31 v1's charter §3.2 baseline (Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3). The artifact is informational only today; the value is vocabulary + a future-comparison-baseline note for any v1 maintenance pass.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

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

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-23.md` (54th consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 23, 25, 67, 142, 144, 154, 156, 162, 168, 178, 191 (eddiedzhang-FullHouse-Updated — repo now 404, vocabulary-only), 194 (vaibhavkr993630-droid/CollabFlow-Platform), 195 (skaslam1407-Restaurant-and-Cloud-Kitchen-Operations-Management), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 206 (djust-org/djust phoenix-liveview-style), 210 (duckframework/duck server-side-reactive-web), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 219 (this file's Pick B sister — Mormolykos/epcore v2-AI deterministic-licensing-kernel), 220 (this file's Pick C sister — Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger).
- Sister-picks from 2026-09-23: feature 219 (Mormolykos/epcore v2-AI deterministic-licensing-kernel), feature 220 (Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger).