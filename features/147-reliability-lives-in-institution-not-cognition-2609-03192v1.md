# Feature 147 — reliability-lives-in-institution-not-cognition-2609-03192v1 (defer)

> **NEW observation (2026-09-07).** Documents in-window arXiv paper `2609.03192v1` Marsden, Collecutt, Marsden, **2026-09-02 22:21:02Z** (cs.MA, 31 pages, 5 figures): *Where Reliability Lives: Experimental Localisation of Behavioural Properties in an Agent System*. The paper built a system where "reliability claims about agentic systems implicitly locate each property somewhere: in the model, or in the machinery around it" and treated the location as an experimental question. The subject is a persistent simulated settlement whose *authoritative append-only ledger adjudicates every attempted act against world state; accepted history is the only reality*. Mind, institution and world were separated before any experiment. Holding cognition fixed, they intervened on the institution's epistemic mechanisms; preregistered experiments refuted the central prediction twice, in opposite directions. **Five pre-declared properties did not move in any tested trajectory** (verbatim): *"accepted reality stayed singular, invalid attempts were refused with typed reasons, duties outlived their processes, no work was accepted twice, and no false completion was ever accepted (2,581 substituted-panel claims, none false)."* Each property maps 1:1 onto an LE31 charter §3.1 invariant. **The paper is a preregistered *experimental* test of the architectural pattern LE31 has *asserted***. The **first** in the 39-pass series to do so. Bucket: **v2 owner-pains (architecture-reference)** — watch-list defer. Zero build time today.

## Goal

Retain the **"reliability lives in the institution, not the cognition"** architectural finding — and the **five pre-declared properties that survive all interventions** — as a persistent cross-section reference for the next v2 surface that proposes a change to LE31's `audit_logs` discipline or operational-transition machinery. The artifact is the persistent cross-section reference + a candidate **verification protocol** for the next v2 surface to use. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the paper's five pre-declared properties and their 1:1 mapping to LE31's operational invariants.
- A written record of the paper's *intervention protocol* (hold cognition fixed, intervene on the institution) as a candidate verification pattern for any future v2 change.
- A decision record: today's verdict is `defer` because no v2 surface that would use this verification pattern exists yet.
- A cross-section reference with prior picks: features 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `audit_logs` schema.
- Any change to the operational-transition machinery.
- Any AI integration (the paper's subject is a simulated settlement, not a restaurant).
- Any verification harness or property-based-test tooling (the paper's intervention protocol is documented for human review, not automated test execution).

## Evidence / JTBD

When a future LE31 v2 surface changes the `audit_logs` discipline (e.g. feature 121 field-tier minimization, feature 68 demand-estimation, feature 138 institutional-continuity model), the owner/waiter/cook wants *to verify the operational invariants still hold*, but struggles because *the current verification is test-only (per §3.4)*, so that *the v2 change is verifiably non-breaking*.

- **Evidence class**: observed (the paper is a peer-registered experimental test, not a low-star repo or a vendor blog post). The five properties did not move in any tested trajectory in 2,581 substituted-panel claims with **zero false completions accepted**.
- **Confidence**: high for the paper's experimental design (preregistered refutations, dual interventions, falsifier); medium-high for the *transferability* of the architectural pattern to LE31 (the paper tests an agent in a simulated settlement, not a restaurant waiter; the *property names* map but the *property content* is the LE31 invariant, not the paper's settlement rules).
- **Real observed LE31 JTBD**: none directly; LE31 v1 has no v2 surface that changes the audit discipline; v1's test coverage is the only verification path today.
- **The value is architectural validation**, not direct demand: when a v2 surface *is* proposed, the paper's five pre-declared properties are a ready-made invariant checklist.

## Description

arXiv `2609.03192v1` Marsden, Collecutt, Marsden 2026-09-02 22:21:02Z (cs.MA) — *Where Reliability Lives: Experimental Localisation of Behavioural Properties in an Agent System*. 31 pages, 5 figures, "Ancillary files: related-work search appendix, artefact manifest, verification receipts".

The paper's central question (verbatim): "Reliability claims about agentic systems implicitly locate each property somewhere: in the model, or in the machinery around it." The subject is "a persistent simulated settlement whose authoritative append-only ledger adjudicates every attempted act against world state; accepted history is the only reality." Mind, institution and world were separated before any experiment.

**Five pre-declared properties (verbatim, did not move in any tested trajectory):**

1. *"accepted reality stayed singular"* — at most one version of the world is real; rejected attempts do not produce a competing reality.
2. *"invalid attempts were refused with typed reasons"* — the institution (the ledger) refuses attempts with explicit typed reasons; the reason is part of the refused-attempt event.
3. *"duties outlived their processes"* — duties (a kind of state) outlive the processes that performed them; if a process dies mid-duty, the duty is still recordable.
4. *"no work was accepted twice"* — duplicate attempts are refused by the institution; acceptance is at-most-once.
5. *"no false completion was ever accepted (2,581 substituted-panel claims, none false)"* — completion requires more than a claim; the institution has an independent acceptance test.

**The 1:1 mapping onto LE31 charter §3.1:**

| Paper property | LE31 invariant | Charter section |
|---|---|---|
| accepted-reality-stay-singular | `audit_logs` per mutation + derived-state discipline | §3.1 (Stock: every prepared-item quantity change is a new `StockEntry`. Never update or delete ledger events. Current stock is derived from entries.) |
| invalid-attempts-refused-with-typed-reasons | explicit operational transitions (do not silently send, serve, close, or reconcile an order) | §3.1 (State: operational transitions are explicit user actions.) |
| duties-outlived-processes | audit-trail over operational events; events persist independent of the request lifecycle | §3.1 + §3.3 |
| no-work-accepted-twice | `Order.id` uniqueness + `Bill` derivation (a Bill is derived from order line items, not a separate mutable record) | §3.1 (Money: never use binary floats. Preserve exact EUR values and explicit tax/tip derivations.) |
| no-false-completion-accepted | explicit-close requirement (shift close is a discrete user action with a recorded variance) | §3.1 (State: operational transitions are explicit user actions.) |

**The intervention protocol:**

The paper holds **cognition fixed** (the agent's "mind" — its decision-making logic) and intervenes on the **institution** (the append-only ledger + adjudication rules). The transferability to LE31 is: for any v2 surface that proposes a change to the `audit_logs` discipline, the verification protocol is to hold the *operational* cognition (the waiter's order-taking flow, the cook's confirmation flow) fixed and intervene on the *institutional* layer (the `audit_logs` schema, the `StockEntry` event types, the `Bill` derivation logic). The five properties are the invariant checklist.

**The falsifier and the negative result:**

> "preregistered experiments refuted our central prediction twice, in opposite directions"

The paper's central prediction was that intervening on the institution would change the *measurable* behavioural properties. The prediction was refuted twice — the five properties survived *both* interventions. This is a **negative result** that is a **credibility signal** (the paper is willing to publish the falsifier, which is the gold standard in experimental science). The "designed world, not a population of institutions" caveat is acknowledged; the paper's claim is limited to this setting.

**Cross-section with prior picks:**

- **Feature 121 ledger-commitment-field-tier-minimization** (2026-08-27) — the *what is committed* axis. The 2609.03192 paper's *accepted-reality-stayed-singular* property is the LE31 §3.1 *current stock is derived from entries* invariant; feature 121's *canonical digest of the full, unminimized parameters* is the *commitment* that makes accepted-reality-singular verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** (2026-08-27) — the *what is queried* axis. The 2609.03192 paper's *no-false-completion* property is what CAIT measures; feature 122 supplies the measurement, the paper supplies the invariant.
- **Feature 125 auditable-continual-learning-three-axis** (2026-08-29) — the *commit-time gate* axis. The 2609.03192 paper's intervention protocol is the *what to do at commit time* recipe.
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** (2026-08-29) — the *operational mode of ledger-based control*. The 2609.03192 paper's "institution" is the ledger; feature 127's *proposal-then-action* primitive is the *action* the institution adjudicates.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** (2026-08-28) — the *explanation-time* axis. The 2609.03192 paper's *duties-outlived-processes* property is what a claim-to-evidence graph would *show*: the duty continues after the process is gone.
- **Feature 133 hansard-runtime-witnessing** (2026-08-29) — the *who witnessed* axis. The 2609.03192 paper's *invalid-attempts-refused-with-typed-reasons* property requires a *witness*; feature 133 supplies the witness.
- **Feature 134 echo-record-shape** (2026-08-29) — the *record shape* axis. The 2609.03192 paper's append-only-ledger record shape is the same *commit* primitive.
- **Feature 135 dreamledger-execution-settled-credit-ledger** (2026-08-29) — the *credit ledger dual*. The 2609.03192 paper's append-only ledger is the *state ledger*; dreamledger is the *credit ledger* (record-shape primitive companion).
- **Feature 137 natural-language-policies-executable-obligations** (2026-08-29) — the *policy compilation* axis. The 2609.03192 paper's intervention protocol would *test* whether a feature 137-derived obligation is institutionally compatible.
- **Feature 138 institutional-continuity-infrastructure-formal-model** (2026-08-30) — the *formal model* of institutional continuity. The 2609.03192 paper is the *experimental* test of one of the 8 joins in feature 138's 9-node continuity model.
- **Feature 139 stale-constraints-budgeted-verification-failures** (2026-08-30) — the *stale-constraint* problem. The 2609.03192 paper's *duties-outlived-processes* property is the *opposite* of a stale constraint: a duty that *outlives* its process is *not* a stale constraint; the *verification budget* in feature 139 is the *resource* that the 2609.03192 paper's intervention protocol consumes.
- **Feature 141 krineia-five-invariants** (2026-09-04) — the *proof/record distinction*. The 2609.03192 paper's *accepted-reality-stayed-singular* property is the LE31 §3.1 *proof-of-record* invariant; feature 141's `trust-root separation` is the *why*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** (2026-09-05) — the *frozen mandate* primitive. The 2609.03192 paper's "Mind, institution and world were separated before any experiment" is the *experimental* instantiation of the frozen-mandate discipline: the institution is fixed by construction.
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** (2026-09-05) — the *JTBD framing*. The 2609.03192 paper's five properties are the *test* that a slashbooks-style "replace outsourced bookkeeper" surface would need to pass; the JTBD validation in feature 146 is upstream of this test.

The 14 picks (this one + 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146) form the **deepest single-vocabulary cluster in the 39-pass series** for the *append-only-ledger + institution-cognition-separation* architectural pattern. **All 14 are `defer`; no code change today; the cluster is the persistent cross-section reference for the next v2 surface that proposes a change to the audit discipline.**

**What the paper does NOT transfer:**

- The paper's "subject is a persistent simulated settlement" — not a restaurant.
- The paper's "1,000 yen / 2,581 substituted-panel claims" — not a real budget, not a real order count.
- The paper's "One designed world, not a population of institutions; no test of an agent optimising against the institution" — the paper's claim is limited; the LE31 transferability inherits this limit (one restaurant, not a population).
- The paper's "Ancillary files: related-work search appendix, artefact manifest, verification receipts" — the *verifier* is in the paper's ancillary files, not the main text; a future v2 implementation would need to either re-implement the verifier or read the ancillary files (full text unread today).

## Data model

**No data model change.** The defer artifact is documentation only.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference + the candidate verification protocol:

1. **Read the paper's full text** (31 pages, 5 figures, ancillary files) — owner decision required to read the verifier implementation; **not a v1 surface**.
2. **Add the five pre-declared properties to `specs/2026-09-07-reliability-lives-in-institution-not-cognition-2609-03192v1-HANDOFF.md`** as a candidate invariant checklist — already done in the HANDOFF.md.
3. **Wait for the first v2 surface that proposes a change to the `audit_logs` discipline** — trigger condition: first v2 PR that adds a new `audit_logs` event type, a new `StockEntry` source, or a new operational transition.
4. **On trigger, run the paper's intervention protocol** — hold operational cognition fixed, intervene on the institutional layer, verify the five properties do not move. This is the v2 verification path, not v1.

## Telegram interaction if any

**None.** The defer artifact is documentation only; no operator surface changes.

## Dependencies

- **arXiv access** — public, no dependency.
- **Paper's ancillary files** — public, but full text unread today; future v2 work would need to read them.
- **No LE31 code dependency** — defer artifact is documentation only.

## Open questions

1. **Who would ever run the offline verifier?** (Same as feature 121's open question.) The owner is the only stakeholder; an "institutional conformance test" is over-engineered for a single-restaurant operation. The paper's 2,581 substituted-panel claims correspond to *acceptance attempts in a simulated settlement*; the analogous LE31 v2 surface would be *order-acceptance attempts at a real restaurant*, which are bounded by daily volume (~50-200 orders/day, vs. the paper's 2,581 in an experimental run).
2. **Is the intervention protocol transferable to LE31's operational transitions?** (Same as feature 125, 138.) The paper's "hold cognition fixed" is a controlled experiment; the LE31 v2 surface would be a *retrospective audit* (a change is rolled out, the audit logs are inspected post-hoc to verify the five properties held). The paper's protocol is *prospective*; LE31's would be *retrospective*. The five properties are invariant; the protocol is the open question.
3. **Should the five properties be added to the LE31 charter §3.1 explicitly?** Owner decision required. The five properties are *implied* by the existing §3.1 wording (append-only, derived state, explicit transitions); making them *explicit* is a documentation change, not a code change. Recommend: no, the §3.1 wording is already canonical; adding the five properties is *redundant*.

## Why this matters

**The paper is the first in the 39-pass series to *experimentally* test the architectural pattern LE31 has *asserted*.** Prior picks (features 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146) were *proposals*, *models*, or *case studies*; this paper is the first to *intervene* and *measure*. The five pre-declared properties that survived *both* interventions are a **ready-made invariant checklist** for any future v2 surface that proposes a change to the audit discipline. The negative result (the central prediction was refuted) is a **credibility signal**: the paper is willing to publish the falsifier, which is the gold standard in experimental science.

**The cluster (this paper + 13 prior picks) is the deepest single-vocabulary cluster in the 39-pass series.** When the first v2 surface that proposes a change to the audit discipline lands, this cluster is the *ready-made* cross-section reference. Today, the cluster is observational; tomorrow, it is the verification protocol.
