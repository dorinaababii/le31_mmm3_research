# longnick-star-velocity-watch — HANDOFF (v4, 2026-08-19 update)

> **Slice for the coding agent.** Read this *and*
> `features/71-longnick-star-velocity-watch.md` before touching any
> code. Do not paste chat excerpts back into the build. This is the
> **v4 HANDOFF** for feature 71 (the original HANDOFF was created on
> 2026-08-16, the v2 HANDOFF on 2026-08-17, the v3 HANDOFF on
> 2026-08-18, and this v4 reflects the 20-pass observation through
> 2026-08-19 which confirms the watch has **definitively EXPIRED +
> −1★/24h anomaly under confirmation** — GitHub star counts do not
> normally decrease; the 95★ → 94★ observation today with a NEW push
> in past 24h warrants a 2026-08-20 confirmation check).

## Frozen identifiers (do not rename)

- Feature ID: `71`
- Slug: `longnick-star-velocity-watch`
- Contract file: `features/71-longnick-star-velocity-watch.md`
- Bucket: **v2 utility (watch-list)** — defer; watch definitively
  EXPIRED + −1★/24h anomaly under confirmation
- Linear parent: `HMM-103` (Research 2026-08-19 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (GitHub Search Repositories API across the 20-pass
daily-research series — 50★ baseline 2026-08-13 → 91★ (+41★/24h peak
2026-08-14) → 95★ (+4★/24h deceleration 2026-08-15) → 95★ (+0★/24h
stagnation 2026-08-16) → 95★ (+0★/48h CONFIRMED, repo actively
pushed 2026-08-17T02:17:41Z) → 95★ (+0★/72h CONFIRMED, repo last
pushed 2026-08-17T02:17:41Z — **no new push in past 24h**) → 94★
(**−1★/24h ANOMALY** 2026-08-19, repo last pushed
**2026-08-18T12:02:14Z — NEW push in past 24h**). 7-day trajectory
is +0.43★/24h average (with the −1★ anomaly in the last 24h).

**Confidence:** **high** for the JTBD pull (94★ at the 7-day floor
for a TS POS starter with 90 forks is very high; the +41★/24h peak
was a one-day velocity phenomenon that has now decayed), **zero**
for the stack match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
longnick is TypeScript + React 19 + Vite 8).

**Decision: defer (watch-list, watch definitively EXPIRED + −1★/24h anomaly under confirmation).**
The slice boundary is hard: one Markdown file update, zero source
code changes, zero migrations, zero new dependencies. Circuit
breaker: delete this file + the corresponding `INDEX.md` row; no
other code changes to revert.

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
features/71-longnick-star-velocity-watch.md  # already created (v2)
specs/longnick-star-velocity-watch-HANDOFF.md  # already created (v1)
INDEX.md                                     # EDIT: add active feature pipeline row
```

Zero source files touched. Zero migrations. Zero new config keys.
Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/71-longnick-star-velocity-watch.md` and
   confirm it matches the daily-research report's
   "longnick-star-velocity-watch" pick description (v4 with the
   2026-08-19 20-pass observation and the −1★/24h anomaly).
2. **Read back** the new row in `INDEX.md` "Active feature
   pipeline" table and confirm the date (2026-08-19), pick slug
   (`longnick-star-velocity-watch`), feature path
   (`features/71-longnick-star-velocity-watch.md`), and Linear
   sub-issue ID.
3. **On the next daily-research pass (2026-08-20):** query the
   GitHub Search Repositories API for `longnick/small-pos-open-source`
   and record the new ★ count. If the ★ count is in the revised
   target window (95★ ± 5), the −1★ anomaly was a single-star-removal
   or API staleness (hypothesis (a) or (c)). If the ★ count stays
   at 94★ or drops further, hypothesis (b) (mass un-star / API
   anomaly) gains weight and the watch remains in "plateau but
   anomaly" state.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID
`fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`
(label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 71 — longnick star velocity watch` (v4, watch
  definitively EXPIRED + −1★/24h anomaly under confirmation).
- Body: the contract from `features/71-longnick-star-velocity-watch.md`
  (or a short summary + the file path).
- Parent: `HMM-103` (Research 2026-08-19 — daily, the Linear index
  issue created in this cron).
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

**As of 2026-08-17, the watch has definitively EXPIRED**: the
velocity-driven signal (which was the original reason to watch) is
gone. JTBD pull is confirmed (95★ in 5 days is very high for a TS POS
starter with 93 forks) but the velocity that made it special has
decayed to a normal slow-growth / stagnation pattern.
**The +0★/48h observation with active pushes is a stronger "defer"
signal than yesterday's +0★/24h** — an active repo that is not
gaining stars is consistent with the JTBD pull being sated by
existing organic discovery.

**As of 2026-08-18 (19-pass observation, +0★/72h CONFIRMED with no new
push in the past 24h), the watch has DEFINITIVELY EXPIRED.** The
+0★/72h observation across 4 consecutive daily passes is the
strongest "defer" signal yet — the repo is now demonstrably in the
long-term plateau phase, not the velocity-driven discovery phase.
**The +0★/72h observation with no new push in the past 24h** is a
stronger "defer" signal than yesterday's +0★/48h with active pushes
— an active repo that has stopped pushing AND has stopped gaining
stars is consistent with the JTBD pull being fully sated by existing
organic discovery.

**Risk of NOT tracking:** the JTBD pull could re-activate (e.g. a
backend PR or a Hacker News Show HN post) and the team would miss
the window. The watch exists to catch that re-activation.

**Risk of over-tracking:** the watch is now mostly noise (the
velocity-driven signal is definitively gone); over-tracking
consumes daily-research cycles that could be spent on higher-signal
in-window candidates.

**Net:** keep the watch active for one more 7-day window, then
close it if the revised target window (95★ ± 5) is sustained.