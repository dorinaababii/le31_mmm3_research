# Feature 242 — `shayangolmezerji-menu-events-mit-append-only-event-store-restaurant-menus-optimistic-concurrency-idempotent-commands-replayable-projections-python-fastapi-postgresql-v1-production-restaurant-event-store-reference` (defer)

> **NEW observation (2026-09-28).** Documents in-window GitHub Search `fastapi+restaurant` query result: `shayangolmezerji/menu-events` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **1★/0⑂**, Python, **pushed 2026-09-27T09:42:37Z** (in-window by `pushed_at`), **created 2026-09-26T16:37:40Z** (in-window by `created_at` — **2-day-old repo**), **repo size = 114 KB modest repo** (parent-verified via raw GitHub API JSON), `default_branch=main`, `archived=false`). **No topics** (parent-verified from raw JSON: `"topics": []`). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-28): *"Append-only event store for restaurant menus: optimistic concurrency, idempotent commands, replayable projections. Python, FastAPI, PostgreSQL."* The **Python + FastAPI + PostgreSQL = the EXACT LE31 v1 stack** (FastAPI + SQLModel + Postgres); the **append-only + optimistic concurrency + idempotent commands + replayable projections** quadruple-primitive = the **§3.3 stock-discipline vocabulary mapped 1:1 onto a real-world 2026 restaurant event store**. The **strongest single net-new v1 vocabulary artifact of the 59-pass daily-research series**. Bucket: **v1 production-restaurant-event-store-reference (defer, parking-lot, vocabulary reference)** — zero build time today.

## Goal

Retain the **Python + FastAPI + PostgreSQL + append-only + optimistic concurrency + idempotent commands + replayable projections** quadruple-primitive + stack-shape as a persistent cross-section reference for any future LE31 v1 surface that introduces (a) **menu-event-store** (a restaurant's menu changes are recorded as events, not as a single current-state row), (b) **append-only** (every event is recorded once and never modified), (c) **optimistic concurrency** (concurrent menu updates are detected and rejected at the database level, not by a single-process lock), and (d) **idempotent commands + replayable projections** (the same command can be applied twice without changing the result; the current menu state can be derived by replaying events from a known starting point). The artifact is the persistent cross-section reference + the verbatim description + the stack-shape. No code today (MIT license permits future code reuse; vocabulary-only artifact today; 114 KB modest-repo size is comfortably readable).

## Scope

**In scope (defer artifact):**
- A written record of the **append-only event store** discipline: the *append-only + no-mutation* primitive applied to the *menu* dimension (LE31 v1's `audit_logs` is already append-only but does NOT serve as a *menu-event-store*; the *menu-event-store* layer is the *menu-state-history* layer between operator and cook that records every menu change as an event).
- A written record of the **optimistic concurrency** discipline: the *optimistic-concurrency* primitive applied to the *menu-update* dimension (LE31 v1's transactional state uses Postgres-level locks; the *optimistic-concurrency* posture is the *versioned + reject-on-stale-version* posture applied to menu updates; this is the §3.1 explicit-state-transitions discipline applied at the database-version level).
- A written record of the **idempotent commands + replayable projections** discipline: the *idempotent-commands + replayable-projections* primitive pair (LE31 v1's operational commands are not yet idempotent at the database level; the *idempotent-commands* posture is the *same-command-twice-produces-same-result* posture; the *replayable-projections* posture is the *current-state-derived-from-event-replay* posture).
- A decision record: today's verdict is `defer` because LE31 v1 has no menu-event-store surface today (charter §3.1 v1 surfaces are sufficient for v1 ops); the cross-section reference is informative, not a v1 build-trigger.
- A cross-section reference with the prior event-sourced + append-only-ledger cluster: features 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 125 (Auditable Continual Learning), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 135 (DreamLedger), 137 (NL-to-Executable-Obligations), 141 (KRINEIA five-invariants), 148 (coxswain-graphs), 153 (chronology-protocol post-quantum anchoring), 154 (asset-ledger content-addressed), 155 (openshare-ledger SHA-256 hash chain), 161 (claims-ledger Toulmin), 167 (provtrail hash-chained ledger), 168 (edusouzaxgv asset-ledger content-addressed), 169 (akoffice933 openshare-ledger SHA-256 hash chain), 181 (Merkle Audit), 182 (fredhead88/do-it merge-guard), 183 (n0-public autonomous-agent-ledger), 185 (fredhead88/do-it-v2 watch-list), 187 (traust-ledger disposition-ledger-kernel), 192 (LinkedParticles/particles-standard sourced + confidence-scored append-only ledger), 193 (jchen7222/supply-chain-event-platform bitemporal event-sourced), 196 (monstabravo agent-ledger), 197 (rajo69-ledgerkb vocabulary-only — repo now 404), 198 (aidankaras-arbiter postgresql point-in-time), 203 (shawn-durrani/membro append-only-fact-ledger — duplicate of 236), 212 (yesterday's vocabulary-only watch-list), 219 (Mormolykos/epcore deterministic-licensing-kernel), 220 (Jita81/commit-replay-bench append-only-evidence-ledger — today's Pick B watch-list update), 230 (mentu-ai/commitment-protocol accountability-ledger), 231 (LinkedParticles/particles-standard sourced-claim-ledger), 232 (lpalbou/AbstractGateway durable-control-plane), 236 (shawn-durrani/membro local-first-ai-assistant-memory), 237 (willykeenan/agentbrain-contextlib markdown-contextlib). The *transferable insight* is the **Python + FastAPI + PostgreSQL + append-only + optimistic concurrency + idempotent commands + replayable projections** quadruple-primitive + the *exact-stack-shape match* (FastAPI + SQLModel + Postgres is LE31 v1).

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2 horizontal-expansion surface in v2 (charter §3.1 + §3.2 invariant: v2 surface expansion is the next boundary; this is a vocabulary reference, not a v2 expansion trigger).
- Any menu-event-store implementation in v1 (the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off).

## Description

The pick is **`shayangolmezerji/menu-events`** — a Python + MIT + append-only-event-store-for-restaurant-menus + optimistic-concurrency + idempotent-commands + replayable-projections vocabulary artifact. **Charter §3.4 NOT triggered** because the artifact is operator-tooling (the event store records menu changes from the operator's supervised workflows), NOT customer-facing (no restaurant diner interacts with the menu-event-store; the diner interacts with the menu that the cook reads). The artifact is the persistent cross-section reference for the verbatim description + the 4 named primitives + the stack-shape.

**Stack-shape match (the load-bearing primitive):** the *Python + FastAPI + PostgreSQL* triple is **byte-for-byte the LE31 v1 stack** (FastAPI + SQLModel + Postgres are all on the LE31 pin set). The verbatim stack match is the **strongest single-repo cross-section signal for v1 vocabulary of the 59-pass series** (comparable in strength to the `Sholu021/KitchenIQ` feature 173/176/186 stack-shape match but with the additional *append-only + idempotency* primitives that LE31 v1's `StockEntry` already operates by).

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v1 surface that adopts the *menu-event-store* primitive would extend the LE31 v1 data model with appropriate new tables (e.g., a `menu_event` table with `event_id, menu_id, event_type, event_data, event_version, recorded_at, parent_event_id`; a `menu_projection` table with `projection_id, menu_id, projection_version, projection_state, derived_at`; or a `current_menu_state` view that is a deterministic fold of the `menu_event` table). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v1 PR is triggered by the trigger condition below, the implementation would:
1. Read the `shayangolmezerji/menu-events` README at https://github.com/shayangolmezerji/menu-events for the *append-only + optimistic concurrency + idempotent commands + replayable projections* quadruple-primitive.
2. Cross-reference with LE31 v1's `StockEntry` schema to identify the *delta* (the *delta* = `shayangolmezerji/menu-events` introduces append-only-event-store-for-menus + optimistic-concurrency + idempotent-commands + replayable-projections primitives that LE31 v1's `StockEntry` does not have for the menu dimension; LE31 v1's `StockEntry` is append-only but does NOT serve as a *menu-event-store* — the *menu-event-store* discipline is the *menu-state-history* layer between operator and cook).
3. Apply charter §3.1 explicit-state-transitions review to the *delta* (any new v1 surface requires explicit owner/charter sign-off; the *menu-event-store* surface is charter §3.1-compatible provided the explicit state transitions are preserved — i.e., the operator can read every menu state via the projection view without using the event-replay).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the `shayangolmezerji/menu-events` reference is the *vocabulary* for *append-only + optimistic concurrency + idempotent commands + replayable projections*, NOT for *menu-event-store replacement*.

## Telegram interaction

Zero Telegram interaction today (defer artifact). If a future v1 PR is triggered by the trigger condition below, the implementation would add `/menu_history` (read-only) and `/menu_replay` (admin-only with confirmation) commands to the cook Telegram bot. The cook already reads the menu from the v1 menu surface; the new commands would let the cook see *how the menu got to the current state* and let the admin replay the menu-event-store to verify the projection matches expectations.

## Dependencies

- **LE31 v1 menu surface** — every menu change is recorded by the operator as a current-state row update today; the *menu-event-store* primitive would change this to record every menu change as an event.
- **LE31 v1 `StockEntry` schema** — already append-only; the *menu-event-store* primitive mirrors the `StockEntry` discipline for the menu dimension.
- **LE31 v1 `audit_logs` schema** — already append-only; the *menu-event-store* primitive mirrors the `audit_logs` discipline for the menu dimension.
- **LE31 v1 FastAPI + SQLModel + Postgres stack** — already pinned; the *menu-event-store* primitive is implemented with the same stack.
- **Cross-references:** features 148 (coxswain-graphs), 153 (chronology-protocol), 154 (asset-ledger content-addressed), 181 (Merkle Audit), 183 (n0-public autonomous-agent-ledger), 187 (traust-ledger disposition-ledger-kernel), 192 (LinkedParticles/particles-standard sourced-claim-ledger), 193 (jchen7222/supply-chain-event-platform bitemporal event-sourced), 196 (monstabravo agent-ledger), 197 (rajo69-ledgerkb vocabulary-only — repo now 404), 198 (aidankaras-arbiter postgresql point-in-time), 203 (shawn-durrani/membro append-only-fact-ledger — duplicate of 236), 219 (Mormolykos/epcore deterministic-licensing-kernel), 220 (Jita81/commit-replay-bench append-only-evidence-ledger — today's Pick B), 230 (mentu-ai/commitment-protocol accountability-ledger), 232 (lpalbou/AbstractGateway durable-control-plane), 236 (shawn-durrani/membro local-first-ai-assistant-memory), 237 (willykeenan/agentbrain-contextlib markdown-contextlib).

## Open questions

- Does LE31 v1 want a *menu-event-store* surface at all? The current v1 menu surface uses a single current-state row per menu item; the *menu-event-store* primitive would change this to a per-event record. The trade-off is: (a) current-state row = simpler, fewer rows, faster reads; (b) event-store = full history, replayable projections, optimistic concurrency. The decision is **owner's** — the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off.
- Does LE31 v1 want *optimistic concurrency* at the database-version level? The current v1 transactional state uses Postgres-level locks; the *optimistic-concurrency* posture would replace these with versioned rows + reject-on-stale-version. The trade-off is: (a) Postgres-locks = simpler, fewer roundtrips, single-process; (b) optimistic-concurrency = multi-process-safe, replayable, reject-on-stale. The decision is **owner's**.
- Does LE31 v1 want *idempotent commands + replayable projections*? The current v1 operational commands are not yet idempotent at the database level; the *idempotent-commands* posture would require a command-id field on every command + a uniqueness check. The trade-off is: (a) non-idempotent = simpler, no command-id bookkeeping; (b) idempotent = retry-safe, replayable, audit-friendly. The decision is **owner's**.

## Why this matters

- The **verbatim stack match** (Python + FastAPI + PostgreSQL = LE31 v1) is the strongest single-repo cross-section signal for v1 vocabulary of the 59-pass series. The *exact-stack-match* is high-value for any future LE31 v1 *menu-state-history* surface.
- The **append-only + optimistic concurrency + idempotent commands + replayable projections** quadruple-primitive is the **§3.3 stock-discipline vocabulary mapped 1:1 onto a real-world 2026 restaurant event store**. The future LE31 v1 surface that adopts the *menu-event-store* primitive can adopt the verbatim 4-primitive set.
- The artifact is **vocabulary-only**; zero build time today; fully reversible (delete the feature file + the HANDOFF + the Linear sub-issue is the complete rollback).
- The trigger condition is **the first v1 PR that proposes a menu-state-history surface, a menu-replay surface, or a menu-event-store surface**.

## Cross-section evidence (one-line each)

- The `append-only + idempotent commands + optimistic concurrency + replayable projections` quadruple-primitive is the LE31 §3.3 stock-discipline vocabulary mapped onto the menu dimension.
- The `Python + FastAPI + PostgreSQL` triple is byte-for-byte the LE31 v1 stack.
- The 4 named primitives (append-only + optimistic concurrency + idempotent commands + replayable projections) are the load-bearing value of the artifact.
- Net-new observation 2026-09-28 (ripgrep-confirmed unique vs features 1–241).
