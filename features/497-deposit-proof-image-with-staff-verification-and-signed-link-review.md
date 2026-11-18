# Feature 497 — `v2-deposit-proof-image-with-staff-verification-and-signed-link-review`

> **Pick C of Daily Research 2026-11-18.** **Bucket: v2 (reservations / deposits domain — out of LE31 v1 scope).** **Verdict: `defer` — parking-lot reference.**
>
> **Source artifact:** `ifwian/the-sifted-cafe` — **no license metadata** (not OSI-declared), ★1 / ⑂0, JavaScript/Node/Supabase, created 2026-11-09, pushed 2026-11-17T07:58:56Z. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-18/gh/repo_30_ifwian_the-sifted-cafe.json`; README: `/tmp/le31-daily-2026-11-18/gh/readme_30_ifwian_the-sifted-cafe.md` (9,902 bytes); source URL: https://github.com/ifwian/the-sifted-cafe.
>
> **Why this pick:** the artifact treats a **payment proof as an object with a lifecycle** — private storage, server-computed amount, staff review through short-lived signed links, an explicit rejection state, and a guest re-upload path. That lifecycle is net-new to the corpus: parent-run dedup across all 1,016 feature and spec files gives `downpayment proof` → **0 hits**, `payment proof` → **0 hits**, `deposit proof` → **0 hits**.
>
> **Two hard constraints are recorded rather than engineered around:** (1) the repository has **no license metadata**, so this is a *pattern* reference with **no code reuse permitted**; (2) the payment rail is **GCash**, a Philippine mobile-money system — not the European payments LE31 serves.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). `le31 v2 owner-pains` and `le31 v2-AI` **do not exist**, so the matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **payment-proof lifecycle vocabulary** as the reference design for a future LE31 v2 reservations-and-deposits surface:

1. the deposit **amount is computed by the server**, not stated by the guest;
2. the proof is an **uploaded image object** stored in **private** storage;
3. the browser **never receives a storage credential** — proof files are served through **short-lived signed links**;
4. proof review is an **explicit staff action** with a verification outcome;
5. **rejection is a recoverable state**: the guest can re-upload, and the new attempt is a new object rather than an overwrite;
6. the guest's identity is **not** derived from the proof — the proof is about a payment, and the person is a separate relation.

No deposit, no proof, no upload, and no storage is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the six-point lifecycle summary above.
- The explicit privacy boundary this mechanism sits against (LE31 v1 guest data is counts, not identity or contact data).
- The two recorded constraints: no license metadata, and a non-European payment rail.
- The dedup result establishing the mechanism is net-new to the corpus.

## Out of scope

- No deposit, reservation, downpayment, or payment-proof table.
- No file upload, no object storage, no signed-link issuance, no private bucket.
- No guest-facing surface — LE31 v1's charter names a waiter web UI and a cook Telegram bot; a guest surface is a third.
- No GCash integration, no mobile-money reconciliation, no European payment-rail mapping.
- No adoption of the reference codebase. **No license was declared, so no code may be reused, in whole or in part.**
- No storage of guest payment images under any bucket in LE31.

## Description

The source README describes the mechanism in concrete terms:

- *"**GCash downpayment** — a **30% downpayment** is calculated by the server, and a …"* (the sentence continues past what the README states about the deposit calculation).
- *"**Payment verification** — open proof files through short-lived signed links, … staff can change statuses or read payment proofs."*
- *"Proof files live in a private bucket and are served through signed links."*
- *"can re-upload proof if a payment is rejected."*
- *"**Database** | Supabase PostgreSQL with Row Level Security"* and *"**File storage** | Supabase Storage — private `payment-proofs` bucket"*.
- *"The browser never receives a Supabase key. The API calls the database **as the …** … key is used only for private payment-proof storage."*
- *"Same-origin API only; the front end never talks to Supabase directly."*

The transferable idea is the **lifecycle**, not the rail and not the code. A payment proof is not a boolean and not a screenshot on a shared drive; it is an object with a state machine — *uploaded → under review → verified | rejected → superseded by a re-upload* — that a staff member advances by an explicit action, and that is readable only through a link that expires.

Two properties of the source design are worth carrying as design constraints rather than as code:

- **The deposit amount is computed by the server.** The guest states which booking; the server states what is owed. A guest-supplied amount is a request, not a charge.
- **The browser never holds a storage credential.** The frontend talks to the application's API; the API talks to storage. Proof files are reachable only through server-issued, short-lived links.

The second property is the one that matters most for LE31, because it is the difference between *private* and *hidden*. LE31's privacy invariant restricts v1 guest data to counts rather than identity or contact data. A stored proof image is neither a count nor an operational necessity — it is a guest's payment artefact, and it is exactly the kind of data the invariant exists to keep out of the system. That is why this reference is filed as v2 and explicitly disclaims any authorization to store such images.

## Data model

No schema change. The future reference shape, explicitly **not proposed today**, is:

```text
PaymentProof (future reference)
  id, booking_ref, guest_ref,
  amount_expected, amount_declared, currency,
  storage_object_ref,             # opaque; never a public URL
  state,                          # uploaded | under_review | verified | rejected | superseded
  submitted_at, reviewed_at, reviewed_by,
  supersedes_ref

PaymentProofLink (future reference)
  id, proof_ref, issued_to, expires_at, revoked_at
```

Three properties in this shape are deliberate:

- `amount_expected` is stored **separately** from `amount_declared`, so a mismatch is representable rather than being overwritten by the later value.
- `supersedes_ref` makes re-upload a **new object** rather than a mutation, which keeps the rejected attempt on the record.
- `storage_object_ref` is an opaque reference. A **signed link is never persisted** — the link is issued on demand and expires.

## Implementation

None in this feature. When deposits and proof handling are promoted into a scoped v2 feature:

1. Decide the **payment rail** — what European payment method the proof evidences, and whether a proof is even the right artifact for it.
2. Decide whether the deposit **percentage** is a business rule or a per-booking amount, and where the rule lives (feature 408's "no home in config" defect is the standing warning about where a rule like this belongs).
3. Decide the **storage boundary** and prove the browser never receives a storage credential. This is verifiable and must be tested, not assumed.
4. Make **link expiry short and link issuance audited** — every issuance records who asked and when.
5. Make **rejection recoverable** — a rejected proof produces a new attempt, never a silent overwrite, and the guest can be told why.
6. Keep the **guest's identity separate from the proof**. The proof is about a payment; the guest relation is a separate edge.
7. Decide the **erasure path**: what is deleted when a booking or guest is deleted, and what hash (if any) is retained to prove the proof existed. LE31's privacy invariant makes this a first-class question, not a cleanup task.
8. Keep every state transition an **explicit staff action**. LE31 forbids silently reconciling or closing; a proof moving to `verified` by a background job is a silent transition.

## Telegram interaction

None today. A future design might let staff verify a proof from the cook bot, but that would be a staff surface change with its own acceptance path and its own privacy review — it is explicitly not authorized by this reference. Note that a Telegram bot is a poor fit for image review in any case, since the source design's whole point is that a human opens the file and looks at it.

## Dependencies

- Existing feature 13 — reservations and deposits, already recorded as a domain.
- Existing feature 402 — reservations are out of v1.
- Existing feature 448 — bill identity; a deposit is not a bill and must not be minted as one.
- Existing feature 450 — a refund has no payment to be capped against; a deposit flow would need a matching cancellation/refund path.
- Charter §3.2 / privacy invariant — v1 guest demographics are counts, not identity or contact data. A stored payment image crosses this line and is therefore out of v1.
- Charter §3.1 — two operational surfaces; a guest upload surface is a third.
- Charter §3.4 — AI may assist staff with observable evidence and a non-AI fallback; any future proof triage must keep a human decision.
- Charter §3.6 — `Decimal`, never float; the expected amount is money.
- `le31 v2 owner-pains` and `le31 v2-AI` **do not exist** in the workspace; the sub-issue is attached to `le31 Research`.

## Open questions

1. Is deposit handling a real LE31 owner need? No operator has asked for it in any pass to date.
2. If yes, is a **payment proof image** even the right mechanism for European payments, or is a bank-transfer reference sufficient? This is the question that decides whether the whole reference applies.
3. Who is allowed to verify a proof — owner only, or staff? What is the audit trail for the verification action?
4. What is the deposit's business rule and where does it live? Feature 408 records that LE31 has no home for a tax rate; a deposit percentage would be the same class of rule.
5. What is erased when a guest is deleted, and what is retained to prove a deposit was made and later refunded?
6. Is the expected amount a fixed percentage, a table amount, or a per-booking value?
7. Does a rejected proof trigger any automated consequence, or is the guest told and nothing else happens? LE31's charter forbids silent reconciliation, so the automatic options are constrained.
8. If the proof is stored at all, how is it prevented from appearing in logs, in error messages, and in backups indefinitely?

## Why this matters

The artifact is ★1 with no license and a non-European payment rail, so on traction alone it is the weakest of the three picks today. It is filed anyway because the **lifecycle** it describes is precise, net-new to a 1,016-file corpus, and because it forces an honest conversation about a boundary LE31's charter draws sharply: a guest's payment image is not operational data, and a system that decides it is worth storing has made a privacy decision the charter has not authorized.

The correct disposition is **defer**, and the deferral is stronger than the other two picks: this reference must not become a proposal to store proof images in LE31 without an explicit owner decision, and no code from the reference repository may be reused at all, because it declares no license. What is worth keeping is the state machine, the server-computed amount, the short-lived signed link, and the recoverable rejection — the vocabulary of confirming a payment without trusting the payer.
