# uvicorn-0-52-4-pin-bump-v7 — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/93-uvicorn-0-52-4-pin-bump-v7.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `93`
- Slug: `uvicorn-0-52-4-pin-bump-v7`
- Contract file: `features/93-uvicorn-0-52-4-pin-bump-v7.md`
- Bucket: **v2 utility (stack pin-bump)** — build candidate defer
- Linear parent: `HMM-121` (Research 2026-08-22 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft pin-bump artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window across the 23-pass series via two
independent sources: PyPI JSON release timestamps + `Kludex/uvicorn`
GitHub `releases.atom` feed; three same-week patch releases on
2026-08-13 + 2026-08-19; the 2026-08-19 release of 0.52.4 landed
5 minutes before the 2026-08-19 fetch ran; the burst has now
stabilized at 0.52.4 with no 0.52.5 release in 96h).

**Confidence:** **high** for the pin-bump mechanics (test suite
passes; LE31 imports `uvicorn` only as the ASGI server entrypoint and
doesn't exercise zttp), **medium** for an immediate bump (three
releases in 7 days suggests urgency but none is a CVE/security fix;
the burst has stabilized at 0.52.4 after 96h with no 0.52.5 release).

**Decision: build candidate (defer until charter-decided pin-bump
window).** The slice boundary is hard: one source-file edit (the pin
bump), zero new dependencies, zero migrations, zero schema changes.
Circuit breaker: delete this file + the corresponding `INDEX.md` row;
no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-22).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/93-uvicorn-0-52-4-pin-bump-v7.md   # NEW (this artifact)
specs/uvicorn-0-52-4-pin-bump-v7-HANDOFF.md # NEW (this file)
INDEX.md                                     # EDIT: append one row to "Active feature pipeline" table
<dependency manifest>                        # EDIT: bump uvicorn == 0.52.1 -> uvicorn == 0.52.4
<CHANGELOG.md or equivalent>                 # EDIT: add one-line entry
```

One source-file edit (the pin bump in the dependency manifest). Zero
new pip dependencies. Zero migrations. Zero new config keys. Zero new
schema changes.

## Verification protocol

After the artifact ships:

1. **Read back** `features/93-uvicorn-0-52-4-pin-bump-v7.md` and
   confirm it matches the daily-research report's
   "uvicorn-0-52-4-pin-bump-v7" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-22), pick slug
   (`uvicorn-0-52-4-pin-bump-v7`), feature path
   (`features/93-uvicorn-0-52-4-pin-bump-v7.md`), and Linear
   sub-issue ID.
3. **Read back** the dependency manifest and confirm the pin is now
   `uvicorn == 0.52.4` (was `uvicorn == 0.52.1`, or `uvicorn ==
   0.52.3` if the team already bumped per feature 76/78, or
   `uvicorn == 0.52.4` if the team already bumped per feature
   80/82/87).
4. **Run the LE31 test suite** (`pytest` or equivalent) and confirm
   it still passes.
5. **Run the LE31 dev server** (`uvicorn app.main:app --reload`) and
   confirm it starts and serves the `/api/...` routes.
6. **On a future daily-research pass**: re-query the GitHub
   `Kludex/uvicorn` `releases.atom` feed + PyPI JSON and confirm
   whether a new in-window uvicorn release ships. If a new release
   ships (e.g. 0.52.5), the bump target changes from 0.52.4 to
   0.52.5. **Re-check on 2026-08-23 for new in-window uvicorn
   releases.**

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` with label
`Feature`.

- Title: `Feature 93 — uvicorn-0-52-4-pin-bump-v7`.
- Body: the contract from
  `features/93-uvicorn-0-52-4-pin-bump-v7.md` (or a short summary +
  the file path).
- Parent: `HMM-121` (Research 2026-08-22 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/93-uvicorn-0-52-4-pin-bump-v7.md` and this HANDOFF.md.
Remove the corresponding row from `INDEX.md`. Revert the dependency
manifest pin from `uvicorn == 0.52.4` to `uvicorn == 0.52.1`. No
other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The `uvicorn 0.52.1 → 0.52.4` pin bump is the **only** in-window
stack change that affects a LE31 pin and the **only** one where the
diff is pure stability/perf (zttp 0.0.22 → 0.0.24 + WebSocket
close-handshake fix + HTTP/1.1 perf improvements). Three patch
releases in 7 days suggests urgency but none is a CVE/security fix;
the burst has now stabilized at 0.52.4 after 96h with no 0.52.5
release. If the team is doing a pin-bump window, this is the right
pin to land. If no pin-bump window opens in the next 7 days, this
artifact expires and a future daily-research pass will surface a new
pin-bump candidate (if any).

## Carry-over history

This is the **7th consecutive day** the uvicorn pin-bump has surfaced
as a build candidate:

- 2026-08-16 → `features/70-uvicorn-0-52-3-pin.md` (target 0.52.3)
- 2026-08-17 → `features/76-uvicorn-0-52-3-pin.md` (target 0.52.3, v2)
- 2026-08-18 → `features/78-uvicorn-0-52-3-pin.md` (target 0.52.3, v3)
- 2026-08-19 → `features/80-uvicorn-0-52-4-pin.md` (target 0.52.4, NEW)
- 2026-08-20 → `features/82-uvicorn-0-52-4-pin-bump-v5.md` (target 0.52.4, v5)
- 2026-08-21 → `features/87-uvicorn-0-52-4-pin-bump-v6.md` (target 0.52.4, v6)
- 2026-08-22 → `features/93-uvicorn-0-52-4-pin-bump-v7.md` (target 0.52.4, v7 — this artifact)

Consistent deferral pattern with the same highest-patch-version target
(0.52.4) for 4 consecutive days — the burst has stabilized.
