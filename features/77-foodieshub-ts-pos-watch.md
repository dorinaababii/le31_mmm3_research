# Feature 77 — FoodiesHub TypeScript POS Watch

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-17 (Pick C, **NEW**
> watch-list) · **Bucket**: v2 utility (watch-list)
> **One-line**: A research-only watch-list artifact that records the
> `helloman3/foodieshub` GitHub repo's emergence as the **closest
> direct JTBD pull in window** for LE31. **3★ TypeScript React PWA
> 954KB 2026-08-17T04:45:51Z** with description "A modern,
> high-performance Restaurant & Bar POS Web Application (PWA) with
> real-time multi-device sync, thermal KOT/BOT printing, and CSV
> bulk management." **Stack match zero (TS + React PWA, not Python);
> JTBD direct match** (restaurant/bar POS + multi-device sync +
> KOT/BOT printing + CSV bulk = exactly the LE31 feature surface from
> features 02/03/09/14). **Fails the LE31 gate today.**

## Goal

`helloman3/foodieshub` (TypeScript React PWA, 954KB, 3★, 2026-08-17,
restaurant/bar POS + multi-device sync + KOT/BOT printing + CSV bulk
management) emerged as the **closest direct JTBD pull in window**
across the 17-pass daily-research series.

The 3★ in <2 hours of push is a soft-velocity signal comparable to the
longnick +41★/24h peak (3★ vs 95★, both per-hour rates are similar).
The signal needs 7+ days of sustained velocity to confirm; the 1-day
observation is consistent with a startup push, not organic growth.

**Stack match:** zero (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
helloman3 is TypeScript + React PWA).

**JTBD pull:** direct match. The description's feature surface
(restaurant/bar POS + multi-device sync + KOT/BOT printing + CSV bulk
management) overlaps exactly with the LE31 feature surface from
features 02 (order taking), 03 (kitchen stock tracker), 09 (kitchen
delay visibility), and 14 (split bills).

The slice ships **zero code**; the slice ships **one watch-list
artifact** that future passes can reference. The slice boundary is
hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies.

## Scope

**In scope (v2 utility, S effort, ≤1 day, watch-list defer):**

- One source-file edit: this `features/77-foodieshub-ts-pos-watch.md`
  artifact (the watch-list record).
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
Repositories API on 2026-08-17; direct repo inspection confirms the
description, language, and topics).

**Confidence:** **high** for the JTBD pull (restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management = exactly
the LE31 feature surface from features 02/03/09/14), **zero** for
the stack match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
helloman3 is TypeScript + React PWA).

**Cross-validation anchors:**

- **`longnick/small-pos-open-source`** (95★, TypeScript React PWA
  Vite, 2026-08-12 → 2026-08-17, +0★/48h CONFIRMED stagnation with
  active pushes) — the prior closest JTBD pull in window but velocity
  has definitively EXPIRED. The foodieshub emergence is a fresh
  direct JTBD pull signal but with a much smaller velocity baseline.
- **`satisfecho/pos`** (27★, Python FastAPI+SQLModel+Postgres+KDS+WS,
  pushed 2026-08-02, no activity since 2026-08-13) — the closest
  **stack match** in window; confirms the JTBD pull on the Python
  side but no velocity-driven signal.

**Decision: defer (watch-list, fails the gate).** The slice boundary
is hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-17, pick `foodieshub-ts-pos-watch`,
   feature path `features/77-foodieshub-ts-pos-watch.md`, Linear
   sub-issue ID (TBD), status "Watch-list (defer, fails the gate)".
2. **Re-check** on 2026-08-18 for sustained velocity (target band:
   5★+ in 24h, or maintain 3★+ for 48h).
3. **Read the helloman3/foodieshub README** on the 2026-08-18 pass
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
  grow, or will it stagnate like longnick?** Re-check on 2026-08-18.
  If the ★ count remains 3★ or below for 7 days, the watch is
  effectively over and the JTBD pull is confirmed as a startup push
  rather than organic growth. If the ★ count grows above 10★, the
  watch re-activates as a velocity-driven signal.
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

The `helloman3/foodieshub` repo is the **closest direct JTBD pull
in window** for LE31 (restaurant/bar POS + multi-device sync +
KOT/BOT printing + CSV bulk management = exactly the LE31 feature
surface from features 02/03/09/14), but the **stack match is zero**
(TypeScript + React PWA, not Python + FastAPI + SQLModel + aiogram +
Postgres). The watch exists to track whether the JTBD pull accumulates
star velocity that would justify a from-scratch Python rewrite or a
charter-decided stack change to TypeScript.

**As of 2026-08-17, the watch is fresh**: 3★ in <2 hours of push is a
soft-velocity signal comparable to the longnick +41★/24h peak.
The signal needs 7+ days of sustained velocity to confirm.

**Risk of NOT tracking:** the JTBD pull could re-activate (e.g. a
README deep-dive or a Hacker News Show HN post) and the team would
miss the window. The watch exists to catch that re-activation.

**Risk of over-tracking:** the watch is now mostly noise (3★ is a
very low baseline; velocity-driven signal is not yet established);
over-tracking consumes daily-research cycles that could be spent on
higher-signal in-window candidates.

**Net: keep the watch active for one more 7-day window, then close
it if the ★ count remains below 10★.**

## Status: watch-list (defer, fails the gate)

This file is a **watch-list artifact (defer)**. The slice boundary is
hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies. No code change today. The
research-side subagent (Pass 18, 2026-08-17) records the watch as
**fresh** with 3★ in <2 hours and revises the target window to
**5★+ in 24h, or maintain 3★+ for 48h**.