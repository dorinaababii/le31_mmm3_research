# Feature 489 — `v1-idempotent-receiving-and-derived-stock-movement-ledger`

> **Pick A of Daily Research 2026-11-17.** **Bucket: v1.** **Verdict: `defer` — parking-lot vocabulary reference.**
>
> **Source artifact:** `ShahabAhmed01/apexPOS` — MIT, ★1 / ⑂1, TypeScript/Electron/React/SQLite, created 2026-09-17, pushed 2026-11-12. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-17/repos/08_ShahabAhmed01_apexPOS.json`; README: `/tmp/le31-daily-2026-11-17/readme/08_ShahabAhmed01_apexPOS.md`; source URL: https://github.com/ShahabAhmed01/apexPOS.
>
> **Why this pick:** one compact README states three mechanisms as one operating model — purchase-order receiving is idempotent; on-hand stock is derived from a movement ledger; adjustments/waste are explicit authorized events. The combination is net-new in LE31's corpus even though each individual word is familiar.
>
> **Boundary:** LE31 already owns the append-only `StockEntry` ledger and derive-current-stock rule (features 373 and 374). This feature does **not** replace or duplicate them. It records the *receiving-side* vocabulary for a future supplier-receiving scope.

## Goal

When a future LE31 scope introduces supplier or purchase-order receiving, ensure that:

1. receiving the same delivery twice cannot create two stock movements;
2. on-hand stock remains `opening + Σ movements`, never a separately edited balance;
3. corrections and waste are explicit manager-authorized ledger events, not edits to a prior receipt.

No production code is authorized by this feature. It is a reference contract for a future receiving feature.

## Scope

**In scope (defer artifact):**

- Record the source artifact's three-mechanism combination with verbatim evidence.
- Record the boundary against features 373, 374, 400, 421 and 432.
- State the trigger for promoting this vocabulary into a scoped implementation.

**Out of scope (defer artifact):**

- No supplier, purchase-order, product, supplier-invoice, warehouse, or receiving table.
- No LE31 API route or Telegram command.
- No adoption of apexPOS code, Electron, React, TypeScript, or SQLite-specific implementation.
- No change to `StockEntry`, `Batch.qty_remaining`, or the append-only rule.
- No receiving implementation in v1 while the charter has no supplier-receiving surface.

## Description

apexPOS describes a hybrid retail/restaurant desktop POS. The relevant README statements are:

- *"Purchasing — suppliers, purchase orders (draft → sent → partially received → received / cancelled), idempotent receiving, weighted-average costing, branch-scoped"*.
- *"Inventory — product catalog, stock movement ledger (opening + Σ movements = on-hand), low-stock alerts, manager-authorized stock adjustments / waste"*.
- *"Adversarially hardened — money, refunds, register cash, modifier pricing, sessions/lock, branch scope, IPC fuzzing, and multi-process races all regression-tested"*.

The transferable pattern is the coupling of three rules:

1. **The receipt is an idempotent operation.** A repeated delivery event must resolve to the same inventory fact.
2. **The balance is derived.** Receipt and movement events determine on-hand stock; they do not patch a mutable quantity.
3. **Correction is an authorized event.** A manager records an adjustment/waste event; nobody edits the receipt that caused the discrepancy.

This is a stronger and more operational statement than a generic inventory ledger because it names the receiving boundary and the authorization boundary.

## Data model

No schema change. The reference shape for a future receiving feature would be:

```text
StockReceipt / purchase receipt (reference; NOT proposed here)
  id, purchase_order_ref, received_at, idempotency_key, actor_id
Stock movement (LE31's existing StockEntry)
  batch_id, qty_delta, reason, ref_order_item_id, by_user_id, at
```

The required rule is that on-hand quantity is derived from movement events and that a receipt cannot be applied twice. Whether a separate receipt table is needed, or whether a receipt is merely a typed set of `StockEntry` rows, remains a future decision.

## Implementation

None in this feature. When a future receiving feature is approved:

1. Define one idempotency namespace for receipt attempts.
2. Make the receipt application atomic with the movement rows it creates.
3. Derive on-hand quantity; never maintain a second mutable balance.
4. Represent adjustments and waste as explicit authorized ledger events.
5. Add regression tests for duplicate receipt, partial receipt, and unauthorized adjustment.

## Telegram interaction

None. Supplier receiving is not a cook-bot interaction, and adding a cook command would cross the two-role charter boundary.

## Dependencies

- Existing feature 373 — derive-never-store and integer-money/offline vocabulary.
- Existing feature 374 — persisted `qty_remaining` contradiction; source of the derive rule.
- Existing feature 400 — void/reversal and client-minted idempotency vocabulary.
- Existing feature 421 — the single `StockEntry` write path and append-only linter rule.
- Existing feature 432 — reason/sign coherence.
- No new packages and no external service.

## Open questions

1. Is supplier receiving in LE31's product scope at all, or should the future scope remain kitchen-consumption only?
2. If receiving is added, is a purchase-order table necessary, or is a receipt event enough?
3. Which actor may authorize waste and stock adjustments: owner only, or manager too?
4. Should partial receipts create distinct movements or one movement per receipt event?
5. Does the weighted-average costing vocabulary belong to the same future scope, or should costing remain separate?

## Why this matters

LE31's hardest stock rules are already written down. The missing piece is the **receiving boundary**: where goods enter, how a duplicate delivery is prevented, and how an incorrect receipt is corrected without editing history. apexPOS states that boundary in three lines and backs it with a movement ledger and manager authorization.

The pick is filed as a reference, not a build, because no LE31 operator has asked for supplier receiving and the current charter's surface count does not include it. The value is having a compact, source-backed answer ready when that scope is opened.
