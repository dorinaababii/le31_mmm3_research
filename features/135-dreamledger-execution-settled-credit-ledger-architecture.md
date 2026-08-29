# Feature 135 — DreamLedger execution-settled credit-ledger architecture (defer)

> **NEW observation (2026-08-29).** Documents in-window arXiv paper `2608.23863v2` DreamLedger (2026-08-24, cs.RO) from the 2026-08-29 daily-brainstorm pass. The paper describes a **persistent reliability ledger + consult-before-use** primitive: an *execution-settled credit file* records how often consumed predictions are borne out, indexed by operating condition, region, and prediction horizon, and gates future consumption. Every reliance event is auditable via dependency tickets and replayable logs. Bucket: **v2 owner-pains (architecture reference)** — watch-list defer. Zero build time today.

## Goal

Retain the **execution-settled credit ledger** mechanism as a design constraint for the first LE31 v2 surface that exposes an "AI suggestion", an external signal, or any "next action" that the system could take or recommend. The mechanism answers: *how does the owner decide whether to trust a given signal-source under current conditions?*

The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the paper's mechanism (claim → settle → credit → gate; dependency tickets; replayable logs).
- A decision record: today's verdict is `defer` because LE31 v1 has no signal-source beyond operator input, and the charter does not authorise v2 work that would expose such a surface.
- A reference for the next time LE31 considers a v2 surface that ingests an external signal or an "AI suggestion" that the operator might choose to follow.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any user-facing credit-rail surface (no owner-facing "track record" view today).
- Any "AI suggestion" surface — LE31 v1 ships none.
- Implementation of the paper's robotic world-model conditions (`operating_condition × region × prediction_horizon`) — they are out-of-domain for LE31.

## Description

arXiv `2608.23863v2` DreamLedger — *"DreamLedger: Execution-Settled Credit Files for World-Model Imagination in Robot Decision Loops"* — proposes treating **reliability as a persistent deployment object** rather than an instantaneous model-internal signal. The mechanism has four parts:

1. **Claim** — each consumed prediction is registered as a claim (a small attestation: *what was predicted, by whom, under what conditions*).
2. **Settlement** — attributable outcomes are settled against arriving reality at zero labelling cost. An attribution stage excludes measurement-contaminated outcomes.
3. **Credit** — the resulting credit file records how often consumed predictions are borne out, indexed by operating condition, region, and prediction horizon.
4. **Gate** — before each new consumption, the credit file is consulted: low-credit predictions shorten the dependent horizon or trigger additional observation.

Every reliance event remains **auditable via dependency tickets and replayable logs**. The paper verifies the mechanism in three simulated domains (indoor flight, tabletop manipulation, 2D navigation) and on a real Franka manipulator: *Claim failure is dose-monotone in all 12 held-out condition-horizon cells. Credit-gated planning reduces burned imagination (consumed claims that later fail to redeem) by 62% (95% CI 43-81%) versus blind consumption, with equal success and comparable collision rates.*

LE31 v1 currently has no signal-source beyond operator input, so the credit-rail primitive is **a future v2 surface, not a v1 gap**. The paper's value for LE31 is therefore *naming* + *architectural vocabulary* + *the empirical claim that consult-before-use reduces failure rate by 62%*:

- **Naming** — when LE31 v2 considers any "AI suggestion" or external signal, the relevant question is *what is the credit ledger?* — not *what is the prediction?*.
- **Architectural vocabulary** — the `claim → settle → credit → gate` cycle is the **credit-ledger dual of LE31's append-only `StockEntry` ledger**. Where LE31 currently answers *"what is the current stock?"* by replaying `StockEntry` (a *structural* derivation), DreamLedger answers *"should I trust this next prediction?"* by replaying `claim → settlement` history (a *credibility* derivation). The shared primitive is **persistent reliability ledger + consult-before-use**, applied in different domains.
- **Empirical claim** — the 62% reduction in burned imagination is the strongest single-paper piece of evidence that *consult-before-use* is a measurable primitive, not a vague principle.

LE31 v1's `StockEntry` ledger does not need a credit-rail because v1 has no signal-source. The defer surfaces the pattern for the day when v2 first proposes an "AI suggestion" surface (e.g., a demand-forecast signal from feature 07 `demand-estimation`, or an external data feed from a POS-vendor API).

## Data model

No schema change today. The defer artifact documents that the future `ReliabilityLedger` table — if built — would have columns `(signal_kind, condition, outcome, claim_id, settlement_id, recorded_at)` and a consult-before-use helper. The "condition" column is the rabbit hole (see Implementation steps).

## Implementation steps

None today (defer). When LE31 first considers a v2 surface that exposes an "AI suggestion" or external signal:

1. **Re-run the LE31 feature gate** with the DreamLedger paper in hand.
2. **Define the "condition" taxonomy for LE31's natural conditions.** The paper's conditions are `operating-condition × region × horizon` for robots; LE31's natural conditions are `shift × daypart × menu-section`, which are much fewer and much more uniform than the paper's. The taxonomy design is the real cost.
3. **Decide whether `ReliabilityLedger` is a new table or a column on existing `audit_logs`.** A new table keeps the append-only `audit_logs` shape simple; a column on `audit_logs` makes the "credit" query trivial but couples two primitives that may evolve independently.
4. **Decide whether the consult-before-use helper is built into the v2 surface or a middleware.** The paper puts it inside the consumer; LE31 may prefer a middleware pattern so the consult-before-use is observable from outside the consumer.
5. **Pilot on one signal-source first.** Do not design the credit-rail for all signal-sources at once.

## Dependencies

- Charter §3.1 (append-only posture) — the credit-rail must remain additive over the existing `audit_logs`.
- Charter §3.4 (no customer-facing AI) — credit-rail surfaces are owner/staff, not diner.
- Feature 07 `demand-estimation` — first candidate signal-source.
- Feature 134 `echo-auditable-memory-plane-stockentry-audit` — companion: ECHO is about *records*, DreamLedger is about *signal reliability*.

## Open questions

- **What "condition" means in a single-restaurant setting.** LE31's conditions are `shift × daypart × menu-section`; the paper's are `operating-condition × region × horizon`. The taxonomy design is the real cost.
- **Who computes the credit.** The paper has the consumer compute it; LE31 may prefer a middleware.
- **What happens when a signal-source is replaced.** The credit file is per-signal-kind; if the signal-source changes, does the credit file reset? The paper does not address this directly.
- **Whether the consult-before-use helper should be visible to the operator.** LE31 charter §3.1 favours explicit state transitions; an automatic consult-before-use is implicit. Tension to surface at build time.

## Why this matters

The paper provides three things LE31 does not currently have: (i) **architectural vocabulary** for "reliability as a persistent deployment object"; (ii) **an empirical claim** (62% reduction in burned imagination) that consult-before-use is a measurable primitive, not a vague principle; (iii) **a dated reference** for the next time LE31 proposes a v2 surface that ingests an external signal. The cost of *not* filing this today is the risk that the first v2 surface that proposes an "AI suggestion" reinvents the credit-rail from scratch, or omits it entirely. Filed now so the v2 boundary has the vocabulary ready when the surface is proposed.