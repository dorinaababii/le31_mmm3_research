# Feature 500 — `v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface`

> **Pick C of Daily Research 2026-11-19.** **Bucket: v2 (new bucket — justified below).** **Verdict: `defer` — parking-lot vocabulary reference.**
>
> **Source artifact:** `nikhilb2/simple-invoicing-free-gst-billing-software` — MIT, ★22 / ⑂80, created 2026-03-29, pushed 2026-11-18T16:00:00Z (the same artifact as feature 499; a *different* mechanism in a *different* domain). Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-19/gh/repo_07_nikhilb2_simple-invoicing-free-gst-billing-software.json`; README: `/tmp/le31-daily-2026-11-19/gh/readme_07_nikhilb2_simple-invoicing-free-gst-billing-software.md`; source URL: https://github.com/nikhilb2/simple-invoicing-free-gst-billing-software.
>
> **Why this pick:** one README line states a **single reconciliation surface** across every ledger — *"Day Book Register — Cross-ledger voucher register for reconciliation"* — and the same README exposes it in the API listing as *"Ledgers, statements, day book, tax ledger, GSTR-1 and the GSTR-3B worksheet"*. LE31 has per-domain append-only ledgers and, since yesterday, an export that *asserts* reconciliation identities (feature 496) — but **nothing that produces them from one place**.
>
> **Why it is net-new:** the parent ran a targeted dedup sweep across all **1,022 feature and spec files**: `day ?book` → **0 files**; `voucher register` → **0**; `cross-ledger` → **1** (feature 81 `append-only-immutable-audit-check`, whose single mention is a hash-chain verification walk over the `StockEntry` ledger — a **single**-ledger integrity check, not a cross-ledger register); `(all|across).{0,20}ledgers.{0,30}register` → **0**. The concept of *one register spanning every ledger, existing to reconcile them*, has never been written down.
>
> **Boundary with feature 496 (`audit-ready-daily-export-with-financial-reconciliation-identities`), filed 2026-11-18:** this pick is **upstream of** it, not a duplicate of it. Feature 496 owns the **export** — the flat file that carries the reconciliation identities an accountant opens. This pick owns the **register that produces them**. Shipping 496 without a register produces identities asserted without a producer: the export would state equations that nothing computes.
>
> **Boundary with feature 81 (`append-only-immutable-audit-check`):** feature 81 walks one ledger's hash chain to prove integrity. This pick spans ledgers to reconcile them. A register built from per-ledger chains does not replace 81; it consumes what 81 verifies.
>
> **Bucket justification (new bucket):** no existing bucket covers "a cross-ledger read model for reconciliation". It is not v1 (the charter's owner-facing surface is the waiter UI and the cook bot; a register is neither), not v2 owner-pains (it is a read model, not a workflow), and not v2-AI (no model involved). Recorded as **v2** because it arrives with the accounting/reporting scope LE31 defers past v1.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **cross-ledger register** as the reference design for any future LE31 reconciliation surface:

1. there is **one** register that spans **every** ledger, not one view per ledger;
2. the register is a **voucher register** — each entry is a voucher (a balanced movement), not a raw row from a domain table;
3. the register exists **for reconciliation** — its purpose is to let a reader check that the ledgers agree, and that is the reason it is a separate surface rather than a query;
4. the register is **read-only over the ledgers**: it is a read model, and the ledgers remain the source of truth;
5. the register is exposed as **one endpoint/surface**, not as a family of per-ledger reports;
6. the register is the thing from which the **other** accounting artefacts are derived (statements, returns, period worksheets) — it is upstream of them, not a peer.

No register, no voucher model, no read model and no reconciliation endpoint is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the six-point mechanism summary above.
- The explicit **upstream-of-feature-496** boundary, stated in both directions.
- The dedup result that establishes the mechanism is net-new to the corpus.
- The explicit boundary with feature 81 (single-ledger integrity) and with features 373/374 (the append-only `StockEntry` ledger and derive-current-stock rule), which the register must not become a second source of.
- The requirement that the register is **derived**, never independently written to.
- A future-project attachment decision: `le31 Research`, because no v2 project exists and this pick is not v1 work today.

## Out of scope

- No register table, no voucher model, no read model, no endpoint.
- No tax ledger, no GSTR-1 or GSTR-3B worksheet, no period close, no trial balance, no balance sheet, no ageing, no cash-flow statement. The source's accounting breadth is **not** carried over; only the cross-ledger register shape is.
- No change to the append-only `StockEntry` ledger, the derive-current-stock rule, or the bill lifecycle.
- No change to feature 496's export format or its reconciliation identities.
- No multi-currency and no currency revaluation (the source has both; LE31 is single-currency per §3.1).
- No adoption of the source's data model, its number-series format, or its GST tax model.

## Description

The source README states the mechanism twice — once as a feature bullet, once in the API listing — and the two statements together define it:

> *"**Day Book Register** — Cross-ledger voucher register for reconciliation"*

> *"`/api/ledgers` | Ledgers, statements, day book, tax ledger, GSTR-1 and the GSTR-3B worksheet (an estimate, not a filing)"*

**The observation that makes this worth recording.** LE31 does not have a ledger problem. It has a *reconciliation* problem, and the two are different. LE31's ledger is exactly what it should be: append-only, derived-from-movements, hard to corrupt (features 373, 374, 470). The weakness is that reconciliation in LE31 today is a **claim** rather than a **computation**. Feature 496 — filed yesterday — specifies an export that "carries explicit financial reconciliation identities — named equations relating a total to its components", and its own contract says the identities are "stated in the artifact, so a reader knows what was checked". But a stated identity is not a checked identity. Someone has to evaluate it, and the report does not say from what.

The source answers that question structurally: there is **one register**, spanning every ledger, holding **vouchers** (balanced movements), and its stated purpose is reconciliation. Every other artefact — statements, returns, worksheets — is derived from it. That ordering is the transferable part. It is a **single point of truth for "do the ledgers agree?"**, and it is a *read model over the ledgers*, not a second place where transactions live.

**Why "voucher" and not "row".** A voucher is a **balanced movement** — the accounting unit that can be summed, netted and reconciled. LE31's `StockEntry` rows are movements of *stock*, not balanced vouchers; a bill is a total, not a debit/credit pair. A register of raw domain rows would not reconcile anything; it would just be a union view. The voucher concept is what makes the register a reconciliation instrument rather than a reporting convenience.

**Why one surface and not several.** The source's value is that the day book is *cross-ledger*: it spans ledgers rather than presenting each one separately. Per-ledger statements answer "what happened in this ledger"; a cross-ledger register answers "do the ledgers agree with each other", which is a question no single-ledger statement can answer.

**What the source does not specify, and this contract therefore does not guess.** The README does not define the voucher's structure, does not say how a voucher is derived from LE31-shaped ledgers (which have no debit/credit columns), does not say whether the register is materialised or computed on read, and does not say how the reconciliation identities are evaluated against it. Those are the four decisions a future implementation must make and record.

**A caution this contract records deliberately.** A cross-ledger register is a *derived* artefact. If it is ever written to directly, it becomes a second source of truth and the reconciliation it exists to perform becomes meaningless — a register that can disagree with the ledgers by construction cannot detect disagreement. The "read-only over the ledgers" property is therefore load-bearing, not decorative.

**Adjacent but not owned.** The same source describes *"Day Book Register"* alongside *"GSTR-1 and the GSTR-3B worksheet (an estimate, not a filing)"*. The parenthetical is worth noting as a design precedent — *an estimate, explicitly not a filing* — but the statutory-reporting scope is excluded from this pick and is not bundled.

## Data model

**None is created by this feature.** The following is a *reference shape* recorded for a future implementation, and it is deliberately not a schema:

```
LedgerVoucher
  voucher_id       opaque identifier
  voucher_date     the business date the voucher belongs to
  ledger_ref       which source ledger the voucher came from
  lines            balanced debit/credit-style lines, summing to zero

ReconciliationIdentity
  identity_ref     which named equation this is
  left_expr        a total, derived from vouchers
  right_expr       its components, derived from vouchers
  holds            whether the identity holds for the period
```

**The two rules, stated once each, as the contract's load-bearing sentences:**

1. *The register is **derived** from the ledgers; there is **no** write path that creates or amends a voucher independently of a ledger movement.*
2. *A reconciliation identity is **evaluated** against the register; a register row that is merely written down is not an identity and cannot fail.*

**The reference shape is deliberately incomplete**, and the gaps are named rather than guessed: the **voucher structure** is unspecified (in particular, how a balanced movement is expressed over LE31 ledgers that have no debit/credit columns); **materialised vs. computed-on-read** is unspecified; the **period boundary** and whether an open period can be reconciled are unspecified; and how a **failed** identity surfaces (fail-visible, as feature 496 requires, vs. a warning) is unspecified. An implementer must decide all four and record the decision.

## Implementation

**No implementation is authorised by this feature.** It is a `defer` reference.

If a future feature is separately approved, the plausible touch points would be:

- `backend/app/models.py` — future `LedgerVoucher` view/table, if the register is materialised;
- `backend/app/services/reconciliation.py` — future voucher derivation and identity evaluation;
- `backend/app/routers/reconciliation.py` — future single register endpoint and identity evaluation endpoint;
- `backend/app/services/export.py` — the **future** call site where feature 496's export would source its identities from this register rather than asserting them;
- tests — voucher lines balance, register is a pure function of ledger state, identity evaluation fails visibly, register cannot be written to directly.

**Ordering constraint.** A future implementation must land **before** feature 496 is built, not after. Feature 496 exports identities; if it is built first, the identities are asserted by the export itself and the register arrives later to a surface that already claims to be checking. A register that is upstream of an export and arrives afterwards is a retrofit; the same register arriving first is the design.

## Telegram interaction

**None.** The cook Telegram bot is not a consumer of the register in this disposition, and no bot command is added. A future owner-facing "did the day balance?" surface would be a separate feature and would need its own actor model (feature 403) and its own chat-id allowlist decision.

## Dependencies

**Existing LE31 features this pick depends on or is adjacent to:**

- **Feature 496** (`audit-ready-daily-export-with-financial-reconciliation-identities`) — **this pick is upstream of it.** 496 is the export; this is the register that produces the identities it exports. **Ordering constraint.**
- **Feature 373** (`append-only-stock-ledger`) and **feature 374** (`derive-current-stock`) — the ledgers the register reads. **Prerequisite.**
- **Feature 470** (`ledger-delete-guard`) — the register must not be a way around the append-only guard. **Adjacent.**
- **Feature 81** (`append-only-immutable-audit-check`) — single-ledger integrity; the register consumes what 81 verifies. **Adjacent, not owned.**
- **Feature 391** (`shift-variance-derivation`) and **feature 426** (`shift-close-lifecycle`) — the money-side ledgers a register would span. **Adjacent.**
- **Feature 403** (`role-carrying-bot-chat-table`) — the actor for a future owner-facing register surface. **Adjacent.**
- **Feature 499** (`quotation-on-its-own-number-series`) — a converted offer's invoice lands in the register. **Adjacent, and recorded separately.**

**External dependency:** none. The source artifact is a MIT-licensed reference, not a code dependency; nothing is imported.

## Open questions

1. **Does a cross-ledger register make sense over LE31's ledger shapes at all?** LE31 has stock movements and bill totals, not debit/credit pairs. A "voucher" may need to be defined, not borrowed — and it is possible the honest answer is that LE31 has two ledgers, not a set, and a register over two things is a spreadsheet.
2. **Materialised or computed on read?** A materialised register is fast and can drift; a computed one is always true and is expensive. The source does not say.
3. **What is the period boundary?** A service day, an accounting period, a calendar day? LE31's service-day concept (feature 448's number series is `<service-day>-<sequence>`) hints at the answer but does not establish it.
4. **How does a voucher balance over stock?** A stock movement has a quantity, not a debit and a credit. The correspondence is unclear and is the central design question.
5. **Can an open period be reconciled?** If a visit is still open, its bill does not exist yet. The register must state what it does with open periods, and the source is silent.
6. **Is this worth building at all after feature 496?** If the export's identities are evaluated directly against the ledgers by a single function, a separate register may be unnecessary machinery. That is a legitimate argument for deleting this feature rather than deferring it.

## Why this matters

Feature 496 was filed yesterday with a note that its identities are "stated in the artifact, so a reader knows what was checked". That phrasing contains the gap this pick names: an accountant reading the export is being *told* what was checked, and is being asked to trust it. There is a real difference between *stating* an identity and *evaluating* it, and the difference is exactly where a reconciliation goes wrong — quietly, at the end of a long service, when nobody re-adds the columns.

The source artifact's answer is a design that LE31 has not chosen: one register, spanning every ledger, holding balanced vouchers, read-only over the ledgers, existing for the single purpose of letting a reader check that the ledgers agree. That is a **provenance-bearing** answer to the owner's actual question — "did the day balance?" — and it is the same shape as the append-only discipline LE31 already applies to stock, applied to *money across domains* for the first time.

There is also an honest counter-argument, recorded in the open questions rather than hidden: LE31 may simply have two ledgers, not a set, and a register over two things could be a spreadsheet with extra steps. **A legitimate outcome of this feature is that it is deleted at review**, because the vocabulary showed the shape was not needed. That is a better use of the pass than a contract that pretends the shape fits.

What is not in doubt is the ordering: if LE31 ever builds feature 496, this register should exist *underneath* it, not arrive afterwards to retrofit a surface that already claims to be checking.
