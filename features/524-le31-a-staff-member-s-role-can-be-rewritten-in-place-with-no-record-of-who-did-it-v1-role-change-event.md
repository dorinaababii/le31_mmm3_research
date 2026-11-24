# Feature 524 — A staff member's role can be rewritten in place with no record of who did it: the roster's authority is mutable and untraceable

> **Pick C of Daily Brainstorm 2026-11-24 (107th daily-brainstorm pass).** **Bucket: v1.** **Verdict: `build` — first-party, proven by execution, and recorded UNOWNED by the corpus itself (twice).**
>
> **Evidence class: FIRST-PARTY, PROVEN BY EXECUTION.** The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-24-scripts/probe_schema.py`.
>
> **The single sentence this feature exists to make true:** *a staff member's role changes through a recorded event, by someone accountable, and the record survives the change.*

## Goal

Make the **roster's** authority mean **one thing**: a role is a recorded fact about a staff member, changed by a recorded event, with the event kept.

Concretely, three things:

1. **A role change must leave a record.** `UPDATE app_user SET role = ...` is accepted today, silently, and nothing records who changed it or when.
2. **A role change must be attributable.** "Who gave this person the manager role?" has no answer today.
3. **The change must not be a bare `UPDATE`.** The rule belongs to a write path, not to each caller — the corpus's own lesson from feature **444**.

**The charter rows this supports, verbatim** (`PROJECT_CHARTER.md`, §3.1 In scope v1):

> - **One Telegram bot, role-based via chat_id allowlist** (cook + manager).

and the charter's own §3.2 non-goal this slice must respect — **a role is an authorisation fact, and a role *event* is not a customer-facing AI surface**, so nothing here touches §3.2.

**The charter's own words on authority** (feature **403** quotes them): *"Manager approval by PIN for voids, large discounts and refunds."* **A role decides who may approve.** The thing that grants the authority is mutable and untraceable today.

## Scope

**In scope (v1):**

- **A role-change record** — one row per change: the staff member, the old role, the new role, the actor, the moment.
- **A write path that goes through it** — a role change is a recorded event, not a bare `UPDATE` on `app_user`.
- **A read helper** that returns a staff member's current role and, on request, their role history.
- **A regression check** that fails on today's shape and passes on the fixed one: after a role change, the old role is recoverable and the actor is recorded.
- **A cleanup note for the owner** if a live database already holds unrecorded role changes — **this slice cannot reconstruct them and must not pretend to.**

**Explicitly NOT in scope:**

- **Which roles may do what.** Feature **403** owns the role policy — the Telegram chat→role mapping and the role-permission table. **This slice owns the *change event*, not the policy.** 403's own text says the enum *"is declared and never consulted"*; **this slice does not make it consulted.**
- **The `UserRole` enum's membership.** The three members — `server`, `cook`, `manager` — stand. **No role is added, renamed or removed.**
- **The fact that enum columns have no membership constraint.** Feature **442** owns that, and it is a **hard dependency of correctness** for any check this slice writes (see *Dependencies*).
- **The staff member's name uniqueness.** Feature **462** owns it.
- **The staff PIN credential.** Feature **463** owns it, and feature **32** owns the config-level owner PIN. **No change to `pin_hash` behaviour.**
- **The staff's role in a visit.** Feature **451** owns *which role may be a visit's server*.
- **The bill closer's role.** Feature **443** owns it, and it explicitly says *"A `UserRole` change. Feature 403's territory"* — **that is the policy, and 403 owns it.**
- **Any change to `AppUser`'s columns** — no new column on `app_user`; the history is a table.
- **Any change to `Visit`, `Bill`, `OrderItem` or any other table.**
- **Any router beyond the role-change route, any new dependency, any Python file beyond `models.py` and the roster service.**
- **Any change to `index.html`** — the twelve-way collision zone.
- **Any change to `PROJECT_CHARTER.md`.**

## Description

### The defect, as executed

`backend/app/models.py`, verbatim:

```python
class AppUser(SQLModel, table=True):
    __tablename__ = "app_user"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    pin_hash: str     # bcrypt-hashed
    role: UserRole
```

**The role is a plain column and the whole schema carries no `CheckConstraint` and no trigger.** The executed guard census over LE31's **real schema**:

```text
PROBE D — schema-level guard census
  app_user       unique=[] check=[]
  ...
```

**`app_user` carries zero unique constraints and zero check constraints.** And the mutation, executed against the real schema:

```text
PROBE A — the staff role is mutable in place, with no trace and no guard
  UPDATE app_user SET role='manager' WHERE id=<cook>         ACCEPTED
  UPDATE app_user SET role='bogus_role' WHERE id=<server>    ACCEPTED
  UPDATE app_user SET name='Zed' WHERE id=<server>           ACCEPTED
  UPDATE app_user SET pin_hash='' WHERE id=<server>          ACCEPTED
  roles now: [(1, 'Ada', 'manager'), (2, 'Zed', 'bogus_role'), (3, 'Cy', 'manager')]
```

**Three separate findings in four lines:**

1. **A cook became a manager, silently, and nothing recorded it.** No event, no actor, no moment.
2. **A role was set to `'bogus_role'` — a value that is not a member of the enum — and it was accepted and stored.** (The membership gap itself is feature **442**'s; **this slice's finding is that the *change* is untraceable even when the value is legal**.)
3. **`pin_hash` was set to the empty string** — the credential column accepts an empty credential. (Feature **463** owns the credential; this is recorded here as adjacent evidence, **not** claimed by this slice.)

### The corpus already recorded this gap and left it open — twice

**Feature 470**, in its *Adjacent evidence*, verbatim:

> - **`UPDATE app_user.role server->manager` was ACCEPTED**, and `UPDATE app_user.name` was ACCEPTED. The corpus sweep for `appuser.{0,30}role.{0,30}(update|change|mutable)` returns **0 hits** — **no feature owns the staff-role change event.** Recorded, not filed.

**Feature 471**, in its *Adjacent evidence*, verbatim — the same finding, a second time, on a different day, by a different pass:

> - **`UPDATE app_user.role server->manager` was ACCEPTED.** Feature **462**/**463**/**464** each own one facet of the roster; **the role's mutability is a fourth.** Recorded, not filed.

**"No feature owns the staff-role change event. Recorded, not filed."** — twice. **That is the sixth instrument's shape exactly**: *a feature that found a defect, did not own it, and said so.*

**The corpus sweep confirms it is still unowned.** Over all **555** feature contracts and **511** HANDOFFs:

| pattern | hits | what they are |
|---|---|---|
| `staff.role.{0,40}(change\|event\|mutab)` | 1 | feature **470** — the recording |
| `role.{0,30}(change\|reassign\|promot)\w*\s*(event\|record\|log)` | 1 | feature **470** — the recording |
| `who changed.{0,20}role` | **0** | — |
| `role.{0,20}mutation` | **0** | — |

**The nearest neighbours, and why they do not own it:**

- **Feature 462** owns `AppUser.name` uniqueness — *"Any change to `AppUser` other than the `name` constraint. No new column, no new table, no change to `pin_hash`, `role` or `id`."* **It names `role` to disclaim it.**
- **Feature 463** owns the PIN credential — *"Nothing else on `AppUser` changes. `name`, `role` and `id` are untouched."* **Also a disclaimer.**
- **Feature 451** owns *which role may be a visit's server* — *"No change to `UserRole`. The enum's three members are already what the guard needs."* **Also a disclaimer.**
- **Feature 443** (bill closer's role) says, verbatim: *"A `UserRole` change. Feature 403's territory, and **adding a role is not the fix** — the defect is that **no rule exists**, not that the role set is wrong."* **443 points at 403 for the policy.** **403 is the policy — the mapping from a chat to a role, and what each role may do.** **403 owns no change event, and says nothing about who may change a role or when.**
- **Feature 403**'s own diagnosis, verbatim: *"**Zero** qualified read sites (`UserRole.server`, `UserRole.cook`, `UserRole.manager`) exist anywhere in `backend/`. The enum is declared and never consulted."*

**That last sentence is why this pick exists.** The role is **declared and never consulted** — so today nothing reads it, and a silent rewrite of it has no *visible* effect. **The moment 403 lands and the role starts deciding what a person may do, the untraceable rewrite becomes a live authorization defect.** **This slice is the companion 403 does not have: the event that says the authority moved.**

## Data model

**One new table. No new column on `app_user`.**

```python
class RoleChange(SQLModel, table=True):
    """Append-only record of every change to a staff member's role."""
    __tablename__ = "role_change"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="app_user.id", index=True)
    old_role: UserRole
    new_role: UserRole
    by_user_id: int | None = Field(foreign_key="app_user.id")
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
```

**Why a table and not a column.** A `previous_role` column on `app_user` preserves **one** change and loses the second. **A history is not a column** — the corpus has learned this three times (features **470**, **471**, **444**).

**Why append-only.** The same discipline feature **470** established for `stock_entry`: *"Never UPDATE or DELETE rows."* A role change is a sequence of facts, each true at a moment.

**Why `old_role` and `new_role` are both stored** rather than only `new_role`: the *current* role is on `app_user`; the history's job is to say **what it was before**. With only `new_role`, the history cannot answer "what was this person's role when they closed that bill on the 14th?" — and that is the question that matters.

**The nullable `by_user_id`.** A role may be changed by a migration or a seed; a history that refuses to record the actor is worse than one that records "unknown". **Feature **451** owns the actor-resolution seam — this slice reuses it and does not build authentication.**

## Implementation

**Files to touch:**

| file | change |
|---|---|
| `backend/app/models.py` | the `RoleChange` table |
| `backend/app/services/roster_service.py` *(new)* | `set_user_role(session, user_id, new_role, by_user_id)` — writes the change row **and** updates the column **in one transaction** |
| `backend/app/routers/staff.py` *(new or existing)* | the role-change route — a role change goes through the service, never a bare `UPDATE` |
| tests | a regression test that fails on today's shape |

**Order of work:**

1. **Add the table.** A new table, so `create_all()` creates it — **no migration needed.**
2. **Write the service function.** The change row and the column update in **one transaction.** A change row without the column update — or the reverse — is worse than neither.
3. **Write the route.** A role change goes through the service. **If a role can still be changed by a bare `UPDATE` anywhere, the guard is decorative.**
4. **Write the regression test.**

**The regression test, specified:**

```python
def test_a_role_change_leaves_the_old_role_recoverable(...):
    user = make_user(role=UserRole.server)
    set_user_role(session, user.id, UserRole.manager, by_user_id=manager.id)
    assert user.role == UserRole.manager
    changes = list_role_changes(session, user.id)
    assert changes[0].old_role == UserRole.server
    assert changes[0].new_role == UserRole.manager
    assert changes[0].by_user_id == manager.id
```

**The negative control (the check must be able to fail):** the same test with the service bypassed **must fail** — i.e. a bare `UPDATE app_user SET role` leaves no row, and the test must catch that. **If the test passes when the write path is bypassed, it proves nothing.**

**The membership check, and its dependency.** Because feature **442** records that LE31's enum columns are `VARCHAR` with **no membership constraint**, a stored role can be a value outside the enum. **The service must therefore validate the new role against `UserRole`'s members before writing** — and, per the corpus's own rule from feature **459**, that check belongs **in Python on the enum**, not as a SQL `WHERE role IN (...)` string list that can drift.

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface. **Feature 403** owns the Telegram role mapping and this slice does not touch it. *(If the owner wants the manager to promote a staff member from the bot, that is a separate feature that cites this one and cites 403.)*

## Dependencies

- **Feature 442** — **a HARD dependency of correctness, not of the feature.** 442 owns the fact that LE31's enum columns are `VARCHAR` with no membership constraint. **If 442 has landed, the stored representation may differ and this slice's validation must be re-checked against the real DDL.** This is the same dependency shape feature **452** records verbatim. **442 need not land first** — the Python-side enum check works either way — **but the DDL assumption must be re-verified if it has.**
- **Feature 403** — **adjacent.** 403 owns the role *policy* (the chat→role mapping and what each role may do). **This slice owns the role *change event*.** **403's own diagnosis — "the enum is declared and never consulted" — is why the event must exist before the enum starts being consulted.**
- **Feature 451** — **reused.** 451 owns the actor-resolution seam; this slice records `by_user_id` and reuses 451's resolution. **It does not build authentication.**
- **Feature 462** — **adjacent.** 462 owns `AppUser.name` uniqueness and explicitly disclaims `role`.
- **Feature 463** — **adjacent.** 463 owns the PIN credential and explicitly disclaims `role`. **The empty-`pin_hash` observation from the probe is 463's territory, not this slice's.**
- **Feature 443** — **adjacent.** 443 owns the bill closer's role and points the *policy* at 403.
- **Feature 464** — **adjacent.** 464 owns the roster's third facet (per the 471 recording).
- **Feature 470** and **feature 471** — **adjacent.** Both recorded this finding; both established the append-only and table-not-column shapes.
- **No migration dependency** — this slice adds a new table, which `create_all()` can create.

## Open questions

1. **Who may change a role?** The recommendation is **a manager or the owner** — but the role set has **no** `owner` member (only `server`, `cook`, `manager`). **Recorded default: a `manager` may change a role, and a staff member may not change their own.** **This is an owner decision and it is recorded, not made here** — and feature **403** owns the policy that would have to say it.
2. **Should the actor be allowed to be the subject?** (A manager promoting themselves.) **Recorded default: no** — a self-promotion is exactly the case an audit trail exists to make visible. **Recorded so the implementer does not decide it by accident.**
3. **Should a role change be reversible, and does the history record the reversal?** **Recorded default: yes, and yes** — a reversal is just another change, with its own row. **No `reverted_at` column.**
4. **Should the history expire?** **Recorded default: no.** A role history is small and its whole value is that it is complete.
5. **Should a role change notify anyone?** **Recorded default: no** — LE31 has no notification surface today, and this slice adds none. **Recorded so it is not silently assumed.**
6. **What happens to a visit whose server's role changed afterwards?** **Recorded default: nothing** — a visit records `server_id`, not a role snapshot. **The history answers "what was the role at the time" for anyone who asks.** **This is a deliberate choice, recorded.**

## Why this matters

**Because authority in a restaurant is a fact about people, and LE31 lets it change without a word.**

The failure mode is quiet. A cook becomes a manager; nobody knows; nothing is written down. **Today it is harmless** — feature **403** proved the role is *"declared and never consulted"*, so no decision has turned on it yet. **That is exactly the argument for fixing it now rather than later**: the moment 403 lands and the role starts deciding what a person may do — *"Manager approval by PIN for voids, large discounts and refunds"* — **an untraceable rewrite of that role is an authorization defect with no audit trail at all.** The corridor between "cook" and "manager" in LE31 v1 is **one `UPDATE` wide**, and it is unmonitored.

**And a restaurant's roster changes constantly.** Staff turnover is the normal condition of a small restaurant: a server leaves in March, a new cook starts in April, a manager covers the floor in August when someone is on holiday. **Each of those is a role change**, and each is currently invisible. When the owner asks the only question that matters — *who had the manager role on the night of the 14th, when the till did not balance?* — **LE31 cannot answer, because the answer was never written down.**

**The corpus knew, twice.** Features **470** and **471** each wrote, in their own words, *"no feature owns the staff-role change event"* and *"the role's mutability is a fourth … Recorded, not filed."* **Two passes, two days, two recordings, zero filings.** **The four features that do own the roster — 462, 463, 464 and 451 — each explicitly disclaim `role` in their own *Out of scope* lists.** The corpus has systematically closed every other facet of the roster and left exactly this one open. **This contract is that last facet.**

## Out of scope

*(Repeated at the end deliberately: the boundary is the point.)*

- **Which roles may do what, and the Telegram chat→role mapping** — **feature 403**.
- **The `UserRole` enum's membership** — no role is added, renamed or removed. **The enum's lack of a membership constraint** — **feature 442**.
- **The staff member's name uniqueness** — **feature 462**.
- **The staff PIN credential and the empty-`pin_hash` observation** — **feature 463** (and **feature 32** for the config-level owner PIN).
- **Which role may be a visit's server** — **feature 451**.
- **The bill closer's role** — **feature 443**.
- **The roster's other facets** — **feature 464**.
- **Any change to `AppUser`'s columns** — no new column on `app_user`; the history is a table. **A `previous_role` column preserves one change and loses the second.**
- **Any change to `Visit`, `Bill`, `OrderItem`, `MenuItem`, `Batch`, `StockEntry`, `Shift`, `DerivedTip` or `Table`.**
- **Any router beyond the role-change route**, any new dependency, any Python file beyond `models.py` and the roster service.
- **Any change to `index.html`** — the twelve-way collision zone.
- **Any change to `PROJECT_CHARTER.md`.**
