# le31-a-seated-visit-s-party-size-can-be-rewritten-after-the-party-is-seated — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/533-le31-a-seated-visit-s-party-size-can-be-rewritten-after-the-party-is-seated-first-party-nothing-records-it-v1-visit-composition-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `533`
- Slug: `le31-a-seated-visit-s-party-size-can-be-rewritten-after-the-party-is-seated`
- Contract file: `features/533-le31-a-seated-visit-s-party-size-can-be-rewritten-after-the-party-is-seated-first-party-nothing-records-it-v1-visit-composition-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the third rule in a family the corpus has already filed twice — for the other two spoken identifiers.**

> **Feature 526**: *"A table may carry an empty label — the one name the waiter says out loud may be nothing."*
> **Feature 527**: *"A table whose area is spelled differently is invisible on the floor map."*
> **Feature 458**: *"A menu item's name is not unique — two dishes may share the one name the waiter says out loud."*
> **Feature 462**: *"An app user's name is not unique — two staff may share the one name the owner calls out."*

**The pattern is explicit and repeated: a fact the operator speaks out loud must be present, must be spelled one way, and must be unique.** `party_size` is the operator's spoken fact about **how many** are at the table — and it has **none** of the three properties.

**Four things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| does the party **fit** the table (`party_size` vs `Table.seats`) | a comparison at the seat | **feature 414** — filed |
| does the composition **add up** (`party_size` vs `adults + children`) | a comparison at the seat | **feature 423** — filed |
| how many people may **join** (the peak count) | a growth rule | **feature 416** — filed as **`defer`**, and it **stays deferred** |
| may `Table.seats` be **zero** | a lower bound | **feature 501** — filed |
| **the composition being rewritten after the seat** | **event table + write-path guard** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is REVIVING FEATURE 416.** 416 asks *"what if the party grew?"* and is **`defer`red** because the need is INFERRED. **This slice does not revive it.** This slice is not about *how many* people may join — it is about the fact that **if** the number changes, **the change is recorded.** **416's question stays parked; a later pass may close it, and this slice is where its answer should land.**

**The single sentence this feature exists to make true:** *a visit's party composition is written once, when the party is seated; afterwards it is a fact with a history.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with a 4-seat `Table`, one `AppUser` and one `Visit` with `party_size=2, adults=2, children=0`. `UPDATE visit SET party_size=40, adults=40` was **ACCEPTED** — **a party of two, at a four-seat table, became a party of forty.** The probe compared **two numbers that should agree**: `table_.seats` = **4** against `visit.party_size` = **40** — **the comparison feature 414 makes at the seat now fails, silently, on the stored value.** The full schema census confirmed **zero `CHECK` constraints across all ten tables.**

The probe is re-runnable: `/opt/data/le31-brainstorm-2026-11-26-scripts/probe_round2.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract). **INFERRED for priority** — no code path changes a visit's composition today, so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no write-once rule where one is needed), the **seventh shape** (a covered concept — "the party size is right", owned twice by 414 and 423 — with an uncovered instance — "the party size cannot be quietly replaced"), and a **held-fact gap** (the spoken-fact family of 526, 527, 458 and 462, with its third member unfiled).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

- `backend/app/models.py` — **one new append-only table**, the visit-composition change event (visit id, the three old values, the three new values, `by_user_id`, `at`). **No column is added to `visit`.** Nothing else in the file changes.
- `backend/app/services/visits_service.py` (NEW) — the composition-change helper: it either refuses, or it writes the event and the change in one transaction. **It does not rewrite the seat route's semantics** — feature **388** owns that.
- `backend/tests/test_visit_composition_change.py` (NEW) — the regression test.

**Do NOT touch:** `Visit`'s columns, `Table`, `Bill`, `OrderItem`, `MenuItem`, `Batch`, `StockEntry`, `DerivedTip`, `Shift`, any router, `index.html`, `PROJECT_CHARTER.md`.

**Do NOT add:** a `previous_party_size` column (it preserves one change and loses the second — feature **523** states this rule), a capacity comparison in the post-seat path (**that is feature 414's rule and 414 does not own the post-seat case**), a growth or peak-count rule (**feature 416 is `defer`red and stays that way**), a `CHECK (adults + children = party_size)` constraint (**feature 423** names it as *not* a schema constraint and enforces it in the router — do not change that), a browser-side capacity check (**feature 486**).

## Endpoints and contracts added

**None.** This slice adds no route. **The seat route exists** (`POST /api/tables/{id}/seat`) — this slice adds the **helper and the guard** beside it, and **does not change what the route accepts**. A future route that changes a composition calls the helper.

## Telegram interaction

**None.** No bot command, no FSM state, no chat surface.

## Verification protocol (end-to-end acceptance path)

1. **Pre-flight**: load all five mandatory LE31 skills; confirm the contract file matches the frozen identifiers above; confirm the statuses of features **388**, **414**, **416**, **423**, **486** and **501**.
2. **The write-path guard is the acceptance criterion** — a schema constraint cannot carry this rule (the database has no notion of a row's history). Build LE31's schema with `SQLModel.metadata.create_all` against a throwaway SQLite file and assert:

   | scenario | expected |
   |---|---|
   | the **seat write** creates the visit with its composition | **ACCEPTED** (the guard must not block the legitimate write) |
   | change `party_size` on a seated visit (`closed_at IS NULL`), **no** event | **REFUSED**, stored composition unchanged |
   | change the composition on a seated visit **with** an event in the same transaction | **ACCEPTED**, event carries all six old and new values, actor, time |
   | update or delete an event row | **REFUSED** |
   | `party_size == adults + children` after any accepted change | **still holds** — feature 423's rule is not broken by this slice |

   **The probe that produced today's numbers is `probe_round2.py` in the research-side scripts directory; run it against the pre-change schema FIRST to watch it fail.** Its output: *"UPDATE visit SET party_size=40, adults=40 (table seats=4) -> ACCEPTED"* and *"visit now: party_size=40 adults=40 children=0"*.
3. **The two-numbers check** — after any accepted change, `visit.party_size` and the visit's own event history must agree on the current composition. **A single number never shows a divergence.**
4. **The negative control** — remove the guard and confirm the regression test **fails**. **A test that passes without the guard proves nothing.** This is the single most important check in this slice.
5. **Regression** — features **388** (the seat write and the table-state machine), **414** (the capacity comparison), **423** (the composition comparison), **416** (the peak count — must stay `defer`red), **486** (the browser-side capacity check), **501** (`Table.seats`' lower bound), **06** and **29** (the KPI formulas), **443** and **451** (the actor) must all be unaffected. **⚠️ Feature 06 and 29's formulas keep their definitions — this slice changes no formula; it only stops the denominator being silently replaced.**
6. **End-to-end** — through the API's terms: seat a party of two at a four-seat table, attempt to change the composition without an event and confirm the refusal; then change it *with* an event and confirm the event's six values, actor and time.

## Rollback / feature-removal path

- Remove the event model from `backend/app/models.py`.
- Remove `backend/app/services/visits_service.py`.
- Remove `backend/tests/test_visit_composition_change.py`.
- **⚠️ Rolling back requires the same migration work as applying it** — dropping a table cannot be done by `create_all()` either. **Record the prod-migration step in the PR description.**
- **No data loss of existing rows:** the slice adds no column to any existing table. **The event rows it creates are history; dropping the table discards that history — record the count before dropping.**

## What remains safe if removed

- A seated visit's party size can be rewritten silently again — **which is the defect.** Do not describe the removal as neutral.
- The day's covers and the revenue per cover can be moved by a typo, with no record — **which is the defect.**

## Adjacent work (recorded, NOT picked)

- **The order line's quantity being rewritten after the line exists** — **feature 531**, filed in this same pass. **Same family, different table.**
- **The bill's money columns being rewritten after the close** — **feature 532**, filed in this same pass. **Same family, different table.**
- **The peak-count / party-growth question** — **feature 416**, filed as `defer`. **It stays `defer`red. This slice records that the number moved; it does not decide how many people may join.**
- **The table's spoken facts** — **features 526** (an empty label), **527** (an area spelled two ways), **460** (the area's spelling), **501** (`seats = 0`), **520** (two tables on one coordinate). **The spoken-fact family — this slice is its third member for the visit.**
- **The table's label uniqueness** — **feature 455**; **the menu item's name uniqueness** — **feature 458**; **the staff name's uniqueness** — **feature 462**.
- **A question this slice deliberately does not answer** — should a change that raises `party_size` above `Table.seats` be refused outright? See *Open questions* 3 in the contract. **It is recorded, not decided.**
