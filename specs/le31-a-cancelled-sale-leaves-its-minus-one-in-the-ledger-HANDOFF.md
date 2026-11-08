# HANDOFF — Feature 461: a cancelled sale leaves its `-1` in the ledger

> **Slice contract for the coding agent.** Feature: `features/461-le31-a-cancelled-sale-leaves-its-minus-one-in-the-ledger-stockreason-has-no-reversal-member.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (executed against LE31's real schema on 2026-11-08).
> Filed by: Daily Brainstorm 2026-11-08 (99th daily-brainstorm pass), Pick C.

---

## 1. The active feature path

```
features/461-le31-a-cancelled-sale-leaves-its-minus-one-in-the-ledger-stockreason-has-no-reversal-member.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 374 / 432 / 426 / 417 / 421 / 382 / 419 / 459, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | Executed against LE31's real schema. A `StockEntry(qty_delta=-1, reason='sale')`; the order line is then set to `status='cancelled'`; **the ledger row is still there and nothing was written back.** `SUM(qty_delta)` for the batch = **−1** — the batch is one short and the ledger cannot say why. |
| 2 | The defect is in LE31's own code | **PASS** | `backend/app/models.py` lines 57–61: `StockReason` has **five** members — `initial`, `sale`, `waste`, `restock`, `sold_out` — **none of them means "this sale was undone"**. |
| 3 | No filed feature owns it | **PASS** | Sweep over **947** feature contracts + HANDOFFs: `cancelled_sale` → **0**, `cancel_sale` → **0**; `reversal`/`reversed`/`restore the stock` hit **only** features **303**, **390** and **400** — **all three are third-party vocabulary (`defer`) references, none is a contract**. Feature **400** states the gap verbatim: *"`StockReason` has **no reversal member** … the reason it would carry does not exist yet."* |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **432** owns the *sign matrix* (to be amended by one line). **374** owns the *derivation*. **426**/**417** own *other columns' FKs*. **419** owns `sold_out`. **382** asks a different question (*shortfall vs negative stock*). **459** (this pass's Pick A) owns **the bill**; this slice owns **the stock ledger**. |
| 5 | The demand is real | **PASS — stronger than the other two picks** | **Three separate filed features describe the missing mechanism** — 303 (the primitive), 390 (the hazard), 400 (the gap in LE31's own vocabulary) — **and none of them is a contract for it.** The demand is established; only the implementation is missing. |
| 6 | It is cheap now and expensive later | **PASS** | One enum member, one nullable column, one helper, two tests. **No data is at risk** — no `StockEntry` row has ever been written by shipped code. Expensive later: **the wrong ledger rows would be written into an *append-only* table** — the one table where a mistake is hardest to correct. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — and it FIRES** | **Feature 374 owns the derivation this reversal exists to correct.** Until 374 lands, `qty_remaining` is a stored column and **a reversal row would be invisible to it**. **374 must land first, or in the same PR.** |

**Overall: `build`.** **This is the only one of the three picks whose demand check is a clean PASS** — the corpus has said three times that LE31 needs this and has never filed it.

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `backend/app/models.py` | **Add `reversal` to `StockReason`**; **add `reverses_entry_id`** to `StockEntry` (nullable, self-FK to `stock_entry.id`) | **One definition each.** |
| `backend/app/services/stock_service.py` — **create it if absent**; feature **374** names this exact path | **Add `reverse_stock_entry(session, entry_id, by_user_id)`** | If 374 has not landed, create the directory and file; **record that you did.** |
| `features/432-le31-stockentry-reason-sign-coherence-first-party-the-charter-names-a-sign-for-every-ledger-reason-and-the-schema-enforces-none-of-it-v1-reason-sign-coherence.md` | **One line** — extend the sign matrix with `reversal` | **Do not restate 432's matrix in code.** Amend it. |
| `features/446-le31-has-no-schema-evolution-mechanism.md` — **or whichever file owns 446** | **Name this feature in 446's blocked-features list** | **This slice adds a column. `create_all()` cannot alter an existing table.** See §5.1. |
| `tests/` (whatever the repo's test path is — **check**) | **Two regression tests** | The reversal test and the double-reversal test. |

**Do NOT touch:** `Batch.qty_remaining` (feature 374), `StockEntry.ref_order_item_id` (feature 426), `StockEntry.by_user_id` (feature 417), `StockReason`'s other members, `sold_out` (feature 419), any `UPDATE`/`DELETE` of a ledger row (**never**), `OrderItem` (features 379 / 452 / 456 / 459), `Bill` (feature 415 / 457).

## 4. The implementation, in order

1. **Record the decisions first** — the reason's name, the column's name, which reasons are reversible, whether a reversal may itself be reversed, and whether the reversal is written in the same transaction as the cancellation. **The corpus's precedent is that the recorded decision is what stops the next pass from re-deriving it.**
2. **Add `StockReason.reversal`** and **`StockEntry.reverses_entry_id`**.
3. **Amend feature 432's sign matrix by one line** — `reversal`'s sign is **the opposite of the row it reverses**; there is no fixed sign for it.
4. **Add `reverse_stock_entry(...)`** — it loads the original, **refuses** if the original is already reversed, **refuses** if the original's reason is not reversible, and **writes a NEW row** with `qty_delta = -original.qty_delta`, `reason = StockReason.reversal`, `batch_id = original.batch_id`, `reverses_entry_id = original.id`. **It never touches the original row.**
5. **Write the two regression tests** — they must **fail on today's code** (there is no `reversal` member, so the helper cannot even be written).
6. **Record what was and was not verified** in this HANDOFF (see §6).

## 5. The four things that will go wrong if nobody tells you

1. **The column lands and does not exist in the running database.** **`create_all()` cannot ALTER an existing table.** A `reverses_entry_id` column would be added to the model, the code would merge, deploy, pass its tests — **and the column would not exist in the running database.** This is the trap feature **455** recorded for `Table.label`'s `NOT NULL`. **Feature 446 owns the mechanism; name this feature in 446's blocked-features list.**
2. **Writing a `restock` row of `+1` instead of a `reversal` row.** This is the *tempting* wrong answer and it **records a lie** — the ledger would say the kitchen made another tiramisu, and the next stock-take would count a phantom preparation. **The same trap with `waste` is worse:** `waste` has a **negative** sign per the charter's matrix, so a positive `waste` is a sign violation feature 432's rule would refuse. **The schema offers no correct option today; this feature creates one.**
3. **Writing the reversal with the wrong `batch_id`.** The quantity must go back to **the same batch** the sale came from. **This is a coherence rule on the write path — a `CHECK` cannot reference another row.**
4. **Reversing something that was never a mistake.** `initial` and `restock` are **not** mistakes to undo — the stock was prepared and it exists. **Record which reasons are reversible before writing the helper**, because the refusal rule depends on it.

## 6. Verification protocol

Five offline commands, plus the executed tests:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The reason exists.
grep -n "reversal" backend/app/models.py | wc -l         # >= 2 (enum member + column)

# 2. The back-reference column exists and is a self-FK.
grep -n "reverses_entry_id" backend/app/models.py | wc -l # >= 2

# 3. Feature 432's sign matrix has been amended.
grep -c "reversal" features/432-le31-stockentry-reason-sign-coherence-first-party-the-charter-names-a-sign-for-every-ledger-reason-and-the-schema-enforces-none-of-it-v1-reason-sign-coherence.md

# 4. NO code path UPDATEs or DELETEs a stock_entry row.
grep -rn "update(StockEntry)\|delete(StockEntry)\|session.delete" backend/   # must print nothing

# 5. The corpus agrees: the reversal is now owned.
grep -rn "reversal" features/ | wc -l                     # must now hit 461
```

**The executed regression tests:**

- **Reversal test** — sale of `−1`, then a reversal: the batch's **derived** remaining quantity equals its **pre-sale** value, and the ledger contains **two** rows (not one edited row).
- **Double-reversal test** — a second reversal of the same sale is **refused**. A reversal that can be applied twice puts the stock back twice, and the batch then reads as **over-stocked by one unit** — a plausible number, and therefore a quiet failure.

**The negative control** — remove the reversal write (so the cancellation leaves the ledger untouched) and confirm the reversal test **fails**. A test that only ever passed proves nothing.

**Record in the HANDOFF:** whether the reversal was exercised on **both** SQLite and Postgres, or only SQLite. **`psycopg` was not importable in the parent's verification venv** — if you did not exercise Postgres, **say so plainly.** Note that feature **427**'s finding means the FK on `reverses_entry_id` is **unenforced on SQLite**, so the refusal of a nonexistent row must be **application-level**.

## 7. Rollback path

**Partially reversible, and the asymmetry must be stated.** Reverting the code removes the ability to *write* a reversal; **it does not remove reversal rows already written**, because the ledger is append-only and **must not be edited**.

1. Revert the enum member and the column.
2. **Leave the existing reversal rows in place.** They are correct records of what happened. **Deleting them would violate charter §4.3.**
3. If the column must physically go, that is a **migration**, and it is feature **446**'s territory.

**No data is at risk today** — no `StockEntry` row has ever been written by shipped code, so there is nothing to leave behind.

## 8. The mandatory LE31 skill list

Read these before writing code — **all of them**, in this order:

1. `le31-conventions` — the schema conventions and the known conflicts.
2. `le31-data` — the data-model rules (money, timestamps, enums, the ledger).
3. `le31-v1-feature-pattern` — the v1 feature shape.
4. `le31-backend` — the FastAPI/SQLModel conventions.
5. `le31-handoff-spec` — the handoff format itself.
6. `le31-coding-agent-brief` — **produces the paste-in prompt from this contract. Do not paste chat excerpts.**

**And read these six feature contracts in full before you start:**

- `features/374-le31-qty-remaining-derived-not-stored-charter-4-3-vs-schema-contradiction-first-party-v1-derive-batch-qty-remaining-from-stockentry-ledger.md` — **the derivation this reversal exists to correct. Must land first.**
- `features/432-le31-stockentry-reason-sign-coherence-first-party-the-charter-names-a-sign-for-every-ledger-reason-and-the-schema-enforces-none-of-it-v1-reason-sign-coherence.md` — **the sign matrix you must amend.**
- `features/421-le31-stockentry-append-only-linter-rule-first-party-the-charter-names-a-linter-rule-for-stockentry-writes-and-no-feature-owns-it-v1-ledger-append-only-mechanism.md` — **the mechanism that makes "never update the original" enforceable.**
- `features/427-le31-sqlite-never-enables-pragma-foreign-keys-first-party-every-declared-fk-is-unenforced-in-dev-while-postgres-enforces-it-in-prod-v1-sqlite-fk-enforcement.md` — **why the refusal rules are application-level.**
- `features/382-dc-tech-inc-dotnet-pos-integration-mit-csharp-dotnet-sql-server-idempotency-in-the-database-shortfall-instead-of-negative-stock-cursor-and-retry-launch-guards-at-the-terminal-v1-stock-deduction-idempotency-and-shortfall-vocabulary.md` — **a `defer` that asks a different question; do not answer it here.**
- `features/459-le31-a-cancelled-order-line-is-still-on-the-bill-the-subtotal-formula-has-no-status-predicate.md` — **this pass's Pick A. The sibling on the *bill* side. Do not merge the two.**

## 9. The one thing that matters

**A derived quantity can only be corrected by an additional event.** LE31's stock quantity is derived from the ledger (feature 374), and the ledger's event vocabulary has **no member for "this sale did not happen"**. **So the moment the selling path exists, every cancellation leaves the batch permanently short — and a derived number with no correcting event carries the error forward, forever.** The charter §4.3's promise is that the ledger is the system of record; **a ledger that cannot record a correction is not a system of record for a business where corrections are daily.**
