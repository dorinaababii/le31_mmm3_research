# longnick-star-velocity-watch-v5 — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/71-longnick-star-velocity-watch.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `71`
- Slug: `longnick-star-velocity-watch-v5`
- Contract file: `features/71-longnick-star-velocity-watch.md`
- Bucket: **v2 utility (watch-list)** — research-only, defer
- Linear parent: `HMM-111` (Research 2026-08-20 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window across the 21-pass series via direct
GitHub repo API GETs;
`api.github.com/repos/longnick/small-pos-open-source`).

**Confidence:** **high** for JTBD pull ("small café POS" — exactly
the LE31 user surface from features 02/03/05), **zero** for stack
match (FastAPI �, SQLModel ✗, aiogram ✗, Postgres ✗;
`longnick/small-pos-open-source` is TypeScript + React 19 + Vite 8).

**Decision: watch-list defer.** The watch-list status moves from
"anomaly under confirmation" (yesterday's verdict) to "real
star-loss trend" (today's verdict). **Two consecutive days of
−1★/24h is now statistically significant; GitHub star counts do not
normally decrease.** The watch remains active with the revised target
window of 95★ ± 5 sustained over the next 7 days. **Re-check on
2026-08-21 to confirm.**

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
features/71-longnick-star-velocity-watch.md   # UPDATED v5 (this artifact)
specs/longnick-star-velocity-watch-HANDOFF.md # UPDATED v5 (this file)
INDEX.md                                      # EDIT: append one row to "Active feature pipeline" table
```

Zero source-code edits. Zero new pip dependencies. Zero migrations.
Zero new config keys. Zero new schema changes. The slice is a
research-note artifact only.

## Verification protocol

After the artifact ships:

1. **Read back** `features/71-longnick-star-velocity-watch.md` and
   confirm it matches the daily-research report's
   "longnick-star-velocity-watch-v5" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-20), pick slug
   (`longnick-star-velocity-watch-v5`), feature path
   (`features/71-longnick-star-velocity-watch.md`), and Linear
   sub-issue ID.
3. **Re-check the longnick star count on 2026-08-21** via direct
   GitHub repo API GET (`api.github.com/repos/longnick/small-pos-open-source`)
   and confirm whether the −1★/24h decay stabilizes (returns to 94★
   or holds at 93★), accelerates (sub-90★ territory — move to
   parking-lot), or reverses (back to growth).

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID
`fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`
(label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 71 — longnick-star-velocity-watch-v5`.
- Body: the contract from
  `features/71-longnick-star-velocity-watch.md` (or a short summary +
  the file path).
- Parent: `HMM-111` (Research 2026-08-20 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete the v5 row from `features/71-longnick-star-velocity-watch.md`
(revert to v4 from 2026-08-19). Remove the corresponding row from
`INDEX.md`. No code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

`longnick/small-pos-open-source` was the highest-star-velocity
in-window GitHub peer across the 15-pass series (+41★/24h peak on
2026-08-13→2026-08-14) and was a real-world market validation that
small-F&B owners want a free open POS starter. The +41★/24h peak was
a one-day phenomenon; the subsequent 8-day trajectory is now **+5.4★/24h
average** (decayed from the peak), with **−1★/24h sustained for 48h =
−2★/48h cumulative** (NEW finding on 2026-08-20).

The velocity-driven watch has definitively EXPIRED. The +0★/72h
steady-state highlight (2026-08-15 → 2026-08-18) has now been replaced
by the −1★/24h sustained decay trend (2026-08-19 → 2026-08-20). **Two
consecutive days of −1★ is now statistically significant; GitHub star
counts do not normally decrease.**

**Risk of NOT tracking the −1★/24h decay**: if the decay accelerates
to a mass un-star event (sub-90★ territory), the watch would need to
move from "defer (watch expired + sustained decay)" to "defer
(parking-lot — repo no longer in velocity-driven discovery)". The
artifact captures the trajectory for future passes to reference.

**Risk of overreacting to the −1★/24h signal**: the decay could
stabilize at the 93★ floor (within the 90★-100★ band); the
research-note artifact should not be used to recommend action without
the next 7-day observation period.

**Net: continue the watch; re-check on 2026-08-21; the watch remains
active with the revised target window of 95★ ± 5 sustained over the
next 7 days.**
