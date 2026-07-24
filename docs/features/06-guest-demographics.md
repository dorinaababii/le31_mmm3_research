# Feature 06 — Guest Demographics & Visit Analytics

## Goal

Capture lightweight, privacy-respecting per-visit data so the restaurant owner
can answer questions like "How many covers on Saturday?", "What's our average
dwell time?", "Spend per adult vs. child?".

## Scope

**In scope (v1):**
- Capture `party_size`, `adults`, `children` at seating time.
- Capture `opened_at` and `closed_at` → dwell time.
- Manager dashboard: covers/day, avg spend/cover, avg dwell, top items.

**Out of scope (v1):**
- Per-guest gender breakdown (privacy concerns; punt to v2).
- Loyalty / repeat-customer tracking (v2+).
- Customer-facing receipts / surveys.

## Description

When a party is seated, the waiter enters the party size breakdown into a
small form (1 screen, ~3 fields). That's it. No names, no phones, no emails
in v1. Dwell time is automatic from `opened_at` / `closed_at`.

## Data model

```
Visit  (id, table_id, server_id, opened_at, closed_at,
        party_size, adults, children)
```

Per-visit spend is computed: `bill.subtotal_items / party_size = spend_per_cover`.
Per-adult spend: `bill.subtotal_items / adults` (when `adults > 0`).

## Manager dashboard (web `/reports`)

Cards:
- **Today**: covers, sales, tips, avg cover, dwell time
- **This week**: same + comparison vs last week
- **By hour**: histogram of covers per hour-of-day
- **Top items**: top 10 by quantity sold today / week / month
- **Server leaderboard**: sales + tips per waiter

Charts (Chart.js via CDN, served from the static `index.html` shell):
- Covers by hour (bar)
- Spend distribution (histogram)
- Top items (horizontal bar)

## Privacy stance

- **No PII in v1** — no names, phones, emails. Only counts and timestamps.
- **Aggregated views only** — never "show me which tables had 4 adults last
  week" (would be re-identifiable in a small restaurant).
- **Retention**: keep `Visit` rows for 12 months for trend analysis; aggregate
  older data into monthly summaries.

## Dependencies

- [01-table-management.md](01-table-management.md) — seating creates the visit.
- [02-order-taking.md](02-order-taking.md) — order items feed spend metrics.
- [05-payment-tip-reconciliation.md](05-payment-tip-reconciliation.md) —
  closed visits generate the bill that backs spend metrics.

## Open questions

- What threshold of "covers per hour" is meaningful? (Need to mock with
  synthetic data first.)
- Server leaderboard: opt-in (some restaurants ban internal competition) or
  always-on?
- Hour-of-day granularity: by 30-min or 60-min buckets?

## Why skip gender in v1

- **GDPR risk**: gender is personal data; needs lawful basis, retention
  policy, opt-out, etc. Not worth the complexity for v1.
- **Data-entry friction**: waiters won't reliably capture it on a busy floor.
- **Limited insight** without longitudinal data anyway.
- Easy to add later if the owner actually wants it.