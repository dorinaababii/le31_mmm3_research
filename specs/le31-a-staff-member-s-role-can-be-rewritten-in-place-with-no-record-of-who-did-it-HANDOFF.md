# le31-a-staff-member-s-role-can-be-rewritten-in-place-with-no-record-of-who-did-it — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/524-le31-a-staff-member-s-role-can-be-rewritten-in-place-with-no-record-of-who-did-it-v1-role-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `524`
- Slug: `le31-a-staff-member-s-role-can-be-rewritten-in-place-with-no-record-of-who-did-it`
- Contract file: `features/524-le31-a-staff-member-s-role-can-be-rewritten-in-place-with-no-record-of-who-did-it-v1-role-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the fourth facet of the roster that the corpus left open.** Two features, on two different days, by two different passes, found this exact defect and both wrote *"recorded, not filed"*:

> **Feature 470**, *Adjacent evidence*: *"**no feature owns the staff-role change event.** Recorded, not filed."*

> **Feature 471**, *Adjacent evidence*: *"Feature **462**/**463**/**464** each own one facet of the roster; **the role's mutability is a fourth.** Recorded, not filed."*

**Four features own the roster. Every one of them explicitly disclaims `role` in its own *Out of scope* list:**

| facet | owner | what it says about `role` |
|---|---|---|
| the staff member's **name** | **feature 462** | *"No new column, no new table, no change to `pin_hash`, `role` or `id`."* |
| the staff **credential** | **feature 463** | *"Nothing else on `AppUser` changes. `name`, `role` and `id` are untouched."* |
| the roster's third facet | **feature 464** | — |
| **which role may be a visit's server** | **feature 451** | *"No change to `UserRole`."* |
| **which roles may do what** | **feature 403** | the **policy** — the chat→role mapping |
| **the role's change event** | **THIS SLICE** | — |

**⚠️ THE TIMING ARGUMENT, and it is the reason this slice is filed now rather than when 403 lands.** Feature **403**'s own diagnosis, verbatim: *"**Zero** qualified read sites (`UserRole.server`, `UserRole.cook`, `UserRole.manager`) exist anywhere in `backend/`. The enum is declared and never consulted."* **Today a silent role rewrite has no visible effect — because nothing reads the role.** **The moment 403 lands and the role starts deciding what a person may do (*"Manager approval by PIN for voids, large discounts and refunds"*), an untraceable rewrite of that role becomes a live authorization defect with no audit trail.** **This slice is the companion 403 does not have.**

**⚠️ DO NOT IMPLEMENT THIS AS A COLUMN.** A `previous_role` column on `app_user` preserves **one** change and loses the second. **A history is a table** — the corpus has learned this three times (features 470, 471, 444).

**The single sentence this feature exists to make true:** *a staff member's role changes through a recorded event, by someone accountable, and the record survives the change.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with three `AppUser` rows. `UPDATE app_user SET role='manager' WHERE id=<cook>` was **ACCEPTED**; `UPDATE app_user SET role='bogus_role'` was **ACCEPTED and stored**; `UPDATE app_user SET pin_hash=''` was **ACCEPTED**. The probe also read the schema's constraint lists directly: **`app_user` carries 0 `UniqueConstraint`s and 0 `CheckConstraint`s**, and **every `ondelete` in all ten tables is `None`**.

The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-24-scripts/probe_schema.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path changes a role today, so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no change event where one is needed), unenforced mechanism (a column that grants authority with nothing enforcing or recording it), and the "corpus hand-off" shape (a defect recorded twice and filed never).

**Two probe bugs were found and corrected during this pass, and the corrections matter for anyone re-running this:** a first probe labelled a **failed** write as "ACCEPTED" because it rolled back and swallowed the exception (the `bill.visit_id` duplicate was **refused** by the unique constraint, exactly as it should be), and an early probe pointed at a non-existent directory and failed with `unable to open database file`. **Both were probe defects, not product defects. The numbers in the contract are the corrected ones.**

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **the new `RoleChange` table.** No change to `AppUser`'s columns.
- `backend/app/services/roster_service.py` (NEW) — `set_user_role()` and `list_role_changes()`.
- `backend/app/routers/staff.py` (NEW or existing) — the role-change route, which must go through the service.
- `backend/tests/test_role_change_event.py` (NEW) — the regression test.

**Do NOT touch:** `AppUser`'s columns, `UserRole`'s members, `Visit`, `Bill`, `OrderItem`, any other table, any other router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `previous_role` column, a new role member, a native Postgres `ENUM` type (feature **388** records that it does not port between SQLite and Postgres), a PIN or login mechanism (features **463** and **32**), a Telegram role mapping (feature **403**).

## Endpoints and contracts added

One route: the staff role change. **It writes the change row and the column in one transaction**, and it is the only way a role may change.

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface. **Feature 403** owns the Telegram role mapping and this slice does not touch it.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; confirm features **403**, **442**, **451**, **462**, **463**, **464**'s status.
2. **The history is the acceptance criterion.** Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | a `server` promoted to `manager` | **both** the column and one change row exist |
   | the change row's `old_role` | **`server`** |
   | the change row's `new_role` | **`manager`** |
   | the change row's `by_user_id` | **the actor** |
   | the change row's `at` | **set** |
   | a role change to a value **outside** the enum | **REFUSED** — validated in Python against `UserRole`'s members |
   | a staff member changing **their own** role | **REFUSED** (per *Open questions* 2) |
   | a role change that does not change the role | **no row** |

   **The probe that produced today's numbers is `probe_schema.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"UPDATE app_user SET role='manager' WHERE id=<cook> ACCEPTED … roles now: [(1, 'Ada', 'manager'), (2, 'Zed', 'bogus_role'), (3, 'Cy', 'manager')]"*.
3. **⭐ THE ENUM-VALIDATION CHECK MUST BE IN PYTHON, NOT SQL.** Feature **442** records that LE31's enum columns are `VARCHAR` with **no membership constraint**, so a stored role can be a value outside the enum. **Per feature **459**'s rule, the comparison belongs in Python on the enum — a SQL `WHERE role IN ('server','cook','manager')` is a duplicated string list that can drift from the enum.** **Assert the check is the Python one.**
4. **The negative control** — change the role with a **bare `UPDATE`** and confirm the regression test **fails** (no row is written). **A test that passes when the write path is bypassed proves nothing.** This is the single most important check in this slice.
5. **Two rows, one transaction** — assert the change row and the column update commit together. Force the failure and assert nothing is written.
6. **The table, not a column** — assert `app_user` still has exactly the columns it has today, and that a `role_change` table exists.
7. **The Postgres rendering** — assert the DDL renders. **⚠️ Postgres was NOT exercised** (see *Adjacent work*).
8. **Regression** — features **403**, **442**, **451**, **462**, **463**, **464** and **443** must be unaffected. **Note for 442:** if 442 has landed, the stored representation of the enum column may differ and the validation must be re-checked against the real DDL — the same dependency shape feature **452** records.
9. **End-to-end** — through the API's terms: promote a staff member, confirm the roster read shows the new role, confirm the history read shows the old role and the actor.

## Rollback / feature-removal path

- Remove the `RoleChange` table from `backend/app/models.py`.
- Remove `backend/app/services/roster_service.py` and the role-change route.
- Remove `backend/tests/test_role_change_event.py`.
- **The table is additive**, so the rollback is a plain drop — **no migration is needed to undo it.**
- **Data loss:** the history rows are lost. **That is the only thing this slice creates, and it is the thing the slice exists to keep.**
- **⚠️ Roles changed before the slice landed have no history and cannot be reconstructed.** Record the count in the PR description; **do not fabricate the missing history.**

## What remains safe if removed

- A staff member's role can be rewritten with no record of what it was, who changed it, or when — **which is the defect.** Do not describe the removal as neutral.

## Adjacent work (recorded, NOT picked)

- **`UPDATE app_user.pin_hash -> ''` was ACCEPTED** — the credential column accepts an empty credential. **Feature 463** owns the credential; this is recorded here and **not** claimed by this slice.
- **`UPDATE app_user.name` was ACCEPTED** — feature **462** owns the name's uniqueness; the *mutability* of the name is adjacent. **Recorded, not picked.**
- **Which roles may change a role** — see *Open questions* 1. **The role set has no `owner` member** (only `server`, `cook`, `manager`), so the recommendation is a `manager`. **An owner decision, recorded not made.**
- **The catalogue's delete path** — **feature 522**; **the catalogue's price history** — **feature 523**. Both filed in this same pass.
- **The SQLite foreign-key pragma** — feature **427**. Not a dependency of this slice.
