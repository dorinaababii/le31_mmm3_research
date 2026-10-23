# HANDOFF — Feature 366: `sepehr071-snapp-mcp-readonly-vendor-price-adapter-vocabulary`

**Upstream source repo: [`sepehr071/snapp-mcp`](https://github.com/sepehr071/snapp-mcp)** — see `features/366-sepehr071-snapp-mcp-readonly-vendor-price-adapter-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

> **⚠️ BINDING LEGAL-RISK FLAG.** This feature records a shape, and the shape involves scraping a third party's closed API. **Nothing in this document authorises building such an adapter for LE31.** A future implementer must not treat the presence of this HANDOFF as approval. See "Circuit breaker" below.

## Active feature path

`features/366-sepehr071-snapp-mcp-readonly-vendor-price-adapter-vocabulary.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-23).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ⚠️ | **No observed JTBD.** The hypothetical JTBD is recorded explicitly as hypothetical. No LE31 owner has asked for competitor or market pricing in 84 passes. Evidence class: **inferred**, confidence **low**. |
| 2 | Viability | ⚠️ | **MIT ✓ §3.2 STRICTLY-COMPATIBLE**, ★35⑂3 (highest-traction pick of this pass; mid-series overall). **⚠️ Traction caveat: the audience is MCP/Claude users, NOT restaurant operators — ★35 is not evidence that owners demand market data.** More seriously, **viability is the binding check and it fails**: a scraper must be maintained when a third party silently changes an API, and the owner cannot self-perform that. That is exactly what §3.2 forbids. |
| 3 | Practicability and confidence | ⚠️ | Python on-stack, 728 KB, small. Technically easy; **operationally fragile**. Depends on an API the vendor can change without notice and may prohibit in its ToS. Evidence strength: high that third parties build these; low that LE31 should. |
| 4 | Conflict | ✓ | Does not violate §3.7 — market data is not guest data. **⚠️ But it conflicts with §3.2 (viability: un-maintainable by the owner) and §3.4 (deterministic kernel: behaviour depends on an external unversioned surface).** These are recorded as blocking, not resolved. |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v1 defer outcome. Max time: 45 min documentation. **Today: 0 build time.** |
| 6 | Cost to operational value | ⚠️ | Value is naming a question LE31 cannot answer. Cost if built is ongoing and owner-borne. **The ratio is unfavourable and is why this is `defer`, not `build`.** |
| 7 | Circuit breaker + reversibility | ✓ | No code today; revert by `git rm`. **If ever built, the circuit breaker is: no scraping without an explicit owner decision AND legal advice on ToS compliance for the target market. A lawful alternative (public price indices, or a manually-entered competitor sheet) was identified but deliberately NOT researched this pass — researching it would imply intent to build.** |

**Gate verdict: `defer` (parking-lot)** — no check hard-fails, but checks 1, 2, 3 and 6 all carry material reservations. `defer` because there is no observed need and the dominant risk is legal/maintenance rather than technical.

## Bucket

**v1 (unofficial read-only third-party market-data adapter vocabulary)** — Pick C of Daily Brainstorm 2026-10-23. `le31 v1 — Core MVP` exists (P-HMM-3); per `le31-feature-pipeline/SKILL.md` line 33 this sub-issue attaches to **`le31 Research` P-HMM-1**.

## Files to touch

**None today. None without the circuit breaker above clearing.**

If (and only if) an owner decision plus legal advice clears the breaker, the expected files are:

- `backend/models/market_price_snapshot.py` — new **append-only** `MarketPriceSnapshot` (item_name, menu_price_eur, delivered_price_eur, captured_at, source_label). **Never authoritative.** `Decimal`, never binary float (§3.6).
- `backend/services/market_data_adapters/` — one adapter module per vendor, each read-only, each declaring the endpoint it depends on.
- `backend/services/price_comparison_service.py` — compares `MarketPriceSnapshot` against `MenuItem.price_eur`. **Read-only against MenuItem — no write path may exist.**
- `tests/test_price_comparison_service.py` — **assert there is no code path from a MarketPriceSnapshot to `MenuItem.price_eur`.** This test is the feature: market data must never become authoritative.

## Verification protocol reference

`le31-conventions`: "Declaring done from a diff or passing tests alone" is a pitfall. The behavioural check that matters is the **absence** of a write path — assert it, don't assume it.

## Rollback path

`git rm features/366-*.md specs/369-*-HANDOFF.md`. Documentation-only. Fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — invariants, seven-check gate, and the "no fabricated requirements" rule
- `le31-data` — append-only rules
- `le31-finance-analytics` — EUR exactness (§3.6, `Decimal` not float)
- `le31-backend` — FastAPI/SQLModel patterns
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth

## Open questions carried into any future build

1. **Is market pricing a real LE31 need or a hypothetical one?** Currently hypothetical.
2. **What is the lawful alternative?** Unresearched, deliberately.
3. **Does this touch §3.7?** No — market data is not guest data. The exposure is ToS/legal, not privacy.