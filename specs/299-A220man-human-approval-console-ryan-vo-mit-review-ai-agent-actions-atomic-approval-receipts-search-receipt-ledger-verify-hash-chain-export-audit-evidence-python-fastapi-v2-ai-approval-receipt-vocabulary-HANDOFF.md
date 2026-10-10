# HANDOFF — Feature 299: `A220man-human-approval-console-ryan-vo-...-v2-ai-approval-receipt-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/299-A220man-human-approval-console-ryan-vo-mit-review-ai-agent-actions-atomic-approval-receipts-search-receipt-ledger-verify-hash-chain-export-audit-evidence-python-fastapi-v2-ai-approval-receipt-vocabulary.md` — defer/parking-lot (Pick A of Daily Research 2026-10-10).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes an *operator-approval of AI-agent actions with atomic approval receipts + search + verify + export audit evidence* primitive, the owner wants *evidence that this approval-receipt-vocabulary exists in 2026 with a hash-chained-audit-evidence-export shape*, but struggles because *LE31 has no documented v2-AI approval-receipt-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31 + the audit-evidence-export primitive"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (atomic approval receipts + receipt-ledger + hash-chain verify + audit-evidence export) without specialist help. The 2★ with single-maintainer cadence (3-day-old repo, first in-window push) makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **Python + FastAPI on-stack** (LE31 stack match). Required data + permissions + infrastructure: Python FastAPI runtime + hash-chained audit-log + receipt-table. No AI capability required (the approval-receipt primitive is deterministic). Rabbit hole: the React + TypeScript frontend is off-LE31-frontend-stack (LE31 uses HTMX + minimal HTML). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *atomic-approval-receipt + hash-chain + audit-evidence-export* primitives are §3.1-aligned (explicit state transitions, append-only discipline). The `export-audit-evidence` primitive maps 1:1 onto the v1 `audit_logs` schema. No §3.4 customer-facing AI (the AI agent is operator-tooling). No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI outcome (operator-approval of AI-agent actions). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (`audit_logs` + `StockEntry`) already implement the discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + 3-day-old repo + React+TypeScript frontend off-LE31-stack + no v2-AI surface in v1 charter).

## Bucket

**v2-AI** (approval-receipt-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the 4-primitive set (`atomic approval receipts + search the receipt ledger + verify its complete hash chain + export audit evidence`) + the tech-stack (Python + FastAPI + React + TypeScript).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that adds a v2-AI surface that requires operator-approval of AI-agent actions with a hash-chained-audit-trail):

1. `backend/app/audit/models.py` — add new `ApprovalReceipt` SQLModel table with columns: `id` (UUID), `agent_id` (str), `action` (str), `proposed_payload` (JSON), `operator_user_id` (UUID FK), `approved_at` (timezone-aware datetime), `previous_receipt_hash` (str), `this_receipt_hash` (str).
2. `backend/app/audit/models.py` — add new `ai_agents` SQLModel table with columns: `id` (UUID), `name` (str), `description` (str), `allowed_actions` (JSON), `created_at`, `updated_at`.
3. `backend/alembic/versions/` — add Alembic migration for the new tables.
4. `backend/app/audit/repository.py` — add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `ApprovalReceipt` insert path (for the *atomic-receipt* primitive).
5. `backend/app/audit/hash_chain.py` — NEW: hash-chain utility that computes `this_receipt_hash = SHA-256(previous_receipt_hash + receipt_payload)`.
6. `backend/app/api/v2/audit/receipts.py` — NEW: `GET /v2/audit-logs/receipts/search?operator=<>&agent=<>&action=<>&as_of=<>` search endpoint.
7. `backend/app/api/v2/audit/receipts.py` — NEW: `GET /v2/audit-logs/receipts/verify` hash-chain-verify endpoint.
8. `backend/app/api/v2/audit/receipts.py` — NEW: `GET /v2/audit-logs/receipts/export?format=json|csv` audit-evidence-export endpoint.
9. `backend/app/api/v2/agents.py` — NEW: `POST /v2/agents/<agent_id>/actions/propose` endpoint.
10. `backend/app/api/v2/agents.py` — NEW: `POST /v2/agents/<agent_id>/actions/<action_id>/approve` endpoint.
11. `backend/app/api/v2/agents.py` — NEW: `POST /v2/agents/<agent_id>/actions/<action_id>/reject` endpoint.
12. `backend/app/api/v2/agents.py` — NEW: `GET /v2/audit-logs/receipts?status=pending|approved|rejected` query endpoint.

## Verification protocol

1. `git clone https://github.com/A220man/human-approval-console-ryan-vo` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/A220man/human-approval-console-ryan-vo/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set).
3. `curl -sS -H "Authorization: Bearer $HERME...OKEN" "https://api.github.com/repos/A220man/human-approval-console-ryan-vo"` for star count, fork count, license, language, pushed_at, created_at, topics, description (parent-verified 2026-10-10).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the approval-receipt + hash-chain + search + verify + export changes are isolated to the expected files.
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec` before any implementation.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2-AI trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the new tables + remove the new API endpoints.
- No data loss if the rollback happens BEFORE any approval-receipt row is written.
- Full data retention if the rollback happens AFTER rows are written (the new tables are dropped but the original `audit_logs` rows are preserved per the *append-only* invariant).

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (append-only StockEntry, etc.).
4. `le31-handoff-spec` — the handoff-spec requirements (frozen contract discipline, mandatory skill list, verification protocol).
5. `le31-feature-pipeline` — the feature-pipeline workflow (parent research issue, sub-issue creation, handoff file).

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-10 / Pick A — v2-AI approval-receipt-vocabulary (A220man/human-approval-console-ryan-vo)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-10.linear-fallback.json`. Sub-issue project = `le31 Research` (P-HMM-1) per `le31-feature-pipeline/SKILL.md` line 33 since `le31 v2-AI` does not exist.

## Parent research issue

[linear: blocked — workspace plan-limit error 20th consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-10.linear-fallback.json`]
