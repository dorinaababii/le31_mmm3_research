# AI/ML Features Research — Summary

> **Compiled**: 2026-07-24
> **Method**: 1 delegated subagent (`delegate_task`) running 8 API calls
> in 13 minutes (slow because GitHub rate limits + search). Full 11 KB report
> saved at `/opt/data/cache/delegation/subagent-summary-0-20260724_182134_143346.txt`.
> **Outputs**: 4 new feature specs (`19`–`22`), plus a summary file.

## TL;DR — Ship in this order

1. **Menu engineering** ([feature 19](../features/19-menu-engineering.md)) — 2-3 days, pure SQL on existing data, immediate margin insight. **#1 pick by AI/ML research.**
2. **Waste prediction** ([feature 20](../features/20-waste-prediction.md)) — 5-7 days software-only, uses the prepared-item ledger (our killer feature) as direct input. **#2 pick.**
3. **Recipe generation from leftovers** ([feature 21](../features/21-recipe-generation.md)) — 2-4 days with local Qwen2.5-3B. **#3 pick.** Compounds with #2.
4. **Sentiment analysis** ([feature 22](../features/22-sentiment-analysis.md)) — "weekend polish" feature. Defer until core is shipping.

## What the subagent covered

8 AI/ML features, each scored on:
- Use case (plain English)
- OSS / commercial APIs (URLs, license, stars, language)
- Effort estimate
- Data requirements
- Privacy / cost / practicality notes

The subagent ranked features by "ship first for a small restaurant" and we
followed that ranking in the feature spec order.

## Feature comparison

| # | Feature | Effort | Privacy | Cost | Rank | Our spec |
|---|---|---|---|---|---|---|
| 1 | Demand forecasting (Prophet / NeuralForecast) | 3-5d | low | free | – | [feature 17](../features/17-demand-forecasting-ml.md) (already specced) |
| 2 | Menu engineering (Kasavana-Smith matrix) | 2-3d | none | free | **#1** | [feature 19](../features/19-menu-engineering.md) |
| 3 | Food waste prediction | 5-7d (no CV) | low | free | **#2** | [feature 20](../features/20-waste-prediction.md) |
| 4 | Dynamic pricing | 7-10d | low | free | defer | not specced (low ROI for single restaurant) |
| 5 | Sentiment analysis of reviews | 3-4d | none | $5-15/mo | "polish" | [feature 22](../features/22-sentiment-analysis.md) |
| 6 | Menu A/B testing | 5-7d | low | free | defer | not specced (low traffic for single location) |
| 7 | CV plate waste | 15-25d | medium | $$$ hardware | defer | not specced (overkill) |
| 8 | Recipe generation from leftovers | 2-4d | low | free | **#3** | [feature 21](../features/21-recipe-generation.md) |

## Why this is mostly local-only

The subagent's key insight: **most of these features run fully on-prem** —
no per-call API cost, no privacy concerns, no vendor lock-in.

| Feature | Local? | Required model size |
|---|---|---|
| Demand forecasting (Prophet) | ✅ | <100 MB |
| Menu engineering | ✅ (pure SQL) | 0 |
| Waste prediction | ✅ | <100 MB |
| Recipe generation | ✅ | ~4 GB (Qwen2.5-3B) |
| Sentiment analysis | ✅ | ~250 MB (DistilBERT) |

Only **sentiment** has a modest recurring cost (Google Places API ~$5-15/mo).
Everything else is free at the inference level once the models are downloaded.

## Cross-feature synergies

The 4 new features **compose** with each other and with existing v1/v2 features:

```
                    ┌────────────────────────┐
                    │  Allergen tracking (10) │
                    │  Ingredient + Recipe    │
                    └───────────┬────────────┘
                                │ provides Ingredient.cost_per_unit
                                ▼
                    ┌────────────────────────┐
                    │  Menu engineering (19)  │
                    │  Kasavana-Smith matrix  │
                    └───────────┬────────────┘
                                │ uses popularity + margin
                                ▼
                    ┌────────────────────────┐
                    │  Stock tracker (03)     │
                    │  Prepared-item ledger   │
                    └───────────┬────────────┘
                                │ data source
                                ▼
                    ┌────────────────────────┐
                    │  Waste prediction (20)  │
                    │  Tonight's likely waste │
                    └───────────┬────────────┘
                                │ predict leftovers
                                ▼
                    ┌────────────────────────┐
                    │  Recipe generation (21) │
                    │  Suggest dishes         │
                    └───────────┬────────────┘
                                │ tomorrow's menu
                                ▼
                    ┌────────────────────────┐
                    │  Demand forecast (17)   │
                    │  Prep quantities        │
                    └────────────────────────┘
```

This is the **flywheel**: better ingredient data → better menu engineering →
better stock tracking → better waste prediction → better recipe generation →
better demand forecasting → less waste, more profit.

## What was deliberately skipped (not specced)

- **Dynamic pricing (#4)** — needs more traffic than a single location has; risk of alienating guests with visible price changes. Better suited to chains.
- **Menu A/B testing (#6)** — same issue; statistical power too low at single-restaurant volume. Build only if we have multi-location data.
- **Computer vision plate waste (#7)** — needs camera hardware ($250+ for Jetson), labels a custom dataset, and the prepared-item ledger captures ~70% of the value at 10% of the cost. Build only if the soft approach underdelivers.

## Library stack — recommended starting point

For someone implementing these features:

```txt
# Forecasting
prophet>=1.2

# Tabular ML (XGBoost for waste prediction)
xgboost>=2.0

# NLP (sentiment, recipe generation)
transformers>=4.40
torch>=2.3   (CPU-only is fine)

# Local LLM (recipe generation)
ollama>=0.3  # then: ollama pull qwen2.5:3b

# Embeddings (recipe retrieval)
sentence-transformers>=3.0
```

Total disk footprint for the AI features: **~5 GB** (mostly the local LLM).

## Method note (for the next agent)

The subagent's full report is at:
```
/opt/data/cache/delegation/subagent-summary-0-20260724_182134_143346.txt
```

The adjacent-OSS subagent's output (10 categories — QR menus, loyalty,
delivery, kiosks, reservations, voice, CV occupancy, scheduling, suppliers,
accounting) was unfortunately truncated to one planning line in the live
transcript. The owner-pains research came through clean and drove 8 of the
10 v2 specs; the AI/ML research came through clean and drove these 4
additional specs (19–22). If you need deeper adjacent-OSS research, re-dispatch
that subagent with a smaller scope (3 categories at a time, 200-word response cap).