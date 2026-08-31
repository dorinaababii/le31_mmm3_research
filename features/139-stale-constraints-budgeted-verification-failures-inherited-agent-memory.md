# Feature 139 — Stale-Constraints budgeted verification failures in inherited agent memory (defer)

> **NEW observation (2026-08-30).** Documents in-window OpenAlex paper `W7204257200` / DOI `10.5281/zenodo.22147784` *When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory* (v3, Zenodo, 2026-08-28, Nakayashiki) from the 2026-08-30 daily-brainstorm pass. The paper studies a six-memory scenario where 16 language models had a verification budget of two records and a constraint that had been **superseded** by a later record. Result: stale-consistent decisions in **77.3% / 74.7% / 74.7%** of episodes across a primary run, a replication and a held-out domain. A target-blind rule *"prefer memories that state a limit on a candidate direction"* recovered **+89.3 points** accuracy. Bucket: **v2 owner-pains (architecture reference + empirical evidence)** — watch-list defer. Zero build time today.

## Goal

Retain the **verification-budget finding + the shape-of-row lesson** as the empirical evidence for the next time LE31 proposes a v2 surface where the operator is asked to re-verify a record (e.g., a v2 owner-facing history surface for `Visit`, `Bill`, or `Shift`). The empirical claim is that **the operational verification budget is the binding constraint, not the audit trail's reachability** — even when every `StockEntry` is reachable, an operator (or an LLM) will not click through every record; the **shape** of the row determines whether the constraint stands out at look-up time.

The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the paper's empirical finding (stale-consistent decisions in ~75% of episodes; +89.3 points with a target-blind rule).
- A decision record: today's verdict is `defer` because LE31 v1 doesn't ask operators to verify provenance; the value of this paper today is *evidence that the shape of the appended row matters*, not *implementation*.
- A reference for the next time LE31 proposes a v2 surface where the operator (or an LLM assistant) is asked to re-verify a record.
- The transferable lesson: **the shape of the appended row matters; the operational verification budget is the binding constraint, not the audit-trail reachability.**

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema today.
- Any change to the `audit_logs` schema today.
- Any "auto-reverify" surface — LE31 v1 doesn't ask operators to re-verify.
- Replication of the 6-memory × 16-LLM experimental design — out-of-scope for LE31.

## Description

OpenAlex `W7204257200` / Zenodo `10.5281/zenodo.22147784` (v3, Nakayashiki, 2026-08-28) studies the **verification budget** for agents with inherited memory. The setup:

- A consolidated memory that states a **decision constraint** (e.g., *"this item is restricted"*).
- A source record that has since been **superseded** by a record that **withdraws** the constraint.
- An agent with a **verification budget of 2 records** (i.e., it can inspect at most 2 links before deciding).
- 16 language models tested in a six-memory scenario.

The finding: **agents rarely re-verified a constraint that read as settled** — they inspected the provenance path in about **one episode in five**, and produced **stale-consistent decisions** (decisions that match the now-withdrawn constraint) in:

- **77.3%** of episodes in the primary run,
- **74.7%** of episodes in a replication,
- **74.7%** of episodes in a held-out domain.

The paper then shows that **re-assigning one of the two budget slots to the critical path** removed most of the stale-consistent decisions:

- **+74.0 / +72.7 / +61.3** points (positive in every model),
- **+80.7** in a prospectively frozen interleaved replication with a repaired non-critical control,
- **+62.0** on a panel of 10 models from 9 organisations new to the study,
- **+73.3** on a corrected re-run of the held-out scenario.

The paper also identifies a **target-blind rule** that recovers the oracle contrast without experimenter knowledge of the critical path: *"prefer memories that state a limit on a candidate direction"*. With this rule applied, the agent's own allocation moves onto the critical path and recovers **+89.3 points** in a store where the constraint limits a tempting action.

The paper's verification is rigorous: four pre-registered experiments (A, B, X, C) all specified, frozen, hashed, committed, cryptographically timestamped (OpenTimestamps, 2026-08-25 23:05:06 UTC) before the first confirmatory model call. All 5,400 confirmatory episode files + frozen analysis outputs + sealed smoke-gate outputs are deposited at OSF (project `axsnm`). Self-found defects are disclosed in the paper's appendices.

**Cross-section with LE31**:

- **The transferable lesson is not "implement verification re-assignment"** — LE31 v1 doesn't ask operators to verify provenance.
- **The transferable lesson is "the shape of the appended row matters"**. A solo cook/owner checking stock at end-of-shift will not click through every `StockEntry` even if the link is right there — they will read whichever row catches their eye. A row that **states a limit on a candidate direction** ("remaining: ≤ 3 portions", "reorder by: Friday") out-performs a row with no such signal.
- **The paper is empirical evidence** for the design principle that *appending more metadata is not enough* — what matters is whether the row **stands out at look-up time**.
- This is **not a build pick** — LE31 v1 doesn't ask operators to re-verify. It is filed as the **first** empirical evidence in the 31-pass series that the `audit_logs` shape itself is a design surface, not a passive record.

**Cross-section with prior picks**:
- **Feature 121 Field-Tier Minimization** (2026-08-27) — *"what is committed is canonical even if later reclassified"*. This paper is the *operational-budget dual* of feature 121: feature 121 says the commitment persists; this paper says the commitment *stands out* only if its shape signals a limit.
- **Feature 122 Trace Integrity CAIT** (2026-08-27) — *"what is queried is the right answer"*. This paper is the *upstream* of feature 122's measurement: feature 122 measures the answer; this paper measures *whether the constraint gets read at all*.
- **Feature 129 LEDGER Claim-to-Evidence Trace Graphs** (2026-08-28) — LEDGER adds typed edges. This paper says typed edges are not enough either; the *budget* of the reader is the binding constraint.
- **Feature 137 NL-to-Executable-Obligations** (2026-08-29) — NL policies compiled to typed rules. This paper is the *complement*: even if the rule is compiled correctly, the operator (or the LLM) must still read it within the verification budget.

## Data model

No schema change today. The defer artifact documents that the future v2 surface that adopts this lesson would add **a "limit on a candidate direction" field** to the `StockEntry` row — e.g., a `candidates_blocked` text field that names the action(s) the row constrains. The shape signal ("this row blocks candidate action X") is the target-blind rule the paper validates.

## Implementation steps

None today (defer). When LE31 first proposes a v2 surface where the operator (or an LLM) is asked to re-verify a record:

1. **Re-run the LE31 feature gate** with this paper in hand.
2. **Identify which `StockEntry` shapes "state a limit on a candidate direction"**. For LE31 v1's `StockEntry` lifecycle, the candidate actions are: reorder, sell, write-off, transfer. The rows that *constrain* one of these actions are the ones the paper's target-blind rule would surface.
3. **Decide whether the shape signal is implicit** (the row's amount + item combination implicitly blocks reorder when amount ≤ threshold) **or explicit** (a new `candidates_blocked` field).
4. **Pilot on one shape signal first**. Do not add multiple shape signals at once.
5. **Measure the operational verification budget** — the paper uses 2 records; LE31's operator budget is unknown. The first step is to measure how many `StockEntry` rows the operator actually reads before making a decision (it is likely ≤ 3).

## Dependencies

- Charter §3.1 (append-only posture) — the shape signal must remain additive over `audit_logs` (no breaking changes to the row's append-only semantics).
- Charter §3.4 (no customer-facing AI) — surface is owner/staff, not diner.
- Feature 121 Field-Tier Minimization — companion: feature 121 says the commitment persists; this paper says the commitment stands out only if its shape signals a limit.
- Feature 122 Trace Integrity CAIT — companion: CAIT measures the answer; this paper measures whether the constraint gets read.
- Feature 129 LEDGER Claim-to-Evidence Trace Graphs — companion: LEDGER adds typed edges; this paper says typed edges are not enough; the budget is the binding constraint.
- Feature 137 NL-to-Executable-Obligations — companion: even with compiled rules, the operator's verification budget is the binding constraint.

## Open questions

- **What is LE31's operator verification budget?** The paper uses 2 records; LE31's operator budget is unknown. The first step is to measure how many rows the operator reads before deciding.
- **Should the shape signal be implicit or explicit?** Implicit = the row's amount + item combination implies a limit; explicit = a new `candidates_blocked` field. Explicit is more discoverable but adds a schema column; implicit is more discoverable to humans but requires interpretation.
- **Does the shape signal apply to v1's existing `StockEntry` rows?** LE31 v1 already has rows with `amount` + `item` — the implicit shape signal may already be present. The question is whether the operator reads it.
- **What is the cost of being wrong about the shape signal?** If the operator reads the wrong row, the consequence is a bad decision. The paper's empirical claim is that the target-blind rule *out-performs* uniform allocation, but it does not claim the target-blind rule is perfect — it claims +89.3 points, not 100 points.
- **Is the "limit on a candidate direction" framing universal?** LE31's natural candidates are: reorder, sell, write-off, transfer. Are there other candidates the v2 surface should consider?

## Why this matters

The paper provides LE31 with three things it does not currently have: (i) **empirical evidence** that append-only provenance is not enough — the shape of the row matters; (ii) **a target-blind rule** ("prefer memories that state a limit on a candidate direction") that recovers +89.3 points without experimenter knowledge of the critical path; (iii) **a quantified baseline** (~75% stale-consistent decisions even with full provenance) for what "operator re-verification" actually means in practice.

The cost of *not* filing this today is the risk that the first v2 surface that asks the operator to re-verify a record assumes the audit trail's reachability is sufficient — and then watches the operator skim the first row that catches their eye. Filed now so the v2 boundary has the empirical baseline when the surface is proposed.

**Fully reversible.** Filing as a defer artifact does not commit to any schema change or any v2 work.

**Disclosure note**: the paper's author disclosed AI assistance (Anthropic's Claude + OpenAI's ChatGPT) for design/execution tooling, with the 16 models studied as experimental subjects (not co-authors). Same epistemic posture as the HANSARD / ECHO picks (2026-08-29). The AI assistance is **disclosed in the paper's back matter**, and the data + code are deposited at OSF (project `axsnm`) with frozen analysis outputs. No fabrication concern; this is reproducible research.
