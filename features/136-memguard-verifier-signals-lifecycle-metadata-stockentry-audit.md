# Feature 136 — MemGuard verifier-signals lifecycle-metadata StockEntry audit (defer)

> **NEW observation (2026-08-29).** Documents in-window arXiv paper `2608.21867v1` MemGuard (2026-08-22, cs.AI) from the 2026-08-29 daily-brainstorm pass. The paper's core mechanism is **persistent lifecycle metadata on memory records, not a one-shot filter**: multi-criteria score-token verification is converted into reward, confidence, label, and uncertainty descriptors attached to every memory candidate before activation and reused during retrieval, conflict resolution, summarization, and archival. Bucket: **v2 owner-pains (architecture reference)** — watch-list defer. Zero build time today.

## Goal

Retain the **verifier-signals-as-lifecycle-metadata** mechanism as a design constraint for the first LE31 v2 surface that exposes owner-facing history for non-stock entities (`Visit`, `Bill`, `Shift`). The mechanism answers: *how does the system tell a fresh record from a stale one, without replaying the full audit chain by hand?*

The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the paper's two failure modes (unreliable admission, memory drift) and the lifecycle-metadata mechanism that addresses both.
- A decision record: today's verdict is `defer` because LE31 v1 has no owner-facing history surface for non-stock entities, and the charter does not authorise v2 audit-trail work yet.
- A reference for the next time LE31 considers an owner-facing history surface for `Visit`, `Bill`, or `Shift`.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any user-facing history surface.
- Implementation of the paper's multi-criteria verifier (reward / confidence / label / uncertainty) — the natural LE31 verifier signals are operational, not LLM-output-derived.
- Implementation of any memory-bucket-management primitive (the paper's *conflict resolution / summarization / archival* steps are out-of-scope at LE31's scale).

## Description

arXiv `2608.21867v1` MemGuard — *"MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance"* — identifies two failure modes in long-running LLM-agent memory:

1. **Unreliable admission** — failed trajectories, accidental successes, and misleading observations enter memory because they appear relevant, then mislead later decisions.
2. **Memory drift** — long-running banks accumulate duplicate, stale, and conflicting records that retrieval alone cannot repair.

MemGuard's core distinction is to **treat verifier output not as a one-shot filter, but as persistent lifecycle metadata.** Multi-criteria score-token verification is converted into reward, confidence, label, and uncertainty descriptors attached to every memory candidate **before activation** and **reused during retrieval, conflict resolution, summarization, and archival**. The paper verifies empirically on Terminal-Bench 2.0, SWE-Bench Verified, WebArena, and Mind2Web across 4 backbones, comparing against 4 memory baselines plus a verifier-only control under matched runtime budgets: *averaged over 5 seeds, MemGuard achieves the best success metric and lowest average steps in all 16 backbone-benchmark settings, improving over ReasoningBank, the strongest prior baseline among the memory methods we evaluate, with a largest gain of 7.9 success-rate points on WebArena.*

LE31 v1 has no owner-facing history surface for non-stock entities (`Visit`, `Bill`, `Shift`), so the lifecycle-metadata primitive is **a future v2 surface, not a v1 gap**. The paper's value for LE31 is therefore *naming* + *the dual relationship to feature 134* + *the empirical claim*:

- **Naming** — when LE31 v2 considers an owner-facing history surface, the relevant question is *what is the lifecycle of each record?* — not *what is the latest version of each record?*.
- **Dual relationship to feature 134 (ECHO)** — ECHO argues *replace* append-only conversation history with auditable structured records (because chat history is not a state ledger). MemGuard argues *augment* memory records with persistent lifecycle metadata (verifier signals survive as columns, not as ephemeral filter results). The two are companion architectural primitives: ECHO is about *the shape of records*; MemGuard is about *the metadata attached to records*.
- **Empirical claim** — the +7.9 success-rate points on WebArena is the strongest single-paper evidence that *lifecycle metadata* is a measurable primitive, not a vague principle.

LE31's natural verifier signals are operational, not LLM-output-derived:
- *"Was this `Bill` reconciled within shift?"*
- *"Was this `Visit` closed at end of service?"*
- *"Was this `StockEntry` reconciled by the nightly close?"*
- *"Was this `Shift` reconciliation accepted by the owner?"*

These are *operational verifier signals* in MemGuard's sense: each is a binary / categorical / numeric value computed at a specific moment in the record's lifecycle, attached to the record as a persistent column, and reused whenever the record is surfaced to the owner. The defer surfaces this mapping as a future v2 design constraint.

## Data model

No schema change today. The defer artifact documents that the future `RecordLifecycle` table — if built — would have columns `(record_kind, record_id, admitted_at, last_verified_at, superseded_by, archived_at, verifier_signal_json)` keyed by `(record_kind, record_id)`.

## Implementation steps

None today (defer). When LE31 first considers a v2 owner-facing history surface:

1. **Re-run the LE31 feature gate** with the MemGuard paper in hand.
2. **Define the LE31 operational verifier signal taxonomy.** The paper's signals are multi-criteria reward / confidence / label / uncertainty from LLM outputs; LE31's signals are operational (reconciled? closed? accepted? superseded?). The mapping is the real cost.
3. **Decide whether `RecordLifecycle` is a new table or columns on existing entity tables.** A new table keeps the entity tables simple; columns on entity tables make the lifecycle query trivial but couple entity evolution to lifecycle evolution.
4. **Decide what "superseded_by" means in a single-restaurant setting.** The paper's memory records can be superseded by new versions; LE31's `Bill` can be superseded by a re-issue, but the original `Bill` row must remain in the append-only `audit_logs` per charter §3.1. The lifecycle metadata must not be confused with the audit chain.
5. **Pilot on one entity first.** Do not design the lifecycle metadata for `Visit + Bill + Shift` at once.

## Dependencies

- Charter §3.1 (append-only posture) — the lifecycle metadata must remain additive over the existing `audit_logs`.
- Charter §3.5 (privacy) — operational verifier signals must not include diner-identifying fields.
- Feature 134 `echo-auditable-memory-plane-stockentry-audit` — companion: ECHO is about *record shape*; MemGuard is about *record lifecycle*.
- Feature 108 `telegram-chat-history-fuzzy-search-stockentry-audit` — adjacent: chat-history fuzzy-search is a related v2 audit-trail surface.

## Open questions

- **What operational verifier signals make sense for `Visit` vs `Bill` vs `Shift`.** The mapping is not 1:1.
- **Whether the verifier signals are computed automatically or operator-declared.** LE31 charter §3.1 favours explicit state transitions; an automatic verifier is implicit.
- **What "superseded" means in an append-only setting.** Charter §3.1 forbids silent rewriting; the lifecycle metadata must record supersession explicitly.
- **Whether the lifecycle metadata is visible to the cook/waiter or owner-only.** Charter §3.4 (operator/staff assistance) suggests staff-relevant, not diner-facing.

## Why this matters

The paper provides three things LE31 does not currently have: (i) **architectural vocabulary** for "verifier signals as persistent lifecycle metadata"; (ii) **the dual relationship to feature 134** that completes the audit-trail story (record-shape + record-lifecycle); (iii) **an empirical claim** (+7.9 success-rate points on WebArena) that the lifecycle-metadata discipline is a measurable primitive, not a vague principle. The cost of *not* filing this today is the risk that the first v2 owner-facing history surface omits the lifecycle metadata entirely, then has to retrofit it onto records that were never designed to carry it. Filed now so the v2 boundary has the vocabulary ready when the surface is proposed.