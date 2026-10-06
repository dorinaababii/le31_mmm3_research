# Handoff — Feature 282 — v2-AI capability-arbiter-runtime-vocabulary (defer)

> **Pick:** `AllStreets/ONEXUS` — v2-AI cross-section reference for **local-first-AI-agent-runtime + capability-arbiter + declared-manifest + earned-trust-scoring + immutable-audit-ledger + mcp-integration** primitive. **Only Python on-stack v2-AI capability-arbiter-runtime pick of the 68-pass series**.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v2-AI surface that adopts the *capability-arbiter + declared-manifest + earned-trust-scoring + immutable-audit-ledger* primitives.
> **Source:** Daily Research 2026-10-06 (68th consecutive daily-research pass) → Pick B.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/282-AllStreets-ONEXUS-apache-2-0-local-first-ai-agent-runtime-capability-arbiter-declared-manifest-earned-trust-immutable-audit-ledger-python-mcp-v2-ai-capability-arbiter-runtime-vocabulary.md`
> **Raw fetches:** `/tmp/le31-daily-2026-10-06/ghverify__parent_AllStreets_ONEXUS.json` (parent-verified direct GitHub API GET, raw JSON, 5.5 KB)
> **Homepage**: https://allstreets.github.io/ONEXUS/ (confirms it is a real project with documentation, not a name-squat)

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 v2-AI control-plane wants to run an AI agent that takes actions on the operator's behalf, the operator wants every tool call to clear a capability-arbiter that gates against a declared manifest, scores on earned trust, and writes to an immutable audit ledger, but struggles because the existing audit_logs SQLModel table is a flat log without capability-arbiter or earned-trust-scoring, so that an adversary or buggy agent cannot execute a tool call without leaving a verifiable, scored audit trail. **v2-AI expansion → NEW pain** |
| 2 | Viability | ✓ viable as a vocabulary reference | Non-technical owner CAN understand (the *capability-arbiter + declared-manifest* is operator-readable); CAN recover (the *immutable-audit-ledger* is recoverable via Postgres backup); CAN maintain (the *capability-arbiter + declared-manifest* surface is documentation-only at v1; v2-AI surface would require Python+FastAPI+SQLModel+Postgres+MCP expertise). **§3.1 owner-readable profile**; **STRONGER EVIDENCE THAN PICK A**: 4★/1⑂ at 29358 KB substantial + Python on-stack ✓ + has a homepage at https://allstreets.github.io/ONEXUS/ = real project with documentation, not a name-squat |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 268 (sattyamjjain/agent-audit-kit Apache-2.0 static scanner for MCP-connected AI agent pipelines) + 273 (truongpx396/intel-audit MIT tamper-evident-audit-trail-per-tenant-hash-chain-db-enforced-immutability) + 274 (Mfrostbutter/ageniusdesk-ce MIT fastapi-control-plane-dashboard-observability-mcp-self-hosted-workflow-automation) + 277 (basalt-os/ai-audit-suite Apache-2.0 public-adversarial-test-suite + agent-confinement + network-egress + ledger-integrity + confirmation-boundary + prompt-injection) + 232 (lpalbou/AbstractGateway MIT HTTP control plane for durable AI runs + append-only ledger + Telegram surface). The *capability-arbiter + declared-manifest + earned-trust-scoring + immutable-audit-ledger* posture IS the canonical **v2-AI capability-arbiter-runtime-vocabulary**; **the only Python on-stack v2-AI capability-arbiter pick of the 68-pass series** |
| 4 | Charter conflict | ✓ none hard | §3.1 PARTIAL ALIGNMENT (the *capability-arbiter + declared-manifest + immutable-audit-ledger* IS the §3.1 *explicit-state-transition + append-only-ledger* charter invariant; the *earned-trust-scoring* discipline is OFF-§3.1 at v1 because LE31 v1 stores counts, not scores = explicit charter-decision needed); §3.2 STRICTLY-COMPATIBLE (Apache-2.0 permissive); §3.3 ✓ (the *immutable-audit-ledger* IS the §3.3 *audit-log-immutability* charter invariant); §3.4 STRONG ALIGNMENT (the *capability-arbiter + declared-manifest + earned-trust-scoring + sandboxing* IS the §3.4 *AI-sandbox-as-auditable-test* primitive — the **strongest §3.4-alignment signal of the 68-pass series for any v2-AI surface** that uses a declared-manifest as a runtime gate); §3.7 PARTIAL CONCERN (the *local-first-AI-agent-runtime* IS the *§3.7 on-device-persistence* charter invariant = privacy-aligned; the *immutable-audit-ledger* may need a charter §3.7 review for any v2-AI surface that adopts it). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v2-AI outcome (capability-arbiter-runtime-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v2-AI PR = 2-4 weeks for design + 4-6 weeks for *capability-arbiter + declared-manifest + earned-trust-scoring* surface + 2 weeks for verification = 2-3 months total |
| 6 | Cost to operational value | ✓ marginal at v1, HIGH at v2-AI | Pain frequency = low at v1 (LE31 v1 has no v2-AI control-plane today); money vocabulary = minimal; implementation cost = 2-3 months v2-AI PR. **HIGH VALUE at v2-AI** if LE31 ever adopts an agent runtime |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *capability-arbiter + declared-manifest + earned-trust-scoring* adoption; review point = first v2-AI PR that proposes *capability-arbiter* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v2-AI PR trigger)

If a future v2-AI PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/v2_ai/capability_arbiter.py` (NEW) | `CapabilityArbiter` class | gates every tool call against a declared manifest + writes the decision to the `capability_arbiter_decision` table |
| `app/v2_ai/declared_manifest.py` (NEW) | `DeclaredManifest` SQLModel table | `manifest_id, manifest_name, manifest_tool_call_allowlist_json, manifest_version, manifest_signed_by, manifest_signed_at` for *declared-manifest* discipline; charter §3.1 *explicit-state-manifest* invariant |
| `app/v2_ai/earned_trust_score.py` (NEW) | `EarnedTrustScorer` class + `EarnedTrustScore` SQLModel table | scores every agent action on earned trust + updates the `earned_trust_score` table. **OFF-§3.1 at v1** — explicit charter-decision needed |
| `app/v2_ai/immutable_audit_ledger.py` (NEW) | `ImmutableAuditLedger` SQLModel table | `entry_id, entry_tool_call_kind, entry_tool_call_payload_json, entry_tool_call_at, entry_capability_arbiter_decision_id, entry_signature` for *immutable-audit-ledger* discipline; charter §3.3 *audit-log-immutability* invariant |
| `app/v2_ai/local_first_runtime.py` (NEW) | `LocalFirstRuntime` class | runs the agent locally + emits an `immutable_audit_ledger` row for every action |
| `app/v2_ai/mcp_integration.py` (NEW) | MCP server | exposes the agent's tools + queries the audit ledger via MCP |
| `app/api/v2_ai_capability_arbiter.py` (NEW) | FastAPI route + endpoint | `/api/v2-ai/capability-arbiter` (GET show, GET recent, GET manifest, GET trust) |
| `app/templates/v2_ai_capability_arbiter.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for the capability-arbiter |
| `migrations/versions/<hash>_add_capability_arbiter_tables.py` (NEW) | alembic migration | creates `capability_arbiter_decision + declared_manifest + earned_trust_score + immutable_audit_ledger` tables |
| `tests/test_v2_ai_capability_arbiter.py` (NEW) | pytest coverage | covers capability-arbiter, declared-manifest, earned-trust-scoring, immutable-audit-ledger, MCP-integration |
| `PROJECT_CHARTER.md` (UPDATE) | charter §3.1 + §3.4 update | explicitly authorize the v2-AI surface + the *earned-trust-scoring* discipline before any PR |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v2-AI PR would:
1. Run `pytest tests/test_v2_ai_capability_arbiter.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.v2_ai.capability_arbiter import CapabilityArbiter; print(CapabilityArbiter.__name__)"` to confirm the class loads.
4. Manually verify via `curl http://localhost:8000/api/v2-ai/capability-arbiter/recent` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the owner-v2-ai-capability-arbiter surface that the *capability-arbiter + declared-manifest + earned-trust-scoring + immutable-audit-ledger + MCP-integration* discipline works end-to-end (agent tool-call → capability-arbiter decision → declared-manifest lookup → earned-trust-scoring → immutable-audit-ledger entry → MCP query).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this daily-research parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v2-AI PR ships and the *capability-arbiter + declared-manifest + earned-trust-scoring + immutable-audit-ledger + MCP-integration* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `capability_arbiter_decision + declared_manifest + earned_trust_score + immutable_audit_ledger` tables.
2. Delete `app/v2_ai/capability_arbiter.py` + `app/v2_ai/declared_manifest.py` + `app/v2_ai/earned_trust_score.py` + `app/v2_ai/immutable_audit_ledger.py` + `app/v2_ai/local_first_runtime.py` + `app/v2_ai/mcp_integration.py` + `app/api/v2_ai_capability_arbiter.py` + `app/templates/v2_ai_capability_arbiter.html` + the alembic migration + the pytest files.
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
- The LE31 owner explicitly asks for a v2-AI agent surface (e.g., "I want an AI agent to help me with X"), AND
- The owner explicitly authorizes charter §3.1 + §3.4 to add a v2-AI control-plane, AND
- The owner explicitly accepts the *capability-arbiter + declared-manifest + earned-trust-scoring + immutable-audit-ledger* discipline as the gate for the v2-AI surface, AND
- The owner explicitly accepts the *earned-trust-scoring* discipline (OFF-§3.1 at v1) as a v2-AI primitive.

Until all four conditions are met, this HANDOFF is **dormant** (vocabulary-only, zero build time, zero code shipped).
