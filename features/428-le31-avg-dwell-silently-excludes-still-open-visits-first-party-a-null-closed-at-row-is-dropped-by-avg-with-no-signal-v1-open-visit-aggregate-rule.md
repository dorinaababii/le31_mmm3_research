# Feature 428 — "avg dwell" silently excludes still-open visits: a `NULL closed_at` row is dropped by `AVG` with no signal

> **Pick C of Daily Brainstorm 2026-11-02 (95th pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proven by EXECUTION, not by reading.**
>
> `backend/app/models.py`, `class Visit` (line 129):
>
> ```
> 131:    table_id: int = Field(foreign_key="table_.id")
> 132:    server_id: int = Field(foreign_key="app_user.id")
> 133:    opened_at: datetime = Field(default_factory=utcnow, ...)
> 134:    closed_at: datetime | None = Field(default=None, ...)     ← NULLABLE
> ```
>
> The charter's P1 row (`PROJECT_CHARTER.md` §2):
>
> ```
> | **P1** | Manager dashboard shows covers today, sales, tips, avg dwell, top items.
> |         | `/api/reports/today` returns KPIs + top-items list. |
> ```
>
> **The parent proved the consequence against a real SQLite database built from LE31's own `models.py`** (`_exec_proof2_2026_11_02.py`):
>
> ```
> seeded 4 visits: 3 closed (dwell=60min), 1 STILL OPEN (elapsed=10min)
>
> NAIVE  AVG over ALL visit rows        -> 59.99999977648258 minutes
>        The still-open visit is SILENTLY DROPPED (closed_at IS NULL -> the
>        subtraction is NULL -> AVG ignores it). No error. No warning.
>
> EXPLICIT AVG WHERE closed_at IS NOT NULL -> 59.99999977648258 minutes
>        Same number. The defect is that the two AGREE: the naive query gives no
>        signal that it dropped a row.
>
> ROW COUNTS: COUNT(closed_at)=3  COUNT(*)=4  -> 1 row(s) invisible to the KPI
> ```
>
> Bucket: **v1 (visit-analytics aggregation semantics — the sixth first-party defect of the brainstorm series)** — Pick C of Daily Brainstorm 2026-11-02. Build verdict: **`build`** (first-party fix: one written rule for the open-visit population + one helper + one regression test).

## Goal

Make LE31's manager dashboard say **what its numbers are about** — so that
`avg dwell` and `covers today` cannot silently change their population
depending on which visits happen to be closed.

**The single sentence this feature exists to make true:** *a KPI that excludes
rows must say so.*

Two concrete outcomes:

1. **The open-visit population is defined, once, and written down.** "Average
   dwell" is computed over **closed** visits; "currently seated" is a
   **separate, visible** number. Neither is a silent consequence of a `NULL`.
2. **The Python form and the SQL form agree, and are tested against each
   other.** LE31's derivations are written in SQL (`AVG`, `COUNT`) but the
   *rule* has to be expressible in Python too — and the two disagree today, in
   the worst direction: **Python raises on `None > x`; SQL silently excludes
   the row.**

## Scope

**In scope (v1):**
- One written rule (in the charter's §4 area or in a service module's
  docstring) stating: **`avg dwell` is computed over visits with
  `closed_at IS NOT NULL`**; visits that are still open are reported
  separately as *"currently seated"*, with their elapsed occupancy.
- One service helper that computes the manager-dashboard KPI set from a
  `Visit` query, with the population rule applied **in one place** rather than
  repeated in each query.
- One regression test that asserts the **population**, not just the value:
  *"the number of visits contributing to `avg dwell` plus the number reported
  as currently-seated equals the total number of visits."*
- A paired Python/SQL test: the same population rule expressed in Python
  (`[v for v in visits if v.closed_at is not None]`) and in SQL
  (`WHERE closed_at IS NOT NULL`) must select the **same rows**.
- One row in `INDEX.md`'s "Active feature pipeline" table.

## Out of scope

- **Writing `Visit.closed_at`.** That is **feature 415**
  (`le31-bill-closes-visit-edge`) — *"Nothing ties a paid bill to a closed
  visit"*. **⏱️ ORDERING: feature 415 lands first, or in the same PR.** Before
  it lands, `closed_at` is **never written**, so *every* visit is open and the
  KPI has nothing to average. This feature fixes the **population rule**; 415
  supplies the **data**. **Not bundled** — different edges, different failure modes.
- **Deciding the dwell *endpoint*.** Whether dwell is `closed_at − opened_at` or
  `paid_at − opened_at` is **feature 415's open question**, recorded verbatim
  there: *"Should `closed_at` be set to the payment instant or to the moment
  the waiter taps 'close'? … **Not decided.**"* This feature does **not**
  decide it and does **not** change `Visit.closed_at`'s semantics.
- **Any change to `Visit`, `OrderItem`, `Bill`, `Shift` or `DerivedTip`.**
- **Any change to `backend/app/models.py`.** No column changes. This is a
  *rule* and a *helper*, not a schema change.
- **Building the manager dashboard.** This feature defines the KPI population
  and supplies the helper. The dashboard UI is separate work.
- **`/api/reports/today`.** The route does not exist. This feature supplies the
  helper the route will call; it does not create the route.
- **The service-charge / tip / tax KPI semantics.** Those are features 408
  (tax rate), 411 (precision) and 420 (tendered vs received).
- **Alembic.** §3.2's stated v1 policy is `init_db()`.

## Description

### The defect, as observed by execution on 2026-11-02

Parent-verified against a real SQLite database built from LE31's own `models.py`
(`SQLModel.metadata.create_all(engine)` against a throwaway file). Re-runnable:
`_exec_proof2_2026_11_02.py`.

| Probe | Result |
|---|---|
| Seed | 3 closed visits at 60 min dwell, 1 still-open visit 10 min elapsed |
| `AVG((closed_at − opened_at))` over **all** visit rows | `59.99999977648258` minutes |
| `AVG(...) WHERE closed_at IS NOT NULL` | `59.99999977648258` minutes — **the same number** |
| `COUNT(closed_at)` vs `COUNT(*)` | `3` vs `4` — **one row invisible to the KPI** |
| `MIN(elapsed) WHERE closed_at IS NULL` (currently-seated occupancy) | `10.000167042016983` minutes — **never appears in avg dwell** |
| `COUNT(*)` vs `COUNT(*) WHERE closed_at IS NOT NULL` (the sibling "covers today" KPI) | `4` vs `3` |

### Why this is not cosmetic, and not the same defect as feature 415

**Feature 415 owns the missing WRITER.** Its own text states it, verbatim:

> *"**Consequence 2 — dwell time is never computed.** Feature 06's P1 manager dashboard must show *'avg dwell'*. Dwell is `closed_at − opened_at`. With `closed_at` never written, **every visit has infinite dwell**, and the P1 dashboard has no dwell figure to show."*

That is a **different edge**. 415 says *"the value is never written"*. This
feature says *"when the value IS written, the aggregate silently changes its
population"*.

The two are visible **only together**, and the proof above is the demonstration:
with the writer fixed, the naive query and the explicit query **return the same
number**. The naive one dropped a row and said nothing.

**This is the SQL three-valued-logic trap, in LE31's own numbers.** The rule
*"`avg dwell` is the average over closed visits"* is what the analyst intends.
The SQL that expresses it accidentally is `AVG(...)` with no `WHERE`. The two
differ:

| Form | `closed_at IS NULL` row | Result |
|---|---|---|
| Python: `None > x` | **raises** `TypeError` | loud |
| SQL: `AVG(a − b)` where `b IS NULL` | **excluded silently** | quiet |

**The two forms do not just differ in loudness — they differ in result.** A
developer testing the rule in Python gets an error and adds a `WHERE`; a
developer writing only SQL gets a number that is *wrong by exactly the open
visits*, and never finds out.

### The defect generalises to the sibling KPI

`covers today` — the KPI next to `avg dwell` in the same charter row — has the
**same** population hazard, and it is the more dangerous one:

- *"covers today"* means **covers seated today**. The natural implementation
  filters on `closed_at IS NOT NULL` (a visit that closed today) — which
  **excludes the busiest hours**, when every table is full and nobody has left
  yet.
- So the dashboard would show **fewer covers at 21:00 than at 20:00**, on the
  same evening. A number that goes *down* while the restaurant gets *busier*
  is the kind of thing an owner stops trusting permanently.

**The population rule must be written once and applied to both.**

### Why the corpus did not catch this

The concept sweep over all 456 feature contracts found **zero** uncovered
concepts — the audit is **saturating**, and this defect was found only by
auditing the charter's P1 row against the schema **one row at a time** rather
than by grepping for words.

That is worth recording: `dwell` appears in **2** contracts (feature 06 and
feature 415), and feature 06 — the contract that *owns the KPI* — is a **brief**,
not a defect contract. It has `## Goal`, `## Scope`, `## Description`,
`## Data model`, `## Manager dashboard (web /reports)`, `## Privacy stance`,
`## Dependencies`, `## Open questions`, `## Why skip gender in v1` — and
**neither `## Out of scope` nor `## Why this matters`**. It states the goal
(*"Capture `opened_at` and `closed_at` → dwell time"*) and moves on. **Nobody
had asked what the aggregate is over.**

### The external instrument: an in-window third-party vocabulary

`FreeOpenSourcePOS/FloCafe` (MIT ✓ §3.2; TypeScript/Electron **off-stack**;
★166, created 2026-05-07, pushed 2026-11-02 = in-window by push only; 21,666 B
README read in full). Its README records, verbatim:

> *"**Daily sales & accounting export:** Audit-ready CSV/Excel reporting with **financial reconciliation identities**."*

and, about its own local-first data, verbatim:

> *"**Automated database backups:** **Pre-migration automatic snapshots**, manual exports, and optional Google Drive sync."*

**The transferable item is the vocabulary of a report that states its own
identity** — *"reconciliation identities"* is the shape of a report whose
numbers can be checked against each other, and *"pre-migration automatic
snapshots"* is the shape of a system that keeps a verifiable history rather
than a mutable present. LE31's `avg dwell` currently has **no identity**: it
does not say which visits it covers, so it cannot be reconciled against
anything.

**⚠️ This repo is already feature 353** (`353-FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary`) and was **cited again as an adjacent instrument** in the 2026-11-01 pass. **It is recorded here as adjacent evidence only — it is NOT re-picked.** The vocabulary is the transfer; no code is adopted (MIT ✓ allows adoption, but TypeScript/Electron is **off-stack** for LE31's Python 3.13 / FastAPI / SQLModel stack).

## Data model

**No schema change.** The nullable `closed_at` is **correct** — a visit in
progress genuinely has no end time. The defect is that the *rule* about the
resulting population was never written.

```python
# backend/app/models.py — class Visit (line 129), unchanged by this feature

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

### The rule, as it should be written

> **Rule — the manager dashboard's visit population.**
>
> 1. **`avg dwell`** is `AVG(closed_at − opened_at)` over visits with
>    `closed_at IS NOT NULL`. Visits still open are **excluded by definition**,
>    not by accident.
> 2. **`covers today`** counts visits whose `opened_at` falls on the service
>    day — **regardless of `closed_at`**. A visit that is still open is still a
>    cover.
> 3. **`currently seated`** counts visits with `closed_at IS NULL`, and
>    reports their elapsed occupancy (`now − opened_at`). This is the number
>    that replaces the silent exclusion.
> 4. **The population is stated in the response.** The KPI payload carries the
>    counts it was computed over, so a reader can check
>    `dwell_population + currently_seated == total_visits`.
>
> Rules 1 and 2 are different populations and **must not share a filter**.
> Rule 1 excludes open visits; rule 2 includes them.

### The helper's shape

```python
# backend/app/services/visit_analytics.py — new module (the directory does not exist yet)

def dwell_summary(visits: list[Visit], now: datetime) -> dict:
    """The manager dashboard's visit KPI population.

    RULE: `avg_dwell` is computed over CLOSED visits only. Visits still open
    are excluded BY DEFINITION (not by accident) and reported separately as
    `currently_seated`, with their elapsed occupancy.

    The counts are returned alongside the values so the population is visible
    in the response rather than implied by it.
    """
    closed = [v for v in visits if v.closed_at is not None]
    open_ = [v for v in visits if v.closed_at is None]

    durations = [(v.closed_at - v.opened_at).total_seconds() / 60.0 for v in closed]
    elapsed = [(now - v.opened_at).total_seconds() / 60.0 for v in open_]

    return {
        "avg_dwell_minutes": (sum(durations) / len(durations)) if durations else None,
        "dwell_population": len(closed),          # ← the count, so it can be checked
        "covers_today": len(visits),               # ← RULE 2: open visits INCLUDED
        "currently_seated": len(open_),
        "current_occupancy_minutes": (sum(elapsed) / len(elapsed)) if elapsed else None,
        "total_visits": len(visits),
    }
```

**Note the two different filters.** `avg_dwell` uses `closed`; `covers_today`
uses `visits`. **That asymmetry is the whole point of the rule**, and it is
exactly what a single shared `WHERE` clause would have destroyed.

## Implementation steps

1. **Write the rule down.** Add the "Rule — the manager dashboard's visit
   population" block above to the charter's §4 area (next to §4.3) **or** to
   the helper's docstring if the charter is not to be edited. **The rule must
   exist in text before the code, so that the next field added to `Visit`
   inherits it.**
2. **Create `backend/app/services/__init__.py` and
   `backend/app/services/visit_analytics.py`** with `dwell_summary` as shown.
   **Note:** `backend/app/services/` **does not exist yet** (verified 2026-11-02)
   — the charter's §4.4 folder layout lists it, so creating it is expected.
3. **Write the SQL equivalent** in the same module, so the two forms sit side
   by side and are testable against each other:
   ```python
   SQL_AVG_DWELL = text(
       "SELECT AVG((julianday(closed_at) - julianday(opened_at)) * 24 * 60) "
       "FROM visit WHERE closed_at IS NOT NULL"
   )
   ```
   **The `WHERE closed_at IS NOT NULL` is the entire point.** The naive form
   (no `WHERE`) returns the same number — the defect this feature exists to
   make impossible.
4. **Add the regression tests:**
   - `test_avg_dwell_population_excludes_open_visits` — seed 3 closed + 1 open;
     assert `dwell_population == 3` and `currently_seated == 1` and
     `total_visits == 4`.
   - `test_covers_today_includes_open_visits` — assert `covers_today == 4`
     (not 3). **This is the sibling-KPI test**, and it is the one that fails
     first if someone shares one filter between the two.
   - `test_python_and_sql_populations_agree` — the same seed, through
     `dwell_summary` and through `SQL_AVG_DWELL`; assert they select the same
     rows and produce the same number.
   - `test_population_counts_reconcile` — assert
     `dwell_population + currently_seated == total_visits`.
5. **Record the dependency on feature 415 in this contract** (done in
   *Dependencies*) and in the PR description, so the ordering is visible from
   both ends.
6. **Add one row** to `INDEX.md`'s "Active feature pipeline" table.
7. **Run the LE31 test suite** and confirm no regressions.

## Telegram interaction if any

**None.** The manager dashboard is a web surface (`/reports`), not a Telegram
surface, and no Telegram command reads dwell time. The cook's `/forecast`
(feature 07) and the EOD summary are **different populations** and are not
touched.

## Dependencies

- **⭐ Feature 415 (`le31-bill-closes-visit-edge`)** — **MUST LAND FIRST, OR IN THE SAME PR.** It owns the missing **writer** (`closed_at` is never written). Before it lands, `closed_at IS NULL` for *every* visit, so `dwell_population` is 0 and `avg dwell` has no value to be wrong about. **Name it in the PR description.** This is the "upstream-of-filed-work" rule in its clearest form: **a filed feature (415) would otherwise implement the aggregation half without the population half.**
- **Feature 06 (`le31-guest-demographics`)** — owns the KPI *goal* as a brief. It is **not** a defect contract (it has neither `## Out of scope` nor `## Why this matters`), and it states *"Capture `opened_at` and `closed_at` → dwell time"* without saying what the average is over. **This feature supplies the missing population rule; feature 06 is not modified.** A one-line amendment to feature 06 pointing at 428 is acceptable and is recorded in *Open questions*.
- **Feature 405 (`le31-service-day-boundary`)** — defines the *service day*. It is **adjacent and important**: rule 2 (*"covers today" counts visits whose `opened_at` falls on the service day*) **depends on a service-day definition**. **Not a dependency** — this feature defines the rule in terms of whatever service day is in force and does not decide it — but the implementation must not silently assume UTC midnight. **Read feature 405 before implementing rule 2.**
- **Feature 388 (`le31-table-state-machine`)** — reads `closed_at == None` to derive the table's status. **Adjacent.** The same `NULL` is the signal for "still occupied"; this feature must not change that meaning.
- **Feature 414 (`le31-table-capacity`)** and **feature 423 (`le31-party-composition`)** — both in the visit/party domain. **Adjacent, not blocking.**
- **Feature 408 / 411 / 420** — the money KPIs on the same dashboard (sales, tips). **Adjacent.** The population rule applies to *visits*; the money KPIs have their own semantics and their own filed defects.

## Open questions

1. **Should the KPI payload carry the population counts, or should the dashboard render them separately?** **Recorded default: carry them in the payload.** The point of the feature is that the population is *visible without asking*; a separate rendering step can be forgotten, a payload field cannot. **Not a decision for this feature to block on** — the helper returns them; the route decides how to present them.
2. **Should `avg dwell` be `AVG` or a median?** The charter says *"avg dwell"*. **Recorded default: `AVG`, as the charter names it.** A median is arguably a better dwell statistic (a long party skews the mean), but that is a **product decision about the KPI's definition**, not a defect fix, and it is **not** decided here.
3. **Should a visit still open after N hours be flagged as abandoned?** **Recorded default: no.** That is a product rule with an operational consequence (a table appears occupied forever). **Not decided here.** Recorded so the next pass does not mistake it for an oversight.
4. **Should `covers_today` use `opened_at` or `closed_at` for the service-day boundary?** **Recorded default: `opened_at`** (a cover is seated, not closed). Feature 405's service-day definition is the authority on the *day* boundary itself. **Not decided here** — stated as rule 2 above, with the day boundary delegated to 405.
5. **Should feature 06 be amended to point at this feature?** **Recorded default: yes — a one-line amendment**, exactly as feature 404's deferral note about `ref_order_item_id` is amended by feature 426. **An amendment, not a rewrite.**

## Sources

- **LE31's own code** — `backend/app/models.py`, `class Visit` (line 129), read on 2026-11-02.
- **LE31's own charter** — `PROJECT_CHARTER.md` §2 (the P1 manager-dashboard row), §4.4 (the folder layout, which lists `backend/app/services/`), §3.2 (the Alembic non-goal).
- **Execution proof** — `_exec_proof2_2026_11_02.py`, run 2026-11-02 against a throwaway SQLite database built from LE31's own `models.py` with `SQLModel.metadata.create_all`. Probe: the naive `AVG` and the explicit `WHERE closed_at IS NOT NULL` `AVG` returned **the same** value `59.99999977648258`; `COUNT(closed_at)=3` vs `COUNT(*)=4`; `MIN(elapsed) WHERE closed_at IS NULL = 10.000167042016983` minutes.
- **Third-party instrument (vocabulary only, ALREADY FEATURE 353)** — `FreeOpenSourcePOS/FloCafe`, GitHub API `/repos/` GET on 2026-11-02, HTTP 200: ★166, MIT, TypeScript/Electron **off-stack**, created 2026-05-07, pushed 2026-11-02 = **in-window by push only** (created 5 months before the 2026-10-03 window start — **not a fresh discovery**), 21,666 B README read in full. **Recorded as adjacent evidence; NOT re-picked** — it is already feature 353 and was cited again on 2026-11-01.
- **Corpus evidence** — features 06, 388, 405, 414, 415, 423 read in full on 2026-11-02. `grep -rilE 'dwell' features/*.md` → feature 06 and feature 415 (plus 405, 422, 423, 425 by proximity). Feature 06 has **no** `## Out of scope` and **no** `## Why this matters` — confirmed by parsing its headings.

## Why this matters

**Because a number the owner cannot reconcile is a number the owner stops
believing — and this one fails silently, in the direction that looks like good
news.**

The proven behaviour is the sharpest version of this: **the naive query and
the careful query return the identical value.** There is no discrepancy to
notice, no log line, no exception. The dashboard says "average dwell 60
minutes" while a guest has been sitting at table 4 for ten minutes, and the
number is not merely incomplete — it is **identical to what the careful query
would have said**. The defect is that it is **wrong about the world and
invisible about itself.**

And the sibling KPI makes it worse. `covers today` implemented as "closed
today" would report **fewer covers at 21:00 than at 20:00** on the same
evening — a number that falls while the restaurant gets busier. The owner
would not debug that; they would stop reading the dashboard.

**The rule is cheap; the cost of skipping it is permanent.** One written rule
and one helper. But LE31's whole product claim is *"the owner sees a truthful
stock ledger"* — the same claim extends to every number the manager sees. A
dashboard that reports a number over an *unstated* population is not a
dashboard the owner can trust, and **trust is the product**.

**Finally, this is the first finding in the series produced by auditing the
charter row-by-row rather than by grepping the corpus.** The concept sweep
over 456 contracts returned **zero** uncovered concepts — the audit is
saturating — and this defect was still there, because the words it is written
in (*"avg dwell"*) appear in a **brief**, not in a contract, and the concept it
is about (*"which visits does an average cover?"*) appears **nowhere**. **A
zero-hit sweep is a candidate, not a licence** — and neither is a zero-hit
sweep on the *concepts* a licence to stop.

## Adjacent evidence

| # | Item | Relationship |
|---|---|---|
| 1 | **Feature 415** — the bill-closes-visit edge | **⭐ Must land first, or in the same PR.** Owns the **writer**; this owns the **population**. Different edges. |
| 2 | **Feature 405** — service-day boundary | **Adjacent and important.** Rule 2's *"today"* depends on 405's service day. Read before implementing rule 2. |
| 3 | **Feature 06** — Guest Demographics & Visit Analytics | **Owns the KPI goal as a brief.** A one-line amendment is proposed (Open question 5). |
| 4 | **Feature 388** — table state machine | **Adjacent.** Reads the same `closed_at == None` as "table still occupied". Meaning unchanged. |
| 5 | **Feature 414 / 423** — table capacity, party composition | **Adjacent, same visit/party domain.** |
| 6 | **Feature 408 / 411 / 420** — tax rate, precision, tendered vs received | **Adjacent.** The money KPIs on the same dashboard; their own semantics. |
| 7 | **Feature 353** — `FreeOpenSourcePOS/FloCafe` | **Recorded-not-picked.** The third-party instrument for this pick is already filed as 353 and is used here as **adjacent vocabulary only**. |
| 8 | **Feature 07** — demand estimation (`avg_14d × 1.1`) | **Adjacent.** A *different* average over a *different* population (sales over the last 14 days). Its rule is explicit and its population is closed. **Recorded to prevent confusion: 07 owns its own rule; this feature does not touch it.** |
