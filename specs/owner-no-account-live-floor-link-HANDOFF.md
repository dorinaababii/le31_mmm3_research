# owner-no-account-live-floor-link — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/29-owner-no-account-live-floor-link.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `29`
- Slug: `owner-no-account-live-floor-link`
- Contract file: `features/29-owner-no-account-live-floor-link.md`
- Bucket: v2 owner-pains (read-only single-page owner surface)
- Linear parent: HMM-24 (Brainstorm 2026-08-04 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build.** No failed checks.

Evidence precondition: **observed** (3 in-window small-business repos
from the same author — `slotone`, `slipbook`, `shelftrack` — share the
no-account, ephemeral-link primitive; OpenAlex q3 surfaces the no-build
framework trend). Confidence: **medium**.

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
backend/app/main.py                          # include the new router
backend/app/models.py                        # new OwnerLink SQLModel
backend/app/routers/owner_link.py            # NEW — GET /owner/<token> + POST /owner/<token>/revoke
backend/app/bot/cook_bot.py                  # add /ownerlink
backend/app/templates/owner.html             # NEW — Jinja2 + htmx page
backend/README.md                            # note the new endpoint + bot command
```

No new dependencies. `htmx` is loaded from CDN at runtime; no
`requirements.txt` change.

## Endpoints and contracts added

- `GET /owner/<token>` — renders `owner.html`. No login. No cookies.
  Returns 410 Gone on expiry or unknown token.
- `POST /owner/<token>/revoke` — sets `revoked_at = now()`, returns
  204.
- Cook-bot `/ownerlink` — generates a fresh `token_urlsafe(32)`,
  stores SHA-256 hash, returns the full URL.

One new table:

```
OwnerLink  (id, token_hash TEXT UNIQUE, created_at, expires_at, revoked_at NULL)
```

Token is 256-bit random. Raw token lives in the URL only; database
stores only the SHA-256 hash. Default expiry: 12 h.

## Verification protocol (end-to-end acceptance path)

Follow this exact sequence. "OK" only when the literal user actions
behave as described.

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the
   contract file matches the frozen identifiers above. Mirror the
   identifiers back to the research-side Hermes before implementing.
2. **Stack**: `cd backend && pip install -U -r requirements.txt` —
   confirm FastAPI + uvicorn pins from features 25 + 27 resolve.
3. **Schema**: `init_db()` creates the `OwnerLink` table if absent.
4. **Run**: `uvicorn app.main:app --reload`.
5. **Generate**: in Telegram (cook role), `/ownerlink` → URL of the
   form `http://localhost:8000/owner/<token>`.
6. **Open**: open the URL on a fresh incognito window (no cookies, no
   login). Confirm the floor grid renders, last 10 orders appear,
   today's cover count is non-zero, prep-time histogram renders,
   reorder line appears if feature 26 is enabled.
7. **Auto-refresh**: leave the page open for 30 s and confirm the
   table grid updates when a state transition is committed in another
   session (htmx 10 s poll).
8. **Revoke**: `curl -X POST http://localhost:8000/owner/<token>/revoke`
   → 204. Reload page → 410 Gone.
9. **Expiry**: shorten the expiry in `config.py` to 5 s for the test,
   generate a link, wait 6 s, reload → 410 Gone.
10. **Privacy**: view source of the rendered page → confirm no
    customer names, no order-item text, no PII. Only counts and item
    count per order.
11. **Regression**: confirm existing flows (seat, order, serve, bill,
    tip) still work and that the existing role checks still gate the
    waiter UI.

## Rollback / feature-removal path

- Drop the `OwnerLink` table from `backend/app/models.py`.
- Delete `backend/app/routers/owner_link.py` and remove its
  `include_router` from `main.py`.
- Delete `backend/app/templates/owner.html`.
- Revert the `/ownerlink` command in `backend/app/bot/cook_bot.py`.
- No data migration needed; no data retention — `OwnerLink` rows are
  throwaway.

## What remains safe if removed

- No customer data, no historical state.
- The existing waiter UI and cook bot are unaffected.
- The privacy invariant is reinforced by the read-only design of the
  page (the page cannot store PII because it is rendered server-side
  from aggregate queries).

## Sign-off gap

External coding agent must mirror the five frozen identifiers
(Feature ID, slug, contract file path, bucket, Linear parent HMM-24)
back to the research-side Hermes before implementing. If any of
these conflict with what the agent sees locally, **stop and ask** —
do not silently rename.