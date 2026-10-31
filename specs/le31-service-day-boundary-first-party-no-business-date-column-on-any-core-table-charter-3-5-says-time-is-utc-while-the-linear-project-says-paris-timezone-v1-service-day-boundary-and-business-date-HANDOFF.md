# HANDOFF — 405-le31-service-day-boundary

**Status**: **build** (v1, first-party defect in LE31's own schema and charter)
**Date**: 2026-10-30
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/405-le31-service-day-boundary-first-party-no-business-date-column-on-any-core-table-charter-3-5-says-time-is-utc-while-the-linear-project-says-paris-timezone-v1-service-day-boundary-and-business-date.md`
**LE31 feature gate verdict**: **build** — all seven checks pass. Evidence class **OBSERVED** (schema and charter read directly; the charter contradiction is verbatim from two LE31 documents). **This is not a vocabulary artifact — it produces code.**

## Trigger policy

This is a **build** contract. The external coding agent **should** implement it.

**Before writing any code**, the agent must:

1. Load the active feature file, this handoff, and the parent report (`/opt/data/le31-daily-research-2026-10-30.md`).
2. Load **feature 404** (the active-batch predicate — *adjacent, not identical*) and **feature 374** (`Batch.qty_remaining` — *a different rule about a different kind of value*). **Do not merge either into this slice.**
3. Read the two charter statements side by side and **write the reconciliation paragraph** into `PROJECT_CHARTER.md` as step 1 of the implementation.
4. **Confirm the two owner decisions are still open** (see *Frozen contract* below). If the owner has since decided them, use the decision. **If not, implement the recorded defaults** — local-midnight boundary, `Europe/Paris` as the venue timezone — and **leave the `tz` parameter in place** so a later configuration change is one line.

**Disambiguation**: this slice is about **which day a row belongs to**. It is **not** about the active-batch predicate (feature 404), **not** about deriving stock quantities (feature 374), **not** about converting stored timestamps to local time (**nothing does that**), and **not** about the day-scoped ticket-code mechanism (the artifact's code-shape is **not adopted**).

## Frozen contract

**The one thing this contract exists to make true:** *LE31 knows which service day an order belongs to.*

**The helper** — exactly this, in a new file `backend/app/services/business_time.py`:

```python
from datetime import date, datetime
from zoneinfo import ZoneInfo

VENUE_TZ = ZoneInfo("Europe/Paris")


def business_date(instant: datetime, tz: ZoneInfo = VENUE_TZ) -> date:
    """The service day `instant` belongs to, in the venue's timezone."""
    if instant.tzinfo is None:
        raise ValueError("business_date() requires a timezone-aware instant")
    return instant.astimezone(tz).date()
```

**The columns** — nullable `date`, on three tables only:

| Table | Column | Indexed |
|---|---|---|
| `Visit` | `business_date: date \| None = None` | yes |
| `Bill` | `business_date: date \| None = None` | yes |
| `Shift` | `business_date: date \| None = None` | no |

**NOT** on `StockEntry`, **NOT** on `Batch`, **NOT** on `OrderItem`, **NOT** on `MenuItem`. `StockEntry.at` and `Batch.prepared_at` are **instants and remain instants**. Adding a day column to `Batch` would **pre-empt feature 404's Open question 2** ("what is a service day?"), which this slice answers — so it must be done **here or there, once**, not twice.

**The writers** — set at creation, in the same statement:

```python
business_date=business_date(utcnow()),
```

`grep -rn 'Visit(\|Bill(\|Shift(' backend/` must show **every** construction site setting it. A construction site that does not set it is a defect **in this slice**, not a follow-up.

**The `NULL` rule** — `business_date IS NULL` means *"the business day was not recorded"*. Readers **must not** silently substitute `business_date(opened_at)`: re-deriving reintroduces the split-brain this slice exists to remove. **Write this rule into the feature docs where a reader will find it.**

**The charter paragraph** — one short block in `PROJECT_CHARTER.md` stating: storage is timezone-aware UTC (**unchanged**); the service day is derived in the venue's timezone; `Europe/Paris` is the default until the owner says otherwise. **A charter that still states only *"Time is UTC"* is the defect, still present.**

**Anti-goals, stated so they are not drifted into:**

- **No conversion of stored timestamps.** Nothing in this slice renders a UTC instant as local wall-clock time. The charter's *"Time is UTC"* remains **true of storage**.
- **No timezone configuration system.** The `tz` parameter exists so that decision can be deferred without a schema change. **Do not build a settings table.**
- **No backfill of historical rows.** `business_date` is `NULL` for pre-existing rows, and that is **correct**. A backfill touches historical rows, is a separate change, and needs its own gate. **Record it as follow-up.**
- **No ticket-code mechanism.** No `code_sequences` table, no `K-YYMMDD-NNN`. The artifact's code-shape is Electron/React/Express/PGlite — **off-stack, and not adopted**.
- **No multi-country / localization work.** Feature 64 owns that. **Do not merge.**
- **No `CHECK` constraints on the money columns.** That is the *other* feature 404. **Do not merge.**

## Files to touch

| File | Change |
|---|---|
| `backend/app/services/business_time.py` | **NEW.** `VENUE_TZ` + `business_date()`. Requires creating `backend/app/services/` with `__init__.py` (**it does not exist today**). |
| `backend/app/models.py` | **ADD** `business_date: date \| None = None` to `class Visit`, `class Bill`, `class Shift` **only**. **Do not touch any other class, field or timestamp.** Import `date` from `datetime`. |
| `backend/app/routers/tables.py` | **SET** `business_date=business_date(utcnow())` at the `Visit(...)` construction site (the `seat_party` handler). Import the helper. |
| `PROJECT_CHARTER.md` | **ADD** the reconciliation paragraph (§7 Quality bar, next to the *"Time is UTC"* bullet). |
| `features/405-…md` | **AMEND** the *Data model* section to record the **chosen** boundary rule and the `NULL` rule. |
| `backend/tests/test_business_time.py` (or the repo's existing test location) | **NEW.** The regression tests below. |

**Any other file is out of scope.** If the agent believes another file must change, that is a **new finding** — surface it, do not silently widen the slice.

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — the seven-check feature gate and the hard invariants (charter §3.2 fixed stack and surfaces, §3.4 AI boundary, §3.6 money, business-time invariant).
- `le31-v1-feature-pattern` — the canonical contract shape and the slicing rules.
- `le31-research` — the source-of-truth discipline behind the artifact quotes.
- `le31-handoff-spec` — the frozen-contract discipline.
- `development` — the generic code pipeline (specify → plan → tasks → implement → independent review).

The agent must **NOT** load `le31-feature-pipeline` — the slice is already in the pipeline.

## Mandatory inputs

- **Active feature**: `features/405-le31-service-day-boundary-first-party-…-v1-service-day-boundary-and-business-date.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-30.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-30/`
  - `gh/repo_zakariaelqannaa-dv__resto-management.json` — direct `GET /repos/` (HTTP 200)
  - `gh/readme_zakariaelqannaa-dv__resto-management.md` — README (base64-JSON payload; decode `content` before reading)
  - `gh/tree_zakariaelqannaa-dv__resto-management.json` — file tree
- **Decoded README** (parent-produced): `/opt/data/le31-fetch-2026-10-30/readmes/zakariaelqannaa-dv__resto-management.markdown`
- **LE31 source of truth**:
  - `backend/app/models.py` — `class Batch` (the docstring promising *"for a specific day"*), `class Visit` (line 129), `class Bill` (line 158), `class Shift` (line 181), `class StockEntry` (line 113)
  - `backend/app/routers/tables.py` — `seat_party` (the `Visit(...)` construction site)
  - `grep -rn 'business_date\|service_date' backend/` → **no output** (the evidence that the day does not exist)
  - `grep -rn 'audit_log\|class Audit' backend/app/models.py` → **no output**
  - `grep -rn 'UserRole\.' backend/` → **no output**
  - `backend/app/routers/` → **contains only `tables.py`**
- **Charter §7 Quality bar** (the *"Time is UTC"* bullet) and **§8 Verification protocol** — `PROJECT_CHARTER.md`
- **Sibling features to read but NOT merge**: 404 (active-batch predicate — *both* 404s are adjacent), 374 (`qty_remaining` derive-never-store), 392 (unit meaning), 34 (stock board — the "today's batches" question), 39 (owner daily recap — the first consumer), 43 / 44 (`service_date` precedent on their own new tables).

## Verification protocol reference

Follow **`PROJECT_CHARTER.md` §8 Verification protocol** steps 1–11, with these slice-specific additions:

**Step 9 (inspect SQLite) becomes two inspections:**
```bash
sqlite3 backend/restaurant.db ".schema visit"
sqlite3 backend/restaurant.db ".schema bill"
sqlite3 backend/restaurant.db ".schema shift"
```
Assert each shows a `business_date` column of type `DATE` and **nullable**.

**Add these regression tests** (the second and third are the ones that keep the feature alive):

```python
def test_friday_night_order_belongs_to_friday():
    # 2026-10-30T23:30:00Z is Saturday 01:30 in Paris — the order is Friday's.
    assert business_date(datetime(2026, 10, 30, 23, 30, tzinfo=timezone.utc)) == date(2026, 10, 30)

def test_after_midnight_paris_is_the_next_service_day():
    assert business_date(datetime(2026, 10, 31, 0, 30, tzinfo=timezone.utc)) == date(2026, 10, 31)

def test_midday_is_not_a_utc_truncation():
    assert business_date(datetime(2026, 10, 30, 12, 0, tzinfo=timezone.utc)) == date(2026, 10, 30)

def test_naive_datetime_is_rejected():
    with pytest.raises(ValueError):
        business_date(datetime(2026, 10, 30, 23, 30))
```

**The first three must assert against a literal `date`, not against a re-implementation of the same expression.** A test that recomputes the answer the same way the code does proves nothing.

**End-to-end acceptance path** (per `le31-v1-feature-pattern`): a `Visit` created through `POST /api/tables/{id}/seat` at a Friday 23:30 UTC instant **must** show `business_date = 2026-10-30` in the DB, and the seated table's API response must agree. **Exercise the real router** — per `le31-conventions` common pitfall 4, *"tests pass" is not the acceptance path.*

**Must-fail-first discipline**: write the `test_friday_night_order_belongs_to_friday` test **before** the helper exists and **watch it fail**, then implement, then watch it pass. A test that has only ever passed proves nothing.

## Rollback path

**Fully reversible, and deliberately so.**

1. **Revert the commit.** The feature is one commit adding one file, three columns, three writer edits, one charter paragraph and one test file.
2. **Or, piecewise:** drop the three columns, delete `backend/app/services/business_time.py`, revert the three writer lines, revert the charter paragraph. **No data is lost** — `business_date` is nullable and additive, and **no existing row is rewritten or deleted.**
3. **No migration to undo.** §3.2's stated v1 policy is `init_db()`. A dev database is recreated from the schema; a production database is migrated forward with a nullable column, which is additive.
4. **What remains safe if removed:** every existing behaviour. **Nothing in LE31 reads `business_date` today** — the column is written and unused until a report surface lands. **The slice is therefore inert on its own**, which is precisely why it is cheap and why it must land **before** the report surface.

**Retained data:** the `business_date` values written by the three writers. **They remain correct under any future boundary rule for the rows they describe** — except for the boundary decision itself, which is why the rule is written down and not left to each caller.

## Sign-off gap

**Two owner decisions are open, and the agent must implement the recorded defaults rather than guess beyond them:**

1. **Does the service day start at local midnight, or at the venue's opening time?** **Recorded default: local midnight.** A venue that opens at 11:00 may want a 00:30 table to belong to the previous night's service. **This is an owner decision, not a research finding.**
2. **Is the venue's timezone `Europe/Paris`, or configurable?** **Recorded default: `Europe/Paris`**, because `le31-conventions` and the Linear project summary both state Paris. **The helper already takes a `tz` parameter**, so making it configurable later is one line and needs no schema change.

**The agent must not widen either decision.** If the implementation seems to require a different answer, that is a **finding to surface**, not a choice to make.

**Also open, and explicitly not decided here:** the **`NULL` backfill question** (historical rows keep `NULL`; a backfill is a separate, separately-gated change) and **whether `Europe/Paris` is right for a venue outside France** (feature 64 owns any change).

## Handoff summary

LE31 promises, in `Batch`'s own docstring, *"a concrete prepared quantity of a MenuItem **for a specific day**"* — and has no way to name a day. There is no business-date column on `Visit`, `Bill`, `Shift`, `StockEntry` or `Batch` (`grep -rn 'business_date\|service_date' backend/` → no output), and three LE31 documents state the rule three different ways: the charter says *"Time is UTC"*, the Linear project says *"Paris timezone"*, `le31-conventions` says *"render business dates in `Europe/Paris`"*. **None is implemented.**

The failure is not an error — it is a **wrong number in a report, concentrated in the hours a restaurant is busiest.** A Friday 23:30 UTC order is Saturday 01:30 in Paris; two reasonable callers disagree about which day it belongs to, and **nothing in LE31 can tell the owner which one was used.** The charter's P0 *"browse **today's** menu"* and P1 *"dashboard shows covers **today**"* both need the answer.

The fix is small and should land now, while it is still inert: **one helper with exactly one home, three nullable `date` columns with exactly one writer each, one charter paragraph, one regression test that pins the Friday-night case.** The external artifact (`zakariaelqannaa-dv/resto-management`, MIT) contributed the vocabulary — *"a **service date** and a **day-scoped code number**"*, the day as part of a ticket's identity rather than a function of a timestamp. **Its code-shape is not adopted.**
