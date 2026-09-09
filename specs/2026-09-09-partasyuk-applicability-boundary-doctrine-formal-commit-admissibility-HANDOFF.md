# 2026-09-09 — `partasyuk-applicability-boundary-doctrine-formal-commit-admissibility` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/162-partasyuk-applicability-boundary-doctrine-formal-commit-admissibility.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v2 introduces an owner-facing audit trail, the operator wants *a ready-made formal commit-eligibility vocabulary*, but struggles because *the audit trail today is a flat log*, so that *the v2 audit trail has a defensible commit-eligibility schema*." **PASS** (zero-pain today; the surface that would *use* the schema doesn't exist; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 2 KB Zenodo abstract? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public Zenodo access; no new infrastructure; no new stack dependencies; no new permissions. **PASS** (MIT-equivalent Zenodo CC-BY 4.0 license permits documentation reference). Confidence high for the vocabulary match (Admissible Basis / Operative Capacity / Common-Cause Independence / Re-Provability is the standard formal commit-eligibility framework); high for the derivation match (the four invariants are the *commit-time* analog of charter §3.1's *"current stock is derived from entries"* invariant). |
| 4 | **Conflict** | None. The Applicability Boundary Doctrine *"commit-time admissibility"* schema maps 1:1 onto charter §3.1's *"every operational transition is a new audit_logs row"* invariant. The Partasyuk vocabulary is a *commit-time* formalization of what LE31 operationalizes at *runtime*. **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2 KB abstract + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2 KB is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-09-partasyuk-applicability-boundary-doctrine-formal-commit-admissibility-HANDOFF.md` and `features/162-partasyuk-applicability-boundary-doctrine-formal-commit-admissibility.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 owner-facing commit-eligibility moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an owner-facing audit trail, a `source` field on `audit_logs`, a `cites` field on `audit_logs`, or a formal type-lock on `audit_logs.action`):

- `app/models/audit_logs.py` — possibly add `source` + `cites` fields (depends on the v2 change).
- `app/models/audit_logs.py` — possibly add a formal type-lock check on `action` (depends on the v2 change).
- `app/bot/owner.py` (owner recap Telegram bot) — possibly modify to expose the Admissible Basis / Operative Capacity / Common-Cause Independence / Re-Provability schema (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/162-partasyuk-applicability-boundary-doctrine-formal-commit-admissibility.md` exists and is read back by the parent.
- [ ] `specs/2026-09-09-partasyuk-applicability-boundary-doctrine-formal-commit-admissibility-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The 3 Zenodo records (`21983371`, `21988251`, `21985437`) are quoted verbatim from Zenodo REST API.
- [ ] The Admissible Basis / Operative Capacity / Common-Cause Independence / Re-Provability schema is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an owner-facing audit trail, a `source` field on `audit_logs`, a `cites` field on `audit_logs`, or a formal type-lock on `audit_logs.action` lands):**
- [ ] The PR is read back by the parent.
- [ ] The Applicability Boundary Doctrine schema is evaluated against the PR's changes: does the change preserve *Admissible Basis* + *Operative Capacity* + *Common-Cause Independence* + *Re-Provability*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `source` + `cites` fields; restore the original `audit_logs` schema.
- Migration cost: depends on the v2 change; the Applicability Boundary Doctrine's *append-only* implies *no new migrations* (the new fields are additive on top of the existing append-only log).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the new fields are *additive*, not a schema change.

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
| Feature ID | 162 |
| Slug | `partasyuk-applicability-boundary-doctrine-formal-commit-admissibility` |
| Bucket | v2 owner-pains architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/audit_logs.py` (possibly) + `app/bot/owner.py` (possibly) |
| Trigger condition | First v2 PR that adds an owner-facing audit trail, a `source` field on `audit_logs`, a `cites` field on `audit_logs`, or a formal type-lock on `audit_logs.action` |
| Verification protocol | Does the change preserve *Admissible Basis* + *Operative Capacity* + *Common-Cause Independence* + *Re-Provability*? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-226 (to be created) |
| Linear sub-issue | (to be created) |
| Lead source | OpenAlex `W7203599068` / `W7203663783` / `W7203618587` (Zenodo `21983371` / `21988251` / `21985437`, Vadym Partasyuk, 2026-08-17..18) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds an owner-facing audit trail, a `source` field on `audit_logs`, a `cites` field on `audit_logs`, or a formal type-lock on `audit_logs.action` lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the Applicability Boundary Doctrine schema is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that adds an owner-facing audit trail, a `source` field on `audit_logs`, a `cites` field on `audit_logs`, or a formal type-lock on `audit_logs.action` will append a row here with: PR number, the Applicability Boundary Doctrine schema evaluated, the evaluation result, and the operator's sign-off.)*