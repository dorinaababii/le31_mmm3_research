# Feature 477 — Covers by hour: the chart binds 24 hour-of-day buckets positionally to ten labels, so every bar is rendered under the wrong hour

> **Pick A of Daily Research 2026-11-14.** **First-party, execution-proven.** The defect is in LE31's own shipped `index.html`.
>
> **Executed under Node v22 (2026-11-14):**
>
> ```text
> hourCounts = [0,0,1,2,3,5,4,2,1,0,...]   # index 0..23 = hour of day
> hours     = ['12','13','14','15','18','19','20','21','22','23']
> loop      = hours.forEach((h, i) => height = hourCounts[i] / max)
> ```
>
> The true peak is bucket **5** (value **5**), but bucket 5 is rendered under the label **19h**. The ten displayed bars sum to **18** covers while the adjacent KPI card hard-codes **38**.
>
> **Ambiguity disclosed after independent review:** the fixture does not declare whether the ten values are hour-of-day buckets or a compact service-hours series. The defect that is proven without interpretation is that the renderer reads `hourCounts[i]` positionally, so **the displayed label is not bound to the value it displays**. The proposed implementation must make that binding explicit; it must not merely re-key the existing values under the current labels, because that preserves the same displayed peak and total.

## Goal

Make the shipped reports view label every covers-by-hour bar with the hour-of-day bucket it actually represents, so the owner's peak-hour reading is true.

**The single sentence this feature exists to make true:** *the label under each covers-by-hour bar is the hour-of-day index of the value that bar displays.*

## Scope

**In scope (v1):**

- One binding in `index.html` that pairs each displayed hour label with `hourCounts[hour]`, not `hourCounts[displayIndex]`.
- One fixture correction so the reports view's hourly counts and the covers KPI describe the same day.
- One deterministic test that catches an off-by-label mapping.

**Out of scope (v1):**

- Live report data, persistence, a reports API, or authentication.
- The other reports KPIs, top-items rendering, and chart styling.
- Any feature that edits the waiter UI's money arithmetic, seat form, fixture statuses, floor grid, order state, or menu availability.

## Out of scope

The exclusions listed under **Scope** are binding: live report data, a reports API, authentication, other reports KPIs, chart styling, and the waiter-screen regions owned by features 465, 466, 467, 474, 475 and 476.

## Description

The reports view contains a covers-by-hour chart and a KPI card. The chart's data and labels have different shapes:

- `hourCounts` has 24 entries, one for each hour of day.
- `hours` has 10 entries: `12,13,14,15,18,19,20,21,22,23`.
- The renderer iterates `hours` and reads `hourCounts[i]`, where `i` is the display position.

The result is a chart whose labels are not the keys of its values. The value at index 5 appears under `19h`. The owner sees a different peak hour than the fixture encodes.

This is a truthfulness defect, not a preference. The report view is a P1 operator surface in the charter and the shipped screen is currently the only reports surface.

## Data model

No schema change, no model, no API. This is a fixture-and-binding correction in `index.html`.

The corrected fixture should use one explicit representation, for example (the values below are intentionally illustrative, not the shipped values):

```javascript
const coversByHour = {
  12: 0, 13: 0, 14: 1, 15: 2, 18: 3, 19: 5, 20: 4, 21: 2, 22: 1, 23: 0,
};
const hours = Object.keys(coversByHour);
const values = hours.map((h) => coversByHour[h]);
```

The invariant is `values[i] === coversByHour[hours[i]]` by construction.

## Implementation steps

1. Replace the positional arrays with one hour-keyed object or with two arrays whose positions are deliberately identical only because they are generated from the same keys. **The implementer must first decide and record whether the intended series is hour-of-day or compact service-hours.** If hour-of-day, the fixture must be populated at the intended hours and must not render all-zero bars. If compact service-hours, the labels and values must be generated from one service-hour list. In both cases, the invariant is `displayed_value === fixture_value_for_displayed_label`.
2. Render `height` from the value paired with the label, not from the display index.
3. Make the covers KPI derive from the same fixture or correct its hard-coded value so the screen is internally consistent.
4. Add a test or deterministic browser probe that asserts the displayed label/value pairs and the covers total.
5. Exercise the reports tab in the shipped page and read back the rendered labels and bars. **The implementer must establish the test harness if the repository does not already contain one; this contract does not assume a package.json, pytest configuration, or test directory exists.**

## Telegram interaction if any

None. This feature changes the owner-facing reports view only.

## Dependencies

- `index.html` — reports view (`view-reports`), `renderReports()`, KPI cards, and mock data.
- Feature 06 owns the product goal of covers-by-hour reporting; this feature corrects the shipped rendering of that goal.
- The reports view is a file-level collision zone. The regions touched here are disjoint from the waiter-screen corrections filed as features 465, 466, 467, 474, 475 and 476, but a rebase is required if those contracts land first.

## Open questions

1. Should the reports fixture cover every hour 0–23, or only service hours? The current contract uses an explicit key per displayed hour, which supports either; the owner decides the product scope.
2. Should the covers KPI derive from the hourly fixture or remain an independent value? The contract requires internal consistency but does not decide the product's source of truth.
3. Is a separate reports fixture file worth introducing? The default is no — keep the correction in the existing file.

## Why this matters

The owner uses the reports view to decide when to staff the floor. A chart that says the peak was at 19h when the fixture says 05h is worse than no chart: it invites a scheduling decision based on a false hour. The defect is small, local, and observable now.

## Adjacent evidence

- The same reports fixture hard-codes other KPI values (sales, tips, dwell) and top-item counts. They are adjacent inconsistencies, not part of this slice.
- The ten labels and the twenty-four buckets can also be read as a compact service-hours series with a positional lookup. Under that reading the chart is already internally consistent; the proven defect is the **absence of an explicit binding**, not a wrong numeric value. This ambiguity is recorded rather than guessed.
- The same file is under active correction by several filed features; their regions are disjoint.

## Verification protocol

1. Render the reports view under Node/jsdom or a real browser-free DOM harness.
2. Assert each rendered label has exactly one bar and that its height is derived from the fixture value for that label.
3. Assert the peak bar's label is the hour whose fixture value is maximal.
4. Assert the sum of displayed values equals the covers KPI shown on the same view.
5. `git diff -- index.html` must show only the reports fixture/binding region.

## Rollback path

Revert the `index.html` change. No data, schema, migration, or user state is affected.
