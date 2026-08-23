# httpx-1-0-dev-track-v2 — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation of the in-window httpx v1.0 dev-cycle signal, not a
> feature build. The slice boundary is hard: zero source-file edits,
> zero schema changes, zero new config keys, zero pin bumps.
> Read this *and* `features/101-httpx-1-0-dev-track-v2.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `101`
- Slug: `httpx-1-0-dev-track-v2`
- Contract file: `features/101-httpx-1-0-dev-track-v2.md`
- Bucket: **v2 utility (stack pin-track, watch-list)** — hard defer
  pending a stable 1.0 release + a charter-decided httpx version cut
- Linear parent: `HMM-129` (Research 2026-08-23 — daily, created in
  this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via PyPI JSON: `httpx 1.0.dev4`
2026-08-19T12:36:32Z + `httpx 1.0.dev5` 2026-08-21T10:59:57Z; v1 dev
cycle resumed after 336-day gap from `1.0.dev3` 2025-09-15; **NEW
data point today: 0 dev releases in 44h** (between `1.0.dev5` at
2026-08-21T10:59:57Z and today's fetch at 2026-08-23T06:31:35Z); LE31
currently pins `httpx 0.28.1`).

**Confidence:** **high** for the dev-cycle observation (PyPI JSON
timestamps are author-controlled); **low** for the v1.0 stable cut
timing (no public roadmap).

**Decision: watch-list continue; hard defer pending stable 1.0
release + charter-decided httpx version cut.** The slice boundary is
hard: zero pin bumps, zero source-file edits, zero migrations, zero
schema changes. Circuit breaker: delete this file + the
corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-23).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/101-httpx-1-0-dev-track-v2.md       # NEW (this artifact)
specs/httpx-1-0-dev-track-v2-HANDOFF.md      # NEW (this file)
INDEX.md                                     # EDIT: append one row to "Active feature pipeline" table (watch-list continue entry)
```

Zero source-file edits outside the research artifacts. Zero pin bumps.

## Verification protocol

After the artifact ships:

1. **Read back** `features/101-httpx-1-0-dev-track-v2.md` and confirm
   it matches the daily-research report's "httpx-1-0-dev-track-v2"
   pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-23), pick slug
   (`httpx-1-0-dev-track-v2`), feature path
   (`features/101-httpx-1-0-dev-track-v2.md`), and Linear sub-issue
   ID.
3. **On a future daily-research pass**: re-query PyPI JSON for `httpx`
   and confirm whether a new in-window dev release ships. If a new
   release ships (e.g. `1.0.dev6`), the watch-list entry should be
   updated to feature 102 (`httpx-1-0-dev-track-v3`). If a stable
   `1.0.0` ships, surface a `httpx-1-0-stable-cut` artifact analogous
   to feature 99 (`uvicorn-0-52-4-pin-bump-v8`). **Re-check on
   2026-08-24.**
4. **Optional next-pass deep-read**: read the httpx changelog via raw
   curl to
   `https://raw.githubusercontent.com/encode/httpx/master/CHANGELOG.md`
   to confirm the v1.0 release scope.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2 owner-pains` with label
`Feature`.

- Title: `Feature 101 — httpx-1-0-dev-track-v2`.
- Body: the contract from
  `features/101-httpx-1-0-dev-track-v2.md` (or a short summary + the
  file path).
- Parent: `HMM-129` (Research 2026-08-23 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/101-httpx-1-0-dev-track-v2.md` and this HANDOFF.md.
Remove the corresponding row from `INDEX.md`. No other code changes
to revert. No data migration to revert.

## Why this matters (for the research agent)

The httpx v1 dev cycle resumption is the **first in-window dev-cycle
signal on any LE31-stack package** since the 2026-08-19 carry-over
uvicorn 0.52.4 patch. Two dev releases in 2 days (`1.0.dev4` +
`1.0.dev5`) suggested the maintainer was actively pushing toward the
1.0 stable cut; **the NEW cadence-shift data point today (0 dev
releases in 44h) is the first sign of cadence change since the v1
dev cycle resumed**. LE31 currently pins `httpx 0.28.1`; no
immediate action is warranted (dev releases are not pinned by
convention), but the watch-list entry is the persistent record so
future research passes can compare against this baseline. The next
stable 1.0 release will be the trigger for a `httpx-1-0-stable-cut`
artifact.

## Carry-over history

This is the **2nd consecutive day** the httpx 1.0 dev-cycle
observation has surfaced as a watch-list entry:

- 2026-08-22 → `features/95-httpx-1-0-dev-track.md` (day-1
  observation; the inaugural dev-cycle watch after the 336-day gap)
- 2026-08-23 → `features/101-httpx-1-0-dev-track-v2.md` (day-2
  observation; **NEW cadence-shift data point**: 0 dev releases in
  44h, **this artifact**)