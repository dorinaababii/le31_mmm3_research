# HANDOFF — Feature 302: `warrant-ai-warrant-apache-2-0-decision-ledger-ai-agents-mandate-evidence-cost-outcome-replay-before-ship-ed25519-merkle-tree-rfc-8785-langgraph-mcp-python-temporal-v2-ai-decision-ledger-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/302-warrant-ai-warrant-apache-2-0-decision-ledger-ai-agents-mandate-evidence-cost-outcome-replay-before-ship-ed25519-merkle-tree-rfc-8785-langgraph-mcp-python-temporal-v2-ai-decision-ledger-vocabulary.md` — defer/parking-lot (Pick A of Daily Research 2026-10-11).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *decision-ledger for AI agents with mandate + evidence + cost + outcome + replay-before-ship + ed25519 + merkle-tree + RFC-8785 + langgraph + MCP + Python + observability + policy + temporal* primitive, the owner wants *evidence that this decision-ledger-vocabulary exists in 2026 with a cryptographic-verifiability surface + replay-before-ship semantics + AI-agent framework stack*, but struggles because *LE31 has no documented v2-AI decision-ledger-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31 + the mandate+evidence+cost+outcome attribution quadruple + the replay-before-ship primitive"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (decision ledger + mandate + evidence + cost + outcome + replay-before-ship) without specialist help. The 0★/1⑂ with single-maintainer cadence makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **Python on-stack** (LE31 stack match). The **MCP + ed25519 + merkle-tree + RFC-8785 + Temporal** stack is the v2-AI stack-shape, not the v1 stack-shape. Required data + permissions + infrastructure: Python FastAPI runtime + cryptographic-verifiability surface + replay-before-ship validation primitive. No AI capability required today (the decision-ledger primitive is deterministic). Rabbit hole: langgraph + MCP + Temporal are NEW transitive dependencies for v2-AI. Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *decision-ledger + mandate + evidence + cost + outcome + replay-before-ship + ed25519 + merkle-tree + RFC-8785* primitives are §3.1-aligned (explicit state transitions, append-only discipline). No §3.4 customer-facing AI (the AI agent is operator-tooling). No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI outcome (decision-ledger for AI agents with replay-before-ship semantics). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry`) already implement the append-only discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 0★ + langgraph + MCP + Temporal NEW transitive dependencies for v2-AI).

## Bucket

**v2-AI** (decision-ledger-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the 5-primitive set (`decision ledger + mandate + evidence + cost + outcome + replay-before-ship`) + the cryptographic stack (`ed25519 + merkle-tree + RFC-8785`) + the AI-agent framework stack (`langgraph + MCP + Temporal`).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that adds a v2-AI surface that requires decision-ledger with mandate+evidence+cost+outcome+replay-before-ship semantics):

1. `backend/app/audit/models.py` — add new `DecisionLedgerEntry` SQLModel table with columns: `id` (UUID), `agent_id` (str), `mandate` (str), `evidence` (JSON), `cost` (JSON), `outcome` (JSON), `decided_at` (timezone-aware datetime), `previous_entry_hash` (str), `this_entry_hash` (str), `ed25519_signature` (str).
2. `backend/app/audit/models.py` — add new `policy_engine` SQLModel table with columns: `id` (UUID), `agent_id` (str FK), `action` (str), `allowed` (bool), `enforced_at` (timezone-aware datetime).
3. `backend/app/audit/models.py` — add new `langgraph_agent` SQLModel table with columns: `id` (UUID), `name` (str), `description` (str), `graph_definition` (JSON), `created_at`, `updated_at`.
4. `backend/alembic/versions/` — add Alembic migration for the new tables.
5. `backend/app/audit/repository.py` — add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `DecisionLedgerEntry` insert path.
6. `backend/app/audit/merkle_tree.py` — NEW: merkle-root computation utility.
7. `backend/app/audit/rfc8785_canonical.py` — NEW: RFC-8785 JSON canonicalization utility.
8. `backend/app/audit/ed25519_sign.py` — NEW: ed25519 sign/verify utility.
9. `backend/app/api/v2/decision_ledger.py` — NEW: `GET /v2/decision-ledger/search?agent=<>&mandate=<>&as_of=<>` search endpoint.
10. `backend/app/api/v2/decision_ledger.py` — NEW: `GET /v2/decision-ledger/replay?from=<>&to=<>` replay endpoint.
11. `backend/app/api/v2/decision_ledger.py` — NEW: `GET /v2/decision-ledger/verify` hash-chain-verify endpoint.
12. `backend/app/api/v2/decision_ledger.py` — NEW: `GET /v2/decision-ledger/export?format=json` audit-evidence-export endpoint.
13. `backend/app/api/v2/agents.py` — NEW: `POST /v2/agents/<agent_id>/decisions/propose` endpoint.
14. `backend/app/api/v2/agents.py` — NEW: `POST /v2/agents/<agent_id>/decisions/<decision_id>/execute` endpoint.

## Verification protocol

1. `git clone https://github.com/warrant-ai/warrant` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/warrant-ai/warrant/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set).
3. `curl -sS -H "Authorization: Bearer ***" "https://api.github.com/repos/warrant-ai/warrant"` for star count, fork count, license, language, pushed_at, created_at, topics, description (parent-verified 2026-10-11).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the decision-ledger + replay-before-ship + ed25519 + merkle-tree + RFC-8785 changes are isolated to the expected files.
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec` before any implementation.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2-AI trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the new tables + remove the new API endpoints.
- No data loss if the rollback happens BEFORE any decision-ledger row is written.
- Full data retention if the rollback happens AFTER rows are written (the new tables are dropped but the original `audit_logs` rows are preserved per the *append-only* invariant).

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (append-only StockEntry, etc.).
4. `le31-handoff-spec` — the handoff-spec requirements (frozen contract discipline, mandatory skill list, verification protocol).
5. `le31-feature-pipeline` — the feature-pipeline workflow (parent research issue, sub-issue creation, handoff file).

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-11 / Pick A — v2-AI decision-ledger-vocabulary (warrant-ai/warrant)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-11.linear-fallback.json`. Sub-issue project = `le31 Research` (P-HMM-1) per `le31-feature-pipeline/SKILL.md` line 33 since `le31 v2-AI` does not exist.

## Parent research issue

[linear: blocked — workspace plan-limit error 21st consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-11.linear-fallback.json`]