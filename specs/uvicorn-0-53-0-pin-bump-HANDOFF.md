# Spec 179 — `uvicorn-0-53-0-pin-bump` (HANDOFF)

**Source feature:** `features/179-uvicorn-0-53-0-pin-bump.md`
**Parent research issue:** HMM-241
**Linear sub-issue:** HMM-242
**Filed:** 2026-09-15 by the LE31 daily-research cron

---

## Active feature path

- **Repo:** `dorinaababii/le31_mmm3_research.git` (working dir: `/opt/data/le31_mmm3_research_work/`)
- **Feature spec file:** `features/179-uvicorn-0-53-0-pin-bump.md`
- **This HANDOFF file:** `specs/uvicorn-0-53-0-pin-bump-HANDOFF.md`

## Seven-check gate verdict

| # | Check | Status |
|---|---|---|
| 1 | Goal stated | PASS |
| 2 | Evidence / JTBD stated | PASS (26-day stagnation of uvicorn stable releases; first new minor version in 26 days; pure stack maintenance) |
| 3 | Scope + Out-of-scope stated | PASS (pin-bump only; no behavior change; no other pin-bumps today) |
| 4 | User flow described | PASS (server-launch + `/health` + Telegram long-polling smoke) |
| 5 | Data model described | PASS (no data model change) |
| 6 | Dependencies + failure-recovery + DoD | PASS (read release notes first; rollback = revert commit; DoD = tests pass + smoke passes + push to main) |
| 7 | Open questions listed | PASS (dependency-file format; deploy supervisor; CI matrix coverage) |

**Gate verdict:** PASS — v1 build candidate.

## Files to touch

1. **`pyproject.toml`** OR **`requirements.txt`** (confirm via `le31-conventions/SKILL.md` and `project-repo-hygiene/SKILL.md`):
   - Change: `uvicorn==0.52.4` → `uvicorn==0.53.0`
2. **`uv.lock`** OR **`requirements.txt.lock`** (confirm format):
   - Regenerate via `uv lock --upgrade uvicorn` (if uv) or `pip-compile` (if pip-tools).
3. **`CHANGELOG.md`** (if LE31 maintains one):
   - Add an entry under the next version heading: `Bump uvicorn 0.52.4 → 0.53.0 (PyPI release 2026-09-14, first uvicorn stable in 26 days).`

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md`, the coding agent should:

1. **Read the release notes first.** Visit `https://github.com/encode/uvicorn/releases/tag/0.53.0` and review the changelog. Document any breaking changes in the PR description.
2. **Run the test suite.** `pytest` (or whatever LE31's test runner is). All tests must pass.
3. **Run the smoke test.** Launch the server, hit `/health`, confirm 200. Send a test Telegram long-polling request (or simulate one), confirm no error.
4. **Confirm no behavior change.** The diff should be 3–4 lines (dependency file + lock file + maybe a CHANGELOG entry). Anything larger is suspicious — investigate.
5. **Pre-merge review.** Per `pre-merge-review/SKILL.md`, this is a non-author-coded change to a non-trivial layer (ASGI runtime); it MUST pass independent review before merge.
6. **Push to main.** `git push origin main`.
7. **Update Linear sub-issue HMM-242** to `Done`.

## Rollback path

1. **Git revert the commit.** `git revert <commit-sha>` produces a new commit that reverts the pin-bump.
2. **Push the revert.** `git push origin main`.
3. **Redeploy.** The deploy supervisor picks up the reverted code.
4. **Verify.** Confirm the server is back on `uvicorn 0.52.4` and the smoke test passes.
5. **Document in Linear sub-issue.** Comment on HMM-242 with the revert commit SHA and the reason for rollback.

The rollback is **low-risk**: reverting the pin-bump restores the exact prior state (`uvicorn==0.52.4`) and there is no data migration / forward-only state involved.

## Mandatory LE31 skill list

The coding agent MUST load and apply these skills before starting:

1. `le31-conventions` — for the dependency-file format, CI commands, deploy process, and test suite location.
2. `le31-v1-feature-pattern` — for the canonical v1 feature contract shape (this HANDOFF follows that shape; the agent should re-read the spec to confirm).
3. `development` — for the spec → plan → tasks → implement pipeline.
4. `pre-merge-review` — for the non-author-independent-review gate.
5. `python-debugpy` — for debugging if the test suite reveals a uvicorn-related regression.
6. `test-driven-development` — for the test-first discipline (the test suite must pass; if a regression is found, write a regression test first).
7. `verify-before-fixing` — for the discipline of "the diff is 3–4 lines; if it's larger, something is wrong; investigate before pushing."

## Notes for the coding agent

- **The pin-bump target is `uvicorn==0.53.0`. Do not bump to `0.53.1` or any later version today.** If a quick-burst patch follow-up appears in the next 7 days (e.g., `uvicorn 0.53.1` within 24–48h), file a follow-up pick; do not pre-bump.
- **The `SQLAlchemy 2.0.53` pin-bump candidate (released 2026-09-14T22:39:47Z) is queued behind this pick.** Do NOT bump SQLAlchemy in the same commit. Two stack-pin-bumps in one commit dilutes the diff and obscures the cause if anything breaks.
- **Do NOT touch any other pin in this commit.** Pin-bumps should be one-at-a-time for clean rollback.
- **The release notes are the gate.** If you cannot reach `https://github.com/encode/uvicorn/releases/tag/0.53.0`, the release notes are blank, or there is a documented breaking change that affects LE31's use of uvicorn — STOP and report the blocker on the Linear sub-issue rather than pushing a partial fix.
