# Guest / Table Analytics

The user wants the waiter to capture per-visit:
- party size
- number of adults
- adult gender breakdown (M/F/other)
- number of children
- child gender breakdown (M/F/other)
- dwell time (open → close)
- spend per adult / per child

## What existing systems track

- **evan361425/flutter-pos-system** (488⭐, Flutter): has a "Customer"
  entity with `name`, `phone`, `gender` — closest fit for demographics.
- **TastyIgniter**: customer is a `Customer` table with `first_name`,
  `last_name`, `email`, `telephone`. No per-visit demographics.
- **URY** (Frappe/ERPNext): customers + sales history, no party-size or gender.
- **harismuneer/Restaurant-Management-System** (Java/Android): has basic
  customer management but no analytics dashboard.

## Standard restaurant metrics (industry)

None of these are standard in open-source POS; they are standard in commercial
tools (Toast, Square, TouchBistro) but the open-source world lags.

Metrics worth tracking:
- **Dwell time** = `bill.paid_at - order.opened_at` — tells us table turnover.
- **Spend per cover** = `bill.total / party_size`.
- **Spend per adult** = `bill.total / adults` (children typically eat less).
- **Average party size by hour-of-day** — staffing insights.
- **Demographic mix by day-of-week** — marketing/segmentation.

## Data model

```
Visit       (id, table_id, server_id, opened_at, closed_at, party_size,
             adults, adult_m, adult_f, adult_other, children, child_m, child_f)
Bill        (id, visit_id, ...)             -- 1 bill per visit, split if needed
VisitItem   (visit_id, menu_item_id, qty, unit_price, consumed_by_adult_or_child)
```

The `VisitItem.consumed_by_adult_or_child` lets us analyze kids' menu uptake.

## Privacy note

GDPR / data-protection laws in many countries restrict collecting gender unless
there's a legitimate reason. Make the gender fields **optional** and don't
store anything beyond what's needed for analytics. Document this in a privacy
notice in the app.

## Recommendation

- **v1**: capture only `party_size`, `adults`, `children`. Skip gender.
- **v2** (after user feedback): add gender if they want analytics on it.

This avoids both legal risk and data-entry friction on the floor.

See [../features/06-guest-demographics.md](../features/06-guest-demographics.md).