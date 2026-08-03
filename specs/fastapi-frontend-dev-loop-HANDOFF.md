# fastapi-frontend-dev-loop — HANDOFF

> **Slice for the coding agent.** Read this *and* `features/25-fastapi-frontend-dev-loop.md`
> before touching any code. This is the prerequisite for `sse-cook-channel`.

## Frozen identifiers (do not rename)

- Feature ID: `25`
- Slug: `fastapi-frontend-dev-loop`
- Contract file: `features/25-fastapi-frontend-dev-loop.md`
- Bucket: v1 ops / DX (pure tooling pin)
- Linear parent: HMM-16 (Research 2026-08-03 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Decision: **build**. All seven checks answered in the contract file under
"LE31 gate verdict". No failed checks. Evidence precondition: **observed**
(FastAPI 0.141.0 release notes; agent already imports `app.frontend` once it
exists). Confidence: **high**.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions`.
2. `le31-v1-feature-pattern`.
3. `le31-handoff-spec`.
4. `le31-daily-research`.

## Files the slice touches

```
backend/requirements.txt                 # pin fastapi>=0.141.0,<0.142.0
backend/app/main.py                      # replace StaticFiles mount with app.frontend(check_dir='auto')
backend/README.md                        # document the dev loop
```

No schema impact. No migration.

## Endpoints and contracts added

None — this is a tooling pin. The `/` static-mount behavior is unchanged
from the user's perspective.

## Verification protocol (end-to-end acceptance path)

1. Load all four mandatory LE31 skills.
2. Mirror the five frozen identifiers back to research-side Hermes.
3. Confirm `fastapi>=0.141.0,<0.142.0` resolves: `pip install -r
   backend/requirements.txt`.
4. `uvicorn app.main:app --reload`; open `http://localhost:8000/`;
   confirm `index.html` still loads (same content as before).
5. Edit `index.html` (add a comment); reload the browser tab; confirm
   the change appears without a server restart (proves `auto` mount is
   live, not cached).
6. `curl http://localhost:8000/`; confirm 200 and the same HTML.
7. Smoke-test feature 23 (SSE cook channel) once it lands — its SSE
   endpoints depend on the `0.140.13` streaming fixes.

## Rollback / feature-removal path

- Revert `fastapi>=0.141.0,<0.142.0` to the previous pin.
- Revert `app.frontend(check_dir='auto')` to the prior static mount (or
  remove it if there wasn't one).
- No data migration, no data retention.

## What remains safe if removed

- The dev loop reverts to the prior configuration.
- No customer data, no historical state, no schema impact.

## Sign-off gap

External coding agent must mirror the five frozen identifiers back to
research-side Hermes before implementing. If any conflict, **stop and ask**.