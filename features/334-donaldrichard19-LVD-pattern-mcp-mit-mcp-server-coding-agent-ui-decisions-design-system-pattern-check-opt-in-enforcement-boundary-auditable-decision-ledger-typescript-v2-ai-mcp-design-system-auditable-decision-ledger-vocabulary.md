# Feature 334 — `donaldrichard19-LVD/pattern-mcp` MIT v2-AI MCP-server-design-system-pattern-check-+-auditable-decision-ledger-vocabulary (defer, parking-lot)

> **NEW observation (2026-10-17).** Documents in-window GitHub repo `donaldrichard19-LVD/pattern-mcp` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★9/⑂0**, **TypeScript** (off-stack but the *MCP-server-with-auditable-decision-ledger* vocabulary IS portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 via a future v2-AI PR), **19698 KB modest**, `default_branch=main`, **pushed 2026-10-16T20:29:35Z = in-window by `pushed_at` (yesterday's push)**, **created 2026-08-24T02:45:35Z** = ~2-month-old repo with in-window `pushed_at` = IN-WINDOW BY `pushed_at` ONLY (`created_at` is OUT-OF-WINDOW by ~47 days before window-start), **archived=`False`**). **11 topics** (verbatim, parent-verified GitHub API direct-GET 2026-10-17 from `/tmp/le31-daily-2026-10-17/verify/ghverify_donaldrichard19-LVD_pattern-mcp.json`): `ai + ai-agents + ai-agents-mcp + design + design-patterns + design-systems + mcp + mcp-server + ui-components + ui-design + ui-library` = **2nd-most-topic-rich v2-AI MCP-server-with-auditable-decision-ledger candidate of the 78-pass series** (11 topics = 2nd-highest topic count of any v2-AI MCP-server pick in the 78-pass series; only `musterhq/muster` at 16 topics is richer for the MCP-related cluster). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-17): *Pattern checks a coding agent's UI decisions against your own design system before it builds, whether that lives in code or in Figma. It helps the agent reuse what the product already has and build only what is actually missing. An opt-in enforcement boundary can make that check required, and every decision is recorded in an auditable ledger.*. The **MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger + code-or-Figma** quintuple-primitive + the **MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger** discipline (a coding agent's UI decisions are checked against a design system via an MCP-server; the check is opt-in enforcement = the developer chooses whether to make the check required; every decision is recorded in an auditable ledger for traceability) = the **canonical v2-AI MCP-server-with-auditable-decision-ledger-vocabulary of the 78-pass series**. Bucket: **v2-AI (parking-lot, vocabulary reference)** — Pick C of Daily Research 2026-10-17. Build verdict: `defer` (parking-lot, vocabulary-only). Zero build time today.

## Goal

Retain the **MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger + code-or-Figma** discipline as a persistent cross-section reference for the LE31 v2-AI *MCP-server-with-auditable-decision-ledger* surface, and document the **opt-in enforcement boundary** discipline (the developer chooses whether to make the check required; the default is advisory) that an independent maintainer arrived at in 2026 (2-month-old repo with yesterday-push) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger + code-or-Figma** quintuple-primitive: (1) *MCP-server* (the pattern-check is exposed via Model Context Protocol = standardized interface for AI-agent-tool-calls); (2) *design-system-pattern-check* (the pattern-check examines the agent's UI decisions against a design system); (3) *opt-in-enforcement-boundary* (the developer chooses whether to make the check required; the default is advisory); (4) *auditable-decision-ledger* (every decision is recorded in an auditable ledger for traceability); (5) *code-or-Figma* (the design system can live in code OR in Figma = the check works against both)
- A written record of the **MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger** discipline applied to the *coding-agent-UI-decisions* dimension: a *coding-agent-UI-decision* is checked against a design system via an MCP-server; the check is opt-in = the developer chooses whether to make it required; every decision is recorded in an auditable ledger
- A written record of the **opt-in enforcement boundary** posture: the developer chooses whether to make the check required; the default is advisory; the *opt-in* posture IS the §3.4 *non-AI-fallback* charter invariant applied to the *AI-agent-decision-enforcement* dimension (the developer can always opt out = the check is not a hard-gate by default; only when the developer explicitly opts in does the check become a hard-gate)
- A decision record: today's verdict is `defer (vocabulary-only, v2-AI MCP-server-with-auditable-decision-ledger with §3.4 review)` because (1) LE31 v1 charter explicitly scopes the v1 architecture to one small restaurant and excludes AI surface per charter §3.4 "no customer-facing AI"; (2) the *MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger* primitive IS a v2-AI owner-assistant surface that requires §3.4 review; (3) the *design-system-pattern-check* is unique to the UI/UX dimension = LE31 v1 has no UI design-system (LE31 v1 uses raw HTML + minimal HTMX); (4) the *MCP-server + auditable-decision-ledger* vocabulary IS portable to non-UI surfaces (any AI-agent-decision can be recorded in an auditable ledger via an MCP-server)

**Out of scope (defer artifact):**

- Any change to LE31 v1 (charter explicitly scopes the v1 architecture to one small restaurant; the v1 surface has no AI surface + no UI design-system)
- Any change to LE31 v2-AI surface today (charter §3.4 not yet triggered for v2-AI; the v2-AI bucket exists in the skill file but does NOT exist as a Linear project per today's confirmed workspace-state — only 3 projects exist: `le31 v1 — Core MVP`, `le31 Workflow`, `le31 Research`)
- **Adoption of the `pattern-mcp` codebase — explicitly NOT adopted because the codebase is TypeScript (off-§3.1 stack) + requires MCP-runtime (not on the LE31 v1 stack) which would require §3.1 + §3.2 + §3.4 charter review before adoption**
- Cross-pollination with the *Figma* surface (charter §3.7 §3.7 N/A = no PII; design-system patterns in Figma are public data; the Figma-integration is OFF-§3.1 = explicit charter-decision needed for any v1 PR)

## Evidence / JTBD

When a future LE31 v2-AI surface proposes *"the design-system enforcement boundary for AI-coding-agents-modifying-LE31-UI, with opt-in-enforcement-boundary + auditable-decision-ledger"*, the owner wants *a primitive that proves this MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger pattern is real and well-tested in 2026*, but struggles because *LE31 has no documented evidence that "MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger" is a real reference MCP-server-with-auditable-decision-ledger pattern*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the MCP-server-with-auditable-decision-ledger pattern"*.

- **Evidence class**: observed (the description names the primitives explicitly: `MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger + code-or-Figma`)
- **Confidence**: medium-high for the MCP-server-with-auditable-decision-ledger-vocabulary match (the verbatim description names the 5-primitive set); low for transferability (TypeScript off-§3.1 + MCP-runtime off-§3.1 + the *design-system-pattern-check* is unique to UI/UX = LE31 v1 has no UI design-system; but the *MCP-server + auditable-decision-ledger* vocabulary IS portable to non-UI surfaces)
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has no AI surface + no UI design-system; the v2-AI bucket is not yet open; the existing v1 owner-daily-recap does NOT include design-system-pattern-check; the *MCP-server + auditable-decision-ledger* posture is a forward-looking v2-AI vocabulary); the value is the **MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger** vocabulary — when the first v2-AI owner-assistant PR lands, the `pattern-mcp` pattern is a ready-made *named MCP-server-with-auditable-decision-ledger-primitive*

## Description

GitHub `donaldrichard19-LVD/pattern-mcp` (MIT, ★9/⑂0, TypeScript, 19698 KB modest, pushed 2026-10-16T20:29:35Z = in-window by `pushed_at`, created 2026-08-24T02:45:35Z = 2-month-old repo with in-window push). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-17):

> *Pattern checks a coding agent's UI decisions against your own design system before it builds, whether that lives in code or in Figma. It helps the agent reuse what the product already has and build only what is actually missing. An opt-in enforcement boundary can make that check required, and every decision is recorded in an auditable ledger.*

The MCP-server-with-auditable-decision-ledger primitive has 5 distinct sub-primitives that map 1:1 onto the LE31 v2-AI *MCP-server-with-auditable-decision-ledger* surface:

1. **MCP-server** — the pattern-check is exposed via Model Context Protocol (MCP) = standardized interface for AI-agent-tool-calls; the *MCP-server* posture IS the §3.1 *standardized-interface* charter invariant applied to the *AI-agent-tool-call* dimension (MCP is a 2026 industry standard; LE31 v2-AI surface would adopt MCP for tool-calls)
2. **Design-system-pattern-check** — the pattern-check examines the agent's UI decisions against a design system; the *design-system-pattern-check* posture IS the §3.4 *observable-evidence* charter invariant applied to the *AI-agent-UI-decision* dimension (the check provides observable evidence of whether the agent's UI decisions comply with the design system)
3. **Opt-in-enforcement-boundary** — the developer chooses whether to make the check required; the default is advisory; the *opt-in* posture IS the §3.4 *non-AI-fallback* charter invariant applied to the *AI-agent-decision-enforcement* dimension (the developer can always opt out = the check is not a hard-gate by default; only when the developer explicitly opts in does the check become a hard-gate)
4. **Auditable-decision-ledger** — every decision is recorded in an auditable ledger for traceability; the *auditable-decision-ledger* posture IS the §3.3 *audit-log-immutability* charter invariant applied to the *AI-agent-decision* dimension (LE31 v1 `audit_logs` is already append-only = the *auditable-decision-ledger* primitive is a future extension)
5. **Code-or-Figma** — the design system can live in code OR in Figma; the *code-or-Figma* posture IS the §3.7 *data-source-agnostic* charter invariant applied to the *design-system* dimension (the check works against both)

**The 1:1 mapping onto LE31 v1 + v2-AI surface:**

| `pattern-mcp` primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| MCP-server | `MCP` integration (proposed) | §3.1 | **Not implemented** — v2-AI surface not yet open; v1 has no MCP-runtime |
| Design-system-pattern-check | `DesignSystemPatternCheck` (proposed) | §3.4 | **Not implemented** — v1 has no UI design-system |
| Opt-in-enforcement-boundary | `OptInEnforcementBoundary` config (proposed) | §3.4 | **Not implemented** — v2-AI surface not yet open |
| Auditable-decision-ledger | `audit_logs` table (already append-only) + `AIDecisionLedger` extension (proposed) | §3.3 | **Partial (v1)** — `audit_logs` is append-only; the *auditable-decision-ledger* discipline is a v1 PR candidate (no §3.4 review needed) |
| Code-or-Figma | `DesignSystemSource` config (proposed; supports both code and Figma) | §3.7 | **Not implemented** — v1 has no UI design-system |
| **ACTUAL implementation** | pattern-mcp codebase (TypeScript + MCP-runtime + Figma-API) | §3.1 + §3.2 | **NOT adopted** — vocabulary-only; the MCP-server + opt-in-enforcement-boundary + auditable-decision-ledger primitives are vocabulary-portable; the design-system-pattern-check is OFF-§3.1 = explicit charter-decision needed; the TypeScript codebase itself is OFF-§3.1 |
| **Future re-implementation** | v2-AI owner-tooling in Python + FastAPI + Postgres + SQLModel + aiogram v3 + MCP-runtime | §3.1 + §3.2 + §3.4 | **Future v2-AI PR target** |

## Data model

This defer artifact does NOT modify any LE31 data model. The data model below describes the **vocabulary reference only**, not an actual v2-AI implementation:

- `AIDecisionLedger` (id, decision_by_agent_id: int, decision_type: str enum `[ui-decision, code-decision, config-decision, query-decision]`, decision_description: str, decision_audited_by: int, decision_recorded_at: datetime) — vocabulary reference: a SQLModel table that records each AI-decision (APPEND-ONLY; §3.3 invariant; v1 PR candidate = extend `audit_logs` with `decision_type` + `decision_by_agent_id` columns)
- `DesignSystemPattern` (id, pattern_name: str, pattern_source: str enum `[code, figma]`, pattern_definition: JSON, pattern_created_at: datetime) — vocabulary reference: a SQLModel table that records each design-system-pattern (v1 PR candidate; v1 has no UI design-system today)
- `OptInEnforcementBoundary` (id, boundary_name: str, boundary_required: bool, boundary_opted_in_by: int, boundary_opted_in_at: datetime) — vocabulary reference: a SQLModel table that records each opt-in-enforcement-boundary (v1 PR candidate; the *opt-in* discipline is directly applicable to v1 + v2-AI)

All tables would require §3.3 (append-only + auditable-decision-ledger) + §3.4 (opt-in-enforcement-boundary is operator-tooling AI; surface accepts the chokepoint-governed + human-gate + observable-evidence + non-AI-fallback charter invariant) charter review before adoption.

## Implementation steps

This is a defer artifact (vocabulary-only). No implementation today. The 3 placeholder steps below document the future-v1 + v2-AI re-implementation path:

1. **Defer (vocabulary-only today)** — file the contract; no code change
2. **Re-evaluate at first v1 PR that proposes auditable-decision-ledger-extension to `audit_logs`** — when a future v1 PR proposes extending `audit_logs` with `decision_type` + `decision_by_agent_id` columns for AI-decision-audit, the `pattern-mcp` pattern is a ready-made *named auditable-decision-ledger-primitive*; re-run the LE31 feature gate (no §3.4 review needed for v1 PR)
3. **Re-implement in Python+FastAPI+Postgres+SQLModel+aiogram v3** — if the future v2-AI PR adopts the `pattern-mcp` vocabulary, re-implement from scratch in the LE31 v2-AI stack (Python+FastAPI+Postgres+SQLModel+aiogram v3 + MCP-runtime); do NOT add `pattern-mcp` to `requirements.txt`; design the v2-AI surface as a fresh Python+FastAPI+Postgres+SQLModel+aiogram v3 implementation that captures the *MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger* primitives

## Telegram interaction

This defer artifact does NOT add any Telegram interaction today. The future v2-AI MCP-server-with-auditable-decision-ledger surface would add Telegram commands (operator-tooling; charter §3.4 NOT triggered for the owner-bot exposure; charter §3.4 RIPGL_REVIEW REQUIRED if any Telegram-client exposure is added to restaurant diners):

- `/ai-decision show <decision_id>` — owner shows an AI-decision from the auditable-decision-ledger
- `/ai-decision list` — owner lists all AI-decisions
- `/ai-decision verify <decision_id>` — owner verifies an AI-decision against the design-system
- `/ai-decision opt-in <boundary_name>` — owner opts-in to an enforcement-boundary
- `/ai-decision opt-out <boundary_name>` — owner opts-out of an enforcement-boundary

## Dependencies

- **No new LE31 v1 dependencies** — this is a vocabulary-only defer artifact; the *auditable-decision-ledger* primitive is a v1 PR candidate (extend `audit_logs` with `decision_type` + `decision_by_agent_id` columns; no §3.4 review needed)
- **Future v1 PR dependencies** (would require §3.3 charter review; NO §3.4 review needed):
  - `audit_logs` table extension (already on v1 stack)
- **Future v2-AI re-implementation dependencies** (would require §3.1 + §3.2 + §3.4 charter review):
  - MCP-runtime (Python or TypeScript; OFF-§3.1 = explicit charter-decision needed)
  - Figma-API (for Figma-integration; OFF-§3.7 = explicit charter-decision needed)
- **Sister-shape** via the v2-AI MCP-server-with-auditable-decision-ledger-vocabulary cluster:
  - features 232 (`lpalbou/AbstractGateway` HTTP control plane for durable AI runs + append-only ledger + Telegram surface)
  - features 287-289 (the persistent v2-AI audit-trail-decision vocabulary cluster)
  - features 298 (carry-over from 10-13 `the-vibey-project/vibey` agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger)
  - features 302 (`warrant-ai/warrant` decision-ledger)
  - features 306 (`gtheonse/resortflow` hold-then-confirm-saga-concierge)
  - features 312 (`Alex8791-cyber/cognithor` local-first-agent-OS)
  - features 313 (`jklthinking/retinue` self-hosted-AI-worker-coordination)
  - features 327 (carry-over from 10-16 `musterhq/muster` agent-harness-with-audit-ledger-+-token-waste-ledger)
  - features 332 (today's `vsov/xcheck` cross-agent-audit-methodology)
  - features 333 (today's `FlashyLabs/flashy-ledger` append-only-hash-chained-ledger-rules)

## Open questions

- **Could the existing v1 `audit_logs` table be extended with `decision_type` + `decision_by_agent_id` columns for AI-decision-audit?** This is the cheapest path; a v1 PR could add the columns and reuse the existing append-only primitive; no §3.4 review needed
- **Should LE31 v1 adopt the *opt-in enforcement boundary* discipline for non-AI work?** The discipline is vocabulary-portable to non-AI work (e.g. opt-in boundary for cook-vs-waiter-order-validation); a v1 PR could adopt the discipline without §3.4 review
- **Could the *design-system-pattern-check* discipline be applied to LE31 v1's existing UI?** LE31 v1 uses raw HTML + minimal HTMX; there is no formal design-system today; a v1 PR could formalize a design-system + adopt the pattern-check discipline without §3.4 review
- **What is the relationship between the *MCP-server* primitive and the existing v1 `audit_logs` table?** The MCP-server would call into the existing v1 `audit_logs` table for the *auditable-decision-ledger* discipline; the v1 PR would add the `decision_type` + `decision_by_agent_id` columns + the MCP-server integration
- **Should the *opt-in enforcement boundary* default to *advisory* or *required* for v2-AI?** The `pattern-mcp` discipline defaults to *advisory*; the developer opts-in to *required*; the LE31 v2-AI surface would adopt the same default (advisory = non-AI-fallback = charter §3.4)

## Why this matters

This is the **canonical v2-AI MCP-server-with-auditable-decision-ledger-vocabulary of the 78-pass series**. The 5-rule *MCP-server + design-system-pattern-check + opt-in-enforcement-boundary + auditable-decision-ledger + code-or-Figma* discipline is a unique cross-section reference that no other v2-AI pick in the 78-pass series captures. The transferability to LE31 v1 is medium (1 of 5 rules is a v1 PR candidate; 4 of 5 rules are v2-AI forward-looking); the transferability to LE31 v2-AI is high (the 5 rules are vocabulary-portable to Python+FastAPI+Postgres+SQLModel+aiogram v3 + MCP-runtime); the cost is low (vocabulary-only artifact, no code today); the trigger condition is clear (first v1 PR that proposes auditable-decision-ledger-extension OR first v2-AI surface that wants MCP-server-with-auditable-decision-ledger). Per the 9-feature-pipeline-rule + the 77+ passes of consistency, parking-lot `defer` is the verdict. The artifact is the persistent cross-section reference for any future v1 PR that proposes auditable-decision-ledger-extension OR any future v2-AI PR that proposes MCP-server-with-auditable-decision-ledger. LE31 v2-AI surface is not yet open. All ripgrep-verified unique vs features 1..331. **Fully reversible** (vocabulary-only artifact).
