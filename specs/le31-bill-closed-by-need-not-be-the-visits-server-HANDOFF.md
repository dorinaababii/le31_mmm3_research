# HANDOFF — le31-bill-closed-by-need-not-be-the-visits-server

> **Slice contract for the coding agent.** Produced by the 98th LE31 daily-brainstorm pass (2026-11-05), Pick C.
>
> **Feature file**: `features/443-le31-bill-closed-by-need-not-be-the-visits-server.md`
>
> **LE31 feature gate verdict**: **build** — evidence class **OBSERVED** (executed against LE31's real schema: `SQLModel.metadata.create_all` on a throwaway SQLite file, then a `Visit` with `server_id=<the server>` and a `Bill` with `closed_by=<the cook>` — **ACCEPTED**; and `SELECT DISTINCT role FROM app_user` returned `['server','cook','manager']` with **no rule anywhere saying which of them may close a bill**). All seven checks pass; see the feature file's *Description* and *Why this matters*.

## Trigger policy

This is a **`build`** contract. The external coding agent **is** authorised to implement this slice, and to do so **without asking**.

**What the agent MAY do, and should do without further scoping:**

1. Load the active feature file and this handoff.
2. Load **`le31-conventions`** — §3.2 (the fixed stack, `init_db()`-not-Alembic, no new dependency), §4.1 (SQLite dev / Postgres prod), §7 (the quality bar), the truth invariant, and the **seven-check feature gate**.
3. Load **`le31-v1-feature-pattern`** — the contract shape, the slicing rules, and the *Definition of Done*.
4. **Read `features/415-…` FIRST** and confirm the ordering described under *Frozen contract* below. **Feature 415 is about to write the bills router, and the plausible implementation takes `closed_by` from the request body — which is how a cook's id ends up on a server's bill.**
5. **Create `backend/app/services/billing_rules.py`** with `assert_bill_closer_is_entitled(session, bill, bill_close_roles)` — **one definition of the rule.** It reads the **visit** (not the caller) and the closer's role, and raises `ValueError` when the closer is neither the visit's server nor a holder of a permitted role.
6. **Define `BILL_CLOSE_ROLES` as a named constant with the recorded default `{UserRole.manager}`** — **and mark it clearly as an owner decision the owner may change.** **The agent may implement the default; the agent may NOT change the default.**
7. **Apply the helper at the write path** — feature 415's bills router if it exists; **otherwise expose the helper and leave the call site, recording that in the commit message.**
8. **Write the regression test first, watch it fail, then apply the change and watch it pass.** The test that matters most is `test_cook_closing_a_servers_bill_is_refused` — it is what proves the rule is not decorative.
9. **Record the deferral-chain correction** — one line in `features/415-…` *Adjacent work*, saying *"who may close a bill is feature 443."*

**What the agent MUST NOT do** — each of these is another feature's territory, and widening into any of them is a defect, not initiative:

- **Create the bills router, or the bill-closes-visit edge.** That is **feature 415**. **⚠️ ORDERING: 415 must land after this, or in the same PR.** **This feature does not create a router.**
- **Add the tip derivation, or change `DerivedTip`.** That is **features 415 / 05**.
- **Add the `BotChat` table, the capability map, or any read site for `UserRole`.** That is **feature 403**. **If 403 has landed, express the rule as `can(role, "bill.close")` — and record that 403's `can()` gains the capability. If 403 has not landed, use a local `BILL_CLOSE_ROLES` set and record the duplication.**
- **Add the `StockEntry.by_user_id` foreign key.** That is **feature 417**. **A different column on a different table.**
- **Add the `Shift.by_user_id` actor, or the shift close lifecycle.** That is **features 391 / 426**.
- **Add the `Visit.server_id` foreign key.** It already exists and is correct. **Do not touch it.**
- **Add a `UserRole` member — in particular a `waiter`.** That is **feature 403 / 421** territory. **The charter says "Waiter" and the enum says `server`; that naming mismatch is recorded (feature file *Open questions* 5) and is NOT this slice's to fix.**
- **Add a column to `Bill`** — not a boolean "closed on behalf of", not a second FK. **The recommended position is to accept the loss** (feature file *Open questions* 2). **If the agent believes a column is needed, it must record that as a deviation, not add it silently.**
- **Make `Bill.closed_by` nullable.** The recorded position is that it stays `NOT NULL` — a bill is closed by a person. **Feature 417 raises the identical question for the ledger; do not answer it twice.**
- **Constrain `AppUser.role`'s value set.** That is **feature 442**. **This feature does not add a `CHECK`.**
- **Introduce Alembic**, or write a migration. Charter §3.2: `init_db()` is the v1 policy. **No `Bill` row has ever been written.**
- **Change `PROJECT_CHARTER.md`.** The charter is the owner's document.

**Disambiguation**: this slice is about **who is entitled to close a bill**. It is **not** about the bill's arithmetic (408/415/435), the bill's membership (435), the tip formula (415/420), the ledger's actor (417/441), or the role policy (403).

## Frozen contract

**The one thing this contract exists to make true:** *a bill records not only who closed it, but whether that person was entitled to close it.*

Concretely, after this slice lands:

1. A bill whose `closed_by` **is** the visit's `server_id` is **accepted**.
2. A bill whose `closed_by` holds a **permitted role** (the recorded default: `manager`) and differs from the visit's `server_id` is **accepted** — **because the manager may close for a server who is off the floor.**
3. A bill whose `closed_by` holds a **non-permitted role** (the cook) and differs from the visit's `server_id` is **refused**.
4. A bill whose `closed_by` names a user who **served a different visit** and holds no permitted role is **refused**.
5. **The rule is a set, not an equality.** `closed_by == server_id` is **one** permitted case, not **the** rule.

**The prohibition:** *a rule of the form "`closed_by` must equal `server_id`"*, and *a bills router that takes the account-holder from the request body.*

### The 415 ordering — resolve before writing code

| If | Then |
|---|---|
| **415 has not landed** (today's state) | 443 lands alone. The helper is created and **exported**; the call site is left to 415. **The commit message must say so.** |
| **415 has landed first** | 443's helper **must** be called from 415's bills router, and 415 **must not** take `closed_by` from the request body. **If 415's router writes `closed_by=request.closed_by` and this rule is not in place, the client chooses the account the money is booked to — and that is the failure this contract exists to prevent.** |
| **403 has landed** | Express the rule as `can(role, "bill.close")` and **record the capability addition in 403's text.** |
| **403 has not landed** | Use a local `BILL_CLOSE_ROLES` set with the recorded default `{UserRole.manager}`. **Record the duplication** so the next pass can collapse it into 403's map. |
| **442 has landed** | `AppUser.role` is guaranteed to be one of the three members, so `role_of()` cannot return an unknown value. **If 442 has NOT landed**, `role_of()` must handle an unknown value — and the recorded behaviour is that an **unknown role is refused** (the safe direction), not allowed. |

### Why the rule is a **set** and not an equality

**An equality rule would be wrong in production.** The parent records this explicitly because it is the plausible wrong answer:

- The server may be **off the floor** when the table asks for the bill.
- A **manager** may close it.
- A **shift handover** may mean the closing user served a *different* table.

**`ycy-ui/DineReserve`'s README (in-window, MIT, read in full) states the reason directly:** *"During service **the host is also the person answering the phone**… staff see the floor plan, check parties in, mark no-shows and read occupancy reports."* **The host serves several functions at once** — so the two ids must be *allowed* to differ.

**The alternative — forbidding the difference — is worse, and the contract says why:** it pushes the behaviour into the data. The manager would **write their own id into `server_id`**, or the schema would need a "closed on behalf of" column. **Both are worse than keeping the two ids separate and stating which combinations are legal.**

### Why the check lives in the application and not in a `CHECK` constraint

A `CHECK` constraint **cannot** express this rule: it would have to compare `bill.closed_by` with `visit.server_id` across **two tables**, and SQLite `CHECK` constraints may only reference columns of the row's own table. **A database trigger could** — that is **feature 413**'s territory, and it is **recorded, not adopted**, because **triggers exist in Postgres and not in SQLite** (413 has already recorded that), so a trigger would reintroduce a dev/prod divergence.

**So: one helper, called at the write path, in a service module — testable without a router.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `backend/app/services/__init__.py` | **create** | `backend/app/services/` **does not exist today.** ⚠️ **Features 421, 441 and 442 also want to create it** — if one of them has landed, **extend that package, do not replace it.** |
| `backend/app/services/billing_rules.py` | **create** | `assert_bill_closer_is_entitled(session, bill, bill_close_roles)`, plus `role_of(session, user_id) -> UserRole \| None`. |
| `backend/app/services/billing_rules.py` | — | `BILL_CLOSE_ROLES: set[UserRole] = {UserRole.manager}` — **named, with a comment recording that it is an owner decision with this default.** |
| `backend/app/routers/bills.py` | **create or modify** | Feature 415's router, **if it exists**. **If it does not exist, do NOT create it** — leave the helper exported and record that. |
| `backend/tests/test_bill_closer_entitlement.py` | **create** | The four regression tests listed below. **Confirm the project's test path before assuming this one.** |
| `features/415-le31-bill-closes-visit…` | **modify** | One line in *Adjacent work*: who may close a bill is feature 443. |

**Not touched:** `backend/app/models.py` (no schema change), `backend/app/routers/tables.py`, `backend/app/db.py`, `backend/app/bot/`, `backend/app/config.py`, `index.html`, `PROJECT_CHARTER.md`, every other model.

## Mandatory LE31 skill list

The coding agent **must** load these before writing code. They are in the project repo at `skills/`, and on this VPS they are **not** in the standard `skills_list` index — read them from disk:

- **`le31-conventions`** — `skills/le31-conventions/SKILL.md`. **The fixed stack, the hard invariants, and the seven-check gate.**
- **`le31-v1-feature-pattern`** — `skills/le31-v1-feature-pattern/SKILL.md`. **The contract shape and the Definition of Done.**
- **`development`** → `speckit-specify` / `speckit-plan` / `speckit-tasks` / `speckit-implement`. **Product behaviour changes go through the development pipeline.**
- **`pre-merge-review`** — **product code does not merge on the author's say-so.** An independent reviewer must sign off.

**Also read (not skills, but mandatory context):** `features/415-…` (the bills router), `features/403-…` (the role capability map), `features/417-…` (the actor FK), `features/379-…` (the order line's transition actor), `features/435-…` (the bill's membership), `features/442-…` (the enum membership constraint), and `PROJECT_CHARTER.md` §3.1 and §3.2.

## Mandatory inputs

| Input | Where | Why |
|---|---|---|
| `PROJECT_CHARTER.md` §3.1 (explicit user actions; role-based), §3.2 (non-goals) | repo root | **§3.1 is the requirement.** **§3.2's guest-data rule is about counts, not identity — and this rule is about a staff member's role, so it is NOT a §3.2 non-goal.** |
| `features/415-…` (bill closes visit; the tip derivation) | `features/` | **The ordering dependency.** Read it first. |
| `features/403-…` (role-based bot allowlist; the capability map) | `features/` | **Where the capability belongs.** |
| `features/417-…` (the actor FK) | `features/` | The sibling actor column, and the boundary. |
| `features/379-…` (transition actor attribution) | `features/` | The sibling attribution concept. |
| `features/435-…` (bill membership) | `features/` | **Different fact: what the bill charged vs who closed it.** |
| The parent's proof script | `/opt/data/le31-brainstorm-2026-11-05-scripts/audit_lifecycle3.py` | **The parent's execution transcript for this finding** (probe H). Run it with `/opt/data/le31-verify-2026-10-27/.venv/bin/python` — that venv has `sqlmodel`/`fastapi`/`pydantic` installed; **the system Python does not have `sqlmodel`.** |
| The pass report | `/opt/data/le31-brainstorm-2026-11-05.md` | The pass, the evidence, and the rejected alternatives. |

## Verification protocol reference

**Reference**: `skills/le31-research-workflow/SKILL.md` (the curl-only anti-fabrication and signed-delta discipline) and `skills/le31-first-party-defect-proving/SKILL.md` (the execution-proof method). **Read `le31-first-party-defect-proving` — this feature was proven that way and the agent must preserve that property in its own tests.**

**The four required regression tests** (all in `backend/tests/test_bill_closer_entitlement.py`):

1. `test_server_closing_their_own_bill_is_accepted` — `closed_by == visit.server_id` → **no raise**.
2. `test_manager_closing_for_an_absent_server_is_accepted` — `closed_by` is a `manager`, `server_id` is a different user → **no raise**. **This is the test that proves the rule is a set, not an equality.**
3. `test_cook_closing_a_servers_bill_is_refused` — `closed_by` is a `cook`, `server_id` is a different user → **raises**.
4. `test_unrelated_user_closing_a_bill_is_refused` — `closed_by` is a user who served a **different** visit and holds no permitted role → **raises**.

**Method — the one that matters:** **write the tests first, watch them fail against the current code, then apply the change and watch them pass.** A test that only ever passed proves nothing.

**End-to-end before commit** (charter §7): run the actual bills route — **or, if no bills route exists, the actual helper** — against a real database and observe the behaviour change. **Do not declare done from a diff or from green tests alone.**

**Anti-fabrication:** every claim in the PR description must be traceable to a command you ran and its output. **No number, no status code and no test count that you did not observe.**

## Rollback path

**Fully reversible, and deliberately so.**

- **The code rollback:** delete `services/billing_rules.py`, delete the test file, revert the one-line note in `features/415-…`, and remove the helper call from the router. **Nothing today writes a `Bill`, so no existing behaviour can regress.**
- **The data rollback:** **there is nothing to roll back.** No bills router exists; **no `Bill` row has ever been written.**
- **The migration rollback:** LE31 uses `init_db()` (charter §3.2 — **Alembic is a non-goal for v1**), so there is no migration file to revert. **If a migration file is created anyway, that is a scope violation of this contract.**
- **The one irreversible thing:** **if a bill is closed by an unauthorised user while this feature is in flight, the accountability record is wrong and there is no audit trail to reconstruct who *should* have closed it.** The `Bill` row is not append-only, but the *knowledge* that it was wrong is lost the moment the row is written. **This asymmetry — cheap now, unrecoverable later — is why this contract states the rule before the router exists.**

**Rollback cost:** minutes. **No data is at risk.**

## Sign-off gap

**What this contract does NOT establish, and the agent must not assume:**

- **That the bill's closer is the *only* accountability record.** It is not — `StockEntry.by_user_id` and `Shift.by_user_id` are the siblings, and **this slice does not constrain them.** Recorded, not bundled.
- **That the owner agrees with `{UserRole.manager}`.** It is a **recorded default**, not a decision. **The agent must implement the default and flag it clearly for the owner.** **If the owner says "any server may close any bill", that is a one-line change to the constant — not a re-specification.**
- **That "waiter" is a role.** It is not — `UserRole` has `server`, `cook`, `manager`, while the charter's P0 row 47 says *"Waiter can close a bill"*. **That naming mismatch is recorded (feature file *Open questions* 5) and is NOT this slice's to fix.**
- **That the rule survives a schema rebuild.** It is application-layer, so it does — but only if the **call site** is re-established. **A helper with no caller is not a rule** — see the boundary table.
- **That feature 403's capability map exists.** It does not. **If it does not, this rule is a local constant and the duplication must be recorded** so a later pass can collapse the two.
- **That feature 442 constrains `AppUser.role`.** It does not, today. **An unknown role must be REFUSED** — the recorded safe direction.

## Handoff summary

One helper, one named constant with a recorded default, one call site (or one exported helper with no caller), one test file, one one-line note. **Two to three hours.**

The gap was **proven by execution**, not inferred: LE31 has **two** user columns — `Visit.server_id` (*who served the table*) and `Bill.closed_by` (*who closed the bill*) — and **the schema records them side by side and never relates them**. The parent seated a party served by one user and closed the bill as **the cook**, and **the database accepted it**. `UserRole` has three members and **nothing anywhere says which of them may close a bill.**

**The one boundary that must not be crossed:** feature **415** owns *how a bill closes the visit*; this feature owns *who may close it*. **And the ordering is the sharpest point: 415 is about to write the bills router, and the plausible implementation takes `closed_by` from the request body — which means the client chooses the account the money is booked to.** **The cheap moment to state the rule is now, before the router exists, because once the router exists the rule becomes a breaking change to a live endpoint.**

**The one thing that must not happen:** a rule of the form *"`closed_by` must equal `server_id`"*. **The manager closing the bill for a server who is off the floor is normal restaurant operation** — and `ycy-ui/DineReserve`'s README says so in one line: *"During service the host is also the person answering the phone."* **The rule is a set, not an equality.**
