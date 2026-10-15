# HANDOFF — Feature 316: `the-vibey-project-vibey-mit-ai-coding-agents-orchestrator-append-only-postgresql-ledger-crash-safe-resumable-v2-ai-agent-orchestration-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **Note on filename**: the HANDOFF filename uses the full slug per the v1 feature contract shape (see `features/316-…-vocabulary.md`).

## Active feature path

`features/316-the-vibey-project-vibey-mit-ai-coding-agents-orchestrator-append-only-postgresql-ledger-crash-safe-resumable-v2-ai-agent-orchestration-vocabulary.md` — defer/parking-lot (Pick C of Daily Research 2026-10-13 carry-over).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface needs AI-agent-orchestration with crash-safe append-only PostgreSQL-ledger recovery, *the owner-cook-reviewer wants* orchestrator that records the crashed-agent's work in the append-only ledger so it can be picked up by another agent instead of being lost, *but struggles because* today's AI-agent-orchestrators store state in either local-filesystem (unrecoverable across crashes) or in-memory (lost on restart), *so that* the crashed-agent's partial work survives across agent-session-boundaries. |
| 2 | Viability | ✓ | Single-developer v2-AI surface (requires Python+Postgres operator skills; viable per charter §3.1 + §3.2); vocabulary-only artifact today; REVERSIBLE. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + PostgreSQL ✓ ON-STACK. The 2/2 LE31-backend-stack-match + the unique append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive = the strongest in-window 2026 v2-AI agent-orchestrator-with-crash-safe-append-only-PostgreSQL-ledger peer of the 75-pass series. 20 topics = the most topic-rich v2-AI orchestrator of the 75-pass series (tied with `djust-org/djust` at 20-topic threshold). Rabbit hole: the v2-AI bucket is undefined per charter §3.4 (no operator-AI surface exists in v1 today). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *append-only-PostgreSQL-ledger* primitive is consistent with LE31's charter §3.1 invariant that operational transitions are explicit user actions (the ledger's append-only-nature aligns with the §3.1 stock-ledger append-only rule). The *crashed-agent-resumable* primitive is consistent with charter §3.4 *AI may assist owner/staff with observable evidence* (the spec-interview + human-gated-review are the observable-evidence primitives). No §3.4 customer-facing AI. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI polish outcome (AI-agent-orchestration surface for the LE31 single-restaurant Swiss kitchen). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the v2-AI bucket is undefined per charter §3.4; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot, v2-AI cross-section)** — 7/7 gate checks pass; build verdict `defer` because the v2-AI bucket is undefined per charter §3.4 + the code is not adoptable (the *AI-agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger* primitive is a v2-AI polish surface; v2-AI is undefined per charter §3.4).

## Bucket

**v2-AI** (agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 7-tuple-primitive set (open-source-orchestrator + spec-interview + unattended-builds + human-gated-review + append-only-PostgreSQL-ledger + crashed-agent-resumable + 20-topics).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review* discipline on a v2-AI AI-orchestrator surface lands, the files to touch are:
- `backend/alembic/versions/` — add migration for `AIAgentSession`, `AIAgentAction`, `AIAgentSpecInterview` tables.
- `backend/ai_agent_orchestrator.py` — new file with `AIAgentOrchestrator` class.
- `backend/ai_agent_spec_interview.py` — new file with `AIAgentSpecInterviewService` class.
- `backend/ai_agent_ledger_replayer.py` — new file with `AIAgentLedgerReplayer` class.
- `backend/main.py` — add `/api/ai-orchestrator` FastAPI endpoint set.

## Verification protocol reference

When the first v2-AI PR that adopts the *append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review* discipline lands, the verification protocol is:
1. Run `pytest tests/test_ai_agent_orchestrator.py` and verify the orchestrator produces a valid v2-AI session.
2. Run `pytest tests/integration/test_ai_agent_ledger_replayer.py` and verify the replayer recovers a crashed-agent session from the append-only-PostgreSQL-ledger.
3. Run `uvicorn backend.main:app` and curl `/api/ai-orchestrator` to verify the endpoint returns the session as JSON.
4. Inspect the `AIAgentAction` table in Postgres and verify every orchestrator-action writes an append-only entry (the §3.1 append-only-ledger invariant).

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review* discipline lands, the rollback path is:
1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the three tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:
- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules (NB: this is v2-AI bucket, but the v1 contract shape still applies for now; v2-AI uses the same slicing rules).
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v2-AI PR that adds a v2-AI agent-orchestrator-with-crash-safe-append-only-PostgreSQL-ledger recovery surface to the LE31 single-restaurant Swiss kitchen** lands. At that point:
1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which AI-agent-session (prep-scheduling? menu-pricing? recipe-scaling?), which AI-agent-action (add Pydantic schema? delete Pydantic schema?), which AI-agent-spec-interview (question + answer), and which existing v1 surface to inherit the Pydantic schemas from.
3. Adopt the *append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review* discipline on the existing v1 append-only `audit_logs` SQLModel table.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v2-AI code is shipped.