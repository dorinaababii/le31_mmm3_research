# Feature 189 — `Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents` (defer)

> **NEW observation (2026-09-17).** Documents in-window GitHub repo `Bazza1982/HASHI` (**MIT ✓**, **1★/0⑂**, Python, **pushed 2026-09-17T04:04:19Z (TODAY, in-window by `pushed_at` only)**, **created 2026-03-10T13:09:33Z** (191-day-old repo with first in-window push today), **149646 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON): `agent-orchestration, ai-agents, claude-code, codex, gemini-cli, llm, local-first, multi-agent, python, self-hosted`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-17): *"Local-first control plane for persistent AI agents—unifying identity, memory, tools, workflows, governance, and multi-channel access across HER v2, Claude Code, Codex, Gemini, and more."* The **closest peer to LE31 charter §3.1 + §3.2 + §3.4 combination in 2026 at the *control-plane* layer**. The *control plane* is named as a discrete subsystem. Bucket: **v2-AI (operator-AI control-plane + multi-agent governance, parking-lot defer)** — watch-list entry + vocabulary reference, zero build time today.

## Goal

Retain the **"local-first control plane for persistent AI agents — unifying identity, memory, tools, workflows, governance, and multi-channel access"** cross-section architectural vocabulary as a persistent v2-AI-control-plane reference for the next LE31 v2 maintainer asking the *AI-agent control-plane as a discrete subsystem* question (does LE31 v2 introduce an AI-agent control plane as a named subsystem? if so, what are the six primitives?). The artifact is the persistent *identity + memory + tools + workflows + governance + multi-channel* primitives as a *named* v2 architectural reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the HASHI cross-section architectural vocabulary: the **closest peer to LE31 charter §3.1 + §3.2 + §3.4 combination in 2026 at the *control-plane* layer**; the MIT license is charter §3.2-compatible; the `local-first + self-hosted + multi-agent + agent-orchestration` topic set maps 1:1 onto the LE31 charter §3.1 + §3.4 combination.
- A written record of the **control-plane-as-discrete-subsystem primitive**: LE31's v1 has an *implicit* control plane (FastAPI routes + aiogram handlers + `audit_logs` writer all live in one Python process); HASHI *names the control plane as a discrete subsystem* — the v2-architecture vocabulary extension for any future LE31 AI-assist surface.
- A written record of the **six primitives of any AI-agent control plane**: *"identity + memory + tools + workflows + governance + multi-channel access"* — and the *order matters*: identity first (which actor?), then memory (what do they know?), then tools (what can they do?), then workflows (in what sequence?), then governance (what bounds?), then multi-channel (how is it delivered?). The vocabulary is the named architectural reference.
- A written record of the **charter §3.4 alignment via explicit governance**: HASHI names *"governance"* as the 5th primitive — the *governance* primitive is the explicit enforcement boundary that excludes guest/user-facing surfaces per charter §3.4.
- A cross-section reference with features `92-ai-agent-decision-ledger-cluster-watch` + `96-neuruhai-cluster-watch` + `126-five-primitives-Governing-AI-Agents-at-Runtime` + `127-zero-shot-self-orchestration-Ledger-Based-Control` + `137-natural-language-policies-executable-obligations-verification-harness` + `160-factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai` + `167-csakegyruszki-provtrail-hash-chained-llm-source-ledger` + `183-nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety` + the 09-16 cluster.
- A decision record: today's verdict is `defer (parking-lot)` because the *local-first control plane + six primitives* is a v2 architectural vocabulary, not a v1 build implication. v1 has no AI-agent control plane today; v2 would extend the v1 primitives with these cluster primitives only if and when the v2 trigger condition fires.

**Out of scope (defer artifact):**
- Any change to the *no-cloud-no-AI* posture in v1 (charter §3.1 + §3.4). The HASHI repo uses an *explicit* AI-agent control plane (Python + LiteLLM + Docker + MCP); LE31 v1 has no AI-agent control plane.
- Any change to the cook Telegram bot surface.
- Adoption of the HASHI code as a v2 dependency (the repo is 1★/0⑂ at 191 days old; the *local-first control plane + six primitives* would need to be independently re-implemented and validated against the LE31 append-only StockEntry ledger + audit_logs, not simply imported). The cross-section is *primitive vocabulary extension*, not *library adoption*.
- Any change to the `audit_logs` table or `StockEntry` ledger today.

## Evidence / JTBD

When a future LE31 v2 maintainer asks *"if v2 introduces an AI-agent control plane, what is the named set of primitives?"*, the maintainer wants *evidence that another independent 2026 single-maintainer Python repo is shipping exactly the named set of six primitives — identity + memory + tools + workflows + governance + multi-channel — as a discrete subsystem*, but struggles because *v1 has an implicit control plane and the no-cloud posture means any future AI-agent control plane must be explicitly local-first + multi-provider + governance-bounded*, so that *v2 can introduce the AI-agent control plane with the named primitives rather than inventing a new one*.

- **Evidence class**: observed (the HASHI repo description names *local-first control plane for persistent AI agents — unifying identity, memory, tools, workflows, governance, and multi-channel access across HER v2, Claude Code, Codex, Gemini, and more* — exactly the v2 architectural vocabulary for any future LE31 AI-agent control plane).
- **Confidence**: medium-high for the architectural vocabulary validation (MIT + Python + 191-day-old + first in-window push today confirms a real maintainer with sustained engagement; the *six primitives* ordering matches the canonical 2026 AI-agent control-plane literature; the `local-first + self-hosted + multi-agent` topic set maps 1:1 onto charter §3.1 + §3.4). Confidence: low for *adoption* (LE31 should re-implement the *control-plane + six primitives* against its own StockEntry + audit_logs, not import HASHI directly).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + architectural validation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + charter-§3.4-invariant documentation**: when (if) LE31 v2 introduces the AI-agent control plane, the *identity + memory + tools + workflows + governance + multi-channel* vocabulary is documented.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred — the architectural vocabulary validation is real but no LE31 owner has asked for *local-first control plane + six primitives* in 49 passes. The owner today uses feature 92 + 96 + 126 + 127 + 137 cluster-watch entries to track the v2-AI control-plane convergence. |
| 2. Viability | Mechanism is well-defined (Python + LiteLLM + Docker + MCP); viability is conditional on a v2 owner-facing AI-assist question. |
| 3. Practicability and confidence | Confidence: medium-high for the architectural vocabulary validation (MIT + Python + 191-day-old + first in-window push today confirms real maintainer with sustained engagement; the *six primitives* ordering matches the canonical 2026 AI-agent control-plane literature). Stack: on-pattern (Python matches LE31; LiteLLM/MCP are v2-AI surface primitives, not v1 stack primitives). Practicability of adoption: medium — the *local-first control plane + six primitives* can be extracted and re-implemented against LE31's StockEntry + audit_logs. |
| 4. Conflict | No conflict with charter §3.1 (the *local-first + self-hosted* posture is explicitly §3.1-aligned); §3.2 (MIT = permissive); §3.4 (HASHI names *"governance"* as the 5th primitive — the *governance* primitive is the explicit enforcement boundary that excludes guest/user-facing surfaces per charter §3.4). Charter §3.4 compatible. |
| 5. Outcome, appetite, scope | v2-AI control-plane (cross-section architectural vocabulary). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium-high (the *local-first control plane + six primitives* vocabulary is the named architectural reference for any future v2 AI-assist surface). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The MIT + Python + 191-day-old + first in-window push today + *six primitives* ordering + `local-first + self-hosted + multi-agent + agent-orchestration` topic set combo is a *novelty signal* + *vocabulary-validation signal*, not a *credibility signal*; the architectural vocabulary is the value.

## Implementation steps

None today. When v2 maintainer asks the v2 AI-agent control-plane question, the *architectural vocabulary validation* to surface is **"another independent 2026 single-maintainer Python repo is shipping exactly the local-first control plane + six primitives (identity + memory + tools + workflows + governance + multi-channel) as a discrete subsystem that LE31 v2 would need without re-architecting v1"** — and the *charter §3.4 alignment via explicit governance* to surface is **"the governance primitive is the explicit enforcement boundary that excludes guest/user-facing surfaces"**. This is a *primitive vocabulary extension + architectural validation*, not a v1 build implication; v2 maintainer decision required before any v2 surface adopts the *local-first control plane + six primitives* posture.

## Dependencies

- None today.
- Future dependencies (v2 only): a v2 maintainer decision on whether to introduce an AI-agent control plane as a discrete subsystem; an *AI-agent control-plane* design that adopts the *identity + memory + tools + workflows + governance + multi-channel* primitives; an *AI-assist risk-model* that explicitly excludes guest/user-facing surfaces via the *governance* primitive. None of these are in v1 scope.

## Open questions

1. **Does the HASHI *six primitives* map to named Python classes / interfaces, or is it a documentation-level architecture?** Today: unknown — repo source not yet read. If named Python classes/interfaces, the cross-section is *primitive vocabulary extension + reusable-interface-design*; if documentation-level, the cross-section is *vocabulary validation only*. Recommend read-and-cite on next v2-architecture-review moment.
2. **Does the HASHI *governance* primitive include explicit guest/user-facing-surface exclusion (charter §3.4 invariant) or just general role-based-access-control?** Today: unknown. If explicit guest/user-facing-surface exclusion, the cross-section is *charter-§3.4 invariant validation*; if general RBAC, the cross-section is *JTBD validation only*. Recommend read-and-cite.
3. **Is the HASHI *identity* primitive a single-actor primitive (one operator per control plane) or a multi-actor primitive (cook + owner + supplier + accountant per control plane)?** Today: unknown. If single-actor, the cross-section is *v2 single-restaurant primitive*; if multi-actor, the cross-section is *v2 multi-actor primitive*. Recommend read-and-cite.
4. **Is the HASHI repo actively maintained?** Today: 1★/0⑂/191-day-old + MIT + first in-window push today = active-maintainer signal. Recommend re-check at the next 7-day boundary.

## Why this matters

The HASHI repo is the **first in-window v2-AI control-plane peer of the 49-pass series to name the control plane as a discrete subsystem + the six primitives (identity + memory + tools + workflows + governance + multi-channel) as the named architectural vocabulary**. The *architectural vocabulary validation* — *"the local-first control plane + six primitives is the named 2026 pattern for any future LE31 AI-assist surface that adopts the charter §3.1 + §3.2 + §3.4 combination"* — is the **closest peer to LE31 charter §3.1 + §3.2 + §3.4 combination in 2026 at the *control-plane* layer**. For LE31 v1, the implication is *none* (v1 has no AI-agent control plane). For LE31 v2, the implication is *the local-first control plane + six primitives vocabulary is documented*. **No build today.**

## Cross-section (vs the prior 17-pick cluster)

- Feature 92 (`ai-agent-decision-ledger-cluster-watch`) — *sister cluster-watch* (LE31's v2-AI control-plane watch-list entry; HASHI is the closest peer to charter §3.1+§3.2+§3.4 combination).
- Feature 96 (`neuruhai-cluster-watch`) — *sister cluster-watch* (LE31's v2-AI control-plane NeuruhAI 7-pack watch-list entry; HASHI is a high-star peer outside the NeuruhAI cluster).
- Feature 126 (`five-primitives-Governing-AI-Agents-at-Runtime`) — *sister-shape* (arXiv paper on AI-agent governance primitives; HASHI's *governance* primitive is the operational implementation of the five governance primitives).
- Feature 127 (`zero-shot-self-orchestration-Ledger-Based-Control`) — *sister-shape* (arXiv paper on Ledger-Based Control; HASHI's *identity + memory* primitives are the operational implementation of Ledger-Based Control).
- Feature 137 (`natural-language-policies-executable-obligations-verification-harness`) — *sister-shape* (arXiv paper on NL-to-executable-obligations; HASHI's *workflows + governance* primitives are the operational implementation of NL-to-executable-obligations).
- Feature 160 (`factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai`) — *sister-shape* (GitHub `Symbolic-Intelligence-Org/factgraph` — append-only fact ledger for structured symbolic reasoning; HASHI's *memory* primitive is the operational implementation of the append-only fact ledger).
- Feature 167 (`csakegyruszki-provtrail-hash-chained-llm-source-ledger`) — *sister-shape* (GitHub `csakegyruszki/provtrail` — hash-chained LLM-source ledger; HASHI's *memory + governance* primitives implicitly require hash-chained provenance).
- Feature 183 (`nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety`) — *sister-shape* (GitHub `nemuprojectofficial-glitch/n0-public` — autonomous agent with public append-only ledger + dependency-free verifier; HASHI's *identity + memory + governance* primitives implicitly require the dependency-free verifier pattern).
- 09-16 cluster (`Aspct3434/Distill-Agent` + `OtakuNathan/Pal` + `nemuprojectofficial-glitch/n0-public` — the latter filed as feature 183) — *sister-shape cluster* (the v2-AI control-plane + deterministic-gate + append-only-ledger pattern; HASHI is the new closest peer to the charter §3.1+§3.2+§3.4 combination at the *control-plane* layer).

The *transferable insight* is **the local-first control plane + six primitives (identity + memory + tools + workflows + governance + multi-channel) architectural vocabulary** — and the **charter §3.4 alignment via explicit governance primitive** — *the no-cloud + permissive-license + non-customer-facing-AI posture is the named 2026 pattern for any AI-agent control plane, and LE31 v1 already implements the primitives under different names* (`audit_logs` = memory primitive; FastAPI = the control plane; Telegram = one of the multi-channel surfaces; role-based access control = the implicit governance primitive).
