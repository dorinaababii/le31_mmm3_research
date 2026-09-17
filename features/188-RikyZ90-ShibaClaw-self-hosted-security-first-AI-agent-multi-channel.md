# Feature 188 — `RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel` (defer)

> **NEW observation (2026-09-17).** Documents in-window GitHub repo `RikyZ90/ShibaClaw` (**Apache-2.0 ✓**, **81★/9⑂** — the **highest in-window star count of any 2026-09-17 net-new candidate**, Python, **pushed 2026-09-17T04:55:23Z (TODAY, in-window by `pushed_at` only)**, **created 2026-03-20T00:26:05Z** (181-day-old repo with first in-window push today), **55279 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON): `agent-framework, ai-agent, ai-agents, automation, chatbot, docker, llm, local, matrix, mcp`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-17): *"🐕 Self-hosted security-first AI agent · 28 providers · 11 chat channels · WebUI · 3-level memory · task-schedule · automation · skills · MCP"*. **First surface of this repo in the 49-pass series** (parent-verified by ripgrep against all features 1–187 + all brainstorm reports 2026-08-04..2026-09-16). The **new high-water mark for the v2-AI control-plane cluster** (vs ≤3★ for the 09-16 Distill-Agent/Pal/n0-public cluster). Bucket: **v2-AI (operator-AI control-plane, parking-lot defer)** — watch-list entry + vocabulary reference, zero build time today.

## Goal

Retain the **"self-hosted security-first AI agent · 28 providers · 11 chat channels · WebUI · 3-level memory · task-schedule · automation · skills · MCP"** cross-section architectural vocabulary as a persistent v2-AI-control-plane reference for the next LE31 v2 maintainer asking the *AI-agent control-plane* question (does LE31 v2 introduce an AI-agent surface? if so, what are the v2 architectural primitives?). The artifact is the persistent *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* primitives as a *named* v2 architectural reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the ShibaClaw cross-section architectural vocabulary: the **highest in-window star count** (81★/9⑂) for any 2026-09-17 net-new v2-AI control-plane candidate; the Apache-2.0 license is charter §3.2-compatible; the `self-hosted + security-first + 3-level-memory + multi-channel + MCP` topic set is the *closest peer in 2026* to the LE31 charter §3.1 + §3.2 + §3.4 combination.
- A written record of the **charter §3.1 + §3.2 + §3.4 triple-invariant vocabulary validation**: *"security-first"* (threat-model explicit) + *"self-hosted"* (no cloud dependency) + *"28 providers"* (multi-provider abstraction) = the exact pattern LE31's *no-cloud + permissive-license + non-customer-facing-AI* posture is converging toward.
- A written record of the **3-level memory primitive**: LE31's `audit_logs` + `StockEntry` ledger + `notes` are an implicit 3-level memory hierarchy today (system-of-record, stock-ledger, free-form notes); ShibaClaw *names the 3 levels as a discrete subsystem* — the v2-architecture vocabulary extension for any future LE31 AI-assist surface.
- A written record of the **multi-channel-delivery primitive**: LE31 v1 has only Telegram + web today; ShibaClaw's *11 chat channels* pattern is the v2-architecture reference for adding voice/email/SMS without re-architecting.
- A cross-section reference with features `92-ai-agent-decision-ledger-cluster-watch` + `96-neuruhai-cluster-watch` + `126-five-primitives-Governing-AI-Agents-at-Runtime` + `127-zero-shot-self-orchestration-Ledger-Based-Control` + `128-skill-state-scalable-long-horizon-agent-skills` + `137-natural-language-policies-executable-obligations-verification-harness` + `181-merkle-audit-tamper-evident-root-hash-batching` + `187-traust-security-traust-ledger-append-only-disposition-ledger-kernel` + the 09-16 cluster (`Aspct3434/Distill-Agent` feature from 09-16 was discussed but the feature contract was never filed).
- A decision record: today's verdict is `defer (parking-lot)` because the *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* primitives are a v2 architectural vocabulary, not a v1 build implication. v1 has no AI agent surface today; v2 would extend the v1 primitives with these cluster primitives only if and when the v2 trigger condition fires.

**Out of scope (defer artifact):**
- Any change to the *no-cloud-no-AI* posture in v1 (charter §3.1 + §3.4). The ShibaClaw repo uses an *explicit* AI-agent surface (FastAPI + LiteLLM + Docker + MCP); LE31 v1 has no AI-agent surface.
- Any change to the cook Telegram bot surface.
- Adoption of the ShibaClaw code as a v2 dependency (the repo is 81★/9⑂ at 181 days old; the *self-hosted + security-first + 3-level-memory + multi-channel + MCP* primitives would need to be independently re-implemented and validated against the LE31 append-only StockEntry ledger + audit_logs, not simply imported). The cross-section is *primitive vocabulary extension*, not *library adoption*.
- Any change to the `audit_logs` table or `StockEntry` ledger today.

## Evidence / JTBD

When a future LE31 v2 maintainer asks *"if v2 introduces an AI-assisted operator surface, what architectural primitives does LE31 adopt?"*, the maintainer wants *evidence that another independent 2026 single-maintainer Python repo at 81★ is shipping exactly the primitives that LE31 v2 would need — self-hosted, security-first, 28-provider abstraction, 11-channel-delivery, 3-level-memory, MCP-server integration — without re-architecting the v1 StockEntry + audit_logs*, but struggles because *v1 has no AI agent surface and the no-cloud posture means any future AI agent must be explicitly security-first + multi-channel + 3-level-memory + MCP-integrated*, so that *v2 can introduce the AI-assist primitives with the cluster's vocabulary rather than inventing a new one*.

- **Evidence class**: observed (the ShibaClaw repo description names *self-hosted security-first AI agent · 28 providers · 11 chat channels · WebUI · 3-level memory · task-schedule · automation · skills · MCP* — exactly the v2 architectural vocabulary for any future LE31 AI-assist surface).
- **Confidence**: medium-high for the architectural vocabulary validation (81★/9⑂ is the highest in-window star count for any v2-AI peer in 2026; Apache-2.0 + Python + 181-day-old + first in-window push today confirms a real maintainer with sustained engagement; the topic set maps 1:1 onto charter §3.1 + §3.2 + §3.4 invariants). Confidence: low for *adoption* (LE31 should re-implement the *self-hosted + security-first + 3-level-memory + multi-channel + MCP* primitives against its own StockEntry + audit_logs, not import ShibaClaw directly).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + architectural validation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + charter-§3.1-§3.2-§3.4-triple-invariant documentation**: when (if) LE31 v2 introduces the AI-assist surface, the *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* vocabulary is documented.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred — the architectural vocabulary validation is real but no LE31 owner has asked for *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* in 49 passes. The owner today uses feature 92 + 96 + 126 + 127 cluster-watch entries to track the v2-AI control-plane convergence. |
| 2. Viability | Mechanism is well-defined (Python + FastAPI + LiteLLM + Docker + MCP); viability is conditional on a v2 owner-facing AI-assist question. |
| 3. Practicability and confidence | Confidence: medium-high for the architectural vocabulary validation (81★/9⑂ is the new high-water mark for any v2-AI peer in 2026; Apache-2.0 + Python + 181-day-old + first in-window push today confirms real maintainer with sustained engagement; the topic set maps 1:1 onto charter §3.1 + §3.2 + §3.4). Stack: on-pattern (Python matches LE31; LiteLLM/MCP are v2-AI surface primitives, not v1 stack primitives). Practicability of adoption: medium — the *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* primitives can be extracted and re-implemented against LE31's StockEntry + audit_logs. |
| 4. Conflict | No conflict with charter §3.1 (the *self-hosted + security-first* posture is explicitly §3.1-aligned); §3.2 (Apache-2.0 = permissive); §3.4 (ShibaClaw is an operator-facing AI agent, not customer-facing — *security-first* posture explicitly excludes guest/user-facing surfaces). Charter §3.4 compatible. |
| 5. Outcome, appetite, scope | v2-AI control-plane (cross-section architectural vocabulary). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium-high (the *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* vocabulary is the named architectural reference for any future v2 AI-assist surface). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The 81★/9⑂ + Apache-2.0 + 181-day-old + Python + first-in-window-push-today + topic-set-mapping-1:1-onto-charter-§3.1+§3.2+§3.4 combo is a *novelty signal* + *vocabulary-validation signal*, not a *credibility signal*; the architectural vocabulary is the value.

## Implementation steps

None today. When v2 maintainer asks the v2 AI-assist question, the *architectural vocabulary validation* to surface is **"another independent 2026 single-maintainer Python repo at 81★ is shipping exactly the self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP primitives that LE31 v2 would need without re-architecting v1"** — and the *charter §3.1 + §3.2 + §3.4 triple-invariant validation* to surface is **"the self-hosted + security-first + 28-provider + 11-channel pattern is the exact pattern that LE31's no-cloud + permissive-license + non-customer-facing-AI posture is converging toward"**. This is a *primitive vocabulary extension + architectural validation*, not a v1 build implication; v2 maintainer decision required before any v2 surface adopts the *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* posture.

## Dependencies

- None today.
- Future dependencies (v2 only): a v2 maintainer decision on whether to introduce an AI-assist surface; an *AI-agent control-plane* design that adopts the *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* primitives; an *AI-assist risk-model* that explicitly excludes guest/user-facing surfaces per charter §3.4. None of these are in v1 scope.

## Open questions

1. **Is the ShibaClaw `3-level memory` a discrete subsystem with named levels, or a marketing term for the standard LiteLLM conversation-history + vector-store + episodic-memory pattern?** Today: unknown — repo source not yet read. If discrete subsystem with named levels, the cross-section is *primitive vocabulary extension*; if marketing term, the cross-section is *JTBD validation only*. Recommend read-and-cite on next v2-architecture-review moment.
2. **Does the ShibaClaw `security-first` posture include explicit threat-model documentation (CVE-history, sandbox boundary, supply-chain audit) or is it a marketing label?** Today: unknown. If explicit threat-model, the cross-section is *charter-§3.4 invariant validation*; if marketing label, the cross-section is *JTBD validation only*. Recommend read-and-cite.
3. **Is the ShibaClaw `MCP` integration a peer-server surface (LE31 v1 could implement MCP-client to talk to the ShibaClaw MCP-server) or a peer-to-peer surface (LE31 v1 + ShibaClaw as MCP-servers talking to each other)?** Today: unknown. If peer-server, the cross-section is *v2-integration primitive*; if peer-to-peer, the cross-section is *v2-mesh-architecture*. Recommend read-and-cite.
4. **Is the ShibaClaw repo actively maintained?** Today: 81★/9⑂/181-day-old + Apache-2.0 + first in-window push today = active-maintainer signal. Recommend re-check at the next 7-day boundary.

## Why this matters

The ShibaClaw repo is the **first in-window v2-AI control-plane peer of the 49-pass series at 81★** + Apache-2.0 + 181-day-old + first in-window push today. The *architectural vocabulary validation* — *"self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP is the named 2026 pattern for any future LE31 AI-assist surface that adopts the charter §3.1 + §3.2 + §3.4 triple-invariant"* — is the **new high-water mark** for the v2-AI control-plane cluster (vs ≤3★ for the 09-16 Distill-Agent/Pal/n0-public cluster). For LE31 v1, the implication is *none* (v1 has no AI-agent surface). For LE31 v2, the implication is *the self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP vocabulary is documented*. **No build today.**

## Cross-section (vs the prior 17-pick cluster)

- Feature 92 (`ai-agent-decision-ledger-cluster-watch`) — *sister cluster-watch* (LE31's v2-AI control-plane watch-list entry; ShibaClaw is a new high-water-mark peer).
- Feature 96 (`neuruhai-cluster-watch`) — *sister cluster-watch* (LE31's v2-AI control-plane NeuruhAI 7-pack watch-list entry; ShibaClaw is a high-star peer outside the NeuruhAI cluster).
- Feature 126 (`five-primitives-Governing-AI-Agents-at-Runtime`) — *sister-shape* (arXiv paper on AI-agent governance primitives; ShibaClaw's *security-first + 3-level-memory + multi-channel + MCP* primitives are the operational implementation of the governance primitives).
- Feature 127 (`zero-shot-self-orchestration-Ledger-Based-Control`) — *sister-shape* (arXiv paper on Ledger-Based Control as the load-bearing component; ShibaClaw's *security-first* posture is the operational implementation of Ledger-Based Control).
- Feature 128 (`skill-state-scalable-long-horizon-agent-skills`) — *sister-shape* (arXiv paper on SKILL.state for long-horizon agents; ShibaClaw's *3-level memory* is the operational implementation of SKILL.state).
- Feature 137 (`natural-language-policies-executable-obligations-verification-harness`) — *sister-shape* (arXiv paper on NL-to-executable-obligations; ShibaClaw's *task-schedule + automation + skills* primitives are the operational implementation of NL-to-executable-obligations).
- Feature 181 (`merkle-audit-tamper-evident-root-hash-batching`) — *sister-shape* (the Merkle-audit cryptographic-verifiability primitive; ShibaClaw's *security-first* posture implicitly requires Merkle-audit-style verifiability for any future v2 AI-assist surface).
- Feature 187 (`traust-security-traust-ledger-append-only-disposition-ledger-kernel`) — *sister-shape* (the security-audit-domain append-only-ledger-kernel pattern; ShibaClaw's *security-first* posture implicitly requires append-only-ledger-kernel for any future v2 AI-assist audit surface).
- 09-16 cluster (`Aspct3434/Distill-Agent` + `OtakuNathan/Pal` + `nemuprojectofficial-glitch/n0-public` — the latter filed as feature 183) — *sister-shape cluster* (the v2-AI control-plane + deterministic-gate + append-only-ledger pattern; ShibaClaw is the new high-star peer at 81★ vs ≤3★ for the 09-16 cluster).

The *transferable insight* is **the self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP architectural vocabulary** — and the **charter §3.1 + §3.2 + §3.4 triple-invariant validation** — *the no-cloud + permissive-license + non-customer-facing-AI posture is the named 2026 pattern for any AI-agent control-plane, and LE31 v1 already implements the primitives under different names* (`audit_logs` = 3-level-memory level-1; `StockEntry` = 3-level-memory level-2; `notes` = 3-level-memory level-3; Telegram = 1 of 11 channels; FastAPI = the control plane).
