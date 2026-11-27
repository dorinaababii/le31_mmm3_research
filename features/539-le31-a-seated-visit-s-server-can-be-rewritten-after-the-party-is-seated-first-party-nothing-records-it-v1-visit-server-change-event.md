# Feature 539 — A seated visit's server can be rewritten, and the bill's closer stops being the person whose table it was

> **Pick C of Daily Brainstorm 2026-11-27 (109th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own schema, and it is proved by EXECUTION against LE31's real schema.**
>
> `backend/app/models.py`, `class Visit`, verbatim (lines 126–139):
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
> **`server_id` is a bare foreign key with no constraint, no history, and no write-path rule for changing it.** The server is the member of staff the party belongs to — the person whose table it is, the person whose tips it counts for, the person the manager asks *"whose table?"* about.
>
> **Executed against LE31's real schema** (`SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with three staff — a `server`, a `cook` and a `manager` — one visit whose `server_id` pointed at the server, one order line, and one paid bill whose `closed_by` was that same server):
>
> ```
>   UPDATE visit SET server_id = <the manager> WHERE id = 1    ->  ACCEPTED
>
>   visit.server_id  = <the manager>      (was <the server>)
>   bill.closed_by   = <the server>       (unchanged)
> ```
>
> **⭐ TWO NUMBERS THAT SHOULD AGREE, DISAGREEING — AND NOTHING RECORDS THAT THEY EVER AGREED.** Feature **443** exists precisely to give this comparison a meaning: *"Make LE31 able to answer **'who took this payment, and were they entitled to?'** — and to say so **from the schema**, rather than leaving the two user columns on `Visit` and `Bill` side by side, unrelated."* **After the rewrite the two columns disagree, and there is no record anywhere that they used to agree** — so the schema cannot distinguish *"the manager closed it for the server"* (443's legitimate case) from *"the server was silently replaced"*.
>
> **⭐ AND IT BREAKS THE ACTOR'S ROLE MEANING AT THE SAME TIME.** Feature **451** exists to make a visit's server mean *"a member of staff who serves tables"* — and it does so **at the write path**: *"The role is checked at the write path. A visit may only be attributed to a user holding `UserRole.server`."* **A rewrite of `server_id` after the visit exists bypasses that check entirely**: the role predicate ran once, at creation, against a value that has since moved. **The cook, the manager and the server are all equally writable into the column today.**
>
> **⭐ AND NO FEATURE OWNS IT.** A corpus-wide sweep over all **570** feature contracts and **525** HANDOFFs (1,093 files) finds **no feature** that owns the *mutation*:
>
> | sweep | files | hits | what those hits are |
> |---|---|---|---|
> | `visit.{0,50}server_id.{0,60}(update\|rewrite\|mutab\|reassign\|chang(e\|ing))` | 2 | 2 | **feature 451** (the write-path *role* rule) and **feature 533** (the composition event) — **both explicitly disclaim the column** |
> | `visit.{0,40}server.{0,40}(immutable\|fixed\|history\|attribution)` | 2 | 2 | the same two files |
> | `bill.closed_by.{0,50}visit.server_id.{0,50}(differ\|change\|mutab)` | 1 | 1 | **feature 443** — the comparison, not the mutation |
>
> **Feature 533's own words** (*Out of scope*, line 72): *"**The visit's actor / `server_id`.** Feature **443** owns the bill's closer against the visit's server; **feature 451** owns the actor-resolution seam. **This slice does not change `server_id`.**"* And feature **451**'s own words, line 53: *"**No change to `Visit.server_id`'s type, its nullability, or its foreign key.** The column stays exactly as it is. This feature adds the **rule** that makes the reference meaningful."* **451 owns the rule at creation. 443 owns the comparison. Neither owns what happens when the value moves afterwards.**
>
> | rule | mechanism | owner |
> |---|---|---|
> | a visit's server must hold `UserRole.server` | a role check at the write path | **feature 451** — **at creation** |
> | the actor is resolved server-side, not asserted by the client | an actor-resolution seam | **feature 451** |
> | the bill's closer vs the visit's server — what a difference *means* | a schema-level statement | **feature 443** |
> | the visit's **composition** (`party_size`, `adults`, `children`) after seating | an event table + a write-path guard | **feature 533** |
> | **the visit's server after seating** | **event table + write-path guard** | **THIS SLICE** |
>
> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED** (executed). Confidence: **high** for the defect, **low** for the demand (no operator has reported a swapped server; no code path changes `server_id` today — there is no route that reassigns a seated party).
>
> The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`.

## Goal

Make a seated visit's **server** mean one thing: **the member of staff the party belongs to, recorded when the party is seated, and afterwards a fact with a history.**

The concrete outcome: **the server of a visit that has been seated cannot be rewritten silently**, and where the domain genuinely requires it (a section handover — the shift changes and the tables pass to the next waiter), that handover is **a recorded event** carrying the old server, the new server, the actor and the time, and **the new server's role is checked at the moment of the handover, not only at creation**.

The single sentence this feature exists to make true: *a party belongs to a server from the moment they are seated; after that, a change of server is a recorded handover, not a silent rewrite.*

## Scope

- **One new table** — `VisitServerChange` — recording `visit_id`, `from_server_id`, `to_server_id`, `by_user_id`, `at`.
- **One write-path rule**: the server of a seated visit may be changed only through a helper, and only to a staff member who holds `UserRole.server` — **feature 451's role predicate, applied at the handover as well as at creation.**
- **A refusal** when the target does not hold the `server` role, naming the target's actual role — **the same legible refusal 451 specifies**, so the two entry points read identically.
- **A regression test** that asserts a handover to a non-`server` is refused, that a permitted handover writes exactly one change row with the old server, the new server, the actor and the time, and that the bill's `closed_by` is **not** affected by the handover.

**The handover is recorded in an event table, not by a `previous_server_id` column.** A column preserves one handover and loses the second; feature **523** established that argument for the catalogue's price (*"a `previous_price` column preserves one change and loses the second"*), and the same argument applies here.

## Out of scope

- **The role predicate at creation.** Feature **451** owns it: *"The role is checked at the write path. A visit may only be attributed to a user holding `UserRole.server`."* **This slice reuses that predicate and does not re-implement it, and does not add a second, different role check.**
- **The actor-resolution seam.** Feature **451** owns it, and its own *Out of scope* says *"Authentication"* is out of scope. **This slice does not build authentication, a session, a token or a login.**
- **The bill's closer vs the visit's server — what a difference means.** Feature **443** owns it. **This slice does not change 443's rule and does not decide what "the manager closed it for the server" means.**
- **The bill-close path.** Feature **415** owns it. The tip derivation — features **05** / **415**.
- **The visit's composition** (`party_size`, `adults`, `children`). Feature **533** owns it and its own *Out of scope* names *"the actor-resolution seam — **feature 451**, filed"*. **This slice does not touch those columns and does not add a composition event.**
- **The visit's table.** Feature **538** (this pass's pick B) owns it. **The two slices touch the same table and are pairwise disjoint** — 538 owns `table_id`, this slice owns `server_id`, and **neither may reuse the other's event table.**
- **`AppUser.role` itself.** Feature **524** owns the role's *mutability* (a role rewritten in place). **This slice does not change `app_user`, does not add a role and does not change the enum.**
- **A departed staff member.** Feature **464** owns the roster's deactivation and feature **451** owns the actor-resolution seam's eligibility filter. **This slice does not add an `is_active` column.**
- **Any change to `OrderItem`, `MenuItem`, `Batch`, `StockEntry`, `Bill`, `Shift` or `DerivedTip`.**
- **A floor-plan, menu or waiter-UI change.** `index.html` is feature **08**'s scope and a thirteen-way collision zone.
- **Alembic**, except as noted in *Dependencies* for feature **446**.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### The defect, as executed

The schema declares `server_id` as a bare foreign key. There is no `UniqueConstraint`, no `CheckConstraint`, no `ondelete` clause, and **no write path exists** that could enforce anything about it after creation. The visit therefore names a server, and nothing stops that name from changing.

The executed probe seeded a coherent world and then made one change:

```
  app_user  id=7  name='w'   role=server
  app_user  id=8  name='c'   role=cook
  app_user  id=9  name='m'   role=manager
  visit(id=1, table_id=T1, server_id=7, party_size=2, adults=2, children=0, closed_at=NULL)
  order_item(id=1, visit_id=1, menu_item_id=1, qty=2, unit_price=14.00, status='served')
  bill(id=1, visit_id=1, subtotal_items=28.00, total_due=33.60, total_paid=33.60, payment_method='cash', closed_by=7)

  UPDATE visit SET server_id = 9 WHERE id = 1;      ->  ACCEPTED
```

and then read back the two numbers that must agree:

| what | value after the rewrite | what it should say |
|---|---|---|
| `visit.server_id` | **9** (the **manager**) | 7 (the **server**) — the party belongs to the server |
| `bill.closed_by` | **7** (the server) | 7 — the bill's closer |

**Nothing raised. Nothing was written to any log. And the schema now shows a visit whose server is a manager and a bill closed by a server, with nothing recording that they were ever the same person.**

### Why the role check is bypassed, not merely undone

Feature **451**'s guarantee is a statement about a **write path**: *"The role is checked at the write path. A visit may only be attributed to a user holding `UserRole.server`."* That guarantee is **true at the moment of creation and silent afterwards.**

This is the same shape as two guarantees the corpus has already had to state explicitly, and the corpus's own words for them apply here verbatim:

- Feature **531** (the line's quantity): *"a quantity is set while the line is `new`; after the line has been fired, the quantity is a fact with a history."*
- Feature **533** (the party's composition): *"the party size and its composition are recorded when the party is seated, and afterwards they are facts with a history."*

**A write-path rule that is not accompanied by a rule about *when* the value may change is a rule about a moment, not about the data.** The role predicate ran once; the value can then be moved to anybody in the roster — including the cook and the manager, whom 451's rule exists to keep out.

### Why the domain does have a real handover

**A section handover is a real event in a restaurant.** The shift changes; the tables pass from the outgoing waiter to the incoming one; the tips for the evening are split by who served which table. If LE31 cannot record a handover, then either the handover does not happen (the tables stay with the outgoing waiter for the whole service, which is wrong), or it happens **invisibly** — which is the defect.

The contract therefore does **not** forbid the change. It makes it **a recorded handover with the role re-checked at the handover**:

> **A party's server changes only when the shift changes, and the new server must be a member of staff who serves tables — checked at the moment of the handover, because that is the moment the rule has to hold.**

### Why the bill's closer must not be affected

Feature **443**'s rule is that the schema must say **what it means** when `bill.closed_by` and `visit.server_id` differ, because *"the manager closed it for the server"* and *"the cook closed it"* must not be the same shape. **This slice must not disturb that comparison.**

Therefore: **a handover changes the visit's server and nothing else.** It does **not** change `bill.closed_by` — the bill's closer is who actually took the money, and that is a fact about the payment, not about the party's current owner. **The implementer must not write the handover helper so that it also rewrites the bill's closer**, and the regression test must assert that `bill.closed_by` is untouched.

**And the consequence is recorded, not decided:** after a handover, the bill's closer and the visit's server are *different people*, and **443 owns what that means**. This slice's *Open questions* record that the owner should read 443's rule with this case in mind — it does not answer it.

### Why an event table and not a guard alone

1. A handover to another **`server`** is legitimate and **must be possible**.
2. When it happens it must be **visible afterwards**: who served the table before, who serves it now, who made the handover and when.
3. The reader must be able to ask *"was this table handed over?"* and get an answer.

A `previous_server_id` column satisfies (1)–(2) once and fails on the second handover. Feature **523** has already made this argument for the catalogue's price; the same argument applies here.

### The actor

The actor is a **staff** member (`app_user`), never a guest — consistent with charter §3.1 and with the corpus's actor convention as recorded in feature **417**'s schema note: *"every actor field carries a foreign key."* `by_user_id` is **nullable** with a foreign key — the same form features **379** and **417** specify.

**Note the distinction this table keeps**: `from_server_id` and `to_server_id` are **the party owner**; `by_user_id` is **the person who performed the handover** — the outgoing waiter, or the manager who reassigned the table. **They are not the same fact and the table must not conflate them.** This is feature **379**'s actor convention applied to a second actor, and it is why the table has three user columns rather than two.

## Data model

```python
# backend/app/models.py — ADD, do not modify any existing class

class VisitServerChange(SQLModel, table=True):
    """A seated visit changed hands: its server was handed over. Append-only."""
    __tablename__ = "visit_server_change"

    id: int | None = Field(default=None, primary_key=True)
    visit_id: int = Field(foreign_key="visit.id", index=True)
    from_server_id: int = Field(foreign_key="app_user.id")
    to_server_id: int = Field(foreign_key="app_user.id")
    by_user_id: int | None = Field(default=None, foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

Notes the implementer must honour:

- The class name and table name follow the corpus's convention: **`visit_server_change`**, in the pluralised snake style of `stock_entry` and `order_item`.
- `by_user_id` is **nullable** with a foreign key — the corpus's actor convention, applied a fourth time (features **379**, **417** and this slice).
- **Do not add a `UniqueConstraint`** on `(visit_id, …)`. A table may be handed over more than once; a constraint would forbid the second handover.
- **Do not add a column for the bill.** The bill's closer is unaffected by a handover, and duplicating it here would create a second source of truth for a money fact — which is precisely the failure feature **532** was filed for.

**Migration path.** `PROJECT_CHARTER.md` §3.2 says v1 uses `init_db()` rather than Alembic, and `create_all()` **cannot alter an existing table** — but this slice **adds** a table and **changes no existing column**, so `create_all()` is sufficient for a fresh database. **If the deployment has an existing database, feature **446** owns the migration path and this slice must not invent one.**

## Implementation

1. **`backend/app/models.py`** — add `class VisitServerChange` exactly as specified above. **Do not touch `Visit`, `AppUser`, `OrderItem`, `Bill`, `Batch`, `StockEntry`, `Shift` or `DerivedTip`.**
2. **The handover helper** — one function, `hand_over_visit(session, visit_id, to_server_id, actor_id)`, which:
   - loads the visit and the target staff member;
   - **refuses** when the target does not hold `UserRole.server`, raising a legible error naming the target's actual role — **feature 451's predicate, reached through 451's helper, not re-implemented here**;
   - writes **one** `VisitServerChange` row;
   - sets `visit.server_id = to_server_id`;
   - **does not touch `bill.closed_by`**;
   - commits **once**.
3. **The helper is the only writer of `visit.server_id` after the visit is created.** A grep for `server_id =` under `backend/` must return the seat path and this helper, and nothing else. **Record the grep output in the PR description** — a rule with two writers is not a rule.
4. **Regression tests** — at minimum:
   - a handover to a **`cook`** is **refused**, and the error names the role; the visit is unchanged; **zero** `VisitServerChange` rows exist;
   - a handover to a **`server`** is **accepted**, writes exactly **one** change row with the old server, the new server, the actor and the time, and sets `visit.server_id`;
   - a handover to a **`manager`** is **refused** — 451's own *Open questions* records that whether a manager may serve tables is an owner decision, and the recorded default is **no**;
   - a **second** handover produces a **second** row — the case a `previous_server_id` column would have lost;
   - **the bill's `closed_by` is unchanged** by a handover.
5. **The consistency assertion** — a test that, for every `VisitServerChange`, asserts the visit's current `server_id` equals the **latest** change's `to_server_id`.

**The implementer must not guess at step 2's package location.** LE31 has **no `services/` package** today (`backend/app/` holds `models.py`, `main.py`, `routers/`, `bot/`). Feature **441** says it *"supplies the rule and the helper"* and feature **421** supplies *"the single write path"*; whichever lands first **creates** the package. **If `backend/app/services/` does not exist when you start, create it — and say so in the PR.** Do not put the helper in `routers/`: it is not a route.

## Telegram interaction

**None.** The waiter UI is `index.html`, feature **08**'s scope and a thirteen-way collision zone. This slice changes **no** surface.

The refusal is raised at the write path and reaches whichever surface eventually calls the helper — and **the helper's error must be legible**, because a surface that cannot express the refusal will swallow it. That is feature **486**'s problem, not this slice's, and it is recorded in *Dependencies*.

The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched. The Telegram chat-id → role mapping is feature **403**'s territory and is explicitly out of scope here.

## Dependencies

- **Feature 451 (the role check and the actor-resolution seam) — ⭐ THIS SLICE REUSES ITS RULE AND MUST NOT RE-IMPLEMENT IT.** 451 owns the predicate *"a visit may only be attributed to a user holding `UserRole.server`"* **at creation**. **This slice applies the same predicate at the handover.** The implementer of 451 must not add a handover helper and the implementer of this slice must not add a second role check with a different message. **451's own text records that the two error messages at the seat route must be distinguishable; this slice's error message must match 451's shape, not the seat route's.**
- **Feature 443 (the bill's closer vs the visit's server) — adjacent, and this slice must not disturb it.** 443 owns what a difference between the two columns *means*. **This slice changes `visit.server_id` and nothing else; `bill.closed_by` is untouched.** **The owner should read 443's rule with the handover case in mind — this contract records that and does not decide it.**
- **Feature 533 (the visit's composition change event) — adjacent, same table, same shape, may land in either order.** 533 owns `party_size`/`adults`/`children` and its own *Out of scope* says *"This slice does not change `server_id`."* **This slice owns `server_id`.** **The two must not share an event table and must not be merged.**
- **Feature 538 (the visit's table change event, this pass's pick B) — adjacent, same table, pairwise disjoint.** 538 owns `table_id`; this slice owns `server_id`. **Neither may reuse the other's event table, and neither may add a column to the other's event.** They may land in either order, or in one PR with the two tables kept separate.
- **Feature 415 (the bill-close path) — untouched.** The tip derivation — features **05** / **415**.
- **Feature 524 (the role's own mutability) — adjacent.** 524 owns a role rewritten in place. **This slice does not change `app_user` and does not add a role.**
- **Feature 464 (the staff deactivation) — adjacent.** 464 owns the roster's departure and feature 451 owns the actor-resolution seam's eligibility filter. **This slice does not add an `is_active` column and does not filter inactive staff** — it reuses 451's predicate as it stands.
- **Feature 427 (the SQLite FK pragma) — adjacent.** The pragma is off by default in SQLite (`PRAGMA foreign_keys = 0` — proved by execution), so this table's foreign keys are enforced in Postgres and not in SQLite. **The write-path rule does not depend on them**, and the implementer must not write a test that passes only because SQLite ignores a foreign key.
- **Feature 446 (the migration path) — needed only if the deployment already has a database.** This slice **adds** a table and changes no existing column, so `create_all()` suffices for a fresh database. **If an existing database must be migrated, 446 owns the mechanism and this slice must not invent one.**

## Open questions

1. **May a manager be a visit's server?** Feature **451**'s own *Open questions* records this: *"**Whether a manager may be a visit's server.** The recommendation is **no** — a manager serves tables too in a small restaurant — but this is an **owner decision**, recorded in `Open questions`."* **Recorded default: no.** **This slice follows 451's recorded default and does not re-open the question** — but it inherits the decision, so the refusal message for a manager is the one 451 specifies.
2. **When may a handover happen?** The contract's rule is *"a handover happens when the shift changes"*. **There is no shift-change event in the schema today** — feature **426** owns the shift close lifecycle and feature **391** owns the shift-to-payment edge. **Recorded default: the handover helper does not itself check the shift; the caller asserts the handover, and the event records when it happened.** **The implementer must not build a shift-change trigger** — that is 426's and 391's territory, and this slice must not depend on them.
3. **What happens to a handover after the bill is closed?** The visit's server changes, and the bill's closer does not. **443 owns what the difference means.** **Recorded and escalated — this slice does not decide.**
4. **Is the actor required?** `by_user_id` is nullable, matching the corpus's convention. **Recorded default: nullable — a handover made by an unauthenticated path is still a handover, and a missing actor is visible as a missing actor.**
5. **Does the same rule apply to `visit.opened_at` and `visit.closed_at`?** Both are equally rewritable, and feature **428** and feature **454** each mention `closed_at` in a different question (the open-visit aggregate and the close-without-a-bill case). **That is a different question and it is recorded here so the next pass files it or discards it deliberately. It is NOT taken by this slice.**

## Why this matters

**"Whose table is this?" is the question a manager asks most often**, and `visit.server_id` is the answer. **A value that can be rewritten silently makes the answer unverifiable** — and the difference between a manager closing a bill for a server (legitimate) and a server having been silently replaced (not legitimate) becomes indistinguishable, because **nothing records that the two columns ever agreed.**

**It is the same shape as seven defects the corpus has already filed** — features **531** (the quantity), **532** (the bill's money), **533** (the party's composition), **534** (the tender method), **535** (the tip's formula version), **536** (the shift's opening float), **538** (the visit's table) — and the corpus sweep found **no feature** that owns the *mutation* of the server. **Seven sibling facts have a rule; the eighth does not.**

**It also exposes a gap in a filed feature's guarantee, which is worth more than the defect itself.** Feature **451** guarantees *"a visit may only be attributed to a user holding `UserRole.server`"*. **That guarantee is true at creation and silent afterwards** — and 451's own words say *"No change to `Visit.server_id`'s type, its nullability, or its foreign key. The column stays exactly as it is."* **451 is not wrong; it is incomplete in a way it did not know it was incomplete, and this slice is what completes it.** That is the shape the corpus's own hand-off instrument looks for: a feature that found the boundary of its rule and did not own the other half of it.

**The demand is INFERRED and the contract says so.** No operator has reported a swapped server, because no route reassigns a seated party — `backend/app/routers/` holds only `__init__.py` and `tables.py`. **The defect is latent, not corrupting data.** That is exactly the moment to add the rule: before the first write path exists, not after. **The evidence for the defect is OBSERVED — executed, re-runnable, with the numbers in this contract — and the evidence for the priority is INFERRED.** Those are different claims and the gate asks for both.

## Adjacent evidence

- **Feature 451** (`le31-a-visit-may-name-a-cook-as-its-server`) — *"The role is checked at the write path. A visit may only be attributed to a user holding `UserRole.server`."* And: *"**No change to `Visit.server_id`'s type, its nullability, or its foreign key.** The column stays exactly as it is."*
- **Feature 443** (`le31-bill-closed-by-need-not-be-the-visits-server`) — *"Make LE31 able to answer **'who took this payment, and were they entitled to?'** … rather than leaving the two user columns on `Visit` and `Bill` side by side, unrelated."*
- **Feature 533** (`le31-a-seated-visit-s-party-size-can-be-rewritten-after-the-party-is-seated-…`) — the sibling contract. Its *Out of scope*, verbatim: *"**The visit's actor / `server_id`.** … **This slice does not change `server_id`.**"*
- **Feature 524** (`le31-a-staff-member-s-role-can-be-rewritten-in-place-with-no-record-of-who-did-it-…`) — the role's own mutability, and the corpus's actor convention.
- **Feature 379** — the actor convention this slice's `by_user_id` follows.
- **Feature 417** — *"every actor field carries a foreign key"*, the schema note this slice's foreign keys follow.
- **Feature 426 / 391** — the shift close lifecycle and the shift-to-payment edge; the shift-change moment this slice's rule refers to but does not implement.
- **Charter §3.1** — v1 stores counts, not guest identities; the actor is staff.
- **Feature 427** — the SQLite FK pragma, proved by execution (`PRAGMA foreign_keys = 0`), which is why this slice's rule lives at the write path.

## Verification protocol

**Re-run the probe.** `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py` builds LE31's real schema on a throwaway SQLite file and executes the rewrite. **Its output, before the fix, is `ACCEPTED`.** After the fix, the same probe must show the rewrite **refused**.

**The negative control is load-bearing.** A test that asserts "the handover is refused" **must fail** when the guard is removed — assert that by commenting out the refusal and watching the test go red. **A test that passes both with and without the guard proves nothing.**

**The assertions, in order:**

1. `UPDATE visit SET server_id` on a seated visit is **refused**; the visit is unchanged; **zero** `VisitServerChange` rows exist.
2. `hand_over_visit(..., to_server_id=<a server>)` is **accepted**; exactly **one** change row exists with `from_server_id`, `to_server_id`, `by_user_id` and `at` correct; `visit.server_id` moved.
3. A handover to a **`cook`** is **refused**, and the error names the target's actual role.
4. A handover to a **`manager`** is **refused** (451's recorded default).
5. A **second** handover produces a **second** row (the case a `previous_server_id` column loses).
6. The consistency assertion holds: `visit.server_id == latest_change.to_server_id`.
7. **`bill.closed_by` is unchanged** by a handover — a handover relocates the party's owner, it does not rewrite who took the money.
8. `grep -rn "server_id = " backend/` returns the seat path and the handover helper, **and nothing else**.

**A note on the numbers in this contract.** Every number quoted here was produced by execution against LE31's real schema on 2026-11-27, by the parent, with the probe in the `scripts/` directory named above. **They are not transcribed from a subagent's prose.** Where a claim is not proved by execution — Postgres behaviour, the UI's reaction, the operational demand — this contract says so explicitly, in the *Evidence class* line, in the *Open questions*, and in *Why this matters*.
