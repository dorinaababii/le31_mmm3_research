# 157 — Talos self-hosted Telegram+terminal agent deterministic-permission-kernel HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/157-talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains (operator-architecture reference)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce an *AI-assisted operator* layer where the AI helps the cook or owner with routine tasks, the owner wants *every AI tool call to be gated by an explicit permission check and every permission check to be recorded as an audit log entry*, but struggles because *v1 has no AI agent and no permission kernel*, so that *v2 can offer an AI-assisted operator surface without re-architecting v1*." **PASS** (zero-pain today; v1 has no AI; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read 7.6 KB? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium for the architectural match (the *permission-ledger-as-audit-log* discipline is the architectural twin of LE31 §3.1 explicit-state-transitions). Stack mismatch (Talos has its own AI-agent framework; no code adoption is possible). **PASS**. |
| 4 | **Conflict** | None. The Talos *deterministic permission kernel* primitive *is* the LE31 §3.1 *explicit-state-transitions* discipline applied to AI-agent tool calls; it does not violate §3.4 (the AI is *staff-facing*, not customer-facing, because it cannot act without permission). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains (operator-architecture reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 7.6 KB description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (7.6 KB is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/157-talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel-HANDOFF.md` and `features/157-talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 operator-architecture reference moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an AI-assisted operator surface, a permission-kernel module, or a permission-ledger-as-audit-log enforcement layer):

- `app/permissions/kernel.py` — possibly add a permission-kernel module (depends on the v2 change).
- `app/permissions/ledger.py` — possibly add a permission-ledger-as-audit-log enforcement layer (depends on the v2 change).
- `app/models/audit_log.py` — possibly add a permission-related field (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/157-talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel.md` exists and is read back by the parent.
- [ ] `specs/157-talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The Talos description is quoted verbatim (7.6 KB repo).
- [ ] The 9★ + MIT + self-hosted + local-first + privacy-friendly cluster is documented.
- [ ] The *permission-ledger-as-audit-log* discipline is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an AI-assisted operator surface, a permission-kernel module, or a permission-ledger-as-audit-log enforcement layer lands):**
- [ ] The PR is read back by the parent.
- [ ] The Talos primitive set is evaluated against the PR's changes: does the change preserve *every AI tool call gated by an explicit permission check*? Does the change add *every permission check recorded as an audit log entry*? Does the change preserve the *self-hosted + local-first + privacy-friendly* posture?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new permission-kernel module; remove the new permission-ledger-as-audit-log enforcement layer; remove the new permission-related field on `audit_logs`; restore the original `audit_logs` schema.
- Migration cost: depends on the v2 change; the Talos pattern's *permission-ledger* implies *additive schema* (the new permission-related field is additive on top of the existing append-only log).
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
| Feature ID | 157 |
| Slug | `talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel` |
| Bucket | v2 owner-pains (operator-architecture reference) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/permissions/kernel.py` (possibly) + `app/permissions/ledger.py` (possibly) + `app/models/audit_log.py` (possibly) |
| Trigger condition | First v2 PR that adds an AI-assisted operator surface, a permission-kernel module, or a permission-ledger-as-audit-log enforcement layer |
| Verification protocol | Does the change preserve *every AI tool call gated by an explicit permission check*? Does it add *every permission check recorded as an audit log entry*? Does it preserve *self-hosted + local-first + privacy-friendly*? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-218 |
| Linear sub-issue | HMM-220 (to be created) |
| Lead source | GitHub `talos-kernel/talos` (MIT, 9★, pushed 2026-09-08T06:47:50Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds an AI-assisted operator surface, a permission-kernel module, or a permission-ledger-as-audit-log enforcement layer lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the Talos primitive set is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that adds an AI-assisted operator surface, a permission-kernel module, or a permission-ledger-as-audit-log enforcement layer will append a row here with: PR number, the Talos primitive set evaluated, the evaluation result, and the operator's sign-off.)*