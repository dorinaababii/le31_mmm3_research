# Feature 351 — `austinchima-elodea-apache-2-0-inline-policy-enforcement-proxy-for-ai-agents-opa-policies-on-mcp-tool-calls-human-approval-for-risky-actions-hash-chained-audit-log-go-v2-ai-policy-chokepoint-vocabulary` (defer)

> **Pick B of Daily Research 2026-10-21.** Documents in-window GitHub repo `austinchima/elodea` (**Apache-2.0 ✓ §3.2 permissive**, **★1/⑂0**, **34898 KB substantial**, **Go — OFF-STACK for LE31 v1** (which is Python 3.13 + FastAPI + SQLModel + Postgres + aiogram v3); the *vocabulary* is portable, the *code-shape* is not adopted, **pushed 2026-10-18T03:52:59Z** = in-window by `pushed_at`, **created 2026-09-18T16:16:40Z** = ~1-month-old repo with in-window push, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-21): *"Inline policy enforcement proxy for AI agents: OPA policies on MCP tool calls, human approval for risky actions, and a hash-chained audit log."* Topics (verbatim, parent-verified, **6 topics**): `agent-security, ai-agents, ai-safety, audit-log, fintech, golang`. Bucket: **v2-AI** (parking-lot, vocabulary reference only). Build verdict: `defer`. **§3.4 posture: chokepoint-governed + human-approval-gated + hash-chained-audit = the canonical LE31 §3.4 non-AI-fallback invariant applied to the MCP-tool-call dimension.**

## Goal

Retain the **inline-policy-enforcement-proxy + OPA-policy-engine + MCP-tool-call-gating + human-approval-for-risky-actions + hash-chained-audit-log** vocabulary as a persistent cross-section reference for the LE31 v2-AI *MCP-tool-call-chokepoint* dimension, documenting the primitive an independent maintainer shipped in 2026. The artifact is a vocabulary reference + a demand signal for a future LE31 v2-AI policy-chokepoint surface. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **OPA-policies-on-MCP-tool-calls + human-approval-for-risky-actions + hash-chained-audit-log** 3-tuple-primitive: an AI agent's tool calls are routed through a policy engine *inline* (not audited after the fact), risky actions require *explicit human approval* before execution, and every gated call is written to a *hash-chained* audit log so the chain is tamper-evident. **The transferable primitive is *the-tool-call-as-the-chokepoint*:** the enforcement point is the tool invocation itself, not the model's reasoning.
- A written record of the *hash-chained-audit-log* posture: this is the strongest §3.3 audit-chain vocabulary of the 82-pass series expressed as a *chokepoint artifact* rather than a *ledger of business events*. Sister-shape to features 187 (`traust-security/traust-ledger` — append-only disposition ledger kernel), 300 (`glassbox` — tamper-evident audit ledger with ed25519/ML-DSA), 273 (`intel-audit` — hash-chain DB-enforced immutability), 334 (`pattern-mcp` — auditable decision ledger). **The distinguishing primitive here is that the chain records *policy decisions about tool calls*, not business facts.**
- A written record of the *human-approval-for-risky-actions* posture: this is the canonical §3.4 *AI may assist owner/staff, with observable evidence and a non-AI fallback* invariant made concrete — a risky action is not performed by the AI at all; it is queued for a human decision. Sister-shape to features 264 (`ai-proposes-deterministic-kernel-checks-human-decides`), 322 (`3-claude-code-agents-dispatcher-closed-loop-human-publish-button`), 306 (`resortflow — hold-then-confirm sagas`), 231 (`particles-standard` — confidence-scored claims).
- A decision record: today's verdict is `defer` because (1) LE31 v1 has **no MCP server surface** and **no AI surface at all** (charter §3.4: no customer-facing AI; AI may assist owner/staff only); (2) the codebase is Go = off-stack; (3) REGO (OPA's policy language) is not LE31-stack; (4) no owner has raised a need for agentic tool-call governance.

**Out of scope:**

- Any adoption of the elodea codebase (Go + OPA/REGO + fintech domain = triple off-stack).
- Any MCP server in LE31 v1.
- Any AI surface of any kind in LE31 v1 (charter §3.4 is not triggered *because there is no AI surface*, not because the policy gate would permit one).
- Any REGO policy authoring surface in LE31.

## Out of scope

- See the explicit out-of-scope list above. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes *"an agent surface where tool calls are policy-gated inline, risky actions require explicit owner approval, and every gated call is recorded in a tamper-evident chain"*, the owner wants *a primitive that proves this chokepoint discipline is buildable and that it does not violate the charter's no-customer-facing-AI rule*, but struggles because *LE31 has no MCP surface and no policy-engine precedent*, so that *the v2-AI surface can be defended with "an independent Apache-2.0 maintainer shipped exactly this OPA + MCP + human-approval + hash-chain posture in 2026"*.

- **Evidence class**: **observed** (the verbatim description names `Inline policy enforcement proxy`, `OPA policies on MCP tool calls`, `human approval for risky actions`, `hash-chained audit log`).
- **Confidence**: **medium-high** for the vocabulary match (all 4 primitives named explicitly in the description); **low** for present urgency (zero owner mentions in 82 passes; LE31 has no AI surface to govern).
- **Real observed LE31 JTBD**: **zero direct JTBD today.** LE31 v1 is FastAPI + aiogram with no LLM call anywhere; there is nothing to policy-gate. The value is *vocabulary for the day LE31 adds its first agent surface*.

## Description

GitHub `austinchima/elodea` (Apache-2.0 ✓ §3.2, ★1/⑂0, 34898 KB substantial, **Go off-stack**, `agent-security + ai-agents + ai-safety + audit-log + fintech + golang`, pushed 2026-10-18T03:52:59Z, created 2026-09-18T16:16:40Z, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-21): *"Inline policy enforcement proxy for AI agents: OPA policies on MCP tool calls, human approval for risky actions, and a hash-chained audit log."*

The architectural primitive has sub-primitives that map onto LE31's charter invariants:

1. **Inline policy enforcement proxy** — the agent does not call tools directly; it calls *through a proxy* that evaluates policy on the way past. This IS the canonical §3.4 *chokepoint-governed* invariant applied to the *tool-invocation* dimension: the enforcement point is not the model's reasoning (unreliable) but the side effect (controllable).
2. **OPA policies on MCP tool calls** — policies are declarative and external to the agent. This IS the canonical §3.1 *rules-as-code* posture, but note it runs *inversely* to how LE31's charter frames rules — see Open questions.
3. **Human approval for risky actions** — the policy can require a human decision before the tool executes. This IS the canonical §3.4 *non-AI-fallback* invariant in its strongest form: the risky action is **not performed by the AI at all**.
4. **Hash-chained audit log** — each gated decision is linked to the previous by a hash, so removal or alteration of any entry is detectable. This IS the canonical §3.3 *audit-chain* invariant applied to the *policy-decision* dimension (rather than the business-event dimension).

The defer artifact retains the **4-tuple-primitive** (inline-policy-proxy + OPA-policy-engine + human-approval-gate + hash-chained-audit-log) as a persistent cross-section reference.

## Data model

N/A (defer artifact; vocabulary-only; no schema today).

When the first v2-AI agent-surface PR adopts this discipline, the shape is:

```sql
-- A tool call is a first-class, policy-gated record (NOT a log line).
CREATE TABLE agent_tool_call (
    id BIGSERIAL PRIMARY KEY,
    agent_surface TEXT NOT NULL,        -- which LE31 surface proposed the call
    tool_name TEXT NOT NULL,
    tool_args JSONB NOT NULL,
    policy_decision TEXT NOT NULL,      -- 'allow' / 'deny' / 'require_approval'
    policy_rule_id TEXT NOT NULL,       -- FK to the declarative policy definition
    decided_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    executed_at TIMESTAMPTZ             -- NULL until approved + executed
);

-- Human approval is an EXPLICIT state transition (charter §3.1: no silent transitions).
CREATE TABLE agent_tool_call_approval (
    id BIGSERIAL PRIMARY KEY,
    tool_call_id BIGINT NOT NULL REFERENCES agent_tool_call(id),
    approved_by TEXT NOT NULL,          -- the human who decided
    decision TEXT NOT NULL,             -- 'approve' / 'reject'
    decided_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    note TEXT
);

-- The hash chain is APPEND-ONLY (charter §3.1: never update or delete ledger events).
CREATE TABLE agent_policy_audit_chain (
    seq BIGSERIAL PRIMARY KEY,
    tool_call_id BIGINT NOT NULL REFERENCES agent_tool_call(id),
    entry_hash BYTEA NOT NULL,          -- sha256(prev_hash || canonical(entry))
    prev_hash BYTEA NOT NULL,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

**Stock impact**: none. **Money impact**: none. **§3.1 invariants preserved**: `agent_policy_audit_chain` is append-only; `executed_at` is NULL until an explicit approval row exists; there is no code path that executes a `require_approval` call without one.

## Implementation steps

**None today.** The defer artifact is documentation only.

When the first v2-AI agent-surface PR adopts this discipline:

1. Add `AgentToolCall` SQLModel table with `policy_decision` + `policy_rule_id` (declarative, external to the agent).
2. Add `AgentToolCallApproval` SQLModel table (explicit human decision; no implicit default).
3. Add `AgentPolicyAuditChain` SQLModel table (hash-chained; append-only; no update/delete paths).
4. Add a **policy proxy layer** between the agent and the tool executor (the chokepoint) — in Python, a `PolicyProxy` wrapper the agent must call instead of the tool directly.
5. Add `/api/agent-tool-calls` (POST proposal) + `/api/agent-tool-calls/{id}/approval` (POST human decision) FastAPI endpoints.
6. Add cook-bot aiogram v3 `/approvals` + `/approve <call_id>` + `/reject <call_id>` handlers (the human-approval surface).
7. Add unit + integration tests asserting: a `require_approval` call never executes without an approval row; the hash chain verifies; chain entries cannot be updated or deleted.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

When the first v2-AI agent-surface PR adopts this discipline, the cook-bot (aiogram v3) interaction would be:

- `/approvals` — bot lists pending `require_approval` tool calls with their proposed `tool_name` + `tool_args`.
- `/approve <call_id>` — explicit human approval; the tool then executes.
- `/reject <call_id>` — explicit human rejection; the tool never executes; the rejection is recorded in the chain.

**§3.4 note**: the AI proposes; the human disposes; the chain records both. This is the strongest possible reading of the charter §3.4 invariant "AI may assist owner/staff, with observable evidence and a non-AI fallback" — the non-AI fallback here is not a degraded mode, it is the *primary* decision path for risky actions.

## Dependencies

- Python 3.13, FastAPI, SQLModel, Postgres (production) — all already LE31 v1 stack.
- aiogram v3 for the approval surface.
- A declarative policy format. **Note: OPA/REGO itself is off-stack**; if LE31 ever adopts this discipline the realistic substitution is a small Python policy evaluator over a YAML/JSON policy file (e.g. `policy.yaml` with per-tool allow/deny/require-approval rules), which preserves the *external-declarative-policy* primitive without the REGO dependency.
- `hashlib` (stdlib) for the hash chain — **zero new pip dependencies** for a Python implementation.

## Open questions

- **⚠️ Charter §3.1 tension (same tension recorded in feature 137 `natural-language-policies-executable-obligations`):** the *policy-as-input* posture is the **inverse** of LE31's *rules-as-code* posture. Either restrict any future policy-authoring surface to **non-operational** rules (display-only, approval-only) or amend the charter. **Owner decision required before any implementation.**
- **Does LE31 v2-AI ever gain an MCP surface?** Today no — LE31 has no LLM call anywhere. **Decision pending.**
- **Who approves?** The single owner is the only plausible approver, which means the "human approval" gate degenerates to "the owner must click" — is that a real safety property for a single-tenant system, or does it just add friction? This is the same open question that killed several audit-ledger picks earlier in the series (features 129, 230, 231). **Recorded, not resolved.**
- **Is a hash chain the right primitive for a single-tenant system where the owner can read the DB directly?** A hash chain protects against *tampering by someone with DB write access*, which for a single-tenant on-premise system is mostly the owner. The value may be **disclosure** (the owner can prove to themselves what happened) rather than **security**. **Decision pending.**

## Why this matters

This is the strongest **v2-AI policy-chokepoint vocabulary** of the 82-pass series: it is the only in-window repo that combines **all four** primitives in a single description — inline enforcement (not post-hoc audit), a declarative external policy engine, an explicit human-approval gate for risky actions, and a tamper-evident hash chain — and it does so with the human-approval gate stated as a first-class feature rather than an audit artifact.

The `human-approval-for-risky-actions` posture is the single most directly transferable idea in the 82-pass series for the LE31 v2-AI dimension: it makes the charter §3.4 non-AI-fallback invariant *structurally* enforced rather than merely documented. If LE31 ever adds an agent surface, this is the shape that keeps the charter intact without an amendment.

Why it is filed at `defer`: LE31 has no AI surface to govern today, the codebase is Go, and REGO is off-stack. Filing it now costs nothing and means the design question is already answered when the first agent surface is proposed.

Fully reversible: vocabulary-only artifact; deletion has zero runtime impact.