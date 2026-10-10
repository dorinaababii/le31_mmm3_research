# HANDOFF — Feature 301: `New1Direction-korg-...-v2-ai-verifiable-cognition-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/301-New1Direction-korg-mit-verifiable-cognition-ai-agents-tamper-evident-replayable-ledger-what-agent-did-why-korg-ledger-spec-rust-v2-ai-verifiable-cognition-vocabulary.md` — defer/parking-lot (Pick C of Daily Research 2026-10-10).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *verifiable-cognition + tamper-evident + replayable + ledger-of-what-an-agent-did-and-why + named-spec (korg-ledger spec)* primitive, the owner wants *evidence that this verifiable-cognition-vocabulary exists in 2026 with a deterministic-replay shape + named-spec framing*, but struggles because *most v2-AI audit-ledger candidates lack deterministic-replay semantics OR lack a named-spec framing*, so that *the v2-AI surface has a credible peer reference with a named spec (korg-ledger spec) that any future v2 surface can reference*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (verifiable cognition + tamper-evident + replayable). The 4★ with single-maintainer cadence (142-day-old repo, in-window push today) makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **Rust off-stack but the korg-ledger spec is a *specification*, not a code dependency** (the spec is portable to Python). The `deterministic` topic suggests a §3.1-aligned deterministic-replay discipline. Required data + permissions + infrastructure: Python runtime + hash-chained replay-log. Rabbit hole: the Rust core (LE31 stack is Python-only); the spec framing bridges this. Evidence strength: high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant as a vocabulary reference. The `autonomous-agents` topic is OFF v1 charter (v2-AI surface). The `korg-core + korg-ledger` spec is OFF v1 charter (v2-AI spec adoption). The *deterministic + replayable + audit* primitives are §3.1-aligned (append-only discipline + explicit state transitions). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI outcome (verifiable-cognition surface). Maximum time worth spending: 30 min documentation. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | ~15 min documentation; zero code cost. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + Rust core off-LE31-stack + korg-core runtime is OFF v1 charter + no v2-AI surface in v1 charter).

## Bucket

**v2-AI** (verifiable-cognition-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the 5-primitive set (`verifiable cognition + tamper-evident + replayable + ledger of what an agent did and why + korg-ledger spec`) + the tech-stack (Rust + korg-core + korg-ledger spec + mcp + runtime).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires deterministic-replay + tamper-evident + what-did-the-agent-do-and-why + named-spec):

1. `backend/app/agent_audit/models.py` — add new `AgentAction` SQLModel table with columns: `id` (UUID), `agent_id` (str), `action` (str), `reasoning` (str), `proposed_payload` (JSON), `actual_payload` (JSON), `deterministic_state_hash` (str), `previous_action_hash` (str), `this_action_hash` (str), `created_at` (timezone-aware datetime), `recorded_at` (timezone-aware datetime).
2. `backend/app/agent_audit/models.py` — add new `korg_ledger_spec_compliance` SQLModel table that tracks the spec compliance per action.
3. `backend/alembic/versions/` — add Alembic migration for the new tables.
4. `backend/app/agent_audit/repository.py` — add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `AgentAction` insert path.
5. `backend/app/agent_audit/deterministic_state.py` — NEW: deterministic-state-hash utility (uses `pydantic` for the deterministic serialization).
6. `backend/app/api/v2/agents/audit.py` — NEW: `POST /v2/agents/<agent_id>/actions` endpoint to record an action.
7. `backend/app/api/v2/agents/audit.py` — NEW: `GET /v2/agents/<agent_id>/actions/replay?start=<>&end=<>` endpoint that deterministically replays the agent's actions from a starting state.
8. `backend/app/api/v2/agents/audit.py` — NEW: `GET /v2/agents/<agent_id>/actions/explain?action_id=<>` endpoint that explains *what-did-the-agent-do-and-why* for a given action.
9. `backend/app/api/v2/audit_log.py` — NEW: `GET /v2/audit-log/spec-compliance` endpoint that reports the korg-ledger-spec compliance.
10. `backend/app/mcp_server/agents.py` — NEW: MCP-server integration that exposes the replay + explain endpoints via MCP (uses `mcp` library).
11. `PROJECT_CHARTER.md` — append the `korg-ledger spec` adoption as a v2-AI surface primitive (charter decision required).
12. `skills/le31-conventions/SKILL.md` — append the `korg-ledger spec` as a §3.1-aligned v2-AI audit-log pattern.

## Verification protocol

1. `git clone https://github.com/New1Direction/korg` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/New1Direction/korg/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set + korg-ledger spec).
3. `curl -sS -H "Authorization: Bearer $HERME...OKEN" "https://api.github.com/repos/New1Direction/korg"` for star count, fork count, license, language, pushed_at, created_at, topics, description (parent-verified 2026-10-10).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the AgentAction + replay + explain + spec-compliance + MCP changes are isolated to the expected files.
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec` before any implementation.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2-AI trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the new tables + remove the new API endpoints + remove the MCP-server integration + revert the `PROJECT_CHARTER.md` and `skills/le31-conventions/SKILL.md` changes.
- No data loss if the rollback happens BEFORE any AgentAction row is written.
- Full data retention if the rollback happens AFTER rows are written (the new tables are dropped but the original `audit_logs` rows are preserved per the *append-only* invariant).

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (append-only StockEntry, etc.).
4. `le31-handoff-spec` — the handoff-spec requirements (frozen contract discipline, mandatory skill list, verification protocol).
5. `le31-feature-pipeline` — the feature-pipeline workflow (parent research issue, sub-issue creation, handoff file).

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-10 / Pick C — v2-AI verifiable-cognition-vocabulary (New1Direction/korg)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-10.linear-fallback.json`. Sub-issue project = `le31 Research` (P-HMM-1) per `le31-feature-pipeline/SKILL.md` line 33 since `le31 v2-AI` does not exist.

## Parent research issue

[linear: blocked — workspace plan-limit error 20th consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-10.linear-fallback.json`]
