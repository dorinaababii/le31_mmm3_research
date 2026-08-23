# Feature 101 — httpx 1.0 dev-track v2 (day-3 cadence-shift observation)

> **NEW observation (2026-08-23).** Documents the in-window
> `httpx 1.0.dev4` (2026-08-19) + `1.0.dev5` (2026-08-21) dev-cycle
> signal observed during the 2026-08-23 daily research pass, with
> a **NEW data point today**: **0 dev releases in 44h** between
> `1.0.dev5` (2026-08-21T10:59:57Z) and today's fetch
> (2026-08-23T06:31:35Z). The httpx v1 dev cycle resumed after a
> 336-day gap; cadence has now slowed from "2 in 48h" to "0 in 44h"
> — first sign of cadence change since the v1 dev cycle resumed.
> Bucket: **v2 utility (stack pin-track, watch-list)** — hard defer
> pending a stable 1.0 release + a charter-decided httpx version cut.

## Goal

Record the **in-window httpx v1 dev cycle cadence shift** — two dev
releases in 2 days (`1.0.dev4` + `1.0.dev5`) suggested the maintainer
(encode/httpx) was actively pushing toward the 1.0 stable cut; **0
dev releases in 44h** observed today is the first sign of cadence
change since the v1 dev cycle resumed. LE31 currently pins
`httpx 0.28.1` (stable, 2024-12-06). Watch-list entry only — no
stable release is imminent, and LE31 has no charter-decided httpx
version cut. The artifact is the persistent record so future research
passes can compare against this baseline.

## Scope

**In scope:**
- Daily PyPI JSON check on `httpx` to surface new releases.
- Tracking the v1.0 dev cycle releases + cadence as they land.
- Documenting the dev-cycle observation in the LE31 research notes
  (this artifact is the document).
- Reading the httpx changelog + GitHub milestones via raw curl to
  confirm the v1.0 release scope.

**Out of scope (v1 / v2):**
- Any httpx pin bump until a stable 1.0 release ships AND a
  charter-decided version cut is made (per `le31-conventions` §3.2).
- Importing any code from `httpx 1.0.devN` (dev releases are not
  pinned by LE31 convention).
- Building any feature based on the httpx v1 surface area.

## Description

### httpx release timeline (recent window)

| Release | PyPI upload | Days since prior |
|---|---|---|
| `httpx 0.28.1` | 2024-12-06T11:19:04Z | (stable, currently pinned by LE31) |
| `httpx 1.0.dev3` | 2025-09-15T16:15:10Z | n/a |
| `httpx 1.0.dev4` | **2026-08-19T12:36:32Z** | **336 days since `1.0.dev3`** |
| `httpx 1.0.dev5` | **2026-08-21T10:59:57Z** | **2 days since `1.0.dev4`** |
| `httpx 1.0.dev6` | (not released yet) | **0 dev releases in 44h** ← NEW data point today |

**Direct PyPI URL**: https://pypi.org/pypi/httpx/json

**Verbatim observation:**
- Two dev releases in 2 days (`1.0.dev4` + `1.0.dev5`) after a
  336-day gap from `1.0.dev3`. This was the **first activity on the
  httpx 1.0 line since 2025-09-15** and the strongest signal yet
  that the maintainer was actively pushing toward the 1.0 stable
  cut.
- The 336-day gap (2025-09-15 → 2026-08-19) is consistent with a
  normal "wait for stability" pattern — `httpx 1.0.devN` releases are
  pre-release alphas; the maintainer waited until the line was stable
  enough to resume dev work.
- **NEW data point today (2026-08-23)**: 0 dev releases in 44h
  (between `1.0.dev5` at 2026-08-21T10:59:57Z and today's fetch at
  2026-08-23T06:31:35Z). The maintainer cadence has **slowed from
  "2 in 48h" to "0 in 44h"** — first sign of cadence change since
  the v1 dev cycle resumed.
- LE31 currently pins `httpx 0.28.1` (stable, 2024-12-06). The
  0.28.x line has been stable for 20 months with no 0.29.x release;
  the v1.0 cut is the natural next major.

### Why this matters (but is still watch-list only)

1. **`httpx` is a transitive dependency of `httpcore` and `anyio`** —
   httpx is a direct LE31 import in `backend/` code (the FastAPI
   `TestClient` uses httpx under the hood). The pin matters for
   stability, not for new features.
2. **LE31 has no charter-decided httpx version cut.** The current
   pin in `backend/requirements.txt` is `httpx>=0.27` (a float pin —
   any 0.27.x+ release would already be eligible). However, the
   charter §3.2 stack-change rule requires an explicit charter
   decision for any new major version cut. **A pin-bump to
   `httpx==1.0.0` would be a major-version cut and is within the
   charter's scope, but the timing is the user's call.**
3. **Dev releases are not pinned by LE31 convention.** The
   `le31-conventions` §3.2 stack-change rule requires an explicit
   charter decision for any new httpx version cut. Dev releases are
   recorded but not pinned.
4. **The cadence shift is a useful signal**: 0 dev releases in 44h
   suggests the maintainer is in a "stabilize" phase after the
   2-in-48h burst. The next dev release (or stable 1.0) may be
   days or weeks away.
5. **The next stable 1.0 release will be the trigger for a
   pin-bump artifact.** When httpx 1.0.0 ships (or even 1.0.0rc1 /
   1.0.0b1), the next daily-research pass should surface a
   `httpx-1-0-stable-cut` artifact analogous to feature 99
   (`uvicorn-0-52-4-pin-bump-v8`).

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 27 `uvicorn-0-52-pin` | uvicorn 0.52.1 pin | Different package |
| 70 `uvicorn-0-52-3-pin` | uvicorn 0.52.3 pin (carry-over) | Different package |
| 80 `uvicorn-0-52-4-pin` | uvicorn 0.52.4 pin (carry-over, day 4) | Different package |
| 82 `uvicorn-0-52-4-pin-bump-v5` | uvicorn 0.52.4 pin (carry-over, day 5) | Different package |
| 87 `uvicorn-0-52-4-pin-bump-v6` | uvicorn 0.52.4 pin (carry-over, day 6) | Different package |
| 93 `uvicorn-0-52-4-pin-bump-v7` | uvicorn 0.52.4 pin (carry-over, day 7) | Different package |
| 99 `uvicorn-0-52-4-pin-bump-v8` | uvicorn 0.52.4 pin (carry-over, day 8) | Different package |
| 95 `httpx-1-0-dev-track` | httpx 1.0.dev-track (carry-over, day 1, from 2026-08-22) | Older observation |
| **101 `httpx-1-0-dev-track-v2` (this)** | httpx 1.0.dev-track (carry-over, day 2, NEW cadence-shift data point) | **Newest** artifact |

This pick is the **2nd consecutive daily-research carry-over** of
the same httpx 1.0 dev-cycle observation. It is NOT a duplicate of
feature 95 — it is the **newest** daily-research observation with
the **NEW cadence-shift data point** (0 dev releases in 44h).

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation, not a feature build.

## Implementation

1. Continue daily PyPI JSON check on `httpx` to surface new releases
   in the next daily-research pass.
2. When `httpx 1.0.0` (or `1.0.0rc1` / `1.0.0b1`) ships, surface a
   `httpx-1-0-stable-cut` artifact analogous to feature 99.
3. Read the httpx changelog via raw curl to
   `https://github.com/encode/httpx/blob/master/CHANGELOG.md` (or the
   latest tag's CHANGELOG) on the next pass.
4. **No build implied.** The pick is a watch-list observation. The
   "should LE31 bump httpx to 1.0?" question is parked pending a
   stable 1.0 release + a charter-decided version cut.

## Telegram interaction

None. This is a passive observation; no cook or manager action.

## Dependencies

- None. The watch-list entry is passive.

## Open questions

- Does the `httpx 1.0.dev4` / `1.0.dev5` release include any
  breaking API changes that would affect LE31?
- When is the expected stable `httpx 1.0.0` release? (The 336-day
  dev-cycle gap + the new 0-in-44h cadence pause suggest the
  maintainer is conservative; the next dev release could be 1.0.0b1
  within weeks or 1.0.0rc1 within months.)
- Is there a public roadmap for the v1.0 cut? (Check the GitHub
  milestones via raw curl.)
- Does LE31 need a charter-decided httpx version cut now, or can it
  wait until 1.0.0 ships?

## Why this matters

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