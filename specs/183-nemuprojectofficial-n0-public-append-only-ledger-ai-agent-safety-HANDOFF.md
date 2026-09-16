# 183 — nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI control-plane surface (or v2 second-stakeholder surface) becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/183-nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety.md` (defer artifact; **no code today**).

Bucket: **v2-AI control-plane (dependency-free verifier primitive; charter §3.4 territory; staff-tooling territory if exposed to a customer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 surface introduces a second stakeholder (accountant, tax authority, regulator) OR an LLM-assisted surface, the owner wants *a primitive that lets the stakeholder verify the LE31 `audit_logs` chain integrity without running the LE31 codebase*, but struggles because *LE31 v1's audit_logs are written by the FastAPI process and the verifier would have to depend on the FastAPI runtime*, so that *the v2 surface can offer external-auditor verification with a defensible answer*." **PASS** (zero-pain today; v1 has no second stakeholder; the JTBD is primitive documentation, not a build-need). |
| 2 | **Viability** | Owner can read the description (1-line)? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (MIT Python + `psycopg` + `argparse` are widely-available). Confidence medium-high for the primitive match (description + 8 topics align with v2-AI control-plane vocabulary); low for transferability (LE31 v1 has no external-auditor surface). §3.4 conflict: **the verifier itself is not AI; the *autonomous-agent* that produces the ledger is autonomous-agents territory, but the verifier is a format-checker; if a v2 surface ever exposes the verifier to a customer, it would be a *verification tool*, not an AI assistant — §3.4 not triggered for the verifier itself**. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The n0-public *dependency-free verifier* primitive *is* a v2 question, not a v1 question; it does not violate §3.1 (the verifier is read-only; the append-only invariant is preserved). §3.4 conflict is contingent on whether the v2 surface is staff-tooling or customer-facing (none currently planned); the *primitive itself* is not AI. **PASS** (charter §3.1 invariant-compatible for v1; §3.4 contingent on future surface design). |
| 5 | **Outcome, appetite, scope** | v2-AI control-plane (dependency-free verifier + 8-topic vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-line description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (1 line is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/183-nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety-HANDOFF.md` and `features/183-nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section vocabulary for the next v2-AI control-plane question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 surface that introduces a second stakeholder OR an LLM-assisted surface):

- `scripts/verify_audit_logs.py` (new) — standalone Python verifier; no FastAPI, no SQLModel, no aiogram dependencies; reads `audit_logs` from PostgreSQL with read-only credentials; verifies (a) chain integrity (no row deleted or updated; monotonic `id`; no gaps) and (b) schema integrity (every row matches the expected schema; every `actor_user_id` is a valid user; every `action` is a valid action enum).
- `.github/workflows/verify_audit_logs.yml` (new) — CI workflow that runs the verifier on every commit; fails CI if the verification fails.
- Optional: `app/services/llm_provenance.py` (new, if §3.4 LLM-assisted surface lands) — wires the verifier into the LLM-assisted recommendation flow so the verifier runs *before* the recommendation is shown to the cook.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-conventions` §Definition of done:

**Today (defer artifact):**
- [ ] `features/183-nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety.md` exists and is read back by the parent.
- [ ] `specs/183-nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The n0-public description is quoted verbatim (1-line + 8 GitHub topics).
- [ ] The 0★/0⑂ + MIT + 10-day-old + Python + 220+ KB stack-shape cluster is documented.
- [ ] The *dependency-free verifier for the ledger format* primitive is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 surface introduces a second stakeholder OR an LLM-assisted surface):**
- [ ] The PR is read back by the parent.
- [ ] The n0-public JTBD-validation set is evaluated against the PR's changes: does the verifier read `audit_logs` with read-only credentials? Does the verifier check chain integrity (no row deleted or updated)? Does the verifier check schema integrity (every row matches the expected schema)? Does the verifier have *no* LE31-application-runtime dependencies?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove `scripts/verify_audit_logs.py`; remove the CI workflow; remove the `llm_provenance` service (if §3.4 surface lands).
- Migration cost: depends on the v2 change; the n0-public pattern's *dependency-free verifier* implies *additive architecture* (the verifier is a separate standalone program; no schema change required for the basic verifier; the `chain_position` column from feature 182 would be needed for chain-integrity verification).
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
| Feature ID | 183 |
| Slug | `nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety` |
| Bucket | v2-AI control-plane (dependency-free verifier for the ledger format) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `scripts/verify_audit_logs.py` (new) + `.github/workflows/verify_audit_logs.yml` (new) + optional `app/services/llm_provenance.py` (if §3.4 surface lands) |
| Trigger condition | First v2 surface that introduces a second stakeholder OR an LLM-assisted surface |
| Verification protocol | Does the verifier read audit_logs with read-only credentials? Does it check chain integrity (no row deleted or updated)? Does it check schema integrity (every row matches the expected schema)? Does it have no LE31-application-runtime dependencies? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-259 (Research 2026-09-16 — daily) |
| Linear sub-issue | HMM-261 (Feature 183 — nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety) |
| Lead source | GitHub `nemuprojectofficial-glitch/n0-public` (MIT, 0★, Python, pushed 2026-09-16T05:37:14Z, created 2026-09-06) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 surface introduces a second stakeholder or an LLM-assisted surface): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the *dependency-free verifier + chain-integrity + schema-integrity + no-runtime-dependencies* JTBD validation is the right architectural checklist (an owner decision).
