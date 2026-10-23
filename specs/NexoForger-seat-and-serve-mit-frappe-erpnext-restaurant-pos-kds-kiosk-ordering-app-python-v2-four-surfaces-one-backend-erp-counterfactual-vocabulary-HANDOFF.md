# HANDOFF — 364-NexoForger-seat-and-serve-frappe-erpnext-erp-counterfactual

**Status**: defer (parking-lot, watch-list, counterfactual record, no build today)
**Date**: 2026-10-23
**Active feature path**: `/opt/data/le31_mmm3_research/features/364-NexoForger-seat-and-serve-mit-frappe-erpnext-restaurant-pos-kds-kiosk-ordering-app-python-v2-four-surfaces-one-backend-erp-counterfactual-vocabulary.md`
**LE31 feature gate verdict**: **defer** — adoption would be a rewrite, not an integration. Filed as the pass's only serious **counterfactual**: the ERP-monolith route LE31 deliberately does not take.

## Gate verdict (seven checks)

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | **FAIL as adoption** — LE31's owner wants the *smallest useful ops system*, which §3.1 already settles. The ERP route answers a question the charter has answered. Evidence class: **assumed**. |
| 2 | Viability | **FAIL as adoption** — an ERP carries its own administration burden, configuration, and specialist-maintenance expectation, all of which check 2 exists to exclude. |
| 3 | Practicability | **FAIL as adoption** — Python ✓ matches, Postgres ✓ matches, but **Frappe/ERPNext is entirely OFF-STACK** and ERPNext's double-entry stock ledger is categorically different from LE31's §3.3 append-only `StockEntry` with derived state. Mapping one to the other is the entire cost. |
| 4 | Conflict | **HARD CONFLICT** — adoption is a §3.1 **stack change**, which requires an explicit charter decision. None exists. Secondary conflict: POS + KDS + kiosk + ordering = **four clients** against §3.1's two-role discipline. |
| 5 | Outcome / scope | **NOT REACHED** — v2 bucket, and unreachable without a charter amendment. |
| 6 | Cost to value | **FAVOURS DEFERRAL** — a rewrite to serve an unchanged set of pains. |
| 7 | Circuit breaker | **N/A for a defer.** Fully reversible: delete one file, nothing depends on it. |

**Decision: defer.** Check 4 is a hard blocker: this is a charter-level question, not a feature.

## Trigger policy

This is a **defer artifact (parking-lot)** — a counterfactual record. It does not start a build.

This artifact has a **different trigger** from the other two picks. It does not wait for LE31 to want what the pick offers. It waits for the **stack decision itself** to be reopened:

> **If the owner ever reopens the §3.1 stack decision**, this pick is the named counterfactual to weigh against the smallest-useful-ops-system principle — and that decision would be a **charter amendment**, taken deliberately, with **its own research pass**. This artifact does not authorise it.

Secondary trigger: **if LE31 ever adds a kiosk or any surface beyond the two charter roles**, re-read this artifact together with feature 355 (`Haroon-World/RestaurantPOS_Android`, which would be client 3). Do not treat each as a standalone addition — the surface-count tension compounds.

If neither trigger fires, do nothing.

## Files to touch

**None today, and none under this artifact.** An ERP adoption is a rewrite with a different data model; it must never be smuggled in as an implementation task. Any such work requires an explicit charter amendment **first**.

## Verification protocol reference

- **Parent-verified direct GET**: `https://api.github.com/repos/NexoForger/seat-and-serve` → HTTP 200, 2026-10-23. Confirms `stargazers_count=2`, `forks_count=0`, `size=1928`, `language=Python`, `license.spdx_id=MIT`, `created_at=2026-10-01T10:22:51Z`, `pushed_at=2026-10-22T16:45:09Z`, `archived=false`, `fork=false`, **zero topics**. **Read from `/repos/`, NOT from search-result numbers.**
- **Traction disclosure**: ★2/0⑂ with zero topics — minimal evidence in either direction. The pick is about the *shape*, not the project's adoption.
- **Raw fetch**: `/tmp/le31-daily-2026-10-23/pv/NexoForger_seat-and-serve.json`
- **Anti-fabrication canary**: `grep -rcF 'LE31' /tmp/le31-daily-2026-10-23/` → 0 files with non-zero matches (parent-run).
- **Distinct-from-features**: verified 0 matches against all 349 pre-existing files in `features/`.

## Rollback path

Fully reversible. Vocabulary-only artifact — delete `features/364-*.md` and this HANDOFF, revert the commit. No runtime dependency, no schema, no migration, no retained data.

**Rollback asymmetry note:** this pick carries no safety property, so there is no rollback that would be mistaken for discarding one. (Recorded so it is not conflated with the 2026-10-21 policy-chokepoint pick, where reverting *does* discard a safety property.)

## Mandatory LE31 skill list

- `le31-conventions` — seven-check gate, hard invariants (§3.1 two-role discipline **and the stack-change rule**, §3.3 append-only ledger, §3.4 chokepoint).
- `le31-research` — GitHub-as-source-of-truth discipline.
- `le31-v1-feature-pattern` — canonical contract shape (informative: this is a v2-bucket pick).
- Do NOT load `le31-feature-pipeline` until this defer is promoted by the owner **and** a §3.1 charter amendment exists. Note `le31 v2 owner-pains` **does not exist** in the workspace; per `le31-feature-pipeline/SKILL.md` line 33 a sub-issue would attach to `le31 Research` (P-HMM-1).