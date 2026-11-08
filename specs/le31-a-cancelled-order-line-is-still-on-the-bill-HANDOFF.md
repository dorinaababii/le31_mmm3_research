# HANDOFF — Feature 459: a cancelled order line is still on the bill

> **Slice contract for the coding agent.** Feature: `features/459-le31-a-cancelled-order-line-is-still-on-the-bill-the-subtotal-formula-has-no-status-predicate.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (executed against LE31's real schema on 2026-11-08).
> Filed by: Daily Brainstorm 2026-11-08 (99th daily-brainstorm pass), Pick A.

---

## 1. The active feature path

```
features/459-le31-a-cancelled-order-line-is-still-on-the-bill-the-subtotal-formula-has-no-status-predicate.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 435 / 415 / 456 / 379, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | Executed against LE31's real schema (`SQLModel.metadata.create_all` on a throwaway SQLite file, real inserts). Two numbers: **415's formula over ALL lines = 11.00**, **the same sum excluding `cancelled` = 5.00**. **Divergence 6.00.** The derived tip on a **5.00** payment becomes **−6.50**. |
| 2 | The defect is in LE31's own code, not a third party's | **PASS** | `backend/app/models.py` lines 142–155 (`OrderItem.status: ItemStatus`), lines 35–40 (`ItemStatus.cancelled` exists). Feature **415**'s formula line 141 carries no `WHERE`. |
| 3 | No filed feature owns it | **PASS** | Sweep over **947** feature contracts + HANDOFFs: `cancelled.{0,60}subtotal` → **0**, `subtotal.{0,60}cancelled` → **0**, `excluded from the subtotal` → **0**. Feature **435** *records* the rule as a default and **explicitly disclaims** implementing it ("deliberately not decided here"). |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **435** owns the *membership* (a `bill_line` table) and disclaims the *predicate*. **415** owns the *route* and the *derivation site*. **456** owns `qty`'s sign. **379** owns the transition log. **This slice owns the predicate only.** |
| 5 | The demand is real | **PARTIAL — recorded honestly** | No operator has reported a wrong bill. **No bill has ever been closed by shipped code** (there is no `routers/bills.py`), so there is no report to have been made. The defect is **currently inert**. |
| 6 | It is cheap now and expensive later | **PASS** | One constant, two helpers, two tests. **No schema change.** Expensive later: the moment **415** lands, every bill charges cancelled lines — **and the wrong subtotal is stored, so the bill cannot be audited against the visit.** |
| 7 | The upstream-of-filed-work condition is checked | **PASS — and it FIRES** | **Feature 415 is about to write this derivation and will write it faithfully, including the omission.** **This must land before 415, or in the same PR.** |

**Overall: `build`.** The weakest link is check 5, and it is weak for a mechanical reason — the feature that would produce the complaint does not exist yet. **That is also the reason to land it first.**

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `backend/app/models.py` | **Add `BILLABLE_ITEM_STATUSES`** immediately after `class ItemStatus`, plus a `billable_lines()` and `subtotal_items_derived()` helper | **One definition. Do not duplicate.** If `backend/app/services/` exists (feature 374's `stock_service.py`), the helpers may live there — **record which path you chose.** |
| `backend/app/routers/bills.py` | **Only if feature 415 has already landed** — wire the derivation to `subtotal_items_derived` | **If 415 has NOT landed, do NOT create the route.** The helper exists and is tested; 415 consumes it. |
| `features/435-le31-bill-records-no-which-lines-it-charged-first-party-a-bill-has-no-edge-to-order-item-so-the-stored-subtotal-is-a-number-nobody-can-audit-v1-bill-line-membership.md` | **One line** — point its recorded default at this constant | Do not otherwise change 435. |
| `features/415-le31-bill-closes-visit-first-party-no-bills-router-exists-and-nothing-ties-a-paid-bill-to-a-closed-visit-v1-bill-closes-visit-edge.md` | **One line** — its formula comment must say *"over the billable lines (see feature 459)"* | Do not otherwise change 415's implementation. **415 owns the route.** |
| `tests/` (whatever the repo's test path is — **check**) | **Two regression tests** | The subtotal test and the tip test. |

**Do NOT touch:** `backend/app/models.py`'s `ItemStatus` enum members, `OrderItem`'s columns, `Bill`, `DerivedTip`, the `bill_line` table (feature 435), any `CHECK` constraint (feature 404), `StockEntry` (features 417 / 426 / 432), `MenuItem` (feature 458), `Table` (features 455 / 460).

## 4. The implementation, in order

1. **Record the decisions first** — the two open questions (which statuses are billable; the case of "must a line be `served` first"). **The corpus's precedent is that the recorded decision is what stops the next pass from re-deriving it.**
2. **Add `BILLABLE_ITEM_STATUSES`** — a `frozenset[ItemStatus]`, `cancelled` **excluded**, `served` **not** required.
3. **Add `billable_lines(session, visit_id)`** and **`subtotal_items_derived(session, visit_id)`** — the money arithmetic in `Decimal`, seeded with `Decimal("0.00")` so an empty set is `0.00` and not `None` or an int.
4. **Write the two regression tests** — they must **fail on today's code**.
5. **Amend features 435 and 415 by one line each.**
6. **Record what was and was not verified** in this HANDOFF (see §6).

## 5. The three things that will go wrong if nobody tells you

1. **Writing the predicate in SQL.** `ItemStatus` is a `str` Enum stored in a `VARCHAR` column with **no membership constraint** (feature **442**). A `WHERE status IN ('new','preparing','ready','served')` **duplicates the enum as a string list** and can drift from it. **Filter in Python on the enum.** One definition.
2. **Summing in SQL.** Feature **411** proved `Decimal` is a Python-side guarantee the storage layer does not enforce — **Postgres rounds where SQLite does not**, so dev and prod would disagree about the subtotal. **Compute the sum in Python, on `Decimal`, before the write.** This is also feature 415's own recorded obligation.
3. **Reading the empty sum as `None`.** `sum(..., Decimal("0.00"))` — seed it. A visit with no billable lines must yield `Decimal("0.00")`.

## 6. Verification protocol

Four offline commands, plus the executed tests:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The predicate exists and has exactly ONE definition.
grep -rn "BILLABLE_ITEM_STATUSES" backend/ features/ specs/ | wc -l    # >= 3 (def + import + test)

# 2. The rule EXCLUDES 'cancelled'.  (must print exactly one match)
grep -rn "BILLABLE_ITEM_STATUSES" backend/ -A 12 | grep -c "ItemStatus.cancelled"

# 3. No bare SUM left in the derivation.
grep -rn "SUM(order_item.unit_price" backend/    # must print nothing

# 4. The corpus agrees: the predicate is now implemented, not just recorded.
grep -rn "cancelled.{0,60}subtotal" features/    # must now hit 459
```

**The executed regression test** — build the real schema, insert a visit with one live line (2 × 2.50) and one `cancelled` line (1 × 6.00), and assert the subtotal is `Decimal("5.00")`. **It must fail before the change and pass after.**

**The negative control** — re-admit `cancelled` (`frozenset(ItemStatus)`) and confirm the test **fails**. A test that only ever passed proves nothing.

**Record in the HANDOFF:** whether you ran the executed test on **both** SQLite and Postgres, or only SQLite. **`psycopg` was not importable in the parent's verification venv** — if you did not exercise Postgres, say so plainly.

## 7. Rollback path

**Fully reversible in one step.** Revert the constant and the two helpers. **No data is at risk** — no bill has ever been closed by shipped code, so no `bill.subtotal_items` was computed with the defect. **No column, no table, no migration, no backfill.**

## 8. The mandatory LE31 skill list

Read these before writing code — **all of them**, in this order:

1. `le31-conventions` — the schema conventions and the known conflicts.
2. `le31-data` — the data-model rules (money, timestamps, enums).
3. `le31-v1-feature-pattern` — the v1 feature shape.
4. `le31-backend` — the FastAPI/SQLModel conventions.
5. `le31-handoff-spec` — the handoff format itself.
6. `le31-coding-agent-brief` — **produces the paste-in prompt from this contract. Do not paste chat excerpts.**

**And read these four feature contracts in full before you start:**

- `features/435-le31-bill-records-no-which-lines-it-charged-first-party-a-bill-has-no-edge-to-order-item-so-the-stored-subtotal-is-a-number-nobody-can-audit-v1-bill-line-membership.md` — the sibling; **its recorded default is what you are implementing.**
- `features/415-le31-bill-closes-visit-first-party-no-bills-router-exists-and-nothing-ties-a-paid-bill-to-a-closed-visit-v1-bill-closes-visit-edge.md` — the route; **it must consume your constant.**
- `features/456-le31-order-item-qty-may-be-zero-or-negative-first-party-a-bill-line-may-carry-a-negative-quantity-and-nothing-refuses-it-v1-order-line-quantity-rule.md` — the *adjacent* rule on a *different* column. **Do not merge.**
- `features/432-le31-stockentry-reason-sign-coherence-first-party-the-charter-names-a-sign-for-every-ledger-reason-and-the-schema-enforces-none-of-it-v1-reason-sign-coherence.md` — the **precedent for the shape**: a named, table-shaped rule in one place.

## 9. Ordering — the one sentence that matters

**Feature 415 is about to write the derivation and will write it faithfully, including the omission. This must land before 415, or in the same PR.** If 415 has already merged when you start, **amend its derivation to use `BILLABLE_ITEM_STATUSES`** — and say so in your report, because a bill closed between the two landings was charged the cancelled line.
