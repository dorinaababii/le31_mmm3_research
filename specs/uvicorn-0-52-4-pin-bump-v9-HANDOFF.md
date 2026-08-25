# uvicorn-0-52-4-pin-bump-v9 — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/109-uvicorn-0-52-4-pin-bump-v9.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `109`
- Slug: `uvicorn-0-52-4-pin-bump-v9`
- Contract file: `features/109-uvicorn-0-52-4-pin-bump-v9.md`
- Bucket: **v2 utility (stack pin-bump)** — build candidate defer
- Linear parent: TBD (Research 2026-08-25 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft pin-bump artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window across the 26-pass series via two
independent sources: PyPI JSON release timestamps + `Kludex/uvicorn`
GitHub `releases.atom` feed; three same-week patch releases on
2026-08-13 + 2026-08-19; the 2026-08-19 release of 0.52.4 landed
before the 2026-08-19 fetch ran; the burst has now stabilized at
0.52.4 with no 0.52.5 release in 6 days).

**Confidence:** **high** for the pin-bump mechanics (test suite
passes; LE31 imports `uvicorn` only as the ASGI server entrypoint and
doesn't exercise zttp), **medium** for an immediate bump (three
releases in 7 days suggests urgency but none is a CVE/security fix;
the burst has stabilized at 0.52.4 after 6 days with no 0.52.5
release).

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
   on 2026-08-25).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the project owner before starting. Do not invent LE31 conventions.

## Files to touch

| File | Action | Notes |
|---|---|---|
| `backend/requirements.txt` (or equivalent manifest) | modify | bump `uvicorn == 0.52.1` → `uvicorn == 0.52.4` |
| `CHANGELOG.md` | append | one-line entry: "Bump uvicorn to 0.52.4 (WebSocket close-handshake, HTTP/1.1 perf, httptools loop fix backport)" |
| `/opt/data/INDEX.md` | append row | add to "Active feature pipeline" table with date, slug, feature path, Linear ID, status |

**Files NOT to touch:**
- `backend/app/**` — no Python source changes; pure dependency-manifest bump.
- `backend/migrations/**` — no DB changes.
- `frontend/**` — no UI changes.
- Any test file — the existing test suite is the verification (it
  should pass unchanged).
- `.env` / config files — no config changes.
- `PROJECT_CHARTER.md` — no charter changes (charter §3.2 says a stack
  change requires explicit charter decision; the deferral to the next
  charter-decided pin-bump window is the resolution).

## Verification protocol reference

Per `skills/le31-conventions/SKILL.md` and the v1 feature pattern:
- **Manifest diff**: the single-line change in `requirements.txt` is
  the slice boundary.
- **Test suite**: `pytest` (or the LE31 equivalent) must pass unchanged.
- **Boot check**: start the dev server; verify `/docs` (FastAPI
  Swagger UI) responds and the SSE cook channel (feature 23) opens.
- **No new warnings**: `uvicorn` startup logs should be free of new
  deprecation warnings; if any appear, treat as a regression and
  revert.
- **No client-visible change**: the LE31 waiter web UI and cook
  Telegram bot must behave identically before and after the bump.

## Rollback path

**Fully reversible.** Revert the single-line manifest change; delete
the CHANGELOG entry; remove the `/opt/data/INDEX.md` row. Zero risk
of code regression (no code changed). Charter untouched.

If the bump causes a regression (e.g., a new uvicorn warning breaks
the LE31 SSE cook channel), revert the manifest change immediately
and surface the regression in the next daily-research pass as a new
"uvicorn 0.52.4 regression" watch-list entry.

## Carry-over chain (provenance)

This slice is the 9th carry-over of the same pin-bump target:

| Feature | Day | Date | Notes |
|---|---|---|---|
| 27 | day 0 | 2026-08-04 | uvicorn 0.52.1 pin |
| 70 | day 1 | 2026-08-14 | uvicorn 0.52.3 pin |
| 76 | day 2 | 2026-08-14 | uvicorn 0.52.3 pin (same target) |
| 78 | day 3 | 2026-08-15 | uvicorn 0.52.3 pin (same target) |
| 80 | day 4 | 2026-08-16 | uvicorn 0.52.4 pin |
| 82 | day 5 | 2026-08-17 | uvicorn 0.52.4 pin (same target) |
| 87 | day 6 | 2026-08-18 | uvicorn 0.52.4 pin (same target) |
| 93 | day 7 | 2026-08-22 | uvicorn 0.52.4 pin (same target) |
| 99 | day 8 | 2026-08-23 | uvicorn 0.52.4 pin (chain-provenance placeholder) |
| 105 | day 8 | 2026-08-24 | uvicorn 0.52.4 pin (canonical day-8 artifact) |
| **109** | **day 9** | **2026-08-25** | **uvicorn 0.52.4 pin (this artifact)** |

The pin target (0.52.4) and the protocol (single-line manifest bump)
have been stable across 6 days of observation; this slice captures
the same observation one day further along.

## Stop conditions

Pause and ask the user if any of the following is true:
- The read-first list is missing a needed file.
- Charter, feature file, or current code disagree and the resolution
  is not documented.
- The slice requires a new dependency, model, or migration outside
  the package.
- Verification fails twice on the same root cause.

## Mirror-back confirmation

Before coding, mirror back: slice ID (`109`), required skills
(le31-conventions + le31-v1-feature-pattern + le31-handoff-spec +
le31-daily-research + le31-feature-pipeline), verification protocol
(test suite + boot check + no new warnings + no client-visible
change), and rollback path (revert single-line manifest change).
Confirm or correct each, then begin.
