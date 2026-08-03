# Feature 25 — FastAPI Frontend Dev Loop

## Goal

Adopt FastAPI `>=0.141.0` in `backend/requirements.txt` and use the new
`app.frontend(check_dir='auto')` convenience so the dev loop (edit
`index.html` → reload browser → see change) stops requiring manual static-mount
configuration, and so the SSE streaming fixes shipped in `0.140.13 / 0.140.12
/ 0.141.1` are available for feature 23 (`sse-cook-channel`).

## Scope

**In scope (v1):**
- Pin `fastapi>=0.141.0,<0.142.0` in `backend/requirements.txt`.
- Replace the manual `StaticFiles` mount in `backend/app/main.py` (if any) with
  `app.frontend(check_dir='auto')`.
- Verify the existing `index.html` still serves at `/` and `/index.html`.
- Document the dev loop in `backend/README.md`.

**Out of scope (v1):**
- Production static-file serving (still nginx / a real CDN in production).
- New FastAPI features beyond `app.frontend(check_dir='auto')`.

## Description

FastAPI 0.141.0 (released 2026-07-29, confirmed in
`/tmp/le31-daily-2026-08-03/fastapi-releases.atom`) adds
`app.frontend(check_dir='auto')` — when called at FastAPI startup, it looks
for a `frontend/` directory at `cwd`, then `cwd/..`, then `cwd/../frontend`,
and mounts the first one it finds as the static root at `/`. LE31's planned
layout (charter §4.4) has `index.html` at the repo root and the FastAPI entry
at `backend/app/main.py` — the new `auto` check picks the right one without
the dev agent having to compute relative paths.

The 0.140.13 / 0.140.12 patch releases also fixed SSE / JSONL streaming
`status_code` and line-splitting. Feature 23 (`sse-cook-channel`) needs both.

## Data model

No schema impact. Pure tooling pin.

## Implementation

1. **Edit `backend/requirements.txt`** — change `fastapi==...` (or whatever the
   current pin is) to `fastapi>=0.141.0,<0.142.0`.
2. **Edit `backend/app/main.py`** — replace any `StaticFiles(...)` mount for
   the root with `app.frontend(check_dir='auto')`. If there's no current
   static mount, add it.
3. **Verify** — `cd backend && uvicorn app.main:app --reload`, open
   `http://localhost:8000/`, confirm `index.html` loads.
4. **Document** — add a 3-line section to `backend/README.md` describing the
   auto-mount and where to put the static UI.

## Telegram interaction

None.

## Dependencies

- None — this is the prerequisite for feature 23 (`sse-cook-channel`).

## Open questions

- Should the pin be `>=0.141.0,<0.142.0` (tight) or `>=0.141.0` (loose)?
  Default tight; bump to loose once 0.142.x is observed in the daily-research
  window and verified compatible.
- Should we also pin `uvicorn[standard]` to a matching minor? Not strictly
  required; FastAPI 0.141.0's release notes don't change uvicorn coupling.

## Why this matters

The active FastAPI release cadence in the 2026-07-27..08-03 window (10
releases, including the `app.frontend(check_dir='auto')` convenience and four
SSE / JSONL streaming fixes) is a small but cumulative dev-velocity win. Pinning
to `>=0.141.0` is the cheapest way to claim those wins — one line in
`requirements.txt` — and is a hard prerequisite for feature 23
(`sse-cook-channel`) which depends on the SSE fixes. Without this pin, every
LE31 coding agent has to re-derive the dev-loop mount path or skip the SSE
convenience; with it, they don't.