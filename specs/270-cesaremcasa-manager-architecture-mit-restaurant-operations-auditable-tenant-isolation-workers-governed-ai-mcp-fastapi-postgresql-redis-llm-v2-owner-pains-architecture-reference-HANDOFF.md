# HANDOFF — Feature 270: `cesaremcasa-manager-architecture-...-v2-owner-pains-architecture-reference`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/270-cesaremcasa-manager-architecture-mit-restaurant-operations-auditable-tenant-isolation-workers-governed-ai-mcp-fastapi-postgresql-redis-llm-v2-owner-pains-architecture-reference.md` — defer/parking-lot (Pick B of Daily Research 2026-10-09).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2 surface proposes a `restaurant-tech + multi-tenant + auditable + workers + governed AI/MCP` architecture, the owner wants *evidence that this stack-shape exists in 2026 for restaurant operations*, but struggles because *most in-domain references are single-tenant + non-auditable + non-AI/MCP*, so that *the v2 surface has a credible peer reference*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (auditable + tenant isolation + workers). The 67-day-old single-maintainer repo makes code adoption not viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: FastAPI + PostgreSQL + Redis + Python. Workers + LLM = pattern vocabulary. The `ai-agents + llm + multi-tenant` topics suggest a §3.4-aware AI integration (need ripgrep verification before any future v2 build). Evidence strength: high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant as a vocabulary reference. The `multi-tenant` scope is OFF v1 charter (v2 surface). The `governed AI/MCP` integration is §3.4-compatible IF the AI is owner/staff-assist (need ripgrep verification). No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2 outcome (owner-pains cluster). Maximum time worth spending: 1 hour documentation. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | ~30 min documentation; zero code cost. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 67-day-old repo + multi-tenant + AI/MCP scope is OFF v1 charter + requires §3.4 ripgrep verification).

## Bucket

**v2** (owner-pains architecture-reference) — the *architecture reference* is the value, not the code. The literal `restaurant-tech` GitHub topic is the strongest domain-match signal of any 2026-10 in-window repo.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that introduces the multi-tenant restaurant-operations architecture):

1. `backend/app/data/models.py` — add `tenant_id: UUID` column on every table (Alembic migration).
2. `backend/alembic/versions/` — add a new Alembic migration: `ALTER TABLE stock_entry ADD COLUMN tenant_id UUID NOT NULL REFERENCES tenant(id);` (and similar for every table).
3. `backend/app/data/tenant_repo.py` — NEW: tenant-aware repository pattern that filters by `tenant_id` on every query.
4. `backend/app/workers/celery_app.py` — NEW: Celery (or RQ) workers module that runs heavy work asynchronously.
5. `backend/app/ai/copilot.py` — NEW: AI-assisted copilot that wraps every LLM call with an explicit human-review gate per §3.4.
6. `backend/app/ai/mcp.py` — NEW: MCP (Model Context Protocol) integration if MCP is the chosen AI interface.
7. New feature file at `features/NNN-multi-tenant-restaurant-ops.md` (NOT this defer artifact).

## Verification protocol

1. `git clone https://github.com/cesaremcasa/manager-architecture` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/cesaremcasa/manager-architecture/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/cesaremcasa/manager-architecture"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-10-09).
4. Pre-implementation §3.4 ripgrep REQUIRED: `grep -rE "openai|llm|ai-agent|gpt|claude|copilot" backend/app/` (after the v2 surface is approved) to confirm the AI integration is owner/staff-assist (allowed) and NOT customer-facing (forbidden per §3.4).
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern` (for the v1 polish surface), `le31-handoff-spec`.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2 trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the `tenant_id` column from every table + delete `tenant_repo.py` + `celery_app.py` + `copilot.py` + `mcp.py`.
- The §3.4 non-AI fallback is preserved by the absence of `copilot.py` + `mcp.py`.

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — for the v1 polish prerequisites (charter §3.1 + append-only stock).
4. `le31-handoff-spec` — the handoff-spec requirements.

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-09 / Pick B — v2 owner-pains architecture-reference (cesaremcasa/manager-architecture)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-09.linear-fallback.json`.
