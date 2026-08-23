# pronto-watch-v3 — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation of the in-window `SGrappelli/pronto` cross-section
> peer, not a feature build. The slice boundary is hard: zero
> source-file edits, zero schema changes, zero new config keys,
> zero code imports from pronto. Read this *and*
> `features/100-pronto-watch-v3.md` before touching any code. Do
> not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `100`
- Slug: `pronto-watch-v3`
- Contract file: `features/100-pronto-watch-v3.md`
- Bucket: **v2 owner-pains (watch-list, cross-section peer)** —
  hard defer pending charter §3.1 surface-expansion review
- Linear parent: `HMM-129` (Research 2026-08-23 — daily, created in
  this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct-repo GET today:
`SGrappelli/pronto` 40★, 12 forks, **NEW push 2026-08-22T19:10:54Z**
~11.3h before today's fetch, `updated_at` 2026-08-22T19:11:18Z;
size 5706KB, +295KB / +5.5% overnight; license MIT; topics include
`cafe`, `telegram`, `whatsapp`, `nextjs`, `supabase`, `docker`,
`self-hosted`, `booking`, `pos`, `crm`, `inventory`).

**Confidence:** **high** for the 3-day sustained maintainer activity
(direct-repo GET is author-controlled + the size delta is concrete
evidence of active code work), **low** for the build implication
(charter §3.1 says Telegram-only; "expand to WhatsApp?" is a
charter-level decision; full stack mismatch with LE31).

**Decision: watch-list continue; hard defer pending charter §3.1
surface-expansion review.** The slice boundary is hard: zero code
imports from pronto, zero source-file edits, zero migrations, zero
schema changes. Circuit breaker: delete this file + the
corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-23).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/100-pronto-watch-v3.md              # NEW (this artifact)
specs/pronto-watch-v3-HANDOFF.md             # NEW (this file)
INDEX.md                                     # EDIT: append one row to "Active feature pipeline" table (watch-list continue entry)
```

Zero source-file edits outside the research artifacts. Zero code
imports from pronto. Zero pin bumps. Zero schema changes.

## Verification protocol

After the artifact ships:

1. **Read back** `features/100-pronto-watch-v3.md` and confirm it
   matches the daily-research report's "pronto-watch-v3" pick
   description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-23), pick slug
   (`pronto-watch-v3`), feature path
   (`features/100-pronto-watch-v3.md`), and Linear sub-issue ID.
3. **On a future daily-research pass**: re-query the GitHub
   `SGrappelli/pronto` repo via direct-repo GET and confirm whether
   new in-window maintainer activity, stars, or forks appear. If
   new maintainer activity ships (e.g. another push in the next 24h),
   the watch-list entry should be updated to feature 102
   (`pronto-watch-v4`). **Re-check on 2026-08-24.**
4. **Optional next-pass deep-read**: read the pronto README + commit
   log via raw curl
   (`https://raw.githubusercontent.com/SGrappelli/pronto/main/README.md`
   + `https://github.com/SGrappelli/pronto/commits/main`) to confirm
   what the maintainer is working on.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2 owner-pains` with label
`Feature`.

- Title: `Feature 100 — pronto-watch-v3`.
- Body: the contract from
  `features/100-pronto-watch-v3.md` (or a short summary + the file
  path).
- Parent: `HMM-129` (Research 2026-08-23 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/100-pronto-watch-v3.md` and this HANDOFF.md. Remove
the corresponding row from `INDEX.md`. No other code changes to
revert. No data migration to revert.

## Why this matters (for the research agent)

The 3-day sustained maintainer activity + the +295KB overnight size
delta is the **strongest in-window cross-section peer signal** for
LE31's cook-Telegram-bot surface observed across the 24-pass series.
The maintainer is back to active development after the carry-over
2026-08-20 baseline stagnation. Pronto is the closest peer to LE31's
cook-Telegram-bot cross-section surface (WhatsApp + Telegram reminders,
self-hosted Docker); the Telegram-reminder pattern is the relevant
LE31 adjacency. The artifact is the persistent watch-list record so
future research passes can compare against this baseline.

## Carry-over history

This is the **3rd consecutive day** the pronto observation has surfaced
as a watch-list entry:

- 2026-08-21 → `features/90-pronto-cafe-telegram-reminders-cross-section.md`
  (day-1 observation; the inaugural cross-section peer watch)
- 2026-08-22 → `features/94-pronto-watch-v2.md` (day-2 observation;
  +1★/24h + +1 fork/24h + new push)
- 2026-08-23 → `features/100-pronto-watch-v3.md` (day-3 observation;
  +0★/24h + +0 forks/24h + new push + **+295KB size delta**,
  **this artifact**)