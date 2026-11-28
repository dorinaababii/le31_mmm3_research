# le31-a-visit-can-close-before-it-opened — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/542-le31-a-visit-can-close-before-it-opened-first-party-the-floor-map-then-reads-free-v1-visit-span-constraint.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `542`
- Slug: `le31-a-visit-can-close-before-it-opened`
- Contract file: `features/542-le31-a-visit-can-close-before-it-opened-first-party-the-floor-map-then-reads-free-v1-visit-span-constraint.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice closes a gap the corpus found and filed twice — and never.**

Feature **452** wrote, verbatim, in its *Adjacent evidence*:

> *"`Visit.closed_at` is unconstrained against `opened_at` — executed: a visit can close three days **before** it opened. Feature **428** owns the *population* rule for open visits; feature **415** owns *writing* `closed_at`. **Neither owns the ordering constraint. Recorded, not picked** — a visit's duration is a different fact from a line's state."*

**That is the corpus's own hand-off.** 452 named the two neighbours, and **both neighbours disclaim it** — 415's *Out of scope* is about the `Table` status column, and 428's *Out of scope* says *"**Writing `Visit.closed_at`. That is feature 415**"*. **Neither one owns the constraint between the two columns.**

**Why this is not the same defect as 415's or 428's:**

| rule | mechanism | owner |
|---|---|---|
| **writing** `Visit.closed_at` (the close write) | a route | **feature 415** |
| the **population** for the dwell average | an aggregate helper | **feature 428** |
| the **table's** status | a derived helper + a `Table.status` column | **feature 388** |
| the visit's **table** changing after seating | an event table | **feature 538** |
| the visit's **server** changing after seating | an event table | **feature 539** |
| the visit's **composition** changing | an event table | **feature 533** |
| **a close that precedes the open** | **a `CHECK` constraint** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is filing a duplicate of 415.** 415 owns *the write*. This slice owns *the possibility of the value the write produces*. **Fixing 415 without this feature produces a close write with no guard behind it; fixing this without 415 produces a constraint that never fires.**

**The single sentence this feature exists to make true:** *a visit that has closed did not close before it began.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one table, one server, one menu item, one open visit opened `2026-11-27 12:00Z`, one order line and one paid bill with `paid_at = 2026-11-27 13:00Z`.

`UPDATE visit SET closed_at = '2026-11-24 09:00:00'` was **ACCEPTED**. The probe then read back **two numbers that must agree**, and they disagreed:

| what | value | should say |
|---|---|---|
| the visit's own duration, `closed_at − opened_at` | **−4,500 minutes** | ≥ 0 |
| the bill's `paid_at` − the visit's `closed_at` | **+4,560 minutes** | ≥ 0 |

And the shipped read changed with it: `_table_status()`'s query (`closed_at IS NULL`) went from **1** open visit on that table to **0**, so the floor map read **`free`** — while the guest was sitting there and their bill was already paid.

The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path writes `closed_at` today, so the defect is **latent**. **But see the caveat below: the precondition for it is a filed feature that is about to land.**

**The finding shapes present:** omission (no ordering rule where one is needed), the **seventh shape** (a covered concept — 415's close write, 428's dwell aggregate — with an uncovered **instance** — the relation *between* the two timestamps), **upstream-of-filed-work** (415 is about to start writing `closed_at`), and the **two-numbers-that-must-agree** family.

## Mandatory LE31 skill list (load these first)

1. `skills/le31-conventions/SKILL.md` — the seven-check gate, the naming conventions and the table conventions.
2. `skills/le31-backend/SKILL.md` — the backend layout, the SQLModel conventions and the write-path rules.
3. `skills/le31-data/SKILL.md` — the data-model conventions, the actor convention and the decimal rules.
4. `skills/le31-handoff-spec/SKILL.md` — this document's shape, for reference.
5. `skills/le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern this contract follows.
6. `skills/le31-coding-agent-brief/SKILL.md` — **produces the paste-in prompt automatically from this contract. Do not paste chat excerpts into a prompt.**

**Read `features/453-le31-sqlite-silently-drops-the-utc-offset-…md` before writing the constraint** — it is the authority on the SQLite `DATETIME` offset behaviour this constraint sits on. **And read `features/520-le31-two-tables-can-sit-on-the-same-floor-map-coordinate-…md`** — it is the precedent for adding a constraint to a table that carried zero constraints, and for a constraint that must work on SQLite as well as Postgres.

## Files the slice touches

- **`backend/app/models.py`** — **ADD** a `CheckConstraint` to `class Visit`. **DO NOT** modify any column, and **DO NOT** modify `Table`, `AppUser`, `MenuItem`, `Batch`, `StockEntry`, `OrderItem`, `Bill`, `DerivedTip` or `Shift`.
- **Tests** — the regression tests listed in the contract's *Verification protocol*, including the **negative control**.
- **`PROJECT_CHARTER.md`** — one sentence recording that a visit's span is bounded.

**NOT touched:** `index.html` (feature **08**'s scope; a thirteen-way collision zone — features 465/466/467/474/475/476/484/487/489/509/511/516 and this corpus's other UI owners), `backend/app/routers/tables.py`, `backend/app/bot/cook_bot.py`, `backend/app/services/` (does not exist), and every file outside `backend/app/models.py`, the tests and `PROJECT_CHARTER.md`.

## Endpoints and contracts added

**None.** This slice adds **no route**, **no request shape** and **no response shape**. It adds a constraint and a test.

**The refusal is part of the contract even though there is no route:** the database's own constraint-violation error must surface, wrapped by whatever error shape LE31 uses. **⚠️ Do not add a route to produce it** — feature **415** owns the close write, and **388** owns the `Table.status` column and the seat guard.

## Telegram interaction

**None.** No Telegram surface is added or changed. The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched.

## Verification protocol (end-to-end acceptance path)

**Re-run the probe first.** `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`. **Before the fix they print `update_accepted: true` with a negative duration.** After the fix, the same probe must show the backdated close **refused**.

**The negative control is load-bearing.** A test that asserts *"a close before the open is refused"* **must fail** when the constraint is removed — comment out the constraint and watch the test go red. **A test that passes both with and without the constraint proves nothing.**

The assertions, in order:

1. A `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = 2026-11-24 09:00Z` → **REJECTED**.
2. A `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = 2026-11-27 13:00Z` → **ACCEPTED**.
3. A `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = None` → **ACCEPTED**. **⚠️ THIS IS THE CASE A BADLY-WRITTEN NULL CHECK WOULD REJECT.** `closed_at IS NULL OR closed_at >= opened_at` must write the NULL branch **explicitly true**; a `CHECK` evaluating to `UNKNOWN` **passes** in SQL three-valued logic — feature **91**'s shape.
4. A `Visit` with `opened_at = 2026-11-27 12:00Z` and `closed_at = 2026-11-27 12:00Z` → **ACCEPTED** (the boundary — equal is not before).
5. The DDL contains the constraint: rebuild the schema and read `sqlite_master` back — assert the constraint text is present.
6. **No route, service or model outside `Visit` changed**: `git diff --stat` shows `backend/app/models.py`, the tests and `PROJECT_CHARTER.md` only.

**⚠️ Postgres was NOT exercised** — `psycopg` is not importable in the verification venvs on this VPS (sqlmodel 0.0.48 / SQLAlchemy 2.1.8). **Every Postgres claim in the contract is proved from the DDL rendering and dialect behaviour, not a live round trip.** **Do not report the Postgres behaviour as tested.** The constraint must use a **plain comparison** — **not** a `strftime`/`typeof` expression, which is SQLite-only and therefore a dev/prod divergence (feature **453**).

**⚠️ The demand is UNEVIDENCED — but with one important difference from the usual case.** No code path writes `closed_at` today, so the defect is **latent**. **However**, feature **415** is about to create the close write, and `seat_party` (`tables.py:33–61`) runs **today** with **no guard at all** — line 50 is a literal `# TODO: reject if table is not FREE`. **So the precondition for this defect is a filed feature that is about to land. That is why 415 must land first, or in the same PR.**

## Rollback / feature-removal path

1. Remove the `CheckConstraint` from `class Visit` in `backend/app/models.py`.
2. Remove the tests.
3. Remove the one-line charter note.

**The rollback is safe because the slice is subtractive.** It adds a constraint and **changes no column, no route and no table** — so removing it cannot leave a half-migrated database. **The one caveat: a row that violates the constraint cannot exist while it is in place, so dropping it cannot lose data** — but dropping it re-opens the defect, and any row written in the meantime may violate it.

## What remains safe if removed

- **Every existing behaviour is unchanged.** No route, no request shape and no response shape is touched, so no client can notice the removal.
- **`visit.closed_at` remains exactly as it is** — the same bare nullable timestamp, with the same defect. **The defect returns with the feature; the slice only ever made it impossible to exercise.**
- **Feature 415's close write keeps working** — it simply has no guard behind it.
- **Feature 428's dwell aggregate keeps working** — it will again be able to compute a negative average.
- **Features 388, 452, 533, 538, 539 are unaffected** — a different table or a different rule.

## Adjacent work (recorded, NOT picked)

- **`visit.opened_at` itself** — equally rewritable, and no feature owns its mutability. **Recorded in the contract's *Open questions* 5. It is NOT taken by this slice.** The same question applies to `batch.prepared_at` and `shift.opened_at`.
- **`visit.opened_at` vs `visit.closed_at` vs `bill.paid_at`** — the *third* timestamp in the same span. Feature **415**'s *Open questions* 1 (*"should `closed_at` be the payment instant or the moment the waiter taps close?"*) is **not answered here**, and this constraint is compatible with either answer.
- **`batch.expires_at` vs `batch.prepared_at`** — filed by this same pass as **feature 543**.
- **`shift.closed_at` vs `shift.opened_at`** — filed by this same pass as **feature 544**.
- **`order_item`'s `fired_at` / `ready_at` / `served_at`** — the same class on the order line. Feature **452** owns the *status ↔ timestamps* rule; the timestamps' own ordering and mutability is a separate question, recorded in 452's *Adjacent evidence*. **Not taken.**
- **`stock_entry.at` vs `batch.prepared_at`** — the same class on the ledger. Feature **417** owns the actor and **421** owns where the row may be written. **Not taken.**
- **The `# TODO: reject if table is not FREE` at `tables.py:50`** — feature **388**'s. **Not taken.**
