# HANDOFF — Feature 496: v1 audit-ready daily export with financial reconciliation identities

## Active feature path

`features/496-audit-ready-daily-export-with-financial-reconciliation-identities.md`

**Disposition:** `defer` — v1 parking-lot owner-reporting vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the mechanism, the candidate identity list, and the trigger for a future, separately-gated owner-reporting scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no operator has asked for a daily report or an owner surface |
| 2. Viability | PASS in principle — a reconciliation identity is a small, well-understood artifact |
| 3. Practicability / confidence | MEDIUM — the source does not state which identities it checks, so the rule set is LE31's own decision, not a copy |
| 4. Conflict | No hard conflict — aligns with charter §3.6 exact EUR and no floats; would *surface* features 411/420/457 rather than create them |
| 5. Outcome, appetite, scope | DEFER — the owner-reporting surface is not among LE31 v1's two operational surfaces |
| 6. Cost to operational value | LOW today, MEDIUM later — the vocabulary is cheap; a real export surface is a separate slice |
| 7. Circuit breaker / reversibility | PASS — documentation only |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future owner-reporting feature is separately approved, likely touch points are:

- `backend/app/models.py` — future identity-definition and identity-run models;
- `backend/app/services/reconciliation.py` — future identity evaluation and run recording;
- `backend/app/routers/reports.py` — future export route;
- `backend/app/services/bills.py` — the **bill-line membership** change (feature 435) is a hard prerequisite: several candidate identities are not computable without it;
- `backend/app/config.py` — the tax-rate home (feature 408) and the money-rule reconciliation (feature 410) must land first, because an identity crossing a tax boundary cannot be published while they are open;
- tests — identity evaluation, failing-identity visibility, exactness under `Decimal`, service-day boundary at daypart rollover.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/496-audit-ready-daily-export-with-financial-reconciliation-identities.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-18/gh/readme_07_FreeOpenSourcePOS_FloCafe.md` and repository metadata at `/tmp/le31-daily-2026-11-18/gh/repo_07_FreeOpenSourcePOS_FloCafe.json`.
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-18.md` records the pick as `DEFER` and the project attachment as `le31 Research`.

For a future implementation, required verification includes an exactness test proving an identity holds under `Decimal` with no float anywhere in the path, a **failing-identity test proving the failure is visible in the exported artifact itself** (a failure that appears only in a log is not audit-ready), and a proof that the export is a read model that cannot mutate `Bill`, `Payment`, or `StockEntry`.

## Rollback path

- Delete `features/496-audit-ready-daily-export-with-financial-reconciliation-identities.md`.
- Delete `specs/496-audit-ready-daily-export-with-financial-reconciliation-identities-HANDOFF.md`.
- Remove the feature-496 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.6 (Decimal, never float; exact EUR; explicit tax/tip derivations), the truth invariant, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions and the *Definition of Done*;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when the owner explicitly requests a daily or per-shift report, **and** feature 435 (bill-line membership) is closed so the candidate identities are computable, **and** features 408 and 410 are resolved so an identity can name a tax rate without picking a side, **and** a new feature is separately scoped and gated. An owner-facing report is a third surface and needs an explicit owner decision on the charter's surface count.
