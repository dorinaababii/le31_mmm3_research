# Feature 441 — `le31-stockentry-may-name-a-batch-and-an-order-line-for-different-dishes`

> **Pick A of Daily Brainstorm 2026-11-05 (98th daily-brainstorm pass).** **FIRST-PARTY, and the gap was PROVEN BY EXECUTION on 2026-11-05 — not inferred from reading code.**
>
> LE31's own `backend/app/models.py` declares:
>
> ```python
> class StockEntry(SQLModel, table=True):
>     """Append-only ledger. Never UPDATE or DELETE rows."""
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
> A ledger row carries **two** pointers that both name *what was affected*:
> `batch_id` (which batch was consumed) and `ref_order_item_id` (which order line caused it). **Nothing in the schema says the two must be talking about the same dish.**
>
> The parent proved the gap **by execution** — building a real SQLite database from LE31's own models via `SQLModel.metadata.create_all`, then inserting:
>
> ```
> order_item  id=1  menu_item_id=1  qty=2   (the "Soup" line)
> batch       id=1  menu_item_id=1  qty_start=10
> batch       id=2  menu_item_id=2  qty_start=5   (a batch of the "Cake")
> ```
>
> and then writing a ledger row naming the **Cake's** batch against the **Soup's** order line:
>
> ```
> StockEntry(batch_id=2, qty_delta=-1, reason=sale, ref_order_item_id=1)   -> ACCEPTED
> ```
>
> **The row was accepted.** `stock_entry.batch_id` points at a batch whose `menu_item_id` is **2**, and `stock_entry.ref_order_item_id` points at an order line whose `menu_item_id` is **1**. The database — LE31's own schema — says that **one unit of cake was consumed because a guest ordered soup**. The ledger is append-only by charter, so this row is **permanent and auditable**: it will look perfectly well-formed (both foreign keys non-null, both pointing at real rows) while being **wrong**.
>
> The parent also wrote a **magnitude** mismatch, which is the same defect in a different dimension:
>
> ```
> StockEntry(batch_id=1, qty_delta=-7, reason=sale, ref_order_item_id=1)   -> ACCEPTED
> ```
>
> The order line says **`qty=2`**, at **`unit_price=5.00`**. The ledger says **7 units were consumed**. Nothing objects. The bill would say `subtotal_items = 2 × 5.00 = 10.00` while the stock ledger says **7** units left the shelf.
>
> **Why this matters concretely.** LE31's entire pitch is *"current stock is derived from entries"* (§3.3) and *"money is `Decimal`, never `float`" (§3.6). A derived number is only as trustworthy as the rows it is derived from. If a ledger row can name the wrong dish and the wrong quantity, then the derivation is still *arithmetically* correct and still *semantically* wrong — which is precisely the failure class the charter's arithmetic rules cannot catch. The stock number is the product. **A restaurant owner's confidence in LE31's stock number is the product.**
>
> **The external trigger (in-window, read in full).** `ahmershahdev/karobar-erp` (MIT ✓ §3.2, **★1/⑂0 = NO traction evidence in either direction**, Python/Django + MySQL 8.4, created **2026-11-02** AND pushed **2026-11-03** = **IN-WINDOW BY BOTH FIELDS**, README read in full, 5,038 B) — verbatim:
>
> > *"The hard parts of an ERP are not the forms: it is **books that always balance**, stock that stays right when two cashiers sell the last item at the same moment, and one business never seeing another's data."*
>
> A system whose stated hard part is *"books that always balance"* has had to answer *"`qty_delta` and the order line it points at — do they agree?"* — and answered it **in the data model**: a sale posts **its own journal entry** carrying **the document it came from**. LE31 encodes the same relationship in **prose only**.
>
> **⚠️ THE UPSTREAM-OF-FILED-WORK ORDERING — READ THIS FIRST.** Feature **421** (`le31-stockentry-append-only-linter-rule-…`) is building **the single `StockEntry` write path**, and its *Out of scope* section states verbatim:
>
> > *"**A `StockEntry` write path's business rules.** Feature **03** (kitchen stock tracker) and feature **385** (batch selection and sale provenance) own *what* a ledger row means. This feature owns **where a ledger row may be written** and **how it may not be changed**."*
>
> Feature **426** (`…stockentry-ref-order-item-id-has-no-foreign-key…`) adds the foreign key that makes `ref_order_item_id` point at a **real** order line — and its *Goal* is verbatim *"the ledger's back-pointer to the order line is exactly as trustworthy as its forward-pointer to the batch"* — but **existence is not coherence**: 426 makes the back-pointer *provably valid*, not *provably about the same dish*.
>
> Feature **385** (`…order-item-batch-provenance…`) adds the **forward** pointer `OrderItem.batch_id` — and its own text says *"The link is therefore **one-directional**."*
>
> **So: 385 owns the forward pointer, 426 owns the back-pointer's FK, 421 owns where the row may be written — and the RULE that the two pointers must agree is owned by NOBODY.** Worse: 421 is about to build the one and only write path through which every future ledger row will pass. **If this feature has not landed first, 421 will implement the defect faithfully**, because 421 explicitly places the business rules out of scope. **This is the upstream-of-filed-work condition, and this contract therefore states the ordering explicitly: this lands FIRST, or in the same PR as 421.**
>
> **Boundary — this is NOT feature 426 and NOT feature 385.**
> - **426** = *the back-pointer points at a row that **exists***. This = *the back-pointer points at a row that exists **and is about the same dish, with the same quantity***.
> - **385** = *the order line names the batch it consumed*. This = *the ledger row's own two pointers are **mutually** coherent*.
> - **421** = *where a ledger row may be written*. This = *what a ledger row may **say***.
> - **432** (`…reason-sign-coherence…`) = *the sign of `qty_delta` must match its `reason`*. This = *the **magnitude** of `qty_delta` must match the order line it names*. **Different axis: 432 is about `reason`, this is about the order line.** They may be bundled into one PR but they are **two different rules** and the HANDOFF must keep them separate.
> - **394** (guarded-transition primitive) = *how a guarded write is written*. This = *what the guard must **check***. 394's own Open Question 1 (*"may a derived stock balance be negative?"*) is **unrelated** to this rule and is **not answered here**.
>
> **The three extra checks, answered explicitly** (the coverage-sweep contract requires all three):
> - **(a) Charter §3.2 non-goals?** **No.** The charter's §3.3 says *"current stock is derived from entries"* — this feature is about making the **entries** mean one thing. It is a **schema/validation** change, not a new capability.
> - **(b) Already an open owner question?** **No.** Feature 421's open question is about the **linter rule's mechanism**; 426's is about **which FK lands first**; 385's is about **which batch is active**; 394's is about **whether a balance may be negative**. **None of them is this question.**
> - **(c) Covered under different words?** **No.** A corpus-wide grep over **474 feature contracts + 440 HANDOFFs** for *"the ledger row and the order line must name the same dish"* and for *"the ledger's `qty_delta` must equal the order line's `qty`"* returned **zero hits**, and the strictest possible phrasing — `same menu item` / `same item` / `same dish` / `corresponding item` / `must be the same` — matched **nine** files, **none of which** is about the ledger's two pointers (they are about batches of the same item, tax on the same item, order lines with the same payload, and the `identical field values` phrase). A **passing negative control** (`zzq-nonexistent-control-token-2026-11-05`) found **zero** corpus hits, so the sweep's "uncovered" verdict is not self-contamination.
>
> **Corroboration from a second in-window source (not picked).** `thomas0903/tickertape` (Apache-2.0 ✓ §3.2, Rust, created 2026-11-01, pushed 2026-11-03) describes an append-only journal whose records carry *"opaque payload bytes, a **gap-free sequence number**, a **schema id** and two timestamps you supply"* — i.e. **the record identifies its own schema**, so a reader can tell what a payload means. LE31's ledger row carries a `reason` (a schema id of sorts) but **no** statement of which dish the row is about. Recorded as adjacent evidence.

## Goal

Make it **impossible to write a `StockEntry` whose `batch_id` and `ref_order_item_id` refer to different dishes**, and to write one whose `qty_delta` contradicts the order line it names.

**The single sentence this feature exists to make true:** *a ledger row that says "this dish was consumed because of that order line" is a claim the database can check — and LE31 currently cannot check at all.*

The concrete outcome: after this lands, a write naming the cake's batch against the soup's order line is **rejected**, a write claiming `-7` against a `qty=2` line is **rejected**, and the ledger's two pointers are **mutually redundant** — either one alone identifies the dish, because they are constrained to agree.

## Scope

**In scope (v1):**

- **One validation rule**, enforced at the single write path, that requires — for `reason='sale'` — that `batch_id` and `ref_order_item_id` resolve to the **same `menu_item_id`**.
- **One validation rule**, enforced at the same place, that requires the **magnitude** of a sale's `qty_delta` to equal the referenced order line's `qty` (allowing for the multi-line case stated below).
- **One helper** (`assert_ledger_row_is_coherent(stock_entry)`) in the service layer, so the rule is **one function**, callable from the write path and from a regression test.
- **One regression test** that writes the incoherent rows and asserts both are **rejected**.
- **One deferral-chain correction** recorded in feature 421's and feature 385's own text (a one-line amendment each), so the next pass does not re-derive this and re-file it.
- One row in `INDEX.md`'s "Active feature pipeline" table.

## Out of scope (v1)

- **Any write path.** This feature supplies the **rule** and the **helper**; feature **421** supplies the **single write path** the helper is called from. **This feature does not create `backend/app/services/`.**
- **The append-only linter rule.** Feature **421**. This feature does not touch the lint configuration, the pre-commit hook, or the `StockReason` reversal member.
- **The `ref_order_item_id` foreign key.** Feature **426** adds it. **⚠️ ORDERING: 426 must land FIRST, or in the same PR** — the cross-item rule reads `menu_item_id` *through* the order line, and if the back-pointer can name a nonexistent row, the rule has nothing to compare against. As long as the pragma is off (feature **427**), the FK is **declared but unenforced** — so the **coherence rule must be enforced in the application helper, not by the FK**, and this contract says so.
- **The `OrderItem.batch_id` forward pointer.** Feature **385**. This feature does not add it and does not need it.
- **The `by_user_id` foreign key.** Feature **417**.
- **The reason/sign rule.** Feature **432**. Same PR is fine; **different rule**. Keep them separate in the code and in the HANDOFF.
- **The `qty_remaining` derivation.** Feature **374**.
- **The `sold_out` inverse operation.** Feature **419**.
- **The null-safe active-batch predicate.** Feature **404**.
- **Any database trigger.** Feature **413** owns the trigger vocabulary and records the dev/prod divergence honestly (triggers are enforced in Postgres, absent in SQLite). This feature's rule is enforced in the **application helper**, which behaves identically on both databases. **Recorded, not adopted.**
- **A `StockEntry` write for `reason='initial'`, `'restock'` or `'waste'`.** Those rows legitimately have `ref_order_item_id = NULL` and are **not** constrained by this rule. **Only `reason='sale'` carries the coherence requirement.**
- **The multi-batch case.** If a sale legitimately consumes two batches, the rule must not force one line to name one batch — see *Open questions* 1. **The rule as specified here assumes one batch per sale line**, which is the common case and the one the charter's §4.3 insert-path table describes.
- **Any retro-fitting of historical rows.** There are none — no `StockEntry` write path exists yet (`grep -rn "StockEntry(" backend/` returns exactly **one** hit, the class declaration itself).

## Description

### What the schema says today

`StockEntry` has two pointers into the order/batch world:

| Column | Points at | Foreign key? |
|---|---|---|
| `batch_id` | `batch.id` | **yes** — `foreign_key="batch.id"` |
| `ref_order_item_id` | `order_item.id` | **no** — `int | None = None` (feature 426) |

and **one** business pointer:

| Column | Meaning |
|---|---|
| `reason` | `StockReason` — `initial` / `sale` / `waste` / `restock` / `sold_out` |

`Batch` has `menu_item_id → menu_item.id`. `OrderItem` has `menu_item_id → menu_item.id`. **Both point at a menu item, and the two menu items are never compared.**

### The two incoherent rows the parent wrote (by execution)

```
order_item id=1  menu_item_id=1  qty=2  unit_price=5.00
batch      id=1  menu_item_id=1  qty_start=10
batch      id=2  menu_item_id=2  qty_start=5

StockEntry(batch_id=2, qty_delta=-1, reason='sale', ref_order_item_id=1)   ACCEPTED
    -> the ledger says 1 unit of item 2 was consumed because of an order line for item 1

StockEntry(batch_id=1, qty_delta=-7, reason='sale', ref_order_item_id=1)   ACCEPTED
    -> the ledger says 7 units were consumed; the order line says 2
```

Both rows are **individually** well-formed: both foreign keys are non-null, and (after feature 426) both point at real rows. **Nothing about them is malformed. They are semantically incoherent, and there is no rule that could notice.**

### Why this is the *same shape* as two already-filed defects, and why it is still new

| Filed feature | The shape | What it fixes |
|---|---|---|
| **426** | dangling reference | the back-pointer may name a row that **does not exist** |
| **385** | missing forward pointer | the order line does not name its batch |
| **432** | wrong sign | `qty_delta`'s sign contradicts its `reason` |
| **417** | dangling actor | `by_user_id` may name a user that **does not exist** |
| **404** | missing `CHECK` | a corrupt `qty_delta` text makes `SUM()` return **0.0**, so the row reads as **sold out** |

**This feature is a fifth instance of the same family — and it is the only one that survives all four of the others.** Apply 426, 417, 404 and 432 to the row above: the FKs are satisfied, the actor exists, the delta is an integer, and the sign matches `reason='sale'`. **The row is still wrong.** That is the definition of a gap the others do not close.

### The two numbers that should agree

This feature is built on the pass's standard instrument — **compare two numbers that should agree, never one**:

| Number | Where it lives |
|---|---|
| `menu_item_id` of the referenced batch | `batch.menu_item_id` |
| `menu_item_id` of the referenced order line | `order_item.menu_item_id` |

and, for the magnitude rule:

| Number | Where it lives |
|---|---|
| `ABS(qty_delta)` of the ledger row | `stock_entry.qty_delta` |
| `qty` of the referenced order line | `order_item.qty` |

**A single number never shows a divergence.** The parent's execution printed both sides of both pairs; they disagreed.

## Data model

**No schema change.** The rule is an **application-layer invariant**, enforced by the helper the write path calls.

```
Batch      -> menu_item_id  (existing FK)
OrderItem  -> menu_item_id  (existing FK)
StockEntry -> batch_id      (existing FK)  ─┐
StockEntry -> ref_order_item_id (426's FK) ─┴─ MUST resolve to the same menu_item_id
                                              ── for reason='sale'
StockEntry.qty_delta ABS value MUST equal OrderItem.qty  (for reason='sale')
```

The helper's contract:

```python
def assert_ledger_row_is_coherent(se: StockEntry) -> None:
    """Raise ValueError if the ledger row contradicts the order line it names.

    Applies ONLY to reason='sale'.  A NULL ref_order_item_id on an
    initial/restock/waste row is legitimate and is NOT an error.

    Two checks, in order:
      1. COHERENCE:  batch.menu_item_id == order_item.menu_item_id
      2. MAGNITUDE:  abs(se.qty_delta) == order_item.qty
    """
```

**Why no schema change.** Three of the neighbouring features already change this schema (374 drops a column, 385 adds one, 426 adds a foreign key), and adding a fourth constraint would mean four migrations to one table before a single line of LE31 code writes it. **The invariant is expressible in one function, and the function is where feature 421's write path will call it.** The database-level backstop (a trigger, a composite FK) is feature **413**'s territory and is **recorded, not adopted**.

**⚠️ The `CHECK`-constraint question is NOT answered here.** Feature **394**'s Open Question 1 (*"may a derived stock balance be negative?"*) is **unrelated** and stays open. This feature's rule is about **coherence between two pointers**, and it is answerable without deciding the sign question.

## Implementation steps

1. **Add the helper** to `backend/app/services/stock_rules.py` (new file; `backend/app/services/` does not exist yet — feature 421 creates it). If 421 has not landed, this file may be created by this feature and 421 imports from it. **⚠️ If both land, they must agree on the module path.**
2. **Add the lookup helpers** the rule needs: `get_batch_menu_item_id(session, batch_id)`, `get_order_line(session, order_item_id)` — or one `resolve_sale_context(session, se)` returning a small dataclass carrying `menu_item_id` and `qty`.
3. **Add the call site** to feature **421**'s single write path, **or** — if 421 has not landed — expose the helper with a docstring that says *"the write path must call this"* and leave the call site to 421. **State which of the two happened in the commit message.**
4. **Add the regression test** `backend/tests/test_stock_ledger_coherence.py`:
   - a sale row whose batch is a **different dish** than its order line → **raises**;
   - a sale row whose `ABS(qty_delta)` is **not** the order line's `qty` → **raises**;
   - a sale row naming the **same** dish and the **same** quantity → **accepted**;
   - an `initial` row with `ref_order_item_id = NULL` → **accepted**;
   - a `waste` row with `ref_order_item_id = NULL` → **accepted**.
5. **Record the deferral-chain correction** — one line in feature 421's *Adjacent work* and one in feature 385's, saying *"the coherence rule between the two pointers is feature 441."*
6. **Verify** by re-running the parent's execution probe (the two incoherent rows) against the patched code and asserting both writes are refused.

## Telegram interaction if any

**None.** This feature adds no Telegram surface. It adds a rule to a ledger write path that does not yet exist.

If the write path is later exposed through the cook bot, a **refused** write is an **error path on an existing action** — it must be visible on the surface that made the attempt, consistent with feature 388's HTTP-409-with-`visit_id` precedent. **That is 421's and 413's concern, not this feature's.**

## Dependencies

- **⚠️ Feature 426** (`…stockentry-ref-order-item-id-has-no-foreign-key…`) — **must land FIRST, or in the same PR.** The rule reads `menu_item_id` *through* the order line; if the back-pointer can name a nonexistent row, there is nothing to compare. **Note that 426's FK is declared but unenforced while the pragma is off.**
- **⚠️ Feature 427** (`…sqlite-never-enables-pragma-foreign-keys…`) — **must land FIRST, or in the same PR**, for the same reason: without it, every FK in this table is decorative. **This feature does not enable the pragma.**
- **⚠️ Feature 421** (`…stockentry-append-only-linter-rule…`) — **must land AFTER this one, or in the same PR.** 421 is about to build the single write path; if this rule is not in that path, 421 will implement the defect faithfully, because 421's own text places the business rules out of scope. **This is the upstream-of-filed-work condition.**
- Feature **385** (`…order-item-batch-provenance…`) — **independent.** 385 adds the forward pointer; this rule does not need it and does not conflict with it. **If both land, the two pointers become triply redundant, which is the intended end state.**
- Feature **432** (`…reason-sign-coherence…`) — **independent.** Different axis (`reason` vs the order line). **Same PR is fine; keep the two rules separate.**
- Feature **417** (`…stockentry-actor-foreign-key…`) — **independent.** A different column and a different defect.
- Feature **413** (database triggers) — **the backstop is not adopted here.** Recorded.
- **No new dependency.** The helper uses only `sqlmodel.Session` and the existing models.

## Open questions

1. **⭐ What if a sale legitimately consumes more than one batch?** (A dish with two active batches — the FIFO question feature 03 leaves open.) **The rule as specified assumes one batch per sale line.** Options: (a) one ledger row per batch consumed, each naming the same order line with a **partial** `qty_delta` — which then **breaks the magnitude rule**; (b) allow `|qty_delta| <= order_item.qty` and let the split be the writer's business; (c) defer the magnitude rule until the batch-selection rule (385 + 03's FIFO question) is settled, and keep only the **coherence** rule now. **This is an owner decision and it is not made here.** **The recommended starting position is (c) — ship the coherence rule, which is unambiguous, and defer the magnitude rule until FIFO is answered** — but the contract does not decide it.
2. **Should a `waste` row ever name an order line?** (A waiter cancels a fired line — is that `waste` with a back-pointer, or `cancelled` on the order line with no ledger row?) The rule as specified leaves `waste` unconstrained, because `reason='waste'` rows legitimately have `ref_order_item_id = NULL`. **If waste ever names an order line, the magnitude rule must apply to it too.**
3. **What should the rejection look like?** A raised `ValueError` at the service layer is the default. **HTTP 409** (feature 388's precedent) is the surface-level answer, but the write path does not exist yet, so **there is no surface to answer on.** Recorded for 421 and 413.
4. **Does the rule belong in the database after all?** A composite foreign key (`batch_id`, `menu_item_id`) → `batch(batch_id, menu_item_id)` is expressible in both Postgres and SQLite — but **SQLite requires a `UNIQUE` on the referenced pair**, and `batch` has no such index. **This is a schema change and is deliberately not made here.** It is the natural successor once the pragma and the write path exist.
5. **Should the ledger row snapshot the dish's name?** (The order line does not snapshot the name either — see feature 435's membership finding.) **Not this feature's question.** Recorded.

## Why this matters

**A derived number is only as trustworthy as the rows it is derived from, and LE31's stock number is the product.**

The charter's §3.3 makes current stock a **derivation** from ledger entries. That is the right design — it is the same design feature 374 exists to restore, and the same design that `Donkie/Spoolman` (feature 371) and `ramaraihan12/warung-pos` (feature 373) demonstrate. But a derivation inherits every defect in its inputs. **426 makes the inputs well-formed; 432 makes their sign honest; 404 makes their type honest; 417 makes their actor honest. None of them makes the inputs *coherent with each other*.**

So the failure this feature prevents is the specific one the charter's arithmetic rules **cannot** catch: **an exact derivation over a wrong row is still wrong.** `SUM(qty_delta)` will happily return a number. The bill will happily total a number. Every number in LE31 will be *exactly* right and the **stock on the shelf will not match the stock in the ledger**.

**And it is permanent.** The ledger is append-only **by charter** — that is a feature (features 49, 141, 151, 245, 300 and 421's own linter rule), and it is the right design. But append-only means **a wrong row is forever**: there is no `UPDATE`, no `DELETE`, and (as of today) not even a reversal member. Recovering from a bad row requires a **historical audit with no ground truth to audit against** — which is precisely the failure mode feature 374's `qty_remaining` and feature 385's `OrderItem.batch_id` are named for. **The cheap moment to prevent it is now, before the first ledger row is ever written.**

**Why the ordering with 421 is the sharpest point.** Feature 421 is not a distant feature — it is the feature that builds **the one and only function through which every `StockEntry` in LE31 will ever be written.** It has already decided (correctly) that business rules are somebody else's job. If this contract is not in place when 421 lands, **the wrong rule becomes permanent at the moment the right rule becomes cheap.** That is the whole asymmetry this pass exists to record.

**The cost of getting it wrong.** One stock number is wrong, and it is wrong *silently* — the kitchen screen says 3 portions left and the shelf says 4, and neither number is ever checked against the other. The owner stops trusting the number. **A restaurant owner's confidence in LE31's stock number is the product.**

**The cost of getting it right.** One function, one call site, one test file. Roughly **3–5 hours**, fully reversible (delete the helper and the call), and it makes the ledger's two pointers *mutually redundant* — which is the smallest possible change to the largest possible trust problem.

## Adjacent evidence

- **`ahmershahdev/karobar-erp`** — MIT ✓ §3.2, **★1/⑂0 = NO traction evidence in either direction**, Python/Django + MySQL 8.4, created 2026-11-02, pushed 2026-11-03 = **IN-WINDOW BY BOTH FIELDS**, README read in full (5,038 B). Verbatim: *"The hard parts of an ERP are not the forms: it is **books that always balance**, stock that stays right when two cashiers sell the last item at the same moment."* — **A system that states "books that always balance" as its hard part has had to make the ledger row agree with its source document. LE31 encodes the same relationship in prose only.** ⚠️ **Off-stack** (Django + MySQL) — **the vocabulary-shape is transferable, the code-shape is NOT adopted.**
- **`thomas0903/tickertape`** — Apache-2.0 ✓ §3.2, Rust, created 2026-11-01, pushed 2026-11-03, ★3, README read in full (10,999 B). Its records carry *"opaque payload bytes, a **gap-free sequence number**, a **schema id** and two timestamps"* — **the record identifies what its payload means.** LE31's ledger row carries a `reason` but no statement of which dish the row is about. **Off-stack** (Rust) — vocabulary only.
- **`AlgoVyn/bikri`** — MIT ✓ §3.2, **★1/⑂0**, TypeScript/Hono/Cloudflare, created 2026-10-26, pushed 2026-11-04, README read in full (2,858 B). Its *"Day close and reports — cash-drawer reconciliation"* pairs each end-of-day report with the movements it reconciles. **Not the same rule** (this is the shift/cash side, feature 391's) — recorded as adjacent, **not picked**.
- **`Doublzzz/FactoryFlow`** — MIT ✓ §3.2, Python/FastAPI/Postgres/React, created 2026-10-24, pushed 2026-11-05, ★3, README read in full (11,709 B). Verbatim: *"**每一步由人确认，数量对得上。**"* / *"Every step is confirmed by a person; the quantities add up."* — **the human-confirmation step is the analogue of this rule.** Recorded; **not bundled** (the analogue for the cash path is feature 391's `counted_cash`).

## Adjacent work — recorded, NOT picked

One source artifact touching several invariants → **pick one, record the rest.**

| Rule (source) | LE31's owner | Disposition |
|---|---|---|
| *"stock that stays right when two cashiers sell the last item at the same moment"* (karobar) | feature **394** (guarded-transition primitive) + feature **432** (reason/sign) | **Recorded.** The concurrency half is 394's; this pick is the **coherence** half. |
| *"Every step is confirmed by a person; the quantities add up"* (FactoryFlow) | feature **391** (cash), features 166/172/191 (AI approval) | **Recorded.** Not bundled. |
| *"books that always balance"* (karobar) | feature **433** (double-entry vocabulary) | **Recorded.** Not bundled. |
| *"cash-drawer reconciliation"* (bikri) | feature **391** | **Recorded.** Not bundled. |
