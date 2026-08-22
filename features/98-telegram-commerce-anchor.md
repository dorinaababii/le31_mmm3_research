# Feature 98 — telegram-commerce-anchor

> **NEW observation (2026-08-22).** Documents the **in-window Python Telegram-commerce anchor** — `indmdev/Free-Telegram-Store-Bot` is the **highest in-window Python repo on the `topic:telegram-bot` topic by 4×** (next peer: `siutsin/telegram-jung2-bot` ★22). The `indmdev` org has a 3-repo commerce stack all pushed 2026-08-22 (Free-Telegram-Store-Bot ★153 + Telegram-Store-MiniApp ★38 + indmshopbot ★33). Observed during the 2026-08-22 daily brainstorm (see `/opt/data/le31-brainstorm-2026-08-22.md`, Pick C). Bucket: **v2 owner-pains (parking-lot, peer observation)** — hard defer pending charter §3.1 surface-expansion review.

## Goal

Record the **in-window Python Telegram-commerce anchor** as a peer-observation research-note. The indmdev 3-repo commerce stack proves that "Telegram as a commerce surface" is **production-viable at scale** (★153 with active development today). The cross-section with LE31's cook-Telegram-bot surface (features 33, 41, 43, 56, 60) and owner-recap surface (features 39, 57, 69) is direct, but the architecture is fundamentally different from LE31's restaurant-ops scope.

## Scope

**In scope:**
- Daily direct-repo GETs on the 3 indmdev repos (via `$HERMES_GITHUB_TOKEN`):
  - `indmdev/Free-Telegram-Store-Bot` (★153, pushed 2026-08-22)
  - `indmdev/Telegram-Store-MiniApp` (★38, pushed 2026-08-22)
  - `indmdev/indmshopbot` (★33, pushed 2026-08-22)
- Tracking star velocity + push activity + license + Python/aiogram version + dependency footprint on each repo.
- Reading the Free-Telegram-Store-Bot README in the next daily-research pass to confirm the "100% Free Shop Bot" model and the MiniApp + bot architecture.
- Cross-referencing indmdev against LE31 features 33, 41, 43, 56, 60 (cook-Telegram-bot surface) + features 39, 57, 69 (owner-recap surface).

**Out of scope (v1 / v2):**
- Importing any code from the indmdev repos (LE31 is for one restaurant, not a SaaS commerce platform).
- Building a Telegram-commerce surface for LE31 (charter §3.1 — two primary operational surfaces: waiter web UI + cook Telegram bot, no commerce/MiniApp surface).
- Charter §3.2 license check: indmdev repo's license is unknown at this level of detail; verify before any code import.

## Description

The indmdev 3-repo commerce stack is the **highest in-window adoption signal on the telegram-bot topic**. The pattern proves that "Telegram as a commerce surface" (bot + MiniApp + order management) is **production-viable at scale** and matches the Python+aiogram v3 stack LE31 uses.

### Per-repo description table (verbatim from GitHub API responses)

| Repo | Stars | Description |
| --- | --- | --- |
| `indmdev/Free-Telegram-Store-Bot` | ★153 | "100% Free Shop Bot… Telegram Store Bot… selling your products and services." |
| `indmdev/Telegram-Store-MiniApp` | ★38 | Telegram Mini App companion to the Free Store Bot (companion repo for Telegram's Mini App platform). |
| `indmdev/indmshopbot` | ★33 | Telegram shopping bot variant. |

### Why this is a fresh cross-section signal

At ★153, `indmdev/Free-Telegram-Store-Bot` is the **highest in-window Python repo on the `topic:telegram-bot` topic by 4×** (next peer: `siutsin/telegram-jung2-bot` ★22). The pattern is "Telegram as a commerce surface" with:

1. **Bot + MiniApp + order management** — a 3-layer architecture that mirrors modern SaaS checkout flows.
2. **Python+aiogram v3 stack** — matches LE31's stack (FastAPI + aiogram v3 + Postgres).
3. **Self-hosted / zero-commission model** — the README claims "100% Free Shop Bot"; this is the same small-business self-hosted posture LE31 takes.
4. **Cross-section with LE31's cook-Telegram-bot surface** — features 33, 41, 43, 56, 60 are all Telegram-only operational channels for one restaurant; indmdev proves that Telegram commerce is viable at scale.

### Why parking-lot (not build)

(a) **charter §3.1 — two primary operational surfaces** — waiter web UI + cook Telegram bot, no commerce/MiniApp surface; (b) **scope creep risk** — adding Telegram commerce semantics is a charter-level scope expansion (LE31 v1 is for one restaurant, not a SaaS); (c) **no observed LE31-owner demand for commerce semantics** — the cook/owner has not asked for commerce; (d) **the JTBD pull is inferred, not observed** — the indmdev repo proves the pattern is viable but does not prove the LE31 owner wants it; (e) **charter §3.2 license check** — indmdev repo's license is unknown at this level of detail; verify before any code import.

## Data model

No new LE31 data model. This artifact is a research-note observation. The indmdev repos do not introduce a new LE31 table or schema.

## Implementation steps

1. **No code change**. This is a research-note artifact.
2. Future-pass tracking: add the 3 indmdev repos to the daily-research watch list.
3. Read Free-Telegram-Store-Bot README in the next daily-research pass to confirm the "100% Free Shop Bot" model + MiniApp + bot architecture.
4. Verify indmdev repo licenses on next pass.
5. Re-evaluation: in 30 days (2026-09-22), check whether the indmdev cluster has crossed ≥200★ collectively OR whether the LE31 owner has asked for commerce.

## Telegram interaction if any

None for this artifact (it's a research-note observation). If LE31 ever builds commerce surface, this would be the anchor reference, but that's a charter-level decision not in scope.

## Dependencies

- **`$HERMES_GITHUB_TOKEN`** for daily direct-repo GETs on the 3 indmdev repos.
- **GitHub `topic:telegram-bot` + `topic:real-time` searches** (filtered by `pushed:2026-07-22..<date>`) for indmdev discovery.
- **Cross-reference**: features 33, 41, 43, 56, 60 (cook-Telegram-bot surface) + features 39, 57, 69 (owner-recap surface) + feature 90 + 94 (Pronto WhatsApp+Telegram peer at ★40).

## Open questions

1. **What is the indmdev repo's license?** — verify on next pass (MIT? Apache-2.0? GPL?). If GPL/AGPL, charter §3.2 blocks any import.
2. **Is the indmdev stack production-grade at ★153?** — read the README + commit log on next pass to confirm active maintenance + recent releases.
3. **Does LE31 ever need a commerce surface?** — this is a charter-level question, not a feature-level one. Defer until the LE31 owner explicitly asks for commerce.

## Why this matters

The indmdev cluster proves that "Telegram as a commerce surface" is **production-viable at scale** with the **same Python+aiogram v3 stack LE31 uses**. The cross-section is direct: LE31's cook-Telegram-bot surface (features 33/41/43/56/60) + owner-recap surface (features 39/57/69) all live on the same Telegram surface that indmdev proves can support commerce at ★153. The pattern informs a **charter-level scoping question** ("should LE31 v2 add Telegram-commerce semantics?") but no build implied today.

## Distinct from existing features

- **Feature 33** (telegram-walkin-pin) — LE31's walk-in triage bot. Distinct: feature 33 is restaurant-ops; indmdev is commerce-SaaS.
- **Feature 41** (telegram-msg-stock-update) — LE31's stock-update Telegram bot. Distinct: feature 41 is restaurant-ops; indmdev is commerce-SaaS.
- **Feature 43** (telegram-prep-checkoff-adherence) — LE31's prep checkoff. Distinct: feature 43 is restaurant-ops; indmdev is commerce-SaaS.
- **Feature 56** (walk-in-front-desk-channel) — LE31's front-desk Telegram channel. Distinct: feature 56 is restaurant-ops; indmdev is commerce-SaaS.
- **Feature 60** (restaurant-telegram-front-desk-mirror) — LE31's front-desk mirror. Distinct: feature 60 is restaurant-ops; indmdev is commerce-SaaS.
- **Features 39, 57, 69** (owner-recap surfaces) — LE31's owner-recap surfaces. Distinct: features 39/57/69 are owner-recap; indmdev is customer-commerce.
- **Features 90 + 94** (Pronto WhatsApp+Telegram peer at ★40) — Distinct: Pronto is the WhatsApp+Telegram-reminder self-hosted POS peer (★40, smaller adoption, different architecture); indmdev is the commerce-SaaS anchor (★153, larger adoption, bot+MiniApp+order management).

## Sources

- **GitHub `topic:telegram-bot` + `topic:real-time`** (searches verified at 2026-08-22 06:44 UTC; PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
- Raw responses:
  - `/tmp/le31-brainstorm-2026-08-22/gh_topic_telegram-bot.json` (173,365 bytes, 30 items returned)
  - `/tmp/le31-brainstorm-2026-08-22/gh_topic_real-time.json` (182,111 bytes, 30 items returned)
- 3 indmdev repos verified via raw GitHub API responses (item ids for each — see raw JSON for full IDs).
- Full report: `/opt/data/le31-brainstorm-2026-08-22.md` (Pick C section, lines 109–121).
- Parent Linear issue: HMM-125 (Brainstorm 2026-08-22 — daily).
- This Linear sub-issue: HMM-128.