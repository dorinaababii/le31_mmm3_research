# HANDOFF — 332-vsov-xcheck

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today) — **v2-AI cross-agent-audit-methodology-vocabulary only; the `xcheck` codebase is OFF-§3.1 (LLM-API-key + findings-ledger SQLite not in v1 stack) and NOT adopted; a future v2-AI owner-tooling PR would adopt the 2-AI-agents + 1-human + findings-ledger + cross-verify vocabulary from scratch, re-implementing in Python+FastAPI+Postgres+SQLModel+aiogram v3 + 2-LLM-provider-pluggable + findings-ledger**

**Date**: 2026-10-17
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/332-vsov-xcheck-mit-cross-agent-audit-remediation-methodology-2-ai-agents-1-human-audit-fix-cross-verify-findings-ledger-python-v2-ai-cross-agent-audit-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no AI surface; v2-AI bucket exists in skill but does NOT exist as a Linear project per today's confirmed workspace-state — only 3 projects exist: `le31 v1 — Core MVP`, `le31 Workflow`, `le31 Research`; the cross-agent-audit + 2-AI-agents + 1-human + findings-ledger + cross-verify vocabulary is a forward-looking v2-AI reference; the `xcheck` codebase requires an LLM-API-key + a `findings-ledger` SQLite database which are NOT currently in the LE31 v1 stack and require §3.1 + §3.2 + §3.4 charter review).

## Trigger policy

This is a **defer artifact (parking-lot, v2-AI cross-agent-audit-methodology-vocabulary only)** — a watch-list entry. It does not start a build. It surfaces the `vsov/xcheck` GitHub repo (MIT, **★5 / ⑂2**, **1814 KB modest**, Python ✓ ON-STACK, **pushed 2026-10-16T18:19:15Z = in-window by `pushed_at` (yesterday's push) AND created 2026-07-21T16:56:29Z = ~3-month-old repo with in-window `pushed_at` = IN-WINDOW BY `pushed_at` ONLY**) as a dated, in-window **v2-AI cross-agent-audit-methodology-vocabulary peer** for LE31's potential *2-AI-agents + 1-human + audit + fix + cross-verify + findings-ledger* surface.

If the trigger condition (LE31 first proposes a v2-AI surface that wants *cross-agent-audit* OR *2-AI-agents + 1-human + findings-ledger + cross-verify* OR *audit + fix + cross-verify* OR *code-review* OR *methodology* primitives, OR a future owner decision opens the v2-AI bucket for operator-tooling AI surfaces with charter §3.4 review) is met, the external coding agent should:

1. Load this artifact and the parent daily-research report (`/opt/data/le31-daily-research-2026-10-17.md`).
2. Load the `xcheck` repo: `https://github.com/vsov/xcheck` — README + 2-AI-agents + 1-human + findings-ledger + cross-verify docs; **the codebase is OFF-§3.1 (LLM-API-key + findings-ledger SQLite not in v1 stack) and NOT adopted — the cross-agent-audit-methodology vocabulary is**.
3. Load the companion features 232 + 287-289 + 298 + 302-304 + 306 + 312-313 + 327 + 333 + 334 (the persistent v2-AI cross-agent-audit + auditable-ledger vocabulary cluster).
4. **Adopt the cross-agent-audit-methodology vocabulary (2-AI-agents + 1-human + audit + fix + cross-verify + findings-ledger), NOT the `xcheck` codebase**. The transferable items are: (a) *2-AI-agents*; (b) *1-human*; (c) *audit*; (d) *fix*; (e) *cross-verify*; (f) *findings-ledger*. Each is a *pattern* in LE31's v2-AI charter, not a *code dependency*.
5. Re-run the LE31 feature gate with the adoption in mind. **Critical charter checks before any adoption**:
   - §3.1 partial (Python ✓; LLM-API-key OFF-§3.1 = explicit charter-decision needed for v2-AI PR)
   - §3.2 partial (LLM-API-key + findings-ledger-SQLite = 2 dependencies to add to the v1 dependency-whitelist = §3.2 charter review; LLM-API-key + findings-ledger-SQLite are NOT currently in v1 whitelist = 2 NEW dependencies)
   - §3.3 N/A (the *findings-ledger* is a v2-AI primitive; LE31 v1 `audit_logs` is already append-only)
   - §3.4 partial (cross-agent-audit = operator-tooling AI per §3.4 charter invariant "AI may assist owner/staff, with observable evidence and a non-AI fallback"; the surface accepts the chokepoint-governed + human-gate + observable-evidence + non-AI-fallback charter invariant; the 1-human is the chokepoint = §3.4 invariant)
   - §3.7 N/A (no PII; code-review + audit are public data)
6. **Decide whether the proposed v2-AI surface benefits from the cross-agent-audit-methodology vocabulary**. If the v2-AI surface wants *cross-agent-audit* OR *2-AI-agents + 1-human + findings-ledger + cross-verify* primitives, the `xcheck` pattern is purpose-built for that use case (re-implement in Python+FastAPI+Postgres+SQLModel+aiogram v3 + 2-LLM-provider-pluggable + findings-ledger). If the v2-AI surface only wants to add a *static-dashboard* without AI-decisions, `xcheck` adds no value.
7. **If the cross-agent-audit-methodology vocabulary is proposed for adoption**: do NOT add `xcheck` to `requirements-xcheck.txt`; instead, design the v2-AI surface as a fresh Python+FastAPI+Postgres+SQLModel+aiogram v3 implementation that captures the *2-AI-agents + 1-human + audit + fix + cross-verify + findings-ledger* primitives. Add to `requirements-new-v2-ai-cross-agent-audit.txt` only the new dependencies (2 LLM-API-key clients; the v1 SQLModel+Postgres+aiogram v3 stack is already adopted). Add a single test cross-agent-audit call against a single audit from the LE31 owner-side. Compare against the existing v1 manual-audit flow. If the test cross-agent-audit adds operator-assistant-value, propose a v2-AI extension; if not, document the comparison and defer.
8. **If the cross-agent-audit-methodology vocabulary is not adopted**: document the comparison and defer. No charter §3.1 + §3.2 + §3.4 change is needed.
9. **Pilot on one real-restaurant first**. Do not ship the cross-agent-audit project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/332-vsov-xcheck-...md`
- **Parent daily-research report**: `/opt/data/le31-daily-research-2026-10-17.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-17/gh/gh_g9.json` and `/tmp/le31-daily-2026-10-17/verify/ghverify_vsov_xcheck.json` (where `vsov/xcheck` is listed; parent-verified raw JSON has `stargazers_count=5`, `forks_count=2`, `license.spdx_id=MIT`, `pushed_at=2026-10-16T18:19:15Z`, `created_at=2026-07-21T16:56:29Z`, `description="Cross-agent audit & remediation methodology: two AI agents and one human audit, fix, and cross-verify large projects (code or text) through a findings ledger"`, `size=1814`, `topics=["ai-agents", "audit", "code-review", "methodology"]`)
- **`xcheck` repo**: `https://github.com/vsov/xcheck` (parent-fetched 2026-10-17 metadata; verify-via-direct-GitHub-API-GET at `/tmp/le31-daily-2026-10-17/verify/ghverify_vsov_xcheck.json` — **for v2-AI cross-agent-audit-methodology-vocabulary reference only, NOT for code adoption**)
- **Companion artifacts**:
  - `features/232-...md` (carry-over from 08-30 `lpalbou/AbstractGateway` MIT HTTP control plane for durable AI runs + append-only ledger + Telegram surface)
  - `features/287-noise01-endoxa-...md` (carry-over from 10-07 `noise01/endoxa` Apache-2.0 governed-beliefs-for-llm-agents + append-only-ledger + SMT-checked-consistency)
  - `features/288-pete-builds-mcp-nixreview-...md` (carry-over from 10-07 `pete-builds/mcp-nixreview` MIT MCP-server + CVE/KEV-attestation-gate + AI-agents + append-only-audit-ledger)
  - `features/289-shivamk01here-LedgerLoop-...md` (carry-over from 10-07 `shivamk01here/LedgerLoop` MIT Python-runtime-for-financial-AI-agents + hash-chained-audit-ledger + 760+ tests)
  - `features/298-the-vibey-project-vibey-...md` (carry-over from 10-13 `the-vibey-project/vibey` MIT AI-coding-agents-orchestrator + append-only-PostgreSQL-ledger + crash-safe-resumable)
  - `features/302-...md` (carry-over from 10-11 `warrant-ai/warrant` decision-ledger)
  - `features/303-...md` (carry-over from 10-11 `Bastardki11er/tally` double-entry-ledger)
  - `features/304-...md` (carry-over from 10-11 `DSHCorrectover/agent-second-fuse` fail-closed-second-fuse)
  - `features/306-...md` (carry-over `gtheonse/resortflow` hold-then-confirm-saga-concierge)
  - `features/312-...md` (carry-over `Alex8791-cyber/cognithor` local-first-agent-OS)
  - `features/313-...md` (carry-over `jklthinking/retinue` self-hosted-AI-worker-coordination)
  - `features/327-musterhq-muster-...md` (carry-over from 10-16 `musterhq/muster` MIT AI-agent-harness + audit-ledger + token-waste-ledger + leak-proof-scoped-memory + 20+-LLM-providers)
  - `features/333-FlashyLabs-flashy-ledger-...md` (today's `FlashyLabs/flashy-ledger` Apache-2.0 open-ledger-rules + append-only + hash-chained + integer minor units + idempotent writes + balances always derived)
  - `features/334-donaldrichard19-LVD-pattern-mcp-...md` (today's `donaldrichard19-LVD/pattern-mcp` MIT MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger)
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.3 append-only audit-log-immutability, §3.4 no-customer-facing-AI + owner/staff-assist-only + observable-evidence + non-AI-fallback, §3.7 privacy + data-protection).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Files to touch

This is a defer artifact. The future-v2-AI re-implementation would touch:
- `le31-backend/app/ai_agents/` (NEW directory for v2-AI agent orchestration)
- `le31-backend/app/ai_agents/cross_agent_audit.py` (NEW: 2-AI-agents + 1-human + audit + fix + cross-verify + findings-ledger)
- `le31-backend/app/audit_log_decision_extension.py` (NEW: extend v1 `audit_logs` with `decision_type` + `decision_by_agent_id` columns)
- `le31-backend/app/llm_provider_pluggable.py` (NEW: 2-LLM-provider-pluggable interface)
- `le31-backend/migrations/2026_XX_XX_add_ai_decision_columns.py` (NEW Alembic migration)
- `le31-backend/tests/test_cross_agent_audit.py` (NEW: test cross-agent-audit + findings-ledger)
- `le31-backend/tests/test_audit_log_decision_extension.py` (NEW: test audit_log extension)

## Verification protocol

The external coding agent verifies:
1. The 7-feature-gate re-ran with the §3.1 + §3.2 + §3.4 review
2. The audit_log extension is backward-compatible with the v1 append-only invariant
3. The 2-LLM-provider-pluggable interface is testable in isolation
4. The findings-ledger is append-only (no updates, no deletes)
5. The end-to-end acceptance path is executable in the configured environment (1 owner starts a cross-agent-audit; 2 AI agents + 1 human participate; the audit produces a findings-ledger; the findings are recorded in the extended `audit_logs` table)
6. The rollback path is reversible (delete the new directory + revert the migration + restore the original `audit_logs` schema)
7. The LLM-API-key is stored securely (charter §3.7 partial; the LLM-API-key is a secret and must NOT be logged)

The agent must mirror back the slice ID, the required skills, the verification protocol, and the rollback path before implementing.

## Rollback path

This is a defer artifact. The future-v2-AI re-implementation rollback path:
1. Stop the v2-AI cross-agent-audit service
2. Drop the new tables (`AIAgent`, `AIAudit`, `AIAuditFix`, `AICrossVerify`, `AIFindingsLedger`)
3. Revert the Alembic migration (drop the new columns from `audit_logs`)
4. Delete the new directory `le31-backend/app/ai_agents/`
5. Delete the new test files
6. Verify the v1 `audit_logs` schema is restored to its pre-migration state
7. Verify the v1 surface (waiter web UI + cook Telegram bot) still works

The rollback is fully reversible (vocabulary-only artifact today; future v2-AI re-implementation would be a fresh v2-AI extension with no v1 schema change required if the v1 `audit_logs` extension is the only schema touch).

## Open questions

- **What is the exact chokepoint sequence in v2-AI cross-agent-audit?** See feature 332 open questions.
- **How does the findings-ledger interact with the existing LE31 v1 `audit_logs` table?** See feature 332 open questions.
- **What is the cross-verify failure-mode?** See feature 332 open questions.
- **Should LE31 v1 adopt the *2-AI-agents + 1-human + cross-verify* discipline today for non-AI work?** See feature 332 open questions.
- **Could the existing v1 `audit_logs` table be extended with a `severity` column to capture cross-agent-audit findings without adding a new table?** See feature 332 open questions.

## Adjacent evidence

- `features/333-FlashyLabs-flashy-ledger-...md` (today's `FlashyLabs/flashy-ledger` Apache-2.0 open-ledger-rules + append-only + hash-chained + integer minor units + idempotent writes + balances always derived)
- `features/334-donaldrichard19-LVD-pattern-mcp-...md` (today's `donaldrichard19-LVD/pattern-mcp` MIT MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger)
- `features/332-vsov-xcheck-...md` (today's `vsov/xcheck` MIT cross-agent-audit-methodology)

The 3 today's picks form an "auditable-ledger-cluster" = cross-agent-audit + open-ledger-rules + auditable-decision-ledger = a unified audit-ledger vocabulary for any future v2-AI surface.
