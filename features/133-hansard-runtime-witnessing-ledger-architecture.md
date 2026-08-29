# Feature 133 — HANSARD runtime-witnessing ledger-architecture (defer)

## Goal

Surface arXiv `2608.22512v1` HANSARD (2026-08-23, cs.AI) as a
dated, in-window architectural reference for any future LE31 v2
audit-trail surface — specifically, the **"runtime witnessing"**
framing as a named primitive that operationalises what LE31's
`StockEntry` ledger already does at single-restaurant scale.

## Scope

**In scope (defer artifact):**
- A written record of the paper's threat model ("the record is
  produced by the suspects"), mechanism (forensic readiness + runtime
  witnessing + graded attribution), and architectural primitives.
- A decision record: today's verdict is `defer` because LE31 v1 has
  no audit-trail viewer surface and the charter does not authorise
  v2 audit-trail work yet.
- A reference for the next time LE31 considers an audit-trail viewer
  for any non-stock entity (visit, bill, shift).

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any user-facing audit-trail viewer surface.
- Any owner-facing forensic-readiness tooling.
- Implementation of the paper's graded-attribution primitives (they
  are no-ops at LE31's scale).

## Description

arXiv `2608.22512v1` HANSARD — "A Reference Architecture for Forensic
Readiness, Runtime Witnessing, and Graded Attribution in Autonomous
Multi-Agent AI Systems" — is the strongest single in-window arXiv
signal of the LE31 daily-research 30-pass series. The threat model
is explicit: *the record is produced by the suspects*. The proposed
answer has three parts:

1. **Forensic readiness** — the system is built from the start so
   that any future audit can reconstruct what happened.
2. **Runtime witnessing** — at the moment a record is produced, the
   system produces a *witness* (a small attestation: who authorised
   the action, what alternatives were considered, what the system
   knew at the time).
3. **Graded attribution** — when multiple actors are involved (a
   human user, an LLM agent, an external service), the witness
   records each actor's contribution separately, so that "X caused
   this row" can be answered precisely.

LE31 v1 already operationalises a thin version of all three at a
single-restaurant scale:

1. **Forensic readiness** is the charter §3.1 append-only `StockEntry`
   ledger: the record exists, is append-only, and can be reconstructed.
2. **Runtime witnessing** is the `actor_user_id` + `actor_role`
   fields on `StockEntry`: at the moment a row is written, the
   witness records who wrote it and what role they had.
3. **Graded attribution** is currently *absent*: every `StockEntry`
   row attributes the write to a single actor, even though real
   restaurant operations sometimes involve multiple humans (the cook
   who took the photo, the manager who confirmed the menu, the
   cashier who closed the bill).

The paper's value for LE31 is therefore *naming* rather than
*mechanism*: a future v2 contributor reading the LE31 codebase is
more likely to *respect* the `actor_user_id` field as a *runtime
witness* than as a passive metadata field. The functional name
encodes the operational responsibility: the witness attests, and
the attestation is auditable.

The paper's primitives (graded attribution across multi-actor
chains) are out of scope for LE31 v1 — the threat model does not
match. LE31's actors are cook + manager + waiter, all humans, all
allowlisted; there is no agent-ephemeral population, no
model-selected-action regime. The primitives are no-ops at LE31's
scale.

## Data model

No schema change. The defer artifact documents that the
`StockEntry` `actor_user_id` + `actor_role` fields should be
described in future v2 documentation as *runtime witnesses*, not as
passive metadata. This is a documentation decision, not a code
decision.

## Implementation steps

None today (defer). When LE31 first considers an audit-trail viewer
surface for non-stock entities:

1. Load this artifact and the linked arXiv paper.
2. Re-run the LE31 feature gate with the paper in hand.
3. Decide whether graded attribution (multi-actor `StockEntry`
   writes) is in scope for the v2 audit-trail surface.
4. If yes, design a `witness_tokens` schema that names the
   witnesses per row.
5. If no, close this artifact.

## Telegram interaction if any

None. This is an architectural reference, not a user-facing feature.

## Dependencies

- LE31 charter §3.1 (append-only ledger invariant) — the witness
  framing *strengthens* this invariant, does not weaken it.
- LE31 charter §3.4 (observable evidence) — the witness framing
  is exactly the charter §3.4 obligation at single-restaurant scale.
- `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md`
  — companion observation: "Ledger-Based Control" is the
  *operational* framing; "Runtime Witnessing" is the
  *attestation* framing. Both belong in the same v2 documentation.
- `features/108-telegram-chat-history-fuzzy-search-stockentry-audit.md`
  — companion observation for v2 audit-trail surface architecture.
- `features/121-ledger-commitment-field-tier-minimization.md` —
  related: a witness can be the unit of disclosure minimisation.

## Open questions

- Does the v2 audit-trail surface need graded attribution, or is
  single-actor attribution (current LE31 posture) sufficient?
- Should the witness identifier be a hash (cryptographic
  commitment) or a soft reference (foreign-key to actor table)?
  Paper is silent on the choice; LE31 will need to decide.
- If LE31 ever ships a non-staff-actor surface (delivery driver,
  booking service, automated pricing), should the witness model
  extend to *agent principals* per the paper's framing? The
  paper's primitives are designed for exactly that transition.

## Why this matters

The HANSARD paper is the strongest single in-window arXiv signal in
30 passes because it names a precise primitive — *runtime witnessing*
— that LE31's existing `StockEntry` ledger already operationalises.
The naming difference is meaningful: "the ledger is a record" is
descriptive; "the ledger is a witness" is functional. A future v2
contributor is more likely to *respect* a witness than a record.
Filing this artifact today costs near-zero (defer) and creates dated,
in-window academic reference for the next time LE31 considers an
audit-trail viewer surface. The paper is not a feature; it is a
*vocabulary* for the existing feature.