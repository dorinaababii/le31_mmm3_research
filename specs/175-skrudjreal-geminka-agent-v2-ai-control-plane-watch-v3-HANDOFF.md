# 175 — skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3 HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/175-skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3.md` (defer artifact; **no code today**).

Bucket: **v2-AI control-plane (watch-list)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants *AI-assisted owner-side workflows* (e.g., AI-summarised daily recap, AI-assisted stock replenishment suggestions, AI-assisted menu engineering), the owner wants *a cross-section reference for the staff-only AI control-plane primitive*, but struggles because *v1 has no AI surface and charter §3.4 forbids customer-facing AI*, so that *v2 can offer staff-only AI assistance without violating §3.4*." **PASS** (zero-pain today; v1 has no AI surface; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read 0.8 KB push-idle-history description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the push-idle-broken observation (parent-verified by direct-repo GET at `/tmp/le31-daily-2026-09-14/gh_parent_repo_SkrudjReal__geminka-agent.json`). Charter §3.2 MIT permissive; §3.4 owner/staff-assist compatible. **PASS**. |
| 4 | **Conflict** | None. The push-idle-broken signal is maintainer-still-active evidence; it does not violate §3.4 (Gemini is staff-only, not customer-facing). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI control-plane (watch-list); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 0.8 KB push-idle-history + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (push-idle-broken is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/175-skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3-HANDOFF.md` and `features/175-skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI surface).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a staff-only AI control-plane surface):

- `app/ai/agent.py` — possibly add a Gemini-powered agent (depends on the v2 change; requires owner decision on Gemini API choice).
- `app/ai/control_plane.py` — possibly add a control-plane primitive (depends on the v2 change).
- `app/ai/non_ai_fallback.py` — possibly add a non-AI fallback (charter §3.4 requires observable evidence + non-AI fallback).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/175-skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3.md` exists and is read back by the parent.
- [ ] `specs/175-skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The push-idle-broken history is documented (6-day push-idle broken by 2026-09-12T20:30:46Z).
- [ ] The Gemini-as-agent-brain pattern is documented.
- [ ] The charter §3.4 owner/staff-assist compatibility is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a staff-only AI control-plane surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `SkrudjReal/geminka-agent` repo is fetched fresh and the push-idle-history is re-evaluated.
- [ ] The cross-section comparison between `SkrudjReal/geminka-agent` and the LE31 v2 AI surface is documented in the PR's Linear issue.
- [ ] The charter §3.4 owner/staff-assist compatibility is re-verified.
- [ ] The comparison result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new Gemini-powered agent; remove the new control-plane primitive; remove the new non-AI fallback; restore the original v1 surface (no AI).
- Migration cost: depends on the v2 change; the AI surface is additive on top of v1 (charter §3.4 owner/staff-assist compatible; no v1 surface change required).
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
| Feature ID | 172 |
| Slug | `skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3` |
| Bucket | v2-AI control-plane (watch-list, parking-lot defer) |
| Parent research issue | HMM-245 (Research 2026-09-14 — daily) |
| Linear sub-issue | HMM-248 (Feature) — to be created on the next sub-issue step |
| Status today | defer (parking-lot) |
| No code today | yes |
| Verifiability today | feature file + HANDOFF file + INDEX.md row + parent research issue |
| Trigger condition (future v2) | first v2 PR that adds a staff-only AI control-plane surface |
| Disable path | delete `features/175-...md` + `specs/175-...-HANDOFF.md` |
| Migration cost | additive (depends on v2 change) |
| Retained data | none |
| Parent issue | HMM-245 (parent research issue; le31 Research) |
| Report path | /opt/data/le31-daily-research-2026-09-14.md |
| Raw fetches path | /tmp/le31-daily-2026-09-14/ |
