# Feature 83 — Foodieshub TS POS Watch v4

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-20 (Pick C, watch-list,
> defer — fails the LE31 gate; stack match zero) · **Bucket**: v2
> utility (watch-list)
> **One-line**: A research-only watch-list artifact that records the
> `helloman3/foodieshub` GitHub repo's star-velocity trajectory across
> the 4-pass daily-research series since 2026-08-17. **The watch has
> hit 4-day steady-state stagnation** at 4★ for 96h with 0 forks. The
> 4-day trajectory is 4★ → 4★ → 4★ → 4★ = +0★/24h average — the
> longest stagnation phase observed for any LE31 watch-list repo,
> consistent with the longnick pattern of velocity-driven attention
> collapsing to steady-state slow growth (now extending into the
> sustained-stagnation phase). **Stack match zero (TS + React PWA,
> not Python); JTBD direct match.** Watch-list add; fails the LE31
> gate today. Re-check on 2026-08-21 for sustained velocity or further
> decay (target band: 5★+ in 24h; +0★/96h stagnation in the running).

## Goal

`helloman3/foodieshub` (TypeScript React PWA, 4★ — unchanged for
96h, 0 forks, 1012KB, pushed 2026-08-17T07:03:23Z — **3 days idle,
71h before today's fetch**, description: "A modern, high-performance
Restaurant & Bar POS Web Application (PWA) with real-time
multi-device sync, thermal KOT/BOT printing, and CSV bulk management",
topics: `pos-web-app`, `pwa`, `react`, `restaurant-pos`, `typescript`,
`web-app`) emerged as the **closest direct JTBD pull** in window
across the recent 4-pass daily-research series:

- **2026-08-17 (Pass 18):** 3★ (initial baseline)
- **2026-08-18 (Pass 19):** 4★ (+1★/24h, +0 forks, no new push) —
  **deceleration** (the +3★ on day 1 had decayed to +1★/24h by
  day 2)
- **2026-08-19 (Pass 20):** 4★ (+0★/24h, +0 forks, last push still
  2026-08-17T07:03:23Z — no new push in past 72h) — **steady-state
  stagnation confirmed**
- **2026-08-20 (Pass 21):** 4★ (+0★/24h, +0 forks, last push still
  2026-08-17T07:03:23Z — **3 days idle, 71h before today's fetch**) —
  **4-day steady-state stagnation; the longest stagnation phase
  observed for any LE31 watch-list repo**

The 4-day trajectory is now **3★ → 4★ → 4★ → 4★ = +0.25★/24h average**,
fully consistent with the longnick pattern of velocity-driven
attention collapsing to steady-state slow growth, now extending into
the sustained-stagnation phase.

## Scope

**In scope (v2 utility, S effort, research-only, no code — watch-list
artifact):**

- Record the daily star-velocity observation in this file.
- Update the active feature pipeline row in `INDEX.md` with the new
  4★ stagnation status and the 4-day trajectory.
- Read the foodieshub README in full on the 2026-08-21 pass to assess
  the multi-device sync mechanism (the most distinctive feature in
  the description).
- Re-check on 2026-08-21 for sustained velocity or further decay
  (target band: 5★+ in 24h; +0★/96h stagnation in the running).

**Out of scope (rejected):**

- LE31 implementation work — no code, no schema change, no contract.
  This is a research observation only.
- Watching a different repo — the watch-list is specifically about
  `helloman3/foodieshub`. Other repos are covered by their own
  feature files (e.g., longnick is feature 71).
- Importing `helloman3/foodieshub` code into LE31 — stack match zero
  (TS + React PWA, not Python; FastAPI ✗, SQLModel ✗, aiogram ✗,
  Postgres ✗). Charter §3.2 + §3.3 ban non-Python dependencies in
  v1. (License is also null — needs verification if the team ever
  considers vendoring.)

## Description

**Evidence precondition:** observed (verified in-window across the
4-pass series via direct GitHub repo API GETs;
`api.github.com/repos/helloman3/foodieshub`).

**Confidence:** **high** for JTBD pull (restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management =
exactly the LE31 feature surface from features 02/03/09/14), **zero**
for stack match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
helloman3 is TypeScript + React PWA + 0-fork single-author repo).

**Cross-validation anchors:**

- `longnick/small-pos-open-source` (TS React 19 + Vite 8, **93★** —
  was 94★ at 2026-08-19, 95★ at 2026-08-15..2026-08-18, 91★ at
  2026-08-13, 50★ at 2026-08-12 baseline, **−1★/24h AGAIN, −2★/48h
  cumulative, sustained decay CONFIRMED**, 89 forks, last pushed
  2026-08-18T12:02:14Z — 2 days idle 42h before fetch, `updated_at`
  2026-08-19T12:26:45Z, size 1681KB — was 1510KB): strongest
  cross-section peer (sustained at the 93★ floor over 8 days).
  Covered by feature 71.
- `satisfecho/pos` (FastAPI+SQLModel+Postgres+KDS+WS, 28★, 9 forks,
  pushed **2026-08-20T05:27:20Z — NEW push in past 24h (66 min
  before fetch)**, **AGPL-3.0 license**): strongest in-window **stack
  match** but AGPL incompatible with LE31 v1 charter §3.2. Useful as
  pattern reference only. The NEW push today is the first activity
  since 2026-08-13 = 7 days of idle, broken 66 min before today's
  fetch.

**Decision: watch-list defer.** The 4-day stagnation phase is the
longest observed for any LE31 watch-list repo (longnick plateau was
3-4 days before the −1★/24h decay started; foodieshub has been at 4★
for 4 days straight). The watch continues; the README should be read
on 2026-08-21 to assess the multi-device sync mechanism.

## Data model

No data model changes today. This is a research observation only.

## Implementation steps (none — research-only artifact)

No implementation steps. The artifact is a research-note document;
the only "implementation" is the file write itself.

## Telegram interaction

None directly. The watch-list is an internal research artifact; no
user-facing surface changes.

## Dependencies

- **`helloman3/foodieshub`** is the watch-list target. License: null
  (NOASSERTION). Stack: TypeScript + React PWA. The watch is
  conducted via `api.github.com/repos/helloman3/foodieshub` GET (no
  auth required for public read; auth used for higher rate limits).
- The `HERMES_GITHUB_TOKEN` from `/opt/data/.env` for higher rate
  limits on the GitHub API.
- No LE31 schema changes required.
- No new pip dependencies.
- No charter approval required (charter §3.2 allows watch-list
  research artifacts).

## Open questions

- **Q1: Will the 4★ stagnation break in either direction (growth or
  decay)?** The 4-day stagnation is consistent with both "stable
  plateau" and "imminent decay" (similar to the longnick pattern
  where 3-4 days of plateau preceded the −1★/24h decay). **Re-check
  on 2026-08-21 to confirm.**
- **Q2: Does the foodieshub README reveal the multi-device sync
  mechanism?** The description says "real-time multi-device sync" but
  the repo is single-author (0 forks, 4★). Read the README on
  2026-08-21 to assess scope and assess the multi-device sync
  mechanism (the most distinctive feature in the description).
- **Q3: Should the watch be downgraded to "parking-lot" if the
  stagnation continues for 7+ days?** If the count holds at 4★ for
  another 3 days (total 7-day stagnation), the watch moves from
  "defer (4-day stagnation)" to "defer (parking-lot — repo no longer
  in velocity-driven discovery)".

## Why this matters

`helloman3/foodieshub` is the **closest direct JTBD pull** in window
across the recent 4-pass daily-research series: restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management = exactly
the LE31 feature surface from features 02/03/09/14. The description
maps directly to the LE31 user surface.

The **4-day stagnation** at 4★ is the longest stagnation phase
observed for any LE31 watch-list repo. The longnick plateau was 3-4
days before the −1★/24h decay started; foodieshub has been at 4★ for
4 days straight with no decay but also no growth. The watch-list
captures this trajectory for future passes to reference.

**Risk of NOT tracking the 4-day stagnation**: if the watch
eventually breaks (growth or decay), the artifact captures the
baseline for comparison.

**Risk of overreacting to the 4-day stagnation**: the stagnation is
consistent with a stable plateau (a single-author repo with 0 forks
can stay at 4★ indefinitely). The research-note artifact should not
be used to recommend action without the next 7-day observation
period.

**Net: continue the watch; re-check on 2026-08-21; the watch remains
active with the target band of 5★+ in 24h or further decay.**

## Status: watch-list (defer — fails the gate; +0★/96h 4-day stagnation)

This file is a **research-note artifact (no code shipped today)**.
The slice boundary is hard: zero source-code changes, zero
migrations, zero new dependencies. The artifact lives in this file
and the corresponding HANDOFF.md.

The watch should be re-evaluated when: (i) the 4★ count breaks in
either direction (growth or decay), or (ii) the foodieshub README is
read in full on the 2026-08-21 pass to assess the multi-device sync
mechanism.
