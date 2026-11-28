# le31-a-batch-can-expire-before-it-was-prepared — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/543-le31-a-batch-can-expire-before-it-was-prepared-first-party-the-batch-is-then-invisible-v1-batch-window-constraint.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `543`
- Slug: `le31-a-batch-can-expire-before-it-was-prepared`
- Contract file: `features/543-le31-a-batch-can-expire-before-it-was-prepared-first-party-the-batch-is-then-invisible-v1-batch-window-constraint.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**A batch that expires before it was prepared was never in service — and LE31 cannot tell the difference.**

Feature **404** owns the active-batch predicate (*"`expires_at IS NULL OR expires_at > now()`"*) and feature **447** owns the refusal to sell from an expired batch. **Both read `expires_at` as *"the instant this batch stops being usable"*.** Neither reader can detect that the value they read was **never a possible value**.

**Why this one matters more than a routine constraint addition — feature 374 makes it worse:**

Feature **374** is about to **remove** `Batch.qty_remaining` and replace every read with `SUM(stock_entry.qty_delta) WHERE batch_id = X`. **That derivation does not consult `expires_at` at all.** So from 374 onward:

- the **ledger** says the batch holds its stock, and
- the **active-batch predicate** says the batch does not exist,

**and the two can never agree.** A batch with an impossible expiry is **permanently invisible stock**: ten prepared tiramisus that no query can find.

**Five things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| the **active-batch predicate** | a helper | **feature 404** |
| refusing to sell from an **expired** batch | a write-path precondition | **feature 447** |
| **deriving** `qty_remaining` from the ledger | removing a column | **feature 374** |
| the batch's **preparer** (no actor column) | a nullable column | **feature 445** |
| the **order-line → batch** provenance | a pointer + a selection rule | **feature 385** |
| a ledger row's batch and line must name the **same dish** | a write-path rule | **feature 441** |
| **a batch that expires before it was prepared** | **a `CHECK` constraint** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is filing a duplicate of 404 or 447.** 404 owns *the predicate*; 447 owns *the refusal*. **Both consume `expires_at`; neither says the value may be impossible.** Feature 447's own *Out of scope* says, verbatim: *"**The active-batch predicate itself.** Feature 404 owns the rule … **This feature consumes that rule; it does not redefine it.**"*

**The single sentence this feature exists to make true:** *a batch that expires did not expire before it was made.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one menu item, one batch prepared `2026-11-20 09:00Z` and expiring `2026-11-21 09:00Z`, and one server.

`UPDATE batch SET expires_at = '2026-11-19 09:00:00'` was **ACCEPTED**. The probe then read back **two numbers that must agree**, and they disagreed:

| what | value | should say |
|---|---|---|
| the batch's own lifetime, `expires_at − prepared_at` | **−24.0 hours** | ≥ 0 |
| the number of batches the active-batch predicate sees | **0** | 1 — the batch exists and holds stock |
| the batch's own `qty_remaining` | **10** | 10 — the stock is real |

The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code writes `expires_at` today (feature **404**'s *Open questions* 3 records this), so the defect is **latent**.

**The finding shapes present:** omission (no ordering rule where one is needed), the **seventh shape** (a covered concept — 404's predicate, 447's refusal, 374's derivation — with an uncovered **instance** — the possibility of the value all three read), **upstream-of-filed-work** (374 will make the disagreement permanent), and the **two-numbers-that-must-agree** family.

## Mandatory LE31 skill list (load these first)

1. `skills/le31-conventions/SKILL.md` — the seven-check gate, the naming conventions and the table conventions.
2. `skills/le31-backend/SKILL.md` — the backend layout, the SQLModel conventions and the write-path rules.
3. `skills/le31-data/SKILL.md` — the data-model conventions, the actor convention and the decimal rules.
4. `skills/le31-handoff-spec/SKILL.md` — this document's shape, for reference.
5. `skills/le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern this contract follows.
6. `skills/le31-coding-agent-brief/SKILL.md` — **produces the paste-in prompt automatically from this contract. Do not paste chat excerpts into a prompt.**

**Read `features/453-le31-sqlite-silently-drops-the-utc-offset-…md` before writing the constraint** — it is the authority on the SQLite `DATETIME` offset behaviour this constraint sits on. **And read `features/520-le31-two-tables-can-sit-on-the-same-floor-map-coordinate-…md`** — it is the precedent for adding a constraint to a table that carried zero constraints, and for a constraint that must work on SQLite as well as Postgres.

## Files the slice touches

- **`backend/app/models.py`** — **ADD** a `CheckConstraint` to `class Batch`. **DO NOT** modify any column, and **DO NOT** modify `Table`, `AppUser`, `MenuItem`, `StockEntry`, `Visit`, `OrderItem`, `Bill`, `DerivedTip` or `Shift`.
  - **⚠️ Do NOT touch `qty_remaining` and do NOT touch `qty_start`.** Feature **374** owns both — 374 removes `qty_remaining`, and its *Open questions* 1 asks whether `qty_start` survives. **That question is not answered here.**
- **Tests** — the regression tests listed in the contract's *Verification protocol*, including the **negative control**.
- **`PROJECT_CHARTER.md`** — one sentence recording that a batch's preparation window is bounded.

**NOT touched:** `index.html` (feature **08**'s scope; a thirteen-way collision zone — features 465/466/467/474/475/476/484/487/489/509/511/516 and this corpus's other UI owners), `backend/app/routers/tables.py`, `backend/app/bot/cook_bot.py`, `backend/app/services/` (does not exist), and every file outside `backend/app/models.py`, the tests and `PROJECT_CHARTER.md`.

## Endpoints and contracts added

**None.** This slice adds **no route**, **no request shape** and **no response shape**. It adds a constraint and a test.

**The refusal is part of the contract even though there is no route:** the database's own constraint-violation error must surface, wrapped by whatever error shape LE31 uses. **⚠️ Do not add a writer to produce it** — feature **404**'s *Open questions* 3 (*"who sets `expires_at` in practice?"*) is 404's, and the prep flow is feature **03**'s.

## Telegram interaction

**None.** No Telegram surface is added or changed. The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched — a batch's window is a fact about the batch, not a cook-side command.

## Verification protocol (end-to-end acceptance path)

**Re-run the probe first.** `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`. **Before the fix they print `update_accepted: true` with a negative lifetime.** After the fix, the same probe must show the backdated expiry **refused**.

**The negative control is load-bearing.** A test that asserts *"an expiry before the preparation is refused"* **must fail** when the constraint is removed — comment out the constraint and watch the test go red. **A test that passes both with and without the constraint proves nothing.**

The assertions, in order:

1. A `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = 2026-11-19 09:00Z` → **REJECTED**.
2. A `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = 2026-11-21 09:00Z` → **ACCEPTED**.
3. A `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = None` → **ACCEPTED**. **⚠️ THIS IS THE CASE A BADLY-WRITTEN NULL CHECK WOULD REJECT — AND IT IS THE COMMON CASE**, because `expires_at` is nullable and no writer sets it today (feature 404's *Open questions* 3). `expires_at IS NULL OR expires_at >= prepared_at` must write the NULL branch **explicitly true**; a `CHECK` evaluating to `UNKNOWN` **passes** in SQL three-valued logic — feature **91**'s shape.
4. A `Batch` with `prepared_at = 2026-11-20 09:00Z` and `expires_at = 2026-11-20 09:00Z` → **ACCEPTED** (the boundary — equal is not before).
5. The DDL contains the constraint: rebuild the schema and read `sqlite_master` back — assert the constraint text is present.
6. **No route, service or model outside `Batch` changed**: `git diff --stat` shows `backend/app/models.py`, the tests and `PROJECT_CHARTER.md` only.

**⚠️ Postgres was NOT exercised** — `psycopg` is not importable in the verification venvs on this VPS (sqlmodel 0.0.48 / SQLAlchemy 2.1.8). **Every Postgres claim in the contract is proved from the DDL rendering and dialect behaviour, not a live round trip.** **Do not report the Postgres behaviour as tested.** The constraint must use a **plain comparison** — **not** a `strftime`/`typeof` expression, which is SQLite-only and therefore a dev/prod divergence (feature **453**).

**⚠️ The demand is UNEVIDENCED.** No code writes `expires_at` today, so the defect is **latent**. **But feature 374 will make it materially worse**, because the ledger derivation it introduces does not read `expires_at` at all. **374 must land first, or in the same PR.**

## Rollback / feature-removal path

1. Remove the `CheckConstraint` from `class Batch` in `backend/app/models.py`.
2. Remove the tests.
3. Remove the one-line charter note.

**The rollback is safe because the slice is subtractive.** It adds a constraint and **changes no column, no route and no table** — so removing it cannot leave a half-migrated database. **The one caveat: a row that violates the constraint cannot exist while it is in place, so dropping it cannot lose data** — but dropping it re-opens the defect, and any row written in the meantime may violate it.

## What remains safe if removed

- **Every existing behaviour is unchanged.** No route, no request shape and no response shape is touched, so no client can notice the removal.
- **`batch.expires_at` remains exactly as it is** — the same bare nullable timestamp, with the same defect. **The defect returns with the feature; the slice only ever made it impossible to exercise.**
- **Feature 404's predicate keeps working** — it will again be able to select a batch that was never in service.
- **Feature 447's refusal keeps working** — it will again refuse a sale from a batch that never existed as sellable stock.
- **Feature 374's derivation keeps working** — it will again be able to disagree with the active-batch predicate.
- **Features 385, 441, 445 are unaffected** — a different rule, a different table or a different column.

## Adjacent work (recorded, NOT picked)

- **`batch.prepared_at` itself** — equally rewritable, and no feature owns its mutability. **Recorded in the contract's *Open questions* 3. It is NOT taken by this slice.**
- **`stock_entry.at` vs `batch.prepared_at`** — a ledger row stamped before its batch was prepared is the same class on a different table. Feature **417** owns the actor, **421** owns where the row may be written, **441** owns the dish coherence. **Recorded in the contract's *Open questions* 4. Not taken.**
- **`batch.expires_at`'s default** — feature **404**'s *Open questions* 3 (*"who sets `expires_at` in practice?"*) and its option B (a default of end-of-service-day). **Not taken.**
- **A repair path for already-stored impossible batches** — the contract's *Open questions* 5 records that this slice does **not** migrate data, and that a repair would be a separate change. **Not taken.**
- **`visit.closed_at` vs `visit.opened_at`** — filed by this same pass as **feature 542**.
- **`shift.closed_at` vs `shift.opened_at`** — filed by this same pass as **feature 544**.
- **`batch.qty_start`** — rewritable; feature **374**'s *Open questions* 1 asks whether it survives at all. **Not taken.**
