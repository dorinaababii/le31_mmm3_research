# foodieshub-ts-pos-watch — HANDOFF (v3, 2026-08-19 update)

> **Slice for the coding agent.** Read this *and*
> `features/81-foodieshub-ts-pos-watch.md` before touching any
> code. Do not paste chat excerpts back into the build. This is the
> **v3 HANDOFF** for the foodieshub watch-list (the original HANDOFF
> was created on 2026-08-17 with feature 77, the v2 HANDOFF on
> 2026-08-18 with feature 79, and this v3 reflects the 20-pass
> observation through 2026-08-19 which records the +0★/72h
> steady-state stagnation and the longnick-pattern velocity collapse).

## Frozen identifiers (do not rename)

- Feature ID: `81` (v3 of the foodieshub watch)
- Slug: `foodieshub-ts-pos-watch`
- Contract file: `features/81-foodieshub-ts-pos-watch.md`
- Bucket: **v2 utility (watch-list)** — defer; fails the gate
- Linear parent: `HMM-103` (Research 2026-08-19 — daily, created in
  this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list record
  update)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (GitHub Search Repositories API on 2026-08-17 +
2026-08-18 + 2026-08-19; direct repo inspection confirms the
description, language, and topics).

**Confidence:** **high** for the JTBD pull (restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management = exactly
the LE31 feature surface from features 02/03/09/14), **zero** for the
stack match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗; helloman3 is
TypeScript + React PWA + 0-fork single-author repo).

**Decision: defer (watch-list, fails the gate + +0★/72h steady-state
stagnation observed).** The slice boundary is hard: one Markdown file
update, zero source code changes, zero migrations, zero new
dependencies. Circuit breaker: delete this file + the corresponding
`INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2 utility, the slicing discipline
   inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-research` (this pick came from the daily research
   job on 2026-08-18).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/79-foodieshub-ts-pos-watch.md   # NEW (this artifact, v2)
specs/foodieshub-ts-pos-watch-HANDOFF.md # NEW (this file, v2)
INDEX.md                                # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys.
Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/81-foodieshub-ts-pos-watch.md` and
   confirm it matches the daily-research report's
   "foodieshub-ts-pos-watch" pick description (v3 with the
   2026-08-19 20-pass observation and +0★/72h steady-state).
2. **Read back** the new row in `INDEX.md` "Active feature
   pipeline" table and confirm the date (2026-08-19), pick slug
   (`foodieshub-ts-pos-watch`), feature path
   (`features/81-foodieshub-ts-pos-watch.md`), and Linear sub-issue
   ID.
3. **On the next daily-research pass (2026-08-20):** query the
   GitHub Search Repositories API for `helloman3/foodieshub` and
   record the new ★ count. If the ★ count grows above 5★, the
   velocity is sustained and the watch re-activates. If the ★
   count holds steady at 4★ for another 7 days, the velocity
   collapse is confirmed and the watch is effectively over.
4. **Read the helloman3/foodieshub README** on the 2026-08-20 pass
   to confirm scope (multi-device sync mechanism is the most
   distinctive feature of the description).

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID
`fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`
(label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 81 — foodieshub ts pos watch` (v3, watch-list,
  fails the gate + +0★/72h steady-state stagnation).
- Body: the contract from `features/81-foodieshub-ts-pos-watch.md`
  (or a short summary + the file path).
- Parent: `HMM-103` (Research 2026-08-19 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/79-foodieshub-ts-pos-watch.md` and this HANDOFF.md.
Remove the corresponding row from `INDEX.md`. No other code changes to
revert. No data migration to revert.

## Why this matters (for the coding agent)

The `helloman3/foodieshub` repo is the **closest direct JTBD pull
in window** for LE31 (restaurant/bar POS + multi-device sync +
KOT/BOT printing + CSV bulk management = exactly the LE31 feature
surface from features 02/03/09/14), but the **stack match is zero**
(TypeScript + React PWA, not Python + FastAPI + SQLModel + aiogram +
Postgres). The watch exists to track whether the JTBD pull accumulates
star velocity that would justify a from-scratch Python rewrite or a
charter-decided stack change to TypeScript.

**As of 2026-08-18 (19-pass observation, +1★/24h from yesterday's
3★, 0 forks), the watch is fresh but the velocity is collapsing.**
The +3★ in <2 hours of push on 2026-08-17 has decayed to +1★/24h
on 2026-08-18, a +0.5★/24h average across the 2-day window. This is
**consistent with the longnick pattern of velocity-driven attention
collapsing to steady-state slow growth** (longnick went from
+41★/24h peak to +0★/72h plateau over 6 days). The 0-fork observation
confirms this is a single-author repo with no community traction yet.

**Risk of NOT tracking:** the JTBD pull could re-activate (e.g. a
README deep-dive or a Hacker News Show HN post) and the team would
miss the window. The watch exists to catch that re-activation.

**Risk of over-tracking:** the watch is now mostly noise (4★ is a
very low baseline; velocity-driven signal is already decaying);
over-tracking consumes daily-research cycles that could be spent on
higher-signal in-window candidates.

**Net: keep the watch active for one more 7-day window, then close
it if the ★ count remains below 10★.**
