# Feature 71 — Longnick Star Velocity Watch v4

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-19 (Pick B, watch-list,
> defer — watch definitively EXPIRED + −1★/24h anomaly under
> confirmation) · **Bucket**: v2 utility (watch-list)
> **One-line**: A research-only watch-list artifact that records the
> `longnick/small-pos-open-source` GitHub repo's star-velocity
> trajectory across the 20-pass daily-research series. **The watch
> has definitively EXPIRED** as of 2026-08-17 (CONFIRMED stagnation
> at 95★ for 48h) and was confirmed again on 2026-08-18 (95★ for 72h).
> **This pass observed −1★/24h anomaly (95★ → 94★)** with a NEW push
> in past 24h (last pushed 2026-08-18T12:02:14Z, NEW vs yesterday's
> 2026-08-17T02:17:41Z). **GitHub star counts do not normally
> decrease**; possible causes: (a) single user removing a star, (b)
> star-account deletion, (c) GitHub API anomaly. **Re-check on
> 2026-08-20 to confirm.** The revised target window is 95★ ± 5
> sustained over the next 7 days (band: 90★ ≤ star count ≤ 100★;
> today's 94★ is within this band but the −1★ direction warrants
> confirmation). No code; no new LE31 implementation.

## Goal

`longnick/small-pos-open-source` (TypeScript, MIT, 1510KB, **94★** —
was 95★ at 2026-08-15 + 2026-08-16 + 2026-08-17 + 2026-08-18; **−1★
in last 24h**, 90 forks — was 91 forks at 2026-08-18; minor
fluctuation, Vite/React/TS reference frontend for a small café POS)
emerged as the **highest-star-velocity in-window GitHub peer** across
the 20-pass daily-research series:

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

The 7-day trajectory is now **91★ → 95★ → 95★ → 95★ → 95★ → 95★ →
94★ = +0.43★/24h average** (decayed from the +41★/24h one-day peak),
with the **−1★ anomaly in the last 24h**.

## Scope

**In scope (v2 utility, S effort, research-only, no code — watch-list
artifact):**

- Record the daily star-velocity observation in this file.
- Update the active feature pipeline row in `INDEX.md` with the new
  star count and the −1★/24h anomaly note.
- Append a row to the longnick watch-list section of this file.
- Re-check on 2026-08-20 to confirm whether the −1★ stabilizes
  (returns to 95★), sustains at 94★, or drops further (mass un-star
  event).

**Out of scope (rejected):**

- LE31 implementation work — no code, no schema change, no contract.
  This is a research observation only.
- Watching a different repo — the watch-list is specifically about
  `longnick/small-pos-open-source`. Other repos are covered by their
  own feature files (e.g., `helloman3/foodieshub` watch-list is
  feature 81).
- Importing `longnick/small-pos-open-source` code into LE31 — stack
  match zero (TS + React PWA, not Python; FastAPI ✗, SQLModel ✗,
  aiogram ✗, Postgres ✗). Charter §3.2 + §3.3 ban non-Python
  dependencies in v1.

## Description

**Evidence precondition:** observed (verified in-window across the
20-pass series via direct GitHub repo API GETs;
`api.github.com/repos/longnick/small-pos-open-source`).

**Confidence:** **high** for JTBD pull ("small café POS" — exactly
the LE31 user surface from features 02/03/05), **zero** for stack
match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
`longnick/small-pos-open-source` is TypeScript + React 19 + Vite 8).

**Cross-validation anchors:**

- `satisfecho/pos` (FastAPI+SQLModel+Postgres+KDS+WS, 28★, 9 forks,
  pushed 2026-08-13T14:04:11Z, **AGPL-3.0 license — NEW finding on
  2026-08-19**): strongest in-window **stack match** but AGPL
  incompatible with LE31 v1 charter §3.2. Useful as pattern reference
  only.
- `helloman3/foodieshub` (TypeScript React PWA, 4★, 0 forks, pushed
  2026-08-17T07:03:23Z): strongest **direct JTBD pull** in the
  same recent window; stack match zero; covered by feature 81
  (foodieshub-ts-pos-watch v3).
- 20-pass observation (2026-08-03..2026-08-19) — the
  longnick trajectory is **definitive**: 6 days of 95★ plateau
  (2026-08-14 → 2026-08-18) + 1 day of −1★ anomaly (2026-08-19).
- **Velocity-driven watch has definitively EXPIRED.** JTBD pull
  remains confirmed (94★ at the 7-day floor is very high for a TS
  POS starter with 90 forks); the velocity-driven
  market-validation data point is no longer accumulating; the repo
  is in steady-state slow-growth phase.

**−1★/24h anomaly analysis:**

GitHub star counts do not normally decrease. Possible causes:

- **(a) Single user removing a star** — most likely cause. A user
  may have discovered the repo, starred it during the +41★/24h peak
  window, then later (after reviewing the code and deciding it
  doesn't meet their use case) removed the star. The decayed
  velocity + stable JTBD pull is consistent with this hypothesis.
- **(b) Star-account deletion** — if a GitHub user account is
  deleted, all stars from that account are removed along with it.
  This is rare but possible.
- **(c) GitHub API anomaly** — the public API occasionally returns
  stale or cached counts; a 30-minute retry might return 95★ again.
  Possible but less likely.

**Action:** **Re-check on 2026-08-20 to confirm**. If the count
returns to 95★, hypothesis (a) or (c) is correct (single
star-removal or API staleness); if it stays at 94★ or drops
further, hypothesis (b) (mass un-star) gains weight.

**Decision: defer (watch-list, no code change).** The watch is
research-only; no LE31 feature contract to build today.

## Data model

No data model changes. The slice is research observation only.

## Implementation steps

1. **Re-check on 2026-08-20** via the daily-research cron — fetch
   `api.github.com/repos/longnick/small-pos-open-source` and record
   the new star count + push time.
2. **Record the finding** in the 2026-08-20 daily research report
   (continues the trajectory log: 50★ → 91★ → 91★ → 95★ → 95★ →
   95★ → 95★ → 95★ → 94★ → [2026-08-20 read]).
3. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-19, pick `longnick-star-velocity-watch`
   (v4), feature path `features/71-longnick-star-velocity-watch.md`
   (updated v4), Linear sub-issue ID (TBD), status "Backlog
   (watch-list, defer — watch definitively EXPIRED + −1★/24h anomaly
   under confirmation)".
4. **No code change** — this is a research-only slice.

## Telegram interaction

None. The slice is research observation only; no user-facing
Telegram surface changes.

## Dependencies

- Direct GitHub repo API access
  (`api.github.com/repos/longnick/small-pos-open-source` via the
  `HERMES_GITHUB_TOKEN` PAT). Must be reachable from the
  daily-research VPS.
- The daily-research cron (`le31-daily-research` skill).

No new pip dependencies. No new system dependencies. No new
external services.

## Open questions

- **Q1: Will the −1★/24h observation revert on 2026-08-20?** If the
  count returns to 95★, hypothesis (a) or (c) is correct. If it
  stays at 94★, hypothesis (b) gains weight. Re-check on the next
  pass.
- **Q2: Is the longnick watch now permanently expired, or is there
  a meaningful plateau signal?** The 7-day floor at 94★ is very
  high for a TS POS starter. The plateau is the new steady-state;
  the watch remains active with the 95★ ± 5 target band.
- **Q3: Does the team want to read the longnick README in full to
  assess the underlying patterns?** Recommended for the 2026-08-20
  pass; useful as a v2 owner-pains reference for JS POS
  architectures (not a v1 import candidate).

## Why this matters

The `longnick-star-velocity` watch remains the **strongest in-window
JTBD pull** for the LE31 surface (small café POS), but the velocity-
driven signal is definitively gone. The 6-day 95★ plateau confirmed
stagnation on 2026-08-14 + 2026-08-15 + 2026-08-16 + 2026-08-17 +
2026-08-18; today's −1★/24h anomaly with a NEW push in past 24h is
the most unexpected observation in the 20-pass series.

The watch's continued existence reflects the fact that LE31 has no
in-house >90★ OSS counterpart in window — the longnick project is a
real-world market-validation data point that small-F&B owners want a
free open POS starter. **JTBD pull is confirmed and stable at the
94★ floor**; velocity-driven urgency is definitively gone.

**Risk of NOT continuing the watch**: lost visibility into a real
v2 scope question (could LE31 ever vendor a TypeScript reference
frontend?). Low-severity risk; the watch is research-only.

**Risk of continuing the watch**: daily-research resources spent on
a watch that has plateaued. Low cost (one direct repo API GET per
pass).

**Net: continue the watch at 95★ ± 5 over the next 7 days; re-
evaluate on 2026-08-20 after the −1★/24h observation stabilizes.**

## Status: watch-list defer (no code)

This file is a **watch-list artifact (defer)**. The slice is
research-only; no LE31 feature contract to build today. The
research-side subagent (Pass 20, 2026-08-19) records the
recommendation as **unchanged** (watch continues; −1★/24h anomaly
under confirmation; target band 95★ ± 5).
