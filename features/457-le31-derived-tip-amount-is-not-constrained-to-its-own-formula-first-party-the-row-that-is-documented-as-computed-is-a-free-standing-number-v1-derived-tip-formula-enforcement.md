# Feature 457 — The tip row is documented as computed and is in fact a free-standing number

> **Pick B of Daily Research 2026-11-08 (86th daily-research pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class DerivedTip`, verbatim (lines 172–177):
>
> ```python
> class DerivedTip(SQLModel, table=True):
>     """Computed on bill close: tip = total_paid − (subtotal_items + subtotal_tax)."""
>     __tablename__ = "derived_tip"
>
>     bill_id: int = Field(foreign_key="bill.id", primary_key=True)
>     amount: Decimal = Field(max_digits=10, decimal_places=2)
>     formula_version: str = "v1"
> ```
>
> **The docstring states a formula. The schema states nothing.** `amount` is a `Decimal` column a caller writes. `formula_version` is a bare `str` with **no default constraint and no reference to any formula** — nothing in the database can say which formula `v1` is, and nothing checks that `amount` is the result of applying it.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then real inserts):
>
> ```
>   bill 1: total_paid=25.00  subtotal_items=20.00  subtotal_tax=2.00
>           => the documented formula gives tip = 3.00
>           DerivedTip(bill_id=1, amount=999.00)  -> ACCEPTED       (the formula says 3.00)
>
>   bill 2: total_paid=10.00  subtotal_items=20.00  subtotal_tax=2.00
>           => the documented formula gives tip = -12.00
>           DerivedTip(bill_id=2, amount=-12.00) -> ACCEPTED       (a negative tip, on an underpaid bill)
>
>   DerivedTip(bill_id=1, amount=1.00) -> REFUSED: IntegrityError
>           (bill_id is the PRIMARY KEY, so there is exactly one tip row per bill)
> ```
>
> **⭐ AND NO FEATURE OWNS IT.** A sweep over all **941** feature contracts and HANDOFFs in `features/` + `specs/` returns **zero hits** for a rule constraining `DerivedTip.amount` to its formula — the searches `derived_?tip.{0,60}(constraint|enforce|check)`, `derived_?tip.{0,40}amount.{0,40}enforce` and `formula_version.{0,40}enforce` all return **0**.
>
> **⭐ AND THE CORPUS ALREADY OWNS THE FORMULA'S *INPUT*.** Feature **420** owns what `total_paid` means (*"tendered, not received"* — the change gets booked as tip). **Nothing owns the formula's *output*.** Feature **404** constrains `derived_tip.amount` only to `round(amount, 2)` — **a shape check, not a value check**; a tip of 999.00 passes 404's rule perfectly.
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **medium** for the demand (the charter states the rule; the schema contradicts it). The honest framing: **the charter says the tip is derived and never manually entered, and the schema cannot tell a derived tip from a typed one.**

## Goal

Make the tip **mean one thing**: **the tip on a bill is the number LE31's own formula produces for that bill**, so that when the owner reads the day's tips, every row is a fact rather than a number someone wrote.

The concrete outcome: **the tip is computed from the bill it points at, and the write path refuses a caller-supplied tip amount.**

## Scope

**In scope (v1):**

- **A derivation of `DerivedTip.amount` from the bill** — the tip row's amount is **computed** from `total_paid − (subtotal_items + subtotal_tax)` on the referenced bill, exactly as the class docstring says.
- **A refusal of a caller-supplied `amount`** — the write path does not accept a tip amount from the caller; if one is supplied and it disagrees with the derivation, the write is **refused** with a message naming the bill and both figures.
- **A decision about the negative case** — what happens when `total_paid < subtotal_items + subtotal_tax`. *Recorded default: the tip is derived and may be negative, and the derivation is not refused* — because the bill is underpaid, and **that is a fact about the bill, not an error in the tip.** The bill's own state is a separate question (see *Open questions* 1).
- **A regression test** that fails on today's code and passes on the fixed code: a tip row whose `amount` disagrees with the formula is **refused**, and a tip row whose `amount` agrees is **accepted**.
- **One line in `features/05-payment-tip-reconciliation.md`**, whose data model lists `DerivedTip (bill_id, amount, formula_version)`, so the contract and the schema agree that `amount` is derived.

## Out of scope (v1)

- **The meaning of `total_paid` (tendered vs received).** That is **feature 420** — filed, `build`. **420 changes what the formula yields; it does not enforce that the tip equals the formula.** **420 must be read first — see *Dependencies*.**
- **The tax *rate*.** That is **feature 408** — filed. 408 owns the missing rate that `subtotal_tax` floats free of. **The tip's value is a different question from the tax's rate.**
- **A `CHECK` on `derived_tip.amount`'s shape.** That is **feature 404** — filed. 404 owns `round(x, 2)`. **This slice owns the value's *meaning*, not its shape.**
- **Split bills.** That is **feature 14** — filed. **This is the real rabbit hole: a tip split across two cards has no single `total_paid`, so the derivation has no single answer.** *Open questions* 2 records this and it must be resolved before the slice lands — **not by widening this slice.**
- **The `Bill → order_item` edge and the derivation of `subtotal_items`.** That is **feature 435** — filed. **This slice does not need the edge**: the tip is derived from the *bill's own* four money columns, all of which already exist.
- **A refund.** That is **feature 450** — filed. A refund would change what `total_paid` means; **this slice does not touch refunds.**
- **A `CHECK` constraint on `derived_tip.amount`.** See *Data model* for why a plain SQL `CHECK` **cannot** express this rule and why the implementer must not pretend otherwise.
- **Any change to `Bill`, `OrderItem`, `Visit`, `MenuItem`, `Table`, `Batch`, `StockEntry` or `Shift`.**
- **Alembic.**

## Description

### The defect, as observed in LE31's own code on 2026-11-08

**The charter's P0 acceptance criterion**, `PROJECT_CHARTER.md` line 47, verbatim:

> | **P0** | Waiter can close a bill; tip is **derived** as `total_paid − subtotal_items − subtotal_tax`. | `tip` field appears on `DerivedTip` row; never manually entered. |

**And the schema:**

```python
class DerivedTip(SQLModel, table=True):
    """Computed on bill close: tip = total_paid − (subtotal_items + subtotal_tax)."""
    bill_id: int = Field(foreign_key="bill.id", primary_key=True)
    amount: Decimal = Field(max_digits=10, decimal_places=2)
    formula_version: str = "v1"
```

**The docstring is the specification. The schema does not implement it.** `amount` is `NUMERIC(10, 2) NOT NULL` and nothing more.

**Executed — the live DDL, read back from the created database:**

```sql
CREATE TABLE derived_tip (
    bill_id INTEGER NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,     <- no CHECK, no default, no derivation
    formula_version VARCHAR NOT NULL,    <- a bare string; no constraint, no reference
    PRIMARY KEY (bill_id),
    FOREIGN KEY(bill_id) REFERENCES bill (id)
)
```

**And the whole schema's constraint census:**

```
  TOTAL CHECK constraints across 10 tables: 0
  UNIQUE constraints: bill -> ['visit_id']   (and nothing else)
  UNIQUE indexes:     {}
```

### ⭐ Why this is a first-party defect and not a nitpick

**1. The charter makes a promise the schema does not keep, and the promise is a P0.**

The charter says the tip is **derived** and **"never manually entered"**. Today **nothing in the database can tell a derived tip from a typed one.** A tip of 999.00 on a 22.00 bill and the correct tip of 0.00 are **identical in kind** — both are `NUMERIC(10,2) NOT NULL` rows on `derived_tip`. **The schema cannot honour the charter's P0, and the docstring is the only place the rule exists — which is exactly the "documentation, not a guarantee" shape feature 404 named.**

**2. The tip is the number the owner judges the day by.**

Feature **05** is *Payment, Tip & Reconciliation* — the tip is the receipt of the service, and the day's tip figure is the headline the owner takes away. **A tip that was typed is not a fact about the evening; it is a fact about whoever typed it.** The whole `derived_tip` table exists to be *derived*, and its name says so. **The table is named for the derivation and does not implement it.**

**3. The negative case is where the divergence is largest — and that is exactly where the owner is least able to see it.**

Executed: on a bill where `total_paid = 10.00` and `subtotal_items + subtotal_tax = 22.00`, the formula gives **-12.00**, and a tip of **-12.00** is accepted. **But so is a tip of 999.00 on the *same* underpaid bill.** **Underpayment is the situation where the owner most needs the tip to be a fact and least has the time to check it.** And underpayment is precisely the situation feature **420** identifies as *systematic* — *"the change gets booked as tip"* — **so the formula's output is already known to be fragile in that case.**

**4. `formula_version` is a version string with no referent.**

`formula_version: str = "v1"` exists so that a later formula can be told apart from this one. **But there is nothing in the database that says what `v1` computes, and no rule that ties `amount` to it.** The version column is a **label on a number**, which is the same failure as feature **448**'s *"a bill has no human-facing identity"* — **a name that does not refer to anything checkable.**

### ⭐ The corroboration is inside the corpus already

- **Feature 420** owns the formula's **input** (`total_paid` means tendered, not received). **It does not own the output.**
- **Feature 404** constrains `derived_tip.amount` to `round(amount, 2)` — **a shape check.** 999.00 passes it. **404's own scope says it is about "columns where corruption is currently silent"** — *silent corruption* is a **type** failure (a float in a money column, a text in an integer column). **A tip of 999.00 is not corrupt; it is a perfectly-shaped number that is simply not the right number.** **That is a different failure and a different rule.**
- **Feature 411** owns money *precision* — `Decimal` declared but not enforced, `12.345` silently coerced. **Again: a shape failure.** A tip of 999.00 is precise.
- **Feature 408** owns the tax *rate*. **The tip is not the tax.**
- **Feature 435** owns the missing `Bill → order_item` edge — **how `subtotal_items` is arrived at.** **This slice starts one step later: given the four money columns the bill already has, is the tip the formula's answer?**

**The pattern is exact: three features own the *shape* of LE31's money, and none owns the *meaning* of its most judgement-bearing number.**

### Why it lands before the bill route ships

**No bill-closing route exists.** The shipped backend has one router (`backend/app/routers/tables.py` — `list_tables`, `seat_party`) and **no bill, no payment, no reconciliation**. Feature **415** records this: *"no bills router exists and nothing ties a paid bill to a closed visit."* **So there is no write path to correct today, and no data to migrate.** **The rule is free to install now and expensive to retrofit** — once bills exist, a wrong tip is already in the owner's records.

## Data model

**No new table. No new column. One derivation, enforced in the write path.**

```
  BEFORE (today)
    derived_tip
      bill_id         INTEGER  primary key
      amount          NUMERIC(10, 2) NOT NULL     <- a caller writes this
      formula_version VARCHAR NOT NULL
      ...

  AFTER (this slice)
    derived_tip
      bill_id         INTEGER  primary key
      amount          NUMERIC(10, 2) NOT NULL     <- COMPUTED from the bill
      formula_version VARCHAR NOT NULL            <- the version the derivation used
      ...
```

**⭐ The rule cannot be a plain SQL `CHECK`, and the implementer must not pretend it can.**

A SQL `CHECK` constraint may only reference columns of the **same row**. `amount` depends on `bill.total_paid`, `bill.subtotal_items` and `bill.subtotal_tax` — **three columns of another table.** There is no portable `CHECK` that expresses *"this number equals that formula over there"*. **A `CHECK` on `amount` could only assert something about `amount` alone** (for example `amount = round(amount, 2)`), **which is feature 404's shape check and does not enforce the formula.**

**Therefore the enforcement is in the write path, and the contract says so:**

1. **The tip amount is computed by the code that closes a bill**, from the bill's own four money columns: `amount = total_paid − (subtotal_items + subtotal_tax)`, in `Decimal` arithmetic, with the **same rounding rule the rest of LE31's money uses** (feature **410** owns the reconciliation of the charter's flat-rate total against the per-line rate — **this slice must not invent a third rule; it must use the one 410 records, and if 410 has not landed, the implementer records which rule they used and why**).
2. **A caller-supplied `amount` is refused.** If a caller supplies an amount and it disagrees with the derivation, the write is **refused** with a message naming the bill and both figures. **If it agrees, it is accepted** — so a round-trip that happens to be correct is not punished.
3. **`formula_version` is written by the derivation**, not by the caller, and it records **which formula produced the number** — which is the only thing that makes the column refer to something.
4. **One tip row per bill** — already true, because `bill_id` is the primary key. **This slice preserves it and must not weaken it.** (Executed: a second `DerivedTip` for the same bill is refused with `IntegrityError`.)

**⭐ Why the derivation, and not a trigger, and not a view.** A **trigger** would put business logic in the database, where LE31's other rules live in Python, and would need to be duplicated per engine. A **view** would not protect the stored value. **The write path is where LE31's other invariants live** — feature **452**'s "a served line must not still say it is new" is enforced there too. **One place, one rule.**

**The `Decimal` requirement is not negotiable.** The derivation must use `Decimal` arithmetic end to end and must not round-trip through `float` — **feature 411** proved that `Decimal` is a Python-side guarantee the storage layer does not enforce, and this slice is on the Python side, so **this slice is the one place the guarantee can actually be kept.**

## Implementation steps

1. **Read feature 420 FIRST and confirm what `total_paid` means** in the version being implemented. **420 changes the formula's output.** If 420 has not landed, **record that the derivation follows the charter's formula against the current meaning of `total_paid`, and note that the value will change when 420 lands.**
2. **Read feature 410 and use the recorded rounding rule.** **Do not invent one.** If 410 has not landed, **record the rule used and the reason.**
3. **Write the failing test first.** A test that closes a bill and asserts the tip equals the formula — and a test that supplies a **wrong** tip amount and asserts the write is **refused**. **On today's code the wrong amount is ACCEPTED** — show it succeeding, then show it failing after the fix. **A test that only ever passed proves nothing.**
4. **Implement the derivation** as a small pure function — `derive_tip(bill) -> Decimal` — in the service layer, returning the amount **and** the `formula_version` it used.
5. **Refuse a caller-supplied `amount`** in the bill-closing write path when it disagrees with the derivation; **the message names the bill, the supplied amount and the derived amount.**
6. **Write `formula_version` from the derivation**, not from the caller.
7. **Update `features/05-payment-tip-reconciliation.md`**'s data-model line to state that `amount` is derived, so the contract and the schema agree.
8. **Add the tests:**
   - the tip on a normally-paid bill equals the formula;
   - a supplied amount that **agrees** with the formula is accepted (**this test matters: a rule that only ever refuses is a bad rule**);
   - a supplied amount that **disagrees** is refused, and the message names both figures;
   - **a second tip row for the same bill is refused** (the primary key must survive the change);
   - the derivation uses `Decimal` and does **not** round-trip through `float` — a test that asserts `isinstance(result, Decimal)` and that a bill whose subtotals have more than two decimals is rounded by the **recorded** rule;
   - **the negative case** — an underpaid bill derives a negative tip and **is not refused** (*Open questions* 1's default).
9. **Record the precedent.** A note that LE31 now has **a derived money value**, and that **`derived_tip` is the first table whose value is computed rather than supplied** — so that a later feature adding another derived column knows where the rule lives.

## Telegram interaction if any

**None.** This slice touches no bot command and no handler. The tip is computed at bill close, which is a waiter-surface action.

**The one relationship worth stating:** feature **39** (the owner daily recap) and feature **05** (payment, tip and reconciliation) both read the day's tips. **A typed tip makes the recap report a number that was never earned and was never derived** — and the recap is the artifact the owner actually reads. **That is a consequence of the defect, not a separate scope, and no bot change is proposed here.**

## Dependencies

- **Feature 420 (`le31-total-paid-means-tendered-not-received`) — READ FIRST; this slice's derivation depends on it.** 420 establishes that `total_paid` means *tendered*, not *received*, so the change is booked as tip. **That changes what the formula yields.** **This is a dependency, not a conflict** — 420 owns the *input*, this slice owns the *output*. **If 420 lands after this slice, the derived values change and the slice's tests must be updated; the implementer must say which order was used and why.**
- **Feature 410 (`le31-two-money-rule-sources`) — read for the rounding rule.** This slice must not invent a third money rule. **If 410 has not landed, record the rule used.**
- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — NOT a hard blocker for this slice, unlike features 456 and 458.** This slice adds **no schema change** — it changes the **write path**. **It is recorded here so the implementer does not assume it is exempt for the wrong reason:** if the implementer *does* add a column (for example, a stored `formula_amount` or a derivation marker), **446 then blocks it.**
- **Feature 404 (`le31-sqlite-tables-not-strict`) — adjacent, not blocking.** 404 owns the *shape* check on `derived_tip.amount`; this slice owns the *meaning*. **Separate slices.**
- **Feature 411 (`le31-money-precision-declared-not-enforced`) — adjacent, not blocking.** 411 owns precision; this slice owns derivation. **A value can be precise and wrong** — 999.00 satisfies both slices.
- **Feature 435 (`le31-bill-records-no-which-lines-it-charged`) — adjacent, not blocking.** 435 owns where `subtotal_items` comes from. **This slice uses the bill's stored columns as they are** and does not need the edge.
- **Feature 415 (`le31-bill-closes-visit`) — the route this slice lands in.** 415 owns the bill-closing edge and **owns the route that does not exist yet.** **This slice's derivation belongs in that write path** — and if 415 has not landed, **this slice's rule has nowhere to live and must wait or must introduce the write path itself, which would duplicate 415.** **Recorded explicitly, because "the write path does not exist" is the single most likely way for this slice to go wrong.**
- **Feature 14 (`split-bills`) — the real rabbit hole.** A tip split across two tenders has no single `total_paid`, so the derivation has no single answer. **Open questions* 2 records this. **This slice must not resolve it by widening.**
- **Feature 450 (`le31-a-refund-has-no-payment-to-be-capped-against`) — adjacent, not blocking.** A refund changes what was paid; this slice does not touch refunds.

## Open questions

1. **What happens when the derived tip is negative** (an underpaid bill)? *Recorded default: **the tip is derived and may be negative, and the derivation is not refused.*** The bill being underpaid is a **fact about the bill**, not an error in the tip — and refusing the write would leave the bill closed with **no tip row at all**, which is worse. **The bill's own state for an underpayment is a separate question that this slice does not answer.** **Recorded so the negative is a decision, not an oversight.**
2. **How does the formula behave on a split bill** (feature 14)? *Recorded default: **this slice does not answer it and must not be widened to.*** A split bill has several tenders; the tip on it is either allocated across the splits or booked against the whole bill. **This is a design question for feature 14 and must be settled there before this slice's derivation meets a split bill.** **If 14 lands first, this slice must read it.**
3. **Should the derived tip be stored at all, or computed on read?** *Recorded default: **stored**, because that is what the charter's P0 says (*"`tip` field appears on `DerivedTip` row"*) and because the table already exists. **A computed-on-read tip would remove the column rather than constrain it — a v2 decision, not this slice's.**
4. **What does `formula_version = "v1"` refer to, and where is it defined?** *Recorded default: **the implementer must define it in code as the single named constant the derivation uses**, and the stored value is that constant's value. **Today `formula_version` is a bare literal default and nothing in the database or the code refers to it.** **Recorded because a version string with no referent is exactly feature 448's shape, and this slice should not reproduce it.**
5. **Does a *correct* caller-supplied amount get accepted, or is every supplied amount refused?** *Recorded default: **accepted if it agrees with the derivation; refused if it disagrees.*** Refusing every supplied amount would break a round-trip and teach the caller the rule is hostile. **Recorded so the implementer does not over-reach.**

## Why this matters

**Because the tip is the number the owner takes away, and LE31 lets it be a number someone typed.**

Everything else LE31 has been careful about money has been about the **shape** of the value: `Decimal` and not `float` (411), two-decimal rounding (404), a rate for the tax (408), an edge to the lines that were charged (435). **Every one of those is about making a number well-formed.** **None of them is about making the number *right*.** And the tip is the one number in the system that is **not** a measurement of a physical thing — it is the result of a rule, and therefore the one number that most needs the rule to be enforced.

**The cost of the defect is not a crash.** It is a day that closes with a tip of 999.00, a recap that reports it, and an owner who has no way to tell a derived fact from a typed one — because in the database, **there is no difference to tell**. The table is *named* `derived_tip`. **The name is the promise, and the schema is the place where a promise has to be kept.**

**The cost of the fix is small and the value is high.** The derivation is a subtraction the charter already specifies. **The fix is to make the code that closes a bill compute the tip instead of accepting it.** There is no migration, no schema change, no new table, and no new surface.

**And today it is free.** No bill-closing route exists, so no bill has ever been closed and no tip has ever been written. **The rule can be installed before the first one.** That is the whole argument for doing it now rather than after the first day of service.

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`Apurba94/shopdesk`** — MIT ✓ §3.2 strictly-compatible, **★0 / ⒂0 = NO traction evidence in either direction**, **15 KB**, Python (on-stack language), created and pushed **2026-11-04** = **in-window by both fields**, README read in full. Its stated rules, verbatim:
  > *"**Bills** with discounts, and loose quantities such as 1.5 kg. Stock falls by itself, and **you cannot sell more than you hold**"*
  > *"**True profit:** cost uses the weighted average, so profit stays right when buying prices change"*
  > *"**Money is held as whole paisa**, so totals are always exact."*
  > *"App tests run a sale end to end and **confirm that a failed sale changes nothing**, and that **a customer cannot pay more than they owe**."*

  **Recorded because the last clause is this slice's rule in a different costume:** *"a customer cannot pay more than they owe"* is the same discipline as *"the tip on a bill cannot be more than the derivation says"* — **a value checked against the fact it derives from, at write time.** And *"confirm that a failed sale changes nothing"* is the **end-to-end acceptance shape** this slice's tests should take.

  **The transferable idea is the write-time refusal and the end-to-end proof.** **No code is adopted**, and the reason is recorded plainly: its money is held as **whole paisa**, a **v2 representation decision LE31 has explicitly deferred** (feature 404 records it), and **★0 / ⒂0 is no traction in either direction.**

- **`smithadifd/ledger`** — MIT ✓, **★0 / ⒂0 = NO traction evidence**, 550 KB, Python (on-stack), created **2026-11-02** and pushed **2026-11-07** = **in-window by both fields**, README read in full. Verbatim:
  > *"Current state is derived from the events and never edited."*
  > *"Every fact has one owner, and the views that show a fact name the events they were built from."*

  **Recorded because it states the exact discipline this slice is about, in one sentence:** a derived value is derived and never edited. **`DerivedTip` names a formula in a docstring and nothing else** — it does not name the events it was built from, and it can be edited freely. **The vocabulary transfers; no code is adopted** (a hash-chained work-item log for AI agents, not a restaurant tip).

- **`huv0310-arch/verdict-ledger`** — MIT ✓, **★0 / ⒂0 = NO traction evidence**, 167 KB, Python (on-stack), created **2026-11-06** and pushed **2026-11-08** = **in-window by both fields**, README read in full. Verbatim:
  > *"**判错了能翻** —— 翻案走追加：新判决盖在旧判决上，历史一行不删，**谁翻的、为什么翻都留在账上**——「改过」本身也是审计要的证据。"*
  > (A reversal is an append: the new verdict overlays the old, not one line of history is deleted; **who reversed it and why both stay on the ledger — *the fact of having been changed* is itself the evidence the audit needs.**)

  **Recorded because it answers the obvious objection to this slice** — *"what if the tip was wrong?"* **In that ledger, a correction is a new fact, and the old fact survives.** **LE31's `DerivedTip` has no correction path at all** — `bill_id` is the primary key, so a second tip row for the same bill is refused. **That is a genuine tension and it is recorded, not resolved here**: this slice makes the *first* tip correct; **the ability to correct it is a separate question, and the append-only answer (a correction row plus a supersession marker) is a v2 shape that would change `DerivedTip`'s primary key.** **Recorded as adjacent, out of scope, and worth a future pass.**

**Adjacent first-party work — recorded, NOT picked:**

| Feature | Why it is adjacent and NOT picked |
|---|---|
| **420** `le31-total-paid-means-tendered-not-received` | Owns the formula's **input**. **Read first.** Not merged. |
| **410** `le31-two-money-rule-sources` | Owns the money rounding-rule reconciliation. **Read for the rule.** Not merged. |
| **404** `le31-sqlite-tables-not-strict` | Owns the **shape** check on `derived_tip.amount`. **This slice owns the *meaning*.** Not merged. |
| **411** `le31-money-precision-declared-not-enforced` | Owns money **precision**. **A precise number can still be the wrong number.** Not merged. |
| **408** `le31-tax-rate-has-no-home` | Owns the **tax rate**. **The tip is not the tax.** Not merged. |
| **435** `le31-bill-records-no-which-lines-it-charged` | Owns the missing `Bill → order_item` edge. **This slice needs the bill's stored columns, not the edge.** Not merged. |
| **415** `le31-bill-closes-visit` | Owns the bill-closing edge and the route that does not exist yet. **This slice's derivation belongs in that route.** Not merged. |
| **14** `split-bills` | Owns the multi-tender case. **The real rabbit hole.** Not merged. |
| **450** `le31-a-refund-has-no-payment-to-be-capped-against` | Owns refunds. Not merged. |

**External source families fetched this pass (all raw, all re-derived from disk by the parent):**

- **GitHub Search** — 14 date-filtered queries + a 4-request qualifier probe, **18/18 HTTP 200**; aggregate `total_count` = **19,648**; **zero** 73-byte or 6-byte stubs; the **correct `pushed:>=` qualifier** was used and the **dead `pushed_at:>=` qualifier was proved dead by a paired probe** (`topic:restaurant` → 2,972; `pushed_at:>=2026-11-01` → **0**; `pushed:>=2026-11-01` → **169**; `created:>=2026-11-01` → **45**). **The restaurant-shaped cluster is ALIVE.** **30 candidates verified by a direct `GET /repos/{owner}/{repo}`** plus a README fetch: **10 permissive / 20 licence-incompatible**, **30/30 in-window by BOTH fields**, **every permissive candidate ★0 or ★1 and ⒂0 — NO traction in either direction.**
- **HN Algolia** — 10 queries, 10/10 HTTP 200, **30 hits**, `title: null` = **0**; **4 of 10 queries returned `nbHits = 0`** and are reported as counts. **All 30 hits read; 0 promoted to a signal** — the largest bucket (`point of sale`, 17 hits) holds **zero POS items**.
- **OpenAlex** — 9 queries, 9/9 HTTP 200, `meta.count` = **611 / 626 / 886 / 56 / 66 / 29 / 57 / 3,113** — distinct; a nonsense-term control returned **0**, proving the filter is live. Abstracts carried as **raw `abstract_inverted_index` dumps**, never paraphrased. **0 papers promoted to a signal.**
- **PyPI** — 10/10 HTTP 200; **4 in-window releases** (`fastapi` ×2, `sqlalchemy` ×4 versions, `pydantic` ×1); `sqlmodel`, `aiogram`, `uvicorn`, `alembic`, `httpx` = **0 in-window**. **No pin-bump proposed.**
- **GitHub `release.atom`** — 9/10 HTTP 200, **90 entries**; `sqlmodel/sqlmodel` = **0 entries** (valid empty feed); `python-telegram/bot` = **HTTP 404**.
- **EU** — 5/5 HTTP 200; ECB daily XML `time='2026-11-06'`, **USD = 1.1165**; CNIL EN/FR RSS 10 items each; **EUR-Lex ELI = HTTP 200 with the real GDPR document**.
- **ScienceDirect** — **NOT RETRIEVABLE** (blocked on this VPS; not attempted).
