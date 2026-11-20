# Feature 506 — `v2-checkout-time-credit-detection-for-unallocated-advances-and-credit-notes`

> **Pick C of Daily Research 2026-11-20.** **Bucket: v2.** **Verdict: `defer` — parking-lot vocabulary reference.**
>
> **Source artifact:** `kodlyft/xpos` — MIT, ★55 / ⑂47, TypeScript/Vue on Frappe+ERPNext, created 2026-02-26, pushed 2026-11-19T15:55:22Z, 9,504 KB. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-20/gh/repo_36_kodlyft_xpos.json`; README (base64-decoded): `/tmp/le31-daily-2026-11-20/gh/readme_plain/plain_36_kodlyft_xpos.md`; source URL: https://github.com/kodlyft/xpos. **Same artifact as feature 504; a different section of the same README.**
>
> **Why this pick:** one README states a **checkout-time detector** for money the customer already holds — *"**Customer credit** – Auto-detect unallocated advances and credit notes at checkout"* — paired with *"**Draft invoices** – Save, retrieve, and manage multiple open orders per session"*, *"**Return mode** – Process returns linked to original invoices with automatic credit notes"* and *"**Outstanding settlement** – View and pay against a customer's open invoices"*. The operator-facing idea is that money already paid or already owed is **detected at the till**, not discovered at close.
>
> **Why it is net-new:** the parent ran a targeted dedup sweep across all **1,034 feature and spec files** in the repository before selecting this pick: `unallocated advance` → **0 files**; `draft invoice` → **0 files**; `credit note` → 3 hits across 2 files (feature 435's bill-line-membership contract mentions it twice, and feature 435 does not own a credit-note class); `customer credit` → 9 hits across 3 files, all about a **credit-limit policy** (feature 170) or a **bill** (feature 435), not about **detecting money the customer already holds**; `liability ledger` → 2 hits in 1 file (feature 135, a crypto credit-ledger architecture reference). The **unallocated-advance detector at the point of sale** has never been written down in the corpus.
>
> **Boundary with feature 435 (`le31-bill-records-no-which-lines-it-charged-first-party-a-bill-has-no-edge-to-order-item-so-the-stored-subtotal-is-a-number-nobody-can-audit`):** 435 owns **the bill's line membership** — which order lines a bill charges for. This pick owns **the detector that runs before the bill is taken**.
>
> **Boundary with yesterday's Pick B (`v2-quotation-on-its-own-number-series-with-no-effect-until-converted`):** yesterday's pick owns **a document that has no effect until converted**. This pick owns **the detection of existing money at the moment of sale**. They are complementary but not the same: a quotation creates a document; this creates a *suggestion*.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **checkout-time credit detection** as the reference design for any future LE31 customer-credit surface:

1. **money the customer already holds is detected at the point of sale**, not discovered later at close;
2. the detector distinguishes **an unallocated advance** (money received that was never attached to anything) from **a credit note** (a document created by a return or a credit event);
3. both are **unallocated** until something binds them — the detector's job is to *surface* them, not to apply them silently;
4. **draft invoices** exist so that an open order can be retrieved and continued rather than re-entered — multiple open orders per session;
5. a **return is linked to the original invoice**, and the credit it creates is a *consequence of that link*, not an unrelated document;
6. an **outstanding balance** is visible — a customer with open invoices can be settled against them.

No customer model, no advance store, no credit-note class, no detector and no checkout surface is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the six-point mechanism summary above.
- The dedup result that establishes the mechanism is net-new to the corpus (`unallocated advance` → 0 files).
- The explicit boundary with feature 435 (the bill's line membership) and yesterday's Pick B (the non-effecting document).
- The explicit **tension with charter §3.2 privacy** — recorded, not resolved.
- The load-bearing sentence of the design, stated once: **the detector surfaces unallocated money at the till; it never applies it without an explicit user action.**
- A future-project attachment decision: `le31 Research`, because no v2 project exists and this is not v1 work today.

## Out of scope

- No customer model, no customer identity store, no advance store, no credit-note schema.
- No change to the waiter web UI, the cook Telegram bot, the `StockEntry` ledger, or the bill lifecycle.
- No change to how a bill is computed or what it charges for — feature 435 owns the bill's membership.
- **No resolution of charter §3.2's privacy boundary.** This feature explicitly does not decide whether LE31 may hold a customer identity or a customer balance.
- **No loyalty programme, no stored-value gift card, no customer credit limit, no customer addresses.** The source ships all four; none is transferred.
- No adoption of the TypeScript/Vue/Frappe/ERPNext stack.
- No public, customer-facing or online surface. The detector runs on the waiter's till, not on a guest's phone.
- No return/refund workflow — feature 415 (`bill closes visit`) and the bill family own the terminal transitions; the source's *"Return mode"* is recorded as vocabulary only.

## Description

The source artifact's README states the customer-money family in four lines, verbatim:

> *"**Customer credit** – Auto-detect unallocated advances and credit notes at checkout"*
> *"**Draft invoices** – Save, retrieve, and manage multiple open orders per session"*
> *"**Return mode** – Process returns linked to original invoices with automatic credit notes"*
> *"**Outstanding settlement** – View and pay against a customer's open invoices"*

**1. The detector runs at the till, at the moment of sale.** This is the whole idea and it is a *timing* idea. A customer who prepaid €50 last week and whose prepayment was never written down is, to the system, a customer with no credit — until they sit down and order. The detector's value is that it fires **then**: at the moment the money's existence would actually change the amount owed. A credit balance that is only reconciled at close is a credit balance that is useless at the table.

**2. Two kinds of unallocated money.** An **unallocated advance** is money received without a purpose. A **credit note** is a document produced by an event — a return, a price correction. The source detects both and treats them as different things that happen to share the property "not yet attached to anything". Keeping them distinct matters: an advance is money the restaurant holds; a credit note is a *claim* the restaurant holds.

**3. "Auto-detect" means surface, not apply.** The word "auto" is doing less work than it appears. The detector *notices* and *offers*; the operator chooses. If the detector auto-applied an unallocated advance to a bill, it would be deciding on the operator's behalf how €50 of unlabelled money is spent — which is exactly the kind of silent state transition LE31's charter §3.1 forbids: *"Do not silently send, serve, close, or reconcile an order."*

**4. Draft invoices enable continuity.** *"Save, retrieve, and manage multiple open orders per session"* — an open order that can be put down and picked up again, several at once. This is a real operational shape (a table orders, the waiter is called away, the table adds more) and it is **not** what LE31's order model supports today. It is recorded here because the source's detector depends on it: an advance can only be detected at checkout if there is a well-defined "checkout" moment, which requires the open order to be a resumable object.

**5. A return is linked to its original invoice.** *"Process returns linked to original invoices with automatic credit notes"* — the credit note is *caused by* a link to a prior document. This is the same "no effect without a cause" discipline as LE31's `StockEntry` ledger, transposed onto money.

**6. An outstanding balance is visible.** *"View and pay against a customer's open invoices"* — the customer's position is a thing the operator can look at.

**Why the source's own limits are recorded rather than hidden.** The README does not specify how an advance is created, how it is matched to a customer, what "unallocated" means operationally (is it matched by customer? by amount? by date?), or what happens when an advance exceeds the bill. So this contract records a **shape**, not a copyable design. A future implementation would have to specify all four, and this contract is honest that they are unspecified.

**Adjacent but not owned.** The same README ships *"Loyalty programs – Point accumulation, redemption, and multi-program support"* (feature 18 owns gift cards; the loyalty family is a different concept), *"Credit limits – Enforce customer credit policies during checkout"* (a **policy** on how much a customer may owe — the opposite direction from this pick's *money already held*), *"Gift cards – Sell stored-value cards anyone can spend in parts, with a liability ledger reconciled to the GL"* (feature 18), and *"Address management – Multiple billing and shipping addresses per customer"* (§3.2 privacy territory). None is bundled.

## Data model

**None is created by this feature.** The following is a *reference shape* recorded for a future implementation, and it is deliberately not a schema:

```
UnallocatedMoney (what the detector looks for)
  money_id         opaque identifier
  kind             'advance' | 'credit_note'
  amount           exact EUR value, minor units, never a float
  received_at      timezone-aware instant
  allocated_to     what it is attached to, if anything (null while unallocated)
  cause_ref        the document that caused it (a return's original invoice)

DetectedAtCheckout
  detected_at      the instant of the checkout
  order_ref        the order being taken
  candidates       the unallocated money that was surfaced
  applied          what the operator chose — an explicit user action
```

**The load-bearing sentence, stated once, as the contract's design:** *the detector surfaces unallocated money at the till; it never applies it without an explicit user action, and an unallocated amount is never silently inferred into a bill.*

**The reference shape is deliberately incomplete**, and the gaps are named rather than guessed: the **matching rule** is unspecified (how the system decides which advance belongs to which customer — by identity, by amount, by recency); the **customer identity** question is unspecified and is the §3.2 blocker; the **partial-allocation** case is unspecified (an advance of €50 against a €30 bill); the **expiry** case is unspecified (whether an advance lapses); and **draft invoices** are unspecified as a data model. An implementer must decide all five and record the decision. A contract that guessed them would be worse than one that names them.

## Implementation

**No implementation is authorised by this feature.** It is a `defer` reference.

If a future feature is separately approved, the plausible touch points would be:

- `backend/app/models.py` — future `UnallocatedMoney` and draft-invoice models;
- `backend/app/services/credits.py` — future detection and the explicit application path;
- `backend/app/routers/checkout.py` — future checkout surface returning detected candidates;
- the waiter web UI — future "unallocated money available" affordance at the bill;
- tests — detection surfaces candidates without applying them; an application requires an explicit action; a credit note is always linked to a cause; an over-payment is handled per a recorded rule.

**Ordering constraint (not optional).** A future implementation must land **after** charter §3.2's privacy boundary has been answered for customer identity, and **after** the bill's line membership (feature 435) exists, because the detector's output is applied *to* a bill. Building the detector before 435 gives a suggestion with nowhere to go.

## Telegram interaction

**None.** The cook Telegram bot is not a consumer of a checkout-time credit detector, and no bot command is added. The detector belongs to the waiter's till, not the kitchen. A future "table 4 has €50 in credit" bot message would need its own owner decision, its own chat-id allowlist treatment (feature 403), and would have to respect §3.1's ban on silently acting on operational state.

## Dependencies

**Existing LE31 features this pick depends on or is adjacent to:**

- **Feature 435** (`le31-bill-records-no-which-lines-it-charged`) — owns the bill's line membership. **Prerequisite.** The detector's output is applied to a bill.
- **Feature 415** (`bill closes visit`) — a bill is the terminal event; an advance must not close one. **Adjacent.**
- **Feature 448** (`le31-a-bill-has-no-human-facing-identity`) — a credit note and an advance both need an identity if they are documents. **Adjacent.**
- **Feature 500** (`v2-quotation-on-its-own-number-series-with-no-effect-until-converted`) — yesterday's Pick B owns a document that has no effect until converted. **Adjacent, complementary.**
- **Feature 18** (`gift-cards`) — stored value, a liability position. **Adjacent, explicitly not bundled.**
- **Feature 170** (`devshakib015-shopdesk-offline-pos-as-stock-ledger`) — credit limits. **Adjacent, opposite direction.** A credit limit says how much a customer may owe; this says how much they already hold.
- **Charter §3.2** — *"store only data needed for restaurant operations; v1 guest demographics are counts, not identity or contact data"* and the out-of-scope line on customer accounts. **Blocking.**

**External dependency:** none. The source artifact is a MIT-licensed reference, not a code dependency; nothing is imported.

## Open questions

1. **Does LE31 ever hold a customer identity?** This is the blocker. Charter §3.2 says v1 guest demographics are **counts**, not identity or contact data. A customer-credit mechanism needs somewhere to attach the advance. The charter has not answered whether an anonymous, till-scoped balance is acceptable.
2. **Is an advance a customer concept at all, or a per-visit concept?** If a restaurant's regulars are known by name and face, an advance is a customer fact. If customers are strangers, an advance is almost never worth the complexity — and the detection-at-checkout idea collapses to "the waiter remembers".
3. **How is an advance matched?** By customer identity, by amount, by recency? The source does not say, and the three give very different behaviours.
4. **What happens when the advance exceeds the bill?** Remain as a balance, or is the difference returned? The source's *"Outstanding settlement"* suggests a balance survives, but the transition is unspecified.
5. **Do advances expire?** An unexpired advance is a liability; an expired one is a write-off. LE31's `StockEntry` rule (never update or delete a ledger event) would make expiry a new event, not an edit.
6. **Is "auto-detect" the right verb for LE31?** If the charter's explicit-state principle is applied strictly, the surface might be a *list of unallocated amounts the operator can choose from* rather than a detector that decides. The source's phrasing may be looser than LE31 would accept.
7. **Does the draft-invoice shape have independent value?** It may be the more useful half of this source, and it is a different feature. It is recorded here, not bundled.

## Why this matters

LE31 has no customer accounts, no customer money, and — by charter — no customer identity. So this pick is not a gap in a roadmap; it is a mechanism that would have to **create** a concept the charter currently excludes. That is exactly why it is recorded as `defer` with the tension stated rather than quietly filed as a future feature.

The value of recording it now is that the **§3.2 tension is worth surfacing while it is cheap.** If LE31 ever wants to accept a prepayment — which is a real thing small restaurants do informally, in a notebook — the question of where that money lives, how long it lives, and whether it is tied to a person at all, is a charter decision. The source answers it one way (a customer ledger). LE31 might answer it another (an anonymous till-scoped balance). Having the mechanism on file means the question gets asked with a reference in hand rather than invented from scratch.

Two things this contract deliberately refuses to do. It does not resolve the privacy boundary, because the charter is the owner's document and §3.2's line about guest demographics is unambiguous enough that the resolution must be deliberate. And it does not pretend the source's design is more specified than it is: the matching rule, the partial-allocation case, the expiry rule, the customer-identity model and the draft-invoice model are all named as open questions rather than invented.

The honest summary is that this is the weakest of today's three picks on fit — it is the only one with a charter tension rather than merely a missing concept — and it is filed for exactly that reason. The corpus did not have a place to record "an operator-facing mechanism that LE31 might want but cannot have without a charter decision", and this is that place.
