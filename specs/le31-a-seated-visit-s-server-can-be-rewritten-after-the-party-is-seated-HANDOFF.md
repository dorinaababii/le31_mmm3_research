# le31-a-seated-visit-s-server-can-be-rewritten-after-the-party-is-seated — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/539-le31-a-seated-visit-s-server-can-be-rewritten-after-the-party-is-seated-first-party-nothing-records-it-v1-visit-server-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `539`
- Slug: `le31-a-seated-visit-s-server-can-be-rewritten-after-the-party-is-seated`
- Contract file: `features/539-le31-a-seated-visit-s-server-can-be-rewritten-after-the-party-is-seated-first-party-nothing-records-it-v1-visit-server-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice completes a guarantee that feature 451 filed, and 451's own words show it did not know it was incomplete.**

> **Feature 451**, verbatim: *"The role is checked at the write path. A visit may only be attributed to a user holding `UserRole.server`."*
>
> and, verbatim: *"**No change to `Visit.server_id`'s type, its nullability, or its foreign key.** The column stays exactly as it is. This feature adds the **rule** that makes the reference meaningful."*

**A write-path rule is a rule about a *moment*, not about the *data*.** 451's predicate ran once, at creation. The value can then be moved to anybody in the roster — including the **cook** and the **manager**, whom 451's rule exists to keep out. **The role check is bypassed, not merely undone.**

**And the two numbers that must agree are exactly feature 443's pair.** 443 exists to answer *"who took this payment, and were they entitled to?"* — and after a rewrite the schema shows a visit whose server is a manager and a bill closed by a server, **with nothing recording that they were ever the same person.**

**Six things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| a visit's server must hold `UserRole.server` | a role check **at creation** | **feature 451** |
| the actor is resolved server-side, not asserted by the client | an actor-resolution seam | **feature 451** |
| the bill's closer vs the visit's server — what a difference *means* | a schema-level statement | **feature 443** |
| the visit's **composition** after seating | event table + write-path guard | **feature 533** |
| the visit's **table** after seating | event table + write-path guard | **feature 538** |
| **the visit's server after seating** | **event table + write-path guard** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is filing a duplicate of 451.** 451 owns *the predicate*. This slice owns *when the value may change*. **Fixing 451 without this feature produces a guarantee over a value that can move; fixing this without 451 produces a handover that may land on a cook.**

**The single sentence this feature exists to make true:** *a party belongs to a server from the moment they are seated; after that, a change of server is a recorded handover, not a silent rewrite.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with three staff (a `server`, a `cook` and a `manager`), one visit whose `server_id` pointed at the server, one order line and one paid bill whose `closed_by` was that same server.

`UPDATE visit SET server_id = <the manager>` on the seated visit was **ACCEPTED**. The probe then read back **two numbers that must agree**:

| what | value after the rewrite | should say |
|---|---|---|
| `visit.server_id` | **the manager** | **the server** — the party belongs to the server |
| `bill.closed_by` | **the server** | the server |

**Nothing raised, nothing was logged, and nothing records that the two columns ever agreed.**

The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path reassigns a seated party today (there is no such route), so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no server-change rule where one is needed), the **seventh shape** (a covered concept — the role predicate, feature 451 — with an uncovered instance — the value it was checked against), **upstream-of-filed-work** (443's comparison is meaningless if the column can move after the comparison's premise was set), and the **duplicated-derivation** family inverted: two numbers that must agree and do not.

## Mandatory LE31 skill list (load these first)

1. `skills/le31-conventions/SKILL.md` — the seven-check gate, the naming conventions and the table conventions.
2. `skills/le31-backend/SKILL.md` — the backend layout, the SQLModel conventions and the write-path rules.
3. `skills/le31-data/SKILL.md` — the data-model conventions, the actor convention and the decimal rules.
4. `skills/le31-handoff-spec/SKILL.md` — this document's shape, for reference.
5. `skills/le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern this contract follows.
6. `skills/le31-coding-agent-brief/SKILL.md` — **produces the paste-in prompt automatically from this contract. Do not paste chat excerpts into a prompt.**

## Files the slice touches

- **`backend/app/models.py`** — **ADD** `class VisitServerChange` (`__tablename__ = "visit_server_change"`). **DO NOT** modify `Visit`, `AppUser`, `OrderItem`, `Bill`, `Batch`, `StockEntry`, `Shift` or `DerivedTip`. **DO NOT** add an `is_active` column (feature **464**) and **DO NOT** change `UserRole` (feature **524**).
- **A new helper** — `backend/app/services/visit_service.py` (or the package feature **441** / **421** creates; **if `backend/app/services/` does not exist, create it and say so in the PR**). One function: `hand_over_visit(session, visit_id, to_server_id, actor_id)`.
  - **DO NOT** put the helper in `routers/` — it is not a route.
  - **DO NOT** add a second role check — **feature 451's predicate is reused through 451's helper.**
  - **DO NOT** change `bill.closed_by`, and **DO NOT** decide what a difference between it and `visit.server_id` means — that is feature **443**'s rule.
  - **DO NOT** build a shift-change trigger — features **426** / **391** own the shift's lifecycle.
- **Tests** — the regression tests listed in the contract's *Verification protocol*, including the **negative control**.

**NOT touched:** `index.html` (feature **08**'s scope; a thirteen-way collision zone — features 465/466/467/474/475/476/484/487/489/509/511/516), `backend/app/routers/tables.py` (feature **388**'s file), `backend/app/bot/cook_bot.py` (feature **403**'s chat-role mapping), `PROJECT_CHARTER.md`, and every file outside `backend/app/models.py` and the new helper.

## Endpoints and contracts added

**None.** This slice adds **no route**, **no request shape** and **no response shape**. It adds a table, a helper and a rule.

**The refusal is part of the contract even though there is no route:** a handover to a staff member who does not hold `UserRole.server` raises a legible error naming the target's actual role — **feature 451's refusal, reached through 451's helper, not re-implemented here.** **The message must match 451's shape**, because a surface that cannot express the refusal will swallow it.

## Telegram interaction

**None.** No Telegram surface is added or changed. The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched — the Telegram chat-id → role mapping is feature **403**'s territory and is explicitly out of scope here.

## Verification protocol (end-to-end acceptance path)

**Re-run the probe first.** `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`. **Before the fix it prints `ACCEPTED`.** After the fix, the same probe must show the rewrite **refused**.

**The negative control is load-bearing.** A test that asserts "the handover is refused" **must fail** when the guard is removed — comment out the refusal and watch the test go red. **A test that passes both with and without the guard proves nothing.**

The assertions, in order:

1. `UPDATE visit SET server_id` on a seated visit is **refused**; the visit is unchanged; **zero** `VisitServerChange` rows exist.
2. `hand_over_visit(..., to_server_id=<a server>)` is **accepted**; exactly **one** change row exists with `from_server_id`, `to_server_id`, `by_user_id` and `at` correct; `visit.server_id` moved.
3. A handover to a **`cook`** is **refused**, and the error names the target's actual role.
4. A handover to a **`manager`** is **refused** — **feature 451's own *Open questions* records the recommendation *"no"*; this slice follows the recorded default and does not re-open the owner's decision.**
5. A **second** handover produces a **second** row — **the case a `previous_server_id` column would have lost.**
6. The consistency assertion holds: `visit.server_id == latest_change.to_server_id`.
7. **`bill.closed_by` is unchanged** by a handover — a handover relocates the party's owner; it does not rewrite who took the money.
8. `grep -rn "server_id = " backend/` returns the seat path and the handover helper, **and nothing else**.

**⚠️ Postgres was NOT exercised** — `psycopg` is not importable in the verification venvs on this VPS (sqlmodel 0.0.48 / SQLAlchemy 2.1.6). **Every Postgres claim in the contract is proved from the DDL rendering and dialect behaviour, not a live round trip.**

**⚠️ The shift-change question is RECORDED, NOT DECIDED.** The contract's *Open questions* 2 says the handover helper does **not** itself check the shift — the caller asserts it, and the event records when it happened. **The implementer must not build a shift-change trigger**; features **426** and **391** own that, and this slice must not depend on them.

**⚠️ The demand is UNEVIDENCED.** No route reassigns a seated party today. The defect is **latent**. The contract says so in its *Evidence class* line and in *Why this matters*.

## Rollback / feature-removal path

1. Drop `VisitServerChange` (`DROP TABLE visit_server_change;`).
2. Delete the helper file, or reduce it to a single function that always refuses.
3. Remove the `VisitServerChange` import and class from `backend/app/models.py`.
4. Remove the tests.

**The rollback is safe because the slice is additive.** It adds a table and a helper and **changes no existing column** — so removing it cannot leave a half-migrated database. **The one caveat: if a handover was ever recorded and then the feature is rolled back, the recorded handovers are lost and the visit's current server is unrecoverable.** That is why the table is append-only and why the rollback step says to check for rows before dropping.

## What remains safe if removed

- **Every existing behaviour is unchanged.** No route, no request shape and no response shape is touched, so no client can notice the removal.
- **`visit.server_id` remains exactly as it is** — the same bare foreign key, with the same defect. **The defect returns with the feature; the slice only ever made it impossible to exercise.**
- **Feature 451's role predicate keeps working at creation.** This slice does not own it and does not change it.
- **Feature 443's comparison between `bill.closed_by` and `visit.server_id` is untouched.**
- **Features 415, 524, 464, 533, 538 are unaffected** — a different column, a different rule, a different event table.

## Adjacent work (recorded, NOT picked)

- **`visit.table_id`** — the party's table is likewise rewritable after seating, **0** corpus hits for the mutation. **It is filed by this same pass as **feature 538**. **The two slices are pairwise disjoint** — 538 owns `table_id`, 539 owns `server_id` — and **neither may reuse the other's event table.** They may land in either order, or in one PR with the two tables kept separate.
- **`visit.party_size` / `adults` / `children`** — filed by the 108th pass as **feature 533**.
- **`visit.opened_at` / `closed_at`** — rewritable, and features **428** and **454** each mention `closed_at` in a *different* question (the open-visit aggregate; the close-without-a-bill case). **The timestamps' own mutability is a separate question, recorded here, not taken.**
- **`bill.closed_by`** — the bill's closer can be rewritten, **0** corpus hits for the mutation. **Feature **443** owns the comparison against `visit.server_id`; its own mutability is a separate question, recorded here, not taken.**
- **`app_user.name`** — rewritable, and features **526**, **527** and **458** own the *spoken-name* family (presence, spelling, uniqueness) on other entities. **The staff name's own mutability is a separate question, recorded here, not taken.**
- **`shift.by_user_id` / `shift.opened_at` / `shift.closed_at`** — rewritable, **0** corpus hits for the mutation. **Feature **426** owns the shift close lifecycle and **536** owns the opening float's history. **The shift's own columns' mutability is a separate question, recorded here, not taken.**
- **`stock_entry.reason` / `ref_order_item_id`** — rewritable in principle, **but feature **470**'s database trigger refuses **all** `UPDATE` and `DELETE` on `stock_entry`, so they are covered by a filed feature. **Not taken.**
