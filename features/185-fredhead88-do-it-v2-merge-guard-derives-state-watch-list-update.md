# Feature 185 — `fredhead88-do-it-v2-merge-guard-derives-state-watch-list-update` (defer)

> **NEW observation on 2026-09-17.** Documents the first-time-in-watchlist-history NEW PUSH of GitHub repo `fredhead88/do-it-v2` (license `null` in API response = no LICENSE file detected; **0★/0⑂**, Python, **pushed 2026-09-17T06:32:24Z** = first-time-in-watchlist-history active development after the 09-16 filing day, in-window by push only, **created 2026-08-27** = 21-day-old repo, **1000 KB** = +104 KB growth over the 09-16 filing day's 896 KB). Predecessor repo `fredhead88/do-it` (MIT permissive) — relicense would be required for adoption of v2. Description (verbatim from GitHub API): *"A ledger that derives state, and the guards that read it. Append-only events, nothing stamped; a merge guard that performs the merge instead of modelling it. Successor to DO-IT v4.7."* Two net-new primitives (carry-over from feature 182 filed 2026-09-16): **(1) "merge guard that performs the merge instead of modelling it"** — the *derivation primitive* (vs coxswain-graphs feature 148's *derivation target primitive*); **(2) "Append-only events, nothing stamped"** — the *event-time vs chain-time* discipline. Bucket: **v2 architecture-reference (defer, parking-lot)** — watch-list update to existing feature 182. Zero build time today.

## Goal

Retain the **"merge guard that performs the merge instead of modelling it"** + **"Append-only events, nothing stamped"** primitives as a persistent cross-section reference for any future LE31 v2 surface that introduces a second stakeholder (accountant, tax authority, regulator) who needs to ask provenance questions. The artifact is the persistent cross-section reference + a candidate *derivation primitive + event-time vs chain-time* vocabulary for the next v2-hardening moment. No code today.

## Scope

**In scope (defer artifact — watch-list update to feature 182):**

- A written record of the **NEW PUSH event on 2026-09-17** (was 896 KB on 09-16 = feature 182 filing day; today 1000 KB = +104 KB growth in 24h = first-time-in-watchlist-history active development).
- A written record of the **"merge guard that performs the merge instead of modelling it"** primitive (carry-over from feature 182): the guard is the *agent* that performs the merge, not a *function that models the merge*. **Complementary dual** to feature 148 coxswain-graphs (which is the *derivation target primitive* = graphs derive from the log); feature 182/185 is the *derivation mechanism primitive* = the merge is performed by a guard.
- A written record of the **"Append-only events, nothing stamped"** primitive (carry-over from feature 182): timestamps are derived from chain position, not asserted by the writer. This is the *event-time vs chain-time* discipline. Exactly the question an accountant would face when defending a row before tax filing: writer-asserted timestamp vs chain-position-derived timestamp.
- A decision record: today's verdict is `defer` because no v1 owner demand exists for either primitive; the v2 trigger is the introduction of a second stakeholder.
- A cross-section reference with the v2-hardening cluster: features 121, 122, 133, 134, 135, 141, **148**, 167, 168, 169, 181, **182** (the latter is the existing feature 182 to which this is a watch-list update).

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI or cook Telegram bot.
- Any change to LE31 v1's `audit_logs` schema (the optional `chain_position` BIGSERIAL column is a *future v2* addition; no migration today).
- Any change to the FastAPI route handler structure (the rename `route_handler → merge_guard` is a *vocabulary* question, not a code-change question).
- Adoption of the do-it-v2 codebase (the repo is no-license; the predecessor is MIT but the successor is a relicense-required import).
- Any AI integration in the v2 surface that exposes to a customer (charter §3.4).

## Evidence / JTBD

When a future LE31 v2 surface introduces a second stakeholder (accountant, tax authority, regulator), the owner wants *a primitive that lets the stakeholder verify "when was this row committed?" without trusting the LE31 codebase*, but struggles because *LE31 v1's audit_logs uses writer-asserted timestamps*, so that *the v2 surface can answer provenance questions with a defensible answer*.

- **Evidence class**: observed (the do-it-v2 description names the primitives directly).
- **Confidence**: high for the primitive match (the description is direct; the two primitives are well-established in audit-log research).
- **NEW observation (2026-09-17)**: maintenance activity has resumed after the 09-16 filing day (21-day-old repo with 2-consecutive-day activity = structurally the same shape as a v2 architecture reference but the activity continuation confirms it's not abandoned). The +104 KB growth in 24h is a sustained-implementation signal that updates the feature 182 baseline.
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no accountant-facing surface; the v2 surface that would *use* the primitive doesn't exist.
- **The value is naming, not direct demand**: when the first v2 surface introduces a second stakeholder, the do-it-v2 pattern is a ready-made *named* vocabulary slot.

## Description

GitHub `fredhead88/do-it-v2` (no-license ⚠ from GitHub API, 0★/0⑂, Python, pushed 2026-09-17T06:32:24Z = NEW PUSH TODAY = first-time-in-watchlist-history, created 2026-08-27 = 21-day-old repo, 1000 KB = +104 KB growth in 24h) — successor to `fredhead88/do-it` (MIT, 0★/0⑂, Python, pushed 2026-08-05, created 2026-06-01).

Description (verbatim): *"A ledger that derives state, and the guards that read it. Append-only events, nothing stamped; a merge guard that performs the merge instead of modelling it. Successor to DO-IT v4.7."*

The architectural primitive has two clauses and two net-new sub-primitives:

1. **"merge guard that performs the merge instead of modelling it"** — the *derivation mechanism*. Coxswain-graphs (feature 148) is the *derivation target* (graphs derive from the log); do-it-v2 is the *derivation mechanism* (the merge is executed by a guard, not modelled as a function). The two are *complementary, not competing*: coxswain-graphs says *what* is derived; do-it-v2 says *how* the derivation happens.
2. **"Append-only events, nothing stamped"** — the *event-time vs chain-time* discipline. Writer-asserted timestamps are *one* answer to "when was this row committed?"; chain-position-derived timestamps are *another*, more defensible answer (the chain position is auditable independently of the writer's clock).

**The 1:1 mapping onto LE31 v1 architecture (today):**

| do-it-v2 primitive | LE31 v1 today | Charter section | Status |
|---|---|---|---|
| Ledger that derives state | `audit_logs` is the source of truth; current stock / current bill / current visit are *derived* from `audit_logs` | §3.1 ✓ | **Implemented (v1)** |
| Guards that read it | FastAPI route handlers are the *guards* that read `audit_logs` | §3.1 ✓ | **Implemented (v1, implicit)** |
| Merge guard performs the merge | The route handler *executes* the merge (POST → audit_log INSERT → response) — implicit | §3.1 ✓ | **Implemented (v1, implicit)** |
| Append-only events | `audit_logs` rows are append-only (charter §3.1) | §3.1 ✓ | **Implemented (v1)** |
| Nothing stamped | `audit_logs.created_at` is writer-asserted; chain-position is *implicit* in the BIGSERIAL `id` column | §3.1 + v2 hardening | **Partially implemented (v1, implicit via BIGSERIAL id)** |
| Successor pattern (v1 → v2) | (LE31 v1 → LE31 v2 architecture evolution) | v2 | **Not started** — charter §3.1 does not require explicit version tracking |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 surface that introduces a second stakeholder), the v2 schema migration would need:

- An optional `chain_position` BIGSERIAL column on `audit_logs` (already BIGSERIAL via `id`; the explicit `chain_position` would be a *semantic alias* for `id` to make the discipline explicit).
- A guard-layer abstraction (FastAPI middleware or decorator) that *executes* the merge, not *models* it — vocabulary-only change.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v2 implementation would include:

1. Add an explicit `chain_position` semantic-alias view on `audit_logs.id` (no schema migration; just a documented view).
2. Wire a guard-layer abstraction (FastAPI middleware) that wraps the route handlers and enforces the merge-execution discipline.
3. Add a v2 surface that exposes the chain-of-custody proof to the second stakeholder (e.g., "was this row committed before tax filing?" → returns chain_position + derived timestamp).

**No existing code change today.**

## Telegram interaction

**None today.** The defer artifact is documentation only.

Future v2: the cook Telegram bot would not change; the v2 surface would be an accountant/tax-authority-facing endpoint, not a Telegram-bot surface.

## Dependencies

1. Read access to the LE31 `audit_logs` schema documentation (no code change today).
2. Read access to the do-it-v2 repository on GitHub (vocabulary reference, not adoption).
3. Owner decision on whether the future v2 trigger (introduction of second stakeholder) should preempt the v2 surface scope.

## Open questions

1. **License-clearance path**: do-it-v2 has `license: null` in the GitHub API response (= no LICENSE file detected). Should we request the upstream author (`fredhead88`) to add a LICENSE file (likely MIT to match the predecessor `fredhead88/do-it`)? Or should we treat the do-it-v2 pattern as vocabulary-only and not adopt any code? **Recommend: treat as vocabulary-only for now.** Owner decision required before any code adoption.
2. **What does "merge guard" map to in FastAPI?** FastAPI doesn't have a native "guard" concept; the closest primitives are `Depends()` (dependency injection) and middleware. Should the v2 guard-layer abstraction wrap route handlers in middleware, or should it use `Depends()` to inject a "guard" object? **Vocabulary-only question; defer until v2 trigger.**
3. **How does "chain position" interact with `audit_logs.created_at`?** If the chain-position is the `id` BIGSERIAL value, then `created_at` is redundant for provenance purposes. Should the v2 schema deprecate `created_at` in favor of `chain_position` (= `id`)? **Vocabulary-only question; defer until v2 trigger.**

## Why this matters

The do-it-v2 pattern names **the derivation mechanism** for LE31's append-only StockEntry ledger — a pattern LE31 has been implicitly operationalizing since v1 (every FastAPI route handler that does POST → `audit_log` INSERT is a "merge guard"). Naming the pattern is **vocabulary-additive**, not behavior-changing: it gives future LE31 developers a *named* primitive to reason about when the first v2 surface introduces a second stakeholder who asks "when was this row committed?". The 2026-09-17 NEW PUSH + +104 KB growth + the first-time-in-watchlist-history active development confirms the pattern is not abandoned.

The 2 primitives are the **strongest single signal in the 49-pass series** for "merge guard performs the merge" as a named architectural primitive — and the **NEW observation** on 2026-09-17 (the first-time-in-watchlist-history NEW PUSH after the 09-16 filing day) is a sustained-implementation signal that strengthens the cross-section reference.