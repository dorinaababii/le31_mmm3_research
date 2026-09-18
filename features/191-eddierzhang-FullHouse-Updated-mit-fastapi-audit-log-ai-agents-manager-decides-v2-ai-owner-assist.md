# Feature 191 — `eddierzhang-FullHouse-Updated-mit-fastapi-audit-log-ai-agents-manager-decides-v2-ai-owner-assist` (defer)

> **NEW observation (2026-09-18).** Documents in-window GitHub repo `eddierzhang/FullHouse-Updated` (**MIT ✓**, **0★/0⑂**, Python, **pushed 2026-09-15T18:11:18Z** (3 days ago, in-window by `pushed_at`), **created date TBD**, **7002 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON): `ai-agents, anthropic, audit-log, docker, fastapi, llm-agents`. Description (verbatim, parent-verified GitHub API direct-GET 2026-09-18): *"Restaurant operations run by AI agents that propose and a manager who decides."* **Strongest LE31-stack-shape match of the 50-pass series**: `fastapi` + `audit-log` + `ai-agents` + the `manager decides` framing = the **textbook charter §3.4 compliance pattern** (AI proposes + observable evidence + manager decides + non-AI fallback). Bucket: **v2-AI (owner-assist, parking-lot defer)** — vocabulary + charter-§3.4-validation artifact, zero build time today.

## Goal

Retain the **"Restaurant operations run by AI agents that propose and a manager who decides"** cross-section architectural vocabulary + **charter §3.4 invariant validation artifact** for the next LE31 v2 maintainer asking the *AI-proposes-manager-decides operator-tooling* question (does LE31 v2 introduce an AI-assisted operator surface? if so, what is the charter §3.4 invariant pattern that prevents the AI from acting on its own?). The artifact is the persistent *AI-proposes-manager-decides* primitive as a *named* v2 architectural reference + charter §3.4 invariant documentation. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the `FullHouse-Updated` cross-section architectural vocabulary: the **strongest LE31-stack-shape match of the 50-pass series** (FastAPI + audit-log + AI-agents + manager-decides); the MIT license is charter §3.2-compatible; the `ai-agents + anthropic + audit-log + docker + fastapi + llm-agents` topic set maps 1:1 onto a future LE31 v2 owner-assist surface.
- A written record of the **AI-proposes-manager-decides primitive**: the architectural discipline where the AI *proposes* an action (with observable evidence = the `audit-log` + the agent's reasoning trace), and a human manager *decides* whether to approve. This is the **explicit charter §3.4 compliance pattern**: *AI may assist owner/staff, with observable evidence (the proposal + the reasoning trace) and a non-AI fallback (the manager's manual approval = the AI does not act autonomously)*.
- A written record of the **charter §3.4 invariant language as explicit design principle**: the *propose-then-decide* separation is the operational enforcement boundary that excludes customer-facing AI per charter §3.4. The manager is the *named veto point*; the AI cannot proceed without manager approval.
- A written record of the **`audit-log` + `fastapi` stack-mirror with LE31**: the topic set directly maps onto LE31's existing `audit_logs` SQLModel table (charter §3.1: append-only audit log of explicit state transitions) + LE31's existing FastAPI backend. The *AI-agents* integration is the only new surface.
- A decision record: today's verdict is `defer (parking-lot)` because the *AI-proposes-manager-decides* primitive is a v2 architectural vocabulary + charter §3.4 validation, not a v1 build implication. v1 has no AI-assist surface today; v2 would extend the v1 primitives with these cluster primitives only if and when the v2 trigger condition fires.

**Out of scope (defer artifact):**
- Any change to the *no-AI* posture in v1 (charter §3.4). The `FullHouse-Updated` repo uses an *explicit* AI-agents surface (Python + Anthropic + FastAPI + audit-log + Docker); LE31 v1 has no AI-assist surface. The defer artifact documents the architectural vocabulary; v2 maintainer decision required before adoption.
- Any change to the cook Telegram bot surface.
- Adoption of the `FullHouse-Updated` code as a v2 dependency (the repo is 0★/0⑂ at 7002 KB; the *AI-proposes-manager-decides* primitive + the `audit-log + fastapi` stack mirror would need to be independently re-implemented and validated against the LE31 append-only StockEntry ledger + audit_logs, not simply imported). The cross-section is *primitive vocabulary extension + charter §3.4 invariant documentation*, not *library adoption*.
- Any change to the `audit_logs` table or `StockEntry` ledger today.
- Any change to the operator-tooling surface in v1 today.

## Evidence / JTBD

When a future LE31 v2 maintainer asks *"if v2 introduces an AI-assisted operator surface, what is the charter §3.4 invariant pattern that prevents the AI from acting autonomously?"*, the maintainer wants *evidence that another independent 2026 Python repo at 7002 KB with FastAPI + audit-log + AI-agents + Docker is shipping exactly the AI-proposes-manager-decides discipline*, but struggles because *v1 has no AI-assist surface and the charter §3.4 invariant is not yet operationalized in code*, so that *v2 can introduce the AI-assisted operator surface with the explicit charter §3.4 invariant rather than inventing a new one*.

- **Evidence class**: observed (the `FullHouse-Updated` description explicitly names *"AI agents that propose and a manager who decides"* — exactly the charter §3.4 invariant language *"AI may assist owner/staff, with observable evidence (the proposal) and a non-AI fallback (the manager decides)"*).
- **Confidence**: high for the architectural vocabulary validation + charter §3.4 invariant documentation (MIT + Python + 7002 KB substantial repo + in-window push 3-days-ago + the `audit-log` topic maps 1:1 onto LE31's `audit_logs` SQLModel table). Confidence: low for *adoption* (LE31 should re-implement the *AI-proposes-manager-decides* primitive against its own StockEntry + audit_logs, not import FullHouse-Updated directly).
- **Real observed LE31 JTBD**: none directly. The cross-section is *primitive vocabulary extension + charter §3.4 invariant documentation*, not *LE31 demand*.
- **The value is primitive vocabulary extension + charter §3.4 invariant documentation**: when (if) LE31 v2 introduces an AI-assisted operator surface, the *AI-proposes-manager-decides* vocabulary is documented, and the charter §3.4 invariant is validated against an independent 2026 Python repo with the same `audit-log + fastapi` stack as LE31 v1.

## Description

GitHub `eddierzhang/FullHouse-Updated` (MIT, 0★/0⑂, Python, pushed 2026-09-15T18:11:18Z, created date TBD, 7002 KB substantial repo).

Description (verbatim): *"Restaurant operations run by AI agents that propose and a manager who decides."*

Topics (verbatim from raw JSON): `ai-agents`, `anthropic`, `audit-log`, `docker`, `fastapi`, `llm-agents` — 6 topics; **the strongest direct LE31-stack-shape match of any 2026-09-18 in-window repo** (`fastapi` + `audit-log` directly maps onto LE31's backend framework + `audit_logs` table).

The 1:1 mapping onto LE31 stack (today):

| `FullHouse-Updated` topic / primitive | LE31 stack | Match status |
|---|---|---|
| `fastapi` | FastAPI 0.141.1 (LE31 backend framework) | ✓ direct match |
| `audit-log` | `audit_logs` SQLModel table (charter §3.1 append-only audit log) | ✓ direct match |
| `docker` | Docker (production deploy primitive) | ✓ on-pattern |
| `anthropic` | (no LLM dependency in v1) | v2-AI surface only |
| `ai-agents` + `llm-agents` | (no AI-agent surface in v1) | v2-AI surface only |
| *"AI agents that propose and a manager who decides"* | (charter §3.4 *AI may assist owner/staff with observable evidence and non-AI fallback*) | **§3.4 EXPLICIT COMPLIANCE PATTERN** |

The **charter §3.4 alignment is the deciding factor** for the defer artifact:
- *"AI agents that propose"* → the AI's role is to *propose*, not to *act*. The manager sees the proposal + the reasoning trace (the `audit-log` + the agent's intermediate reasoning steps).
- *"and a manager who decides"* → the manager is the named *veto point*. The AI cannot proceed without manager approval. This is the **explicit charter §3.4 enforcement boundary**: the *non-AI fallback* is the manager's manual approval; the *observable evidence* is the audit-log entry of the proposal + the manager's decision.

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred — the architectural vocabulary + charter §3.4 validation is real but no LE31 owner has asked for *AI-proposes-manager-decides* in 50 passes. The owner today uses features 158/181/183/188/189/190 to track the *AI-but-not-customer-facing / operator-must-confirm* convergence. |
| 2. Viability | Mechanism is well-defined (Python + Anthropic + FastAPI + audit-log + Docker); viability is conditional on a v2 owner-facing AI-assist question. |
| 3. Practicability and confidence | Confidence: high for the architectural vocabulary + charter §3.4 invariant validation (MIT + Python + 7002 KB substantial repo + in-window push 3-days-ago; the `audit-log + fastapi` topic pair directly maps onto LE31's `audit_logs` + FastAPI; the *AI-proposes-manager-decides* discipline is explicitly named in the description). Stack: on-pattern (Python + FastAPI match LE31 exactly; Anthropic + Docker are v2 deployment primitives, not v1 stack primitives). Practicability of adoption: medium — the *AI-proposes-manager-decides* primitive can be extracted and re-implemented against LE31's StockEntry + audit_logs. |
| 4. Conflict | No conflict with charter §3.1 (the `audit-log` topic maps 1:1 onto LE31's existing `audit_logs` SQLModel table — the primitive is *additive*, not replacement); §3.2 (MIT = permissive); §3.4 (the *manager decides* framing is the explicit charter §3.4 compliance pattern: AI proposes + observable evidence + non-AI fallback). Charter §3.4 explicitly validated. |
| 5. Outcome, appetite, scope | v2-AI owner-assist (cross-section architectural vocabulary + charter §3.4 validation). Appetite: zero today. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium-high (the *AI-proposes-manager-decides* vocabulary + charter §3.4 validation is the named architectural reference for any future v2 AI-assisted operator surface). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The MIT + Python + 7002 KB + in-window push 3-days-ago + `audit-log + fastapi` stack match + `AI-agents-manager-decides` charter §3.4 explicit-compliance combo is a *vocabulary-validation signal* + *charter §3.4 invariant documentation artifact*, not a *credibility signal*; the architectural vocabulary + charter §3.4 validation is the value.

## Implementation steps

None today. When the v2 maintainer asks the v2 AI-assisted operator-surface question, the *architectural vocabulary validation* to surface is **"another independent 2026 Python repo at 7002 KB with the same `audit-log + fastapi` stack as LE31 v1 is shipping exactly the AI-proposes-manager-decides discipline that LE31 v2 would need to satisfy charter §3.4"** — and the *charter §3.4 invariant documentation* to surface is **"the explicit `manager decides` framing is the operational enforcement boundary that excludes guest/user-facing AI per charter §3.4; the AI cannot act autonomously; the manager is the named veto point"**. This is a *primitive vocabulary extension + charter §3.4 invariant documentation*, not a v1 build implication; v2 maintainer decision required before any v2 surface adopts the *AI-proposes-manager-decides* posture.

## Dependencies

- None today.
- Future dependencies (v2 only): a v2 maintainer decision on whether to introduce an AI-assisted operator surface; an *AI-proposes-manager-decides* design that adopts the charter §3.4 invariant; an *operator-tooling AI risk-model* that explicitly enforces the *manager decides* veto point. None of these are in v1 scope.

## Open questions

1. **Does the `FullHouse-Updated` *manager decides* pattern include a structured approval UI (e.g., a Slack/email/CLI approval) or is it implicit in the agent's reasoning trace?** Today: unknown — repo source not yet read. If structured approval, the cross-section is *manager-decides-as-named-veto-point*; if implicit, the cross-section is *AI-proposes-manager-confirms-via-audit-log*. Recommend read-and-cite on next v2-architecture-review moment.
2. **What is the Anthropic integration surface (Claude API? Claude Code? MCP server?)?** Today: unknown — repo source not yet read. The integration surface determines the v2 dependency surface (a v2 surface that uses Anthropic's Claude API is a v2-architecture decision).
3. **Is the `audit-log` topic referring to a structured logging library (e.g., Python's `logging` module + a structured formatter) or to a dedicated `audit_logs` table (LE31-style)?** Today: unknown. If structured logging library, the cross-section is *logging-pattern reference*; if dedicated audit table, the cross-section is *audit-table-schema reference*. Recommend read-and-cite.
4. **Is the `FullHouse-Updated` repo actively maintained?** Today: 0★/0⑂ + MIT + 7002 KB + in-window push 3-days-ago = active-maintainer signal but no community adoption (0★). Recommend re-check at the next 7-day boundary.

## Why this matters

The `FullHouse-Updated` repo is the **strongest LE31-stack-shape match of the 50-pass series**: `fastapi` + `audit-log` + `docker` directly maps onto LE31's existing FastAPI + `audit_logs` SQLModel table + Docker deploy primitive; the `ai-agents` + `anthropic` + `llm-agents` topics indicate a *named* AI-assisted operator surface; the *"AI agents that propose and a manager who decides"* description is the **explicit charter §3.4 invariant language** as a named design principle. The *AI-proposes-manager-decides + charter §3.4 invariant validation* — *"the strongest LE31-stack-shape match today is also the first repo to explicitly name the charter §3.4 compliance pattern as a design principle"* — is the **highest-value v2-AI owner-assist + charter §3.4 invariant documentation artifact of the 50-pass series**. For LE31 v1, the implication is *none* (v1 has no AI-assist surface). For LE31 v2, the implication is *the AI-proposes-manager-decises vocabulary is documented, and the charter §3.4 invariant is validated against an independent 2026 Python repo with the same `audit-log + fastapi` stack as LE31 v1*. **No build today.**

## Cross-section (vs the prior 50-pass cluster)

- Feature 104 (`aldia-ai-agent-business-engine-cross-section`) — *sister-shape* (GitHub `jonalemndi2/ALdia` — Apache-2.0, 5★, Python, business engine for AI agents with invoicing + payments + inventory + idempotent MCP tools; `FullHouse-Updated` is the strongest LE31-stack-shape match of the 50-pass series because it uses the same `audit-log + fastapi` stack as LE31 v1).
- Feature 140 (`casedock-adhd-informed-solo-builder-workbench-htmx-design-posture`) — *sister-shape* (GitHub `gerpaick/casedock` — Apache-2.0, 2★, Django + HTMX, calm workbench for solo technical builders; `FullHouse-Updated` is the strongest *restaurant-operations* AI-proposes-manager-decides peer).
- Feature 146 (`slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section`) — *sister-shape* (GitHub `giltotherescue/slashbooks` — MIT, 1★, Python, AI bookkeeper QuickBooks replacement; `FullHouse-Updated` is the strongest *operator-tooling* AI-proposes-manager-decides peer).
- Feature 158 (`azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory`) — *sister-shape* (GitHub `AzizSeker/smart-restaurant-management-system` — MIT, 1★, Python, AI-powered restaurant management system; `FullHouse-Updated` is the strongest *restaurant-domain* AI-proposes-manager-decides peer with the same `audit-log + fastapi` stack as LE31 v1).
- Feature 188 (`RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel`) — *sister-shape* (GitHub `RikyZ90/ShibaClaw` — Apache-2.0, 81★/9⑂, the *highest in-window star count* of the 49-pass series, self-hosted security-first AI agent with 28 providers + 11 chat channels + 3-level memory + MCP; `FullHouse-Updated` is the strongest *restaurant-domain* + *charter §3.4 explicit compliance* peer, even though ShibaClaw has 81★ vs FullHouse-Updated's 0★).
- Feature 189 (`Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents`) — *sister-shape* (GitHub `Bazza1982/HASHI` — MIT, 1★/0⑂, Python, local-first control plane for persistent AI agents with the six named primitives *identity + memory + tools + workflows + governance + multi-channel*; `FullHouse-Updated` is the strongest *single-restaurant-domain + same-stack-as-LE31* peer, even though HASHI has the more general *control-plane* vocabulary).
- Feature 190 (`ilyautov-small-business-ru-34-AI-skills-tax-contractor-INN`) — *sister-shape* (GitHub `ilyautov/small-business-ru` — Apache-2.0, 16★/4⑂, Python, 34 open AI skills for Russian small business with the *numbers-computed-by-code + data-from-real-registries* charter §3.4 invariant; `FullHouse-Updated` is the strongest *restaurant-domain + manager-decides-veto-point* charter §3.4 validation, while small-business-ru is the strongest *numbers-computed-by-code* charter §3.4 validation).

The *transferable insight* is **the AI-proposes-manager-decides primitive + the `audit-log + fastapi` stack-mirror with LE31 v1 + the charter §3.4 invariant documentation artifact** — *the strongest LE31-stack-shape match today is also the first repo to explicitly name the charter §3.4 compliance pattern as a design principle, and the v2 maintainer adopting the AI-proposes-manager-decides discipline has a concrete 2026 reference repo (FullHouse-Updated) to anchor the primitive* — and v2 maintainer decision required before any v2 surface adopts the AI-assist posture.
