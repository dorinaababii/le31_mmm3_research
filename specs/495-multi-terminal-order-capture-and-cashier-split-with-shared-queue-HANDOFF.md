# HANDOFF — Feature 495: v1 multi-terminal order capture and cashier split with shared queue

## Active feature path

`features/495-multi-terminal-order-capture-and-cashier-split-with-shared-queue.md`

**Disposition:** `defer` — v1 parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the mechanism and the trigger for a future, separately-gated multi-surface floor scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no operator has asked for a second counter terminal |
| 2. Viability | PASS in principle — the mechanism is well-specified and MIT-licensed |
| 3. Practicability / confidence | MEDIUM — FloCafe is TypeScript/Electron (off-stack); the README is a design statement, not LE31-stack validation |
| 4. Conflict | No hard conflict, but features 474 and 476 must be closed before a second writer exists |
| 5. Outcome, appetite, scope | DEFER — LE31 v1 has a single-counter surface by design |
| 6. Cost to operational value | LOW today, HIGH if adopted — a second surface model plus a queue authority |
| 7. Circuit breaker / reversibility | PASS — documentation only |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future multi-surface floor feature is separately approved, likely touch points are:

- `backend/app/models.py` — future counter-terminal, shared-queue, and ticket models;
- `backend/app/services/queue.py` — future queue authority and claim protocol;
- `backend/app/routers/queue.py` — future queue and ticket-lookup routes;
- `backend/app/services/orders.py` — the **visit ownership** change (feature 474) and the **line-phase** change (feature 476) are prerequisites, not peers;
- tests — two-terminal claim, orphaned claim on terminal death, served-line visibility across terminals, bill-number allocation under concurrency (feature 448).

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/495-multi-terminal-order-capture-and-cashier-split-with-shared-queue.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-18/gh/readme_07_FreeOpenSourcePOS_FloCafe.md` and repository metadata at `/tmp/le31-daily-2026-11-18/gh/repo_07_FreeOpenSourcePOS_FloCafe.json`.
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-18.md` records the pick as `DEFER` and the project attachment as `le31 Research`.

For a future implementation, required verification includes a two-terminal test proving the capture and payment actions stay **separate explicit actions** (no implicit close), an orphaned-claim test proving the queue fails closed when a claiming terminal dies mid-order, and a cross-terminal served-line test proving the kitchen is notified of a quantity change (feature 476).

## Rollback path

- Delete `features/495-multi-terminal-order-capture-and-cashier-split-with-shared-queue.md`.
- Delete `specs/495-multi-terminal-order-capture-and-cashier-split-with-shared-queue-HANDOFF.md`.
- Remove the feature-495 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.1 two-surface invariant, the truth invariant, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, slicing rules, and the *Definition of Done*;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when the owner explicitly requests a second counter terminal or a split capture/payment counter, **and** features 474 (per-table visit ownership) and 476 (order-line quantity phase) are closed, **and** a new feature is separately scoped and gated. A second terminal exceeds the charter's two-surface count and therefore needs an explicit owner decision on the charter itself.
