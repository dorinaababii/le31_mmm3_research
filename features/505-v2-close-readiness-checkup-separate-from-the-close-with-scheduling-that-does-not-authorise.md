# Feature 505 — `v2-close-readiness-checkup-separate-from-the-close-with-scheduling-that-does-not-authorise`

> **Pick B of Daily Research 2026-11-20.** **Bucket: v2.** **Verdict: `defer` — parking-lot vocabulary reference.**
>
> **Source artifact:** `giltotherescue/slashbooks` — Apache-2.0, ★40 / ⑂6, Python, created 2026-06-18, pushed 2026-11-20T03:08:39Z, 9,959 KB, `default_branch=main`, `archived=False`. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-20/gh/repo_41_giltotherescue_slashbooks.json`; README (base64-decoded): `/tmp/le31-daily-2026-11-20/gh/readme_plain/plain_41_giltotherescue_slashbooks.md`; source URL: https://github.com/giltotherescue/slashbooks.
>
> **Why this pick:** one README separates two things the LE31 corpus treats as one, and states the separating rule flatly — *"Schedule authorized bookkeeping preparation with current books ready for review; **final close requires explicit authorization**."* The workflow tree lists a **readiness review** *"/books-checkup      review setup, mappings, and close readiness"* **separately** from the close itself *"/books-close        import activity, review unknowns, and finalize a period"*. The governing sentence is unambiguous: *"**Scheduling does not authorize a close, publication, or money movement.**"*
>
> **Why it is net-new:** the parent ran a targeted dedup sweep across all **1,034 feature and spec files** in the repository before selecting this pick: `close readiness` → **0 files**; `books.?checkup` → **0 files**; `schedul\w*.{0,60}authoriz` → **0 files**; `unknowns` → **0 files**; `explicit authoriz\w* to clos` → 17 hits across 13 files, **every one about an order or a bill transition** (features 502, 443, 408, 173) and **none about a period close**; `trial balance` → 1 hit, and it is in yesterday's Pick C contract rather than an implementation; `reconciliation` → 35 hits across 29 files, **none pairing a readiness review with a separate finalisation**. The **readiness-then-authorise** pair has never been written down in the corpus.
>
> **Boundary with feature 426 (`le31-shift-close-lifecycle`):** 426 owns **the close transition itself** — a shift's close. This pick owns **the gate in front of a close**, for a *period* rather than a shift.
>
> **Boundary with yesterday's Pick C (`v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface`):** yesterday's pick owns **the register that produces reconciliation identities**. This pick owns **the readiness review that must pass before a period can be finalised**. They are two halves of one future slice, described from two sides.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **close-readiness discipline** as the reference design for any future LE31 period-closing surface:

1. **preparation and finalisation are different operations** — a period can be prepared, reviewed and left open, without ever being closed;
2. a **readiness checkup is a separate, repeatable review** — it is not a dry run of the close, and it can be run many times;
3. the checkup's output is a list of **what needs attention**, not a verdict and not a number;
4. **the close requires explicit authorisation** that is distinct from the act of preparing the work;
5. **scheduling never authorises** — a scheduled preparation, a cron job, or an agent waking up on a schedule may prepare and may even report, but **may not close, publish, or move money**;
6. **unexplained entries are surfaced for classification** before they become trusted — *"review unknowns"* is a named step, not an accident;
7. an **export is gated on a saved reconciliation** — *"Reconcile each bank account first; export needs a saved reconciliation."* — so a downstream artefact cannot be produced from an unchecked state.

No readiness model, no checkup surface, no scheduler and no close implementation is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the seven-point mechanism summary above.
- The dedup result that establishes the mechanism is net-new to the corpus (`close readiness` → 0 files).
- The explicit boundary with feature 426 (the close transition) and with yesterday's Pick C (the register).
- The load-bearing sentence of the design, stated once: **scheduling does not authorise a close, publication, or money movement.**
- The ordering constraint that the readiness gate sits *upstream* of yesterday's cross-ledger register and *upstream* of any export.
- A future-project attachment decision: `le31 Research`, because no v2 project exists and this is not v1 work today.

## Out of scope

- No readiness model, no checkup implementation, no scheduler, no schema change.
- No change to the waiter web UI, the cook Telegram bot, the `StockEntry` ledger, or the bill lifecycle.
- No change to how the **shift** close works — feature 426 owns that, and this pick is about a *period*, not a shift.
- No accounting-period concept. LE31 has no books, no fiscal year, no tax return, and no general ledger.
- No import of the source's QuickBooks / Stripe / Mercury connectors, or its Beancount export format.
- No agent workflow, no `books` CLI, no MCP surface. The source's *"the agent workflows call the `books` CLI and don't compute financial totals themselves"* is recorded as a **design principle**, not as something to copy.
- **No resolution of whether LE31 ever needs a period close.** That is a charter question and this contract does not answer it.

## Description

The source artifact's README states the mechanism in four places, verbatim:

> *"Schedule authorized bookkeeping preparation with current books ready for review; **final close requires explicit authorization**."*
> *"**`/books-checkup`      review setup, mappings, and close readiness**"* — listed **separately** from *"**`/books-close`        import activity, review unknowns, and finalize a period**"*
> *"**Scheduling does not authorize a close, publication, or money movement.**"*
> *"Reconcile each bank account first; **export needs a saved reconciliation**."*

And the question the design exists to answer, in the source's own words: *"Ask about recorded income, expenses, unpaid balances, overdue amounts, or **what needs attention before close**."*

**1. Two operations, not one.** Almost every accounting tool conflates "do the work" with "finalise the result". The source does not. Preparation is scheduled and repeatable; the close is a separate, explicit act. The checkup is a **third** thing again — it is a *review* whose output is a list, not an action.

**2. The checkup's output is a list of what needs attention.** Not a score, not a pass/fail, not a number that must be compared to a threshold. It is an enumeration of open items: unpaid balances, overdue amounts, unknown transactions. This is what makes it *repeatable*: running a checkup twice is free and produces the same kind of answer, whereas running a close twice is a state transition you cannot undo.

**3. "Unknowns" are a named step.** *"import activity, review unknowns, and finalize a period"* — the close has a middle stage in which entries the system cannot classify are surfaced. The source also says *"Review unfamiliar transactions before they become trusted rules."* The design treats an unexplained entry as **a thing to look at**, not as something to silently round, default, or drop. That is the same posture LE31's charter takes toward stock reasons (feature 432) and money precision (feature 411).

**4. Scheduling is explicitly not authority.** This is the sentence the whole artifact exists for: *"Scheduling does not authorize a close, publication, or money movement."* The source is an **AI-agent** product, and the rule is about the agent specifically — an agent that wakes on a cron may prepare the books and may report, but the human's authorisation is a separate input that the schedule cannot supply. LE31's charter §3.1 already says *"operational transitions are explicit user actions. Do not silently send, serve, close, or reconcile an order."* **This pick applies that rule to a period** — and the corpus does not do that anywhere.

**5. Exports are gated on reconciliation.** *"Reconcile each bank account first; export needs a saved reconciliation."* The downstream artefact — the thing a tax preparer or an accountant consumes — may not be produced from an unreconciled state. LE31 feature 496 already says the export must carry the reconciliation identities that were checked. **This pick names the gate in front of them.**

**Why the source's own limits are recorded rather than hidden.** The README does not specify the checkup's rule set, what makes an item "needs attention", how authorisation is represented, or how the checkup's output is presented. So this contract records a **shape**, not a copyable design. A future implementation would have to specify all four, and this contract is honest that they are unspecified.

**Adjacent but not owned.** The source also ships *"Keep the ledger in a local SQLite store you own, with Beancount-style exports when you need plain text"*, *"Accrue estimates that reverse themselves or are trued up to the actual bill"*, and *"Spread annual software or insurance costs across their service months"*. The accrual vocabulary is LE31-unrelated (2 corpus hits, both incidental); the plain-text export is feature 496's territory; and the accrual machinery is **not** transferred. None is bundled.

## Data model

**None is created by this feature.** The following is a *reference shape* recorded for a future implementation, and it is deliberately not a schema:

```
ReadinessCheckup
  checkup_id       opaque identifier
  period_ref       the period being reviewed
  run_at           timezone-aware instant
  items_need_attention   the open items the checkup surfaced

CloseAuthorisation
  period_ref       the period being closed
  authorised_by   who authorised it
  authorised_at   when
  basis           the saved reconciliation the authorisation rests on
```

**The load-bearing sentence, stated once, as the contract's design:** *a scheduled or automated preparation may produce a readiness checkup and may report it; it may not produce a close authorisation, and the close may not occur without one.*

**The reference shape is deliberately incomplete**, and the gaps are named rather than guessed: the **checkup's rule set** is unspecified (what makes an item "needs attention"); the **presentation** of the item list is unspecified; the **authorisation's form** is unspecified (a click, a typed confirmation, a separate recorded act); and the **relationship between a checkup and a close** is unspecified (must a checkup pass immediately before the close, or is any saved checkup sufficient?). An implementer must decide all four and record the decision. A contract that guessed them would be worse than one that names them.

## Implementation

**No implementation is authorised by this feature.** It is a `defer` reference.

If a future feature is separately approved, the plausible touch points would be:

- `backend/app/models.py` — future `ReadinessCheckup` and `CloseAuthorisation` models;
- `backend/app/services/readiness.py` — future rule evaluation producing the items-needing-attention list;
- `backend/app/services/close.py` — future close gate: refuse a close without a prior authorisation;
- `backend/app/routers/periods.py` — future checkup and close routes;
- the waiter/owner UI — future "what needs attention before close" surface;
- tests — a scheduled preparation cannot authorise; a close without authorisation is refused; a checkup can be run repeatedly; an export without a saved reconciliation is refused.

**Ordering constraint (not optional).** A future implementation must land **after** yesterday's Pick C (`v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface`, feature 500) — the readiness gate needs the register that produces the identities it checks — and **after** feature 496 (`audit-ready-daily-export-with-financial-reconciliation-identities`), whose export is what the gate protects. Building the gate before the register gives a readiness checkup with nothing to check.

## Telegram interaction

**None.** The cook Telegram bot is not a consumer of a readiness checkup in this disposition, and no bot command is added. A future owner-facing "what needs attention before close" message would need its own owner decision and its own chat-id allowlist treatment (feature 403). Note that the charter forbids the bot from *acting* on operational state without an explicit user action, so a checkup that merely **reports** is compatible with §3.1 while a checkup that *closes* is not.

## Dependencies

**Existing LE31 features this pick depends on or is adjacent to:**

- **Feature 500** (`v2-cross-ledger-voucher-register-as-the-single-reconciliation-surface`) — owns the register that produces reconciliation identities. **Prerequisite.** The readiness gate checks what the register produces.
- **Feature 496** (`audit-ready-daily-export-with-financial-reconciliation-identities`) — owns the export whose reconciliation requirement this pick's gate protects. **Prerequisite.**
- **Feature 426** (`le31-shift-close-lifecycle`) — owns the shift close. **Adjacent.** A shift close is a different granularity from a period close; the source's rule is about periods.
- **Feature 391** (`le31-shift-variance-stored-no-derivation-no-payment-table`) — the shift variance is one of the items a readiness checkup would surface. **Adjacent.**
- **Feature 403** (`role-carrying-bot-chat-table`) — an actor is needed for "who authorised". **Adjacent.**
- **Feature 432** (`le31-stockentry-reason-sign-coherence`) — the "review unknowns before they become trusted rules" posture is the same discipline as a stock reason's sign coherence. **Adjacent.**

**External dependency:** none. The source artifact is an Apache-2.0-licensed reference, not a code dependency; nothing is imported.

## Open questions

1. **Does LE31 ever have a period to close?** A single-operator restaurant with a shift close and a daily export may never need a weekly or monthly close. If the answer is "never", this pick should be deleted rather than deferred.
2. **What is the checkup's rule set?** The source does not specify what makes an item "needs attention". This is the substance of the feature and it is entirely unspecified by the source.
3. **Must a checkup pass immediately before the close, or is any saved checkup sufficient?** The former is a tight gate; the latter permits a stale checkup to authorise a close.
4. **How is authorisation represented** — a click, a typed confirmation, a separate recorded act? The source requires "explicit authorization" without saying what that looks like.
5. **What is a "period" for LE31** — a business day in `Europe/Paris` (charter §3.5), a week, a month, a fiscal quarter? This is a business-time question the charter has not answered.
6. **Does the source's "review unfamiliar transactions before they become trusted rules" apply to LE31 at all?** LE31 has no learned rules; the analogous risk is a default that silently classifies an unexplained entry. The discipline transfers, the mechanism does not.
7. **Is the "unknowns" stage about classification or about the human's attention?** The source treats unfamiliar transactions as a review queue; LE31's unknowns would more likely be malformed rows. These are different problems with the same name.

## Why this matters

LE31's charter already holds the principle this pick records — §3.1, *"operational transitions are explicit user actions"*. What the corpus does not have is the **gate between preparation and finalisation**: a repeatable review whose output is a list of what needs attention, and a rule that an automated schedule can never supply the authorisation. In a system where an agent (this very research pipeline) runs on a cron, that distinction is not academic.

The value of recording it now, while it is still a `defer`, is that **the gate is cheap to get right on paper and expensive to get wrong in code**. A close that a scheduler can trigger is not a close that a human authorised — and the failure mode is silent: the books close, the numbers are wrong, and nothing in the log says a human did not agree. The source states the rule in one sentence, and that sentence is the entire transferable content.

Two things this contract deliberately refuses to do. It does not invent an accounting period for LE31, because the charter has not said there is one and a single-operator restaurant may never need one. And it does not pretend the source's design is more specified than it is: the checkup's rule set, the presentation, the authorisation form and the checkup-to-close relationship are all named as open questions rather than invented.

The honest summary is that this is the **second consecutive defer on the reconciliation theme**, and that is itself the signal. Yesterday established the register; today establishes the gate in front of it. A third contract on the same theme would be refining a vocabulary that has no caller. The pair is worth holding; a third piece is not.
