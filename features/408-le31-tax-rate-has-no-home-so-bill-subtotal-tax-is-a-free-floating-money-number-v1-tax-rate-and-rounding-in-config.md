# Feature 408 — LE31's tax rate has no home, so `Bill.subtotal_tax` is a free-floating money number

> **Pick A of Daily Brainstorm 2026-10-30 (90th brainstorm pass).** **FIRST-PARTY, and the defect is in LE31's own source and LE31's own charter** — not inferred from a third-party repo.
>
> `PROJECT_CHARTER.md` §7 Quality bar, verbatim:
>
> > - **Money is `Decimal`, never `float`.** SQLModel fields with `max_digits=10, decimal_places=2`.
> > - **Money sums use `Decimal` arithmetic.** No `float(qty * price)` anywhere.
> > - **No magic numbers.** Tax rate, tip rounding rules, buffer factors — all in `config.py` or `services/`.
>
> `backend/app/config.py` (the whole file is 31 lines) declares exactly nine settings:
>
> ```python
> app_name, debug, secret_key, database_url,
> telegram_bot_token, telegram_allowed_user_ids,
> llm_api_key, llm_model, llm_base_url
> ```
>
> **There is no tax rate. There is no rounding rule. There is no buffer factor.** `backend/app/services/` **does not exist** — `ls backend/app/` returns `bot/`, `routers/` and nothing else.
>
> And `backend/app/models.py` stores the tax as a **number with no rate behind it**:
>
> ```python
> class Bill(SQLModel, table=True):
>     subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
>     subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)
>     total_due: Decimal = Field(max_digits=10, decimal_places=2)
>     total_paid: Decimal = Field(max_digits=10, decimal_places=2)
> ```
>
> **The charter names the tax rate three times and never puts one anywhere.** §3.1 In scope: *"**Flat tax** (single rate, e.g. 10%)."* §3.3 Open scope question: *"**Tax** — flat 10%? Per-category? Per-item?"* §3.3 Defaults: *"…EUR, **flat 10% tax**, tablet UI, no service charge."* §11 Sign-off: *"The defaults in section 3.3 … unless the user overrides."*
>
> **Evidence class: OBSERVED** (every claim below is a reproducible command against LE31's own tree, or an execution against LE31's own schema). Confidence: **high** — the defect is a missing file section, not an inference.
>
> **Bucket: v1.** The need is a §3.1 in-scope v1 requirement. **Build verdict: `build`.**

## Goal

Give LE31 a **single, explicit home for the tax rate and the money rounding mode** — `config.py` — so that `Bill.subtotal_tax` is a **derived** number whose derivation is reproducible from the stored data, instead of a number a caller must supply from somewhere undefined.

## Scope

- Add a tax-rate setting to `backend/app/config.py`.
- Add an explicit money-rounding-mode setting to `backend/app/config.py`.
- Make the **derivation** of `Bill.subtotal_tax` and `Bill.total_due` reproducible from `subtotal_items` and the configured rate.
- Record enough on the bill row that a later reader can reconstruct which rate and which rounding mode produced the stored tax.

## Out of scope (v1)

- **Per-category or per-item tax rates.** The charter's §3.3 default is flat 10%; per-category is an *open owner question*, not a defect. This feature ships the **flat-rate mechanism**; the rate itself is configurable so the owner can change it without a schema change.
- **Service charge.** Feature 05 lists it as a separate open question (*"in scope for v1? (Common in EU restaurants… Decide before coding.)"*). Not decided here.
- **Discounts / promo codes.** Feature 05 recommends punting; not decided here.
- **A `Payment` table.** Feature 391 owns the money-edge and the `Shift`↔`Payment` link. This feature does not touch it.
- **`CHECK` constraints on the money columns.** Feature 404 owns the column-level *type* guards (`x = round(x, 2)`, `typeof(x) = 'integer'`). This feature adds the **cross-column and configuration** guards that 404 does not cover. See *Adjacent work* below.
- **Changing `Decimal` to integer minor units.** Feature 373 records the integer-money pattern as a vocabulary reference; LE31's `Decimal` choice is not being changed here.

## Description

### The defect, precisely

`Bill.subtotal_tax` is a **stored** `Decimal`. To compute it, a caller needs (a) a rate and (b) a rounding mode. **LE31 has neither.** There is no `tax_rate` field, no `Settings.tax_rate`, no constant, and no `services/` module in which a derivation could live.

The consequence is that the tax line is **whatever the caller passed in**. It is not checked against any rate, and it is not checked against the other money columns on the same row.

### What was proven by execution, not by reading

The probe (`_bs_probe_money2_2026-10-30.py`, re-runnable — see *Verification* below) builds **LE31's real schema** with `SQLModel.metadata.create_all` against a throwaway SQLite file and then poisons it.

**Finding 1 — the rounding mode is a real fork, and it changes a stored money value.**

For a flat 10% rate, four entirely realistic restaurant totals produce a product whose third decimal digit is non-zero:

```
items=12.45   raw=1.2450    HALF_UP -> 1.25   DOWN -> 1.24   HALF_EVEN -> 1.24   DIVERGES
items=7.35    raw=0.7350    HALF_UP -> 0.74   DOWN -> 0.73   HALF_EVEN -> 0.74   DIVERGES
items=19.99   raw=1.9990    HALF_UP -> 2.00   DOWN -> 1.99   HALF_EVEN -> 2.00   DIVERGES
items=3.35    raw=0.3350    HALF_UP -> 0.34   DOWN -> 0.33   HALF_EVEN -> 0.34   DIVERGES
```

**4 of 4 diverge.** The stored tip then differs for an identical visible input:

```
items=12.45, total_paid=20.00
  mode=HALF_UP    tax=1.25   total_due=13.70   tip=6.30
  mode=DOWN       tax=1.24   total_due=13.69   tip=6.31
  mode=HALF_EVEN  tax=1.24   total_due=13.69   tip=6.31
```

**Same items, same amount paid, two different stored tips — because a rule that was never written was silently supplied by whichever `Decimal.quantize` call happened to be in the caller's head.**

**Finding 2 — the bill table accepts a tax and a total that contradict each other.**

```
ACCEPTED [total_due != items + tax]  bill=1  items=12.45  tax=0.00   total_due=999.99  tip=-979.99
ACCEPTED [free-floating tax]         bill=2  items=100.00 tax=7.77   total_due=107.77  tip=-87.77
```

`total_due` is a **third stored money column** and nothing forces it to equal `subtotal_items + subtotal_tax`. The database stored `999.99` and derived a tip of **−979.99** without complaint.

**Finding 3 — the tip cannot be audited back to its basis.**

`DerivedTip` has exactly three columns:

```
['bill_id', 'amount', 'formula_version']
```

**No tax column. No items column.** Feature 05's justification is explicit — *"**Auditable**: `tip = paid - items - tax` is provable from the data."* — and the auditability claim **does not hold**: the tip row carries the amount and nothing that says which tax it came from. `formula_version` is the constant string `"v1"`; it versions the *formula*, not the rate and not the rounding mode.

### The finding shapes (all five)

| Shape | Here |
|---|---|
| **(a) contradiction** | §7 says the tax rate lives in `config.py` or `services/`; **neither contains one**. |
| **(b) omission** | `Bill` has no rate-bearing column and no derivation site; `DerivedTip` has no tax column while its sibling `Bill` has `subtotal_tax`. |
| **(c) missing inverse edge** | `Bill.subtotal_tax` ↔ the rate that produced it: **the row points at nothing**. |
| **(d) undefined term** | *"tax rate"* — the charter says *flat 10%*, §3.3 asks *flat? per-category? per-item?*, and §7 says it lives somewhere; **nowhere defines what a tax rate is a function of** (items only? items + category? items + category + date?). |
| **(e) unenforced mechanism** | §7's mechanism is *"put it in `config.py`"*. The mechanism is a **file with nine unrelated settings in it**; there is no `config.py` section, no `services/` module, and **no test or assertion** that would notice if a rate were added and then used inconsistently. A written rule and a mechanism that cannot carry it. |

### The four audit shapes in ONE defect

This is the **fourth** pass to find all four classical shapes at once, and the **first** to add the fifth (§e) on top:

| Pass | Source artifact | Shape found | Domain |
|---|---|---|---|
| 85th | `warung-pos` — *"Stock is never a stored number"* | contradiction | stock |
| 86th | `Ordova` + `KitchenLink` — *"who did what, when, from what state"* | omission | order |
| 87th | `xpos` — *"select specific batch/serial numbers during sale"* | missing inverse edge + undefined term | stock |
| 88th | `ironwaves` — *"variance detection between expected and counted cash"* | **all four at once** | money |
| 89th | `partner-kit` + `medusa-pos` | concept with no representation + rule with no consumer | menu |
| **90th (this one)** | **`dkitchen` + `big-market-pos`** — *"the rules every station follows live in `kitchen/`"* | **all four + (e)** | **money (tax line)** |

**The method is now seven-for-seven.** And the **same domain** has now fired twice: the 88th pass found the money domain's *variance* edge, this pass finds the money domain's *tax* edge. **LE31's stock side has a designed append-only ledger; its money side has columns.** That asymmetry is not a recorded design decision — it is what happens when the schema grows around the domain the P0 rows describe.

### The external instrument

`917Dhj/dkitchen` (MIT, ★9, Python, created 2026-10-10, pushed 2026-10-30 = **in-window by both fields**) is a multi-agent kitchen-orchestration framework. Its README is explicit that the rules live in **one place** and that the framework's value is that they are *enforced there*:

> *"The rules every station follows live in `kitchen/`: who owns what, how tickets are written, when to stop and ask, and optional modules for run budgets…"*

> *"**if anyone would do it the same way, the agents do it. If the choice changes the results, the cost, or the direction, they stop and wait for you.**"*

The transferable rule: **a rule that governs money must live in exactly one named place, and anything that changes the outcome must be visible in the record that stores the outcome.** LE31's tax rate governs money and lives in *nowhere*; and the record that stores the outcome (`DerivedTip`) does not show which rate produced it.

`0xyz-exe/big-market-pos` (MIT, PHP, ★1, created 2026-10-20, pushed 2026-10-23 = **in-window by both fields**) contributes the second half from the *same* domain — operational expenses, in Indonesian, on a multi-branch supermarket POS:

> *"Pencatatan biaya operasional per cabang dengan alur **pending/approved/rejected, alasan penolakan, dan pencegahan self-approval**."*

The transferable rule: **a money record carries the rule that produced it, and a decision about it is a record, not a number.** LE31's tax line carries no rule.

### Adjacent work — what is NOT filed here

- **Feature 404** (research, 2026-10-29) proposes column-level `CHECK` constraints on the money columns — `CHECK (subtotal_tax = round(subtotal_tax, 2))` and friends. **All of those are single-column scale checks.** This feature adds a **cross-column** check (`total_due = subtotal_items + subtotal_tax`) and the **configuration** the checks would reference. The two are complementary, not overlapping. Verified: `grep -rniE "total_due\s*=\s*subtotal_items|subtotal_items \+ subtotal_tax" features/` returns **no hit**.
- **Feature 391** (research, 2026-10-28) records the `DerivedTip` formula as having *"no computation site"* and says explicitly *"**Recorded here; not fixed here.**"* This feature **fixes** that: it is the computation site for the tip.
- **Feature 05** names the tax rate as an **Open question** (line 86) and shows `subtotal_tax = 3.90 (10 %)` — **a magic number inside a feature contract**, which is precisely what §7 forbids. It never states a *rule* with a *home*.
- **Features 290 / 294 / 83** each say a *future* field "would need to specify the exact rounding rule". **None** specifies the rounding rule for LE31's **existing** `Bill` money columns.

## Data model

```python
# backend/app/config.py -- NEW settings
class Settings(BaseSettings):
    ...
    # ───── Money ─────
    # Flat tax rate applied to the billable item subtotal.
    # §3.3 default: flat 10%. §3.3 owner question: flat? per-category? per-item?
    tax_rate: Decimal = Field(default=Decimal("0.10"), gt=Decimal("0"), le=Decimal("1"))

    # Rounding mode for every money computation, as a decimal rounding mode name.
    # "ROUND_HALF_UP" | "ROUND_HALF_EVEN" | "ROUND_DOWN" | "ROUND_CEILING" | "ROUND_FLOOR"
    money_rounding: str = "ROUND_HALF_UP"

    # The tip is derived; this is the threshold at which the waiter is asked
    # to confirm before the bill closes. (Currently a bare "50%" in feature 05.)
    tip_confirm_ratio: Decimal = Field(default=Decimal("0.50"), gt=Decimal("0"))
```

```python
# backend/app/models.py -- Bill gains ONE column
class Bill(SQLModel, table=True):
    ...
    subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)
    total_due: Decimal = Field(max_digits=10, decimal_places=2)
    total_paid: Decimal = Field(max_digits=10, decimal_places=2)

    # NEW: the rate and rounding mode that produced subtotal_tax, so the
    # stored tax is auditable back to its rule (feature 05's "provable from
    # the data" claim) even after the configured rate changes.
    tax_rate_applied: Decimal = Field(default=Decimal("0.10"), max_digits=5, decimal_places=4)
```

**No new table.** No migration of existing rows is required for v1 (there is no production data); the column has a default so existing inserts still work.

**Derivation site** — a new module, which is also the `services/` directory §7 names:

```python
# backend/app/services/money.py
from decimal import Decimal, ROUND_HALF_UP
from ..config import settings

_ROUNDING_MODES = {
    "ROUND_HALF_UP": ROUND_HALF_UP, "ROUND_HALF_EVEN": ROUND_HALF_EVEN,
    "ROUND_DOWN": ROUND_DOWN, "ROUND_CEILING": ROUND_CEILING,
    "ROUND_FLOOR": ROUND_FLOOR,
}

def quantize_money(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=_ROUNDING_MODES[settings.money_rounding])

def compute_tax(subtotal_items: Decimal, rate: Decimal | None = None) -> Decimal:
    rate = settings.tax_rate if rate is None else rate
    return quantize_money(subtotal_items * rate)

def compute_total_due(subtotal_items: Decimal, subtotal_tax: Decimal) -> Decimal:
    return quantize_money(subtotal_items + subtotal_tax)

def compute_tip(total_paid: Decimal, subtotal_items: Decimal, subtotal_tax: Decimal) -> Decimal:
    return quantize_money(total_paid - (subtotal_items + subtotal_tax))
```

**Cross-column check** (the one feature 404 does not cover):

```python
class Bill(SQLModel, table=True):
    __table_args__ = (
        CheckConstraint("total_due = subtotal_items + subtotal_tax",
                        name="ck_bill_total_due_is_items_plus_tax"),
    )
```

## Implementation steps

1. **Add the settings** to `backend/app/config.py`: `tax_rate`, `money_rounding`, `tip_confirm_ratio`. Use `Decimal` throughout; do **not** introduce a float literal.
2. **Create `backend/app/services/`** and `backend/app/services/money.py` with the five functions above. The rounding-mode name must be validated at import: an unknown `money_rounding` must raise, not silently fall through to a default.
3. **Add `Bill.tax_rate_applied`** to `backend/app/models.py`, and add the `CheckConstraint` to `Bill.__table_args__`.
4. **Replace the magic numbers** in feature 05's flow with the settings: the `10 %` becomes `settings.tax_rate`; the `50%` tip threshold becomes `settings.tip_confirm_ratio`.
5. **Write the bill** through `compute_tax` / `compute_total_due` / `compute_tip`, and set `tax_rate_applied` to the rate actually used, so a later rate change does not rewrite history.
6. **Derive `DerivedTip` from `compute_tip`** — that is the computation site feature 391 recorded as missing. Set `formula_version` to a value that identifies the **rounding mode and rate** as well as the formula shape (e.g. `"v1:rate=0.10,ROUND_HALF_UP"`), so the existing column starts carrying the basis.
7. **Add the `CHECK` constraint to the schema** and confirm that an inconsistent bill is now **rejected** rather than accepted.
8. **Do not add a `Payment` table here** — feature 391 owns it.

## Telegram interaction if any

None. This feature touches no Telegram surface. The waiter flow (feature 05) gains a `settings.tip_confirm_ratio` threshold, but that is a **value** change inside an existing interaction, not a new command.

## Dependencies

- **`features/05-payment-tip-reconciliation.md`** — the flow this feature makes well-defined. Feature 05 supplies `subtotal_items` and the tip formula; this feature supplies the rate, the rounding mode and the derivation.
- **`features/404-…-check-constraints-on-silent-corruption-columns.md`** — sibling work on the *same* tables. 404 adds **single-column** type guards; this feature adds the **cross-column** check and the config the money path reads. **Both must land without conflicting on `Bill.__table_args__`** — 404 owns `Field(...)`-level `CheckConstraint`s per column; this feature owns the **table-level** `__table_args__` constraint. They compose; if both edit the same block, land this feature's `__table_args__` **first** and let 404's per-column checks merge in.
- **`features/391-…-shift-payment-link-and-cash-variance-derivation.md`** — the other money-domain first-party defect; it records the `DerivedTip` formula as having no computation site, which this feature provides.
- **`PROJECT_CHARTER.md` §3.3** — the tax-rate open question and its default. **This feature implements the default** and makes it configurable; it does **not** close the per-category/per-item sub-question.
- **`backend/app/models.py`** — the schema.
- **`backend/app/config.py`** — the settings.

## Open questions

1. **Should `tax_rate_applied` be on the `Bill` row, or should the whole rate live only in config and the history be unrecoverable?** Recommendation: **keep the column.** A bill is a historical financial record; if the owner changes the rate in November, an October bill must still be explainable. This is the same reasoning as feature 379's tamper-evidence cross-section note — LE31's records are append-only in spirit, and a money row that cannot be explained is a money row that cannot be audited.
2. **Should the `CHECK (total_due = subtotal_items + subtotal_tax)` constraint be added now, or only after the write path is unified?** If any current write path computes `total_due` differently, the constraint will reject it. Recommendation: **unify the write path first, then add the constraint in the same PR** — otherwise the constraint turns a silent inconsistency into a loud failure in an unknown place.
3. **Should `money_rounding` be a string in config, or a `Decimal` rounding-mode enum?** A string is friendlier in `.env`; an enum is safer. Recommendation: **a `str` field validated against a fixed set at import** — the import-time validation gives the enum's safety with the `.env` ergonomics.
4. **Is `ROUND_HALF_UP` the right default?** This is an **owner decision**, not a technical one. EU retail convention is generally half-up; accounting convention is often half-even. Recommendation: **half-up**, and say so in the config comment so the next reader sees it was a choice, not an accident. **Do not** let this feature quietly pick one without recording it.
5. **Does the cross-column `CHECK` belong in feature 404 rather than here?** It is the same table and the same kind of guard. Recommendation: **keep it here**, because the constraint is only meaningful once `subtotal_tax` is derived from a configured rate — 404's constraints are about *type*, this one is about *arithmetic consistency*. If the two land in the same week, merge the `Bill` block rather than editing the same lines twice.
6. **Should the tip be stored at all?** `DerivedTip` stores a derived number — the same "derived values are methods" question feature 374 raises for `Batch.qty_remaining`. Recommendation: **keep storing it for now** (the tip is a *reportable* fact about a closed bill, and it is the audit record), but record the question. This feature does not change it.

## Why this matters

**LE31's charter says the tax rate lives somewhere. It does not. The tax is a number with no rule behind it, and it is stored on the row that records what a customer paid.**

Three things make this the most consequential first-party defect found in seven passes of this audit:

1. **It is a P0 path.** The bill close is on the charter's demo path (*"start app → seat party → order → close bill → cook confirms via bot"*) and on the P0 acceptance criteria (charter §3.1 row: *"Waiter can close a bill; tip is **derived** as `total_paid − subtotal_items − subtotal_tax`"*). The first bill LE31 closes will write a tax number that no rule produced.

2. **It is currently inert but frozen in.** No code writes a `Bill` yet (`Bill(` is constructed **zero** times outside its own class declaration — the same "no write site" condition the 86th pass found for `OrderItem`'s actor). That is exactly the asymmetry the 87th-pass rule names: *a defect in a rule the feature pipeline is about to implement is worse than a defect nothing reads yet, because the plausible wrong answer is the quiet one.* Here the quiet wrong answer is *"the caller will pass the tax in"* — true today, and **silently false** the moment a second write path appears with a different rounding.

3. **The exact arithmetic does not save you.** LE31 gets the *type* right — every money column is `Decimal(max_digits=10, decimal_places=2)`, there is **no** `float()` anywhere in `backend/`, and feature 404 already covers the type guards. But `Decimal` guarantees the *arithmetic* is exact; it does not tell you **which number you should have computed**. Exact arithmetic over an undefined quantity is still wrong — the same sentence that earned feature 387's place.

**The cost asymmetry is the argument for `build` over `defer`:** one config entry, one small services module, one column and one constraint. Cheap now, while the write path does not exist. Expensive after — once bills are closed, a tax that cannot be explained is a tax that cannot be corrected, and the historical record has no ground truth to audit against.
