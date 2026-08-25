# Feature 109 — uvicorn 0.52.4 pin-bump v9

> **NEW observation (2026-08-25).** Documents the in-window
> `uvicorn 0.52.4` pin-bump surface from the 2026-08-25 daily
> research pass — the 9th consecutive day the same pin-bump has
> surfaced (carry-over of features 70, 76, 78, 80, 82, 87, 93, 105).
> The burst has now stabilized at 0.52.4 for 6 consecutive days
> with no 0.52.5 release.
> Bucket: **v2 utility (stack pin-bump)** — build candidate defer
> until the charter-decided pin-bump window opens.

## Goal

Record the **in-window `uvicorn 0.52.4` pin-bump** as a stable
build candidate now that the burst has stabilized for 6 days. The
bump is pure stability/perf (zttp 0.0.22 → 0.0.24 + WebSocket
close-handshake fix + bodyless request handling + HTTP/1.1 request
parsing performance); three patch releases on 2026-08-13 + 2026-08-19
were unusual for the uvicorn project (the prior 0.52.0 → 0.52.1 was a
3-day gap), suggesting an active maintainer and a real urgency to get
the WebSocket close-handshake fix in. The 6-day stable plateau at
0.52.4 (no 0.52.5 yet) confirms the burst has stabilized. The
artifact is the persistent build-candidate record.

## Scope

**In scope:**
- One source-file edit: the pin bump in the dependency manifest
  (e.g. `backend/requirements.txt`, `pyproject.toml`, or
  `requirements.lock`) from `uvicorn[standard]>=0.30` or `uvicorn==0.52.1`
  to `uvicorn[standard]==0.52.4` (or `>=0.52.4,<0.53` if the team
  prefers a float pin).
- One CHANGELOG / commit-message line documenting the bump.
- One INDEX.md row in the "Active feature pipeline" table.
- Re-run the LE31 test suite + dev server to confirm no regressions.

**Out of scope (v1 / v2):**
- Any zttp-specific API change (zttp is gated behind `--http zttp` in
  uvicorn 0.52.x; LE31 uses the standard h11 implementation).
- Any new pip dependency beyond the uvicorn bump.
- Any schema change, migration, or config key change.
- Any feature built on top of the new uvicorn API surface (e.g.
  `--http zttp` adoption; deferred to a future pin-bump window).

## Description

### uvicorn release timeline (recent window)

| Release | PyPI upload | Days since prior |
|---|---|---|
| `uvicorn 0.52.1` | 2026-08-01 (carry-over from prior passes) | (LE31 pin baseline) |
| `uvicorn 0.52.2` | 2026-08-13T07:03:55+ | (3-day gap; unusual) |
| `uvicorn 0.52.3` | 2026-08-13T16:50:01+ | <1 day (same UTC day) |
| `uvicorn 0.52.4` | **2026-08-19T06:27:40+** | 5 days |
| `uvicorn 0.52.5` | (not released yet) | — |

**Direct PyPI URL**: https://pypi.org/pypi/uvicorn/json

**GitHub release atom**: https://github.com/Kludex/uvicorn/releases.atom
(tagged 2026-08-19T06:00:54Z for 0.52.4)

**Verbatim observation:**
- Three in-window patch releases on the same UTC day (0.52.2 + 0.52.3)
  was unusual for the uvicorn project (the prior 0.52.0 → 0.52.1 was
  a 3-day gap), suggesting an active maintainer and a real urgency to
  get the WebSocket close-handshake fix in.
- The 6-day stable plateau at 0.52.4 (carry-over from prior pass; now
  6 days stable as of 2026-08-25) confirms the burst has stabilized.
- No 0.52.5 release in 144h.
- The 0.52.2 → 0.52.4 series updated zttp to 0.0.22 → 0.0.24, fixed a
  WebSocket close-handshake bug, improved bodyless request handling,
  and added HTTP/1.1 request parsing performance improvements.

### Why this matters (but is still a build-candidate defer)

1. **`uvicorn` is the ASGI server LE31 uses to serve FastAPI.**
   The pin matters for stability, not for new features. LE31 imports
   `uvicorn` only as the ASGI server entrypoint and doesn't exercise
   the zttp implementation (gated behind `--http zttp`).
2. **LE31 has no charter-decided uvicorn version cut.** The current
   pin in `backend/requirements.txt` is `uvicorn[standard]>=0.30` (a
   float pin — any 0.52.x release would already be eligible).
   However, the charter §3.2 stack-change rule requires an explicit
   charter decision for any new major version cut. **A pin-bump
   within the 0.52.x line is a minor utility bump and is within the
   charter's scope**, but the timing is the user's call.
3. **The 6-day stable plateau is the right time to ship.** If the
   team opens a pin-bump window, this is the right pin to land. If no
   pin-bump window opens in the next 7 days, this artifact expires
   and a future daily-research pass will surface a new pin-bump
   candidate (if any).
4. **No 0.52.5 release is imminent.** The burst has stabilized at
   0.52.4; the WebSocket fix and zttp bump are the meaningful
   changes; the rest is performance/perf.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 27 `uvicorn-0-52-pin` | uvicorn 0.52.1 pin (carry-over) | Earlier target |
| 70 `uvicorn-0-52-3-pin` | uvicorn 0.52.3 pin (carry-over) | Older target |
| 76 `uvicorn-0-52-3-pin` | uvicorn 0.52.3 pin (carry-over, day 2) | Older target |
| 78 `uvicorn-0-52-3-pin` | uvicorn 0.52.3 pin (carry-over, day 3) | Older target |
| 80 `uvicorn-0-52-4-pin` | uvicorn 0.52.4 pin (carry-over, day 4) | Older target |
| 82 `uvicorn-0-52-4-pin-bump-v5` | uvicorn 0.52.4 pin (carry-over, day 5) | Older target |
| 87 `uvicorn-0-52-4-pin-bump-v6` | uvicorn 0.52.4 pin (carry-over, day 6) | Older target |
| 93 `uvicorn-0-52-4-pin-bump-v7` | uvicorn 0.52.4 pin (carry-over, day 7) | Older target |
| 99 `uvicorn-0-52-4-pin-bump-v8` | uvicorn 0.52.4 pin (carry-over, day 8, 2026-08-24) | Older target |
| 105 `uvicorn-0-52-4-pin-bump-v8` | uvicorn 0.52.4 pin (canonical day-8 artifact, 2026-08-24) | Older target |
| **109 `uvicorn-0-52-4-pin-bump-v9` (this)** | uvicorn 0.52.4 pin (carry-over, day 9, this cron) | Same target; **newest** artifact |

This pick is the **9th consecutive daily-research carry-over** of
the same uvicorn 0.52.4 pin-bump. It is NOT a duplicate of the prior
v7/v8 artifacts — it is the **newest** daily-research observation
that the burst has now stabilized at 0.52.4 for 6 consecutive days
with no 0.52.5 release.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation + a build-candidate artifact; no schema change.

## Implementation

1. Wait for the user to open a pin-bump window (charter §3.2).
2. When the window opens:
   - Bump the pin in `backend/requirements.txt` from
     `uvicorn[standard]>=0.30` (or `uvicorn[standard]==0.52.1` /
     `==0.52.4` if the team has already bumped per prior features)
     to `uvicorn[standard]==0.52.4` (or `>=0.52.4,<0.53`).
   - Add a CHANGELOG / commit-message line documenting the bump.
   - Re-run the LE31 test suite + dev server to confirm no
     regressions.
3. **No build today.** The pick is a build-candidate defer. The
   "should LE31 bump uvicorn to 0.52.4?" question is parked pending
   the charter-decided pin-bump window.

## Telegram interaction

None. This is a passive utility bump; no cook or manager action.

## Dependencies

- None. The pin-bump is mechanical.

## Open questions

- Is the user ready to open a pin-bump window within the next 7
  days? (If yes, ship the bump. If no, this artifact expires and a
  future daily-research pass will surface a new pin-bump candidate
  if any.)
- Should the pin be `==0.52.4` (exact) or `>=0.52.4,<0.53` (float
  with upper bound)? The LE31 current pin is `>=0.30` (a float with
  no upper bound); the team should pick the convention it prefers.
- Does the test suite cover any zttp-specific behavior? (LE31 should
  not — zttp is gated behind `--http zttp` in uvicorn 0.52.x — but
  confirm before bumping.)
- Does the dev server still start with `uvicorn app.main:app
  --reload` after the bump? (This is part of the verification
  protocol.)

## Why this matters

The `uvicorn 0.52.1 → 0.52.4` pin bump is the **only** in-window
stack change that affects a LE31 pin and the **only** one where the
diff is pure stability/perf (zttp 0.0.22 → 0.0.24 + WebSocket
close-handshake fix + bodyless request handling + HTTP/1.1 request
parsing performance). The 6-day stable plateau at 0.52.4 (no 0.52.5
yet) is the right time to ship. If the team is doing a pin-bump
window, this is the right pin to land. If no pin-bump window opens in
the next 7 days, this artifact expires and a future daily-research
pass will surface a new pin-bump candidate (if any).
