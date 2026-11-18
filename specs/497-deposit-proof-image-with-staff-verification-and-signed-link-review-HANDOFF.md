# HANDOFF — Feature 497: v2 deposit proof image with staff verification and signed-link review

## Active feature path

`features/497-deposit-proof-image-with-staff-verification-and-signed-link-review.md`

**Disposition:** `defer` — v2 parking-lot pattern reference. **A coding agent must not implement this feature from this handoff.** The handoff records the payment-proof lifecycle vocabulary and the trigger for a future, separately-gated reservations-and-deposits scope.

> **⚠️ TWO HARD CONSTRAINTS ON THIS SLICE, both recorded rather than engineered around:**
> 1. **No code reuse.** The source repository declares **no license metadata**. It is a *pattern* reference only. No code from it may be reused, in whole or in part, in any form.
> 2. **No storage of guest payment images.** Charter §3.2 restricts v1 guest data to counts, not identity or contact data. A stored payment proof image crosses that line. This contract does **not** authorize storing such an image, and a future promotion requires an explicit owner privacy decision before any code is written.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no owner has asked for deposit handling in any pass to date |
| 2. Viability | PASS in principle — the lifecycle is small and its states are enumerable |
| 3. Practicability / confidence | LOW — no license metadata, ★1, and the payment rail is GCash (Philippine mobile money), not the European payments LE31 serves |
| 4. Conflict | SCOPE CONFLICT for v1 — a guest upload surface is a third surface, and a stored payment image crosses the §3.2 privacy boundary |
| 5. Outcome, appetite, scope | DEFER to v2 — feature 13 already records the domain; no owner request |
| 6. Cost to operational value | HIGH today — a new domain, a new stored-object lifecycle, and a new privacy surface |
| 7. Circuit breaker / reversibility | PASS — documentation only |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future deposits-and-proof feature is separately approved, likely touch points are:

- `backend/app/models.py` — future payment-proof and proof-link models, with the guest reference kept **separate** from the proof;
- `backend/app/services/payments.py` — future server-side deposit-amount computation and proof state transitions;
- `backend/app/storage.py` — future private object storage, short-lived signed-link issuance, and issuance auditing;
- `backend/app/routers/reservations.py` — future guest upload and staff review routes;
- `backend/app/services/gdpr.py` or the existing erasure path — future erasure semantics for proof objects and the retained hash;
- tests — browser-never-holds-a-storage-credential, link expiry, link revocation, rejection-then-re-upload creates a new object, guest identity is not derived from the proof, no proof bytes in logs.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/497-deposit-proof-image-with-staff-verification-and-signed-link-review.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-18/gh/readme_30_ifwian_the-sifted-cafe.md` and repository metadata at `/tmp/le31-daily-2026-11-18/gh/repo_30_ifwian_the-sifted-cafe.json`.
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-18.md` records the pick as `DEFER`, the project attachment as `le31 Research`, and the license/rail caveats as stated.

For a future implementation, required verification includes a credential-exposure test proving the browser never receives a storage credential, an expiry test proving a signed link stops working after its stated lifetime, a re-upload test proving a rejection produces a **new** proof object rather than an overwrite, and an erasure test proving proof bytes are removed on guest deletion while a retained hash survives.

## Rollback path

- Delete `features/497-deposit-proof-image-with-staff-verification-and-signed-link-review.md`.
- Delete `specs/497-deposit-proof-image-with-staff-verification-and-signed-link-review-HANDOFF.md`.
- Remove the feature-497 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.2 (guest data is counts), §3.4 (AI assists staff with observable evidence and a non-AI fallback), §3.6 (Decimal, never float), the privacy invariant, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, even for a v2 reference;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when **all** of the following hold: the owner explicitly requests deposit handling for reservations; the owner makes an **explicit privacy decision** on storing guest payment artefacts (the §3.2 boundary is not something an agent may decide); a European payment rail is identified such that a proof image is the right artefact rather than a bank-transfer reference; and a new feature is separately scoped and gated. No v2 project currently exists; the Linear sub-issue is therefore attached to `le31 Research`.
