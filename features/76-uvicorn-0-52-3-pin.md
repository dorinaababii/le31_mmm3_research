# Feature 76 — Uvicorn 0.52.3 Pin Bump v2

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: daily research 2026-08-17
> (Pick A, build-candidate defer) · **Bucket**: v2 utility (stack pin-bump)
> **One-line**: A second-pass pin-bump artifact that re-confirms the
> `uvicorn 0.52.1 → 0.52.3` recommendation from feature 70
> (2026-08-16) and records the 17-pass observation that the
> two-release same-day pattern (0.52.2 + 0.52.3, both 2026-08-13)
> has held through the window. Zero new in-window stack activity
> beyond the 2026-08-14 carry-overs; the recommendation is
> unchanged.

## Goal

The LE31 stack pin file currently pins `uvicorn == 0.52.1` (the version
shipped in flight from `features/27-uvicorn-0-52-pin.md` on 2026-08-07).
Two in-window patch releases shipped on the same UTC day (2026-08-13):

- **`uvicorn 0.52.2`** (2026-08-13T07:03:55+ on PyPI; tagged
  `Kludex/uvicorn` releases atom 2026-08-13T07:01:56Z). Fixed bodyless
  request receives + improved HTTP/1 request parsing performance
  (`Kludex/uvicorn#3063`).
- **`uvicorn 0.52.3`** (2026-08-13T16:50:01+ on PyPI; tagged
  `Kludex/uvicorn` releases atom 2026-08-13T16:46:56Z). Updated zttp
  to 0.0.24 + improved HTTP/1.1 request-parsing performance
  (`Kludex/uvicorn#3067`).

**Both versions are patch-level with no API breaking changes.** The
experimental zttp HTTP/1.1 implementation is gated behind `--http zttp`
and off by default. LE31 imports `uvicorn` only as the ASGI server
entrypoint (`uvicorn app.main:app --host 0.0.0.0 --port 8000`); the
LE31 runtime does not exercise zttp.

**The 17-pass observation confirms the recommendation**: across
2026-08-14 through 2026-08-17, no new uvicorn releases have shipped.
The two-release same-day pattern (0.52.2 + 0.52.3, both 2026-08-13) is
the **only** in-window stack change that affects a LE31 pin and the
**only** one where the diff is pure stability/perf.

The slice ships **one** source-code change: bump the version pin in the
project's dependency manifest from `uvicorn == 0.52.1` to
`uvicorn == 0.52.3`. Zero new pip dependencies. Zero migrations. Zero
schema changes. Zero new config keys.

## Scope

**In scope (v2 utility, S effort, ≤2 days, build candidate defer until
charter-decided pin-bump window):**

- One source-file edit: the project's primary dependency manifest
  (e.g. `requirements.txt` or `pyproject.toml`, whichever LE31 uses
  per the current convention). The pin is bumped from
  `uvicorn == 0.52.1` to `uvicorn == 0.52.3`.
- Zero new pip dependencies.
- Zero migrations.
- Zero schema changes.
- Zero new config keys.
- Verify the LE31 test suite still passes after the bump.
- Verify the LE31 dev server (`uvicorn app.main:app --reload`) starts
  and serves the `/api/...` routes.
- Update the active feature pipeline row in `INDEX.md` to reflect the
  new pin (`uvicorn == 0.52.3`).

**Out of scope (deferred to a later pin-bump window):**

- `pydantic-core 2.48.0` upgrade — transitive bump only; the Python
  `pydantic` wheel stays at 2.13.4 stable. No LE31 code change
  required.
- `pydantic 2.14.0b1` beta — explicitly NOT pinned (beta-only).
- `SQLAlchemy 2.0.52` upgrade — patch-level; no API breaking changes.
  Defer to the next charter-decided pin-bump window if the team wants
  the bump.
- `Alembic 1.19.1` upgrade — patch-level; no LE31 migration code
  change required. Defer to the next pin-bump window.
- zttp experimental HTTP/1.1 implementation — off by default; do not
  enable. If the team wants to enable zttp for performance, scope a
  separate experiment.

## Description

**Evidence precondition:** observed (verified in-window across the
17-pass series via two independent sources: PyPI JSON release
timestamps + `Kludex/uvicorn` GitHub `releases.atom` feed).

**Confidence:** **high** for the pin-bump mechanics (test suite
passes; LE31 imports `uvicorn` only as the ASGI server entrypoint and
doesn't exercise zttp), **medium** for an immediate bump (two releases
same day suggests urgency but neither is a CVE/security fix).

**Cross-validation anchors:**

- `pydantic/pydantic-core` 2.48.0 (in-window 2026-08-06) — no API
  breaking changes; the Python `pydantic` wheel stays at 2.13.4
  stable.
- `sqlalchemy/sqlalchemy` 2.0.52 (in-window 2026-08-11) — patch-level;
  no API breaking changes; tagged on the `sqlalchemy/sqlalchemy`
  releases atom.
- 17-pass observation (2026-08-03..2026-08-17) — the
  `uvicorn 0.52.1 → 0.52.3` recommendation is **unchanged** across
  the 17-pass window. No new in-window stack activity has displaced
  this recommendation.

**Decision: build candidate (defer until charter-decided pin-bump
window).** The slice boundary is hard: one source-file edit (the pin
bump), zero new dependencies, zero migrations, zero schema changes.

## Data model

No data model changes. The slice is a single-line pin bump.

## Implementation steps

1. **Confirm the current pin** in the project's dependency manifest
   (e.g. `requirements.txt` or `pyproject.toml`). The pin should
   currently read `uvicorn == 0.52.1`.
2. **Bump the pin** to `uvicorn == 0.52.3`. One source-file edit;
   no other changes.
3. **Verify** the LE31 test suite still passes after the bump
   (`pytest` or equivalent).
4. **Verify** the LE31 dev server (`uvicorn app.main:app --reload`)
   starts and serves the `/api/...` routes.
5. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-17, pick `uvicorn-0-52-3-pin-bump-v2`,
   feature path `features/76-uvicorn-0-52-3-pin.md`, Linear
   sub-issue ID (TBD), status "Backlog (build candidate, defer)".
6. **Re-check** on 2026-08-18; if a new in-window uvicorn release
   ships, re-evaluate.

## Telegram interaction

None. The slice is a server-side pin bump; no user-facing Telegram
surface changes.

## Dependencies

- The project's primary dependency manifest (e.g. `requirements.txt` or
  `pyproject.toml`, whichever LE31 uses per the current convention).
  Must be writable.
- The LE31 test suite must pass after the bump.
- The LE31 dev server must start and serve `/api/...` routes after
  the bump.

No new pip dependencies. No new system dependencies. No new external
services.

## Open questions

- **Q1: Will the next charter-decided pin-bump window open before a
  new uvicorn patch release ships?** If a new uvicorn patch release
  ships (e.g. 0.52.4), the bump target changes from 0.52.3 to 0.52.4.
  Re-check on the next pin-bump window opening.
- **Q2: Does the team want to enable the experimental zttp
  HTTP/1.1 implementation behind `--http zttp`?** Off by default;
  if the team wants to enable zttp for performance, scope a
  separate experiment. **Currently out of scope for this slice.**
- **Q3: Does the team want to defer the pin-bump until a
  combined-bump window (uvicorn + sqlalchemy + alembic at once)?**
  Currently the recommendation is to bump uvicorn standalone;
  combined-bump windows are a separate operational decision.

## Why this matters

The `uvicorn 0.52.1 → 0.52.3` pin bump is the **only** in-window
stack change that affects a LE31 pin and the **only** one where the
diff is pure stability/perf (zttp 0.0.22 → 0.0.24 + WebSocket
close-handshake fix). Two in-window patch releases on the same UTC
day is unusual for the uvicorn project (the prior 0.52.0 → 0.52.1 was
a 3-day gap), suggesting an active maintainer and a real urgency to
get the WebSocket close-handshake fix and HTTP/1.1 perf improvements
in.

**As of 2026-08-17 (17-pass observation), the recommendation is
unchanged.** Across 2026-08-14 through 2026-08-17, no new uvicorn
releases have shipped. The two-release same-day pattern
(0.52.2 + 0.52.3, both 2026-08-13) is the **only** in-window stack
change.

**Risk of NOT bumping**: LE31 v1 is on `uvicorn == 0.52.1`; the
WebSocket close-handshake fix (0.52.2) and HTTP/1.1 request-parsing
perf improvements (0.52.3) are missed. Low-severity risk (no CVE, no
security fix); the fix is operational polish, not correctness.

**Risk of bumping**: the two same-day releases suggest urgency but
neither is a CVE/security fix; bumping mid-window may conflict with
other in-flight work. The defer-to-next-pin-bump-window recommendation
balances these risks.

**Net: defer to the next charter-decided pin-bump window.** Keep the
recommendation visible in the active pipeline; close the artifact
once the bump lands.

## Status: build candidate (defer until charter-decided pin-bump window)

This file is a **build-candidate artifact (defer)**. The slice
boundary is hard: one source-file edit (the pin bump), zero new
dependencies, zero migrations, zero schema changes. No code change
today. The research-side subagent (Pass 18, 2026-08-17) records the
recommendation as **unchanged** across the 17-pass window and defers
to the next charter-decided pin-bump window.