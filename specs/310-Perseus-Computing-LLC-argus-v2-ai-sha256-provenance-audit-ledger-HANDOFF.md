# 310-Perseus-Computing-LLC-argus — HANDOFF

> **Slice for the coding agent.** Read this *and* `features/310-Perseus-Computing-LLC-argus-mit-tamper-evident-append-only-sha256-provenance-audit-ledger-autonomous-agents-v2-ai-sha256-provenance-audit-ledger-vocabulary.md` before touching any code. Do not paste chat excerpts back into the build.
>
> **Defer artifact (no code today).** This is a parking-lot vocabulary reference. There is no build candidate. The HANDOFF documents what the trigger condition would be and what the slice would look like if the trigger fires.

## Frozen identifiers (do not rename)

- Feature ID: `310`
- Slug: `Perseus-Computing-LLC-argus-v2-ai-sha256-provenance-audit-ledger`
- Contract file: `features/310-Perseus-Computing-LLC-argus-mit-tamper-evident-append-only-sha256-provenance-audit-ledger-autonomous-agents-v2-ai-sha256-provenance-audit-ledger-vocabulary.md`
- Bucket: **v2-AI (SHA-256-provenance-audit-ledger-vocabulary)** — build verdict `defer`
- Linear parent (intake only — Linear is currently BLOCKED): **intended** `Research 2026-10-12 — daily` (parent fallback at `/opt/data/le31-daily-research-2026-10-12.linear-fallback.json`)
- Linear sub-issue (intake only): **intended** `Research 2026-10-12 / Pick C — v2-AI SHA-256-provenance-audit-ledger-vocabulary (Perseus-Computing-LLC/argus)` with label `Feature`, project `le31 Research` (per `le31-feature-pipeline/SKILL.md` line 33 — `le31 v2-AI` does NOT exist; use `le31 Research` for v2-AI bucket picks); state `Triage`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed** (verified in-window by parent re-parse of `gsearch9.json` raw JSON; the description names the 6-primitive set explicitly: `tamper-evident + append-only + SHA-256 + provenance + audit-ledger + autonomous-agents`).

**Confidence:** **medium** for the vocabulary match (the verbatim description names the 6-primitive set); **low** for transferability (LE31 v1 has no v2-AI surface; the 39 KB tiny repo is the 2nd-smallest v2-AI pick of the 74-pass series; the 0★/1⑂ is a low community-traction signal).

**Decision: defer (parking-lot, vocabulary reference).** Sister-shape to features 187+188+232+287-289+299-304 (the persistent v2-AI audit-trail vocabulary cluster) but with the unique *SHA-256 (vs ed25519) + autonomous-agents (vs ai-agents)* framing. No build today; the *SHA-256-provenance-audit-ledger-vocabulary* is a persistent cross-section reference for any future v2-AI surface that requires SHA-256-provenance + audit-ledger for autonomous-agents.

## Trigger condition (when to un-defer)

This slice un-defers if AND ONLY IF all of the following are true:

1. The first v2 PR that introduces a v2-AI surface that requires **SHA-256-provenance + audit-ledger for autonomous-agents** lands (e.g., a v2 surface that introduces an AI-assisted owner-side workflow where the autonomous AI agent proposes a supplier reorder; the proposal is recorded in the SHA-256-provenance + audit-ledger; the operator reviews the audit trail; the operator confirms or rejects the proposal).
2. The proposed surface requires *SHA-256* content-addressing (vs the more common *ed25519* signing in sister-shape audit-ledger repos).
3. The proposed surface requires *autonomous-agents* (agents that act without human-in-the-loop).
4. Charter §3.4 *non-AI-fallback + human-gate* invariant can be maintained (the autonomous-agent's actions must be operator-confirmed, not autonomous-on-customer-facing-surfaces).

If the trigger condition is met, follow the slice plan below.

## Slice plan (if trigger fires)

### Files to touch

1. **New** `app/db/migrations/2026_XX_XX_add_content_hash_to_audit_logs.py` (Alembic migration): add the `content_hash` column to `audit_logs`.
2. **New** `app/db/migrations/2026_XX_XX_add_provenance_to_audit_logs.py` (Alembic migration): add the `provenance` column to `audit_logs`.
3. **New** `app/db/migrations/2026_XX_XX_add_autonomous_agent_audit.py` (Alembic migration): add the `AutonomousAgentAudit` table.
4. **New** `app/db/migrations/2026_XX_XX_add_merkle_proof.py` (Alembic migration): add the `MerkleProof` table.
5. **New** `app/api/autonomous_agent_audit.py`: implement `GET /v2/autonomous-agent-audit?agent=<>&action=<>&as_of=<>` + `POST /v2/autonomous-agent-audit/record` + `GET /v2/autonomous-agent-audit/{audit_id}/merkle-proof` + `POST /v2/autonomous-agent-audit/{audit_id}/confirm`.
6. **New** `app/bot/handlers/autonomous_agent.py`: implement the `autonomous_agent_audit_request` Telegram handler.
7. **Update** `app/db/__init__.py`: register the new SQLModel classes.
8. **Update** `app/main.py`: include the new routers.

### Schema additions (Alembic migrations)

1. `audit_logs.content_hash` column: `str` (SHA-256 content hash of the audit-log payload, unique per audit-log row). Nullable for legacy rows.
2. `audit_logs.provenance` column: `str` (provenance metadata: `agent_id + action_id + upstream_source`). Nullable for legacy rows. Index on `provenance` for efficient provenance search.
3. `AutonomousAgentAudit` table: `id` (UUID PK), `agent_id` (str), `action_id` (str), `proposed_action` (str), `proposed_by` (str agent-id), `content_hash` (str SHA-256), `merkle_root` (str SHA-256 merkle-tree-root), `recorded_at` (DateTime TZ), `confirmed_by` (str nullable operator-id), `confirmed_at` (DateTime TZ nullable), `rejected_reason` (str nullable). Index on `(agent_id, recorded_at)`.
4. `MerkleProof` table: `id` (UUID PK), `audit_id` (UUID FK to `AutonomousAgentAudit`), `proof_path` (JSON list of SHA-256 hashes), `leaf_hash` (str SHA-256), `root_hash` (str SHA-256 merkle-tree-root), `verified_at` (DateTime TZ nullable). Index on `audit_id`.

### Verification protocol

Per `le31-daily-research/SKILL.md` + `le31-conventions/SKILL.md` + `le31-v1-feature-pattern/SKILL.md`:

1. Run `pytest app/tests/test_autonomous_agent_audit.py` (new test file). Confirm 100% pass.
2. Run `pytest app/tests/test_merkle_proof.py` (new test file). Confirm 100% pass.
3. Manually exercise the end-to-end acceptance path: log in as owner → open the v2 surface → propose an autonomous-agent action → confirm via Telegram → verify the `AutonomousAgentAudit` record is created with `content_hash` + `merkle_root` populated.
4. Inspect the `MerkleProof` table to confirm the merkle-proof is correctly formed and the `verified_at` is populated.
5. Verify the SHA-256 content hash is unique per audit-log row (`SELECT COUNT(*), COUNT(DISTINCT content_hash) FROM audit_logs WHERE content_hash IS NOT NULL`).
6. Confirm charter §3.4 invariant is maintained: the autonomous-agent's actions must be operator-confirmed, not autonomous-on-customer-facing-surfaces.

### Rollback path

1. Revert the Alembic migrations: `alembic downgrade -1` (4x).
2. Delete the new files: `app/api/autonomous_agent_audit.py` + `app/bot/handlers/autonomous_agent.py`.
3. Revert the `app/main.py` + `app/db/__init__.py` updates.
4. Verify: `pytest` passes with no test errors.
5. The SHA-256-provenance is vocabulary-only; the rollback is safe (no data loss beyond the dropped tables).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job on 2026-10-12).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).
6. `le31-research` (so the agent understands the research methodology that produced this pick).
7. `le31-coding-agent-brief` (so the agent uses the standard brief shape).

## Handoff summary

This is a **defer / parking-lot / vocabulary reference**. No build today. The slice un-defers only when the trigger condition is met. Until then, the artifact is documentation only.

**Sign-off gap:** none. The defer artifact is complete. The trigger condition is explicit. The slice plan is explicit. The verification protocol is explicit. The rollback path is explicit.

---

## Sign-off

- [x] Feature gate verdict is recorded (defer).
- [x] Feature contract (`features/310-...md`) is linked.
- [x] Mandatory LE31 skill list is named.
- [x] Trigger condition is explicit.
- [x] Verification protocol and rollback path are present (for the un-defer scenario).
- [x] Status matches the Linear fallback JSON.
