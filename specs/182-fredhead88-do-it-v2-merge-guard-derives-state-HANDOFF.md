# 182 — fredhead88-do-it-v2-merge-guard-derives-state HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 second-stakeholder surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/182-fredhead88-do-it-v2-merge-guard-derives-state.md` (defer artifact; **no code today**).

Bucket: **v2 architecture-reference (merge-guard-as-derivation-mechanism + event-time-vs-chain-time discipline; charter §3.1 territory; second-stakeholder introduction primitive)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 surface introduces a second stakeholder (accountant, tax authority, regulator), the owner wants *a primitive that lets the stakeholder verify 'when was this row committed?' without trusting the LE31 codebase*, but struggles because *LE31 v1's audit_logs uses writer-asserted timestamps*, so that *the v2 surface can answer provenance questions with a defensible answer*." **PASS** (zero-pain today; v1 has no second stakeholder; the JTBD is primitive documentation, not a build-need). |
| 2 | **Viability** | Owner can read the description (1-line)? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (predecessor is MIT Python; do-it-v2 is no-license — adoption requires relicense or treat as vocabulary-only). Confidence high for the primitive match (description + 2 sub-primitives align with event-time vs chain-time + merge-guard mechanism); low for transferability (LE31 v1 has no second-stakeholder surface). §3.4 conflict: **the primitives are not customer-facing AI; the Claude-Code integration pattern in the predecessor is staff-tooling territory** — §3.4 not triggered. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The do-it-v2 *merge-guard-as-derivation-mechanism + event-time-vs-chain-time* primitives *are* a v2 question, not a v1 question; they do not violate §3.1 (append-only posture is preserved — the optional `chain_position` column is semantic alias for the existing BIGSERIAL `id`). §3.4 conflict is contingent on whether the v2 surface is staff-tooling or customer-facing (none currently planned); the *primitives themselves* are not AI. **PASS** (charter §3.1 invariant-compatible for v1; §3.4 contingent on future surface design). |
| 5 | **Outcome, appetite, scope** | v2 architecture-reference (merge-guard-as-derivation-mechanism + event-time-vs-chain-time vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-line description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (1 line is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/182-fredhead88-do-it-v2-merge-guard-derives-state-HANDOFF.md` and `features/182-fredhead88-do-it-v2-merge-guard-derives-state.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section vocabulary for the next v2 second-stakeholder question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 surface that introduces a second stakeholder — accountant, tax authority, regulator):

- `app/models/audit_log.py` — possibly add an explicit `chain_position` semantic-alias view on `audit_logs.id` (depends on the v2 change; no schema migration needed since `id` is already BIGSERIAL).
- `app/routers/` (FastAPI route handlers) — possibly wrap in a guard-layer middleware that enforces the merge-execution discipline (depends on the v2 change).
- `app/services/provenance.py` (new) — possibly add a v2 surface that exposes the chain-of-custody proof to the second stakeholder (e.g., `/audit-proof/<row_id>` returning the chain position + derived timestamp).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-conventions` §Definition of done:

**Today (defer artifact):**
- [ ] `features/182-fredhead88-do-it-v2-merge-guard-derives-state.md` exists and is read back by the parent.
- [ ] `specs/182-fredhead88-do-it-v2-merge-guard-derives-state-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The do-it-v2 description is quoted verbatim (1-line + 2 sub-primitives).
- [ ] The 0★/0⑂ + no-license (predecessor MIT) + 20-day-old + Python + 896 KB stack-shape cluster is documented.
- [ ] The *merge-guard-as-derivation-mechanism + event-time-vs-chain-time* primitives are documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 surface introduces a second stakeholder):**
- [ ] The PR is read back by the parent.
- [ ] The do-it-v2 JTBD-validation set is evaluated against the PR's changes: does the change preserve *append-only* discipline? Does the change introduce *chain-position-derived* timestamps alongside writer-asserted timestamps? Does the change preserve *merge-guard-execution* discipline (vs *merge-modelling* discipline)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `chain_position` semantic-alias view; remove the new guard-layer middleware; remove the new `provenance` service; remove the new `/audit-proof/<row_id>` endpoint.
- Migration cost: depends on the v2 change; the do-it-v2 pattern's *merge-guard-as-derivation-mechanism + event-time-vs-chain-time* implies *additive architecture* (the new layer is additive on top of the existing v1 surfaces — `audit_logs` append-only + StockEntry ledger).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

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
| Feature ID | 182 |
| Slug | `fredhead88-do-it-v2-merge-guard-derives-state` |
| Bucket | v2 architecture-reference (merge-guard-as-derivation-mechanism + event-time-vs-chain-time) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/audit_log.py` (possibly `chain_position` semantic-alias view) + `app/routers/` (possibly guard-layer middleware) + `app/services/provenance.py` (possibly new v2 surface) |
| Trigger condition | First v2 surface that introduces a second stakeholder (accountant, tax authority, regulator) |
| Verification protocol | Does the change preserve append-only discipline? Does it introduce chain-position-derived timestamps alongside writer-asserted timestamps? Does it preserve merge-guard-execution discipline? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-259 (Research 2026-09-16 — daily) |
| Linear sub-issue | HMM-260 (Feature 182 — fredhead88-do-it-v2-merge-guard-derives-state) |
| Lead source | GitHub `fredhead88/do-it-v2` (no-license, 0★, Python, pushed 2026-09-16T04:20:14Z, created 2026-08-27) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 surface introduces a second stakeholder): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the *merge-guard-as-derivation-mechanism + event-time-vs-chain-time + second-stakeholder* JTBD validation is the right architectural checklist (an owner decision).
