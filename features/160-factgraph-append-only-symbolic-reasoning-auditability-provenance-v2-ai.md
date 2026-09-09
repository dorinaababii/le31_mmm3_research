# Feature 160 — factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai (defer)

> **NEW observation (2026-09-09).** Documents in-window GitHub repo `Symbolic-Intelligence-Org/factgraph` (Apache-2.0, **1★/0⑂**, Python, **pushed 2026-09-08T16:00:59Z**, in-window by push only, 13 KB description). Description (verbatim): *"FactGraph is an append-only fact ledger for structured symbolic reasoning with strong emphasis on auditability, provenance, and explainability."* **The ≥1★ + auditability+provenance+explainability vocabulary maps 1:1 onto LE31 charter §3.4** (AI with observable evidence). Bucket: **v2-AI architecture-reference** — watch-list defer. Zero build time today.

## Goal

Retain the **"append-only fact ledger for structured symbolic reasoning with auditability+provenance+explainability"** vocabulary as a persistent cross-section reference for the next v2-AI surface that consults the LE31 `audit_logs` table. The artifact is the persistent cross-section reference + a candidate *named vocabulary* for any future AI-assisted LE31 feature. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **auditability+provenance+explainability vocabulary**: the three named properties that an AI-assisted feature must satisfy to be LE31 §3.4-compliant.
- A written record of the **1:1 mapping onto LE31 charter §3.4**: charter §3.4 says *AI may assist owner/staff, with observable evidence and a non-AI fallback*; the auditability+provenance+explainability vocabulary is the *named discipline* that operationalizes "observable evidence".
- A written record of the **append-only ledger discipline**: every fact is a new ledger row; current fact set is **derived** from the ledger, never stored as a mutable cache.
- A decision record: today's verdict is `defer` because the LE31 v1 codebase does not yet have any AI-assisted feature; the auditability+provenance+explainability vocabulary is a future v2-AI surface, not v1.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema (charter §3.1: append-only).
- Any change to the `StockEntry` schema (charter §3.1: append-only).
- Any new AI-assisted feature (charter §3.4: no customer-facing AI; AI may assist owner/staff with observable evidence and a non-AI fallback).
- Any new fact-ledger schema (LE31 v1 does not have a fact-ledger; introducing one would require an owner decision per charter §3.2).
- Adoption of the factgraph code (the repo is a 13 KB description + a Python codebase; the *vocabulary* is transferable; the *code* is not adoptable).

## Evidence / JTBD

When a future LE31 v2-AI feature (e.g. menu suggestion, prep-time forecast, owner recap) is introduced, the operator wants *a named auditability+provenance+explainability vocabulary*, but struggles because *the primitive doesn't exist in the LE31 codebase today*, so that *the v2-AI surface has observable evidence per charter §3.4*.

- **Evidence class**: observed (the factgraph README names the auditability+provenance+explainability vocabulary).
- **Confidence**: high for the vocabulary match (auditability + provenance + explainability = LE31 §3.4's "observable evidence"); medium for the transferability (the symbolic-reasoning substrate may be over-engineered for a small restaurant's AI assistance).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no AI-assisted feature.
- **The value is naming, not direct demand**: when the first v2-AI surface lands, the factgraph vocabulary is a ready-made *named* discipline.

## Description

GitHub `Symbolic-Intelligence-Org/factgraph` (Apache-2.0, 1★/0⑂, Python, pushed 2026-09-08T16:00:59Z, in-window by push only, 13 KB description). Description (verbatim): *"FactGraph is an append-only fact ledger for structured symbolic reasoning with strong emphasis on auditability, provenance, and explainability."*

The architectural pattern has one core principle and three named properties:

1. **"Append-only fact ledger"** — every fact is a new ledger row; current fact set is **derived** from the ledger, never stored as a mutable cache. This is the *commit primitive*; the *commit* is the only place where a fact becomes part of the system.
2. **Auditability** — every fact in the ledger has a *trail* (who added it, when, why, with what evidence). The trail is queryable; the operator can ask "why does this fact exist?" and get a complete answer.
3. **Provenance** — every fact has a *source* (where did this fact come from? which document, which sensor, which observation?). The source is recorded at commit time and is queryable; the operator can ask "where did this fact come from?" and get a complete answer.
4. **Explainability** — every fact derivation (e.g. "current fact set" derived from the ledger) has an *explanation* (how was this fact derived from which other facts?). The derivation is recorded and queryable; the operator can ask "how was this fact derived?" and get a complete answer.

**The 1:1 mapping onto LE31 v1 architecture:**

| factgraph component | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| Append-only fact ledger | `audit_logs` table (every operational transition is a new row) + `StockEntry` table (every prepared-item quantity change is a new row) | §3.1 (Never update or delete ledger events) | **Same discipline** — both use append-only |
| Auditability | `audit_logs.actor_user_id` + `actor_role` + `created_at` (charter §3.1 audit trail) | §3.1 (explicit operational state transitions) | **Implemented in v1** — the audit trail exists but is not yet exposed as a queryable surface |
| Provenance | (LE31 v1 does not have a `source` field on `audit_logs` rows) | (future v2 surface) | **Not implemented** — would require a new `source` field on `audit_logs` |
| Explainability | (LE31 v1 does not have a `derivation_chain` field on `audit_logs` rows) | (future v2 surface) | **Not implemented** — would require a new `derivation_chain` field on `audit_logs` |
| Structured symbolic reasoning | (LE31 v1 does not have symbolic reasoning) | (future v2-AI surface) | **Not implemented** — would require a new AI-assisted feature |

**What factgraph does NOT transfer:**
- The repo is a 13 KB description + a Python codebase; the *symbolic-reasoning* substrate may be over-engineered for a small restaurant's AI assistance. The codebase is not adoptable.
- The author is a *new maintainer* (created recently; in-window push 2026-09-08; 1★/0⑂ traction). The 1-day-old repo is *not* production-traction evidence.
- The "structured symbolic reasoning" discipline is a *symbolic AI* discipline (rule-based reasoning, logic programming, constraint satisfaction); LE31 v1's future v2-AI surface might use a *neural AI* discipline (LLM-based assistance) instead. The *auditability+provenance+explainability vocabulary* is portable; the *symbolic-reasoning implementation* is not.

**Cross-section with prior picks:**
- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. Factgraph's *append-only fact ledger* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Factgraph's *auditability* is the *queryable audit trail*; feature 122 supplies the query-time measurement.
- **Feature 125 auditable-continual-learning-three-axis** — the *commit-time gate* axis. Factgraph's *auditability+provenance+explainability* is the *commit-time gate*; feature 125's *auditable continual learning* is the AI-discipline analog.
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Factgraph's *append-only fact ledger* is the ledger; feature 127's *proposal-then-action* is the action the ledger authorizes.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Factgraph's *explainability* is the *explanation-time primitive* (how was this fact derived from which other facts?); feature 129's *graph* is the *typed edges* that make the explanation queryable.
- **Feature 133 hansard-runtime-witnessing** — the *who witnessed* axis. Factgraph's *auditability* is the *commit-time witness*; feature 133 supplies the runtime witness.
- **Feature 134 echo-record-shape** — the *record shape* axis. Factgraph's *append-only fact ledger* is the *commit*; feature 134 is the *record shape* of the commit.
- **Feature 135 dreamledger-execution-settled-credit-ledger** — the *credit ledger* dual. Factgraph's *append-only fact ledger* is the *fact ledger*; feature 135 is the *credit ledger* for AI agent actions.
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* axis. Factgraph's *append-only fact ledger* is the *commit*; feature 137's obligations would be *compiled into* the ledger.
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Factgraph is the *informal* statement of feature 138's 9-node model.
- **Feature 139 stale-constraints-budgeted-verification-failures** — the *stale-constraint* problem. Factgraph's *append-only fact ledger* is the *record*; feature 139's verification budget is the resource.
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Factgraph's *append-only fact ledger* is the *record*; feature 141's invariants are the *proof*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** — the *frozen mandate* primitive. Factgraph's *append-only fact ledger* is the *commit*; the mandate is what the production-run holds fixed.
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** — the *JTBD framing*. Factgraph is the *symbolic-reasoning JTBD*; feature 146 is the *bookkeeping JTBD*.
- **Feature 147 reliability-lives-in-institution-not-cognition-2609-03192v1** — the *experimental test* of the architecture. Factgraph is the *informal* statement; feature 147 is the *experimental* test (preregistered refutations of the five properties).
- **Feature 148 coxswain-graphs-harness-owns-consequence-architecture-pattern** — the *one harness owns every consequence* pattern. Factgraph's *append-only fact ledger* is the *commit*; feature 148's *one harness* is the *one place where consequence is owned*.
- **Feature 149 personal-agent-blueprint-telegram-chokepoint-architecture-pattern** — the *authorization chokepoint* pattern. Factgraph's *append-only fact ledger* is the *commit*; feature 149's *chokepoint* is the *enforcement of the authorization*.
- **Feature 153 sausageos-production-erp-append-only-stock-fefo-versioned-recipes** — the *manufacturing-stock discipline*. Factgraph is the *symbolic-reasoning discipline*; feature 153 is the *production-ERP pattern*.
- **Feature 154 chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive** — the *cryptographic-verifiability primitive*. Factgraph is the *auditability vocabulary*; feature 154 is the *cryptographic anchoring*.
- **Feature 155 ha-filament-ledger-end-user-deployable-append-only-integration-pattern** — the *end-user deployable integration pattern*. Factgraph is the *symbolic-reasoning substrate*; feature 155 is the *end-user deployable integration*.
- **Feature 156 awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent** — the *every-act-cites-the-rule* primitive. Factgraph's *auditability* is the *audit trail*; feature 156 is the *rule-citation primitive*.
- **Feature 157 talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel** — the *deterministic permission kernel*. Factgraph's *provenance* is the *source-tracking primitive*; feature 157 is the *deterministic permission kernel*.
- **Feature 158 azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory** — the *in-domain restaurant-POS+KDS+inventory integration*. Factgraph is the *append-only fact ledger*; feature 158 is the *integrated restaurant system*.
- **Feature 159 ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment** — the *production deployment topology*. Factgraph is the *vocabulary*; feature 159 is the *deployment topology*.

The 26 picks (this one + 25 prior) form the **deepest single-vocabulary cluster in the 41-pass series** for the *append-only-ledger + AI-discipline + audit-trail* architectural pattern. **All 26 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The auditability+provenance+explainability vocabulary is a future v2-AI surface and would require:
- A new `source` field on `audit_logs` (for provenance).
- A new `derivation_chain` field on `audit_logs` (for explainability).
- A new `ai_assistance_log` table that records each AI-assisted suggestion + the operator's accept/reject decision (for auditability).

None of these are v1; all are v2-AI surfaces that would require an *owner decision* per charter §3.2 and §3.4.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the factgraph auditability+provenance+explainability vocabulary to `specs/2026-09-09-factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai-HANDOFF.md`** as a named vocabulary for any future v2-AI surface — already done in the HANDOFF.md.
2. **Wait for the first v2-AI surface that consults `audit_logs`** — trigger conditions: (a) first v2-AI PR that adds an AI-assisted suggestion (menu suggestion, prep-time forecast, owner recap); (b) first v2-AI PR that adds an `ai_assistance_log` table; (c) first v2-AI PR that adds a `source` or `derivation_chain` field to `audit_logs`.
3. **On trigger, evaluate the change against the factgraph vocabulary** — does the change satisfy *auditability* (every AI suggestion has a queryable trail)? Does the change satisfy *provenance* (every AI suggestion has a source)? Does the change satisfy *explainability* (every AI suggestion has a derivation chain)? Does the change have a non-AI fallback per charter §3.4? The vocabulary is the *what to verify*, not the *what to implement*.
4. **Future v2-AI surface (NOT v1)**: the auditability+provenance+explainability vocabulary is a candidate v2-AI surface. Owner decision required: which v2-AI feature (menu suggestion, prep-time forecast, owner recap) should be added first? Each is a separate owner decision per charter §3.2 and §3.4.

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2-AI surface** (if the owner decides to add an AI-assisted feature) would: (a) add an `ai_assistance_log` table that records each AI suggestion + operator's accept/reject; (b) modify the cook Telegram bot or owner recap to expose the AI suggestion + the auditability trail; (c) provide a non-AI fallback for every AI suggestion per charter §3.4. This is a *v2-AI surface*, not v1.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2-AI dependencies** (if auditability+provenance+explainability are adopted): schema changes on `audit_logs`; new `ai_assistance_log` table; possible new operational transitions. All future; no v1 dependency.

## Open questions

1. **Which v2-AI feature should LE31 add first?** Owner decision required. Options: menu suggestion (LLM suggests menu items based on stock), prep-time forecast (LLM predicts prep time based on stock + history), owner recap (LLM generates daily/weekly recap for owner). Each is a separate charter §3.2 + §3.4 decision. Recommend: owner recap first (lowest risk, highest owner value, simplest auditability trail).
2. **Is the factgraph symbolic-reasoning substrate a blocking factor?** The *auditability+provenance+explainability vocabulary* is portable; the *symbolic-reasoning implementation* is not (it uses rule-based reasoning, logic programming, constraint satisfaction; LE31 might use LLM-based reasoning instead). The vocabulary is transferable; the codebase is not adoptable.
3. **Is the factgraph 1-day-old 1★/0⑂ repo a credible production-traction data point?** Charter §3.2: stars are popularity proxy, not gate. The *vocabulary* is the value, not the maintainer's track record. The 13 KB description is substantial; the *auditability+provenance+explainability* discipline is named clearly. **The vocabulary is transferable; the codebase is not adoptable**.
4. **Should the LE31 v1 audit_logs gain a `source` field today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant does not need a `source` field on every audit log row (the audit trail is sufficient); the v2-AI surface that needs to track AI suggestions needs a `source` field. Recommend: defer to v2-AI if/when the owner asks for AI assistance.

## Why this matters

**Factgraph is the only in-window ≥1★ Python repo with the auditability+provenance+explainability vocabulary today.** The 13 KB README is the tightest single-paragraph AI-discipline statement of the series; the 1-day-old 1★ repo is a new maintainer's first attempt at the pattern. The vocabulary maps 1:1 onto LE31 charter §3.4 (AI with observable evidence and a non-AI fallback).

**The cluster (26 picks, this one + 25 prior) is the persistent cross-section reference for the next v2-AI architecture-review moment.** All 26 are `defer`; no code change today. The cluster is the *what the LE31 v2-AI architecture is*, named across 26 different sources, and ready to be referenced when the first v2-AI surface lands.

**The most operationally valuable future v2-AI surface is owner recap**: introducing an LLM-based daily/weekly recap for the owner (with auditability+provenance+explainability) would close the *owner-recap gap* (today, the owner must read the `audit_logs` manually). Owner decision required; not v1.
