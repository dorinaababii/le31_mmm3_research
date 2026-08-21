# satisfecho-devnest-stack-shape-watch — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation combining two stack-shape peers, not a feature build.
> The slice boundary is hard: zero source-file edits, zero schema
> changes, zero new config keys. Read this *and*
> `features/89-satisfecho-devnest-stack-shape-watch.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `89`
- Slug: `satisfecho-devnest-stack-shape-watch`
- Contract file: `features/89-satisfecho-devnest-stack-shape-watch.md`
- Bucket: **v2 watch-list (stack-shape + JTBD observation)** — hard
  defer pending README read
- Linear parent: `HMM-114` (Research 2026-08-21 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on both peers;
`satisfecho/pos` 30★ +2★/24h + second push in 30h carry-over from
2026-08-20; `devnest-hq/restaurant-management-system` 1★ active push
4h before today's fetch, MIT license, README not yet read).

**Confidence:** **high** for the stack-shape match (both peers
described as Python FastAPI+SQLModel+Postgres+KDS+Billing+Inventory);
**high** for the `satisfecho/pos` AGPL block (charter §3.2 prohibits
GPL/AGPL dependencies in v1 regardless of README content); **medium**
for the `devnest` README confirmation (the description pattern
matches but the README has not been read; the actual code may
diverge from the description).

**Decision: watch-list continue; hard defer pending README read.**
The `devnest` README read is the single blocker for moving `devnest`
to priority 1 on the watch list. If the README confirms the
full-stack description + a clean license, this is the watch-list
upgrade of the 22-pass series. If the README shows a divergence
(e.g. SQLite-only, no Telegram surface, no `StockEntry` ledger),
the watch-list upgrade is rejected and `devnest` stays at low
priority.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-21).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/89-satisfecho-devnest-stack-shape-watch.md   # NEW (this artifact)
specs/satisfecho-devnest-stack-shape-watch-HANDOFF.md # NEW (this file)
INDEX.md                                                # EDIT: append one row to "Active feature pipeline" table (watch-list continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back** `features/89-satisfecho-devnest-stack-shape-watch.md`
   and confirm it matches the daily-research report's
   "satisfecho-devnest-stack-shape-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-21), pick slug
   (`satisfecho-devnest-stack-shape-watch`), feature path
   (`features/89-satisfecho-devnest-stack-shape-watch.md`), and Linear
   sub-issue ID.
3. **On the next daily-research pass**:
   a. Read the `devnest-hq/restaurant-management-system` README via
      `curl -sS` to
      `https://raw.githubusercontent.com/devnest-hq/restaurant-management-system/main/README.md`
      (or whatever branch the active push targets). Compare against
      the description: "Python FastAPI+SQLModel+Postgres+KDS+Billing+
      Inventory". Confirm the full-stack match + the license.
   b. Read the `satisfecho/pos` commit log via
      `curl -sS -H "Authorization: token $HERMES_GITHUB_TOKEN"`
      `"https://api.github.com/repos/satisfecho/pos/commits?since=2026-08-20T00:00:00Z"`.
      Confirm the +2★/24h + second push in 30h activity.
4. If the `devnest` README confirms full-stack + clean license, move
   `devnest` to watch-list priority 1 (above foodieshub, below
   longnick/satisfecho).
5. If the `satisfecho/pos` commit log shows actual code changes (not
   README-only), note the changes; the AGPL block is charter-level
   and will not change.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2 owner-pains` (the
watch-list bucket) with label `Feature`.

- Title: `Feature 89 — satisfecho-devnest-stack-shape-watch`.
- Body: the contract from
  `features/89-satisfecho-devnest-stack-shape-watch.md` (or a short
  summary + the file path).
- Parent: `HMM-114` (Research 2026-08-21 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/89-satisfecho-devnest-stack-shape-watch.md` and this
HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other
code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

The two peers in this watch are the highest-priority in-window
stack-shape matches for LE31. The AGPL block on `satisfecho/pos` is
charter-level and will not change; `satisfecho` is useful as a pattern
reference only (already covered by features 40/42). The `devnest` peer
is the closest **importable** stack-shape match in window (MIT, Python
FastAPI+SQLModel+Postgres+KDS+Billing+Inventory); the README read is
the single blocker for moving `devnest` to priority 1 on the watch
list. If the README confirms the description, this is the watch-list
upgrade of the 22-pass series.

## Carry-over history

This is the **NEW observation** (2026-08-21); no prior artifact
exists. Combines:

- The carry-over `satisfecho/pos` AGPL-blocked stack-shape match
  (already covered by features 40/42 from 2026-08-07 pass).
- The NEW `devnest-hq/restaurant-management-system` in-window active
  push (1★, MIT, Python FastAPI+SQLModel+Postgres+KDS+Billing+
  Inventory, README not yet read).
