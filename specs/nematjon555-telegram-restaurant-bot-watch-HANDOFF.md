# nematjon555-telegram-restaurant-bot-watch — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation of the in-window `nematjon555/telegram-restaurant-delivery-bot`
> cross-section peer, not a feature build. The slice boundary is
> hard: zero source-file edits, zero schema changes, zero new config
> keys. Read this *and*
> `features/110-nematjon555-telegram-restaurant-bot-watch.md`
> before touching any code. Do not paste chat excerpts back into
> the build.

## Frozen identifiers (do not rename)

- Feature ID: `110`
- Slug: `nematjon555-telegram-restaurant-bot-watch`
- Contract file: `features/110-nematjon555-telegram-restaurant-bot-watch.md`
- Bucket: **v2 owner-pains (watch-list, defer)** — peer is
  informative for LE31 v2 cook-assistant transport-layer
  architecture (cross-section for the Telegram-bot surface) but
  not actionable as a build today.
- Linear parent: TBD (Research 2026-08-25 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via GitHub Search API +
`ghsearch_aiogram_restaurant` query; peer `nematjon555/telegram-restaurant-delivery-bot`
created in window; Python + aiogram 3 + restaurant domain
features; pushed 2026-08-23T10:38:41Z).

**Confidence:** **medium** for the framework-match (Python +
aiogram is LE31's stack; peer's aiogram 3 matches LE31's pinned
`aiogram 3.30.0`); **low** for the LE31-specific build implication
(0★ = no community traction; no observed pain at scale; license
= None detected blocks any code-import per charter §3.2).

**Decision: watch-list defer (hard defer until stars ≥1 OR peer
README reveals a reusable pattern).** The slice boundary is hard:
zero source-file edits, zero schema changes, zero new config
keys. The watch-list tracking tests whether the peer gains
traction or reveals a reusable pattern.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-25).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/110-nematjon555-telegram-restaurant-bot-watch.md   # NEW (this artifact)
specs/nematjon555-telegram-restaurant-bot-watch-HANDOFF.md # NEW (this file)
INDEX.md                                                    # EDIT: append one row to "Active feature pipeline" table (watch-list defer entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

- **Today**: verify that this `HANDOFF.md` exists + the
  `features/110-…md` contract file exists + the `INDEX.md` row was
  added + the `Research 2026-08-25 — daily` Linear issue was created
  with the parent body + the `le31_v2_owner_pains` Linear sub-issue
  was created with the contract body and `Feature` label.
- **Daily (next 7 days)**: track `nematjon555/telegram-restaurant-delivery-bot`
  star velocity via
  `GET https://api.github.com/repos/nematjon555/telegram-restaurant-delivery-bot`
  (via `$HERMES_GITHUB_TOKEN`).
- **Tomorrow (2026-08-26)**: read the
  `nematjon555/telegram-restaurant-delivery-bot` README + commit
  log + Python source (READ ONLY — no import) and confirm:
  - Does the peer have a usable pattern for menu + table reservation
    in a Telegram bot that LE31 v2 cook-assistant could borrow?
  - Does the peer's Excel integration reveal a v2 owner-pains pattern
    (spreadsheet-friendly workflows)?
  - Does the peer have a license? (License = None detected in GitHub
    API response.)
- **Re-check threshold**: if stars ≥1 OR the README reveals a
  reusable pattern OR ≥3 independent aiogram-restaurant bot peers
  converge on the same pattern, the slice is un-deferred and becomes
  a v2 charter-question prompt.
- **Drop threshold**: if the peer remains 0★ for 7 consecutive
  days with no meaningful pushes, surface in the next daily-research
  pass as a "drop" signal (remove from watch-list).

## Rollback path

**Fully reversible.** Delete this file + the corresponding
`INDEX.md` row. Zero risk of code regression (no code changed).

## Carry-over chain (provenance)

This slice is the **first in-window aiogram-restaurant bot peer**
in the 26-pass daily-research series. There is no carry-over chain
— this is the **inaugural entry** for the
`nematjon555-telegram-restaurant-bot-watch` slug. Future daily-
research passes may add `nematjon555-telegram-restaurant-bot-watch-v2`
+ `-v3` if the peer gains traction.

## Stop conditions

Pause and ask the user if any of the following is true:
- The peer reaches ≥1★ within the next 7 days (would trigger
  gate re-evaluation).
- The peer README reveals a reusable pattern that maps to a
  v2 LE31 build candidate (would trigger a new build pick).
- The peer's GitHub repository is deleted or made private (would
  trigger a "drop" signal).
- The peer is found to have a license (would re-open the
  code-import question per charter §3.2).
- Verification fails twice on the same root cause.

## Mirror-back confirmation

Before coding (or in this case, before tracking), mirror back:
slice ID (`110`), required skills (le31-conventions +
le31-v1-feature-pattern + le31-handoff-spec + le31-daily-research +
le31-feature-pipeline), verification protocol (star velocity +
README read + push cadence), and rollback path (delete file +
INDEX.md row). Confirm or correct each, then begin tracking.
