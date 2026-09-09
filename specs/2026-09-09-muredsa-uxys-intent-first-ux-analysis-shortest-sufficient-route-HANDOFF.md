# 2026-09-09 — `muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/164-muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route.md` (defer artifact; **no code today**).

Bucket: **v2 operator-UX architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v2 introduces an operator-facing review or recap surface, the operator wants *a static-analysis tool that surfaces the smallest sufficient action set at every moment*, but struggles because *the v1 waiter web UI shows all menu items at every moment*, so that *the v2 surface can be audited for operator-UX quality*." **PASS** (zero-pain today; the surface that would *use* the audit doesn't exist). |
| 2 | **Viability** | Owner can read the 1-line description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. **PASS** (MIT license permits documentation reference). Confidence high for the primitive match (the *"shortest sufficient route"* is the operator-UX dual of charter §3.1's *"explicit state transitions"* + *"explicit user actions"* invariants); low for transferability (the UXYS README has not been read; the underlying prompt logic is unknown). |
| 4 | **Conflict** | **Partial: charter §3.4 territory.** UXYS is described as a *"skill for AI agents"* — the framing suggests AI surface integration. Charter §3.4 explicitly rules out customer-facing AI; owner-facing AI is allowed with observable evidence. UXYS is a *static-analysis skill*, not a customer-facing surface — so the conflict is **deferred, not blocking**. **PASS** (charter §3.4 decision deferred to v2). |
| 5 | **Outcome, appetite, scope** | v2 operator-UX architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document the 1-line description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (the description is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-09-muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route-HANDOFF.md` and `features/164-muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 operator-UX moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an operator-UX surface, a user-intent model, or a smallest-sufficient-action-set derivation query):

- `app/web/waiter_ui.py` — possibly redesign the waiter web UI for intent-first posture (depends on the v2 change).
- `app/bot/cook.py` — possibly redesign the cook Telegram bot for shortest-sufficient-route posture (depends on the v2 change).
- `app/ux/audit.py` — possibly add (depends on the v2 change; would integrate the UXYS skill as a static-analysis tool).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/164-muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route.md` exists and is read back by the parent.
- [ ] `specs/2026-09-09-muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The UXYS description is quoted verbatim from GitHub API.
- [ ] The *"shortest sufficient route"* primitive is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an operator-UX surface, a user-intent model, or a smallest-sufficient-action-set derivation query lands):**
- [ ] The PR is read back by the parent.
- [ ] The *"shortest sufficient route"* primitive is evaluated against the PR's changes: does the change expose the smallest sufficient action set at every moment? Does the change anchor on operator intent (not application features)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; restore the original waiter web UI + cook Telegram bot.
- Migration cost: depends on the v2 change; the *"shortest sufficient route"* redesign is a *UI surface change*, not a schema change.
- Retained data: no data retention concern; the UI redesign is purely presentational.

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
| Feature ID | 164 |
| Slug | `muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route` |
| Bucket | v2 operator-UX architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/web/waiter_ui.py` (possibly) + `app/bot/cook.py` (possibly) + `app/ux/audit.py` (possibly) |
| Trigger condition | First v2 PR that adds an operator-UX surface, a user-intent model, or a smallest-sufficient-action-set derivation query |
| Verification protocol | Does the change expose the smallest sufficient action set at every moment? Does it anchor on operator intent (not application features)? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-226 (Brainstorm 2026-09-09 — daily) |
| Linear sub-issue | HMM-229 (Feature 164 — muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route, Backlog, Feature label) |
| Lead source | GitHub `Muredsa/UXYS` (MIT, 1★, pushed 2026-09-04T17:08Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds an operator-UX surface, a user-intent model, or a smallest-sufficient-action-set derivation query lands): the external agent must mirror back the frozen contract (per §6 above) AND the operator must confirm the *"shortest sufficient route"* primitive is the right design discipline AND a charter §3.4 decision must be made (no customer-facing AI; AI may assist owner/staff with observable evidence and a non-AI fallback).

## 9. Verification log

*(Empty today. The first v2 surface that adds an operator-UX surface, a user-intent model, or a smallest-sufficient-action-set derivation query will append a row here with: PR number, the *"shortest sufficient route"* primitive evaluated, the evaluation result, and the operator's sign-off.)*