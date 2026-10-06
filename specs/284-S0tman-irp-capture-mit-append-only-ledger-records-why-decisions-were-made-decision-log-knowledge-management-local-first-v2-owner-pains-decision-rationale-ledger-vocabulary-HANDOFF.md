# Handoff — Feature 284 — v2 owner-pains decision-rationale-ledger-vocabulary (defer)

> **Pick:** `S0tman/irp-capture` — v2 cross-section reference for **append-only-ledger-that-records-why-decisions-were-made + decision-log + claude + knowledge-management + local-first + devtools + python** primitive.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v2 surface that adopts the *records-why-decisions-were-made + decision-log + knowledge-management + local-first + devtools + python* primitives.
> **Source:** Daily Brainstorm 2026-10-06 (68th consecutive daily-brainstorm pass) → Pick A.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/284-S0tman-irp-capture-mit-append-only-ledger-records-why-decisions-were-made-decision-log-knowledge-management-local-first-v2-owner-pains-decision-rationale-ledger-vocabulary.md`
> **Raw fetches:** `/tmp/le31-brainstorm-2026-10-06/verify_S0tman_irp-capture.json` (parent-verified direct GitHub API GET, raw JSON)

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 owner wants to find out why an order was discounted, why a recipe was changed, why a staff shift was swapped, or why a stock entry was reversed, the owner wants a *records-why-decisions-were-made + decision-log* audit-trail, but struggles because the existing `audit_logs` table has *no decision-rationale-markdown field + no decision-log surface + no knowledge-link surface*, so the v2 surface-extension needs a *records-why-decisions-were-made + decision-log + knowledge-management + local-first* discipline. **v2 expansion → NEW pain** |
| 2 | Viability | ✓ viable | Non-technical owner CAN understand (the *records-why-decisions-were-made + decision-log + knowledge-management* primitive is operator-readable); CAN recover (the *append-only-ledger + audit_logs* discipline is recoverable via Postgres backup); CAN maintain (the *records-why-decisions-were-made + decision-log + knowledge-management + local-first* surface is documentation-only at v2; v2 surface would require FastAPI + SQLModel + Postgres + ULID + decision-event-id-infrastructure expertise). **§3.1 owner-readable profile** |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 197 (rajo69/ledgerkb Apache-2.0 v2-owner-pains evidence-bearing-assertions-position-over-time-append-only-ledger-rag-knowledge-graph = *position-over-time + multiple-projections-from-one-ledger + evidence-bearing-assertion* triple-primitive) + 245 (EvezArt/evez-event-spine MIT append-only-hash-linked-event-log-immutable-verifiable-readable-truth-content-hash-chain-discipline-python) + 271 (znbsf/agent-case-graph MIT evidence-first-append-only-case-ledger-provenance-graph-deterministic-validation-audit-trail-jsonl-event-sourcing-knowledge-graph) + today's daily-research Pick A 281 (siezonsolutions/Seintinel-WasmGate Apache-2.0 zero-trust-execution-gate-cryptographic-audit-ledger-wasm-ed25519-sqlite-langchain-fastify). The *records-why-decisions-were-made + decision-log + knowledge-management + local-first* posture IS the canonical **v2 owner-pains decision-rationale-ledger-vocabulary** |
| 4 | Charter conflict | ✓ none hard | §3.1 STRICTLY-COMPATIBLE (Python + minimal-HTML posture; the *records-why-decisions-were-made + decision-log + knowledge-management + local-first* posture IS the §3.1 *single-restaurant + single-owner + on-premise-deployment + explicit-state-transition* invariant applied to the *decision-rationale* dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive + 3★/0⑨ community traction start); §3.4 RIPGL_REVIEW REQUIRED (the *decision-log* surface is operator-tooling per charter §3.4 invariant; the *records-why-decisions* is a deterministic append-only primitive, not customer-facing AI; the *claude* topic in the topic array is vocabulary-only; any future v2 surface that exposes the *decision-rationale* to diners requires explicit §3.4 review); §3.7 N/A (no privacy primitive change). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v2 outcome (decision-rationale-ledger-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v2 PR = 1-2 weeks for design + 2-3 weeks for *records-why-decisions-were-made + decision-log + knowledge-management + local-first* surface + 1 week for verification = 1-2 months total |
| 6 | Cost to operational value | ✓ marginal | Pain frequency = low (LE31 v1 has no v2 decision-rationale surface today; no owner has asked for v2 decision-rationale); money vocabulary = minimal; implementation cost = 1-2 months v2 PR. **MARGINAL VALUE at v2** |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *records-why-decisions-were-made + decision-log + knowledge-management + local-first* adoption; review point = first v2 PR that proposes *records-why-decisions-were-made + decision-log + knowledge-management + local-first* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v2 PR trigger)

If a future v2 PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/models/decision_rationale.py` (NEW) | `DecisionRationale` SQLModel table | `decision_id, decision_kind, decision_payload_json, decision_rationale_markdown, decision_rationale_at, decision_rationale_owner_id, decision_parent_id` |
| `app/models/decision_rationale_entry.py` (NEW) | `DecisionRationaleEntry` SQLModel table | `entry_id, decision_id, entry_event_id, entry_event_kind, entry_event_payload_json, entry_event_at, entry_event_parent_id` for *records-why-decisions-were-made + append-only-ledger* discipline |
| `app/models/decision_log.py` (NEW) | `DecisionLog` SQLModel table | `log_id, log_decision_id, log_event_id, log_event_kind, log_event_at, log_event_parent_id` for *decision-log* discipline |
| `app/models/knowledge_link.py` (NEW) | `KnowledgeLink` SQLModel table | `link_id, link_source_id, link_target_id, link_kind, link_rationale_id, link_at` for *knowledge-management* discipline |
| `app/api/decision_rationale.py` (NEW) | FastAPI route + endpoint | `/api/decision-rationale` (POST create, GET list, GET show, POST rationale) |
| `app/templates/decision_rationale.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for decision-rationale with records-why-decisions-were-made + decision-log + knowledge-management |
| `migrations/versions/<hash>_add_decision_rationale_tables.py` (NEW) | alembic migration | creates `decision_rationale + decision_rationale_entry + decision_log + knowledge_link` tables |
| `tests/test_decision_rationale_api.py` (NEW) | pytest coverage | covers DecisionRationale CRUD + records-why-decisions-were-made + decision-log + knowledge-management |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v2 PR would:
1. Run `pytest tests/test_decision_rationale_api.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.models.decision_rationale import DecisionRationale; print(DecisionRationale.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/api/decision-rationale/status` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the owner-decision-rationale-dashboard that the *records-why-decisions-were-made + decision-log + knowledge-management + local-first* discipline works end-to-end (create rationale → list rationales → verify decision-log → verify knowledge-link).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this brainstorm parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v2 PR ships and the *records-why-decisions-were-made + decision-log + knowledge-management + local-first* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `decision_rationale + decision_rationale_entry + decision_log + knowledge_link` tables.
2. Delete `app/models/decision_rationale.py` + `app/models/decision_rationale_entry.py` + `app/models/decision_log.py` + `app/models/knowledge_link.py` + `app/api/decision_rationale.py` + `app/templates/decision_rationale.html` + the alembic migration + the pytest files.
3. Re-run `alembic upgrade head` to confirm clean state.
4. Re-run `pytest -v` to confirm no regressions.

## Mandatory LE31 skill list

The future v2 PR author MUST load + apply these skills before any code is written:

| Skill | Why |
|---|---|
| `le31-conventions` | Repository-wide Python + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX conventions |
| `le31-v1-feature-pattern` | Existing v1 feature pattern (table management, cook-channel, stock-ledger) |
| `le31-handoff-spec` | Slice handoff format |
| `le31-coding-agent-brief` | Paste-in prompt generation from this slice contract |
| `systematic-debugging` | 4-phase root cause debugging if any test fails |
| `verify-before-fixing` | Verify diagnostic / CI / delegated subagent before fixing |
| `pre-merge-review` | Independent non-author review before merging |

## Bucket

**v2 owner-pains** (attached to `le31 Research` P-HMM-1 per the verified workspace project list of 2026-10-06; the `le31 v2 owner-pains` and `le31 v2-AI` projects do NOT exist per `le31-feature-pipeline/SKILL.md` line 33; the parent of the sub-issue is `le31 Research` since v2 owner-pains bucket has no dedicated project).

## Trigger condition

First v2 PR that adds a `decision_rationale` SQLModel table + a `DecisionRationaleEntry` append-only event table + a `/api/decision-rationale` FastAPI endpoint + a `decision-rationale.html` minimal-HTML/HTMX template; OR first v2 PR that adopts the *records-why-decisions-were-made + decision-log + knowledge-management + local-first* discipline on the existing `audit_logs` SQLModel table.

## Charter compatibility

§3.1 + §3.2 STRICTLY-COMPATIBLE; §3.4 RIPGL_REVIEW REQUIRED (the *decision-log* surface is operator-tooling per charter §3.4 invariant; the *records-why-decisions* is a deterministic append-only primitive, not customer-facing AI; the *claude* topic in the topic array is vocabulary-only).

## Companion artifacts

- Feature file: `/opt/data/le31_mmm3_research_work/features/284-S0tman-irp-capture-mit-append-only-ledger-records-why-decisions-were-made-decision-log-knowledge-management-local-first-v2-owner-pains-decision-rationale-ledger-vocabulary.md`
- Spec file: `/opt/data/le31_mmm3_research_work/specs/284-S0tman-irp-capture-mit-append-only-ledger-records-why-decisions-were-made-decision-log-knowledge-management-local-first-v2-owner-pains-decision-rationale-ledger-vocabulary-HANDOFF.md`
- Linear sub-issue: BLOCKED (workspace plan-limit error: *"You've exceeded the free issue limit for this workspace"* — **17th consecutive day**; verified today via 1 write-probe with requestId TBD; parent fallback at `/opt/data/le31-brainstorm-2026-10-06.linear-fallback.json`)
- Report: `/opt/data/le31-brainstorm-2026-10-06.md`
- Raw fetches: `/tmp/le31-brainstorm-2026-10-06/verify_S0tman_irp-capture.json` (parent-verified direct GitHub API GET, raw JSON)
