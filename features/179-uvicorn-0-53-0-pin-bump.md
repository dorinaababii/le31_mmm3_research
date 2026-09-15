# Feature 179 — `uvicorn-0-53-0-pin-bump`

**Bucket:** v1 build candidate (stack maintenance)
**Filed:** 2026-09-15 by the LE31 daily-research cron
**Source:** Daily Research 2026-09-15, Pick A
**Gate:** PASS (v1 build candidate)

## Goal

Pin-bump the LE31 v1 stack from `uvicorn==0.52.4` to `uvicorn==0.53.0` and verify that the existing test suite + Telegram long-polling + FastAPI SSE paths still work end-to-end without behavior change.

## Scope

1. `pyproject.toml` (or the LE31-equivalent dependency file): replace `uvicorn==0.52.4` with `uvicorn==0.53.0`.
2. `uv.lock` (or equivalent): regenerated to reflect the new pin.
3. CI / smoke-test suite: confirm `pytest` still passes (or whatever LE31's CI is — confirm via `le31-conventions`).
4. End-to-end smoke: launch the LE31 FastAPI server with `uvicorn app.main:app` (or the LE31-equivalent entry-point), confirm `/health` returns 200, confirm at least one Telegram long-polling endpoint cycles (no consumer).
5. **Read the 0.53.0 release notes before bumping** (per `le31-feature-pipeline/SKILL.md` discipline): PyPI `uvicorn 0.53.0` upload_time is 2026-09-14T07:44:22Z; release.atom entry title = "Version 0.53.0" without detail. The agent must read the GitHub Release notes page (`https://github.com/encode/uvicorn/releases/tag/0.53.0`) for the changelog before committing.

## Out of scope

1. Any **behavior change** — this is a pin-bump, not a feature; the only acceptable change is "uvicorn version number went up, tests still pass".
2. Migration to a different ASGI server (hypercorn, granian, etc.). Out of scope.
3. Bumping any other LE31 pin today. The `SQLAlchemy 2.0.53` pin-bump candidate (released 2026-09-14T22:39:47Z) is queued behind this one — picked on the next pass that surfaces a uvicorn-confirmed-clean state.
4. Any AI integration. Charter §3.4 not triggered.

## Description

`uvicorn 0.53.0` was uploaded to PyPI on 2026-09-14T07:44:22Z (verified by `pypi.org/pypi/uvicorn/json`) and the GitHub Release `Version 0.53.0` was published 2026-09-14T07:35:46Z (verified by `releases_encode_uvicorn.atom`). This is the **FIRST new uvicorn stable in 26 days** — the previous stable, `uvicorn 0.52.4`, was uploaded 2026-08-19T06:00:54Z (released after the 0.52.3 same-day pair on 2026-08-13). LE31 currently pins `uvicorn==0.52.4`. Per the standing discipline (features 70/76/78/80/82/87/93/99/105/109/115/116), the pin-bump target has been stable at 0.52.4 for 26 days and now flips to 0.53.0.

Why pin-bump today and not wait:
- The 26-day stagnation is the longest observed in the LE31 series.
- The release is a true version change (0.52.x → 0.53.x), not a patch-bump.
- LE31's other stack pins are all current (fastapi 0.141.1 / 47-day stable; aiogram 3.31.0 / 19-day stable; sqlmodel 0.0.42 / 25-day stable; pydantic 2.13.5 / 47-day stable) — no other stack migration in flight.

## Data model

**No data model change.** This is a runtime-stack pin-bump; the SQLAlchemy models, alembic migrations, and `audit_logs` + `StockEntry` invariants are untouched.

## Implementation

1. Read the `uvicorn 0.53.0` release notes (`https://github.com/encode/uvicorn/releases/tag/0.53.0`) and confirm there is no documented breaking change that affects LE31's use of `uvicorn.run()` / `uvicorn.Config()` / `Server.serve()`.
2. Update the LE31 dependency file: `uvicorn==0.52.4` → `uvicorn==0.53.0`.
3. Regenerate the lock file (uv / pip-tools / equivalent — confirm via `le31-conventions`).
4. Run the test suite (`pytest` or equivalent). All tests must still pass.
5. Run the end-to-end smoke test: launch the server, hit `/health`, send a test Telegram long-polling request (or simulate one), confirm no error.
6. Commit: `chore(deps): bump uvicorn 0.52.4 → 0.53.0`.
7. Push to main.
8. File a `Done` status on the Linear sub-issue (HMM-242).

## Telegram interaction

None. This is a backend stack pin-bump with no Telegram-side change. The Telegram-bot long-polling is only verified by the smoke test in step 5 above (a simple "the long-polling endpoint still cycles" check, no actual user-visible interaction).

## Dependencies

1. **Read access to the LE31 dependency file** + `pyproject.toml` / `requirements.txt` / equivalent — confirm via `le31-conventions`.
2. **Read access to the LE31 CI / test suite** — confirm via `le31-conventions`.
3. **GitHub Release page** for `uvicorn 0.53.0` (`https://github.com/encode/uvicorn/releases/tag/0.53.0`) — verify release notes.
4. **Python 3.13** runtime (LE31 currently uses `python=3.13` per `pyproject.toml`).

## Open questions

1. **Is the LE31 dependency file `pyproject.toml` (uv) or `requirements.txt` (pip-tools)?** Confirm via `le31-conventions/SKILL.md` and `project-repo-hygiene/SKILL.md`. If `uv.lock` is the lock file, regenerate via `uv lock --upgrade uvicorn`. If `requirements.txt` + `pip-tools`, regenerate via `pip-compile`.
2. **Is there an ALB / load balancer / process supervisor in front of uvicorn that re-reads the entry-point command on deploy?** If so, the pin-bump is observable; if not, the deploy team must restart the LE31 process manually.
3. **Does the LE31 CI matrix include a Python 3.13 + uvicorn integration test that simulates long-polling?** If yes, that's the existing safety net. If no, the smoke test in step 5 of Implementation is the only end-to-end check.

## Why this matters

The `uvicorn` ASGI server is the runtime that serves the LE31 FastAPI backend, which is the runtime that drives the Telegram bot's long-polling, the FastAPI SSE endpoints, and the owner's htmx surface. A 26-day stagnation in uvicorn stable releases is unusual (the LE31 history shows uvicorn stable releases every 5–10 days in normal times). `0.53.0` is a new minor-version release and likely contains bug fixes + minor enhancements that the LE31 stack would benefit from (especially around WebSocket handling, graceful shutdown, and httptools / uvloop integration). The pin-bump is **low-risk, high-hygiene** — if the test suite passes, the upgrade is essentially free.

The 26-day stagnation pattern is worth noting: if `uvicorn 0.53.1` or `0.53.2` follows within 24–48h (the pattern from the `0.52.2 → 0.52.3 → 0.52.4` burst in August), the recommendation is to **wait for the burst to settle** before pinning. Per the LE31 pin-bump discipline, the pin target locks at the **first stable** after a 7-day quiet window — today is day-1 of the 0.53.0 release, so the discipline says **pin 0.53.0 now and watch for a quick-burst patch follow-up in the next 3 days**; if `0.53.1` appears within 7 days, file a follow-up pin-bump to `0.53.1` immediately.
