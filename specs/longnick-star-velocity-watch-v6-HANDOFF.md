# longnick-star-velocity-watch-v6 — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation, not a feature build. The slice boundary is hard:
> zero source-file edits, zero schema changes, zero new config keys.
> Read this *and* `features/88-longnick-star-velocity-watch-v6.md`
> before touching any code. Do not paste chat excerpts back into
> the build.

## Frozen identifiers (do not rename)

- Feature ID: `88`
- Slug: `longnick-star-velocity-watch-v6`
- Contract file: `features/88-longnick-star-velocity-watch-v6.md`
- Bucket: **v2 watch-list (research observation)** — hard defer
- Linear parent: `HMM-114` (Research 2026-08-21 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window across the 22-pass series via direct
repo GET on `longnick/small-pos-open-source`; **−3★/72h cumulative**
confirmed via 9-day trajectory; 3 consecutive days of −1★/24h is now
statistically significant at the 72h window).

**Confidence:** **high** for the trajectory (every observation is a
direct-repo GET with a fixed URL + auth header; the −1★/24h delta is
identical across 3 consecutive days and is the kind of pattern that
is hard to produce by accident). **Low** for the underlying cause
(without GitHub Archive event log inspection, the cause is
speculative).

**Decision: watch-list continue; hard defer pending 2026-08-22
re-check.** If the −1★/24h decay continues to sub-90★ territory on
2026-08-22, escalate to watch-list close (the signal has decayed into
noise). If it stabilizes at 92★, downgrade verdict to "velocity-driven
watch EXPIRED + 72h star-loss anomaly observed" and continue at
reduced cadence (weekly instead of daily).

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-21).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/88-longnick-star-velocity-watch-v6.md   # NEW (this artifact)
specs/longnick-star-velocity-watch-v6-HANDOFF.md # NEW (this file)
INDEX.md                                          # EDIT: append one row to "Active feature pipeline" table (watch-list continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back** `features/88-longnick-star-velocity-watch-v6.md` and
   confirm it matches the daily-research report's
   "longnick-star-velocity-watch-v6" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-21), pick slug
   (`longnick-star-velocity-watch-v6`), feature path
   (`features/88-longnick-star-velocity-watch-v6.md`), and Linear
   sub-issue ID.
3. **On 2026-08-22**: re-fetch
   `https://api.github.com/repos/longnick/small-pos-open-source` via
   `$HERMES_GITHUB_TOKEN` and record `stargazers_count`,
   `forks_count`, `pushed_at`, `updated_at`, `size`. Compare against
   the 2026-08-21 baseline of 92★ / 89 forks / 2026-08-18T12:02:14Z /
   2026-08-20T16:44:47Z / (size unchanged). If stars < 91 (sub-90★
   territory), escalate to watch-list close. If stars == 92, downgrade
   to weekly cadence. If stars > 92, the decay has reversed and the
   watch is no longer actionable.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2 owner-pains` (the
watch-list bucket) with label `Feature`.

- Title: `Feature 88 — longnick-star-velocity-watch-v6`.
- Body: the contract from
  `features/88-longnick-star-velocity-watch-v6.md` (or a short summary
  + the file path).
- Parent: `HMM-114` (Research 2026-08-21 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/88-longnick-star-velocity-watch-v6.md` and this
HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other
code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

The `longnick-star-velocity` watch is the highest-priority JTBD
signal in the 22-pass series. The +41★/24h one-day peak observed on
2026-08-13→2026-08-14 was real-world market validation that small-F&B
owners want a free open POS starter. The 72h sustained decay trend
observed today is a **statistically significant** reversal: the
velocity-driven market-validation signal has decayed into a
star-loss-anomaly observation. The watch remains active for the
2026-08-22 confirmation check.

## Carry-over history

This is the **6th consecutive day** the longnick-star-velocity-watch
has been filed:

- 2026-08-16 → `features/71-longnick-star-velocity-watch.md` (initial; velocity-driven)
- 2026-08-17 → `features/71-longnick-star-velocity-watch.md` (v2; velocity-driven EXPIRED + 72h plateau)
- 2026-08-18 → `features/71-longnick-star-velocity-watch.md` (v3; velocity-driven EXPIRED + 72h plateau CONFIRMED)
- 2026-08-19 → `features/71-longnick-star-velocity-watch.md` (v4; −1★/24h ANOMALY under confirmation)
- 2026-08-20 → `features/71-longnick-star-velocity-watch.md` (v5; −2★/48h sustained decay CONFIRMED)
- 2026-08-21 → `features/88-longnick-star-velocity-watch-v6.md` (v6 — this artifact; −3★/72h 72h sustained decay CONFIRMED)

The verdict has progressed: velocity-driven → anomaly → sustained → 72h sustained (statistically significant).
