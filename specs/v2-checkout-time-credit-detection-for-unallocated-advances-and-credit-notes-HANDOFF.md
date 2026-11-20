# HANDOFF — Feature 506: v2 checkout-time credit detection for unallocated advances and credit notes

## Active feature path

`features/506-v2-checkout-time-credit-detection-for-unallocated-advances-and-credit-notes.md`

**Disposition:** `defer` — v2 parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the mechanism, the **charter §3.2 privacy tension** that blocks it, the boundary with feature 435, and the trigger for a future, separately-gated customer-credit scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no LE31 operator has asked for a customer-credit surface; the JTBD is inferred from the source's own operator-facing language (*"auto-detect unallocated advances and credit notes at checkout"*) |
| 2. Viability | PASS in principle — the mechanism is stated in four README lines and the source is MIT |
| 3. Practicability / confidence | LOW — the source is TypeScript/Vue on Frappe+ERPNext (off-stack), and the mechanism requires a **customer identity** and an **advance/credit-note store**, neither of which exists in LE31 v1. It also inherits the source's customer-management surface (addresses, loyalty, credit limits), most of which is far outside LE31's scope. The transferable part is narrow: *detect unallocated money at the till before the bill is taken* |
| 4. Conflict | **TENSION with charter §3.2 privacy** — *"store only data needed for restaurant operations; v1 guest demographics are counts, not identity or contact data"*, plus §3.2's out-of-scope line on customer accounts. A customer-credit mechanism needs a customer identity to attach the advance to. The tension is resolvable by keeping the advance anonymous and till-scoped, but that resolution is a **product decision the charter has not made**. **This feature explicitly does not resolve it** |
| 5. Outcome, appetite, scope | DEFER — no observed LE31 demand, no host surface, and an unresolved §3.2 tension |
| 6. Cost to operational value | LOW today (one document), HIGH if adopted (customer/advance/credit-note stores + a matching rule + a detection surface) for a single-table restaurant with no accounts |
| 7. Circuit breaker / reversibility | PASS — documentation only, fully reversible, no code authorised |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future customer-credit feature is separately approved, likely touch points are:

- `backend/app/models.py` — future `UnallocatedMoney` and draft-invoice models;
- `backend/app/services/credits.py` — future detection and the **explicit** application path;
- `backend/app/routers/checkout.py` — future checkout surface returning detected candidates;
- the waiter web UI — future "unallocated money available" affordance at the bill;
- tests — detection surfaces candidates without applying them; an application requires an explicit action; a credit note is always linked to a cause; an over-payment is handled per a recorded rule.

**Ordering constraints (not optional):**
1. **Charter §3.2's privacy boundary must be answered for customer identity first.** This is the blocker — without it there is nothing to attach an advance to.
2. Feature 435 (`le31-bill-records-no-which-lines-it-charged`) must land first — the detector's output is applied *to* a bill.
3. Feature 504 (feature 504's till-cash family) is a **peer, not a prerequisite**: operator cash and customer credit are different concerns and are deliberately not bundled.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/506-v2-checkout-time-credit-detection-for-unallocated-advances-and-credit-notes.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-20/gh/readme_plain/plain_36_kodlyft_xpos.md` (the README decoded from the base64 GitHub payload) and the repository metadata at `/tmp/le31-daily-2026-11-20/gh/repo_36_kodlyft_xpos.json` (MIT, ★55, ⑂47, pushed 2026-11-19T15:55:22Z).
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-20.md` records the pick as `DEFER` and the project attachment as `le31 Research`.
4. Confirm the dedup result by re-running the corpus sweep: `grep -rilE 'unallocated advance|draft invoice' features/ specs/` → **0 files**.
5. Confirm the source's mechanism lines verbatim: `grep -F 'Auto-detect unallocated advances and credit notes at checkout' /tmp/le31-daily-2026-11-20/gh/readme_plain/plain_36_kodlyft_xpos.md` → **1 line**.
6. Confirm the charter tension is still open in `PROJECT_CHARTER.md` §3.2 — this pick must not be read as having answered it.

For a future implementation, required verification includes a test proving **the detector surfaces candidates without applying them**, a test proving **applying a candidate requires an explicit user action**, a test proving **a credit note is always linked to a cause document**, and a test proving **an unallocated amount is never silently inferred into a bill**. The repository currently has **no test harness, no `pyproject.toml`, no `pytest`/`conftest.py` and no test directory** — the implementer must establish the harness as part of the slice, and must not assume one exists.

## Rollback path

- Delete `features/506-v2-checkout-time-credit-detection-for-unallocated-advances-and-credit-notes.md`.
- Delete `specs/v2-checkout-time-credit-detection-for-unallocated-advances-and-credit-notes-HANDOFF.md`.
- Remove the feature-506 row from `/opt/data/INDEX.md` and from the repository `INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.1/§3.2/§3.3 scope rules, the truth invariant, the privacy boundary, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, slicing rules, and the *Definition of Done*;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when **all** of the following hold:

1. **the charter has answered §3.2's customer-data question** — whether LE31 may hold a customer identity, and whether an advance is a customer concept or a per-visit concept. If the answer is "never", **delete this feature rather than promoting it**;
2. feature 435 (`le31-bill-records-no-which-lines-it-charged`) has landed, so the detector has a bill to apply to;
3. the matching rule, the partial-allocation case, the expiry rule and the customer-identity model have owner answers, because the source specifies none of them;
4. a new feature is separately scoped and gated under a project that exists at that time — the workspace currently has only `le31 v1 — Core MVP`, `le31 Workflow` and `le31 Research`, and **no v2 project**.
