# Feature 71 — Longnick Star Velocity Watch

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-16 (Pick B, watch-list,
> defer — watch expired) · **Bucket**: v2 utility (watch-list)
> **One-line**: A research-only watch-list artifact that records the
> `longnick/small-pos-open-source` GitHub repo's star-velocity
> trajectory across the 17-pass daily-research series. **The watch has
> effectively expired** as of 2026-08-16 (3-day average +1.5★/24h,
> decayed from +41★/24h one-day peak). Revised target window: 95★ ± 10
> sustained over the next 7 days. No code; no new LE31 implementation.

## Goal

`longnick/small-pos-open-source` (TypeScript, MIT, 1462KB, 95★, 94
forks, Vite/React/TS reference frontend for a small café POS) emerged
as the **highest-star-velocity in-window GitHub peer** across the
17-pass daily-research series:

- **2026-08-13 (Pass 15):** 50★ (baseline)
- **2026-08-14 (Pass 16):** 91★ (+41★/24h) — the **one-day peak**
- **2026-08-15 (Pass 17, 16th consecutive quiet day):** 95★ (+4★/24h) —
  **deceleration**
- **2026-08-16 (Pass 17, 17th consecutive quiet day):** 95★ (+0★/24h) —
  **stagnation**

The 3-day average velocity is now +1.5★/24h; the 4-day average is
+11.25★/24h (95★ total - 50★ baseline over 4 days). **The velocity-driven
watch has effectively expired** as of 2026-08-16. JTBD pull is still
confirmed (95★ in 4 days is very high for a TS POS starter with 94
forks) but the velocity-driven market-validation data point is no
longer accumulating.

The slice ships **zero code**; the slice ships **one watch-list
artifact** that future passes can reference. The slice boundary is
hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies.

## Scope

**In scope (v2 utility, S effort, ≤1 day, watch-list defer — watch
expired):**

- One source-file edit: this `features/71-longnick-star-velocity-watch.md`
  artifact (the watch-list record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (not this slice):**

- A new LE31 feature. The watch-list artifact records the market
  signal; it does NOT spawn a new LE31 implementation.
- A longnick codebase fork or adaptation. `longnick/small-pos-open-source`
  is TypeScript + React 19 + Vite 8 (frontend reference), not LE31's
  Python + FastAPI + SQLModel + aiogram + Postgres stack. Stack match:
  zero. Adaptation would require a from-scratch rewrite in Python; not
  justified by the JTBD pull alone.
- A live star-velocity monitoring cron job. The watch is a manual
  daily-research observation; an automated cron would require
  GitHub API auth, polling cadence, and a persistence layer that
  LE31 doesn't yet need.

## Description

**Evidence precondition:** observed (verified via the GitHub Search
Repositories API across the 17-pass series).

**Confidence:** **high** for the JTBD pull ("small café POS" matches
the LE31 owner pain exactly), **zero** for the stack match (FastAPI ✗,
SQLModel ✗, aiogram ✗, Postgres ✗; longnick is TypeScript + React 19 +
Vite 8).

**Cross-validation anchors:**

- **2026-08-14 GitHub `topic:small-business` cluster** — the longnick
  repo sits in a cluster of small-business repos that gained star
  velocity in the same window. The JTBD pull is the cluster, not
  longnick alone.
- **`satisfecho/pos`** (25★, Python FastAPI+SQLModel+Postgres+KDS+WS,
  pushed 2026-08-02, carry-over from 2026-08-07) — the closest **stack
  match** in window; confirms the JTBD pull on the Python side but
  no velocity-driven signal.

**Decision: defer (watch-list, watch expired).** The slice boundary is
hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-16, pick `longnick-star-velocity-watch`,
   feature path `features/71-longnick-star-velocity-watch.md`, Linear
   sub-issue ID (TBD), status "Watch-list (defer — watch expired)".
2. **Re-check** on 2026-08-17 for sustained stagnation; record the
   new ★ count + delta.

## Telegram interaction

None. The slice is a research artifact; no user-facing Telegram
surface changes.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- Future daily-research passes must continue to query the GitHub
  Search Repositories API for `longnick/small-pos-open-source` and
  record the ★ count.

No new pip dependencies. No new system dependencies. No new external
services.

## Open questions

- **Q1: Will the longnick repo's ★ count continue to stagnate, or will
  it resume organic growth?** Re-check on 2026-08-17. If the ★ count
  remains in the revised target window (95★ ± 10), the watch is
  effectively over and the JTBD pull is confirmed as a steady-state
  signal. If the ★ count resumes growth above 105★, the watch
  re-activates.
- **Q2: Will longnick ever ship a backend?** Today the repo is a
  frontend reference (Vite/React/TS). If a backend is added, the
  stack match question re-opens. **Currently the repo description
  confirms frontend-only; no backend in window.**
- **Q3: Does the team want to keep tracking longnick indefinitely, or
  close the watch after the next 7-day stagnation check?** If the
  next 7-day check confirms stagnation, close the watch. **Scope this
  as a separate question, not this slice.**

## Why this matters

The `longnick/small-pos-open-source` repo is the **closest JTBD pull
in window** for the LE31 owner-pain (small café POS), but the **stack
match is zero** (TypeScript + React 19 + Vite 8 frontend, no Python
backend). The watch exists to track whether the JTBD pull accumulates
star velocity that would justify a from-scratch Python rewrite or a
charter-decided stack change to TypeScript.

**As of 2026-08-16, the watch has effectively expired**: the
velocity-driven signal (which was the original reason to watch) is
gone. The JTBD pull is confirmed (95★ is very high) but the velocity
that made it special has decayed to a normal slow-growth / stagnation
pattern.

**Risk of NOT tracking:** the JTBD pull could re-activate (e.g. a
backend PR or a Hacker News Show HN post) and the team would miss the
window. The watch exists to catch that re-activation.

**Risk of over-tracking:** the watch is now mostly noise (the
velocity-driven signal is gone); over-tracking consumes daily-research
cycles that could be spent on higher-signal in-window candidates.

**Net:** keep the watch active for one more 7-day window, then close
it if the revised target window (95★ ± 10) is sustained.

## Status: watch-list (defer — watch expired)

This file is a **watch-list artifact (defer)**. The slice boundary is
hard: one Markdown file update, zero source code changes, zero
migrations, zero new dependencies. No code change today. The
research-side subagent (Pass 17, 2026-08-16) records the watch as
**expired** and revises the target window to **95★ ± 10 sustained over
the next 7 days**.
