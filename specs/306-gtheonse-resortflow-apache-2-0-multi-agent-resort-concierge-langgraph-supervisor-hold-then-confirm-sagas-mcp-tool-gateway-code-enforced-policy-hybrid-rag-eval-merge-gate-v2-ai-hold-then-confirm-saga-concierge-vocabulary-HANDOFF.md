# HANDOFF — Feature 306: `gtheonse-resortflow-apache-2-0-multi-agent-resort-concierge-langgraph-supervisor-hold-then-confirm-sagas-mcp-tool-gateway-code-enforced-policy-hybrid-rag-eval-merge-gate-v2-ai-hold-then-confirm-saga-concierge-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/306-gtheonse-resortflow-apache-2-0-multi-agent-resort-concierge-langgraph-supervisor-hold-then-confirm-sagas-mcp-tool-gateway-code-enforced-policy-hybrid-rag-eval-merge-gate-v2-ai-hold-then-confirm-saga-concierge-vocabulary.md` — defer/parking-lot (Pick B of Daily Brainstorm 2026-10-11).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *multi-agent-concierge-with-hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback + MCP-as-cross-system-tooling primitive*, the owner wants *evidence that this hold-then-confirm-saga-concierge-vocabulary exists in 2026 with the same hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback posture*, but struggles because *LE31 has no documented v2-AI hold-then-confirm-saga-concierge-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same multi-agent-resort-concierge-platform + hold-then-confirm-sagas + code-enforced-policy + eval-merge-gate + runs-locally-against-simulated-vendors posture"*. |
| 2 | | ✓ | The owner/staff can understand the operator-facing vocabulary (multi-agent-resort-concierge + hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback + MCP-as-cross-system-tooling) without specialist help. The 0★/0⑨ with IN-WINDOW BY BOTH FIELDS (2-day-old repo with same-day-pushed) makes vocabulary viable, but code adoption is not viable (v2-AI roadmap not yet active + no v2-AI multi-agent-concierge surface in v2-AI charter). |
| 3 | | ✓ | Fits the fixed stack: Apache-2.0 + 0★/0⑨ + 1643 KB modest + 18-topic array + Python ✓ ON-STACK + IN-WINDOW BY BOTH FIELDS (2-day-old repo with same-day-pushed). The *multi-agent-resort-concierge + hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback + MCP-as-cross-system-tooling* vocabulary IS stack-adjacent for any future v2-AI multi-agent-concierge surface. Required data + permissions + infrastructure: Python 3.13 + FastAPI + langgraph + langfuse + fastmcp + MCP + qdrant + opentelemetry + ragas + docker-compose. The azure-openai + langgraph + qdrant stack is OFF-§3.1 for LE31 v1 today but is portable to LE31 v2-AI's Python stack. No AI capability required at v1; the v2-AI roadmap would add azure-openai + qdrant as v2-AI stack extensions. Rabbit hole: the *azure-openai + langgraph + qdrant + opentelemetry + ragas* stack is off-LE31-v1-stack (LE31 v1 uses Python + FastAPI + Postgres, not langgraph + qdrant + opentelemetry + ragas). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | | ✓ | Does not violate any invariant. The *multi-agent-resort-concierge + hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback + MCP-as-cross-system-tooling* primitives are §3.1 + §3.4-aligned (explicit-state-transition + deterministic-rule + non-AI-fallback + observable-evidence + MCP-as-cross-system-tooling). The *hold-then-confirm-saga* posture IS the §3.1 *explicit-state-transition* charter invariant applied to the *concierge-action* dimension. The *code-enforced-policy* posture IS the §3.4 *deterministic-rule* charter invariant. The *eval-merge-gate* posture IS the §3.4 *observable-evidence* charter invariant. The *non-AI-fallback + runs-locally-against-simulated-vendors* posture IS the §3.4 *non-AI-fallback* charter invariant. The *MCP-tool-gateway + fastmcp* posture IS the §3.4 *MCP-as-cross-system-tooling* charter invariant. The *multi-agent + langgraph-supervisor* posture IS the *durable-control-plane* charter §3.1 invariant. No §3.4 customer-facing AI (the concierge surface is operator-tooling + non-AI-fallback). No data rule violation. |
| 5 | | ✓ | Maps to v2-AI polish outcome (multi-agent-concierge surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry`) already implement the *append-only + idempotent* discipline; the reference is *naming*, not new build. |
| 7 | | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (v2-AI roadmap not yet active + no v2-AI multi-agent-concierge surface in v2-AI charter + 0★/0⑨ + 2-day-old repo).

## Bucket

**v2-AI** (hold-then-confirm-saga-concierge-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 18-tuple-primitive set (multi-agent-resort-concierge + langgraph-supervisor + hold-then-confirm-sagas + MCP-tool-gateway + code-enforced-policy + hybrid-RAG + eval-merge-gate + runs-locally-against-simulated-vendors + azure-openai + langfuse + fastmcp + opentelemetry + ragas + qdrant + docker-compose + hospitality + multi-agent + python) + the tech-stack (Python + FastAPI + langgraph + langfuse + fastmcp + MCP + azure-openai + qdrant + opentelemetry + ragas + docker-compose).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback + MCP-as-cross-system-tooling* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `ConciergeSaga`, `ConciergeSagaStep`, `ConciergeVendor`, `ConciergePolicy`, `ConciergeEval` tables.
- `backend/concierge_saga.py` — new file with `ConciergeSagaBuilder` class.
- `backend/code_enforced_policy.py` — new file with `CodeEnforcedPolicyEngine` class.
- `backend/eval_merge_gate.py` — new file with `EvalMergeGate` class.
- `backend/main.py` — add `/api/concierge-saga` FastAPI endpoint.
- `frontend/templates/concierge-saga.html` — new minimal-HTML/HTMX template.
- `backend/mcp_server_concierge_saga.py` — new file with `McpServerForConciergeSaga` FastMCP sub-app.
- `tests/test_concierge_saga.py` — new unit test for `ConciergeSagaBuilder`.
- `tests/integration/test_mcp_concierge_saga.py` — new integration test for `McpServerForConciergeSaga`.

## Verification protocol reference

When the first v2-AI PR that adopts the *hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback + MCP-as-cross-system-tooling* discipline lands, the verification protocol is:

1. Run `pytest tests/test_concierge_saga.py` and verify the `ConciergeSagaBuilder` creates a hold-then-confirm-saga correctly.
2. Run `pytest tests/integration/test_mcp_concierge_saga.py` and verify the MCP-server exposes the saga correctly.
3. Run `uvicorn backend.main:app` and curl `/api/concierge-saga` to verify the endpoint returns the saga as JSON.
4. Open `frontend/templates/concierge-saga.html` in a browser and verify the saga renders as a navigable tree.
5. Inspect the `ConciergeSaga` + `ConciergeSagaStep` + `ConciergePolicy` + `ConciergeEval` tables in Postgres and verify the hold-then-confirm-saga discipline is enforced.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback + MCP-as-cross-system-tooling* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the five tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

First v2-AI PR that adds a `ConciergeSaga` SQLModel table + a `ConciergeSagaStep` append-only event table + a `hold_then_confirm_saga` FastAPI endpoint set + a `/api/concierge-saga` FastAPI endpoint + a `concierge-saga.html` minimal-HTML/HTMX template with hold-then-confirm-saga + code-enforced-policy + eval-merge-gate + non-AI-fallback metrics; OR first v2-AI PR that adopts the *multi-agent-resort-concierge-platform + hold-then-confirm-sagas + code-enforced-policy + eval-merge-gate* discipline on the existing audit_logs SQLModel table.

## Adjacent evidence

- [../features/232-lpalbou-AbstractGateway-...-v2-ai-durable-control-plane.md](../features/232-lpalbou-AbstractGateway-...-v2-ai-durable-control-plane.md) — sister-shape for durable-control-plane.
- [../features/263-multiples-hq-business-state-machine-mcp-...-v2-ai-postgres-business-state-machine-ledger-vocabulary.md](../features/263-multiples-hq-business-state-machine-mcp-...-v2-ai-postgres-business-state-machine-ledger-vocabulary.md) — sister-shape for postgres-business-state-machine-ledger.
- [../features/287-noise01-endoxa-...-v2-ai-governed-beliefs-vocabulary.md](../features/287-noise01-endoxa-...-v2-ai-governed-beliefs-vocabulary.md) — sister-shape for governed-beliefs.
- [../features/289-shivamk01here-LedgerLoop-...-v2-ai-ledger-discipline-runtime-vocabulary.md](../features/289-shivamk01here-LedgerLoop-...-v2-ai-ledger-discipline-runtime-vocabulary.md) — sister-shape for ledger-discipline-runtime.
- [../features/299-A220man-human-approval-console-...-v2-ai-approval-receipt-vocabulary.md](../features/299-A220man-human-approval-console-...-v2-ai-approval-receipt-vocabulary.md) — sister-shape for approval-receipt.
- [../features/300-farooqarahim-glassbox-...-v2-ai-eu-ai-act-ledger-vocabulary.md](../features/300-farooqarahim-glassbox-...-v2-ai-eu-ai-act-ledger-vocabulary.md) — sister-shape for eu-ai-act-ledger.
- [../features/301-New1Direction-korg-...-v2-ai-verifiable-cognition-vocabulary.md](../features/301-New1Direction-korg-...-v2-ai-verifiable-cognition-vocabulary.md) — sister-shape for verifiable-cognition.
- [../features/302-warrant-ai-warrant-...-v2-ai-decision-ledger-vocabulary.md](../features/302-warrant-ai-warrant-...-v2-ai-decision-ledger-vocabulary.md) — sister-shape for decision-ledger.

## Notes

- The Python ✓ ON-STACK + IN-WINDOW BY BOTH FIELDS (2-day-old repo with same-day-pushed) makes this a strong vocabulary candidate for any future v2-AI multi-agent-concierge surface.
- The Apache-2.0 permissive license + 0★/0⑨ makes code adoption not viable today but the vocabulary IS portable to LE31 v2-AI's Python stack.
- The hold-then-confirm-saga discipline is the canonical v2-AI explicit-state-transition + saga-pattern + human-gate vocabulary applied to the concierge-action dimension.
- The code-enforced-policy + eval-merge-gate + non-AI-fallback posture is consistent with the v2-AI deterministic-rule + observable-evidence + non-AI-fallback posture (features 232 + 263 + 287-289 + 299-302 + Pick C).