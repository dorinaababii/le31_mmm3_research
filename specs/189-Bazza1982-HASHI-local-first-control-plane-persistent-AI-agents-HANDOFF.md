# 189 — Bazza1982/HASHI local-first control plane for persistent AI agents HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI control-plane surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/189-Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents.md` (defer artifact; **no code today**).

Bucket: **v2-AI (operator-AI control-plane + multi-agent governance, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces an AI-agent control plane, what is the named set of primitives?'*, the maintainer wants *evidence that another independent 2026 single-maintainer Python repo is shipping exactly the named set of six primitives — identity + memory + tools + workflows + governance + multi-channel — as a discrete subsystem*, but struggles because *v1 has an implicit control plane and the no-cloud posture means any future AI-agent control plane must be explicitly local-first + multi-provider + governance-bounded*, so that *v2 can introduce the AI-agent control plane with the named primitives rather than inventing a new one*." **PASS** (zero-pain today; v1 has an implicit control plane; the JTBD is primitive vocabulary extension, not a build-need). |
| 2 | **Viability** | Owner can read 149646 KB repo description + 10 topics? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the architectural vocabulary validation (MIT + Python + 191-day-old + first in-window push today confirms real maintainer with sustained engagement; the *six primitives* ordering matches the canonical 2026 AI-agent control-plane literature). Stack: on-pattern (Python matches LE31; LiteLLM/MCP are v2-AI surface primitives, not v1 stack primitives). Practicability of adoption: medium — the *local-first control plane + six primitives* can be extracted and re-implemented against LE31's StockEntry + audit_logs. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The HASHI *local-first + self-hosted* posture is explicitly §3.1-aligned; §3.2 (MIT = permissive); §3.4 (HASHI names *"governance"* as the 5th primitive — the *governance* primitive is the explicit enforcement boundary that excludes guest/user-facing surfaces per charter §3.4). Charter §3.4 compatible. **PASS** (charter §3.1 + §3.2 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI control-plane (cross-section architectural vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 149646 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (149646 KB is already substantial; only the *control-plane + six primitives* + description need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/189-Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents-HANDOFF.md` and `features/189-Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary for the next v2-AI control-plane question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an AI-agent control plane as a discrete subsystem, an *identity* primitive, a *memory* primitive, a *tools* primitive, a *workflows* primitive, a *governance* primitive, or a *multi-channel* primitive):

- `app/ai/control_plane/` — possibly add an AI-agent control plane as a discrete subsystem with named primitives (identity + memory + tools + workflows + governance + multi-channel; depends on the v2 change).
- `app/ai/identity.py` — possibly add an *identity* primitive (which actor?; depends on the v2 change).
- `app/ai/memory.py` — possibly add a *memory* primitive (what do they know?; depends on the v2 change).
- `app/ai/tools.py` — possibly add a *tools* primitive (what can they do?; depends on the v2 change).
- `app/ai/workflows.py` — possibly add a *workflows* primitive (in what sequence?; depends on the v2 change).
- `app/ai/governance.py` — possibly add a *governance* primitive (what bounds?; charter §3.4 alignment via explicit enforcement; depends on the v2 change).
- `app/ai/channels.py` — possibly add a *multi-channel* primitive (how is it delivered?; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/189-Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents.md` exists and is read back by the parent.
- [ ] `specs/189-Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The HASHI description is quoted verbatim (149646 KB repo).
- [ ] The 1★/0⑂ + MIT + 191-day-old + Python + first-in-window-push-today + *local-first + self-hosted + multi-agent + agent-orchestration* topic set + *identity + memory + tools + workflows + governance + multi-channel* six-primitive vocabulary is documented.
- [ ] The charter §3.4 alignment via explicit *governance* primitive is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an AI-agent control plane as a discrete subsystem, an *identity* primitive, a *memory* primitive, a *tools* primitive, a *workflows* primitive, a *governance* primitive, or a *multi-channel* primitive lands):**
- [ ] The PR is read back by the parent.
- [ ] The HASHI architectural-vocabulary set is evaluated against the PR's changes: does the change address the *control-plane + six primitives* vocabulary? Does the change address the *governance* primitive (charter §3.4 alignment)? Does the change preserve the *local-first + self-hosted + multi-agent* posture?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new AI-agent control plane; remove the new *identity + memory + tools + workflows + governance + multi-channel* primitives; remove the new governance enforcement layer; restore the original `audit_logs` + `StockEntry` + `notes` schemas.
- Migration cost: depends on the v2 change; the HASHI pattern's *local-first control plane + six primitives* implies *additive architecture* (the new control plane is additive on top of the existing v1 surfaces — FastAPI routes + aiogram handlers + `audit_logs` writer all live in one Python process today; the new control plane adds a discrete subsystem layer with named primitives).
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
| Active feature path | `features/189-Bazza1982-HASHI-local-first-control-plane-persistent-AI-agents.md` |
| Bucket | v2-AI (operator-AI control-plane + multi-agent governance, parking-lot defer) |
| Build verdict | **`defer`** (charter §3.1 + `le31-conventions` Feature gate) |
| Parent research issue | HMM-270 (Brainstorm 2026-09-17 — daily) |
| GitHub URL | https://github.com/Bazza1982/HASHI |
| License | MIT ✓ |
| Stars / forks | 1★ / 0⑂ |
| Pushed at / created at | 2026-09-17T04:04:19Z / 2026-03-10T13:09:33Z |
| Files to touch today | NONE (defer artifact, documentation only) |
| Verification protocol | `le31-verification-protocol/SKILL.md` + `le31-conventions` §Definition of done |
| Rollback path | Delete `features/189-...md` + `specs/189-...-HANDOFF.md` (trivially reversible) |
| Mandatory skills | le31-conventions + le31-v1-feature-pattern + le31-handoff-spec + le31-conventions-coder + le31-arch-patterns + le31-data-correctness + le31-quality-gates |

**Mirror-back required**: the external agent must echo this frozen contract (Section 1 + 2 + 3 + 4 + 5 + 6) back before implementing and stop if it cannot.
