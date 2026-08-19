# Feature 79 — FoodiesHub TypeScript POS Watch v2

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-18 (Pick C, watch-list,
> defer — fails the gate; +1★/24h trajectory observed) · **Bucket**:
> v2 utility (watch-list)
> **One-line**: A research-only watch-list artifact that updates the
> `helloman3/foodieshub` GitHub repo's emergence as the **closest
> direct JTBD pull in window** for LE31. **4★ TypeScript React PWA
> 1012KB 2026-08-18** (was 3★ at 2026-08-17 baseline; +1★/24h; 0
> forks) with description "A modern, high-performance Restaurant &
> Bar POS Web Application (PWA) with real-time multi-device sync,
> thermal KOT/BOT printing, and CSV bulk management." **2-day
> trajectory: 3★ → 4★ = +0.5★/24h average** (the +3★ in <2 hours of
> push on day 1 has decayed to +1★/24h on day 2 — consistent with the
> longnick pattern of velocity-driven attention collapsing to
> steady-state slow growth). **Stack match zero (TS + React PWA, not
> Python); JTBD direct match** (restaurant/bar POS + multi-device sync
> + KOT/BOT printing + CSV bulk = exactly the LE31 feature surface
> from features 02/03/09/14). **Fails the LE31 gate today.**

## Goal

`helloman3/foodieshub` (TypeScript React PWA, 1012KB, 4★ at
2026-08-18, was 3★ at 2026-08-17 baseline; +1★/24h; 0 forks;
2026-08-17T04:45:51Z initial push, last pushed 2026-08-17T07:03:23Z;
restaurant/bar POS + multi-device sync + KOT/BOT printing + CSV bulk
management) remains the **closest direct JTBD pull in window** across
the 19-pass daily-research series.

The 2-day trajectory is now 3★ (2026-08-17) → 4★ (2026-08-18) =
**+0.5★/24h average**. The +3★ in <2 hours of push on day 1 has
decayed to +1★/24h on day 2 — **the velocity-driven signal is
already collapsing to steady-state slow growth** (the same pattern
observed in `longnick/small-pos-open-source` over the 19-pass
series). The 0-fork observation confirms this is a single-author
repo with no community traction yet.

**Stack match:** zero (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
helloman3 is TypeScript + React PWA).

**JTBD pull:** direct match. The description's feature surface
(restaurant/bar POS + multi-device sync + KOT/BOT printing + CSV bulk
management) overlaps exactly with the LE31 feature surface from
features 02 (order taking), 03 (kitchen stock tracker), 09 (kitchen
delay visibility), and 14 (split bills).

The slice ships **zero code**; the slice ships **one watch-list
artifact update** that future passes can reference. The slice boundary
is hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies.

## Scope

**In scope (v2 utility, S effort, ≤1 day, watch-list defer):**

- One source-file edit: this `features/79-foodieshub-ts-pos-watch.md`
  artifact (the watch-list record update).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (not this slice):**

- A new LE31 feature. The watch-list artifact records the market
  signal; it does NOT spawn a new LE31 implementation.
- A helloman3 codebase fork or adaptation. `helloman3/foodieshub` is
  TypeScript + React PWA, not Python + FastAPI + SQLModel + aiogram +
  Postgres. Stack match: zero. Adaptation would require a
  from-scratch rewrite in Python; not justified by the JTBD pull
  alone.
- A live star-velocity monitoring cron job. The watch is a manual
  daily-research observation; an automated cron would require
  GitHub API auth, polling cadence, and a persistence layer that
  LE31 doesn't yet need.

## Description

**Evidence precondition:** observed (verified via the GitHub Search
Repositories API on 2026-08-17 + 2026-08-18; direct repo inspection
confirms the description, language, and topics).

**Confidence:** **high** for the JTBD pull (restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management = exactly
the LE31 feature surface from features 02/03/09/14), **zero** for
the stack match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
helloman3 is TypeScript + React PWA).

**Cross-validation anchors:**

- **`longnick/small-pos-open-source`** (95★, TypeScript React PWA
  Vite, 2026-08-12 → 2026-08-18, +0★/72h CONFIRMED stagnation with
  no new push in past 24h) — the prior closest JTBD pull in window
  but velocity has definitively EXPIRED. The foodieshub emergence is
  a fresh direct JTBD pull signal but with a much smaller velocity
  baseline. **The longnick pattern of velocity-driven attention
  collapsing to steady-state slow growth is repeating in foodieshub
  (3★ in <2h on day 1 → +1★/24h on day 2 = +0.5★/24h average
  across the 2-day window).**
- **`satisfecho/pos`** (27★, Python FastAPI+SQLModel+Postgres+KDS+WS,
  pushed 2026-08-02, no activity since 2026-08-13, 7 forks up from 6
  at 2026-08-17) — the closest **stack match** in window; confirms
  the JTBD pull on the Python side but no velocity-driven signal.

**Decision: defer (watch-list, fails the gate).** The slice boundary
is hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-18, pick `foodieshub-ts-pos-watch`,
   feature path `features/79-foodieshub-ts-pos-watch.md`, Linear
   sub-issue ID (TBD), status "Watch-list (defer, fails the gate;
   +1★/24h trajectory observed)".
2. **Re-check** on 2026-08-19 for sustained velocity (target band:
   5★+ in 24h, or maintain 4★+ for 48h).
3. **Read the helloman3/foodieshub README** on the 2026-08-19 pass
   to confirm scope (multi-device sync mechanism is the most
   distinctive feature of the description).

## Telegram interaction

None. The slice is a research artifact; no user-facing Telegram
surface changes.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- Future daily-research passes must continue to query the GitHub
  Search Repositories API for `helloman3/foodieshub` and record the
  ★ count.
- The README at the helloman3/foodieshub repo — must be read to
  confirm scope.

No new pip dependencies. No new system dependencies. No new external
services.

## Open questions

- **Q1: Will the helloman3/foodieshub repo's ★ count continue to
  grow, or will it stagnate like longnick?** Re-check on 2026-08-19.
  The 2-day trajectory of +0.5★/24h is consistent with a startup
  push decaying to slow growth. If the ★ count remains 4★ or below
  for 7 days, the watch is effectively over and the JTBD pull is
  confirmed as a startup push rather than organic growth. If the ★
  count grows above 10★, the watch re-activates as a velocity-driven
  signal.
- **Q2: What is the multi-device sync mechanism?** The description
  mentions "real-time multi-device sync" but does not specify the
  mechanism (WebSocket? Server-Sent Events? Polling?). If the
  mechanism is WebSocket or SSE, it overlaps with LE31's cook-surface
  pattern (SSE). **Currently the README has not been read.**
- **Q3: Does the team want to keep tracking helloman3/foodieshub
  indefinitely, or close the watch after the next 7-day
  velocity check?** If the next 7-day check confirms stagnation,
  close the watch. **Scope this as a separate question, not this
  slice.**
- **Q4: Does the team want to engage with helloman3/foodieshub as a
  reference implementation** (read its code, learn its patterns)?
  Currently out of scope for this slice; if the watch re-activates as
  a velocity-driven signal, this becomes a legitimate follow-up
  question.

## Why this matters

The `helloman3/foodieshub` repo is the **closest direct JTBD pull
in window** for LE31 (restaurant/bar POS + multi-device sync +
KOT/BOT printing + CSV bulk management = exactly the LE31 feature
surface from features 02/03/09/14), but the **stack match is zero**
(TypeScript + React PWA, not Python + FastAPI + SQLModel + aiogram +
Postgres). The watch exists to track whether the JTBD pull accumulates
star velocity that would justify a from-scratch Python rewrite or a
charter-decided stack change to TypeScript.

**As of 2026-08-18 (19-pass observation, +1★/24h from yesterday's
3★, 0 forks), the watch is fresh but the velocity is collapsing.**
The +3★ in <2 hours of push on 2026-08-17 has decayed to +1★/24h
on 2026-08-18, a +0.5★/24h average across the 2-day window. This is
**consistent with the longnick pattern of velocity-driven attention
collapsing to steady-state slow growth** (longnick went from
+41★/24h peak to +0★/72h plateau over 6 days). The 0-fork observation
confirms this is a single-author repo with no community traction yet.

**Risk of NOT tracking:** the JTBD pull could re-activate (e.g. a
README deep-dive or a Hacker News Show HN post) and the team would
miss the window. The watch exists to catch that re-activation.

**Risk of over-tracking:** the watch is now mostly noise (4★ is a
very low baseline; velocity-driven signal is already decaying);
over-tracking consumes daily-research cycles that could be spent on
higher-signal in-window candidates.

**Net: keep the watch active for one more 7-day window, then close
it if the ★ count remains below 10★.**

## Status: watch-list (defer, fails the gate)

This file is a **watch-list artifact update (defer)**. The slice
boundary is hard: one Markdown file update, zero source code changes,
zero migrations, zero new dependencies. No code change today. The
research-side subagent (Pass 19, 2026-08-18) records the watch as
**failing the gate + +1★/24h trajectory observed** (was 3★ at
2026-08-17, now 4★ at 2026-08-18; +0.5★/24h average across 2-day
window; 0 forks). The target window is **5★+ in 24h, or maintain
4★+ for 48h**.
