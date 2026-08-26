# Feature 117 — `nematjon555/telegram-restaurant-delivery-bot` watch-list v2

> **NEW observation (2026-08-26, 2nd pass).** Documents the
> carry-over watch-list entry for the first in-window
> `aiogram-restaurant bot` peer in the 27-pass series. Carry-over of
> feature 110 (2026-08-25).
> Bucket: **v2 owner-pains watch-list** — continue tracking, defer.

## Goal

Track the `nematjon555/telegram-restaurant-delivery-bot` peer
(0★, Python + aiogram 3, restaurant domain features: menu +
reservations + delivery + Excel) as the **first in-window
aiogram-restaurant bot peer in the 27-pass series**. The 2nd pass
focuses on a README read to determine whether the menu + reservation
+ delivery + Excel integration is a Telegram-native pattern that
LE31 could borrow or whether it's a one-off implementation.

## Scope

**In scope:**
- One-time README read (raw GitHub GET, no clone) of the peer.
- One-line summary added to the daily-research report's "Adjacent
  evidence" section in the next pass (2026-08-27).
- Re-check the peer's star velocity + push activity in the next
  pass (2026-08-27); if stars or pushes move, re-gate; if not,
  demote to low-confidence watch-list and stop tracking in 7 days.

**Out of scope (v1 / v2):**
- Any code import from the peer (charter §3.2: peer has no LICENSE
  file detected; permissive license is a hard precondition for
  any import).
- Any schema change, migration, or config key change.
- Any new pip dependency beyond what aiogram 3 ships.
- Any new Telegram Mini App surface (charter §3.4 prohibits
  customer-facing AI).

## Description

### Peer metadata (verified 2026-08-26)

| Field | Value |
|---|---|
| `full_name` | `nematjon555/telegram-restaurant-delivery-bot` |
| Description | "Telegram bot for restaurants and cafes with food menu, table reservation system, delivery links, and Excel integration (Aiogram 3)." |
| Primary language | Python |
| Stars | 0 (unchanged from 2026-08-25 baseline) |
| Forks | 0 (unchanged) |
| Last push | 2026-08-23T10:38:41Z (~68h before today's fetch, 2.83 days idle) |
| `updated_at` | 2026-08-23T10:38:45Z (carry-over; unchanged from 2026-08-25) |
| License | NONE (no LICENSE file detected) |
| Size | small (carry-over reading; README size suggests <50KB) |
| Default branch | (not yet inspected; default assumed `main` or `master`) |

**Direct repo URL**: https://github.com/nematjon555/telegram-restaurant-delivery-bot

### Why this matters (cross-section for LE31 v1 / v2)

1. **`aiogram 3`** is the Telegram-bot framework LE31 ships per
   charter §3.1. The peer is the **first in-window aiogram-restaurant
   bot peer in the 27-pass series** — the framework + domain match
   is direct.
2. **The peer's restaurant-domain features** (menu + reservations +
   delivery + Excel) align with LE31's v1 charter (waiter + cook
   surfaces; menu-first operations). The Excel integration is
   adjacent to LE31 v1's append-only `StockEntry` ledger (Excel as
   the upstream inventory system that LE31 might import from).
3. **The 2.83-day idle is consistent with a one-off implementation**
   (not an active project). The README read should confirm whether
   the menu + reservation + delivery + Excel integration is a
   Telegram-native pattern (reusable) or a one-off implementation
   (single-restaurant deployment).

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 90 `pronto-cafe-telegram-reminders-cross-section` | pronto cross-section Telegram reminders | Different peer (pronto 41★ MIT TS) |
| 94 `pronto-watch-v2` | pronto watch-list continue | Different peer |
| 78 `telegram-agent-control-plane-watch` | cross-section Telegram-bot pattern | Different peer (general cluster) |
| 102 `nightmux-stdlib-telegram-bridge` | v2-AI watch-list | Different peer (Telegram topic-as-tmux) |
| 110 `nematjon555-telegram-restaurant-bot-watch` | first observation (2026-08-25) | Earlier observation (no README read yet) |
| **117 `nematjon555-telegram-restaurant-bot-watch-v2` (this)** | 2nd pass; README read pending | **Latest** observation; README read next pass |

This pick is the **2nd pass** of the same peer observation. It is
NOT a duplicate of feature 110 — it is the **2nd-pass** watch-list
entry that focuses on the README read + the gate verdict update.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a
watch-list observation + a 2nd-pass gate-verdict artifact; no
schema change.

## Implementation

1. **In the next daily-research pass (2026-08-27):**
   - Fetch the peer's README via `curl -sSL
     https://raw.githubusercontent.com/nematjon555/telegram-restaurant-delivery-bot/main/README.md`
     (or master, depending on the default branch).
   - Read the README; summarize the architecture + the 4 domain
     features (menu + reservations + delivery + Excel).
   - Determine: reusable Telegram-native pattern, or one-off
     single-restaurant deployment?
   - Re-gate: re-evaluate the seven checks from the LE31 conventions
     skill. If the README confirms a reusable pattern with a
     permissive license, escalate to a build candidate (charter §3.2
     may need a decision on the no-license status). If the README
     confirms a one-off deployment, demote to low-confidence
     watch-list and stop tracking in 7 days.
2. **In the next 7 days (2026-08-27 through 2026-09-03):**
   - Re-check star velocity + push activity every daily-research pass.
   - If stars move to ≥1★, re-gate.
   - If a new push appears, re-gate (the peer may be active again).
   - If neither moves for 7 days, demote to low-confidence watch-list
     and stop tracking.
3. **No build today.** The pick is a watch-list continue. The
   "should LE31 borrow from this peer?" question is parked pending
   the README read + the gate verdict update.

## Telegram interaction

None directly from this feature. The watch-list entry does not
change the existing Telegram cook-bot surface.

## Dependencies

- None. The watch-list entry is passive.
- (Optional) README read in the next daily-research pass (2026-08-27)
  is the only action required.

## Open questions

- Is the README content a reusable Telegram-native pattern, or a
  one-off single-restaurant deployment? (Answer pending the next
  pass.)
- What is the peer's default branch? (`main` vs `master`; not yet
  inspected.)
- Does the peer have a CHANGELOG or release history that confirms
  the maintenance cadence? (Not yet inspected.)
- Should LE31 borrow any of the peer's 4 domain features (menu +
  reservations + delivery + Excel)? (Answer pending the README
  read + the gate verdict update.)

## Why this matters

The `nematjon555/telegram-restaurant-delivery-bot` peer is the
**first in-window aiogram-restaurant bot peer in the 27-pass series**.
The framework + domain match is direct (Python + aiogram 3 + restaurant
domain). The peer is currently 0★ + 2.83-day idle (one-off
implementation pattern); the README read in the next pass is the only
action required to determine whether the peer is a reusable pattern
or a one-off deployment. If reusable, the peer informs LE31 v1 polish
(features 04 menu-photo-bot, 22 sentiment-analysis, 41
telegram-msg-stock-update). If one-off, the peer is demoted to
low-confidence watch-list and stops being tracked in 7 days.