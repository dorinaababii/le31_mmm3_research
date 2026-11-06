# Feature 447 — `le31-an-expired-batch-can-still-be-sold-from`

> **Pick A of Daily Brainstorm 2026-11-06 (99th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Batch` (lines 96–110), verbatim:
>
> ```python
> class Batch(SQLModel, table=True):
>     """A concrete prepared quantity of a MenuItem for a specific day.
>
>     E.g. '8 pieces of Tiramisu, prepared 09:00 today'.
>     """
>     __tablename__ = "batch"
>
>     id: int | None = Field(default=None, primary_key=True)
>     menu_item_id: int = Field(foreign_key="menu_item.id")
>     qty_start: int
>     qty_remaining: int
>     prepared_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     expires_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     photo_url: str | None = None
>     notes: str | None = None
> ```
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite DB, then real inserts):
>
> ```
>   batch 1  expires_at = 2026-11-01 09:00   (EXPIRED — four days in the past)
>   batch 2  expires_at = 2026-11-30 09:00   (FRESH)
>   batch 3  expires_at = NULL                (no expiry)
>
>   StockEntry(batch_id=1, qty_delta=-1, reason='sale')                          -> ACCEPTED
>   OrderItem(...) + StockEntry(batch_id=1, qty_delta=-1, reason='sale',
>                                ref_order_item_id=<the new line>)                -> ACCEPTED
>
>   the active-batch predicate (feature 404's), evaluated in SQL:
>     rows matching 'expires_at IS NULL OR expires_at > now()':
>       batch 2  expires_at=2026-11-30 09:00   -> ACTIVE
>       batch 3  expires_at=None                -> ACTIVE
>     rows NOT matching (i.e. EXPIRED):
>       batch 1  expires_at=2026-11-01 09:00   -> EXPIRED but STILL SELLABLE
>
>   TWO NUMBERS: expired batches = 1 ; sales accepted against an expired batch = 2
> ```
>
> **The finding, in one line: the expiry predicate exists and is correct — but it is a SELECT-time filter, and NOTHING at the WRITE path refuses a sale from a batch the predicate has already excluded.**
>
> **Evidence class: OBSERVED** (every claim below is a reproducible execution against LE31's own schema). **Confidence: high** for the gap; **medium** for the operational pain (see *Evidence* in the gate verdict and *Open questions*).
>
> **Bucket: v1.** **Build verdict: `build`.**

## Goal

Make an **expired batch unsellable**.

One rule, one place, at the point where stock leaves a batch: **a sale may not consume a batch whose `expires_at` is in the past.**

## Scope

- Add **one helper** that decides whether a batch may be sold from.
- Call it from **the one write path that consumes a batch** (the `StockEntry` sale write).
- **Refuse** the write — do not silently pick a different batch, and do not silently sell anyway.
- Expose the refusal as a **named, catchable error** so the caller can say *why*.

## Out of scope (v1)

- **The active-batch predicate itself.** Feature **404** owns the rule *"`expires_at IS NULL OR expires_at > now()`"*. **This feature consumes that rule; it does not redefine it.** **404 must land first, or in the same PR** — the helper below is written against 404's predicate, and a NULL-expiry batch must be treated as **sellable** (it has not expired).
- **Deciding which batch a sale consumes.** Feature **385** owns the order-line→batch provenance and the batch-selection question. **This feature does not choose a batch; it refuses one that is named.**
- **The `StockEntry` write path's other rules.** Feature **421** owns the append-only linter rule and where a ledger row may be written; feature **441** owns the rule that the batch pointer and the order-line pointer must name the same dish. **This feature adds one more precondition to the same write path and must not modify their rules.**
- **Auto-marking `sold_out` at expiry.** Explicitly out of scope in feature **404**, and out of scope here. A batch that expires does not become sold-out; it becomes **unsellable**, which is a different statement.
- **A FEFO / first-expired-first-out consumption order.** Features **153** and **372** own FEFO as a deferred v2 surface. **This feature does not reorder consumption.**
- **What an expiry MEANS as a business fact** — whether a batch's expiry is a hard safety deadline or a freshness estimate, and who sets it. Feature **03** owns the batch-creation write path and therefore who writes `expires_at`; feature **405** owns the service-day boundary that an expiry is measured against. **Recorded as open questions, not decided here.**
- **`Batch.expires_at` becoming required.** Feature **404** records the NULL semantics. **This feature does not change the column.**
- **Any new table, router, endpoint or Telegram command.** The slice ships **the rule**, not a surface.
- **Alembic, a migration, or any change to `PROJECT_CHARTER.md`.**
- **Any new pip dependency.**

## Description

### What LE31 already believes

LE31's own vocabulary says an expired batch is not active. Feature **03**'s open question and feature **34**'s rule both use the same wording, quoted in feature **404**:

> *"a batch is active while `SUM(qty_delta) > 0` and `expires_at > now()`"*

Feature **404** then fixes the NULL case and states the predicate as `expires_at IS NULL OR expires_at > now()`.

So LE31 has **one** rule, written **once**, and it is **correct**.

### The gap is not the predicate — it is that nothing enforces it

A predicate used in a `SELECT` is a **filter**. It changes what a *reader* sees. It does not change what a *writer* may do.

Today, `Batch.expires_at` is a column with **no consumer at the write path**. When a sale consumes a batch, the batch is named — and nothing asks whether that batch has expired. The expiry is a **fact about the batch**; the sale is a **fact about the ledger**; **nothing connects them.**

### The direction of the asymmetry matters

This is the same shape as the defect family LE31's audit has now found repeatedly: **a rule that exists in the vocabulary but has no mechanism that can carry it.**

The asymmetry is precise:

- A **reader** that asks "which batches are active?" gets the right answer (feature 404's predicate).
- A **writer** that consumes a batch gets **no question asked at all**.

And the consequence is asymmetric in the *expensive* direction. An expired tiramisu that is sold is **wrong and permanent** — the `StockEntry` ledger is append-only by charter (§4.3), so the row is forever, and it is a row that looks perfectly well-formed: a non-null `batch_id`, an integer `qty_delta`, a `reason` that matches the sign, and an actor who exists. **Nothing about it is malformed. It is semantically incoherent, and there is no rule that could notice.**

### Why the plausible wrong answer is the quiet one

The plausible wrong answer is *"the predicate already handles it"*.

That answer is **true about queries** and **silent about writes**. It is exactly the shape of the 98th pass's *bill membership* finding: a derivation that exists, with no rule about which members qualify. The predicate filters a set; the sale adds a member to a ledger. **Those are two different operations, and only one of them is guarded.**

The second plausible wrong answer is *"there is no selling path yet, so it cannot happen."*

That is **true today** and **irrelevant tomorrow**. There is no `StockEntry` write path outside `models.py` — the parent verified this by execution: `grep -rn 'StockEntry(' backend/` returns **exactly one hit**, the class declaration. But the ledger's write path is **about to be built** (feature **421** owns it), and the same is true of the order path. **A rule that is not written before the path it guards will be written *after* it, and then it will be written wrong** — the path will take the batch id from the request and never ask the question.

### The evidence class is important here — and it cuts both ways

- **The gap is OBSERVED** — a sale against an expired batch was accepted, twice, against LE31's real schema.
- **The pain is INFERRED.** No owner has said *"I sold a stale tiramisu"*. There is no complaint, because **there is no selling path and therefore no ticket that could have generated one.**

This is why the contract is deliberately small: **one helper, one call site, one error type.** It is not a feature that adds a surface; it is a rule that has to exist before the surface it guards.

## Data model

**No schema change.** The rule is an application-level precondition on an existing write.

```python
# backend/app/services/stock_service.py  (feature 374 already plans this module)

class BatchExpiredError(Exception):
    """Raised when a sale tries to consume a batch that has already expired."""
    def __init__(self, batch_id: int, expires_at: datetime):
        self.batch_id = batch_id
        self.expires_at = expires_at
        super().__init__(
            "batch %s expired at %s and cannot be sold from" % (batch_id, expires_at)
        )


def is_sellable(batch: Batch, now: datetime | None = None) -> bool:
    """Feature 404's predicate, evaluated for a WRITE.

    A batch with no expiry has NOT expired (feature 404's recorded default).
    """
    now = now or datetime.now(timezone.utc)
    if batch.expires_at is None:
        return True
    return batch.expires_at > now


def assert_sellable(batch: Batch, now: datetime | None = None) -> None:
    """Raise BatchExpiredError if the batch may not be sold from."""
    if not is_sellable(batch, now=now):
        raise BatchExpiredError(batch.id, batch.expires_at)
```

**Why an application helper and not a `CHECK` constraint:** the rule spans `batch` and `stock_entry`, and a SQLite `CHECK` constraint may only reference the row's own table. A trigger would reintroduce a **dev/prod divergence** (feature **413**'s territory). The rule belongs in the application helper — the same place feature **441**'s coherence rule will live.

**Why not a database trigger:** because LE31 runs SQLite in dev and Postgres in prod (§4.1). A trigger written once does not behave identically in both. **One Python helper, one behaviour, two engines.**

## Implementation steps

1. **Write the regression test FIRST, and watch it fail.** A test that has only ever passed proves nothing. The test that matters is `test_sale_from_expired_batch_is_refused`.
2. **Create `backend/app/services/stock_service.py`** (feature **374** plans this module; if it does not yet exist, create it) with `is_sellable`, `assert_sellable` and `BatchExpiredError`.
3. **Call `assert_sellable(batch)` at the one place a batch is consumed** — the `StockEntry` sale write. **Not** at the `OrderItem` write: the order line may legitimately be written first and the stock deducted at a later step (kitchen dispatch), and refusing at the order write would be the wrong moment. **Record which one you chose and why.**
4. **Do NOT silently substitute a different batch.** If the named batch is expired, the write is refused. Choosing another batch is feature **385**'s question and must not be decided here.
5. **Do NOT auto-mark the batch `sold_out`.** An expired batch is unsellable; `sold_out` is a *different* state (feature **397**).
6. **Use feature 404's predicate exactly**: `expires_at IS NULL OR expires_at > now()`. Do not write a third variant.
7. **Use the same `now` for the whole write.** Read the clock once and pass it down, so a sale cannot straddle a millisecond boundary and disagree with itself.
8. **Handle the NULL case explicitly.** A batch with `expires_at IS NULL` **is sellable** — it has not expired. This is feature 404's recorded default, and getting it backwards would make every null-expiry batch unsellable, which is a worse failure than today's.
9. **Add the refusal to the operator-facing surface later, not now.** The error carries `batch_id` and `expires_at`; what the waiter sees is a later feature's job.

### The scenario table (each row is a test)

| # | Batch | Action | Expected |
|---|---|---|---|
| 1 | `expires_at` in the past | sale consumes it | **REFUSED** — `BatchExpiredError` |
| 2 | `expires_at` in the future | sale consumes it | **ACCEPTED** |
| 3 | `expires_at IS NULL` | sale consumes it | **ACCEPTED** (404's default) |
| 4 | `expires_at` in the past | `reason='waste'` | **ACCEPTED** — waste of an expired batch is *correct*, not an error |
| 5 | `expires_at` in the past | `reason='restock'` | **ACCEPTED** — restocking does not consume |
| 6 | `expires_at` in the past | `reason='initial'` | **ACCEPTED** — not a consumption |
| 7 | `expires_at` exactly == now | sale consumes it | **REFUSED** — `>` is strict; the batch expires AT its expiry instant |
| 8 | expired batch, sale refused | ledger rows for that batch | **UNCHANGED** — the refusal must not half-write |

**Row 4 is the one that will be got wrong.** A rule that refuses *any* write against an expired batch would prevent the kitchen from recording the **waste** of the batch that just expired — which is precisely the write LE31 most wants. **Only `reason='sale'` is a consumption.**

## Telegram interaction if any

**None in this slice.** The slice ships the rule and the error type.

The operator-facing surface (a waiter offering a dish whose batch expired, or the cook being told *"that tiramisu batch expired at 14:00"*) is a **later feature**, and it needs the kitchen dispatch path that does not exist yet. The error carries `batch_id` and `expires_at` so that surface can be built later without changing this slice.

## Dependencies

- **Feature 404** (`le31-active-batch-rule-excludes-null-expiry`) — **HARD dependency.** It owns the predicate this feature consumes. **404 must land first, or in the same PR.**
- **Feature 421** (`le31-stockentry-append-only-linter-rule`) — owns the `StockEntry` write path this feature adds a precondition to. **This must land first, or in the same PR** — 421 is about to build the one and only write path through which every future ledger row will pass, and it explicitly places *business rules* out of scope. **If 421 lands first without this rule, it will implement the gap faithfully.**
- **Feature 441** (`le31-stockentry-may-name-a-batch-and-an-order-line-for-different-dishes`) — owns the *coherence* rule at the same write path. **Adjacent, not blocking; the two must not conflict.**
- **Feature 385** — owns the order-line→batch provenance pointer and the batch-selection question. **Adjacent, not owned here.**
- **Feature 372** / **153** — own FEFO/expiry vocabulary as deferred v2 surfaces. **Adjacent, not owned here.**
- **Feature 397** — owns the `sold_out` state. **Adjacent: this feature does not write `sold_out`.**
- **Feature 405** — owns the service-day boundary an expiry is measured against. **Adjacent, not owned here.**
- **Feature 446** — owns the schema-evolution mechanism. **This slice adds NO column and NO table, so it is not blocked by 446** — but if `backend/app/services/` does not yet exist, note that 446's backup-before-`create_all()` behaviour is the safety net for the first `create_all()` that runs with the new module present.

## Open questions

1. **Is an expiry a hard safety deadline or a freshness estimate?** If it is a freshness estimate, refusing the sale may be the wrong response and the right one may be a warning. **This is an owner decision and it is NOT made here.** The contract implements the *strict* reading because that is the only reading under which the stored `expires_at` means anything at all — and the contract says so rather than guessing.
2. **What happens when the freshest batch is expired but an older one is not?** Refusing outright would stop a sale the restaurant could still serve. Choosing another batch is feature **385**'s question. **This slice refuses; it does not substitute.**
3. **Should the refusal be overridable by a manager?** A manager-comped item is normal in restaurants. **An override path is an owner decision and is not implemented here.**
4. **Should the cook be told at the moment of expiry, or only on the next attempt to sell?** Feature **397**'s `sold_out` state and the kitchen board are the likely homes for a proactive surface.
5. **Is the comparison in UTC or in the restaurant's local service day?** Feature **405** owns the service day. **This slice compares the stored `expires_at` against UTC `now`**, consistent with §3.5, and records the dependency.

## Why this matters

An expired batch that is sold is **wrong in a way the restaurant cannot undo**. The ledger is append-only by charter; the row is permanent; it looks well-formed; and once the bill closes, the money is booked (feature **415** derives the bill from the lines). A customer who is served a batch that expired four days ago is a complaint LE31 cannot answer, because the record says the sale was perfectly ordinary.

And the failure is **invisible by construction**. Feature 404's predicate is a read filter. If the write path never asks the question, then the expiry is recorded, and ignored, forever — and the only place it surfaces is the one place nobody looks: the raw ledger.

This is the cheapest possible prevention of a permanently-wrong record: **one helper, one call site, one error type, no schema change, fully reversible** (delete the helper and the call site and LE31 is exactly where it was). It must land **before** the selling path, because after the selling path exists, the rule will be written against a path that already assumes it is allowed.

## Adjacent evidence

- **Trigger source**: `johnny4young/puntovivo` — **Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **★1/⑂1**, Go, created **2026-10-07** (in-window by both `created_at` and `pushed_at`; `pushed_at` 2026-11-05), README read in full (16,815 B). Verbatim from its README, lines 65–67:
  > *"**📦 Site-owned inventory** — per-site stock authority, a materialized stock rollup maintained by SQLite triggers, **FEFO lot tracking, and an expiry radar** that surfaces value-at-risk before shrinkage happens."*
  **What transfers: the vocabulary and the shape — an expiry is a property of a LOT, and a system that tracks lots surfaces expiry as a first-class condition rather than a filter.** What does **not** transfer: the implementation (SQLite triggers, FEFO ordering, an "expiry radar" dashboard). FEFO ordering is feature **153**'s deferred v2 surface and is **not** adopted here; the expiry *radar* is a surface, and surfaces are out of scope in this slice. **LE31's transferable primitive is narrower and stronger: the write path asks the expiry question and refuses.**
- **Corroborating source**: `hitaishi2222/kinv` — MIT ✓, in-window by `pushed_at` (2026-10-20), README read in full (638 B). Verbatim: *"Searched many inventory system to self-host to keep my kitchen organized and to **know what items I should use before expiry dates**."* **Already filed as feature 372** (a `defer` vocabulary artifact). **It is recorded here as corroboration, not as a second pick**, and it is **not** re-picked.
- **The corpus probe**: a corpus-wide sweep of all **480 feature contracts** and **446 HANDOFFs** for `expired batch`, `expired stock`, `past its expiry`, `sell from an expired`, `refuse … expiry`, `already expired` and `stale batch` returned **0 matching files**. The concept **"an expired batch can still be sold from"** is **unowned**.

## Adjacent work — recorded, NOT picked

- **Auto-marking `sold_out` at expiry** — feature **03**'s open question 2. Explicitly out of scope in feature **404** and here.
- **FEFO consumption ordering** — features **153** and **372** (deferred v2 surfaces).
- **Who writes `expires_at`** — feature **03** owns the batch-creation write path.
- **The service-day boundary** — feature **405**.
- **The NULL-expiry semantics** — feature **404** (the recorded default this feature consumes).
- **The batch-selection question** (which batch a sale consumes) — feature **385**.
- **The coherence rule at the same write path** (the batch pointer and the order-line pointer must name the same dish) — feature **441**.
- **The order line's own batch pointer** — feature **385**.
