# pronto-cafe-telegram-reminders-cross-section — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation of the in-window Pronto cross-section peer, not a
> feature build. The slice boundary is hard: zero source-file edits,
> zero schema changes, zero new config keys. Read this *and*
> `features/90-pronto-cafe-telegram-reminders-cross-section.md`
> before touching any code. Do not paste chat excerpts back into the
> build.

## Frozen identifiers (do not rename)

- Feature ID: `90`
- Slug: `pronto-cafe-telegram-reminders-cross-section`
- Contract file: `features/90-pronto-cafe-telegram-reminders-cross-section.md`
- Bucket: **v2 owner-pains (watch-list, cross-section peer)** — hard
  defer pending charter §3.1 surface-expansion review
- Linear parent: **TBD** (Brainstorm 2026-08-21 — daily, created in
  this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on Pronto; ★39
mid-adoption; TypeScript stack; WhatsApp + Telegram reminders;
self-hosted Docker; pushed 2026-08-19).

**Confidence:** **high** for the cross-section pattern (WhatsApp +
Telegram reminders is a direct cross-section to LE31's cook-bot
surface); **low** for the build implication (charter §3.1 says
Telegram-only; "expand to WhatsApp" is a charter-level decision).

**Decision: watch-list continue; hard defer pending charter §3.1
surface-expansion review.** The Pronto README read is the next
research-side action. The "expand to WhatsApp?" question is parked
pending charter approval.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job on 2026-08-21).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/90-pronto-cafe-telegram-reminders-cross-section.md   # NEW (this artifact)
specs/pronto-cafe-telegram-reminders-cross-section-HANDOFF.md # NEW (this file)
INDEX.md                                                       # EDIT: append one row to "Active feature pipeline" table (watch-list continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back**
   `features/90-pronto-cafe-telegram-reminders-cross-section.md`
   and confirm it matches the daily-brainstorm report's
   "pronto-cafe-telegram-reminders-cross-section" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-21), pick slug
   (`pronto-cafe-telegram-reminders-cross-section`), feature path
   (`features/90-pronto-cafe-telegram-reminders-cross-section.md),
   and Linear sub-issue ID.
3. **On the next daily-research pass**:
   a. Read the Pronto README via `curl -sS` to
      `https://raw.githubusercontent.com/SGrappelli/pronto/main/README.md`
      (or whatever branch the active push targets). Confirm the
      WhatsApp + Telegram reminders pattern.
   b. Track star velocity + push activity via
      `GET https://api.github.com/repos/SGrappelli/pronto` (with
      `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
4. If the Pronto README confirms the WhatsApp + Telegram reminders
   pattern + a public API surface, document the pattern in the LE31
   research notes (this artifact is the document).
5. **No build implied.** The pick is a watch-list observation. The
   "should LE31 expand to WhatsApp?" question is parked pending
   charter §3.1 surface-expansion review.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2 owner-pains` (the
watch-list bucket) with label `Feature`.

- Title: `Feature 90 — pronto-cafe-telegram-reminders-cross-section`.
- Body: the contract from
  `features/90-pronto-cafe-telegram-reminders-cross-section.md` (or
  a short summary + the file path).
- Parent: **TBD** (Brainstorm 2026-08-21 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/90-pronto-cafe-telegram-reminders-cross-section.md`
and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No
other code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

The Pronto cross-section peer is the **only in-window mid-adoption
(★25-50) peer** that combines: (a) small-business self-hosted POS,
(b) WhatsApp + Telegram reminders, (c) cafe/booking/CRM surface. The
pattern is direct and worth documenting. The cross-section signals
that the small-business self-hosted POS market is converging on
dual-channel bot reminders (Telegram + WhatsApp). LE31's charter
§3.1 currently says Telegram-only; the "expand to WhatsApp" question
is a charter-level decision that Pronto's existence supports but
does not yet require. The artifact is filed as a watch-list entry
with a clear re-evaluation trigger so the next research pass knows
what to look for.

## Carry-over history

This is the **NEW observation** (2026-08-21); no prior artifact
exists. Combines:

- The cross-section pattern from `SGrappelli/pronto` (`★39`, pushed
  2026-08-19, TypeScript, WhatsApp + Telegram reminders).
- The 22-pass observation that LE31's cook-bot surface is
  Telegram-only (charter §3.1) and the "expand to WhatsApp?"
  question is a charter-level surface-expansion decision.
