# Feature 499 — `v2-quotation-on-its-own-number-series-with-no-effect-until-converted`

> **Pick B of Daily Research 2026-11-19.** **Bucket: v2 (new bucket — justified below).** **Verdict: `defer` — parking-lot vocabulary reference.**
>
> **Source artifact:** `nikhilb2/simple-invoicing-free-gst-billing-software` — MIT, ★22 / ⑂80, created 2026-03-29, pushed 2026-11-18T16:00:00Z. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-19/gh/repo_07_nikhilb2_simple-invoicing-free-gst-billing-software.json`; README: `/tmp/le31-daily-2026-11-19/gh/readme_07_nikhilb2_simple-invoicing-free-gst-billing-software.md`; source URL: https://github.com/nikhilb2/simple-invoicing-free-gst-billing-software.
>
> **Why this pick:** one README sentence states an **effect-semantics rule** that LE31's ledger discipline has never had a place for — *"Quotations & Proforma Invoices — Offers on their own number series with PDF and share links, converted to an invoice through the composer. **No effect on stock, ledgers or returns until then**"*. The mechanism is not the quotation. It is the **"until then"**: a document that has an identity, can be shared, and yet deliberately moves nothing — and whose conversion is a single explicit event.
>
> **Why it is net-new:** the parent ran a targeted dedup sweep across all **1,022 feature and spec files**: `quotation` → 3 (feature 161's claims-ledger assertion model, and two HANDOFFs using the word in an unrelated sense); `proforma|pro forma` → **0**; `no effect on (stock|ledger)` → **0**; `(offer|quote).{0,30}(own|separate).{0,20}number` → **0**; `number series` → **0**; `does not (affect|change).{0,30}(stock|inventory|ledger)` → 5 (feature 267's walk-in triage, feature 268's HCI audit, feature 395's recipe-consumption snapshot — none is an offer document with an identity and a conversion rule). **The concept of a document that is deliberately non-effecting has never been written down in the corpus.**
>
> **Boundary with features 373/374 (the append-only `StockEntry` ledger and the derive-current-stock rule):** those own what **moves** stock. This pick is about a document that **deliberately moves nothing** but has its own identity and can later be converted. The two are complementary — 373/374 have no concept of a non-effecting document, and a quotation without a ledger would be a spreadsheet. The contract does not weaken the append-only rule; it adds a class of thing the rule does not apply to, and says so explicitly.
>
> **Bucket justification (new bucket):** no existing bucket covers "a document class with explicit effect semantics". It is not v1 (LE31 v1 records orders, not offers, and §3.2 excludes customer-facing surfaces), not v2 owner-pains (not an operator workflow surface), and not v2-AI (no model involved). Recorded as **v2** because it arrives with a quoting/pre-order scope, which LE31 defers past v1.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **non-effecting-document semantics** as the reference design for any future LE31 document that is *not* yet a fact:

1. an offer has **its own number series**, distinct from the invoice series, so the two can never be confused by a reader or by a query;
2. an offer **has an identity** of its own, before any conversion;
3. an offer is **shareable** — it exists outside the system as something a person can read;
4. an offer **has no effect on stock, on ledgers, or on returns** while it is an offer;
5. an offer is **converted into an invoice through an explicit composer step**, not by editing;
6. the conversion is the **single moment** at which effects begin — "no effect **until then**" is the contract, and the word "until" is the design;
7. the offer's *own* number series continues to exist after conversion, as the provenance of the invoice that followed it.

No offer, no quotation, no proforma, no number series and no conversion event is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the seven-point mechanism summary above.
- The explicit effect-semantics rule — no effect on stock, ledgers or returns until conversion — stated as the contract's load-bearing sentence.
- The dedup result that establishes the mechanism is net-new to the corpus.
- The explicit boundary with features 373/374 (what moves stock) and with feature 448 (a bill's human-facing identity) and feature 415 (a bill closes a visit).
- The statement that this feature **does not weaken** the append-only ledger rule; it names the class of document the rule does not apply to.
- A future-project attachment decision: `le31 Research`, because no v2 project exists and this pick is not v1 work today.

## Out of scope

- No quotation, proforma or offer entity; no number-series allocation; no composer.
- No PDF generation and no share-link machinery. The source's PDF and share-link features are *how the offer is delivered*, not the effect-semantics rule that is being recorded; they are explicitly not carried over.
- No change to the append-only `StockEntry` ledger, the derive-current-stock rule, or the bill lifecycle.
- No customer-facing surface. The source shares offers with a customer; **this contract does not**, and §3.2 excludes customer-facing surfaces in v1.
- No pricing, discounting or promotion logic — §3.2 excludes discount and promo codes.
- No payment, deposit or prepayment concept.
- No adoption of the GST / India tax model, and no adoption of the source's number-series format.

## Description

The source README states the mechanism in one line, and the line is remarkable because it separates three things that are usually fused:

> *"Quotations & Proforma Invoices — Offers on their own number series with PDF and share links, converted to an invoice through the composer. No effect on stock, ledgers or returns until then"*

**What LE31 has today.** LE31's write model is deliberately narrow and strong: the `StockEntry` ledger is append-only, and on-hand stock is derived, never edited (features 373 and 374). A `Bill` closes a `Visit` (feature 415). A bill has a human-facing identity (feature 448). Every one of those documents **means something immediately**: writing an order line changes stock; writing a bill closes a visit.

**What LE31 has never had.** A document that is *recorded* but means nothing yet. There is no place in the LE31 model for "we agreed a price for the table, and nothing has happened yet." If a waiter writes such a thing today, it has to be a note in a free-text field, or it has to be a real order line — and a real order line **moves stock**, which means a table that is still deciding what it wants has already decremented the kitchen's inventory.

**Why that matters for a restaurant, concretely.** A table of six orders the food, asks what the total will be, and changes their minds about the second bottle. Under LE31's current model the "asking" is a real order (stock moves, the cook sees it), or it is nothing at all (and the owner cannot answer the question). The source's mechanism gives the third option: a document with its own number that holds the answer without touching anything.

**The "until then" is the whole design.** The important word in the source sentence is not "quotation" — it is **"until"**. The offer has no effect *for now*, and the moment of effect is a single named event (the composer converting it to an invoice), not an edit. That distinction is what keeps the offer out of the ledger: an offer that can be edited into an invoice has no well-defined "before", and a ledger with no well-defined "before" cannot be reconciled.

**The "own number series" is the second load-bearing part.** An offer on the invoice series would mean the offer and the invoice are the same kind of thing, differing only in a status field — and a status field is exactly the shape that makes "no effect until then" unenforceable, because anything reading the row has to know to check the status. Separate series make the class distinction structural rather than conditional.

**What the source does *not* specify, and this contract therefore does not guess.** The README does not say what happens to the offer's number after conversion, whether an offer can be partially converted, what the cancellation semantics are, or how a converted offer relates to the stock movement it eventually causes. Those are the four things a future implementation must decide, and naming them is more useful than inventing them.

**Adjacent but not owned.** The same README also describes *"Day Book Register — Cross-ledger voucher register for reconciliation"* — that is recorded separately as feature 500 and is not bundled here. The two are different mechanisms in different domains: one is a **document with effect semantics**, the other is a **read model over ledgers**.

## Data model

**None is created by this feature.** The following is a *reference shape* recorded for a future implementation, and it is deliberately not a schema:

```
Offer
  offer_id         opaque identifier
  offer_number     on a number series DISTINCT from the invoice series
  status           offer | converted | cancelled
  issued_at        when the offer was issued
  lines            the proposed lines, carrying no stock effect
  converted_to     the invoice this offer became, once converted

Bill
  bill_number      on the invoice series
  ...
```

**The two rules, stated once each, as the contract's load-bearing sentences:**

1. *An offer in `offer` status contributes **no** `StockEntry` row, **no** ledger entry, and **no** return; no derived quantity may change because of it.*
2. *An offer's number series is **distinct** from the invoice series; the two are never allocated from the same counter.*

**The reference shape is deliberately incomplete**, and the gaps are named rather than guessed: the fate of the offer number **after** conversion is unspecified; **partial** conversion (one line of a three-line offer converted, the rest not) is unspecified; **cancellation** semantics are unspecified; and the relationship between a converted offer and the stock movement it eventually causes is unspecified. An implementer must decide all four and record the decision.

## Implementation

**No implementation is authorised by this feature.** It is a `defer` reference.

If a future feature is separately approved, the plausible touch points would be:

- `backend/app/models.py` — future `Offer` model and a distinct number-series allocator;
- `backend/app/services/offers.py` — future offer lifecycle: issue, convert, cancel;
- `backend/app/services/orders.py` — the **conversion** call site, which is where effects begin;
- `backend/app/routers/offers.py` — future offer and conversion routes;
- tests — offer-writes-nothing-to-the-ledger, offer-number-not-in-the-invoice-series, conversion-writes-once, conversion-is-not-an-edit (i.e. re-converting is refused rather than applied twice).

**Ordering constraint.** A future implementation must land **after** features 373/374 (the append-only ledger and derive-current-stock rule) are closed, because the whole point of the offer is that it writes nothing — and that guarantee is only meaningful once the thing it writes nothing to is trustworthy. It must also land after feature 448 (a bill's human-facing identity), because the offer's own number series is the same class of problem and two conflicting answers would be worse than one.

## Telegram interaction

**None.** The cook Telegram bot is not a consumer of offers in this disposition, and no bot command is added. A future "table 4 asked for a quote" surface would need its own owner decision and its own actor model (feature 403).

## Dependencies

**Existing LE31 features this pick depends on or is adjacent to:**

- **Feature 373** (`append-only-stock-ledger`) — the ledger the offer must not touch. **Prerequisite.**
- **Feature 374** (`derive-current-stock`) — the rule that makes "no effect" checkable. **Prerequisite.**
- **Feature 415** (`bill-closes-visit`) — a bill is the terminal event; an offer must not be. **Adjacent.**
- **Feature 448** (`bill-has-no-human-facing-identity`) — the same identity class as the offer number. **Adjacent.**
- **Feature 403** (`role-carrying-bot-chat-table`) — the actor for issue/convert/cancel. **Adjacent.**
- **Feature 500** (`cross-ledger-voucher-register`) — a converted offer's invoice lands in the register. **Adjacent, and recorded separately.**

**External dependency:** none. The source artifact is a MIT-licensed reference, not a code dependency; nothing is imported.

## Open questions

1. **Does an offer ever get a customer-facing surface?** The source shares offers via PDF and link. That is excluded in v1 by §3.2 and this contract does not carry it. A future decision would need to revisit §3.2 explicitly.
2. **Is partial conversion allowed?** Converting one line of a three-line offer and leaving the rest — the source is silent, and the answer changes whether the offer is one document or a set.
3. **What happens to the offer number after conversion?** The contract records that the series continues to exist as provenance, but the source does not say whether the offer row is retained, archived or deleted.
4. **Does a cancelled offer have any effect?** It should have none, like an offer — but cancellation needs its own recorded semantics so that a cancelled offer cannot later be converted.
5. **Does the offer carry a validity period or a price hold?** An offer that is not time-bound and not price-bound is a note; one that is, is a commitment. The source does not say.
6. **What is the offer's relationship to the charter's §3.2 "no reservations / no online ordering"?** A table holding an agreed price for an unfixed set of items is arguably a reservation in all but name. This needs an explicit owner ruling before the pick can be promoted.

## Why this matters

LE31's ledger discipline is the strongest thing the project has, and it is also what makes this pick awkward: every document LE31 can write **means something immediately**. That is a virtue for auditability and a limitation for anything conversational. A restaurant's actual first interaction with a price is very often not an order — it is *"what will this be, roughly?"* — and LE31 currently has no honest way to answer that without either moving stock or moving nothing and answering from memory.

The mechanism's value is that it makes the **"until then"** an explicit, structural fact rather than an omission. An offer on its own number series with a stated non-effect rule is a document that can be shared, quoted, revised and forgotten, and whose only moment of consequence is a named conversion. That is a materially different object from a draft order, and from a note in a text field that nobody can reconcile later.

Recording it as a `defer` is the honest call: no LE31 operator has asked for quotes, and charter §3.2 explicitly excludes the customer-facing surface that would make it a product. But the vocabulary is cheap now and expensive to rediscover, and the one sentence worth keeping — *no effect on stock, ledgers or returns until then* — is the sentence that makes the whole design auditable.
