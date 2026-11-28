# le31-a-shift-can-close-before-it-opened — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/544-le31-a-shift-can-close-before-it-opened-first-party-the-shift-s-own-duration-and-its-variance-disagree-v1-shift-span-constraint.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `544`
- Slug: `le31-a-shift-can-close-before-it-opened`
- Contract file: `features/544-le31-a-shift-can-close-before-it-opened-first-party-the-shift-s-own-duration-and-its-variance-disagree-v1-shift-span-constraint.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This is the one place where a backdated timestamp leaves the money verdict intact — and where it fools the guard that was written to stop it.**

Feature **426** owns the shift lifecycle, the close route and the open-shift guard. Its guard asks *"is there a shift with `closed_at IS NULL`?"* and refuses a second open shift with a **409**. **The guard is not wrong. The data it was given is.**

**A shift's `variance` is derived from two money columns — `counted_cash` and `opening_float` — and from NO timestamp.** So backdating the close leaves the variance untouched:

| what | value after the backdating |
|---|---|
| the shift's own duration, `closed_at − opened_at` | **−12.0 hours** |
| the open-shift count the guard queries | **0** — it is the only shift in the table |
| `opening_float` / `counted_cash` / `variance` | **100.00 / 100.00 / 0.00** — *"the drawer balanced"* |

**The verdict the owner acts on says the shift was clean. The shift's own timestamps say it ran for minus twelve hours.** And the guard that was written specifically to prevent two overlapping shifts cannot see it.

**Four things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| the **open-shift guard** (one open shift at a time, HTTP 409) | a query | **feature 426** |
| the **close route** and the variance derivation | a route | **feature 426** |
| the shift's **opening float** and its change event | an event table | **feature 536** |
| the shift's **actor** (`by_user_id`) | a column + FK | **feature 417** |
| **a shift that closes before it opened** | **a `CHECK` constraint** | **THIS SLICE** |

**⚠️ The two corpus hits that look like owners are not.** Feature **426**'s *Implementation steps* 3 says, verbatim: *"Implement the open-shift guard as a query for an existing open shift (`closed_at IS NULL`) before inserting a new one … **The guard is a query, not a database constraint** — feature 404's territory, and adding a partial unique index here would be that feature's territory."*

**That is a guard on how many shifts may be open — not a rule about when a shift may close.** And it is the reason this defect is live: **the corpus has already decided, once, that the shift's lifecycle is guarded by queries rather than by the database.** That decision is correct for *how many* shifts are open and is **not** a decision about *when* a shift may close. Feature 426's *Open questions* (the cash-tip term, close idempotency, an empty shift) contain **no** ordering rule.

**The single sentence this feature exists to make true:** *a shift that closed did not close before it began.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one server and one shift opened `2026-11-27 08:00Z` with `opening_float = 100.00`, `counted_cash = 100.00`, `variance = 0.00`.

`UPDATE shift SET closed_at = '2026-11-26 20:00:00'` was **ACCEPTED**. The probe then read back **two numbers that must agree**, and they disagreed:

| what | value | should say |
|---|---|---|
| the shift's own duration, `closed_at − opened_at` | **−12.0 hours** | ≥ 0 |
| the open-shift count the guard queries | **0** | 1 — the shift is open until it is closed |
| the stored money verdict | **100.00 / 100.00 / variance 0.00** | unchanged — **and that is the tell** |

The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code writes `closed_at` today, so the defect is **latent**.

**The finding shapes present:** omission (no ordering rule where one is needed), the **seventh shape** (a covered concept — 426's open-shift guard, 426's variance derivation, 536's float event — with an uncovered **instance** — the relation *between* the two timestamps), **upstream-of-filed-work** (426 is about to create the close write and the guard that trusts `closed_at`), and the **two-numbers-that-must-agree** family — **inverted**, because here the *money* numbers agree with each other and disagree with the *time*.

## Mandatory LE31 skill list (load these first)

1. `skills/le31-conventions/SKILL.md` — the seven-check gate, the naming conventions and the table conventions.
2. `skills/le31-backend/SKILL.md` — the backend layout, the SQLModel conventions and the write-path rules.
3. `skills/le31-data/SKILL.md` — the data-model conventions, the actor convention and the decimal rules.
4. `skills/le31-handoff-spec/SKILL.md` — this document's shape, for reference.
5. `skills/le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern this contract follows.
6. `skills/le31-coding-agent-brief/SKILL.md` — **produces the paste-in prompt automatically from this contract. Do not paste chat excerpts into a prompt.**

**Read `features/453-le31-sqlite-silently-drops-the-utc-offset-…md` before writing the constraint** — it is the authority on the SQLite `DATETIME` offset behaviour this constraint sits on. **And read `features/520-le31-two-tables-can-sit-on-the-same-floor-map-coordinate-…md`** — it is the precedent for adding a constraint to a table that carried zero constraints, and for a constraint that must work on SQLite as well as Postgres.

## Files the slice touches

- **`backend/app/models.py`** — **ADD** a `CheckConstraint` to `class Shift`. **DO NOT** modify any column, and **DO NOT** modify `Table`, `AppUser`, `MenuItem`, `Batch`, `StockEntry`, `Visit`, `OrderItem`, `Bill` or `DerivedTip`.
  - **⚠️ Do NOT touch `opening_float`, `counted_cash` or `variance`.** Feature **536** owns the float's mutability and its change event; feature **426** owns the variance derivation. **Neither is touched.**
- **Tests** — the regression tests listed in the contract's *Verification protocol*, including the **negative control**.
- **`PROJECT_CHARTER.md`** — one sentence recording that a shift's working period is bounded.

**NOT touched:** `index.html` (feature **08**'s scope; a thirteen-way collision zone — features 465/466/467/474/475/476/484/487/489/509/511/516 and this corpus's other UI owners), `backend/app/routers/tables.py`, `backend/app/bot/cook_bot.py`, `backend/app/services/` (does not exist), and every file outside `backend/app/models.py`, the tests and `PROJECT_CHARTER.md`.

## Endpoints and contracts added

**None.** This slice adds **no route**, **no request shape** and **no response shape**. It adds a constraint and a test.

**The refusal is part of the contract even though there is no route:** the database's own constraint-violation error must surface, wrapped by whatever error shape LE31 uses. **⚠️ Do not add a route to produce it** — feature **426** owns the close route, and it will want a **better error message** on top of this constraint.

## Telegram interaction

**None.** No Telegram surface is added or changed. The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched — a shift's window is a fact about the shift, not a cook-side command.

## Verification protocol (end-to-end acceptance path)

**Re-run the probe first.** `/opt/data/le31-brainstorm-2026-11-28-scripts/probe_1128.py` and `probe_two_numbers.py`. **Before the fix they print `update_accepted: true` with a negative duration.** After the fix, the same probe must show the backdated close **refused**.

**The negative control is load-bearing.** A test that asserts *"a close before the open is refused"* **must fail** when the constraint is removed — comment out the constraint and watch the test go red. **A test that passes both with and without the constraint proves nothing.**

The assertions, in order:

1. A `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = 2026-11-26 20:00Z` → **REJECTED**.
2. A `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = 2026-11-27 20:00Z` → **ACCEPTED**.
3. A `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = None` → **ACCEPTED**. **⚠️ THIS IS THE CASE A BADLY-WRITTEN NULL CHECK WOULD REJECT — AND IT IS EVERY SHIFT**, because `closed_at` is nullable and no route writes it today. `closed_at IS NULL OR closed_at >= opened_at` must write the NULL branch **explicitly true**; a `CHECK` evaluating to `UNKNOWN` **passes** in SQL three-valued logic — feature **91**'s shape.
4. A `Shift` with `opened_at = 2026-11-27 08:00Z` and `closed_at = 2026-11-27 08:00Z` → **ACCEPTED** (the boundary — equal is not before).
5. The DDL contains the constraint: rebuild the schema and read `sqlite_master` back — assert the constraint text is present.
6. **No route, service or model outside `Shift` changed**: `git diff --stat` shows `backend/app/models.py`, the tests and `PROJECT_CHARTER.md` only.

**⚠️ Postgres was NOT exercised** — `psycopg` is not importable in the verification venvs on this VPS (sqlmodel 0.0.48 / SQLAlchemy 2.1.8). **Every Postgres claim in the contract is proved from the DDL rendering and dialect behaviour, not a live round trip.** **Do not report the Postgres behaviour as tested.** The constraint must use a **plain comparison** — **not** a `strftime`/`typeof` expression, which is SQLite-only and therefore a dev/prod divergence (feature **453**).

**⚠️ Do NOT turn the open-shift guard into a partial unique index.** Feature **426** decided against it with a correct portability argument: a partial unique index is **not expressible in SQLite**, which is LE31's dev database (charter §3.1), and a rule that works in prod and not in dev is exactly the class of defect feature **427** exists for. **This slice's constraint is deliberately a plain `CHECK` — no partial index, no dialect-specific form. 426's decision is not reopened.**

**⚠️ The demand is UNEVIDENCED.** No code writes `closed_at` today, so the defect is **latent**. **But feature 426 is about to create the close write AND the guard that trusts `closed_at` absolutely.** **426 must land first, or in the same PR.**

## Rollback / feature-removal path

1. Remove the `CheckConstraint` from `class Shift` in `backend/app/models.py`.
2. Remove the tests.
3. Remove the one-line charter note.

**The rollback is safe because the slice is subtractive.** It adds a constraint and **changes no column, no route and no table** — so removing it cannot leave a half-migrated database. **The one caveat: a row that violates the constraint cannot exist while it is in place, so dropping it cannot lose data** — but dropping it re-opens the defect, and any row written in the meantime may violate it.

## What remains safe if removed

- **Every existing behaviour is unchanged.** No route, no request shape and no response shape is touched, so no client can notice the removal.
- **`shift.closed_at` remains exactly as it is** — the same bare nullable timestamp, with the same defect. **The defect returns with the feature; the slice only ever made it impossible to exercise.**
- **Feature 426's open-shift guard keeps working** — it will again trust a backdated close.
- **Feature 426's variance derivation keeps working** — it will again be able to certify a minus-twelve-hour shift as clean.
- **Feature 536's float guard keeps working** — a different column, a different rule.
- **Features 542 and 543 are unaffected** — a different table and a different rule.

## Adjacent work (recorded, NOT picked)

- **`shift.opened_at` itself** — equally rewritable, and no feature owns its mutability. **Recorded in the contract's *Open questions* 4. It is NOT taken by this slice.**
- **A derived shift duration** — the contract's *Open questions* 5 records that deriving the duration (rather than computing it from the two timestamps) would be immune to a backdated close in the same way feature **374**'s derived `qty_remaining` is. **Recorded default: not in this slice** — that is a charter-shape question about whether a duration is a fact or a computation, and it touches feature 426's variance derivation. **Not taken.**
- **A repair path for already-stored impossible shifts** — the contract's *Open questions* 6 records that this slice does **not** migrate data, and that a repair would be a separate change. **Not taken.**
- **`visit.closed_at` vs `visit.opened_at`** — filed by this same pass as **feature 542**.
- **`batch.expires_at` vs `batch.prepared_at`** — filed by this same pass as **feature 543**.
