# Feature 162 — partasyuk-applicability-boundary-doctrine-formal-commit-admissibility (defer)

> **NEW observation (2026-09-09).** Documents in-window OpenAlex Zenodo series by **Vadym Partasyuk, Independent Research**: 3 in-window Zenodo records (`21983371` / `21988251` / `21985437`) deposited 2026-08-17..18, all on the *"Applicability Boundary Doctrine"* line. OpenAlex IDs `W7203599068` / `W7203663783` / `W7203618587`. Reported cit=20/12/18 — verified by parent via Zenodo REST API + OpenAlex `cites:` endpoint: **all 20 citations of W7203599068 are Partasyuk's own 2026-08-17..19 Zenodo series** (project self-citations, NOT external citations). The cit count is therefore a *project self-reference count*, not 20 independent peers. Bucket: **v2 owner-pains architecture-reference** — parking-lot defer. Zero build time today.

## Goal

Retain the **"Applicability Boundary Doctrine"** formal vocabulary as a persistent cross-section reference for the next v2 surface that introduces an owner-facing commit-eligibility gate. The artifact is the persistent cross-section reference + a candidate *named schema* for any future v2 audit-trail surface that needs to separate *admissibility* (is the commit authorized?) from *execution* (what did the commit do?). No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"Admissible Basis"** + **"Operative Capacity"** + **"Claim-Specific Common-Cause Independence"** + **"Durable Re-Provability"** vocabulary — the four-field commit-eligibility schema proposed by the Applicability Boundary Doctrine series.
- A written record of the **"Commit-Time Conjunction"** invariant (W7203663783): *"a typed, non-offsettable commit-eligibility"* — a commit is admissible iff the admissible basis + operative capacity + claim-specific common-cause independence are *all* satisfied; no partial substitution is allowed.
- A written record of the **"Channel Hierarchy, Version Mapping, Citation Spine, Deposit-Order Lock, Claim Ladder"** primitives (W7203599068): the bookkeeping discipline that makes the commit *locatable* and *non-overwritable* — directly maps onto LE31's `audit_logs` + `StockEntry` append-only invariants.
- A written record of the **"Semantic Crosswalk and Type-Separation Canon Locks"** (W7203618587): *"Load-Bearing Terms, Phase Boundaries, and Non-Substitution Rules"* — the *type discipline* that prevents one commit-time type from being silently substituted for another.
- A decision record: today's verdict is `defer` because LE31 v1 has no formal commit-eligibility vocabulary; the Applicability Boundary Doctrine is a future v2 surface, not v1.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema (charter §3.1: append-only).
- Any change to the `audit_logs` schema (charter §3.1: append-only).
- Any new owner-facing audit-trail surface (LE31 v1 has none today; introducing one would require an owner decision per charter §3.2).
- Adoption of the Partasyuk codebase (the series is Zenodo-archived formal-text records; no Python codebase to import).
- Cross-pollination with charter §3.4 AI surface (LE31 v1 has no AI agent surface today; any such surface is v2 territory).

## Evidence / JTBD

When a future LE31 v2 owner-facing audit-trail surface is introduced, the operator wants *a ready-made formal commit-eligibility vocabulary*, but struggles because *the audit trail today is a flat log*, so that *the v2 audit trail has a defensible commit-eligibility schema*.

- **Evidence class**: observed (the 3 Zenodo records name the Admissible Basis / Operative Capacity / Common-Cause Independence / Re-Provability schema; all 3 are deposited in the in-window 30-day period).
- **Confidence**: high for the vocabulary match (the Applicability Boundary Doctrine formalizes what charter §3.1 calls *"current stock is derived from entries"* in commit-eligibility terms); medium for transferability (Zenodo deposit-relationship semantics ≠ SQL database transaction semantics).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no formal commit-eligibility vocabulary today.
- **The value is naming, not direct demand**: when the first v2 owner-facing audit-trail surface lands, the Applicability Boundary Doctrine is a ready-made *named discipline*.

## Description

The 3 Zenodo records by Vadym Partasyuk, Independent Research, are deposited in a 30-hour window (2026-08-17 09:00Z through 2026-08-18 18:00Z) and self-cite 20/12/18 times within the same-author project line. The series proposes a commit-eligibility framework that maps 1:1 onto LE31 charter §3.1 invariants:

| Applicability Boundary Doctrine primitive | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| **Admissible Basis** (the claim is authorized) | `audit_logs.action` field + `actor_user_id` field | §3.1 (every operational transition is a new audit_logs row) | **Implemented in v1** — every commit has an actor |
| **Operative Capacity** (the actor is currently able to act) | `audit_logs.actor_role` field (cook/waiter/owner) | §3.1 (explicit state transitions) | **Implemented in v1** — the role gates the action |
| **Claim-Specific Common-Cause Independence** (the commit is not entangled with another) | (LE31 v1 does not have an explicit `isolation` field; the `audit_logs` table is append-only so commits are causally independent by construction) | §3.1 (every commit is a new audit_logs row) | **Implemented in v1** *by construction* — append-only = independence |
| **Durable Re-Provability** (the commit can be re-proven at any future time) | `audit_logs.row_hash` field (or future `digest` field) | §3.1 (the audit log is durable) | **Implemented in v1** for basic re-prove; **future v2** for cryptographic re-prove |
| **Channel Hierarchy** (the commit is locatable by source) | `audit_logs.source` field | (future v2 surface) | **Not implemented** — would require a new `source` field on `audit_logs` |
| **Version Mapping** (the commit is locatable in version history) | `audit_logs.id` + `created_at` field | §3.1 (every commit has a stable ID + timestamp) | **Implemented in v1** |
| **Citation Spine** (the commit cites its evidence) | (LE31 v1 does not have a structured citation field) | (future v2 surface) | **Not implemented** — would require a new `cites` field on `audit_logs` |
| **Deposit-Order Lock** (commits are not reorderable) | (LE31 v1 has the `created_at` timestamp but no formal *order-lock* guarantee) | §3.1 (append-only = order-locked by primary key) | **Implemented in v1** *by construction* — append-only |
| **Claim Ladder** (the commit is one step in a chain) | `audit_logs` table (every commit is a row) | §3.1 (the audit log IS the chain) | **Implemented in v1** |
| **Type-Separation Canon Lock** (one commit type is not silently substituted for another) | (LE31 v1 does not have a formal type-lock; SQLAlchemy enum types are check-constrained) | §3.1 (every commit has a typed `action`) | **Implemented in v1** *partially* (SQL types) |
| **Non-Substitution Rules** (a partial commit is not accepted as a full commit) | (LE31 v1 commits are atomic by SQL transaction) | §3.1 (the commit is one row) | **Implemented in v1** *by construction* |

**Cross-section with prior picks (LE31 cluster of 26 defer picks, this is pick #26 = +1):**

- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. Partasyuk's *Admissible Basis* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Partasyuk's *Durable Re-Provability* is the queried record; feature 122 supplies the query-time measurement.
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Partasyuk's *Channel Hierarchy* is the *who can commit* discipline; feature 127's *proposal-then-action* is the action the channel authorizes.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Partasyuk's *Citation Spine* is the *commit-time citation*; feature 129's *graph* is the *typed edges* that make the citation queryable.
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Partasyuk is a *commit-eligibility* formal model; feature 138 is an *institutional-continuity* formal model.
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Partasyuk's *Admissible Basis + Operative Capacity + Common-Cause Independence + Re-Provability* are 4 invariants; feature 141's KRINEIA invariants are 5. The clusters overlap on *append-only* + *external analysis*; Partasyuk adds *operative capacity* + *common-cause independence* which KRINEIA does not.
- **Feature 161 claims-ledger-toulmin-model-assertion-grounds-warrant-backing-schema** — the *commit-time schema*. Partasyuk is the *commit-eligibility schema*; claims-ledger is the *commit-content schema*.

The 26 picks form the **deepest single-vocabulary cluster in the 42-pass series** for the *append-only-ledger + audit-trail-schema + owner-pains* architectural pattern. **All 26 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The Applicability Boundary Doctrine is a future v2 owner-facing audit-trail surface and would require (optionally):
- A new `source` field on `audit_logs` rows (Channel Hierarchy primitive).
- A new `cites` field on `audit_logs` rows (Citation Spine primitive).
- A formal *order-lock* check on `audit_logs` insertion (Deposit-Order Lock primitive — partially implemented by append-only PK).
- A formal *type-lock* check on `audit_logs.action` (Type-Separation Canon Lock primitive — partially implemented by SQL types).

None of these are v1; all are v2 surfaces that would require an *owner decision* per charter §3.2.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the Applicability Boundary Doctrine vocabulary to `specs/2026-09-09-partasyuk-applicability-boundary-doctrine-formal-commit-admissibility-HANDOFF.md`** as a named commit-eligibility discipline for any future v2 owner-facing audit-trail surface — already done in the HANDOFF.md.
2. **Wait for the first v2 surface that introduces an owner-facing audit trail** — trigger conditions: (a) first v2 PR that adds an owner-facing audit-trail surface; (b) first v2 PR that adds a `source` field on `audit_logs`; (c) first v2 PR that adds a `cites` field on `audit_logs`; (d) first v2 PR that adds a formal type-lock on `audit_logs.action`.
3. **On trigger, evaluate the change against the Applicability Boundary Doctrine schema** — does the change preserve *Admissible Basis* + *Operative Capacity* + *Common-Cause Independence* + *Re-Provability*? The schema is the *what to verify*, not the *what to implement*.

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2 surface** (if the owner decides to add an owner-facing audit trail) would: (a) add a `source` field to `audit_logs`; (b) add a `cites` field to `audit_logs`; (c) add a formal type-lock check on `audit_logs.action`. This is a *v2 surface*, not v1.

## Dependencies

- **Zenodo access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2 dependencies** (if Applicability Boundary Doctrine is adopted): schema changes on `audit_logs`; new `source` + `cites` fields; new type-lock checks. All future; no v1 dependency.

## Open questions

1. **Is the Partasyuk Zenodo series a credible production-traction data point?** Charter §3.2: stars are popularity proxy, not gate. The series is by **Vadym Partasyuk, Independent Research** (single author); the 3 records are deposited within 30 hours; the cit counts are project self-references (not external citations). The *vocabulary* is the value; the *traction* is not.
2. **Should the LE31 v1 `audit_logs` gain `source` + `cites` fields today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant does not need structured source/cites fields today (the audit trail is sufficient); the v2 surface that needs to expose the Applicability Boundary Doctrine schema needs these fields. Recommend: defer to v2 if/when the owner asks for an owner-facing audit trail.
3. **Does the Applicability Boundary Doctrine overlap with feature 141 KRINEIA?** Partially: both name invariants for an audit log to constitute a governance proof; Partasyuk names 4 invariants (Admissible Basis + Operative Capacity + Common-Cause Independence + Re-Provability); KRINEIA names 5 invariants (append-only + no reward-path self-reference + minimal operators + external analysis only + trust-root separation). The clusters overlap on *append-only* + *external analysis*; Partasyuk adds *operative capacity* + *common-cause independence* which KRINEIA does not. **The clusters are complementary, not duplicate.**
4. **Does the Applicability Boundary Doctrine overlap with feature 161 claims-ledger?** Partially: Partasyuk is the *commit-eligibility schema* (is the commit authorized?); claims-ledger is the *commit-content schema* (what is the commit claiming?). **The clusters are complementary, not duplicate.**

## Why this matters

**The Applicability Boundary Doctrine is the only in-window cluster today that names *commit-eligibility* as a formal discipline.** The vocabulary (Admissible Basis + Operative Capacity + Common-Cause Independence + Re-Provability) is the most concise formal statement of *"is this commit authorized?"* in the in-window academic pool. The 3-record Zenodo series is the tightest single-author formal commit-eligibility statement of the 42-pass series.

**The cluster (26 picks, this one + 25 prior) is the persistent cross-section reference for the next v2 owner-pains audit-trail moment.** All 26 are `defer`; no code change today. The cluster is the *what the LE31 v2 owner-pains audit-trail architecture is*, named across 26 different sources, and ready to be referenced when the first v2 owner-facing audit-trail surface lands.

**The most operationally valuable future v2 surface is owner daily recap**: introducing a Telegram-based daily recap with Applicability-Boundary-Doctrine-structured audit trail (Admissible Basis + Operative Capacity + Common-Cause Independence + Re-Provability) would close the *owner-visibility gap* (today, the owner must read the `audit_logs` manually). Owner decision required; not v1.