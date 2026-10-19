# Slice Handoff — Feature 344 (devaccuracy/ledgerforge)

> **Feature ID**: 344
> **Feature path**: `/opt/data/le31_mmm3_research_work/features/344-devaccuracy-ledgerforge-apache-2-0-go-ai-native-money-movement-double-entry-ledger-exact-integer-money-verifiable-audit-chain-server-enforced-spending-limits-approvals-for-ai-agents-mcp-server-vocabulary.md`
> **Decision**: defer (parking-lot, vocabulary reference)
> **Bucket**: v2-AI

## LE31 feature gate verdict (carried from feature contract)

- **Evidence precondition**: inferred (vocabulary observation, not observed LE31 user pain). Confidence: high.
- **Seven checks**:
  1. **JTBD**: When a v2-AI workflow needs to handle money (Pick A), the operator wants every money amount to be exact integer + every state transition to be verifiable in an audit chain + every spending to be server-enforced with spending limits and approvals + the API to be exposed as an MCP server.
  2. **Viability**: medium — the *integer-money + audit-chain + chokepoint + MCP-server* discipline is operator-readable but the *server-enforced-spending-limits + approvals-for-AI-agents* requires a v2-AI workflow window + charter §3.4 review.
  3. **Practicability and confidence**: Go off-stack; the *vocabulary* is portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 with a charter §3.6 + §3.3 + §3.4 review; confidence: medium.
  4. **Conflict**: no hard conflict with any charter invariant. v2-AI bucket pick; the `le31 v2-AI` project does NOT exist in the workspace, so this pick attaches to `le31 Research` P-HMM-1 as parent of the sub-issue.
  5. **Outcome / appetite / scope**: v2-AI outcome; 0 build time today; max 4 weeks if a v2-AI window opens (1 week to specify, 1 week to plan, 2 weeks to build + verify).
  6. **Cost to operational value**: low RICE; not a v1 PR candidate.
  7. **Circuit breaker / reversibility**: fully reversible (vocabulary-only artifact; no code adoption).
- **Decision**: **defer (parking-lot, vocabulary reference)**.

## Files this slice will touch (when implemented)

> Not implemented today. When a v2-AI window opens, the implementation will touch:

- `app/v2/ai/money/__init__.py` — new package
- `app/v2/ai/money/models.py` — `Account` + `MoneyEntry` (append-only per charter §3.3) + `SpendingLimit` + `ApprovalRequest` SQLModel tables
- `app/v2/ai/money/ledger.py` — `record_money_entry` + `verify_audit_chain` + `enforce_spending_limit` business logic
- `app/v2/ai/money/router.py` — FastAPI router under `/v2/ai/money` with CRUD endpoints + MCP-server adapter
- `app/v2/ai/money/templates/` — HTMX templates for the operator-facing account/entry/approval UI
- `app/v2/ai/money/tests/` — verify the double-entry invariant (debit == credit) + verify the audit-chain integrity (hash-chained) + verify the spending-limit enforcement
- `migrations/` — alembic migration for the new tables

> **Greenfield**: no existing v1 files are touched by this slice (LE31 v1 has no money-movement surface; the v1 only handles EUR receipt recording via the payment-processor payout reconciliation feature 05, which is a different concern).

## Verification protocol (when implemented)

1. Run `pytest app/v2/ai/money/tests/` and verify all tests pass.
2. Manually create a `MoneyEntry` with debit != credit; verify the router returns HTTP 400 with a descriptive error (double-entry invariant violation).
3. Manually create a `MoneyEntry` with a tampered `audit_chain_hash`; verify the `verify_audit_chain` function returns False (audit-chain integrity violation).
4. Manually create a `MoneyEntry` that exceeds the `SpendingLimit`; verify the `enforce_spending_limit` function returns False (spending-limit enforcement violation).
5. Manually create a `MoneyEntry` that exceeds the `SpendingLimit`; verify the `ApprovalRequest` row is created (human-gate per charter §3.4).
6. Verify the HTMX account/entry/approval UI renders the account list + the entry list + the approval list.
7. Verify the MCP-server endpoint returns the tool list (the MCP-server adapter is correctly wired).

## Rollback path

- `git revert <commit-hash>` to remove the v2-AI money-movement surface.
- `alembic downgrade -1` to drop the new tables.
- No v1 data is affected (greenfield; no migration of existing v1 data).
- All `MoneyEntry` rows are append-only per charter §3.3; they remain in the audit trail even after the rollback (the rollback only removes the application code, not the audit data).

## Mandatory LE31 skill list for the external coding agent

Before starting, the external coding agent MUST load these skills:

1. **`le31-conventions`** — the global LE31 decision layer + feature gate + hard invariants.
2. **`le31-v1-feature-pattern`** — the canonical contract shape + slicing rules + definition of done.
3. **`le31-handoff-spec`** — the handoff discipline + frozen contract + verification protocol.
4. **`le31-coding-agent-brief`** — the paste-in prompt template that produces the slice prompt from this HANDOFF.
5. **`le31-research`** — the research workflow + evidence-before-recommendation discipline.
6. **`development`** — the generic code-development pipeline (specify → plan → tasks → implement).

## Trigger policy for the external coding agent

- **DO NOT start** until a v2-AI workflow window opens in the LE31 charter roadmap.
- **DO NOT start** until a future v2-AI PR proposes a money-movement surface, an MCP-server adapter for the LE31 API, an integer-money discipline, a verifiable-audit-chain discipline, or a chokepoint-governed-spending-limits-and-approvals discipline.
- **DO NOT start** until the charter §3.6 + §3.3 + §3.4 review has been completed.
- When triggered, mirror back the frozen contract fields (feature ID, decision, bucket, files to touch, verification protocol) before implementing; stop if the mirror-back does not match.

## External-context Linear reference

- Parent research issue: Research 2026-10-19 — daily (Linear MCP BLOCKED 30th consecutive day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-19.linear-fallback.json` documents the intended parent + 3 sub-issues).
- This feature: Feature 344 — devaccuracy/ledgerforge (intended sub-issue in `le31 Research` P-HMM-1).

## Sign-off gap

- External agent has NOT yet been dispatched.
- Charter §3.6 + §3.3 + §3.4 review has NOT yet been completed.
- v2-AI workflow window has NOT yet opened.
- No v1 PR today.
