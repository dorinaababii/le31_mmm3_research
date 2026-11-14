# Slice contract — `le31-covers-by-hour-chart-labels-are-positional-not-hour-of-day`

## Active feature path

`features/477-le31-covers-by-hour-chart-labels-are-positional-not-hour-of-day-first-party-the-twenty-four-slot-hour-array-is-bound-positionally-to-ten-labels-so-every-bar-is-rendered-under-the-wrong-hour-v1-hourly-covers-label-binding.md`

## Seven-check gate verdict

**BUILD.** Evidence class: **observed**, execution-proven under Node v22; confidence high for the defect and medium for demand frequency.

1. **JTBD:** When the owner opens reports, they want to know when service peaked, but every hourly bar is labeled positionally, so the owner sees the wrong peak hour.
2. **Viability:** pass; one local binding and one test, no administration.
3. **Practicability:** pass; local frontend fixture, no stack or permission change.
4. **Conflict:** none; corrects a shipped mock-up only.
5. **Outcome/scope:** v1 P1 reports surface; scope limited to the hourly chart and its fixture.
6. **Cost/value:** small cost; prevents a false staffing decision.
7. **Circuit breaker:** stop if reports are replaced; revert one file; no data risk.

## Files to touch

- `index.html` — reports view fixture and `renderReports()` only.
- A focused test/probe file for the reports binding if the repository's test structure supports it.

Do not edit the waiter money arithmetic, seat form, fixture statuses, floor grid, per-table order state, sold-out rendering, or quantity-phase logic owned by features 465, 466, 467, 474, 475 and 476.

## Verification protocol reference

Follow the feature contract's `## Verification protocol`:

1. Render the reports view in a browser-free DOM harness. **The implementer must establish the harness if the repository does not already contain one.** The harness must expose the label and value actually paired for each rendered bar.
2. Assert every bar's height comes from the fixture value for the displayed hour.
3. Assert the peak bar's label is the hour whose fixture value is maximal.
4. Assert the displayed hourly total agrees with the covers KPI on the same screen.
5. Inspect `git diff -- index.html` and confirm only the reports region changed.

The regression test must fail against the current positional binding before the fix is applied. **The implementer must first decide and record whether the fixture is hour-of-day or compact service-hours; the fix must not merely re-key the current values under the current labels.**

## Rollback path

Revert the `index.html` fixture/binding change. No schema, data, migration, or persistent state is affected.

## Mandatory LE31 skill list

- `le31-conventions`
- `le31-v1-feature-pattern`
- `development`
- `speckit-specify`
- `speckit-plan`
- `speckit-tasks`
- `speckit-implement`
- `verify-before-fixing`
- `pre-merge-review`

## Linear reference

Created as a draft Feature sub-issue under the 2026-11-14 research issue. If Linear writes remain blocked, use the fallback payload in `/opt/data/le31-daily-research-2026-11-14.linear-fallback.json` and record `linear: blocked`; do not claim an issue ID that was not returned by Linear.
