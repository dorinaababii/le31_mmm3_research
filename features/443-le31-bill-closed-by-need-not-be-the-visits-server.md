# Feature 443 — `le31-bill-closed-by-need-not-be-the-visits-server`

> **Pick C of Daily Brainstorm 2026-11-05 (98th daily-brainstorm pass).** **FIRST-PARTY, and the gap was PROVEN BY EXECUTION on 2026-11-05 — not inferred from reading code.**
>
> LE31's own `backend/app/models.py` declares **two** user columns, and they sit in **two different tables**:
>
> ```python
> class Visit(SQLModel, table=True):
>     __tablename__ = "visit"
>     id: int | None = Field(default=None, primary_key=True)
>     table_id: int = Field(foreign_key="table_.id")
>     server_id: int = Field(foreign_key="app_user.id")     # <-- who SERVED the table
>     opened_at: datetime = Field(default_factory=utcnow, ...)
>     closed_at: datetime | None = Field(default=None, ...)
>     party_size: int
>     adults: int
>     children: int = 0
>
> class Bill(SQLModel, table=True):
>     __tablename__ = "bill"
>     id: int | None = Field(default=None, primary_key=True)
>     visit_id: int = Field(foreign_key="visit.id", unique=True)
>     subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
>     subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)
>     total_due: Decimal = Field(max_digits=10, decimal_places=2)
>     total_paid: Decimal = Field(max_digits=10, decimal_places=2)
>     payment_method: PaymentMethod
>     paid_at: datetime = Field(default_factory=utcnow, ...)
>     closed_by: int = Field(foreign_key="app_user.id")     # <-- who CLOSED the bill
> ```
>
> **`Visit.server_id` and `Bill.closed_by` are the same type, the same foreign key, and there is no rule relating them.**
>
> The parent proved the gap **by execution** — building LE31's real schema (`SQLModel.metadata.create_all` on a throwaway SQLite file), seating a party served by one user and closing the bill as **a different one**:
>
> ```
> server "Ana"  (UserRole.server)   ->  Visit.server_id
> cook  "Cyril" (UserRole.cook)     ->  Bill.closed_by
>
> INSERT INTO visit (table_id, server_id, party_size, adults) VALUES (1, <Ana>, 1, 1)
> INSERT INTO bill  (visit_id, ..., closed_by)               VALUES (<visit>, ..., <Cyril>)
> ```
>
> **ACCEPTED.** The bill was closed by the **cook**, on a visit served by the **server**. And the parent then confirmed the generalisation — a role check on `closed_by` does not exist either:
>
> ```
> SELECT DISTINCT role FROM app_user   ->  ['server', 'cook', 'manager']
> ```
>
> **The `UserRole` enum has three members and nothing anywhere says which of them may close a bill.** A manager may close it. A cook may close it. **Nobody has ever been asked.**
>
> **Why this matters concretely.** `Bill.closed_by` is the **accountability record** for the money. It answers the only question that matters when money is disputed: *"who took this payment?"* Today the schema records an actor **and records the server separately, side by side, without relating them** — so the answer is *"a user id"*, and the system cannot distinguish:
>
> - the **server who served the table and took the payment** (normal),
> - the **manager who closed the bill for the server** (also normal — the server may be off the floor),
> - the **cook who closed it** (not normal at all — a cook has no business taking a payment),
> - a **user who was never part of this visit at all** (not normal at all — and **not even prevented**).
>
> **Nothing distinguishes these four.** The column is a foreign key, so it names a **real user** — and that is the whole of its honesty. Feature **417** already established the generalisation about LE31's actor columns: *"the ledger accepts an actor who does not exist"* — that defect is fixed by adding an FK. **This defect is the one the FK cannot reach: the actor exists, and is still not a plausible closer.**
>
> **Boundary — this is NOT feature 403, NOT feature 415, NOT feature 417.**
> - **403** (`le31-role-based-bot-allowlist…`) owns the **role policy** — which chat id maps to which role, and what a role may do. Its *Adjacent work* says, of this very column, verbatim: *"Its three sibling classes that record **who did something** — `StockEntry.by_user_id`, `Shift.by_user_id`, `Bill.closed_by` — are all written. The one enum that describes **what kind of person** did something is never consulted."* **403 owns the capability map; it does not decide which roles may close a bill, and it explicitly does not touch `AppUser`.**
> - **415** (`le31-bill-closes-visit…`) owns the **bill-closes-visit edge** and the tip derivation. Its own text lists `Bill.closed_by → app_user.id` and `Visit.server_id → app_user.id` **on adjacent lines** and never relates them. **415 writes the edge; it does not constrain who may traverse it.**
> - **417** (`le31-stockentry-actor-foreign-key…`) owns the **actor FK** on the ledger. **Its own text names `Bill.closed_by` as a sibling that "is written"** — and its defect is *"the actor field has no foreign key"*, **not** *"the actor may be anyone"*. **A different column, and a different question.**
> - **379** (`le31-order-item-transition-actor-attribution…`) owns the **order-line transition's** actor. **This is the bill's actor.**
>
> **The three extra checks, answered explicitly** (the coverage-sweep contract requires all three):
> - **(a) Charter §3.2 non-goals?** **No.** §3.1 says *"operational transitions are explicit user actions"* and requires a **role-based** model; §3.6 says money is exact. **Who may take a payment is an operational transition.** The charter's §3.2 guest-data rule is about **counts, not identity** — and this rule is about **the staff member's role**, not about a guest. **Not a §3.2 non-goal.**
> - **(b) Already an open owner question?** **No.** 403's open question is *"which chat id maps to which role"*; 415's is *"which single-tender or split-tender shape"*; 417's is *"may `by_user_id` be NULL for a system actor"*; 394's is *"may a balance be negative"*. **None of them is "who may close a bill".**
> - **(c) Covered under different words?** **No.** A corpus-wide grep over **474 feature contracts + 440 HANDOFFs** for *"the bill's closer must be the visit's server"*, for *"who may close a bill"*, for *"bill close authority"*, for *"the bill's actor"*, and for *"manager closes for the server"* returned **zero hits** on every phrasing except the bare tokens `closed_by` (17 files) and `server_id` (33 files) — **which appear as column names in other features' context tables and never as a relation between the two.**
>
> **The external trigger (in-window, read in full).** `baba-dev/menuminute` (MIT ✓ §3.2, **★1/⑂0 = NO traction evidence in either direction**, TypeScript/Node + PostgreSQL + Drizzle, created **2026-10-13** AND pushed **2026-11-03** = **IN-WINDOW BY BOTH FIELDS**, README read in full, 13,808 B) — verbatim, from its *Approved architecture and implementation status* section:
>
> > *"Phase 2 adds organization/outlet management, **scoped roles**, durable projection jobs and **explicit billing entitlements**."*
>
> **"Explicit billing entitlements"** — the right to bill is a **role-scoped capability**, stated as a first-class thing in the architecture. And from its *approved product requirements* pointer:
>
> > *"…support for **worldwide multi-outlet scope**, **outlet-type onboarding, role permissions**, variants/add-ons, closing-time expiry and the initial 25-owner / 50-restaurant / 1,000-orders-per-hour planning envelope."*
>
> A system that treats **"who may bill"** as an explicit, role-scoped entitlement has had to answer *"is the person taking the payment the person who served the table, or somebody authorised to act for them?"* — and answered it **in the data model**. LE31 records the actor and the server **and never asks the question**.
>
> **Corroboration from a second in-window source (not picked).** `ahmedgaboelnaga/n8n-restaurant-order-inventory-automation` (MIT ✓ §3.2, **★1/⑂0**, created **2026-10-14** AND pushed **2026-10-14** = **IN-WINDOW BY BOTH FIELDS**, README read in full, 6,770 B) — verbatim, from its *Orders confirmation* workflow description:
>
> > *"Staff send `Done <order#>`, `Cancel <order#>`, or `Done <order#>` commands to a Telegram bot. The workflow updates the order status, decrements stock, and notifies staff."*
>
> The **same command** — `Done <order#>` — is sent by **any** staff member the bot accepts, and the workflow **does not distinguish who sent it**. **That is the same gap: the actor is recorded but not constrained.** ⚠️ **Off-stack** (n8n + Sheets) — **vocabulary only.**
>
> **Corroboration from a third in-window source (not picked).** `manoranjan2050/RestoPro-ERP-Web` (MIT ✓ §3.2, PHP/Laravel 12 + Livewire 3, created **2026-11-04** AND pushed **2026-11-05** = **IN-WINDOW BY BOTH FIELDS**, ★1, README read in full, 13,235 B) — its *Staff* section describes a **staff attendance register** and a **salary ledger with carry-forward**, i.e. **staff identity and role are a first-class modelled concept** in a restaurant back-office. Recorded as adjacent evidence; **no claim beyond its existence as an in-window MIT-licensed reference with a staff model.**

## Goal

Make LE31 able to answer **"who took this payment, and were they entitled to?"** — and to say so **from the schema**, rather than leaving the two user columns on `Visit` and `Bill` side by side, unrelated.

**The single sentence this feature exists to make true:** *a bill records not only who closed it, but whether that person was entitled to close it.*

Two concrete outcomes:

1. **The rule is stated, in the place an implementer will read it**, so the first bills router does not invent one.
2. **The two numbers that should agree are compared**: `Bill.closed_by` against `Visit.server_id` — and the schema says **what it means when they differ**, because *"the manager closed it for the server"* and *"the cook closed it"* must not be the same shape.

## Scope

**In scope (v1):**

- **One recorded rule** stating which roles may close a bill, and **what the relationship between `closed_by` and `server_id` means when they differ.**
- **One recorded decision** on whether the difference is **permitted** (a manager may close for a server) or **an error** (only the server may close), with the options stated and the trade-off named — **the decision itself is an owner decision and is not made here.**
- **One validation rule** at the write path, enforcing whatever the decision is, so that the *shape* of the difference is checked even if the *policy* is deferred.
- **One regression test** pinning the chosen rule.
- One row in `INDEX.md`'s "Active feature pipeline" table.

## Out of scope (v1)

- **Any write path.** No bills router exists (feature **415** builds it). `backend/app/routers/` holds only `__init__.py` and `tables.py`.
- **The bill-closes-visit edge.** Feature **415** owns it and its atomicity. **This feature does not create the edge and does not change its transaction.**
- **The tip derivation.** Feature **415** / feature **05**.
- **The role capability map.** Feature **403** owns `can(role, capability)`. **This feature does not add a capability to it** — it records **which capability** the bill close is, and states the rule. **If 403 has landed, this feature's rule should be expressed as a `can(role, "bill.close")` call rather than as a hand-rolled role list.**
- **The `StockEntry.by_user_id` actor FK.** Feature **417**. **A different column, and it already owns that one.**
- **The `Shift.by_user_id` actor.** Feature **391** (shift close) and **426** (shift close lifecycle). **Different table.**
- **The `Visit.server_id` FK.** It already exists and is correct. **This feature does not touch it.**
- **A `UserRole` change.** Feature **403**'s territory, and **adding a role is not the fix** — the defect is that **no rule exists**, not that the role set is wrong.
- **Guest identity.** The charter says v1 stores counts, not identities. **This rule is about a staff member's role, not a guest.**
- **Any retro-fitting of historical rows.** There are none — no bills router exists, so no `Bill` row has ever been written.

## Description

### What the schema says today

| Table | Column | Type | Meaning |
|---|---|---|---|
| `visit` | `server_id` | `int → app_user.id` | **who served the table** |
| `bill` | `closed_by` | `int → app_user.id` | **who closed the bill** |

**Both are foreign keys. Both are non-null. Neither is checked against the other. Neither is checked against a role.**

### The execution the parent performed

```
app_user:  id=1 "Ana"  role=server
app_user:  id=2 "Cyril" role=cook
app_user:  id=3 "Marta" role=manager

visit:  table_id=1, server_id=1 (Ana),   party_size=1, adults=1
bill:   visit_id=<that visit>, closed_by=2 (Cyril, the COOK), total_due=10.90, total_paid=15.00
        -> ACCEPTED

SELECT b.closed_by, v.server_id, u.role FROM bill b
  JOIN visit v ON v.id = b.visit_id JOIN app_user u ON u.id = b.closed_by
  -> closed_by=2  server_id=1  role='cook'
```

**The cook closed the bill. Nothing objected.** And `SELECT DISTINCT role FROM app_user` returns `['server', 'cook', 'manager']` — **three roles, and no rule saying which may close a bill.**

### The two numbers that should agree

| Number | Where it lives |
|---|---|
| `Bill.closed_by` | the **bill** |
| `Visit.server_id` | the **visit** |

**The parent's execution printed both sides. They disagreed, and nothing noticed.**

**⭐ The key observation is that they may legitimately disagree.** The manager closing the bill for an off-floor server is **normal restaurant operation**. So a rule of the form *"`closed_by` must equal `server_id`"* would be **wrong** — it would encode a workflow assumption the restaurant does not have.

**The correct rule is not an equality. It is a *set*.** The question is not *"is the closer the server?"* but *"is the closer **entitled** to close?"* — and the honest formulation of that is:

> `closed_by` must be **the visit's server**, **or a user whose role is permitted to close on the server's behalf.**

**That formulation is what this feature records. Which roles are permitted is the owner decision.** The schema's own vocabulary — `UserRole` with three members, and feature 403's `can(role, capability)` — already has the shape the rule needs.

### The failure this prevents

Today, when a customer disputes a payment, LE31 can say *"user 2 closed bill 1"*. It cannot say:

- whether user 2 **served** that table;
- whether user 2 **was allowed** to close it;
- whether user 2 was **even on shift**.

**The bill is the one record where accountability matters most** — it is the only place LE31 holds an amount of money that a person took. And its accountability column is a bare integer.

**Note the asymmetry with the ledger.** `StockEntry.by_user_id` records who moved stock. `Bill.closed_by` records who took money. **Both are bare integers. Neither is checked against the visit, the table, or the shift.** The ledger's defect (417) is that the actor may not exist; the bill's defect is that the actor may be **anyone at all**.

## Data model

**No new columns. No new tables.** The change is **one recorded rule**, **one validation at the write path**, and **one regression test**.

### The rule, in the form the schema can express it

```
Bill.closed_by  must satisfy ONE of:

  (a)  Bill.closed_by == Visit.server_id          -- the server closes their own table
  (b)  Bill.closed_by's UserRole is in BILL_CLOSE_ROLES   -- an authorised role closes for them

BILL_CLOSE_ROLES : set[UserRole]     -- OWNER DECISION, not made here
```

**The recorded default for (b), stated rather than implied:** **`{UserRole.manager}`.** A manager may close a bill on behalf of a server. **A cook may not** — a cook's job is the kitchen, and feature **00**-series ownership (the cook bot, feature 04) has no money surface.

**⚠️ The recorded default is a *default*, not a decision.** The owner's restaurant may have a **floor manager** who is a `server` with extra rights, or a **head chef** who does take payments at a counter. **This feature states the default and names the decision it defers.** The *shape* of the rule is settled; the *membership* of the set is not.

### Why the rule is a set and not an equality

**An equality rule would be wrong and would be wrong in production.** The parent records this explicitly because it is the plausible wrong answer:

- The server may be **off the floor** when the table asks for the bill.
- A **manager** may close it.
- A **shift handover** may mean the closing user served a *different* table.

**So the rule must permit a difference, and say what the difference means.** The alternative — forbidding the difference — would push the behaviour into the data: the manager would **write their own id into `server_id`**, or the schema would need a "closed on behalf of" column. **Both are worse.** This feature's rule keeps the two ids separate and says which combinations are legal.

**That is the "a covered concept, an uncovered INSTANCE" shape, applied to this pair.** The concept *"who did what"* is covered — feature 379 (order lines), 417 (the ledger's actor), 403 (the role map), 379's own wording about "the one enum that describes what kind of person did something". **The instance — the bill's closer, against the visit's server, with no rule — is unowned.**

### The validation, at the write path

```python
def assert_bill_closer_is_entitled(
    session: Session, bill: Bill, bill_close_roles: set[UserRole]
) -> None:
    """Raise ValueError if the closer is neither the visit's server nor an
    authorised role.

    (a) bill.closed_by == visit.server_id   -> allowed
    (b) role_of(bill.closed_by) in bill_close_roles -> allowed
    otherwise -> refused

    The bill's visitor must be read from the visit, not from the caller.
    """
```

**⚠️ Where the check lives is a decision with a real cost.** Options: (a) in the bills router (feature **415**), where it is one `if`; (b) in a `CHECK` constraint — **impossible**, because the check spans two tables; (c) as a database trigger — feature **413**'s territory, and **recorded, not adopted**; (d) in a service helper called by the router — **the recommended shape**, because it is testable without a router.

**This is the same "shape mismatch" the 91st pass found in the charter's role-based allowlist: a rule that crosses a table boundary cannot be expressed as a column constraint.** It must live in the application, and the contract says so.

## Implementation steps

1. **Record the rule** — add it to the bills feature's contract (feature **415**) or to this feature's own *Description*, in the form above, with `BILL_CLOSE_ROLES` named as an owner decision with the recorded default `{UserRole.manager}`.
2. **Add the helper** `assert_bill_closer_is_entitled(session, bill, bill_close_roles)` to `backend/app/services/billing_rules.py` (a new file; `backend/app/services/` does not exist yet).
3. **Add the resolver** `role_of(session, user_id) -> UserRole | None` — reads `AppUser.role`. **If feature 442 has landed, `role` is guaranteed to be a member; if not, this helper must handle an unknown value** (see *Dependencies*).
4. **Add the call site** to feature **415**'s bills router, **or**, if 415 has not landed, expose the helper and leave the call site, recording that in the commit message.
5. **Add the regression tests** `backend/tests/test_bill_closer_entitlement.py`:
   - `closed_by == visit.server_id` → **accepted**;
   - `closed_by` is a `manager`, `server_id` is a different user → **accepted**;
   - `closed_by` is a `cook`, `server_id` is a different user → **refused**;
   - `closed_by` names a user who served **a different visit** and holds no permitted role → **refused**.
6. **Verify by execution** — re-run the parent's probe against the patched code and assert the cook-closed-bill write is now refused.

## Telegram interaction if any

**None.** This feature adds no Telegram surface.

**Note for feature 04's cook bot:** the cook bot is a **cook**-role surface. If the cook bot is ever given a "close the bill" command — **which feature 415 does not propose** — then this rule would **refuse** it under the recorded default. **That is the desired behaviour and it is the reason the rule exists.** Recorded so the next pass does not "fix" the refusal by widening the role set.

## Dependencies

- **Feature 415** (`le31-bill-closes-visit…`) — **owns the bills router and the edge.** This feature supplies the **rule**; 415 supplies the **call site**. **Ordering: 415 first, or together.** If 415 lands first, **it will write `closed_by` from the request body** — which is exactly how a cook's id ends up on a server's bill. **This feature must land first or in the same PR.**
- **Feature 403** (`le31-role-based-bot-allowlist…`) — **owns the capability map.** If 403 has landed, express this rule as `can(role, "bill.close")` **and record that 403's `can()` gains the capability.** If 403 has not landed, use a local `BILL_CLOSE_ROLES` set and **record the duplication** so the next pass can collapse it.
- **⚠️ Feature 442** (`le31-enum-columns-are-varchar…`) — **optional but strongly recommended, and it is a *nice-to-have* here, not a dependency.** 442 constrains `AppUser.role` to the three declared members. Without it, `role_of()` can return a value that is **not** a `UserRole` — and the comparison against `BILL_CLOSE_ROLES` then **silently fails to match**, which is the safe direction (refuse). **So 442 is not a hard dependency: the failure mode without it is 'refuse', not 'allow'.** **That asymmetry is stated so the ordering is not made a hostage.**
- **Feature 417** (`le31-stockentry-actor-foreign-key…`) — **independent.** A different column on a different table.
- **Feature 391** / **426** (shift close) — **independent.** The `Shift.by_user_id` actor is a **different** actor on a **different** table. **Recorded, not bundled.**
- **Feature 379** (`le31-order-item-transition-actor-attribution…`) — **independent.** The order line's transition actor.
- **No new dependency.** The helper uses only `sqlmodel.Session` and the existing models.

## Open questions

1. **⭐ WHICH ROLES MAY CLOSE A BILL?** The recorded default is `{UserRole.manager}`. Options: (a) **server or manager** — the most permissive reading, admitting anyone who legitimately touched the table; (b) **manager only** — the strict reading; (c) **server or manager**, with the *server* case being the default and the *manager* case recorded as an override **on the bill** (which would need a column — **not recommended for v1**). **This is an owner decision and it is not made here.** The *shape* of the rule is settled by this contract; the *membership* of the set is the owner's.
2. **Should the difference between `closed_by` and `server_id` be RECORDED?** If a manager closes for a server, **the fact that it was an override is lost** — the bill says "closed by Marta" and the visit says "served by Ana", and nothing says whether that was normal or an exception. Options: (a) **accept the loss** — v1 has one bill per visit and one closer, and the *capability check* is the guarantee that it was permitted; (b) **add a boolean or a second FK** — costs a column and a migration. **The recommended position is (a) for v1**, because the *permission* is what matters and the *reason* is a reporting nicety. **Recorded, not decided.**
3. **What if the server has left the building?** (Their user is deactivated; the manager closes.) **Nothing in LE31 models user deactivation.** Feature **403**'s `BotChat` mapping has the same question. **Recorded — not this feature's.**
4. **Should `Bill.closed_by` be `NULL`-able for a system-closed bill?** (A nightly process closes unattended tables.) Feature **417** raises the identical question for `StockEntry.by_user_id` and answers it there. **This feature records that the same question exists and does not answer it twice.** **The recorded position: `closed_by` stays `NOT NULL` — a bill is closed by a person.**
5. **Does the *waiter* close the bill, or the *manager*?** Feature **415** says *"Waiter can close a bill"* (the charter's P0 row 47). **The charter says waiter, and `UserRole` has no `waiter` member — it has `server`.** **This is a naming mismatch between the charter and the enum, and it is recorded here rather than fixed, because renaming a role is feature 403's business.** **⚠️ The parent's execution shows the charter's word "waiter" has no home in the schema's role vocabulary.**

## Why this matters

**The bill is the only place LE31 records that a person took money. Its accountability column is a bare integer.**

Every other money-adjacent fact in LE31 is either derived (the tip) or reconciled (the shift's variance). The bill is the one row where **a human being is on the hook**, and it stores **who** — but not **whether they were allowed to**.

**The four states the schema cannot tell apart**, listed from most to least normal:

1. the **server** closed their own table — *normal*;
2. the **manager** closed it for a server who was off the floor — *normal*;
3. the **cook** closed it — *not normal*;
4. an **unrelated user** closed it — *not normal, and not even prevented.*

**Today all four produce an identical row shape.** The only difference is the integer in `closed_by`, and nothing reads it.

**Why this is worth a contract before the bills router exists.** This is the **upstream-of-filed-work** condition again, and it is the sharpest one in this pass. Feature **415** is going to write the bills router, and the router's obvious implementation is:

```python
bill = Bill(visit_id=..., subtotal_items=..., total_paid=..., closed_by=request.closed_by, ...)
```

**`closed_by` taken from the request body.** That is the plausible wrong answer — and it means **the client chooses the account the money is booked to.** If 415 lands without a rule, the write path will take the actor from the caller, and **the schema's two user columns will have been in place since day one, unrelatable, with nothing ever checking them.** The cheap moment to state the rule is now, before the router exists — because **once the router exists, the rule becomes a breaking change to a live endpoint.**

**The cost of getting it right.** One recorded rule, one helper, one test file. Roughly **2–3 hours**, fully reversible. **The cost of getting it wrong** is a bill that can be closed by anyone, on a ledger of accountability that no feature reads — in a product whose entire claim is that the numbers are right.

## Adjacent evidence

- **`baba-dev/menuminute`** — MIT ✓ §3.2, **★1/⑂0 = NO traction evidence in either direction**, TypeScript/Node + PostgreSQL + Drizzle + Better Auth, created **2026-10-13** AND pushed **2026-11-03** = **IN-WINDOW BY BOTH FIELDS**, README read in full (13,808 B). Verbatim: *"Phase 2 adds organization/outlet management, **scoped roles**, durable projection jobs and **explicit billing entitlements**."* — **"Explicit billing entitlements"** is the right to bill, modelled as a role-scoped capability. ⚠️ **Off-stack** (TypeScript/Postgres) — **vocabulary only, no code adopted.**
- **`ahmedgaboelnaga/n8n-restaurant-order-inventory-automation`** — MIT ✓ §3.2, **★1/⑂0**, n8n + Google Sheets + Telegram, created **2026-10-14** AND pushed **2026-10-14** = **IN-WINDOW BY BOTH FIELDS**, README read in full (6,770 B). Verbatim: *"Staff send `Done <order#>`, `Cancel <order#>`, or `Done <order#>` commands to a Telegram bot."* — **the same command from any staff member; the actor is recorded but not constrained.** Off-stack — vocabulary only.
- **`manoranjan2050/RestoPro-ERP-Web`** — MIT ✓ §3.2, PHP/Laravel 12 + Livewire 3, created **2026-11-04** AND pushed **2026-11-05** = **IN-WINDOW BY BOTH FIELDS**, ★1, README read in full (13,235 B). Its *Staff* section models a **staff attendance register** and a **salary ledger** — **staff identity and role are first-class in a restaurant back-office.** Recorded as adjacent evidence.
- **`ycy-ui/DineReserve`** — MIT ✓ §3.2, PHP, created 2026-10-06, pushed 2026-11-04, ★1, README read in full (10,086 B). Verbatim: *"During service **the host is also the person answering the phone**… staff see the floor plan, check parties in, mark no-shows and read occupancy reports."* — **the host serves several functions at once**, which is the *real-world reason* the two ids must be allowed to differ. **Recorded as the reason the rule is a set, not an equality.**

## Adjacent work — recorded, NOT picked

One source artifact touching several invariants → **pick one, record the rest.**

| Rule (source) | LE31's owner | Disposition |
|---|---|---|
| *"explicit billing entitlements"* (menuminute) | feature **403** (capability map) | **Recorded.** 403 owns the map; this feature names **one capability** in it. |
| *"Staff send `Done <order#>`"* (n8n) | feature **421** (the ledger write path) | **Recorded.** The same "any staff member" shape on the stock side. Not bundled. |
| *"the host is also the person answering the phone"* (DineReserve) | — | **Recorded.** The reason the two ids may legitimately differ. |
| staff attendance / salary ledger (RestoPro) | — | **Recorded.** Staff identity as a first-class concept. Not in scope for v1. |
