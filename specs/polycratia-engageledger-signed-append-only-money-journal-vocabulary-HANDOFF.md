# HANDOFF — `polycratia-engageledger-signed-append-only-money-journal-vocabulary`

> **Build verdict: `defer`.** This slice contract exists because `le31-feature-pipeline` requires one per pick. **The coding agent should not start work.** Two of this pick's four primitives already exist in LE31; the third has no surface to attach to.

## Active feature path

`features/357-polycratia-engageledger-signed-append-only-money-journal-vocabulary.md`

External source: `https://github.com/polycratia/engageledger` (MIT, Go OFF-STACK, ★1/⑂0, **9 KB — smallest pick of the 84-pass series**, created 2026-10-19, pushed 2026-10-21, **zero topics**). All fields parent-verified 2026-10-22 from `GET /repos/...`.

## Seven-check gate verdict

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | **FAIL** — job is B2B contracting; LE31 has no counterparty, no contract, no invoice |
| 2 | Viability | pass — nothing to operate |
| 3 | Practicability & confidence | pass — Go off-stack, logic portable in principle, but nothing needs porting |
| 4 | Conflict | **no hard conflict** |
| 5 | Outcome / appetite / scope | **partial fail** — 2 of 4 primitives duplicate feature 54 + feature 49 |
| 6 | Cost to operational value | near-zero; overlaps existing work |
| 7 | Circuit breaker / reversibility | fully reversible; 9 KB |

**Decision: `defer`.** Evidence class **observed**, confidence **high** on the shape / **low** on LE31 relevance.

**Overlap declaration — read before considering a build:** the *invoices-derived-from-journal* and *signed-append-only-single-source* primitives are already covered by `features/54-corner-mart-pos-double-entry` and `features/49-postledger-tamper-evident-hash`. This pick contributes **one** new idea against two already-filed ones.

## The one new idea

*"Acceptance is a business-day clock stopped only by a rejection that names a criterion."*

A rejection that does not name a criterion is indistinguishable from a stall. LE31 persists timezone-aware instants and renders business dates in `Europe/Paris` (§3.7); what it lacks is any clock that can be **halted** by a reason-coded event.

## Files to touch

**None.** Vocabulary artifact; no LE31 source file is modified.

If the trigger ever fires, the realistic first change is a **mandatory reason code on a Telegram state transition**, not a data-model change. Recorded so the constraint is not rediscovered later.

## Verification protocol reference

None required — nothing is built. If a future build proposes the reason-code rule, the mandatory test is: *no code path can halt a business-day clock without a non-null `rejection_criterion`.* A test that permits a bare reject **must not** be written to make the check pass.

## Rollback path

Delete `features/357-…md` and this file. No runtime footprint, no data, no migration.

## Trigger condition (all must hold)

1. LE31 grows a business-day SLA that can be halted — realistic candidates: a supplier delivery window, an order-quote validity period.
2. Feature 54's double-entry work has defined how a rejection reason is represented.

**Note the cost against §3.5:** a mandatory reason code adds friction to the cook's hands-busy Telegram surface. That is a real cost and must be weighed, not waved away — §3.4 wants *more* explicitness, §3.5 wants *less* friction, and this pick sits exactly where they pull against each other.

## Mandatory LE31 skill list

- `le31-conventions` — the seven-check gate; §3.4 explicitness vs §3.5 friction tension.
- `le31-daily-research` — provenance.
- `le31-feature-pipeline` — why this contract exists despite `defer`.
- `le31-v1-feature-pattern` — the feature-file template shape.
- `features/54-corner-mart-pos-double-entry` — **must be read** before any build, to avoid re-implementing what exists.

## Status

- **Linear sub-issue:** NOT created. Write endpoint blocked, **34th consecutive day** (HTTP 400 `invalid_request`, free-issue-limit, requestId `a4e675dd19dbdc59`). Intended attachment: `le31 Research` (P-HMM-1), label `Feature`.
- **Fallback payload:** `/opt/data/le31-daily-research-2026-10-22.linear-fallback.json`.
- **Report:** `/opt/data/le31-daily-research-2026-10-22.md`.
- **Bucket:** v2 (vocabulary only). `le31 v2 owner-pains` does not exist — attached to `le31 Research` per SKILL.md line 33.