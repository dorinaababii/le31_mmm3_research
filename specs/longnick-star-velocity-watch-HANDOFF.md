# longnick-star-velocity-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/71-longnick-star-velocity-watch.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `71`
- Slug: `longnick-star-velocity-watch`
- Contract file: `features/71-longnick-star-velocity-watch.md`
- Bucket: **v2 utility (watch-list)** — defer; watch has expired
- Linear parent: `HMM-85` (Research 2026-08-16 — daily)
- Linear sub-issue: **TBD** (create as a draft watch-list record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (GitHub Search Repositories API across the 17-pass
daily-research series — 50★ baseline 2026-08-13 → 91★ (+41★/24h peak
2026-08-14) → 95★ (+4★/24h deceleration 2026-08-15) → 95★ (+0★/24h
stagnation 2026-08-16). 3-day average velocity is +1.5★/24h).

**Confidence:** **high** for the JTBD pull (95★ in 4 days for a TS
POS starter with 94 forks), **zero** for the stack match (FastAPI ✗,
SQLModel ✗, aiogram ✗, Postgres ✗; longnick is TypeScript + React 19
+ Vite 8).

**Decision: defer (watch-list, watch expired).** The slice boundary
is hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies. Circuit breaker: delete this
file + the corresponding `INDEX.md` row; no other code changes to
revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2 utility, the slicing discipline
   inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-research` (this pick came from the daily research
   job on 2026-08-16).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/71-longnick-star-velocity-watch.md   # NEW (this artifact)
specs/longnick-star-velocity-watch-HANDOFF.md # NEW (this file)
INDEX.md                                       # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys.
Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/71-longnick-star-velocity-watch.md` and
   confirm it matches the daily-research report's
   "longnick-star-velocity-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature
   pipeline" table and confirm the date (2026-08-16), pick slug
   (`longnick-star-velocity-watch`), feature path
   (`features/71-longnick-star-velocity-watch.md`), and Linear
   sub-issue ID.
3. **On the next daily-research pass (2026-08-17):** query the
   GitHub Search Repositories API for `longnick/small-pos-open-source`
   and record the new ★ count. If the ★ count is in the revised
   target window (95★ ± 10), the watch is effectively over. If the
   ★ count resumes growth above 105★, the watch re-activates.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID
`fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`
(label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 71 — longnick star velocity watch`.
- Body: the contract from `features/71-longnick-star-velocity-watch.md`
  (or a short summary + the file path).
- Parent: `HMM-85` (Research 2026-08-16 — daily).
- Status: `Backlog`.

## Rollback path

Delete `features/71-longnick-star-velocity-watch.md` and this
HANDOFF.md. Remove the corresponding row from `INDEX.md`. No
other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The `longnick/small-pos-open-source` repo is the **closest JTBD
pull in window** for the LE31 owner-pain (small café POS), but the
**stack match is zero** (TypeScript + React 19 + Vite 8 frontend,
no Python backend). The watch exists to track whether the JTBD
pull accumulates star velocity that would justify a from-scratch
Python rewrite or a charter-decided stack change to TypeScript.

**As of 2026-08-16, the watch has effectively expired**: the
velocity-driven signal (which was the original reason to watch)
is gone. The JTBD pull is confirmed (95★ is very high) but the
velocity that made it special has decayed to a normal slow-growth
/ stagnation pattern.

**Risk of NOT tracking:** the JTBD pull could re-activate (e.g. a
backend PR or a Hacker News Show HN post) and the team would miss
the window. The watch exists to catch that re-activation.

**Risk of over-tracking:** the watch is now mostly noise (the
velocity-driven signal is gone); over-tracking consumes
daily-research cycles that could be spent on higher-signal
in-window candidates.

**Net:** keep the watch active for one more 7-day window, then
close it if the revised target window (95★ ± 10) is sustained.
