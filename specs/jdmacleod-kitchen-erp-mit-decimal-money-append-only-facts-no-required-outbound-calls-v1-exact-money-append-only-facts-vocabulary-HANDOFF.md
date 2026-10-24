# HANDOFF — Feature 370: `jdmacleod/kitchen-erp` — exact-money + append-only-facts vocabulary

**Upstream source repo: [`jdmacleod/kitchen-erp`](https://github.com/jdmacleod/kitchen-erp)** — see `features/370-jdmacleod-kitchen-erp-mit-decimal-money-append-only-facts-no-required-outbound-calls-fastapi-sqlalchemy-postgresql-v1-exact-money-append-only-facts-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/370-jdmacleod-kitchen-erp-mit-decimal-money-append-only-facts-no-required-outbound-calls-fastapi-sqlalchemy-postgresql-v1-exact-money-append-only-facts-vocabulary.md` — defer/parking-lot (Pick A of Daily Research 2026-10-24).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL** | When the owner wants to know what ingredients cost, they want *supplier price history*, but LE31 has **no reported cost pain** and no supplier role — evidence class **inferred**. **A failing check 1 is what makes this a defer.** |
| 2 | Viability | ✓ | MIT ✓ §3.2 STRICTLY-COMPATIBLE, ★0⑂0, 8,283 KB, Python on-stack. **Traction caveat recorded plainly: ★0⑂0 is no traction evidence in either direction.** The pick is about the *shape*, not the project. |
| 3 | Practicability and confidence | ✓ | The upstream stack (FastAPI + SQLAlchemy + PostgreSQL + Docker) is on-stack; the upstream *domain* (household pantry) is not, so no code is adoptable. **The vocabulary is fully portable.** Evidence strength: **high** for the vocabulary match (the triad is named in the project's own one-line description), **low** for present urgency. |
| 4 | Conflict | ✓ | No invariant is violated — the triad **is** §3.3 + §3.5 + §3.6. **But adopting any of the feature's substance WOULD conflict:** vendor/purchase entities introduce a **third role** (§3.1 says two) and a cost-tracking domain LE31 v1 does not have. |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v1 defer outcome. Maximum time worth spending: **45 min documentation**. **Today: 0 build time.** |
| 6 | Cost to operational value | ✓ | The value is naming LE31's own invariants with external prior art. Roughly 45 min of documentation; no build, no training, no maintenance. |
| 7 | Circuit breaker + reversibility | ✓ | No code; no rollback needed. Revert by `git rm`. |

**Gate verdict: `defer` (parking-lot)** — check 1 fails on evidence class. The other six pass because the *vocabulary* is sound; what LE31 does not have is the pain.

## Bucket

**v1 (exact-money + append-only-facts vocabulary)** — Pick A of Daily Research 2026-10-24. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — today's confirmed workspace state is exactly 3 projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1); `le31 v2 owner-pains` and `le31 v2-AI` **do not exist**. Because the **parent research issue for this pass also failed to create**, the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload.

## Files to touch

**None today.** Documentation-only.

If the owner ever asks for supplier/cost visibility, the expected files are:

- `backend/app/models.py` — **new** `Vendor` and `Purchase` SQLModel classes. **⚠️ This is a §3.1 role expansion and needs an explicit owner decision before code.**
- `backend/app/models.py` — **any new money field must be `Decimal`**, never `float`. Per §3.6 and the conventions' *Money* rule.
- `backend/app/models.py` — `MenuItem` price fields: **read-only audit.** Confirm they are already `Decimal` and not `float`. **This is the load-bearing check of any future build** — the entire value of this pick is that the invariant is real, so it must be verified, not assumed.
- `backend/services/stock_service.py` — if the triad is quoted, the "no required outbound calls" rule should be enforced **structurally** (no outbound network call in the core order/stock path), not just documented.
- `docs/` or `ARCHITECTURE.md` — **the recommended change**: quote the upstream triad as external prior art next to §3.3/§3.5/§3.6.
- `tests/test_money_precision.py` — **the load-bearing test**: assert that a price summed over many items is exactly the expected `Decimal`, with no float drift. A test that fails if any price field is typed `float`.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. For this feature the observable behaviour is **the precision of a real bill**: add several items, serve them, and confirm the derived total is exactly the expected `Decimal` to the cent — in the running system, through the waiter UI, not only in a unit test. The "no required outbound calls" property is verified by **disabling network egress** and confirming the order and stock path still completes.

## Rollback path

`git rm features/370-*.md specs/jdmacleod-kitchen-erp-*-HANDOFF.md`. Documentation-only, no migration, no data. Fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *Money* and *Stock* rules first)
- `le31-data` — append-only ledger rules (`StockEntry`: never update or delete)
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for invariants (§3.3, §3.5, §3.6, §4.3)

## Open questions carried into any future build

1. **Should LE31's architecture notes quote the triad?** This feature's recommendation says yes, as external prior art. **Unmade owner decision.**
2. **Is "no required outbound calls" a rule LE31 wants stated explicitly?** Currently implicit in the single-VPS posture. Making it explicit changes what future features may propose.
3. **Does LE31 ever want supplier/purchase data?** §3.2 excludes online ordering and payment gateways; §3.1 names two roles. A supplier role has been unmade across 86 passes.
4. **Are LE31's current price fields actually `Decimal`?** Unverified in this pass — it is a cheap check and the whole value of this pick depends on it. **Do it before citing this feature as prior art.**
