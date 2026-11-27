# Feature 535 — The tip's formula version can be rewritten after the tip is computed, and nothing records it

> **Pick B of Daily Research 2026-11-27.** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class DerivedTip`, verbatim (lines 172–178):
>
> ```python
> class DerivedTip(SQLModel, table=True):
>     """Computed on bill close: tip = total_paid − (subtotal_items + subtotal_tax)."""
>     __tablename__ = "derived_tip"
>
>     bill_id: int = Field(foreign_key="bill.id", primary_key=True)
>     amount: Decimal = Field(max_digits=10, decimal_places=2)
>     formula_version: str = "v1"
> ```
>
> **Three columns. One of them is the number. One of them is the *name of the rule that produced the number*. And the name of the rule can be rewritten, silently, with no trace.**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with a 4-seat table, one staff member, one visit, one order line, one bill and one `DerivedTip` row with `amount=0.50, formula_version='v1'`):
>
> ```
>   UPDATE derived_tip SET amount = -99.00          ->  ACCEPTED
>   UPDATE derived_tip SET formula_version = 'v0-legacy'  ->  ACCEPTED
>   derived_tip now: amount=-99.00  formula_version='v0-legacy'
> ```
>
> **A tip computed by `v1` now claims to have been computed by `v0-legacy` — and the number it carries was changed too.** No error, no event, and **no way to tell afterwards which rule produced the original number.**
>
> **⭐ AND THE CORPUS OWNS THE *AMOUNT* AND EXPLICITLY DISCLAIMS THE *VERSION*.** This is the sharpest boundary in the corpus on this table, and it is stated in three places:
>
> - **Feature 532** (the bill-money change event, filed 2026-11-26), *Out of scope*: *"**The tip formula itself.** That is **feature 05** (the rule) and **feature 457** (the formula's enforcement and its `formula_version`). **This slice changes no formula and no `formula_version`.**"* — **verbatim.**
> - **Feature 532**, *Dependencies*: *"Feature **457** owns the tip's formula and `formula_version`. **Unaffected** — this slice changes no formula."*
> - **Feature 532**, *Out of scope*: *"The tip formula, **`formula_version`** and the tip's enforcement — **features 05, 457**, filed."*
>
> **Feature 457 owns the formula's *definition* — and says so, in its own Open question 4:**
>
> > *"**What does `formula_version = "v1"` refer to, and where is it defined?** *Recorded default: **the implementer must define it in code as the single named constant the derivation uses**, and the stored value is that constant's value. **Today `formula_version` is a bare literal default and nothing in the database or the code refers to it.** **Recorded because a version string with no referent is exactly feature 448's shape, and this slice should not reproduce it.**"*
>
> **⭐ THAT IS THE GAP, STATED BY THE CORPUS ITSELF.** Feature 457 says *"a version string with no referent is exactly feature 448's shape"* — **feature 448 is the bill's human-facing identity**, whose defect is that **the number the guest is shown has no owner and no history.** **457 noticed the shape and disclaimed it. Nobody owned it.**
>
> **⭐ AND THE SWEEP CONFIRNS NOBODY DID.** A corpus-wide sweep over all **567** feature contracts and **520** HANDOFFs:
>
> | sweep | files |
> |---|---|
> | `formula_version.{0,120}(rewrit\|change event\|mutab\|flip\|immutab\|history\|append)` | **0** (the only hit is feature **532**'s *own dedup table*, which records the probe and its **0** result) |
> | `(formula\|derivation).{0,50}version.{0,80}(rewrit\|chang\|mutab\|tamper)` | 0 real hits — features 415, 420 and 532 all *disclaim* it |
> | `version.{0,50}(string\|tag\|label).{0,80}(rewrit\|chang\|tamper\|untrustw)` | **0** |
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a wrong tip; the corpus confirms nobody owns the rule).

## Goal

Make the tip's `formula_version` mean **one thing**: **it names the rule that produced the tip, and that name is a fact with a history.**

The concrete outcome: **a `DerivedTip` row's `formula_version` cannot be rewritten silently**, and the version string is not a bare literal — **it is a named constant in the code, and the stored value is that constant's value.**

## Scope

**In scope (v1):**

1. **The write-path guard.** A `DerivedTip` row's `formula_version` is **written once**, at the tip's computation. A later write is refused unless it carries an event.
2. **A recorded formula-version change.** A change after the computation is an **event**: the tip row, the field that changed, the old value, the new value, the actor (`by_user_id`) and the time. The mechanism is a new append-only table, mirroring feature **532**'s bill-money change event and feature **534**'s tender-method change event.
3. **The referent, which is the substance of the slice.** Feature 457's Open question 4 records the recorded default: *"the implementer must define it in code as the single named constant the derivation uses, and the stored value is that constant's value."* **This slice implements that recorded default.** It means:
   - a **named constant** in the code (e.g. `DERIVED_TIP_FORMULA_VERSION = "v1"`) is the *only* source of the string;
   - the derivation writes that constant's value and **never a caller-supplied one**;
   - the constant is **importable and assertable**, so a test can compare the stored value against the code's current value.
4. **The relation to feature 457, stated explicitly.** Feature 457 owns the **formula** — *"the tip's value is derived and may be negative, and the derivation is not refused"* — and the **enforcement** that the tip equals the derivation. This slice owns **the name of the rule** and its **history**. **The two are complementary and must not be confused:** 457 says *the number must equal the derivation*; this slice says *the name of the derivation must not change afterwards*.
5. **The relation to feature 532, stated explicitly.** Feature 532 owns the **four money columns** and **explicitly disclaims** `formula_version` — *"This slice changes no formula and no `formula_version`."* This slice owns it. **The two are compatible and must not be confused:** 532 says the *inputs* may not change; this slice says the *name of the rule that read them* may not change. **They share the event-table shape and should land in one PR or in either order.**
6. **The relation to feature 448, stated explicitly.** Feature 448 is the bill's **human-facing identity** — the number the guest is shown, which has no owner and no history. **457 named 448's shape as the thing to avoid reproducing.** This slice is the *other* half of that shape: 448 owns the **displayed identity**, this slice owns the **recorded provenance**. **This slice does not touch 448's number and must not be widened to cover it.**
7. **A regression test** for each row of the scenario table below.

**Out of scope (v1):**

- **The tip formula itself and the tip's amount.** That is **feature 05** (the rule) and **feature 457** (the enforcement). This slice changes no formula and computes no tip.
- **The meaning of `total_paid` (tendered vs received).** That is **feature 420** — filed.
- **The four money columns on the bill.** That is **feature 532** — filed.
- **The `Bill → order_item` edge and the derivation of `subtotal_items`.** That is **feature 435** — filed.
- **A refund.** That is **feature 450** — filed.
- **Split bills and tip pooling.** That is **feature 14** — filed.
- **The tip's *shape* (`round(x, 2)`, `typeof(x) = 'integer'`).** That is **feature 404** — filed. This slice owns *when the version may change*, not what a number may look like.
- **A correction path for the tip's amount.** Feature 457's *Adjacent evidence* records this as an open tension — *"a correction row plus a supersession marker is a v2 shape that would change `DerivedTip`'s primary key"*. **Recorded, not resolved here, and this slice must not widen into it.**
- **Any change to `Bill`, `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry` or `Shift`.**
- **A floor-plan, menu or waiter-UI change.** The mock-up is `index.html`; feature **08**'s scope.
- **Alembic, or a migration framework.** §3.2's stated v1 policy is `init_db()`. **No `alembic.ini`, no `migrations/` directory, no `alembic` dependency.**
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the defect

`DerivedTip` is the corpus's clearest case of a **derived** value: the class docstring says, verbatim, *"Computed on bill close: tip = total_paid − (subtotal_items + subtotal_tax)."* Its three columns are the bill it belongs to, the number, and **the name of the rule that produced the number.**

**The number is protected. The name is not.**

Feature **457** filed the enforcement: *"the tip row is documented as computed and is in fact a free-standing number"* — the tip must equal the derivation. That slice is filed, and it is about the **amount**.

**This slice is about `formula_version`, and the corpus's own text shows the seam.** Feature 532 disclaimed it twice, in the same contract, using the same phrase — *"This slice changes no formula and no `formula_version`"* and *"The tip formula, `formula_version` and the tip's enforcement — features 05, 457, filed."* Feature 420 listed it as *"There is no `tendered`, no `change_given`, no `amount_received`"* and pointed at `formula_version` as the thing that would change if the formula changed.

**And feature 457's Open question 4 is the sharpest statement of the gap in the entire corpus:**

> *"**Today `formula_version` is a bare literal default and nothing in the database or the code refers to it.** **Recorded because a version string with no referent is exactly feature 448's shape, and this slice should not reproduce it.**"*

Read that carefully: 457 names the defect — **a version string with no referent** — and then declines to own it, because 457's slice is about the *amount*. **The result is a column that the corpus has described, in its own words, as having no referent, and that no feature owns.**

### ⭐ Why the plausible wrong answer is not the answer

**Wrong answer — *"457 enforces the tip, so the version is covered."*** 457's *Scope* is the derivation and the write-time refusal of a disagreeing amount. **457's Open question 4 is a recorded default for the implementer of 457's slice — it is not a guard, and it does not survive the tip being written.** The guard this slice adds is what makes the recorded default true.

**Wrong answer — *"the tip row is one row per bill, so nothing can change it."*** `bill_id` is the primary key, so **a second tip row for the same bill is refused** — feature 457's *Adjacent evidence* says so verbatim. **That is an argument about *adding* a row. It says nothing about *editing* the existing one.** Executed: `UPDATE derived_tip SET formula_version = 'v0-legacy'` is **ACCEPTED**. **The primary key prevents a second row; it does not prevent a rewrite of the first.**

### The two-numbers check

The defect is only meaningful if two things that should agree can diverge. **They can:**

| what | before | after |
|---|---|---|
| the version the code uses today (`DERIVED_TIP_FORMULA_VERSION`) | `v1` | `v1` |
| the version stored on the tip row | `v1` | `v0-legacy` |

**The code says one thing and the database says another, and there is no record of when they parted.** That is the whole defect. Every question a future reader might ask — *"why does this tip differ from what the code computes?"*, *"was this bill computed before or after the formula changed?"* — becomes unanswerable, because **the field that would have answered it can be rewritten by whoever changed it.**

### ⭐ The compounding consequence

Feature 457's slice is designed so that **the tip row is trustworthy** — the amount cannot disagree with the derivation. **This slice is what makes the version trustworthy**, and the two together are what let a reader say *"this tip was produced by rule v1, which is the rule the code still runs."*

**Without it, the entire edifice rests on a column nobody guards.** A tip computed by `v1` can claim to be `v0-legacy`, and a reader comparing the tip against today's derivation will find a disagreement with **no explanation** — **and will have no way to tell a stale tip from a tampered one.** That is the difference between a version string and a lie.

### The cost of getting it wrong

- The owner reconciles the day's tips against the code's derivation and finds a mismatch. **There is no way to tell which tips were computed under an older rule and which are wrong.**
- When the formula genuinely changes (and it will — feature 420's tendered-vs-received change alone alters it), **the old tips must be distinguishable from the new ones**. **A mutable version string makes that impossible**, because the distinction is exactly what gets overwritten.
- The tip row is the one row in the schema that documents its own provenance. **Letting that provenance be edited makes the row a number with a caption.**

## Data model

**No column is added to `derived_tip`.** The tip row keeps its three columns; the history lives in the event table.

```python
# backend/app/models.py — NEW, appended after DerivedTip

class DerivedTipVersionChange(SQLModel, table=True):
    """Append-only history of a tip row's formula_version changing.

    A tip records the rule that produced it ONCE. If that name ever changes,
    the change is a fact of its own, not a silent overwrite.
    """
    __tablename__ = "derived_tip_version_change"

    id: int | None = Field(default=None, primary_key=True)
    bill_id: int = Field(foreign_key="bill.id", index=True)
    field: str = "formula_version"      # names the column that changed
    old_value: str
    new_value: str
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

| column | type | meaning |
|---|---|---|
| `id` | int PK | |
| `bill_id` | int FK → `bill.id`, indexed | the tip row whose version changed |
| `field` | str | names the column that changed — `"formula_version"` today |
| `old_value` | str | the version before |
| `new_value` | str | the version after |
| `by_user_id` | int? FK → `app_user.id` | the actor — nullable, matching the corpus's actor convention |
| `at` | datetime (UTC) | when |

**Why `bill_id` and not `tip_id`:** `DerivedTip`'s primary key **is** `bill_id`, and feature 457's *Adjacent evidence* records that a supersession marker would *"change `DerivedTip`'s primary key"* — **which this slice must not do.** The event references the bill, and the tip row is found by it.

**The named constant — the substance of the slice:**

```python
# backend/app/services/derived_tip_service.py (NEW) — or wherever 457 puts its helper
DERIVED_TIP_FORMULA_VERSION = "v1"
```

**The constant must be the single source of the string**, the derivation must write *that* value, and **a caller-supplied version must be refused.** A test asserts that a tip row's stored `formula_version` equals `DERIVED_TIP_FORMULA_VERSION` — **and, when the constant is bumped, that test is the thing that fails.** That is what makes the column a referent rather than a caption.

**Append-only.** Never updated, never deleted. It is a fact table.

## Implementation steps

1. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:

   | scenario | expected |
   |---|---|
   | the tip's **computation write** creates the row with `formula_version = DERIVED_TIP_FORMULA_VERSION` | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `formula_version` on an existing tip row, **no** event | **REFUSED**, stored value unchanged |
   | change `formula_version` on an existing tip row **with** an event in the same transaction | **ACCEPTED**, event carries old value, new value, actor, time |
   | update or delete an event row | **REFUSED** |
   | a **caller-supplied** `formula_version` at the derivation | **REFUSED** — the code's constant is the only accepted source |
   | the stored `formula_version` and `DERIVED_TIP_FORMULA_VERSION` | **must agree** — the two-numbers check |
   | update or delete an event row | **REFUSED** |

2. **Add the event model** to `backend/app/models.py`, following the `StockEntry` / role-change-event / bill-money-event shape (an append-only fact with `by_user_id` and `at`). **No column is added to `derived_tip`.**

3. **Add the named constant** and make the derivation write it. **Read feature 457 first** — if 457 has landed, its helper is where the constant belongs and its write path is where the guard goes. **If 457 has not landed, this slice defines the constant and the helper that 457's slice will use**, and says so in the PR description. **The two must not define two constants.**

4. **Add the guard** as a service helper beside the derivation: a single function that either refuses the version change, or writes the event and the change in one transaction.

5. **Route the tip's computation through the helper.** Today there is **no route that computes a tip** — feature 415 owns the close route and does not exist yet. **Record that in the PR description**: the helper stands alone, and the close route, when it lands, must call it.

6. **Add the two-numbers regression test** — after any accepted change, the tip row's `formula_version` and the event history's latest `new_value` must agree; and the stored value must equal `DERIVED_TIP_FORMULA_VERSION` unless a recorded event says otherwise.

7. **Do not add a `CHECK` constraint** on `formula_version`. It cannot express a history rule, and feature 404 owns the constraint family.

## Telegram interaction if any

**None.** No bot command, no FSM state, no chat surface. This slice is a backend write-path guard on the tip row that the close route (feature 415) will produce.

## Dependencies

- **Feature 457 (`le31-derived-tip-formula-enforcement`) — read first, and the sibling this slice completes.** 457 owns the formula, the amount's enforcement, and **the recorded default this slice implements** (Open question 4: *"the implementer must define it in code as the single named constant the derivation uses"*). **If 457 has landed, its helper is where the constant goes and its write path is where the guard sits.** **If 457 has not landed, this slice defines the constant and 457 must read it — the two must not define two constants.** **457 does not own the version's *history*, and this slice does not own the formula.**
- **Feature 05 (`le31-payment-tip-reconciliation`) — read first.** 05 owns the *rule* and specifies the `DerivedTip` row's shape, including `formula_version`. This slice does not change the rule.
- **Feature 532 (`le31-bill-money-change-event`) — the sibling slice, and the reason this slice exists.** 532 owns the four money columns and **explicitly disclaims** `formula_version` — *"This slice changes no formula and no `formula_version`."* **The two are compatible and must not be confused.** 532's guard refuses a change to the *inputs*; this slice's guard refuses a change to the *name of the rule that read them*. **They share the event-table shape and should land together or in either order.**
- **Feature 448 (`le31-bill-human-facing-identity`) — read first.** 448 owns the bill's **displayed** identity. 457 named 448's shape — *"a version string with no referent is exactly feature 448's shape"* — as the thing to avoid. **This slice is the other half of that shape.** This slice does not touch 448's number and must not be widened to cover it.
- **Feature 415 (`le31-bill-closes-visit`) — the route that will compute the tip.** 415 owns the close write. **This slice's helper has no caller until 415 lands.** Recorded, because *"the write path does not exist"* is the single most likely way for this slice to go wrong.
- **Feature 420 (`le31-total-paid-means-tendered-not-received`) — read first.** 420 owns what `total_paid` means and **changes what the formula yields**. **That is precisely why the version must be a guarded fact**: when 420 lands, the tips computed before it and after it must be distinguishable. **This slice does not change 420's semantics and must not be widened to cover them.**
- **Feature 404 (`le31-money-precision`) — unaffected.** 404 owns the number's *shape*; this slice owns the version's *history*.
- **Feature 435 (`le31-bill-line-membership`) — unaffected.**
- **Feature 450 (`le31-a-refund-has-no-payment-to-be-capped-against`) — unaffected.**
- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — NOT a hard blocker for this slice.** This slice adds **one new table** and **no column to any existing table.** **It is recorded here so the implementer does not assume it is exempt for the wrong reason:** if the implementer *does* add a column (for example, a `superseded_at` marker on `derived_tip`), **446 then blocks it.**
- **Alembic.** §3.2's stated v1 policy is `init_db()`. **Do not add `alembic`, an `alembic.ini`, a `migrations/` directory, a version table, or an `alembic` dependency.**

## Open questions

1. **What happens when the formula genuinely changes and the constant is bumped?** *Recorded default: **the constant is bumped in code; tips already computed keep their old stored version; the guard prevents the stored version from being edited; and the constant's new value does not retroactively change existing rows.** This is the whole point of the slice — **a formula change must be visible as a difference between old rows and new rows**, not a silent reinterpretation of history.*
2. **Should the guard refuse the change outright, or record it?** *Recorded default: **record it.** The guard refuses a change that arrives **without** an event; a change **with** an event is **ACCEPTED.** Refusing every change would make a legitimate re-derivation impossible.*
3. **Should this slice also own the tip's *amount* being rewritten?** *Recorded default: **no.** Feature 457 owns the amount's enforcement, and 457's *Adjacent evidence* records the correction path as *"a v2 shape that would change `DerivedTip`'s primary key"*. **Recorded, not resolved here, and this slice must not widen into it.**
4. **What is the actor when the version is corrected by the owner?** *Recorded default: **`by_user_id` is nullable**, matching the corpus's actor convention (feature 417's). A correction made by the owner outside a staff session has no actor id, and the event must still be recordable.*
5. **Is the constant's name a product decision?** *Recorded default: **no — it is an implementation detail, and it must not appear in any user-facing surface.** The tip's version is provenance for the owner's records, not a number the guest sees.*

## Why this matters

**The tip is the one number in LE31 that the product promises not to be entered by hand.** The charter's acceptance criterion is, verbatim: *"tip field appears on `DerivedTip` row; **never manually entered**."* Feature 457 enforces that the tip equals its derivation.

**This slice protects the last thing that makes that promise auditable.** If the derivation is `v1` today and `v2` after feature 420, then a stored tip says *which* derivation produced it. **A tip row that can be relabelled is a tip row whose provenance is a caption.**

**And the corpus knows this.** Feature 457 wrote, in its own contract, that *"a version string with no referent is exactly feature 448's shape"* — it **identified** the shape, **named** the sibling feature, and **parked** it. **This slice is that parked shape, filed.** It is the eighth shape the corpus has found: **a fact that is owned by nobody, in a table where every neighbouring fact has an owner.**

**The practical consequence for the owner is small today and grows quietly.** Today there is one version, `v1`, and no tip is computed. **The moment feature 420 changes the formula — or 457 lands and the tip starts being written — tips computed before and after the change become indistinguishable**, and the owner reconciling a day of tips has no way to know which is which. **This slice is cheapest now, before there is a single tip row to protect.**

**For the corpus, this slice closes a seam that three separate contracts each described accurately and none closed.** 457 named it. 532 disclaimed it twice. 420 pointed at it. **Nobody owned it.** That is the shape of the finding, and it is the same shape as the two preceding passes: **a covered concept with an uncovered instance** — *the tip is protected* is owned twice (05, 457); *the tip's provenance is protected* is owned zero times.

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`Mindenry/tabletap`** — licence **`null`** (no SPDX id) → §3.2 strictly-incompatible → **vocabulary-only, the code-shape is NOT adopted**; ★0/⑂0, TypeScript, created **2026-11-26** and pushed **2026-11-26** = **in-window by both fields**, 7.8 MB; README at `gh/readme/Mindenry__tabletap.md`. Verbatim, **line 80**: *"**Audit log, platform administration, transactional outbox, Redis-backed realtime, health and …**"* and verbatim, **line 89**: *"**Refunds do not move money. Recording one updates the ledger and the audit log.**"* — **the second clause is this slice's shape**: the movement is *recorded*, the record is *not edited. Recorded because it is the closest in-window statement of "a provenance record that is appended to" — and because the repository is TypeScript/SQLite and LE31's stack is Python 3.13/FastAPI/SQLModel/Postgres.
- **`ahmedshawky7/shifra-restaurant-platform`** — licence **`null`** → §3.2 strictly-incompatible → **vocabulary-only**; ★0/⑂0, Java/Spring Boot, created **2026-11-23** and pushed **2026-11-24** = **in-window by both fields**, 3.5 MB; README at `gh/readme/ahmedshawky7__shifra-restaurant-platform.md`. Verbatim, **line 29**: *"**Immutable Financial Audit Ledger: Append-only `audit_logs` table (`@Immutable` + `@PreUpdate`/`@PreRemove` guards) tracking bill closures, discounts, order cancellations, and menu price updates.**"* — **the `@PreUpdate`/`@PreRemove` guard half is exactly this slice's refusal at the write path**, and the *append-only* half is exactly its event table. **Recorded because it is a peer implementation of the mechanism; Java/Spring, off-stack, and unlicensed, so no code is adopted.**
- **`Simon-Keya/mekuin`** — licence **`null`** → §3.2 strictly-incompatible → **vocabulary-only**; ★0/⑂0, Go, created **2026-11-25** and pushed **2026-11-26** = **in-window by both fields**, 8.8 MB; README at `gh/readme/Simon-Keya__mekuin.md`. Verbatim, **line 90**: *"v52: authenticated provider reconciliation; **`provider_confirmed` is not settled**."* — **the same distinction this slice protects**: *a provider's confirmation* is not *settlement*; *the version the code runs* is not *the version the row claims*. Verbatim, **line 130**: *"…**cash variances**, plus acknowledgement/resolution history and an **immutable business audit ledger**."* **No code is adopted.**
- **`nishantmlad/Restaurant-POS`** — licence **AGPL-3.0** → §3.2 **strictly-incompatible** → **reference-only**; ★1/⑂0, TypeScript, created **2026-11-25** and pushed **2026-11-26** = **in-window by both fields**. **AGPL-3.0 is why no code is adopted.**

**Adjacent first-party work — recorded, NOT picked:**

- **The bill's four money columns being rewritten after the close** — **feature 532**, filed 2026-11-26. **Same family, adjacent table, and the sibling that disclaimed `formula_version` twice.**
- **A closed bill's tender method being rewritten after the close** — **feature 534**, filed in this same pass. **Same family, different column.**
- **The tip's amount and the formula itself** — **feature 457**, filed. **Read, not changed.** This slice owns the version's *history* and 457 owns the formula's *enforcement*.
- **The bill's human-facing identity** — **feature 448**, filed. **Read, not changed.** 457 named 448's shape as the thing to avoid reproducing; this slice is that shape, on the other half of the row.
