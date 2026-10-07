# HANDOFF — 289-shivamk01here-LedgerLoop-v2-ai-ledger-discipline-runtime-vocabulary

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-07
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-hash-chained-audit-ledger-policy-engine-human-approvals-crash-safe-resumable-runs-automatic-rollback-760-tests-v2-ai-ledger-discipline-runtime-vocabulary.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; 760+ tests for 1580 KB = strongest v2-AI formal-test-coverage of 69-pass series; only Python on-stack v2-AI financial-AI-agent-runtime with hash-chained-audit-ledger + 760+-tests pick of 69-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window
v2-AI vocabulary reference (`shivamk01here/LedgerLoop`, MIT, 0★/0⑂, 1580 KB modest,
Python on-stack ✓, 760+ tests for 1580 KB = ~0.5 tests-per-KB = strongest v2-AI
formal-test-coverage of the 69-pass series) for the next time the LE31 owner
opens a v2-AI runtime-surface window.

If the trigger condition (v2-AI runtime-surface window opens) is met, the
external coding agent should:

1. Read the active feature file in full.
2. Confirm the `shivamk01here/LedgerLoop` repo is still in-window (pushed within last 7 days
   from the trigger date) and the description is still the same.
3. Implement the `ToolCall` + `AuditLedgerEntry` (hash-chained) + `PolicyDecision` + `Checkpoint` + `RollbackEvent`
   SQLModel tables as described in the active feature's Data model section.
4. Implement the exactly-once-execution dispatcher service.
5. Implement the policy-engine with human-approval gates service.
6. Implement the checkpoint + resume logic service.
7. Implement the automatic-rollback logic service.
8. Run the v1 test suite + the new v2-AI runtime-surface test suite.
9. Surface any test failures to the owner (LE31 v1 has no AI agent today;
   the test suite will be green if the `ToolCall` table is empty, but the
   exactly-once-execution must be verified against a simulated retry scenario
   to detect any idempotency bugs).
10. Verify the v1 `audit_logs` SQLModel table is untouched (the v2-AI runtime audit ledger
    is a NEW hash-chained table with cryptographic-signature-as-audit-evidence,
    not a migration of the v1 audit log).

If the trigger condition is **not** met, do nothing. The defer
artifact can be safely ignored until the owner opens a v2-AI runtime-surface
window.

## Mandatory inputs

- **Active feature**: `features/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-hash-chained-audit-ledger-policy-engine-human-approvals-crash-safe-resumable-runs-automatic-rollback-760-tests-v2-ai-ledger-discipline-runtime-vocabulary.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-07.md` (pass 69, pick C)
- **Raw fetches**: `/tmp/le31-daily-2026-10-07/gh-q9-ai-agent-audit-ledger.json` (parent re-fetched the productive g9 query) and `/tmp/le31-daily-2026-10-07/verify/ghverify__parent_shivamk01here_LedgerLoop.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 69-pass series**:
  - **Feature 281 — `siezonsolutions/Seintinel-WasmGate`** (10-06 pick) — v2-AI zero-trust-execution-gate-vocabulary
  - **Feature 282 — `AllStreets/ONEXUS`** (10-06 pick) — v2-AI capability-arbiter-runtime-vocabulary
  - **Feature 283 — `NovasPlace/CSM`** (10-06 pick) — v2-AI persistent-memory-vocabulary
  - **Feature 287 — `noise01/endoxa`** (10-07 pick) — v2-AI governed-beliefs-vocabulary
  - **Feature 288 — `pete-builds/mcp-nixreview`** (10-07 pick) — v2-AI MCP-server-attestation-vocabulary (provides the `MCP-server` primitive that Pick C could integrate with for tool-call routing)
- **Charter §3.1 + §3.3 + §3.4 invariants**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the
  hard invariants (charter §3.1 explicit-state-transition + §3.3 audit-log-immutability + §3.4 AI-sandbox-as-auditable-test + non-AI-fallback + observable-evidence).
- `le31-v1-feature-pattern` — for the canonical contract shape.
- `le31-research` — for the source-of-truth discipline on GitHub
  repository verification.
- `development` — for the generic code-change workflow.

The agent must NOT load `le31-feature-pipeline` (this is a defer
artifact, not a build pipeline candidate).

## Frozen contract

The v2-AI vocabulary reference is:

- **Repo**: `shivamk01here/LedgerLoop`
- **License**: MIT (permissive; charter §3.2 strictly-compatible)
- **Stars**: 0★/0⑂ at parent-verification time
- **Pushed**: 2026-10-05T04:58:06Z (in-window by `pushed_at` at 2026-10-07)
- **Created**: 2026-07-17T07:27:47Z (out-of-window by `created_at` = ~75 days before window-start)
- **Size**: 1580 KB modest
- **Language**: Python ✓ (on-stack)
- **Topics (1)**: `ai-agents` (sparse topics, but description is rich)
- **Description (verbatim)**: *Python runtime for financial AI agents: idempotent exactly-once execution, hash-chained audit ledger, policy engine with human approvals, crash-safe resumable runs, and automatic rollback. Strictly typed, 760+ tests.*
- **Test density**: 760+ tests for 1580 KB = **~0.5 tests-per-KB = the strongest v2-AI formal-test-coverage signal of the 69-pass series**

The vocabulary primitives are:

- `ToolCall` (id, agent_id, function_name, args, idempotency_key, status, executed_at, retried_at)
- `AuditLedgerEntry` (id, tool_call_id, content, hash, prev_hash, at)
- `PolicyDecision` (id, tool_call_id, policy_name, decision, decided_at, approver_user_id)
- `Checkpoint` (id, run_id, state, hash, at)
- `RollbackEvent` (id, tool_call_id, reason, rolled_back_at, by_user_id)

The `AuditLedgerEntry` table is an **append-only ledger with hash-chain** (each entry's
hash includes the previous entry's hash). The `ToolCall` table tracks the
idempotency state (which tool calls have been executed and skipped on retry).
The `Checkpoint` table tracks the resumable-run state. The `RollbackEvent`
table tracks the rollback events. Never `UPDATE` or `DELETE` `AuditLedgerEntry`
or `RollbackEvent` rows.

## Files to touch (when v2-AI runtime-surface window opens)

- `/opt/data/le31_mmm3_research_work/backend/app/models/agent_tool_call.py` — new SQLModel `ToolCall` + `AuditLedgerEntry` (hash-chained) + `PolicyDecision` + `Checkpoint` + `RollbackEvent` tables.
- `/opt/data/le31_mmm3_research_work/backend/app/services/idempotency.py` — exactly-once-execution dispatcher.
- `/opt/data/le31_mmm3_research_work/backend/app/services/policy_engine.py` — policy-engine with human-approval gates.
- `/opt/data/le31_mmm3_research_work/backend/app/services/checkpoint.py` — checkpoint + resume logic.
- `/opt/data/le31_mmm3_research_work/backend/app/services/rollback.py` — automatic-rollback logic.
- (No other files expected to require changes for a vocabulary-only PR.)
- (Do NOT modify the existing v1 `audit_logs` SQLModel table; the v2-AI runtime audit ledger is a NEW hash-chained table with cryptographic-signature-as-audit-evidence.)

## Verification protocol

When the v2-AI runtime-surface window opens:

1. Confirm the `shivamk01here/LedgerLoop` repo is still in-window (pushed within last 7 days
   from the trigger date) via `git ls-remote` or direct GitHub API GET.
2. Run `uv sync` (or `pip install -e .`) to install any new dependencies.
3. Run the v1 test suite — all tests must pass.
4. Run the new v2-AI runtime-surface test suite (if any) — the exactly-once-execution
   test must verify that a simulated retry scenario (execute → crash → retry) results in
   only one `ToolCall` row (idempotency).
5. Run the LE31 v1 `audit_logs` test suite — the v1 audit log is untouched
   by the v2-AI runtime-surface PR.
6. Surface any test failures to the owner (LE31 v1 has no AI agent today;
   the test suite will be green if the `ToolCall` table is empty, but the
   exactly-once-execution must be verified against a simulated retry scenario
   to detect any idempotency bugs).

## Rollback path

If the v2-AI runtime-surface PR causes regressions:

1. Revert the SQLModel table additions (drop the `ToolCall` + `AuditLedgerEntry` + `PolicyDecision` + `Checkpoint` + `RollbackEvent` tables via Alembic downgrade).
2. Revert the idempotency + policy-engine + checkpoint + rollback service additions.
3. Re-run the v1 test suite.
4. Surface to the owner.

The v2-AI runtime-surface PR is fully reversible — no v1 code is touched; the
v2-AI tables are new additions, not migrations of v1 tables.

## Sign-off gap

No build today. The defer artifact does not require sign-off from
the owner; it surfaces a dated, in-window v2-AI vocabulary reference
and waits for the next v2-AI runtime-surface window.

If the owner opens a v2-AI runtime-surface window, the external coding
agent must mirror this contract back to the owner before implementing
and stop if it cannot.
