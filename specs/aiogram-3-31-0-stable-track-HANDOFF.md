# aiogram-3-31-0-stable-track — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/116-aiogram-3-31-0-stable-track.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `116`
- Slug: `aiogram-3-31-0-stable-track`
- Contract file: `features/116-aiogram-3-31-0-stable-track.md`
- Bucket: **v2 utility (stack pin-bump)** — build candidate defer
- Linear parent: **HMM-151** (Research 2026-08-26 — daily, created in this cron)
- Linear sub-issue: **HMM-153** (Feature)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window on 2026-08-26 via two independent
sources: PyPI JSON upload timestamp 2026-08-26T00:00:42Z +
`aiogram/aiogram` GitHub `releases.atom` feed entry "Telegram Bot API
10.3" at 2026-08-25T23:59:50Z; the release is the first aiogram
stable in the 27-pass series since 3.30.0 from 2026-07-17, 5.6 weeks
ago; the 5.6-week cadence is typical for aiogram).

**Confidence:** **high** for the pin-bump mechanics (aiogram 3.x is
API-stable; LE31 imports aiogram only as the Telegram-bot framework;
no breaking changes for LE31's current usage), **medium** for an
immediate bump (the 5.6-week gap is normal but the release aligns
with upstream Telegram Bot API 10.3 which may have subtle behavior
changes; confirm via the Telegram-bot smoke test before bumping).

**Decision: build candidate (defer until charter-decided pin-bump
window).** Likely bundled with feature 115 (`uvicorn 0.52.4`
pin-bump). The slice boundary is hard: one source-file edit (the pin
bump), zero new dependencies, zero migrations, zero schema changes.
Circuit breaker: delete this file + the corresponding `INDEX.md` row;
no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-26).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the project owner before starting. Do not invent LE31 conventions.

## Files to touch

| File | Action | Notes |
|---|---|---|
| `backend/requirements.txt` (or equivalent manifest) | modify | bump `aiogram` pin from current (permissive or 3.30.0) to `aiogram == 3.31.0` |
| `CHANGELOG.md` | append | one-line entry: "Bump aiogram to 3.31.0 (Telegram Bot API 10.3 alignment)" |
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
- **Telegram-bot smoke test**: start a bot with the new aiogram pin,
  send a test message, verify the bot responds with the expected
  ack/callback flow. Use a sandbox/test chat ID; do not test in
  production.
- **No new warnings**: `aiogram` startup logs should be free of new
  deprecation warnings; if any appear, treat as a regression and
  revert.
- **No client-visible change**: the LE31 cook Telegram bot must
  behave identically before and after the bump (Telegram Bot API
  10.3 alignment is supposed to be transparent).

## Rollback path

**Fully reversible.** Revert the single-line manifest change; delete
the CHANGELOG entry; remove the `/opt/data/INDEX.md` row. Zero risk
of code regression (no code changed). Charter untouched.

If the bump causes a regression (e.g., a new aiogram deprecation
warning breaks the LE31 Telegram-bot smoke test), revert the
manifest change immediately and surface the regression in the next
daily-research pass as a new "aiogram 3.31.0 regression" watch-list
entry.

## Carry-over chain (provenance)

This slice is the **first aiogram-pin-bump feature** in the LE31
daily-research series. Pattern reference: structurally identical to
the `uvicorn 0.52.4` pin-bump carry-overs (features 27, 70, 76, 78,
80, 82, 87, 93, 99, 105, 109, 115). The artifact is the persistent
build-candidate record; if the team opens a pin-bump window, this
artifact should be bundled with feature 115 in a single PR.

| Feature | Day | Date | Notes |
|---|---|---|---|
| **116** | **day 1** | **2026-08-26** | **aiogram 3.31.0 stable (this artifact; first aiogram pin-bump)** |

## Mirror-back confirmation

Before coding, mirror back: slice ID (`116`), required skills
(le31-conventions + le31-v1-feature-pattern + le31-handoff-spec +
le31-daily-research + le31-feature-pipeline), verification protocol
(test suite + Telegram-bot smoke test + no new warnings + no
client-visible change), and rollback path (revert single-line
manifest change). Confirm or correct each, then begin.