# Spec 185 — `fredhead88-do-it-v2-merge-guard-derives-state-watch-list-update` (HANDOFF)

**Source feature:** `features/185-fredhead88-do-it-v2-merge-guard-derives-state-watch-list-update.md`
**Parent research issue:** HMM-266 (Research 2026-09-17 — daily)
**Linear sub-issue:** HMM-267
**Filed:** 2026-09-17 by the LE31 daily-research cron (Pick A of Daily Research 2026-09-17)

---

## Active feature path

- **Repo:** `dorinaababii/le31_mmm3_research.git` (working dir: `/opt/data/le31_mmm3_research_work/`)
- **Feature spec file:** `features/185-fredhead88-do-it-v2-merge-guard-derives-state-watch-list-update.md`
- **This HANDOFF file:** `specs/185-fredhead88-do-it-v2-merge-guard-derives-state-watch-list-update-HANDOFF.md`
- **Parent feature:** `features/182-fredhead88-do-it-v2-merge-guard-derives-state.md` (the existing feature 182 to which this is a watch-list update)

## Seven-check gate verdict

| # | Check | Status |
|---|---|---|
| 1 | Goal stated | PASS (carry-over from feature 182) |
| 2 | Evidence / JTBD stated | PASS (carry-over from feature 182 + NEW 2026-09-17 NEW PUSH observation) |
| 3 | Scope + Out-of-scope stated | PASS (vocabulary-only artifact; no code change; no library; no new dependency) |
| 4 | User flow described | PASS (no user-visible flow today; the v2 trigger is the introduction of a second stakeholder) |
| 5 | Data model described | PASS (no data model change today; the future v2 schema migration is described) |
| 6 | Dependencies + failure-recovery + DoD | PASS (relicense-clearance dependency; no recovery needed; DoD = feature spec exists + HANDOFF exists + Linear sub-issue created + parent research issue exists + push to main) |
| 7 | Open questions listed | PASS (3 open questions, all related to license-clearance + future v2 schema) |

**Gate verdict:** PASS — v2 architecture-reference defer (parking-lot). No build today.

## Files to touch

**None today.** This is a vocabulary-only artifact. The coding agent does NOT need to touch any files in `le31_mmm3_research` today.

If the future v2 trigger condition fires (first v2 surface that introduces a second stakeholder), the files to touch would be:

1. `features/<NN>-<v2-surface>.md` — the new v2 surface feature spec, which would reference this feature 185 as a v2 architecture reference.
2. `app/audit_logs.py` (hypothetical v2 file) — the `audit_logs` schema would gain an optional `chain_position` BIGSERIAL column (semantic alias for `id`).
3. `app/middleware.py` (hypothetical v2 file) — a guard-layer abstraction that wraps route handlers in middleware and enforces the merge-execution discipline.

**No files to touch today.**

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md`, the coding agent should:

1. **Confirm no build is required today.** This is a defer/parking-lot artifact; the only verification is that the feature spec exists, the HANDOFF exists, and the Linear sub-issue is created.
2. **If the future v2 trigger condition fires**: read the do-it-v2 repository on GitHub (`fredhead88/do-it-v2`) and inspect the merge-guard implementation to understand the primitive before designing the v2 surface.
3. **Read the `features/182-fredhead88-do-it-v2-merge-guard-derives-state.md` feature spec** (the parent feature to which this is a watch-list update) to understand the full context.
4. **Pre-merge review.** Per `pre-merge-review/SKILL.md`, this is a documentation-only artifact (no code change), so the pre-merge review is light.
5. **Push to main.** `git push origin main`.
6. **Update Linear sub-issue HMM-267** to `Done` when the watch-list update is filed (today's cron run does this automatically).

## Rollback path

**None needed.** This is a documentation-only artifact (vocabulary observation + Cross-section reference). There is no code change to roll back. The watch-list update simply adds to the existing feature 182 record; if the maintenance activity stops or the upstream repository disappears, the next pass would file a new observation that supersedes this one (or updates the existing record).

If the parent feature 182 is retired for any reason, this watch-list update would also be retired (the two are linked — feature 185 is explicitly a watch-list update to feature 182).

## Mandatory LE31 skill list

The coding agent MUST load and apply these skills before starting:

1. `le31-conventions` — for the LE31 charter §3.1, §3.2, §3.4 invariants that apply to v2 architecture-reference deferrals.
2. `le31-v1-feature-pattern` — for the canonical v1 feature contract shape (this HANDOFF follows that shape; the agent should re-read the spec to confirm).
3. `development` — for the spec → plan → tasks → implement pipeline (no implementation today, but the skill list applies for any future v2 surface that builds on this artifact).
4. `pre-merge-review` — for the non-author-independent-review gate (light, since no code change today).
5. `verify-before-fixing` — for the discipline of "this is a defer/parking-lot artifact; no implementation is needed; verify the artifact is correctly filed rather than starting to fix things."

## Notes for the coding agent

- **No build today.** This is a defer/parking-lot artifact. The coding agent should NOT touch any files in `le31_mmm3_research` today beyond the cron-generated files.
- **The artifact is a watch-list update to feature 182, not a new feature.** If the coding agent is reviewing this artifact, they should also read feature 182 to understand the full context.
- **The 2026-09-17 NEW PUSH observation** is the data point that justifies filing this artifact. The maintenance activity has resumed after the 09-16 filing day (the repo grew from 896 KB to 1000 KB in 24h).
- **License clearance is OPEN.** The do-it-v2 repository has `license: null` in the GitHub API response (= no LICENSE file detected). The predecessor `fredhead88/do-it` is MIT permissive. Adoption of do-it-v2 would require relicense. Owner decision required before any code adoption.
- **The two net-new primitives are carry-overs from feature 182:** (1) "merge guard that performs the merge instead of modelling it" — the *derivation mechanism*; (2) "Append-only events, nothing stamped" — the *event-time vs chain-time* discipline. Both are documented in feature 182 and feature 185.
- **Future v2 trigger condition** = the introduction of a second stakeholder (accountant, tax authority, regulator) who needs to ask "when was this row committed?". When that trigger fires, the v2 surface that addresses it should reference feature 185 + feature 182 + feature 148 (coxswain-graphs) as the v2 architecture-reference triple.