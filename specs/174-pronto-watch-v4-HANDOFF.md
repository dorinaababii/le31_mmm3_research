# 174 — pronto-watch-v4 HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/174-pronto-watch-v4.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains (watch-list)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to *expand the cook-Telegram-bot surface* (e.g., add multi-language menu support, prep-time SLAs, station-routing, or any other cook-side expansion), the owner wants *a cross-section peer to compare the LE31 cook-bot architecture against*, but struggles because *v1's cook-bot surface is intentionally small (charter §3.4) and there is no ready-made cross-section reference*, so that *v2 can expand the cook-bot surface without re-architecting v1*." **PASS** (zero-pain today; v1's cook-bot is feature 14 and works; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read 0.8 KB floor-trajectory description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the floor-trajectory observation (parent-verified by direct-repo GET at `/tmp/le31-daily-2026-09-14/gh_parent_repo_SGrappelli__pronto.json`). **PASS**. |
| 4 | **Conflict** | None. The 8-day sustained-inflow signal is operator-side-market-pull evidence; it does not violate §3.1, §3.4, or any other charter invariant. **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains (watch-list); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 0.8 KB floor-trajectory + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (8-day floor-trajectory is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/174-pronto-watch-v4-HANDOFF.md` and `features/174-pronto-watch-v4.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 cook-surface expansion).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a cook-Telegram-bot surface expansion, e.g., multi-language menu support, prep-time SLAs, or station-routing):

- `app/cook_bot/handlers.py` — possibly add new aiogram handlers (depends on the v2 change).
- `app/cook_bot/messages.py` — possibly add new message templates (depends on the v2 change).
- `app/state/cook_station_routing.py` — possibly add a station-routing state machine (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/174-pronto-watch-v4.md` exists and is read back by the parent.
- [ ] `specs/174-pronto-watch-v4-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The 8-day floor-trajectory is documented (41→54★ / 19→23⑂).
- [ ] The `updated_at` 2026-09-14T03:51:14Z active metadata movement without code push is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a cook-Telegram-bot surface expansion lands):**
- [ ] The PR is read back by the parent.
- [ ] The `SGrappelli/pronto` repo is fetched fresh and the floor-trajectory is re-evaluated.
- [ ] The cross-section comparison between `SGrappelli/pronto` and the LE31 cook-bot is documented in the PR's Linear issue.
- [ ] The comparison result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new cook-bot handlers; remove the new message templates; remove the new station-routing state machine; restore the original cook-bot surface.
- Migration cost: depends on the v2 change; the cook-bot expansion is additive on top of feature 14 (charter §3.4 compatible; no v1 surface change required).
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
| Feature ID | 171 |
| Slug | `pronto-watch-v4` |
| Bucket | v2 owner-pains (watch-list, parking-lot defer) |
| Parent research issue | HMM-245 (Research 2026-09-14 — daily) |
| Linear sub-issue | HMM-247 (Feature) — to be created on the next sub-issue step |
| Status today | defer (parking-lot) |
| No code today | yes |
| Verifiability today | feature file + HANDOFF file + INDEX.md row + parent research issue |
| Trigger condition (future v2) | first v2 PR that adds a cook-Telegram-bot surface expansion |
| Disable path | delete `features/174-...md` + `specs/174-...-HANDOFF.md` |
| Migration cost | additive (depends on v2 change) |
| Retained data | none |
| Parent issue | HMM-245 (parent research issue; le31 Research) |
| Report path | /opt/data/le31-daily-research-2026-09-14.md |
| Raw fetches path | /tmp/le31-daily-2026-09-14/ |
