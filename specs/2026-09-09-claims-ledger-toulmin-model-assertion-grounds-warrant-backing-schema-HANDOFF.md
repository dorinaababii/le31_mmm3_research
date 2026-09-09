# 2026-09-09 — `claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/161-claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v2 introduces an owner-facing audit trail, the operator wants *a ready-made schema for separating claim from justification*, but struggles because *the audit trail today is a flat log*, so that *the v2 audit trail has a defensible schema*." **PASS** (zero-pain today; the surface that would *use* the schema doesn't exist; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 2 KB? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. MIT license permits documentation reference. Confidence high for the schema match (assertion/grounds/warrant/backing is the standard Toulmin model); high for the derivation match (the verdict-list derivation is the same pattern as charter §3.1's "current stock is derived from entries"). **PASS**. |
| 4 | **Conflict** | None. The claims-ledger *"append-only verdict list"* pattern *is* the LE31 §3.1 *"current stock is derived from entries"* invariant generalized to audit trails; the *"assertion/grounds/warrant/backing schema"* is a structured extension of the audit trail. **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2 KB description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2 KB is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-09-claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema-HANDOFF.md` and `features/161-claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 owner-facing audit-trail surface).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an owner-facing audit trail, a `verdict` table, or `grounds`/`warrant`/`backing` fields on `audit_logs`):

- `app/models/audit_logs.py` — possibly add `grounds` + `warrant` + `backing` fields (depends on the v2 change).
- `app/models/verdict.py` — possibly add (depends on the v2 change).
- `app/state/transitions.py` — possibly add an owner-facing audit-trail transition (depends on the v2 change).
- `app/bot/owner.py` (owner recap Telegram bot) — possibly modify to expose the Toulmin-model schema (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/161-claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema.md` exists and is read back by the parent.
- [ ] `specs/2026-09-09-claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The claims-ledger description is quoted verbatim (2 KB repo).
- [ ] The Toulmin-model schema (assertion/grounds/warrant/backing) is documented.
- [ ] The verdict-list derivation is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an owner-facing audit trail, a `verdict` table, or `grounds`/`warrant`/`backing` fields on `audit_logs` lands):**
- [ ] The PR is read back by the parent.
- [ ] The claims-ledger Toulmin-model schema is evaluated against the PR's changes: does the change preserve *append-only verdict list*? Does the change introduce the *assertion/grounds/warrant/backing schema*? Does the change add the *source field* for provenance?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `verdict` table; remove the `grounds` + `warrant` + `backing` fields; restore the original `audit_logs` schema.
- Migration cost: depends on the v2 change; the claims-ledger pattern's *append-only* implies *no new migrations* (the new fields are additive on top of the existing append-only log).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `verdict` is a *new* table, not a schema change.

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
| Feature ID | 161 |
| Slug | `claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema` |
| Bucket | v2 owner-pains architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/audit_logs.py` (possibly) + `app/models/verdict.py` (possibly) + `app/state/transitions.py` (possibly) + `app/bot/owner.py` (possibly) |
| Trigger condition | First v2 PR that adds an owner-facing audit trail, a `verdict` table, or `grounds`/`warrant`/`backing` fields on `audit_logs` |
| Verification protocol | Does the change preserve *append-only verdict list*? Does it introduce the *assertion/grounds/warrant/backing schema*? Does it add the *source field* for provenance? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-222 |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `Ybx-jp/claims-ledger` (MIT, 0★, pushed 2026-09-09T06:32:26Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds an owner-facing audit trail, a `verdict` table, or `grounds`/`warrant`/`backing` fields on `audit_logs` lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the claims-ledger Toulmin-model schema is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that adds an owner-facing audit trail, a `verdict` table, or `grounds`/`warrant`/`backing` fields on `audit_logs` will append a row here with: PR number, the claims-ledger schema evaluated, the evaluation result, and the operator's sign-off.)*
