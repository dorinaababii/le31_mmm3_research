# Feature 79 — FastAPI+SQLModel+Postgres Restaurant POS Stack Peer Watch

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-17 (Pick B, **defer**) · **Bucket**: v1 (stack validation)
> **One-line**: A research-only watch-list artifact that records the in-window appearance of **the FIRST in-window FastAPI+SQLModel+Postgres restaurant POS peer** (`Ing-JuanDavid/restaurant-backend-POS` 0★ 2026-08-15T22:39:51Z, 216KB, full FastAPI + SQLModel + Postgres restaurant POS backend) — a stack match for LE31 without the LE31 differentiator (no per-batch append-only `StockEntry` ledger, no Telegram cook surface, no cook-as-decision-maker). **No code today; deferred indefinitely until either (a) one of these peers crosses ≥10★ and validates the demand, or (b) LE31 ships the `StockEntry` ledger and the differentiator becomes observable.**

## Goal

The 2026-08-17 brainstorm scan surfaced two FastAPI+restaurant-POS first-pushes in 24 hours combined with yesterday's `satisfecho/pos` 27★ carry-over (FastAPI+SQLModel+Postgres+KDS+WS, last pushed 2026-08-13). The three repos together confirm that **FastAPI+SQLModel+Postgres restaurant POS is now a recognized GitHub-space pattern in 2026-08**. The appearance of an in-window STACK match for LE31 (without the LE31 differentiator) is the strongest market-validation data point we have that the LE31 stack choice is mainstream for restaurant POS.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v1 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 team wants to confirm that the FastAPI+SQLModel+Postgres restaurant POS stack is the right v1 choice, the team wants to know whether independent developers in 2026-08 are reaching for the same stack, so that the team can decide whether the LE31 strategic posture is "mainstream stack + unique differentiator" (validated) or "niche stack + unique differentiator" (re-evaluate).

**Why this is a fresh cross-section signal today**: the GitHub `restaurant POS created:>2026-07-17 language:python` cluster (30 repos) produced **two new first-pushes in 24 hours** (`Ing-JuanDavid/restaurant-backend-POS` 2026-08-15 + `tlongmx4/restaurant-pos` 2026-08-16) plus the `satisfecho/pos` 27★ carry-over. The cluster-shipping rate (2 new first-pushes in 24h) confirms the stack is a 2026-08 GitHub-space pattern. The fact that the highest-star (`satisfecho/pos` 27★) is a FastAPI+SQLModel+Postgres+KDS+WS repo makes the pattern materially meaningful.

## Scope

**In scope (v1, S effort, ≤1 day, defer — `StockEntry` ledger not yet shipped):**
- One source-file edit: this `features/79-restaurant-pos-fastapi-stack-peer-watch.md` artifact (the watch-list record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (no new LE31 implementation):**
- A new FastAPI+SQLModel+Postgres restaurant POS implementation. LE31 already ships it.
- A new `StockEntry` ledger refactor. The watch-list is parked behind the `StockEntry` ledger prerequisite.
- A new competitive analysis. Features 40 (satisfecho-watch) + 42 (self-hosted-pos-watch-3) already cover the in-window stack match peers.

## Description

**Evidence precondition:** observed (GitHub `restaurant POS created:>2026-07-17 language:python` cluster — `Ing-JuanDavid/restaurant-backend-POS` 0★ 2026-08-15T22:39:51Z + `tlongmx4/restaurant-pos` 0★ 2026-08-16T16:02:47Z + `satisfecho/pos` 27★ carry-over). Confidence: **high** for the stack pattern (the description of `Ing-JuanDavid/...` explicitly confirms the FastAPI + SQLModel + Postgres stack); **low** for the LE31 differentiator (no peer has the `StockEntry` ledger + Telegram cook + cook-as-decision-maker combination).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: Independent developers in 2026-08 are reaching for the FastAPI+SQLModel+Postgres stack for restaurant POS. If the pattern is mainstream, LE31's stack choice is validated. Plausible.
2. **Viability**: Once the stack is confirmed mainstream, LE31's existing implementation is the viability. No new viability required.
3. **Practicability and confidence**: LE31 already ships the FastAPI+SQLModel+Postgres stack. High confidence today that the stack is mainstream; high confidence today that the LE31 differentiator is not yet observable (the `StockEntry` ledger has not shipped to production).
4. **Conflict**: No invariant conflict. The pattern strengthens the existing feature 40/42 line.
5. **Outcome, appetite, scope**: v1 watch-list. S effort.
6. **Cost to operational value**: Low value today (the LE31 stack is already shipped and the differentiator is not yet observable). High value as a market-validation signal only if one of the 2 first-pushes crosses ≥10★.
7. **Circuit breaker**: Delete this file + the corresponding `INDEX.md` row + the Linear sub-issue. No other code changes to revert.

**Decision: defer (watch-list).** Cargo-culted from feature 71's pattern.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline" table with date 2026-08-17, pick `restaurant-pos-fastapi-stack-peer-watch`, feature path `features/79-restaurant-pos-fastapi-stack-peer-watch.md`, Linear sub-issue ID (TBD), status "Watch-list (defer — `StockEntry` ledger not yet shipped)".
2. **Re-check** on a future daily-research pass. If either `Ing-JuanDavid/restaurant-backend-POS` or `tlongmx4/restaurant-pos` reaches ≥10★ sustained for 7+ days, the watch re-activates (re-evaluate the gate). If `satisfecho/pos` (27★ carry-over) crosses 50★, the watch may upgrade to "stack match peer is mainstream, differentiator is the wedge."

## Telegram interaction

None. The slice is a research artifact; no user-facing Telegram surface changes.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- The `StockEntry` append-only ledger (charter §3.2) must ship to production before the LE31 differentiator becomes observable. The watch-list is sequenced behind the `StockEntry` ledger prerequisite.
- Features 40 (satisfecho-python-pos-watch) + 42 (self-hosted-pos-watch-3) already cover the in-window stack match peers.

No new pip dependencies. No new system dependencies. No new external services.

## Open questions

- **Q1: Will `Ing-JuanDavid/restaurant-backend-POS` reach ≥10★ in the next 30 days?** Re-check on a future pass. Currently 0★ after 2 days. If the README documents the `StockEntry` ledger + Telegram cook surface, the pattern would be a meaningful LE31 follow-on.
- **Q2: Will `tlongmx4/restaurant-pos` move beyond the 9KB scaffold?** Currently 9KB after 1 day. Watch-list dormant unless the repo grows past 100KB.
- **Q3: Will `satisfecho/pos` reach 50★?** Currently 27★, no activity since 2026-08-13. If the repo resumes activity and crosses 50★, the FastAPI+SQLModel+Postgres restaurant POS pattern is fully mainstream.

## Why this matters

The LE31 FastAPI+SQLModel+Postgres stack is **the LE31 v1 foundation** (PROJECT_CHARTER.md + the charter §3.2 stack rule). The 3-repo in-window cluster confirms that the stack is at a 2026-08 GitHub-space pattern in the broader ecosystem. The LE31 differentiator (per-batch append-only `StockEntry` ledger + Telegram cook surface + cook-as-decision-maker) is intact because no peer has yet shipped the combination.

**Risk of NOT tracking**: the stack match peers may consolidate in 2026-H2; if the watch-list is not in place when that happens, LE31 either re-derives the same conclusions (wasted cycles) or misses the validation (strategic risk).

**Risk of over-tracking**: the pattern is observed at the repo level only; the watch-list is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "defer until either `StockEntry` ledger ships to production or peer-velocity re-activates it." Re-evaluate when one of the 2 first-pushes crosses ≥10★ sustained for 7+ days.

## Status: watch-list (defer)

This file is a **watch-list artifact (defer)**. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. No code change today. The research-side subagent (Pass 18, 2026-08-17) records the watch as **defer — `StockEntry` ledger not yet shipped**.

## Cross-validation anchors

- **GitHub `restaurant POS created:>2026-07-17 language:python` cluster (2026-08-15..2026-08-16 push)** — 2 new first-pushes in 24h (`Ing-JuanDavid/restaurant-backend-POS` 2026-08-15 + `tlongmx4/restaurant-pos` 2026-08-16) plus the `satisfecho/pos` 27★ carry-over. The cluster confirms the FastAPI+SQLModel+Postgres restaurant POS stack is at a 2026-08 GitHub-space pattern.
- **Feature 40 (satisfecho-python-pos-watch)** — companion feature for the in-window stack match peers. The watch-list is sequenced behind feature 40.
- **Feature 42 (self-hosted-pos-watch-3)** — companion feature for the in-window self-hosted-POS peers. The watch-list is sequenced behind feature 42.
- **`satisfecho/pos` 27★ carry-over (last pushed 2026-08-13, no activity since)** — the strongest in-window stack match; the watch-list tracks when the repo resumes activity.
- **No HN / OpenAlex validating peer** — the GitHub `restaurant POS` cluster is the only in-window signal. No HN thread, no OpenAlex paper, no ProductHunt item validates the FastAPI+SQLModel+Postgres pattern for restaurant POS beyond the GitHub-space observation.
