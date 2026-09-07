# 2026-09-07 — `reliability-lives-in-institution-not-cognition-2609-03192v1` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/147-reliability-lives-in-institution-not-cognition-2609-03192v1.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains (architecture-reference)**. Build verdict: **`defer`** (charter §3.2 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 surface changes the `audit_logs` discipline (e.g. feature 121 field-tier minimization, feature 68 demand-estimation, feature 138 institutional-continuity model), the owner/waiter/cook wants *to verify the operational invariants still hold*, but struggles because *the current verification is test-only (per §3.4)*, so that *the v2 change is verifiably non-breaking*." **PASS** (no LE31 pain observed today; the v2 surface that would *use* this test doesn't exist yet — the JTBD is forward-looking). |
| 2 | **Viability** | Owner can read the paper? Yes (arXiv public access, 31 pages, 5 figures, ancillary files). LE31 v1 has no AI surface to test today. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public arXiv access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the experimental design (preregistered refutations, dual interventions, falsifier); medium-high for the *transferability* to LE31 (the paper tests an agent in a simulated settlement, not a restaurant waiter; the *property names* map but the *property content* is the LE31 invariant). **PASS**. |
| 4 | **Conflict** | None. The paper's "accepted reality stayed singular" property *is* the LE31 §3.1 *current stock is derived from entries* invariant; the paper's "invalid attempts were refused with typed reasons" property *is* the LE31 §3.1 *operational transitions are explicit user actions* invariant; the paper's "duties outlived their processes" property *is* the LE31 §3.1 *audit-trail over operational events* invariant; the paper's "no work was accepted twice" property *is* the LE31 §3.1 *Order.id uniqueness + Bill derivation* invariant; the paper's "no false completion was ever accepted (2,581 substituted-panel claims, none false)" property *is* the LE31 §3.1 *explicit-close requirement* invariant. **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 architecture-reference; **zero build time today**. Maximum time worth spending: 2 hours (read paper + write cross-section document). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Read 1 paper (1 hour). Document cross-section (1 hour). Total: 2 hours. **Cost-to-value ratio: high** (single-document with 5 invariants that map 1:1 onto LE31's existing operational invariants). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-07-reliability-lives-in-institution-not-cognition-2609-03192v1-HANDOFF.md` and `features/147-reliability-lives-in-institution-not-cognition-2609-03192v1.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 surface that proposes a change to the `audit_logs` discipline).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a new `audit_logs` event type, a new `StockEntry` source, or a new operational transition):

- `models/audit_log.py` — possibly add a new event type or constraint (depends on the v2 surface).
- `models/stock_entry.py` — possibly add a new `StockEntry` source (depends on the v2 surface).
- `app/api/orders.py` — possibly add a new operational transition (depends on the v2 surface).
- `app/audit/verify.py` — **NEW** (if a verification harness is built; **not v1**). Would contain the verification protocol from §2 of the HANDOFF (hold operational cognition fixed, intervene on the institutional layer, verify the five properties do not move).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/147-reliability-lives-in-institution-not-cognition-2609-03192v1.md` exists and is read back by the parent.
- [ ] `specs/2026-09-07-reliability-lives-in-institution-not-cognition-2609-03192v1-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The five pre-declared properties are quoted verbatim from the paper.
- [ ] The 1:1 mapping onto LE31 charter §3.1 invariants is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that changes the audit discipline lands):**
- [ ] The PR is read back by the parent.
- [ ] The five pre-declared properties are evaluated against the PR's changes.
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the verification harness; remove the new event type / source / transition.
- Migration cost: depends on the v2 surface; the paper's intervention protocol suggests *retrospective* (post-hoc) audit verification, which is *no migration* (the existing `audit_logs` is the audit trail).
- Retained data: the `audit_logs` table retains all rows (charter §3.1: never update or delete ledger events); the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.

## 7. Handoff summary

| Field | Value |
|---|---|
| Feature ID | 147 |
| Slug | `reliability-lives-in-institution-not-cognition-2609-03192v1` |
| Bucket | v2 owner-pains (architecture-reference) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `models/audit_log.py` (possibly) + `models/stock_entry.py` (possibly) + `app/api/orders.py` (possibly) + `app/audit/verify.py` (NEW, not v1) |
| Trigger condition | First v2 PR that adds a new `audit_logs` event type, a new `StockEntry` source, or a new operational transition |
| Verification protocol | Hold operational cognition fixed; intervene on the institutional layer; verify the five pre-declared properties do not move |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-204 (Research 2026-09-07 — daily) |
| Linear sub-issue | HMM-205 (to be created) |
| Lead source | arXiv 2609.03192v1 (Marsden, Collecutt, Marsden, 2026-09-02) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that changes the audit discipline lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the five pre-declared properties are the right invariant checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that changes the audit discipline will append a row here with: PR number, the five pre-declared properties evaluated, the evaluation result, and the operator's sign-off.)*
