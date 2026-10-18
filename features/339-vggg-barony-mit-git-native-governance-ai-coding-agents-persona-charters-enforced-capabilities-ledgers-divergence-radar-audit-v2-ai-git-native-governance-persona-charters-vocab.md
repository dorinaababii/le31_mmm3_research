# Feature 339 — vggg/barony (v2-AI git-native-governance-for-AI-coding-agent-teams-+-persona-charters-+-enforced-capabilities-+-ledgers-+-divergence-radar-+-audit)

> **Bucket**: v2-AI (parking-lot, vocabulary reference)
> **GitHub**: https://github.com/vggg/barony
> **License**: MIT
> **Status (as of 2026-10-18)**: ★9 / ⑂1; 2 KB tiny; pushed 2026-10-18T00:53:18Z (TODAY); created 2026-05-22T20:16:45Z (~5 months old); default_branch=main; archived=False
> **Topics (verbatim, 0)**: `[]` (no GitHub topics; empty array)
> **Description (verbatim)**: *Barony — git-native governance for teams of AI coding agents: persona charters, enforced capabilities, ledgers, divergence radar, audit. CLI: baron.*
> **Star-density signal**: 9★ for a 2 KB tiny repo = strongest star-density signal of any v2-AI pick of the 79-pass series
> **Cross-section**: features 81/96/97/121/122/126/127/134/137/141/145/167/168/169/181/183/187/188/189/190/191/192/193/196/232/268/287/288/289/296/297/299/310/327/332/333/334/338 (the persistent v2-AI agent-governance + audit-ledger + persona-charter cluster)
> **Decision**: defer (parking-lot, vocabulary reference)
> **Parent research issue**: Research 2026-10-18 — daily (Linear MCP blocked; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-18.linear-fallback.json`)
> **Slice handoff**: `/opt/data/le31_mmm3_research_work/specs/339-vggg-barony-mit-git-native-governance-teams-ai-coding-agents-persona-charters-enforced-capabilities-ledgers-divergence-radar-audit-HANDOFF.md`

## Goal

When a future v2-AI LE31 workflow introduces AI-assisted features for the owner/staff, the system wants every AI coding agent to operate under a **persona-charter** that the operator writes, with **enforced capabilities** (a git hook rejects out-of-scope actions), and **divergence radar** that surfaces when an agent has drifted from its charter, but today AI agents operate without persona-charters, without capability enforcement, and without drift detection, so that the operator cannot govern what an AI agent is allowed to do or detect when it has drifted.

## Evidence / JTBD

**Inferred** (vocabulary observation, not observed LE31 user pain). The pain is *possible* in any future v2-AI workflow window but is not *directly observed* in any LE31 v1 user flow today.

When a v2-AI agent assists the owner/staff with a multi-step workflow, the operator wants every agent action to be **bounded by acceptance criteria** (Pick A: haiplane), **governed by a persona-charter** (Pick B: barony), and **logged in a shared append-only work ledger** (Pick C: worklog), but struggles because today AI agents operate without explicit acceptance gates, without persona-charters, and without cross-session-persistent-context, so that the workflow audit trail is incomplete and the operator cannot reconstruct what the agent did or why.

Confidence: **medium** (the maintainer is shipping real code + 9 stars for a 2 KB tiny repo = strong signal that the primitive works + the maintainer is responsive to user feedback; the vocabularies are transferable to a Python+FastAPI+Postgres+SQLModel+aiogram v3 stack with a charter §3.4 review).

## Scope

- v2-AI only: applies to a future v2-AI workflow window (operator + staff tooling, not customer-facing).
- The transferable vocabulary is the **persona-charter-first-agent-onboarding** sextuple-primitive: persona charters + enforced capabilities + ledgers + divergence radar + audit + git-native-anchoring.
- The Python stack is portable to LE31 v2-AI with a charter §3.4 review (AI-sandbox-as-auditable-test + non-AI-fallback + observable-evidence).
- No v1 PR today; no v1 build today; no quota-filling.

## Out of scope

- v1 product surface (waiter web UI + cook Telegram bot). LE31 v1 has no AI agent surface.
- Any customer-facing AI per charter §3.4 (the barony vocabulary is operator-tooling only).
- Any runtime import of barony as a dependency (the barony codebase is the vocabulary reference, not the code dependency).
- Any LE31-specific schema migration or model change (barony is vocabulary-only; the v2-AI surface is greenfield).
- The "git-native" aspect is the most transferable primitive; LE31 v2-AI would adopt the *persona-charter + enforced-capabilities + divergence-radar* vocabulary without necessarily adopting the *git-native-anchoring* implementation (LE31 v2-AI would anchor in Postgres per charter §3.3 + charter §3.1).

## Description

The barony vocabulary is the **git-native-governance-for-AI-coding-agent-teams** sextuple-primitive:

1. **Persona charters** — every AI coding agent operates under a written persona-charter that the operator writes. The persona-charter is a Markdown file in the repo (`.barony/personas/<agent>.md`) that describes the agent's role, scope, capabilities, and constraints. This is the **persona-charter-as-governance-document** discipline.
2. **Enforced capabilities** — the agent's capabilities are enforced via git hooks. When an agent attempts an action outside its persona-charter, the hook rejects the action. This is the **capability-as-git-hook-rejection** discipline applied to AI-agent-action-mediation.
3. **Ledgers** — every agent action is recorded in a git-anchored ledger (a structured log file in the repo). The ledger is append-only and is committed to git on every agent action. This is the **git-anchored-audit-ledger** discipline (charter §3.3 primitive applied to AI-agent-action).
4. **Divergence radar** — the system surfaces when an agent has drifted from its persona-charter. The drift detection compares the agent's recent actions against its persona-charter constraints and reports drift. This is the **drift-detection-as-continuous-monitoring** discipline applied to AI-agent-governance.
5. **Audit** — every agent action is auditable via the git history (the ledger is committed to git; the persona-charter is committed to git; the drift events are committed to git). This is the **git-history-as-audit-trail** discipline (the audit trail is the git log itself).
6. **Git-native-anchoring** — the entire governance system is anchored in git (not in a separate database). This means the governance is reproducible from the git history alone, without any external state. This is the **git-as-source-of-truth** discipline applied to AI-agent-governance.

The Python stack + the 9★ for 2 KB tiny = strongest star-density signal of any v2-AI pick of the 79-pass series.

## Data model

No LE31 schema change today. The barony vocabulary is operator-tooling infrastructure that would be introduced in a future v2-AI window. The data model for a future barony-style v2-AI governance surface would be:

- `PersonaCharter` — id, agent_id, role, scope (JSONB), capabilities (JSONB), constraints (JSONB), created_at, updated_at, committed_sha (the git commit that authored the charter)
- `CapabilityEnforcementLog` — id, agent_id, attempted_action, was_allowed, rejection_reason, persona_charter_id, created_at (append-only per charter §3.3)
- `DriftEvent` — id, agent_id, persona_charter_id, drift_type, drift_severity, evidence (JSONB), detected_at, resolved_at (append-only per charter §3.3)

The barony vocabulary *anchors* all three tables in Postgres (not in git) per LE31 charter §3.3 + §3.1; the *vocabulary* of persona-charter-first + enforced-capabilities + divergence-radar is portable; the *git-native-anchoring* implementation is not portable to LE31 v2-AI (LE31 anchors in Postgres).

## Implementation steps

Not implemented today (parking-lot). When a v2-AI window opens, the implementation would be:

1. Add a `persona_charters` SQLModel table with the schema above.
2. Add a FastAPI router under `/v2/ai/personas` with CRUD endpoints.
3. Add a `capability_enforcement_check` decorator that wraps every AI-agent action and rejects out-of-scope actions per the persona-charter.
4. Add a `drift_detection` background task that compares recent AI-agent actions against persona-charter constraints and surfaces drift events.
5. Add an HTMX template for the operator-facing persona-charter-management UI.
6. Add an integration test that verifies the capability-enforcement rejects out-of-scope actions + the drift-detection surfaces drift.

## Telegram interaction

If a future v2-AI operator workflow adopts barony vocabulary, the operator Telegram bot would gain:
- `/personas` — list all persona-charters + their capabilities
- `/persona <agent_id>` — show a specific persona-charter
- `/drift` — show recent drift events
- `/resolve_drift <drift_event_id>` — mark a drift event resolved

The `/drift` command surfaces the **divergence-radar** discipline at the operator-side.

## Dependencies

- A future v2-AI window opening (no v1 PR today).
- Charter §3.4 review (AI-sandbox-as-auditable-test + non-AI-fallback + observable-evidence).
- The barony codebase is the vocabulary reference; no runtime dependency on the barony project itself.
- The drift-detection requires a persona-charter comparison engine; LE31 v2-AI would build this on Postgres + a periodic background task.

## Open questions

- Is the LE31 v2-AI workflow window opening in 2026-Q4 or later? (parent has no visibility into the charter roadmap).
- Does a future v2-AI workflow actually need a persona-charter-governance surface, or is the existing v1 `audit_logs` append-only ledger sufficient for operator-side audit? (likely yes for any multi-agent workflow).
- Should the barony vocabulary be combined with the haiplane vocabulary (Pick A) for persona-charter-governed acceptance-criteria, or should they be adopted independently? (likely independently first, then combined).
- Should LE31 v2-AI anchor the governance in git (barony's choice) or in Postgres (LE31's choice)? (LE31's choice is Postgres per charter §3.3 + §3.1).
- How does barony's persona-charter interact with charter §3.7 GDPR scope? (the persona-charter would need to include a GDPR-compliance clause).

## Why this matters

The barony vocabulary is the **canonical persona-charter + divergence-radar + git-anchored-audit-ledger discipline** of the 79-pass series. It is the strongest v2-AI governance primitive that the LE31 project has observed, and the adoption is **fully reversible** (vocabulary-only artifact; no code dependency). When a v2-AI window opens, the barony vocabulary becomes the actionable governance reference for any LE31 v2-AI workflow that needs to govern multiple AI coding agents on multi-step restaurant operations tasks.

Charter §3.4 alignment is strong: barony enforces capabilities via git hooks (chokepoint-governed) + requires persona-charter (human-gate) + anchors every action in a ledger (observable-evidence) + has a non-AI-fallback (the operator can manually approve any agent action via the persona-charter management UI).

Sister-shape cross-section: features 316/322 (the-vibey-project/vibey, which uses append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive), 187/188 (traust-security/traust-ledger), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 327 (musterhq/muster), 332/333/334 (vsov/xcheck + FlashyLabs/flashy-ledger + donaldrichard19-LVD/pattern-mcp), 338 (agentdrover/haiplane).

## Trigger condition

Re-evaluate when:
1. A v2-AI workflow window opens in the LE31 charter roadmap.
2. A future v2-AI PR proposes a multi-agent governance surface with persona-charters.
3. A future v2-AI PR proposes a capability-enforcement gate for AI-agent-action.
4. A future v2-AI PR proposes a divergence-radar / drift-detection surface.
5. A future v2-AI PR proposes a git-anchored or Postgres-anchored audit-ledger for AI-agent-action.

At that point, the barony vocabulary becomes actionable for the LE31 v2-AI surface.