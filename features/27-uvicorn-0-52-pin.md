# Feature 27 — Uvicorn 0.52 Pin

## Goal

Pin `uvicorn>=0.52.0` (specifically `~=0.52.1`) in
`backend/requirements.txt` so the SSE cook-channel (feature 23) and every
future FastAPI 0.141.x consumer run on the in-window tested combination —
removing a hidden cross-version drift risk that yesterday's research missed.

## Scope

**In scope (v1):**
- Add `uvicorn>=0.52.0,<0.53` (or `uvicorn~=0.52.1`) to
  `backend/requirements.txt`.
- Update `backend/README.md` dev-setup snippet to include
  `pip install -U -r requirements.txt` so contributors pick up the new pin.

**Out of scope (v1):**
- Pinning the worker class (`uvicorn.workers.UvicornWorker` for gunicorn) —
  LE31 v1 uses uvicorn directly via `uvicorn app.main:app --reload`.
- Adopting `uvloop` — separate dependency, separate decision.
- Switching to `granian` or `hypercorn` — out of charter scope.

## Description

Yesterday's daily research (2026-08-03) recorded FastAPI 0.141.0 +
`0.140.12/0.140.13` SSE fixes in window but **missed the matching uvicorn
major release**. Today (2026-08-04) the subagent fetched
`https://pypi.org/pypi/uvicorn/json` and confirmed:

- **`0.52.0`** — 2026-07-29 — fresh major release.
- **`0.52.1`** — 2026-08-01 — patch release inside the 7-day window.

uvicorn `0.52.x` is the canonical runtime for FastAPI `0.141.x`. The
worker-shutdown behaviour in `0.51.x` and `0.52.x` differs in ways that
matter for long-lived SSE connections (feature 23). Pinning the
combination in `requirements.txt` removes a real regression-risk path
that would otherwise surface as flaky SSE tests on first local-dev
session after Pick A is shipped.

The change is one line in `requirements.txt` plus a one-line README
update. No code changes. No schema change. No migration.

## Data model

None. This is a dependency pin only.

## Implementation

1. **Edit `backend/requirements.txt`** — change (or add)
   `uvicorn>=0.52.0,<0.53` (or `uvicorn~=0.52.1` to lock to the in-window
   tested combination).
2. **Edit `backend/README.md`** — append `pip install -U -r requirements.txt`
   to the dev-setup snippet.
3. **Manual verification**:
   - `cd backend && rm -rf .venv && python -m venv .venv && source .venv/bin/activate && pip install -U -r requirements.txt`
   - Confirm `uvicorn --version` prints `0.52.x`.
   - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` — confirm
     the existing `/api/health` returns 200.
   - Confirm the SSE endpoint from feature 23 (Pick A), once implemented,
     can be hit with `curl -N http://localhost:8000/api/cook/stream` and
     receives the heartbeat `:` line within 15s without worker-shutdown
     errors in the uvicorn log.

## Telegram interaction

None. This is a pure dependency pin.

## Dependencies

- [25-fastapi-frontend-dev-loop.md](../features/25-fastapi-frontend-dev-loop.md)
  — already pinned `fastapi>=0.141.0` yesterday; this contract is the
  matching uvicorn pin.
- [23-sse-cook-channel.md](../features/23-sse-cook-channel.md) —
  verification protocol relies on this pin; SSE worker-shutdown behaviour
  is the regression risk being removed.

## Open questions

- Should we lock to `~=0.52.1` (strict pin) or `>=0.52.0,<0.53`
  (minor-floats-up)? Default: `~=0.52.1` to lock the in-window tested
  combination; bump explicitly when needed.
- Does the production systemd unit need updating? No — it shells out to
  `uvicorn` directly; the pin travels with `requirements.txt`.

## Why this matters

This is the cheapest possible pick with the smallest possible blast
radius — one line in `requirements.txt` — and it removes a hidden
regression-risk path that would otherwise surface only on the first
local-dev session that wires up SSE. The Pick-A verification protocol
in `specs/sse-cook-channel-HANDOFF.md` calls for SSE smoke tests; those
tests would be flaky on uvicorn `0.51.x` because of worker-shutdown
differences.