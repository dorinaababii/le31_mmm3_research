# Feature 299 — `A220man-human-approval-console-ryan-vo-mit-review-ai-agent-actions-atomic-approval-receipts-search-receipt-ledger-verify-hash-chain-export-audit-evidence-python-fastapi-v2-ai-approval-receipt-vocabulary` (defer)

> **NEW observation (2026-10-10).** Documents in-window GitHub repo `A220man/human-approval-console-ryan-vo` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **2★/0⑂**, Python + FastAPI + React + TypeScript, **pushed 2026-10-09T18:09:40Z**, in-window by `pushed_at` only, **created 2026-10-07T16:15:10Z** — 3-day-old repo with first in-window push, **155 KB modest repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-10): *"Ryan Vo | Review AI agent actions with atomic approval receipts, search the receipt ledger, verify its complete hash chain, and export audit evidence."* Topics (verbatim, parent-verified): `agent-evaluation, ai, ai-agents, artificial-intelligence, fastapi, llm, machine-learning, python, react, typescript` — 10 topics including **`fastapi` + `python`** (LE31 backend stack match) + **`agent-evaluation` + `ai-agents` + `llm`** (LE31 v2-AI domain match) + **`react` + `typescript`** (off-LE31-frontend-stack but the backend is on-stack). Bucket: **v2-AI (approval-receipt-vocabulary)** — Pick A of Daily Research 2026-10-10. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`atomic approval receipts + search the receipt ledger + verify its complete hash chain + export audit evidence`** quadruple-primitive as a persistent cross-section reference for the LE31 v2-AI *operator-approval of AI-agent actions with hash-chained-audit-trail + search + verify + export* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (3-day-old repo with first in-window push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`atomic approval receipts + search the receipt ledger + verify its complete hash chain + export audit evidence`** quadruple-primitive: every AI-agent action is wrapped in an atomic approval-receipt primitive; the receipt-ledger is searchable; the hash-chain is verifiable; the audit-evidence can be exported. This is the §3.1 explicit-state-transitions primitive applied to AI-agent actions with operator-approval as the gate + hash-chained-audit-trail as the record.
- A written record of the **`Python + FastAPI + React + TypeScript`** stack-shape: this is **2 of 4 LE31 backend stack primitives** matched (Python + FastAPI is on-stack; React + TypeScript is the off-LE31-frontend-stack but is the standard 2026 React-app pattern); the **Python + FastAPI backend** is the LE31-stack-match primitive.
- A written record of the **`operator-approval-of-AI-agent-actions`** operator-surface-shape: every AI-agent action requires an explicit operator-approval before the action is executed; the approval is recorded as an atomic receipt; the receipt is hash-chained; the chain is searchable + verifiable + exportable. Sister-shape to feature 232 (lpalbou/AbstractGateway — durable AI control plane) + feature 287 (noise01/endoxa — governed beliefs for LLM agents) + feature 288 (pete-builds/mcp-nixreview — advisory NixOS change-review with CVE attestation gate for AI agents) + feature 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents with idempotent exactly-once execution).
- A decision record: today's verdict is `defer` because (1) the repo is 2★ with single-maintainer cadence (3-day-old, first in-window push); (2) the stack-shape match is the value, not the code (LE31 v1 has no AI agent; the v2-AI surface is OFF v1 charter); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the A220man codebase (3-day-old single-maintainer repo with no observed production usage).
- Cross-pollination with the v2-AI approval primitive in v1 (LE31 v1 has no AI agent).
- Cross-pollination with the React + TypeScript frontend (LE31 uses HTMX + minimal HTML, not React).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the operator-approval of AI-agent actions with atomic approval receipts + search + verify + export audit evidence primitive" (e.g., a v2 surface that introduces an AI-assisted owner-side workflow like "the owner asks the AI assistant to add a new menu item, the AI assistant proposes a draft, the owner approves the draft with an atomic approval-receipt, the receipt is recorded in the audit-log + the chain is searchable + verifiable + exportable"), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "operator-approval-of-AI-agent-actions with atomic approval-receipts + hash-chained-audit-trail + search + verify + export" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same stack as LE31"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly: `agent-evaluation, ai, ai-agents, fastapi, python, react, typescript, llm, machine-learning`).
- **Confidence**: medium-high for the vocabulary match (the verbatim description names the 4-primitive set + the tech-stack); low for transferability (LE31 v1 has no AI agent; v2-AI surface is OFF v1 charter).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI agent); the value is the *operator-approval-of-AI-agent-actions + atomic-approval-receipts + hash-chained-audit-trail + search + verify + export* vocabulary — when the first v2 PR that adds a v2-AI surface lands, the A220man pattern is a ready-made *named primitive*.

## Description

GitHub `A220man/human-approval-console-ryan-vo` (MIT, 2★/0⑂, Python + FastAPI + React + TypeScript, pushed 2026-10-09T18:09:40Z, created 2026-10-07T16:15:10Z, 155 KB). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-10): *"Ryan Vo | Review AI agent actions with atomic approval receipts, search the receipt ledger, verify its complete hash chain, and export audit evidence."*

The architectural primitive has four sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **`Atomic approval receipts`** — every AI-agent action requires an explicit operator-approval; the approval is recorded as an atomic receipt (the receipt is either created or not, as a single transaction). The *atomic-receipt* primitive maps 1:1 onto LE31's `audit_logs` schema (which already implements atomic-append-only insertion).
2. **`Search the receipt ledger`** — every receipt is searchable by operator / agent / action / timestamp. The *search* primitive maps 1:1 onto any future v2 surface that needs a `GET /v2/audit-logs?operator=<>&agent=<>&action=<>&as_of=<>` query.
3. **`Verify its complete hash chain`** — every receipt is hash-chained; the chain is verifiable from the genesis block to the latest receipt. The *hash-chain-verify* primitive maps 1:1 onto LE31's append-only discipline (§3.1).
4. **`Export audit evidence`** — the chain can be exported as an audit-evidence package (e.g. for an external auditor or regulator). The *export-audit-evidence* primitive maps 1:1 onto any future v2 surface that needs `GET /v2/audit-logs/export?format=<>&as_of=<>` for an accountant or regulator.

**The 1:1 mapping onto LE31 surface:**

| A220man primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Atomic approval receipts | `audit_logs` (append-only atomic) | §3.1 ✓ | **Implemented (v1)** |
| Search the receipt ledger | (LE31 v1 has no search UI) | v1 polish | **Not implemented** — v1 polish surface |
| Verify its complete hash chain | `audit_logs` (append-only hash-chained) | §3.1 ✓ | **Implemented (v1, partial)** |
| Export audit evidence | (LE31 v1 has no export endpoint) | v1 polish | **Not implemented** — v1 polish surface |
| Python + FastAPI | Python + FastAPI + SQLModel | §3.1 ✓ | **Implemented (v1)** |
| React + TypeScript | (LE31 v1 uses HTMX + minimal HTML) | off-stack | **Not implemented** — different frontend |
| AI agent | (LE31 v1 has no AI agent) | v2-AI | **Not implemented** — v2-AI surface |
| operator-approval gate | (LE31 v1 has explicit user actions but no AI-approval gate) | v1+v2-AI | **Not implemented** — v2-AI surface |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires operator-approval-of-AI-agent-actions with hash-chained-audit-trail), the implementation would add:

1. A new `ApprovalReceipt` table (Alembic migration) with columns: `id` (UUID), `agent_id` (str), `action` (str), `proposed_payload` (JSON), `operator_user_id` (UUID FK), `approved_at` (timezone-aware datetime), `previous_receipt_hash` (str), `this_receipt_hash` (str).
2. A `ai_agents` table (Alembic migration) with columns: `id` (UUID), `name` (str), `description` (str), `allowed_actions` (JSON), `created_at`, `updated_at`.
3. An `INSERT ... ON CONFLICT DO NOTHING` guard on the `ApprovalReceipt` insert path (for the *atomic-receipt* primitive).
4. A `GET /v2/audit-logs/receipts?operator=<>&agent=<>&action=<>&as_of=<>` search endpoint.
5. A `GET /v2/audit-logs/receipts/verify` hash-chain-verify endpoint.
6. A `GET /v2/audit-logs/receipts/export?format=<>&as_of=<>` audit-evidence-export endpoint.

The HANDOFF is to evaluate whether the v2-AI surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires:

**For v2-AI approval-receipt-vocabulary surface** (if approved):

1. Add a new `ApprovalReceipt` SQLModel table (Alembic migration).
2. Add a new `ai_agents` SQLModel table (Alembic migration).
3. Add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `ApprovalReceipt` insert path.
4. Add a `GET /v2/audit-logs/receipts/search` FastAPI endpoint with the operator/agent/action/as_of query parameters.
5. Add a `GET /v2/audit-logs/receipts/verify` FastAPI endpoint that walks the hash chain from genesis to the latest receipt and verifies each `this_receipt_hash == SHA-256(previous_receipt_hash + receipt_payload)`.
6. Add a `GET /v2/audit-logs/receipts/export?format=json|csv` FastAPI endpoint that exports the chain as a downloadable file.
7. Add a `POST /v2/agents/<agent_id>/actions/propose` FastAPI endpoint that records a proposed AI-agent action as a pending receipt.
8. Add a `POST /v2/agents/<agent_id>/actions/<action_id>/approve` FastAPI endpoint that records the operator-approval and atomically transitions the receipt from `pending` to `approved`.
9. Add a `POST /v2/agents/<agent_id>/actions/<action_id>/reject` FastAPI endpoint that records the operator-rejection and atomically transitions the receipt from `pending` to `rejected`.
10. Add a `GET /v2/audit-logs/receipts?status=pending|approved|rejected` query endpoint for the operator UI.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires, the v2-AI surface would add **a v2-AI owner-Telegram-notification primitive** (e.g. the owner gets a Telegram notification when an AI-agent action is proposed + when it is approved/rejected). The notification primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; matches A220man's Python + FastAPI backend).
- **External**: None (the receipt primitive is local to the LE31 instance; no external API).
- **Internal**: §3.1 (append-only discipline for `audit_logs`); §3.2 (MIT permissive license compatible); §3.4 (operator-tooling only, no customer-facing AI).
- **Trigger dependency**: future v2 PR that adds a v2-AI surface that requires operator-approval of AI-agent actions.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a v2-AI surface? The v1 charter explicitly excludes customer-facing AI (§3.4); v2-AI is OFF v1 charter but the §3.4 owner/staff-assist allowance leaves the door open for v2.
- **Q2**: If v2-AI lands, will it require the operator-approval primitive? The A220man pattern assumes a *propose-approve-execute* lifecycle, but LE31 v1's explicit-state-transitions primitive (§3.1) is already a *propose-execute* primitive. The *approve* step is the new addition.
- **Q3**: Will the receipt primitive be §3.1-compliant if the *approve* step is missing? Today, LE31 v1's `audit_logs` already records every state transition; the A220man pattern is a richer *approve-then-record* primitive.
- **Q4**: How will the *export audit evidence* primitive interact with the v1 `audit_logs` schema? The v1 schema is append-only + hash-chained; the *export* primitive is a read-only operation that serializes the chain to JSON or CSV.

## Why this matters

The **`atomic approval receipts + search the receipt ledger + verify its complete hash chain + export audit evidence`** quadruple-primitive is the **strongest direct LE31 v2-AI approval-receipt-vocabulary reference of the 72-pass series** for three reasons:

1. **The 4-primitive vocabulary is the future v2-AI surface primitive**: when LE31 v2 introduces an AI-assisted owner-side workflow (e.g. an AI assistant that proposes draft menu items, draft supplier orders, draft daily recaps), the operator-approval primitive is the gate that satisfies §3.1 + §3.4. The A220man pattern is a ready-made *named primitive* for this gate.

2. **The Python + FastAPI on-stack match is the strongest of the 72-pass series**: A220man's backend is Python + FastAPI (LE31 stack match), and the React + TypeScript frontend is the standard 2026 React-app pattern (off-LE31-frontend but the on-LE31-stack is the value).

3. **The 3-day-old repo with first in-window push is the demand signal**: the maintainer is iterating fast (3-day-old repo with first in-window push today) without reading the LE31 charter. The demand for the *operator-approval-of-AI-agent-actions* primitive is real, observable, and growing.

Sister-shape to features 187 + 188 (traust-ledger — append-only disposition ledger) + 232 (lpalbou/AbstractGateway — durable AI control plane) + 287 (noise01/endoxa — governed beliefs for LLM agents) + 288 (pete-builds/mcp-nixreview — advisory NixOS change-review with CVE attestation gate for AI agents) + 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents with idempotent exactly-once execution). The A220man pattern is the **strongest direct operator-approval primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v2 PR that adds a v2-AI surface that requires operator-approval of AI-agent actions with a hash-chained-audit-trail.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/142-feldroy-air-fastapi-htmx-ai-write-framework.md` — carry-over FastAPI + HTMX + Pydantic reference
- `features/187-traust-security-traust-ledger-apache-2-0-append-only-disposition-ledger-kernel-security-auditing-workflows-v2-owner-pains-architecture-reference.md` — carry-over append-only disposition ledger
- `features/188-traust-security-traust-ledger-apache-2-0-append-only-disposition-ledger-v2-architecture-reference.md` — sister-shape
- `features/199-karusrus-transparency-kit-noassertion-eu-ai-act-article-50-audit-log-hash-chained-ledger-human-gate-slack-v2-ai-compliance-primitive.md` — EU AI Act Article 50 + audit-log + hash-chained-ledger + human-gate
- `features/232-lpalbou-AbstractGateway-mit-replay-first-durable-ai-control-plane-http-telegram-persistence-append-only-ledger-v2-ai-durable-control-plane.md` — durable AI control plane
- `features/236-shawn-durrani-membro-mit-local-first-memory-ai-assistants-append-only-fact-ledger-deterministic-extraction-walls-immutable-transcripts-provenance-v2-ai-local-first-ai-assistant-memory.md` — local-first AI assistant memory
- `features/266-ierg-lab-ergon-mcp-server-ai-agent-tools-workspace-context-mcp-secure-tool-execution-apache-2-0-v2-ai-mcp-server-vocabulary.md` — MCP server for AI agents
- `features/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary.md` — governed beliefs for LLM agents
- `features/288-pete-builds-mcp-nixreview-mit-advisory-nixos-change-review-cve-kev-attestation-gate-ai-agents-mcp-server-v2-ai-mcp-change-review-vocabulary.md` — advisory NixOS change-review with CVE attestation gate for AI agents
- `features/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-execution-hash-chained-ledger-v2-ai-exactly-once-execution-vocabulary.md` — Python runtime for financial AI agents with idempotent exactly-once execution
- `features/291-Volcarone-badcop-mit-chase-unpaid-invoices-with-escalating-reminder-ladder-accounts-identity-csv-in-email-out-zero-dependencies-self-stay-good-cop-v1-owner-supplier-payment-chasing-vocab.md` — v1 owner-supplier-payment-chasing-vocabulary
- `features/298-erhatechnologiesai-point-of-sale-system-mit-cloud-point-of-sale-pos-touchscreen-cashier-register-mock-payments-automated-receipt-generation-customer-loyalty-rewards-v1-small-shop-pos-vocabulary-reference.md` — v1 small-shop POS vocabulary reference
