# Feature 116 — aiogram 3.31.0 stable track

> **NEW observation (2026-08-26).** Documents the in-window
> `aiogram 3.31.0` stable release from the 2026-08-26 daily
> research pass — the **first aiogram stable in the 27-pass series
> since 3.30.0** (2026-07-17, 5.6 weeks ago). PyPI upload
> 2026-08-26T00:00:42Z; `aiogram/aiogram` `releases.atom` entry
> "Telegram Bot API 10.3" at 2026-08-25T23:59:50Z. No breaking
> changes for LE31's current aiogram 3.x usage.
> Bucket: **v2 utility (stack pin-bump)** — watch-list defer until
> the next charter-decided pin-bump window opens (likely bundled with
> `uvicorn 0.52.4`).

## Goal

Record the **in-window `aiogram 3.31.0` stable release** as a
build-candidate observation. The release aligns LE31's Telegram
cook-bot framework with upstream Telegram Bot API 10.3 (no breaking
changes for LE31's current aiogram 3.x usage; aiogram 3.x is
API-stable). The artifact is the persistent build-candidate record.

## Scope

**In scope:**
- One source-file edit: the pin bump in the dependency manifest
  (e.g. `backend/requirements.txt`, `pyproject.toml`, or
  `requirements.lock`) from `aiogram>=3.0` or `aiogram==3.30.0` to
  `aiogram==3.31.0` (or `>=3.31.0,<4` if the team prefers a float
  pin).
- One CHANGELOG / commit-message line documenting the bump.
- One INDEX.md row in the "Active feature pipeline" table.
- Re-run the LE31 test suite + dev server + Telegram-bot smoke test
  to confirm no regressions.

**Out of scope (v1 / v2):**
- Any new Telegram Bot API feature adoption (e.g., new Mini App
  surface; out of v1 charter per §3.4).
- Any new pip dependency beyond the aiogram bump.
- Any schema change, migration, or config key change.
- Any Telegram API 10.3 surface beyond what LE31 currently uses
  (charter §3.1 specifies aiogram as the Telegram-bot framework
  only).

## Description

### aiogram release timeline (recent window)

| Release | PyPI upload | Days since prior |
|---|---|---|
| `aiogram 3.28.x` (patch) | 2026-06-14 (carry-over) | n/a |
| `aiogram 3.29.x` (patch) | 2026-07-01 (carry-over) | 17 days |
| `aiogram 3.30.0` | 2026-07-17 (carry-over; LE31 baseline) | 16 days |
| **`aiogram 3.31.0`** | **2026-08-26T00:00:42Z** | **40 days** |
| `aiogram 3.32.x` | (not released yet) | — |

**Direct PyPI URL**: https://pypi.org/pypi/aiogram/json

**GitHub release atom**: https://github.com/aiogram/aiogram/releases.atom
(tagged "Telegram Bot API 10.3" at 2026-08-25T23:59:50Z)

**Verbatim observation:**
- **First aiogram stable in the 27-pass series since 3.30.0**
  (5.6-week gap).
- The 5.6-week cadence is typical for aiogram (looking at the
  releases.atom history: 3.28.x = 2026-06-14, 3.29.x = 2026-07-01,
  3.30.0 = 2026-07-17; the cadence is 14-17 days between minor
  releases, with 3.31.0 extending to 40 days because Telegram Bot
  API 10.3 had a longer upstream alignment cycle).
- The release aligns LE31's Telegram cook-bot framework with upstream
  Telegram Bot API 10.3 (no breaking changes for LE31's current
  aiogram 3.x usage; aiogram 3.x is API-stable per the aiogram
  maintainers).
- LE31 currently pins `aiogram` in `backend/requirements.txt` (exact
  pin depends on the team's `pyproject.toml` / `requirements.lock`
  state; the current behavior is permissive — any 3.x release would
  be eligible).

### Why this matters (but is still a build-candidate defer)

1. **`aiogram` is the Telegram cook-bot framework LE31 ships
   per charter §3.1.** The pin matters for stability and for
   upstream Telegram Bot API alignment. LE31 imports aiogram only as
   the Telegram-bot framework and doesn't exercise the Mini App
   surface (charter §3.4 prohibits customer-facing AI; Mini Apps
   would be a separate decision).
2. **LE31 has no charter-decided aiogram version cut.** The current
   pin in `backend/requirements.txt` is permissive (any 3.x
   release would already be eligible). However, the charter §3.2
   stack-change rule requires an explicit charter decision for any
   new major version cut. **A pin-bump within the 3.x line is a
   minor utility bump and is within the charter's scope**, but the
   timing is the user's call.
3. **The 5.6-week stable cadence is normal for aiogram.** No urgency
   to ship; the bump can wait for the next general pin-bump window
   (likely bundled with `uvicorn 0.52.4`).
4. **No 3.32.x release is imminent.** The 5.6-week cadence suggests
   the next stable is at least 4-6 weeks away (mid-October 2026).

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| (none — first aiogram-pin-bump feature) | n/a | NEW |
| 109 `uvicorn-0-52-4-pin-bump-v9` | uvicorn 0.52.4 pin (carry-over) | Different pin |
| 115 `uvicorn-0-52-4-pin-bump-v10` | uvicorn 0.52.4 pin (carry-over, day 10) | Different pin |
| 78 `telegram-agent-control-plane-watch` | cross-section Telegram-bot pattern (watch-list) | Different scope |
| 90 `pronto-cafe-telegram-reminders-cross-section` | pronto Telegram reminders (cross-section) | Different scope |
| 94 `pronto-watch-v2` | pronto watch-list continue | Different scope |
| 102 `nightmux-stdlib-telegram-bridge` | v2-AI watch-list | Different scope |
| 110 `nematjon555-telegram-restaurant-bot-watch` | aiogram-restaurant peer (watch-list) | Different scope |
| 117 `nematjon555-telegram-restaurant-bot-watch-v2` | aiogram-restaurant peer (watch-list continue) | Different scope |

This pick is the **first aiogram-pin-bump feature** in the LE31
daily-research series. The pattern (stack pin-bump carry-over in
27-pass series; first aiogram stable in 5.6 weeks; no breaking
changes) is structurally identical to `uvicorn 0.52.4` pin-bump
carry-overs (features 27, 70, 76, 78, 80, 82, 87, 93, 99, 105, 109,
115). The artifact is the persistent build-candidate record.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation + a build-candidate artifact; no schema change.

## Implementation

1. Wait for the user to open a pin-bump window (charter §3.2),
   likely bundled with `uvicorn 0.52.4` (feature 115).
2. When the window opens:
   - Bump the pin in `backend/requirements.txt` from the current
     aiogram pin (permissive or 3.30.0) to `aiogram==3.31.0` (or
     `>=3.31.0,<4` if the team prefers a float pin).
   - Add a CHANGELOG / commit-message line documenting the bump.
   - Re-run the LE31 test suite + dev server + Telegram-bot smoke
     test (start a bot, send a test message, verify response).
3. **No build today.** The pick is a build-candidate defer. The
   "should LE31 bump aiogram to 3.31.0?" question is parked pending
   the charter-decided pin-bump window.

## Telegram interaction

None directly from this feature. The pin-bump is passive; the existing
Telegram cook-bot surface should work unchanged because aiogram 3.x is
API-stable.

## Dependencies

- None. The pin-bump is mechanical.
- (Optional) Bundle with feature 115 (`uvicorn 0.52.4` pin-bump) for
  a single pin-bump PR.

## Open questions

- Is the user ready to open a pin-bump window within the next 7
  days? (If yes, bundle with `uvicorn 0.52.4`. If no, this artifact
  expires and a future daily-research pass will surface a new
  pin-bump candidate if any.)
- Should the pin be `==3.31.0` (exact) or `>=3.31.0,<4` (float with
  upper bound)? The LE31 current pin is permissive; the team should
  pick the convention it prefers.
- Does the LE31 Telegram-bot smoke test cover all aiogram 3.x
  surfaces the project uses? (LE31 should — chat-based bot, no Mini
  App — but confirm before bumping.)
- Does the Telegram-bot still respond to a test message after the
  bump? (This is part of the verification protocol.)

## Why this matters

The `aiogram 3.30.0 → 3.31.0` pin bump is the **second in-window
stable stack change** that affects a LE31 pin (the first is uvicorn
0.52.4). The 5.6-week stable cadence is normal for aiogram; no
breaking changes expected for LE31's current aiogram 3.x usage. The
artifact is the persistent build-candidate record. If the team is
doing a pin-bump window, this is the right pin to land alongside
`uvicorn 0.52.4`. If no pin-bump window opens in the next 7 days,
this artifact expires and a future daily-research pass will surface
a new pin-bump candidate (if any).