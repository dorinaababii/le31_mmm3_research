# 158 — Azizsekerdil Smart Restaurant Management System AI-powered POS+KDS+inventory HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/158-azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains (cross-section competitive signal)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner asks *'does the operator want a single integrated AI-assisted surface for restaurant ops?'*, the owner wants *evidence that another independent maintainer is building exactly that surface in 2026*, but struggles because *v1 has no such surface and the no-AI posture is structurally entrenched*, so that *v2 can offer an AI-assisted operator surface without re-architecting v1*." **PASS** (zero-pain today; v1 has no AI; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read 17.6 KB? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the JTBD validation (the description is a *direct competitor signal* from an independent maintainer in 2026). Stack mismatch (NOASSERTION fails §3.2; AI-powered raises §3.4) → no code adoption is possible. **PASS**. |
| 4 | **Conflict** | None. The Azizsekerdil *single-app-single-integrated-surface* cluster *is* a v2 question, not a v1 question; it does not violate §3.1 (append-only posture is preserved) or §3.4 (the v1 surface remains no-AI; the v2 surface would adopt the AI-assisted posture). **PASS** (charter §3.1 + §3.4 invariant-compatible for v1; v2 question is a v2 question). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains (cross-section competitive signal); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 17.6 KB description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (17.6 KB is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/158-azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory-HANDOFF.md` and `features/158-azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section JTBD-validation for the next v2 owner-pains question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an AI-assisted operator surface, a single-app-single-integrated-surface layer, or an AI-powered top layer):

- `app/ai_assisted/operator.py` — possibly add an AI-assisted operator layer (depends on the v2 change).
- `app/ai_assisted/integrated_surface.py` — possibly add a single-app-single-integrated-surface layer (depends on the v2 change).
- `app/models/audit_log.py` — possibly add an AI-related field (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/158-azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory.md` exists and is read back by the parent.
- [ ] `specs/158-azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The Azizsekerdil description is quoted verbatim (17.6 KB repo).
- [ ] The 0★ + NOASSERTION + 23-day-old repo cluster is documented.
- [ ] The *single-app-single-integrated-surface* cluster is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an AI-assisted operator surface, a single-app-single-integrated-surface layer, or an AI-powered top layer lands):**
- [ ] The PR is read back by the parent.
- [ ] The Azizsekerdil JTBD-validation set is evaluated against the PR's changes: does the change address the *single-app-single-integrated-surface* JTBD? Does the change address the *AI-powered top layer* JTBD? Does the change preserve *POS + inventory + kitchen display + reporting + local or cloud AI integrations*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new AI-assisted operator layer; remove the new single-app-single-integrated-surface layer; remove the new AI-related field on `audit_logs`; restore the original `audit_logs` schema.
- Migration cost: depends on the v2 change; the Azizsekerdil pattern's *single-app-single-integrated-surface* implies *additive architecture* (the new layer is additive on top of the existing v1 surfaces).
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
| Feature ID | 158 |
| Slug | `azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory` |
| Bucket | v2 owner-pains (cross-section competitive signal) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/ai_assisted/operator.py` (possibly) + `app/ai_assisted/integrated_surface.py` (possibly) + `app/models/audit_log.py` (possibly) |
| Trigger condition | First v2 PR that adds an AI-assisted operator surface, a single-app-single-integrated-surface layer, or an AI-powered top layer |
| Verification protocol | Does the change address the *single-app-single-integrated-surface* JTBD? Does it address the *AI-powered top layer* JTBD? Does it preserve *POS + inventory + kitchen display + reporting + local or cloud AI integrations*? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-218 |
| Linear sub-issue | HMM-221 (to be created) |
| Lead source | GitHub `Azizsekerdil/smart-restaurant-management-system` (NOASSERTION, 0★, pushed 2026-09-07T03:13:20Z, created 2026-08-15) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds an AI-assisted operator surface, a single-app-single-integrated-surface layer, or an AI-powered top layer lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the *single-app-single-integrated-surface* + *AI-powered top layer* JTBD validation is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that adds an AI-assisted operator surface, a single-app-single-integrated-surface layer, or an AI-powered top layer will append a row here with: PR number, the Azizsekerdil JTBD-validation set evaluated, the evaluation result, and the operator's sign-off.)*