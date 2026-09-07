# 2026-09-07 — `coxswain-graphs-harness-owns-consequence-architecture-pattern` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/148-coxswain-graphs-harness-owns-consequence-architecture-pattern.md` (defer artifact; **no code today**).

Bucket: **v1 architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 maintainer reads the codebase, the owner wants *a one-sentence statement of the architecture*, but struggles because *the architecture is implicit in the code*, so that *the next maintainer can verify the architecture hasn't drifted*." **PASS** (zero-pain today; the codebase is small enough that the architecture is implicit; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 619 B? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the architectural match (the four sub-primitives — gate / worktree / checks / append-only ledger — map onto LE31's operational-transition gate, FastAPI request handling, validation pipeline, and audit_logs respectively). **PASS**. |
| 4 | **Conflict** | None. The coxswain-graphs "graphs own sequence and write nothing" pattern *is* the LE31 §3.1 *current stock is derived from entries* invariant; "one harness owns every consequence" *is* the LE31 §3.1 *do not silently send, serve, close, or reconcile* invariant. **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v1 architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 619 B description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (619 B is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-07-coxswain-graphs-harness-owns-consequence-architecture-pattern-HANDOFF.md` and `features/148-coxswain-graphs-harness-owns-consequence-architecture-pattern.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v1 architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that adds a new subsystem, refactors the FastAPI process structure, or splits the harness into multiple processes):

- `app/main.py` — possibly refactor the FastAPI process structure (depends on the v1 change).
- `app/audit/log.py` — possibly add a new audit event type (depends on the v1 change).
- `app/state/transitions.py` — possibly add a new operational transition (depends on the v1 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/148-coxswain-graphs-harness-owns-consequence-architecture-pattern.md` exists and is read back by the parent.
- [ ] `specs/2026-09-07-coxswain-graphs-harness-owns-consequence-architecture-pattern-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The coxswain-graphs description is quoted verbatim (619 B repo).
- [ ] The 1:1 mapping onto LE31 v1 architecture is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that adds a new subsystem, refactors the FastAPI process structure, or splits the harness into multiple processes):**
- [ ] The PR is read back by the parent.
- [ ] The coxswain-graphs pattern is evaluated against the PR's changes: does the change preserve *one harness owns every consequence*? Does it preserve *graphs own sequence and write nothing*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new subsystem; restore the original FastAPI process structure.
- Migration cost: depends on the v1 change; the coxswain-graphs pattern's "one harness" implies *no new migrations* (the harness is the FastAPI process, not a new schema).
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
| Feature ID | 148 |
| Slug | `coxswain-graphs-harness-owns-consequence-architecture-pattern` |
| Bucket | v1 architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/main.py` (possibly) + `app/audit/log.py` (possibly) + `app/state/transitions.py` (possibly) |
| Trigger condition | First v1 PR that adds a new subsystem, refactors the FastAPI process structure, or splits the harness into multiple processes |
| Verification protocol | Does the change preserve *one harness owns every consequence*? Does it preserve *graphs own sequence and write nothing*? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-204 (Research 2026-09-07 — daily) |
| Linear sub-issue | HMM-206 (to be created) |
| Lead source | GitHub `ppfenning/coxswain-graphs` (MIT, 0★, pushed 2026-09-06T21:17:39Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v1 trigger sign-off gap** (when the first v1 PR that changes the architecture lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the coxswain-graphs pattern is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v1 surface that changes the architecture will append a row here with: PR number, the coxswain-graphs pattern evaluated, the evaluation result, and the operator's sign-off.)*
