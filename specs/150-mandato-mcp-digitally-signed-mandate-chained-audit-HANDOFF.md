# Slice HANDOFF — Feature 150 (Mandato MCP digitally-signed-mandate chained-audit)

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## Active feature path

`/opt/data/le31_mmm3_research_work/features/150-mandato-mcp-digitally-signed-mandate-chained-audit.md`

## Frozen contract fields

| Field | Value |
|---|---|
| Feature ID | 150 |
| Slug | `mandato-mcp-digitally-signed-mandate-chained-audit` |
| Bucket | v2 owner-pains (architecture-reference) |
| Decision | **defer (parking-lot)** |
| Evidence class | inferred |
| Confidence | medium (mechanism) / low (present urgency) |
| Source paper | arXiv 2608.14074 (2026-08-14, 0 citations, Giovanni Racioppi) |
| Source URL | https://doi.org/10.48550/arxiv.2608.14074 |
| Window | in-window by `publication_date` 2026-08-14 |
| Charter conflict | none |

## Seven-check gate verdict (defer rationale)

1. **Raison d'être / JTBD** — Inferred only. No observed LE31 v1 pain.
2. **Viability** — Mechanism is well-defined; LE31 v1 has no AI-agent surface, so viability is conditional on v2.
3. **Practicability and confidence** — Confidence: medium. No MCP, no agent surface in v1. No rabbit holes visible today.
4. **Conflict** — None. Charter §3.4 (no customer-facing AI) is the *trigger* for this primitive's relevance, not a conflict.
5. **Outcome, appetite, scope** — v2 owner-pains. Appetite: zero today.
6. **Cost to operational value** — Zero cost today; zero value today. Future contingency value: medium.
7. **Circuit breaker and reversibility** — Trivially reversible: written reference, no code.

## Files to touch (when this becomes buildable)

| File | Action |
|---|---|
| `features/150-mandato-mcp-digitally-signed-mandate-chained-audit.md` | Read-only (already exists) |
| `backend/audit_logs.py` | Add `mandate_hash` column (v2) — populates with SHA-256 of operator-signed mandate |
| `backend/stock_entry.py` | Reference `mandate_hash` from `StockEntry` (v2) |
| New migration | `migrations/versions/XXXX_add_mandate_hash_to_audit_logs.py` (v2) |
| `backend/tests/test_audit_logs.py` | Test mandate-hash derivation (v2) |

## Verification protocol (v2)

1. Reproduce the end-to-end mandate-hash flow on the configured environment:
   - Cook confirms order → `audit_logs` row written with `mandate_hash` = SHA-256(canonicalised_row).
   - Tamper attempt on a single `audit_logs` row → `mandate_hash` mismatch on verification.
2. Inspect the actual database rows after the change is applied.
3. Confirm forbidden transitions (delete a row, edit a row) are detected by hash-chain verification.
4. Run lint, type check, and tests available in this repo.
5. Commit, push, and report with the required evidence.

## Rollback / feature-removal path (v2)

- One-shot migration reverses `mandate_hash` column drop.
- `audit_logs` rows written before the column was added retain their NULL `mandate_hash` value (acceptable; the *tamper-evident* primitive applies only to rows written after the column was added).
- Existing v1 `audit_logs` consumer code does not depend on `mandate_hash`; no v1 behaviour change.

## Mandatory LE31 skill list

- `skills/le31-conventions/SKILL.md` — global LE31 decision layer (append-only invariant, charter §3.1)
- `skills/le31-v1-feature-pattern/SKILL.md` — v1 feature contract shape (v2 work inherits the slicing rules)
- `skills/le31-handoff-spec/SKILL.md` — handoff-to-coding-agent discipline
- `skills/le31-coding-agent-brief/SKILL.md` — paste-in prompt format

## Trigger policy

Do not implement this slice today. **Re-evaluate the `defer` decision if and only if** LE31 v2 introduces an AI-assisted operator surface (charter §3.4 trigger condition). Until then, this HANDOFF is a written reference, no code.

## Sign-off gap

None today (defer status). When this becomes buildable, the v2 owner must sign off on the *charter §3.4 trigger condition* before the slice is implemented.
