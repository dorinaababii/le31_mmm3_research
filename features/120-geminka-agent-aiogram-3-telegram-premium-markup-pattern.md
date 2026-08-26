# Feature 120 — geminka-agent aiogram-3 Telegram Premium markup pattern

> **NEW observation (2026-08-26).** Documents the in-window
> `SkrudjReal/geminka-agent` aiogram-3 + Telegram Premium rich-markup
> AI-companion agent (7★ **MIT** Python, pushed **2026-08-25 yesterday**)
> — the highest-star aiogram-3 + Telegram peer in window with the
> architectural primitives LE31's cook-bot surface already plans
> (`Deny-by-Default Auth Middleware` mirrors charter §3.1 chat-id
> allowlist; `Per-User Concurrency Lock` avoids race conditions on
> chat_id updates; `SQLite WAL State` mirrors single-writer append-only
> `StockEntry` ledger posture) plus a **Telegram Premium rich-markup**
> capability LE31's bot does not currently exploit.
> Bucket: **v2 owner-pains (parking-lot, future-cook-bot-rich-markup-
> surface), defer** — the peer is a pattern-record artifact (the
> aiogram-3 architectural primitives are informational reference for
> future v2 cook-bot rich-markup + auth-pattern consideration), not a
> v1 build candidate.

## Goal

Track the in-window `SkrudjReal/geminka-agent` aiogram-3 + Telegram
Premium rich-markup agent as **pattern-record peer** for the LE31 v2
cook-bot rich-markup + auth-pattern consideration. The README's
aiogram-3 architectural primitives (`Deny-by-Default Auth Middleware`
+ `Per-User Concurrency Lock` + `SQLite WAL State`) mirror the LE31
charter §3.1 deterministic-gate + chat-id allowlist + single-writer
append-only `StockEntry` ledger posture. The Telegram Premium markup
capability is a v2 rich-markup consideration that LE31's bot does not
currently exploit (charter §3.2 keeps v1 minimal). Watch-list continue
(defer until the v2 charter review surfaces the cook-bot rich-markup
extension).

## Scope

**In scope:**
- Cite `geminka-agent` as a pattern-record peer in the next
  daily-research pass.
- Track whether `geminka-agent` reaches ≥15★ in the next 30 days
  (community-traction signal).
- Cross-reference `geminka-agent` against LE31 features 41 + 43 + 65
  v2 cook-bot rich-markup + auth-pattern extension in the LE31
  feature-gate trail when the v2 charter review opens.
- Add a row to `/opt/data/INDEX.md` "Active feature pipeline" table
  with date, pick, feature path, Linear ID, status (Backlog,
  watch-list defer, v2 owner-pains).
- Re-evaluate `geminka-agent` on star velocity + push activity in the
  next 30 days; if ≥15★ or new significant architectural changes,
  surface as a future-v2 charter-question prompt.

**Out of scope:**
- Any code change to the LE31 backend (peer is informational).
- Any schema change, migration, or config key change.
- Any new pip dependency (the LE31 stack already has aiogram 3.x +
  chat-id allowlist; the Telegram Premium markup is a v2 question).
- Any charter change (charter §3.2 minimal-v1-surface posture
  remains correct; v2 cook-bot rich-markup = parked).
- Any code-borrow from `geminka-agent` (the AI-companion / roleplay
  domain is far from LE31's cook-bot domain; the aiogram-3
  architectural primitives are the actionable insight, but
  informational, not blocking).

## Description

### Peer overview

| Field | Value |
|---|---|
| Repo | `SkrudjReal/geminka-agent` |
| Stars | 7★ (highest in the aiogram-3 + Telegram-niche pool in window) |
| License | **MIT** (permissive, no contagion) |
| Last push | 2026-08-25 (yesterday) |
| Topics | `ai-companion, aiogram-3, antigravity, gemini, roleplay, telegram-bot` |
| URL | https://github.com/SkrudjReal/geminka-agent |
| README verification | Verified directly from `api.github.com/repos/SkrudjReal/geminka-agent/readme` with `HERMES_GITHUB_TOKEN` at 2026-08-26 06:32 UTC |

### Description (verbatim from GitHub API)

> "🌸 Autonomous AI Companion & Assistant on Google Antigravity &
> Gemini with real-time live streaming, dynamic emotional intelligence,
> 50/50 sticker harvesting, and rich Telegram Premium markup."

### README key claims (verbatim, verified 2026-08-26 06:32 UTC)

- `aiogram 3.x` (LE31's own framework, charter §3.1)
- `Telegram Updates` (LE31's own input surface)
- `Deny-by-Default Auth Middleware` (mirrors LE31 charter §3.1
  chat-id allowlist — the cook role + manager role are explicitly
  allowlisted; deny-by-default for unknown chat_ids)
- `Per-User Concurrency Lock` (avoids race conditions on chat_id
  updates; not currently in LE31 v1 explicitly — a v2 polish item)
- `SQLite WAL State` (single-writer append-only surface that mirrors
  `StockEntry` ledger posture; charter §3.2 keeps v1 on Postgres
  but the SQLite WAL pattern is informational)
- `Tests 16 Passed` (active maintenance)
- `License: MIT` (verified)

### LE31 adjacency analysis

The `geminka-agent` README's pattern maps directly to LE31's existing
feature contracts + architectural primitives:

| `geminka-agent` pattern | LE31 feature / primitive | Status |
|---|---|---|
| `aiogram 3.x` | Feature 04 (cook-bot, aiogram 3 framework) | Active in v1 |
| `Telegram Updates` | Feature 04 + Feature 41 (telegram-msg-stock-update) + Feature 43 (telegram-prep-checkoff-adherence) | Active in v1 |
| `Deny-by-Default Auth Middleware` | Charter §3.1 chat-id allowlist (cook + manager only; deny-by-default) | Active in v1 |
| `Per-User Concurrency Lock` | (no direct LE31 feature; race-condition guard for chat_id updates; v2 polish item) | v2 polish (parking-lot) |
| `SQLite WAL State` | Per-batch `StockEntry` ledger (charter §3.2 Postgres-only, but SQLite WAL pattern is informational) | v1 Postgres; v2 SQLite = parked |
| `rich Telegram Premium markup` | Charter §3.2 minimal-v1-surface; v2 cook-bot rich-markup = parked | v2 cross-section (parking-lot) |
| `Tests 16 Passed` (active maintenance) | Feature 04 active maintenance pattern | Active in v1 |

The peer's aiogram-3 architectural primitives (`Deny-by-Default Auth
Middleware` + `Per-User Concurrency Lock` + `SQLite WAL State`) are
**individually familiar to LE31 charter §3.1**. The Telegram Premium
markup capability is a *new surface* — LE31's bot does not currently
exploit rich markup (charter §3.2 keeps v1 minimal). The peer is the
*external validation* of the aiogram-3 architectural primitives.

### Why this peer matters (but is still a watch-list defer)

1. **Direct aiogram-stack match for LE31's cook-Telegram-bot surface**
   (charter §3.1). 7★ is highest in the aiogram-3 + Telegram-niche
   pool in window. MIT permissive.
2. **Architectural primitive validation**. `Deny-by-Default Auth
   Middleware` mirrors charter §3.1 chat-id allowlist (cook + manager
   only; deny-by-default). `Per-User Concurrency Lock` is a v2 polish
   item for race-condition guards. `SQLite WAL State` mirrors
   `StockEntry` ledger posture.
3. **Telegram Premium markup capability is new for LE31**. LE31's
   bot does not currently exploit rich markup (charter §3.2 keeps v1
   minimal). The peer's Telegram Premium markup is a v2 cross-section
   candidate for the cook-bot surface.
4. **Permissive-licensed**. MIT license = no contagion for code or
   pattern-borrow.
5. **Watch-list defer**. The peer is a pattern-record signal, not a
   v1 build candidate. Watch-list continue until the v2 charter
   review surfaces the cook-bot rich-markup extension.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 41 `telegram-msg-stock-update` | Telegram message → StockEntry update (LE31 v1) | LE31 feature, not external peer |
| 43 `telegram-prep-checkoff-adherence` | Telegram prep-checkoff adherence (LE31 v1) | LE31 feature, not external peer |
| 65 `cook-photo-stock-list-pwa` | Cook photo + stock-list PWA (LE31 v1) | LE31 feature, not external peer |
| 102 `nightmux-stdlib-telegram-bridge` | Stdlib-only Telegram-agent bridge peer (LE31-direct) | Different peer, stdlib-only framing |
| 110 `nematjon555-telegram-restaurant-bot-watch` | First in-window aiogram-restaurant bot peer (LE31-direct) | Different peer, restaurant domain (vs AI-companion) |
| 117 `nematjon555-telegram-restaurant-bot-watch-v2` | 2nd pass for feature 110 | Different peer, restaurant domain |
| **120 `geminka-agent-aiogram-3-telegram-premium-markup-pattern` (this)** | `geminka-agent` aiogram-3 + Telegram Premium rich-markup peer (MIT) | **Pattern-record** — aiogram-3 architectural primitives validation + Telegram Premium markup new surface (v2 cook-bot rich-markup candidate) |

This pick is **pattern-record**, not a duplicate of features
41/43/65/102/110/117. It is the highest-star aiogram-3 + Telegram peer
in window with the Telegram Premium markup new-surface candidate.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation + a watch-list artifact; no schema change.

## Implementation

1. Read `geminka-agent` README in full in the next daily-research pass
   (2026-08-27) and cite in the report.
2. Track `geminka-agent` star velocity + push activity in the next 30
   days. If ≥15★ or new significant architectural changes, surface as
   a future-v2 charter-question prompt.
3. Cross-reference `geminka-agent` against features 41 + 43 + 65 v2
   cook-bot rich-markup extension in the LE31 feature-gate trail when
   the v2 charter review opens.
4. **No build today.** The pick is a watch-list defer. The "should
   LE31 v2 adopt a Telegram Premium markup surface for the cook-bot?"
   question is parked pending the v2 charter review.

## Telegram interaction

**Reference only, no immediate change.** The peer's architectural
primitives (`Deny-by-Default Auth Middleware` + `Per-User Concurrency
Lock` + `SQLite WAL State`) are *individually familiar to LE31 charter
§3.1* and require no change to the existing Telegram cook-bot
surface. The Telegram Premium markup is a v2 cross-section
consideration that the v1 charter §3.2 keeps out of scope.

## Dependencies

- None. The `geminka-agent` peer is a pattern-record signal; no new
  dependencies. The Telegram Premium markup is a v2 question, not a
  v1 path. The aiogram-3 architectural primitives are individually
  familiar to LE31 charter §3.1.

## Open questions

- Does `geminka-agent` reach ≥15★ in the next 30 days? (If yes,
  indicates community traction in the aiogram-3 + Telegram Premium
  niche.)
- Does the `geminka-agent` maintainer push a v2 of the architecture
  with multi-tenant posture? (If yes, surfaces as a v2 charter-
  question prompt.)
- Does the v2 charter review surface the cook-bot rich-markup
  extension in the next 90 days? (If yes, `geminka-agent` becomes a
  charter-question reference for the Telegram Premium markup.)
- Does `geminka-agent` ship a public release of the reference
  implementation with a stable `requirements.txt`? (If yes, evaluate
  for code-borrow per charter §3.2 — MIT permissive.)

## Why this matters

The `SkrudjReal/geminka-agent` peer is the **highest-star aiogram-3 +
Telegram peer in window** with the architectural primitives LE31's
cook-bot surface already plans. The README's verbatim aiogram-3
primitives (`Deny-by-Default Auth Middleware` + `Per-User Concurrency
Lock` + `SQLite WAL State`) are individually familiar to LE31 charter
§3.1 and serve as external validation of the architectural choices.
The Telegram Premium markup capability is a *new surface* — LE31's
bot does not currently exploit rich markup (charter §3.2 keeps v1
minimal). The peer is a **pattern-record signal** for the LE31 v2
cook-bot rich-markup + auth-pattern consideration. MIT permissive.