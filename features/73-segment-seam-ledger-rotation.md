# Feature 73 — Segment-Seam Ledger Rotation for StockEntry

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-16 (Pick A, **defer**) · **Bucket**: v2 utility (append-only ledger hardening)
> **One-line**: A research-only watch-list artifact that records the in-window GitHub repos `nradawg/segment-seam-chain` (pushed 2026-08-15T21:45:59Z, MIT, 0★) and `nradawg/skew-ratchet-clock` (pushed 2026-08-15T21:22:06Z, MIT, 0★) — a same-author same-day push that pairs **rotation-and-seam verification** with **monotonic-timestamp integrity** for append-only logs. The pattern is the missing piece that would let feature 49's per-row tamper-evident `StockEntry` hash chain compact into cold segments without losing end-to-end verification. **No code today; deferred until feature 49 ships to production and the rotation threshold is observable.**

## Goal

Feature 49 (`postledger-tamper-evident-hash`) covers per-row tamper-evidence on `StockEntry` but assumes an unbounded single-table chain. After 6-12 months of production at a single restaurant the table will exceed the practical backup/replay window; rotation to cold segments is the missing piece. The segment-seam pattern from `nradawg/segment-seam-chain` solves exactly this: a deleted segment cannot pass as `N` valid files because the seam-hash links every segment to its predecessor. The same author's `skew-ratchet-clock` solves the companion problem: monotonic-timestamp integrity across rotation boundaries (forward ceiling + cumulative backward drift).

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 owner wants to retain the append-only `StockEntry` ledger for accounting traceability beyond 6 months, the owner wants the table to rotate into cold segments, but the integrity guarantee of feature 49's per-row hash chain is lost at the rotation boundary, so that a future v2 pass can ship a segment-rotation scheme that preserves feature 49's chain integrity across segment boundaries.

**Why this is a fresh cross-section signal today**: the GitHub `topic:append-only` cluster (139 repos) shipped a same-author same-day push on 2026-08-15 that pairs **both** primitives (rotation + monotonic clock). The cluster confirms the production-hardening inflection point for append-only logs in the broader ecosystem. The LE31 owner has not yet reported the pain (LE31 has not yet shipped feature 49 to production), so the evidence precondition is **observed** at the GitHub-repo level but **inferred** at the LE31 owner-pain level.

## Scope

**In scope (v2 utility, S effort, ≤1 day, defer — feature 49 unproven):**
- One source-file edit: this `features/73-segment-seam-ledger-rotation.md` artifact (the watch-list record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (deferred to a future v2 scope when feature 49 ships):**
- A new LE31 segment-rotation implementation. The watch-list artifact records the pattern; it does NOT spawn a new LE31 implementation.
- A new LE31 monotonic-clock primitive. Same.
- A migration to feature 49's hash chain. Feature 49 is the prerequisite; this feature cannot ship without it.
- A `nradawg/segment-seam-chain` or `nradawg/skew-ratchet-clock` fork or adaptation. Both are TypeScript; LE31 ships Python. Pattern transfers, not code.

## Description

**Evidence precondition:** observed (GitHub `topic:append-only` cluster — `nradawg/segment-seam-chain` + `nradawg/skew-ratchet-clock` + `Diegobraun/braunlog` + `Number2i/PaymentOrchestrationSystem` + `AxFab/pocket-db` all pushed 2026-08-15). Confidence: **medium** for the JTBD shape (the pattern is well-established in the broader ecosystem), **low** for the LE31-specific pain (no observed pain at the LE31 owner level).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: Accountable ledger survives backup/replay window — speaks to owner's right-to-audit pain (already covered by feature 49). Plausible.
2. **Viability**: Once feature 49 exists, the rotation scheme is a build-time concern (no user-facing impact). High.
3. **Practicability and confidence**: Feature 49 prerequisite not yet shipped. Low confidence today.
4. **Conflict**: No invariant conflict. Append-only invariants (feature 49) are preserved by segment rotation.
5. **Outcome, appetite, scope**: v2 utility. S effort.
6. **Cost to operational value**: Low value today (feature 49 not shipped). High value once feature 49 is in production.
7. **Circuit breaker**: Delete this file + the corresponding `INDEX.md` row + the Linear sub-issue. No other code changes to revert.

**Decision: defer (watch-list).** Cargo-culted from feature 71's pattern.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline" table with date 2026-08-16, pick `segment-seam-ledger-rotation`, feature path `features/73-segment-seam-ledger-rotation.md`, Linear sub-issue ID (TBD), status "Watch-list (defer — feature 49 prerequisite not yet shipped)".
2. **Re-check** on a future daily-research pass once feature 49 ships to production and the `StockEntry` table begins to approach the rotation threshold. If the in-window GitHub `topic:append-only` cluster continues to ship same-author same-day push patterns, the watch re-activates.

## Telegram interaction

None. The slice is a research artifact; no user-facing Telegram surface changes.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- Feature 49 (`postledger-tamper-evident-hash`) must ship to production before this feature can be evaluated. The watch-list is a sequence marker.

No new pip dependencies. No new system dependencies. No new external services.

## Open questions

- **Q1: Will the `nradawg/segment-seam-chain` + `nradawg/skew-ratchet-clock` pattern stabilize in the broader ecosystem?** Re-check on a future pass. If the same author ships a third in-window primitive (e.g., compaction / sparse-index), the pattern is consolidating.
- **Q2: Will feature 49 ship to production first?** Without feature 49, this feature has no place to land. The watch-list is parked until feature 49 lands.
- **Q3: Will the LE31 owner's append-only ledger need 6-12 months of data before rotation becomes necessary?** Unknown. LE31 v1 has not yet shipped the append-only audit chain (feature 49 is in backlog). The rotation threshold is hypothetical today.

## Why this matters

The append-only `StockEntry` ledger is **the LE31 differentiator** (PROJECT_CHARTER.md + 16+ feature files reference it). Feature 49 covers the per-row tamper-evidence; this feature would cover the rotation boundary. **The pair is the production-grade append-only ledger pattern** that the LE31 charter implicitly assumes but does not yet ship.

**Risk of NOT tracking**: the rotation-threshold problem will surface after feature 49 is in production for 6-12 months. If the watch-list is not already in place when that happens, the build will be rushed. The watch exists to ensure the pattern is already-evaluated when the trigger condition arrives.

**Risk of over-tracking**: feature 49 is not yet shipped. The watch-list artifact is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "defer until feature 49 ships to production and the rotation threshold is observable." Re-evaluate when feature 49 lands.

## Status: watch-list (defer)

This file is a **watch-list artifact (defer)**. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. No code change today. The research-side subagent (Pass 17, 2026-08-16) records the watch as **defer-until-feature-49-prerequisite**.

## Cross-validation anchors

- **GitHub `topic:append-only` cluster (2026-08-15 push)** — `nradawg/segment-seam-chain` + `nradawg/skew-ratchet-clock` + `Diegobraun/braunlog` + `Number2i/PaymentOrchestrationSystem` + `AxFab/pocket-db` all pushed within a 24-hour window. The cluster confirms the pattern is at a production-hardening inflection point.
- **Feature 49 carry-over** — `postledger-tamper-evident-hash` is the prerequisite. The watch-list is sequenced behind feature 49.
- **Feature 30 (`append-only-audit-redirect`)** — companion feature for the audit chain. The rotation scheme interacts with feature 30's redirect logic.
- **Feature 31 (`peer-ledger-compare`)** — peer-architecture comparison of append-only ledger patterns. Future pass can compare LE31's chain against `nradawg/segment-seam-chain` once feature 49 ships.
- **No HN / OpenAlex validating peer** — the GitHub `topic:append-only` cluster is the only in-window signal. No HN thread, no OpenAlex paper, no ProductHunt item validates the pattern yet.
