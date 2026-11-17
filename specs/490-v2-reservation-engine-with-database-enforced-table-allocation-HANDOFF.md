# HANDOFF — Feature 490: v2 reservation engine with database-enforced table allocation

## Active feature path

`features/490-v2-reservation-engine-with-database-enforced-table-allocation.md`

**Disposition:** `defer` — v2 parking-lot architecture reference. **A coding agent must not implement this feature from this handoff.** The handoff records the mechanism and the trigger for a future, separately-gated reservations scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — reservations are outside LE31 v1's fixed two-surface scope |
| 2. Viability | PASS — database-enforced non-overlap is coherent |
| 3. Practicability / confidence | MEDIUM — Apache-2.0, ★2, pre-alpha, off-stack |
| 4. Conflict | SCOPE CONFLICT for v1; belongs to v2 |
| 5. Outcome, appetite, scope | DEFER to v2 |
| 6. Cost to operational value | HIGH today; architecture decision value later |
| 7. Circuit breaker / reversibility | PASS — documentation only |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future reservation feature is separately approved, likely touch points are:

- `backend/app/models.py` — future reservation and allocation models;
- `backend/app/services/reservations.py` — future allocation service;
- `backend/app/routers/reservations.py` — future reservation route;
- migrations/constraints — future PostgreSQL exclusion constraint plus the cross-database strategy;
- tests — concurrent allocation, duplicate write, seat-without-table refusal, erasure.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/490-v2-reservation-engine-with-database-enforced-table-allocation.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-17/readme/09_David-Cabeza_OpenCovers.md` and repository metadata at `/tmp/le31-daily-2026-11-17/repos/09_David-Cabeza_OpenCovers.json`.
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-17.md` records the pick as `DEFER` and the project attachment as `le31 Research`.

For a future implementation, required verification includes a concurrent allocation test proving the database rejects overlap, a replay test proving idempotency, and a refusal test proving a reservation cannot be seated without a table.

## Rollback path

- Delete `features/490-v2-reservation-engine-with-database-enforced-table-allocation.md`.
- Delete `specs/490-v2-reservation-engine-with-database-enforced-table-allocation-HANDOFF.md`.
- Remove the feature-490 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter surface and scope invariants;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, even for a v2 reference;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when the owner explicitly requests reservations, waitlist, or host workflows and a new v2 feature is separately scoped and gated. No v2 project currently exists; the Linear sub-issue is therefore attached to `le31 Research`.
