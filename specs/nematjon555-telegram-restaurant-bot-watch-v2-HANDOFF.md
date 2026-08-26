# nematjon555-telegram-restaurant-bot-watch-v2 — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/117-nematjon555-telegram-restaurant-bot-watch-v2.md`
> before touching any code. This is a **watch-list continue / 2nd
> pass** slice, NOT a build slice. The only deliverable is a
> README read + gate-verdict update in the next daily-research pass
> (2026-08-27). Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `117`
- Slug: `nematjon555-telegram-restaurant-bot-watch-v2`
- Contract file: `features/117-nematjon555-telegram-restaurant-bot-watch-v2.md`
- Bucket: **v2 owner-pains watch-list continue** — defer
- Linear parent: **HMM-151** (Research 2026-08-26 — daily, created in this cron)
- Linear sub-issue: **HMM-154** (Feature)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**inferred** (Python + aiogram 3 + restaurant-domain description =
first such peer in 27-pass series; confidence medium for
framework-match, low for LE31-specific urgency because 0★ + 2.83-day
idle = one-off-implementation pattern). README read pending.

**Confidence:** **medium** for the framework + domain match (Python +
aiogram 3 + restaurant domain features = direct cross-section for
LE31 charter §3.1), **low** for the LE31-specific urgency (0★ + 2.83-
day idle = one-off-implementation pattern; no LICENSE file detected =
charter §3.2 import blocked).

**Decision: watch-list continue (defer).** The slice boundary is
narrow: one-time README read + one-line summary in the next
daily-research report. Zero new dependencies, zero migrations, zero
schema changes. Circuit breaker: demote to low-confidence watch-list
and stop tracking in 7 days if neither stars nor pushes move.

## Mandatory LE31 skill list (load these first)

External coding agent (or the next-pass daily-research cron) MUST
load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-research` (research observation discipline; no fabrication).
3. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-26).
4. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the project owner before starting. Do not invent LE31 conventions.

## Files to touch

| File | Action | Notes |
|---|---|---|
| `/opt/data/le31-daily-research-2026-08-27.md` | append | one-line summary in the "Adjacent evidence" section based on the README read |
| `/opt/data/INDEX.md` | (no change) | watch-list continues; no new row needed unless the gate verdict changes |

**Files NOT to touch:**
- `backend/**` — no code changes; watch-list continue only.
- `frontend/**` — no UI changes.
- `.env` / config files — no config changes.
- `PROJECT_CHARTER.md` — no charter changes.

## Verification protocol reference

Per `skills/le31-conventions/SKILL.md` and the research discipline:
- **README read**: fetch the peer's README via curl (no browser):
  ```
  curl -sSL https://raw.githubusercontent.com/nematjon555/telegram-restaurant-delivery-bot/main/README.md
  ```
  (or `master` if the default branch is `master`; check via the GitHub
  API or the repo's GET endpoint).
- **Gate verdict update**: re-evaluate the seven checks from the LE31
  conventions skill. If the README confirms a reusable pattern with a
  permissive license, escalate to a build candidate (charter §3.2 may
  need a decision on the no-license status). If the README confirms a
  one-off deployment, demote to low-confidence watch-list and stop
  tracking in 7 days.
- **Star velocity + push activity re-check**: re-fetch the peer's
  GitHub repo GET and verify whether either stars or pushes have moved
  since the 2026-08-26 baseline (0★ + last push 2026-08-23T10:38:41Z).
- **No fabrication**: do not invent README content. If the README is
  empty or unavailable, record that as the finding.

## Rollback path

**N/A — no code changes were made.** The watch-list continue is
passive; the only rollback option is to delete the feature file + the
corresponding `INDEX.md` row (if it was added) + the corresponding
HANDOFF.md file.

## Carry-over chain (provenance)

This slice is the **2nd pass** of the same peer observation:

| Feature | Day | Date | Notes |
|---|---|---|---|
| 110 | day 1 | 2026-08-25 | First observation (no README read yet) |
| **117** | **day 2** | **2026-08-26** | **2nd pass; README read pending (this artifact)** |

## Stop conditions

Pause and ask the user if any of the following is true:
- The README content is ambiguous and the gate verdict cannot be
  determined.
- The peer has gained a LICENSE file (re-gate; charter §3.2 may now
  allow code import).
- The peer has gained ≥1★ (re-gate; star velocity may indicate
  active maintenance).

## Mirror-back confirmation

Before coding, mirror back: slice ID (`117`), required skills
(le31-conventions + le31-research + le31-daily-research +
le31-feature-pipeline), verification protocol (README read + gate
verdict update + star velocity + push activity re-check + no
fabrication), and rollback path (delete feature file + INDEX.md row
+ HANDOFF.md). Confirm or correct each, then begin.