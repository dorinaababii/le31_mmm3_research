# Feature 105 — uvicorn 0.52.4 pin-bump (v8)

> **Carry-over from 2026-08-16 (feature 70) → 2026-08-17 (feature 76) → 2026-08-18 (feature 78) → 2026-08-19 (feature 80) → 2026-08-20 (feature 82) → 2026-08-21 (feature 87) → 2026-08-22 (feature 93, v7) → 2026-08-24 (this feature, v8).**
> Supersedes `features/93-uvicorn-0-52-4-pin-bump-v7.md`.
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
- The v0.52.5 bump if it lands (re-check on 2026-08-25 — none observed
  today; burst has stabilized at 0.52.4 for 5 consecutive days).

## Description

The uvicorn project shipped three same-week patch releases between
2026-08-13 and 2026-08-19:

| Release | PyPI upload | Kludex/uvicorn releases atom | Notable diff |
|---|---|---|---|
| 0.52.2 | 2026-08-13T~ | 2026-08-13 | zttp 0.0.22 → 0.0.23 |
| 0.52.3 | 2026-08-13T~ | 2026-08-13 | zttp 0.0.23 → 0.0.24 |
| 0.52.4 | 2026-08-19T06:27:40Z | 2026-08-19T06:00:54Z | WebSocket close-handshake fix + HTTP/1.1 perf improvements + httptools loop fix backport |

Per the **2026-08-24 daily-research pass** (25th consecutive pass), all three
releases remain in the LE31 carry-over list; the 0.52.4 release is now
**5 consecutive days stable** (no 0.52.5 yet observed). The 0.52.1 → 0.52.4
bump has surfaced as a build candidate on every daily pass from 2026-08-16
through 2026-08-24 (8 consecutive days). The pattern is firmly
established: the burst has stabilized at 0.52.4.

**Why defer**: charter §3.2 explicitly says a stack change requires an
explicit charter decision. The pin-bump is a stack change. The deferral
window is "the next charter-decided pin-bump window", which has not yet
opened.

## Data model

**No schema changes.** Stack-pin bump only.

## Implementation steps

1. Open `backend/requirements.txt` (or equivalent manifest — verify with
   the coding agent before editing).
2. Change the line `uvicorn == 0.52.1` (or current pin) to `uvicorn == 0.52.4`.
3. Re-run the test suite to confirm no regressions.
4. Append a CHANGELOG entry: "Bump uvicorn to 0.52.4 (WebSocket close-
   handshake, HTTP/1.1 perf, httptools loop fix backport)".
5. Update the active feature pipeline row in `/opt/data/INDEX.md` to
   mark v8 done (or remove if the slice is being treated as a one-off
   pin-bump with no follow-up artifact).

## Telegram interaction if any

**None.** This is a stack-pin bump; no user-facing behavior change. The
LE31 Telegram-bot surface (cook-bot, charter §3.1) is unaffected.

## Dependencies

- **uvicorn 0.52.4** — uploaded to PyPI on 2026-08-19T06:27:40Z, tagged
  on `Kludex/uvicorn` releases atom at 2026-08-19T06:00:54Z.
- **zttp 0.0.24** — transitive dependency updated as part of the
  0.52.4 bump.
- **httptools loop fix backport** — transitive dependency fix.
- **Charter §3.2 review trigger** — the next charter review should
  consider whether to consolidate the 8-day pin-bump surfacing pattern
  into a routine pin-bump cadence (e.g., "all patch-version bumps land
  on the next charter-decided window without explicit charter review
  unless a major-version bump is involved").

## Open questions

1. **Does LE31 have a `backend/requirements.txt` (or equivalent)?**
   The coding agent should verify the manifest path before editing.
2. **Is the WebSocket close-handshake fix relevant to LE31's cook-Telegram-bot
   surface?** Charter §3.1 mentions SSE for the cook channel; uvicorn's
   WebSocket fix is therefore orthogonal but should not regress.
3. **Should the 0.52.1 → 0.52.4 bump be combined with the httpx 1.0.dev-track
   watch (feature 95) into a single "stack-pin-bump window" artifact?**
   The httpx v1 dev cycle is forward-looking only; the consolidation
   decision belongs to the next charter review.

## Why this matters

The 0.52.4 pin-bump is the highest-confidence pure-stability/perf bump
in the LE31 carry-over list:
- 8 consecutive days of surfacing as a build candidate (the longest
  carry-over streak in the 25-pass series).
- 5 consecutive days of "no 0.52.5 yet" — the burst has stabilized.
- Zero API breaking changes documented in the 0.52.2 / 0.52.3 / 0.52.4
  release notes.
- Zero new transitive dependencies beyond the zttp / httptools version
  increments that uvicorn already controls.

The deferral is per charter §3.2, not per evidence. When the next
charter-decided pin-bump window opens, this is the first one to land.