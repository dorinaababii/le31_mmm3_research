# Feature 82 — Owner Public-Data Watch Bot

> **Priority**: P2 · **Effort**: M (3–5 days) · **Source**: brainstorm 2026-08-18 (cross-section pick B) · **Bucket**: v2 owner-pains
> **One-line**: A new `/whats-new-today` command on the existing cook bot that surfaces owner-relevant public-data changes (EUR-Lex regulatory shifts, ECB FX, CNIL updates, owner-configured keywords) filtered by the owner's profile, in plain language.

## Goal

The owner of a single small restaurant does not have time to monitor EUR-Lex, the ECB, CNIL, and BOFiP for regulatory / FX / privacy / tax changes that affect their operation. But these changes do affect them (a new VAT rule, a USD/EUR swing that hits USD-imported ingredients, a CNIL privacy-rule update). The cross-section pattern (owner profile + public open-data + rule filter + actionable push) is observed in `djfksjd/sole-search` (45★ Python, 206KB, in-window push 2026-07-30T08:10:40Z, Korean small-business-owner public-support-program research agent: scrapes 소상공인24 + 기업마당, applies 5-stage eligibility rule from the owner profile, returns a "what to apply for today" report).

## Scope

**In scope (v2 owner-pains):**
- A new `/whats-new-today` command on the existing cook bot (aiogram v3) that surfaces owner-relevant public-data changes.
- Data sources (initial):
  - **EUR-Lex REST API search/notice endpoint** (NOT the RSS, which is WAF-blocked on this VPS for 14+ consecutive days) — daily fetch of new notices matching `restaurant OR hospitality OR catering OR VAT OR service-charge OR tickets-restaurant` keywords.
  - **ECB FX RSS** (USD/EUR daily reference rate) — already fetched daily by the daily-research pass; can be sourced from there.
  - **CNIL EN+FR** (privacy regulator) — daily fetch of new decisions.
  - **Owner-configured keywords** (e.g., "VAT", "tickets-restaurant", "service-charge", "smoking ban") — stored in a new `OwnerWatchKeywords` table.
- Profile filter: the owner's profile is `{city: str, license_type: str, hours: enum, has_alcohol_license: bool, has_terrace: bool, ...}` — already captured in `Restaurant` / `OwnerProfile` table.
- Plain-language summary: "EUR-Lex: 2 new VAT-relevant notices since yesterday; ECB: USD/EUR 1.1593 (flat vs. last week); CNIL: 0 new in-window; your keywords matched: 0".
- Rule engine: deterministic Python (NOT AI in v1); an optional AI summarizer layer is v2-AI and out of scope.

**Out of scope (v2 owner-pains):**
- Real-time push (this is a daily digest on demand, not a real-time alert).
- AI summarization (charter §3.2 "AI may assist owner/staff, with observable evidence and a non-AI fallback" — the rule engine IS the non-AI fallback; AI is a v3 cross-cut).
- Government-grant / subsidy matching (the Korean peer's domain; not EU-relevant today).
- Regulatory compliance dashboard (v3 territory; defer).

## Description

The owner types `/whats-new-today` on the cook bot (which they're already on, per feature 29's owner chat id). The bot fetches the latest EUR-Lex REST search results (24h window), ECB daily FX (USD/EUR), CNIL daily decisions, and owner-configured keyword matches. It applies the rule filter (keywords matching owner's profile + configured keywords) and returns a plain-language summary with at most 5 items per source.

The EUR-Lex REST API (CEF API: https://eur-lex.europa.eu/content/help/data-reuse/celex-web-service.html) replaces the broken RSS. The API returns JSON for queries like `?q=restaurant&dateFrom=2026-08-17&dateTo=2026-08-18&type=notice` — the bot calls this once per `/whats-new-today` invocation with a 24h window. The response is cached for 1 hour to avoid hammering the endpoint.

The owner-configured keywords live in a new table:

```sql
CREATE TABLE owner_watch_keywords (
    id SERIAL PRIMARY KEY,
    owner_user_id INT REFERENCES users(id),
    keyword TEXT NOT NULL,
    source TEXT NOT NULL,  -- 'eurlex' | 'cnil' | 'custom'
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    UNIQUE(owner_user_id, keyword, source)
);
```

Keywords are added via `/watch-add <keyword>` (cook bot) and removed via `/watch-rm <keyword>`. The owner can have up to 20 keywords.

## Data model

New table `owner_watch_keywords` (above). Reads:
- EUR-Lex REST API (no schema; cached in `agent/cache/eurlex_<date>.json` for 1h).
- ECB FX (already in daily-research; cached).
- CNIL RSS/HTML (already in daily-research; cached).
- `Restaurant` / `OwnerProfile` (existing tables).

No migration to `StockEntry`, `Visit`, `Order`, `OrderItem`, `Bill`, `Payment`. **Zero schema impact on the core ledger.**

## Implementation steps

1. Wire EUR-Lex REST API client in `agent/services/public_data/eurlex.py` (HTTP GET, JSON parse, 1h cache).
2. Wire ECB FX client in `agent/services/public_data/ecb.py` (reuse daily-research cache).
3. Wire CNIL client in `agent/services/public_data/cnil.py` (reuse daily-research cache).
4. Add `OwnerWatchKeywords` SQLModel table + Alembic migration.
5. Add `cook_bot/handlers/whats_new_today.py` aiogram v3 handler bound to `/whats-new-today` (owner chat id).
6. Add `cook_bot/handlers/watch_add_rm.py` for `/watch-add` / `/watch-rm` keyword management.
7. Add `agent/services/rule_engine.py` with `apply_profile_filter(notices, owner_profile) -> list[Notice]` deterministic rule engine.
8. Write 6 acceptance tests in `agent/tests/test_whats_new_today.py`:
   - empty data sources → "no new items today"
   - EUR-Lex has 2 notices matching "VAT" → both surface in summary
   - EUR-Lex has 10 notices → only top 5 by recency surface
   - owner keyword "service-charge" with 0 matches → "0 matches" in summary
   - owner profile excludes `alcohol_license` → alcohol-related notices are filtered out
   - cache hit within 1h → second call within 1h does NOT re-hit EUR-Lex
9. Run all tests; commit + push.

## Telegram interaction if any

- `/whats-new-today` (owner) — returns the daily summary as a Telegram message (max 4096 chars; truncate + "..." for very long summaries).
- `/watch-add <keyword>` (owner) — adds a keyword to the owner's watch list.
- `/watch-rm <keyword>` (owner) — removes a keyword.

## Dependencies

- **EUR-Lex REST API** (CEF API) reachable. **The current EUR-Lex RSS is blocked on this VPS**; the REST API is the replacement. Verify reachability with a `curl -sS "https://eur-lex.europa.eu/..."` smoke test before committing to this slice.
- **ECB FX data source** (already fetched daily; reuse the daily-research cache).
- **CNIL data source** (already fetched daily; reuse the daily-research cache).
- **[feature 29] Owner No-Account Live-Floor Link** — adjacent but not a prerequisite. The owner chat id can be derived from `users` table if feature 29 not shipped.
- `[feature 39] Owner Daily Recap Telegram` — adjacent but not a prerequisite. Feature 39 is the **internal ledger** recap; this feature is the **public regulatory** recap.

## Open questions

- Should `/whats-new-today` be **proactively pushed** at a fixed time each day (e.g., 07:00 local) or only on demand? Charter §3.2 "explicit operational state" suggests on-demand only — owner must ask. Recommend on-demand for v1.
- Should owner-configured keywords support **boolean AND** (e.g., "VAT AND restaurant") or just **substring match**? Substring match is sufficient for v1.
- Should the rule engine include a **priority rank** (e.g., "VAT notice is high priority, service-charge notice is low priority")? Out of scope for v1; rule engine returns items in source-default order.

## Why this matters

The owner of a single small restaurant is regulatorily exposed: VAT rules change, EUR/USD swings hit USD-imported ingredients, CNIL privacy updates affect guest data handling, BOFiP tax notices affect payroll. Without a profile-aware public-data push, the owner learns about regulatory changes only when something breaks (an inspector visit, a tax audit, a privacy complaint). With `/whats-new-today`, the owner gets a daily plain-language summary of the regulatory deltas that affect their specific profile, on the surface they already use (Telegram), in the language they already understand (no jargon). The cross-section pattern (profile + public-data + rule filter + push) is observed in the in-window Korean sole-search agent at 45★ — the strongest small-business-owner JTBD signal of the 19-pass series.

## Distinct from existing features

- **Feature 29 (Owner No-Account Live-Floor Link)** gives the owner a signed expiring link to a private page. `/whats-new-today` gives the owner an inline Telegram summary.
- **Feature 39 (Owner Daily Recap Telegram)** surfaces **internal ledger** deltas (covers count, voids, top movers). `/whats-new-today` surfaces **public regulatory** deltas.
- **Feature 69 (Owner No-Account Shift Recap Link)** gives a printable end-of-shift recap. `/whats-new-today` gives an end-of-day regulatory recap.

## Cross-section evidence

- **Anchor**: [djfksjd/sole-search](https://github.com/djfksjd/sole-search) — 45★ Python, 206KB, pushed 2026-07-30T08:10:40Z. Korean small-business-owner public-support-program research agent skill.
- **Adjacent (in-window)**: `zhengjinjun1975/factory-ontology` (6★, JS, 2026-08-18) — Chinese factory-data QA framework with ontology + GraphRAG; adjacent JTBD (small-business operational data QA) but JS stack.
- **Adjacent (carry-over)**: `bilalfarukozdemir/vitrinci` (5★, TS, 2026-08-14) — local-business website builder.
- **Daily-research backdrop**: the daily-research pass has been reporting EUR-Lex RSS WAF-block for 14+ consecutive days; this slice switches to EUR-Lex REST API as a result.

## Re-evaluation trigger

- EUR-Lex REST API confirmed reachable from this VPS → status becomes build-candidate.
- An in-window ≥10★ EU-specific profile-aware public-data peer surfaces → escalates evidence to high.
- The LE31 owner explicitly asks for it → status becomes build.
- Charter §3.2 revised to allow proactive regulatory push → expand scope to include cron-driven daily push.

## Status

**defer** — gate verdict from brainstorm 2026-08-18 (HMM-99). EUR-Lex RSS currently blocked on VPS; switch to EUR-Lex REST API when wiring the slice. No observed owner pain in window. Re-evaluate when EUR-Lex REST API is wired and reachable.
