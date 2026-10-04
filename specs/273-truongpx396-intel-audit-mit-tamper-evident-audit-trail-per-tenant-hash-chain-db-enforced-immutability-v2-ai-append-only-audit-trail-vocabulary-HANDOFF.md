# Pick B — `truongpx396/intel-audit` — v2-AI append-only-audit-trail-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/273-truongpx396-intel-audit-mit-tamper-evident-audit-trail-per-tenant-hash-chain-db-enforced-immutability-v2-ai-append-only-audit-trail-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2-AI PR that adds a `tenant_id UUID NULL` column + a `prev_hash VARCHAR(64) NULL` column + a `hash VARCHAR(64) NULL` column to the existing `audit_logs` SQLModel table.
2. First v2-AI PR that adopts a `verify_audit_log_chain(tenant_id)` Python service that computes the hash-chain + verifies the tamper-evident posture.
3. First v2-AI PR that adds a `/api/audit-logs/verify` + `/api/audit-logs/<log_id>/verify` FastAPI endpoint set.
4. First v2-AI PR that adopts a Postgres-extension-style hash-chain-engine (e.g., a Postgres-extension that computes the hash-chain + enforces the database-enforced-immutability).
5. First v2-AI PR that adopts a *spec-driven-development* posture on the existing audit_logs schema (i.e., the `audit_logs` schema is documented as a spec before any code change).
6. First v2-AI PR that adopts a *retention-no-tampering* posture on the existing audit_logs retention policy.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v2-AI surface wants to add a **tenant-isolated-hash-chain + database-enforced-immutability + tamper-evident + retention-no-tampering** surface to the existing `audit_logs` SQLModel table (e.g., a v2-AI surface that extends the existing audit_logs with a *per-tenant-hash-chain* + *REVOKE UPDATE / REVOKE DELETE on audit_logs* + *append-only-records* discipline), the operator wants a known-good Go-library-or-container blueprint with tenant-isolation + hash-chain + database-enforced-immutability + retention-no-tampering + spec-driven-development posture, but LE31 today has a *single-tenant* + *no-hash-chain* + *no-database-enforced-immutability* + *no-retention-no-tampering* audit_logs surface, so that any future v2-AI extension has a documented reference."* — PASS (links to features 121 + 133 + 135 + 137 + 159 + 161 + 187 + 192 + 197 + 203 + 257 + 258 + 263 + 271; justifies a new v2-AI pain).
2. **Viability** — Owner does not need to understand the implementation; they only see the *tenant-isolated-hash-chain + database-enforced-immutability + tamper-evident + retention-no-tampering* surface on the existing minimal-HTML/HTMX audit_logs dashboard. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 N/A (no AI surface); confidence **high** for vocabulary transferability, **low** for immediate LE31 v2-AI urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling + observable-evidence + non-AI-surface; §3.1 explicit-state-transitions preserved; §3.3 append-only-StockEntry invariant preserved. PASS.
5. **Outcome, appetite, and scope** — **v2-AI** outcome (cross-section to features 121 + 133 + 135 + 137 + 159 + 161 + 187 + 192 + 197 + 203 + 257 + 258 + 263 + 271). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = medium (~300-500 lines of Python + SQLModel + Alembic + optional-Go-library-wrapper + Postgres-extension code; 10-20 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/audit_logs.py` (modified) — add `tenant_id UUID NULL`, `prev_hash VARCHAR(64) NULL`, `hash VARCHAR(64) NULL` columns to the existing `AuditLog` SQLModel table
- `le31/app/services/audit_logs.py` (modified) — add `verify_audit_log_chain(tenant_id)` + `compute_audit_log_hash(tenant_id, log_id)` + `record_audit_log(tenant_id, actor, action, payload)` Python services
- `le31/app/services/audit_logs_hash_chain.py` (new) — hash-chain-engine service that computes the per-tenant hash-chain + verifies the tamper-evident posture (Python wrapper around the Go library via ctypes / cffi / subprocess if Go-library is adopted)
- `le31/app/api/v1/audit_logs.py` (modified) — add `GET /api/audit-logs/verify` + `POST /api/audit-logs/verify` + `GET /api/audit-logs/<log_id>/verify` + `POST /api/audit-logs/<log_id>/verify` FastAPI endpoint set
- `le31/app/owner_dashboard/templates/audit_logs_verify.html` (new) — minimal-HTML/HTMX owner-dashboard template for audit-logs-verify
- `le31/migrations/versions/<revision>_audit_logs_hash_chain.py` (new) — Alembic migration for the new columns + the *REVOKE UPDATE / REVOKE DELETE on audit_logs* permission migration
- `le31/app/database/audit_logs_retention.sql` (new) — Postgres-extension-style retention-no-tampering policy migration

## Verification protocol reference

- Run `pytest le31/tests/test_audit_logs_hash_chain.py -v` to verify the new columns + endpoints + minimal-HTML/HTMX template
- Run `pytest le31/tests/test_audit_logs_tamper_evidence.py -v` to verify the tamper-evident posture
- Run `pytest le31/tests/test_audit_logs_retention_no_tampering.py -v` to verify the retention-no-tampering posture
- Run `pytest le31/tests/test_charter_3_3_append_only_ledger.py -v` to verify §3.3 append-only-StockEntry invariant (the *tenant-isolated-hash-chain + database-enforced-immutability* discipline is compatible with the existing §3.3 invariant)
- Run `pytest le31/tests/test_charter_3_6_money_primitive.py -v` to verify §3.6 money-primitive invariant (the *audit_logs* is NOT a money-primitive; the *tenant-isolated-hash-chain* is operator-tooling only)

## Rollback path

- Revert the SQLModel migration: `alembic downgrade -1`
- Restore the original *audit_logs* permissions: `GRANT UPDATE, DELETE ON audit_logs TO <role>`
- Delete the new files (`le31/app/services/audit_logs_hash_chain.py` + `le31/app/owner_dashboard/templates/audit_logs_verify.html` + `le31/migrations/versions/<revision>_audit_logs_hash_chain.py` + `le31/app/database/audit_logs_retention.sql`)
- Revert the `audit_logs` table changes (drop `tenant_id + prev_hash + hash` columns)
- Restart the FastAPI server

## Mandatory LE31 skill list

- `le31-conventions` (charter §3.1 + §3.2 + §3.3 + §3.4 + §3.6 + §3.7 invariants; seven-check feature gate)
- `le31-feature-pipeline` (vocabulary-to-build pipeline + parking-lot-vs-build decision)
- `le31-v1-feature-pattern` (existing v1 feature patterns + audit_logs-schema invariants)
- `le31-data` (existing audit_logs + sqlmodel-extensions patterns + hash-chain-engine patterns)
- `le31-quality-gates` (existing quality-gates + tamper-evident posture patterns)