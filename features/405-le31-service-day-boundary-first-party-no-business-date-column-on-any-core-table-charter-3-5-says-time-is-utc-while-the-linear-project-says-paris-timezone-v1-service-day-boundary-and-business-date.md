# Feature 405 — LE31 has no business day: a Friday-night order lands on Saturday's report

> **Pick A of Daily Research 2026-10-30 (92nd pass).** **FIRST-PARTY, and the defect is in LE31's own schema and LE31's own charter** — not inferred from a third-party repo.
>
> `backend/app/models.py`, `class Batch` docstring, verbatim:
>
> > *"A concrete prepared quantity of a MenuItem **for a specific day**."*
>
> The table has **no day column at all**. It has `prepared_at: datetime` — a **wall-clock UTC timestamp**.
>
> `grep -rn 'business_date\|service_date' backend/` returns **no hits**. There is **no business-date column on `Visit`, `OrderItem`, `Bill`, `StockEntry`, `Shift` or `Batch`**, and **no shared definition of what a service day is**.
>
> And LE31's own documents state the rule **three different ways**:
>
> | Source | Verbatim |
> |---|---|
> | `PROJECT_CHARTER.md` §7 Quality bar | *"**Time is UTC.** `datetime.now(timezone.utc)` everywhere."* |
> | Linear project `le31 v1 — Core MVP` summary | *"…EUR, **Paris timezone**."* |
> | `le31-conventions` hard invariants | *"Business time: persist timezone-aware instants and **render business dates in `Europe/Paris`**."* |
>
> **None of the three is implemented, and no document says which of them governs a *day*.** Feature 404 (filed 2026-10-29) already named this as *"a real and separate question"* and **explicitly did not answer it**.
>
> **The external instrument** was `zakariaelqannaa-dv/resto-management` (MIT, ★1, created 2026-10-26, pushed 2026-10-28 — in-window by both fields, all fields parent-verified via direct `GET /repos/`): every kitchen ticket there carries *"a **service date** and a **day-scoped code number**"* (`K-YYMMDD-NNN`), with sequences *"reserved atomically in `code_sequences` with `INSERT … ON CONFLICT … DO UPDATE … RETURNING`"* so *"two tickets can never share a code"*, and *"Moving a ticket to another service date re-issues its sequence automatically"*. **The day is part of the ticket's identity, not a function of a timestamp.**
>
> **Bucket: v1. Build verdict: `build`.** Evidence class: **OBSERVED** (schema and charter read directly on 2026-10-30; the charter contradiction is verbatim from two LE31 documents).

## Goal

Give LE31 a **business day** — one definition, one helper, one column where a surface needs it — so that *"today"* means the same thing to the waiter, the cook, the owner and the reports.

Two concrete outcomes:

1. **A Friday-night order belongs to Friday's service.** An order placed at `2026-10-30T23:30:00+00:00` (which is `2026-10-31T01:30:00+02:00` in Europe/Paris) must be **Friday's** sale if the venue is in Paris, not Saturday's.
2. **One function answers "which day is this?"** — never three documents, never a caller's own `datetime.now()` arithmetic.

**The single sentence this feature exists to make true:** *LE31 knows which service day an order belongs to.*

## Scope

**In scope (v1):**

- **One shared helper** that maps an instant to a business date, used by every consumer.
- **One nullable `business_date` column** on the tables that need to *record* which day a row belongs to, plus **the writer** for each.
- **A charter paragraph** that reconciles §7's *"Time is UTC"* with the project summary's *"Paris timezone"* — **store UTC, derive the day at the venue's timezone.** Both statements stay true; the charter says so.
- **A regression test** that pins the boundary and asserts the Friday-night case.
- **An explicit record of the two owner decisions** (see *Open questions*) — **recorded, not guessed.**

**Out of scope (v1):**

- **Any change to how instants are stored.** `prepared_at`, `opened_at`, `at`, `paid_at` stay **timezone-aware UTC instants**. **Nothing about this feature converts a stored timestamp to a local wall-clock time.** The charter's *"Time is UTC"* remains true of storage.
- **A timezone configuration system.** Europe/Paris is the default; whether it is configurable is **Open question 2**, and it is **not** decided here.
- **Multi-restaurant / multi-country support.** Feature 64 owns the localization-profile shape. **Do not merge with it.**
- **Any change to `Batch.expires_at`.** That is **feature 404** and is **adjacent, not identical**: 404 owns the *predicate* (`expires_at IS NULL OR expires_at > now()`), this feature owns the *day*. **They must not be merged** — a reviewer must be able to check each on its own.
- **`Batch.qty_remaining`.** That is **feature 374** (derive, don't store).
- **The ticket-code / day-scoped-sequence mechanism itself.** `K-YYMMDD-NNN` and the `code_sequences` table are **not adopted** — the artifact's code-shape is Electron/React/Express/PGlite, off-stack. **Only the vocabulary transfers**: the day is part of the row's identity.
- **Auto-marking `sold_out` at a service-day boundary.** A periodic job is a separate change with its own gate.
- **Alembic / migrations.** §3.2's stated v1 policy is `init_db()`.

## Description

### The defect, as observed in LE31's own code on 2026-10-30

**Shape (a) — a promise the schema cannot keep.**

```
models.py, class Batch docstring   "A concrete prepared quantity of a MenuItem for a specific day"
models.py, class Batch fields       id, menu_item_id, qty_start, qty_remaining,
                                    prepared_at (datetime, UTC), expires_at (datetime|None), …
                                    <-- no day column
```

`prepared_at` is an **instant**. An instant alone cannot name a day, because a day is a **half-open interval in a named timezone**, and the instant does not say which interval it belongs to.

**Shape (b) — the rule exists in three places and in none of them is it implemented.**

`PROJECT_CHARTER.md` says *"Time is UTC"*. The Linear project summary says *"Paris timezone"*. `le31-conventions` says *"render business dates in `Europe/Paris`"*. **`grep -rn 'business_date\|service_date' backend/` → no output.** No surface computes a day. No table stores one. **"Today" is not computable from LE31's data today** — it can only be guessed by a caller that independently applies a timezone, and *each caller will guess differently*.

**Shape (c) — the failure is a wrong number, not an error.**

Consider the owner-facing daily recap (feature 39, P1: *"Manager dashboard shows covers today, sales, tips, avg dwell, top items"*, `GET /api/reports/today`). Suppose the implementation asks *"which `Visit`s are today's?"*. Two callers, both reasonable:

```
caller A:  Visit.opened_at.date() == datetime.now(timezone.utc).date()
caller B:  Visit.opened_at.astimezone(ZoneInfo("Europe/Paris")).date() == datetime.now(ZoneInfo("Europe/Paris")).date()
```

These agree **except** in the few hours around midnight. The hours around midnight are **exactly when a restaurant is busiest** — the late service, the last orders of the night, the early shift. So the divergence is not random noise in a quiet hour; it is a **divergence concentrated in the hours that matter most**.

Concretely: an order at **Friday 23:30 UTC** is **Saturday 01:30 in Paris**. Caller A says Friday; caller B says Saturday. **One of them is wrong and the owner cannot tell which**, because the report shows a plausible number either way. There is no exception, no alert, no red row. **The owner's Friday sales figure is quietly short by the late service.**

**Shape (d) — the day is also needed for identity, not only for reporting.**

The external artifact makes the day **part of the ticket's key**: `K-261026-007`. LE31's `Bill` is keyed on `visit_id` (unique) and `StockEntry` on `id` — both **globally unique and day-agnostic**, which is fine. But the *day-scoped sequence* pattern answers a question LE31 has not asked: **"how many covers did we serve on Tuesday?"** — which is not the same question as *"how many `Visit`s have `opened_at` in a 24-hour window I computed myself?"*.

**Shape (e) — the charter contradicts itself, and both halves are right.**

*"Time is UTC"* is a **storage** rule and it is correct — UTC instants are unambiguous and DST-free. *"Paris timezone"* is a **rendering** rule and it is also correct — a business day is a local-calendar concept. **The charter never says these are two different things**, so a reader can reasonably implement either and be "following the charter". Feature 404 noticed this and called it *"itself worth reconciling"*.

### Why the failure is silent, and why that is the whole point

A missing column does not raise. A wrong day does not raise. The report is computed, the number is plausible, and **nothing in LE31 can tell the owner that Friday's late service was excluded**. There is **no ground truth to audit against**, because there is no query that reports *"visits whose business day differs between two plausible derivations"*.

**Today this is almost entirely inert** — there is no daily-report endpoint, no bill router, and `backend/app/routers/` contains **only `tables.py`**. That is exactly the shape the 85th–91st passes found repeatedly: **cheap now, expensive after**, because the first daily-report implementation will have to make this choice, and the plausible wrong answer is the quiet one:

> *"Just use `datetime.now(timezone.utc).date()` — the charter says time is UTC."*

That is **true today** (there is no report) and **silently false** the moment there is one, **concentrated in the hours when a restaurant is busiest**.

## Data model

**One nullable column, on the tables that record a day, plus one helper.**

```python
# NEW FILE: backend/app/services/business_time.py
from datetime import date, datetime
from zoneinfo import ZoneInfo

#: The venue's timezone. Open question 2 asks whether this is configurable;
#: until the owner answers, Europe/Paris is the recorded default because it is
#: what le31-conventions and the Linear project summary both state.
VENUE_TZ = ZoneInfo("Europe/Paris")


def business_date(instant: datetime, tz: ZoneInfo = VENUE_TZ) -> date:
    """The service day `instant` belongs to, in the venue's timezone.

    `instant` MUST be timezone-aware. A naive datetime is rejected rather than
    silently assumed to be UTC: a naive call site is exactly the bug this
    feature exists to prevent.
    """
    if instant.tzinfo is None:
        raise ValueError("business_date() requires a timezone-aware instant")
    return instant.astimezone(tz).date()
```

```python
# backend/app/models.py — added to the tables that must RECORD a day.
# Each is nullable so the migration is additive and the column can be backfilled.

class Visit(SQLModel, table=True):
    …
    business_date: date | None = None   # ADDED: the service day this visit belongs to

class Bill(SQLModel, table=True):
    …
    business_date: date | None = None   # ADDED

class Shift(SQLModel, table=True):
    …
    business_date: date | None = None   # ADDED
```

**On `StockEntry` and `Batch`:** **no column is added here.** `StockEntry.at` is an audit timestamp — when the ledger event happened — and `Batch.prepared_at` is when the cook made it. **Both are instants, and both are correctly instants.** Feature 404 owns the *service-day* question for `Batch`; adding a column here would **pre-empt that feature's decision** (its Open question 2 is *"what is a service day?"* — the very question this feature answers). **Recorded, not decided here.**

**The `date` type, not `datetime`.** A business day is a **calendar date**, not an instant. Storing it as `datetime` would reintroduce the ambiguity this feature removes.

**The writer.** `business_date` is set **at write time** by the same code path that creates the row, using `business_date(utcnow())`:

```python
visit = Visit(
    table_id=table_id,
    server_id=server_id,
    party_size=party_size,
    adults=adults,
    children=children,
    business_date=business_date(utcnow()),   # ADDED: derived once, at write
)
```

**Derived once, stored once.** Storing it avoids every reader having to agree on the derivation — which is the whole point. **It is NOT derived-never-store** (that is feature 374's rule, for *stock quantities*): a business date is a **fact about when the row happened**, not a quantity that can drift.

**On the column being nullable:** nullable means a row written before this feature, or by a path that forgot to set it, reads as `NULL` — which is **distinguishable from a real day**, and the reader must decide what `NULL` means. **The decision is recorded in the feature: `NULL` means "the business day was not recorded"**, and readers **must not** silently re-derive it, because re-deriving reintroduces the split-brain. A backfill is a separate, explicitly-scoped step.

## Implementation steps

1. **Write the charter paragraph.** One short block in `PROJECT_CHARTER.md` stating: *storage is timezone-aware UTC (unchanged); the service day is derived in the venue's timezone; `Europe/Paris` is the default until the owner says otherwise.* **A charter that still states only *"Time is UTC"* is the defect, still present.**
2. **Create `backend/app/services/business_time.py`** with `VENUE_TZ` and `business_date(instant, tz=VENUE_TZ)`. **`backend/app/services/` does not exist today** — create it with `__init__.py`. The point of the module is that **the definition has exactly one home** and every caller imports it.
3. **Add the columns** to `Visit`, `Bill` and `Shift` exactly as written in *Data model*. **`date` columns; nullable; indexed** on `Visit` and `Bill` (the two surfaces a daily report will filter on).
4. **Set the writers.** Wherever a `Visit`, a `Bill` or a `Shift` is created, set `business_date=business_date(utcnow())` in the same statement. `grep -rn 'Visit(\|Bill(\|Shift(' backend/` must show **every** construction site setting it.
5. **Guard the naive-datetime case.** `business_date()` raises on a naive input. **Add a test that passes a naive datetime and asserts the raise** — the guard is worthless if it is untested.
6. **Add the regression test.** Three cases, all on the same helper:
   - `2026-10-30T23:30:00+00:00` → business date **`2026-10-30`** (Friday) — *the late-service case; this is the test that exists to keep the feature alive.*
   - `2026-10-31T00:30:00+00:00` → business date **`2026-10-31`** (Saturday).
   - `2026-10-30T12:00:00+00:00` → business date **`2026-10-30`** — *the quiet midday case, to prove the helper is not simply truncating UTC.*
   The first two must be **asserted against a literal**, not against a re-implementation of the same expression.
7. **Add the `NULL` rule to the contract.** State in the feature docs that `business_date IS NULL` means *"not recorded"* and that readers **must not** silently substitute `business_date(opened_at)`. **Write it where a reader will find it.**
8. **Do not backfill in this PR.** A backfill is a separate, explicitly-scoped step with its own gate (it touches historical rows, and historical rows are exactly where the derivation is ambiguous). **Record it as follow-up.**

## Telegram interaction if any

**None.** This feature does not add a command, does not change a command, and does not change what the cook sees.

**What changes observably**: nothing today — there is no report, no bill router, and no daily recap to move. **That is not nil once the daily recap lands**, which is why this must be fixed **before** it, not after.

**One consequence to state explicitly, because it is a behaviour change and not only a code change**: after this feature, a shift that opens at 00:30 Paris time belongs to **Saturday's** business date, not Friday's. **The owner should know that**, because *"what day is it?"* is a question an owner will ask.

## Dependencies

- **No new package.** `zoneinfo` is **stdlib** (Python 3.9+); LE31 is Python 3.13. **Do not** add `pytz` or `dateutil`.
- **No stack change.** This is not a §3.2 stack decision.
- **Must not be merged with feature 404** (`Batch` active-batch predicate). Adjacent and different: 404 is a **filter that excludes rows**; this is a **day that does not exist**. If both land in one PR, each must be stated separately so a reviewer can check it on its own.
- **Not** feature 374 (`Batch.qty_remaining` derive-never-store) — a different rule about a different kind of value.
- **Related, not blocking:** feature 34 (stock board — the "today's batches" question), feature 39 (owner daily recap — the first consumer that will need this), feature 12 (pre-shift briefing), feature 43 / 44 (both already carry a `service_date` on **their own** new tables — `PrepTask` and `DayCard` — **which is precedent, not duplication**: they name a day for a task, not for a visit).
- **Related, not blocking:** feature 64 (localization profile — **v2**; do not merge).

## Open questions

1. **Does the service day start at local midnight, or at the venue's opening time?** A venue that opens at 11:00 may consider a 00:30 table to belong to **last night's** service. **Midnight is the recorded default in this feature** (and is the simpler rule); **the owner decides whether a later boundary is wanted.** This is a genuine owner decision, **not a research finding**, and it is **not** guessed here.
2. **Is the venue's timezone Europe/Paris, or configurable?** `le31-conventions` and the Linear project summary both say Paris. **A configurable setting is not built here** — the helper already takes a `tz` parameter, so adding configuration later is **one line**, and the parameter exists **precisely so this decision can be deferred without a schema change**.
3. **Who writes `business_date` for a row whose "natural" day differs from its creation day?** A `Visit` opened at 23:30 belongs to Friday, but a `Shift` opened at 23:30 might be *Saturday's* shift depending on the venue's convention. **Each writer uses the same helper**, so the only open part is whether a writer should pass a **different instant** than `utcnow()`.
4. **What happens to historical rows?** `business_date` is `NULL` for everything written before this feature. **Options: leave `NULL`, or backfill.** **This feature leaves them `NULL`** and records the rule; **a backfill is a separate, separately-gated step.**
5. **Is `Europe/Paris` right for a venue outside France?** §3.2 fixes EUR and the project summary says Paris, so **yes for now**. Feature 64 owns any change.

## Why this matters

**Because this is LE31's own rule failing against LE31's own schema, and the failure lands on a P0 acceptance criterion.** The charter's P0 list includes *"Waiter can browse **today's** menu"* and the P1 list includes *"Manager dashboard shows covers **today**, sales, tips"*. **"Today" is the operative word in both, and LE31 cannot currently compute it.**

**The asymmetry that argues for `build` over `defer`.** There is no report endpoint today, so the defect is **completely inert** — it cannot hurt anyone. The moment the daily recap lands, it becomes **live**, and the wrong answer is the quiet one: *"use UTC, the charter says UTC."* **Cheap now, expensive after** — one helper and one column today, versus a silent wrong daily-revenue figure on every Friday night after.

**And this is the third time in four passes that an *external artifact* has produced a first-party finding by making the parent read LE31's own code** — the pattern the 85th–91st passes established and this pass continues:
- 87th (`xpos`) → `OrderItem` missing its batch edge
- 88th (`ironwaves`) → the money domain's missing shapes
- 89th (`partner-kit`, `medusa-pos`) → a state with no representation, a rule with no consumer
- **91st (`resto-management`) → the active-batch predicate excludes rows it should include (feature 404)**
- **92nd (`resto-management` again, a different corner of the same artifact) → LE31 has no day at all**

**The artifact did not tell LE31 anything about timezones.** It told LE31 that **a day is part of a ticket's identity, not a function of a timestamp**. That was enough to make the parent read `Batch`, then `Visit`, then `Bill`, then `Shift`, then the charter — and to find that **four tables carry a timestamp and none of them carries a day**. **Ninety citations had not found the first defect; four greps and one `sed` did.**

**Why this artifact mattered, precisely.** `resto-management` gets the day right in two ways at once: it **stores** `business_date` on the ticket, **and** it keys its sequence on it (`code_sequences (scope, business_date) → last_seq`) so two tickets can never share a code. **Storing the day and keying the day on it are the same discipline.** LE31 needs only the first half — and, notably, **it needs it on the tables that report rather than the tables that key**, because LE31's keys are already globally unique.

**The counter-argument, stated honestly.** LE31's owner has never complained about a wrong day. The gap is **OBSERVED**; the *pain* is **INFERRED**. This feature is therefore **defensive rather than reactive** — and it is filed as `build` anyway because the fix is one helper, the cost is one column, and the alternative is a decision made by accident inside a future report implementation, at the busiest hour of the night, with no way to detect that it was wrong.
