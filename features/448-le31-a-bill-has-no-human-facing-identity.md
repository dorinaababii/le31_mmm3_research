# Feature 448 — `le31-a-bill-has-no-human-facing-identity`

> **Pick B of Daily Brainstorm 2026-11-06 (99th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Bill` (lines 158–169), verbatim:
>
> ```python
> class Bill(SQLModel, table=True):
>     __tablename__ = "bill"
>
>     id: int | None = Field(default=None, primary_key=True)
>     visit_id: int = Field(foreign_key="visit.id", unique=True)
>     subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
>     subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)
>     total_due: Decimal = Field(max_digits=10, decimal_places=2)
>     total_paid: Decimal = Field(max_digits=10, decimal_places=2)
>     payment_method: PaymentMethod
>     paid_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     closed_by: int = Field(foreign_key="app_user.id")
> ```
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite DB, then real inserts):
>
> ```
>   bill id=1 visit_id=2 total_due=5.00 paid_at=2026-11-06 07:09:49.197849
>   bill id=2 visit_id=3 total_due=5.00 paid_at=2026-11-06 07:09:49.214689
>   bill id=3 visit_id=4 total_due=5.00 paid_at=2026-11-06 07:09:49.231427
>
>   TWO NUMBERS: bills on table 1 = 3 ; DISTINCT total_due among them = 1
>
>   Is there ANY human-facing label on a bill?
>      bill.number     present=False
>      bill.no         present=False
>      bill.receipt    present=False
>      bill.code       present=False
>      bill.reference  present=False
>      bill.label      present=False
> ```
>
> **The finding, in one line: LE31 can record that money changed hands, and cannot tell anyone WHICH receipt it was.**
>
> **Evidence class: OBSERVED** (every claim below is a reproducible execution against LE31's own schema). **Confidence: high** for the gap; **medium** for the operational pain (see *Evidence* in the gate verdict and *Open questions*).
>
> **Bucket: v1.** **Build verdict: `build`.**

## Goal

Give every bill **an identity a human can read out loud and a person can point at**.

One column, one allocation rule, one question answered: **"which receipt is this?"**

## Scope

- Add **one column** to `Bill` — a human-facing bill number.
- Allocate it **deterministically**, per service day, from a single sequence.
- Make it **unique** within its period, and **readable** wherever a bill is returned.
- Give the number a **documented shape** so it can be quoted over the phone and found on a receipt.

## Out of scope (v1)

- **A receipt printer, a receipt template, or any printing surface.** Features **362** (ESC/POS receipt vocabulary) and **353** (FloCafe) are the adjacent reference points. **This feature ships the identifier, not the paper.**
- **The bill's membership of lines** — feature **435** owns *which lines a bill charged*.
- **The bill-close route and the bill→visit edge** — feature **415** owns `backend/app/routers/bills.py`.
- **The tip formula and the money rules** — features **408** (tax rate home), **410** (two rule sources), **411** (Decimal guard), **420** (tendered vs received).
- **Split bills.** Feature **14** (`split-bills`) owns the split concept, and `Bill.visit_id` is `unique=True` today, so a split is **not** representable as two bills on one visit. **This feature does not change that** — it gives the bill that *does* exist an identity. **Record the boundary.**
- **A fiscal / legally-numbered invoice.** Feature **131** is a `defer`/parking-lot artifact on fiscal numbering for Latin America; feature **422** records the country-tax boundary. **A fiscal number is jurisdiction-specific and is NOT what this feature adds.**
- **The currency of the money columns.** The charter's §3.6 fixes EUR; feature **409** records the currency question as an open owner question. **This feature does not add a currency column and does not decide the currency.**
- **`Shift` and the `Shift`↔`Bill` money edge** — feature **391** owns those.
- **Alembic, a migration, or any change to `PROJECT_CHARTER.md`.**
- **Any new pip dependency.**

## Description

### What LE31 already believes

LE31 is a **floor** system. Its whole surface is a waiter and a cook, at a table, mid-service. Feature **05** (`payment-tip-reconciliation`) is where the money comes in; feature **415** is where the bill closes.

And yet the bill — the single artefact that represents "the guest has paid" — has **no name**.

### The gap, stated precisely

`Bill.id` is an **auto-increment integer**. It exists, it is a primary key, and it is:

- **never shown to a human** — nothing in the corpus proposes rendering it;
- **not stable across a restore** — an auto-increment sequence is a property of the database file, not of the business, so a restored backup re-issues the same numbers for different bills;
- **not groupable** — there is no service day on it, so "bill 47" does not even mean which evening.

A waiter who wants to confirm *"was this one paid?"* against a receipt has nothing to match. An owner reconciling a stack of receipts has nothing to order them by. A guest reading a receipt has nothing to quote back.

### The direction of the asymmetry matters

This is the same shape as the defect family LE31's audit has now found repeatedly: **a fact the business needs, with no place to put it.**

The asymmetry is precise:

- `Bill` carries **every number** that matters for the money — `subtotal_items`, `subtotal_tax`, `total_due`, `total_paid`, `payment_method`, `paid_at`, `closed_by`.
- `Bill` carries **no name at all**.

And note the neighbouring contrast: **`Table.label` exists.** A table has a name the operator says out loud ("table 4", "the corner one"). A bill — the thing that represents money received — does not. **The system that names its furniture does not name its receipts.**

### Why the plausible wrong answer is the quiet one

The plausible wrong answer is *"the id is the number."*

That answer is **true of the database and false of the restaurant.** The id is a database fact; the number a guest quotes is a **business** fact. Three things follow, and each is a real failure:

1. **It is not stable.** After a restore, id 42 may be a different bill. A receipt in a drawer and a row in the database would then disagree about their identity — and **nothing would detect the disagreement.**
2. **It does not group.** A single counter over the whole database cannot answer *"which bills did we take on Tuesday?"* without an extra query on `paid_at`, and **cannot** be read aloud as "bill forty-two, Tuesday" — the day is not in the number.
3. **It leaks.** Auto-increment ids reveal volume ("we did 400 covers"), and they leak across tenants if LE31 ever hosts more than one restaurant. That last one is a v2 concern and is **recorded, not designed for**.

### Why this is not a small cosmetic thing

The bill is **the receipt**. Feature **415** will write the bill-close route, and the route's natural output is what the guest is handed. If the number does not exist by then, the receipt carries either **nothing** or **an internal id** — and the first is unusable while the second is a leak.

And the cost of adding it *later* is not linear. A bill number allocated after bills exist must either be **backfilled** (inventing numbers for history — a set of numbers the restaurant never saw) or **started mid-stream** (two populations of numbers, one of which the owner must never quote). **Adding the number before the first bill is written is free; adding it after is a permanent complication.**

### The evidence class is important here — and it cuts both ways

- **The gap is OBSERVED** — three bills on one table with identical totals and no distinguishing human-facing field, and a `PRAGMA table_info(bill)` that returns `False` for every candidate name.
- **The pain is INFERRED.** No owner has said *"I could not find the receipt."* There is no complaint, because **there is no bill-close route and therefore no receipt that could have generated one.**

This is why the contract is deliberately small: **one column, one allocator, one uniqueness constraint.** It is not a feature that adds a surface; it is an identifier that has to exist before the surface that shows it.

## Data model

```python
class Bill(SQLModel, table=True):
    __tablename__ = "bill"

    id: int | None = Field(default=None, primary_key=True)
    visit_id: int = Field(foreign_key="visit.id", unique=True)
    bill_number: str = Field(index=True)        # NEW — human-facing, unique per service day
    subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
    ...
```

**The number's shape.** `<service-day>-<sequence>`, e.g. `2026-11-06-0007`. Three properties, each chosen for a reason:

- **the service day** — so a number is self-describing when quoted, and so the day's bills are a contiguous, greppable run;
- **a zero-padded sequence** — so `0007` sorts before `0010` as a *string*, which is how a human reads it and how a spreadsheet sorts it;
- **a hyphen, not a slash** — `2026-11-06-0007` survives being typed into a shell, a URL, a filename and a Telegram message without escaping. (`manoranjan2050/RestoPro-ERP-Web` uses `2026-27/0001`; the slash is fine in a UI and awkward everywhere else.)

**Why the service day and not the calendar date.** The service day is the business day the bill belongs to, and **feature 405** owns that boundary (charter §3.5 says UTC while the linear project says Paris time). **This feature consumes 405's service-day decision and must not define its own.** **If 405 has not landed, this contract's allocator must call the same service-day helper 405 introduces — and must not quietly fall back to `date.today()`.** That is a **hard dependency**, and the alternative (a UTC calendar date) is a *documented fallback*, not a decision.

**Uniqueness.** `UniqueConstraint("bill_number")` — the number is unique **globally**, not per day, because the service day is already inside the number. A per-day unique constraint would allow two bills to share `2026-11-06-0007` if one of them was allocated against the wrong day. **One number, one bill, everywhere.**

**Why a string and not an integer.** The number contains a date and a zero-padded sequence. `20261106-0007` as an integer loses the padding, and `20261106-7` is not the same string a guest reads. A `str` is what actually gets printed. **The type follows the artefact.**

**Allocation.** A single allocator, called from the bill-close write path:

```python
# backend/app/services/billing.py
def next_bill_number(session, service_day: date) -> str:
    """Allocate the next human-facing bill number for a service day."""
    prefix = service_day.isoformat()          # "2026-11-06"
    last = session.exec(
        select(func.max(Bill.bill_number))
        .where(Bill.bill_number.like(prefix + "-%"))
    ).scalar()
    seq = (int(last.rsplit("-", 1)[1]) + 1) if last else 1
    return "%s-%04d" % (prefix, seq)
```

**The race that this allocator has, stated plainly.** A `MAX()+1` is **not safe under concurrency**: two bills closed in the same second could read the same `MAX` and allocate the same number. The `UniqueConstraint` catches it — the second insert raises `IntegrityError` — but **the right response is to retry, not to catch-and-ignore.** Write the allocator so that an `IntegrityError` on the bill number is **retried** with the next sequence value, up to a small bound, and **fails loudly** past that bound. **Do not paper over the collision**: a duplicate number is worse than a failed close, because a failed close is visible and a duplicate number is not.

**A cheaper alternative exists and is recorded, not chosen.** A per-service-day counter *row* (one row per day, incremented under a row lock) makes the allocation atomic without a retry loop. **It adds a table.** For a single-counter restaurant, the `MAX()+1` + constraint + retry is the smaller change; for a busy multi-terminal floor, the counter row is the right answer. **This is recorded as an open question with a named trigger condition, and the contract does not decide it.**

## Implementation steps

1. **Write the regression test FIRST, and watch it fail.** The test that matters most is `test_two_bills_in_one_day_get_different_numbers`.
2. **Add `bill_number: str` to `class Bill`**, non-null, indexed. **The existing `Bill` table has no rows** (no bill-close route exists), so there is **nothing to backfill** — say so in the PR rather than writing a backfill.
3. **Add `UniqueConstraint("bill_number")`** to `Bill.__table_args__`.
4. **Create `backend/app/services/billing.py`** with `next_bill_number(session, service_day)`.
5. **Call the allocator from the bill-close write path** — feature **415** owns that route. **This feature provides the allocator; if 415 has not landed, provide a small `create_bill(...)` helper that the future route will call.** Do not write the route; that is 415's.
6. **Use the service-day helper from feature 405.** Do not call `date.today()` directly. **Do not re-derive the service-day boundary here** — that is 405's, and re-deriving it is how two features end up disagreeing about which evening a bill belongs to.
7. **Handle the `IntegrityError` retry** described above. Two concurrent closes must not silently produce two bills with one number.
8. **Expose `bill_number` wherever a bill is returned**, and **include it in the bill-close response** so the future receipt can print it.
9. **Do not renumber, reorder, or reformat existing numbers.** If the shape changes, it changes for future bills only, and the change is recorded.
10. **Keep `Bill.id` exactly as it is.** It remains the primary key and the FK target for `DerivedTip.bill_id`. **The id does not go away — it simply stops being the only identity.**

### The scenario table (each row is a test)

| # | Situation | Expected |
|---|---|---|
| 1 | First bill of service day `2026-11-06` | `2026-11-06-0001` |
| 2 | Second bill of the same day | `2026-11-06-0002` |
| 3 | First bill of service day `2026-11-07` | `2026-11-07-0001` — **the sequence restarts, the day does not** |
| 4 | Ten bills in one day | `…-0010` — **zero-padded, so it sorts as a string** |
| 5 | Two bills closed concurrently | **two different numbers** — one insert retries |
| 6 | The same number allocated twice | **the second insert raises `IntegrityError`** — never two rows |
| 7 | A bill closed just before midnight | allocated against the **service day**, not the wall clock (feature 405) |
| 8 | The number as rendered | contains the service day and a zero-padded sequence, **and no character that needs shell/URL/filename escaping** |

## Telegram interaction if any

**None in this slice.** The slice ships the identifier.

The operator surface (a receipt carrying the number, a daily summary listing the day's numbers, a `/bill 2026-11-06-0007` lookup) is a **later feature**. The number's shape is chosen so those surfaces are trivial to build later without changing this slice.

## Dependencies

- **Feature 405** (`le31-service-day-boundary`) — **HARD dependency for the allocator.** It owns which business day a bill belongs to. **405 must land first, or in the same PR.** A documented UTC-calendar-date fallback is allowed **only** as an interim, and must be replaced when 405 lands.
- **Feature 415** (`le31-bill-closes-visit`) — owns the bill-close route this feature's allocator is called from. **This slice provides the allocator and, if 415 has not landed, a `create_bill(...)` helper; it does not write the route.**
- **Feature 446** (`le31-has-no-schema-evolution-mechanism`) — **HARD dependency.** This slice **adds a column to an existing table**, which is exactly the operation `create_all()` cannot perform. **446 must land first, or in the same PR.**
- **Feature 435** — owns which lines a bill charged. **Adjacent, not owned here.**
- **Feature 391** — owns the `Payment` table and the `Shift`↔`Payment` edge. **Adjacent.**
- **Feature 14** (`split-bills`) — owns the split concept. **Adjacent: `Bill.visit_id` stays `unique=True` in this slice.**
- **Feature 409** — records the currency question as an open owner question. **Adjacent.**
- **Feature 131** — the `defer`/parking-lot fiscal-numbering artifact. **Recorded, not adopted; a fiscal number is jurisdiction-specific and is out of scope here.**

## Open questions

1. **Should the number restart each service day, or run continuously across days?** This contract chooses **per-day** (the day is inside the number, so it is self-describing). **A continuous counter is the alternative.** The owner's answer determines whether the shape changes, and it should be asked before the first bill is written — **not after.**
2. **Is a per-day counter row worth a table?** The `MAX()+1` + constraint + retry works for a single counter. A busy multi-terminal floor wants an atomic counter row. **Recorded as an open question with a named trigger condition, not decided here.**
3. **Should the number be printed on the guest's receipt, the kitchen ticket, or both?** The receipt is obvious; the kitchen ticket is not, and the two have different audiences. **A later feature's question.**
4. **Should a voided or reopened bill keep its number or consume one?** Feature **37** (`void-rationale-ledger-field`) is adjacent on the void question. **A void policy for bill numbers is not decided here.**
5. **What is the number's format in the guest's language?** The shape here is ASCII and sortable. A localized receipt header is a later concern.
6. **Does the number leak volume?** Per-day numbering makes it worse than a continuous counter — a guest can see how many covers preceded them. **Recorded; not designed for.**

## Why this matters

A restaurant without receipt numbers is a restaurant where *"which one was mine?"* cannot be answered by anyone. The waiter cannot confirm a payment against a receipt. The owner cannot reconcile a stack of paper against a database. The guest cannot quote a number to a phone.

And the failure is **invisible until it is expensive**: a wrong receipt number does not raise an error, does not fail a test, and does not look wrong in the database. It looks like a receipt. It is discovered when a customer disputes a charge and the restaurant cannot produce the matching record — **at which point the amount is small but the trust cost is not.**

The cost of preventing this is **one column, one allocator, one constraint**, with **no rows to backfill** because no bill has ever been written. That is the cheapest moment in LE31's entire history to add it: **the database is empty, so the number can start at 1 with no history to reconcile.**

## Adjacent evidence

- **Trigger source**: `manoranjan2050/RestoPro-ERP-Web` — **MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★1/⑂0**, PHP/Laravel, created **2026-11-04** + pushed **2026-11-05** (in-window by both fields), README read in full (13,110 B). Verbatim, line 91:
  > *"hold and resume, **bill numbers per financial year (`2026-27/0001`)**."*
  **What transfers: the shape — a period prefix plus a zero-padded sequence — and the discipline of restarting the sequence per period so the number says which period it belongs to.** What does **not** transfer: the implementation (Laravel, MySQL/SQLite, a PDF invoice, a "private bill link for the customer", GST/Tax-Invoice switches). **LE31's narrower primitive is a self-describing string that a person can read out loud.**
- **Corroborating source**: `Zula-stdnt/sarisari-store-pos` — **MIT ✓ §3.2**, **★0/⑂0**, JavaScript, created **2026-11-04** + pushed **2026-11-05** (in-window by both fields), README read in full (20,713 B). Verbatim, line 119:
  > *"**🧾 Master-Detail Thermal Receipt Modal:** Completing a sale launches an authentic thermal-receipt dialog complete with **cashier name, transaction ID, timestamp, line breakdown, and change computation**."*
  **The corroboration is in what it puts BESIDE the transaction ID: the cashier's name and the timestamp.** A receipt is identified by a *bundle* of facts about a moment — who, when, which number — and LE31 has **all of the other two** (`Bill.closed_by`, `Bill.paid_at`) and **none of the number.**
- **The corpus probe**: a corpus-wide sweep of all **480 feature contracts** and **446 HANDOFFs** for `bill number`, `bill no`, `bill_no`, `receipt number`, `receipt no`, `invoice number`, `bill identification`, `operator distinguishing bills`, `bill label` and `sequential number` returned **0 matching files** for every phrasing except one incidental mention of `bill.label` in a feature whose subject was a different defect. **The concept "a bill has no human-facing identity" is unowned.**

## Adjacent work — recorded, NOT picked

- **Split bills** — feature **14**. `Bill.visit_id` remains `unique=True`.
- **The receipt-printing surface** — features **362** and **353** (vocabulary references).
- **Fiscal / legally-numbered invoices** — feature **131** (defer/parking-lot) and feature **422** (country tax boundary).
- **The currency of the money columns** — feature **409** (open owner question).
- **The bill's membership of lines** — feature **435**.
- **The bill-close route** — feature **415**.
- **The `Payment` table and the shift money edge** — feature **391**.
- **Voiding and reprinting a bill** — feature **37** (void rationale) and the reprint vocabulary in features **125**, **129**, **130**, **136**, **141**, **150**.
