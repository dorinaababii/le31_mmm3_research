# Feature 304 — `DSHCorrectover-agent-second-fuse-mit-independent-fail-closed-second-fuse-ai-agents-runtime-guard-signed-receipts-append-only-ledger-incident-reports-v2-ai-fail-closed-second-fuse-vocabulary` (defer)

> **NEW observation (2026-10-11).** Documents in-window GitHub repo `DSHCorrectover/agent-second-fuse` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Python, **pushed 2026-10-10T03:34:07Z**, in-window by `pushed_at` only, **created 2026-XX-XX**, **84 KB tiny repo**). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-11): *"Independent fail-closed second fuse for AI agents: runtime guard + signed receipts + append-only ledger + incident reports."* Topics (verbatim, parent-verified): **0 topics listed in API** (sparse topics from the description). Bucket: **v2-AI (fail-closed-second-fuse-vocabulary)** — Pick C of Daily Research 2026-10-11. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports`** quintuple-primitive as a persistent cross-section reference for the LE31 v2-AI *independent-runtime-guard-with-fail-closed-semantics* wedge, and document the **vocabulary validation** that an independent maintainer arrived at in 2026 without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`fail-closed-second-fuse + runtime-guard`** double-primitive: a *second fuse* is an independent runtime guard that runs in parallel with the primary AI guard; if the primary AI guard is bypassed (e.g., by a prompt injection or a misconfigured tool), the second fuse catches the action and **fails-closed** (the action is denied, not silently allowed). The *second fuse* discipline is the **strongest v2-AI independent-runtime-guard vocabulary of the 73-pass series**. This is the §3.4 *non-AI-fallback + human-gate* charter invariant applied to the *AI-agent-action* dimension, where the *non-AI-fallback* is the second fuse (a deterministic rule-based guard that is independent of the AI model).
- A written record of the **`signed-receipts + append-only-ledger + incident-reports`** triple-primitive: every action caught by the second fuse is signed (with a cryptographic signature), recorded in an append-only ledger (no UPDATE or DELETE), and triggers an incident report (a structured report that is sent to the operator). The *signed-receipt* primitive maps 1:1 onto LE31's `audit_logs` schema. The *append-only-ledger* primitive is §3.1-aligned. The *incident-report* primitive maps 1:1 onto any future v1/v2 incident-reporting surface.
- A written record of the **fail-closed-second-fuse** operator-surface-shape: the operator can rely on the second fuse to catch any action that bypasses the primary AI guard; the operator gets an incident report when the second fuse triggers; the operator can review the append-only ledger to understand what happened. Sister-shape to feature 232 (lpalbou/AbstractGateway — durable AI control plane) + feature 287-289 (v2-AI audit-trail vocabulary cluster) + feature 299 (A220man/human-approval-console-ryan-vo — atomic approval receipts) + feature 300 (farooqarahim/glassbox — tamper-evident audit ledger with EU AI Act + MCP) + feature 301 (New1Direction/korg — verifiable cognition for AI agents) + feature 302 (warrant-ai/warrant — decision-ledger with mandate+evidence+cost+outcome+replay-before-ship).
- A decision record: today's verdict is `defer` because (1) the repo is 0★ with single-maintainer cadence (84 KB tiny; could be abandoned); (2) the *fail-closed-second-fuse-vocabulary* is the value, not the code (LE31 v1 has no AI agent; the v2-AI surface is OFF v1 charter); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of the DSHCorrectover codebase (0★ with single-maintainer cadence; 84 KB tiny; no observed production usage).
- Cross-pollination with the v2-AI fail-closed-second-fuse primitive in v1 (LE31 v1 has no AI agent).
- Cross-pollination with the runtime-guard + signed-receipts + incident-reports pattern in v1 (LE31 v1 has no incident-reporting surface).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports primitive" (e.g., a v2 surface that introduces an AI-assisted owner-side workflow like "the owner asks the AI assistant to issue a refund to a supplier; the AI assistant proposes the refund; the second fuse verifies that the supplier is on the real whitelist and that the refund amount is within the daily limit; if either check fails, the refund is denied and the operator gets an incident report"), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same fail-closed-second-fuse framing + the incident-reports primitive"*.

- **Evidence class**: observed (the description names the 5-primitive quintuple set explicitly: `fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports`).
- **Confidence**: medium for the vocabulary match (the verbatim description names the 5-primitive set); low for transferability (LE31 v1 has no AI agent; v2-AI surface is OFF v1 charter; 84 KB tiny repo is the smallest v2-AI pick of the 73-pass series).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI agent); the value is the *fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports* vocabulary — when the first v2 PR that adds a v2-AI surface lands, the DSHCorrectover pattern is a ready-made *named primitive*.

## Description

GitHub `DSHCorrectover/agent-second-fuse` (MIT, 0★/0⑂, Python, pushed 2026-10-10T03:34:07Z, created 2026-XX-XX, 84 KB tiny). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-11): *"Independent fail-closed second fuse for AI agents: runtime guard + signed receipts + append-only ledger + incident reports."*

The architectural primitive has five sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **`Fail-closed second fuse`** — a *second fuse* is an independent runtime guard that runs in parallel with the primary AI guard; if the primary AI guard is bypassed, the second fuse catches the action and **fails-closed** (denies the action rather than allowing it). The *second fuse* discipline is the **strongest v2-AI independent-runtime-guard vocabulary of the 73-pass series**. The *fail-closed* posture means that any ambiguity results in denial (not silent allowance), which is the §3.4 *non-AI-fallback + safe-default* charter invariant applied to the *AI-agent-action* dimension.
2. **`Runtime guard`** — the second fuse is implemented as a runtime guard that runs at the point of action execution (not as a static analysis or a separate audit step). The *runtime-guard* primitive maps 1:1 onto any future v2 surface that needs per-action validation at the moment of action.
3. **`Signed receipts`** — every action caught by the second fuse is signed with a cryptographic signature (so the receipt is tamper-evident). The *signed-receipt* primitive maps 1:1 onto LE31's `audit_logs` schema (which can be extended with a `signature` column for v2-AI surfaces).
4. **`Append-only ledger`** — every signed receipt is stored in an append-only ledger (no UPDATE or DELETE on receipt rows). The *append-only-ledger* primitive is §3.1-aligned.
5. **`Incident reports`** — every signed receipt triggers an incident report (a structured report that is sent to the operator). The *incident-report* primitive maps 1:1 onto any future v1/v2 incident-reporting surface (e.g., a Telegram notification when an action is denied by the second fuse).

**The 1:1 mapping onto LE31 surface:**

| DSHCorrectover primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Fail-closed second fuse | (LE31 v1 has no AI agent, so no second fuse) | v2-AI | **Not implemented** — v2-AI surface |
| Runtime guard | (LE31 v1 has no runtime guard for AI actions) | v2-AI | **Not implemented** — v2-AI surface |
| Signed receipts | `audit_logs` (append-only atomic; can be extended with `signature` column) | §3.1 ✓ | **Implemented (v1, partial)** |
| Append-only ledger | `audit_logs` (append-only atomic) | §3.1 ✓ | **Implemented (v1)** |
| Incident reports | (LE31 v1 has no incident-reporting surface) | v1+v2-AI | **Not implemented** — v1 polish surface |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires fail-closed-second-fuse with runtime-guard + signed-receipts + append-only-ledger + incident-reports semantics), the implementation would add:

1. A `signature` column on the existing `audit_logs` table (Alembic migration) for v2-AI receipts (a str column that stores the cryptographic signature of the receipt payload).
2. A new `IncidentReport` table (Alembic migration) with columns: `id` (UUID), `receipt_id` (UUID FK to `audit_logs`), `denied_action` (str), `denial_reason` (str), `denied_at` (timezone-aware datetime), `notified_operator_at` (timezone-aware datetime nullable), `operator_response` (str nullable).
3. A `second_fuse_rule` table (Alembic migration) with columns: `id` (UUID), `agent_id` (str), `action` (str), `rule` (JSON), `enabled` (bool), `created_at`, `updated_at`.
4. A `second_fuse_decision` table (Alembic migration) with columns: `id` (UUID), `action_id` (str), `decision` (enum: ALLOW / DENY), `reason` (str), `decided_at` (timezone-aware datetime), `signature` (str).
5. A `GET /v2/second-fuse/decisions?agent=<>&action=<>&as_of=<>` search endpoint.
6. A `POST /v2/second-fuse/decide` FastAPI endpoint that records a second-fuse decision.
7. A `POST /v2/incidents` FastAPI endpoint that records an incident report.
8. A `GET /v2/incidents?denied=<>&notified=<>&as_of=<>` query endpoint for incident reports.

The HANDOFF is to evaluate whether the v2-AI surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires:

**For v2-AI fail-closed-second-fuse-vocabulary surface** (if approved):

1. Add a `signature` column on the `audit_logs` table (Alembic migration).
2. Add a new `IncidentReport` SQLModel table (Alembic migration).
3. Add a new `second_fuse_rule` SQLModel table (Alembic migration).
4. Add a new `second_fuse_decision` SQLModel table (Alembic migration).
5. Add a `second_fuse_runtime.py` module that evaluates a rule against an action and returns ALLOW / DENY.
6. Add an `incident_report.py` module that formats a structured incident report.
7. Add a `signature.py` utility module that signs/verifies with ed25519 (sister-shape to feature 302 step 7).
8. Add a `GET /v2/second-fuse/decisions?agent=<>&action=<>&as_of=<>` FastAPI endpoint.
9. Add a `POST /v2/second-fuse/decide` FastAPI endpoint.
10. Add a `POST /v2/incidents` FastAPI endpoint.
11. Add a `GET /v2/incidents?denied=<>&notified=<>&as_of=<>` query endpoint.
12. Add a Telegram notification hook in `backend/app/bot/notifications.py` that sends a Telegram message to the operator when an incident is recorded.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires, the v2-AI surface would add **a v2-AI owner-Telegram-incident-notification primitive** (e.g. the owner gets a Telegram notification when the second fuse denies an action + when the operator responds to the incident). The notification primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram).

## Open questions

- **None today.** The defer artifact is documentation only.

## Why this matters

- **Vocabulary persistence**: the **`fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports`** quintuple-primitive is a **named primitive** that any future LE31 v2-AI surface can reference without re-deriving the concept. The verbatim description names the 5-primitive set.
- **Independent-runtime-guard validation**: the *second-fuse* framing is the **strongest v2-AI independent-runtime-guard vocabulary of the 73-pass series**. The *fail-closed* posture means that any ambiguity results in denial (not silent allowance), which is the §3.4 *non-AI-fallback + safe-default* charter invariant applied to the *AI-agent-action* dimension.
- **Incident-report primitive**: the *incident-report* primitive is a **named primitive** that any future v1/v2 surface can reference. The *incident-report + signed-receipt* pair is the §3.4 *observable-evidence* charter invariant applied to the *AI-agent-action-denied* dimension.
- **Sister-shape to features 232 + 287-289 + 299 + 300 + 301 + 302**: DSHCorrectover/agent-second-fuse is the 8th addition to the persistent v2-AI audit-trail vocabulary cluster (the 73-pass series). The cluster now covers: durable AI control plane (lpalbou/AbstractGateway) + governed beliefs (noise01/endoxa) + MCP CVE-attestation (pete-builds/mcp-nixreview) + Python runtime for financial AI agents (shivamk01here/LedgerLoop) + atomic approval receipts (A220man/human-approval-console-ryan-vo) + EU AI Act + post-quantum (farooqarahim/glassbox) + verifiable cognition (New1Direction/korg) + decision-ledger with mandate+evidence+cost+outcome+replay-before-ship (warrant-ai/warrant) + **fail-closed-second-fuse + runtime-guard + signed-receipts + append-only-ledger + incident-reports (DSHCorrectover/agent-second-fuse)** = the strongest v2-AI audit-trail-decision-incident vocabulary cluster of the 73-pass series.