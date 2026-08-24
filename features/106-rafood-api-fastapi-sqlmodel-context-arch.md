# Feature 106 — Rafood FastAPI+SQLModel context-architecture (Watch-list)

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-24 (Pick A, **defer**) · **Bucket**: v2 owner-pains (parking-lot, future-context-decomposition)
> **One-line**: A research-only watch-list artifact that records the in-window `RafaelEmery/rafood-api` cross-section peer (3★ Python, pushed 2026-08-23) — **FastAPI + SQLModel + Alembic + Postgres + K8s + 5-context DDD separation** — as a future reference for LE31 v2 multi-context decomposition if/when it becomes necessary. **No code today; deferred indefinitely until either (a) LE31 v2 explicitly opens the multi-context decomposition question (charter §3 review pending), or (b) ≥2 independent FastAPI+SQLModel peers converge on the same 5→7 context count.**

## Goal

The 2026-08-24 brainstorm scan surfaced `RafaelEmery/rafood-api` (3★, Python, pushed 2026-08-23T22:28:04Z, https://github.com/RafaelEmery/rafood-api) — a FastAPI + SQLModel + Alembic + Postgres + K8s restaurant/products/offers API documented as **5 contexts**: Restaurants + Restaurant Schedules, Products, Offers + Offer Schedules, Categories, Users. The README literally lists "FastAPI + SQLModel & Alembic + PostgreSQL, PostGIS and GiST index for location data + Docker & Docker Compose + Kubernetes and Helm Charts on local Minikube cluster + GitOps with ArgoCD". This is **the exact LE31 v1 stack** (FastAPI + SQLModel + Alembic + Postgres) plus a 5-context DDD separation pattern that LE31 v1 doesn't currently document.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 v2 team considers whether to decompose the LE31 backend into multiple bounded contexts (e.g., splitting `StockEntry` writes from menu reads from owner-recap reads), the team wants to know whether a peer FastAPI + SQLModel + Alembic + Postgres project documents a clean 5-context separation, so that the decomposition is informed by a working reference and not invented from scratch.

**Why this is a fresh cross-section signal today**: `RafaelEmery/rafood-api` is the **only in-window FastAPI + SQLModel + Alembic + Postgres + K8s peer that documents a 5-context DDD separation**. The other in-window LE31-stack peers are:
- `satisfecho/pos` 31★ AGPL-3.0 Python — direct LE31-stack match but AGPL blocks import per charter §3.2; covered by features 40/42/89.
- `devnest-hq/restaurant-management-system` 1★ MIT Python — closest direct LE31-stack match but README not yet read; fails the gate today (defer, carry-over).
- `mileswwatkins/cowen_current_favorites` 11★ Python — restaurant-data scrape, not a backend reference.

None of the above document a 5-context DDD separation. `rafood-api` is the unique pattern-record candidate.

## Scope

**In scope (v2 owner-pains, S effort, ≤1 day, defer — LE31 already ships the surface):**
- Daily direct-repo `GET https://api.github.com/repos/RafaelEmery/rafood-api` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `rafood-api` README + ADRs + ER model in the next daily-research pass to confirm the 5-context separation (READ ONLY — no import).
- Tracking star velocity + push activity on `RafaelEmery/rafood-api`.
- Documenting the 5-context separation pattern in the LE31 research notes (this artifact is the document).

**Out of scope (no new LE31 implementation):**
- A new FastAPI+SQLModel backend. LE31 uses FastAPI + SQLModel + Postgres today and the surface is already shipped.
- A multi-context decomposition of the LE31 backend. LE31's current single-tenant posture (charter §3) is the correct v1 scope; multi-context decomposition is a charter-level decision deferred to v2.
- A `rafood-api` import. The repo has no license detected (`null`); importing unlicensed code is incompatible with charter §3.9 truth.
- Any new feature based on the `rafood-api` code surface.

## Description

**Evidence precondition:** observed (GitHub `RafaelEmery/rafood-api` 3★ + Python + FastAPI + SQLModel + Alembic + Postgres + K8s + 2026-08-23 push + 5-context separation documented in README). Confidence: **medium** for the cross-section pattern (the README documents the 5-context separation explicitly); **low** for LE31-specific urgency (LE31's single-tenant context is correct for v1; the v2 decomposition is a future-tense concern).

### `RafaelEmery/rafood-api`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-24 (this pass) | **3★** | (track) | 2026-08-23T22:28:04Z | none | Python |

**Direct repo URL**: https://github.com/RafaelEmery/rafood-api

**Verbatim description** (from GitHub API):
> FastAPI project to manage restaurants, products and offers :hamburger:

**Verbatim README tools list** (from `GET /repos/RafaelEmery/rafood-api/readme`):
> Python (3.10.7) and Poetry, FastAPI, SQLModel & Alembic, Pytest for testing, PostgreSQL, PostGIS and GiST index for location data, Docker & Docker Compose, Prometheus & Grafana, Locust for load testing, GitHub Actions, Postman Newman for smoke tests on CI, Kubernetes and Helm Charts on local Minikube cluster, GitOps with ArgoCD on local Minikube cluster (PoC/sandbox), Cursor (AI-assisted development with rules and agent prompts)

**Verbatim 5-context README quote**:
> Based on the ER Model there are 5 folder to separate contexts: Restaurants and restaurant schedules, Products, Offers and offers schedules, Categories, Users

**Why this is the cross-section peer of the day:**

1. **The stack match is exact.** FastAPI + SQLModel + Alembic + Postgres — the same stack as LE31 v1. The addition of PostGIS, K8s, Helm, ArgoCD, Prometheus/Grafana, Cursor AI-assisted dev is interesting but secondary to the stack match.
2. **The 5-context separation is novel among in-window LE31-stack peers.** None of the in-window `satisfecho/pos`, `devnest-hq/restaurant-management-system`, `mileswwatkins/cowen_current_favorites`, `maojiebc/majia-huiyuan` document an explicit bounded-context separation. `rafood-api` is the unique pattern-record candidate.
3. **It is the only in-window ≥1★ peer that combines the LE31 stack with documentation of a 5-context DDD separation.** The README is publicly readable and the ADRs are at `adr/` (per README ToC).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 v2 team considers multi-context decomposition, the team wants to know whether a working FastAPI + SQLModel + Alembic + Postgres reference documents a 5-context separation, so that the decomposition is informed by a peer and not invented. Plausible but not currently blocking.
2. **Viability**: No new feature to operate; the pattern informs a future v2 decomposition decision. No new viability required.
3. **Practicability and confidence**: The peer repo is 3★ + Python + FastAPI + SQLModel + Alembic + Postgres + K8s + 5-context separation documented in README; high confidence in the pattern (the constraint is documented in the README). Low confidence in LE31-specific urgency (LE31's single-tenant posture is correct for v1; the v2 decomposition is future-tense).
4. **Conflict**: No invariant conflict. The pattern is informational and does not change LE31 v1 behavior.
5. **Outcome, appetite, scope**: v2 owner-pains parking-lot. S effort. ≤1 day. **Defer** — LE31 v1 single-tenant posture is correct; this artifact records the 5-context separation pattern for future v2 iteration.
6. **Cost to operational value**: Zero implementation cost; pure pattern-record artifact. High upside (architectural clarity for v2) at zero downside.
7. **Circuit breaker and reversibility**: Fully reversible. Watch-list artifact; can be deleted without consequence.

## Data model

**No schema changes.** Watch-list artifact only.

## Implementation steps

**None** — research-only artifact. The slice ships this Markdown file + a one-row `INDEX.md` update + a `*-HANDOFF.md` slice contract for the coding agent (which records the same non-action: "do not implement today; read README on next pass"). The slice hand-off is a no-op directive to the coding agent.

## Telegram interaction if any

**None** — the artifact does not interact with the LE31 Telegram-bot surface. The cross-section is observational only.

## Dependencies

- **No code dependencies** (research-only artifact).
- **External data dependency**: `RafaelEmery/rafood-api` README + ADRs + ER model — to be read in the next daily-research pass (carry-over to 2026-08-25).
- **Watch-list add to `le31-daily-research-2026-08-25` pass**: include `RafaelEmery/rafood-api` in the 5-repo watch list to track star velocity + push activity.

## Open questions

1. **What are the exact ADR topics in `RafaelEmery/rafood-api/adr/`?** The README ToC mentions ADRs at `adr/` folder; the next daily-research pass should confirm what decisions are documented (likely ADRs on stack choice, schema separation, K8s deployment, AI-assisted dev).
2. **Is the 3★ count maintained over the next 7 days?** Velocity will inform whether the pattern is gaining traction or is a single-author hobby project.
3. **Does the 5-context separation actually use Python module boundaries (folder structure) or is it documentation-only?** The answer determines how transferable the pattern is to LE31 v2.
4. **Does LE31 v2 charter need a multi-context decomposition?** This is a charter-level question that the artifact defers. The current charter (PROJECT_CHARTER.md §3) says "two primary operational surfaces—waiter web UI + cook Telegram bot"; it does not constrain the backend decomposition.

## Why this matters

The 2026-08-24 brainstorm pass surfaces `RafaelEmery/rafood-api` as the only in-window FastAPI + SQLModel + Alembic + Postgres + K8s peer that documents a 5-context DDD separation. The pattern informs LE31 v2 multi-context decomposition if/when it becomes necessary: **a clean per-context folder/module separation with one bounded context per business area (Restaurants + Schedules, Products, Offers + Schedules, Categories, Users)**. Today the LE31 backend is a single FastAPI app; the artifact records that the 5-context separation is technically viable for future v2 iteration, without changing the v1 roadmap.

**Cross-section with existing LE31 features**:
- Charter §3 (single-tenant posture) → this artifact is informational only; no charter change.
- Features 23-29 (v1 surface) → this artifact does not affect v1 build behavior.
- Feature 90 (pronto-watch cross-section) → different surface (Telegram + WhatsApp reminders; LE31 is Telegram-only).
- Features 102-104 (2026-08-23 brainstorm picks) → all v2 watch-list artifacts; this is the architectural-decomposition-layer sibling.

**Why defer, not build**: zero observed pain at the LE31-owner level; LE31 v1 single-tenant posture is correct; the multi-context decomposition is a future-tense concern. The artifact is a research-note that records the pattern for future v2-AI iteration.
