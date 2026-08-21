# Feature 89 — satisfecho-devnest-stack-shape-watch

> **NEW observation (2026-08-21).** Combines the carry-over
> `satisfecho/pos` AGPL-blocked stack-shape match (features 40/42)
> with the NEW `devnest-hq/restaurant-management-system` in-window
> active push (1★, MIT, Python FastAPI+SQLModel+Postgres+KDS+Billing+
> Inventory, README not yet read).
> Bucket: **v2 watch-list (stack-shape + JTBD observation)** — hard
> defer pending README read.

## Goal

Track the two highest-priority in-window stack-shape matches for LE31
(the AGPL-blocked `satisfecho/pos` + the MIT-licensed but unverified
`devnest-hq/restaurant-management-system`) and read the
`devnest-hq/restaurant-management-system` README in the next pass to
confirm the full-stack FastAPI+SQLModel+Postgres+KDS+Billing+Inventory
match.

## Scope

**In scope:**
- Daily direct-repo `GET https://api.github.com/repos/satisfecho/pos`
  (via `$HERMES_GITHUB_TOKEN`).
- Daily direct-repo `GET https://api.github.com/repos/devnest-hq/restaurant-management-system`
  (via `$HERMES_GITHUB_TOKEN`).
- Reading the `devnest-hq/restaurant-management-system` README in the
  next daily-research pass to confirm the full-stack description.
- Reading the `satisfecho/pos` commit log + README diff to confirm the
  +2★/24h + second push in 30h activity (carry-over from 2026-08-20 +
  2026-08-21).

**Out of scope (v1 / v2):**
- Importing any code from `satisfecho/pos` (AGPL-3.0 blocks LE31 v1
  import per charter §3.2).
- Importing any code from `devnest-hq/restaurant-management-system`
  until the README confirms full-stack + license clarity.
- Building any feature based on either codebase.

## Description

The two highest-priority in-window stack-shape matches for LE31:

### `satisfecho/pos`

| Date | Stars | Δ stars | Forks | pushed_at | updated_at | License |
|---|---|---|---|---|---|---|
| 2026-08-07 (baseline) | 22★ | — | 8 forks | 2026-08-02 | — | (not checked) |
| 2026-08-10 | 25★ | +3★/24h, +0★/72h | 9 forks | — | — | (not checked) |
| 2026-08-19 | 28★ | +0★/24h, +0★/72h | 9 forks | 2026-08-13T14:04:11Z (6 days idle) | — | **AGPL-3.0** (NEW finding) |
| 2026-08-20 | 28★ | +0★/24h, +3★/7d | 9 forks | 2026-08-20T05:27:20Z (NEW push — first activity since 2026-08-13 = 7 days idle broken 66 min before fetch) | 2026-08-20T05:28:07Z | AGPL-3.0 (carry-over) |
| 2026-08-21 | 30★ | **+2★/24h (FIRST positive movement since 2026-08-10), +5★/7d cumulative** | 9 forks (+1 fork/7d) | 2026-08-20T14:57:25Z (~15h before today's fetch — **second push in past 30h**) | 2026-08-20T15:49:09Z | **AGPL-3.0 (carry-over)** |

**Verdict:** Strongest in-window stack match (FastAPI+SQLModel+Postgres+KDS+WS, Python) but **AGPL blocks LE31 v1 import** per charter §3.2 (which prohibits GPL/AGPL dependencies in v1). Already covered by features 40/42. The +2★/24h + second push in 30h + 7-day idle break is a real signal of returning maintainer activity + first star growth since the idle. **Read the commit log + README diff in the next pass.**

### `devnest-hq/restaurant-management-system`

| Date | Stars | Δ stars | Forks | pushed_at | updated_at | License | Size |
|---|---|---|---|---|---|---|---|
| 2026-08-15 (baseline) | 1★ | — | 0 forks | — | — | MIT | 424KB |
| 2026-08-21 | 1★ | +0★/24h, +0★/7d | 1 fork (+1 fork/7d) | **2026-08-21T02:30:28Z (4h before today's fetch — NEW push)** | 2026-08-20T22:04:10Z | MIT | 424KB |

**Verdict:** **Closest direct LE31-stack match in window** (Python FastAPI+SQLModel+Postgres+KDS+Billing+Inventory — the full LE31 feature surface from features 01–07). **First in-window push observed** for this peer since the 2026-08-15 baseline. **README not yet read; if the README confirms full-stack FastAPI+SQLModel+Postgres+KDS+Billing+Inventory, this is the highest-priority watch-list upgrade.** MIT license (clean for LE31 v1 import, pending README confirmation). Fails the gate today (1★ + active development + no README read; defer until next pass).

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation, not a feature build.

## Implementation

1. Read the `devnest-hq/restaurant-management-system` README in the
   next daily-research pass (raw `curl -sS` to
   `https://raw.githubusercontent.com/devnest-hq/restaurant-management-system/main/README.md`
   or whatever branch the active push targets).
2. If the README confirms the full-stack description + a clean
   license, move `devnest` to watch-list priority 1 (above foodieshub,
   below longnick/satisfecho).
3. Read the `satisfecho/pos` commit log + README diff to confirm the
   +2★/24h + second push in 30h activity. Look for license
   clarification (AGPL-3.0 blocks LE31 v1 import regardless of any
   README update).
4. Continue daily direct-repo GET on both peers.

## Telegram interaction

None. This is a passive observation; no cook or manager action.

## Dependencies

- `$HERMES_GITHUB_TOKEN` for the daily direct-repo GETs (already in
  `/opt/data/.env`).

## Open questions

- Does the `devnest-hq/restaurant-management-system` README confirm the
  full-stack FastAPI+SQLModel+Postgres+KDS+Billing+Inventory match?
- Does the `devnest` README include a sample schema that LE31 could
  compare against feature 01 (`Table` model) + feature 02 (`Order` +
  `OrderItem` models) + feature 03 (`StockEntry` ledger model) +
  feature 04 (menu photo OCR) + feature 05 (`Bill` + `Payment` models)
  + feature 06 (`Visit` demographics model) + feature 07 (demand
  forecast)?
- Does the `satisfecho/pos` commit log show actual code changes vs.
  README-only changes in the past 30h?
- Does the `satisfecho/pos` README clarify the AGPL license (e.g. with
  a "commercial license available" clause that would unblock LE31 v1
  import)?

## Why this matters

The two peers in this watch are the highest-priority in-window
stack-shape matches for LE31. The AGPL block on `satisfecho/pos` is
charter-level and will not change; `satisfecho` is useful as a pattern
reference only (already covered by features 40/42). The `devnest` peer
is the closest **importable** stack-shape match in window (MIT, Python
FastAPI+SQLModel+Postgres+KDS+Billing+Inventory); the README read is
the single blocker for moving `devnest` to priority 1 on the watch
list. If the README confirms the description, this is the watch-list
upgrade of the 22-pass series.
