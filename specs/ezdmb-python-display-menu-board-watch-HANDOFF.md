# ezdmb-python-display-menu-board-watch — HANDOFF

> **Slice for the research agent.** This is a passive parking-lot
> observation of the in-window Python ezdmb cross-section peer, not
> a feature build. The slice boundary is hard: zero source-file
> edits, zero schema changes, zero new config keys. Read this *and*
> `features/91-ezdmb-python-display-menu-board-watch.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `91`
- Slug: `ezdmb-python-display-menu-board-watch`
- Contract file: `features/91-ezdmb-python-display-menu-board-watch.md`
- Bucket: **v2 owner-pains (parking-lot, future-display-surface)**
  — hard defer pending charter §3.1 surface-expansion review
- Linear parent: **TBD** (Brainstorm 2026-08-21 — daily, created in
  this cron)
- Linear sub-issue: **TBD** (create as a draft parking-lot artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GET on ezdmb; ★25
mid-adoption; Python stack; single-purpose digital menu board;
pushed 2026-08-18).

**Confidence:** **high** for the pattern ("single-purpose Python
display surface is buildable in ★25 by a solo developer"); **low**
for the build implication (charter §3.1 says two primary surfaces;
"add a front-of-house display surface" is a charter-level decision).

**Decision: parking-lot; hard defer pending charter §3.1
surface-expansion review.** The ezdmb README read is the next
research-side action. The "should LE31 add a third surface?" question
is parked pending charter approval.

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
features/91-ezdmb-python-display-menu-board-watch.md   # NEW (this artifact)
specs/ezdmb-python-display-menu-board-watch-HANDOFF.md # NEW (this file)
INDEX.md                                                # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back** `features/91-ezdmb-python-display-menu-board-watch.md`
   and confirm it matches the daily-brainstorm report's
   "ezdmb-python-display-menu-board-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-21), pick slug
   (`ezdmb-python-display-menu-board-watch`), feature path
   (`features/91-ezdmb-python-display-menu-board-watch.md`), and
   Linear sub-issue ID.
3. **On the next daily-research pass**:
   a. Read the `ezdmb` README via `curl -sS` to
      `https://raw.githubusercontent.com/justinmichaelvieira/ezdmb/main/README.md`
      (or whatever branch the active push targets). Confirm the
      single-purpose Python display pattern.
   b. Track star velocity + push activity via
      `GET https://api.github.com/repos/justinmichaelvieira/ezdmb`
      (with `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
4. **No build implied.** The pick is a parking-lot observation. The
   "should LE31 add a third surface?" question is parked pending
   charter §3.1 surface-expansion review.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2 owner-pains` (the
parking-lot bucket) with label `Feature`.

- Title: `Feature 91 — ezdmb-python-display-menu-board-watch`.
- Body: the contract from
  `features/91-ezdmb-python-display-menu-board-watch.md` (or a short
  summary + the file path).
- Parent: **TBD** (Brainstorm 2026-08-21 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/91-ezdmb-python-display-menu-board-watch.md` and this
HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other
code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

The `ezdmb` peer proves a single-purpose Python display surface is
**buildable in ★25 by a solo developer**. The pattern is method-
adjacent (Python display, minimal config) but not domain-adjacent
(ezdmb is menu-board, not restaurant-POS). The cross-section question
("should LE31 v2 grow a third surface?") is a charter-level
surface-expansion question that the artifact explicitly defers. The
pick is filed as a parking-lot entry with a clear re-evaluation
trigger so the next research pass knows what to look for.

## Carry-over history

This is the **NEW observation** (2026-08-21); no prior artifact
exists. Combines:

- The cross-section pattern from `justinmichaelvieira/ezdmb` (★25,
  pushed 2026-08-18, Python, single-purpose digital menu board).
- The 22-pass observation that LE31's charter §3.1 says two primary
  surfaces (waiter web UI + cook Telegram bot) and the "add a third
  surface?" question is a charter-level surface-expansion decision.
