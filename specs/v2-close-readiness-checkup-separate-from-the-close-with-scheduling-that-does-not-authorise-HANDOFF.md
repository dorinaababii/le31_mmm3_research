# HANDOFF — Feature 505: v2 close-readiness checkup separate from the close, with scheduling that does not authorise

## Active feature path

`features/505-v2-close-readiness-checkup-separate-from-the-close-with-scheduling-that-does-not-authorise.md`

**Disposition:** `defer` — v2 parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the mechanism, the boundary with feature 426 and with feature 500, and the trigger for a future, separately-gated period-close scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no LE31 operator has asked for a period close; the JTBD is inferred from the source's own operator-facing language (*"what needs attention before close"*, *"final close requires explicit authorization"*) |
| 2. Viability | PASS in principle — the mechanism is stated in four README lines plus a workflow tree and the source is Apache-2.0 |
| 3. Practicability / confidence | MEDIUM-HIGH — the source is **Python**, and its posture *"the agent workflows call the `books` CLI and don't compute financial totals themselves"* is exactly LE31's §3.4 deterministic-tool-plus-human-gate shape. But LE31 v1 has no accounting period and no bookkeeper, so the surface has no current host; the checkup's rule set, its presentation, the authorisation form and the checkup-to-close relationship are all unspecified by the source |
| 4. Conflict | No hard conflict — a **§3.1 reinforcement**. *"Scheduling does not authorize a close, publication, or money movement"* is the charter's explicit-state-transition rule applied to a *period* rather than to an order |
| 5. Outcome, appetite, scope | DEFER — this is the **second consecutive defer on the reconciliation theme** (yesterday's feature 500 established the cross-ledger register; today establishes the gate in front of it). A third contract on the same theme would refine a vocabulary with no caller |
| 6. Cost to operational value | LOW today (one document), MEDIUM if adopted (checkup rule engine + authorisation model + close gate + export gate) with no v1 caller |
| 7. Circuit breaker / reversibility | PASS — documentation only, fully reversible, no code authorised |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future period-close feature is separately approved, likely touch points are:

- `backend/app/models.py` — future `ReadinessCheckup` and `CloseAuthorisation` models;
- `backend/app/services/readiness.py` — future rule evaluation producing the items-needing-attention list;
- `backend/app/services/close.py` — future close gate: refuse a close without a prior authorisation;
- `backend/app/routers/periods.py` — future checkup and close routes;
- the waiter/owner UI — future "what needs attention before close" surface;
- tests — a scheduled preparation cannot authorise; a close without authorisation is refused; a checkup can be run repeatedly; an export without a saved reconciliation is refused.

**Ordering constraints (not optional):**
1. Feature 500 (`v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface`) must land first — the readiness gate checks what the register produces, and a gate with nothing to check is not a gate.
2. Feature 496 (`audit-ready-daily-export-with-financial-reconciliation-identities`) must land first — its export is the artefact the gate protects.
3. Feature 426 (`le31-shift-close-lifecycle`) is a **peer, not a prerequisite**: a shift close is a different granularity from a period close.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/505-v2-close-readiness-checkup-separate-from-the-close-with-scheduling-that-does-not-authorise.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-20/gh/readme_plain/plain_41_giltotherescue_slashbooks.md` and the repository metadata at `/tmp/le31-daily-2026-11-20/gh/repo_41_giltotherescue_slashbooks.json` (Apache-2.0, ★40, ⑂6, pushed 2026-11-20T03:08:39Z).
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-20.md` records the pick as `DEFER` and the project attachment as `le31 Research`.
4. Confirm the dedup result by re-running the corpus sweep: `grep -rilE 'close readiness|books.?checkup|schedul\w*.{0,60}authoriz' features/ specs/` → **0 files**.
5. Confirm the source's load-bearing sentence verbatim: `grep -F 'Scheduling does not authorize a close, publication, or money movement.' /tmp/le31-daily-2026-11-20/gh/readme_plain/plain_41_giltotherescue_slashbooks.md` → **1 line**.

For a future implementation, required verification includes a test proving **a scheduled or automated preparation cannot produce a close authorisation**, a test proving **a close without authorisation is refused**, a test proving **a checkup can be run repeatedly and produces a list rather than a transition**, and a test proving **an export without a saved reconciliation is refused**. The repository currently has **no test harness, no `pyproject.toml`, no `pytest`/`conftest.py` and no test directory** — the implementer must establish the harness as part of the slice, and must not assume one exists.

## Rollback path

- Delete `features/505-v2-close-readiness-checkup-separate-from-the-close-with-scheduling-that-does-not-authorise.md`.
- Delete `specs/v2-close-readiness-checkup-separate-from-the-close-with-scheduling-that-does-not-authorise-HANDOFF.md`.
- Remove the feature-505 row from `/opt/data/INDEX.md` and from the repository `INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.1/§3.2/§3.3 scope rules, the truth invariant, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, slicing rules, and the *Definition of Done*;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when **all** of the following hold:

1. feature 500 and feature 496 have both landed, so there is a register to check and an export to protect;
2. the corpus question *"does LE31 ever have a period to close?"* has an owner answer — if the answer is "never", **delete this feature rather than promoting it**;
3. the checkup's rule set, the authorisation's form, the checkup-to-close relationship and the definition of a "period" (business day in `Europe/Paris`? week? month? fiscal quarter?) have owner answers, because the source specifies none of them;
4. a new feature is separately scoped and gated under a project that exists at that time — the workspace currently has only `le31 v1 — Core MVP`, `le31 Workflow` and `le31 Research`, and **no v2 project**.
