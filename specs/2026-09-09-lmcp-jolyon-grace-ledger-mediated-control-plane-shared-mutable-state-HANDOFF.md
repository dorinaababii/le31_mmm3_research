# 2026-09-09 — `lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/163-lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state.md` (defer artifact; **no code today**).

Bucket: **v2-AI watch-list**. Build verdict: **`defer`** (charter §3.4 territory + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v2 introduces an AI agent surface, the operator wants *a ready-made coordination protocol for human operators + AI agents sharing state*, but struggles because *today's audit trail records only human actions*, so that *the v2 audit trail can record agent + operator actions on equal footing*." **PASS** (zero-pain today; LE31 v1 has no AI agent surface). |
| 2 | **Viability** | Owner can read 2 KB Figshare abstract? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public Figshare access; no new infrastructure; no new stack dependencies; no new permissions. **PASS** (preprint license permits documentation reference). Confidence high for the design-target match (LE31 is exactly an agent + operator + shared mutable state surface); low for transferability (LMCP is a preprint, no peer review, no production implementation). |
| 4 | **Conflict** | **Partial: charter §3.4 territory.** LE31 v1 has no AI agent surface today; introducing one would require a charter §3.4 decision (no customer-facing AI; AI may assist owner/staff with observable evidence and a non-AI fallback). The LMCP primitive is a *coordination protocol*, not a customer-facing surface — so the conflict is **deferred, not blocking**. **PASS** (charter §3.4 decision deferred to v2). |
| 5 | **Outcome, appetite, scope** | v2-AI watch-list; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2 KB abstract + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2 KB is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-09-lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state-HANDOFF.md` and `features/163-lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 AI agent surface).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an `actor_type` field on `audit_logs`, an `agent_id` field on `audit_logs`, or a coordination-events table):

- `app/models/audit_logs.py` — possibly add `actor_type` + `agent_id` fields (depends on the v2 change).
- `app/models/coordination_events.py` — possibly add (depends on the v2 change).
- `app/bot/owner.py` (owner recap Telegram bot) — possibly modify to expose the AI agent + human operator coordination history (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/163-lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state.md` exists and is read back by the parent.
- [ ] `specs/2026-09-09-lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The Figshare preprint ID `33437977` + OpenAlex `W7208739566` + `W7208724202` are quoted verbatim from Figshare REST API + OpenAlex `abstract_inverted_index`.
- [ ] The *"ledger-mediated control plane for asynchronous multi-agent coordination"* primitive is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an `actor_type` field on `audit_logs`, an `agent_id` field on `audit_logs`, or a coordination-events table lands):**
- [ ] The PR is read back by the parent.
- [ ] The LMCP *"ledger-mediated control plane"* primitive is evaluated against the PR's changes: does the change preserve *append-only coordination*? Does the change preserve *asynchronous*? Does the change distinguish *human operator* vs *AI agent*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `actor_type` + `agent_id` fields; remove the new coordination-events table; restore the original `audit_logs` schema.
- Migration cost: depends on the v2 change; the LMCP *"ledger-mediated control plane"* implies *no new migrations* (the new fields are additive on top of the existing append-only log).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the coordination-events table is *new*, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants (especially §3.4 AI).
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
| Feature ID | 163 |
| Slug | `lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state` |
| Bucket | v2-AI watch-list |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/audit_logs.py` (possibly) + `app/models/coordination_events.py` (possibly) + `app/bot/owner.py` (possibly) |
| Trigger condition | First v2 PR that adds an `actor_type` field on `audit_logs`, an `agent_id` field on `audit_logs`, or a coordination-events table |
| Verification protocol | Does the change preserve *append-only coordination*? Does it preserve *asynchronous*? Does it distinguish *human operator* vs *AI agent*? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-226 (Brainstorm 2026-09-09 — daily) |
| Linear sub-issue | HMM-228 (Feature 163 — lmcp-jolyon-grace-ledger-mediated-control-plane-shared-mutable-state, Backlog, Feature label) |
| Lead source | Figshare `33437977` + OpenAlex `W7208739566` (Jolyon Grace, 2026-09-04) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds an `actor_type` field on `audit_logs`, an `agent_id` field on `audit_logs`, or a coordination-events table lands): the external agent must mirror back the frozen contract (per §6 above) AND the operator must confirm the LMCP *"ledger-mediated control plane"* is the right architectural primitive AND a charter §3.4 decision must be made (no customer-facing AI; AI may assist owner/staff with observable evidence and a non-AI fallback).

## 9. Verification log

*(Empty today. The first v2 surface that adds an `actor_type` field on `audit_logs`, an `agent_id` field on `audit_logs`, or a coordination-events table will append a row here with: PR number, the LMCP primitive evaluated, the evaluation result, and the operator's sign-off.)*