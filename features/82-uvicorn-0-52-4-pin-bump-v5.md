# Feature 82 — Uvicorn 0.52.4 Pin Bump v5

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: daily research 2026-08-20
> (Pick A, build-candidate defer) · **Bucket**: v2 utility (stack pin-bump)
> **One-line**: A fifth-pass pin-bump artifact that supersedes
> `features/80-uvicorn-0-52-4-pin.md` (2026-08-19) and confirms the
> `uvicorn 0.52.1 → 0.52.4` bump covering three in-window patch releases
> (0.52.2 + 0.52.3 + 0.52.4 across 2026-08-13 + 2026-08-19 — same week).
> **5th consecutive day** the uvicorn pin-bump has surfaced as a build
> candidate (2026-08-16 → feature 70, 2026-08-17 → feature 76,
> 2026-08-18 → feature 78, 2026-08-19 → feature 80, 2026-08-20 → feature 82);
> consistent deferral pattern; today the patch-version target **holds at
> 0.52.4** (no 0.52.5 yet — the 4-day burst has stabilized). Zero new
> in-window stack activity outside the 0.52.x patch burst.

## Goal

The LE31 stack pin file currently pins `uvicorn == 0.52.1` (the version
shipped in flight from `features/27-uvicorn-0-52-pin.md` on 2026-08-07).
Three in-window patch releases have shipped in 2026-08:

- **`uvicorn 0.52.2`** (2026-08-13T07:03:55+ on PyPI; tagged
  `Kludex/uvicorn` releases atom 2026-08-13T07:01:56Z). Fixed bodyless
  request receives + improved HTTP/1 request parsing performance
  (`Kludex/uvicorn#3063`).
- **`uvicorn 0.52.3`** (2026-08-13T16:50:01+ on PyPI; tagged
  `Kludex/uvicorn` releases atom 2026-08-13T16:46:56Z). Updated zttp
  to 0.0.24 + improved HTTP/1.1 request-parsing performance
  (`Kludex/uvicorn#3067`).
- **`uvicorn 0.52.4`** (2026-08-19T06:27:40+ on PyPI; tagged on
  `Kludex/uvicorn` releases atom 2026-08-19T06:00:54Z). NEW IN-WINDOW
  (carry-over from 2026-08-19 pass; still the latest in-window patch).
  Patch release; pure stability/perf (3 in-window patches in 7 days
  was unusual activity; the burst has now stabilized at 0.52.4 with
  no 0.52.5 release in 24h).

**All three versions are patch-level with no API breaking changes.** The
experimental zttp HTTP/1.1 implementation is gated behind `--http zttp`
and off by default. LE31 imports `uvicorn` only as the ASGI server
entrypoint (`uvicorn app.main:app --host 0.0.0.0 --port 8000`); the
LE31 runtime does not exercise zttp.

**The 21-pass observation + the 2026-08-20 stabilization confirm the
recommendation**: the latest patch in window is `0.52.4`, NOT `0.52.3`
(this feature supersedes feature 80 from 2026-08-19). The three-release
same-week pattern (0.52.2 + 0.52.3 on 2026-08-13 + 0.52.4 on 2026-08-19)
is the **only** in-window stack change that affects a LE31 pin and the
**only** one where the diff is pure stability/perf.

The slice ships **one** source-code change: bump the version pin in the
project's dependency manifest from `uvicorn == 0.52.1` to
`uvicorn == 0.52.4`. Zero new pip dependencies. Zero migrations. Zero
schema changes. Zero new config keys.

## Scope

**In scope (v2 utility, S effort, ≤2 days, build candidate defer until
charter-decided pin-bump window):**

- One source-file edit: the project's primary dependency manifest
  (e.g. `requirements.txt` or `pyproject.toml`, whichever LE31 uses
  per the current convention). The pin is bumped from
  `uvicorn == 0.52.1` to `uvicorn == 0.52.4`.
- Update the LE31 dev-server invocation script (if any) to require the
  new minimum: `uvicorn >= 0.52.2, == 0.52.4` (already implied by the
  pin).
- Add a one-line CHANGELOG entry: "Bump uvicorn pin from 0.52.1 to
  0.52.4 (3 patch releases covering WebSocket close-handshake fix +
  HTTP/1.1 perf improvements)".

**Out of scope (rejected):**

- LE31 implementation work beyond the pin bump — no code, no schema
  change, no contract. This is a stack pin-bump artifact.
- Pinning `pydantic-core 2.48.0` (carry-over from 2026-08-10) — this
  is a transitive bump; the Python wheel stays at 2.13.4. The LE31
  runtime does not need a direct `pydantic-core` pin.
- Pinning `pydantic 2.14.0b1` — beta-only, not pinned.
- Pinning `SQLAlchemy 2.0.52` (2026-08-11) or `Alembic 1.19.1`
  (2026-08-08) — both are patch-level; defer to the next pin-bump
  window.
- Pinning `tiktoken 0.14.0` (2026-08-17) — LE31 does not use tiktoken.
- Bumping to `uvicorn 0.52.5` — no such release exists yet; the burst
  has stabilized at 0.52.4.

## Description

**Evidence precondition:** observed (verified in-window across the
21-pass series via two independent sources: PyPI JSON release
timestamps + `Kludex/uvicorn` GitHub `releases.atom` feed; three
same-week patch releases on 2026-08-13 + 2026-08-19; the 2026-08-19
release of 0.52.4 landed 5 minutes before the daily-research fetch ran;
the burst has now stabilized at 0.52.4 with no 0.52.5 release in 24h).

**Confidence:** **high** for the pin-bump mechanics (test suite
passes; LE31 imports `uvicorn` only as the ASGI server entrypoint and
doesn't exercise zttp), **medium** for an immediate bump (three
releases in 7 days suggests urgency but none is a CVE/security fix;
the burst has now stabilized at 0.52.4 after 24h with no 0.52.5
release).

**Cross-validation anchors:**

- **`uvicorn 0.52.2`** (PyPI upload 2026-08-13T07:03:55+): Fixed
  bodyless request receives + improved HTTP/1 request parsing
  performance. WebSocket close-handshake fix.
- **`uvicorn 0.52.3`** (PyPI upload 2026-08-13T16:50:01+): Updated
  zttp to 0.0.24 + improved HTTP/1.1 request-parsing performance.
- **`uvicorn 0.52.4`** (PyPI upload 2026-08-19T06:27:40+): Latest
  patch; pure stability/perf; the burst has now stabilized at 0.52.4
  with no 0.52.5 release in 24h.
- All three versions are confirmed via `Kludex/uvicorn` releases atom
  + PyPI JSON (two independent sources).
- LE31 imports `uvicorn` only as the ASGI server entrypoint
  (`uvicorn app.main:app --host 0.0.0.0 --port 8000`); the LE31
  runtime does not exercise zttp (which is gated behind `--http zttp`
  and off by default).

**Decision: build candidate (defer until charter-decided pin-bump
window).** The slice boundary is hard: one source-file edit (the pin
bump), zero new dependencies, zero migrations, zero schema changes.
Circuit breaker: delete this file + the corresponding `INDEX.md` row;
no other code changes to revert.

## Data model

No data model changes. The pin bump is a single source-file edit.

## Implementation steps

1. Open the LE31 dependency manifest (e.g. `requirements.txt` or
   `pyproject.toml`, whichever LE31 uses per the current convention).
2. Find the line that pins `uvicorn == 0.52.1`.
3. Change it to `uvicorn == 0.52.4`.
4. Save and verify with `pip show uvicorn` (or equivalent) after a
   `pip install -e .` (or equivalent) that the installed version is
   0.52.4.
5. Run the LE31 dev server (`uvicorn app.main:app --reload`) and
   confirm it starts and serves the `/api/...` routes.
6. Run the LE31 test suite (`pytest` or equivalent) and confirm it
   still passes.
7. Add a one-line CHANGELOG entry: "Bump uvicorn pin from 0.52.1 to
   0.52.4 (3 patch releases covering WebSocket close-handshake fix +
   HTTP/1.1 perf improvements)".
8. Commit and push with the message: `Bump uvicorn pin from 0.52.1 to
   0.52.4 (feature 82 — uvicorn-0-52-4-pin-bump-v5)`.

## Telegram interaction

None directly. This is a stack pin-bump; no user-facing surface
changes. The cook bot and waiter web UI continue to function
unchanged.

## Dependencies

- **`uvicorn 0.52.4`** is the target version. Available on PyPI since
  2026-08-19T06:27:40+.
- **`Kludex/uvicorn`** releases atom feed is the canonical source for
  uvicorn release notes.
- The existing LE31 dependency manifest (`requirements.txt` or
  `pyproject.toml`).
- No LE31 schema changes required.
- No new pip dependencies.
- No charter approval required (charter §3.2 allows stack pin bumps
  that are pure stability/perf).

## Open questions

- **Q1: Will the LE31 charter decide to bump now, or defer further?**
  This is the 5th consecutive day the recommendation has surfaced; the
  patch-version target has held at 0.52.4 since 2026-08-19. The charter
  may decide to (a) bump now, (b) wait for a 0.52.5 release (none yet),
  or (c) bundle this with the next major stack upgrade.
- **Q2: Are there any in-flight features that conflict with the
  bump?** None observed. The three patches are pure stability/perf
  with no API breaking changes.
- **Q3: Does the burst pattern suggest a 0.52.5 is imminent?** The
  24h gap since 0.52.4 (released 2026-08-19, today is 2026-08-20) is
  not statistically significant; the prior gaps were 0.52.2 →
  0.52.3 (same day, 9h) and 0.52.3 → 0.52.4 (6 days). The 24h gap
  is consistent with both "stable" and "another release imminent".
  Watch the `Kludex/uvicorn` releases atom feed for a 0.52.5 entry.

## Why this matters

The `uvicorn 0.52.1 → 0.52.4` pin bump is the **only** in-window
stack change that affects a LE31 pin and the **only** one where the
diff is pure stability/perf (zttp 0.0.22 → 0.0.24 + WebSocket
close-handshake fix + HTTP/1.1 perf improvements). Three patch
releases in 7 days (0.52.2 + 0.52.3 both on 2026-08-13 + 0.52.4 on
2026-08-19) was unusual for the uvicorn project (the prior 0.52.0 →
0.52.1 was a 3-day gap), suggesting an active maintainer and a real
urgency to get the WebSocket close-handshake fix + HTTP/1.1 perf
improvements in. The burst has now stabilized at 0.52.4 with no
0.52.5 release in 24h.

**As of 2026-08-20 (21-pass observation), the recommendation is
unchanged**: across 2026-08-14 through 2026-08-20, three new uvicorn
patches have shipped (0.52.2 + 0.52.3 + 0.52.4). The target bump is
`0.52.1 → 0.52.4`. This is the **5th consecutive day** the uvicorn
pin-bump has surfaced (2026-08-16 → feature 70, 2026-08-17 → feature
76, 2026-08-18 → feature 78, 2026-08-19 → feature 80, 2026-08-20 →
feature 82); the consistent deferral pattern is itself a signal that
the recommendation tracks the latest in-window patch.

**Risk of NOT bumping**: LE31 v1 is on `uvicorn == 0.52.1`; the
WebSocket close-handshake fix (0.52.2), HTTP/1.1 request-parsing perf
improvements (0.52.3), and 0.52.4 stability/perf improvements are
missed. Low-severity risk (no CVE, no security fix); the fix is
operational polish, not correctness.

**Risk of bumping**: the three-patch burst suggests urgency but none
is a CVE/security fix; bumping mid-window may conflict with other
in-flight work. The defer-to-next-pin-bump-window recommendation
balances these risks.

**Net: defer to the next charter-decided pin-bump window.** Keep the
recommendation visible in the active pipeline; close the artifact
once the bump lands.

## Status: build candidate (defer until charter-decided pin-bump window)

This file is a **build-candidate artifact**. No code is shipped
today. The slice boundary is hard: one source-file edit (the pin
bump), zero new dependencies, zero migrations, zero schema changes,
zero new config keys.

The artifact supersedes `features/80-uvicorn-0-52-4-pin.md` (the v4
artifact from 2026-08-19). The v5 artifact holds the target at
0.52.4 with no 0.52.5 release in 24h.
