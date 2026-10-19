# Feature 344 — devaccuracy/ledgerforge (v2-AI AI-native-money-movement-double-entry-ledger-with-exact-integer-money-+-verifiable-audit-chain-+-server-enforced-spending-limits-+-approvals-for-AI-agents-+-MCP-server-vocabulary)

> **Bucket**: v2-AI (parking-lot, vocabulary reference)
> **GitHub**: https://github.com/devaccuracy/ledgerforge
> **License**: Apache-2.0
> **Status (as of 2026-10-19)**: ★411 / ⑂42; 3962 KB modest; pushed 2026-10-16T (in-window); created 2026-05-10T (~5-month-old repo with in-window push); default_branch=main; archived=False
> **Topics (verbatim, 7)**: `ai-tools, billing, double-entry-accounting, fintech, ledger, payout, wallet` = 0/7 LE31-stack-match (Go off-stack; the *vocabulary* is portable to Python+FastAPI+Postgres+SQLModel+aiogram v3)
> **Description (verbatim)**: *The ledger for AI-native money movement. An open-source double-entry ledger for wallets, payouts, marketplaces and billing, with exact integer money, a verifiable audit chain, server-enforced spending limits and approvals for AI agents, and an MCP server. Apache 2.0.*
> **Cross-section**: features 187/188 (traust-security/traust-ledger, the persistent v2-AI audit-ledger vocabulary cluster), 232 (lpalbou/AbstractGateway, replay-first), 268 (sattyamjjain/agent-audit-kit, MCP-scanner), 287-289 (append-only + SMT), 296-297 (yadun-arul-segments/dispatch + yevheniidehtiar/hyper-admin), 299-310 (A220man + farooqarahim + New1Direction + IanWells + t0mer + nikmcfly + sr-857 + nextops + ssi-anik + ilcwd + refactorium + SherlocksLead + the-vibey-project cluster), 327 (musterhq/muster agent-harness-with-audit-ledger), 332/333/334 (vsov/xcheck + FlashyLabs/flashy-ledger + donaldrichard19-LVD/pattern-mcp), 335 (tangwenhai839/create-qingyu append-only-memory-gateway), 338/339/340 (agentdrover/haiplane + vggg/barony + BUGGIEEEEE/worklog) = 24-pick v2-AI agent-money-movement-+-audit-ledger-+-MCP-server + agent-governance cluster of the 80-pass series
> **Decision**: defer (parking-lot, vocabulary reference)
> **Parent research issue**: Research 2026-10-19 — daily (Linear MCP blocked 30th-consecutive-day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-19.linear-fallback.json`)
> **Slice handoff**: `/opt/data/le31_mmm3_research_work/specs/344-devaccuracy-ledgerforge-v2-ai-ai-native-money-movement-double-entry-ledger-exact-integer-money-verifiable-audit-chain-server-enforced-spending-limits-approvals-for-ai-agents-mcp-server-vocab-HANDOFF.md`

## Goal

When a future v2-AI LE31 workflow needs to handle money movement (e.g. supplier payments, owner cash-out, customer refunds, AI-assisted expense approval), the system wants every money amount to be **exact integer** (charter §3.6), every state transition to be **verifiable in an audit chain** (charter §3.3), every spending to be **server-enforced with spending limits and approvals** (charter §3.4 chokepoint-governed), and the API to be **exposed as an MCP server** (portable to v2-AI agent surfaces), but today's LE31 v1 has no money-movement surface; the v1 only handles EUR receipt recording + tip reconciliation + payment-processor payouts, not AI-agent money movement.

## Evidence / JTBD

**Inferred** (vocabulary observation, not observed LE31 user pain). The pain is *possible* in any future v2-AI money-movement workflow window but is not *directly observed* in any LE31 v1 user flow today.

When a v2-AI workflow needs to handle money (Pick A), the operator wants every money amount to be **exact integer** + every state transition to be **verifiable in an audit chain** + every spending to be **server-enforced with spending limits and approvals** + the API to be **exposed as an MCP server**, but struggles because today LE31 v1 has no money-movement surface (the v1 only handles EUR receipt recording via the payment-processor payout reconciliation feature 05, not AI-agent money movement).

Confidence: **high** (★411 + 42 forks + 5-month-old repo + 7-topic alignment = strong adoption signal for the *integer-minor-units + append-only-audit-chain + chokepoint-governed + MCP-server* quartet; the Go language is off-stack but the vocabulary IS portable).

## Scope

- v2-AI only: applies to a future v2-AI money-movement workflow window (operator + staff tooling, not customer-facing).
- The transferable vocabulary is the **integer-money + audit-chain + chokepoint + MCP-server** quartet:
  1. **Integer-money discipline** (charter §3.6) — every money amount is an exact integer minor unit (no float).
  2. **Append-only-audit-chain discipline** (charter §3.3) — every state transition is recorded in a verifiable audit chain (the chain is hash-chained so any tampering is detectable).
  3. **Chokepoint-governed-spending-limits-and-approvals discipline** (charter §3.4) — every spending is gated by server-enforced spending limits + human approval for AI agents.
  4. **MCP-server-as-tool-API discipline** (charter §3.4) — the API is exposed as an MCP server (Model Context Protocol) so AI agents (Claude Code, Codex, etc.) can discover and consume the API through the standard MCP protocol.
- The Go language is off-stack; the *vocabulary* is portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 with a charter §3.6 + §3.3 + §3.4 review.
- No v1 PR today; no v1 build today; no quota-filling.

## Out of scope

- v1 product surface (waiter web UI + cook Telegram bot). LE31 v1 has no money-movement surface (the v1 only handles EUR receipt recording + tip reconciliation + payment-processor payouts, not AI-agent money movement).
- Any customer-facing AI per charter §3.4 (the ledgerforge vocabulary is operator-tooling only).
- Any runtime import of ledgerforge as a dependency (the ledgerforge codebase is the vocabulary reference, not the code dependency).
- Any LE31-specific schema migration or model change (ledgerforge is vocabulary-only; the v2-AI surface is greenfield).
- Money-float-precision is explicitly OUT per charter §3.6 (no binary floats for money; the ledgerforge vocabulary IS the exact-integer-money discipline).

## Description

The ledgerforge vocabulary is the **AI-native-money-movement-double-entry-ledger** quintuple-primitive:

1. **Double-entry-accounting discipline** — every money movement is recorded as a debit on one account and a credit on another; the books always balance. This is the **double-entry-as-implicit-invariant** discipline applied to AI-agent money movement.
2. **Exact-integer-money discipline** — every money amount is an exact integer minor unit (no float). This is the **integer-minor-units-as-money-discipline** applied to AI-agent money movement (charter §3.6).
3. **Verifiable-audit-chain discipline** — every state transition is recorded in a verifiable audit chain; the chain is hash-chained so any tampering is detectable. This is the **append-only-audit-evidence** discipline applied to AI-agent money movement (charter §3.3).
4. **Server-enforced-spending-limits-and-approvals discipline** — every spending is gated by server-enforced spending limits + human approval for AI agents. This is the **chokepoint-governed + human-gate** discipline applied to AI-agent money movement (charter §3.4).
5. **MCP-server-as-tool-API discipline** — the API is exposed as an MCP server (Model Context Protocol) so AI agents (Claude Code, Codex, etc.) can discover and consume the API through the standard MCP protocol. This is the **MCP-server-as-tool-API** discipline applied to AI-agent money movement.

The Go + Apache-2.0 + 7-topic + ★411 + 42-fork + 5-month-old stack is the **highest-star in-window v2-AI agent-money-movement-vocabulary of the 80-pass series**. Charter §3.3 (audit-chain) + §3.4 (chokepoint-governed) + §3.6 (integer-minor-units) are ALL touched by this single pick.

## Data model

The ledgerforge data model is **greenfield** (no v1 file is touched by this slice). The conceptual model is:

```
Account          (id, name, currency, balance_minor_units)        -- balance derived from entries
MoneyEntry       (id, account_id, debit_minor_units, credit_minor_units,
                  audit_chain_hash, created_at)                   -- append-only per charter §3.3
SpendingLimit    (id, account_id, max_minor_units_per_period,
                  period_seconds, requires_approval_above_minor_units)
ApprovalRequest  (id, money_entry_id, requested_by_agent,
                  status, approved_by, approved_at)                -- human-gate per charter §3.4
```

The `balance_minor_units` on `Account` is **derived** from `MoneyEntry` rows per the *balances always derived* AAO-Stack rule (FlashyLabs/flashy-ledger feature 333). The `audit_chain_hash` on `MoneyEntry` is the hash of the previous `MoneyEntry.audit_chain_hash` + the new entry's contents (Merkle-linked append-only chain).

## Implementation

Not implemented today. When a v2-AI window opens, the implementation will touch:

- `app/v2/ai/money/__init__.py` — new package
- `app/v2/ai/money/models.py` — `Account` + `MoneyEntry` (append-only per charter §3.3) + `SpendingLimit` + `ApprovalRequest` SQLModel tables
- `app/v2/ai/money/ledger.py` — `record_money_entry` + `verify_audit_chain` + `enforce_spending_limit` business logic
- `app/v2/ai/money/router.py` — FastAPI router under `/v2/ai/money` with CRUD endpoints + MCP-server adapter
- `app/v2/ai/money/templates/` — HTMX templates for the operator-facing account/entry/approval UI
- `app/v2/ai/money/tests/` — verify the double-entry invariant (debit == credit) + verify the audit-chain integrity (hash-chained) + verify the spending-limit enforcement
- `migrations/` — alembic migration for the new tables

> **Greenfield**: no existing v1 files are touched by this slice (LE31 v1 has no money-movement surface; the v1 only handles EUR receipt recording via the payment-processor payout reconciliation feature 05, which is a different concern).

## Telegram interaction

Not implemented today. When a v2-AI window opens, the Telegram interaction will be:

- The cook Telegram bot (LE31 v1) is **unchanged** by this slice (this slice is v2-AI only).
- The v2-AI surface will use the **AI-agent → MCP-server → ledgerforge-API** flow: the AI agent calls the MCP-server endpoint, the server enforces the spending limit + audit chain, the server returns the result.
- The owner-facing surface (when built) will be a separate Telegram bot for **approval requests**: when a `SpendingLimit` is exceeded, the bot sends an approval request to the owner; the owner replies `/approve <request_id>` or `/deny <request_id>`; the bot records the decision in the `ApprovalRequest` table (append-only).

## Dependencies

- [05-payment-tip-reconciliation.md](05-payment-tip-reconciliation.md) — the v1 EUR-receipt + tip + payment-processor-payout surface; the v2-AI money-movement surface is a **supersurface** that subsumes the v1 EUR-receipt surface for the v2-AI workflow.
- [20-spending-limits.md](20-spending-limits.md) (if it exists) — the v1 spending-limit surface (TBD; this slice assumes a v1 spending-limit surface exists or is built first).
- External: **MCP-runtime** (Model Context Protocol runtime) for the AI-agent → MCP-server flow.
- Cross-section: features 187/188 (traust-security/traust-ledger, the persistent v2-AI audit-ledger vocabulary cluster), 232 (lpalbou/AbstractGateway, replay-first), 333 (FlashyLabs/flashy-ledger, the AAO-Stack ledger rules) — the *integer-minor-units + append-only + hash-chained + idempotent-writes + balances-always-derived* sextuple-primitive from feature 333 is the canonical v2-AI append-only-hash-chained-ledger-rules-vocabulary of the 80-pass series; the *double-entry + integer-money + audit-chain + chokepoint + MCP-server* quintuple-primitive from feature 344 IS the canonical v2-AI agent-money-movement-vocabulary of the 80-pass series; together they form the canonical v2-AI money-movement + audit-ledger cluster of the 80-pass series.

## Open questions

- Does the owner need to approve every AI-agent money movement, or only those above the spending limit? (charter §3.4 human-gate interpretation.)
- Does the v1 EUR-receipt surface (feature 05) need to be migrated to the v2-AI money-movement surface, or can the two surfaces coexist? (charter §3.1 + §3.2 + §3.6 review needed.)
- Does the v1 SQLModel Decimal-based money representation need to be migrated to the v2-AI integer-based money representation? (charter §3.6 review needed; the v1 uses Decimal which IS NOT the v2-AI integer discipline; a migration would be a breaking change.)

## Why this matters

The ledgerforge vocabulary is the **canonical v2-AI agent-money-movement-vocabulary reference of the 80-pass series**. The *integer-money + audit-chain + chokepoint + MCP-server* quartet IS the strongest v2-AI agent-money-movement-vocabulary of the 80-pass series (★411 = highest-star in-window pick; 7-topic alignment with `double-entry-accounting + ledger + payout + wallet + billing + ai-tools + fintech`; 42 forks; 5-month-old repo with in-window push = active maintainer). Charter §3.3 (audit-chain) + §3.4 (chokepoint-governed) + §3.6 (integer-minor-units) are ALL touched by this single pick. The Go language is off-stack but the vocabulary IS portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 with a charter review. When a v2-AI window opens, this vocabulary becomes the canonical reference for any LE31 v2-AI agent-money-movement surface.
