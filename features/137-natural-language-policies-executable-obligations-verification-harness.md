# Feature 137 — Natural-language policies → executable obligations verification-harness (defer)

> **NEW observation (2026-08-29).** Documents in-window arXiv paper `2608.23282v1` AgentGuardUtil / *"From Natural Language Policies to Executable Obligations: A Verification Harness for Dependable In-Car LLM Agents"* (2026-08-24, cs.SE) from the 2026-08-29 daily-brainstorm pass. The paper's core mechanism is **a runtime policy compiler that transforms the natural-language policy into typed machine-checkable rules, plus a deterministic obligation engine that interprets the rules against live state and emits remedial calls with computed arguments**. Bucket: **v2 owner-pains (architecture reference)** — watch-list defer. Zero build time today. **The transitive difference from features 121/122 is that this paper specifies the *policy-compilation step* — the transformation from natural-language rule to typed obligation — which neither feature 121 nor 122 covers.**

## Goal

Retain the **runtime policy compiler + deterministic obligation engine** mechanism as a design constraint for the first LE31 v2 surface that allows the owner to author an operational rule (e.g., "sold-out items must hide from the waiter view", "dishes with allergen X cannot be ordered after 21:00", "cash-only tables cannot be paid by card"). The mechanism answers: *how does the operator's prose rule become a typed machine-checkable obligation checked at commit time?*

The artifact is the persistent design reference. No code today.

**Honesty note**: the paper's *policy-as-input* posture is the **inverse of LE31 charter §3.1's *rules-as-code* posture**. The defer artifact surfaces the paper for v2 use only; it must not be confused with a charter change.

## Scope

**In scope (defer artifact):**
- A written record of the paper's mechanism (natural-language policy → typed machine-checkable rules → deterministic obligation engine → remedial calls with computed arguments).
- A decision record: today's verdict is `defer` because LE31 v1 has no owner-authored-rules surface (rules are hard-coded in the data model today), and the charter does not authorise v2 work that would expose such a surface.
- A reference for the next time LE31 considers a v2 surface that allows the owner to author rules without involving an engineer.

**Out of scope (defer artifact):**
- Any change to the existing rule-as-code data model (charter §3.1).
- Any owner-authored-rules surface today.
- Implementation of the paper's 25 deterministic gates (identifier provenance, schema/enum validity, gather-before-act, confirmation/future-time protocols) — the natural LE31 gates are domain-specific, not generic.
- Implementation of any LLM-critic layer (LE31 charter §3.4 forbids customer-facing AI; any owner-facing AI assistance must have a non-AI fallback).

## Description

arXiv `2608.23282v1` AgentGuardUtil — *"From Natural Language Policies to Executable Obligations: A Verification Harness for Dependable In-Car LLM Agents"* (CAR-bench Track 1 entry) — treats the LLM agent as a fallible proposer inside a grounded verify-and-revise loop. Its core novelty is a **runtime policy compiler**: the natural-language policy shipped with each conversation is compiled, once per policy, into typed machine-checkable rules, a subset of which receive an executable form. A **deterministic obligation engine** interprets these rules against live tool results and the simulated post-write state of the draft itself, emitting the exact remedial calls with computed arguments rather than natural-language reminders. Around this engine, 25 deterministic gates (identifier provenance, schema/enum validity, gather-before-act, confirmation/future-time protocols) and an LLM critic produce tiered findings that drive a bounded revision loop.

LE31 v1 has no owner-authored-rules surface — every operational rule is hard-coded in the data model (charter §3.1 explicit state transitions). Today's rules are:

- "Sold-out items cannot be ordered" — enforced by the `is_sold_out` flag on `MenuItem` + the order-creation validation.
- "Dishes with allergen X carry the allergen label" — enforced by the `MenuItem.allergens` field.
- "Cash-only tables cannot be paid by card" — enforced by the `PaymentMethod` enum on `Bill`.

The paper's mechanism would generalise these into a *compiled rule surface*: the owner writes `"sold-out items must hide from the waiter view"` and the runtime compiles it to `(MenuItem.is_sold_out=True → MenuItemDisplayVisibility=hidden-for-waiter)`. The cost is **two-fold**: the owner must learn to write rules the compiler can compile, and the compiler must reject ambiguous rules deterministically.

LE31 v1 has no such surface and the charter does not authorise it. The defer surfaces the pattern for the day when v2 first proposes a rule-authoring surface.

## Data model

No schema change today. The defer artifact documents that the future `PolicyRule` table — if built — would have columns `(rule_id, natural_language, typed_obligation_json, executable_form_json, applies_to_entity, recorded_at)` plus a deterministic obligation engine. The "applies_to_entity" column is the rabbit hole (see Implementation steps).

## Implementation steps

None today (defer). When LE31 first considers a v2 surface that allows the owner to author rules:

1. **Re-run the LE31 feature gate** with the AgentGuardUtil paper in hand. **Re-confirm charter §3.1** ("operational transitions are explicit user actions") before any rule-authoring surface is scoped.
2. **Decide whether the rule-authoring surface is in scope for charter §3.** The paper's *policy-as-input* posture is the inverse of charter §3.1's *rules-as-code* posture. Either (i) the rule-authoring surface is restricted to a *non-operational* subset (e.g., display-only rules, not state-transition rules), or (ii) the charter is amended to allow operator-authored state-transition rules with explicit deterministic obligation-engine checks. The defer does not pre-judge this; the owner decision is required.
3. **Define the LE31 rule taxonomy.** The paper's rules are in-car driving-domain rules (`gather-before-act`, `confirmation-protocol`, `future-time-protocol`); LE31's natural rules are domain-specific (visibility, allergens, payment-method restrictions). The mapping is the real cost.
4. **Decide the policy-compilation surface.** Single-shot per-rule compile (the paper's pattern) vs continuous compile (every owner edit triggers a re-compile). The paper compiles once per policy; LE31 may want continuous for a single-owner setting.
5. **Decide the deterministic obligation engine's host.** Inside the v2 surface or as middleware. The paper puts it inside the consumer; LE31 may prefer a middleware pattern so the obligation check is observable from outside the surface.
6. **Pilot on one rule class first.** Do not design the policy-compiler for all rule classes at once.

## Dependencies

- Charter §3.1 (explicit state transitions) — **the central tension**. Either the rule-authoring surface is restricted to non-operational rules, or the charter is amended.
- Charter §3.4 (no customer-facing AI; non-AI fallback required) — any LLM-critic layer must have a non-AI fallback.
- Feature 121 `ledger-commitment-field-tier-minimization` — adjacent: feature 121 says *what is committed is canonical*; this paper says *what the operator's prose rules mean*.
- Feature 122 `trace-integrity-cait-acceptance-criterion` — adjacent: feature 122 says *what is queried is the right answer*; this paper says *what the operator's prose rules mean*.
- Feature 133 `hansard-runtime-witnessing-ledger-architecture` — adjacent: HANSARD says *who acted*; this paper says *what rules the actor's action must satisfy*.

## Open questions

- **Whether the rule-authoring surface is in scope for charter §3.** The paper's *policy-as-input* posture conflicts with charter §3.1's *rules-as-code* posture.
- **What rule classes are appropriate for v2.** Visibility-only rules (low risk) vs state-transition rules (high risk) vs reconciliation rules (medium risk).
- **Who compiles the rules.** The owner (requires the owner to learn the compilation language), or an engineer (defeats the point), or an LLM with a deterministic-obligation-engine check (charter §3.4 tension).
- **Whether the deterministic obligation engine is observable to the owner.** LE31 charter §3.1 favours explicit state transitions; an automatic obligation check is implicit.

## Why this matters

The paper provides three things LE31 does not currently have: (i) **architectural vocabulary** for "natural-language policy → typed obligation → deterministic engine"; (ii) **the transitive difference from features 121/122** (those papers cover *what is committed* and *what is queried*; this paper covers *what the operator's prose rules mean*); (iii) **the charter-§3.1 tension as a documented design constraint** — the next time LE31 proposes a v2 rule-authoring surface, the tension must be resolved explicitly, not silently. The cost of *not* filing this today is the risk that the first v2 rule-authoring surface silently bypasses charter §3.1, or reinvents the policy-compilation step from scratch. Filed now so the v2 boundary has the vocabulary *and the tension* ready when the surface is proposed.