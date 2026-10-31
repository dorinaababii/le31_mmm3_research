# Feature 411 — LE31's money has a declared precision but no enforced precision: `Decimal("12.345")` is silently coerced, never rejected

> **Pick A of Daily Research 2026-10-31 (93rd pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it has been named and left open for two passes.**
>
> `backend/app/models.py`, verbatim, all ten money fields:
>
> ```
> 90:    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
> 149:    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
> 163:    subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
> 164:    subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)
> 165:    total_due: Decimal = Field(max_digits=10, decimal_places=2)
> 166:    total_paid: Decimal = Field(max_digits=10, decimal_places=2)
> 177:    amount: Decimal = Field(max_digits=10, decimal_places=2)
> 188:    opening_float: Decimal = Field(max_digits=10, decimal_places=2)
> 189:    counted_cash: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
> 190:    variance: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
> ```
>
> `decimal_places=2` is a **column-type declaration**. It is **not a write-time constraint**, and LE31 has **no** validator, **no** `CheckConstraint`, **no** `quantize()` anywhere:
>
> ```
> $ grep -rnE "field_validator|model_validator|@validator|condecimal|conint" app/     → NO MATCHES
> $ grep -rnE "quantize|ROUND_|round\(|\.normalize\(" app/                           → NO MATCHES
> $ grep -rnE "CheckConstraint|UniqueConstraint|__table_args__" app/                 → NO MATCHES
> ```
>
> **The consequence is the interesting part:** on **Postgres** (production) `NUMERIC(10,2)` **rounds** the value silently on insert — no exception, no 4xx; on **SQLite** (the dev default, `backend/app/config.py:20`: `database_url: str = "sqlite:///./restaurant.db"`) SQLite **does not enforce `NUMERIC` affinity** and stores the value **as-is**. So the *same code* produces a *different stored number* in dev and in production, and **neither path tells anyone**.
>
> **The external instrument** was `rahulkumar96t/double-entry-ledger` (MIT, ★0, created 2026-10-30, pushed 2026-10-30 — in-window by both fields, all fields parent-verified via direct `GET /repos/`), whose README states, verbatim:
>
> > *"**Strict input**: floats, numeric strings and unknown fields are rejected, so `12.5` is never silently"*
> > *"Jackson is configured to reject floats and numeric strings rather than coerce them."*
>
> **Bucket: v1. Build verdict: `build`.** Evidence class: **OBSERVED** (LE31's own schema read directly on 2026-10-31; the absence of a guard established by grep over `backend/app/`).
>
> **This exact question was already raised, twice, and never filed.** Feature 373 (2026-10-24) records it as an unmade owner decision — *"Should LE31 add a fractional-value guard on money writes? The reference says yes. **This is the one unmade decision this pick proposes.** Cost is small (one Pydantic validator on the `Decimal` fields, or a SQL check constraint). **Unmade owner decision.**"* — and its *Why this matters* says the artifact *"made the parent look at LE31's own code, and the code was wrong."* **The look happened; the fix was never filed.** Feature 408 (tax rate) and feature 410 (money rule reconciliation) both concern *which number* the money should be — **neither is about whether an over-precise number is accepted.**

## Goal

Make LE31's money precision **enforced rather than declared**, so that a value which cannot exist in a euro-cent ledger is **rejected at the boundary** instead of being **silently coerced** — and so that **dev and production cannot disagree about what got stored**.

**The single sentence this feature exists to make true:** *LE31 refuses a money value it could not store exactly, the same way in dev and in production.*

Two concrete outcomes:

1. **`Decimal("12.345")` is rejected, not rounded.** Writing three decimal places to `MenuItem.unit_price`, `OrderItem.unit_price`, `Bill.*`, `DerivedTip.amount` or `Shift.*` must fail loudly, with the offending value named.
2. **One rule, one place, applied identically on SQLite and on Postgres.** The rule must not be a database-specific behaviour, because LE31's dev database is SQLite and its production database is Postgres, and today they disagree.

**What this is not:** this is not a change to *how money is represented*. LE31 uses `Decimal` and that stays. This is not the integer-cents-vs-`Decimal` charter conflict — see *Out of scope*. This is not the tax-rate question (feature 408) or the money-rule reconciliation (feature 410).

## Scope

**In scope (v1):**

- **One shared validation primitive** that answers a single question: *"is this `Decimal` exactly representable at the money precision LE31 uses?"* — with **one home**, not one copy per field.
- **Its application to the ten money fields** on `MenuItem`, `OrderItem`, `Bill`, `DerivedTip` and `Shift`.
- **A regression test** that proves an over-precise value is **rejected** (not rounded) on **both** database backends.
- **A record of the owner decision** on the boundary (see *Open questions*) — **recorded, not guessed.**

**Out of scope (v1):**

- **Any change from `Decimal` to integer cents.** `le31-conventions` §*Known conflicts* lists *"integer-cents versus `Decimal`"* as an unresolved charter conflict, and `le31-data` §40 says *"Follow the resolved explicit project decision."* **That conflict is not resolved.** This feature **works with the `Decimal` representation LE31 already has** and must not silently pre-empt the decision. **If the owner later chooses integer cents, this guard is replaced by a different guard — not by nothing.**
- **Any change to the *values* money should have.** The tax rate (feature 408) and the charter-vs-checklist money rules (feature 410) own that. **Do not merge.**
- **Any rounding policy for legitimate half-cent arithmetic.** If a computation legitimately produces a third decimal place (a 3-way split of a euro cent, a percentage), the rule below **rejects it** — and that is intentional. Rounding such a value is a *separate* decision with its own rule, and **this feature does not invent one.** See *Open questions*.
- **Any change to how amounts are *stored*.** The columns stay `NUMERIC(10,2)`. This feature changes **what is allowed in**, not what the database does.
- **A migration or Alembic.** §3.2's stated v1 policy is `init_db()`.
- **A `CheckConstraint` on the money columns *as the primary mechanism*.** A DB-level check is **valid** and may be added as a *belt-and-braces* second layer — but it cannot be the **only** layer, because it would be **enforced on Postgres and silently unenforced on SQLite**, which is exactly the dev/prod divergence this feature exists to remove. **The application-level guard is primary; a DB constraint is optional reinforcement.**
- **Anything about `Batch.qty_remaining`.** Feature 374.
- **Anything about the business day.** Feature 405.

## Description

### The defect, as observed in LE31's own code on 2026-10-31

**All ten money fields are `Decimal` and correctly typed.** `grep -c "decimal_places" backend/app/models.py` → `10`. There is **no float anywhere** — the only `float` hits are the docstring *"Money uses Decimal (never float) — exact arithmetic."* and a field *named* `opening_float` that is itself a `Decimal`. **The charter's money-float invariant is upheld. That part is fine.**

**What is missing is the enforcement of the precision.** `decimal_places=2` is passed to SQLAlchemy's `Numeric` type. It describes the column. It does not inspect what you hand it:

- **Postgres** — `NUMERIC(10,2)` coerces `12.345` to `12.35` (or `12.34`, depending on the rounding mode) **at insert time, silently**. No exception. The application never learns that a value was altered.
- **SQLite** — the dev default. SQLite gives `NUMERIC` a type affinity but **does not enforce the declared precision**; `12.345` is **stored as-is**. The application never learns anything, and the stored value is *different* from what production would have stored.

So the same code path produces **two different stored numbers** depending on the database, and in **neither** case is a human told.

### Why "it is only a rounding of one cent" is the wrong conclusion

The tempting dismissal is that a third decimal place is sub-cent noise. Three facts make it a real defect rather than cosmetic:

1. **It is not one cent. It is a silent change to the stored number.** A `unit_price` of `12.345` stored as `12.35` is a **price**, and a price that is not the price that was entered is a wrong number on the owner's menu. There is no record that the value was altered — the original is gone.
2. **The dev/prod divergence makes it unreproducible.** A bug that reproduces only on Postgres is a bug that the developer's own machine cannot reproduce. LE31's default dev database is SQLite (`backend/app/config.py:20`), so **the entire test suite runs on the path that does not enforce the rule**. A test suite that cannot see the production behaviour is not a test suite for this rule.
3. **The charter promises exactness.** `le31-conventions` §*Hard invariants*: *"Money: never use binary floats. **Preserve exact EUR values** and explicit tax/tip derivations."* "Preserve exact EUR values" is currently **not true of an over-precise input** — the value is not preserved, it is replaced.

### The external instrument

`rahulkumar96t/double-entry-ledger` (MIT, ★0/0⑂, Java, 319-line README, created 2026-10-30, pushed 2026-10-30 — in-window by **both** `created_at` and `pushed_at`; all fields parent-verified via direct `GET /repos/` at `/tmp/le31-daily-2026-10-31/gh/repos/rahulkumar96t__double-entry-ledger.json`) is a **double-entry ledger API** whose README is explicit that it **rejects rather than coerces**:

> L36 — *"**Strict input**: floats, numeric strings and unknown fields are rejected, so `12.5` is never silently"*
>
> L213 — *"Jackson is configured to reject floats and numeric strings rather than coerce them."*
>
> L121 — *"Amounts are integers in minor units (`10000` = 100.00 EUR)."*
>
> L18 — *"...the response includes the currency's minor units (EUR 2, JPY 0, KWD 3)"*
>
> L97 — *"`idempotency_records` | key, operation, SHA-256 of the canonical request, stored status, body and `Location`"*

**What transfers is one idea: a value that cannot be represented in the currency is *rejected at the boundary*, and the currency's precision is *named* rather than implied.** LE31 does not need double-entry, does not need Java, does not need integer minor units — **its representation choice is a separate, unresolved charter conflict.** What LE31 takes is the *rule shape*: **one named precision, checked once, at the boundary, identically on every backend.**

**What does NOT transfer:** the integer-minor-units representation, the `Idempotency-Key` machinery, the double-entry postings model, and the Java/Jackson stack. This is a **vocabulary** import, and the artifact's code-shape is **not adopted**.

### The shape of the failure being prevented

```
# Today, on Postgres:
MenuItem(name="Tiramisu", unit_price=Decimal("12.345"))
→ INSERT succeeds
→ stored unit_price = 12.35
→ no exception, no log, no record that 12.345 was ever entered

# Today, on SQLite (the dev default):
MenuItem(name="Tiramisu", unit_price=Decimal("12.345"))
→ INSERT succeeds
→ stored unit_price = 12.345
→ a number the production database would never store

# After this feature, on both:
MenuItem(name="Tiramisu", unit_price=Decimal("12.345"))
→ REJECTED, naming the value and the field
```

## Data model

**No new table. No new column. No schema change of any kind.**

This is a **validation** change on existing fields. The one piece of new code is a single module:

```python
# NEW FILE: backend/app/services/money.py
#
# One home for LE31's money-precision rule.
#
# The rule: a money amount must be exactly representable at the precision
# LE31 stores money at. "Exactly representable" means: converting the value
# to that precision and back yields the same value.
#
# Deliberately NOT derived from the SQLAlchemy column type. The column
# declaration (max_digits=10, decimal_places=2) describes what the DATABASE
# will hold; it is not a rule the APPLICATION enforces, and SQLite does not
# enforce it at all. The application rule must stand on its own so that dev
# (SQLite) and production (Postgres) behave identically.

from decimal import Decimal, InvalidOperation

#: The precision LE31 stores money at, in decimal places.
MONEY_PLACES = 2


class MoneyPrecisionError(ValueError):
    """Raised when a money amount cannot be represented exactly."""


def assert_exact_money(value: Decimal, places: int = MONEY_PLACES) -> Decimal:
    """Return `value` unchanged, or raise if it is not exactly representable.

    The check is deliberately arithmetic rather than a comparison against a
    rounded copy, so that it does not depend on the database's rounding mode:
    a value with more precision than `places` is rejected outright, and a
    value with exactly `places` (or fewer) passes through untouched.
    """
    if not isinstance(value, Decimal):
        raise MoneyPrecisionError(
            f"money must be a Decimal, got {type(value).__name__}"
        )
    # -value.as_tuple().exponent is the number of digits after the point.
    # A negative exponent means the value was written in scientific form
    # (e.g. 1E+2); treat its scale as 0 for the purposes of this check.
    exponent = value.as_tuple().exponent
    scale = -exponent if isinstance(exponent, int) and exponent < 0 else 0
    if scale > places:
        raise MoneyPrecisionError(
            f"money value {value} has {scale} decimal places; "
            f"LE31 stores money at {places} decimal places "
            f"and rejects values it cannot store exactly"
        )
    return value
```

**How it attaches to the fields.** The application-level guard must be attached in **one** place, not ten. Two candidate homes:

| Candidate | Assessment |
|---|---|
| Ten separate `@field_validator`s on `models.py` | **Rejected.** Ten copies of one rule, spread across five classes, is the shape this feature exists to avoid. A future eleventh money field would silently lack the guard. |
| One `Annotated` money type used by all ten fields | **Preferred.** `MONEY = Annotated[Decimal, AfterValidator(assert_exact_money)]` — one type, one rule, ten declarations that each say `MONEY`. Adding a field later uses the same type and is guarded by construction. |
| A Pydantic `model_validator` per class | **Rejected.** Same proliferation problem, and it cannot catch a value assigned outside validation. |

**The `Annotated` type is the recommendation.** The implementer may choose an equivalent single-home mechanism, but **must record the choice**, and **must not** ship ten hand-written validators.

**The optional DB-level reinforcement.** A `CHECK` constraint (Postgres) on the money columns is **valid and encouraged as a second layer** — but it is **not the primary mechanism**, for the SQLite reason above. If added, it must be documented as defence-in-depth, and the **application guard must still exist and must still be the one that fails on SQLite.**

**Note on `Decimal` scale vs value.** `Decimal("12.340")` has scale 3 but equals `12.34` exactly. Whether such a value is *accepted* (it is numerically exact) or *rejected* (its literal scale exceeds the money precision) is a **real design choice** with user-visible consequences — a JSON payload of `12.340` is a perfectly ordinary way to write twelve euro and thirty-four cents. **This is Open question 1.** The implementation above **rejects by scale**, which is the stricter reading; the implementer must implement whichever the owner chooses, and **must not silently pick the stricter one**.

## Implementation steps

1. **Create `backend/app/services/`** with `__init__.py`. **It does not exist today** — `ls backend/app/services` → *"cannot access … No such file or directory"*. (Feature 405 creates the same directory with `business_time.py`; if that feature has landed, **do not recreate it**, just add `money.py` beside it.)
2. **Write `backend/app/services/money.py`** exactly as specified above, **plus** the `MONEY` annotated type.
3. **Replace the ten field declarations** in `backend/app/models.py` to use `MONEY` instead of bare `Decimal`. **Keep `max_digits=10, decimal_places=2` on every one** — the column type is unchanged; only the *application-level* guard is added. **Do not remove, rename or re-type any column.**
4. **Write the regression tests** (below) **before** the guard exists and **watch them fail**.
5. **Apply the guard**, then **watch them pass**.
6. **Add the optional DB-level check** (Postgres only) and **document it as reinforcement**.
7. **Record the owner decisions** in `PROJECT_CHARTER.md` §*Quality bar* — one bullet stating the money precision rule and what happens to a value that violates it.
8. **Amend this feature file's *Data model* section** with the chosen mechanism and the chosen scale-vs-value answer.

**Do not**, at any point: rename a column, change a column type, add a table, add a migration, change how totals are computed, or introduce a rounding policy.

## Telegram interaction if any

**None.** This feature touches no bot command and no waiter surface.

**This is deliberate and worth stating explicitly:** LE31's cook bot has exactly **two** registered commands (`/start_today`, `/help`) out of the **six** its own docstring advertises (`backend/app/bot/cook_bot.py:9-14`), and the waiter surface is a **static mockup with zero `fetch()` calls** (`index.html`, 719 lines, `grep -c "fetch(" index.html` → `0`). There is therefore **no live surface through which an over-precise money value could currently reach the database** — no order router, no bill router, no payment path exists.

**That is exactly why this is cheap now and expensive later.** The moment the first money-bearing write path lands — the bill router, the payment-tip reconciliation, the end-of-day cash count — this guard becomes load-bearing, and by then it will be **one validator in a router** rather than **one type used by ten fields**. **Do this one before the first selling or billing feature lands.**

## Dependencies

- **`backend/app/models.py`** — the ten money field declarations on `MenuItem` (`:90`), `OrderItem` (`:149`), `Bill` (`:163-166`), `DerivedTip` (`:177`), `Shift` (`:188-190`).
- **`backend/app/config.py:20`** — `database_url: str = "sqlite:///./restaurant.db"` (the dev default that makes the SQLite/Postgres divergence live).
- **`backend/app/db.py:12-17`** — the SQLite engine setup.
- **`PROJECT_CHARTER.md`** — §*Quality bar* (where the money rule is recorded).
- **`le31-conventions`** — the money invariant and the seven-check gate.
- **`le31-v1-feature-pattern`** — the contract shape and the slicing rules.

**Sibling features to read but NOT merge:**

| Feature | Why it is adjacent but separate |
|---|---|
| **373** (`warung-pos`) | **The feature that named this problem.** Its Open question 1 is this exact decision. **This feature answers it** — 373 stays as the vocabulary reference. |
| **408** (tax rate) | Owns *which number* the tax is. Not whether an over-precise number is accepted. |
| **410** (money rule reconciliation) | Owns *which rule* computes the total. Not precision enforcement. |
| **391** (shift variance) | Owns the cash-variance derivation. May produce a half-cent; **its** problem, not this one's. |
| **374** (`qty_remaining`) | Stock, not money. |
| **405** (service day) | Business time, not money. **Shares `backend/app/services/`** — coordinate the directory, do not merge the features. |

## Open questions

**These are owner decisions. The implementer must implement the recorded default, and must not widen the decision.**

1. **Is the rule about *scale* or about *value*?** `Decimal("12.340")` — numerically identical to `12.34`, but written with three decimal places. **Recorded default: reject by scale** (the stricter reading). **Consequence of the default:** a JSON client that sends `12.340` gets a rejection. **If the owner prefers value-equality, the check becomes a round-trip comparison** — one line — but then `12.345` must still be rejected, and the implementer **must write the test that distinguishes the two readings before choosing.** **This is the one genuinely open decision in the slice.**
2. **What happens to a legitimately over-precise *computation*?** A 3-way split of a euro cent, or a percentage of a total, produces a third decimal place. **Recorded default: the guard rejects it, and the caller must decide what to do** — no rounding policy is invented here. **If the owner wants a rounding rule, that is a separate, separately-gated change** (and it interacts with feature 410's money-rule reconciliation).
3. **Is a DB-level `CHECK` constraint added?** **Recorded default: yes, as a second layer, on Postgres only** — with the application guard remaining primary and remaining the one that fails on SQLite. **Adding it must not be described as the fix**, because on SQLite it is not.
4. **Does the integer-cents-vs-`Decimal` charter conflict get resolved by this slice?** **Recorded default: no.** This feature is deliberately orthogonal to it. **If the owner resolves that conflict toward integer cents, this guard is replaced, not removed.**

## Why this matters

Because **it is the last open decision from feature 373 that was never filed**, and because **the answer is "the number can differ between dev and production, silently."**

Every other LE31 first-party finding of the last week has been about a *missing* concept — no business day (405), no derived stock (374), no sold-out state (397), no table-status column (388), no bot allowlist (403). **This one is different: every concept is present, every type is right, and the guard that would make the type *mean* something is absent.** LE31 says "money is `Decimal` at two places" and then never checks that the value it accepted actually has two places.

The failure mode is the quietest kind. It is not an exception; it is a number that changes on the way to the database and no one is told. And the test suite — which runs on SQLite, the one backend that does not enforce the rule — **cannot see it**.

The fix is small: **one type, one rule, ten fields, two tests.** It should land now, while it is still inert — there is no money-bearing write path yet, so there is nothing to migrate and no behaviour to change. **After the bill router lands, the same fix costs more and lands later.**
