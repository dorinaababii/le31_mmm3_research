# HANDOFF — 297-jonalemndi2-ALdia-v1-cross-industry-small-business-erp-with-ai-mcp-tools-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-09
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/297-jonalemndi2-ALdia-apache-2-0-open-source-business-engine-ai-agents-invoicing-payments-inventory-checks-cash-permission-controlled-mcp-tools-idempotency-immutable-audit-trail-self-hosted-offline-first-multi-country-v1-cross-vocabulary-reference.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v1 cross-industry small-business-ERP-with-AI-MCP-tools cross-section pick of the 72-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v1 cross-industry small-business-ERP-with-AI-MCP-tools vocabulary reference (`jonalemndi2/ALdia`, Apache-2.0, 5★/0⑨, 1807 KB modest, Python ✓ on-stack, 20 topics, in-window by `pushed_at`, 5★ community traction today = highest community traction of the 72-pass series) for the next time the LE31 owner opens a v1 cross-industry small-business-ERP-with-AI-MCP-tools surface window.

If the trigger condition (v1 cross-industry small-business-ERP-with-AI-MCP-tools surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `jonalemndi2/ALdia` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Set up FastMCP sub-app under `le31-mcp-server`.
4. Implement the `McpToolRegistry + McpToolPermission + McpToolCall + Country` SQLModel tables as described in the active feature's Data model section.
5. Implement the permission-controlled-MCP-tools discipline (every tool exposes fine-grained permission).
6. Implement the idempotency discipline (every tool call has a unique idempotency key + returns the same result on replay).
7. Implement the structured-error discipline (every tool returns a typed error with code + message + context).
8. Implement the immutable-audit-trail discipline (every tool call writes to `audit_logs`).
9. Implement the offline-first discipline (no remote API dependency for the business-engine layer).
10. Adapt `ALdia`'s SQLite choice to LE31 v1's Postgres invariant.
11. Adapt `ALdia`'s `Country` table to LE31 v1's EUR + Paris-only invariant (charter §3.5 + §3.6).
12. Run the v1 test suite + the new v1 MCP-server test suite.
13. Surface any test failures to the owner (LE31 v1 has no MCP-server today; the test suite will be green if `McpToolRegistry + McpToolPermission + McpToolCall` are empty, but the permission-controlled + idempotency + immutable-audit-trail disciplines must be verified against the v1 stack).
14. Verify the v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are untouched (the v1 `McpToolRegistry + McpToolPermission + McpToolCall + Country` tables are NEW, not a migration of v1 `audit_logs`).
15. **CHARTER §3.4 RIPGL_REVIEW REQUIRED before implementation begins** — the *claude-as-AI-agent-tool-provider* posture IS the §3.4 *AI-as-tool-caller* candidate; the *permission-controlled-MCP-tools + idempotency + immutable-audit-trail* posture IS the *non-AI-fallback + observable-evidence + human-gate + fine-grained-permission* §3.4 invariant. Explicit charter-§3.4-review needed before any v2-AI PR that adopts the *AI-agent-tool-provider* posture with a customer-facing AI.

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v1 cross-industry small-business-ERP-with-AI-MCP-tools surface window.

## Mandatory inputs

- **Active feature**: `features/297-jonalemndi2-ALdia-apache-2-0-open-source-business-engine-ai-agents-invoicing-payments-inventory-checks-cash-permission-controlled-mcp-tools-idempotency-immutable-audit-trail-self-hosted-offline-first-multi-country-v1-cross-vocabulary-reference.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-09.md` (pass 72, pick B)
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-09/verify_jonalemndi2_ALdia.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 72-pass series**:
  - **Feature 286 — `gadyamedia/vocenya-mcp`** — v2-AI MCP-server-for-AI-receptionist
  - **Feature 288 — `pete-builds/mcp-nixreview`** — v2-AI MCP-server-+-CVE/KEV-attestation-gate-+-AI-agents-+-append-only-audit-ledger
  - **Feature 232 — `lpalbou/AbstractGateway`** — v2-AI replay-first-durable-AI-control-plane-+-append-only-ledger
  - **Feature 254 — `OthmaneBlial/lightclaw`** — v2-AI supervise-local-Codex-and-Claude-agents-from-Telegram-+-review-plans-approve-scoped-work-+-inspect-diffs-and-tests
  - **Feature 267 — `S0tman/irp-capture`** — v2 owner-pains append-only-ledger-that-records-why-decisions-were-made-+-decision-log-+-knowledge-management-+-local-first
  - **Feature 197 — `rajo69/ledgerkb`** — v2 owner-pains evidence-bearing-assertions-+-position-over-time-+-append-only-ledger-+-rag-+-knowledge-graph
  - **Feature 245 — `EvezArt/evez-event-spine`** — v2 append-only-hash-linked-event-log-+-immutable-+-verifiable-+-readable-+-truth-+-content-hash-chain-discipline
  - **Feature 271 — `znbsf/agent-case-graph`** — v2 owner-pains evidence-first-append-only-case-ledger-+-provenance-graph-+-deterministic-validation-+-audit-trail-+-jsonl-event-sourcing-+-knowledge-graph

## Verification protocol

Per `le31-conventions/SKILL.md` verification protocol:
- All SQLModel tables must use `Decimal` for any money field (charter §3.6)
- All datetime fields must be timezone-aware (Europe/Paris per charter §3.6)
- All tool-call records must write to `audit_logs` via the standard LE31 audit-pipeline (charter §3.1 + §3.3)
- All on-stack dependencies (FastAPI, Pydantic) per charter §3.1 stack constraint
- All off-stack dependencies (FastMCP, SQLite, Claude API) require explicit charter review

## Rollback path

The pick is a parking-lot vocabulary reference. If the trigger condition is met and the implementation does not work, the implementation can be rolled back by:
1. Dropping the `McpToolRegistry + McpToolPermission + McpToolCall + Country` SQLModel tables (no data loss expected; vocabulary-only references do not have production data)
2. Removing the FastMCP sub-app `le31-mcp-server`
3. Disabling the Claude API integration
4. Removing the `mcp-server` FastAPI endpoints

The rollback is fully reversible; no v1 data is touched.

## Mandatory LE31 skill list

The coding agent MUST load before starting any implementation:
- `le31-conventions` — for the standard v1 conventions (audit_logs, money discipline, Paris timezone)
- `le31-v1-feature-pattern` — for the standard v1 feature pattern (SQLModel tables + FastAPI endpoints + minimal-HTML/HTMX templates + Telegram interaction if any)
- `le31-handoff-spec` — for the slice handoff format (this document)
- `le31-coding-agent-brief` — for the paste-in prompt format (this slice contract is the paste-in prompt)

This is a **defer artifact**; the coding agent does NOT need to start implementation today. The trigger condition (v1 cross-industry small-business-ERP-with-AI-MCP-tools surface window opens) is not met. The artifact is preserved on file for future surfacing.
