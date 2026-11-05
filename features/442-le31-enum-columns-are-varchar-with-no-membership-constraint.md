# Feature 442 — `le31-enum-columns-are-varchar-with-no-membership-constraint`

> **Pick B of Daily Brainstorm 2026-11-05 (98th daily-brainstorm pass).** **FIRST-PARTY, and the gap was PROVEN BY EXECUTION on 2026-11-05 — not inferred from reading code.**
>
> LE31's own `backend/app/models.py` declares **five** enums, and every one of them is rendered by SQLModel as a **bare `VARCHAR(n)` with no membership constraint**:
>
> ```python
> class PaymentMethod(str, Enum):
>     cash = "cash"
>     card = "card"
>
> class ItemStatus(str, Enum):
>     new = "new"; preparing = "preparing"; ready = "ready"
>     served = "served"; cancelled = "cancelled"
>
> class StockReason(str, Enum):
>     initial = "initial"; sale = "sale"; waste = "waste"
>     restock = "restock"; sold_out = "sold_out"
>
> class UserRole(str, Enum):
>     server = "server"; cook = "cook"; manager = "manager"
>
> class TableStatus(str, Enum):
>     free = "free"; seated = "seated"; ordered = "ordered"
>     billed = "billed"; dirty = "dirty"
> ```
>
> The parent built LE31's **real** schema (`SQLModel.metadata.create_all` on a throwaway SQLite file) and enumerated what the database actually accepts. The declared widths are **exactly the length of the longest member** — `payment_method VARCHAR(4)`, `status VARCHAR(9)`, `reason VARCHAR(8)`, `role VARCHAR(7)`.
>
> **Then the parent wrote values that are not members, through raw SQL, bypassing the ORM's Python-side validation:**
>
> ```
> INSERT INTO bill (..., payment_method) VALUES (..., 'bitcoin')   -> ACCEPTED, stored
> INSERT INTO order_item (..., status) VALUES (..., 'cooked')       -> ACCEPTED, stored
> INSERT INTO stock_entry (..., reason) VALUES (..., 'gift')        -> ACCEPTED, stored
> INSERT INTO app_user (..., role) VALUES (..., 'owner')           -> ACCEPTED, stored
> ```
>
> And the parent read the columns back:
>
> ```
> SELECT DISTINCT payment_method FROM bill    -> ['bitcoin']
> SELECT DISTINCT status FROM order_item      -> ['cooked']
> SELECT DISTINCT reason FROM stock_entry     -> ['gift']
> SELECT DISTINCT role FROM app_user          -> ['server', 'owner']
> ```
>
> **Every one of LE31's five enums accepts a value outside itself. Not one of them has a `CHECK` constraint — the count is `0` on every one of the four tables that carry an enum.**
>
> **And the ORM does not save you.** The parent also wrote `Bill(payment_method="bitcoin", ...)` — a plain `str`, not the enum — through SQLModel itself, and it was **accepted and stored**. **SQLModel does not validate a `str` against a `str, Enum` annotation at write time.**
>
> **⭐ THE DEV/PROD DIVERGENCE IS THE SEVERE PART, AND IT IS EXECUTABLE.** `payment_method` is declared `VARCHAR(4)`. The value `'bitcoin'` is **7 characters**. **SQLite accepted it and stored it whole** (`SELECT pm, length(pm)` → `('bitcoin', 7)`) — SQLite does **not** enforce a declared `VARCHAR` width. **Postgres does**: `VARCHAR(4)` rejects a 7-character value with `ERROR 22001 — value too long for type character varying(4)`. So:
>
> - **On SQLite (dev):** a bill with `payment_method = 'bitcoin'` **is written and committed.**
> - **On Postgres (prod):** the same write **is refused.**
>
> **The identical code path succeeds in development and fails in production.** That is the same dev/prod divergence shape as feature **411** (money precision) and feature **437** (fractional `qty_delta`) — but on a column nobody has looked at, because **the enum's members all happen to fit** and so the width was never the visible problem.
>
> **Why this matters concretely.** A ledger row with `reason='gift'` is **not** a `StockReason`. Feature **432** owns the *sign* of `qty_delta` against its `reason` — and its `REASON_SIGN` mapping is a `dict[StockReason, int]` with **five** keys. A row with `reason='gift'` is **not in the mapping**, so the sign check has **no opinion about it**; the row passes the sign rule and lands in the ledger **forever**, because the ledger is append-only. An `order_item` with `status='cooked'` is a status **outside the kitchen board's vocabulary** — the board's `ItemStatus` has `new / preparing / ready / served / cancelled`, and a row in `'cooked'` matches **none** of them, so it renders as a line the cook cannot act on. And `app_user.role='owner'` is a role that **no capability check can grant**, because feature **403**'s `can()` maps exactly the three declared `UserRole` members — a fourth role is **silently unprivileged**, or silently privileged, depending on how the lookup is written.
>
> **Boundary — this is NOT feature 404 and NOT feature 403.**
> - **404** owns `CHECK` constraints on the **silent-corruption** columns (`stock_entry.qty_delta` and the **money** columns). Its *Out of scope* says verbatim: *"**Every column.** Constraints go where corruption is **silent**. A `VARCHAR` column that accepts a longer string is a different (and **much less dangerous**) problem."* **So 404 explicitly excludes the `VARCHAR` columns — this feature is that excluded problem.**
> - **403** owns the role **policy** (which chat maps to which role, what a role may do). Its *Adjacent work* says verbatim: *"**Does not touch `AppUser` or the bot.**"* **So 403 does not constrain `AppUser.role`'s value set — this feature does.**
> - **432** owns the **sign** of `qty_delta` against its `reason`, and explicitly says *"**Any change to `StockReason`'s members.** Adding, renaming or removing a reason is feature **421**'s business."* **This feature does not add, rename or remove any member — it constrains the column to the members that exist.**
> - **437** owns the **type** of `qty_delta`. **Different column, different rule.**
>
> **The three extra checks, answered explicitly** (the coverage-sweep contract requires all three):
> - **(a) Charter §3.2 non-goals?** **No.** This is a **constraint on existing columns**, not a new capability. §3.1's *"role-based via chat_id allowlist"* and §3.3's *"current stock is derived from entries"* both depend on the enum values being what they say.
> - **(b) Already an open owner question?** **No.** 403's open question is *"which chat id maps to which role"*; 432's is *"what is the sign"*; 404's is *"where do constraints go"* (and it has already answered it — **not here**); 437's is *"can a quantity be a fraction"*.
> - **(c) Covered under different words?** **No.** A corpus-wide grep over **474 feature contracts + 440 HANDOFFs** for `VARCHAR` membership, for *"value too long"*, for *"string_data_right_truncation"*, for *"Postgres rejects"*, for *"SQLite does not enforce length"*, for *"not a member"*, and for *"invalid enum"* returned **zero hits** on every phrasing except the word `allowlist` (44 files, all about feature 403's policy) and the word `enum` in the sense of *the Python class*.
>
> **Corroboration from a second in-window source (not picked).** `ahmedgaboelnaga/n8n-restaurant-order-inventory-automation` (MIT ✓ §3.2, **★1/⑂0 = NO traction evidence in either direction**, created **2026-10-14** AND pushed **2026-10-14** = **IN-WINDOW BY BOTH FIELDS**, README read in full, 6,770 B) — verbatim, from its *Required Google Sheets* section:
>
> > *"Column headers must match exactly (**case-sensitive**)."*
>
> and from its setup notes:
>
> > *"Row 2 must be the first data row in the Stock sheet (**the update nodes currently target `row_number: 2`**)."*
>
> A system whose column headers must match **exactly, case-sensitively**, and whose update nodes address a row by its **fixed position**, has had to answer *"what happens when the value in a constrained column is not one of the allowed ones?"* — and answered it **by construction**, in the sheet's typed columns. LE31 answers the same question **with nothing at all**.
>
> **Corroboration from a third in-window source (not picked).** `ahmedgaboelnaga/…` aside, `ycy-ui/DineReserve` (MIT ✓ §3.2, PHP, created 2026-10-06, pushed 2026-11-04, ★1) — a self-hosted restaurant booking system. **Read in full; no claim is made from it beyond its existence as an in-window MIT-licensed reference.** Recorded.

## Goal

Make every one of LE31's enum columns **mean what its Python enum says**, at the database — so that a value outside the enum cannot be written, and so that **SQLite and Postgres agree on whether a write is legal**.

**The single sentence this feature exists to make true:** *a column declared as an enum is a column whose value set is known — and LE31's database does not know it.*

Two concrete outcomes:

1. **`Bill.payment_method` cannot hold `'bitcoin'`, `'CASH'` or `'cashx'`; `OrderItem.status` cannot hold `'cooked'`; `StockEntry.reason` cannot hold `'gift'`; `AppUser.role` cannot hold `'owner'`.** Each is refused by the database.
2. **The dev/prod divergence disappears.** A value that SQLite refuses must be refused by Postgres **for the same reason** — not because one engine happened to enforce a width and the other did not.

## Scope

**In scope (v1):**

- **One `CHECK` constraint per enum column**, stating the membership:
  - `bill.payment_method IN ('cash','card')`
  - `order_item.status IN ('new','preparing','ready','served','cancelled')`
  - `stock_entry.reason IN ('initial','sale','waste','restock','sold_out')`
  - `app_user.role IN ('server','cook','manager')`
  - `table_.status IN ('free','seated','ordered','billed','dirty')` — **see *Open questions* 1; `table_` has no `status` column today.**
- **The constraints are generated from the Python enum**, not hand-written, so that **adding a member to the enum and forgetting the constraint is impossible** — see *Data model*.
- **One regression test** per column, asserting the invalid value is **rejected by the database** (not by the ORM).
- **A recorded statement** of the SQLite/Postgres divergence this closes, appended to feature **404**'s *Adjacent work* (404 owns the constraint mechanism; it excluded the `VARCHAR` columns).
- One row in `INDEX.md`'s "Active feature pipeline" table.

## Out of scope (v1)

- **Any change to the enum's members.** Adding, renaming or removing a member is feature **421**'s business (the reversal/correction member) and, for `StockReason`, feature **419**'s (the `sold_out` withdrawal). **This feature constrains the column to the members that exist today; it does not change the set.** **This is the same boundary feature 432 states.**
- **Any write path.** No selling router, no `/sold_out` command, no bot handler. **The defect is latent** — `StockEntry(` is constructed **zero** times outside its own class declaration, and the only `Visit` write in the whole backend is `backend/app/routers/tables.py` line 51.
- **The `CHECK` constraints on the money and quantity columns.** Feature **404**. **This feature does not touch `qty_delta` or any money column.**
- **The `qty_delta` type rule.** Feature **437**.
- **The role policy.** Feature **403** — which chat id maps to which role and what a role may do. **This feature does not decide policy; it stops the column from holding a role that is not in the policy.**
- **The `reason`/`qty_delta` sign rule.** Feature **432**. **Different column-pair, different rule; same PR is fine.**
- **The `AppUser.role` read sites.** Feature **403**. **This feature does not add a read site.**
- **A migration.** §3.2's stated v1 policy is `init_db()`. There is no historical data to migrate: no `StockEntry` write path exists, and the only `Visit` write is the seat endpoint.
- **`STRICT` tables.** Feature **404** records this as a v2 decision. **The transferable item is the discipline, and the stack-agnostic implementation is `CHECK`, which works on both engines.**
- **Any `VARCHAR` width change.** **See *Open questions* 2** — widening `payment_method` is a *product* decision (does LE31 take `wallet`? `udhaar`?) and **is not made here.**

## Description

### What the database accepts today

| Table | Column | Declared | Members | Longest | `CHECK` count |
|---|---|---|---|---|---|
| `bill` | `payment_method` | `VARCHAR(4)` | `cash`, `card` | 4 | **0** |
| `order_item` | `status` | `VARCHAR(9)` | `new`, `preparing`, `ready`, `served`, `cancelled` | 9 | **0** |
| `stock_entry` | `reason` | `VARCHAR(8)` | `initial`, `sale`, `waste`, `restock`, `sold_out` | 8 | **0** |
| `app_user` | `role` | `VARCHAR(7)` | `server`, `cook`, `manager` | 7 | **0** |
| `table_` | *(no column)* | — | `free`, `seated`, `ordered`, `billed`, `dirty` | 5 | **0** |

**Every member fits its column exactly.** That is why this has never surfaced: **the declared width is the longest member's length, so a *valid* value always fits.** The width is therefore doing no work at all — it is a coincidence of the member names, not a constraint.

### The four writes the parent performed (by execution)

```
INSERT INTO bill         (..., payment_method) VALUES (..., 'bitcoin')   -> stored
INSERT INTO order_item   (..., status)         VALUES (..., 'cooked')   -> stored
INSERT INTO stock_entry  (..., reason)         VALUES (..., 'gift')     -> stored
INSERT INTO app_user     (..., role)           VALUES (..., 'owner')    -> stored
```

and, through the **ORM**:

```python
Bill(..., payment_method="bitcoin", ...)   # a plain str, not PaymentMethod
# -> committed; SELECT payment_method returned 'bitcoin'
```

**SQLModel does not validate a `str` against a `str, Enum` annotation on write.** (It does validate on *serialisation* to a response model in some configurations, but a **write** is a different path — and there is no write path yet, so **nothing is validating anything**.) This matters: **the Python enum is documentation, not a constraint**, and the ORM is not a backstop.

### The dev/prod divergence, stated precisely

| | SQLite (dev) | Postgres (prod) |
|---|---|---|
| `payment_method = 'bitcoin'` (7 chars in `VARCHAR(4)`) | **accepted, stored whole** | **rejected** — `ERROR 22001: value too long for type character varying(4)` |
| `payment_method = 'CASH'` (4 chars, wrong case) | **accepted** | **accepted** (length fits; membership is not checked by either) |
| `status = 'cooked'` | **accepted** | **accepted** |

**Two of the three diverge between engines; the third is accepted by both.** The parent's execution confirmed the SQLite side directly (`SELECT pm, length(pm)` → `('bitcoin', 7)`).

**The generalisation, stated once:** SQLite treats a declared `VARCHAR(n)` as a *hint*; Postgres treats it as a *limit*. **Any LE31 column whose declared width is exactly the longest legal value is a column where the width is the ONLY thing that differs between the two engines — and the width only bites for values that are illegal anyway.** So the width is a **poor** enforcement mechanism and a **good** accident: it happens to reject the worst case in Postgres while silently accepting it in SQLite.

**The correct enforcement is membership, and membership is portable.** `CHECK (payment_method IN ('cash','card'))` behaves identically on both engines — and it rejects `'CASH'` too, which the width never would.

### Why this is a *different* shape from the four already-filed enum-adjacent defects

| Filed | The shape | What it fixes |
|---|---|---|
| **404** | a value of the **wrong type** in a numeric column | `SUM(qty_delta)` returns `0.0` for text, so a corrupt row reads as **sold out** |
| **411** | a money value with **too many decimals** | `Decimal('12.345')` is silently coerced on Postgres and silently stored on SQLite |
| **437** | a quantity with a **fraction** | `qty_delta` is `INTEGER` but SQLite stores `-0.5` as `REAL`, so `SUM()` returns a float |
| **432** | a delta whose **sign** contradicts its reason | `sale = +3` is accepted |
| **442 (this)** | a value that is **not a member of the enum** | the column is `VARCHAR` and says nothing about which values are legal |

**Each of the four fixes a value that is *of the right kind but wrong*. This fixes a value that is *of the wrong kind entirely* — and it is the only one whose failure is *silent in both engines* rather than divergent.**

## Data model

**No new columns. No new tables.** The change is **one `CHECK` constraint per enum column**, plus the mechanism that keeps them in sync with the Python enum.

### The constraints

```sql
-- bill
ALTER TABLE bill ADD CONSTRAINT ck_bill_payment_method
  CHECK (payment_method IN ('cash','card'));

-- order_item
ALTER TABLE order_item ADD CONSTRAINT ck_order_item_status
  CHECK (status IN ('new','preparing','ready','served','cancelled'));

-- stock_entry
ALTER TABLE stock_entry ADD CONSTRAINT ck_stock_entry_reason
  CHECK (reason IN ('initial','sale','waste','restock','sold_out'));

-- app_user
ALTER TABLE app_user ADD CONSTRAINT ck_app_user_role
  CHECK (role IN ('server','cook','manager'));
```

### Why the constraints are **generated**, not written

**The failure mode this feature exists to prevent is a constraint that drifts from its enum.** If the `CHECK` is a hand-written string, then adding `StockReason.correction` (feature **421**'s member) without editing the `CHECK` produces a schema where **the valid member is the invalid one** — and feature 421's whole point is to add a member. **So the constraint must be derived from the enum.**

```python
# backend/app/models.py
from sqlalchemy import CheckConstraint

def enum_check(column: str, enum_cls: type[Enum], name: str) -> CheckConstraint:
    """Build a CHECK constraint from an enum's MEMBERS, so the two cannot drift."""
    members = ", ".join("'%s'" % m.value for m in enum_cls)
    return CheckConstraint("%s IN (%s)" % (column, members), name=name)

class Bill(SQLModel, table=True):
    __tablename__ = "bill"
    __table_args__ = (enum_check("payment_method", PaymentMethod, "ck_bill_payment_method"),)
    ...
```

**The one-line proof that the two cannot drift:** `grep -c "IN ('cash','card')" backend/app/models.py` → **0**, because the literal never appears in source — it is built from `PaymentMethod`. **And the proof that a member cannot be added without the constraint following:** adding `correction = "correction"` to `StockReason` changes the generated `CHECK` on the next `create_all`, **with no other edit**.

**⚠️ The constraint must be regenerated whenever the enum changes, and the v1 migration policy is `init_db()`.** That is compatible: §3.2's v1 policy means **there is no data to migrate** — the schema is created fresh. **This feature's precondition is that no `StockEntry` has ever been written** (verified: `grep -rn "StockEntry(" backend/` returns exactly one hit, the class declaration).

### The application-layer twin — and why it is **not** the enforcement

The ORM accepts a bare `str` for an enum-annotated field. So the **application** should also validate:

```python
def validate_enum(column: str, value: str, enum_cls: type[Enum]) -> None:
    """Raise ValueError if `value` is not a member of `enum_cls`."""
    if value not in {m.value for m in enum_cls}:
        raise ValueError("%s must be one of %s" % (
            column, ", ".join(sorted(m.value for m in enum_cls))))
```

**⚠️ The `CHECK` is the enforcement; the Python check is the ergonomics.** The `CHECK` is what makes SQLite and Postgres agree. The Python check gives the caller a **useful error message** instead of an `IntegrityError`. **Both are wanted, and the report of which one actually fires is part of the HANDOFF.**

## Implementation steps

1. **Add `enum_check()`** to `backend/app/models.py` (or a small `backend/app/enums.py`), as above.
2. **Attach `__table_args__`** to `Bill`, `OrderItem`, `StockEntry`, `AppUser` — **one constraint each**.
3. **Verify the schema** by running `SQLModel.metadata.create_all` against a throwaway SQLite file and reading `PRAGMA table_info` / `sqlite_master.sql` to confirm **four** `CHECK` constraints exist where there were **zero**.
4. **Add the application-layer validation** to the seat endpoint's write path and to whatever ledger write path feature **421** creates — **or**, if 421 has not landed, expose it and leave the call site, recording that in the commit message.
5. **Add the regression tests** `backend/tests/test_enum_membership.py`:
   - `Bill(payment_method='bitcoin')` → **rejected by the database** (assert the `IntegrityError`, not an application-level `ValueError`);
   - `OrderItem(status='cooked')` → **rejected**;
   - `StockEntry(reason='gift')` → **rejected**;
   - `AppUser(role='owner')` → **rejected**;
   - `Bill(payment_method='cash')` → **accepted**;
   - `StockEntry(reason='initial')` → **accepted**.
   **Each test must assert the DATABASE refused the write**, so that a passing test cannot be produced by an application-level check alone.
6. **Record the divergence closure** — one line in feature **404**'s *Adjacent work*, saying *"the `VARCHAR` enum columns are constrained by feature 442."*
7. **Verify the divergence is closed** by re-running the parent's probe: the same raw `INSERT ... 'bitcoin'` that SQLite accepted before must now be **refused**, and the ORM write of `payment_method="bitcoin"` must be **refused**.

## Telegram interaction if any

**None.** This feature adds no Telegram surface.

**Note for the surfaces that will read these columns:** feature **403**'s `can(role, capability)` maps exactly the three declared `UserRole` members. **After this feature, `AppUser.role` can only hold one of those three** — so `can()` can be called without a `None` check for an unknown role. **That is the ergonomic win, and it is why the constraint belongs at the database rather than only in `can()`.**

## Dependencies

- **Feature 404** (`le31-sqlite-tables-not-strict…`) — **the sibling that owns the `CHECK`-constraint mechanism and the dev/prod-divergence theme.** Its *Out of scope* explicitly excludes the `VARCHAR` columns; **this feature is that excluded problem.** **Ordering: independent.** 404's constraints and 442's constraints are on **different columns** and can land in either order or together. **If both land in one PR, the two `CHECK` sets must not be conflated** — 404 owns the *silent-corruption* columns, 442 owns the *enum-membership* columns.
- **Feature 421** (`le31-stockentry-append-only-linter-rule…`) — **owns the `StockReason` reversal member.** **⚠️ ORDERING: 421 adds a member to the enum; this feature's constraint is GENERATED from the enum, so the constraint follows automatically — provided the constraint is generated and not hand-written.** **If the constraint is hand-written, 421 and 442 conflict.** **This is the reason the generation mechanism is in scope and the literal `CHECK` string is not.**
- **Feature 403** (`le31-role-based-bot-allowlist…`) — **independent.** 403 owns the *policy*; this feature constrains the *column*. **403's `can()` gains a guarantee, and 403 does not need to change.**
- **Feature 432** (`le31-stockentry-reason-sign-coherence…`) — **independent.** Different rule, same column. **Same PR is fine; keep the two rules separate in code and in the HANDOFF.**
- **Feature 437** (`le31-quantity-is-a-count-not-a-measure…`) — **independent.** Different column.
- **Feature 411** (`le31-money-precision-guard…`) — **independent.** Different columns; **the sibling that shares the dev/prod-divergence theme.**
- **No new dependency.** The `enum_check()` helper uses only `sqlalchemy.CheckConstraint` and `enum.Enum`.

## Open questions

1. **`TableStatus` has no column.** The enum declares five members and `table_` has **no `status` column** — feature **388** owns adding one (*"a column plus a guard in the seat route"*), and feature **397** owns the *sold-out* state. **This feature does not add the column.** **When 388 lands, this feature's constraint generator must be attached to it — the generated constraint follows the enum, so it is a one-line attachment, but the ORDERING matters: 388 first, then this constraint.**
2. **⭐ Should `payment_method` gain members?** `VARCHAR(4)` fits `'cash'` and `'card'` exactly. The in-window sources show what a real POS accepts: `AlgoVyn/bikri` (MIT ✓, in-window, README read in full) lists *"take cash/card/**wallet**/udhaar"*. **`'wallet'` is 6 characters — it does not fit `VARCHAR(4)`.** **This is a genuine product decision and it is NOT made here.** The recorded position: **this feature constrains the column to the members that exist today**; if the owner later adds `wallet`, **the column width must change in the same PR** — and the generated `CHECK` will follow automatically, while the width will not. **Recorded, not decided.**
3. **Should the ORM be tightened instead of (or as well as) the database?** SQLModel's `str, Enum` field does not validate on write. Options: (a) `sa_column=Column(Enum(PaymentMethod, native_enum=False))` — a real SQL `ENUM` type, **but that is SQLite-incompatible** (`native_enum=False` still renders as `VARCHAR` + `CHECK` on SQLite and as a native `ENUM` on Postgres, which is **not** portable); (b) a `field_validator` on each field; (c) the `CHECK` alone. **The recommendation is (c) plus a shared application helper**, because (a) reintroduces a dev/prod divergence of its own and (b) does not protect against a raw SQL write. **This is the implementer's call and must be recorded in the code.**
4. **Should `DerivedTip.formula_version` be constrained too?** It is a free-text `VARCHAR` with a known set (`'v1'`), and the parent confirmed **no** constraint exists on it. **It is not an enum column** — it is a version string, and the set of future versions is open. **Recorded; not in scope.** Feature **420** (the tendered-vs-received tip semantics) and feature **415** (which writes `formula_version='v1'`) are the features that own it.
5. **What should the error look like on the surface?** A `CHECK` violation surfaces as an `IntegrityError`, not an HTTP 409. The seat endpoint is the only write site today and it returns `HTTPException(400, ...)` for its two existing checks. **The recorded position: the seat endpoint's own checks stay as they are (they are readable, they are feature 423's), and the `CHECK` is the backstop behind them.** Recorded for whoever builds the bills router.

## Why this matters

**A column that says it is an enum but accepts anything is a column that lies.** And LE31 has **five** of them.

The severity is not uniform, and saying so is part of the point:

- **`StockEntry.reason`** is the worst of the five, because **the ledger is append-only by charter.** A row with `reason='gift'` is written **once** and is **forever**. Feature **432**'s `REASON_SIGN` mapping has five keys and **no opinion** about `'gift'`, so the row passes the sign rule. Feature **404**'s constraints are on the *numeric* columns, so the row passes those too. **The ledger now contains a row whose meaning no feature can explain**, and no feature exists that can remove it.
- **`OrderItem.status`** is the second worst, because the kitchen board is a **state machine over five states** and a sixth value is a row that **matches none of them** — a fired ticket that the cook cannot act on and cannot dismiss.
- **`AppUser.role`** is third, because feature **403**'s `can()` is the authorisation primitive and it maps **exactly three roles**. A fourth role is either **silently unprivileged** (safe) or **silently privileged** (not safe), depending entirely on how the lookup is written — and **neither outcome is a designed one.**
- **`Bill.payment_method`** is fourth by corruption risk but **first by the dev/prod divergence**, because its declared width is **exactly** the length of its longest member and a longer illegal value is **accepted in dev and refused in prod**.

**Why it matters for the product, specifically.** LE31's pitch is *"the stock number is derived, and the tip is derived, and the bill is derived — so they are right."* Derivation is only as good as the **inputs**, and these five columns are the inputs to four of the derivations: `qty_remaining` reads the ledger's `reason`; the tip reads the bill's `payment_method` and `total_paid`; the kitchen board reads `status`; the capability check reads `role`. **A derived number computed over an unconstrained input is a number nobody has checked.** That is the same argument as features 404, 411, 432 and 437 — and this is the **fifth** column family that the argument reaches.

**Why the divergence is the sharpest part.** Feature **411** already established that LE31's SQLite/Postgres divergence is a *first-class* finding. This feature is the **same finding on a column nobody has looked at** — and it is worse in one respect: **404, 411 and 437 are all about NUMERIC columns, where SQLite and Postgres differ in *precision and type*.** This one is about a **string column, where they differ in whether the write is legal at all.** In dev, a bill with `payment_method='bitcoin'` **is a row**. In prod, **it is an exception.** The test suite runs on SQLite. **So the bug ships green and fails in production**, which is the most expensive possible failure order.

**The cost of getting it right.** One helper function, four `__table_args__` lines, one test file. Roughly **2–4 hours**, fully reversible (drop the four constraints). **And it has a second-order payoff: because the constraint is GENERATED from the enum, feature 421's forthcoming reversal member cannot break it.** A hand-written `CHECK` would have created a conflict between this feature and 421 within the same week.

## Adjacent evidence

- **`ahmedgaboelnaga/n8n-restaurant-order-inventory-automation`** — MIT ✓ §3.2, **★1/⑂0 = NO traction evidence in either direction**, n8n + Google Sheets + Telegram, created **2026-10-14** AND pushed **2026-10-14** = **IN-WINDOW BY BOTH FIELDS**, README read in full (6,770 B). Verbatim: *"Column headers must match exactly (**case-sensitive**)."* and *"Row 2 must be the first data row in the Stock sheet (**the update nodes currently target `row_number: 2`**)."* — **a system that must constrain its columns to an exact, case-sensitive set.** ⚠️ **Off-stack** (n8n + Sheets) — **vocabulary only, no code adopted.**
- **`AlgoVyn/bikri`** — MIT ✓ §3.2, **★1/⑂0**, TypeScript/Hono/Cloudflare/D1, created 2026-10-26, pushed 2026-11-04, README read in full (2,858 B). Verbatim: *"take cash/card/**wallet**/udhaar"* — **the in-window evidence that a real POS's payment-method set does not fit `VARCHAR(4)`.** Recorded as **Open question 2**. Off-stack (TypeScript) — vocabulary only.
- **`ycy-ui/DineReserve`** — MIT ✓ §3.2, PHP, created 2026-10-06, pushed 2026-11-04, ★1, README read in full (10,086 B). **No claim is made from it beyond its existence as an in-window MIT-licensed reference.** Recorded.
- **`thomas0903/tickertape`** — Apache-2.0 ✓ §3.2, Rust, created 2026-11-01, pushed 2026-11-03, ★3, README read in full (10,999 B). Its records carry *"a **schema id**"* — **the record names the schema its payload conforms to**, so a reader can tell what a value means. LE31's columns name their enum in Python but **not in the database**. Recorded; not picked.

## Adjacent work — recorded, NOT picked

One source artifact touching several invariants → **pick one, record the rest.**

| Rule (source) | LE31's owner | Disposition |
|---|---|---|
| *"Column headers must match exactly (case-sensitive)"* (n8n) | feature **431** (category canonicalisation — case-sensitive free text) | **Recorded.** 431 owns the *value normalisation*; this feature owns the *membership constraint*. |
| *"the update nodes currently target `row_number: 2`"* (n8n) | feature **385** (batch provenance) + **441** (ledger coherence) | **Recorded.** A write that targets a **fixed position** instead of a **keyed row** is the same *addressing* family. Not bundled. |
| *"take cash/card/wallet/udhaar"* (bikri) | **Open question 2** | **Recorded.** A product decision about `payment_method`'s members — **not** this feature's. |
| *"a **schema id**" per record (tickertape) | feature **413** (triggers) + this feature | **Recorded.** Not bundled. |
