# Feature 75 — Day-part × Menu-Margin Owner Drill-in Surface

> **Priority**: P3 (parking-lot) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-16 (Pick C, **parking-lot**) · **Bucket**: v2 owner-pains (extends feature 39)
> **One-line**: A research-only **parking-lot** artifact that records the in-window GitHub repo `Hamuda55/restaurant-ops-dashboard` (pushed 2026-08-13T07:58:05Z, no license, 0★, 548 bytes README-only, "Restaurant operations analytics dashboard (Streamlit) on real, anonymised Square POS data - peak hours, revenue by day-part, menu performance"). The pattern is a **no-account day-part menu-margin drill-in** that extends the existing owner daily-recap Telegram push (feature 39). **No code today; parked until feature 74 (per-recipe cost rollup) ships — without marginal cost, the day-part surface reduces to revenue-only, which is not enough to drive menu decisions.**

## Goal

Feature 39 (`owner-daily-recap-telegram`) ships a single Telegram push at end-of-day. The owner wants to drill in: which dishes made margin at which hours, not just totals. The existing `OrderItem.sold_at` timestamp plus `MenuItem.price` plus (post-feature 74) `MenuItem.theoretical_cost` is the raw data needed. A no-account web page (same pattern as feature 29 / 69) is the smallest surface that gives drill-in without login.

The slice ships **zero code**; the slice ships **one parking-lot artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 owner wants to decide which dishes to keep on the menu and which to retire, the owner wants to see each dish's margin at each day-part (lunch vs dinner), but the existing daily-recap Telegram push only shows daily totals, so that the owner sees "lamb shoulder made 340 EUR in 14 covers between 19:30-21:00 but only 40 EUR in 9 covers between 12:30-14:00" in one tap without logging in.

**Why this is a fresh cross-section signal today**: `Hamuda55/restaurant-ops-dashboard` (no license, Python Streamlit, 0★, 548 bytes README-only, "Restaurant operations analytics dashboard (Streamlit) on real, anonymised Square POS data - peak hours, revenue by day-part, menu performance") was pushed 2026-08-13T07:58:05Z — created 2026-08-12, in-window. The repo's bullet list explicitly enumerates "peak hours, revenue by day-part, menu performance" — the same three dimensions the LE31 owner needs. Combined with `ifrederico/forkluck` (cost side), the two repos form the **owner-side analytics pattern** that LE31 has the raw data to compute but no surface to render.

**Why parking-lot**: 548 bytes README-only is too small to count as a real peer; no observed pain; no license declared; depends on feature 74 (cost rollup) which is itself parking-lot. Streamlit is not the LE31 stack, so the pattern transfers, not the code.

## Scope

**In scope (parking-lot, S effort, ≤1 day, defer — feature 74 prerequisite not yet shipped):**
- One source-file edit: this `features/75-day-part-menu-margin-surface.md` artifact (the parking-lot record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (deferred to a future v2 scope when feature 74 ships):**
- A new no-account web page for day-part menu-margin drill-in. The parking-lot artifact records the pattern; it does NOT spawn a new LE31 implementation.
- A `Hamuda55/restaurant-ops-dashboard` codebase fork or adaptation. Streamlit is not LE31's stack; the repo is 548 bytes README-only with no declared license; pattern transfers, not code.
- The labor-hour dimension — even when feature 74 ships, the labor data is gated behind feature 43 which is also not yet shipped. Two-step parking-lot.
- A new pip dependency. None.

## Description

**Evidence precondition:** inferred (owner-KPI pattern from two 0★ repos, no observed pain). Confidence: **low** for the JTBD shape (the pattern is well-established in the broader ecosystem), **zero** for the LE31-specific pain (no observed pain, no HN/OpenAlex validating peer, no license-acceptable peer).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: Owner needs day-part menu-margin — plausible but not observed at the LE31 owner level. Cross-section pattern from kitchen-analytics ecosystem.
2. **Viability**: Once feature 74 ships, the day-part surface is a no-account web page (same pattern as feature 29 / 69). **High** in that future state; **undefined** today.
3. **Practicability and confidence**: Feature 74 prerequisite not yet shipped. **Low** confidence today.
4. **Conflict**: No invariant conflict. The day-part surface is a read-only query against existing `OrderItem` + `MenuItem` rows.
5. **Outcome, appetite, scope**: v2 owner-pains. S effort (extends feature 39's recap).
6. **Cost to operational value**: Low value today (feature 74 not shipped). Marginal value with feature 74 alone (revenue-only). High value with features 43 + 74 (full margin).
7. **Circuit breaker**: Delete this file + the corresponding `INDEX.md` row + the Linear sub-issue. No other code changes to revert.

**Decision: parking-lot.** Re-evaluate when feature 74 ships to production.

## Data model

No data model changes. The slice is a pure parking-lot artifact. **Future scope** (if the feature un-parked): the existing `OrderItem.sold_at` timestamp + `MenuItem.price` + `MenuItem.theoretical_cost` (post-feature 74) is the raw data needed. No new SQLModel tables.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline" table with date 2026-08-16, pick `day-part-menu-margin-surface`, feature path `features/75-day-part-menu-margin-surface.md`, Linear sub-issue ID (TBD), status "Parking-lot (no observed pain; feature 74 prerequisite not yet shipped)".
2. **Re-check** on a future daily-research pass once feature 74 ships to production. If the in-window GitHub `restaurant created:>2026-07-17 language:python` cluster continues to ship same-week day-part-analytics repos, the parking-lot re-activates.

## Telegram interaction

**Future scope** (if the feature un-parked): the existing feature 39 Telegram push gains a single new button — "drill in" — that opens the no-account web page. Today's slice ships no Telegram code change.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- Feature 74 (`per-recipe-cost-margin-rollup`) must ship to production to provide `MenuItem.theoretical_cost`.
- Feature 39 (`owner-daily-recap-telegram`) must be in production to provide the recap-from-which-to-drill-in.
- Feature 29 (`owner-no-account-live-floor-link`) and feature 69 (`owner-no-account-shift-recap-link`) for the no-account `OwnerLink` token pattern.
- For the full margin (revenue - cost) the day-part surface is a 1-step un-park. For the full P&L (revenue - cost - labor) the day-part surface is a 2-step un-park (also needs feature 43).

No new pip dependencies today. No new system dependencies. No new external services.

## Open questions

- **Q1: Will `Hamuda55/restaurant-ops-dashboard` grow beyond 548 bytes?** Re-check on a future pass. If the repo accumulates real code, the JTBD pull is validated.
- **Q2: Will a non-548-byte, license-clean day-part-analytics peer emerge?** Currently only `Hamuda55/restaurant-ops-dashboard` is in window and it is 548 bytes README-only with no declared license. If a real peer emerges, the parking-lot's evidence precondition can be upgraded from "inferred" to "observed".
- **Q3: Will feature 74 ship first?** Without feature 74, the day-part surface reduces to revenue-only (which is not enough to drive menu decisions — high-revenue dishes can still be high-cost and unprofitable). The parking-lot is parked behind feature 74.
- **Q4: Will the LE31 owner report the day-part menu-margin pain?** Unknown. The owner has not yet reported any day-part analytics need. The parking-lot is parked until either the pain is observed or the prerequisites ship.

## Why this matters

The owner pain "which dishes make margin at which hours?" is a **real LE31 owner problem** (small restaurants often retire high-revenue but low-margin dishes because the labor cost swings at dinner dominate). The pattern is mature in the broader ecosystem (Square POS + 7shifts + Toast all ship day-part analytics). **The blocker is not pattern novelty; the blocker is observed pain + prerequisite availability.**

**Risk of NOT tracking**: the day-part question will surface after the owner reviews a quarterly menu-margin report. If the parking-lot is not already in place when that happens, the build will be rushed. The watch exists to ensure the pattern is already-evaluated when the trigger condition arrives.

**Risk of over-tracking**: feature 74 is not yet shipped. The parking-lot artifact is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the feature under "parking-lot until feature 74 ships to production." Re-evaluate when the prerequisite lands.

## Status: parking-lot

This file is a **parking-lot artifact (no build)**. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. No code change today. The research-side subagent (Pass 17, 2026-08-16) records the pick as **parking-lot — no observed pain; feature 74 prerequisite not yet shipped**.

## Cross-validation anchors

- **`Hamuda55/restaurant-ops-dashboard`** (in-window, 2026-08-13T07:58:05Z push, no license, 0★, 548 bytes README-only, Streamlit) — day-part analytics dashboard. Pattern transfer only.
- **`ifrederico/forkluck`** (in-window, 2026-08-16T04:37:15Z push, AGPL, 0★, Django + Next.js) — kitchen costing (cost side). Same-cluster signal.
- **Feature 39 (`owner-daily-recap-telegram`)** — daily-recap Telegram push. Pick is a drill-in extension of feature 39.
- **Feature 74 (`per-recipe-cost-margin-rollup`)** — cost rollup. Pick needs feature 74's `MenuItem.theoretical_cost`.
- **Feature 29 (`owner-no-account-live-floor-link`)** + **Feature 69 (`owner-no-account-shift-recap-link`)** — no-account `OwnerLink` token pattern. Pick reuses the same token primitive.
- **No HN / OpenAlex validating peer** — the GitHub `restaurant created:>2026-07-17 language:python` cluster is the only in-window signal. No HN thread, no OpenAlex paper, no ProductHunt item validates the LE31-specific pain.
