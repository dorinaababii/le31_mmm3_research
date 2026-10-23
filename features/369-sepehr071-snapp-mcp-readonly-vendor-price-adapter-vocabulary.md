# Feature 369 — `sepehr071-snapp-mcp-readonly-vendor-price-adapter-vocabulary` (defer)

> **NEW observation (2026-10-23).** Documents in-window GitHub repo `sepehr071/snapp-mcp` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★35/⑂3 = the highest-traction pick of this pass** (series context: below feature 353's ★148, above the ★5 that was the series high for most of the 84 passes before it — so ★35 is mid-series, not a record), **728 KB**, **Python ✓ ON-STACK**, created **2026-10-02 AND pushed 2026-10-22 = IN-WINDOW BY BOTH FIELDS**, `archived=false`, `fork=false`, 1 open issue. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-23, not from search-result numbers. Description (verbatim from GitHub API): *"Unofficial read-only MCP server for Snappfood and SnappMarket: search dishes and groceries, compare true prices with delivery, read menus, reviews and flash deals from Claude or Cursor."* Topics (verbatim): `ai-agents, claude, claude-code, cursor, food-delivery, github-copilot, grocery, iran, mcp, mcp-server, model-context-protocol, persian, price-comparison, python, restaurant, snapp, snappfood, snappmarket`. Bucket: **v1 (unofficial read-only third-party market-data adapter vocabulary)** — Pick C of Daily Brainstorm 2026-10-23. Build verdict: `defer` (parking-lot; **vocabulary reference only**; explicit legal-risk flag below).

## Goal

Record the **unofficial read-only vendor adapter** as a persistent cross-section reference: a single-vendor adapter built by a third party against a closed, deliberately-unfriendly API, supplying market data the vendor never intended to expose. **This feature carries an explicit legal-risk flag and is NOT a proposal to build such an adapter for LE31.** No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **market-data shape**: menus, prices, reviews, promotions, delivered-price comparison — read from a dominant delivery platform, exposed read-only.
- A written record of the **commercial question**: the owner already knows today's street prices (competitors, delivery platforms, promotions) and LE31 has no way to hold or compare that. Whether the owner *wants* that is **inferred, not observed** — record it as such.
- A written record of the **legal/maintenance risk** that makes this a `defer` rather than a `build`: scraping a closed API introduces ToS exposure for the owner, and a maintenance burden the owner cannot self-perform.

**Out of scope (defer artifact):**

- Any scraper, adapter, or integration code.
- Any market-data feature.
- **Any statement that this is legal, authorised, or safe to build for LE31.** It is not, absent an explicit owner decision and legal advice.

## Out of scope

- See "Scope" above. Vocabulary-only; no code. **The legal-risk flag is binding on any future reader.**

## Evidence / JTBD

- **Evidence class**: observed for the shape (the repo exists, is MIT, is public, and is read-only by its own description); **inferred** for the LE31 need — no LE31 owner has asked for competitor pricing.
- **Confidence**: high that this shape is built by third parties when a market's dominant platform has no API; **low** that LE31 needs it.
- **Traction caveat, recorded plainly**: ★35⑂3 on 728 KB of adapter code is real API data and indicates that someone found this valuable enough to publish. **It is not evidence that restaurant owners demand market data** — the audience is MCP/Claude users, not restaurant operators. No owner mention of this need exists in 84 passes.
- **JTBD**: none observed. If one existed it would read: *"When the owner sets tomorrow's prices, they want to know what the platforms and the shop next door are charging, but struggle because *there is no tool in the restaurant that holds that number*, so that *pricing is a decision rather than a guess."* Recorded as hypothetical only.

## Description

Snappfood is Iran's largest food-delivery platform. `snapp-mcp` reads its menus, prices, reviews and flash deals and exposes them through MCP to Claude/Cursor. The transferable primitive is not the integration — it is the observation that **every restaurant-tech market has one dominant delivery platform with no public API, and third parties build the adapter anyway.**

Three sub-primitives worth naming:

1. **Read-only by construction.** The adapter does not write. This matters for LE31 because a read-only market-data surface cannot corrupt operational state even if the vendor changes the API — it degrades to "no data", not "wrong orders".
2. **The one-vendor-per-market shape.** Not a general aggregator; a hand-written adapter for one specific platform, by someone who uses that market daily. The competence is local, not technical.
3. **Delivered-price vs menu-price comparison** (`compare true prices with delivery`) — the gap between the menu price and what the customer actually pays after delivery fees. This is a real, LE31-shaped insight about price presentation, though it concerns the platform's pricing, not the restaurant's.

## Data model

None shipped. The vocabulary implies a **MarketPriceSnapshot** (item, menu price, delivered price, timestamp, source) — **append-only, never authoritative.** Critically, this must be a *reference* table with no path into operational state. LE31's `MenuItem.price_eur` remains the single source of truth for what the restaurant charges; a market snapshot is a comparison value with a timestamp and a source label.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) a LE31 owner explicitly asks for competitor/market pricing; (2) an explicit owner decision to accept the legal exposure; (3) legal advice on ToS compliance for the target market. **Absent all three, this must not be built.**

## Telegram interaction if any

None, and explicitly **not recommended**. Market pricing is an owner/staff concern, not a cook concern; surfacing competitor prices on the cook's Telegram surface would be noise.

## Dependencies

None today. If ever built: a scraping/maintenance dependency on an API the vendor can change without notice, and an unversioned third-party surface — both violate §3.2 (viability: the owner must be able to maintain it without specialist help) and §3.4 (deterministic kernel).

## Open questions

1. **Is market pricing a real LE31 need or a hypothetical one?** Currently hypothetical. No owner mention in 84 passes.
2. **Is there a lawful alternative?** Regional public price indices, or a manually-entered competitor sheet, would answer the same question without scraping. Unresearched — deliberately not researched this pass, because researching it implies intent to build.
3. **Does this touch §3.7?** Market data is not guest data, so §3.7 is not triggered. The exposure is legal/ToS, not privacy.

## Why this matters

Because it names a question LE31 cannot currently answer and has never been asked: *what does the market look like today?* And because it is the third pick in three passes to be deferred on a **non-technical** risk rather than a technical one — 366 on legal exposure, 365 on an unmade charter question, 364 on an unmade AI decision. The recurring pattern is that LE31's backlog is gated by owner decisions, not by engineering.

## Cross-section

Features 290 (`prime-cost`), 349 (`gfs-invoice-breakdown`, vendor-document ingestion — the *supplier* side of the same data problem), 353 (FloCafe). Sister-case to 349 in structure (both are third-party data ingestion) but opposite in risk: 349 reads documents the *owner* legitimately possesses; 366 reads a platform the owner does not control. GitHub `sepehr071/snapp-mcp` is unique vs features 1–363 (verified by ripgrep against `features/` and `specs/`). Fully reversible — documentation-only artifact.