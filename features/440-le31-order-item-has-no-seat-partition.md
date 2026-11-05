# Feature 440 — `le31-order-item-has-no-seat-partition`

> **Pick C of Daily Research 2026-11-05 (83rd pass).** **FIRST-PARTY. The gap was proven by execution; the PAIN WAS NOT — and that is why this contract's verdict is `experiment`, not `build`.**
>
> **The gap, proven by execution.** LE31's own `backend/app/models.py`:
>
> ```python
> class Visit(SQLModel, table=True):
>     __tablename__ = "visit"
>     id: int | None = Field(default=None, primary_key=True)
>     table_id: int = Field(foreign_key="table_.id")
>     server_id: int = Field(foreign_key="app_user.id")
>     opened_at: datetime = ...
>     closed_at: datetime | None = None
>     party_size: int
>     adults: int
>     children: int = 0
>
> class OrderItem(SQLModel, table=True):
>     ...
>     visit_id: int = Field(foreign_key="visit.id", index=True)
>     menu_item_id: int = Field(foreign_key="menu_item.id")
>     qty: int = 1
>     ...
>
> class Bill(SQLModel, table=True):
>     ...
>     visit_id: int = Field(foreign_key="visit.id", unique=True)
>     subtotal_items: Decimal = ...
>     subtotal_tax: Decimal = ...
>     total_due: Decimal = ...
> ```
>
> The parent's enumeration, by execution: `Visit` is **one party at one table**; `Bill.visit_id` is **unique** — **one bill per visit**; `OrderItem` has **no seat column** (`['course','fired_at','id','menu_item_id','notes','qty','ready_at','served_at','status','unit_price','visit_id']`).
>
> **So: a table of six who each order a coffee produces six order lines and one bill, and nothing anywhere records which coffee was whose.**
>
> **The gap is uncovered.** The parent's corpus probe for `order item seat`, `per-seat order`, `seat number on the line`, `split the bill across seats` and `seat-level order` returned **0 hits across all 471 feature files and all spec files**, with a **passing negative control** on the same corpus.
>
> **⚠️ BUT THE PAIN IS INFERRED, NOT OBSERVED. This is the whole reason the verdict is `experiment`.**
>
> **There is no evidence that this restaurant needs it.** The parent's execution proved there is **no order-taking router at all** (`backend/app/routers/` contains only `__init__.py` and `tables.py`) and **no bill router** — so **no order line has ever been taken and no bill has ever been closed in this system.** The question "do your guests ever need to know which coffee was whose?" **has not been asked, and this pass cannot answer it.** The gate's own rule is explicit: *an assumed pain becomes a small experiment, not a full feature.*
>
> **THE EXPERIMENT IS ONE QUESTION TO THE OWNER, AND THE ANSWER IS RECORDED IN THIS CONTRACT:**
>
> > **"Do you ever need to know which of the six coffees on a table was whose — or to split a bill between people at the same table?"**
> >
> > - **If YES** → this feature is re-proposed with the frequency evidence in hand, and the shape below is revisited (see *Open questions* 1 and 2, both of which change the shape).
> > - **If NO** → **this feature is closed with the reason recorded, and no code is written.**
>
> **A second, harder problem is named in advance, because it would change the answer even if the owner says yes:** *a party of six arrives together and does not sit in seat order.* A naive `seat: int` field creates a second problem — which physical seat is "seat 3"? — and that problem is **not** solved by adding a column. **It is why the shape below is explicitly provisional.**
>
> **The external trigger (in-window, read in full).** `Jmonczewski-droid/kisnet-pos` (Python 3.12 + FastAPI + SQLAlchemy 2.0 + Alembic + Pydantic, **98 pytest tests**, created 2026-11-03, pushed 2026-11-03, ★0, licence-null) — its Host station, README verbatim:
>
> > *"A 4x4 floor map (tables A1-D4). Creates a party with table, assigned server, name, and **party size**, which starts the table's timer."*
>
> and its Server station:
>
> > *"A drop-down of **only their assigned tables**. Places and edits orders; drinks route to the bar and food routes to the kitchen automatically."*
>
> **This repo has a `Table` with `x`/`y` coordinates and a floor map — but no seat.** It records **party size**, not seat. **That is the transferable observation: the industry-standard table model stops at "how many people are at this table", and the split-the-bill problem is solved elsewhere or not at all.** LE31's `Table` model (`id, label, section, seats, x, y`) and its `Visit` (`party_size, adults, children`) sit in **exactly the same place** — and that is either a signal that the problem is rare, or a signal that the whole industry ignores it. **The corpus of the space cannot tell us which.** **Only the owner can.** **That is exactly what makes this an experiment.**
>
> **The nearest LE31 work, and why this is adjacent rather than duplicate.** Feature **414** owns *party size vs table seats*; feature **423** owns *party composition* (`adults + children == party_size`); feature **435** owns *bill line membership* (which lines a bill charged); feature **415** owns *the bill-closes-visit edge*; feature **388** owns *table state*; feature **436** owns *the active-visit write guard*. **All six are about the party or the table. None is about the individual seat.** The parent's probe confirms it: **0 hits, corpus-wide.**

## Goal

Find out whether LE31's owner needs per-seat attribution on an order line — and, **only if the answer is yes**, give the order line a way to say *"this coffee is for the guest at seat 2"*.

**The primary deliverable of this contract is the recorded answer to the question, not the schema.** The schema below is provisional and is written so that the coding agent does not have to guess at it — but the contract's first instruction is to **ask, and record the answer**, because building the column before the answer is known would be **guessing at a product decision** (the same reason the 2026-11-03 `jackiehe12345-count-vs-record-vocabulary` pick was deferred).

## Scope

**In scope — and this scope is deliberately different from every other feature contract in this repository:**

- **One question to the owner**, asked and **recorded verbatim in this contract** (or in the PR that supersedes it).
- **A recorded answer.** Three possible outcomes, each with its own next step:
  - **"No, we never split a bill by seat"** → **this feature is closed.** The reason is recorded here. **No code is written. No column is added. No schema migration is created.**
  - **"Yes, but only occasionally / only for a table of six or more"** → the feature is **re-scoped** with that frequency evidence, and the shape below is revisited.
  - **"Yes, and here is what we actually need"** → the owner's actual answer may differ from the `seat: int` shape below, and **the contract is rewritten to match it.** **The shape below is a hypothesis, not a decision.**
- **The corpus evidence, recorded so the next pass does not re-derive it:** the probe phrases and their 0-hit results, the negative control, and the list of the six adjacent features that do **not** own this ground.
- **A recorded note of the ordering problem** — that parties do not arrive in seat order — so that a future implementer meets it before writing the column, not after.

**Explicitly NOT in scope:**

- **Any schema change.** **No column is added in this slice.** The column is described in *Data model* as a **provisional shape**, and the implementer's first step is the question, not the migration.
- **Any router, service or helper.** No `seat` helper, no read path, no write path.
- **Any test.** **There is nothing to test until the shape is decided.**
- **Any per-guest identity.** The seat is a **position at a table**, not a person. **No guest table, no guest id, no name on a seat.** This is the same Privacy boundary feature 439 records.
- **Bill splitting by person.** The charter's §3.2 non-goals exclude **tip pooling**; per-seat attribution is not tip pooling, but **a "split the bill" feature is a separate product decision** and is not proposed here.
- **`Visit.party_size` / `Table.seats`.** Features **414** and **423** own them. **This feature does not touch either.**
- **Bill line membership.** Feature **435** owns which lines a bill charged. **This feature does not touch it.**
- **The `Table` model, the floor map, and any seating UI.** Feature 388 owns table state; the floor map is not in scope.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the gap

LE31's data model around a table:

```
Table (id, label, section, seats, x, y)
  └─► Visit (table_id, server_id, party_size, adults, children, opened_at, closed_at)
        └─► OrderItem (visit_id, menu_item_id, qty, unit_price, course, status, notes, ...)
              └─► Bill (visit_id UNIQUE, subtotal_items, subtotal_tax, total_due, total_paid)
```

**Three levels, and no fourth.** A **table** has a capacity. A **visit** has a party size. A **bill** is one aggregate for the whole visit. **Between the party and the bill there is no individual.** A `qty` on a line says *"two coffees"*, not *"one coffee for Anna and one for Bo"*.

### The concrete scenario

A table of six orders: three starters, two main courses, and six coffees. The waiter takes it on one tablet. The six coffees are six `OrderItem` rows (or one row with `qty=6` — **and note that LE31's own feature 430 records that five identical order lines are indistinguishable except by a surrogate key, so a waiter who adds the six coffees as six separate lines produces six rows that cannot be told apart at all**).

At the end of the meal, one guest says *"that's my coffee, not his"*. **LE31 cannot answer.** The bill has one `total_due` for the whole visit. There is no per-seat split, no seat number, and no way to reconstruct who ordered what.

### The ordering problem — named in advance

**This is the part that makes the shape provisional, and it is why the question comes before the code.**

A party of six arrives together and sits down. **Nobody sits in seat order.** The waiter records the order; the guests swap seats; two of them are sharing a plate. A field `seat: int` therefore has to answer: **which physical seat, at which moment, relative to whom?**

Three shapes, and the choice is the owner's operational reality, not a designer's preference:

| Shape | What it means | When it is right |
|---|---|---|
| **`seat: int` on the line** | *"this coffee is for the guest in chair 3"* | The restaurant has **fixed, numbered seats** and the waiter labels them. |
| **`seat_label: str` on the line** | *"this coffee is for 'Anna'"* — a **name or token the waiter types** | Guests identify each other by name. **This is a name, and it touches the Privacy boundary** — a free-text name on an order line is arguably guest data, even if it is the waiter's own annotation. **The charter says v1 stores counts, not identity — and this must be checked against that, not waved through.** |
| **`seat: int` on the `Visit` plus a line-level `seat_ref`** | The *party* is assigned to seats once; lines refer to a seat | The table is re-seated mid-meal and the assignment must be re-settable. |

**All three are defensible and the corpus cannot choose between them.** **This is the second reason the contract's verdict is `experiment` and not `build`: even a yes does not settle the shape.**

### What the industry does — and why that is not evidence either way

`kisnet-pos` — the most complete in-window restaurant-pos implementation the parent read in full — records a **party** and a **table**, and **no seat**. `Table` has `x`/`y` floor-map coordinates and a 4×4 map of tables A1–D4. **It does not model the individuals at a table.** Its Server station sees *"a drop-down of only their assigned tables"*.

**Two readings, and the corpus cannot decide between them:**
- **The problem is rare** — most restaurants never split a bill by seat, so the model does not need it.
- **The problem is real but solved elsewhere** — by the waiter remembering, by a paper docket, or by the restaurant simply not offering it.

**Both readings predict the same schema.** **That is the definition of a question the data cannot answer**, and it is why the owner's answer is the only thing that can move this feature.

### The one thing that is certain

**Whatever the answer, LE31's `OrderItem` today cannot distinguish the six coffees.** Feature 430 records that five identical lines are *"indistinguishable except by a surrogate key"* — **so the six coffees are already six rows that look identical.** Adding a seat is the only way to tell them apart. **If the owner's answer is "no", then the correct conclusion is not "add a seat" but "the waiter should add one line per distinct thing and LE31 should keep them distinguishable for other reasons"** — which is feature 430's ground, already filed. **That possibility is recorded here so the "no" branch is not a dead end.**

## Data model

**⛔ NO SCHEMA CHANGE IS PROPOSED IN THIS SLICE.** The shapes below are the **provisional candidates** the question is meant to choose between.

**Candidate 1 — a seat integer on the line:**

| Table | Column | Type | Notes |
|---|---|---|---|
| `order_item` | `seat` | `int \| None` | The physical seat at the table, as numbered by the restaurant. `NULL` = not recorded. |

**Candidate 2 — a free-text seat label on the line:**

| Table | Column | Type | Notes |
|---|---|---|---|
| `order_item` | `seat_label` | `str \| None` | **⚠️ This may be guest identity and must be checked against the charter's Privacy invariant before it is adopted.** A free-text field on an order line that holds a name is PII about a person, and the charter says v1 stores counts, not identity. |

**Candidate 3 — seat assignment on the visit, reference on the line:**

| Table | Column | Type | Notes |
|---|---|---|---|
| `visit` | `seat_count` | `int \| None` | How many seats this party is using. |
| `order_item` | `seat_ref` | `int \| None` | Which of the party's seats this line is for. |

**If the owner's answer selects Candidate 2, this contract must be re-written and the Privacy question escalated — not implemented as written.**

**What no shape changes:** `Bill` remains one aggregate per visit (`visit_id` is unique). **A per-seat *bill* is a different feature and is not proposed.** The seat, if it exists, is an **attribution** aid on the line, not a partition of the money.

## Implementation steps

**This contract has one implementation step, and it is not code.**

1. **Ask the owner the question** and record the answer **in this contract** (or in a PR that supersedes it). The exact question:

   > *"Do you ever need to know which of the six coffees on a table was whose — or to split a bill between people at the same table?"*

   Record the answer **verbatim**, including any qualification ("only for groups of eight or more", "only at lunch, never dinner").

2. **Branch on the answer:**

   | Answer | Next action |
   |---|---|
   | **No** | **Close this feature.** Append the answer and the date to *Why this matters* or a new *Outcome* section. **No code. No column. No migration.** The contract stays in the repository as a recorded decision — which is what a `defer`/`experiment` outcome is *for*. |
   | **Yes, sometimes** | **Re-scope.** Add the frequency evidence to this contract, pick the shape from the table above, and **re-run the gate** — the `Cost to operational value` check changes from "weak" to "measurable". |
   | **Yes, and here is what we need** | **Rewrite the contract to match.** The owner's actual need may not be a seat at all — it may be "the bill has to split three ways", or "one guest is paying for their own starter". **Write down what they actually said.** |

3. **If the answer is yes and the shape is chosen**, the implementation would be: add the column; add one write path (the waiter surface sets it explicitly, **never inferred**); add one read helper; render it on the bill read; write the regression test. **That work is a new contract, not this one.**

4. **If Candidate 2 is chosen**, **escalate the Privacy question before writing anything.** A name on an order line is guest identity. **The charter says counts, not identity.** That is an owner decision and it must be made explicitly, not inherited from a design sketch.

## Telegram interaction if any

**None, and none is proposed.**

The cook's Telegram bot does not need to know which seat a coffee is for — **the coffee is not made per-seat.** A seat is a **billing and attribution** concern, and the bot is a **kitchen** surface. Adding it would put a billing fact in front of the person who does not use it.

**Recorded as an explicit non-goal with its reason:** if the owner later asks for per-seat lines on the cook's ticket, that is a **separate feature** with its own gate, and it would have to justify why the kitchen needs a billing fact.

## Dependencies

**Must exist before this feature can move past `experiment`:**

- **An answer from the owner.** **This is the only true dependency, and it is not a technical one.** Everything below is a boundary.
- The `OrderItem` and `Visit` models. **Both exist.**
- Feature **435** (bill line membership) — **read it before choosing the shape**, because it establishes what a bill is and is not, and it is the feature most likely to interact with a seat reference.

**Must NOT be implemented by this feature, and the boundaries are load-bearing:**

| Ground | Owner | Why this feature cannot touch it |
|---|---|---|
| `party_size` vs `Table.seats` | **414** | The party count is not a seat. |
| `adults + children == party_size` | **423** | The composition is not a seat. |
| Which lines a bill charged | **435** | **A seat is an attribution on the line, not a partition of the bill.** |
| The bill-closes-visit edge, the tip derivation | **415 / 05** | Untouched. |
| Table state, double-seating | **388** | Untouched. |
| The active-visit write guard | **436** | Untouched. |
| Guest identity, guest demographics | **charter §3.2** | **No guest table, no guest id, no name on a seat** — unless the owner explicitly escalates the Privacy question, which is recorded as Open question 4. |
| Tip pooling | **charter §3.2 non-goal** | Not proposed. |

**Nothing here blocks on an open feature.** Every item above is a **boundary**, not a sequencing requirement.

## Open questions

1. **Does the owner need a seat, or a bill split?** These are different products. A seat says *"this coffee is Anna's"*; a bill split says *"these three people pay separately"*. **The question as written asks about both, and the answer may be "only the second one" — which is a different feature entirely.** **This is the first question, and it is why the question comes before the shape.**
2. **Does the restaurant have fixed, numbered seats?** If not, `seat: int` is meaningless and the physical-seat model cannot work. **The shape table above cannot be chosen without this answer.**
3. **How often?** Once a week? Once a year? **The `Cost to operational value` gate cannot be answered without it, and the gate's rule is that an assumed pain becomes an experiment.** That is why the verdict is `experiment` and not `build`.
4. **If the owner says yes, is a guest's *name* acceptable on an order line?** **This is a Privacy question, not a schema question.** The charter says v1 stores counts, not identity; a free-text seat label that holds a name is identity. **It must be escalated, not inherited from the design sketch above.**
5. **Does "the six coffees" arrive as six lines or one line with `qty=6`?** **LE31's own feature 430 records that five identical lines are indistinguishable except by a surrogate key** — so a seat is also a *disambiguator* for the line itself, independent of billing. **If the answer to the owner's question is "no", the correct conclusion may be "one line with a quantity is the right shape", and the disambiguation question belongs to feature 430's ground rather than to this one.**
6. **What happens to the seat when the party re-seats mid-meal?** Unmodelled in every candidate shape. **Recorded as a known sharp edge, not solved.**

## Why this matters

**It might not matter at all, and the honest answer to that is the point of this contract.**

The gap is real and it is uncovered: **six coffees at one table are six rows that LE31 cannot tell apart, on a bill that cannot say who paid for what.** That is a genuine limit on what the system can explain to a guest.

**But the pass found no evidence that this restaurant has the problem.** There is **no order-taking router and no bill router**, so no order line has ever been taken and no bill has ever been closed in this system. The evidence class is **INFERRED**, and the gate's rule for inferred pain is unambiguous: **an assumed pain becomes a small experiment, not a full feature.**

**The cost of being wrong is asymmetric, and that asymmetry is the reason for the verdict.** If LE31 builds a seat model and the restaurant never uses it, the cost is a column, a helper and a UI affordance nobody touches — small, but not zero, and it adds a concept every future implementer must understand. If LE31 does not build it and the restaurant needs it, the cost is that the owner keeps explaining coffee orders from memory, **and the cost rises with every month that passes** because no historical data would let LE31 reconstruct the mapping later either.

**One hour of the owner's attention resolves it.** That is the entire experiment, and it is cheaper than any of the alternatives — including building it, and including deferring it silently and re-deriving this whole analysis next month.

**This contract is worth more as a recorded decision than as code.** If the answer is "no", the repository gains a documented reason *not* to build a thing, which is exactly as valuable as a documented reason to build it. **The corpus is 471 features deep; a recorded "no, because…" is a real artefact, and this is the honest way to add one.**

## Adjacent evidence

- **`Jmonczewski-droid/kisnet-pos`** (Python 3.12 + FastAPI + SQLAlchemy 2.0 + Alembic + Pydantic, **98 pytest tests**, ★0/⑂0, licence-null, created 2026-11-03, pushed 2026-11-03): **the trigger.** Its Host station records *"table, assigned server, name, and **party size**"*; its Server station sees *"a drop-down of only their assigned tables"*. **It has a floor map with `x`/`y` coordinates and it does not model seats.** **Recorded as vocabulary; the observation is the absence of the concept in the most complete in-window implementation the parent read in full.** No code adopted (licence-null).
- **`ANOUARLEK2026/RestaurantOS`** (local-first, ★0, licence-null, created 2026-10-29): *"Open table / paid order lists"* and *"receivables / payables debts"* — a **customer-account** model, not a seat model. **Adjacent: it shows that "who owes whom" is often solved by attaching an account, not by numbering seats.** **Recorded as an alternative framing the owner's answer might select.**
- **`rkevrellan/ComandaPOS`** (Python/Flask, Panama, ★0, licence-null, created 2026-11-05): *"cuentas separadas"* — **separate accounts** — within one table, plus *"mover líneas entre cuentas"* (**moving lines between accounts**). **This is the strongest external signal in the window that per-line partition within a table is a real restaurant need** — and it also shows the mechanism is **an account that lines move between**, which is closer to candidate 2 than to a seat number. **Recorded as evidence that the problem exists in the space, while the *shape* remains the owner's call.**
- **Feature 435** (bill line membership) — **the adjacent pair, not a duplicate.** 435 owns *which lines a bill charged*; this feature owns *whether a line can be attributed to an individual seat*. **They meet at the bill and must not be merged.**
- **Feature 414** (party size vs table seats), **423** (party composition), **415** (bill-closes-visit), **388** (table state), **436** (active visit) — **the six surrounding features, none of which owns the individual seat.** **Recorded explicitly so a later pass does not re-derive this gap.**
- **Feature 430** (order-item insertion time) — **the reminder that five identical lines are already indistinguishable.** **This feature's `open question 5` is the honest connection: the disambiguation problem is real and is *partly* feature 430's ground, not only this one.**
- **Charter §3.2** — *"Capture of guest gender, age, or any PII beyond counts."* **The constraint that makes candidate 2 an owner decision rather than a schema choice.**
