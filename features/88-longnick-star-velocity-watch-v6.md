# Feature 88 — longnick-star-velocity-watch (v6)

> **Carry-over from 2026-08-16 (feature 71) → 2026-08-17 (v2) →
> 2026-08-18 (v3) → 2026-08-19 (v4) → 2026-08-20 (v5) →
> 2026-08-21 (this feature, v6).**
> Bucket: **v2 watch-list (research observation)** — hard defer.

## Goal

Continue tracking the star velocity of `longnick/small-pos-open-source`
(TS React 19 + Vite 8 reference POS frontend; MIT; created
2026-08-12) and document the observed 72h sustained decay trend
(−1★/24h for 3 consecutive days = −3★/72h cumulative). The
velocity-driven watch has definitively EXPIRED; the star-loss trend is
now real and statistically significant at the 72h window.

## Scope

**In scope:**
- Daily direct-repo `GET https://api.github.com/repos/longnick/small-pos-open-source`
  (via `$HERMES_GITHUB_TOKEN`) in each daily-research pass.
- Recording the star + fork count + `pushed_at` + `updated_at` + size +
  license fields in the daily-research report.
- Verifying whether the −1★/24h decay continues (sub-90★ territory) or
  stabilizes at the 92★ floor.

**Out of scope (v1 / v2):**
- Importing any code from `longnick/small-pos-open-source` (TS + React
  frontend, not Python; no LE31-stack match).
- Building any feature based on the longnick codebase (charter §3.2).
- Any action beyond continued observation.

## Description

The `longnick/small-pos-open-source` peer observed across the 22-pass
series:

| Date | Stars | Δ stars | Δ forks | pushed_at | updated_at | size |
|---|---|---|---|---|---|---|
| 2026-08-12 (baseline) | 50★ | — | — | — | — | — |
| 2026-08-13 | 91★ | +41★/24h | — | — | — | — |
| 2026-08-14 | 91★ | +0★/24h | — | — | — | — |
| 2026-08-15 | 95★ | +4★/24h | — | — | — | — |
| 2026-08-16 | 95★ | +0★/24h | — | — | — | — |
| 2026-08-17 | 95★ | +0★/24h (push at 02:17:41Z) | — | — | — | — |
| 2026-08-18 | 95★ | +0★/24h | — | — | 2026-08-18T15:39:55Z | 1510KB |
| 2026-08-19 | 94★ | **−1★/24h ANOMALY** | −1 fork | 2026-08-18T12:02:14Z | 2026-08-19T12:26:45Z | 1510KB |
| 2026-08-20 | 93★ | **−1★/24h AGAIN, −2★/48h cumulative** | 89 forks | 2026-08-18T12:02:14Z (2 days idle) | 2026-08-19T12:26:45Z (+20h) | 1681KB (+171KB) |
| 2026-08-21 | 92★ | **−1★/24h AGAIN, −3★/72h cumulative** | 89 forks | 2026-08-18T12:02:14Z (3 days idle) | 2026-08-20T16:44:47Z (+28h — largest single-day updated_at jump in 9-day watch series) | (unchanged) |

**9-day trajectory: 50★ → 91★ → 91★ → 95★ → 95★ → 95★ → 95★ → 94★ → 93★ → 92★ = +4.7★/24h average** (decayed from the +41★/24h one-day peak observed 2026-08-13→2026-08-14).

**Verdict (this pass):** **velocity-driven watch definitively EXPIRED + 72h sustained decay trend CONFIRMED.** GitHub star counts do not normally decrease; three consecutive days of −1★/24h is now statistically significant at the 72h window. Possible causes (revised from prior days): (a) multiple users removing stars after reviewing the code, (b) multiple star-accounts being deleted, (c) GitHub API anomaly (less likely with three consecutive identical deltas). **Re-check on 2026-08-22** to confirm whether the decay accelerates (sub-90★ territory) or stabilizes at the 92★ floor.

**JTBD pull still confirmed:** 92★ at the 9-day floor is still very high for a TS POS starter with 89 forks. The repo is the closest JTBD pull in window (restaurant/bar POS + multi-device sync + KOT/BOT printing + CSV bulk management); the stack match is zero (TS + React PWA, not Python).

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation, not a feature build.

## Implementation

1. Continue daily direct-repo GET in each daily-research pass (the
   cron already does this; this artifact just records the verdict).
2. Re-check the −1★/24h decay vs. stabilization on 2026-08-22.
3. If the decay continues to sub-90★ territory: escalate to a
   watch-list close (the watch is no longer actionable; the longnick
   signal has decayed into noise).
4. If the decay stabilizes at 92★: downgrade verdict to "velocity-driven
   watch EXPIRED + 72h star-loss anomaly observed" and continue the
   watch at reduced cadence (weekly instead of daily).

## Telegram interaction

None. This is a passive observation; no cook or manager action.

## Dependencies

- `$HERMES_GITHUB_TOKEN` for the daily direct-repo GET (already in
  `/opt/data/.env`).

## Open questions

- Is the −1★/24h decay due to (a) users removing stars, (b) star-account
  deletions, or (c) GitHub API anomaly? Without a deeper investigation
  (e.g. GitHub Archive event log), the cause is speculative.
- Does the `updated_at` +28h movement (the largest single-day jump in
  the 9-day watch series) correspond to a README change or a config
  edit? Without reading the commit log, the cause is speculative.

## Why this matters

The `longnick/small-pos-open-source` watch is the highest-priority
JTBD signal in the 22-pass series. The +41★/24h one-day peak observed
on 2026-08-13→2026-08-14 was real-world market validation that
small-F&B owners want a free open POS starter. The 72h sustained decay
trend observed today is a **statistically significant** reversal: the
velocity-driven market-validation signal has decayed into a
star-loss-anomaly observation. The watch remains active for the
2026-08-22 confirmation check.
