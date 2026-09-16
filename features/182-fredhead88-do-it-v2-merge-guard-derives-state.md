# Feature 182 — `fredhead88-do-it-v2-merge-guard-derives-state` (defer)

> **NEW observation (2026-09-16).** Documents in-window GitHub repo `fredhead88/do-it-v2` (no-license ⚠, **0★/0⑂**, Python, **pushed 2026-09-16T04:20:14Z**, in-window by push only, **created 2026-08-27** — 20-day-old repo, **896 KB**). Predecessor repo `fredhead88/do-it` (MIT, **0★/0⑂**, Python, pushed 2026-08-05, created 2026-06-01). Description (verbatim from GitHub API): *"A ledger that derives state, and the guards that read it. Append-only events, nothing stamped; a merge guard that performs the merge instead of modelling it. Successor to DO-IT v4.7."* Two net-new primitives beyond features 121/122/148/167/168/169/181: **(1) "merge guard that performs the merge instead of modelling it"** — the *derivation primitive* (vs coxswain-graphs feature 148's *derivation target primitive*); **(2) "Append-only events, nothing stamped"** — the *event-time vs chain-time* discipline. Bucket: **v2 architecture-reference (defer, parking-lot)** — watch-list defer. Zero build time today.

## Goal

Retain the **"merge guard that performs the merge instead of modelling it"** + **"Append-only events, nothing stamped"** primitives as a persistent cross-section reference for any future LE31 v2 surface that introduces a second stakeholder (accountant, tax authority, regulator) who needs to ask provenance questions. The artifact is the persistent cross-section reference + a candidate *derivation primitive + event-time vs chain-time* vocabulary for the next v2-hardening moment. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"merge guard that performs the merge instead of modelling it"** primitive: the guard is the *agent* that performs the merge, not a *function that models the merge*. Inverse of "merge is a function applied to two states" → "merge is an event with consequences". **Complementary dual** to feature 148 coxswain-graphs (which is the *derivation target primitive* = graphs derive from the log); feature 182 is the *derivation mechanism primitive* = the merge is performed by a guard.
- A written record of the **"Append-only events, nothing stamped"** primitive: timestamps are derived from chain position, not asserted by the writer. This is the *event-time vs chain-time* discipline. Exactly the question an accountant would face when defending a row before tax filing: writer-asserted timestamp vs chain-position-derived timestamp.
- A decision record: today's verdict is `defer` because no v1 owner demand exists for either primitive; the v2 trigger is the introduction of a second stakeholder.
- A cross-section reference with the v2-hardening cluster: features 121, 122, 133, 134, 135, 141, **148**, 167, 168, 169, 181.

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
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no accountant-facing surface; the v2 surface that would *use* the primitive doesn't exist.
- **The value is naming, not direct demand**: when the first v2 surface introduces a second stakeholder, the do-it-v2 pattern is a ready-made *named* vocabulary slot.

## Description

GitHub `fredhead88/do-it-v2` (no-license ⚠, 0★/0⑂, Python, pushed 2026-09-16T04:20:14Z, created 2026-08-27, 896 KB) — successor to `fredhead88/do-it` (MIT, 0★/0⑂, Python, pushed 2026-08-05, created 2026-06-01).

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

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

Future v2: the cook Telegram bot would not change; the v2 surface would be an accountant/tax-authority-facing endpoint, not a Telegram-bot surface.

## Dependencies

- **Charter §3.1 invariant compatibility**: ✓ (the primitives are *additive* on top of the existing append-only `audit_logs`; the merge guard is the same FastAPI process today).
- **§3.2 license compatibility**: ⚠ (predecessor is MIT permissive; do-it-v2 is no-license = adoption would require relicense).
- **§3.4 AI compatibility**: ✓ not triggered (the primitives are not customer-facing AI; the Claude-Code integration pattern in the predecessor is *staff-tooling* territory).
- **Stack compatibility**: ✓ (Python; the primitives are architecture patterns, not new dependencies).

## Open questions

1. **Does LE31 v2 need a second-stakeholder surface at all?** The owner is the only stakeholder in v1; the question is whether v2 introduces an accountant, tax authority, or regulator as a second principal. This is an owner decision per charter §3.4 + §3.5.
2. **If yes, is the writer-asserted timestamp sufficient, or is chain-position needed?** Today's `audit_logs.created_at` is writer-asserted; the chain-position discipline would say *no, derive it from insertion order*. For v1 single-restaurant single-postgres the writer-asserted timestamp is sufficient; for v2 accountant-facing audit, chain-position is the more defensible answer.
3. **What is the merge guard in LE31 v1 today, and should it be renamed?** Implicitly, the FastAPI route handlers are the guards; the explicit-naming discipline (rename `route_handler` → `merge_guard`?) is a vocabulary question, not a code-change question. Recommend a *vocabulary* commit to the codebase comments if the v2 trigger fires.

## Why this matters

The **"merge guard that performs the merge" + "Append-only events, nothing stamped"** vocabulary is the **v2-hardening vocabulary** that LE31 needs *before* it can answer the second-stakeholder question. Without this vocabulary, the first v2 surface that introduces a second stakeholder would have no architectural reference (the existing `audit_logs` per-mutation discipline is the *what*; the do-it-v2 primitives are the *how*). The two primitives together with feature 148 coxswain-graphs form a *complete* answer to the question *"how is state derived from the log?"* in two complementary halves.

Companion artifacts: features **148** (coxswain-graphs, the derivation *target* primitive), 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 133 (HANSARD), 134 (ECHO), 135 (DreamLedger), 141 (KRINEIA), 167 (provtrail), 168 (asset-ledger), 169 (openshare-ledger), 181 (Merkle Audit) — all ripgrep-verified distinct from this artifact. Parent research issue HMM-259 (Research 2026-09-16 — daily).
