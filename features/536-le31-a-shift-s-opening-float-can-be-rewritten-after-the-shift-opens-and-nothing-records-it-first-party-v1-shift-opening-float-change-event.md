# Feature 536 — A shift's opening float can be rewritten after the shift opens, and nothing records it

> **Pick C of Daily Research 2026-11-27.** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Shift`, verbatim (lines 181–190):
>
> ```python
> class Shift(SQLModel, table=True):
>     """For end-of-shift cash reconciliation."""
>     __tablename__ = "shift"
>
>     id: int | None = Field(default=None, primary_key=True)
>     opened_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     closed_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     opening_float: Decimal = Field(max_digits=10, decimal_places=2)
>     counted_cash: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
>     variance: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
>     by_user_id: int = Field(foreign_key="app_user.id")
> ```
>
> **The float is the number the whole cash reconciliation is measured against, and it is a mutable column with no constraint, no rule, and no history.**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with one staff member and one shift with `opening_float=100.00`):
>
> ```
>   UPDATE shift SET opening_float = 9999.00  ->  ACCEPTED
>   shift now: opening_float=9999.00
> ```
>
> **The till's starting cash was changed from €100.00 to €9,999.00, silently.** No error, no event, and **no consequence for any report that reconciles the day's cash** — because the variance is computed *against* the float.
>
> **⭐ AND THE CORPUS ALREADY STATES THE RULE — IN PROSE — AND ENFORCES IT NOWHERE.** This is the finding, and it is the sharpest instance yet of the corpus's own recurring shape. **Feature 426's Open Question 1**, verbatim:
>
> > *"**Does the close endpoint take `opening_float`?** Recommendation: **no** — `opening_float` is set when the shift opens and is **not** re-settable at close time. **Re-settable floats make the variance untraceable (the manager would be comparing against a number they could have changed after counting).**"*
>
> **The corpus diagnosed the defect, in one sentence, with the reason — and then scoped it as a question about the *close endpoint's request body*, which is a different thing from the *column*.** Feature 426's *Scope* is *"the shift lifecycle router: open a shift, close a shift, list shifts"* and the endpoint's request bodies. **Feature 426 does not guard the column; it does not own the rule. It stated the rule and left it where it found it.**
>
> **⭐ AND EVERY NEIGHBOUR OWNS A DIFFERENT PIECE.** A corpus-wide sweep over all **567** feature contracts and **520** HANDOFFs:
>
> | sweep | files |
> |---|---|
> | `opening_float.{0,120}(rewrit\|change event\|mutab\|flip\|immutab\|history)` | **0** |
> | `(opening\|starting) (float\|cash\|bank).{0,80}(rewrit\|chang\|mutab\|tamper)` | **0** |
>
> | neighbour | what it owns | what it says about the float |
> |---|---|---|
> | **391** | the `Payment` table, `expected_cash`, `variance = counted_cash − expected_cash` | *"**UNCHANGED by this feature**"* — the `Shift` row, float included, is explicitly out of its scope |
> | **426** | the shift lifecycle **router** and the close endpoint | *"does the close endpoint take `opening_float`?"* — a **route** question; the column is unguarded |
> | **513** | the **ordering** — the count is entered before the expected figure is revealed | *"Any change to `Shift.variance`, `Shift.counted_cash` or `Shift.opening_float`'s **types**"* — types, not mutability |
> | **504** | the **denomination** decomposition of the counted position and mid-shift movements | a different question |
> | **528** | the **reason** a non-zero variance must carry | *"The **derivation** … `Shift` … **UNCHANGED by this feature**"* — and it is about the *variance's* explainability, not the *float's* mutability |
> | **404** | `CHECK` constraints on the money columns, including `shift.opening_float` | the **shape** of the number — `opening_float = round(opening_float, 2)` — **not its history** |
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **medium** for the demand (the corpus's own Open Question 1 argues the rule's *reason* — *"the manager would be comparing against a number they could have changed after counting"* — which is an owner-facing harm, not a hypothetical).

## Goal

Make a shift's opening float mean **one thing**: **the float is what was in the till when the shift opened, and afterwards that fact has a history.**

The concrete outcome: **an open or closed shift's `opening_float` cannot be rewritten silently**, and where the domain genuinely requires a correction, that correction is **a recorded event** carrying the old value, the new value, the actor and the time.

## Scope

**In scope (v1):**

1. **The write-path guard.** Once a shift row exists, `opening_float` is **written once**, at the open. A later write is refused unless it carries an event.
2. **A recorded float change.** A change after the open is an **event**: the shift, the field that changed, the old value, the new value, the actor (`by_user_id`) and the time. The mechanism is a new append-only table, mirroring feature **532**'s bill-money change event, feature **533**'s visit-composition change event, feature **534**'s tender-method change event and feature **535**'s formula-version change event.
3. **The relation to feature 426, stated explicitly.** Feature 426 owns the **shift lifecycle router** and the open/close endpoints. This slice owns **the column's write-once rule and its history**. **426's Open Question 1 stated the rule; this slice implements it.** **426 and this slice are compatible and must not be confused:** 426 decides *what the close endpoint accepts*; this slice refuses a *second write to the stored column* wherever it comes from — the route, the ORM, a script, or the operator's own shell.
4. **The relation to feature 391, stated explicitly.** Feature 391 owns the **derivation** — `expected_cash` and `variance = counted_cash − expected_cash`. **391's Data model says the `Shift` row is *"UNCHANGED by this feature"*, and this slice does not change it either.** This slice's guard protects the **input** 391's derivation reads. **When 391 lands, the float becomes the baseline of a derived number — which is exactly why it must not move underneath the derivation.**
5. **The relation to feature 528, stated explicitly.** Feature 528 owns the **reason** a non-zero variance must carry — *"a number the schema can display but cannot explain"*. **This slice is upstream of it and does not overlap:** 528 asks *why the variance is what it is*; this slice asks *whether the baseline it was computed against could be changed afterwards*. **528's own text says the variance's problem is that *"nothing computes it and nothing says what it was computed from"* — this slice answers the second half for the float.**
6. **The relation to feature 513, stated explicitly.** Feature 513 owns the **ordering** — the count is entered before the expected figure is revealed, so the manager cannot adjust the count to match what they expect. **This slice is the same discipline applied to the other end of the comparison:** 513 hides the expected figure so the count cannot be fitted to it; this slice prevents the float from being fitted to the count. **The two together make the variance honest.** **They are complementary and must not be merged** — 513 is *once 391 lands*, and 513 explicitly excludes *"any change to `Shift.variance`, `Shift.counted_cash` or `Shift.opening_float`'s **types**"*.
7. **A regression test** for each row of the scenario table below.

**Out of scope (v1):**

- **The `Payment` table, the `Shift`↔`Payment` money edge, and the `expected_cash` derivation.** That is **feature 391** — filed. This slice computes no expected cash and adds no payment row.
- **The shift lifecycle router and the open/close endpoints.** That is **feature 426** — filed. This slice adds the guard that runs at the write site and the event table it consults; **it must not write `POST /api/shifts` or `POST /api/shifts/{id}/close`.**
- **The ordering of the count and the expected figure.** That is **feature 513** — filed.
- **The denomination decomposition of the counted position, and mid-shift cash movements.** That is **feature 504** — filed.
- **The reason a non-zero variance must carry.** That is **feature 528** — filed.
- **Cash-in / cash-out movements and inter-register transfers.** That is **feature 393** — filed.
- **`CHECK` constraints and the money columns' shapes.** That is **feature 404** — filed, and it explicitly covers `shift.opening_float`'s *shape*. **This slice owns *when the value may change*, not what the value may look like.**
- **Timestamp and timezone handling on the shift columns.** That is **feature 453** — filed.
- **The business-date / service-day boundary.** That is **feature 405** — filed. A shift that crosses midnight is 405's question and this slice must not decide it.
- **Any change to `Bill`, `DerivedTip`, `Visit`, `OrderItem`, `MenuItem`, `Table`, `Batch` or `StockEntry`.**
- **A Telegram command.** The charter's criterion for the close is an **HTTP** endpoint (feature 426). **No bot surface is added.**
- **A new owner surface.** The count is entered in the existing manager surface. **If the implementer finds there is no manager surface, stop and read feature 05 — do not invent one.**
- **Alembic, or a migration framework.** §3.2's stated v1 policy is `init_db()`. **No `alembic.ini`, no `migrations/` directory, no `alembic` dependency.**
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the defect

A shift is the unit the owner reconciles the day against. Three money columns on it, and the shape is **a balance, not a ledger**: *a float at the start, a count at the end, and a difference.* Feature **393** says this in its own words, verbatim: *"LE31 models a shift's cash as a **balance**, not as a **ledger**: an `opening_float`, a `counted_cash`, and a `variance`. **There is no middle.**"*

**A balance has exactly one thing that makes it a balance: the baseline does not move.** The float is the baseline. The count is what was found. The variance is the difference. **If the baseline can be rewritten after the count, the difference is not a fact about the day's cash — it is a number two people can each change.**

### ⭐ Why the corpus's own sentence is the finding

Feature 426's Open Question 1 is worth reading twice, because it contains the whole defect in one sentence:

> *"Recommendation: **no** — `opening_float` is set when the shift opens and is **not** re-settable at close time. **Re-settable floats make the variance untraceable (the manager would be comparing against a number they could have changed after counting).**"*

**Three things are true about that sentence, and together they are the finding:**

1. **It names the rule** — *"set when the shift opens and not re-settable"*.
2. **It names the harm** — *"the manager would be comparing against a number they could have changed after counting"* — **and the harm is owner-facing, not theoretical.**
3. **It is scoped to the wrong thing.** It is filed as *"Does the close endpoint take `opening_float`?"* — **a question about one endpoint's request body.** **A route that refuses a parameter is not a column that cannot change.** The rule as written has no home, because the column's write path does not exist yet (there is no shift router — feature 426 owns creating it), and because a column can be changed from the ORM, from a script, or from the operator's own `psql` session, none of which pass through a request body.

**And the sweep confirms no feature picked it up.** `opening_float` appears in **six** corpus files, and in every one it appears as a *field declaration* or as a *recommendation about a route*:

| file | the mention |
|---|---|
| **429** | a table listing of the columns — *"the mutable ones get `updated_at`"* — **`shift` is on that list** |
| **404** | the `CHECK` constraint's *shape*: `opening_float = round(opening_float, 2)` |
| **373** | a note that `opening_float` is `Decimal` — *"the gap is not the type — it is the guard"*, where **the guard means a precision check, not a history rule** |
| **393** | the balance-vs-ledger vocabulary |
| **391** | *"**UNCHANGED by this feature**"* |
| **426** | the recommendation quoted above |
| **528** | the variance's reason |

**Six mentions, and not one of them is a rule that a write must obey.**

### ⭐ The sharpest thing in the corpus: `Shift` is on the *mutable* list

Feature **429** records the schema's own convention verbatim, from `models.py`'s module docstring:

> *"- All tables have `created_at`; only mutable ones get `updated_at`."*

And its table listing puts **`shift`** on the mutable side — alongside `menu_item`, `batch`, `visit`, `order_item`, `bill`, `table_`. **But feature 429's own text puts `stock_entry` on the *other* side**: *"Immutable and append-only tables (`app_user` … `stock_entry` — **append-only by charter §4.3, never UPDATE**; `derived_tip` — **one row per bill, written once**) get `created_at` only."*

**Read that list again with `shift` on it.** `stock_entry` is *never UPDATE*. `derived_tip` is *written once*. **`shift` is simply "mutable" — and the mutable list is exactly the list of tables whose facts can be silently replaced.** Feature 429 classifies `shift` as mutable **because it has an `updated_at`**, and the corpus has read that classification as a fact about `shift` rather than as a consequence.

**The corpus has now filed four slices that make individual *facts* on mutable tables write-once** — feature 523 (the menu price), 524 (the staff role), 531 (the order line's quantity), 532 (the bill's money columns), 533 (the visit's composition). **`shift` is the table that the cash reconciliation depends on, and no slice has done it.**

### The two-numbers check

The defect is only meaningful if two numbers that should agree can diverge. **They can, and the corpus already knows the second one exists:**

| what | before | after |
|---|---|---|
| `shift.opening_float` (the baseline) | `100.00` | `9999.00` |
| the day's cash the owner counted | `145.00` | `145.00` |
| `shift.variance` — *as computed at close* | `45.00` | `45.00` |
| `shift.variance` — *recomputed against the rewritten float* | `45.00` | **`-9854.00`** |

**And here is the part that makes it worse than a typo: the stored `variance` does not move.** Executed: the tip-style probe showed the same shape on the bill — *"after `bill.total_paid := 100.00` → stored tip STILL `-99.00`, implied now `-901.50`"*. **The stored variance keeps the number the derivation produced at close, while the baseline it was derived from is now different.** Two numbers that should agree **do not**, and **nothing records that they came apart.**

### ⭐ The compounding consequence: the variance becomes unfalsifiable

Feature **528** owns the rule that a non-zero variance must carry a reason. Feature **391** owns the derivation of the variance from the payments. Feature **513** owns the ordering that stops the count being fitted to the expected figure.

**All three assume the baseline is fixed.** Without this slice:

- The manager's count is protected from being fitted to the expected figure (513) — **but the expected figure's own baseline is not protected from being fitted to the count.** 513 closes one end of the comparison; this closes the other.
- The variance's reason (528) explains *why the difference is what it is* — **but a rewritten float means the difference could have been *chosen*, not found.** **The reason would be an explanation of a number that may not have been derived from the day's cash at all.**
- The derivation (391) computes `variance = counted_cash − expected_cash` — **but if the float moves after the derivation, the stored variance and the recomputed one diverge, and 391's own regression test ("that fails if they disagree") is a test of the derivation, not of the data's stability.**

**Three filed features are all downstream of a baseline that nothing protects.** That is the shape of the finding.

### The cost of getting it wrong

- **The owner's end-of-day cash count stops being evidence.** The variance becomes a number that cannot be trusted or explained, and feature 528's reason requirement becomes theatre.
- **A wrong float and a wrong count are indistinguishable.** Both produce a variance; only one is a mistake.
- **Nothing will ever say *"this shift's float was €100 and is now €9,999"*, because there is no record to say it with.**

## Data model

**No column is added to `shift`.** The shift keeps its seven columns; the history lives in the event table.

```python
# backend/app/models.py — NEW, appended after Shift

class ShiftFloatChange(SQLModel, table=True):
    """Append-only history of a shift's opening float changing.

    A shift records what was in the till when it opened ONCE. If that fact
    ever changes, the change is a fact of its own, not a silent overwrite.
    """
    __tablename__ = "shift_float_change"

    id: int | None = Field(default=None, primary_key=True)
    shift_id: int = Field(foreign_key="shift.id", index=True)
    field: str = "opening_float"      # names the column that changed
    old_value: Decimal = Field(max_digits=10, decimal_places=2)
    new_value: Decimal = Field(max_digits=10, decimal_places=2)
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

| column | type | meaning |
|---|---|---|
| `id` | int PK | |
| `shift_id` | int FK → `shift.id`, indexed | the shift whose float changed |
| `field` | str | names the column that changed — `"opening_float"` today |
| `old_value` | Decimal(10,2) | the float before |
| `new_value` | Decimal(10,2) | the float after |
| `by_user_id` | int? FK → `app_user.id` | the actor — nullable, matching the corpus's actor convention |
| `at` | datetime (UTC) | when |

**The values are `Decimal`, not `str`.** The event records the *numbers*, and a money number recorded as text loses the `Decimal` guarantee feature 411 owns. The `field` column is what makes the table reusable — the same shape as feature 534's and 535's event tables — so a later slice about the shift's other columns does not need a second table.

**Append-only.** Never updated, never deleted. It is a fact table.

## Implementation steps

1. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:

   | scenario | expected |
   |---|---|
   | the **open write** creates the shift with its `opening_float` | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `opening_float` on an open or closed shift, **no** event | **REFUSED**, stored value unchanged |
   | change `opening_float` **with** an event in the same transaction | **ACCEPTED**, event carries old value, new value, actor, time |
   | update or delete an event row | **REFUSED** |
   | the event history's last `new_value` and `shift.opening_float` | **must agree** — the two-numbers check |
   | the stored `shift.variance` and `variance_for_shift(shift)` | **must still agree** — feature **391**'s rule is not broken by this slice |
   | write a value with more than two decimals | **REFUSED** — feature **404**'s rule, unaffected and not re-implemented here |

2. **Add the event model** to `backend/app/models.py`, following the `StockEntry` / role-change-event / bill-money-event shape (an append-only fact with `by_user_id` and `at`). **No column is added to `shift`.**

3. **Add the guard** as a service helper, `backend/app/services/shifts_service.py` (NEW): a single function that either refuses the change, or writes the event and the change in one transaction. **It does not create the shift router and does not change the close route's semantics** — feature **426** owns that.

4. **Route the open write through the helper** if and only if the shift router exists (feature 426). **If 426 has not landed, the helper stands alone and the router, when it lands, must call it.** **Record which of the two is true in the PR description.**

5. **Read features 391, 426 and 513 before writing the helper.** 391's derivation must not be inlined; 426's route must not be rewritten; 513's ordering must not be reordered. **If 391 has landed, the helper's guard must run *before* the variance is derived** — otherwise the derivation reads a float that is about to change.

6. **Add the two-numbers regression test** — after any accepted change, `shift.opening_float` and the event history's latest `new_value` must agree.

7. **Do not add a `CHECK` constraint** on `opening_float`. Feature 404 owns the constraint family, and a `CHECK` cannot express a history rule in any case.

## Telegram interaction if any

**None.** No bot command, no FSM state, no chat surface. The charter's criterion for closing a shift is an **HTTP** endpoint (feature 426). **This slice adds a backend write-path guard and no surface.**

## Dependencies

- **Feature 426 (`le31-shift-close-lifecycle`) — the route this slice's guard belongs to, and the contract that stated the rule.** 426 owns the shift lifecycle router and the open/close endpoints. **426's Open Question 1 stated this slice's rule** (*"`opening_float` is set when the shift opens and is not re-settable"*); **this slice implements it.** **If 426 has not landed, this slice's guard has no route to sit in** and must wait or must introduce the write path itself, which would duplicate 426. Recorded explicitly, because *"the write path does not exist"* is the single most likely way for this slice to go wrong.
- **Feature 391 (`le31-shift-variance-stored-no-derivation-no-payment-table-shift-money-edge`) — read first.** 391 owns the `Payment` table and the `expected_cash` derivation, and its Data model says the `Shift` row is *"UNCHANGED by this feature"*. **This slice does not change it either.** 391's helper is what reads the float, and this slice's guard protects that input.
- **Feature 528 (`v1-shift-variance-reason-a-nonzero-cash-variance-must-carry-a-reason`) — read first.** 528 owns the variance's *reason*. **This slice is upstream and does not overlap.** 528's own text — *"nothing computes it and nothing says what it was computed from"* — is what this slice answers for the float.
- **Feature 513 (`v1-blind-cash-up-the-count-is-entered-before-the-system-reveals-the-expected-figure`) — read first.** 513 owns the *ordering* and is *once 391 lands*. **It explicitly excludes any change to `Shift.opening_float`'s *types*; this slice changes neither the types nor the ordering.** 513 protects the count from being fitted to the expectation; this slice protects the baseline from being fitted to the count.
- **Feature 504 (`v1-till-cash-position-decomposed-into-denominations-with-mid-shift-movements`) — read first.** 504 owns the denomination decomposition and the mid-shift movements, and says it is *"complementary"* to 391. **Untouched here.**
- **Feature 404 (`le31-sqlite-tables-not-strict`) — owns the `CHECK` constraints**, including `shift.opening_float`'s *shape*. **This slice must not duplicate them and must not add one.**
- **Feature 453 — owns the timestamp types on the shift columns.**
- **Feature 405 (`le31-service-day-boundary`) — owns the business-date question.** A shift crossing midnight is 405's question; this slice must not decide it.
- **Feature 393 — owns the cash-movement-ledger vocabulary** (cash-in / cash-out, inter-register transfers). **Explicitly not bundled.**
- **Feature 446 (`le31-has-no-schema-evolution-mechanism`) — NOT a hard blocker for this slice.** This slice adds **one new table** and **no column to any existing table.** **It is recorded here so the implementer does not assume it is exempt for the wrong reason:** if the implementer *does* add a column (for example, a `float_changed_at` marker on `shift`), **446 then blocks it.**
- **Alembic.** §3.2's stated v1 policy is `init_db()`. **Do not add `alembic`, an `alembic.ini`, a `migrations/` directory, a version table, or an `alembic` dependency.**

## Open questions

1. **What happens when the float must legitimately change?** *Recorded default: **the change is an event, not a refusal.** The guard refuses a change that arrives **without** an event; a change **with** an event is **ACCEPTED.** Refusing every change would make a mis-keyed opening float permanent, and feature 528's whole point is that a wrong number must be *explainable*, not frozen.*
2. **Should the guard apply to a closed shift as well as an open one?** *Recorded default: **yes — to both.** A float rewritten *after* the close is the worse case, because the stored variance was already derived from the old float and now silently disagrees. **The guard must not read the shift's closed state as permission to change the baseline.***
3. **Should the event carry the shift's actor (`by_user_id`) as the actor?** *Recorded default: **no — the event carries its own `by_user_id`**, nullable, matching the corpus's actor convention (feature 417's). **The shift's `by_user_id` is who opened the shift; the event's is who changed the float.** They are different facts and confusing them would make the shift's actor wrong.*
4. **Should `counted_cash` get the same treatment?** *Recorded default: **no.** `counted_cash` is the *count* and feature 513 owns its ordering; `counted_cash` is written once at the close by construction. **The `field` column exists so a later slice does not need a second table.** Recorded, not decided.*
5. **Is a shift even openable today?** *Recorded default: **no.** There is no shift router — feature 426 owns creating it — and `Shift` is constructed **zero** times outside its own class declaration. **The defect is therefore latent, not corrupting data**, and this slice is cheapest now, before there is a single shift row to protect.

## Why this matters

**The opening float is the one number in LE31 that the owner's end-of-day count is measured against.** Feature 391 derives the variance from it. Feature 528 demands a reason for the variance. Feature 513 protects the count from being fitted to the expectation. **Three filed features stand on this column, and nothing guards it.**

**And the corpus already said so.** Feature 426 wrote, in its own contract: *"**Re-settable floats make the variance untraceable (the manager would be comparing against a number they could have changed after counting).**"* That sentence is the finding. **The corpus diagnosed the harm, named the rule, and filed it as a question about a request body — which is a question the route answers and the column never hears.**

**This is the ninth instance of the corpus's recurring shape: a fact that is owned by nobody.** And it is the first one where the corpus has *already written down the rule* and simply not given it a home. **That is worth saying plainly, because it is a different failure from the ones the corpus has been fixing.** Features 523, 524, 531, 532, 533, 534 and 535 each found an *unguarded* column. **This one found a *guarded-in-prose* column** — and prose is not a constraint.

**For the owner, the difference is whether the end-of-day count is evidence.** Right now, if the float moves, the variance is a number that could have been chosen rather than found, and **the owner has no way to tell which**. The reason feature 528 requires would become an explanation of a number whose baseline is unknown.

**And it is cheap now.** There is no shift router, no `Shift` row, no shift close. **This is the cheapest slice in the corpus to implement — one table, one helper, one test — and the most expensive to implement later**, because later there will be rows to migrate and a variance that was derived against a float nobody can justify.

## Adjacent evidence

**Third-party trigger — in-window, permissive licence. Recorded as a vocabulary reference only; no code is adopted.**

- **`Simon-Keya/mekuin`** — licence **`null`** (no SPDX id) → §3.2 strictly-incompatible → **vocabulary-only, the code-shape is NOT adopted**; ★0/⑂0, Go, created **2026-11-25** and pushed **2026-11-26** = **in-window by both fields**, 8.8 MB; README at `gh/readme/Simon-Keya__mekuin.md`. Verbatim, **line 130**: *"Phase 5C adds branch-scoped operational alert inboxes for inventory thresholds, pending expense/supplier-invoice approvals and **cash variances**, plus acknowledgement/resolution history and an **immutable business audit ledger**."* — **the two halves of this slice in one sentence**: an *immutable audit ledger* for the cash side, and *acknowledgement/resolution history* for the variance. **The transferable property is that the variance is an object with a history, not a number in a column.** **No code is adopted** — Go, off-stack, and unlicensed.
- **`mysterydwan/sekelas-cafe`** — licence **`null`** → §3.2 strictly-incompatible → **vocabulary-only**; ★0/⑂0, TypeScript, created **2026-11-20** and pushed **2026-11-20** = **in-window by both fields**, 859 KB; README at `gh/readme/mysterydwan__sekelas-cafe.md`. Verbatim, **line 26**: *"append-only movement ledger, waste logging, **blind-count opname with approvals**,"* — the *blind count* is feature 513's discipline (the count is entered before the expectation is revealed) and the *append-only ledger* is this slice's event table. Verbatim, **line 27**: *"restock with weighted unit costs, low-stock alerts everywhere."* **Recorded because it is the closest in-window statement of the counting discipline, and because it is unlicensed and off-stack, so no code is adopted.**
- **`ahmedshawky7/shifra-restaurant-platform`** — licence **`null`** → §3.2 strictly-incompatible → **vocabulary-only**; ★0/⑂0, Java/Spring Boot, created **2026-11-23** and pushed **2026-11-24** = **in-window by both fields**, 3.5 MB; README at `gh/readme/ahmedshawky7__shifra-restaurant-platform.md`. Verbatim, **line 29**: *"**Immutable Financial Audit Ledger: Append-only `audit_logs` table (`@Immutable` + `@PreUpdate`/`@PreRemove` guards) tracking bill closures, discounts, order cancellations, and menu price updates.**"* — **the `@PreUpdate`/`@PreRemove` guard half is exactly this slice's refusal at the write path.** **Recorded because it is a peer implementation of the mechanism; Java/Spring, off-stack, and unlicensed, so no code is adopted.**
- **`narisolutions/medusa-pos`** — Apache-2.0 ✓ §3.2 strictly-compatible; ★36/⑂7, TypeScript/Tauri **✗ off-stack**; created **2026-02-27**, pushed **2026-11-26** — **in-window by `pushed_at` only** (created nine months before the window start; **this is not a fresh discovery**). Verbatim, from its README: *"**Stock is not held while a sale is parked; availability is re-checked on resume and the operator is told what changed. Holding stock is planned.**"* **Recorded as adjacent, not picked** — that is the parked-sale shape, which features 269 and 395 already own, and it is **not** this slice's subject. **Listed here because it is the only permissive-licence in-window source this pass found, and because the honest reading of it is that it does not bear on the float.**
- **`Raktim94/nodedr-restaurant-pos`** — **AGPL-3.0** → §3.2 **strictly-incompatible** → **reference-only**; ★313/⑂205, pushed **2026-11-27**. Verbatim, **line 551**: *"**Money balances are `set`, never `increment`** — any running balance …"* — the same discipline as this slice's *set-once* rule, applied to balances. **AGPL-3.0 is why no code is adopted.** **And note the corpus has already used this exact source as a trigger for feature 433** — it **cannot be re-used as a fresh trigger**, and is listed here only as corroboration of the vocabulary.

**Adjacent first-party work — recorded, NOT picked:**

- **The bill's four money columns being rewritten after the close** — **feature 532**, filed 2026-11-26. **Same family, different table.**
- **A seated visit's party size being rewritten after the party is seated** — **feature 533**, filed 2026-11-26. **Same family, different table.**
- **A closed bill's tender method being rewritten after the close** — **feature 534**, filed in this same pass. **Same family, different table.**
- **The tip's formula version being rewritten after the tip is computed** — **feature 535**, filed in this same pass. **Same family, different table.**
- **The shift's `by_user_id` actor being rewritten** — **recorded here, not picked.** `Shift.by_user_id` is nullable and freely rewritable (the `NOT NULL` constraint is what refuses `NULL`, and the *value* is unguarded). **Feature 417 owns the `StockEntry` actor's foreign key** and the corpus's actor convention generally; **the shift's actor's *history* is a separate question and is not bundled here.**
