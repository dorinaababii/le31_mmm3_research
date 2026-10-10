# HANDOFF — Feature 300: `farooqarahim-glassbox-...-v2-ai-eu-ai-act-ledger-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/300-farooqarahim-glassbox-apache-2-0-tamper-evident-audit-ledger-ai-systems-hash-chained-hybrid-ed25519-ml-dsa-65-signed-append-only-records-llm-interaction-rust-python-typescript-go-sdks-v2-ai-eu-ai-act-ledger-vocabulary.md` — defer/parking-lot (Pick B of Daily Research 2026-10-10).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes an *EU AI Act Article 50 + post-quantum-signature + MCP-server + hash-chained + Python SDK* primitive, the owner wants *evidence that this EU-AI-Act-ledger-vocabulary exists in 2026 with a post-quantum-signature shape + Python SDK*, but struggles because *most v2-AI audit-ledger candidates are off-stack OR lack post-quantum readiness OR lack EU AI Act awareness OR lack Python SDK*, so that *the v2-AI surface has a credible peer reference with a forward-compatible signature scheme*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (audit-ledger + EU-AI-Act + MCP + Python SDK). The 5★ with single-maintainer cadence (99-day-old repo, in-window push today) makes code adoption not viable, but the *vocabulary reference* is viable. |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: **Python SDK on-stack** (Rust core is off-LE31-stack but the Python SDK bridges). Required data + permissions + infrastructure: Python runtime + hash-chained audit-log + Ed25519 + ML-DSA-65 signature keys + MCP-server. The `eu-ai-act + mcp + llm + post-quantum-cryptography` topics suggest a §3.4-aware AI integration. **The post-quantum signature (ML-DSA-65, NIST FIPS 204) is the only post-quantum-readiness signal of the 72-pass series** = strong v2-AI forward-compatibility. Evidence strength: high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant as a vocabulary reference. The `eu-ai-act` topic is OFF v1 charter (v2-AI surface). The `mcp` topic is OFF v1 charter (v2-AI surface). The Python SDK + audit-log + signature primitives are §3.1-aligned (append-only discipline + explicit state transitions). No §3.4 customer-facing AI (the AI is operator/staff-assist via MCP-server). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI outcome (EU-AI-Act-compliance primitive). Maximum time worth spending: 1 hour documentation. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | ~30 min documentation; zero code cost. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (single-maintainer + Rust core off-LE31-stack + EU-AI-Act + MCP + post-quantum-signature v2-AI surface is OFF v1 charter).

## Bucket

**v2-AI** (EU-AI-Act-ledger-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description names the 9-primitive set (`tamper-evident + hash-chained + hybrid Ed25519 + ML-DSA-65 signed + append-only + EU-AI-Act + MCP + Python SDK`) + the tech-stack (Rust core + Python + TypeScript + Go SDKs).

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires EU AI Act Article 50 compliance + post-quantum-signature + MCP-server + hash-chained + Python SDK):

1. `backend/app/llm_audit/models.py` — add new `LLMAuditLogEntry` SQLModel table with columns: `id` (UUID), `llm_id` (str), `request` (JSON), `response` (JSON), `model` (str), `prompt_hash` (str), `completion_hash` (str), `previous_entry_hash` (str), `this_entry_hash` (str), `ed25519_signature` (str), `ml_dsa_65_signature` (str), `created_at` (timezone-aware datetime), `recorded_at` (timezone-aware datetime).
2. `backend/app/llm_audit/models.py` — add new `llm_audit_log_merkle_proofs` SQLModel table with columns: `id` (UUID), `entry_id` (UUID FK), `merkle_root` (str), `merkle_proof` (JSON), `created_at`.
3. `backend/app/llm_audit/models.py` — add new `eu_ai_act_registry` SQLModel table that tracks the registered AI systems + their EU AI Act Article 50 labels.
4. `backend/alembic/versions/` — add Alembic migration for the new tables.
5. `backend/app/llm_audit/repository.py` — add an `INSERT ... ON CONFLICT DO NOTHING` guard on the `LLMAuditLogEntry` insert path.
6. `backend/app/llm_audit/signatures.py` — NEW: Ed25519 + ML-DSA-65 hybrid signature utility (uses `cryptography` library for Ed25519 + `pqcrypto` library for ML-DSA-65).
7. `backend/app/llm_audit/merkle.py` — NEW: Merkle-tree utility for efficient verification.
8. `backend/app/api/v2/llm/audit_log.py` — NEW: `POST /v2/llm/audit-log/entries` endpoint to record an entry.
9. `backend/app/api/v2/llm/audit_log.py` — NEW: `GET /v2/llm/audit-log/entries/verify` endpoint that walks the chain + verifies both Ed25519 + ML-DSA-65 signatures.
10. `backend/app/api/v2/llm/audit_log.py` — NEW: `GET /v2/llm/audit-log/entries/<entry_id>/merkle-proof` endpoint.
11. `backend/app/api/v2/llm/audit_log.py` — NEW: `GET /v2/llm/audit-log/entries?llm_id=<>&as_of=<>` query endpoint.
12. `backend/app/mcp_server/llm_audit.py` — NEW: MCP-server integration that exposes the verify + merkle-proof endpoints via MCP (uses `mcp` library).
13. `backend/requirements.txt` — add `cryptography>=42.0.0` (Ed25519 signing); add `pqcrypto>=0.1.0` (ML-DSA-65 signing); add `mcp>=1.0.0` (MCP-server integration).

## Verification protocol

1. `git clone https://github.com/farooqarahim/glassbox` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/farooqarahim/glassbox/main/README.md` (deferred; the README is the source of truth for the verbatim description + topic set).
3. `curl -sS -H "Authorization: Bearer $HERME...OKEN" "https://api.github.com/repos/farooqarahim/glassbox"` for star count, fork count, license, language, pushed_at, created_at, topics, description (parent-verified 2026-10-10).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the EU-AI-Act + post-quantum + MCP + Python SDK changes are isolated to the expected files.
5. Per `le31-conventions/SKILL.md`: load `le31-conventions`, `le31-research`, `le31-v1-feature-pattern`, `le31-handoff-spec` before any implementation.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2-AI trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the new tables + remove the new API endpoints + remove the MCP-server integration.
- No data loss if the rollback happens BEFORE any LLM-audit-log-entry row is written.
- Full data retention if the rollback happens AFTER rows are written (the new tables are dropped but the original `audit_logs` rows are preserved per the *append-only* invariant).

## Mandatory LE31 skill list

Before any implementation, the coding agent must load:
1. `le31-conventions` — the global LE31 decision layer (charter invariants + feature gate).
2. `le31-research` — the research workflow.
3. `le31-v1-feature-pattern` — v1 feature-pattern enforcement (append-only StockEntry, etc.).
4. `le31-handoff-spec` — the handoff-spec requirements (frozen contract discipline, mandatory skill list, verification protocol).
5. `le31-feature-pipeline` — the feature-pipeline workflow (parent research issue, sub-issue creation, handoff file).

## Linear sub-issue reference

Sub-issue draft (deferred pending Linear MCP write endpoint recovery): `Research 2026-10-10 / Pick B — v2-AI EU-AI-Act-ledger-vocabulary (farooqarahim/glassbox)`. Parent fallback JSON captures the intended sub-issue at `/opt/data/le31-daily-research-2026-10-10.linear-fallback.json`. Sub-issue project = `le31 Research` (P-HMM-1) per `le31-feature-pipeline/SKILL.md` line 33 since `le31 v2-AI` does not exist.

## Parent research issue

[linear: blocked — workspace plan-limit error 20th consecutive day; parent fallback at `/opt/data/le31-daily-research-2026-10-10.linear-fallback.json`]
