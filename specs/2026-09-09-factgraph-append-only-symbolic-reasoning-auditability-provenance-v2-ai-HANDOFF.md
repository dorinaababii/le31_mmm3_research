# 2026-09-09 — `factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/160-factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai.md` (defer artifact; **no code today**).

Bucket: **v2-AI architecture-reference**. Build verdict: **`defer`** (charter §3.4 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v2-AI introduces an AI-assisted feature (e.g. menu suggestion, prep-time forecast, owner recap), the operator wants *a named auditability+provenance+explainability vocabulary*, but struggles because *the primitive doesn't exist in the LE31 codebase today*, so that *the v2-AI surface has observable evidence per charter §3.4*." **PASS** (zero-pain today; the surface that would *use* the primitive doesn't exist; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 13 KB? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Apache-2.0 license permits documentation reference. Confidence high for the vocabulary match (auditability + provenance + explainability = LE31 §3.4's "observable evidence"). **PASS**. |
| 4 | **Conflict** | None. The factgraph *"auditability+provenance+explainability vocabulary"* is the *named discipline* that operationalizes charter §3.4's "AI with observable evidence". **PASS** (charter §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI architecture-reference; **zero build time today**. Maximum time worth spending: 1-2 hours (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 13 KB repo + add cross-section to existing `HANDOFF.md` (1-2 hours). **Cost-to-value ratio: high** (the vocabulary is named clearly in the README). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-09-factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai-HANDOFF.md` and `features/160-factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI surface).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2-AI trigger condition fires (first v2-AI PR that adds an AI-assisted suggestion, an `ai_assistance_log` table, or a `source`/`derivation_chain` field on `audit_logs`):

- `app/models/audit_logs.py` — possibly add a `source` field + a `derivation_chain` field (depends on the v2-AI change).
- `app/models/ai_assistance_log.py` — possibly add (depends on the v2-AI change).
- `app/state/transitions.py` — possibly add an AI-assisted suggestion transition (depends on the v2-AI change).
- `app/bot/cook.py` (Telegram bot) — possibly modify to surface AI suggestions + audit trail (depends on the v2-AI change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/160-factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai.md` exists and is read back by the parent.
- [ ] `specs/2026-09-09-factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The factgraph description is quoted verbatim (13 KB repo).
- [ ] The auditability+provenance+explainability vocabulary is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2-AI trigger (when the first v2-AI PR that adds an AI-assisted suggestion, an `ai_assistance_log` table, or a `source`/`derivation_chain` field on `audit_logs` lands):**
- [ ] The PR is read back by the parent.
- [ ] The factgraph auditability+provenance+explainability vocabulary is evaluated against the PR's changes: does the change satisfy *auditability* (every AI suggestion has a queryable trail)? Does the change satisfy *provenance* (every AI suggestion has a source)? Does the change satisfy *explainability* (every AI suggestion has a derivation chain)? Does the change have a non-AI fallback per charter §3.4?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2-AI surface (if it lands):**
- Disable: revert the PR; disable the AI-assisted feature in production.
- Delete: revert the PR; remove the new `ai_assistance_log` table; remove the `source` + `derivation_chain` fields; restore the original `audit_logs` schema.
- Migration cost: depends on the v2-AI change; the factgraph pattern's *append-only* implies *no new migrations* (the new fields are additive on top of the existing append-only log).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `ai_assistance_log` is a *new* table, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants (especially §3.4: AI with observable evidence and a non-AI fallback).
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
| Feature ID | 160 |
| Slug | `factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai` |
| Bucket | v2-AI architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/audit_logs.py` (possibly) + `app/models/ai_assistance_log.py` (possibly) + `app/state/transitions.py` (possibly) + `app/bot/cook.py` (possibly) |
| Trigger condition | First v2-AI PR that adds an AI-assisted suggestion, an `ai_assistance_log` table, or a `source`/`derivation_chain` field on `audit_logs` |
| Verification protocol | Does the change satisfy *auditability*? Does it satisfy *provenance*? Does it satisfy *explainability*? Does it have a non-AI fallback per charter §3.4? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-222 |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `Symbolic-Intelligence-Org/factgraph` (Apache-2.0, 1★, pushed 2026-09-08T16:00:59Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2-AI trigger sign-off gap** (when the first v2-AI PR that adds an AI-assisted suggestion, an `ai_assistance_log` table, or a `source`/`derivation_chain` field on `audit_logs` lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the factgraph auditability+provenance+explainability vocabulary is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2-AI surface that adds an AI-assisted suggestion, an `ai_assistance_log` table, or a `source`/`derivation_chain` field on `audit_logs` will append a row here with: PR number, the factgraph vocabulary evaluated, the evaluation result, and the operator's sign-off.)*
