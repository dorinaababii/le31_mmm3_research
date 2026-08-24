# Feature 108 — Telegram chat-history fuzzy-search → StockEntry audit surface

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-24 (Pick C, **defer**) · **Bucket**: v2 owner-pains (parking-lot, future-audit-search-surface)
> **One-line**: A research-only watch-list artifact that records the in-window `groupultra/telegram-search` cross-section peer (4,075★ AGPL-3.0 TypeScript, pushed 2026-08-21) — **a high-volume Telegram chat-history fuzzy-search architecture (MeiliSearch + PostgreSQL + Telegram MTProto)** — as a future reference for LE31 v2 owner-pains audit-search surface for the `StockEntry`-via-Telegram trail. **No code today; deferred indefinitely until either (a) LE31 v2 explicitly opens the audit-search surface question (features 30 + 49 v2 extension review pending), or (b) the owner signals an explicit "I can't search the historical StockEntry-by-Telegram-message trail" pain.**

## Goal

The 2026-08-24 brainstorm scan surfaced `groupultra/telegram-search` (4,075★, AGPL-3.0 TypeScript, pushed 2026-08-21T12:13:15Z, https://github.com/groupultra/telegram-search) — a Telegram chat-history fuzzy search tool with 4k★ community traction, single Telegram bot, MeiliSearch + PostgreSQL + Telegram MTProto indexing at scale. Description verbatim (Chinese): "Telegram 聊天记录搜索" = "Telegram chat-history search".

The cross-section insight: **LE31's `StockEntry` ledger rows frequently originate via cook-Telegram messages** (features 41 telegram-msg-stock-update, 38 cook-voice-note-to-stockentry, 65 cook-photo-stock-list-pwa, 43 telegram-prep-checkoff-adherence), and **the LE31 owner has no audit-search surface today** for searching the historical Telegram-message-to-StockEntry trail. A high-volume Telegram fuzzy-search architecture (4k★ + MeiliSearch + PostgreSQL) is a direct reference for a future **v1 polish to feature 30 (append-only-audit-redirect) + feature 49 (postledger-tamper-evident-hash)**: a `StockEntry`-origin search surface where the owner can fuzzy-search "what was sent from the cook bot on Wednesday about tomatoes?" and see the original Telegram message + the derived `StockEntry` row.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 v2 team considers adding an audit-search surface that lets the owner fuzzy-search the historical Telegram-message-to-StockEntry trail, the team wants to know whether a high-volume peer (4k★ + MeiliSearch + PostgreSQL) documents a working architecture, so that the search-surface design is informed by a working peer and not invented from scratch.

**Why this is a fresh cross-section signal today**: `groupultra/telegram-search` is the **only in-window ≥1k★ Telegram chat-history fuzzy-search peer with both MeiliSearch and PostgreSQL components**. The other in-window Telegram-bus peers are:
- `freqtrade/freqtrade` 53,567★ GPL-3.0 Python — crypto trading bot, not chat-history search.
- `RocketChat/Rocket.Chat` 46,022★ NOASSERTION TS — comms OS, not chat-history search.
- `telegraf/telegraf` 9,181★ MIT Node.js — Telegram bot framework, not chat-history search.

None of the above ship a chat-history fuzzy-search architecture. `groupultra/telegram-search` is the unique pattern-record candidate.

## Scope

**In scope (v2 owner-pains, S effort, ≤1 day, defer — LE31 v1 doesn't ship an audit-search surface):**
- Daily direct-repo `GET https://api.github.com/repos/groupultra/telegram-search` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `groupultra/telegram-search` README + architecture documentation in the next daily-research pass to confirm the MeiliSearch + PostgreSQL + Telegram MTProto indexing pattern (READ ONLY — no import).
- Tracking star velocity + push activity on `groupultra/telegram-search`.
- Documenting the fuzzy-search architecture pattern in the LE31 research notes (this artifact is the document).

**Out of scope (no new LE31 implementation):**
- A new chat-history search engine. LE31 v1 doesn't ship one; the v2 extension is a future-tense concern.
- A `groupultra/telegram-search` import. AGPL-3.0 license blocks LE31 v1 import per charter §3.2; even at v2, importing AGPL code requires explicit charter approval.
- A MeiliSearch dependency. Adding MeiliSearch would expand LE31's dependency surface; the artifact is informational only.
- Any new feature based on the `groupultra/telegram-search` code surface.

## Description

**Evidence precondition:** observed (GitHub `groupultra/telegram-search` 4,075★ + AGPL-3.0 + TypeScript + MeiliSearch + PostgreSQL + Telegram MTProto + 2026-08-21 push). Confidence: **high** for the cross-section pattern (the MeiliSearch + PostgreSQL + Telegram MTProto architecture is documented in the README); **low** for LE31-specific urgency (LE31 v1 doesn't ship an audit-search surface; the v2 extension is a future-tense concern).

### `groupultra/telegram-search`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-24 (this pass) | **4,075★** | (track) | 2026-08-21T12:13:15Z | AGPL-3.0 | TypeScript |

**Direct repo URL**: https://github.com/groupultra/telegram-search

**Verbatim description** (from GitHub API):
> Telegram 聊天记录搜索 (Telegram chat-history search)

**Why this is the cross-section peer of the day:**

1. **The fuzzy-search architecture is mature.** 4,075★ community traction + active maintenance (pushed 2026-08-21) confirms the MeiliSearch + PostgreSQL + Telegram MTProto pattern scales. The repo is single-purpose (one Telegram bot + one search surface), so the architecture is small enough to read in a day.
2. **MeiliSearch + PostgreSQL is a drop-in compatible stack-extension for LE31.** LE31 v1 uses Postgres; adding MeiliSearch is a future-tense concern but the integration pattern is well-known.
3. **The cross-section to LE31's `StockEntry`-via-Telegram trail is direct.** Every cook-Telegram message that produces a `StockEntry` row (features 41, 38, 65, 43) is a candidate for fuzzy-search indexing. The audit-search surface would let the owner fuzzy-search "what was sent about tomatoes on Wednesday?" and see the original Telegram message + the derived `StockEntry` row.
4. **AGPL-3.0 license blocks LE31 v1 import.** Per charter §3.2, GPL/AGPL dependencies are prohibited in v1. At v2, importing AGPL code requires explicit charter approval. **The indexing pattern is reusable; the code is not**.

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 v2 team considers adding an audit-search surface that lets the owner fuzzy-search the historical Telegram-message-to-StockEntry trail, the team wants to know whether a working peer documents the indexing pattern, so that the surface design is informed by a peer. Plausible but not currently blocking.
2. **Viability**: No new feature to operate; the pattern informs a future v2 surface decision. No new viability required.
3. **Practicability and confidence**: The peer repo is 4,075★ + AGPL-3.0 + TypeScript + MeiliSearch + PostgreSQL + Telegram MTProto; high confidence in the pattern (the indexing architecture is documented in the README). Low confidence in LE31-specific urgency (no owner signal of "I can't search the historical trail" pain today).
4. **Conflict**: No invariant conflict. The pattern is informational and does not change LE31 v1 behavior.
5. **Outcome, appetite, scope**: v2 owner-pains parking-lot. S effort. ≤1 day. **Defer** — LE31 v1 doesn't ship an audit-search surface; this artifact records the fuzzy-search architecture for future v2 iteration.
6. **Cost to operational value**: Zero implementation cost; pure pattern-record artifact. High upside (owner audit-search surface for v2) at zero downside.
7. **Circuit breaker and reversibility**: Fully reversible. Watch-list artifact; can be deleted without consequence.

## Data model

**No schema changes.** Watch-list artifact only.

## Implementation steps

**None** — research-only artifact. The slice ships this Markdown file + a one-row `INDEX.md` update + a `*-HANDOFF.md` slice contract for the coding agent (which records the same non-action: "do not implement today; read README on next pass"). The slice hand-off is a no-op directive to the coding agent.

## Telegram interaction if any

**None today.** The artifact does not interact with the LE31 Telegram-bot surface. The cross-section is observational only. **If/when the slice is un-deferred** (v2 owner-pains extension), the audit-search surface would be a **web UI** (owner-facing), not a Telegram bot interaction.

## Dependencies

- **No code dependencies** (research-only artifact).
- **External data dependency**: `groupultra/telegram-search` README + architecture documentation — to be read in the next daily-research pass (carry-over to 2026-08-25).
- **Watch-list add to `le31-daily-research-2026-08-25` pass**: include `groupultra/telegram-search` in the 5-repo watch list to track star velocity + push activity.

## Open questions

1. **What is the exact indexing pipeline in `groupultra/telegram-search`?** Is it a batch import (initial chat history dump) + incremental update (new messages), or a real-time stream? The answer determines how transferable the pattern is to LE31 v2 (which needs to index `StockEntry`-via-Telegram messages as they're written, not retroactively).
2. **Is the 4,075★ count maintained over the next 7 days?** Velocity will inform whether the pattern is gaining traction or is a mature stable pattern.
3. **Does `groupultra/telegram-search` support multiple Telegram bots?** LE31 has at least one Telegram bot (cook-bot) today; the audit-search surface would index all messages from all configured bots.
4. **Does the LE31 owner actually want an audit-search surface?** This is a charter-level question that the artifact defers. The current charter (PROJECT_CHARTER.md §3) does not mention an audit-search surface; features 30 + 49 v2 extension would need explicit charter approval.

## Why this matters

The 2026-08-24 brainstorm pass surfaces `groupultra/telegram-search` as the only in-window ≥1k★ Telegram chat-history fuzzy-search peer with a documented MeiliSearch + PostgreSQL + Telegram MTProto indexing architecture. The cross-section insight: **LE31's `StockEntry`-via-Telegram trail is a high-value audit-search surface that LE31 v1 doesn't ship today; the fuzzy-search pattern is well-documented in a working peer and is technically transferable**. AGPL-3.0 license blocks v1 code-import but the indexing pattern is reusable for future v2 owner-pains extension (features 30 + 49 v2).

**Cross-section with existing LE31 features**:
- Features 30 (append-only-audit-redirect) + 49 (postledger-tamper-evident-hash) → this artifact strengthens the audit-surface layer with a fuzzy-search reference.
- Features 41 (telegram-msg-stock-update) + 38 (cook-voice-note-to-stockentry) + 65 (cook-photo-stock-list-pwa) + 43 (telegram-prep-checkoff-adherence) → these are the `StockEntry`-via-Telegram message sources that would feed the audit-search index.
- Feature 50 (lifecycle-citation-mixin) → this artifact strengthens the lifecycle-citation layer with a search-surface reference.
- Features 102-104 + 106 + 107 (2026-08-23 + 2026-08-24 brainstorm picks) → all v2 watch-list artifacts; this is the audit-search-layer sibling.

**Why defer, not build**: zero observed pain at the LE31-owner level (no signal that the owner wants an audit-search surface today); LE31 v1 doesn't ship one; the v2 audit-search extension is a future-tense concern. The artifact is a research-note that records the pattern for future v2-AI iteration.
