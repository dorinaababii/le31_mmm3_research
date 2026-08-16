# telegapper-telegram-mini-app-privacy-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/72-telegapper-telegram-mini-app-privacy-watch.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `72`
- Slug: `telegapper-telegram-mini-app-privacy-watch`
- Contract file: `features/72-telegapper-telegram-mini-app-privacy-watch.md`
- Bucket: **v2-AI (watch-list)** — defer; LE31 v1 ships a chat-based
  bot, not a Mini App
- Linear parent: `HMM-85` (Research 2026-08-16 — daily)
- Linear sub-issue: **TBD** (create as a draft watch-list record)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (arXiv API — TeleGapper paper arXiv:2608.13390, cs.CR,
2026-08-13T15:51:18Z, authors Luca Ferrari, Mariano Ceccato,
Luca Verderame).

**Confidence:** **high** for the empirical findings (59.4% / 78.8% /
none); **medium** for the v2-AI applicability to LE31 (LE31 v1 is a
chat-based bot, not a Mini App; the Mini App surface is a future
v2-AI extension of the waiter web UI from feature 02).

**Decision: defer (v2-AI watch-list).** The slice boundary is hard:
one Markdown file update, zero source code changes, zero migrations,
zero new dependencies. Circuit breaker: delete this file + the
corresponding `INDEX.md` row; no other code changes to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2-AI, the slicing discipline
   inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-research` (this pick came from the daily research
   job on 2026-08-16).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/72-telegapper-telegram-mini-app-privacy-watch.md   # NEW (this artifact)
specs/telegapper-telegram-mini-app-privacy-watch-HANDOFF.md # NEW (this file)
INDEX.md                                                     # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config keys.
Zero new pip dependencies.

## Verification protocol

After the artifact ships:

1. **Read back** `features/72-telegapper-telegram-mini-app-privacy-watch.md`
   and confirm it matches the daily-research report's
   "telegapper-telegram-mini-app-privacy" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-16), pick slug
   (`telegapper-telegram-mini-app-privacy`), feature path
   (`features/72-telegapper-telegram-mini-app-privacy-watch.md`),
   and Linear sub-issue ID.
3. **On any future v2-AI scope decision** that proposes a Telegram
   Mini App surface for the LE31 waiter side, reference this artifact
   to anchor the privacy-policy obligation.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID
`fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`
(label ID `972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`).

- Title: `Feature 72 — telegapper telegram mini app privacy watch`.
- Body: the contract from
  `features/72-telegapper-telegram-mini-app-privacy-watch.md` (or a
  short summary + the file path).
- Parent: `HMM-85` (Research 2026-08-16 — daily).
- Status: `Backlog`.

## Rollback path

Delete `features/72-telegapper-telegram-mini-app-privacy-watch.md`
and this HANDOFF.md. Remove the corresponding row from `INDEX.md`.
No other code changes to revert. No data migration to revert.

## Why this matters (for the coding agent)

The TeleGapper paper establishes a **concrete 2026-08 baseline
data point** for the Telegram-Mini-App privacy compliance gap. If
LE31 ever ships a Telegram Mini App surface (a natural extension
of the waiter web UI from feature 02), the privacy-policy
obligation must be **explicit**:

- An application-specific privacy policy (the 78.8% finding flags
  default-policy reliance as a transparency gap).
- An audit of third-party network traffic (the 59.4% finding flags
  undisclosed third-party contact as a transparency gap).
- A consent / opt-out mechanism (the "none" finding flags the
  absence of consent as a compliance gap).

This artifact records the data point so future v2-AI scope work
does not have to rediscover it.

**Risk of NOT tracking:** a future v2-AI scope decision on a
Telegram Mini App surface would lack the TeleGapper baseline and
would have to rediscover the privacy-policy obligation. **The
artifact prevents that rediscover cost.**

**Risk of over-tracking:** the artifact is a research-note;
over-use of it would be in a future scope decision (not this
slice). **No over-tracking risk today.**
