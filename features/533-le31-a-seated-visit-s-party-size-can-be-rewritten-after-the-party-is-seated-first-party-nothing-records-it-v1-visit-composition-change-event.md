# Feature 533 — A seated visit's party size can be rewritten after the party is seated, and nothing records it

> **Pick C of Daily Brainstorm 2026-11-26 (108th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema**, not by reading.
>
> `backend/app/models.py`, `class Visit`, verbatim (lines 129–137):
>
> ```python
> class Visit(SQLModel, table=True):
>     __tablename__ = "visit"
>
>     id: int | None = Field(default=None, primary_key=True)
>     table_id: int = Field(foreign_key="table_.id")
>     server_id: int = Field(foreign_key="app_user.id")
>     opened_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
>     closed_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
>     party_size: int
>     adults: int
>     children: int = 0
> ```
>
> **Three `int` columns recording who is at the table, and none of them has a constraint, a rule, or a history.**
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with a 4-seat table, one staff member, one visit with `party_size=2, adults=2, children=0`):
>
> ```
>   UPDATE visit SET party_size=40, adults=40  ->  ACCEPTED
>   visit now: party_size=40 adults=40 children=0
> ```
>
> **A party of two, at a four-seat table, became a party of forty.** No error, no event, and **no consequence for the bills, the reports or the KPIs that are computed from `party_size`.**
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **564** feature contracts and **517** HANDOFFs returns **zero hits** for a rule about a seated visit's party size being immutable or traced:
>
> | sweep | files | hits |
> |---|---|---|
> | `visit.{0,40}(party_size\|adults).{0,50}(immutable\|frozen\|rewrite\|mutable\|history\|change)` | 0 | 0 |
> | `party.{0,30}size.{0,40}(change\|edit\|amend)` | 5 | 8 |
> | `(seat\|seating).{0,40}(party_size\|adults).{0,40}(snapshot\|record\|store)` | 0 | 0 |
>
> **⭐ AND THE CORPUS OWNS TWO NEIGHBOURING RULES AND EXPLICITLY DISCLAIMS THIS ONE.** Feature **414** owns the *comparison* (`party_size` vs `Table.seats`) and feature **423** owns the *composition* (`party_size` vs `adults + children`) — **both are rules about a value at the moment of seating.** Neither says the value may not change afterwards. Feature **423**'s own *Out of scope* says, verbatim: *"**Any change to `party_size` as a *peak* count** — the 'what if the party grew' question. That is **feature 416**, and it is `defer`red there because the need is INFERRED."* **Feature 416 is a `defer`, so the growth question is filed and explicitly parked — it is not this slice.**
>
> **⭐ AND THE HELD-FACTS SHAPE IS ALREADY FILED IN THE CORPUS'S OWN VOCABULARY.** Feature **526** — *"A table may carry an empty label — the one name the waiter says out loud may be nothing"* — and feature **527** — *"A table whose area is spelled differently is invisible on the floor map"* — both establish the same principle for the other two spoken identifiers: **a spoken fact may not be nothing, and may not be spelled two ways.** **`party_size` is the third spoken fact about a visit, and it has neither property.** It may be rewritten to any number, and nothing records that it was.
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a wrong party size; the corpus confirms nobody owns the rule).

## Goal

Make a seated visit's party composition mean **one thing**: **the party size and its composition are recorded when the party is seated, and afterwards they are facts with a history.**

The concrete outcome: **a seated visit's `party_size`, `adults` and `children` cannot be rewritten silently**, and where the domain genuinely requires a change (a guest joins, a child turns up), that change is **a recorded event** carrying the old values, the new values, the actor and the time.

## Scope

**In scope (v1):**

1. **The write-path guard.** Once a visit is open (`closed_at IS NULL`), the composition columns — `party_size`, `adults`, `children` — are **written once** at the seat. A later write is refused unless it carries an event.
2. **A recorded composition change.** A change after seating is an **event**: the visit, the old composition, the new composition, the actor (`by_user_id`) and the time. The mechanism is a new append-only table, mirroring feature **524**'s role-change event and feature **532**'s bill-money event.
3. **The relation to the two existing rules, stated explicitly.** Feature **414** (does the party fit the table) and feature **423** (does the composition add up) are **rules at the seat**. This slice adds the rule **after** the seat. **The two are compatible and must not be confused:** 414 and 423 refuse a bad value *arriving*; this slice refuses a good value being *replaced*.
4. **The relation to feature 416, stated explicitly.** Feature **416** asks the *peak-count* question — *"what if the party grew?"* — and is **`defer`red** because the need is INFERRED. **This slice does not revive it.** This slice is not about *how many* people may join; it is about the fact that **if** the number changes, **the change is recorded.** **416's question stays parked.**

**Out of scope (v1):**

- **The capacity comparison (`party_size` vs `Table.seats`).** That is **feature 414** — filed, `build`. 414 owns the comparison at the seating write site.
- **The composition comparison (`party_size` vs `adults + children`).** That is **feature 423** — filed, `build`. 423 owns the composition rule, enforced in the router.
- **The peak-count / party-growth question.** That is **feature 416** — filed as **`defer`**, and it stays that way. **This slice does not decide how many people may join; it records that the number moved.**
- **The "is `seats = 0` legal data" question.** That is **feature 501** — filed. 501 owns the lower bound on `Table.seats`.
- **The seated-at-capacity guard in the shipped screen.** That is **feature 486** — filed. 486 owns the browser-side capacity check in `index.html`.
- **A second `seat` on an occupied table opening a second `Visit`.** That is **feature 388** — filed.
- **The table-state machine.** Feature **388** — filed.
- **The bill-close path.** Feature **415** — filed.
- **The KPI definitions** (`spend_per_cover = bill.subtotal_items / party_size`, feature **06**; today's cover count, feature **29**). **Unaffected and explicitly not changed** — the formulas keep their definitions; what this slice adds is that the denominator is not silently replaced.
- **The visit's actor / `server_id`.** Feature **443** owns the bill's closer against the visit's server; **feature 451** owns the actor-resolution seam. This slice does not change `server_id`.
- **Any change to `Bill`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan, menu or waiter-UI change.** The mock-up is `index.html`; feature **08**'s scope.
- **Alembic.**
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The shape of the defect

LE31's charter **P0** row 42 reads, verbatim:

> *"Waiter can seat a party at any free table and capture `party_size`, `adults`, `children`."*
>
> *Acceptance criterion: "`POST /api/tables/{id}/seat` works; UI shows table card turning yellow."*

**"Capture" is the word, and capture is exactly what is missing.** The charter says the waiter captures the party; it says the party is *captured*, not that the capture **may be replaced**. Today the capture is a **row of three bare `int`s** on a table with **no `CHECK` constraint in the entire database** (feature **470** proved that by execution: ten tables, zero `CHECK` constraints, one `UNIQUE` constraint — `bill.visit_id`).

### The execution, in full

```
=== H: Visit.party_size / adults rewritten after the party is seated ===
  UPDATE visit SET party_size=40, adults=40 (table seats=4) -> ACCEPTED
  visit now: party_size=40 adults=40 children=0
```

**And the comparison the rule exists to make — the two numbers that should agree — is gone:**

```
  table_.seats                = 4
  visit.party_size            = 40
```

**Feature 414's rule was satisfied at the moment of seating and is now silently violated afterwards.** 414 compares `party_size` against `Table.seats` *at the seating write site* — **that comparison is the whole of 414's mechanism**, and it does not re-run when the stored value changes. **The rule holds on entry and evaporates on the stored value.**

**And feature 423's rule, too:** `party_size = 40, adults = 40, children = 0` is still internally consistent, so 423's `adults + children = party_size` check also passes. **Both neighbours' rules are satisfied by the value and unsatisfied by its mutability** — which is the seventh finding shape in its purest form: *a covered concept, an uncovered instance*. The concept *"the party size is right"* is covered twice; **the concept *"the party size cannot be quietly replaced"* is covered zero times.**

### Why this matters more here than it looks

`party_size` is not only a capacity input. It is the **denominator of the business's two most important ratios**:

- `spend_per_cover = bill.subtotal_items / party_size` (feature **06**)
- today's cover count, `SUM(party_size)` (feature **29**)

**A silently rewritten `party_size` changes the restaurant's revenue per cover and its cover count for that day, with no event, no record and no error.** A party of two that becomes forty turns a €60 bill into **€1.50 of spend per cover**, and adds thirty-eight covers to the day's count. **Neither number is wrong in the sense the KPI code can detect — they are computed correctly from a number that was replaced without a trace.**

### The rule this slice files

> **A visit's party composition is written once, when the party is seated. After the seat, the composition is a fact: it changes only through a recorded event that carries the old composition, the new composition, the actor and the time.**

The boundary is already in the schema: `Visit.opened_at` is set at the seat and `Visit.closed_at` is `NULL` until the visit closes (feature **388**'s edge work, feature **415**'s close path).

### The mechanism, stated as the implementer must write it

1. **A new append-only table** — the composition-change event: the visit, the old `party_size` / `adults` / `children`, the new ones, the actor (`by_user_id`) and the time. Never updated, never deleted.
2. **A guard at the write site.** A write that changes any of the three composition columns on a **seated** visit (`closed_at IS NULL`) is refused unless the same transaction writes the event. **The seat write itself must not be refused** — it creates the visit with its composition.
3. **The two neighbours' rules are not changed.** 414 and 423 are enforced in the router at the seat. This slice adds the rule that runs **after** the seat. **Both may be true at once:** a seat that arrives with a bad composition is refused by 423; a good composition that is later replaced without an event is refused by this slice.

## Data model

**New table — the visit-composition change event.** Following the shape of feature **524**'s role-change event and feature **532**'s bill-money event:

| column | type | meaning |
|---|---|---|
| `id` | int PK | |
| `visit_id` | int FK → `visit.id`, indexed | the visit whose composition changed |
| `old_party_size` | int | the party size before the change |
| `old_adults` | int | the adults count before the change |
| `old_children` | int | the children count before the change |
| `new_party_size` | int | the party size after the change |
| `new_adults` | int | the adults count after the change |
| `new_children` | int | the children count after the change |
| `by_user_id` | int FK → `app_user.id` | who made the change |
| `at` | datetime (UTC) | when |

**Rules the table carries:**

- **Append-only.** Never updated, never deleted. It is a fact table.
- **The three old and three new values are carried together**, not one row per column — because **the composition is one fact, not three.** A change from `(2, 2, 0)` to `(3, 2, 1)` is *one* event: a child arrived. **This is deliberately different from feature 532**'s bill-money event, where the four money columns are independent values — and the difference is stated here so the implementer does not copy 532's shape by habit.
- **The chain reconstructs the composition history.** The event's `new_*` values equal the next event's `old_*` values, and the first event's `old_*` values equal what the visit was created with.

**No column is added to `visit`.** The visit keeps its three composition columns; the history lives in the event table.

**`visit` is otherwise untouched** — `table_id`, `server_id`, `opened_at`, `closed_at` are unchanged.

## Implementation

1. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The load-bearing tests:
   - the **seat** write itself creates the visit with its composition and is **ACCEPTED** (the guard must not block the legitimate write);
   - a write that changes `party_size` on a **seated** visit with **no** event is **REFUSED**, and the stored composition is unchanged;
   - a write that changes the composition on a seated visit **with** an event in the same transaction is **ACCEPTED**, and the event carries all six old and new values, the actor and the time;
   - the event table rejects an update and a delete;
   - **the two-numbers check:** after any accepted change, `visit.party_size` and the visit's own event history agree on the current composition — and `party_size == adults + children` still holds (feature **423**'s rule is not broken by this slice).
2. **Add the event model** to `backend/app/models.py`, following the `StockEntry` / role-change-event shape (an append-only fact with `by_user_id` and `at`).
3. **Add the write-path guard** where a visit's composition is written. **Today the seat route exists** (`POST /api/tables/{id}/seat`, owned by feature **388**'s edge work and **02**'s ordering) — so this slice adds the **helper** and the guard, and it **does not rewrite the seat route's semantics**. **The helper's signature must make the safe path the only one the type system permits**: it either refuses, or it writes the event and the change together.
4. **Do not depend on a database constraint alone.** A `CHECK` cannot say "this value may not change after the seat" — the database has no notion of a row's history. **The write path is the mechanism.**
5. **State the ordering against the filed work explicitly** — see *Dependencies*.
6. **Do not modify `index.html`.** The shipped waiter screen is a twelve-way collision zone.

## Telegram interaction

**None.** This slice adds no Telegram command, no bot handler and no message.

## Dependencies

**⭐ THE UPSTREAM-OF-FILED-WORK RULE — THE SEAT ROUTE IS THE WRITE SITE, SO THE ORDERING IS EXPLICIT.**

- **Feature 388** owns the seat write's edge work and the table-state machine. **This slice's guard sits on the same write path.** 388 must land first, or in the same PR, so that the guard has a real write site to attach to. **This slice does not change 388's semantics** — the seat write is permitted by the guard.
- **Feature 414** owns the capacity comparison at the seat. **Unaffected and read, not changed.** **This slice does not re-run 414's comparison after the seat** — the whole point is that the value cannot change, so there is nothing to re-check.
- **Feature 423** owns the composition comparison at the seat. **Unaffected and read, not changed.** Its `CHECK (adults + children = party_size)` is *named* as not-a-schema-constraint in 423's own text and is enforced in the router; this slice adds a rule that is enforced at the same place and does not replace 423's.
- **Feature 416** owns the *peak-count* question and is **`defer`red**. **It stays deferred.** This slice records that the number moved; it does not decide how many people may join. **A later pass may close 416 — and this slice is the right place for the answer to land, because by then the composition will be a fact with a history.**
- **Feature 501** owns the lower bound on `Table.seats`. Unaffected; read, not changed.
- **Feature 486** owns the browser-side capacity check in `index.html`. **Unaffected** — this slice is server-side and schema-side, and `index.html` is a twelve-way collision zone.
- **Features 06 and 29** own the KPI formulas that divide by `party_size`. **Their formulas keep their definitions** — this slice does not change a formula. **What it adds is that the denominator is not silently replaced.** **If either feature later re-derives a day's KPIs, this slice's event table is the record of what the denominator was and when it moved.**
- **Feature 443** owns the bill's closer against the visit's server; **feature 451** owns the actor-resolution seam. **This slice uses the same actor convention** (`by_user_id` → `app_user`) as the rest of the corpus and changes neither.
- **Feature 446** owns the migration path. This slice **adds** a table, which `create_all()` handles; 446 becomes relevant only if the implementer also adds a `CHECK` in the same PR.

## Open questions

1. **Should the guard be keyed on `closed_at IS NULL` (the visit is open) or on a separate "seated" marker?** LE31 has no visit-status column; `closed_at` is the only lifecycle marker. **Recommendation: `closed_at IS NULL`** — a closed visit's composition is as much a fact as an open one's, and the guard should not distinguish them. **But the choice belongs to the implementer, and it must be stated.**
2. **Should the event carry the reason a guest joined or left?** The corpus has a reason vocabulary for the ledger (`StockReason`) but nothing for visits. **Recommendation: no reason column in v1** — the event is a fact and the actor is recorded; adding a reason vocabulary is a separate design. **Not decided here.**
3. **Should a change that raises `party_size` above `Table.seats` be refused outright?** Feature **414** compares at the seat; this slice records after it. **Recommendation: no — this slice does not import 414's comparison into the post-seat path**, because that would be 414's rule and 414 does not own the post-seat case. **But a reviewer may reasonably argue the guard should refuse it. Not decided here.**
4. **Should `adults` and `children` be separately guarded, or only `party_size`?** 423 owns the relation between them. **Recommendation: guard all three together** — they are one fact, and a change to one that breaks 423's relation should be refused. **Not decided here.**
5. **Does the seat route need to write an initial event (the visit's creation)?** **Recommendation: no** — the visit row *is* the creation record, exactly as 523's price history starts at the first change rather than at the catalogue row. **Not decided here.**

## Why this matters

**Three features have now been filed in this exact family for the other two spoken identifiers, and the third was left open.**

- Feature **526** — *"A table may carry an empty label: the one name the waiter says out loud may be nothing."*
- Feature **527** — *"A table whose area is spelled differently is invisible on the floor map."*
- Feature **458** — *"A menu item's name is not unique: two dishes may share the one name the waiter says out loud."*
- Feature **462** — *"An app user's name is not unique: two staff may share the one name the owner calls out."*

**The pattern is explicit and repeated: a fact the operator speaks out loud must be present, must be spelled one way, and must be unique.** `party_size` is the operator's spoken fact about *how many* are at the table — and it has **none** of the three properties. **It may be absent in meaning (a party of "some"), spelled any way (any integer), and rewritten with no trace.**

**The operational shape of the defect.** A party of two is seated at table 4. The waiter later corrects the count to 3 — because a third person joined, or because the note was wrong, or because someone typed 20 instead of 2. **Nothing distinguishes those three cases**, and nothing records that a change happened at all. The day's covers move by one, or by eighteen. The revenue per cover moves with them. **The restaurant's dashboard is then confidently wrong, and the restaurant cannot tell by looking at the data why.**

**Why this is a `build` and not a `defer`.** The change is one table and one guard. The demand is not evidenced by an operator complaint — **the honest framing is that this is a schema-integrity defect on the charter's own P0 row 42, not a reported incident.** But the charter names `party_size` as a **captured** fact, and two filed features already police the other two rules about that captured fact — one for *validity* (423) and one for *fit* (414). **The third rule, that a captured fact cannot be quietly replaced, is the one the corpus has not filed, and it is the rule that makes the other two durable.**

## Out of scope (v1)

- **The capacity comparison** — **feature 414**, filed. **The composition comparison** — **feature 423**, filed. **The peak-count / growth question** — **feature 416**, filed as `defer`, and it **stays** `defer`.
- **`Table.seats`' lower bound** — **feature 501**, filed. **The browser-side capacity check** — **feature 486**, filed. **A second seat on an occupied table** — **feature 388**, filed. **The table-state machine** — **feature 388**, filed.
- **The bill-close path** — **feature 415**, filed. **The bill's closer vs the visit's server** — **feature 443**, filed. **The actor-resolution seam** — **feature 451**, filed.
- **The KPI formulas** — **features 06, 29**, filed. **This slice changes no formula.**
- **Any change to `Bill`, `OrderItem`, `MenuItem`, `Table`, `Batch`, `StockEntry`, `DerivedTip` or `Shift`.**
- **A floor-plan, menu or waiter-UI change** — `index.html` is feature **08**'s scope and a twelve-way collision zone.
- **Alembic**, except as noted in *Dependencies* for feature 446.
- **Any change to `PROJECT_CHARTER.md`.**
