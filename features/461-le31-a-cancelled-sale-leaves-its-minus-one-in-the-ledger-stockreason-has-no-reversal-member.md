# Feature 461 — A cancelled sale leaves its `-1` in the ledger: `StockReason` has no reversal member

> **Pick C of Daily Brainstorm 2026-11-08 (99th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, the two relevant classes, verbatim:
>
> ```python
> class StockReason(str, Enum):          # lines 57–61
>     initial = "initial"
>     sale    = "sale"
>     waste   = "waste"
>     restock = "restock"
>     sold_out = "sold_out"
>
> class StockEntry(SQLModel, table=True): # lines 113–126
>     """Append-only ledger. Never UPDATE or DELETE rows.
>
>     Current stock for a batch = SUM(qty_delta) WHERE batch_id = X.
>     """
>     __tablename__ = "stock_entry"
>
>     id: int | None = Field(default=None, primary_key=True)
>     batch_id: int = Field(foreign_key="batch.id", index=True)
>     qty_delta: int              # positive = added, negative = consumed
>     reason: StockReason
>     ref_order_item_id: int | None = None
>     by_user_id: int | None = None
>     at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
> ```
>
> **Five reasons. None of them means "this sale was undone".**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then real inserts):
>
> ```
>   Batch(menu_item_id=tiramisu, qty_start=8, qty_remaining=8)
>   OrderItem(visit_id=1, menu_item_id=tiramisu, qty=1, unit_price=6.00)
>   StockEntry(batch_id=1, qty_delta=-1, reason=sale, ref_order_item_id=1)   ACCEPTED
>       -- the guest then cancels the tiramisu --
>   OrderItem.status = 'cancelled'                                            ACCEPTED
>
>   the ledger row is STILL THERE.  Nothing was written back.
>
>   SUM(qty_delta) for the batch = -1
>   -> the batch's remaining quantity is one SHORT of what it should be,
>      and the ledger cannot say why.
> ```
>
> **⭐ THE CORPUS ALREADY NAMED THIS EXACT GAP — IN A FEATURE THAT IS NOT A CONTRACT FOR IT.** Feature **400** (`tws-manumaha-cafe-pos-v3`) states, verbatim, in its *Adjacent evidence*:
>
> > *"**Voids & refunds with approval ✅ Manager/owner only; void restores stock and reverses loyalty points**"* — *"a waiter cancelling an order item after it was fired"* — *"`StockReason` has **no reversal member** (`initial`, `sale`, `waste`, `restock`, `sold_out` only). §3.3 forbids fixing this by updating `Batch.qty_remaining`; the **correct** fix is a new `StockEntry`, and the ***reason* it would carry does not exist yet**."*
>
> **Feature 400 is a third-party *vocabulary* pick (`defer`).** It names the missing reason member and it does **not** own the fix.
>
> **⭐ A CORPUS-WIDE SWEEP CONFIRMS NOBODY OWNS IT.** Over **947** feature contracts and HANDOFFs, searching for `reversal`, `reversed`, `cancelled_sale`, `cancel_sale`, `restores stock`, `restore the stock`, `void restor`:
>
> | hit | what it is |
> |---|---|
> | feature **303** (`Bastardki11ar/tally`) | third-party vocabulary: *"a reversal is a new ledger entry that negates a prior entry, never an UPDATE on the original"* — **a `defer` vocabulary reference, no contract** |
> | feature **390** (`bhargavkalita47/pantry`) | third-party vocabulary: *"Orders retain recipe-consumption snapshots, so later recipe edits do not change cancellation quantities"* — **a `defer` vocabulary reference** |
> | feature **400** | the observation above — **a `defer` vocabulary pick** |
> | features **144**, **118**, **284** | unrelated senses of "reversible" |
>
> **Not one LE31 contract owns the rule.** Three vocabulary references name the shape; **nobody builds it.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect (**three** filed vocabulary references describe it and **no** contract implements it); **medium** for the demand framing (no operator has reported lost stock — but **no code path has ever written a `StockEntry`**, so there is no report to have been made).

## Goal

Make a **cancelled sale undoable in the ledger**, so that cancelling a dish the kitchen already fired **puts the stock back** — without ever editing or deleting a ledger row.

**The single sentence this feature exists to make true:** *a cancelled sale is reversed by a new ledger row that names the row it reverses, and the ledger's arithmetic says the right thing.*

Two concrete outcomes:

1. **A reason that means "undone".** `StockReason` gains a member that says *"this movement reverses an earlier one"* — recorded default: **`reversal`** — and it is a **new row**, never an update to the old one.
2. **The reversal names what it reverses.** A ledger row that reverses a sale must point at the sale row it undoes, so the ledger can answer *"was this sale ever reversed?"* and *"how many of this line's units are actually gone?"*.

## Scope

**In scope (v1):**

- **One new `StockReason` member** that means *"this movement reverses an earlier movement"**. *Recorded default: **`reversal`**.* **The implementer must record the choice** — see *Open questions* 1.
- **One nullable back-reference column** on `StockEntry` that names the ledger row this row reverses. *Recorded default: **`reverses_entry_id`** — a nullable FK to `stock_entry.id`.* **The implementer must record the choice** — see *Open questions* 2.
- **One helper** that computes a batch's remaining quantity **and** accounts for reversals — or, more precisely, **one written statement of what the ledger's arithmetic is**, since feature **374** already owns the derivation of `qty_remaining` and this slice must not fork it.
- **A regression test**: a sale of `-1` followed by a reversal of `+1` leaves the batch's remaining quantity **unchanged from before the sale**, and the ledger contains **two** rows, not one edited row.
- **The recorded decision** on the reason's name and the back-reference column's name.

## Out of scope (v1):

- **Any `UPDATE` or `DELETE` of a `StockEntry` row.** The charter §4.3 says *"EVERY change to batch stock is a new StockEntry row. **Never UPDATE or DELETE**."* **This feature is the implementation of that rule, not an exception to it.**
- **`Batch.qty_remaining`.** That is **feature 374** — filed, `build`. 374 owns the *derivation*; this slice owns *the reversal row*. **The two are adjacent and 374 must land first, or in the same PR**, because 374's derivation is the thing that has to *read* the reversal correctly. **See *Ordering*.**
- **The reason-sign matrix.** That is **feature 432** — filed. 432 owns *"given a reason, which signs are legal?"*. **This slice adds a reason; 432's matrix must be extended to cover it, and that extension is 432's, not this slice's.** **The implementer must amend 432's matrix — one line — and must not restate the matrix here.**
- **Whether a sale may proceed when stock is short.** That is **feature 382** — filed, `defer` — and it asks *"should the ledger record a negative quantity, or record the difference separately?"*. **Different question. Neither answers the other.**
- **The `sold_out` semantics.** Feature **419** — filed — owns *"sold_out writes a negative delta so the ledger cannot tell sold-from-withdrawn"*. **This slice must not touch `sold_out`.**
- **The `ref_order_item_id` FK.** Feature **426** — filed — owns the missing FK on that column. **The new back-reference column is a DIFFERENT column and a DIFFERENT defect.** They may be landed together but must not be merged.
- **`StockEntry.by_user_id`'s missing FK.** Feature **417** — filed.
- **`StockEntry`'s append-only linter rule.** Feature **421** — filed. **421 is the mechanism that makes this feature's no-update rule enforceable; this slice does not build the linter.**
- **The `OrderItem.status` transition and its actor.** Features **379** / **394**.
- **The bill-side effect of a cancellation.** That is **feature 459** (this pass's Pick A) — the bill must not charge a cancelled line. **A cancellation has TWO consequences — the money and the stock — and they are two separate contracts on two separate ledgers.** **They must not be merged**, and neither one implies the other: the bill may be right while the stock is wrong, and vice versa.
- **A refund / money-back flow.** Feature **450** owns refunds against a *paid* bill. **This slice is about stock, not money.**
- **Alembic.** Feature **446** owns schema evolution — **and this slice adds a column, so 446 IS a dependency.** See *Dependencies*.

## Description

### The defect, as observed in LE31's own code on 2026-11-08

`StockReason` has exactly five members. Each one names a **cause**:

| reason | what it means | sign (per charter §4.3) |
|---|---|---|
| `initial` | morning prep | `+` |
| `restock` | more was made | `+` |
| `sale` | a unit left the shelf and was sold | `−` |
| `waste` | it was thrown away | `−` |
| `sold_out` | the rest was withdrawn | `−` |

**None of them names a *correction*.** And the charter's §4.3 insert-path list is the same list — **five rows, no reversal**:

```
  • Morning prep       → qty_delta = +N, reason = 'initial'    (one row per batch)
  • Order item served  → qty_delta = -1, reason = 'sale'       (one row per unit sold)
  • /sold_out          → qty_delta = -(remaining), reason = 'sold_out'
  • /leftover N        → qty_delta = -N, reason = 'waste'
  • /restock N         → qty_delta = +N, reason = 'restock'
```

**So the ledger can describe every way stock moves *forward* and every way it moves *backward* — except the one way that is neither: "the sale did not happen after all."**

### The cancellation is not an edge case — it is the most common correction in a service

Executed: a dish is ordered (`StockEntry(-1, reason='sale')`), the kitchen fires it, the guest changes their mind, the waiter cancels the line. **The stock is physically still on the pass. The ledger says it is gone.**

**And the ledger is append-only, so the mistake cannot be corrected by editing the row.** The only correct repair is **a new row** — and **no reason exists to carry it.** The implementer of the cancellation path faces exactly three bad options, and all three are wrong:

1. **Update the sale row's `qty_delta` to 0.** — **Violates charter §4.3** (*"Never UPDATE or DELETE"*) and destroys the evidence that the sale was fired at all.
2. **Write a `restock` row of `+1`.** — **Records a lie.** The stock was never restocked; a sale was undone. The ledger would say the kitchen made another tiramisu. **The next stock-take would count a phantom preparation.**
3. **Write a `waste` row of `+1`.** — **Worse**: `waste` has a **negative** sign per the charter's own matrix (feature 432), so a positive `waste` is a **sign violation** and feature **432**'s rule would refuse it.

**The schema offers no correct option.** That is the finding.

### Why this is a *ledger* defect and not a *cancellation* defect

**Because the ledger is the system of record for stock.** Feature **374** makes `qty_remaining` **derived** from the ledger (*"one ledger, one source of truth, no second copy to drift"*). **That means the reversal is not optional bookkeeping — it is the only thing that can make the derived number correct again.**

A derived number can only be corrected by an additional event. **If the event vocabulary has no member for "undo a sale", then the derived number is permanently wrong for that batch.**

### The quiet wrong answer

The plausible wrong answer is *"a cancelled order line is just a `status` change; the stock is the kitchen's problem."* **That is true today and silently irrelevant:**

- **True today**: nothing writes a `StockEntry` at all — there is no `stock.py` router and no selling path (feature **374** records this: *"no code path has ever moved stock"*). So the question has never arisen.
- **Silently irrelevant the moment the selling path exists**: **the charter's P0 row 45 is a selling path** — *"Selling a prepared item decrements its active batch's `qty_remaining` and writes a `StockEntry(-1, reason='sale')` row"* — and features **03**, **04**, **26**, **34**, **45** all plan to write one. **The first sale written by LE31 will write a `-1` with no way to take it back.**
- **The symptom is a plausible business number, not an error.** A tiramisu that was made, sold, and then cancelled is **stocked out at the kitchen** and **missing from the ledger** — or, in the other direction, **the ledger says the kitchen is short of a tiramisu it actually has.** The prep board (feature **34**) shows a wrong number. **The cook prepares another one that was never needed.** Nothing errors; the number is simply wrong, and wrong in the direction that **over-prepares**.

### The instance sweep, not the concept sweep

A corpus-wide sweep over **947** feature contracts and HANDOFFs for `reversal` / `reversed` / `cancelled_sale` / `cancel_sale` / `restores stock` / `restore the stock` / `void restor`:

| pattern | hits | what they are |
|---|---|---|
| `reversal` | 4 | features **303** (tally vocabulary, `defer`), **144** (biometric "non-reversible", unrelated), **118** (textile ERP, third-party), **284** (decision-log vocabulary, `defer`) |
| `reversed` | 3 | feature **118**, feature **144**, and **303** |
| `restore the stock` / `restores stock` | 3 | feature **400** (the observation), **390** and **378** (third-party vocabulary) |
| `cancelled_sale` / `cancel_sale` | **0** | — |
| `void restor` | 1 | feature **400** |

**Three `defer` vocabulary references describe the shape. No contract implements it.** **This is the seventh finding shape** — *a covered concept with an uncovered instance* — in its purest form: **the concept "a reversal is a new row, not an edit" is in the corpus three times, and the instance "LE31's `StockReason` has no member for it" is nowhere.**

## Data model

```python
class StockReason(str, Enum):
    initial  = "initial"
    sale     = "sale"
    waste    = "waste"
    restock  = "restock"
    sold_out = "sold_out"
    reversal = "reversal"   # NEW — a movement that undoes an earlier movement


class StockEntry(SQLModel, table=True):
    """Append-only ledger. Never UPDATE or DELETE rows.

    Current stock for a batch = SUM(qty_delta) WHERE batch_id = X.
    """
    __tablename__ = "stock_entry"

    id: int | None = Field(default=None, primary_key=True)
    batch_id: int = Field(foreign_key="batch.id", index=True)
    qty_delta: int              # positive = added, negative = consumed
    reason: StockReason
    ref_order_item_id: int | None = None
    by_user_id: int | None = None
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))

    # NEW — the row this row undoes.  Nullable: a row that reverses nothing
    # (a morning prep, a restock, a waste) carries NULL.
    reverses_entry_id: int | None = Field(default=None, foreign_key="stock_entry.id")
```

**The DDL the change produces (read back from a created SQLite database):**

```
CREATE TABLE stock_entry (
    id INTEGER NOT NULL,
    batch_id INTEGER NOT NULL,
    qty_delta INTEGER NOT NULL,
    reason VARCHAR NOT NULL,
    ref_order_item_id INTEGER,
    by_user_id INTEGER,
    at DATETIME NOT NULL,
    reverses_entry_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(batch_id) REFERENCES batch (id),
    FOREIGN KEY(refers...) -- ...
)
```

**Notes for the implementer:**

- **`reverses_entry_id` is a SELF-reference** — a row pointing at another row of the same table. **This is the standard "reversal" shape** and it is what feature **303**'s third-party vocabulary names (*"a reversal is a new ledger entry that negates a prior entry, never an UPDATE on the original"*). **It is NOT an update.**
- **The sign of a reversal is the OPPOSITE of the row it reverses.** A `sale` is `−1`; its reversal is `+1`. **Feature 432's sign matrix must be extended to include `reversal`**, and the extension is 432's to make — **the implementer amends 432's matrix by one line rather than restating it here.**
- **A reversal MUST name the row it reverses.** A `+1` `reversal` row with `reverses_entry_id IS NULL` is **unattributable** and is worse than no reversal at all: it puts the quantity back but leaves the ledger unable to answer *"was this sale reversed?"*. **The implementer must decide whether the back-reference is enforced** — see *Open questions* 3.
- **The reversal row must carry the SAME `batch_id` as the row it reverses.** Otherwise the quantity goes back to the wrong batch. **This is a coherence rule on the write path, not a constraint** (a `CHECK` cannot reference another row).
- **`ref_order_item_id` on the reversal row is optional.** The order line is already recorded on the original sale row. **Recorded default: leave the reversal's `ref_order_item_id` NULL** — the link runs *sale → reversal*, not *reversal → sale*. **The implementer must record the choice.**
- **The FK on `reverses_entry_id` is unenforced on SQLite** — feature **427**'s finding (*"SQLite never enables `PRAGMA foreign_keys`"*). **Do not rely on the database to refuse a reversal naming a nonexistent row**; validate in the application. **Feature 427 owns the general fix; this slice must not wait for it to make its own rule enforceable.**

## Implementation steps

1. **Record the two decisions** (reason name, back-reference column name) in `models.py` and in the HANDOFF, before writing code. **The corpus's precedent is that the recorded decision is what stops the next pass from re-deriving it.**
2. **Add `reversal` to `StockReason`** and **`reverses_entry_id` to `StockEntry`** in `backend/app/models.py`.
3. **Amend feature 432's sign matrix** by one line: `reversal` → *sign is the opposite of the row it reverses; there is no fixed sign for it.* **Do not restate 432's matrix in this contract.**
4. **Add one helper** — `reverse_stock_entry(session, entry_id, by_user_id)` — that:
   - loads the original entry,
   - **refuses** if the original is already reversed (a double reversal would put the quantity back twice),
   - **refuses** if the original's `reason` is not one that can be reversed (`initial` and `restock` are not mistakes to undo — **the implementer must record which reasons are reversible**, see *Open questions* 4),
   - **writes a NEW row** with `qty_delta = -original.qty_delta`, `reason = StockReason.reversal`, `batch_id = original.batch_id`, `reverses_entry_id = original.id`,
   - **never touches the original row.**
5. **Write the regression test**: a sale of `-1`, then a reversal, leaves the batch's **derived** remaining quantity equal to what it was **before** the sale, and the ledger contains **two** rows. **This test fails on today's code** — there is no `reversal` member, so the helper cannot even be written.
6. **Write the negative test**: a **double** reversal is refused. **A reversal that can be applied twice puts the stock back twice, and the second reversal is invisible** — the ledger would show the batch as over-stocked by one unit, which is a plausible number and therefore a quiet failure.
7. **Record what was and was not verified** in the HANDOFF — in particular, **whether the reversal was exercised on Postgres** (see *Dependencies*).

## Telegram interaction if any

**None.** This feature has **no Telegram surface.** It is a ledger-level rule.

**One consequence must be recorded for the cook, though:** when the waiter cancels a dish the kitchen already fired, **the prep board (feature 34) must show the stock back.** Under the recorded default, **the reversal row makes the derived quantity correct**, so the prep board is correct **provided** it reads the derivation and not a stale stored column (feature **374**). **This is the operational reason 374 must land first.**

## Dependencies

| Feature | Relationship | Why it matters |
|---|---|---|
| **374** (`qty_remaining` derived from the ledger) | **UPSTREAM — must land first, or in the same PR** | 374 owns the derivation this reversal exists to correct. **Until 374 lands, `qty_remaining` is a stored column and a reversal row would be invisible to it** — the reversal would exist in the ledger and change nothing. **374 also names the very file (`backend/app/services/stock_service.py`) this helper should live in.** |
| **432** (`StockReason` sign coherence) | **Must be amended, one line** | 432 owns the sign matrix. **The new reason needs a row in it**, and *the reversal's sign is the opposite of the row it reverses* — which is a **new kind of entry** in the matrix. **Amend 432; do not restate it.** |
| **421** (ledger append-only linter rule) | **The mechanism that makes this enforceable** | 421 is the charter's §7 rule (*"Linter rule … for `StockEntry` writes"*). **This feature's "never update the original" promise is only as good as 421's linter.** Not a blocker for the schema change. |
| **426** (`ref_order_item_id` FK) | **Adjacent, different column** | 426 owns the missing FK on `ref_order_item_id`; this slice adds a **different** column with a **different** defect. May land together; must not be merged. |
| **417** (`StockEntry.by_user_id` FK) | **Adjacent** | Owns that column's FK. **The reversal row should carry an actor** — **the `by_user_id` FK is 417's and is not a prerequisite for writing the column.** |
| **382** (shortfall vs negative stock) | **Different question** | 382 asks *"should the ledger record a negative quantity, or record the difference separately?"*. This asks *"how does an undone sale get reversed?"*. **Neither answers the other.** |
| **419** (`sold_out` withdrawal semantics) | **Adjacent** | Owns `sold_out`. **Do not touch it.** |
| **446** (schema evolution) | **HARD dependency** | This slice **adds a column** (`reverses_entry_id`). `create_all()` **cannot alter an existing table**, so the column would land, merge, deploy, pass its tests **and not exist in the running database**. **446's contract must name this feature in its blocked-features list.** **This is the same trap feature 455 recorded.** |
| **427** (SQLite FK enforcement) | **Reason the rule is in the application** | SQLite never enables `PRAGMA foreign_keys`, so the database will not refuse a reversal naming a nonexistent row. **Validate in the application.** |
| **459** (this pass's Pick A — billable statuses) | **Sibling — and must not be merged** | 459 owns **the bill**: a cancelled line must not be charged. **This slice owns the stock ledger.** A cancellation has two consequences on two ledgers, and **either can be right while the other is wrong.** **They are two contracts, two PRs, two reviewable units.** |
| **379 / 394** (order-item transitions) | **Prerequisite of the *trigger*, not of the fix** | The cancellation that triggers a reversal is a status transition. **The trigger's mechanism is theirs; the reversal's mechanism is this slice's.** |

## Open questions

1. **What is the reversal reason called?** *Recorded default: **`reversal`**.* The alternatives are `undo`, `cancelled_sale` and `void`. **`reversal` is the shortest and matches feature 303's third-party vocabulary** (*"a reversal is a new ledger entry that negates a prior entry"*). **The implementer must record the choice.**
2. **What is the back-reference column called?** *Recorded default: **`reverses_entry_id`*** — a nullable FK to `stock_entry.id`. **The implementer must record the choice.** **Note the schema-evolution consequence**: adding a column is blocked on feature **446** (see *Dependencies*), so the column name is written into a migration-sensitive change.
3. **Must a reversal name the row it reverses?** *Recorded default: **yes — a `reversal` row with `reverses_entry_id IS NULL` is refused.*** The reason: **an unattributable reversal restores the quantity but leaves the ledger unable to answer *"was this sale reversed?"*.** **The implementer must record the choice.**
4. **Which reasons can be reversed?** *Recorded default: **`sale` and `sold_out` only.*** `initial` and `restock` are *not* mistakes to undo — the stock was prepared and it exists. `waste` is a recorded loss; reversing it is a correction of the **record**, not of the stock, and **belongs to a different slice**. **The implementer must record the choice, and must record it before writing the helper**, because the helper's refusal rule depends on it.
5. **Should a reversal be reversible?** *Recorded default: **no** — reversing a `reversal` is refused, and a **second** reversal of the same sale is refused.** The reason: **a double reversal puts the stock back twice and is invisible** — the batch reads as over-stocked by one unit, which is a plausible number and therefore a quiet failure. **The implementer must record the choice.**
6. **Should the reversal be recorded in the same transaction as the cancellation?** *Recorded default: **yes** — the cancellation and its reversal are **one transaction**, exactly as feature 454 requires for a void and its close. **A cancellation without its reversal leaves the stock short; a reversal without its cancellation is a phantom.** **The implementer must record the choice.**

## Why this matters

**Because LE31's ledger can describe every way stock moves except the way a service actually behaves most often — the guest changes their mind.**

The charter's §4.3 is explicit that **the ledger is append-only and the current quantity is derived from it**. **A derived quantity can only be corrected by an additional event.** The event vocabulary has five members and none of them is "this did not happen".

**What this costs when it is wrong:**

- **The kitchen is short of a dish it has.** The prep board (feature 34) shows a lower number than the pass holds. **The cook prepares another one that was never needed** — the over-preparation is the visible symptom, and it recurs every time a table cancels a dish.
- **Or the kitchen is short of the truth.** If the implementer chose option 2 above (a `restock` row of `+1`), the ledger says the kitchen made another tiramisu. **The next stock-take counts a phantom preparation, and the variance is unexplained.**
- **The wrongness is permanent.** A derived quantity with no correcting event **cannot be fixed** — every future derivation of that batch carries the error forward, forever. **This is the same permanence feature **444** found in the price domain and feature **454** found in the walk-out domain.**
- **And it is permanent *in the ledger*, which is the thing LE31's whole audit story rests on.** The charter §4.3's promise is that the ledger is the system of record. **A ledger that cannot record a correction is not a system of record for a business where corrections are daily.**

**Why it is cheap today and expensive later:**

- **Cheap today**: one enum member, one nullable column, one helper, two tests. **No data is at risk** — **no `StockEntry` row has ever been written by shipped code**, so there is no ledger to repair.
- **Expensive later**: **the moment the selling path exists, every cancellation is unrecoverable.** The charter's **P0 row 45** is that selling path, and features **03**, **04**, **26**, **34** and **45** all plan to write one. **And unlike most of this series' defects, the wrong ledger rows would be written *into an append-only table*** — which is precisely the table where a mistake is hardest to correct.

**Why it is a `build` and not a `defer`:**

**Because three separate filed features already describe the missing mechanism, and none of them is a contract for it.** Feature **303** states the primitive: *"a reversal is a new ledger entry that negates a prior entry, never an UPDATE on the original."* Feature **390** states the hazard: *"Orders retain recipe-consumption snapshots, so later recipe edits do not change cancellation quantities."* Feature **400** states the gap in LE31's own vocabulary: *"`StockReason` has **no reversal member** … the *reason* it would carry does not exist yet."* **Three `defer` vocabulary references, zero contracts. The demand is established; only the implementation is missing.**

## Adjacent evidence

**Third-party, in-window, permissive licences, no code adopted.** All fields parent-verified via a direct `GET /repos/{owner}/{repo}` on 2026-11-08 and **README read in full**.

- **`AlgoVyn/bikri`** (MIT ✓ §3.2, **★1 / ⑂0 = NO traction evidence in either direction**, TypeScript, 14,238 KB, created **2026-10-26** AND pushed **2026-11-08** = **in-window by BOTH fields**) — README, verbatim: *"**Stock and suppliers** — deliveries, **supplier returns and ledger**, **stock adjustments**, weighted-average cost and Code 128 labels."* **The transferable primitive: a stock *adjustment* is a ledger entry, not an edit of a prior one.** That is the same shape this feature needs, and the README's own vocabulary — *"adjustments"* alongside *"ledger"* — is the evidence that a correction and a ledger entry are the same object in a working POS. **Already cited by features 455, 454 and 447** — recorded so a later pass does not re-derive it as a fresh trigger.
- **`baba-dev/menuminute`** (MIT ✓ §3.2, **★1 / ⑂0**, TypeScript, 92,690 KB, created **2026-10-13** AND pushed **2026-11-08** = **in-window by both fields**) — README, verbatim: *"Dine-in, table and pickup orders with a mobile cart and staff acceptance. **Immutable order snapshots.**"* **The transferable primitive is "the snapshot is immutable; a correction is a separate act"** — the same append-only discipline this feature applies to the stock side. **Already cited by feature 443.**
- **`manoranjan2050/RestoPro-ERP-Web`** (MIT ✓ §3.2, **★1 / ⑂0**, PHP, 7,443 KB, created **2026-11-04** AND pushed **2026-11-05** = **in-window by both fields**) — README, verbatim: *"**Cashier role:** counter only. **Cancelling**, refunds and big discounts stay owner-only."* **The transferable observation: a real restaurant's cancellation is an *authorised, separate act*, not a side effect of editing a row** — which is the authorisation half of this feature's rule. **Already cited by feature 448.**

**Repo self-reported metrics are labelled unverified.** None of these READMEs states a test count or coverage figure that this contract relies on; **nothing here needs an unverified number.**

## Verification protocol

Five commands, all re-runnable, all offline:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The reason exists.
grep -n "reversal" backend/app/models.py | wc -l        # >= 2 (enum member + column)

# 2. The back-reference column exists and is a self-FK.
grep -n "reverses_entry_id" backend/app/models.py | wc -l # >= 2

# 3. Feature 432's sign matrix has been amended.
grep -c "reversal" features/432-le31-stockentry-reason-sign-coherence-first-party-the-charter-names-a-sign-for-every-ledger-reason-and-the-schema-enforces-none-of-it-v1-reason-sign-coherence.md

# 4. NO code path UPDATEs or DELETEs a stock_entry row.
grep -rn "update(StockEntry)\|delete(StockEntry)\|session.delete" backend/   # must print nothing

# 5. The corpus agrees: the reversal is now owned.
grep -rn "reversal" features/ | wc -l                    # must now hit 461
```

Plus the **executed** regression tests: sale of `-1` → reversal → the batch's **derived** remaining quantity equals its pre-sale value, and the ledger contains **two** rows; and a **double reversal is refused**.

**The negative control**: re-inject the defect by removing the reversal helper's write (so the cancellation leaves the ledger untouched) and confirm the regression test **fails**. A test that only ever passed proves nothing.

## Rollback path

**Partially reversible, and the asymmetry must be stated.** Reverting the code removes the ability to *write* a reversal; **it does not remove reversal rows already written**, because the ledger is append-only and **must not be edited**. The rollback path is therefore:

1. Revert the enum member and the column.
2. **Leave the existing reversal rows in place.** They are correct records of what happened. **Deleting them would violate charter §4.3.**
3. If the column must physically go, that is a **migration**, and it is feature **446**'s territory.

**No data is at risk today** — no `StockEntry` row has ever been written by shipped code, so there is nothing to leave behind. **The migration consequence is recorded so the implementer does not discover it at rollback time.**
