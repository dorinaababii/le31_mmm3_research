# Slice HANDOFF — Feature 152 (LATTICE governance-first authorized-autonomous-AI architecture)

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## Active feature path

`/opt/data/le31_mmm3_research_work/features/152-lattice-governance-first-authorized-ai-architecture-calboreanu.md`

## Frozen contract fields

| Field | Value |
|---|---|
| Feature ID | 152 |
| Slug | `lattice-governance-first-authorized-ai-architecture-calboreanu` |
| Bucket | v2 owner-pains (architecture-reference) |
| Decision | **defer (parking-lot)** |
| Evidence class | inferred |
| Confidence | medium (mechanism) / low (present urgency) |
| Source paper | Frontiers in Artificial Intelligence, DOI 10.3389/frai.2026.1800407 (2026-08-14, **3 citations**, Elias Calboreanu, **peer-reviewed**) |
| Source URL | https://doi.org/10.3389/frai.2026.1800407 |
| Window | in-window by `publication_date` 2026-08-14 |
| Charter conflict | none (peer-reviewed governance pattern, not customer-facing AI) |

## Seven-check gate verdict (defer rationale)

1. **Raison d'être / JTBD** — Inferred only. No observed LE31 v1 pain.
2. **Viability** — Mechanism is well-defined (governance contract → operational events).
3. **Practicability and confidence** — Confidence: medium-high (peer-reviewed venue, 3 citations in ~24 days). No v1 surface impact.
4. **Conflict** — None. Charter §3.1 (operational-first) is preserved for v1; LATTICE is a v2 inversion pattern, not a v1 conflict.
5. **Outcome, appetite, scope** — v2 owner-pains. Appetite: zero today.
6. **Cost to operational value** — Zero cost today; zero value today. Future contingency value: medium.
7. **Circuit breaker and reversibility** — Trivially reversible: written reference, no code.

## Files to touch (when this becomes buildable)

| File | Action |
|---|---|
| `features/152-lattice-governance-first-authorized-ai-architecture-calboreanu.md` | Read-only (already exists) |
| `backend/governance_rules.py` | New module: governance-contract storage and authoring surface (v2) |
| `backend/rules_to_events.py` | New module: derivation engine (rules → `StockEntry` events) (v2) |
| `backend/verify_governance.py` | New module: verification layer (events satisfy rules) (v2) |
| New migration | `migrations/versions/XXXX_add_governance_rules.py` (v2) |
| `backend/tests/test_governance_rules.py` | Test rules-to-events derivation (v2) |

## Verification protocol (v2)

1. Reproduce the end-to-end governance-first flow on the configured environment:
   - Owner authors a shift-reconciliation rule → `governance_rules` row written.
   - System derives `StockEntry` events from the rule + operational inputs.
   - `verify_governance` confirms derived events satisfy the rule.
2. Inspect the actual database rows after the change is applied.
3. Confirm forbidden transitions (rule emits event that violates an invariant) are detected by verification.
4. Run lint, type check, and tests available in this repo.
5. Commit, push, and report with the required evidence.

## Rollback / feature-removal path (v2)

- One-shot migration drops `governance_rules` table.
- `StockEntry` rows written via the derivation engine are persisted in the existing `stock_entries` table; rolling back the *governance-first* surface does not delete the *operational events* themselves.
- Existing v1 `StockEntry` consumer code does not depend on `governance_rules`; no v1 behaviour change.

## Mandatory LE31 skill list

- `skills/le31-conventions/SKILL.md` — global LE31 decision layer (append-only invariant, charter §3.1)
- `skills/le31-v1-feature-pattern/SKILL.md` — v1 feature contract shape (v2 work inherits the slicing rules)
- `skills/le31-handoff-spec/SKILL.md` — handoff-to-coding-agent discipline
- `skills/le31-coding-agent-brief/SKILL.md` — paste-in prompt format

## Trigger policy

Do not implement this slice today. **Re-evaluate the `defer` decision if and only if** LE31 v2 introduces an owner-facing reconciliation-rules authoring surface (e.g., shift-specific closing-time rules, prep-cost rules, etc.). Until then, this HANDOFF is a written reference, no code.

## Sign-off gap

None today (defer status). When this becomes buildable, the v2 owner must sign off on the *trigger condition* (owner-facing reconciliation-rules authoring surface) before the slice is implemented.
