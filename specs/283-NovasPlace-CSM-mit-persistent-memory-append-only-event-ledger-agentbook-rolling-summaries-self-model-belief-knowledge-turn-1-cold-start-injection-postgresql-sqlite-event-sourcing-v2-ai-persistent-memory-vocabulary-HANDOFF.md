# Handoff — Feature 283 — v2-AI persistent-memory-vocabulary (defer)

> **Pick:** `NovasPlace/CSM` — v2-AI cross-section reference for **persistent-memory + operational-continuity + append-only-event-ledger-named-AgentBook + rolling-summaries + self-model + belief-knowledge + turn-1-cold-start-frontpage-injection + postgresql + sqlite + event-sourcing** primitive. **Highest-star v2-AI candidate of the 68-pass series (43★/8⑂)**.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v2-AI surface that adopts the *AgentBook + rolling-summaries + self-model + belief-knowledge + cold-start-frontpage-injection* primitives.
> **Source:** Daily Research 2026-10-06 (68th consecutive daily-research pass) → Pick C.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/283-NovasPlace-CSM-mit-persistent-memory-append-only-event-ledger-agentbook-rolling-summaries-self-model-belief-knowledge-turn-1-cold-start-injection-postgresql-sqlite-event-sourcing-v2-ai-persistent-memory-vocabulary.md`
> **Raw fetches:** `/tmp/le31-daily-2026-10-06/ghverify__parent_NovasPlace_CSM.json` (parent-verified direct GitHub API GET, raw JSON, 5.6 KB)
> **OFF-STACK WARNING:** language is TypeScript; LE31 v1 stack is Python+HTMX; per carry-over convention this is a vocabulary-only reference, not a code-import candidate.

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 v2-AI control-plane wants to run an AI coding agent that assists the developer, the developer wants the agent to have persistent-memory across sessions via an append-only-event-ledger-named-AgentBook with rolling-summaries, self-model, belief-knowledge, and turn-1-cold-start-frontpage-injection for deterministic cold-start, but struggles because the existing audit_logs SQLModel table is a flat log without persistent-memory or self-model, so that an AI coding agent can resume from a known-good state on a new session with full continuity. **v2-AI expansion → NEW pain** |
| 2 | Viability | ✓ viable as a vocabulary reference | Non-technical owner CAN understand (the *append-only-event-ledger + rolling-summaries + turn-1-cold-start* is operator-readable); CAN recover (the *AgentBook + postgresql* is recoverable via Postgres backup); CAN maintain (the *AgentBook + self-model + belief-knowledge* surface is documentation-only at v1; v2-AI surface would require Python+FastAPI+SQLModel+Postgres+event-sourcing+LLM expertise). **§3.1 owner-readable profile**; **STRONG EVIDENCE**: 43★/8⑂ = highest-star v2-AI candidate of the 68-pass series; 6283 KB modest; MIT permissive; but **OFF-STACK WARNING**: language is TypeScript |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 262 (Shawn-Durrani/membro MIT local-first memory for AI assistants + append-only fact ledger + MCP tools) + 267 (koorbmeh/minerva MIT personal-AI-agent-runtime + governed-tool-gateway + hash-chained-audit-ledger + job-orchestration + test-suite-as-first-class-citizen) + 232 (lpalbou/AbstractGateway MIT HTTP control plane for durable AI runs + append-only ledger + Telegram surface) + 268 (sattyamjjain/agent-audit-kit Apache-2.0 static scanner for MCP-connected AI agent pipelines) + 277 (basalt-os/ai-audit-suite Apache-2.0 public-adversarial-test-suite + agent-confinement + network-egress + ledger-integrity + confirmation-boundary + prompt-injection). The *persistent-memory + AgentBook + self-model + belief-knowledge + cold-start-frontpage-injection* posture IS the canonical **v2-AI persistent-memory-vocabulary**; **the highest-star v2-AI candidate of the 68-pass series (43★)** |
| 4 | Charter conflict | ✓ none hard | §3.1 PARTIAL ALIGNMENT (the *append-only-event-ledger + postgresql + sqlite + event-sourcing* IS the §3.1 *append-only-ledger* charter invariant; the *self-model + belief-knowledge* are OFF-§3.1 because LE31 v1 has no agent surface = explicit charter-decision needed); §3.2 STRICTLY-COMPATIBLE (MIT permissive); §3.3 ✓ (the *append-only-event-ledger-named-AgentBook* IS the §3.3 *audit-log-immutability* charter invariant applied to *agent-memory* dimension); §3.4 STRONG ALIGNMENT (the *self-model + belief-knowledge + turn-1-cold-start-frontpage-injection* are the §3.4 *AI-self-awareness + AI-belief + deterministic-cold-start* primitives — the **strongest §3.4-alignment signal of the 68-pass series for any v2-AI agent-memory surface** that uses an append-only-event-ledger); §3.7 N/A (no privacy primitive change — the *self-model + belief-knowledge* are about the agent's internal state, not about guest data). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v2-AI outcome (persistent-memory-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v2-AI PR = 2-4 weeks for design + 4-6 weeks for *persistent-memory + AgentBook + self-model + belief-knowledge + cold-start-frontpage-injection* surface + 2 weeks for verification = 2-3 months total |
| 6 | Cost to operational value | ✓ marginal at v1, MEDIUM-HIGH at v2-AI | Pain frequency = low at v1 (LE31 v1 has no v2-AI agent-memory today); money vocabulary = minimal (but **rolling-summaries requires periodic LLM calls = non-trivial operational cost**); implementation cost = 2-3 months v2-AI PR. **MEDIUM-HIGH VALUE at v2-AI** if LE31 ever adopts an agent runtime |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *persistent-memory + append-only-event-ledger-named-AgentBook* adoption; review point = first v2-AI PR that proposes *agent-memory* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v2-AI PR trigger)

If a future v2-AI PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/v2_ai/agent_memory_event.py` (NEW) | `AgentMemoryEvent` SQLModel table | `event_id, event_agent_id, event_kind, event_payload_json, event_at, event_parent_id, event_signed_by` for *append-only-event-ledger-named-AgentBook + event-sourcing* discipline; charter §3.3 *audit-log-immutability* invariant |
| `app/v2_ai/agent_memory_summary.py` (NEW) | `AgentMemorySummary` SQLModel table | `summary_id, summary_agent_id, summary_window_start_at, summary_window_end_at, summary_content, summary_generated_at` for *rolling-summaries* discipline; charter §3.4 *summary-as-audit-evidence* primitive |
| `app/v2_ai/agent_self_model.py` (NEW) | `AgentSelfModel` SQLModel table | `model_id, model_agent_id, model_self_description, model_self_capabilities_json, model_self_limitations_json, model_updated_at` for *self-model* discipline; charter §3.4 *self-model-as-audit-evidence* primitive; **OFF-§3.1 at v1** (LE31 v1 has no agent surface) |
| `app/v2_ai/agent_belief.py` (NEW) | `AgentBelief` SQLModel table | `belief_id, belief_agent_id, belief_statement, belief_confidence_score, belief_evidence_event_ids, belief_updated_at` for *belief-knowledge* discipline; charter §3.4 *belief-as-audit-evidence* primitive; **OFF-§3.1 at v1** (LE31 v1 stores counts, not scores) |
| `app/v2_ai/agent_cold_start_frontpage.py` (NEW) | `AgentColdStartFrontpage` SQLModel table | `frontpage_id, frontpage_agent_id, frontpage_content_json, frontpage_signed_by, frontpage_signed_at` for *turn-1-cold-start-frontpage-injection* discipline; charter §3.4 *deterministic-cold-start-as-auditable-test* primitive |
| `app/v2_ai/cross_session_memory.py` (NEW) | `CrossSessionMemory` class | persists agent memory across sessions using the AgentBook event ledger |
| `app/api/v2_ai_agent_memory.py` (NEW) | FastAPI route + endpoint | `/api/v2-ai/agent-memory` (GET recent, GET summary, GET self_model, GET beliefs, GET frontpage) |
| `app/templates/v2_ai_agent_memory.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for the agent-memory |
| `migrations/versions/<hash>_add_agent_memory_tables.py` (NEW) | alembic migration | creates `agent_memory_event + agent_memory_summary + agent_self_model + agent_belief + agent_cold_start_frontpage` tables |
| `tests/test_v2_ai_agent_memory.py` (NEW) | pytest coverage | covers AgentBook event-ledger, rolling-summaries, self-model, belief-knowledge, cold-start-frontpage-injection, cross-session-memory |
| `PROJECT_CHARTER.md` (UPDATE) | charter §3.1 + §3.4 update | explicitly authorize the v2-AI surface + the *self-model + belief-knowledge* disciplines before any PR |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v2-AI PR would:
1. Run `pytest tests/test_v2_ai_agent_memory.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.v2_ai.agent_memory_event import AgentMemoryEvent; print(AgentMemoryEvent.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/api/v2-ai/agent-memory/recent` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the owner-v2-ai-agent-memory surface that the *persistent-memory + AgentBook + self-model + belief-knowledge + cold-start-frontpage-injection* discipline works end-to-end (agent interaction → AgentBook event → rolling-summaries → self-model update → belief update → cold-start-frontpage injection).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this daily-research parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v2-AI PR ships and the *persistent-memory + AgentBook + self-model + belief-knowledge + cold-start-frontpage-injection* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `agent_memory_event + agent_memory_summary + agent_self_model + agent_belief + agent_cold_start_frontpage` tables.
2. Delete `app/v2_ai/agent_memory_event.py` + `app/v2_ai/agent_memory_summary.py` + `app/v2_ai/agent_self_model.py` + `app/v2_ai/agent_belief.py` + `app/v2_ai/agent_cold_start_frontpage.py` + `app/v2_ai/cross_session_memory.py` + `app/api/v2_ai_agent_memory.py` + `app/templates/v2_ai_agent_memory.html` + the alembic migration + the pytest files.
3. Revert the `PROJECT_CHARTER.md` §3.1 + §3.4 update.
4. Re-run `alembic upgrade head` to confirm clean state.
5. Re-run `pytest -v` to confirm no regressions.

## Mandatory LE31 skill list

The external coding agent (if a future v2-AI PR is triggered) must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 + §3.2 + §3.3 + §3.4 + §3.7).
- `le31-v1-feature-pattern` — for the canonical contract shape (adapt for v2-AI).
- `le31-research` — for the source-of-truth discipline on GitHub release verification.
- `le31-handoff-spec` — for the handoff contract discipline.
- `le31-coding-agent-brief` — for the brief-prompt discipline.
- `development` — for the generic code-change workflow.

The agent must NOT load `le31-feature-pipeline` (this is a defer artifact; the pipeline is run by the parent daily-research cron).

## Trigger condition

The trigger condition for a future v2-AI PR to actually build this surface is:
- The LE31 owner explicitly asks for a v2-AI agent-memory surface (e.g., "I want an AI agent that remembers past interactions"), AND
- The owner explicitly authorizes charter §3.1 + §3.4 to add a v2-AI control-plane, AND
- The owner explicitly accepts the *AgentBook + rolling-summaries + self-model + belief-knowledge + cold-start-frontpage-injection* discipline as the v2-AI agent-memory surface, AND
- The owner explicitly accepts the *self-model + belief-knowledge* disciplines (OFF-§3.1 at v1) as v2-AI primitives, AND
- The owner explicitly accepts the LLM cost of periodic rolling-summaries.

Until all five conditions are met, this HANDOFF is **dormant** (vocabulary-only, zero build time, zero code shipped).
