# HANDOFF — Feature 489: v1 idempotent receiving and derived stock-movement ledger

## Active feature path

`features/489-v1-idempotent-receiving-and-derived-stock-movement-ledger.md`

**Disposition:** `defer` — parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff preserves the mechanism and the trigger so a future, separately-gated receiving scope does not have to re-derive it.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no LE31 operator request for supplier receiving |
| 2. Viability | PASS in principle |
| 3. Practicability / confidence | MEDIUM — MIT, ★1, off-stack reference |
| 4. Conflict | No hard charter conflict; out of current v1 surface scope |
| 5. Outcome, appetite, scope | DEFER — vocabulary only |
| 6. Cost to operational value | LOW now; HIGH only when receiving is scoped |
| 7. Circuit breaker / reversibility | PASS — documentation only |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If and only if a future receiving feature is separately approved, likely touch points are:

- `backend/app/models.py` — future receipt/movement models, if a receipt table is approved;
- `backend/app/services/` — future receipt application and idempotency helper;
- `backend/app/routers/` — future receiving route;
- tests — duplicate receipt, partial receipt, unauthorized adjustment.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/489-v1-idempotent-receiving-and-derived-stock-movement-ledger.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-17/readme/08_ShahabAhmed01_apexPOS.md` and repository metadata at `/tmp/le31-daily-2026-11-17/repos/08_ShahabAhmed01_apexPOS.json`.
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-17.md` records the pick as `DEFER`.

For a future implementation, the required regression cases are: duplicate receipt applied twice produces one set of movement rows; on-hand is derived from movements; waste/adjustment without manager authorization is rejected; corrections are new events rather than edits.

## Rollback path

- Delete `features/489-v1-idempotent-receiving-and-derived-stock-movement-ledger.md`.
- Delete `specs/489-v1-idempotent-receiving-and-derived-stock-movement-ledger-HANDOFF.md`.
- Remove the feature-489 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — stock/money invariants and the seven-check gate;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — existing v1 contract conventions;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when the owner explicitly asks for supplier receiving or purchase orders, and a new feature is separately gated for that scope. At that point, re-run the seven checks against the concrete request and replace this defer contract rather than implementing it as written.
