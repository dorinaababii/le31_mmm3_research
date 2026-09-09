# Feature 161 — claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema (defer)

> **NEW observation (2026-09-09).** Documents in-window GitHub repo `Ybx-jp/claims-ledger` (MIT, **0★/0⑂**, **pushed 2026-09-09T06:32:26Z** — in-window, ~2 minutes before fetch, 2 KB description). Description (verbatim): *"A checked claims ledger: entries that separate assertion, grounds, warrant and backing, hold every quotation to its source, and derive status from an append-only verdict list."* **The Toulmin-model schema (assertion/grounds/warrant/backing) + verdict-list derivation is the load-bearing primitive** for any audit trail that needs to separate the claim from its justification. Bucket: **v2 owner-pains architecture-reference** — watch-list defer. Zero build time today.

## Goal

Retain the **"checked claims ledger with assertion/grounds/warrant/backing schema + verdict-list derivation"** pattern as a persistent cross-section reference for the next v2 surface that introduces an owner-facing audit trail. The artifact is the persistent cross-section reference + a candidate *named schema* for the next v2 audit-trail surface. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **Toulmin-model schema**: every claim in the ledger is structured as `assertion` + `grounds` + `warrant` + `backing`. The four fields separate the claim from its justification.
- A written record of the **verdict-list derivation**: the *status* of each claim is derived from an append-only *verdict list*, not stored as a mutable field. This is the load-bearing derivation primitive (charter §3.1's "current stock is derived from entries" generalized to audit trails).
- A written record of the **"hold every quotation to its source"** discipline: every quotation in the ledger has a *source* field (where did this quotation come from?). This is the *provenance* discipline.
- A decision record: today's verdict is `defer` because the LE31 v1 codebase does not yet have an owner-facing audit trail; the Toulmin-model schema is a future v2 surface, not v1.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema (charter §3.1: append-only).
- Any change to the `StockEntry` schema (charter §3.1: append-only).
- Any new owner-facing audit trail (LE31 v1 does not have an owner-facing audit trail today; introducing one would require an owner decision per charter §3.2).
- Any new claims-ledger schema (LE31 v1 does not have a claims-ledger; introducing one would require a separate owner decision).
- Adoption of the claims-ledger code (the repo is a 2 KB description + a Python codebase; the *schema* is transferable; the *code* is not adoptable).

## Evidence / JTBD

When a future LE31 v2 owner-facing audit trail is introduced, the operator wants *a ready-made schema for separating claim from justification*, but struggles because *the audit trail today is a flat log*, so that *the v2 audit trail has a defensible schema*.

- **Evidence class**: observed (the claims-ledger README names the assertion/grounds/warrant/backing schema and the verdict-list derivation).
- **Confidence**: high for the schema match (assertion/grounds/warrant/backing is the standard Toulmin model for argument structure); high for the derivation match (the verdict-list derivation is the same pattern as charter §3.1's "current stock is derived from entries").
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 does not have an owner-facing audit trail.
- **The value is naming, not direct demand**: when the first v2 audit-trail surface lands, the claims-ledger schema is a ready-made *named* discipline.

## Description

GitHub `Ybx-jp/claims-ledger` (MIT, 0★/0⑂, pushed 2026-09-09T06:32:26Z — in-window, ~2 minutes before fetch, 2 KB description). Description (verbatim): *"A checked claims ledger: entries that separate assertion, grounds, warrant and backing, hold every quotation to its source, and derive status from an append-only verdict list."*

The architectural pattern has one core principle and a four-field schema:

1. **"Append-only verdict list"** — every status assignment is a new verdict row; current status is **derived** from the verdict list, never stored as a mutable field. This is the *derivation primitive* (charter §3.1's "current stock is derived from entries" generalized).
2. **Assertion** — the claim itself. *What is being claimed?* (e.g. "The cook prepared 3 portions of pasta at 14:32").
3. **Grounds** — the evidence for the claim. *What is the evidence?* (e.g. "Cook entered the prep in the Telegram bot at 14:32; the StockEntry row is in the `audit_logs` table").
4. **Warrant** — the reasoning that connects the grounds to the assertion. *Why does the grounds support the assertion?* (e.g. "The cook's Telegram entry is a direct observation; the StockEntry row is the system-of-record").
5. **Backing** — the source of the warrant's authority. *Why is the warrant authoritative?* (e.g. "Charter §3.1: the cook is the source-of-truth for prepped-item quantity changes; the StockEntry row is the system-of-record for the audit trail").
6. **"Hold every quotation to its source"** — every quotation in the ledger has a `source` field (where did this quotation come from?). This is the *provenance* discipline.

**The 1:1 mapping onto LE31 v1 architecture:**

| claims-ledger component | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| Append-only verdict list | (LE31 v1 does not have a verdict list; the `audit_logs` table is the closest analog) | §3.1 (current stock is derived from entries) | **Not implemented** — would require a new `verdict` table + derivation query |
| Assertion | `audit_logs.action` field (the action that was taken) | §3.1 (every operational transition is a new audit_logs row) | **Implemented in v1** — the action is recorded |
| Grounds | (LE31 v1 does not have a structured `grounds` field on `audit_logs` rows) | (future v2 surface) | **Not implemented** — would require a new `grounds` field on `audit_logs` |
| Warrant | (LE31 v1 does not have a structured `warrant` field on `audit_logs` rows) | (future v2 surface) | **Not implemented** — would require a new `warrant` field on `audit_logs` |
| Backing | (LE31 v1 does not have a structured `backing` field on `audit_logs` rows) | (future v2 surface) | **Not implemented** — would require a new `backing` field on `audit_logs` |
| Provenance | (LE31 v1 does not have a `source` field on `audit_logs` rows) | (future v2 surface) | **Not implemented** — would require a new `source` field on `audit_logs` |

**What claims-ledger does NOT transfer:**
- The repo is a 2 KB description + a Python codebase; the *Toulmin-model schema* is a philosophy-of-argument discipline (Stephen Toulmin, 1958); the codebase is not adoptable.
- The author is a *new maintainer* (created recently; in-window push 2026-09-09, ~2 minutes before fetch; 0★/0⑂ traction). The brand-new repo is *not* production-traction evidence.
- The "structured symbolic claims" discipline is a *philosophy-of-argument* discipline; LE31 v1's future v2 audit trail might use a simpler schema (just `action` + `actor` + `timestamp`). The *Toulmin-model schema* is portable; the *symbolic-claims implementation* is not.

**Cross-section with prior picks:**
- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. Claims-ledger's *append-only verdict list* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Claims-ledger's *append-only verdict list* is the queried record; feature 122 supplies the query-time measurement.
- **Feature 125 auditable-continual-learning-three-axis** — the *commit-time gate* axis. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *commit-time structure*; feature 125's *auditable continual learning* is the AI-discipline analog.
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Claims-ledger's *append-only verdict list* is the ledger; feature 127's *proposal-then-action* is the action the ledger authorizes.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *explanation-time structure*; feature 129's *graph* is the *typed edges* that make the explanation queryable.
- **Feature 133 hansard-runtime-witnessing** — the *who witnessed* axis. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *who-witnessed structure*; feature 133 supplies the runtime witness.
- **Feature 134 echo-record-shape** — the *record shape* axis. Claims-ledger's *append-only verdict list* is the *commit*; feature 134 is the *record shape* of the commit.
- **Feature 135 dreamledger-execution-settled-credit-ledger** — the *credit ledger* dual. Claims-ledger's *append-only verdict list* is the *fact ledger*; feature 135 is the *credit ledger* for AI agent actions.
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* axis. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *structured policy*; feature 137's obligations would be *compiled into* the schema.
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Claims-ledger is the *informal* statement of feature 138's 9-node model.
- **Feature 139 stale-constraints-budgeted-verification-failures** — the *stale-constraint* problem. Claims-ledger's *verdict-list derivation* is the *what the verification might miss* (a stale verdict in a non-derivation discipline is a stale constraint); feature 139's verification budget is the resource.
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Claims-ledger's *append-only verdict list* is the *record*; feature 141's invariants are the *proof*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** — the *frozen mandate* primitive. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *frozen mandate structure*; the mandate is what the production-run holds fixed.
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** — the *JTBD framing*. Claims-ledger is the *audit-trail JTBD*; feature 146 is the *bookkeeping JTBD*.
- **Feature 147 reliability-lives-in-institution-not-cognition-2609-03192v1** — the *experimental test* of the architecture. Claims-ledger is the *informal* statement; feature 147 is the *experimental* test (preregistered refutations of the five properties).
- **Feature 148 coxswain-graphs-harness-owns-consequence-architecture-pattern** — the *one harness owns every consequence* pattern. Claims-ledger's *append-only verdict list* is the *commit*; feature 148's *one harness* is the *one place where consequence is owned*.
- **Feature 149 personal-agent-blueprint-telegram-chokepoint-architecture-pattern** — the *authorization chokepoint* pattern. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *authorization structure*; feature 149's *chokepoint* is the *enforcement of the authorization*.
- **Feature 153 sausageos-production-erp-append-only-stock-fefo-versioned-recipes** — the *manufacturing-stock discipline*. Claims-ledger is the *audit-trail schema*; feature 153 is the *production-ERP pattern*.
- **Feature 154 chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive** — the *cryptographic-verifiability primitive*. Claims-ledger is the *schema*; feature 154 is the *cryptographic anchoring*.
- **Feature 155 ha-filament-ledger-end-user-deployable-append-only-integration-pattern** — the *end-user deployable integration pattern*. Claims-ledger is the *schema*; feature 155 is the *end-user deployable integration*.
- **Feature 156 awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent** — the *every-act-cites-the-rule* primitive. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *every-act-cites-the-rule structure*; feature 156 is the *rule-citation primitive*.
- **Feature 157 talos-kernel-talos-self-hosted-telegram-agent-deterministic-permission-kernel** — the *deterministic permission kernel*. Claims-ledger's *assertion/grounds/warrant/backing schema* is the *authorization structure*; feature 157 is the *deterministic permission kernel*.
- **Feature 158 azizsekerdil-smart-restaurant-management-system-ai-powered-pos-kds-inventory** — the *in-domain restaurant-POS+KDS+inventory integration*. Claims-ledger is the *schema*; feature 158 is the *integrated restaurant system*.
- **Feature 159 ledger-api-fastapi-postgresql-terraform-append-only-cloud-run-deployment** — the *production deployment topology*. Claims-ledger is the *schema*; feature 159 is the *deployment topology*.
- **Feature 160 factgraph-append-only-symbolic-reasoning-auditability-provenance-v2-ai** — the *auditability+provenance+explainability vocabulary*. Claims-ledger is the *schema*; feature 160 is the *vocabulary*.

The 26 picks (this one + 25 prior) form the **deepest single-vocabulary cluster in the 41-pass series** for the *append-only-ledger + audit-trail-schema + owner-pains* architectural pattern. **All 26 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The Toulmin-model schema is a future v2 owner-facing audit-trail surface and would require:
- A new `verdict` table that records each status assignment (the verdict list).
- New `grounds` + `warrant` + `backing` fields on `audit_logs` rows.
- A new `source` field on `audit_logs` rows (for provenance).
- A new derivation query that computes current status from the verdict list.

None of these are v1; all are v2 surfaces that would require an *owner decision* per charter §3.2.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the claims-ledger Toulmin-model schema to `specs/2026-09-09-claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema-HANDOFF.md`** as a named schema for any future v2 owner-facing audit-trail surface — already done in the HANDOFF.md.
2. **Wait for the first v2 surface that introduces an owner-facing audit trail** — trigger conditions: (a) first v2 PR that adds an owner-facing audit-trail surface; (b) first v2 PR that adds a `verdict` table; (c) first v2 PR that adds `grounds` + `warrant` + `backing` fields to `audit_logs`.
3. **On trigger, evaluate the change against the claims-ledger schema** — does the change preserve *append-only verdict list*? Does the change introduce the *assertion/grounds/warrant/backing schema*? Does the change add the *source field* for provenance? The schema is the *what to verify*, not the *what to implement*.
4. **Future v2 surface (NOT v1)**: the Toulmin-model schema is a candidate v2 owner-facing audit-trail surface. Owner decision required: which v2 surface (owner daily recap, owner audit-trail page, regulator-facing audit export) should be added first? Each is a separate owner decision per charter §3.2.

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2 surface** (if the owner decides to add an owner-facing audit trail) would: (a) add a `verdict` table that records each status assignment; (b) modify the `audit_logs` table to include `grounds` + `warrant` + `backing` fields; (c) modify the owner recap to expose the Toulmin-model schema. This is a *v2 surface*, not v1.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2 dependencies** (if Toulmin-model schema is adopted): schema changes on `audit_logs`; new `verdict` table; new derivation queries. All future; no v1 dependency.

## Open questions

1. **Which v2 surface should LE31 add first?** Owner decision required. Options: owner daily recap (Telegram push with Toulmin-structured audit trail), owner audit-trail page (web UI with Toulmin-structured audit trail), regulator-facing audit export (CSV/PDF export with Toulmin-structured audit trail). Each is a separate charter §3.2 decision. Recommend: owner daily recap first (lowest cost, highest owner value, simplest Toulmin structure).
2. **Is the claims-ledger Toulmin-model schema a blocking factor?** The *schema* is portable (assertion/grounds/warrant/backing is the standard Toulmin model); the *symbolic-claims implementation* is not. If LE31 ever needs the schema in code, it would be *re-implemented* on the LE31 stack (FastAPI + SQLModel + Postgres), not imported from claims-ledger.
3. **Is the claims-ledger brand-new 0★/0⑂ repo a credible production-traction data point?** Charter §3.2: stars are popularity proxy, not gate. The *schema* is the value, not the maintainer's track record. The 2 KB description is tight; the *Toulmin-model schema* is named clearly. **The schema is transferable; the codebase is not adoptable**.
4. **Should the LE31 v1 audit_logs gain `grounds` + `warrant` + `backing` fields today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant does not need structured grounds/warrant/backing fields (the audit trail is sufficient); the v2 surface that needs to expose the Toulmin-model schema needs these fields. Recommend: defer to v2 if/when the owner asks for an owner-facing audit trail.

## Why this matters

**Claims-ledger is the only in-window repo today with the Toulmin-model schema + verdict-list derivation pattern.** The 2 KB README is the tightest single-paragraph audit-trail-schema statement of the series; the brand-new 0★ repo is a new maintainer's first attempt at the pattern. The schema maps 1:1 onto LE31's future v2 owner-facing audit-trail surface.

**The cluster (26 picks, this one + 25 prior) is the persistent cross-section reference for the next v2 owner-pains audit-trail moment.** All 26 are `defer`; no code change today. The cluster is the *what the LE31 v2 owner-pains audit-trail architecture is*, named across 26 different sources, and ready to be referenced when the first v2 owner-facing audit-trail surface lands.

**The most operationally valuable future v2 surface is owner daily recap**: introducing a Telegram-based daily recap with Toulmin-structured audit trail (assertion/grounds/warrant/backing) would close the *owner-visibility gap* (today, the owner must read the `audit_logs` manually). Owner decision required; not v1.
