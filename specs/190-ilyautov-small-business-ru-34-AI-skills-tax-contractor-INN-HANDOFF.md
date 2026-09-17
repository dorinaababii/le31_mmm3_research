# 190 — ilyautov/small-business-ru 34 AI skills tax contractor INN HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI owner-assist surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/190-ilyautov-small-business-ru-34-AI-skills-tax-contractor-INN.md` (defer artifact; **no code today**).

Bucket: **v2-AI (operator-AI owner-assist, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces an owner-assist AI surface, what is the charter §3.4 invariant pattern?'*, the maintainer wants *evidence that another independent 2026 single-maintainer Python repo at 16★ is shipping exactly the AI-skill-as-package + numbers-computed-by-code + data-from-real-registries primitives that LE31 v2 would need to satisfy charter §3.4*, but struggles because *v1 has no AI-assist surface and the charter §3.4 invariant is not yet operationalized in code*, so that *v2 can introduce the AI-assist surface with the explicit charter §3.4 invariant rather than inventing a new one*." **PASS** (zero-pain today; v1 has no AI-assist surface; the JTBD is primitive vocabulary extension + charter §3.4 validation, not a build-need). |
| 2 | **Viability** | Owner can read 2051 KB repo description + 10 topics? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the architectural vocabulary + charter §3.4 validation (16★/4⑂ is the highest in-window star count for any v2-AI owner-assist peer in 2026; Apache-2.0 + Python + 94-day-old + in-window push 3-days-ago confirms real maintainer with sustained engagement; the *numbers-computed-by-code + data-from-real-registries* principle is explicitly named in the description). Stack: on-pattern (Python matches LE31; Claude Code + Codex + ChatGPT are v2-AI surface primitives, not v1 stack primitives). Practicability of adoption: medium — the *AI-skill-as-package + numbers-computed-by-code + data-from-real-registries* primitives can be extracted and re-implemented against LE31's StockEntry + audit_logs. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The small-business-ru *numbers-computed-by-code + data-from-real-registries* posture is explicitly §3.1-aligned: deterministic state transitions + observable evidence; §3.2 (Apache-2.0 = permissive); §3.4 (the small-business-ru repo is an operator-facing AI-skill package, not customer-facing — the *numbers-computed-by-code + data-from-real-registries* principle is the explicit enforcement boundary that excludes customer-facing AI per charter §3.4). Charter §3.4 explicitly validated. **PASS** (charter §3.1 + §3.2 + §3.4 invariant-compatible + §3.4 validated). |
| 5 | **Outcome, appetite, scope** | v2-AI owner-assist (cross-section architectural vocabulary + charter §3.4 validation); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2051 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2051 KB is already substantial; only the *AI-skill-as-package + numbers-computed-by-code + data-from-real-registries* principle + description need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document + charter §3.4 validation artifact), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/190-ilyautov-small-business-ru-34-AI-skills-tax-contractor-INN-HANDOFF.md` and `features/190-ilyautov-small-business-ru-34-AI-skills-tax-contractor-INN.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + charter §3.4 invariant validation for the next v2-AI owner-assist question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an owner-assist AI surface, an *AI-skill-as-package* subsystem, a *numbers-computed-by-code* deterministic-calc primitive, a *data-from-real-registries* registry-lookup primitive, or an *AI-assist risk-model* with explicit charter §3.4 enforcement):

- `app/ai/skills/` — possibly add an AI-skill-as-package subsystem with discrete Python skills (depends on the v2 change).
- `app/ai/skills/tax.py` — possibly add a *tax* skill (deterministic-calc + registry-lookup; depends on the v2 change).
- `app/ai/skills/money.py` — possibly add a *money* skill (deterministic-calc + bank-registry-lookup; depends on the v2 change).
- `app/ai/skills/contractor_check.py` — possibly add a *contractor-check* skill (registry-lookup via `siret`/`ein`/`inn`; depends on the v2 change).
- `app/ai/governance.py` — possibly add an *AI-assist risk-model* with explicit charter §3.4 enforcement (the AI does not invent numbers; the AI invokes deterministic Python code + reads from real registries; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/190-ilyautov-small-business-ru-34-AI-skills-tax-contractor-INN.md` exists and is read back by the parent.
- [ ] `specs/190-ilyautov-small-business-ru-34-AI-skills-tax-contractor-INN-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The small-business-ru description is quoted verbatim (2051 KB repo).
- [ ] The 16★/4⑂ + Apache-2.0 + 94-day-old + Python + in-window push 3-days-ago + *AI-skill-as-package + numbers-computed-by-code + data-from-real-registries* vocabulary is documented.
- [ ] The charter §3.4 invariant validation (via the *numbers-computed-by-code + data-from-real-registries* principle) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an owner-assist AI surface, an *AI-skill-as-package* subsystem, a *numbers-computed-by-code* deterministic-calc primitive, a *data-from-real-registries* registry-lookup primitive, or an *AI-assist risk-model* with explicit charter §3.4 enforcement lands):**
- [ ] The PR is read back by the parent.
- [ ] The small-business-ru architectural-vocabulary set is evaluated against the PR's changes: does the change address the *AI-skill-as-package + numbers-computed-by-code + data-from-real-registries* vocabulary? Does the change address the charter §3.4 invariant (the *numbers-computed-by-code + data-from-real-registries* principle)? Does the change preserve the *operator-facing + non-customer-facing* posture?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new AI-skill-as-package subsystem; remove the new *numbers-computed-by-code + data-from-real-registries* primitives; remove the new *AI-assist risk-model* with charter §3.4 enforcement; restore the original `audit_logs` + `StockEntry` + `notes` schemas.
- Migration cost: depends on the v2 change; the small-business-ru pattern's *AI-skill-as-package + numbers-computed-by-code + data-from-real-registries* implies *additive architecture* (the new AI-skill-as-package is additive on top of the existing v1 surfaces — `audit_logs` + `StockEntry` + `notes` + aiogram handlers; the new primitive layer adds discrete deterministic-calc + registry-lookup skills).
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
| Active feature path | `features/190-ilyautov-small-business-ru-34-AI-skills-tax-contractor-INN.md` |
| Bucket | v2-AI (operator-AI owner-assist, parking-lot defer) |
| Build verdict | **`defer`** (charter §3.1 + `le31-conventions` Feature gate) |
| Parent research issue | HMM-270 (Brainstorm 2026-09-17 — daily) |
| GitHub URL | https://github.com/ilyautov/small-business-ru |
| License | Apache-2.0 ✓ |
| Stars / forks | 16★ / 4⑂ (highest in-window star count of any 2026-09-17 net-new v2-AI owner-assist candidate) |
| Pushed at / created at | 2026-09-14T15:54:43Z / 2026-06-15T21:29:32Z |
| Files to touch today | NONE (defer artifact, documentation only) |
| Verification protocol | `le31-verification-protocol/SKILL.md` + `le31-conventions` §Definition of done |
| Rollback path | Delete `features/190-...md` + `specs/190-...-HANDOFF.md` (trivially reversible) |
| Mandatory skills | le31-conventions + le31-v1-feature-pattern + le31-handoff-spec + le31-conventions-coder + le31-arch-patterns + le31-data-correctness + le31-quality-gates |

**Mirror-back required**: the external agent must echo this frozen contract (Section 1 + 2 + 3 + 4 + 5 + 6) back before implementing and stop if it cannot.
