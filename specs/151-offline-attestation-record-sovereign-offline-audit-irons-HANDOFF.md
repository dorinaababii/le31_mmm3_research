# Slice HANDOFF — Feature 151 (Offline Attestation Record sovereign-offline tamper-evident audit)

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## Active feature path

`/opt/data/le31_mmm3_research_work/features/151-offline-attestation-record-sovereign-offline-audit-irons.md`

## Frozen contract fields

| Field | Value |
|---|---|
| Feature ID | 151 |
| Slug | `offline-attestation-record-sovereign-offline-audit-irons` |
| Bucket | v2 owner-pains (architecture-reference) |
| Decision | **defer (parking-lot)** |
| Evidence class | inferred |
| Confidence | medium (mechanism) / low (present urgency) |
| Source paper | Zenodo 22143718 (2026-08-28, **12 citations**, Micky Irons) |
| Source URL | https://doi.org/10.5281/zenodo.22143718 |
| Window | in-window by `publication_date` 2026-08-28 |
| Charter conflict | none (additive to §3.1; no third-party attestation service in §3.2) |

## Seven-check gate verdict (defer rationale)

1. **Raison d'être / JTBD** — Inferred only. No observed LE31 v1 pain.
2. **Viability** — Mechanism is well-defined (offline, sovereign, tamper-evident).
3. **Practicability and confidence** — Confidence: medium. Stack: Python stdlib `hashlib` covers SHA-256; optional `cryptography` for ECDSA; on-premises key-management is the only v2-dependency.
4. **Conflict** — None. Charter §3.1 (append-only) is preserved; §3.2 (privacy) is preserved (no third-party attestation service).
5. **Outcome, appetite, scope** — v2 owner-pains. Appetite: zero today.
6. **Cost to operational value** — Zero cost today; zero value today. Future contingency value: high.
7. **Circuit breaker and reversibility** — Trivially reversible: written reference, no code.

## Files to touch (when this becomes buildable)

| File | Action |
|---|---|
| `features/151-offline-attestation-record-sovereign-offline-audit-irons.md` | Read-only (already exists) |
| `backend/audit_logs.py` | Add `row_hash` column (SHA-256 of canonicalised row) + `prev_row_hash` column (chain-link) |
| New migration | `migrations/versions/XXXX_add_hash_chain_to_audit_logs.py` (v2) |
| `backend/tests/test_audit_logs.py` | Test hash-chain tamper-evidence (v2) |
| Optional: `backend/key_management.py` | On-premises ECDSA key storage (v2 only if signatures are required) |

## Verification protocol (v2)

1. Reproduce the end-to-end hash-chain flow on the configured environment:
   - New `audit_logs` row written → `row_hash` = SHA-256(canonicalised_row); `prev_row_hash` = previous row's `row_hash`.
   - Tamper attempt on a single row → `row_hash` mismatch + chain breaks at the tampered row.
2. Inspect the actual database rows after the change is applied.
3. Confirm forbidden transitions (delete a row, edit a row) are detected by hash-chain verification.
4. If signatures are added: confirm ECDSA signature verification catches operator-level tampering.
5. Run lint, type check, and tests available in this repo.
6. Commit, push, and report with the required evidence.

## Rollback / feature-removal path (v2)

- One-shot migration reverses `row_hash` and `prev_row_hash` column drop.
- `audit_logs` rows written before the columns were added retain their NULL `row_hash` / `prev_row_hash` values (acceptable; the *tamper-evident* primitive applies only to rows written after the columns were added).
- Existing v1 `audit_logs` consumer code does not depend on `row_hash`; no v1 behaviour change.

## Mandatory LE31 skill list

- `skills/le31-conventions/SKILL.md` — global LE31 decision layer (append-only invariant, charter §3.1)
- `skills/le31-v1-feature-pattern/SKILL.md` — v1 feature contract shape (v2 work inherits the slicing rules)
- `skills/le31-handoff-spec/SKILL.md` — handoff-to-coding-agent discipline
- `skills/le31-coding-agent-brief/SKILL.md` — paste-in prompt format

## Trigger policy

Do not implement this slice today. **Re-evaluate the `defer` decision if and only if** LE31 v2 introduces a cryptographic-verifiability requirement (regulator-facing audit-export surface, partner-facing audit-export surface, or owner-facing audit-export surface with non-repudiation requirements). Until then, this HANDOFF is a written reference, no code.

## Sign-off gap

None today (defer status). When this becomes buildable, the v2 owner must sign off on the *trigger condition* (regulator/partner/owner-facing audit-export requirement) before the slice is implemented.
