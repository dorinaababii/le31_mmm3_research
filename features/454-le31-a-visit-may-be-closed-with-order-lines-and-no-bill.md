# Feature 454 — A visit may be closed with order lines and no bill: the walk-out is accepted by the schema, and the money it owes is on no bill

> **Pick B of Daily Brainstorm 2026-11-07 (100th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema and the interaction of two filed features, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> **⭐ The finding is a HOLE BETWEEN TWO FILED FEATURES, not a gap in either.**
>
> - **Feature 415** (`le31-bill-closes-visit-edge`) owns the bill → visit edge. It puts the close **in the bill route** and states verbatim, in its Open questions:
>
>   > *"**Does the bill close the visit, or does the *table release* close the visit?** Two candidate write sites: the bill route, or a separate release route (which feature 388 owns). **This contract puts the close in the bill route**, because a paid bill is the last thing that happens at a table — but **a party that leaves without paying** (a walk-out, or a comped table) then never closes its visit. **What closes a walk-out's visit is undecided.**"*
>
> - **Feature 388** (`le31-table-state-machine`) owns the release path, and states verbatim, in its Scope:
>
>   > *"**A release path.** A route or service call that returns a table to `free` when its visit closes — so the table does not become permanently unseatable. … **If you find yourself writing a bill-closing endpoint, stop — that is feature 14/05's job.**"*
>
> **415 says the walk-out's close is *undecided*. 388 supplies a close that does not go through the bill.** Together they admit a state that neither one owns and neither one forbids: **a closed visit that has order lines and no bill.**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, then the exact sequence 388's release path performs):
>
> ```
>   visit 1:  table_id=1, party_size=2, adults=2
>   order_item:  qty=2, unit_price=8.00        -> 1 order line, worth 16.00
>   ... the waiter releases the table (388's release path sets closed_at) ...
>
>   visit 1: closed_at = 2026-11-07 07:01:55   (set)
>   order lines = 1 ; bills = 0
>
>   TWO NUMBERS:
>     SUM(order_item on the closed visit)  = 16.00
>     SUM(bill.total_due)                 =  0.00
>
>   table 1 is free again; open visits on it = 0
> ```
>
> **€16.00 of food is on no bill. The table is free. The next party can sit down. Nothing anywhere shows the discrepancy.**
>
> **⭐ AND NO QUERY CAN TELL THE TWO KINDS OF CLOSED VISIT APART WITHOUT A JOIN NO DERIVATION MAKES:**
>
> ```
>   visit 1  closed_at=True  bills=0  lines=1     <- the walk-out
>   visit 2  closed_at=True  bills=1  lines=1     <- the normal close
>
>   a query for "closed visits" returns BOTH.
>   distinguishing them requires a JOIN to bill -- which no derivation does.
> ```
>
> **⭐ AND THE SILENTNESS IS THE POINT.** There is no error, no failed request, no missing row to notice. The guest left without paying; the order is real; the kitchen may have cooked it; the stock ledger may have decremented for it; and **the day's sales are short by €16.00 with no signal on any surface.**
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **medium** for the demand — a walk-out is a real restaurant event, but its **frequency** in this specific restaurant is not evidenced and is not claimed. The honest framing: **the schema does not forbid a state that the operator will eventually produce.**

## Goal

Make it **impossible for a visit to close without the money being accounted for**, and make the two legitimate ways of ending a visit **explicit and distinct**:

1. **Paid** — the bill closes the visit. **Feature 415 owns this.**
2. **Voided / written off** — the party left, or the table was comped. **This feature owns this**, and the write must say **which** it is.

The concrete outcome: **`Visit.closed_at` may only be written when the visit has a `Bill`, or when a void/walk-out has been recorded against it — and a void/walk-out is a first-class, queryable fact, not the absence of a bill.**

**The absence of a bill must never be a legitimate state of a closed visit.**

## Scope

**In scope (v1):**

- **A way to record that a visit ended without payment** — a *walk-out* / *void* — as a **fact with a reason**, so the money is accounted for (as zero revenue, or as a loss) rather than silently missing.
- **A guard on the visit-close write**: closing a visit that has order lines and no bill must **refuse** unless the close is a recorded void/walk-out.
- **A decision on where the void lives** — a column on `Visit`, or a row. **The contract does not pick the shape; it states the requirement** (see *Open questions* 1). The implementer must record the choice.
- **The two numbers, side by side**, in whatever surface reconciles the day: the sum of a visit's order lines and the sum of its bill must agree, **or the visit must carry a recorded void explaining the difference**.
- **A regression test** that fails on today's code and passes on the fixed code: close a visit with lines and no bill → **refused**; close it with a recorded void → **accepted**.
- **One line in feature 415's Open questions**, answering what it records as *undecided*: *"what closes a walk-out's visit"*.

## Out of scope (v1)

- **The bill → visit edge, the bill route, the tip derivation and the refusal rules.** That is **feature 415** — filed. This slice does not create `bills.py` and does not re-implement any of 415's rules. **This slice is 415's complement**, and the two are siblings.
- **`Table.status` and the double-seating guard.** That is **feature 388** — filed. This slice does not add a status column and does not add a release endpoint. **This slice supplies the rule that the release path must obey.**
- **The bill-line membership table.** That is **feature 435** — filed. This slice does not add a `bill_line` table. *(It reads the visit's lines to decide whether the close is safe — and **435's ordering constraint applies**: if 435 has not landed, the "does this visit have lines?" question is answered by re-summing the order lines, which 435 says you must not do. **Recorded as an ordering constraint in the HANDOFF.**)*
- **The active-visit write guard** (adding a line to a closed visit) — that is **feature 436** — filed. **Unrelated**: 436 stops a line being *created* against a dead visit; this feature stops a visit being *closed* without an account of its lines.
- **Refunds, partial refunds, and comped *items*.** That is **feature 450** (`le31-a-refund-has-no-payment-to-be-capped-against`) and feature **05**. A voided *visit* is not a refunded *bill*.
- **Cash reconciliation and `Shift.variance`.** That is **feature 391** (the derivation) and **feature 426** (the close endpoint).
- **The `DerivedTip` formula and its refusal rules.** That is **feature 05** and **feature 420**.
- **Any change to `OrderItem`, `Bill`, `DerivedTip`, `Shift`, `Batch` or `StockEntry`.**
- **Alembic, a migration, or a backfill.** §3.2's stated v1 policy is `init_db()`. **There is no historical data**: the only `Visit` write in the whole backend is `backend/app/routers/tables.py` line 51, and **no bill has ever been closed by any shipped code** (feature 415 proves the route does not exist). **The state this feature forbids has therefore never been produced.**

## Description

### The state, as observed in LE31's own schema on 2026-11-07

`backend/app/models.py`, `class Visit`, verbatim:

```python
class Visit(SQLModel, table=True):
    __tablename__ = "visit"
    id: int | None = Field(default=None, primary_key=True)
    table_id: int = Field(foreign_key="table_.id")
    server_id: int = Field(foreign_key="app_user.id")
    opened_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
    closed_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    party_size: int
    adults: int
    children: int = 0
```

**`closed_at` is nullable, and there is nothing else on the visit.** There is no status, no outcome, no reason, no bill reference on `Visit` at all. The bill is related to the visit **from the other side** (`Bill.visit_id`), and that relation is **not unique-constrained from the visit's point of view** — the visit cannot tell whether a bill exists without a join.

**Executed — the walk-out, step by step:**

```
  1. seat a party
       visit 1: table_id=1, party_size=2, adults=2
  2. order
       order_item: qty=2, unit_price=8.00          -> 1 line, worth 16.00
  3. the party leaves without paying
       ... the waiter releases the table (388's release path sets closed_at) ...
       visit 1.closed_at = 2026-11-07 07:01:55
  4. the table is free again
       open visits on table 1 = 0

  RESULT:
       order lines = 1 ; bills = 0
       SUM(order_item on the closed visit)  = 16.00
       SUM(bill.total_due)                 =  0.00
```

**Executed — the two kinds of closed visit are indistinguishable to a plain query:**

```
  visit 1  closed_at=True  bills=0  lines=1     <- the walk-out
  visit 2  closed_at=True  bills=1  lines=1     <- the normal close

  a query for "closed visits" returns BOTH rows.
  separating them requires a JOIN to `bill`.
```

### ⭐ Why this is not "feature 415 with more words"

Feature 415 is about **the edge that does not exist** (nothing ties a paid bill to a closed visit). This is about **an edge that is too permissive** (a closed visit that owes money and has no bill).

The two are complementary, and **the corpus says so itself**. Feature 415's own Scope says:

> *"**The bill-closes-visit edge** — the `Visit.closed_at` write, in the **same transaction** as the `Bill` and `DerivedTip` writes."*

and its Open questions say:

> *"**What closes a walk-out's visit is undecided.**"*

**And feature 388's release path is the write that does it without the bill.** 388 says:

> *"**If you find yourself writing a bill-closing endpoint, stop — that is feature 14/05's job.**"*

— which is correct as far as it goes, and is **exactly why the walk-out needs a rule that belongs to neither**: 415 will not write `closed_at` without a bill, and 388 is forbidden from writing a bill. **Nobody owns the third case, and nobody forbids it.**

### The failure, stated in the shape the corpus already knows

**This is the *contradiction* shape, between two filed features and the schema they share.** The schema says `closed_at` is nullable and unconstrained; 415 says the close happens in the bill route; 388 says the release closes the visit and the bill route is not its business. **The schema permits a state that both filed features' rules forbid and neither enforces.**

**The failure is silent, and that is the whole point** — the same shape as feature 436's finding (*"€25 of food is on no bill"*):

> *"**A defect that leaves two subsystems disagreeing, with no surface where the disagreement can appear, is not a bug that gets noticed — it is a bug that gets believed.**"*

Here the two subsystems are **the order book** (€16.00 of lines) and **the money** (€0.00 billed). The stock ledger is a third: if the dish was prepared and sold, **the kitchen's ledger may have decremented while the money never arrived** — and feature 374 owns the derivation that would make that visible, but there is nothing to derive from, because there is no bill.

### Why the operator will eventually produce this state

Not because of a bug — because of a **Tuesday**. A party leaves without paying. A table is comped. The waiter needs the table back for the next seating and cannot wait for a bill that will never be paid. **Today, the only way to release the table is to close the visit** — and nothing asks whether the money was accounted for. The operator is not doing anything wrong; **the schema gives them no correct alternative.**

**And the cost of getting it wrong is not a crashed page.** It is a day whose sales figure is quietly short, with no receipt to check against, in a business with one owner and no finance staff.

## Data model

**No new table is required. One column may be, and the contract deliberately does not pick the shape** — see *Open questions* 1.

**Shape A — a nullable column on `Visit` (the smaller change):**

```
  visit
    ...
    closed_at        datetime | None      # unchanged
    closed_outcome   str | None            # NULL = open, 'paid' = closed by a bill,
                                          # 'walk_out' = party left without paying,
                                          # 'void' = comped / written off
```

**Shape B — a row (the richer change):**

```
  visit_void
    id               int  (PK)
    visit_id         int  (FK -> visit.id)
    reason           str  ('walk_out' | 'comped' | 'written_off' | 'error')
    amount_forgiven  Decimal   # the money deliberately not collected
    recorded_by      int  (FK -> app_user.id)   # who recorded it
    recorded_at      datetime
```

**The contract's requirements, whichever shape is chosen:**

1. **A closed visit with order lines and no bill is REFUSED**, unless a void/walk-out is recorded in the same transaction.
2. **The void's amount is derived from the visit's lines**, not typed in by the waiter — it is the difference the owner is writing off.
3. **The void names an actor and a reason.** A walk-off with no reason is not a record.
4. **The void is a fact, not an edit** — it must not UPDATE or DELETE the order lines. (The charter's append-only discipline applies to the ledger; **the same reasoning applies here**: a voided visit's lines stay on the visit, and the void is an additional fact beside them.)
5. **The two numbers must be reconcilable**: for every closed visit, `SUM(lines)` equals `bill.total_due` **or** equals `void.amount_forgiven` **plus** a billed amount.

**If Shape B is chosen, the `amount_forgiven` must be a `Decimal`, never a float** — the charter's money invariant (§3.6), and the precedent is feature 411, which proved that the `Decimal` declaration is **not enforced** by the storage layer and must therefore be guarded in code.

## Implementation steps

1. **Write the failing test first.** A test that creates a visit with one order line and no bill, then attempts to close it. **On today's code it SUCCEEDS** (nothing refuses it) — **show it succeeding, then show it failing after the fix.** A test that only ever passed proves nothing.
2. **Decide and record the shape** (A or B) in the code, per *Open questions* 1. **The decision is recorded, not assumed** — the corpus's precedent is that a stored shape with no recorded rule becomes a decision made by accident.
3. **Add the guard at the visit-close write.** The close must check: *does this visit have a bill?* If not, *does it have a recorded void?* If neither, **refuse** — with a clear error naming the two ways out (bill it, or record the void).
4. **Write the void as a fact**, in the **same transaction** as the close. A void that is written and the close that is written must both succeed or neither must.
5. **Derive `amount_forgiven` from the visit's lines.** Never accept it from the request body — the same rule as feature 415's *"It must **not** accept `subtotal_items`, `total_due`, or a tip amount."*
6. **Make the day's reconciliation show both numbers.** Wherever the day is summarised, the sum of the lines and the sum of the billed amounts must be comparable, and the void explains the difference. **This is the surface on which the failure would have been visible** — without it, the defect stays invisible even after the fix.
7. **Answer feature 415's Open question 3** in this contract, and add a one-line pointer in 415's Open questions so the next pass does not re-open it.
8. **Add the tests:**
   - close with lines and no bill → **refused**;
   - close with lines and a recorded void → **accepted**, and the void's amount equals the lines' sum;
   - close with a bill → **accepted** (415's path, unchanged);
   - the refusal writes **nothing** — no void, no `closed_at`;
   - the day's reconciliation shows the void's amount.

## Telegram interaction if any

**None, and this is deliberate.** The walk-out is recorded by the **waiter** at the table (or by the owner at the end of service), on the **waiter web UI** — it is not a cook action and it is not a Telegram command. **The cook bot is untouched.**

**One exception the implementer may consider and must record:** if the owner later wants to void a visit from the phone, that is a **new surface** and a **new decision**, not part of this slice. **Do not add a bot command here.**

## Dependencies

- **Feature 415 (`le31-bill-closes-visit-edge`) — sibling, and it must land FIRST or in the same PR.** 415 owns the paid close. This feature's guard sits on the *same* write. If 415 lands first without this contract, **415 will implement the close faithfully** — closing the visit in the bill route — **and will not notice that a second, unbilled close path exists**, because 415 says the release route is 388's business. **Name 415 in the PR description.** This is the upstream-of-filed-work condition: a filed feature would implement the defective shape faithfully.
- **Feature 435 (`le31-bill-line-membership`) — ordering constraint on the guard's implementation.** The guard needs to know *whether the visit has order lines*. **435 says you must not re-sum the order lines to answer a money question** — *"a reconciliation would have to re-sum the visit's lines, which is exactly what feature 435 says you must not do."* **Therefore: if 435 has not landed, this slice's guard may answer the question by counting the visit's `order_item` rows (a yes/no, not a money derivation), and must NOT compute a money total from them.** Record which it did. **If 435 has landed, use its membership table.**
- **Feature 388 (`le31-table-state-machine`) — sibling.** 388 supplies the release path; this slice supplies the rule that release must obey. **388 must not be re-implemented here** and this slice must not add a status column. **The two must land together or 388's release path will close visits with money owed.**
- **Feature 436 (`le31-active-visit-definition-and-write-guard`) — adjacent, not blocking.** 436 stops a line being *created* against a dead visit; this stops a dead visit from *existing* without an account. **Different write, different rule. Not merged.**
- **Feature 450 (`le31-a-refund-has-no-payment-to-be-capped-against`) — adjacent, not blocking.** 450 owns refunding a **paid bill**. A **voided visit** has no bill to refund. **The two are different objects** and a reader must be able to check each on its own.
- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — depends on it IF Shape B is chosen.** Shape B adds a table; Shape A adds a column. **Either way `create_all()` cannot alter an existing column** — so if Shape A is chosen, **446 must land first**. **If Shape B is chosen, 446 is not needed for the table itself, but it is still the right place to record the prod-migration debt.** **The implementer must state which dependency applies.**

## Open questions

1. **A column on `Visit`, or a `visit_void` table?** **Not decided here — the implementer must record the choice.** *Arguments for Shape A (a column):* one nullable column, no new table, no join to answer "was this voided". *Arguments for Shape B (a table):* a void carries a reason, an actor and an amount, and a table is the append-only shape the charter's ledger discipline already uses. **This contract requires the facts to exist and the guard to enforce them; it does not mandate the storage.**
2. **Is a void *always* a loss, or can it be partially recovered?** **Recorded default: the void records the amount written off; how much of it was recovered (cash in the till, a card charge later) is a separate fact and is NOT modelled here.** That is closer to feature 450's refund territory and is deliberately not pulled in.
3. **Can a void be recorded *after* the visit is closed?** **Recorded default: NO** — the void and the close are one transaction. A void that can be added later is an edit to a closed visit, which is the shape the charter's append-only discipline exists to prevent.
4. **Should a void require a manager's role?** **Recorded default: yes** — a void is the owner writing off money, and `UserRole` has a `manager` member. **But this touches feature 403's role policy, which this slice does not modify.** **Recorded for the owner, not decided here.**
5. **Should the reconciliation surface be built now, or only the guard?** **Recorded default: both.** A guard with no reconciliation leaves the money invisible even when the state is legal — and the reconciliation is what turns "the schema forbids it" into "the owner can see it". **The reconciliation is a small read-only surface, not a new router family.**

## Why this matters

**Because a restaurant loses money, and the schema makes the loss invisible.**

A walk-out is not an edge case; it is a Tuesday. And the reason it is dangerous here is not that it happens — it is that **LE31 has no way to record it**, so the operator's only available move is to close the visit and hope nobody asks. The result is a day whose sales figure is short, with no receipt, no exception line, and no error to notice.

**And the operator is not doing anything wrong.** Today, releasing a table *requires* closing the visit — that is what feature 388's release path does — and the release path is **forbidden** from writing a bill. **The schema gives the waiter no correct alternative.** A system that cannot record a real event will, eventually, hide it.

**The fix is small and it is one of the cheapest in the corpus.** One column or one table, one guard at the close write, one derived amount, one read-only reconciliation surface, five tests. **No data is at risk** — the state this feature forbids has never been produced, because no bill has ever been closed and no release path ships yet.

**And it closes a hole that two filed features leave open between them.** 415 records the question as *undecided*; 388 supplies a write that answers it by accident. **The corpus is good at finding defects in one file. This one is between two files, and it took an executed lifecycle — seat, order, close-without-bill, reconcile — to see it.**

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`manoranjan2050/RestoPro-ERP-Web`** — MIT ✓ §3.2 strictly-compatible, **★1 / ⒂0 = NO traction evidence in either direction**, 7,443 KB, PHP (off-stack for LE31's backend), created **2026-11-04** and pushed in-window = **in-window by BOTH fields**. **Its README states, verbatim: *"bill numbers per financial year (`2026-27/0001`)"* — a fiscal numbering scheme, which is a *different* concern from the walk-out.** **Recorded because it shows a POS that treats the bill as a first-class, numbered business record — and therefore has a place to record a void.** LE31's gap is that it has **no such record at all**.
- **`Zula-stdnt/sarisari-store-pos`** — MIT ✓, ★0 / ⒂0 = **NO traction evidence**, 1,890 KB, JavaScript (off-stack), created **2026-11-04**. Its README states, verbatim: *"cashier name, **transaction ID**, timestamp"*. **Recorded as the same contrast: a till that names every transaction has somewhere to put the one that did not happen.** **Already cited by feature 448 for the bill-identity gap; cited here for the *void* shape.**
- **`AlgoVyn/bikri`** — MIT ✓, ★1 / ⒂0 = **NO traction evidence**, 13,320 KB, TypeScript (off-stack). Its data model declares a **`sale_voids` table**, *"Insert only. Never updated or deleted"*, with a **`CHECK`** on its status, and its `sales` row carries a **derived cache** `status` that is `void` when a `sale_voids` row exists, `refunded` when every line's refunded qty equals the sold qty, else `paid`. **The transferable idea is the vocabulary of a void as an append-only fact beside the sale, with the sale's status derived from it.** **No code is adopted** — TypeScript on Cloudflare D1; LE31 is Python + SQLModel + Postgres.

**Adjacent first-party work — recorded, NOT picked:**

| Feature | Why it is adjacent and NOT picked |
|---|---|
| **415** `le31-bill-closes-visit-edge` | **The primary sibling.** Owns the paid close; this owns the unpaid close. **415 must land first or in the same PR.** |
| **388** `le31-table-state-machine` | **The sibling.** Supplies the release path; this supplies the rule it must obey. |
| **435** `le31-bill-line-membership` | Owns *which lines* a bill charged. **Its ordering constrains this slice's guard** — do not re-sum the lines for money. |
| **436** `le31-active-visit-definition-and-write-guard` | Owns the *write* guard on a dead visit. **Different write, different rule.** |
| **450** `le31-a-refund-has-no-payment-to-be-capped-against` | Owns refunding a **paid bill**. A voided visit has no bill. **Different object.** |
| **416 / 444 / 449** | The price-change, price-origin and price-snapshot rules. **Unrelated to visit closure.** |
| **420** `le31-negative-tip-refusal` | Owns the negative-tip refusal. **Unrelated — a voided visit has no bill and therefore no tip.** |
| **450 / 05** | Refunds and comped *items*. **A voided *visit* is not a refunded *bill*.** |

**External source families fetched this pass (all raw, all re-derived from disk by the parent):**

- **GitHub Search** — 17 date-filtered queries + a 4-request qualifier probe, **21/21 HTTP 200**; aggregate `total_count` = **72,050**; **zero** 73-byte or 6-byte stubs; the **correct `pushed:>=` qualifier** was used and the **dead `pushed_at:>=` qualifier was proved dead by a paired probe** (`topic:restaurant` → 2,963; `pushed_at:>=2026-10-08` → **0**; `pushed:>=2026-10-08` → **583**; `created:>=` → 230). **The restaurant-shaped cluster is ALIVE.** Pipeline: **903 unique repos → 864 in-window → 285 created in-window (fresh) → 393 permissive**; **579 in-window repos were created BEFORE the window start** and are labelled as such.
- **HN Algolia** — 8 queries, 8/8 HTTP 200, **21 hits**, `title: null` = **0**. **4 of 8 queries genuinely returned `nbHits=0`** and are reported as counts, not failures. **0 HN items were promoted to a signal.**
- **OpenAlex** — 3 queries, 3/3 HTTP 200, `meta.count` = **4,076 / 5 / 0** — **distinct** (the filter was applied) and **none near corpus scale**; a diagnostic query for a nonsense term returned **0**, proving the filter is live. Abstracts were carried as **raw `abstract_inverted_index` dumps**, **never paraphrased**. **0 papers were promoted to a signal** — the family is **soft this pass**.
- **ProductHunt** — HTTP 200, 44,100 B (soft source; **not used for a pick**).
- **ScienceDirect** — **NOT RETRIEVABLE** (blocked on this VPS; not attempted).
