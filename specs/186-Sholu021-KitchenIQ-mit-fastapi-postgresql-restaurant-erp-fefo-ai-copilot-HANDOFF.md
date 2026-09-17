# Spec 186 — `Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot` (HANDOFF)

**Source feature:** `features/186-Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot.md`
**Parent research issue:** HMM-266 (Research 2026-09-17 — daily)
**Linear sub-issue:** HMM-268
**Filed:** 2026-09-17 by the LE31 daily-research cron (Pick B of Daily Research 2026-09-17)

---

## Active feature path

- **Repo:** `dorinaababii/le31_mmm3_research.git` (working dir: `/opt/data/le31_mmm3_research_work/`)
- **Feature spec file:** `features/186-Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot.md`
- **This HANDOFF file:** `specs/186-Sholu021-KitchenIQ-mit-fastapi-postgresql-restaurant-erp-fefo-ai-copilot-HANDOFF.md`

## Seven-check gate verdict

| # | Check | Status |
|---|---|---|
| 1 | Goal stated | PASS (v2 architecture-reference observation; closest direct LE31-stack-shape match of 2026-09-17) |
| 2 | Evidence / JTBD stated | PASS (GitHub API topic set is direct: fastapi+postgresql+sqlalchemy+python+restaurant) |
| 3 | Scope + Out-of-scope stated | PASS (vocabulary-only artifact; no code change; no library; no new dependency; two caveats acknowledged) |
| 4 | User flow described | PASS (no user-visible flow today; the v2 trigger is the introduction of an external-audit-trail surface that needs an in-domain FastAPI+Postgres restaurant-ERP architectural reference) |
| 5 | Data model described | PASS (no data model change today; the caveats gate any future v2 reference usage) |
| 6 | Dependencies + failure-recovery + DoD | PASS (file-inspection dependency; ripgrep dependency; no recovery needed; DoD = feature spec exists + HANDOFF exists + Linear sub-issue created + parent research issue exists + push to main) |
| 7 | Open questions listed | PASS (3 open questions, all related to the two caveats + a deeper scope-comparison note) |

**Gate verdict:** PASS — v2 architecture-reference defer (parking-lot). No build today.

## Files to touch

**None today.** This is a vocabulary-only artifact. The coding agent does NOT need to touch any files in `le31_mmm3_research` today.

**Read-only inspection tasks** (not file modifications):

1. The coding agent MAY inspect the `KitchenIQ` GitHub repository (`Sholu021/KitchenIQ`) to determine:
   - Is the FastAPI backend decoupled from the NextJS+React frontend? (Read the `app/` directory structure.)
   - Is the `openai` integration staff-tooling (charter §3.4 permits) or customer-facing (charter §3.4 forbids)? (Ripgrep the AI-touching code paths.)

These are **read-only** inspections — they do NOT modify any files in `le31_mmm3_research`.

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md`, the coding agent should:

1. **Confirm no build is required today.** This is a defer/parking-lot artifact; the only verification is that the feature spec exists, the HANDOFF exists, and the Linear sub-issue is created.
2. **If the future v2 trigger condition fires**: read the `KitchenIQ` GitHub repository on GitHub (`Sholu021/KitchenIQ`) and inspect the `app/` directory structure + AI-touching code paths to verify the two caveats.
3. **Read the companion artifacts** (features 89, 106, 158) to understand the prior in-domain FastAPI+restaurant peer observations.
4. **Pre-merge review.** Per `pre-merge-review/SKILL.md`, this is a documentation-only artifact (no code change), so the pre-merge review is light.
5. **Push to main.** `git push origin main`.
6. **Update Linear sub-issue HMM-268** to `Done` when the artifact is filed (today's cron run does this automatically).

## Rollback path

**None needed.** This is a documentation-only artifact (vocabulary observation + two-caveats gate). There is no code change to roll back.

If the upstream `KitchenIQ` repository disappears or its license changes, the next pass would file a new observation that supersedes this one (or updates the existing record). The artifacts are not load-bearing for any LE31 v1 surface.

## Mandatory LE31 skill list

The coding agent MUST load and apply these skills before starting:

1. `le31-conventions` — for the LE31 charter §3.1, §3.2, §3.4 invariants that apply to v2 architecture-reference deferrals.
2. `le31-v1-feature-pattern` — for the canonical v1 feature contract shape (this HANDOFF follows that shape; the agent should re-read the spec to confirm).
3. `development` — for the spec → plan → tasks → implement pipeline (no implementation today, but the skill list applies for any future v2 surface that builds on this artifact).
4. `pre-merge-review` — for the non-author-independent-review gate (light, since no code change today).
5. `verify-before-fixing` — for the discipline of "this is a defer/parking-lot artifact; no implementation is needed; verify the artifact is correctly filed rather than starting to fix things."

## Notes for the coding agent

- **No build today.** This is a defer/parking-lot artifact. The coding agent should NOT touch any files in `le31_mmm3_research` today beyond the cron-generated files.
- **The two caveats are the gate to any future v2 reference usage.** The two next-step questions (FastAPI/NextJS decoupling + `openai` §3.4 ripgrep) are required for any future v2 reference usage. Until both are answered, `KitchenIQ` is vocabulary-only.
- **MIT permissive license confirmed** — charter §3.2 ✓ (license tag: MIT, GitHub API response confirms). No AGPL/SSPL contamination concern at the top-level repository license.
- **`AI-powered` description + `openai` topic** are the §3.4 red flags. The coding agent should ripgrep for `openai`, `customer-facing`, `chatbot` strings before any adoption.
- **`nextjs` + `react` topics** are the frontend stack-mismatch red flags. The coding agent should inspect the `app/` directory structure to determine if the FastAPI backend is decoupled (architectural reference useful) or tightly coupled (architectural reference not useful for LE31).
- **The 1:1 mapping table** in the feature spec (11 topics vs LE31 stack match status) is the at-a-glance gate summary. The coding agent should re-read the table before any adoption decision.
- **Future v2 trigger condition** = the introduction of an external-audit-trail primitive OR the introduction of a multi-restaurant operation that needs an in-domain FastAPI+Postgres restaurant-ERP architectural reference. When that trigger fires, the v2 surface that addresses it should reference feature 186 + features 89, 106, 158 (the in-domain FastAPI+restaurant peer cluster).