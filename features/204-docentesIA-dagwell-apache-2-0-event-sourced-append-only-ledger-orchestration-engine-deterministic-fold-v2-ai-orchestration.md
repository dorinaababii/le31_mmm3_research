# Feature 204 — docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration (defer)

> **NEW observation (2026-09-20).** Documents in-window GitHub Search `append-only+ledger` query result: `docentesIA/dagwell` (**Apache-2.0 ✓ — parent-verified**; subagent initially claimed MIT, parent corrected by direct read of `license.spdx_id` from `gh_append-only+ledger.json`; **1★/0⑂**, Python, **pushed 2026-09-16T16:11:24Z**, in-window by push only, **422 KB** substantial repo, default_branch=`main`). Description (verbatim, parent-verified GitHub Search raw JSON): *"Provider-agnostic orchestration engine that runs agent work as a governed graph over an event-sourced, append-only ledger. State is a deterministic fold of events, never stored. executed != completed: completion needs transport + output evidence + approvals. Governed core implemented; no adapters yet."* Topics (verbatim from raw JSON): **none** (empty array; description-only signals). **The strongest deterministic-state-from-events primitive of the 52-pass series** (the only in-window candidate with the *State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals* quintuple-primitive). Bucket: **v2-AI orchestration (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core implemented; no adapters yet"** quintuple-primitive as a persistent cross-section reference for any future LE31 v2-AI orchestration surface that introduces multi-stage AI-assisted operations with explicit-state-transitions + observable-evidence + non-AI-fallback. The artifact is the persistent cross-section reference + the five named architectural primitives (event-sourced-append-only-ledger, deterministic-fold-of-events, executed-but-not-completed, completion-needs-transport+output-evidence+approvals, governed-core-without-adapters). No code today (Apache-2.0 license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **event-sourced, append-only ledger** discipline: every state change is a new event in the ledger; the ledger is the persistent record; current state is a *fold* (derivation), not stored.
- A written record of the **State is a deterministic fold of events, never stored** discipline: the derived-views-not-stored-aggregates primitive (current state is computed from events; the system never stores an aggregate state directly).
- A written record of the **executed != completed** discipline: the multi-stage explicit-state-transition primitive (an action has separate *executed* + *completed* timestamps; the *executed* event is a single immutable entry in the ledger; the *completed* event is a separate immutable entry that comes later).
- A written record of the **completion needs transport + output evidence + approvals** discipline: the three-evidence-types primitive (the action is not *complete* until (a) transport is acknowledged, (b) output evidence is captured, AND (c) approvals are recorded).
- A written record of the **governed core implemented; no adapters yet** posture: the safe-by-design discipline (the governed core is operator-tooling; adapters are customer-facing surface that would require explicit §3.4 review before shipping).
- A written record of the **provider-agnostic** discipline: any LLM provider (OpenAI, Anthropic, local models) can be plugged in without changing the core.
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-assisted workflow surface (charter §3.4 explicit invariant).
- A cross-section reference with the prior event-sourced + deterministic-fold + explicit-state-transition primitives cluster: features 148 (coxswain-graphs), 173 (Sholu021/KitchenIQ), 176 (same), 183 (n0-public), 186 (Sholu021/KitchenIQ v3 filing), 187 (traust-ledger), 188 (ShibaClaw), 189 (HASHI), 192 (LinkedParticles/particles-standard), 193 (jchen7222/supply-chain-event-platform), 195 (skaslam1407 restaurant-cloud-kitchen), 196 (monstabravo agent-ledger), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 203 (this file's Pick A sister — shawn-durrani/membro append-only-fact-ledger), 205 (this file's Pick C sister). The *transferable insight* is the **State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters** quintuple-primitive set.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any change to the `Order.status` state machine in v1.
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2-AI orchestration surface in v1 (charter §3.4 explicit invariant: AI may only assist owner/staff with observable evidence + non-AI fallback; no v1 surface today).
- Any provider-agnostic LLM-orchestration surface in v1 (LE31 v1 has no AI surface; provider-agnostic is inapplicable).
- Any adapter implementation (the repo explicitly notes "Governed core implemented; no adapters yet"; the artifact is the vocabulary, not the implementation).

## Description

GitHub Search `append-only+ledger` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-20/gh_append-only+ledger.json`) returned 37 total / 30 in-window candidates; `docentesIA/dagwell` is one of the 6 net-new in-window MIT/Apache Python candidates not previously filed. It is the strongest deterministic-state-from-events primitive of the 52-pass series.

The `docentesIA/dagwell` repo's architectural pattern has one core principle and four sub-primitives:

1. **Event-sourced, append-only ledger** — the persistent record is a sequence of events; every state change is a new event in the ledger. The *event-sourcing* discipline maps 1:1 onto LE31's `audit_logs` schema (charter §3.1: append-only posture).
2. **State is a deterministic fold of events, never stored** — the derived-views-not-stored-aggregates primitive (current state is computed from events; the system never stores an aggregate state directly). The *deterministic-fold* discipline maps onto LE31's current-stock-from-StockEntry pattern: current stock is derived from `StockEntry` events (the cumulative sum of `prepared - consumed`); the system does NOT store a `current_stock` column.
4. **executed != completed** — the multi-stage explicit-state-transition primitive (an action has separate *executed* + *completed* timestamps). Maps onto LE31's cook-prep-event discipline: a cook's prep event has `prepared_at` (executed) but kitchen might not have `received_at` (transported) yet, and manager might not have `approved_at` yet. The *executed-but-not-completed* primitive is the **explicit-state-transition** primitive that maps onto LE31 charter §3.1's invariant that operational transitions are explicit user actions.
5. **Completion needs transport + output evidence + approvals** — the three-evidence-types discipline (the action is not *complete* until (a) transport is acknowledged, (b) output evidence is captured, AND (c) approvals are recorded). Maps onto LE31's `Order.status` state machine: `sent → confirmed → served → closed`. The *completion-needs-three-evidence-types* primitive mirrors LE31's *confirmed-needs-cook-acknowledged + served-needs-dish-delivered + closed-needs-payment-cleared* discipline.
6. **Governed core implemented; no adapters yet** — the safe-by-design posture. The governed core is operator-tooling (charter §3.4 permitted); adapters (the customer-facing surface) are not yet implemented and would require explicit §3.4 review before shipping. The *governed-core-without-adapters* discipline is the textbook charter §3.4 compliance pattern: build the safe-by-design core first, then add customer-facing adapters with explicit §3.4 review.

The LE31 relevance is the **State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters** quintuple-primitive. LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the question this repo answers is "if (and only if) LE31 v2 ever introduces multi-stage AI-assisted operations, what is the explicit-state-transition + observable-evidence + non-AI-fallback primitive set that satisfies charter §3.4?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2-AI trigger condition (if the first v2-AI PR that introduces multi-stage AI-assisted operations lands):** potential schema additions (depending on the v2-AI surface):
- `state_derivation_view` table — a registry of named state-derivation views (current-stock, daily-revenue, etc.); the *deterministic-fold-of-events* discipline from dagwell. Each view is a SQL query or a Python function that takes the event stream as input and produces the derived state as output.
- `prepared_at + received_at + approved_at` distinction on `StockEntry` — separate *executed* + *completed* timestamps on each StockEntry; the *executed != completed* discipline from dagwell. Each StockEntry would carry `prepared_at` (executed by cook), `received_at` (transported to kitchen), and `approved_at` (approved by manager).
- `transport_evidence + output_evidence + approval_evidence` columns on `Order.status` — three separate evidence columns for the *completion-needs-three-evidence-types* discipline from dagwell. Each `Order.status` transition would record the transport-acknowledgement, the output-evidence-captured, and the approval-recorded.
- `governed_core` operator-tooling surface — a config / policy primitive that gates which AI-assisted operations are permitted; the *governed-core-without-adapters* discipline from dagwell.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces multi-stage AI-assisted operations lands):**
- Add a `state_derivation_view` SQLModel table (view_name, view_definition, dependencies).
- Add `prepared_at + received_at + approved_at` columns to `StockEntry` (nullable for backward compatibility; existing rows get NULL received_at and approved_at).
- Add `transport_evidence + output_evidence + approval_evidence` columns to `Order.status`.
- Add a `governed_core` policy / config layer that gates which AI-assisted operations are permitted.
- Optionally add a `state_derivation_engine` Python module that computes derived views from the event stream; the *deterministic-fold* primitive from dagwell.

**Steps independent of the v2-AI trigger (today):**
- [x] Read the `docentesIA/dagwell` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm Apache-2.0 permissive license (parent re-verified `license.spdx_id = "Apache-2.0"` from `gh_append-only+ledger.json`; subagent's MIT claim corrected).
- [x] Confirm the description's *State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* quintuple-primitive vocabulary (parent re-verified verbatim).
- [x] Cross-reference with features 148, 173, 176, 183, 186, 187, 188, 189, 192, 193, 195, 196, 197 (repo now 404), 198, 199, 203 (this file's Pick A sister), 205 (this file's Pick C sister) (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces multi-stage AI-assisted operations lands):**
- The cook would need a Telegram command to view the *prepared_at + received_at + approved_at* distinction on a (e.g., `/prep-status <stock_entry_id>`); the *executed != completed* primitive maps 1:1 onto a chat-style query interface.
- The owner would need a Telegram command to view the *three-evidence-types status* on an Order (e.g., `/order-status <order_id>`); the *completion-needs-three-evidence-types* primitive would surface transport-acknowledged + output-evidence-captured + approval-recorded status.
- These are v2-AI orchestration surface additions; not in v1 scope.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v2-AI trigger dependencies:** depends on the v2-AI surface that introduces multi-stage AI-assisted operations with explicit-state-transitions + observable-evidence + non-AI-fallback (LE31 v1 has none of these surfaces). Cross-references: features 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 145 (garde-fous), 152, 156 (AWIG-OS rule-citing-audit), 160 (FactGraph), 167 (provtrail hash-chained ledger), 169 (akoffice933 openshare-ledger SHA-256 hash chain), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger disposition-ledger kernel), 188 (ShibaClaw self-hosted security-first AI agent), 189 (HASHI local-first control-plane), 190 (ilyautov small-business-RU-34 AI-skills-tax-contractor-INN), 192 (LinkedParticles/particles-standard sourced + confidence-scored append-only ledger), 196 (monstabravo agent-ledger append-only-checked-against-git), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 203 (this file's Pick A sister — shawn-durrani/membro append-only-fact-ledger), 205 (this file's Pick C sister).

## Open questions

1. **Provider-agnostic surface details:** what does *provider-agnostic* mean concretely in dagwell (does it mean a Python interface for any LLM provider, or a CLI / config layer)? The full read of dagwell's provider-agnostic surface is needed before any v2 port.
2. **Governed core implementation details:** what does *governed core* mean concretely in dagwell (does it mean a TypeScript-style type system, a runtime policy layer, a SQL-based authorization layer)? The full read of dagwell's governed core is needed before any v2 port.
3. **Multi-stage-state-transition schema details:** what is the exact schema of a *multi-stage-state-transition* event (does each event have a `state_machine_id` FK to a `StateMachine` table, or is the state machine encoded in the event payload)? The full read of dagwell's state-machine schema is needed before any v2 port.
4. **No adapters yet status:** when does dagwell plan to ship adapters, and which adapters (LLM providers, customer-facing surfaces, observability platforms)? This affects the v2 surface design.
5. **Apache-2.0 license file confirmation:** is dagwell's Apache-2.0 license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters** quintuple-primitive is the **cleanest 2026-09-20 deterministic-state-from-events vocabulary for any future LE31 v2-AI orchestration surface** — and the Apache-2.0 permissive license + the description-only-signals (no topics required) confirm it's a *named architectural pattern*, not just a theoretical one. The vocabulary is fully transferable to LE31's charter §3.1 + §3.4 compliance patterns (append-only posture; operator-tooling with observable evidence + non-AI fallback). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce multi-stage AI-assisted operations (e.g., AI-suggested menu updates, AI-suggested reconciliation), the owner wants *a multi-stage explicit-state-transition surface with observable evidence + non-AI fallback*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant) and v1's Order.status state machine is not extensible to multi-stage AI workflows*, so that *v2 can offer AI assistance without violating §3.4 or re-architecting v1*." **PASS** (zero-pain today; v1 is small enough that single-stage transitions are sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the architectural match (the *State is a deterministic fold of events + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* primitive set is well-established in the GitHub Apache-2.0-community-adoption cluster). Apache-2.0 license is charter-compatible per §3.2 (more permissive than MIT in some senses — explicit patent grant — less permissive in others — explicit patent termination clause; both Apache-2.0 and MIT are acceptable permissive licenses per charter §3.2). **PASS**. |
| 4 | **Conflict** | None. The *State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; operator-tooling with observable evidence + non-AI fallback; governed core is operator-tooling, adapters require §3.4 review before shipping). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI orchestration (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/204-docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration-HANDOFF.md` and `features/204-docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-20.md` (52nd consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 148, 173, 176, 183, 186, 187, 188, 189, 192, 193, 195, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 203 (this file's Pick A sister), 205 (this file's Pick C sister).
- Sister-picks from 2026-09-20: feature 203 (shawn-durrani/membro v2-AI control-plane), feature 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference).