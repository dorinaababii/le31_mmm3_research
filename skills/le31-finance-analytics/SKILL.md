---
name: le31-finance-analytics
description: Use when changing LE31 prices, taxes, tips, bills, payments, cash reconciliation, revenue reports, KPIs, exports, forecasts, or AI-derived owner insights. Requires exact reproducible calculations, source-row traceability, and evidence before prediction.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, finance, analytics, reporting, forecasting]
    related_skills: [le31-conventions, le31-data]
---

# LE31 Finance and Analytics

## Overview

Finance and analytics interpret the same operational records. Every amount, KPI, forecast, and recommendation must be reproducible from source rows, explicit assumptions, and a defined restaurant business period.

## When to Use

Use for prices, taxes, tips, bills, payments, shifts, cash variance, revenue, dashboards, CSV exports, menu engineering, demand/waste forecasting, and owner-facing AI insights.

## Financial Rules

- Never use binary floating point for authoritative money.
- Follow the resolved project representation—integer EUR cents or `Decimal`—consistently. The charter history conflicts; resolve before implementation.
- Store/display currency explicitly as EUR unless the single-currency decision changes.
- Tax, rounding, inclusive/exclusive semantics, service charge, discounts, refunds, and tip formula are product decisions, not code defaults.
- The service-charge decision remains pending unless explicitly resolved.
- A closed bill is immutable; corrections use an explicit adjustment/refund workflow.
- Cash reconciliation preserves expected, counted, variance, actor, and timestamp; never overwrite history to force zero variance.

## Metric Contract

Define business question and owner action; numerator/denominator/filters/unit; source rows and eligible states; `Europe/Paris` period boundaries; missing/late/corrected data treatment; and a hand-calculated validation example. Completion: the displayed number is reproducible.

## Analytics Ladder

Use the least complex method: descriptive totals; deterministic ratios/menu engineering; simple baseline forecast; statistical/ML model only with sufficient history and measurable improvement; owner AI only when grounded in cited rows. Do not claim forecasting viability before representative history exists.

## Forecast Contract

Record training window/cutoff, target/unit, feature provenance, baseline, backtest method/metric, uncertainty, model/formula version, generated time, and recommended owner action. Predictions never mutate historical facts; owner can ignore or override them.

## Reporting and Exports

Dashboard and CSV share definitions. Label provisional/open versus finalized/closed values. Preserve exact amounts and stable columns. Explain empty/partial periods. Link owner insights to contributing rows where practical.

## Common Pitfalls

1. Treating revenue, cash, tax, and tips as interchangeable.
2. Choosing rounding rules in code without a decision.
3. Training on too little history or evaluating on training data.
4. Adding ML where a query or moving average suffices.
5. Showing KPIs without eligible states and Paris-day boundaries.
6. Letting AI state unsupported conclusions.

## Verification Checklist

- [ ] Currency representation and financial policies are resolved.
- [ ] Every metric has a reproducible contract and hand-checked example.
- [ ] Dashboard/export totals reconcile to source rows.
- [ ] Forecast beats a named baseline or remains explicitly experimental.
- [ ] Owner recommendations expose evidence, uncertainty, and override behavior.
