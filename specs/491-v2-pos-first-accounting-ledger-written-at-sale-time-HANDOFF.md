# HANDOFF — Feature 491: v2 POS-first accounting ledger written at sale time

## Active feature path

`features/491-v2-pos-first-accounting-ledger-written-at-sale-time.md`

**Disposition:** `defer` — v2 product-pattern reference. **A coding agent must not implement this feature from this handoff.** The source repository is source-available with `NOASSERTION` license metadata and a private backend; no code or dependency may be adopted.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — owner accounting is not an observed LE31 need |
| 2. Viability | PASS in principle — posting at sale time is coherent |
| 3. Practicability / confidence | LOW-MEDIUM — product pattern, not reusable code |
| 4. Conflict | No charter conflict, but a second money ledger must remain distinct from `StockEntry` |
| 5. Outcome, appetite, scope | DEFER to v2 |
| 6. Cost to operational value | HIGH today; architecture-decision value later |
| 7. Circuit breaker / reversibility | PASS — documentation only |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future owner-accounting feature is separately approved, likely touch points are:

- `backend/app/models.py` — future chart-of-accounts and journal models;
- `backend/app/services/accounting.py` — future posting service and idempotency;
- `backend/app/services/outbox.py` — future atomic posting outbox, if that route is chosen;
- `backend/app/routers/accounting.py` — future reporting/export routes;
- tests — sale-to-journal mapping, refund/waste mapping, replay idempotency, month-end-as-reporting.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/491-v2-pos-first-accounting-ledger-written-at-sale-time.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-17/readme/06_yegobox_flipper.md` and repository metadata at `/tmp/le31-daily-2026-11-17/repos/06_yegobox_flipper.json`.
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-17.md` records the pick as `DEFER` and explicitly labels the source as a pattern reference with no license-derived reuse.

For a future implementation, required verification includes: every sale creates exactly one journal effect; replay creates no duplicate; refunds and waste map to explicit financial entries; no accounting query is used to derive stock; month-end produces a report without an import step.

## Rollback path

- Delete `features/491-v2-pos-first-accounting-ledger-written-at-sale-time.md`.
- Delete `specs/491-v2-pos-first-accounting-ledger-written-at-sale-time-HANDOFF.md`.
- Remove the feature-491 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — money invariants and charter boundaries;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, even for a v2 reference;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when the owner explicitly asks for owner accounting, P&L, or accountant-facing reporting and a new v2 feature is separately scoped and gated. If an external accounting system becomes the destination, a human-review-before-submission gate must be part of that scope.
