# Feature 81 — Foodieshub TS POS Watch v3

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-19 (Pick C, watch-list,
> defer — fails the LE31 gate; stack match zero) · **Bucket**: v2
> utility (watch-list)
> **One-line**: A research-only watch-list artifact that records the
> `helloman3/foodieshub` GitHub repo's star-velocity trajectory across
> the 3-pass daily-research series since 2026-08-17. **The watch has
> hit steady-state stagnation** at 4★ for 72h with 0 forks. The
> 3-day trajectory is 4★ → 4★ → 4★ = +0★/24h average — consistent
> with the longnick pattern of velocity-driven attention collapsing
> to steady-state slow growth. **Stack match zero (TS + React PWA,
> not Python); JTBD direct match.** Watch-list add; fails the LE31
> gate today. Re-check on 2026-08-20 for sustained velocity
> (target band: 5★+ in 24h).

## Goal

`helloman3/foodieshub` (TypeScript React PWA, 4★ — unchanged for
72h, 0 forks, 1012KB, pushed 2026-08-17T07:03:23Z — no new push in
past 72h, description: "A modern, high-performance Restaurant & Bar
POS Web Application (PWA) with real-time multi-device sync, thermal
KOT/BOT printing, and CSV bulk management", topics: `pos-web-app`,
`pwa`, `react`, `restaurant-pos`, `typescript`, `web-app`) emerged
as the **closest direct JTBD pull** in window across the recent
3-pass daily-research series:

- **2026-08-17 (Pass 18):** 3★ (initial baseline)
- **2026-08-18 (Pass 19):** 4★ (+1★/24h, +0 forks, no new push) —
  **deceleration** (the +3★ on day 1 had decayed to +1★/24h by
  day 2)
- **2026-08-19 (Pass 20):** 4★ (+0★/24h, +0 forks, last push still
  2026-08-17T07:03:23Z — no new push in past 72h) — **steady-state
  stagnation confirmed**

The 3-day trajectory is now **3★ → 4★ → 4★ = +0.33★/24h average**,
fully consistent with the longnick pattern of velocity-driven
attention collapsing to steady-state slow growth.

## Scope

**In scope (v2 utility, S effort, research-only, no code — watch-list
artifact):**

- Record the daily star-velocity observation in this file.
- Update the active feature pipeline row in `INDEX.md` with the new
  4★ stagnation status and the 3-day trajectory.
- Read the foodieshub README in full on the 2026-08-20 pass to assess
  the multi-device sync mechanism (the most distinctive feature in
  the description).
- Re-check on 2026-08-20 for sustained velocity or further decay.

**Out of scope (rejected):**

- LE31 implementation work — no code, no schema change, no contract.
  This is a research observation only.
- Watching a different repo — the watch-list is specifically about
  `helloman3/foodieshub`. Other repos are covered by their own
  feature files.
- Importing `helloman3/foodieshub` code into LE31 — stack match zero
  (TS + React PWA, not Python; FastAPI ✗, SQLModel ✗, aiogram ✗,
  Postgres ✗). Charter §3.2 + §3.3 ban non-Python dependencies in
  v1. (License is also null — needs verification if the team ever
  considers vendoring.)

## Description

**Evidence precondition:** observed (verified in-window across the
3-pass series via direct GitHub repo API GETs;
`api.github.com/repos/helloman3/foodieshub`).

**Confidence:** **high** for JTBD pull (restaurant/bar POS +
multi-device sync + KOT/BOT printing + CSV bulk management =
exactly the LE31 feature surface from features 02/03/09/14), **zero**
for stack match (FastAPI ✗, SQLModel ✗, aiogram ✗, Postgres ✗;
helloman3 is TypeScript + React PWA + 0-fork single-author repo).

**Cross-validation anchors:**

- `longnick/small-pos-open-source` (TypeScript React 19 + Vite 8,
  94★, 90 forks): strongest **sustained JTBD pull** but a different
  JS POS architecture (no PWA, no KOT/BOT thermal printing). See
  feature 71 (longnick-star-velocity-watch v4).
- `satisfecho/pos` (FastAPI+SQLModel+Postgres+KDS+WS, 28★, 9 forks,
  pushed 2026-08-13T14:04:11Z, **AGPL-3.0 license — NEW finding on
  2026-08-19**): strongest **stack match** but AGPL incompatible
  with LE31 v1 charter §3.2. Covered by features 40/42.
- 3-pass observation (2026-08-17..2026-08-19) — the foodieshub
  trajectory is consistent with the longnick pattern of
  velocity-driven attention collapsing to steady-state slow growth:
  longnick did +41★ on day 1, plateau by day 3 (95★ sustained);
  foodieshub did +3★ on day 1, plateau by day 2-3 (4★ sustained).
  The pattern is the same.

**Decision: defer (watch-list, no code change).** The watch is
research-only; no LE31 feature contract to build today.

**Why this matters for v2 owner-pains:**

The foodieshub feature set (multi-device sync + thermal KOT/BOT
printing + CSV bulk management) is **exactly** the LE31 feature
surface from features 02/03/09/14:

- **Multi-device sync** ← feature 02 (order taking) + feature 03
  (kitchen stock tracker) — both need cross-device state sync.
- **Thermal KOT/BOT printing** ← feature 03 (kitchen stock tracker)
  + feature 09 (kitchen delay visibility) — both need a printing
  surface for the cook (KOT = kitchen order ticket, BOT = bar order
  ticket).
- **CSV bulk management** ← feature 06 (guest demographics) +
  future owner-side bulk data operations.

The fact that `helloman3/foodieshub` exists, ships, and is being
maintained at a steady-state 4★ with 0 forks is **strong third-party
validation that the LE31 JTBD cluster is real**. **JTBD pull is
confirmed and stable at the 4★ floor**; velocity-driven urgency is
definitively gone.

## Data model

No data model changes. The slice is research observation only.

## Implementation steps

1. **Re-check on 2026-08-20** via the daily-research cron — fetch
   `api.github.com/repos/helloman3/foodieshub` and record the new
   star count + push time.
2. **Read the foodieshub README** in full on the 2026-08-20 pass
   to confirm the multi-device sync mechanism (the most distinctive
   feature in the description).
3. **Record the finding** in the 2026-08-20 daily research report
   (continues the trajectory log: 3★ → 4★ → 4★ → [2026-08-20 read]).
4. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-19, pick `foodieshub-ts-pos-watch` (v3),
   feature path `features/81-foodieshub-ts-pos-watch.md`, Linear
   sub-issue ID (TBD), status "Backlog (watch-list, defer — fails
   the gate)".
5. **No code change** — this is a research-only slice.

## Telegram interaction

None. The slice is research observation only; no user-facing
Telegram surface changes.

## Dependencies

- Direct GitHub repo API access
  (`api.github.com/repos/helloman3/foodieshub` via the
  `HERMES_GITHUB_TOKEN` PAT). Must be reachable from the
  daily-research VPS.
- The daily-research cron (`le31-daily-research` skill).

No new pip dependencies. No new system dependencies. No new
external services.

## Open questions

- **Q1: What sync mechanism does foodieshub use?** The description
  says "real-time multi-device sync" — is it WebSocket, Server-Sent
  Events, polling, or something else? Compare to LE31 feature 23
  (sse-cook-channel) + feature 35 (sse-replay-buffer). **Read the
  README in full on the 2026-08-20 pass.**
- **Q2: What thermal printer hardware does foodieshub target?** KOT/
  BOT thermal printing is the most distinctive feature. Is it ESC/
  POS, raw print, or driver-mediated? Compare to LE31 feature 03
  (kitchen stock tracker) + feature 09 (kitchen delay visibility).
  **Read the README in full on the 2026-08-20 pass.**
- **Q3: Is the foodieshub watch worth continuing if it stabilizes at
  4★ for 7+ days?** If yes, lower the check cadence (e.g., weekly
  instead of daily) after a sustained plateau.

## Why this matters

The `helloman3/foodieshub` repo is the **closest direct JTBD pull**
in the 2026-08 in-window GitHub cluster for the LE31 feature
surface. The fact that a TS React PWA POS with the exact same
feature cluster (multi-device sync + KOT/BOT thermal printing + CSV
bulk management) is shipping and being maintained is strong
**third-party validation that the LE31 JTBD cluster is real**.

**Stack match zero** means the architecture is JS-side, not
Python-side — directly incompatible with LE31 v1 charter §3.2 + §3.3.
The repo remains useful as a v2 owner-pains watch-list reference
and as a comparative benchmark for the JS POS ecosystem. **Not LE31
v1 actionable.**

**Risk of NOT continuing the watch**: lost visibility into a real
v2 JTBD pull. Low-severity risk; the watch is research-only.

**Risk of continuing the watch**: daily-research resources spent on
a watch that has plateaued (4★ for 72h). Low cost (one direct repo
API GET per pass).

**Net: continue the watch at the 4★ + 5★/24h target band; lower
cadence to weekly after a 7-day sustained plateau.**

## Status: watch-list defer (no code)

This file is a **watch-list artifact (defer)**. The slice is
research-only; no LE31 feature contract to build today. The
research-side subagent (Pass 20, 2026-08-19) records the
recommendation as **unchanged** (watch continues; +0★/72h stagnation
confirmed; 3-day trajectory 3★ → 4★ → 4★).
