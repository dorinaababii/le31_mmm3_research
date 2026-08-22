# httpx-1-0-dev-track — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation of the in-window httpx v1.0 dev-cycle signal, not a
> feature build. The slice boundary is hard: zero source-file edits,
> zero schema changes, zero new config keys, zero pin bumps.
> Read this *and* `features/95-httpx-1-0-dev-track.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `95`
- Slug: `httpx-1-0-dev-track`
- Contract file: `features/95-httpx-1-0-dev-track.md`
- Bucket: **v2 utility (stack pin-track, watch-list)** — hard defer
  pending a stable 1.0 release + a charter-decided httpx version cut
- Linear parent: `HMM-121` (Research 2026-08-22 — daily, created in
  this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via PyPI JSON: `httpx 1.0.dev4`
2026-08-19T12:36:32Z + `httpx 1.0.dev5` 2026-08-21T10:59:57Z; v1 dev
cycle resumed after 336-day gap from `1.0.dev3` 2025-09-15; LE31
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
   on 2026-08-22).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/95-httpx-1-0-dev-track.md          # NEW (this artifact)
specs/httpx-1-0-dev-track-HANDOFF.md        # NEW (this file)
INDEX.md                                    # EDIT: append one row to "Active feature pipeline" table (watch-list continue entry)
```

Zero source-file edits outside the research artifacts. Zero pin bumps.
Zero schema changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back**
   `features/95-httpx-1-0-dev-track.md` and confirm it matches the
   daily-research report's "httpx-1-0-dev-track" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-22), pick slug
   (`httpx-1-0-dev-track`), feature path
   (`features/95-httpx-1-0-dev-track.md`), and Linear sub-issue ID.
3. **On the next daily-research pass**:
   a. Re-query `https://pypi.org/pypi/httpx/json` and confirm whether
      a new dev release has shipped (look for `1.0.dev6` or
      `1.0.0b1` / `1.0.0rc1`).
   b. Read the httpx changelog via raw curl to
      `https://raw.githubusercontent.com/encode/httpx/master/CHANGELOG.md`
      (or the latest tag's CHANGELOG) to confirm the v1.0 release
      scope.
   c. Track the `httpx` watch-list entry in the
      `Stack-relevant findings` section of the daily-research report.
4. **When `httpx 1.0.0` (or `1.0.0rc1` / `1.0.0b1`) ships**, surface a
   `httpx-1-0-stable-cut` artifact analogous to feature 93
   (`uvicorn-0-52-4-pin-bump-v7`). The artifact should be filed in the
   `le31 v1 — Core MVP` project with label `Feature`, status
   `Backlog`, and a parent reference to the daily-research index
   issue that surfaced it.
5. **No build implied today.** The pick is a watch-list observation.
   The "should LE31 bump httpx to 1.0?" question is parked pending a
   stable 1.0 release + a charter-decided version cut.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (the
v1 stack-pin bucket — analogous to the existing uvicorn pin-bump
features 27, 70, 80, 82, 87, 93). Label `Feature`.

- Title: `Feature 95 — httpx-1-0-dev-track`.
- Body: the contract from
  `features/95-httpx-1-0-dev-track.md` (or a short summary + the file
  path).
- Parent: `HMM-121` (Research 2026-08-22 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/95-httpx-1-0-dev-track.md` and this HANDOFF.md.
Remove the corresponding row from `INDEX.md`. No other code changes to
revert. No data migration to revert. No pin bump to revert (the watch
is passive).

## Why this matters (for the research agent)

The httpx v1 dev cycle resumption is the **first in-window dev-cycle
signal on any LE31-stack package** since the 2026-08-19 carry-over
uvicorn 0.52.4 patch. Two dev releases in 2 days (`1.0.dev4` +
`1.0.dev5`) after a 336-day gap suggests the maintainer is actively
pushing toward the 1.0 stable cut. LE31 currently pins `httpx 0.28.1`;
no immediate action is warranted (dev releases are not pinned by
convention), but the watch-list entry is the persistent record so
future research passes can compare against this baseline. The next
stable 1.0 release will be the trigger for a `httpx-1-0-stable-cut`
artifact.

## Carry-over history

This is the **NEW observation** (2026-08-22); no prior artifact
exists. Combines:

- The in-window PyPI JSON observation of `httpx 1.0.dev4`
  (2026-08-19T12:36:32Z) + `httpx 1.0.dev5` (2026-08-21T10:59:57Z).
- The 336-day gap from `httpx 1.0.dev3` (2025-09-15) which establishes
  the dev-cycle baseline.
- The current LE31 pin `httpx == 0.28.1` (stable, 2024-12-06).
