# solo-operator-floor-pin — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/32-solo-operator-floor-pin.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `32`
- Slug: `solo-operator-floor-pin`
- Contract file: `features/32-solo-operator-floor-pin.md`
- Bucket: v1 owner-pains (web-only; no new client)
- Linear parent: HMM-32 (Brainstorm 2026-08-05 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: build.** No failed checks.

Evidence precondition: **reported** (5 HN solo-founder SaaS threads in
window share the pattern; objectIDs 44767231, 44742032, 44479824, 44571534).
Confidence: **medium**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/config.py                            # NEW: OWNER_PIN_HASH, OWNER_PIN_TTL_HOURS
backend/app/cli.py                               # NEW: rotate_owner_pin subcommand
backend/app/routers/owner_pin.py                 # NEW: GET /pin/<code>, GET /api/owner_pin/state
backend/app/templates/owner_pin.html             # NEW: stripped-down live view
backend/app/static/css/print-prep.css            # NEW: shared print stylesheet (also feature 34)
backend/app/main.py                              # register owner_pin router; lifespan CLI hook
backend/app/auth.py                              # NEW or extend: signed-cookie helper
backend/README.md                                # note the new CLI subcommand + PIN rotation
```

No new dependencies. No Alembic migration (charter §3.2 — `init_db()` for
v1).

## Endpoints and contracts added

Two new routes:

- `GET /pin/<code>` — bcrypt-verifies `<code>` against `OWNER_PIN_HASH`;
  on success sets a signed cookie (`owner_pin_session`, 12 h TTL) and
  renders `owner_pin.html`. Wrong PIN returns 401 with constant-time
  response (~250 ms regardless of validity).
- `GET /api/owner_pin/state` — returns JSON: `{floor: [...], alerts: [...],
  voids: [...]}`. Reads from existing tables only.

One new config field:

```python
OWNER_PIN_HASH         # bcrypt of a 4-digit numeric PIN, set at first boot
OWNER_PIN_TTL_HOURS    # default 12; cookie TTL
```

One new CLI subcommand:

```
python -m app.cli rotate_owner_pin
  # Generates a new random 4-digit PIN, re-bcrypts, writes to .env.
  # Logs the new PIN to stdout exactly once.
```

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn pins from features 25 + 27 resolve.
3. **Config**: confirm `OWNER_PIN_HASH` is set (auto-generated at first
   boot if absent). Note the printed PIN.
4. **Run**: `uvicorn app.main:app --reload`; confirm the existing flows
   (seat, order, serve, bill, tip) still respond.
5. **Wrong PIN**: in browser, navigate to `http://localhost:8000/pin/0000`
   → 401 page with constant-time response.
6. **Right PIN**: navigate to `http://localhost:8000/pin/<correct-pin>`
   → owner_pin.html renders with floor + alerts + voids panels.
   Browser DevTools confirms `owner_pin_session` cookie set with the
   configured TTL.
7. **Cookie reuse**: navigate to `http://localhost:8000/api/owner_pin/state`
   in the same browser → JSON payload returns floor + alerts + voids.
8. **Cookie expiry**: change `OWNER_PIN_TTL_HOURS=0`, restart server →
   the cookie is set with max-age 0 and `/api/owner_pin/state` returns
   401. Revert the TTL.
9. **Rotation**: run `python -m app.cli rotate_owner_pin` → new PIN
   printed. The old PIN now returns 401; the new PIN works.
10. **Regression**: confirm existing flows still work; confirm the
    append-only `StockEntry` ledger is unaffected (no new writes
    expected).

## Rollback / feature-removal path

- Remove `owner_pin.router` from `backend/app/main.py`.
- Delete `backend/app/routers/owner_pin.py` and
  `backend/app/templates/owner_pin.html`.
- Delete `OWNER_PIN_HASH` and `OWNER_PIN_TTL_HOURS` from
  `backend/app/config.py`.
- Delete `backend/app/cli.py` (or strip the `rotate_owner_pin`
  subcommand).
- No data migration needed; no data retention.

## What remains safe if removed

- No customer data, no historical state.
- The append-only `StockEntry` ledger is unaffected (this feature
  reads from `Batch`, `StockEntry`, `Table_`, `Visit`, `Bill`; never
  writes).
- The privacy invariant holds (no new identity is created; the cookie
  is a bearer secret, not a customer account).
- The owner can simply stop issuing the URL and the system behaves
  exactly as before. Feature 29 (`owner-no-account-live-floor-link`)
  still serves waiters on shift.

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-32)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.
