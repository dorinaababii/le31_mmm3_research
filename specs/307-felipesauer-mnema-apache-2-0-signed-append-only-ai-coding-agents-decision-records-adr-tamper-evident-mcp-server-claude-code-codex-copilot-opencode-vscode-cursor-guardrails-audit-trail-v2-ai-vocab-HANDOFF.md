# HANDOFF — Feature 307: `felipesauer-mnema-apache-2-0-signed-append-only-ai-coding-agents-decision-records-adr-tamper-evident-mcp-server-claude-code-codex-copilot-opencode-vscode-cursor-guardrails-audit-trail-v2-ai-vocab`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/307-felipesauer-mnema-apache-2-0-signed-append-only-ai-coding-agents-decision-records-adr-tamper-evident-mcp-server-claude-code-codex-copilot-opencode-vscode-cursor-guardrails-audit-trail-v2-ai-vocab.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-11).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint primitive*, the owner wants *evidence that this signed-append-only-AI-coding-agents-decision-records-vocabulary exists in 2026 with the same signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails posture*, but struggles because *LE31 has no documented v2-AI signed-append-only-AI-coding-agents-decision-records-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint posture"*. |
| 2 | | ✓ | The owner/staff can understand the operator-facing vocabulary (signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint) without specialist help. The 4★/0⑨ + 22954 KB substantial + pushed 2026-10-11T05:45:12Z = TODAY makes vocabulary viable, but code adoption is not viable (TypeScript off-§3.1 stack for LE31 v1 today + v2-AI roadmap not yet active + no v2-AI AI-coding-agent-decision surface in v2-AI charter). |
| 3 | | ✓ | Fits the fixed stack: Apache-2.0 + 4★/0⑨ + 22954 KB substantial + 20-topic array + TypeScript off-§3.1 stack but the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* vocabulary IS stack-agnostic and IS portable to Python. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + Ed25519 + Git. No AI capability required at v1; the v2-AI roadmap would add claude-code/codex/copilot/opencode/vscode/cursor as v2-AI AI-coding-agent extensions. Rabbit hole: the *TypeScript + Node.js + MCP-server + claude-code/codex/copilot/opencode/vscode/cursor* stack is off-LE31-v1-stack (LE31 v1 uses Python + FastAPI + Postgres, not TypeScript + Node.js + MCP-server + claude-code/codex/copilot/opencode/vscode/cursor). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | | ✓ | Does not violate any invariant. The *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* primitives are §3.1 + §3.3 + §3.4-aligned (explicit-state-transitions + append-only-ledger-as-immutable-audit-trail + cryptographic-signature-as-audit-evidence + MCP-as-cross-system-tooling + deterministic-rule + non-AI-fallback). The *signed-append-only-decision-record + ADR* posture IS the §3.1 *explicit-state-transitions* charter invariant applied to the *AI-decision* dimension. The *tamper-evident + audit-trail* posture IS the §3.3 *append-only-ledger-as-immutable-audit-trail + cryptographic-signature-as-audit-evidence* charter invariant applied to the *AI-decision* dimension. The *MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* posture IS the §3.4 *MCP-as-cross-system-tooling + deterministic-rule + non-AI-fallback* charter invariant applied to the *AI-coding-agent-decision* dimension. No §3.4 customer-facing AI (the AI-coding-agent-decision surface is operator-tooling). No data rule violation. |
| 5 | | ✓ | Maps to v2-AI polish outcome (signed-append-only-AI-coding-agents-decision-records surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry`) already implement the *append-only + idempotent* discipline; the reference is *naming*, not new build. |
| 7 | | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (TypeScript + Node.js off-LE31-stack + v2-AI roadmap not yet active + no v2-AI AI-coding-agent-decision surface in v2-AI charter).

## Bucket

**v2-AI** (signed-append-only-AI-coding-agents-decision-records-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 20-tuple-primitive set (signed-append-only-decision-records + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint + agent-memory + ai-governance + coding-agents + ai-agents) + the tech-stack (TypeScript + Node.js + MCP-server + claude-code/codex/copilot/opencode/vscode/cursor).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `MnemaDecisionRecord`, `MnemaRule`, `MnemaGuardrailHit`, `MnemaMcpServer` tables.
- `backend/mnema_decision_record.py` — new file with `MnemaDecisionRecordBuilder` class.
- `backend/mnema_rule_engine.py` — new file with `MnemaRuleEngine` class.
- `backend/mnema_guardrail.py` — new file with `MnemaGuardrail` class.
- `backend/mnema_hash_chain.py` — new file with `MnemaHashChain` class.
- `backend/main.py` — add `/api/mnema-decision-records` FastAPI endpoint.
- `frontend/templates/mnema-decision-records.html` — new minimal-HTML/HTMX template.
- `backend/mcp_server_mnema_decision_records.py` — new file with `McpServerForMnemaDecisionRecords` FastMCP sub-app.
- `tests/test_mnema_decision_record.py` — new unit test for `MnemaDecisionRecordBuilder`.
- `tests/integration/test_mcp_mnema_decision_records.py` — new integration test for `McpServerForMnemaDecisionRecords`.

## Verification protocol reference

When the first v2-AI PR that adopts the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline lands, the verification protocol is:

1. Run `pytest tests/test_mnema_decision_record.py` and verify the `MnemaDecisionRecordBuilder` creates a signed-append-only-decision-record correctly.
2. Run `pytest tests/integration/test_mcp_mnema_decision_records.py` and verify the MCP-server exposes the ledger correctly.
3. Run `uvicorn backend.main:app` and curl `/api/mnema-decision-records` to verify the endpoint returns the ledger as JSON.
4. Open `frontend/templates/mnema-decision-records.html` in a browser and verify the ledger renders as a navigable tree.
5. Inspect the `MnemaDecisionRecord` + `MnemaRule` + `MnemaGuardrailHit` + `MnemaMcpServer` tables in Postgres and verify the signed-append-only-decision-record discipline is enforced.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *signed-append-only-decision-record + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the four tables.
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

First v2-AI PR that adds a `MnemaDecisionRecord` SQLModel table + a `MnemaDecision` append-only event table + a `signed_append_only_decision_records` FastAPI endpoint set + a `/api/mnema-decision-records` FastAPI endpoint + a `mnema-decision-records.html` minimal-HTML/HTMX template with signed-append-only-decision-records + ADR + tamper-evident + audit-trail + MCP-server-as-cross-system-tooling + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint metrics; OR first v2-AI PR that adopts the *signed-append-only-decision-records-for-AI-coding-agents + ADR + tamper-evident + audit-trail + MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint* discipline on the existing audit_logs SQLModel table.

## Adjacent evidence

- [../features/197-rajo69-ledgerkb-...-v2-owner-pains.md](../features/197-rajo69-ledgerkb-...-v2-owner-pains.md) — sister-shape for evidence-bearing-assertions + append-only-ledger.
- [../features/245-EvezArt-evez-event-spine-...-append-only-hash-linked-event-log-...-v2-owner-pains.md](../features/245-EvezArt-evez-event-spine-...-append-only-hash-linked-event-log-...-v2-owner-pains.md) — sister-shape for append-only-hash-linked-event-log.
- [../features/271-znbsf-agent-case-graph-...-v2-owner-pains-audit-architecture-reference.md](../features/271-znbsf-agent-case-graph-...-v2-owner-pains-audit-architecture-reference.md) — sister-shape for evidence-first-append-only-case-ledger.
- [../features/284-S0tman-irp-capture-...-v2-owner-pains-decision-rationale-ledger-vocabulary.md](../features/284-S0tman-irp-capture-...-v2-owner-pains-decision-rationale-ledger-vocabulary.md) — sister-shape for append-only-ledger-that-records-why-decisions-were-made.
- [../features/286-gadyamedia-vocenya-mcp-...-v2-ai-mcp-server-ai-receptionist-vocabulary.md](../features/286-gadyamedia-vocenya-mcp-...-v2-ai-mcp-server-ai-receptionist-vocabulary.md) — sister-shape for mcp-servers-ai-receptionist-small-business.
- [../features/300-farooqarahim-glassbox-...-v2-ai-eu-ai-act-ledger-vocabulary.md](../features/300-farooqarahim-glassbox-...-v2-ai-eu-ai-act-ledger-vocabulary.md) — sister-shape for tamper-evident-audit-ledger-ai-systems.

## Notes

- The 22954 KB substantial + pushed 2026-10-11T05:45:12Z = TODAY makes this a strong vocabulary candidate for any future v2-AI signed-append-only-AI-coding-agents-decision-records surface.
- The TypeScript + Node.js stack is off-§3.1 for LE31 v1 today but the vocabulary IS stack-agnostic and portable to Python + Ed25519 + Git.
- The signed-append-only-decision-record + ADR + tamper-evident + audit-trail discipline is the canonical v2-AI append-only-ledger-as-immutable-audit-trail + cryptographic-signature-as-audit-evidence + explicit-state-transitions vocabulary applied to the AI-coding-agent-decision dimension.
- The MCP-server + guardrails + claude-code/codex/copilot/opencode/vscode/cursor-plugin-as-deployment-blueprint posture is consistent with the v2-AI MCP-as-cross-system-tooling + deterministic-rule + non-AI-fallback posture (Pick B + features 232 + 263 + 287-289 + 299-302).