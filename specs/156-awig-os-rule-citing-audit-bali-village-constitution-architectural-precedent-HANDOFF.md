# 156 — AWIG-OS rule-citing-audit Bali-village-constitution architectural precedent HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/156-awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to author *shift-specific rules* as a *primary surface* (rather than author them implicitly via operational event types), the owner wants *a rule-citing-audit log where every `audit_logs` row carries the rule that authorised the action*, but struggles because *v1 has no such surface and the append-only posture is structurally entrenched*, so that *v2 can offer a rule-citing-audit surface without re-architecting v1*." **PASS** (zero-pain today; v1 is small enough that rules are implicit in the event type; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read 0.8 KB? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium for the architectural match (the *rule-citation-as-first-class-element-of-the-audit-log-entry* primitive is one-shot more specific than features 137/138/141/152). Stack mismatch (Python but GPL-3.0 → §3.2 blocker) → no code adoption is possible. **PASS**. |
| 4 | **Conflict** | None. The AWIG-OS *every-act-cites-the-rule* primitive *is* the LE31 §3.1 *append-only posture* with the rule citation as a first-class field; it does not violate §3.4 (the rule citation is the *authorization*, not the *AI action*). **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 0.8 KB description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (0.8 KB is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/156-awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent-HANDOFF.md` and `features/156-awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a `rule_id` field to `audit_logs`, an `awig-awig` rule-authoring surface, or a *rule-citation enforcement layer*):

- `app/models/audit_log.py` — possibly add a `rule_id` column (depends on the v2 change).
- `app/models/rule.py` — possibly add a rule model (depends on the v2 change).
- `app/state/rule_citation.py` — possibly add a rule-citation enforcement layer (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/156-awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent.md` exists and is read back by the parent.
- [ ] `specs/156-awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The AWIG-OS description is quoted verbatim (0.8 KB repo).
- [ ] The Bali `awig-awig` / `subak` cultural precedent is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a `rule_id` field to `audit_logs`, an `awig-awig` rule-authoring surface, or a rule-citation enforcement layer lands):**
- [ ] The PR is read back by the parent.
- [ ] The AWIG-OS primitive set is evaluated against the PR's changes: does the change preserve *every-act-cites-the-rule*? Does the change add *refusals-recorded-the-same-way*? Does the change add *system-rebuilds-from-its-record*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `rule_id` field; remove the new rule model; remove the new rule-citation enforcement layer; restore the original `audit_logs` schema.
- Migration cost: depends on the v2 change; the AWIG-OS pattern's *every-act-cites-the-rule* implies *additive schema* (the new `rule_id` column is additive on top of the existing append-only log).
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
| Feature ID | 156 |
| Slug | `awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent` |
| Bucket | v2 owner-pains (architecture-reference) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/audit_log.py` (possibly) + `app/models/rule.py` (possibly) + `app/state/rule_citation.py` (possibly) |
| Trigger condition | First v2 PR that adds a `rule_id` field to `audit_logs`, an `awig-awig` rule-authoring surface, or a rule-citation enforcement layer |
| Verification protocol | Does the change preserve *every-act-cites-the-rule*? Does it add *refusals-recorded-the-same-way*? Does it add *system-rebuilds-from-its-record*? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-218 |
| Linear sub-issue | HMM-219 (to be created) |
| Lead source | GitHub `kfkchau/AWIG-OS` (GPL-3.0, 0★, pushed 2026-09-08T03:56:50Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds a `rule_id` field to `audit_logs`, an `awig-awig` rule-authoring surface, or a rule-citation enforcement layer lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the AWIG-OS primitive set is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that adds a `rule_id` field to `audit_logs`, an `awig-awig` rule-authoring surface, or a rule-citation enforcement layer will append a row here with: PR number, the AWIG-OS primitive set evaluated, the evaluation result, and the operator's sign-off.)*