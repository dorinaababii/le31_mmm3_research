# Feature 17 — Demand Forecasting (Beyond Simple Averages)

> **Priority**: P2 · **Effort**: S–M (2–5 days) · **Source**: AI/ML subagent
> research (Nixtla/neuralforecast, unit8co/darts, facebook/prophet) + natural
> extension of [feature 07 — demand estimation](07-demand-estimation.md).
> **One-line**: Replace the simple 14-day average with proper time-series
> forecasting that handles day-of-week, seasonality, and trend.

## Why this matters

Feature 07 already covers "prep quantities for tomorrow" with a simple
`round(avg_14d * 1.1)` formula. That's fine for week 1 but ignores:
- Day-of-week seasonality (Saturday ≠ Tuesday).
- Trend (gradual growth over weeks/months).
- Special events (holidays, local festivals).
- Cross-item correlations (when Schnitzel sells out, Burger spikes).

Time-series libraries handle these properly and are all Python-friendly.

## Goal

Forecast tomorrow's prep quantities per item using proper ML models, with
explainable outputs and a graceful fallback to the simple average when
historical data is sparse.

## Scope

**In scope (v1 of this feature):**
- Forecast for each `MenuItem` for the next 1–14 days.
- Models: Prophet (baseline) + Nixtla NeuralForecast (NHITS, TFT) — both Python.
- Features: day-of-week, week-of-year, French holidays (configurable),
  rolling 7/14/28 day means, item-level trend.
- Backtest harness: train on first 80% of history, test on last 20%, report MAPE.
- Forecast stored in DB; Telegram bot `/forecast` displays it.
- Fallback to simple 14-day average when <14 days of history per item.

**Out of scope:**
- Real-time re-training (we retrain weekly).
- Multi-item joint forecasting (cross-correlations).
- Weather / event data integration (Punted; needs API keys + GDPR).
- LSTM from scratch (overkill; use libraries).

## Description

A nightly APScheduler job rebuilds the forecast for the next 14 days for
each active menu item:

1. **Load history** — `SELECT menu_item_id, date(served_at), SUM(qty) FROM order_item WHERE served_at > NOW() - 90 days GROUP BY 1, 2`.
2. **Build per-item series** — one row per (item, date) including days with 0 sales.
3. **Train** — Prophet (fast, interpretable) per item, or NeuralForecast (better
   accuracy, more compute).
4. **Predict** next 14 days.
5. **Store** in `Forecast` table with confidence intervals.
6. **Surface** via `/forecast` Telegram command.

The cook sees: "Schnitzel — Saturday forecast: 24 (range 18–30). Last Saturday: 22. Buffer included."

## Data model

```
Forecast
  id              PK
  menu_item_id    FK
  forecast_date   DATE
  predicted_qty   Decimal
  p10_qty         Decimal  (10th percentile — for "if I'm conservative")
  p90_qty         Decimal  (90th percentile — for "if I'm aggressive")
  model_version   TEXT    ('prophet-1.5' | 'nhits-1.0' | 'avg14d-fallback')
  generated_at    DATETIME
  trained_until   DATE    (training cutoff)
```

## Implementation

1. **Add `prophet` (or `nixtla`)** to requirements.
2. **Add `Forecast` table**.
3. **Background job** (`backend/app/services/forecast_pro.py`):
   nightly at 03:00; trains + writes forecasts.
4. **Telegram command** in `cook_bot.py`: `/forecast` returns tomorrow's
   predictions formatted nicely.
5. **Backtest script** `scripts/backtest_forecast.py` — measures MAPE on
   historical data; logs which model wins.

## Library choices

| Library | Stars | License | Why pick |
|---|---|---|---|
| **facebook/prophet** | ~18k | MIT | Industry standard, fast, easy to install, well-documented |
| **Nixtla/neuralforecast** | ~3k | Apache-2.0 | State-of-the-art accuracy; supports NHITS, TFT, NBEATS |
| **unit8co/darts** | ~9k | Apache-2.0 | Unified API, lots of models, good docs |
| **sktime/sktime** | ~8k | BSD-3 | Sklearn-compatible time series |
| **PyFlux** | ~2k | MIT | Bayesian; very expressive but slower |

**Recommended start**: Prophet (1 day to integrate, well-known).
**Recommended upgrade**: Nixtla NeuralForecast with NHITS model (3 days, +30% accuracy).

## Telegram interaction

```
Cook: /forecast
Bot:  Forecast for Saturday 25 Jul:

       Item          Predicted  Range         vs. last Sat
       Schnitzel     24         18–30         +2 (+9%)
       Burger        20         15–25         +1 (+5%)
       Tiramisu      8          5–11          +3 (+60%) [⚠ outlier]

       Model: Prophet-1.5 (trained on 87 days)
       Confidence: 80 %

       [Use these numbers] [Edit]
```

## Dependencies

- [07-demand-estimation.md](07-demand-estimation.md) — base feature, this replaces it.
- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — `OrderItem.served_at` is the data source.

## Open questions

- Retrain cadence: nightly vs weekly vs on-demand? (Default: nightly.)
- Holiday list: hard-coded EU/US, or user-configurable? (Default: user-configurable.)
- Should forecasts be shown as a single number (point forecast) or as a range?
  (Range; ranges build trust.)
- How do we handle new items with no history? (Fallback to similar item's history + manual override.)

## Why this matters

The simple 14-day average gets you ~70% accuracy. Prophet with weekly
seasonality gets ~85%. NeuralForecast NHITS gets ~90%. Each percentage point
of accuracy is roughly **€50–100/month saved in waste + lost sales** for a
small restaurant — the ROI on this feature is weeks, not months.

The catch: this feature needs **at least 4 weeks of history** to be useful.
For a brand-new restaurant, fall back to the simple formula from feature 07
until then.