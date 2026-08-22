# Feature 93 — uvicorn 0.52.4 pin-bump (v7)

> **Carry-over from 2026-08-16 (feature 70) → 2026-08-17 (feature 76) → 2026-08-18 (feature 78) → 2026-08-19 (feature 80) → 2026-08-20 (feature 82) → 2026-08-21 (feature 87) → 2026-08-22 (this feature, v7).**
> Supersedes `features/87-uvicorn-0-52-4-pin-bump-v6.md`.
> Bucket: **v2 utility (stack pin-bump)** — build candidate defer.

## Goal

Bump the pinned `uvicorn` runtime in LE31's dependency manifest from
`uvicorn == 0.52.1` to `uvicorn == 0.52.4`, picking up three same-week patch
releases (0.52.2 + 0.52.3 + 0.52.4) that landed between 2026-08-13 and
2026-08-19. The bump is pure stability / perf: zttp 0.0.22 → 0.0.24,
WebSocket close-handshake fix, HTTP/1.1 perf improvements, and a
backport of the httptools loop fix. No API breaking changes.

## Scope

**In scope:**
- One source-file edit: the dependency manifest (`requirements.txt` or
  equivalent — see `backend/requirements.txt`).
- One CHANGELOG / release-notes entry.
- One row appended to `/opt/data/INDEX.md` "Active feature pipeline"
  table (this artifact already counts as a row once the slice lands).

**Out of scope (v1):**
- Any new pip dependency.
- Any DB migration.
- Any schema change.
- Any config key change.
- Any code change outside the dependency manifest.
- The v0.52.5 bump if it lands (re-check on 2026-08-23 — none observed
  today; burst has stabilized at 0.52.4 for 4 consecutive days).

## Description

The uvicorn project shipped three same-week patch releases between
2026-08-13 and 2026-08-19:

| Release | PyPI upload | Kludex/uvicorn releases atom | Notable diff |
|---|---|---|---|
| `0.52.2` | 2026-08-13T07:03:55Z | 2026-08-13T07:01:56Z | httptools loop backport |
| `0.52.3` | 2026-08-13T16:50:01Z | 2026-08-13T16:46:56Z | zttp 0.0.22 → 0.0.24 |
| `0.52.4` | 2026-08-19T06:27:40Z | 2026-08-19T06:00:54Z | WebSocket close-handshake fix + HTTP/1.1 perf |

LE31 imports `uvicorn` only as the ASGI server entrypoint and does not
exercise zttp; the WebSocket close-handshake fix is adjacent to feature
35 (sse-replay-buffer) but does not directly affect LE31 today. The
HTTP/1.1 perf improvements are universal. None of the three releases
are CVE/security fixes; the burst was unusual for the uvicorn project
(suggesting an active maintainer addressing multiple stability items)
and has now stabilized at 0.52.4 for 4 consecutive days with no 0.52.5
yet.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a one-line pin
bump.

## Implementation

1. Edit the dependency manifest to change `uvicorn == 0.52.1` to
   `uvicorn == 0.52.4` (or `uvicorn == 0.52.3` if the team already
   bumped per feature 76/78, or `uvicorn == 0.52.4` if the team already
   bumped per feature 80/82/87). The exact starting pin depends on which
   prior pin-bump (if any) was applied.
2. Add a one-line CHANGELOG / release-notes entry: `Bump uvicorn 0.52.1
   → 0.52.4 (zttp 0.0.24, WebSocket close-handshake fix, HTTP/1.1
   perf)`.
3. Append a row to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-22, pick slug `uvicorn-0-52-4-pin-bump-v7`,
   feature path `features/93-uvicorn-0-52-4-pin-bump-v7.md`, and the
   Linear sub-issue ID created in this cron.

## Telegram interaction

None. The cook's Telegram surface is unaffected by a uvicorn pin bump.

## Dependencies

- None. The bump is self-contained.

## Open questions

- Has the team already applied feature 80 (2026-08-19, v4), feature 82
  (2026-08-20, v5), or feature 87 (2026-08-21, v6)? The exact starting
  pin depends on this. If none was applied, the starting pin is
  `uvicorn == 0.52.1`. If v6 was applied, the starting pin is already
  `uvicorn == 0.52.4` and this artifact is a no-op.

## Why this matters

The `uvicorn 0.52.1 → 0.52.4` pin bump is the **only** in-window stack
change that affects a LE31 pin and the **only** one where the diff is
pure stability/perf. Three patch releases in 7 days suggests urgency
but none is a CVE/security fix; the burst has stabilized at 0.52.4
after 96h with no 0.52.5 release. If the team is doing a pin-bump
window, this is the right pin to land. If no pin-bump window opens in
the next 7 days, this artifact expires and a future daily-research pass
will surface a new pin-bump candidate (if any).
