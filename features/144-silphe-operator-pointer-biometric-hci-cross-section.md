# Feature 144 — silphe operator-pointer-biometric HCI cross-section (defer)

> **NEW observation (2026-09-05).** Documents in-window GitHub repository `martymcenroe/silphe` (3★/0 forks, Apache-2.0, Python, pushed **2026-09-01T00:18:06Z**, in-window by push only): *"Generate and quantify human-fidelity pointer movement — your mouse's signature, captured locally."* **First surface of this repo in the 37-pass series** (parent-verified by ripgrep against all features 1–143 + all brainstorm reports 2026-08-18..2026-09-04). Bucket: **v2 owner-pains (operator-UX research-note)** — watch-list defer. Zero build time today.

## Goal

Retain the **local-only pointer-movement biometric quantifier** as the **architectural primitive** for any future LE31 v2 surface that wants to verify *which operator was at the workstation when a `StockEntry` row was written* without sending biometric data off-device (charter §3.2 privacy constraint). The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the silphe primitive: pointer-movement → biometric signature, computed locally, never persisted as raw movement data.
- A decision record: today's verdict is `defer` because LE31 v1 has no operator-identity-at-the-workstation surface today; the defer surfaces the primitive for the next v2 owner-facing audit surface that needs it.
- A reference for the next time LE31 proposes a v2 owner-facing audit-trail surface that wants to verify *"the same person who closed last night's shift also opened tonight's shift"* without storing biometric identity.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `audit_logs` schema.
- Any user-facing biometric-collection surface (no waiter-facing capture today).
- The full silphe library integration — LE31 has no pointer-movement capture today, so adopting the library would require an integration that doesn't exist.

## Evidence / JTBD

When a future LE31 v2 owner wants to verify *which operator was at the workstation* at a given `StockEntry` row's write time, they want *a signature that changes with the operator and is locally computable*, but they struggle because *storing raw biometric identity violates privacy* (charter §3.2), so that *they can answer the operator-identity question without persisting PII*.

- **Evidence class**: inferred (no LE31 owner has asked for this surface in 37 passes).
- **Confidence**: medium (mechanism) / low (present urgency).
- **Real observed LE31 JTBD**: none. No owner has asked *"who was at the workstation when this `StockEntry` row was written?"* in 37 passes.
- **The value is contingency**, not direct demand: when the question is eventually asked, the primitive already exists.

## Description

GitHub `martymcenroe/silphe` (3★/0 forks, Apache-2.0, Python, pushed 2026-09-01T00:18:06Z) — *"Generate and quantify human-fidelity pointer movement — your mouse's signature, captured locally."*

The transferable primitive is the **local-only mouse-signature quantifier**:

- **Local computation**: the biometric is computed on the operator's workstation; nothing leaves the device.
- **Non-reversible**: the signature *changes with the operator* but cannot be reversed to recover the raw movement data.
- **Operator-specific**: different operators produce different signatures on the same hardware.
- **Time-stable**: the same operator produces a stable signature over weeks/months (the paper's claim; not independently verified in this report).

**Cross-section with LE31 charter §3.1** (mobile-responsive waiter UI):

| Charter invariant | v1 status | Silphe primitive |
|---|---|---|
| **Mobile-responsive waiter UI** (charter §3.1) | **Satisfied** — existing `index.html` works on phone or tablet. | Silphe is the *next-layer* primitive: beyond mobile-responsive, *operator-identity-preserving* mobile. |
| **Privacy: store only data needed for restaurant operations** (charter §3.2) | **Satisfied** — v1 stores counts (`party_size`, `adults`, `children`), no identity or contact data. | Silphe is the **privacy-friendly operator-identity primitive**: store a signature that *changes with the operator* but cannot be reversed to recover the raw biometric. |
| **Explicit operational transitions, no silent automation** (charter §3.1) | **Satisfied** — every `StockEntry` row is an explicit user action. | Silphe could *strengthen* this by adding an *identity-anchor* to each row, but the mechanism (passive collection) sits in tension with explicit-user-action discipline. |

**Cross-section with prior picks:**

- **Feature 130 DHH-kitchen-accessible-operator-ux** (2026-08-28) — *DHH staff need visual + replayable + self-paced workstation prompts*. Silphe adds a different operator-UX primitive: operator-identity, not operator-accessibility.
- **Feature 131 PuntoVivo** (2026-08-28) — *statutory fiscal compliance as a first-class data-model concern*. Silphe is the inverse: privacy-preserving identity, not statutory identity. Different stack, different domain.
- **Feature 134 ECHO Auditable Memory Plane** (2026-09-04) — *replace append-only with structured records*. Silphe is the *provenance layer* that structured records could anchor to (each row's signature = operator identity).
- **Feature 135 DreamLedger** (2026-09-04) — *credit-ledger dual of `StockEntry`*. Silphe could *add* a credit-quality primitive (higher-quality signal from a stable operator signature vs. noisy signal from an unstable operator) without changing the ledger shape.
- **Feature 141 KRINEIA five invariants** (2026-09-04) — *proof/record distinction*. Silphe contributes to the **trust-root separation** invariant: the operator's workstation signature is the *trust root* for the operator's actions.

LE31 v1 currently has no surface that captures operator pointer-movement data; the defer surfaces the silphe primitive for future use. The value is **vocabulary + integration path**, not *implementation*.

## Data model

No schema change today. The defer artifact documents that the future silphe-instantiation would have:

- **Local workstation buffer** (future): a per-memory ring buffer of the last N pointer events; never persisted, only used to compute the signature at sign-off. **Not built today.**
- **Signature column** (future): a new column on `audit_logs` (e.g., `operator_signature`) that stores the locally-computed signature of the operator who triggered the row. **Not built today.**
- **Signature verification API** (future): a thin endpoint that, given a target signature and a candidate operator, returns `match: bool` without exposing the underlying pointer-movement data. **Not built today.**

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to build this in v2, the implementation steps would be:

1. Add a `LE31_SILPHE_ENABLED` env flag (default off).
2. Add a per-memory ring buffer of pointer events at the waiter UI front-end (HTML5 pointer-events API).
3. Compute the silphe signature on demand (e.g., at `/api/visits/{id}/close` time).
4. Add the signature as a new column on `audit_logs` (`operator_signature`).
5. Add a one-page owner-facing audit surface at `/owner/audit/operator` that allows the owner to verify *"was the same operator at the workstation for both last night's close and tonight's open?"*.
6. **Out of scope for v1**: any passive background capture; any cross-session signature reuse (each shift gets a fresh signature); any non-waiter-role capture (cook / manager).
7. **Out of scope for v1**: any data export of operator signatures; any third-party storage.

## Telegram interaction if any

None. Silphe is an operator-UX / owner-audit architecture-reference artifact; no cook-facing Telegram surface today. If the LE31 owner decides to build the v2 owner-facing operator-audit surface, silphe would be exposed *as* part of that surface, not separately.

## Dependencies

- **GitHub**: `martymcenroe/silphe` (3★/0 forks, Apache-2.0, Python, pushed 2026-09-01T00:18:06Z, in-window by push only).
- **Charter §3.1 (mobile-responsive waiter UI)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (privacy: counts not identity)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Companion artifacts**: features 130 / 131 / 134 / 135 / 141 (ripgrep-verified distinct).
- **Stack**: HTML5 pointer-events API on the waiter UI; no new backend dependency.
- **Licence**: Apache-2.0 — importable. README contents not read in this pass (parent relied on the GitHub Search `description` field).

## Open questions

1. **Who would invoke the operator-identity-at-the-workstation surface on a v2 LE31 surface?** LE31 has one stakeholder (the owner). The surface is conceptually useful but adds no operational value if the owner is the only one who would query it. Same open question as feature 121 (Field-Tier Minimization) + 141 (KRINEIA): if LE31's one stakeholder is the only one who can read the audit log, the marginal value of operator-identity-preserving audit over charter §3.1's natural append-only posture is **unproven**. Recommendation: revisit when LE31 v2 has a second stakeholder (a second owner, a reviewer, an auditor).
2. **Does charter §3.1 need an explicit `operator-identity-at-the-workstation` clause?** Today, identity-at-the-workstation is implicit (the `actor_user_id` provenance field on `audit_logs`). A future v2 surface that adds silphe would make this explicit. Recommendation: not a v1 question; revisit when v2 audit-trail surface is considered.
3. **Is the operator signature stable enough over a shift to be useful?** The silphe repo claims weeks/months stability; not independently verified. Recommendation: do not commit to adoption without an in-restaurant stability study (no LE31 owner has run one).
4. **Does LE31's existing `actor_user_id` + `actor_role` provenance satisfy the same JTBD more cheaply?** Today: yes, if the operator is logged in. The silphe primitive's value emerges only when the operator is *not* explicitly logged in (e.g., a shared terminal) — and LE31 v1 charter §3.2 considers hardcoded `server_id = 1` acceptable for v1. Recommendation: revisit when v2 authentication replaces the hardcoded `server_id`.

## Why this matters

LE31 charter §3.2 has been **operationalizing privacy-preserving discipline** for 37 passes without ever surfacing the *operator-identity-at-the-workstation* primitive. Silphe is the **first primitive in the 37-pass series** that gives the operator-identity question a privacy-preserving answer: *a signature that changes with the operator, cannot be reversed to recover raw biometric data, and is computed locally*. The value is not implementation today — LE31 v1 has no surface that captures pointer-movement data. The value is **vocabulary**: any future v2 owner-facing audit-trail surface can now ask *"how do we verify operator-identity without violating charter §3.2?"* and design with silphe as a primitive, instead of rediscovering the privacy-vs-identity tension from first principles each time. This is the **highest-leverage privacy-friendly operator-UX addition of the 37-pass series**.

The defer is fully reversible: if the LE31 owner decides the primitive is not worth carrying, the file can be deleted with no operational impact. The primitive is contained in the file, not in the codebase.