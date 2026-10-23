# HANDOFF — Feature 365: `ytzhiyun-bucketbook-reconciliation-returnable-deposit-vocabulary`

**Upstream source repo: [`ytzhiyun/bucketbook`](https://github.com/ytzhiyun/bucketbook)** — see `features/365-ytzhiyun-bucketbook-reconciliation-returnable-deposit-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/365-ytzhiyun-bucketbook-reconciliation-returnable-deposit-vocabulary.md` — defer/parking-lot (Pick B of Daily Brainstorm 2026-10-23).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ⚠️ | **No JTBD — recorded as a gap, not a need.** LE31 sells food; it does not lend containers. The justification is that the *accounting shape* (an item carrying a liability until it returns) is absent from the model and its absence is currently unfalsifiable because nobody has asked the question. |
| 2 | Viability | ✓ | **MIT ✓ §3.2 STRICTLY-COMPATIBLE**, ★2⑂0, 1,133 KB. **Traction caveat: one day old, no evidence in either direction.** For a restaurant the concept would need explaining to staff — a deposit is not a restaurant-native idea. |
| 3 | Practicability and confidence | ✓ | No code adoptable (HTML, browser-local storage). Vocabulary only. Evidence strength: **high** that the shape works in water delivery (a real trade with real deposit economics); **low** that it transfers — the restaurant case is **inferred, not observed**, and is labelled as such in the feature. |
| 4 | Conflict | ✓ | Does not violate an invariant *as vocabulary*. **⚠️ If ever built it would be charter-level:** a deposit is a **monetary liability**, not a quantity. §3.3 says current stock is *derived from entries*; a liability is derived from a different equation. Admitting liabilities means LE31's stock model stops being purely quantitative. That is an owner/charter decision, not an implementation detail. |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v1 defer outcome. Max time: 45 min documentation. **Today: 0 build time.** |
| 6 | Cost to operational value | ✓ | Value is keeping a genuinely absent concept visible without pretending the answer is obvious. ~45 min documentation. |
| 7 | Circuit breaker + reversibility | ✓ | No code; revert by `git rm`. |

**Gate verdict: `defer` (parking-lot)** — 7/7 checks pass. `defer` because the charter question (does v1 admit liabilities?) is unmade, and because no LE31 user has described a returnable-asset case.

## Bucket

**v1 (reconciliation-as-the-product + returnable-deposit round-trip vocabulary)** — Pick B of Daily Brainstorm 2026-10-23. `le31 v1 — Core MVP` exists (P-HMM-3), but per `le31-feature-pipeline/SKILL.md` line 33 and the consistent practice of recent passes, this sub-issue attaches to **`le31 Research` P-HMM-1** as the parent of the sub-issues.

## Files to touch

**None today.** Documentation-only.

If an owner ever describes a real returnable-asset case, the expected files are:

- `backend/models/returnable_asset_type.py` — new `ReturnableAssetType` (type, deposit_amount_eur, active).
- `backend/models/asset_movement.py` — new **append-only** `AssetMovement` (asset_type_id, dispatched_delta, returned_delta, reason, business_date). **Never updated or deleted** — same rule as `StockEntry`.
- `backend/services/returnable_balance_service.py` — derives the outstanding balance as a **projection**, never a stored mutable figure (the §3.3 rule).
- `backend/services/reconciliation_service.py` — the 对账 surface: period report reconciling dispatched vs returned vs paid.
- `backend/alembic/versions/` — migration for both tables.
- `tests/test_returnable_balance_service.py` — assert the derived balance is reproducible from entries alone (delete nothing, recompute, compare).

## Verification protocol reference

`le31-conventions`: "Declaring done from a diff or passing tests alone" is a pitfall. When built, exercise reconciliation on a real period with deliberate discrepancies and observe the report surfacing them — a reconciliation screen that cannot show a discrepancy is not a reconciliation screen.

## Rollback path

`git rm features/365-*.md specs/368-*-HANDOFF.md`. Documentation-only. Fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — invariants and the seven-check gate
- `le31-data` — append-only ledger rules; projections over stored state
- `le31-finance-analytics` — EUR exactness (a deposit is money: §3.6 forbids binary floats)
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth

## Open questions carried into any future build

1. **Does v1's stock model admit liabilities at all?** Unmade, charter-level.
2. **Is reconciliation a v1 feature?** Implicit in the StockEntry projection but has no surface. Feature 349 (`gfs-invoice-breakdown`, filed 2026-10-20) filed the supplier-document side.
3. **The browser-local storage posture is explicitly REJECTED for v1** (charter §3.5 server-side Postgres) — recorded as a contrast case only, never as an architecture proposal.