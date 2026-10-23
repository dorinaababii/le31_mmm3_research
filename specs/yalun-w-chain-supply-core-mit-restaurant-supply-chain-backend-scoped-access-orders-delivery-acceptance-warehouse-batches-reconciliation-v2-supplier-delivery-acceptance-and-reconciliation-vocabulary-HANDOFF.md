# HANDOFF — 363-yalun-w-chain-supply-core-delivery-acceptance-before-reconciliation

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-23
**Active feature path**: `/opt/data/le31_mmm3_research/features/363-yalun-w-chain-supply-core-mit-restaurant-supply-chain-backend-scoped-access-orders-delivery-acceptance-warehouse-batches-reconciliation-v2-supplier-delivery-acceptance-and-reconciliation-vocabulary.md`
**LE31 feature gate verdict**: **defer** — LE31 v1 has no supplier role and no inbound-goods concept. The peer value is the **acceptance-before-reconciliation ordering**, which satisfies two charter invariants at once.

## Gate verdict (seven checks)

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | **FAIL** — LE31 tracks what the kitchen *consumes*, not what a supplier *delivers*. The pain (missing deliveries, wrong intake quantities) is a **real restaurant pain that LE31's owner has never reported**. Evidence class: **inferred** from the domain, not observed in LE31. |
| 2 | Viability | **PARTIAL** — a supplier-facing flow is operable, but introduces a third party into a system that today has exactly two roles. |
| 3 | Practicability | **PARTIAL** — Python ✓ ON-STACK. But ERPNext-style supply-chain models assume a warehouse and a stock ledger with different semantics from LE31's. |
| 4 | Conflict | **BLOCKING UNTIL DECIDED** — a supplier is a **third role**. §3.1's two-role discipline (waiter web UI, cook Telegram bot) does not accommodate it. Also brushes §3.7 (supplier contact data). |
| 5 | Outcome / scope | **v2 bucket** — owner-pains territory, but the v2 roadmap is unspecified. |
| 6 | Cost to value | **FAVOURS DEFERRAL** — zero current demand against a whole new role and data domain. |
| 7 | Circuit breaker | **N/A for a defer.** Fully reversible: delete one file, nothing depends on it. |

**Decision: defer.** Fails check 1; check 4 is a charter-level blocker.

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build.

If the trigger condition is met — **the owner opens supplier intake, i.e. begins tracking inbound goods as well as kitchen consumption** — the external coding agent should:

1. Load this artifact and the parent daily-research report (`/opt/data/le31-daily-research-2026-10-23.md`).
2. **Treat the third-role question as the FIRST gate item, not an afterthought.** §3.1 says two primary operational surfaces. A supplier role is a charter decision; take it deliberately or do not take it.
3. Adopt **acceptance-before-reconciliation** as the default ordering: orders → delivery acceptance → warehouse batches → reconciliation. Acceptance is a distinct explicit state between "ordered" and "received"; reconciliation happens after it.
4. **Reconcile BY DERIVATION ONLY.** Any design that mutates a stored balance to "correct" it violates §3.3 and must be rejected, not negotiated. Current stock is derived from entries; it is never written.
5. Model inbound deliveries as **append-only** `InboundDelivery` rows (§3.3) — `supplier_ref`, `accepted_at` (tz-aware, Europe/Paris for business dates), `line_items`, `batch_refs`. Warehouse quantity is derived by folding the ledger.
6. Resolve the §3.7 boundary for supplier contact data **before** storing any supplier identity.
7. Re-run the seven-check gate with those answers in hand.

If the trigger condition is **not** met, do nothing.

## Files to touch

**None today.** If promoted to build (only after the owner opens supplier intake):
- A new `InboundDelivery` SQLModel table — append-only (§3.3).
- A derived-quantity projection — **read-only, never a stored mutable balance** (§3.3).
- **Deliberately unspecified and must stay so until triggered:** supplier identity storage (blocked on §3.7).

## Verification protocol reference

- **Parent-verified direct GET**: `https://api.github.com/repos/yalun-w/chain-supply-core` → HTTP 200, 2026-10-23. Confirms `stargazers_count=0`, `forks_count=0`, `size=786`, `language=Python`, `license.spdx_id=MIT`, `created_at=2026-10-21T08:49:52Z`, `pushed_at=2026-10-21T08:49:59Z` (a **7-second create→push gap** — seeded in one sitting), `archived=false`, `fork=false`, **zero topics**. **Read from `/repos/`, NOT from search-result numbers.**
- **Traction disclosure**: ★0/0⑂ is recorded as **NO traction evidence in either direction**. The description's own phrase "Code-only open-source extraction" indicates this is extracted code, not an independently-run project.
- **Raw fetch**: `/tmp/le31-daily-2026-10-23/pv/yalun-w_chain-supply-core.json`
- **Anti-fabrication canary**: `grep -rcF 'LE31' /tmp/le31-daily-2026-10-23/` → 0 files with non-zero matches (parent-run).
- **Distinct-from-features**: verified 0 matches against all 349 pre-existing files in `features/`.

## Rollback path

Fully reversible. Vocabulary-only artifact — delete `features/363-*.md` and this HANDOFF, revert the commit. No runtime dependency, no schema, no migration, no retained data.

## Mandatory LE31 skill list

- `le31-conventions` — seven-check gate, hard invariants (§3.1 two-role discipline, §3.3 append-only ledger + derived state, §3.7 privacy boundary).
- `le31-research` — GitHub-as-source-of-truth discipline.
- `le31-v1-feature-pattern` — canonical contract shape (informative: this is a v2-bucket pick).
- Do NOT load `le31-feature-pipeline` until this defer is promoted to build by the owner. Note `le31 v2 owner-pains` **does not exist** in the workspace; per `le31-feature-pipeline/SKILL.md` line 33 a sub-issue would attach to `le31 Research` (P-HMM-1).