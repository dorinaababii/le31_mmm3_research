# uvicorn-0-52-pin — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/27-uvicorn-0-52-pin.md` before touching any code. Do not
> paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `27`
- Slug: `uvicorn-0-52-pin`
- Contract file: `features/27-uvicorn-0-52-pin.md`
- Bucket: v1 ops (one-line pin; no code, no schema)
- **Linear parent: HMM-20 (Research 2026-08-04 — daily)**
- **Linear sub-issue: HMM-23, `le31 v1 — Core MVP` project, label `Feature`**
- **Patch (2026-08-05, Pick C)**: the parent of this slice is now also
  referenced by HMM-28 (Research 2026-08-05 — daily) as a carry-over
  with a one-line doc note about the `encode/uvicorn` →
  `Kludex/uvicorn` repo transfer. See `specs/uvicorn-0-52-pin-HANDOFF.md`
  for the matching patch. No code change.

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered
in the contract file under "LE31 gate verdict". **Decision: build.**
No failed checks.

Evidence precondition: **observed** (uvicorn 0.52.0 + 0.52.1 release
notes; FastAPI 0.141.x compatibility matrix). Confidence: **high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract
   back).
4. `le31-daily-research` (this pick came from the daily research job).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/requirements.txt       # add uvicorn~=0.52.1 (or uvicorn>=0.52.0,<0.53)
backend/README.md              # dev-setup snippet: pip install -U -r requirements.txt
```

Two files. No code change. No schema change. No migration.

## Endpoints and contracts added

None. This is a dependency pin only.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Clean install**: `cd backend && rm -rf .venv && python -m venv
   .venv && source .venv/bin/activate && pip install -U -r
   requirements.txt`.
3. **Version check**: `uvicorn --version` must print `0.52.x`. If it
   prints `0.51.x`, the pin didn't take — re-check the `requirements.txt`
   format.
4. **Smoke**: `uvicorn app.main:app --reload --host 0.0.0.0 --port
   8000` — confirm `/api/health` returns 200 in <500ms.
5. **Cross-pin check**: confirm `pip freeze | grep -E
   '^(fastapi|uvicorn)=='` shows `fastapi==0.141.x` AND
   `uvicorn==0.52.x` together.
6. **SSE pre-flight (if feature 23 is already merged)**: `curl -N
   http://localhost:8000/api/cook/stream` and confirm the heartbeat
   `:` line arrives within 15s without any worker-shutdown warnings
   in the uvicorn log. If feature 23 is not yet merged, skip this step
   and record as "covered by feature 23 verification once it lands".
7. **Regression**: confirm all existing routes still respond
   (`/api/tables`, `/api/health`, the OpenAPI `/docs`).

## Rollback / feature-removal path

- Revert `backend/requirements.txt` to drop the `uvicorn` pin (or set
  to a wider range).
- Revert `backend/README.md` if needed.
- No data migration, no data retention, no state — pure dependency
  pin.

## What remains safe if removed

- No customer data, no historical state.
- All routes continue to function with any uvicorn that FastAPI 0.141.x
  supports — this pin is a *narrowing*, not a new dependency.
- Removing it is functionally equivalent to pre-pin behaviour.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-20)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** — do
not silently rename.

> **Patch (2026-08-05, Pick C)**: the uvicorn GitHub repository moved
> from `encode/uvicorn` to `Kludex/uvicorn`. The release.atom URL is now
> `https://github.com/Kludex/uvicorn/releases.atom`. The PyPI pin is
> unaffected. No code change. If the coding agent uses any
> GitHub-watch URL in CI, badges, or release notes, update it to the
> `Kludex/uvicorn` path.