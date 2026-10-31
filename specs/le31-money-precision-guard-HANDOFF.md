# HANDOFF — 411-le31-money-precision-guard

**Status**: **build** (v1, first-party defect in LE31's own schema)
**Date**: 2026-10-31
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/411-le31-money-precision-declared-not-enforced-decimal-12-345-is-silently-coerced-on-postgres-and-silently-stored-on-sqlite-dev-and-prod-disagree-v1-money-precision-guard.md`
**LE31 feature gate verdict**: **build** — all seven checks pass. Evidence class **OBSERVED** (LE31's own `backend/app/models.py` read directly on 2026-10-31; the absence of any guard established by grep over `backend/app/`). **This is not a vocabulary artifact — it produces code.**

## Trigger policy

This is a **build** contract. The external coding agent **should** implement it.

**Before writing any code**, the agent must:

1. Load the active feature file, this handoff, and the parent report (`/opt/data/le31-daily-research-2026-10-31.md`).
2. Load **feature 373** (`warung-pos`) — **the feature that named this problem** and left it as an unmade owner decision. **Do not re-file it; answer it here.** Load **feature 408** (tax rate) and **feature 410** (money-rule reconciliation) — **both own a different money question.** **Do not merge any of the three into this slice.**
3. **Read the charter's own money statements** and confirm the *integer-cents-versus-`Decimal`* conflict is **still unresolved**. If it has been resolved, use the resolution. **If not, this slice works with the `Decimal` representation LE31 already has** and must not pre-empt it.
4. **Confirm the scale-vs-value decision is still open** (see *Frozen contract*). If the owner has since decided it, use the decision. **If not, implement the recorded default** and **leave the choice visible in the code and in the feature file.**

**Disambiguation**: this slice is about **whether a money value is allowed in at all**. It is **not** about which number the money should be (408, 410), **not** about stock quantities (374), **not** about the business day (405), and **not** about the integer-cents representation choice, which it deliberately leaves open.

## Frozen contract

**The one thing this contract exists to make true:** *LE31 refuses a money value it could not store exactly, the same way in dev and in production.*

**The module** — exactly this, in a new file `backend/app/services/money.py`:

```python
from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator

#: The precision LE31 stores money at, in decimal places.
MONEY_PLACES = 2


class MoneyPrecisionError(ValueError):
    """Raised when a money amount cannot be represented exactly."""


def assert_exact_money(value: Decimal, places: int = MONEY_PLACES) -> Decimal:
    """Return `value` unchanged, or raise if it is not exactly representable.

    The check is arithmetic, not a comparison against a rounded copy, so it
    does not depend on the database's rounding mode: a value with more
    precision than `places` is rejected outright; a value with exactly
    `places` (or fewer) passes through untouched.
    """
    if not isinstance(value, Decimal):
        raise MoneyPrecisionError(
            f"money must be a Decimal, got {type(value).__name__}"
        )
    exponent = value.as_tuple().exponent
    scale = -exponent if isinstance(exponent, int) and exponent < 0 else 0
    if scale > places:
        raise MoneyPrecisionError(
            f"money value {value} has {scale} decimal places; "
            f"LE31 stores money at {places} decimal places "
            f"and rejects values it cannot store exactly"
        )
    return value


MONEY = Annotated[Decimal, AfterValidator(assert_exact_money)]
```

**The ten field declarations** — change the *type* only. **Keep `max_digits=10, decimal_places=2` on every one**; the column type is unchanged.

| Model | Line (as of 2026-10-31) | Field |
|---|---|---|
| `MenuItem` | `models.py:90` | `unit_price` |
| `OrderItem` | `models.py:149` | `unit_price` |
| `Bill` | `models.py:163` | `subtotal_items` |
| `Bill` | `models.py:164` | `subtotal_tax` |
| `Bill` | `models.py:165` | `total_due` |
| `Bill` | `models.py:166` | `total_paid` |
| `DerivedTip` | `models.py:177` | `amount` |
| `Shift` | `models.py:188` | `opening_float` |
| `Shift` | `models.py:189` | `counted_cash` |
| `Shift` | `models.py:190` | `variance` |

**The single-home rule** — one `MONEY` type, ten declarations that use it. **Ten hand-written `@field_validator`s are rejected** by this contract: a future eleventh money field would silently lack the guard.

**The optional DB-level reinforcement** — a `CHECK` constraint on the money columns is **valid and encouraged**, but it is **not the primary mechanism**: it would be **enforced on Postgres and silently unenforced on SQLite**, which is the exact divergence this slice exists to remove. **The application guard is primary and must be the one that fails on SQLite.** If a `CHECK` is added, document it as defence-in-depth.

**The `NULL`-free rule** — `MoneyPrecisionError` is a `ValueError` subclass, so Pydantic's `AfterValidator` will surface it as a **422 validation error** at any API boundary, naming the offending value and the field. **Do not catch it and coerce.**

**Anti-goals, stated so they are not drifted into:**

- **No change from `Decimal` to integer cents.** The charter conflict is unresolved; this slice is orthogonal to it.
- **No rounding policy.** A computation that legitimately produces a third decimal place is **rejected**, and the caller decides. **This feature does not invent a rounding rule** — that is a separate, separately-gated change interacting with feature 410.
- **No change to any column type, name, or table.** `NUMERIC(10,2)` stays.
- **No migration, no Alembic.** §3.2's stated v1 policy is `init_db()`.
- **No change to how totals are computed.** Features 408 and 410 own that.
- **Nothing about `Batch.qty_remaining`** (374) **or the business day** (405).

## Files to touch

| File | Change |
|---|---|
| `backend/app/services/__init__.py` | **NEW** (the package does not exist today). If feature 405 has landed, **do not recreate it** — add `money.py` beside `business_time.py`. |
| `backend/app/services/money.py` | **NEW.** `MONEY_PLACES`, `MoneyPrecisionError`, `assert_exact_money()`, `MONEY`. |
| `backend/app/models.py` | **CHANGE THE TYPE** of the ten fields listed above from `Decimal` to `MONEY`. **Keep `max_digits=10, decimal_places=2` on each.** **Do not touch any other field, class, or timestamp.** |
| `backend/tests/test_money_precision.py` | **NEW.** The regression tests below. |
| `PROJECT_CHARTER.md` | **ADD** one bullet in §*Quality bar* stating the money-precision rule and what happens to a violating value. |
| `features/411-…md` | **AMEND** the *Data model* section to record the chosen mechanism and the chosen scale-vs-value answer. |

**Any other file is out of scope.** If the agent believes another file must change, that is a **new finding** — surface it, do not silently widen the slice.

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — the seven-check feature gate and the hard invariants (charter §3.2 fixed stack and surfaces, §3.6 money, business-time invariant).
- `le31-v1-feature-pattern` — the canonical contract shape and the slicing rules.
- `le31-research` — the source-of-truth discipline behind the artifact quotes.
- `le31-handoff-spec` — the frozen-contract discipline.
- `development` — the generic code pipeline (specify → plan → tasks → implement → independent review).

The agent must **NOT** load `le31-feature-pipeline` — the slice is already in the pipeline.

## Mandatory inputs

- **Active feature**: `features/411-le31-money-precision-declared-not-enforced-…-v1-money-precision-guard.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-31.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-31/`
  - `gh/repos/rahulkumar96t__double-entry-ledger.json` — direct `GET /repos/` (HTTP 200)
  - `gh/readmes/rahulkumar96t__double-entry-ledger.md` — README, 319 lines, raw text
  - `meta/parent_verified.json` — the parent's independently re-derived headline figures
- **LE31 source of truth**:
  - `backend/app/models.py` — the ten money declarations (`:90`, `:149`, `:163-166`, `:177`, `:188-190`)
  - `backend/app/config.py:20` — `database_url: str = "sqlite:///./restaurant.db"` (the dev default that makes the divergence live)
  - `backend/app/db.py:12-17` — the SQLite engine setup
  - `grep -rnE "field_validator|model_validator|condecimal|quantize|CheckConstraint" backend/app/` → **NO MATCHES** (the evidence that the guard does not exist)
  - `grep -rn "\.update(\|delete(\|session.delete" backend/app/` → **NO MATCHES** (nothing mutates anything today)
- **Charter** — §*Quality bar* (money) and §8 *Verification protocol* — `PROJECT_CHARTER.md`
- **Sibling features to read but NOT merge**: **373** (the feature that raised this question — *answer it here*), 408 (tax rate), 410 (money-rule reconciliation), 391 (shift variance), 374 (`qty_remaining`), 405 (service day — **shares `backend/app/services/`**; coordinate the directory, do not merge the features).

## Verification protocol reference

Follow **`PROJECT_CHARTER.md` §8 Verification protocol** steps 1–11, with these slice-specific additions:

**Add these regression tests:**

```python
def test_three_decimal_places_is_rejected():
    with pytest.raises(MoneyPrecisionError):
        assert_exact_money(Decimal("12.345"))


def test_two_decimal_places_passes_through_unchanged():
    v = Decimal("12.34")
    assert assert_exact_money(v) is v


def test_one_decimal_place_passes_through_unchanged():
    v = Decimal("12.3")
    assert assert_exact_money(v) is v


def test_exact_eur_passes():
    assert assert_exact_money(Decimal("12.34")) == Decimal("12.34")


def test_float_is_rejected_not_coerced():
    with pytest.raises(MoneyPrecisionError):
        assert_exact_money(12.345)  # type: ignore[arg-type]
```

**If the owner chose value-equality over scale**, the third test becomes the discriminator and **must be written first**:

```python
def test_three_trailing_zeros_is_accepted_under_value_equality():
    assert assert_exact_money(Decimal("12.340")) == Decimal("12.34")
```

**The assertions must be against literal values, not against a re-implementation of the same expression.** A test that recomputes the answer the way the code does proves nothing.

**End-to-end acceptance path** (per `le31-v1-feature-pattern`): constructing a `MenuItem` with `unit_price=Decimal("12.345")` **must** raise a validation error naming the value, **through the real Pydantic model**, not by calling the helper directly. **Exercise the real model** — per `le31-conventions` common pitfall 4, *"tests pass" is not the acceptance path.*

**The dev/prod divergence test** — the load-bearing one. The same over-precise value must be rejected **on SQLite and on Postgres identically**. If the agent adds the DB-level `CHECK`, the test must show: on SQLite the **application guard** rejects it (the `CHECK` is absent or inert), and on Postgres **both** reject it. **A test that only exercises one backend does not prove the slice's central claim.**

**Must-fail-first discipline**: write `test_three_decimal_places_is_rejected` **before** the guard exists and **watch it fail**, then implement, then watch it pass. A test that has only ever passed proves nothing.

## Rollback path

**Fully reversible, and deliberately so.**

1. **Revert the commit.** The feature is one commit adding one module, changing ten type annotations, adding one test file and one charter bullet.
2. **Or, piecewise:** delete `backend/app/services/money.py`, revert the ten field types to `Decimal`, revert the charter bullet. **No data is lost** — no column was added, renamed, re-typed or rewritten; **no existing row is touched.**
3. **No migration to undo.** §3.2's stated v1 policy is `init_db()`. A dev database is recreated from the schema; a production database is unaffected, because the **column types are unchanged** — only the application-level validation differs.
4. **What remains safe if removed:** every existing behaviour. **Nothing in LE31 writes money today** — there is no bill router, no payment path, no end-of-day cash count. **The slice is therefore inert on its own**, which is precisely why it is cheap and why it must land **before** the first money-bearing write path.
5. **What would break if it were removed:** nothing, **today**. **That is the risk.** The slice exists to be in place before the write path, not because it fixed a live bug.

**Retained data:** none. The feature **writes no rows and reads no rows.**

## Sign-off gap

**Two owner decisions are open, and the agent must implement the recorded defaults rather than guess beyond them:**

1. **Is the rule about *scale* or about *value*?** `Decimal("12.340")` is numerically identical to `12.34` but is written with three decimal places. **Recorded default: reject by scale** (the stricter reading). **Consequence: a JSON client sending `12.340` gets a rejection.** If the owner prefers value-equality, the check becomes a round-trip comparison — one line — but `12.345` must still be rejected, and **the test that distinguishes the two readings must be written first.**
2. **What happens to a legitimately over-precise *computation*?** A 3-way split of a euro cent, or a percentage of a total, produces a third decimal place. **Recorded default: the guard rejects it and the caller decides — no rounding policy is invented here.** If the owner wants a rounding rule, that is a separate, separately-gated change.

**Also open, and explicitly not decided here:** whether a DB-level `CHECK` constraint is added (**recorded default: yes, as a second layer only**) and whether the **integer-cents-versus-`Decimal`** charter conflict gets resolved by this slice (**recorded default: no — it is deliberately orthogonal**).

**The agent must not widen either decision.** If the implementation seems to require a different answer, that is a **finding to surface**, not a choice to make.

## Handoff summary

LE31 declares its money as `Decimal` at two decimal places in **ten** places — `backend/app/models.py:90, 149, 163-166, 177, 188-190` — and **enforces nothing**. `grep -rnE "field_validator|model_validator|condecimal|quantize|CheckConstraint" backend/app/` → **no matches**. `decimal_places=2` is a *column-type declaration*, and the two backends treat it differently: **Postgres** (`NUMERIC(10,2)`) **silently rounds** `12.345` to two places on insert; **SQLite** — LE31's dev default (`config.py:20`) — **does not enforce `NUMERIC` affinity** and stores `12.345` **as-is**. **The same code stores a different number in dev than in production, and neither path raises.**

The failure is quiet by construction: no exception, no log, no record that the value was altered. And the whole test suite runs on the one backend that does not enforce the rule, so **it cannot see the production behaviour**. `le31-conventions` promises *"Preserve exact EUR values"* — for an over-precise input, that promise is currently false.

The external artifact `rahulkumar96t/double-entry-ledger` (MIT, in-window by both dates) is the instrument: *"**Strict input**: floats, numeric strings and unknown fields are rejected, so `12.5` is never silently"* and *"Jackson is configured to reject floats and numeric strings rather than coerce them."* **Its representation (integer minor units), language (Java) and domain (double-entry) are not adopted** — **its rule shape is**: one named precision, checked once, at the boundary, identically on every backend.

The fix is small and should land now, while it is still inert: **one type used by ten fields, one module, two tests — one of which runs the same over-precise value against both backends.** **Do this before the first selling or billing feature lands.**
