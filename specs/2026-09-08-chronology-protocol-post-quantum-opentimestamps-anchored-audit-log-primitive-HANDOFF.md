# 2026-09-08 — `chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/154-chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains architecture-reference**. Build verdict: **`defer`** (charter §3.1 + §3.2 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v2 introduces a cryptographic-verifiability surface (regulator-facing / partner-facing / owner-facing audit-export with non-repudiation requirements), the owner wants *a ready-made named primitive for post-quantum provenance*, but struggles because *the primitive doesn't exist in the LE31 codebase today*, so that *the v2 surface has a defensible cryptographic foundation*." **PASS** (zero-pain today; the threat model is *accidental corruption*, not *malicious tampering*; the surface that would *use* the primitive doesn't exist). |
| 2 | **Viability** | Owner can read 128 KB substantial repo? Yes (the README + topics are the value; the full code is not required). No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the cryptographic-verifiability primitive (the topics + description align with the OpenTimestamps ecosystem + post-quantum signature research; the *ledger-independent* discipline is a credible design choice). **PASS**. |
| 4 | **Conflict** | None. The chronology-protocol "append-only chronologies" pattern *is* the LE31 §3.1 *current stock is derived from entries* invariant; the "ledger-independent" pattern *is* the LE31 §3.1 *do not silently send, serve, close, or reconcile* invariant (the chronology is a *transformation* of the log, not a separate system). **PASS** (charter §3.1 + §3.2 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains architecture-reference; **zero build time today**. Maximum time worth spending: 1-2 hours (add cross-section to existing documentation; the README is the value, the full code is not required). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document the chronology-protocol primitive + add cross-section to existing `HANDOFF.md` (1-2 hours). **Cost-to-value ratio: high** (the README names the primitive clearly). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-08-chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive-HANDOFF.md` and `features/154-chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a regulator-facing audit-export surface with non-repudiation requirements, a partner-facing audit-export surface with non-repudiation requirements, a post-quantum signature scheme, or an OpenTimestamps anchoring surface):

- `app/audit/log.py` — possibly add a `previous_hash` column to `audit_logs` (depends on the v2 change).
- `app/audit/chronology.py` — possibly add a new chronology module (OpenTimestamps client + Bitcoin block verification).
- `app/audit/anchor.py` — possibly add a new anchoring surface.
- `app/state/transitions.py` — possibly add a new operational transition (regulator-facing audit export).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/154-chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive.md` exists and is read back by the parent.
- [ ] `specs/2026-09-08-chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The chronology-protocol description is quoted verbatim (128 KB substantial repo).
- [ ] The 1:1 mapping onto LE31 v1/v2 architecture is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a cryptographic-verifiability surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The chronology-protocol primitive is evaluated against the PR's changes: does the change preserve *append-only chronologies*? Does the change add *cryptographic renewal*? Does the change add *physical-time observation attestation*? Does the change add *Jan09-compatible block anchoring*? Does the change preserve *ledger-independent* discipline?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR; remove the new `previous_hash` column on `audit_logs`.
- Delete: revert the PR; remove the new chronology module; remove the new anchoring surface; restore the original `audit_logs` schema.
- Migration cost: depends on the v2 change; the chronology-protocol pattern's *append-only* implies *no new migrations* (the new columns are additive on top of the existing append-only log).
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
| Feature ID | 154 |
| Slug | `chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive` |
| Bucket | v2 owner-pains architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/audit/log.py` (possibly) + `app/audit/chronology.py` (new, possibly) + `app/audit/anchor.py` (new, possibly) + `app/state/transitions.py` (possibly) |
| Trigger condition | First v2 PR that adds a regulator-facing audit-export surface with non-repudiation requirements, a partner-facing audit-export surface with non-repudiation requirements, a post-quantum signature scheme, or an OpenTimestamps anchoring surface |
| Verification protocol | Does the change preserve *append-only chronologies*? Does it add *cryptographic renewal*? Does it add *physical-time observation attestation*? Does it add *Jan09-compatible block anchoring*? Does it preserve *ledger-independent* discipline? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | (to be created) |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `machine-native/chronology-protocol` (Apache-2.0, 0★, pushed 2026-09-06T22:55:46Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds a cryptographic-verifiability surface lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the chronology-protocol primitive is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that adds a cryptographic-verifiability primitive will append a row here with: PR number, the chronology-protocol primitive evaluated, the evaluation result, and the operator's sign-off.)*