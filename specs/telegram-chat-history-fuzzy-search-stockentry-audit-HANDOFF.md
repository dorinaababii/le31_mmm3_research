# telegram-chat-history-fuzzy-search-stockentry-audit — HANDOFF

> **Slice for the research agent.** This is a passive parking-lot
> observation of the in-window `groupultra/telegram-search`
> cross-section peer, not a feature build. The slice boundary is
> hard: zero source-file edits, zero schema changes, zero new config
> keys. Read this *and*
> `features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md`
> before touching any code. Do not paste chat excerpts back into the
> build.

## Frozen identifiers (do not rename)

- Feature ID: `108`
- Slug: `telegram-chat-history-fuzzy-search-stockentry-audit`
- Contract file: `features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md`
- Bucket: **v2 owner-pains (parking-lot, future-audit-search-surface)**
  — hard defer pending charter §3 audit-surface review
- Linear parent: **HMM-139** (Brainstorm 2026-08-24 — daily, created in this cron)
- Linear sub-issue: **HMM-142** (create as a draft parking-lot artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on
`groupultra/telegram-search`; ★4,075 high community traction;
AGPL-3.0 license; TypeScript; MeiliSearch + PostgreSQL + Telegram
MTProto indexing; pushed 2026-08-21T12:13:15Z).

**Confidence:** **high** for the pattern (a high-volume Telegram
fuzzy-search architecture at 4k★ community traction validates that
the MeiliSearch + PostgreSQL + Telegram MTProto pattern scales);
**low** for the LE31-specific build implication (LE31 v1 doesn't
ship an audit-search surface; no owner signal of "I can't search the
historical StockEntry-by-Telegram-message trail" pain today; the v2
extension is a future-tense concern).

**Decision: parking-lot; hard defer pending owner-pain signal or
charter §3 audit-surface review.** The README read is the next
research-side action. The "should LE31 v2 add an audit-search surface
for the StockEntry-by-Telegram trail?" question is parked pending
charter approval.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job on 2026-08-24).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md   # NEW (this artifact)
specs/telegram-chat-history-fuzzy-search-stockentry-audit-HANDOFF.md # NEW (this file)
INDEX.md                                                              # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

- **Today**: verify that this `HANDOFF.md` exists + the
  `features/108-…md` contract file exists + the `INDEX.md` row was
  added + the `le31_daily_brainstorm_2026_08_24` Linear issue
  (HMM-139) was created with the parent body + the
  `le31_v1_core_mvp` Linear sub-issue (HMM-142) was created with the
  contract body and `Feature` label.
- **Daily (next 7 days)**: track `groupultra/telegram-search` star
  velocity via `GET
  https://api.github.com/repos/groupultra/telegram-search` (via
  `$HERMES_GITHUB_TOKEN`).
- **Daily (next 7 days)**: read the `groupultra/telegram-search`
  README + architecture documentation and confirm the MeiliSearch +
  PostgreSQL + Telegram MTProto indexing pattern (READ ONLY — no
  import, AGPL blocks anyway).
- **Re-check threshold**: if stars ≥5,000 OR ≥2 independent
  high-volume Telegram fuzzy-search peers with the same
  MeiliSearch+PostgreSQL+MTProto architecture, OR the LE31 owner
  signals an explicit "I can't search the historical
  StockEntry-by-Telegram-message trail" pain, the slice is
  un-deferred and becomes a v2 charter-question prompt.

## Linear sub-issue

- **Parent**: HMM-139 (Brainstorm 2026-08-24 — daily, project `le31
  Research`, status Done).
- **Sub-issue**: HMM-142 (Feature, project `le31 v1 — Core MVP`,
  status Backlog). Body has the full contract body; label `Feature`.

## Rollback path

**Fully reversible.** Delete
`features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md`
+ this `HANDOFF.md` + the `INDEX.md` row + the
`le31_daily_brainstorm_2026_08_24` parent issue + the
`le31_v1_core_mvp` sub-issue (HMM-142). Zero risk of code regression
(no code changed).

## Why this matters (for the research agent)

The 2026-08-24 brainstorm pass surfaces `groupultra/telegram-search`
as the only in-window ≥1k★ Telegram chat-history fuzzy-search peer
with a documented MeiliSearch + PostgreSQL + Telegram MTProto
indexing architecture. The cross-section insight informs LE31 v2
owner-pains audit-search surface for the `StockEntry`-via-Telegram
trail (features 30 + 49 v2 extension). AGPL-3.0 license blocks v1
code-import per charter §3.2 but the indexing pattern is reusable
for future v2 owner-pains extension. The artifact records the
fuzzy-search architecture for future v2-AI iteration.

## Carry-over history

- **2026-08-24**: created from brainstorm 2026-08-24 Pick C.
- **Next pass (2026-08-25)**: down-stream daily-research pass should
  read `groupultra/telegram-search` README + architecture
  documentation and confirm the MeiliSearch + PostgreSQL + Telegram
  MTProto indexing pattern. Add `groupultra/telegram-search` to the
  daily-research watch list (5-repo watch) to track star velocity +
  push activity.

If the destination repo's research-side Hermes instance finds the
README read changes the gate verdict (e.g., the indexing pipeline
turns out to be batch-only with no incremental update), the slice
should be amended rather than re-created.
