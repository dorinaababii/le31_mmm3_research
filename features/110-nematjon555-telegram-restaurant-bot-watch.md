# Feature 110 — nematjon555/telegram-restaurant-delivery-bot watch

> **NEW observation (2026-08-25).** Documents the in-window
> `nematjon555/telegram-restaurant-delivery-bot` cross-section peer
> surfaced via the `ghsearch_aiogram_restaurant` GitHub Search
> query — the **first in-window aiogram-restaurant bot peer in the
> 26-pass daily-research series**. Python + aiogram 3 + restaurant
> domain features (menu + reservations + delivery + Excel) =
> closest direct stack match for LE31's cook-Telegram-bot surface
> (charter §3.1). 0★ fails the gate today (no community
> traction), but the framework + domain combination warrants
> watch-list tracking.
> Bucket: **v2 owner-pains (watch-list, defer)** — the peer is
> informative for LE31 v2 cook-assistant transport-layer
> architecture (cross-section for the Telegram-bot surface) but
> not actionable as a build today.

## Goal

Track the in-window `nematjon555/telegram-restaurant-delivery-bot`
cross-section peer for the next 7 days to confirm whether the
aiogram-restaurant bot pattern is a one-off implementation or a
growing niche signal. The peer is the **first in-window
aiogram-restaurant bot** in the 26-pass series and the closest
direct stack match for LE31's cook-Telegram-bot surface. Watch-list
continue (defer until stars ≥1 or peer README reveals a useful
pattern).

## Scope

**In scope:**
- Read the peer's README + commit log + Python source in the next
  daily-research pass.
- Track star velocity via `GET
  https://api.github.com/repos/nematjon555/telegram-restaurant-delivery-bot`
  (via `$HERMES_GITHUB_TOKEN`) once per daily pass.
- Track push cadence (last push timestamp).
- Track license status (currently None detected — confirm in the
  README read).
- Add a row to `/opt/data/INDEX.md` "Active feature pipeline" table
  with date, pick, feature path, Linear ID, status (Backlog,
  watch-list defer).

**Out of scope:**
- Any code change to the LE31 backend.
- Any schema change, migration, or config key change.
- Any import of nematjon555 code into LE31 (license = None detected
  → blocking until license is confirmed; even with license, the
  peer is a small standalone bot, not a reusable library).
- Any new pip dependency (charter §3.2).

## Description

### Peer overview

| Field | Value |
|---|---|
| Name | `nematjon555/telegram-restaurant-delivery-bot` |
| URL | https://github.com/nematjon555/telegram-restaurant-delivery-bot |
| Stars | 0 |
| Forks | 0 |
| Pushed | 2026-08-23T10:38:41Z (~44h before today's fetch, 1.83 days idle) |
| Languages | Python |
| License | None detected |
| Description | "Telegram bot for restaurants and cafes with food menu, table reservation system, delivery links, and Excel integration (Aiogram 3)." |
| First in-window discovery | 2026-08-25 (today's daily-research pass) |

### Why this peer matters (but is still a watch-list defer)

1. **First in-window aiogram-restaurant bot in the 26-pass
   series.** The peer's framework (Python + aiogram 3) is the
   same library family LE31 uses (charter §3.1 — `aiogram 3.30.0`
   is the LE31-pinned aiogram version). The peer is the
   **closest direct stack match for LE31's cook-Telegram-bot
   surface** in the 26-pass series.
2. **Domain match.** The peer's description lists
   restaurant-domain features (menu + reservations + delivery +
   Excel integration). The "menu + table reservation" feature
   pair is directly adjacent to LE31's v1 charter surfaces
   (waiter + cook; menu-first operations).
3. **Excel integration is a v2 owner-pains watch-list signal.**
   Restaurant operators frequently use Excel/spreadsheets for
   inventory tracking; the peer's Excel integration suggests the
   operator-pain of "I have my inventory in Excel and I need to
   get it into the bot" is being addressed. **This validates the
   LE31 v2 owner-pains thesis** that restaurant operators want
   spreadsheet-friendly workflows even when adopting a chat-based
   bot.
4. **0★ = no community traction.** The peer has 0★ + 0 forks
   → no community validation. This is the **failing-gate signal**
   for today (no observed pain at scale). The watch-list tracking
   tests whether traction develops.
5. **No license detected.** License is None detected → blocking
   for code-import per charter §3.2 (and the peer's repository
   is a standalone bot, not a reusable library, so import was
   never in scope).

### Cross-section peer analysis

The peer's description aligns with LE31's existing v1 charter
(charter §3.1 — one small restaurant + two primary operational
surfaces: waiter web UI + cook Telegram bot). The peer's
restaurant-domain features (menu, reservations, delivery) match
the waiter surface; the Telegram-bot channel matches the cook
surface.

| LE31 surface | Peer feature |
|---|---|
| Waiter web UI (charter §3.1) | Menu + table reservation + delivery |
| Cook Telegram bot (charter §3.1) | Telegram-bot channel |
| Excel/spreadsheet integration (v2 owner-pains) | Excel integration (peer feature) |

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 78 `telegram-agent-control-plane-watch` | Telegram-agent control-plane watch (carry-over) | Cross-section but agent-focused |
| 90 `pronto-watch` | SGrappelli/pronto watch (WhatsApp + Telegram reminders) | Different peer, different framework |
| 94 `pronto-watch-v2` | SGrappelli/pronto watch day-2 | Same peer, different framework |
| 100 `pronto-watch-v3` | SGrappelli/pronto watch day-3 | Same peer, different framework |
| 102 `nightmux-stdlib-telegram-bridge` | stdlib-only Telegram-agent bridge | Different framework (stdlib only, no aiogram) |
| **110 `nematjon555-telegram-restaurant-bot-watch` (this)** | First aiogram-restaurant bot peer in 26-pass series | **First in-window aiogram-restaurant bot** |

This pick is the **first in-window aiogram-restaurant bot peer**
in the 26-pass series. It is NOT a duplicate of features 78/90/94/
100/102 — it is the **first peer** that combines (a) Python
language, (b) aiogram framework, and (c) restaurant domain
features.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation + a watch-list artifact; no schema change.

## Implementation

1. Read the peer's README + commit log + Python source in the
   next daily-research pass (2026-08-26).
2. Track star velocity for the next 7 days (stars, forks, pushed
   timestamp) via direct repo GET.
3. **No build today.** The pick is a watch-list defer. The
   "should LE31 v2 cook-assistant borrow any pattern from this
   peer?" question is parked pending the README read.
4. If the peer reaches ≥1★ OR the README reveals a reusable
   pattern, surface in the next daily-research pass as a build
   candidate.
5. If the peer remains 0★ for 7 consecutive days with no
   meaningful pushes, surface in the next daily-research pass as
   a "drop" signal (remove from watch-list).

## Telegram interaction

None. This is a passive watch-list observation; no LE31
cook/manager action.

## Dependencies

- None. The watch-list tracking is purely observational.

## Open questions

- Does the peer have a usable pattern for menu + table
  reservation in a Telegram bot that LE31 v2 cook-assistant
  could borrow? (Read the README to confirm.)
- Does the peer's Excel integration reveal a v2 owner-pains
  pattern (spreadsheet-friendly workflows)? (Read the source to
  confirm.)
- Does the peer have a license? (Confirm in the README; license
  = None detected in GitHub API response.)
- Does the peer reach ≥1★ within the next 7 days? (Track star
  velocity.)
- Does the peer maintain push cadence? (Track push cadence.)

## Why this matters

The `nematjon555/telegram-restaurant-delivery-bot` peer is the
**first in-window aiogram-restaurant bot** in the 26-pass
daily-research series. It is the closest direct stack match for
LE31's cook-Telegram-bot surface (charter §3.1) and is a
real-world validation that the aiogram-restaurant bot niche
exists in the wild. The peer's 0★ = no community traction
fails the gate today, but the framework + domain combination
warrants watch-list tracking for the next 7 days. If the peer
gains traction (≥1★) or reveals a reusable pattern in the
README, it informs the LE31 v2 cook-assistant transport-layer
architecture. If the peer remains dormant, it is a one-off
implementation and not a niche signal.
