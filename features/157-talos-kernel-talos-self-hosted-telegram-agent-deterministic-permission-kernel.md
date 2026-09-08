# Feature 157 — Talos self-hosted Telegram+terminal agent deterministic-permission-kernel (defer)

> **NEW observation (2026-09-08).** Documents in-window GitHub repo `talos-kernel/talos` (**MIT, 9★/1⑂, Python, pushed 2026-09-08T06:47:50Z**, in-window by push only, 7.6 KB description). Description (verbatim): *"Self-hosted AI agent for terminal and Telegram, with Claude/Codex workers, live activity and a deterministic permission kernel."* Topics include `ai-agent, ai-security, autonomous-agents, capability-security, claude, codex, llm, local-first, mcp, ollama, permission-system, python, redteam, sandbox, security, self-hosted, telegram-bot`. **The highest-stars net-new in-window Python repo in the 41-pass brainstorm series. First surface of this repo in the 41-pass series** (parent-verified by ripgrep against all features 1–155 + all brainstorm reports 2026-08-04..2026-09-08). Bucket: **v2 owner-pains (operator-architecture reference, parking-lot defer)** — watch-list entry, zero build time today.

## Goal

Retain the **"deterministic permission kernel"** primitive as a persistent cross-section reference for any future LE31 v2 surface that adds an *AI-assisted operator* layer where every AI tool call is gated by an explicit permission check and every permission check is itself an audit log entry. The artifact is the persistent architectural vocabulary + the *self-hosted + local-first + privacy-friendly* cluster as a *named* surface discipline. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the Talos primitive: *deterministic permission kernel* + *self-hosted + local-first* + *live activity* + *Telegram + terminal agent*.
- A written record of the *permission-ledger-as-audit-log* discipline: every AI tool call is gated by an explicit permission check; every permission check is itself an audit log entry. This is the **architectural twin of LE31 charter §3.1 (explicit operational transitions)** applied to AI-agent tool calls.
- A cross-section reference with features 92 (AI-agent-decision-ledger cluster-watch) / 134 (ECHO auditable-memory-plane) / 137 (NL-to-Executable-Obligations) / 149 (personal-agent-blueprint Telegram chokepoint) / 150 (Mandato protocol-level digitally-signed mandates) — the *transferable insight* is the *permission-ledger-as-audit-log* discipline.
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-agent surface today (charter §3.4 forbids customer-facing AI; v1 has no AI at all). The Talos primitive is a v2 operator-architecture reference, not a v1 build implication.

**Out of scope (defer artifact):**
- Any change to the cook Telegram bot's authorization flow.
- Any change to the `audit_logs` schema.
- Any addition of an *AI-assisted operator* surface in v1 (charter §3.4).
- Any change to the *no-cloud-no-AI* posture in v1 (charter §3.1 + §3.4).
- Adoption of the Talos code (the surface discipline is the value, not the code).

## Evidence / JTBD

When a future LE31 v2 owner wants to introduce an *AI-assisted operator* layer where the AI helps the cook or owner with routine tasks (e.g., auto-suggesting `StockEntry` writes from natural-language input), the owner wants *every AI tool call to be gated by an explicit permission check and every permission check to be recorded as an audit log entry*, but struggles because *v1 has no AI agent and no permission kernel*, so that *v2 can offer an AI-assisted operator surface without re-architecting v1*.

- **Evidence class**: inferred (no LE31 owner has asked for an AI-assisted operator surface in 41 passes).
- **Confidence**: medium (mechanism) / low (present urgency). 9★ + MIT + self-hosted + privacy-friendly is the strongest single in-window stack-shape match for the *future AI-assisted operator* question; but the §3.4 conflict requires the *deterministic permission kernel* discipline to be the architectural answer.
- **Real observed LE31 JTBD**: none directly. The 9★ count is a *credibility signal*, not an LE31 demand.
- **The value is vocabulary + contingency**: when (if) LE31 v2 introduces an AI-assisted operator surface, the *deterministic permission kernel* discipline is already mapped.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred only — no observed LE31 v1 pain; v2 surface doesn't exist. |
| 2. Viability | Mechanism is well-defined (permission-ledger-as-audit-log); viability is conditional on a v2 owner-facing AI-assisted operator surface. |
| 3. Practicability and confidence | Confidence: medium for the architectural match (the deterministic permission kernel is the architectural twin of LE31 §3.1 explicit-state-transitions). Stack: no impact on v1. |
| 4. Conflict | No conflict with charter §3.1 (append-only posture is preserved); §3.4 risk is mitigated by the *deterministic permission kernel* discipline (AI cannot act without permission = staff-facing not customer-facing). |
| 5. Outcome, appetite, scope | v2 owner-pains (operator-architecture reference). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium (permission-ledger is a v2 operator-architecture pattern). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The 9★ + MIT + self-hosted + privacy-friendly cluster is a *credibility signal*, not a `build` upgrade trigger.

## Implementation steps

None today. When v2 introduces any AI-assisted operator surface, the *primitive* to surface is **"deterministic permission kernel + permission-ledger-as-audit-log"** — the v2 surface would gate every AI tool call with an explicit permission check, and every permission check would be recorded as an audit log entry. The *self-hosted + local-first + privacy-friendly* posture is the *named* surface discipline to adopt. This is a *refinement* of v1's append-only posture; it does not require re-architecting v1.

## Dependencies

- None today.
- Future dependencies (v2 only): an AI agent framework (Claude / Codex / Ollama); a permission-kernel module; a permission-ledger-as-audit-log enforcement layer. None of these are in v1 scope.

## Open questions

1. **Does LE31 v2 ever introduce an AI-assisted operator surface?** Today: no signal. The default answer is *no* unless owner-facing AI-assisted operator pain surfaces.
2. **Is the *deterministic permission kernel* discipline the right §3.4 answer for v2?** The honest answer is *probably yes* — the permission-kernel discipline preserves the *no-customer-facing-AI* posture (AI cannot act without permission = staff-facing) while allowing the *AI-assisted operator* layer to exist. The §3.4 question is a *v2 question*, not a v1 question.
3. **Is the *self-hosted + local-first + privacy-friendly* cluster the right v2 surface discipline?** The cluster is *redundant* with v1 (LE31 v1 is already self-hosted + local-first + privacy-friendly per charter §3.1); the value of the cluster as a *named* v2 surface discipline is *vocabulary*, not *novelty*.

## Why this matters

9★ + MIT + self-hosted + local-first + privacy-friendly is the **strongest single in-window stack-shape match** for any future LE31 v2 surface that introduces an AI-assisted operator layer. The *deterministic permission kernel* discipline is the **architectural twin of LE31 charter §3.1 (explicit operational transitions)** applied to AI-agent tool calls — every LE31 `StockEntry` write is already gated by an explicit operator action; the Talos primitive says *every AI tool call should be gated by an explicit permission check*. The §3.4 risk (Claude/Codex workers = LLM agent) is mitigated by the permission-kernel discipline (AI cannot act without permission = staff-facing not customer-facing). For LE31 v1, the implication is *none*. For LE31 v2, the implication is *the deterministic permission kernel primitive is mapped*. **No build today.**

## Cross-section (vs the prior 35-pick cluster)

- Feature 92 (AI-agent-decision-ledger cluster-watch) — *peer* (same AI-agent-ledger cluster).
- Feature 134 (ECHO auditable-memory-plane) — *peer* (same auditable-memory vocabulary).
- Feature 137 (NL-to-Executable-Obligations) — *peer* (same rules-as-code vocabulary).
- Feature 149 (personal-agent-blueprint Telegram chokepoint) — *closest peer* (Telegram + agent + authorization chokepoint = the same vocabulary; Talos is the *implementation*; personal-agent-blueprint is the *architecture pattern*).
- Feature 150 (Mandato protocol-level digitally-signed mandates) — *peer* (the signed mandate is the *permission*; the permission-ledger is the *audit log*).
- Feature 156 (AWIG-OS rule-citing-audit) — *peer* (same architectural-vocabulary layer; AWIG-OS is the *rule citation as first-class audit log element*; Talos is the *permission-ledger-as-audit-log*).

The *transferable insight* is **the *permission-ledger-as-audit-log* discipline** — every AI tool call gated by an explicit permission check; every permission check recorded as an audit log entry. This is the **architectural twin of LE31 charter §3.1 (explicit operational transitions)** applied to AI-agent tool calls.