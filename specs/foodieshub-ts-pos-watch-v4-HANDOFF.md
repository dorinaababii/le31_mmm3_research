# foodieshub-ts-pos-watch-v4 — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/83-foodieshub-ts-pos-watch-v4.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `83`
- Slug: `foodieshub-ts-pos-watch-v4`
- Contract file: `features/83-foodieshub-ts-pos-watch-v4.md`
- Bucket: **v2 utility (watch-list)** — research-only, defer
- Linear parent: `HMM-111` (Research 2026-08-20 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window across the 4-pass series via direct
GitHub repo API GETs;
`api.github.com/repos/helloman3/foodieshub`).

**Confidence:** **high** for JTBD pull (restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management = exactly
the LE31 feature surface from features 02/03/09/14), **zero** for
stack match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
helloman3 is TypeScript + React PWA + 0-fork single-author repo).

**Decision: watch-list defer.** The 4-day stagnation phase is the
longest observed for any LE31 watch-list repo (longnick plateau was
3-4 days before the −1★/24h decay started; foodieshub has been at 4★
for 4 days straight). The watch continues; the README should be read
on 2026-08-21 to assess the multi-device sync mechanism.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-20).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/83-foodieshub-ts-pos-watch-v4.md   # NEW (this artifact)
specs/foodieshub-ts-pos-watch-v4-HANDOFF.md # NEW (this file)
INDEX.md                                    # EDIT: append one row to "Active feature pipeline" table
```

Zero source-code edits. Zero new pip dependencies. Zero migrations.
Zero new config keys. Zero new schema changes. The slice is a
research-note artifact only.

## Verification protocol

After the artifact ships:

1. **Read back** `features/83-foodieshub-ts-pos-watch-v4.md` and
   confirm it matches the daily-research report's
   "foodieshub-ts-pos-watch-v4" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-20), pick slug
   (`foodieshub-ts-pos-watch-v4`), feature path
   (`features/83-foodieshub-ts-pos-watch-v4.md`), and Linear
   sub-issue ID.
3. **Re-check the foodieshub star count on 2026-08-21** via direct
   GitHub repo API GET (`api.github.com/repos/helloman3/foodieshub`)
   and confirm whether the 4★ stagnation breaks in either direction
   (growth or decay). Read the foodieshub README in full on the
   2026-08-21 pass to assess the multi-device sync mechanism.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID
`fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`
(label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 83 — foodieshub-ts-pos-watch-v4`.
- Body: the contract from
  `features/83-foodieshub-ts-pos-watch-v4.md` (or a short summary +
  the file path).
- Parent: `HMM-111` (Research 2026-08-20 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/83-foodieshub-ts-pos-watch-v4.md` and this HANDOFF.md.
Remove the corresponding row from `INDEX.md`. No code changes to
revert. No data migration to revert.

## Why this matters (for the coding agent)

`helloman3/foodieshub` is the **closest direct JTBD pull** in window
across the recent 4-pass daily-research series: restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management = exactly
the LE31 feature surface from features 02/03/09/14. The description
maps directly to the LE31 user surface.

The **4-day stagnation** at 4★ is the longest stagnation phase
observed for any LE31 watch-list repo. The longnick plateau was 3-4
days before the −1★/24h decay started; foodieshub has been at 4★ for
4 days straight with no decay but also no growth. The watch-list
captures this trajectory for future passes to reference.

**Risk of NOT tracking the 4-day stagnation**: if the watch
eventually breaks (growth or decay), the artifact captures the
baseline for comparison.

**Risk of overreacting to the 4-day stagnation**: the stagnation is
consistent with a stable plateau (a single-author repo with 0 forks
can stay at 4★ indefinitely). The research-note artifact should not
be used to recommend action without the next 7-day observation
period.

**Net: continue the watch; re-check on 2026-08-21; the watch remains
active with the target band of 5★+ in 24h or further decay.**
