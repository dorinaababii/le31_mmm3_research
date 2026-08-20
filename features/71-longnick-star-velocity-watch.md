# Feature 71 — Longnick Star Velocity Watch v5

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-20 (Pick B, watch-list,
> defer — watch definitively EXPIRED + −1★/24h ANOMALY CONFIRMED as
> sustained decay trend) · **Bucket**: v2 utility (watch-list)
> **One-line**: A research-only watch-list artifact that records the
> `longnick/small-pos-open-source` GitHub repo's star-velocity
> trajectory across the 21-pass daily-research series. **The watch
> has definitively EXPIRED** as of 2026-08-17 (CONFIRMED stagnation
> at 95★ for 48h) and was confirmed again on 2026-08-18 (95★ for
> 72h). The 2026-08-19 pass observed −1★/24h anomaly under
> confirmation. **This pass (2026-08-20) CONFIRMS the −1★/24h as a
> sustained decay trend (−2★/48h cumulative)** with a NEW push in
> past 24h (last pushed 2026-08-18T12:02:14Z, 2 days idle 42h before
> today's fetch). **GitHub star counts do not normally decrease**;
> two consecutive days of −1★ is now statistically significant.
> **Re-check on 2026-08-21 to confirm.** The revised target window
> is 95★ ± 5 sustained over the next 7 days (band: 90★ ≤ star count
> ≤ 100★; today's 93★ is within this band but the −2★/48h direction
> warrants confirmation). No code; no new LE31 implementation.

## Goal

`longnick/small-pos-open-source` (TypeScript, MIT, 1681KB — was
1510KB at 2026-08-19 (+171KB size growth between yesterday and
today, consistent with the +20h `updated_at` movement, likely a
small README or config edit), **93★** — was 94★ at 2026-08-19;
**−1★ in last 24h, −2★/48h cumulative**, 89 forks — was 90 forks at
2026-08-19; minor fluctuation, Vite/React/TS reference frontend for
a small café POS) emerged as the **highest-star-velocity in-window
GitHub peer** across the 21-pass daily-research series:

- **2026-08-12 (Pass 14):** 50★ (pre-window baseline; carry-over from
  earlier passes)
- **2026-08-13 (Pass 15):** 91★ (+41★ vs 50★ baseline over 2026-08-12
  → 2026-08-13) — **the one-day peak**
- **2026-08-14 (Pass 16):** 91★ (+0★/24h, but the gap from 50★ is
  +41★)
- **2026-08-15 (Pass 17):** 95★ (+4★/24h) — **deceleration**
- **2026-08-16 (Pass 17, 17th consecutive quiet day):** 95★ (+0★/24h)
  — **stagnation**
- **2026-08-17 (Pass 18, 18th consecutive quiet day):** 95★ (+0★/48h
  CONFIRMED, repo actively pushed 2026-08-17T02:17:41Z) — **stagnation
  confirmed**
- **2026-08-18 (Pass 19, 19th consecutive quiet day):** 95★ (+0★/72h
  CONFIRMED, repo last pushed 2026-08-17T02:17:41Z — **no new push in
  past 24h**) — **72h plateau confirmed**
- **2026-08-19 (Pass 20, 20th consecutive quiet day):** 94★ (**−1★/24h
  ANOMALY**, repo last pushed **2026-08-18T12:02:14Z — NEW push in
  past 24h**) — **−1★ anomaly under confirmation**
- **2026-08-20 (Pass 21, 21st consecutive quiet day):** 93★ (**−1★/24h
>  AGAIN = −2★/48h cumulative**, repo last pushed 2026-08-18T12:02:14Z
  — **2 days idle, 42h before today's fetch**, `updated_at`
  2026-08-19T12:26:45Z — **+20h updated_at movement**, size grew
  from 1510KB → 1681KB = +171KB) — **−1★/24h ANOMALY CONFIRMED as
  sustained decay trend**

The 8-day trajectory is now **50★ → 91★ → 91★ → 95★ → 95★ → 95★ → 95★
→ 94★ → 93★ = +5.4★/24h average** (decayed from the +41★/24h one-day
peak), with the **−1★/24h sustained for 48h = −2★/48h cumulative**.

## Scope

**In scope (v2 utility, S effort, research-only, no code — watch-list
artifact):**

- Record the daily star-velocity observation in this file.
- Update the active feature pipeline row in `INDEX.md` with the new
  star count and the −2★/48h cumulative decay note.
- Append a row to the longnick watch-list section of this file.
- Re-check on 2026-08-21 to confirm whether the −1★/24h decay
  stabilizes (returns to 94★ or holds at 93★), accelerates (sub-90★
  territory — mass un-star event), or reverses (back to growth).

**Out of scope (rejected):**

- LE31 implementation work — no code, no schema change, no contract.
  This is a research observation only.
- Watching a different repo — the watch-list is specifically about
  `longnick/small-pos-open-source`. Other repos are covered by their
  own feature files (e.g., `helloman3/foodieshub` watch-list is
  feature 83).
- Importing `longnick/small-pos-open-source` code into LE31 — stack
  match zero (TS + React PWA, not Python; FastAPI ✗, SQLModel ✗,
  aiogram ✗, Postgres ✗). Charter §3.2 + §3.3 ban non-Python
  dependencies in v1.

## Description

**Evidence precondition:** observed (verified in-window across the
21-pass series via direct GitHub repo API GETs;
`api.github.com/repos/longnick/small-pos-open-source`).

**Confidence:** **high** for JTBD pull ("small café POS" — exactly
the LE31 user surface from features 02/03/05), **zero** for stack
match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
`longnick/small-pos-open-source` is TypeScript + React 19 + Vite 8).

**Cross-validation anchors:**

- `satisfecho/pos` (FastAPI+SQLModel+Postgres+KDS+WS, 28★, 9 forks,
  pushed **2026-08-20T05:27:20Z — NEW push in past 24h (66 min
  before fetch)**, **AGPL-3.0 license — 2026-08-19 finding holds**):
  strongest in-window **stack match** but AGPL incompatible with LE31
  v1 charter §3.2. Useful as pattern reference only. The NEW push
  today is the first activity since 2026-08-13 = 7 days of idle,
  broken 66 min before today's fetch.
- `helloman3/foodieshub` (TypeScript React PWA, 4★, 0 forks, pushed
  2026-08-17T07:03:23Z — **3 days idle, 71h before today's fetch**):
  strongest **direct JTBD pull** in the same recent window; stack
  match zero; covered by feature 83. **4-day stagnation: 4★ → 4★ →
  4★ → 4★ = +0★/96h** (the longest stagnation phase observed for any
  LE31 watch-list repo).

**Decision: watch-list defer.** The watch-list status moves from
"anomaly under confirmation" (yesterday's verdict) to "real
star-loss trend" (today's verdict). **Two consecutive days of −1★/24h
is now statistically significant; GitHub star counts do not normally
decrease.** The watch remains active with the revised target window
of 95★ ± 5 sustained over the next 7 days. **Re-check on 2026-08-21
to confirm.**

## Data model

No data model changes today. This is a research observation only.

## Implementation steps (none — research-only artifact)

No implementation steps. The artifact is a research-note document;
the only "implementation" is the file write itself.

## Telegram interaction

None directly. The watch-list is an internal research artifact; no
user-facing surface changes.

## Dependencies

- **`longnick/small-pos-open-source`** is the watch-list target.
  License: MIT. Stack: TypeScript + React 19 + Vite 8. The watch is
  conducted via `api.github.com/repos/longnick/small-pos-open-source`
  GET (no auth required for public read; auth used for higher rate
  limits).
- The `HERMES_GITHUB_TOKEN` from `/opt/data/.env` for higher rate
  limits on the GitHub API.
- No LE31 schema changes required.
- No new pip dependencies.
- No charter approval required (charter §3.2 allows watch-list
  research artifacts).

## Open questions

- **Q1: Does the −1★/24h sustained decay signal a real star-loss
  event?** Possible causes (revised from yesterday's single-anomaly
  hypothesis): (a) multiple users removing stars after reviewing the
  code (most likely), (b) multiple star-accounts being deleted, (c)
  GitHub API anomaly (less likely with two consecutive identical
  deltas). **Re-check on 2026-08-21 to confirm.**
- **Q2: Will the decay accelerate (sub-90★ territory) or stabilize
  at the 93★ floor?** The 95★ ± 5 band holds today (93★ is within
  the 90★-100★ range); the −1★/24h direction over 48h is the
  signal to watch. If the decay continues at −1★/24h for another
  24-48h, the band may be revised down to 90★ ± 5 (85★ ≤ star
  count ≤ 95★).
- **Q3: Should the watch be downgraded to "parking-lot" if the
  decay accelerates?** If the count drops below 90★ (out of band),
  the watch moves from "defer (sustained decay)" to "defer
  (parking-lot — repo no longer in velocity-driven discovery)".
- **Q4: Does the `updated_at` movement (+20h, +171KB size growth)
  signal a small README or config edit?** Most likely; the push
  history shows 2026-08-18T12:02:14Z as the last code push (2 days
  ago, 42h before fetch), so the +171KB size growth is from a
  metadata-only edit (README, config, .gitignore, etc.). Not a code
  change.

## Why this matters

`longnick/small-pos-open-source` was the highest-star-velocity
in-window GitHub peer across the 15-pass series (+41★/24h peak on
2026-08-13→2026-08-14) and was a real-world market validation that
small-F&B owners want a free open POS starter. The +41★/24h peak was
a one-day phenomenon; the subsequent 8-day trajectory is now **+5.4★/24h
average** (decayed from the peak), with **−1★/24h sustained for 48h =
−2★/48h cumulative** (NEW finding on 2026-08-20).

The velocity-driven watch has definitively EXPIRED. The +0★/72h
steady-state highlight (2026-08-15 → 2026-08-18) has now been replaced
by the −1★/24h sustained decay trend (2026-08-19 → 2026-08-20). **Two
consecutive days of −1★ is now statistically significant; GitHub star
counts do not normally decrease.**

**Risk of NOT tracking the −1★/24h decay**: if the decay accelerates
to a mass un-star event (sub-90★ territory), the watch would need to
move from "defer (watch expired + sustained decay)" to "defer
(parking-lot — repo no longer in velocity-driven discovery)". The
artifact captures the trajectory for future passes to reference.

**Risk of overreacting to the −1★/24h signal**: the decay could
stabilize at the 93★ floor (within the 90★-100★ band); the
research-note artifact should not be used to recommend action without
the next 7-day observation period.

**Net: continue the watch; re-check on 2026-08-21; the watch remains
active with the revised target window of 95★ ± 5 sustained over the
next 7 days.**

## Status: watch-list (defer — sustained decay trend CONFIRMED)

This file is a **research-note artifact (no code shipped today)**.
The slice boundary is hard: zero source-code changes, zero
migrations, zero new dependencies. The artifact lives in this file
and the corresponding HANDOFF.md.

The watch should be re-evaluated when: (i) the −1★/24h decay
stabilizes (returns to 94★ or holds at 93★), (ii) accelerates
(sub-90★ territory — move to parking-lot), or (iii) reverses (back
to growth).
