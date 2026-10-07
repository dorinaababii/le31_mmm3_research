# Feature 289 — `shivamk01here/LedgerLoop` v2-AI ledger-discipline-runtime-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v2-AI (v2-AI project does NOT exist; attach to `le31 Research` P-HMM-1 as the parent of the sub-issue)
> **Date:** 2026-10-07
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-hash-chained-audit-ledger-policy-engine-human-approvals-crash-safe-resumable-runs-automatic-rollback-760-tests-v2-ai-ledger-discipline-runtime-vocabulary.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-hash-chained-audit-ledger-policy-engine-human-approvals-crash-safe-resumable-runs-automatic-rollback-760-tests-v2-ai-ledger-discipline-runtime-vocabulary-HANDOFF.md`
> **Source daily research:** `/opt/data/le31-daily-research-2026-10-07.md` (pass 69, pick C)
> **Parent-verified via:** direct GitHub API GET `/repos/shivamk01here/LedgerLoop` at `/tmp/le31-daily-2026-10-07/verify/ghverify__parent_shivamk01here_LedgerLoop.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed)

## Goal

Surface a v2-AI vocabulary reference for **Python-runtime for financial AI agents with exactly-once-execution + hash-chained-audit-ledger + policy-engine-with-human-approvals + crash-safe-resumable-runs + automatic-rollback + 760+ tests** as a forward-looking pattern for any future LE31 v2-AI control-plane that runs a Python-based AI agent taking actions on the operator's behalf (e.g., modifies the menu, processes a payment, sends a Telegram message).

## Evidence / JTBD

**Evidence classification:** inferred. The *exactly-once-execution + hash-chained-audit-ledger + policy-engine-with-human-approvals* discipline is forward-looking for any future LE31 v2-AI runtime-surface; no LE31 v1 surface today has an AI agent. **Confidence: high** (0★/0⑂ + 1580 KB modest + Python on-stack ✓ + 760+ tests for 1580 KB = **~0.5 tests-per-KB = strongest v2-AI formal-test-coverage of the 69-pass series** + strictly-typed + fresh code delta).

**When** the LE31 v2-AI control-plane wants to run a Python-based AI agent that takes actions on the operator's behalf, **the owner/waiter/cook wants to** know that every tool call is executed exactly once (even under retries/failures) with a hash-chained audit ledger, a policy engine with human approvals, crash-safe resumable runs, and automatic rollback, **but struggles because** the existing `audit_logs` SQLModel table is a flat log without exactly-once-execution or hash-chained-audit-ledger or crash-safe-resumable-runs or automatic-rollback, **so that** an AI agent cannot take a tool-call action without a verifiable, retry-safe, crash-safe audit trail. The *exactly-once-execution + hash-chained-audit-ledger + crash-safe-resumable-runs + automatic-rollback* is the *append-only-ledger + idempotency + crash-recovery* charter §3.1 invariant applied to the *AI-agent-tool-call* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *exactly-once-execution + hash-chained-audit-ledger + policy-engine-with-human-approvals + crash-safe-resumable-runs + automatic-rollback + strictly-typed + 760+ tests* septuple-primitive as a candidate vocabulary for any future LE31 v2-AI runtime-surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive.
- Record the §3.1/§3.2/§3.3/§3.4/§3.7 alignment per `le31-conventions/SKILL.md`.
- Record the strongest v2-AI formal-test-coverage signal of the 69-pass series (760+ tests for 1580 KB = ~0.5 tests-per-KB).

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No AI agent runtime; v2-AI surface is forward-looking.
- No hash-chained-audit-ledger integration into the existing `audit_logs` SQLModel table.

## Description

`shivamk01here/LedgerLoop` is a **Python runtime for financial AI agents** with the following properties:
- **Idempotent exactly-once execution**: every tool call is executed exactly once, even under retries/failures (the runtime tracks which tool calls have been executed and skips already-executed ones on retry).
- **Hash-chained audit ledger**: every action is recorded in a hash-chained audit ledger (each entry's hash includes the previous entry's hash, making any tampering detectable).
- **Policy engine with human approvals**: a policy engine requires human approval for sensitive tool calls (e.g., sending a Telegram message to a customer, modifying the menu, processing a payment).
- **Crash-safe resumable runs**: if a tool call fails (e.g., network error, process crash), the runtime can resume from the last successful checkpoint.
- **Automatic rollback**: if a tool call produces an unwanted side effect, the runtime can automatically roll back to the previous state.
- **Strictly typed**: the codebase is strictly typed (Python type hints throughout).
- **760+ tests**: the runtime has 760+ tests for a 1580 KB codebase = **~0.5 tests-per-KB = the strongest v2-AI formal-test-coverage signal of the 69-pass series**.

The vocabulary is a strong §3.4-alignment signal for any future LE31 v2-AI runtime-surface because:
- The *exactly-once-execution + hash-chained-audit-ledger* IS the §3.3 *audit-log-immutability + idempotency* charter invariant applied to the *AI-agent-tool-call* dimension. The hash-chained is **stronger** than the §3.3 *append-only* primitive (it provides cryptographic-signature-as-audit-evidence).
- The *policy-engine-with-human-approvals* IS the §3.4 *non-AI-fallback* charter invariant applied to the *AI-agent-tool-call* dimension. The human approval is the *operator-must-confirm* posture.
- The *crash-safe-resumable-runs + automatic-rollback* IS the §3.1 *explicit-state-transition* charter invariant applied to the *AI-agent-tool-call-failure* dimension.
- The *strictly-typed + 760+ tests* IS the §3.4 *observable-evidence* charter invariant applied to *runtime-correctness*.

The 1/1 topic-overlap (`ai-agents`) is sparse, but the description is rich and the *760+ tests for 1580 KB = ~0.5 tests-per-KB* is the strongest v2-AI formal-test-coverage signal of the 69-pass series.

## Data model

```
ToolCall          (id, agent_id, function_name, args, idempotency_key, status, executed_at, retried_at)
AuditLedgerEntry  (id, tool_call_id, content, hash, prev_hash, at)
PolicyDecision    (id, tool_call_id, policy_name, decision, decided_at, approver_user_id)
Checkpoint        (id, run_id, state, hash, at)
RollbackEvent     (id, tool_call_id, reason, rolled_back_at, by_user_id)
```

The `AuditLedgerEntry` table is an **append-only ledger** with **hash-chain** (each entry's hash includes the previous entry's hash). The `ToolCall` table tracks the idempotency state (which tool calls have been executed and skipped on retry). The `Checkpoint` table tracks the resumable-run state. The `RollbackEvent` table tracks the rollback events. Never `UPDATE` or `DELETE` `AuditLedgerEntry` or `RollbackEvent` rows.

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v2-AI PR adopts the *exactly-once-execution + hash-chained-audit-ledger* discipline, the following files would be touched:

- `/opt/data/le31_mmm3_research_work/backend/app/models/agent_tool_call.py` — new SQLModel `ToolCall` + `AuditLedgerEntry` (hash-chained) + `PolicyDecision` + `Checkpoint` + `RollbackEvent` tables (append-only, §3.1 invariant).
- `/opt/data/le31_mmm3_research_work/backend/app/services/idempotency.py` — exactly-once-execution dispatcher.
- `/opt/data/le31_mmm3_research_work/backend/app/services/policy_engine.py` — policy-engine with human-approval gates.
- `/opt/data/le31_mmm3_research_work/backend/app/services/checkpoint.py` — checkpoint + resume logic.
- `/opt/data/le31_mmm3_research_work/backend/app/services/rollback.py` — automatic-rollback logic.
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v1 build; vocabulary-only). If a future v2-AI runtime-surface is built, the owner-side Telegram bot could surface tool-call events with their policy-decision state and rollback history (e.g., "Agent tool call: send_telegram. Policy decision: approved by owner. Executed at 14:32. Rollback: not triggered.").

## Dependencies

- **Charter §3.3 (audit-log-immutability)**: existing `audit_logs` SQLModel table is the v1 precedent; the `AuditLedgerEntry` table extends the same pattern to the *AI-agent-tool-call* dimension with **hash-chained cryptographic-signature-as-audit-evidence** (stronger than the v1 append-only primitive).
- **Charter §3.4 (MCP-integration)**: the runtime could integrate with the MCP-server primitive from Pick B (`pete-builds/mcp-nixreview`) for tool-call routing.
- **Charter §3.1 (explicit-state-transition)**: the *automatic-rollback* primitive requires a transactional-outbox pattern to ensure the rollback and the forward transition are atomic.
- **No v1 dependencies**: this is a v2-AI surface; no v1 code depends on it.

## Open questions

1. **Who would ever run the offline verifier of a hash-chained-audit-ledger with exactly-once-execution + crash-safe-resumable-runs + automatic-rollback?** LE31 has exactly one stakeholder (the owner) who can just trust the agent directly. The *exactly-once-execution + hash-chained-audit-ledger + automatic-rollback* may be over-engineering for a single-tenant single-operator scenario.
2. **What is the rollback semantics for a tool call that has external side effects?** If a tool call sends a Telegram message to a customer, the *automatic-rollback* cannot undo the message. The runtime would need to send a *correction* message. A future PR would need to specify the correction-message policy.
3. **What is the human-approval latency budget?** The *policy-engine-with-human-approvals* is a synchronous operator-must-confirm; the latency budget depends on the operator's responsiveness. A future PR would need to specify the timeout policy (e.g., 5 minutes → auto-reject).
4. **What is the relationship between the v1 `StockEntry` event-sourcing pattern and the v2-AI `ToolCall` + `AuditLedgerEntry` pattern?** The v1 pattern is a single-table event-sourcing; the v2-AI pattern is a multi-table + hash-chained + idempotency. A future PR would need to specify the migration path.

## Why this matters

This is the **only Python on-stack v2-AI financial-AI-agent-runtime with hash-chained-audit-ledger + 760+-tests pick of the 69-pass series = the strongest v2-AI ledger-discipline-runtime with formal-test-coverage signal of the 69-pass series**. The *exactly-once-execution + hash-chained-audit-ledger + policy-engine-with-human-approvals* discipline is the closest vocabulary to a future LE31 v2-AI runtime-surface; the *hash-chained-audit-ledger* extends the v1 `audit_logs` SQLModel table to the *AI-agent-tool-call* dimension with **stronger-than-append-only cryptographic-signature-as-audit-evidence**; the *exactly-once-execution + crash-safe-resumable-runs* extend the v1 `StockEntry` event-sourcing pattern to the *AI-agent-tool-call-failure* dimension.

The **760+ tests for 1580 KB = ~0.5 tests-per-KB = the strongest v2-AI formal-test-coverage signal of the 69-pass series** = any future LE31 v2-AI PR that adopts Pick C's vocabulary would inherit a runtime with formal-verification discipline. The *strictly-typed* discipline extends the v1 `pydantic` SQLModel type-safety pattern to the *runtime-correctness* dimension.

**Charter alignment summary:** §3.1 partial (exactly-once-execution + hash-chained-audit-ledger + crash-safe-resumable-runs); §3.2 strictly-compatible (MIT permissive); §3.3 ✓ (hash-chained-audit-ledger = cryptographic-signature-as-audit-evidence = stronger than §3.3 append-only); §3.4 strongest §3.4-alignment signal of the 69-pass series for any v2-AI runtime (policy-engine-with-human-approvals + 760+ tests + non-AI-fallback + observable-evidence); §3.7 N/A.
