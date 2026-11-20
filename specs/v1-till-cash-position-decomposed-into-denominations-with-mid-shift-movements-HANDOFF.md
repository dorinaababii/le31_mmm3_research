# HANDOFF — Feature 504: v1 till cash position decomposed into denominations with mid-shift movements

## Active feature path

`features/504-v1-till-cash-position-decomposed-into-denominations-with-mid-shift-movements.md`

**Disposition:** `defer` — v1 parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the mechanism, the boundary with features 391 and 426, and the trigger for a future, separately-gated cash-management scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no LE31 operator has asked for denomination counting; the JTBD is inferred from the source's own operator-facing language (*"opening balance with cash denomination breakdown"*, *"cash deposits… mid-shift"*, *"cash expenses"*) |
| 2. Viability | PASS in principle — the mechanism is stated in four README lines and the source is MIT; a single operator can count a note stack |
| 3. Practicability / confidence | MEDIUM — the source is TypeScript/Vue on Frappe+ERPNext (off-stack for LE31's Python 3.13 / FastAPI / SQLModel / Postgres / aiogram v3); the README does not specify the denomination set, the closing-count entry surface, the deposit's semantics or the expense's allocation, so this records a **shape**, not a copyable design |
| 4. Conflict | No hard conflict — it extends features 391 and 426 rather than contradicting them. It does impose §3.1's append-only discipline on till movements (a movement is a new record, never an edit to a balance), which is a constraint, not a blocker |
| 5. Outcome, appetite, scope | DEFER — features 391 (shift variance) and 426 (shift close) were filed 2026-11-15/2026-11-16 and are still parked; a third shift-family contract before either of its two predecessors moves is scope accumulation without appetite |
| 6. Cost to operational value | LOW today (one document), MEDIUM if adopted (denomination model + movement ledger + close-position derivation + count-entry surface) with **no v1 caller until 391/426 land** |
| 7. Circuit breaker / reversibility | PASS — documentation only, fully reversible, no code authorised |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future cash-management feature is separately approved, likely touch points are:

- `backend/app/models.py` — future `CashPosition` and `CashMovement` models;
- `backend/app/services/cash.py` — future derivation of the expected close position from the declared position plus the movements;
- `backend/app/routers/shifts.py` — future shift-open declaration and movement-recording routes;
- the waiter web UI — future shift-open denomination entry and cash-movement capture;
- tests — declared position is never edited; a movement never updates a balance; close reconciles against the adjusted position; a duplicate movement is rejected.

**Ordering constraints (not optional):**
1. Feature 391 (`le31-shift-variance-stored-no-derivation-no-payment-table`) must land first — a denomination breakdown is what makes that variance actionable.
2. Feature 426 (`le31-shift-close-lifecycle`) must land first — the movements recorded here change what the close reconciles against.
3. Feature 504 must not be promoted to `build` while both predecessors are parked.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/504-v1-till-cash-position-decomposed-into-denominations-with-mid-shift-movements.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-20/gh/readme_plain/plain_36_kodlyft_xpos.md` (the README decoded from the base64 GitHub payload) and the repository metadata at `/tmp/le31-daily-2026-11-20/gh/repo_36_kodlyft_xpos.json` (MIT, ★55, ⑂47, pushed 2026-11-19T15:55:22Z).
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-20.md` records the pick as `DEFER` and the project attachment as `le31 Research`.
4. Confirm the dedup result by re-running the corpus sweep: `grep -rilE 'denomination|cash deposit|bank drop|till expense' features/ specs/` → **0 files** for the till-cash family.

For a future implementation, required verification includes a test proving **the declared opening position is never edited**, a test proving **a movement never updates a running balance** (it appends), a test proving **the close reconciles against the adjusted position** (declared + movements), and a test proving **a duplicate movement is rejected**. The repository currently has **no test harness, no `pyproject.toml`, no `pytest`/`conftest.py` and no test directory** — the implementer must establish the harness as part of the slice, and must not assume one exists.

## Rollback path

- Delete `features/504-v1-till-cash-position-decomposed-into-denominations-with-mid-shift-movements.md`.
- Delete `specs/v1-till-cash-position-decomposed-into-denominations-with-mid-shift-movements-HANDOFF.md`.
- Remove the feature-504 row from `/opt/data/INDEX.md` and from the repository `INDEX.md`.
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

1. feature 391 (`le31-shift-variance-stored-no-derivation-no-payment-table`) **and** feature 426 (`le31-shift-close-lifecycle`) have both landed;
2. a LE31 operator has stated a real need for **explaining a cash discrepancy** — the corpus question *"does a single-operator restaurant need denominations at all?"* must have an owner answer, and if the answer is "no", **delete this feature rather than promoting it**;
3. the denomination set, the closing-count entry surface, the deposit's semantics and the expense's allocation have owner answers, because the source specifies none of them;
4. a new feature is separately scoped and gated under a project that exists at that time — the workspace currently has only `le31 v1 — Core MVP`, `le31 Workflow` and `le31 Research`, and **no v2 project**.
