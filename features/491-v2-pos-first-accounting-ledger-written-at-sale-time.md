# Feature 491 — `v2-pos-first-accounting-ledger-written-at-sale-time`

> **Pick C of Daily Research 2026-11-17.** **Bucket: v2 (new owner-accounting domain).** **Verdict: `defer` — product-pattern reference only.**
>
> **Source artifact:** `yegobox/flipper` — ★17 / ⑂7, Dart/Flutter, created 2018-12-01, pushed 2026-11-17. GitHub license metadata is `NOASSERTION`; the README says the monorepo is source-available and that backend services and keys are private. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-17/repos/06_yegobox_flipper.json`; README: `/tmp/le31-daily-2026-11-17/readme/06_yegobox_flipper.md`; source URL: https://github.com/yegobox/flipper.
>
> **Why this pick:** the source states one crisp product invariant that removes a whole class of reconciliation ambiguity: the accounting ledger is written when the sale happens, so there is no month-end import.

## Goal

Record the sale-time accounting-posting pattern as the reference for a possible future LE31 v2 owner-accounting surface:

1. a sale produces its accounting consequence at the point of sale;
2. month-end is a reporting period, not a data-import event;
3. the accounting ledger remains distinct from the stock ledger.

No accounting table, endpoint, import, export, or bot command is authorized by this feature.

## Scope

**In scope (defer artifact):**

- The source artifact's three-line product invariant, quoted.
- The boundary between an accounting journal and LE31's `StockEntry`.
- The license/traction caveat: pattern reference only, no code or dependency.

**Out of scope (defer artifact):**

- No chart of accounts, journal, account, balance, P&L, balance-sheet, invoice, expense, recurring-entry, or tax-compliance model.
- No month-end import, accounting export, QuickBooks/Xero integration, or accountant handoff.
- No adoption of the Flutter/Dart codebase or any private backend.
- No v1 scope expansion.

## Description

Flipper's README states:

- *"Flipper Books (accounting) ... every POS sale posts a journal entry at sale time; expenses, recurring entries, P&L and balance sheet"*.
- *"POS-first accounting — no month-end import; the ledger is written as you sell."*
- *"Works offline — every sale is saved on the device first and synced when a connection is available."*
- *"One account, every app — a cashier in POS is the same identity in Books and HR."*

The transferable mechanism is **posting at the source event**. A later import has to reconcile two histories: what the POS believes happened and what the ledger believes happened. Posting at sale time leaves one history, at the cost of requiring accounting rules to be available inside the sale transaction.

For LE31 the critical boundary is categorical: `StockEntry` records **quantity movement**; an accounting journal records **financial consequence**. Feature 441 already records that a sale may post its own journal entry carrying the document it came from, but LE31 itself has no accounting model. This feature does not introduce one.

## Data model

No schema change. The future reference shape, explicitly **not proposed today**, would distinguish:

```text
JournalEntry (future reference)
  id, occurred_at, source_order_ref, source_document_ref,
  account_ref, amount_eur, currency, idempotency_key
```

The accounting ledger is a second, separate history. It must never be folded into `StockEntry`, and its rules must never be used to derive stock quantity.

## Implementation

None in this feature. When owner accounting is promoted into a scoped v2 feature:

1. Define the chart-of-accounts vocabulary and the minimum journal shape.
2. Define how a sale, refund, waste event, and stock correction map to financial entries.
3. Decide whether posting happens in the same transaction as the sale or through an atomic, idempotent outbox.
4. Define month-end as reporting only.
5. Keep the journal and `StockEntry` as separate ledgers with explicit links.
6. Define accountant-facing export and the human-review gate before anything is submitted outside LE31.

## Telegram interaction

None. Accounting is an owner surface, not a cook-bot interaction.

## Dependencies

- Existing feature 441 — sale-to-ledger provenance and the separation of stock and accounting facts.
- Existing features 303 and 259 — double-entry / transactional-outbox vocabulary already in the corpus.
- Existing feature 166 — human-review-before-posting posture for accounting tools.
- Existing feature 413 — attempted/outcome audit vocabulary for cross-system writes.
- No new packages and no source-code dependency.

## Open questions

1. Is owner accounting a real v2 need, or should LE31 leave books to a specialist?
2. If adopted, what is the minimum viable chart of accounts for a small restaurant?
3. Must a journal post atomically with the sale, or may it post through an idempotent outbox?
4. How are refunds, waste, and corrections represented financially?
5. What accountant-facing artifact is actually needed: export, report, or human-readable statement?
6. Which external system, if any, is the eventual destination, and what human gate governs submission?

## Why this matters

Owner accounting is one of the largest natural v2 expansions for a restaurant system, and it is also one where a late, imported ledger creates reconciliation ambiguity. The sale-time posting pattern is a clear answer to that architectural question before the accounting model is written.

The evidence is nevertheless limited: Flipper is a source-available commercial product whose backend is private and whose license is `NOASSERTION`. It is useful as a **product-pattern reference**, not as a code source. The value is the invariant, not the implementation.
