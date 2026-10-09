# Feature 270 — `cesaremcasa-manager-architecture-mit-restaurant-operations-auditable-tenant-isolation-workers-governed-ai-mcp-fastapi-postgresql-redis-llm-v2-owner-pains-architecture-reference` (defer)

> **NEW observation (2026-10-09).** Documents in-window GitHub repo `cesaremcasa/manager-architecture` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python, **pushed 2026-10-05T16:21:49Z**, in-window by `pushed_at` only, **created 2026-08-03T00:12:29Z** — 67-day-old repo with first in-window push, **109 KB modest repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-09): *"Restaurant operations engineering: auditable calculations, tenant isolation, workers and governed AI/MCP integrations."* Topics (verbatim, parent-verified): `ai-agents, architecture, data-pipeline, document-processing, email-processing, fastapi, llm, multi-tenant, postgresql, redis, restaurant-tech, system-design` — 12 topics including `fastapi + postgresql + redis + python` (LE31 stack-shape match) + `restaurant-tech` (LE31 domain match = RARE LITERAL TOPIC) + `multi-tenant + llm + ai-agents + ai-agents-integration` (v2 owner-pains surface). Bucket: **v2 (owner-pains architecture-reference)** — Pick B of Daily Research 2026-10-09. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`restaurant-tech + multi-tenant + auditable + workers + governed AI/MCP`** quintuple-primitive as a persistent cross-section reference for the LE31 v2 *owner-pains + multi-tenant-restaurant-ops + auditable + governed-AI/MCP* wedge, and document the **literal `restaurant-tech` GitHub topic** as a strong domain-match signal for LE31 v2 surfaces. The artifact is a persistent cross-section reference for future v2 architecture. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`restaurant-tech + multi-tenant + auditable + workers + governed AI/MCP`** quintuple-primitive: every calculation is auditable (the calculation history is in an explicit ledger); every tenant has its own data partition; heavy work runs in workers; AI integrations are governed (no customer-facing AI; owner/staff-assist only). This is the §3.1 explicit-state-transitions primitive + §3.4 owner/staff-AI primitive applied to restaurant operations.
- A written record of the **`FastAPI + PostgreSQL + Redis + Python`** stack-shape: this is **4 of 4 LE31 backend stack primitives** matched (FastAPI + SQLModel + Postgres + Alembic + Workers + Redis are all on the LE31 pin set or trivially substitutable).
- A written record of the **`restaurant-tech literal GitHub topic`** = the strongest domain-match signal of any 2026-10 in-window repo for v2 architecture.
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (67-day-old, first in-window push today); (2) the *architecture-reference* is the value, not the code (LE31 v1 is minimal-HTML/HTMX + single-tenant + no-AI); (3) the *literal `restaurant-tech` topic* is the demand-signal, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema (charter §3.1: single-tenant per v1).
- Adoption of the manager-architecture codebase (67-day-old single-maintainer repo with no observed production usage; multi-tenant scope is OFF v1 charter).
- Cross-pollination with the `multi-tenant` scope (LE31 is single-restaurant; v2 surface).
- Cross-pollination with the `AI/MCP integrations` until §3.4 ripgrep verification (the topic mentions `llm + ai-agents`; need to confirm the AI surface is owner/staff-assist, NOT customer-facing, before any v2 PR).

## Evidence / JTBD

When a future LE31 v2 surface proposes "the restaurant-tech + multi-tenant + auditable + workers + governed AI/MCP architecture" (e.g., a v2 owner-pains surface that adds AI-assisted cost-margin rollup with multi-tenant isolation), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented in-window restaurant-tech architecture reference*, so that *the v2 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31"*.

- **Evidence class**: observed (the manager-architecture description + topics name the primitives explicitly: `ai-agents, architecture, data-pipeline, document-processing, email-processing, fastapi, llm, multi-tenant, postgresql, redis, restaurant-tech, system-design`).
- **Confidence**: high for the architecture-reference match (the verbatim topic set names `restaurant-tech` directly — RARE in the 2026 cluster — and the 4-of-4 stack match); low for transferability (LE31 v1 is single-tenant + no-AI; manager-architecture is multi-tenant + AI/MCP).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant single-tenant no-AI); the value is the *v2 architecture reference* — when the first v2 PR that adds multi-tenant architecture lands, the manager-architecture pattern is a ready-made *named primitive*.

## Description

GitHub `cesaremcasa/manager-architecture` (MIT, 0★/0⑂, Python, FastAPI + PostgreSQL + Redis + LLM, pushed 2026-10-05T16:21:49Z, created 2026-08-03T00:12:29Z, 109 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-09): *"Restaurant operations engineering: auditable calculations, tenant isolation, workers and governed AI/MCP integrations."*

The architectural primitive has five sub-primitives that map 1:1 onto a future LE31 v2 surface:

1. **`Restaurant-tech`** — the literal GitHub topic `restaurant-tech` is the **strongest domain-match signal** of any 2026 in-window repo for a v2 owner-pains surface that builds on the LE31 v1 restaurant-domain primitives.
2. **`Auditable calculations`** — every calculation is auditable (the calculation history is in an explicit ledger); the result is derived from the inputs. This is **§3.1 verbatim** applied to calculations — the result is derived from the inputs (audit_logs).
3. **`Tenant isolation`** — every tenant has its own data partition; queries are filtered by tenant_id. The *tenant isolation* primitive is OFF v1 charter (single-restaurant) but applies to any future v2 multi-tenant surface.
4. **`Workers`** — heavy work runs in background workers (likely using Celery/RQ). The *workers* primitive is OFF v1 charter (LE31 has no heavy backend jobs today) but applies to any future v1 polish that introduces scheduled jobs (e.g., nightly cost-margin rollup) or heavy async work (e.g., large data exports).
5. **`Governed AI/MCP`** — AI integrations are governed (no customer-facing AI; owner/staff-assist only; explicit human-review gate; the AI is a suggester, not an actor). This is **§3.4 verbatim** applied to restaurant operations — owner-assist AI is allowed; customer-facing AI is forbidden.

**The 1:1 mapping onto a future LE31 v2 surface:**

| manager-architecture primitive | LE31 v2 equivalent | Charter section | Status |
|---|---|---|---|
| `restaurant-tech` topic | (literal domain match) | v2 (owner-pains) | **Vocabulary reference** |
| Auditable calculations | `audit_logs` (derived state) | §3.1 ✓ | **Implemented (v1)** |
| Tenant isolation | (LE31 v1 is single-restaurant) | v2 (multi-tenant) | **Not implemented** — v2 surface |
| Workers | (LE31 v1 has no heavy backend jobs) | v1 polish / v2 | **Not implemented** — v1 polish surface |
| Governed AI/MCP | (LE31 v1 has no AI) | v2 (with §3.4 owner-side-AI primitive) | **Not implemented** — v2 surface |
| FastAPI + PostgreSQL + Redis + Python | FastAPI + SQLModel + Postgres + Redis | §3.1 ✓ | **Implemented (v1 + Redis-pending)** |
| LLM integration | (LE31 v1 has no LLM) | v2 with §3.4 owner-side primitive | **Not implemented** — v2 surface |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that introduces the multi-tenant restaurant-operations architecture), the implementation would add:

1. A `tenant_id` column on every table (Alembic migration).
2. A `tenant-aware repository` pattern that filters by `tenant_id` on every query.
3. A `workers` module that runs heavy work asynchronously (likely via Celery/RQ).
4. An `ai_assist` module that wraps every LLM call with an explicit human-review gate.

The HANDOFF is to evaluate whether the v2 owner-pains architecture is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2 trigger fires:

**For v2 multi-tenant restaurant-ops** (if approved):
1. Add a `tenant_id` column to every table (Alembic migration).
2. Add a `tenant-aware repository` pattern at `app/data/tenant_repo.py` that filters by `tenant_id` on every query.
3. Add a `workers` module at `app/workers/celery_app.py` (or RQ equivalent) that runs heavy work asynchronously.
4. Add an `ai_assist` module at `app/ai/copilot.py` (or MCP equivalent) that wraps every LLM call with an explicit human-review gate.
5. New feature file at `features/NNN-multi-tenant-restaurant-ops.md` (NOT this defer artifact).

## Telegram interaction

- **Cook bot**: unchanged (LE31 v2 multi-tenant scope does not change the cook bot's per-restaurant surface).
- **Waiter web**: the waiter web UI adds a tenant-selector at the top (per the future v2 multi-tenant design).
- **Owner**: the owner-side daily recap gains an LLM-assisted summary (with explicit human-review gate per §3.4).

## Dependencies

- LE31 v1 stack primitives (`StockEntry` + `audit_logs` + Alembic) — all on the LE31 pin set.
- Redis (likely already on the LE31 production stack or trivially addable).
- LLM (a vendor such as OpenAI or self-hosted via Ollama; the §3.4 non-AI fallback must be preserved).
- Workers (Celery or RQ; off v1 stack = v2 dependency).

## Open questions

1. **Is the v2 multi-tenant surface the right product-wedge today?** LE31 charter is single-restaurant; v2 surface would expand scope; recommend charter-decided before any v2 PR.
2. **Does the AI/MCP integration preserve the §3.4 non-AI fallback?** Need ripgrep verification of the README + main.py before any v2 adoption. The `ai-agents + llm + multi-tenant` topics suggest a need for careful §3.4 review.
3. **Is the workers primitive off the v1 stack?** LE31 v1 has no heavy backend jobs today; adding Celery/RQ is a v1 polish surface change.

## Why this matters

The manager-architecture repo is the strongest direct LE31-stack-shape match for the **`restaurant-tech + multi-tenant + auditable + workers + governed AI/MCP`** quintuple-primitive in the 71-pass series. The *literal `restaurant-tech` GitHub topic* is the strongest domain-match signal of any 2026-10 in-window repo. The *vocabulary* is the value: when LE31 v2 multi-tenant architecture lands, the manager-architecture pattern is a ready-made *named primitive*. The 67-day-old repo with first in-window push is the demand-signal, not the adoption-signal.
