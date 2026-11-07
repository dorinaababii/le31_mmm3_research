# Feature 453 — SQLite silently drops the UTC offset: "Time is UTC" is not enforced by the storage layer, and dev and prod disagree about every timestamp

> **Pick C of Daily Brainstorm 2026-11-07 (100th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema and its own storage layer, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `PROJECT_CHARTER.md` line 230, verbatim:
>
> > - **Time is UTC.** `datetime.now(timezone.utc)` everywhere.
>
> And `backend/app/models.py` line 22, verbatim:
>
> ```python
> def utcnow() -> datetime:
>     return datetime.now(timezone.utc)
> ```
>
> **The SOURCE is correct.** Executed: `utcnow()` returns `datetime.datetime(2026, 11, 7, 7, 5, 6, 742981, tzinfo=datetime.timezone.utc)`; `utcoffset()` is `timedelta(0)`. Every `default_factory=utcnow` writes a correct, tz-aware UTC instant.
>
> **The STORAGE LAYER is not.** Executed against LE31's real schema (`SQLModel.metadata.create_all` on a throwaway SQLite file — the charter's stated dev database):
>
> ```
>   write:  Batch(prepared_at=utcnow())     # tz-aware UTC, correct
>   READ BACK (what every SELECT does):
>     prepared_at = datetime.datetime(2026, 11, 7, 7, 5, 6, 766506)     tzinfo = None
>   RAW stored value = '2026-11-07 07:05:06.766506'    (sqlite typeof = text)
> ```
>
> **⭐ THE VALUE ROUND-TRIPS; THE TYPE DOES NOT.** `DateTime(timezone=True)` on SQLite renders `DATETIME` — a wall-clock **string**. SQLite has no `TIMESTAMPTZ`. The wall-clock is stored correctly (it *is* UTC), but on the way back the `tzinfo` is **gone**: what the application receives is a **naive** datetime. It is no longer an *instant*; it is a wall-clock with no zone attached.
>
> **⭐ AND THE TWO FAILURE MODES ARE DIFFERENT IN KIND — ONE IS A CRASH, NOT A WRONG NUMBER:**
>
> ```
>   # comparison against an aware value
>   b.prepared_at > utcnow()
>     -> TypeError: can't compare offset-naive and offset-aware datetimes
>
>   # and the storage layer does not enforce UTC either
>   write prepared_at = datetime(2026,11,7,23,30, tzinfo=Europe/Paris)   # +01:00
>     RAW stored = '2026-11-07 23:30:00.000000'
>     TRUE instant = 2026-11-07T22:30:00+00:00
>     -> the stored wall-clock is -3600 s from the true instant
> ```
>
> So the charter's *"Time is UTC"* is a **convention the application follows on write and the database does not enforce on read**. A Paris-local instant written by any future code path (the cook bot, a report, an import) is silently stored as the wrong instant — **off by exactly the UTC offset**, which is **+1 hour in winter and +2 hours in summer in Paris**. The offset is not a constant, so the error is not a constant either: it **changes with the season**, and it changes **silently**.
>
> **⭐ AND THE TWO ENVIRONMENTS DISAGREE ABOUT THE PYTHON TYPE.** The same declaration renders `TIMESTAMP WITH TIME ZONE` (`timestamptz`) on Postgres and `DATETIME` (text) on SQLite. On Postgres a read returns an **aware** datetime; on SQLite it returns a **naive** one. The same query code therefore behaves differently in dev and prod — and the failure in dev is a `TypeError` that never occurs in prod, so the bug is **only reachable in the environment where it is least likely to be reproduced**.
>
> **⭐ AND IT BREAKS A FILED FEATURE'S OWN SPECIFIED HELPER.** Feature **405** (`le31-service-day-boundary`) specifies a helper that *refuses* naive input. Executed against the exact guard 405 specifies:
>
> ```python
>   if instant.tzinfo is None:
>       raise ValueError("business_date() requires a timezone-aware instant; ...")
> ```
>
> ```
>   read back prepared_at -> tzinfo = None
>   business_date_405(prepared_at)
>     -> ValueError: business_date() requires a timezone-aware instant; a naive datetime is ambiguous
> ```
>
> **405's helper raises on EVERY value read from SQLite.** The app writes tz-aware UTC; SQLite returns naive; the helper 405 specifies rejects it. **On the charter's own dev database, 405's central helper is un-callable.** This is the *upstream-of-filed-work* condition in its sharpest form: a filed feature would implement a guard that **fails closed on every real query**.
>
> **⭐ AND IT CORRUPTS THE BUSINESS-DAY ANSWER AT THE BUSIEST HOUR.** Executed on one database:
>
> ```
>   prepared_at = 2026-11-07T23:30:00+00:00     (Paris: 2026-11-08 00:30)
>   'today's batches' by UTC date   (2026-11-07) -> 3 rows
>   'today's batches' by Paris date (2026-11-08) -> 0 rows
> ```
>
> **The same database, the same instant, two different answers — 3 rows or 0.** The charter's P0 row 43 says *"Waiter can browse **today's** menu"*, and feature 405 exists precisely to name that day. The midnight hour is **the busiest hour in a restaurant**, not a quiet one, so this divergence is concentrated exactly where the money is.
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a wrong day — the corpus confirms it: feature 405 records *"The LE31 owner has never complained about a wrong day"*). The gap is **defensive rather than reactive**, exactly as 405 itself frames it — but this one is *cheaper* than 405's fix and it **makes 405's fix callable at all**.

## Goal

Make LE31's timestamps be **instants** on every read, on every database, so that:

1. **The storage layer enforces the charter's "Time is UTC" rule** rather than trusting every future writer to comply.
2. **A value read from the database is comparable with `now()`** without a `TypeError`.
3. **Feature 405's specified guard is callable** on the charter's dev database.
4. **Dev and prod return the same Python type** for the same column.

The concrete outcome: **every `datetime` column in LE31 stores and returns a timezone-aware UTC instant, and a naive value cannot be written.**

**This slice does not decide what a service day is.** Feature 405 owns that. This slice makes the *input* to 405's decision trustworthy.

## Scope

**In scope (v1):**

- **A single storage type used by every `datetime` column**, replacing the bare `Column(DateTime(timezone=True))` declarations, so that the value written is always a UTC instant and the value read is always tz-aware.
- **One helper that normalises at the boundary** — e.g. `to_utc_instant(value) -> datetime` — which accepts an aware instant (converting it to UTC) and **rejects a naive value** with a clear error naming the call site.
- **The conversion applied at the two places the values enter and leave**: the `default_factory` writers and the read path.
- **A regression test** that fails on today's code and passes on the fixed code, covering: (a) a value written by `utcnow()` and read back is tz-aware; (b) a Paris-local value is stored as its UTC instant; (c) a read-back value is comparable with `now()`; (d) feature 405's guard accepts a value read from the database.
- **One line in the coding-agent checklist** (`coding-agent/checklist.md`), whose *"Every timestamp is `TIMESTAMPTZ`"* line is already known to be wrong for SQLite (feature 410, Open Question 4), corrected to name the real behaviour.

**Explicitly NOT in scope:**

- **The business-date / service-day column and its semantics.** That is **feature 405** — filed. This slice does not add a column, does not name a day, and does not decide when a service day starts. **405 depends on this slice; this slice does not depend on 405.**
- **Any change to `Batch.expires_at`'s nullability or to the active-batch predicate.** That is **feature 404** — filed. This slice does not touch the predicate's *meaning*.
- **`Batch.qty_remaining`.** That is **feature 374** — filed.
- **Alembic, a migration, or a data backfill.** §3.2's stated v1 policy is `init_db()`. **There is no historical data to migrate**: the only `Visit` write in the whole backend is `backend/app/routers/tables.py` line 51, and no `Batch`, `Bill` or `StockEntry` row has ever been written by any shipped code path. **Recorded, and it is the reason this slice is cheap.**
- **Postgres-specific column types (`TIMESTAMPTZ`, `JSONB`, `UUID`, `ARRAY`).** The charter forbids them in v1 (§ risk table: *"Stick to SQLModel core types"*).
- **Any change to `utcnow()`'s contract.** It is correct today; it stays correct.
- **The `Shift` cash-reconciliation money edge** (391), the **shift-close endpoint** (426), the **`Bill`↔`Visit` edge** (415), or **any money column**.

## Description

### The defect, as observed in LE31's own code on 2026-11-07

`backend/app/models.py`, the writer — **correct**:

```python
def utcnow() -> datetime:
    return datetime.now(timezone.utc)
```

`backend/app/models.py`, the columns — **the declaration is `DateTime(timezone=True)` on every one of them**:

| table | column | declaration |
|---|---|---|
| `batch` | `prepared_at` | `Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))` |
| `batch` | `expires_at` | `Field(default=None, sa_column=Column(DateTime(timezone=True)))` |
| `stock_entry` | `at` | `Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))` |
| `visit` | `opened_at` | `Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))` |
| `visit` | `closed_at` | `Field(default=None, sa_column=Column(DateTime(timezone=True)))` |
| `bill` | `paid_at` | `Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))` |
| `shift` | `opened_at` | `Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))` |
| `shift` | `closed_at` | `Field(default=None, sa_column=Column(DateTime(timezone=True)))` |

**`DateTime(timezone=True)` is a *Postgres* instruction.** SQLite has no `TIMESTAMPTZ` type; SQLAlchemy renders `DATETIME`, which is a **wall-clock string with no zone**. The `timezone=True` flag is silently dropped by the dialect.

**Executed — the round trip (the charter's dev database):**

```
  models.utcnow()                = datetime(2026,11,7,7,5,6,742981, tzinfo=timezone.utc)   # correct
  written raw                    = '2026-11-07 07:05:06.766506'   (sqlite typeof = text)
  read back (Python)             = datetime(2026,11,7,7,5,6,766506)   tzinfo = None         # NAIVE
```

**Executed — the two failure modes:**

```
  (a) COMPARISON (a crash, not a wrong number)
      b.prepared_at > utcnow()
        -> TypeError: can't compare offset-naive and offset-aware datetimes

  (b) A NON-UTC WRITE (a wrong number, silently)
      write prepared_at = datetime(2026,11,7,23,30, tzinfo=Europe/Paris)   # +01:00
        raw stored        = '2026-11-07 23:30:00.000000'
        true instant      = 2026-11-07T22:30:00+00:00
        error             = -3600 s   (and -7200 s in Paris summer time)
```

**Executed — feature 404's own expiry predicate, in the two languages it could be written in:**

```
  SQL form    (feature 404's predicate)  -> 2 rows      # correct
  Python form (the same predicate)        -> TypeError  # crashes
```

**Executed — feature 405's own specified guard:**

```
  read back prepared_at            -> tzinfo = None
  business_date_405(prepared_at)   -> ValueError: business_date() requires a
                                     timezone-aware instant; a naive datetime is ambiguous
```

**Executed — the business-day answer at midnight:**

```
  prepared_at = 2026-11-07T23:30:00+00:00        (Paris: 2026-11-08 00:30)
  'today's batches' by UTC date   (2026-11-07)  -> 3 rows
  'today's batches' by Paris date (2026-11-08)  -> 0 rows
```

### ⭐ Why this is a different defect from feature 405's

Feature 405 says, verbatim, about `Batch.prepared_at`:

> *"`prepared_at` is an **instant**. An instant alone cannot name a day, because a day is a **half-open interval in a named timezone**, and the instant does not say which interval it belongs to."*

and:

> *"**Both are instants, and both are correctly instants.**"*

**That last sentence is the contradiction this slice fixes.** On SQLite they are **not** instants when they come back out — they are naive wall-clocks. 405's premise ("both are correctly instants") is **true on Postgres and false on SQLite**, and 405's own helper (`raise` on naive input) is **un-callable on the database the charter names as the dev database**.

**This is the *contradiction* shape of the audit, and it is a covered concept with an uncovered instance.** Feature 405 owns *"a stored instant is not a day"*. Nobody owns *"a stored instant is not an instant"*.

### Why SQLite specifically

`PROJECT_CHARTER.md` §3.2 and the risk table make SQLite the dev database and Postgres the production one. The divergence is therefore **a dev/prod split**, and the split is in the **Python type**:

| | Postgres | SQLite (dev) |
|---|---|---|
| Column type | `TIMESTAMP WITH TIME ZONE` (`timestamptz`) | `DATETIME` (text) |
| Stored | an absolute instant | a wall-clock string |
| Read back (Python) | **aware** `datetime` | **naive** `datetime` |
| `value > now()` | works | **`TypeError`** |
| 405's `business_date()` | works | **raises** |

**The dev environment fails loudly; prod does not fail at all.** A defect that only reproduces in the environment with the least production traffic is a defect that survives.

## Data model

**No new table. No new column. No schema change.**

The change is to the **type** of the existing `datetime` columns and to the **values** they accept.

```
  BEFORE (today)
    batch.prepared_at        DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)
    batch.expires_at         DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)
    stock_entry.at           DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)
    visit.opened_at          DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)
    visit.closed_at          DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)
    bill.paid_at             DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)
    shift.opened_at          DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)
    shift.closed_at          DATETIME  (SQLite)  /  TIMESTAMPTZ (Postgres)

  AFTER (this slice)
    every column above holds a UTC INSTANT and returns an aware datetime
    the storage layer rejects a naive value on write
```

**The two shapes the implementer may choose (both are acceptable; the contract does not pick):**

1. **A SQLAlchemy `TypeDecorator`** over `DateTime` that (a) converts any aware input to UTC on `bind`, (b) **raises** on a naive input on `bind`, and (c) attaches `tzinfo=timezone.utc` on `result`. This keeps `DateTime` and stays inside SQLModel core types.
2. **A `UTCDateTime` alias plus a single normalisation helper** called at every read and write boundary.

**Either way, the contract is the same:**
- a naive value is **refused at the boundary**, not silently assumed to be UTC;
- a value read from the database is **tz-aware UTC**;
- `value > now()` **does not raise**.

**A `TypeDecorator` is the recommended shape** because it makes the guarantee hold at *every* call site, including call sites nobody has written yet. **The helper-only shape is acceptable** provided the read boundary is centralised and the write boundary rejects naive values.

## Implementation steps

1. **Write the failing test first.** A test that writes `Batch(prepared_at=utcnow())`, reads it back, and asserts `read.tzinfo is not None`. **On today's code it FAILS** (`tzinfo is None`). **A test that only ever passed proves nothing** — run it against the unfixed code and show the failure.
2. **Add the storage type.** A `TypeDecorator` (or the equivalent alias + helper) that converts aware input to UTC on bind, **raises on naive input on bind**, and attaches `tzinfo=timezone.utc` on result.
3. **Apply it to all eight `datetime` columns.** `batch.prepared_at`, `batch.expires_at`, `stock_entry.at`, `visit.opened_at`, `visit.closed_at`, `bill.paid_at`, `shift.opened_at`, `shift.closed_at`. **Grep the file; do not eyeball it** — a missed column is a silent hole.
4. **Add the one normalisation helper** (`to_utc_instant(value)`) and route the read boundary through it. **Do not** add a second copy of the conversion anywhere.
5. **Add the tests:**
   - a value written by `utcnow()` and read back is **tz-aware**;
   - a **Paris-local** aware value is stored as its **UTC instant** (`23:30+01:00` → `22:30Z`) — *this is the C3 case*;
   - a **naive** value is **refused** with an error naming the column;
   - a read-back value is **comparable** with `now()` without raising;
   - **feature 405's guard accepts a value read from the database** — *this is the X1 case, and it is the test that proves the collision is closed*;
   - feature 404's expiry predicate, **written in Python**, evaluates without raising.
6. **Correct the checklist line.** `coding-agent/checklist.md`'s *"Every timestamp is `TIMESTAMPTZ`."* is already known to be wrong for SQLite (feature 410, Open Question 4). **Qualify it** to name the real behaviour — and **coordinate with feature 405** so the two do not contradict.
7. **Add a note to the feature's own documentation** that the value stored is an instant and the value read is an instant, and that the business *day* is a separate question owned by 405.

## Telegram interaction if any

**None.** This slice touches no bot command, no handler and no message. The cook bot's `/start_today` flow writes `Batch.prepared_at` through the same storage type once the slice lands, and **that is the whole relationship**: the bot needs no change.

## Dependencies

- **Feature 405 (`le31-service-day-boundary`) — this slice must land FIRST, or in the same PR.** 405 specifies a `business_date()` helper that **raises on naive input**; on SQLite every value read back is naive, so **405's helper is un-callable until this slice lands**. **405's own claim that its columns "are correctly instants" is false on SQLite.** Name 405 in the PR description. **This is the upstream-of-filed-work condition**: 405 would otherwise implement a guard that fails closed on every real query.
- **Feature 404 (`le31-active-batch-rule`) — adjacent, not blocking.** 404 owns the *predicate*; this slice changes what the value it compares *is*. 404's SQL predicate keeps working unchanged (proved by execution). **Do not merge them** — a reviewer must be able to check each on its own.
- **Feature 411 (`le31-money-precision-declared-not-enforced`) — the pattern is already established.** 411 proved that *"money is `Decimal`, never `float`"* is a convention the storage layer does not enforce, and that **dev and prod disagree**. This slice is **the same shape applied to time**: *"Time is UTC"* is a convention the storage layer does not enforce, and **dev and prod disagree**. Read 411 before starting — it is the precedent, including the "declared, not enforced" vocabulary.
- **Feature 410 (`le31-two-money-rule-sources`) — its Open Question 4 is answered here.** 410 asks *"Is `TIMESTAMPTZ` a checklist error or a Postgres-only note?"* **The answer is: it is a Postgres-only note, and the SQLite behaviour is worse than a note — it is a type change.** Coordinate the checklist line.
- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — no dependency.** This slice adds **no column and no table**, so it does not need 446. **Recorded explicitly** because most slices that touch `models.py` do depend on 446, and this one does not.

## Open questions

1. **Should a naive value be refused or assumed UTC?** **Recorded default: REFUSED.** Assuming UTC is exactly the failure this slice exists to remove, because it is *silent*. A naive value almost always means "somebody built a datetime with `datetime.now()`", and the whole point is that the storage layer stops trusting that. **This is the implementer's call to record in the code**, per feature 405's own precedent of stating the choice.
2. **Should the columns stay `DateTime` under a `TypeDecorator`, or become a distinct alias?** **Not decided here.** Both shapes satisfy the contract. The `TypeDecorator` is recommended because it holds at every call site; the alias is simpler to read. **Whichever is chosen, the guarantee is the same and must be tested.**
3. **Should Postgres get an explicit `TIMESTAMPTZ`?** **Recorded default: no.** §3.2 and the risk table forbid Postgres-specific types in v1, and `DateTime(timezone=True)` already renders `timestamptz` on Postgres. **The Postgres side is already correct**; the defect is the SQLite side.
4. **Is there historical data to backfill?** **No.** The only `Visit` write in the whole backend is `backend/app/routers/tables.py` line 51; no `Batch`, `Bill`, `StockEntry` or `Shift` row has ever been written by shipped code. **Recorded so a later pass does not mistake this for an oversight** — and so that "there is nothing to migrate" is a *fact*, not a hope.
5. **Does the cook bot's `/start_today` write a Paris-local timestamp?** The bot uses `utcnow()` via `default_factory`, so no. **But if a future bot handler builds a datetime by hand, the storage layer is what stops it.** That is the point of the slice.

## Why this matters

**Because the charter's "Time is UTC" is not true today, and the failure is invisible in the number and loud in the type.**

The owner of a one-restaurant business will never see a wrong timestamp in a report that matters — but they will see the wrong **day** at midnight, and they will see the kitchen and the till disagree about when a tiramisu was made, in the hour when the restaurant is busiest. The bill is right; the day is wrong; and nothing reconciles them because nothing reads both.

**And there is a filed feature that depends on this one.** Feature 405 exists to answer *"what day is this?"*. Its answer is a helper that **refuses naive input**. Today, on the charter's dev database, **every value is naive**. So 405's central helper — a piece of work already specified, already gated as `build` — is **un-callable as written**. A coding agent implementing 405 today, faithfully, would write a helper that raises on every query it is given, and would either ship that or "fix" it by deleting the guard. **Both outcomes are worse than the defect 405 was filed to fix.**

**This is the cheapest slice in the corpus.** One type decorator, one helper, eight column declarations, five tests. **No schema change. No migration. No backfill. No data at risk** — because no data exists. It is **reversible in one step** (revert the type to `DateTime`).

**And it is the same shape as a defect the corpus already proved.** Feature 411 proved that *"money is `Decimal`, never `float`"* is declared and not enforced, and that **SQLite and Postgres disagree about it**. This is the identical finding for time: **"Time is UTC" is declared and not enforced, and SQLite and Postgres disagree about it — but with a `TypeError` instead of a wrong number.** The corpus knows this shape; it has simply never applied it to the timestamp columns.

## Adjacent evidence

**Third-party trigger, in-window, permissive licence — recorded as a vocabulary reference only.**

- **`AlgoVyn/bikri`** — MIT ✓ §3.2 strictly-compatible, **★1 / ⒂0 = NO traction evidence in either direction**, 13,320 KB, **TypeScript (off-stack for LE31's backend)**, created **2026-10-26** and pushed in-window = **in-window by BOTH fields**. Read at `/tmp/le31-brainstorm-2026-11-07/readmes/AlgoVyn_bikri.md` and `/tmp/le31-brainstorm-2026-11-07/readmes/AlgoVyn_bikri_docs_02-data-model.md.md`.
  - Its data model declares, verbatim: *"All D1 tables are **`STRICT`**."* and *"Every tenant-scoped D1 table starts with `tenant_id TEXT NOT NULL REFERENCES tenants(id)` … every reference to another tenant-scoped row is a **composite foreign key**."*
  - **The transferable idea is not its code — it is the *shape of its discipline*: a store that decides what a timestamp means and makes the database enforce it.** LE31's equivalent declaration (`DateTime(timezone=True)`) is the *same shape* of intent and **the same failure**, because the intent is not enforced by the SQLite dialect.
  - **Its `day_closes` table is the counter-example that makes the point:** it stores `expected_cash`, `counted_cash` and `difference` **with `CHECK (difference = counted_cash - expected_cash)` written into the DDL** — the *derived* value is checked by the database, not by convention. LE31's `Shift.variance` has no such check (feature 391 owns that gap; **this slice does not touch it**).
  - **No code from `bikri` is adopted.** It is TypeScript on Cloudflare D1; LE31 is Python + SQLModel + Postgres. **Vocabulary only.**
- **`DonnC/dura-pos`** — MIT ✓, ★0 / ⒂0 = **NO traction evidence**, 10,967 B README. Its glossary states, verbatim: *"**Event** | One recorded fact, such as `sale.completed`. It has a stable ID and is never edited. A correction is a new linked event."* — the same "a correction is an append, not an edit" discipline as LE31's ledger (feature 421). **Recorded, not picked.**

**Adjacent first-party work — recorded, NOT picked:**

| Feature | Why it is adjacent and NOT picked |
|---|---|
| **405** `le31-service-day-boundary` | **The primary dependent.** Owns the *day*; this slice owns whether the value is an instant. **405 depends on this slice.** |
| **404** `le31-active-batch-rule` | Owns the expiry *predicate*; its SQL form keeps working (proved by execution). **Not merged.** |
| **411** `le31-money-precision-declared-not-enforced` | **The precedent** — the identical "declared, not enforced, and dev/prod disagree" shape for money. **Read it first.** |
| **410** `le31-two-money-rule-sources` | Its Open Question 4 (*"Is `TIMESTAMPTZ` a checklist error or a Postgres-only note?"*) is answered by this slice. **Coordinate the checklist line.** |
| **374** `le31-qty-remaining-derived-not-stored` | The same "the schema stores a value the ledger derives" family, on stock. **Unrelated to time.** |
| **421** `le31-stockentry-append-only-linter-rule` | The ledger's write discipline. **Unrelated to time.** |
| **446** `le31-has-no-schema-evolution-mechanism` | **No dependency** — this slice adds no column and no table. Recorded so that is not mistaken for an oversight. |

**External source families fetched this pass (all raw, all re-derived from disk by the parent):**

- **GitHub Search** — 17 date-filtered queries + a 4-request qualifier probe, **21/21 HTTP 200**; aggregate `total_count` = **72,050**; **zero** 73-byte or 6-byte stubs; the **correct `pushed:>=` qualifier** was used and the **dead `pushed_at:>=` qualifier was proved dead by a paired probe** (`topic:restaurant` → 2,963; `pushed_at:>=2026-10-08` → **0**; `pushed:>=2026-10-08` → **583**; `created:>=` → 230). **The restaurant-shaped cluster is ALIVE.** Pipeline: **903 unique repos → 864 in-window → 285 created in-window (fresh) → 393 permissive**; **579 in-window repos were created BEFORE the window start** and are labelled as such.
- **HN Algolia** — 8 queries, 8/8 HTTP 200, **21 hits**, `title: null` = **0**. **4 of 8 queries genuinely returned `nbHits=0`** and are reported as counts, not failures. **0 HN items were promoted to a signal** — the "phone-first POS" query returned 12 hits, **none of them restaurant-related**.
- **OpenAlex** — 3 queries, 3/3 HTTP 200, `meta.count` = **4,076 / 5 / 0** — **distinct** (the filter was applied) and **none near corpus scale**; a diagnostic query for a nonsense term returned **0**, proving the filter is live. Abstracts were carried as **raw `abstract_inverted_index` dumps** in `openalex/_raw_abstracts_01..03.json`, **never paraphrased**. **0 papers were promoted to a signal** — the family is **soft this pass**.
- **ProductHunt** — HTTP 200, 44,100 B (soft source; **not used for a pick**).
- **ScienceDirect** — **NOT RETRIEVABLE** (blocked on this VPS; not attempted).

## Adjacent work — recorded, NOT picked

Three other findings from this pass's executed-lifecycle audit are **recorded here rather than picked**, because they are owned by filed features or because they are weaker than the three picks. **Each is named so a later pass does not re-file it.**

1. **A visit may close with order lines and NO bill** (the walk-out) — **this IS pick B, feature 454.** Named here only because the walk-out case is *adjacent* to the walk-out question feature 415 leaves undecided, and the two must not be confused.
2. **`Table.label` is not unique** — **this IS pick A, feature 453's sibling, feature 455.** Named here only for the same reason.
3. **`Table` has no status column, so a second seat opens a second visit** — **owned by feature 388** (filed, `build`). **Executed this pass and confirmed identical to 388's own reproduction** (two open visits on one table). **Not re-picked.**
4. **`Visit.closed_at` is NULL although a paid bill exists** — **owned by feature 415** (the bill-closes-visit edge). **Not re-picked.**
5. **An order line can be added to a closed, already-paid visit** — **owned by feature 436** (the active-visit write guard). **Executed this pass: `SUM(order_item) = 41.00` vs `bill.total_due = 16.00`.** **Not re-picked.**
6. **A bill records no which-lines-it-charged** — **owned by feature 435**. **Not re-picked.**
7. **Multiple open shifts at once, so "the current shift" has no referent** — **owned by feature 426** (it names the six-concurrent-open-shifts defect and the one-open-shift guard). **Executed this pass: 2 open shifts accepted.** **Not re-picked.**
8. **`StockEntry.ref_order_item_id` has no foreign key** — **owned by feature 426** (`le31-stockentry-ref-order-item-id-has-no-foreign-key`). **Executed this pass: a ledger row naming order line 99,999 was accepted.** **Not re-picked.**
9. **`StockEntry` may name a batch and an order line for different dishes** — **owned by feature 441**. **Executed this pass and confirmed identical.** **Not re-picked.**
10. **A ledger row may consume 99 units against an order line for 2** — **owned by feature 441** (the *magnitude* rule, which it defers to the FIFO answer). **Not re-picked.**
11. **`Batch.qty_remaining` disagrees with `SUM(qty_delta)`** — **owned by feature 374** (derive, don't store). **Executed this pass: stored 8 vs derived −92.** **Not re-picked.**
12. **`OrderItem.course` is free text** — **six distinct spellings coexist** (executed). **Out of scope by the charter's silence**, and **feature 430 records that decision explicitly**: *"the charter never mentions 'course' at all — sequencing is out of scope by the charter's silence, and is deliberately not picked."* **Not re-picked, and the charter's silence is respected.**
13. **A `Batch` may exist for a `MenuItem` whose `is_prepared` is False** — **owned by feature 398** (the non-prepared item path) and **feature 385** (*"a non-prepared item carries no batch"*). **Not re-picked.**
14. **`Shift.variance` and `counted_cash` are NULL for an open shift, and `WHERE variance != 0` silently excludes it** — **owned by feature 391** (the derivation) and **feature 426** (the close endpoint). **Executed this pass: the SQL form excludes the NULL row.** **Not re-picked.**
15. **`DerivedTip.amount` may be negative** — **owned by feature 420** (the refusal rule). **Executed this pass: −15.00 storable.** **Not re-picked.**
