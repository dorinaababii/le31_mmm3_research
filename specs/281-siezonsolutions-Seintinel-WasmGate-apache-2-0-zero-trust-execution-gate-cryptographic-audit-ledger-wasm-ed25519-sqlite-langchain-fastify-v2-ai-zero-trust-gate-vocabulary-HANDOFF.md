# Handoff — Feature 281 — v2-AI zero-trust-execution-gate-vocabulary (defer)

> **Pick:** `siezonsolutions/Seintinel-WasmGate` — v2-AI cross-section reference for **zero-trust-execution-gate + cryptographic-audit-ledger + Wasm + ed25519-signature + sqlite-backing + langchain + fastify** primitive.
> **Status:** `defer (parking-lot, vocabulary reference)` — zero build time today; the artifact is vocabulary-only and persists as a future-cast reference for any future LE31 v2-AI surface that adopts the *zero-trust-execution-gate + ed25519-signature + Wasm-sandbox + cryptographic-audit-ledger* primitives.
> **Source:** Daily Research 2026-10-06 (68th consecutive daily-research pass) → Pick A.
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/281-siezonsolutions-Seintinel-WasmGate-apache-2-0-zero-trust-execution-gate-cryptographic-audit-ledger-wasm-ed25519-sqlite-langchain-fastify-v2-ai-zero-trust-gate-vocabulary.md`
> **Raw fetches:** `/tmp/le31-daily-2026-10-06/ghverify__parent_siezonsolutions_Seintinel-WasmGate.json` (parent-verified direct GitHub API GET, raw JSON, 6.3 KB)
> **OFF-STACK WARNING:** language is TypeScript; LE31 v1 stack is Python+HTMX; per carry-over convention this is a vocabulary-only reference, not a code-import candidate.

---

## Seven-check gate verdict (LE31 charter §3.1 + §3.2 + §3.4)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✓ justified as a NEW pain | When the LE31 v2-AI control-plane wants to run an autonomous agent that takes actions on the operator's behalf, the operator wants every action to clear a zero-trust gate with a cryptographic-audit-ledger, but struggles because the existing audit_logs SQLModel table is a flat log without zero-trust enforcement or cryptographic-signature verification, so that an adversary or buggy agent cannot execute an action without leaving a verifiable audit trail. **v2-AI expansion → NEW pain** |
| 2 | Viability | ✓ viable as a vocabulary reference | Non-technical owner CAN understand (the *zero-trust-gate + cryptographic-audit-ledger* is operator-readable); CAN recover (the *ed25519-signature + sqlite-backing* is recoverable via Postgres backup); CAN maintain (the *zero-trust-gate + Wasm-sandbox* surface is documentation-only at v1; v2-AI surface would require Python+FastAPI+SQLModel+Postgres+wasmtime expertise). **§3.1 owner-readable profile** |
| 3 | Strategic fit | ✓ aligned | Cross-section with feature 268 (sattyamjjain/agent-audit-kit Apache-2.0 static scanner for MCP-connected AI agent pipelines) + 273 (truongpx396/intel-audit MIT tamper-evident-audit-trail-per-tenant-hash-chain-db-enforced-immutability) + 277 (basalt-os/ai-audit-suite Apache-2.0 public-adversarial-test-suite + agent-confinement + network-egress + ledger-integrity + confirmation-boundary + prompt-injection) + 232 (lpalbou/AbstractGateway MIT HTTP control plane for durable AI runs + append-only ledger + Telegram surface). The *zero-trust-execution-gate + cryptographic-audit-ledger + Wasm-sandbox + ed25519-signature + sqlite-backing* posture IS the canonical **v2-AI zero-trust-execution-gate-vocabulary** |
| 4 | Charter conflict | ✓ none hard | §3.1 PARTIAL ALIGNMENT (the *zero-trust-gate + cryptographic-audit-ledger + sqlite* IS the §3.1 *explicit-state-transition + append-only-ledger* charter invariant; the *sqlite-backing* is OFF-§3.1 if LE31 v1 is Postgres-only); §3.2 STRICTLY-COMPATIBLE (Apache-2.0 permissive); §3.3 ✓ (the *cryptographic-audit-ledger + ed25519-signature* IS the §3.3 *audit-log-immutability + signature-as-audit-evidence* charter invariant); §3.4 STRONG ALIGNMENT (the *zero-trust-Wasm-gate* IS the §3.4 *AI-sandbox-as-auditable-test* primitive); §3.7 PARTIAL CONCERN (the *on-device-sqlite-backing* is privacy-aligned; the *Wasm-sandbox* may need a charter §3.7 review for any v2-AI surface that adopts it). **No hard conflict** |
| 5 | Outcome, appetite, scope | ✓ alignable | v2-AI outcome (zero-trust-execution-gate-vocabulary). Max time worth spending = 0 minutes today (defer artifact); future v2-AI PR = 2-4 weeks for design + 4-6 weeks for *zero-trust-gate + cryptographic-audit-ledger* surface + 2 weeks for verification = 2-3 months total |
| 6 | Cost to operational value | ✓ marginal at v1, HIGH at v2-AI | Pain frequency = low at v1 (LE31 v1 has no v2-AI control-plane today); money vocabulary = minimal; implementation cost = 2-3 months v2-AI PR. **HIGH VALUE at v2-AI** if LE31 ever adopts an agent runtime |
| 7 | Circuit breaker and reversibility | ✓ reversible | Stop evidence = explicit owner/charter rejection of *zero-trust-execution-gate + cryptographic-audit-ledger* adoption; review point = first v2-AI PR that proposes *zero-trust-gate* surface; migration/rollback = trivial (vocabulary-only artifact, zero code shipped); retained data = N/A |

**Final decision: `defer (parking-lot, vocabulary reference)`.**

## Files to touch (future v2-AI PR trigger)

If a future v2-AI PR is triggered by the trigger condition below, the implementation would touch:

| File | Purpose | Notes |
|---|---|---|
| `app/v2_ai/zero_trust_audit_ledger.py` (NEW) | `ZeroTrustAuditLedger` SQLModel table | `entry_id, entry_action_kind, entry_action_payload_json, entry_action_at, entry_action_signature_ed25519, entry_action_parent_id, entry_zero_trust_gate_decision, entry_wasm_sandbox_run_id` for *zero-trust-execution-gate + ed25519-signature + Wasm-sandbox* discipline; charter §3.3 *append-only-ledger* invariant |
| `app/v2_ai/zero_trust_gate.py` (NEW) | `ZeroTrustGate` class | verifies every action against a declared policy + writes the decision to the `zero_trust_gate_decision` table |
| `app/v2_ai/wasm_sandbox.py` (NEW) | `WasmSandbox` class | runs agent code inside a WebAssembly sandbox + emits a `wasm_sandbox_run` row |
| `app/v2_ai/ed25519_signer.py` (NEW) | `Ed25519Signer` class | signs every agent action with ed25519 + writes the signature to the `zero_trust_audit_ledger` table |
| `app/api/v2_ai_zero_trust_audit.py` (NEW) | FastAPI route + endpoint | `/api/v2-ai/zero-trust-audit` (GET show, GET recent, GET verify) |
| `app/templates/v2_ai_zero_trust_audit.html` (NEW) | minimal-HTML/HTMX template | owner-facing surface for the zero-trust-audit ledger |
| `migrations/versions/<hash>_add_zero_trust_audit_tables.py` (NEW) | alembic migration | creates `zero_trust_audit_ledger + zero_trust_gate_decision + wasm_sandbox_run` tables |
| `tests/test_v2_ai_zero_trust_audit.py` (NEW) | pytest coverage | covers append-only-ledger, ed25519-signature, zero-trust-gate, Wasm-sandbox-isolation |
| `PROJECT_CHARTER.md` (UPDATE) | charter §3.1 + §3.4 update | explicitly authorize the v2-AI surface before any PR |

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md` + `development` skill, the future v2-AI PR would:
1. Run `pytest tests/test_v2_ai_zero_trust_audit.py -v` to confirm all tests pass.
2. Run `alembic upgrade head` to confirm migrations apply cleanly.
3. Run `python -c "from app.v2_ai.zero_trust_audit_ledger import ZeroTrustAuditLedger; print(ZeroTrustAuditLedger.__tablename__)"` to confirm SQLModel loads.
4. Manually verify via `curl http://localhost:8000/api/v2-ai/zero-trust-audit/recent` that the FastAPI endpoint returns 200 with the expected schema.
5. Manually verify via the owner-v2-ai-zero-trust-audit surface that the *zero-trust-execution-gate + cryptographic-audit-ledger + Wasm-sandbox + ed25519-signature* discipline works end-to-end (agent action → zero-trust-gate decision → Wasm-sandbox run → ed25519-signature → audit-ledger entry).
6. Run `mypy app/` + `ruff check app/` to confirm static analysis passes.
7. Confirm feature is in `Backlog` status + parent (this daily-research parent) is in `Done` status in Linear.

## Rollback path

The defer artifact is vocabulary-only, zero code shipped, so no rollback is needed today. If a future v2-AI PR ships and the *zero-trust-execution-gate + cryptographic-audit-ledger + Wasm-sandbox + ed25519-signature* discipline is rejected by the owner/charter:
1. Run `alembic downgrade -1` to drop the `zero_trust_audit_ledger + zero_trust_gate_decision + wasm_sandbox_run` tables.
2. Delete `app/v2_ai/zero_trust_audit_ledger.py` + `app/v2_ai/zero_trust_gate.py` + `app/v2_ai/wasm_sandbox.py` + `app/v2_ai/ed25519_signer.py` + `app/api/v2_ai_zero_trust_audit.py` + `app/templates/v2_ai_zero_trust_audit.html` + the alembic migration + the pytest files.
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
- The owner explicitly accepts the *zero-trust-execution-gate + cryptographic-audit-ledger + Wasm-sandbox + ed25519-signature* discipline as the gate for the v2-AI surface.

Until all three conditions are met, this HANDOFF is **dormant** (vocabulary-only, zero build time, zero code shipped).
