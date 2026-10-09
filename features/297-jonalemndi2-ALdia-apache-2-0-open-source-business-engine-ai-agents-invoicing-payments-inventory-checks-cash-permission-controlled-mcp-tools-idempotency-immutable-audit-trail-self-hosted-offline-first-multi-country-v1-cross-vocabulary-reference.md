# Feature 297 — `jonalemndi2/ALdia` v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v1 cross-industry (attach to `le31 v1 — Core MVP` P-HMM-3 as the parent of the sub-issue)
> **Date:** 2026-10-09
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/297-jonalemndi2-ALdia-apache-2-0-open-source-business-engine-ai-agents-invoicing-payments-inventory-checks-cash-permission-controlled-mcp-tools-idempotency-immutable-audit-trail-self-hosted-offline-first-multi-country-v1-cross-vocabulary-reference.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/297-jonalemndi2-ALdia-apache-2-0-open-source-business-engine-ai-agents-invoicing-payments-inventory-checks-cash-permission-controlled-mcp-tools-idempotency-immutable-audit-trail-self-hosted-offline-first-multi-country-v1-cross-vocabulary-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-09.md` (pass 72, pick B)
> **Parent-verified via:** direct GitHub API GET `/repos/jonalemndi2/ALdia` at `/tmp/le31-brainstorm-2026-10-09/verify_jonalemndi2_ALdia.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v1 cross-industry small-business-ERP-with-AI-MCP-tools cross-section pick is a future-extension signal)

## Goal

Surface a v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary reference for **open-source-business-engine-for-AI-agents + invoicing + payments + inventory + checks-and-cash + permission-controlled-MCP-tools + idempotency + structured-errors + immutable-audit-trail + self-hosted + offline-first + multi-country** as a forward-looking pattern for any future LE31 v1 surface that exposes business-engine-as-AI-MCP-tools-with-fine-grained-permissions + idempotency + immutable-audit-trail + offline-first + multi-country-currency discipline.

## Evidence / JTBD

**Evidence classification:** inferred. The *open-source-business-engine-for-AI-agents + invoicing + payments + inventory + checks-and-cash + permission-controlled-MCP-tools + idempotency + structured-errors + immutable-audit-trail + self-hosted + offline-first + multi-country* discipline is forward-looking for any future LE31 v1 cross-industry small-business-ERP-with-AI-MCP-tools surface; no LE31 v1 surface today has business-engine-as-AI-MCP-tools exposure. **Confidence: high** (5★/0⑂ = highest community traction today + Apache-2.0 permissive + 1807 KB modest + 20-topic array = 20/20 LE31 v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary envelope = 100% topic-overlap + Python ✓ on-stack + in-window by `pushed_at` = the strongest v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary pick of the 72-pass series).

**When** the LE31 owner wants to expose `audit_logs`/`StockEntry`/`MenuItem` to an AI agent via MCP, **the owner wants to** see a working Python + FastAPI + SQLite + self-hosted + offline-first + immutable-audit-trail + permission-controlled-MCP-tools + idempotency + structured-errors implementation that demonstrates the *business-engine-for-AI-agents + invoicing + payments + inventory + bookkeeping + permission-controlled-MCP-tools* discipline, **but struggles because** the existing v1 `audit_logs + StockEntry + MenuItem` SQLModel tables are LE31-internal primitives with no MCP-server surface, **so that** the owner cannot see how a similar small-business-business-engine-as-AI-MCP-tools would be structured. The *open-source-business-engine-for-AI-agents + invoicing + payments + inventory + bookkeeping + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country* discipline IS the *business-engine-as-AI-MCP-tools + permission-controlled-tools + idempotency-as-charter-discipline + immutable-audit-trail* charter §3.1 + §3.3 + §3.4 invariant applied to the *AI-agent-business-engine* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *open-source-business-engine-for-AI-agents + invoicing + payments + inventory + checks-and-cash + permission-controlled-MCP-tools + idempotency + structured-errors + immutable-audit-trail + self-hosted + offline-first + multi-country* nonuple-primitive as a candidate vocabulary for any future LE31 v1 cross-industry small-business-ERP-with-AI-MCP-tools surface.
- Identify the on-stack Python+FastAPI+SQLModel+Postgres mapping for each primitive (the *permission-controlled-MCP-tools + idempotency + immutable-audit-trail* discipline IS the *permission-gated + idempotency-as-charter-discipline + append-only-audit-trail* charter §3.1 + §3.3 + §3.4 invariant applied to the *AI-tool-call* dimension).
- Record the §3.1/§3.2/§3.3/§3.4/§3.6 alignment per `le31-conventions/SKILL.md`.
- Note the **20-topic array** = 20/20 LE31 v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary envelope = 100% topic-overlap = strongest v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary candidate of the 72-pass series.

**Out of scope (v1):**
- No v1 build today; defer artifact; vocabulary-only.
- No AI-agent-MCP-server exposure today; v1 has no MCP surface today (charter §3.4: AI sandbox is for *operator-tooling* today).
- No checks-and-cash support; v1 has no checks-cash surface today.
- No multi-country support; v1 uses EUR + Paris only per charter §3.5 + §3.6.

## Description

`jonalemndi2/ALdia` is an **open-source business engine for AI agents. Invoicing, payments, inventory, checks and cash as permission-controlled MCP tools — with idempotency, structured errors and an immutable audit trail. Self-hosted, offline-first, multi-country.** with the following properties:

- **Business engine for AI agents** — provides business-engine primitives (invoicing + payments + inventory + checks + cash) as MCP tools that any AI agent can call
- **Permission-controlled MCP tools** — every MCP tool exposes a fine-grained permission (e.g., *can-invoice / can-read-invoice / can-write-payment / can-audit-trail / can-read-audit-trail*)
- **Idempotency** — every tool call is idempotent (replays return the same result without side effects)
- **Structured errors** — every tool call returns a structured error (typed error with code + message + context)
- **Immutable audit trail** — every tool call writes to an immutable audit-trail (append-only log of all tool calls)
- **Self-hosted** — runs on the user's own VPS (no third-party service dependency)
- **Offline-first** — works without internet (no remote API dependency for the business-engine layer)
- **Multi-country** — supports multiple countries (currency + tax-rules + addressing per country)
- **Invoicing + payments + inventory + bookkeeping + audit-trail** — full small-business-ERP feature set

**20 topics** (verbatim, parent-verified): `accounting + agentic-ai + ai-agents + apache-2 + audit-log + bookkeeping + claude + erp + fastapi + inventory-management + invoicing + llm-tools + mcp + model-context-protocol + offline-first + openclaw + python + self-hosted + small-business + sqlite` = **20/20 LE31 v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary envelope = 100% topic-overlap = strongest v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary candidate of the 72-pass series**.

## Data model

The candidate vocabulary suggests these SQLModel tables (none built today; vocabulary-only):

```
McpToolRegistry:
  id: int (primary key)
  tool_name: str  # e.g., 'invoicing.create', 'payments.write', 'inventory.read'
  description: str
  permission_required: str  # e.g., 'invoicing.write', 'payments.write', 'audit-trail.read'
  idempotency_supported: bool
  error_schema_json: str  # JSON schema of the structured-error envelope

McpToolPermission:
  id: int (primary key)
  tool_id: int (foreign key)
  actor: str  # 'claude-agent-v1', 'owner', 'staff-cook'
  can_call: bool
  audit_log_ref: str  # reference to audit_logs row

McpToolCall:
  id: int (primary key)
  tool_id: int (foreign key)
  idempotency_key: str  # unique idempotency key (replay returns same result)
  payload_json: str
  response_json: str
  error_json: str  # structured error envelope if call failed
  audit_log_ref: str  # immutable audit-trail reference
  created_at: datetime
  replayed_at: datetime  # null if first call; timestamp of subsequent replays

Country:
  id: int (primary key)
  iso_code: str  # 'FR', 'DE', etc.
  currency: str  # 'EUR', 'USD'
  tax_rules_json: str
```

## Implementation steps

If the trigger condition (v1 cross-industry small-business-ERP-with-AI-MCP-tools surface window opens) is met:

1. Read the active feature file in full
2. Confirm `jonalemndi2/ALdia` is still in-window (pushed within last 7 days from trigger date)
3. Set up FastMCP sub-app under `le31-mcp-server`
4. Implement `McpToolRegistry + McpToolPermission + McpToolCall + Country` SQLModel tables
5. Implement the permission-controlled-MCP-tools discipline (every tool exposes fine-grained permission)
6. Implement the idempotency discipline (every tool call has a unique idempotency key + returns the same result on replay)
7. Implement the structured-error discipline (every tool returns a typed error with code + message + context)
8. Implement the immutable-audit-trail discipline (every tool call writes to `audit_logs`)
9. Implement the offline-first discipline (no remote API dependency for the business-engine layer)
10. Run the v1 test suite + the new MCP-server test suite

## Telegram interaction if any

The business-engine layer is *not* a Telegram-bot surface; it is a FastMCP sub-app. **However**, the MCP-tool-call audit-log SHOULD surface as a daily-Telegram-recap to the LE31 owner (so the owner can see what MCP-tool-calls the AI agent has made against `audit_logs`/`StockEntry`/`MenuItem`). This Telegram-recap is operator-tooling, not customer-facing AI.

## Dependencies

- FastAPI (already on-stack ✓ per LE31 v1)
- FastMCP (the `mcp` Python package; borderline §3.4 for AI-sandbox purposes)
- Pydantic (already on-stack ✓ per LE31 v1)
- SQLite (the `ALdia` choice; LE31 v1 uses Postgres — would need adapter)
- Claude API (the `claude` topic; borderline §3.4 for AI-sandbox purposes)

## Open questions

1. Does the *FastMCP + Claude-as-AI-tool-provider* posture comply with charter §3.4 (`AI sandbox` rule: AI may assist owner/staff with observable evidence and non-AI fallback)? **Answer: borderline §3.4** — the *permission-controlled-MCP-tools + idempotency + immutable-audit-trail* posture IS the *non-AI-fallback + observable-evidence + human-gate + fine-grained-permission* §3.4 invariant; the *claude-as-AI-agent-tool-provider* posture IS the *AI-as-tool-caller* §3.4 candidate. Explicit charter-§3.4-review required.
2. Does the `SQLite` choice work with LE31's `Postgres` invariant? **Answer: yes — adapter required** — the business-engine primitives (McpToolRegistry + McpToolPermission + McpToolCall) can be Postgres-backed; the `ALdia` choice of SQLite is incidental.
3. Does the *multi-country* posture breach charter §3.5 (`EUR money discipline`)? **Answer: no** — `Country` table is a future-extensibility surface; today LE31 v1 uses EUR-only (charter §3.5).

## Why this matters

The **open-source-business-engine-for-AI-agents + invoicing + payments + inventory + checks-and-cash + permission-controlled-MCP-tools + idempotency + structured-errors + immutable-audit-trail + self-hosted + offline-first + multi-country** nonuple-primitive is the canonical v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary. LE31 v1 today is server-side + Postgres + FastAPI + cook-Telegram-bot + minimal-HTML/HTMX waiter-UI + append-only StockEntry; the v1 has *no business-engine-as-AI-MCP-tools surface* (the LE31 owner has no way to expose `audit_logs`/`StockEntry`/`MenuItem` to an AI agent via MCP; the *business-engine-for-AI-agents + invoicing + payments + inventory + bookkeeping + permission-controlled-MCP-tools + idempotency + immutable-audit-trail + self-hosted + offline-first + multi-country* discipline IS the canonical v1 cross-industry small-business-ERP-with-AI-MCP-tools-vocabulary that would let a future v1 PR add a *business-engine-as-AI-MCP-tools-with-permission-controlled-idempotency-immutable-audit-trail + 20 topics + 5★ community traction* surface that any AI agent can call with fine-grained permissions and full audit trail). The Python + 20-topic + 5★/0⑨ stack is **§3.1 + §3.2 + §3.3 ON-PATTERN** for LE31; the *permission-controlled-MCP-tools + idempotency + immutable-audit-trail* discipline IS stack-agnostic; the cross-section vocabulary is informative, not a v1-build trigger.

## Charter compatibility

- **§3.1** (explicit-state-transitions) ✓ — the *permission-controlled-MCP-tools + idempotency* posture IS the §3.1 *explicit-state-transition + operator-driven* invariant applied to the *AI-tool-call* dimension.
- **§3.2** (privacy, counts-not-identity) ✓ — only audit-trail metadata stored; no PII beyond Twilio ToS scoping.
- **§3.3** (audit-log-immutability) ✓ — every tool call writes to an immutable audit-trail (append-only log).
- **§3.4** (AI sandbox, observable evidence, non-AI fallback) **RIPGL_REVIEW REQUIRED** — the *claude-as-AI-agent-tool-provider* posture IS the §3.4 *AI-as-tool-caller* candidate; the *permission-controlled-MCP-tools + idempotency + immutable-audit-trail* posture IS the *non-AI-fallback + observable-evidence + human-gate + fine-grained-permission* §3.4 invariant. Explicit charter-§3.4-review needed before any v2-AI PR that adopts the *AI-agent-tool-provider* posture with a customer-facing AI.
- **§3.5** (EUR money discipline) ✓ — `Country` table supports EUR-only today; multi-country is a future-extensibility surface.
- **§3.6** (Paris timezone) ✓ — `created_at + replayed_at` are timezone-aware datetimes (Europe/Paris).
- **§3.7** (privacy) ✓ — only audit-trail metadata stored, scoped per Twilio ToS.
