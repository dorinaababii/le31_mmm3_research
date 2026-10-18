# Slice Handoff — Feature 339 (vggg/barony)

> **Feature ID**: 339
> **Feature path**: `/opt/data/le31_mmm3_research_work/features/339-vggg-barony-mit-git-native-governance-ai-coding-agents-persona-charters-enforced-capabilities-ledgers-divergence-radar-audit-v2-ai-git-native-governance-persona-charters-vocab.md`
> **Decision**: defer (parking-lot, vocabulary reference)
> **Bucket**: v2-AI

## LE31 feature gate verdict (carried from feature contract)

- **Evidence precondition**: inferred (vocabulary observation, not observed LE31 user pain). Confidence: medium.
- **Seven checks**:
  1. **JTBD**: When a v2-AI agent assists the owner/staff with a multi-step workflow, the operator wants every agent to operate under a persona-charter + enforced capabilities + divergence radar.
  2. **Viability**: medium — non-technical owner/staff would need help to interpret persona-charter / divergence-radar artifacts.
  3. **Practicability and confidence**: medium — Python on-stack; the git-native-anchoring implementation is NOT portable to LE31 (LE31 anchors in Postgres per charter §3.3 + §3.1); the *persona-charter-first + enforced-capabilities + divergence-radar* vocabulary IS portable.
  4. **Conflict**: no hard conflict with any charter invariant; persona-charter would need a GDPR-compliance clause per charter §3.7.
  5. **Outcome / appetite / scope**: v2-AI outcome; 0 build time today; max 4 weeks per pick if a v2-AI window opens.
  6. **Cost to operational value**: low RICE; not a v1 PR candidate.
  7. **Circuit breaker / reversibility**: fully reversible (vocabulary-only artifact; no code adoption).
- **Decision**: **defer (parking-lot, vocabulary reference)**.

## Files this slice will touch (when implemented)

> Not implemented today. When a v2-AI window opens, the implementation will touch:

- `app/v2/ai/personas/__init__.py` — new package
- `app/v2/ai/personas/models.py` — `PersonaCharter` + `CapabilityEnforcementLog` + `DriftEvent` SQLModel tables (all append-only per charter §3.3)
- `app/v2/ai/personas/router.py` — FastAPI router under `/v2/ai/personas` with CRUD endpoints
- `app/v2/ai/personas/templates/` — HTMX templates for the operator-facing persona-charter-management UI
- `app/v2/ai/personas/enforcement.py` — `capability_enforcement_check` decorator that wraps every AI-agent action and rejects out-of-scope actions
- `app/v2/ai/personas/drift.py` — `drift_detection` background task that compares recent AI-agent actions against persona-charter constraints
- `app/v2/ai/personas/tests/` — verify the capability-enforcement rejects out-of-scope actions + the drift-detection surfaces drift
- `migrations/` — alembic migration for the new tables

> **Greenfield**: no existing v1 files are touched by this slice (LE31 v1 has no AI agent surface).
> **Postgres-anchored (not git-anchored)**: the barony vocabulary *anchors* all three tables in Postgres (not in git) per LE31 charter §3.3 + §3.1; the *git-native-anchoring* implementation is NOT portable to LE31 v2-AI.

## Verification protocol (when implemented)

1. Run `pytest app/v2/ai/personas/tests/` and verify all tests pass.
2. Manually create a persona-charter with explicit capabilities; verify the router persists it.
3. Manually attempt an AI-agent action outside the persona-charter's capabilities; verify the `capability_enforcement_check` decorator rejects the action.
4. Manually trigger the `drift_detection` background task; verify the task surfaces drift events for actions that violated the persona-charter.
5. Verify the HTMX persona-charter-management UI renders the charter list + the drift event list.
6. Verify the integration with the v2-AI surface (if the v2-AI surface is already implemented).

## Rollback path

- `git revert <commit-hash>` to remove the v2-AI persona-charter surface.
- `alembic downgrade -1` to drop the new tables.
- No v1 data is affected (greenfield; no migration of existing v1 data).
- All `CapabilityEnforcementLog` + `DriftEvent` rows are append-only per charter §3.3; they remain in the audit trail even after the rollback.

## Mandatory LE31 skill list for the external coding agent

Before starting, the external coding agent MUST load these skills:

1. **`le31-conventions`** — the global LE31 decision layer + feature gate + hard invariants.
2. **`le31-v1-feature-pattern`** — the canonical contract shape + slicing rules + definition of done.
3. **`le31-handoff-spec`** — the handoff discipline + frozen contract + verification protocol.
4. **`le31-coding-agent-brief`** — the paste-in prompt template that produces the slice prompt from this HANDOFF.
5. **`le31-research`** — the research workflow + evidence-before-recommendation discipline.
6. **`development`** — the generic code-development pipeline (specify → plan → tasks → implement).

## Trigger policy for the external coding agent

- **DO NOT start** until a v2-AI workflow window opens in the LE31 charter roadmap.
- **DO NOT start** until a future v2-AI PR proposes a multi-agent governance surface with persona-charters, a capability-enforcement gate for AI-agent-action, a divergence-radar / drift-detection surface, or a git-anchored or Postgres-anchored audit-ledger for AI-agent-action.
- **DO NOT start** until the charter §3.4 AI-sandbox-as-auditable-test review has been completed.
- **DO NOT adopt** the barony `git-native-anchoring` implementation; LE31 v2-AI anchors in Postgres per charter §3.3 + §3.1.
- When triggered, mirror back the frozen contract fields before implementing; stop if the mirror-back does not match.

## External-context Linear reference

- Parent research issue: Research 2026-10-18 — daily (Linear MCP BLOCKED 29th consecutive day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-18.linear-fallback.json` documents the intended parent + 3 sub-issues).
- This feature: Feature 339 — vggg/barony (intended sub-issue in `le31 Research` P-HMM-1).

## Sign-off gap

- External agent has NOT yet been dispatched.
- Charter §3.4 review has NOT yet been completed.
- v2-AI workflow window has NOT yet opened.
- No v1 PR today.

## Cross-references

- Feature contract: `/opt/data/le31_mmm3_research_work/features/339-...md`
- Source artifact: `/opt/data/le31-daily-research-2026-10-18.md` (pick B)
- Sister-shapes: features 316/322 (the-vibey-project/vibey), 187/188 (traust-security/traust-ledger), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 327 (musterhq/muster), 332/333/334 (vsov/xcheck + FlashyLabs/flashy-ledger + donaldrichard19-LVD/pattern-mcp), 338 (agentdrover/haiplane).