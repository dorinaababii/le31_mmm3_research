# day-part-menu-margin-surface — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/75-day-part-menu-margin-surface.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `75`
- Slug: `day-part-menu-margin-surface`
- Contract file: `features/75-day-part-menu-margin-surface.md`
- Bucket: **v2 owner-pains (extends feature 39)** — parking-lot
- Linear parent: `Brainstorm 2026-08-16 — daily` (TBD; created in this cron)
- Linear sub-issue: **TBD** (create as a draft parking-lot record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**inferred** (owner-KPI pattern from two 0★ repos — `Hamuda55/restaurant-ops-dashboard` 548 bytes README-only no license + `ifrederico/forkluck` AGPL — no observed pain).

**Confidence:** **low** for the JTBD shape (the pattern is well-established in the broader ecosystem), **zero** for the LE31-specific pain (no observed pain, no HN/OpenAlex validating peer, no license-acceptable peer).

**Decision: parking-lot.** The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. Circuit breaker: delete this file + the corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules; even though this is parking-lot, the slicing discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-16).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/75-day-part-menu-margin-surface.md   # NEW (this artifact)
specs/day-part-menu-margin-surface-HANDOFF.md # NEW (this file)
INDEX.md                                       # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys. Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/75-day-part-menu-margin-surface.md` and confirm it matches the brainstorm report's "75-day-part-menu-margin-surface" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-16), pick slug (`day-part-menu-margin-surface`), feature path (`features/75-day-part-menu-margin-surface.md`), and Linear sub-issue ID.
3. **On a future daily-research pass**: re-query the GitHub `restaurant created:>2026-07-17 language:python` cluster and confirm a day-part-analytics peer with ≥10 stars and a non-548-byte / non-no-license license has emerged. If so, the parking-lot re-activates (re-evaluate the gate and consider un-park).

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2 owner-pains` with label `Feature`. The Feature label ID is `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb` (workspace-wide as of 2026-08-16).

- Title: `Feature 75 — day-part × menu-margin owner drill-in surface`.
- Body: the contract from `features/75-day-part-menu-margin-surface.md` (or a short summary + the file path).
- Parent: `Brainstorm 2026-08-16 — daily` (the Linear index issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/75-day-part-menu-margin-surface.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The owner pain "which dishes make margin at which hours?" is a **real LE31 owner problem** (small restaurants often retire high-revenue but low-margin dishes because the labor cost swings at dinner dominate). The pattern is mature in the broader ecosystem (Square POS + 7shifts + Toast all ship day-part analytics). **The blocker is not pattern novelty; the blocker is observed pain + prerequisite availability.**

**Risk of NOT tracking**: the day-part question will surface after the owner reviews a quarterly menu-margin report. If the parking-lot is not already in place when that happens, the build will be rushed. The watch exists to ensure the pattern is already-evaluated when the trigger condition arrives.

**Risk of over-tracking**: feature 74 is not yet shipped. The parking-lot artifact is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the feature under "parking-lot until feature 74 ships to production." Re-evaluate when the prerequisite lands.
