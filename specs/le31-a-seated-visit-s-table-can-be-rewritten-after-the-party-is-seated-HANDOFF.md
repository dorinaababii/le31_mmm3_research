# le31-a-seated-visit-s-table-can-be-rewritten-after-the-party-is-seated — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/538-le31-a-seated-visit-s-table-can-be-rewritten-after-the-party-is-seated-first-party-the-floor-map-reads-free-v1-visit-table-change-event.md`
> before touching any code.

## Frozen identifiers (do not rename)

- Feature ID: `538`
- Slug: `le31-a-seated-visit-s-table-can-be-rewritten-after-the-party-is-seated`
- Contract file: `features/538-le31-a-seated-visit-s-table-can-be-rewritten-after-the-party-is-seated-first-party-the-floor-map-reads-free-v1-visit-table-change-event.md`
- Bucket: **v1**
- Linear parent: **NOT CREATED** — see *Linear status* below.
- Linear sub-issue: **NOT CREATED** — see *Linear status* below. **Label `Feature`; project `le31 Research` (P-HMM-1).**

## ⭐ READ THIS BEFORE ORDERING ANY OTHER WORK

**This slice is the third half of a sentence feature 388 already wrote down.**

> **Feature 388**, verbatim: *"**Note on the derived helper:** `_table_status()` must be **rewritten** to read the stored column, not to keep deriving from `Visit`. **Two sources of truth that can disagree is the exact failure the pre-mortem names.** The derived form may be kept **only** as a consistency assertion in a test, never as the display source."*

**388 removes one source of truth (the derivation). It leaves the stored `table.status` to disagree with the stored `visit.table_id` — because nothing owns the relationship between them either.** This slice owns that relationship.

**And the shipped code proves the consequence.** `backend/app/routers/tables.py:64–71`, verbatim:

```python
def _table_status(table_id: int, session: Session) -> str:
    """Derive a table's current status from the latest open Visit."""
    visit = session.exec(
        select(Visit).where(Visit.table_id == table_id, Visit.closed_at == None)
    ).first()
    if not visit:
        return TableStatus.free.value
    return TableStatus.seated.value  # could be 'ordered' / 'billed' with more checks
```

**Six things must not be confused with it, and the corpus says so itself:**

| rule | mechanism | owner |
|---|---|---|
| a **second seat** on an occupied table opens a second visit | stored `Table.status` + API guard | **feature 388** |
| `party_size` vs `Table.seats` — does the party fit | a comparison at the seat | **feature 414** |
| `party_size` vs `adults + children` — is the composition coherent | a comparison at the seat | **feature 423** |
| the peak-party-count question | — | **feature 416**, `defer`red, **and it stays deferred** |
| `Table.seats`' lower bound | a value check | **feature 501** |
| the visit's **composition** after seating | event table + write-path guard | **feature 533** |
| **the visit's table after seating** | **event table + write-path guard** | **THIS SLICE** |

**⚠️ The one thing that can go wrong here is filing a duplicate of 388.** 388 owns the *status column*, the *seat guard* and the *`_table_status()` rewrite*. This slice owns *the pointer between the visit and the table*. **The implementer of 388 must not add a move guard and the implementer of this slice must not add the status column or rewrite the helper.**

**The single sentence this feature exists to make true:** *a party is seated at a table; the table it is at is a fact with a history; and the floor map and the order always agree about which table that is.*

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the contract file.

**Decision: `build`.** Bucket: **v1**.

**Evidence precondition: OBSERVED** — proved by **execution against LE31's own schema**: `SQLModel.metadata.create_all` on a throwaway SQLite file, seeded with two tables (T1 `seats=4`, T2 `seats=2`), one server, one open visit at T1 with `party_size=2`, one served order line and one paid bill.

`UPDATE visit SET table_id = <T2>` on the seated visit was **ACCEPTED**. The probe then read back **two numbers that must agree** — the count of open visits per table, which is exactly what the shipped `_table_status()` counts:

| what | value after the rewrite | should say |
|---|---|---|
| open visits on **T1** (`closed_at IS NULL`) | **0** | **1** — the party is still at T1 |
| open visits on **T2** (`closed_at IS NULL`) | **1** | **0** — nobody is at T2 |
| order lines on the visit | **1** | 1 — the order travelled with the visit |

**And the shipped helper's own answer, from the shipped helper's own query:**

```
  _table_status(T1)  ->  'free'      <-- the guest is sitting at T1
  _table_status(T2)  ->  'seated'    <-- nobody is at T2
```

The re-runnable probe is `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`.

**Confidence: high** for the defect (re-runnable; the numbers are in the contract, and the `_table_status()` answer came from the shipped function's query). **INFERRED for priority** — no code path moves a seated party today (there is no such route), so the defect is **latent**, not corrupting data.

**The finding shapes present:** omission (no table-change rule where one is needed), the **seventh shape** (a covered concept — the table's occupancy state, feature 388 — with an uncovered instance — the visit's own pointer to it), **upstream-of-filed-work** (388 is about to replace the derived status with a stored one, and nothing would keep the two in step), and the **duplicated-derivation** family inverted: two numbers that must agree and do not.

## Mandatory LE31 skill list (load these first)

1. `skills/le31-conventions/SKILL.md` — the seven-check gate, the naming conventions and the table conventions.
2. `skills/le31-backend/SKILL.md` — the backend layout, the SQLModel conventions and the write-path rules.
3. `skills/le31-data/SKILL.md` — the data-model conventions, the actor convention and the decimal rules.
4. `skills/le31-handoff-spec/SKILL.md` — this document's shape, for reference.
5. `skills/le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern this contract follows.
6. `skills/le31-coding-agent-brief/SKILL.md` — **produces the paste-in prompt automatically from this contract. Do not paste chat excerpts into a prompt.**

## Files the slice touches

- **`backend/app/models.py`** — **ADD** `class VisitTableChange` (`__tablename__ = "visit_table_change"`). **DO NOT** modify `Visit`, `Table`, `AppUser`, `OrderItem`, `Bill`, `Batch`, `StockEntry`, `Shift` or `DerivedTip`. **DO NOT** add `table_.status` — that is feature **388**'s column.
- **A new helper** — `backend/app/services/visit_service.py` (or the package feature **441** / **421** creates; **if `backend/app/services/` does not exist, create it and say so in the PR**). One function: `move_visit_to_table(session, visit_id, to_table_id, actor_id)`.
  - **DO NOT** put the helper in `routers/` — it is not a route.
  - **DO NOT** add the seat guard (388's) and **DO NOT** rewrite `_table_status()` (388's).
  - **DO NOT** add the capacity comparison (414's) or the composition comparison (423's).
- **Tests** — the regression tests listed in the contract's *Verification protocol*, including the **negative control**.

**NOT touched:** `index.html` (feature **08**'s scope; a thirteen-way collision zone — features 465/466/467/474/475/476/484/487/489/509/511/516), `backend/app/routers/tables.py` (feature **388**'s file), `backend/app/bot/cook_bot.py`, `PROJECT_CHARTER.md`, and every file outside `backend/app/models.py` and the new helper.

## Endpoints and contracts added

**None.** This slice adds **no route**, **no request shape** and **no response shape**. It adds a table, a helper and a rule.

**The refusal is part of the contract even though there is no route:** a move to an occupied table raises a legible error naming both tables and the destination's state — **feature 388's refusal, reached through 388's helper, not re-implemented here.**

## Telegram interaction

**None.** No Telegram surface is added or changed. The **cook bot** (`backend/app/bot/cook_bot.py`) is untouched — a table move is a floor-floor event.

## Verification protocol (end-to-end acceptance path)

**Re-run the probe first.** `/opt/data/le31-brainstorm-2026-11-27-scripts/probe_candidates.py`. **Before the fix it prints `ACCEPTED` and `open visits on T1 = 0`.** After the fix, the same probe must show the rewrite **refused**, and the shipped `_table_status()`'s own query must show **1** open visit on the table the party is at.

**The negative control is load-bearing.** A test that asserts "the move is refused" **must fail** when the guard is removed — comment out the refusal and watch the test go red. **A test that passes both with and without the guard proves nothing.**

The assertions, in order:

1. `UPDATE visit SET table_id` on a seated visit is **refused**; the visit's `table_id` is unchanged; **zero** `VisitTableChange` rows exist.
2. `move_visit_to_table(..., to_table_id=<free table>)` is **accepted**; exactly **one** change row exists with `from_table_id`, `to_table_id`, `by_user_id` and `at` correct; the visit's `table_id` moved; **both** tables' statuses are correct afterwards.
3. A move to an **occupied** table is **refused**; the visit is unchanged.
4. A **second** move produces a **second** row — **the case a `previous_table_id` column would have lost.**
5. A move to a table that **does not exist** is refused.
6. The consistency assertion holds: `visit.table_id == latest_change.to_table_id`, and **no** open visit sits on a table whose status is `free`.
7. A move writes **no** `StockEntry`, **no** `Bill` and **no** `OrderItem` row — a move relocates the party; it does not re-ring or re-bill anything.
8. `grep -rn "table_id = " backend/` returns the seat path and the move helper, **and nothing else**.

**⚠️ Postgres was NOT exercised** — `psycopg` is not importable in the verification venvs on this VPS (sqlmodel 0.0.48 / SQLAlchemy 2.1.6). **Every Postgres claim in the contract is proved from the DDL rendering and dialect behaviour, not a live round trip.**

**⚠️ The destination-capacity question is RECORDED, NOT DECIDED.** The contract's *Open questions* 1 says the move's destination guard *may* re-check capacity (feature 414's comparison) and escalates it. **The implementer must not silently decide it.** If the owner has not answered, the **recorded default** in the contract is to re-check capacity — and **the decision is recorded and escalated, not guessed**.

**⚠️ The demand is UNEVIDENCED.** No route moves a seated party today. The defect is **latent**. The contract says so in its *Evidence class* line and in *Why this matters*.

## Rollback / feature-removal path

1. Drop `VisitTableChange` (`DROP TABLE visit_table_change;`).
2. Delete the helper file, or reduce it to a single function that always refuses.
3. Remove the `VisitTableChange` import and class from `backend/app/models.py`.
4. Remove the tests.

**The rollback is safe because the slice is additive.** It adds a table and a helper and **changes no existing column** — so removing it cannot leave a half-migrated database. **The one caveat: if a move was ever recorded and then the feature is rolled back, the recorded moves are lost and the visit's current table is unrecoverable.** That is why the table is append-only and why the rollback step says to check for rows before dropping.

## What remains safe if removed

- **Every existing behaviour is unchanged.** No route, no request shape and no response shape is touched, so no client can notice the removal.
- **`visit.table_id` remains exactly as it is** — the same bare foreign key, with the same defect. **The defect returns with the feature; the slice only ever made it impossible to exercise.**
- **Feature 388's stored status column and its `_table_status()` rewrite are unaffected** — this slice does not add the column and does not rewrite the helper.
- **Features 414, 423, 416, 501, 533 are unaffected** — different comparisons, different columns, different events.

## Adjacent work (recorded, NOT picked)

- **`visit.server_id`** — the party's server is likewise rewritable after seating, **0** corpus hits for the mutation, **and feature **533**'s *Out of scope* says verbatim: *"**The visit's actor / `server_id`.** … **This slice does not change `server_id`.**"* **It is filed by this same pass as **feature 539**. **The two slices are pairwise disjoint** — 538 owns `table_id`, 539 owns `server_id` — and **neither may reuse the other's event table.**
- **`visit.party_size` / `adults` / `children`** — filed by the 108th pass as **feature 533**.
- **`visit.opened_at` / `closed_at`** — rewritable, and features **428** and **454** each mention `closed_at` in a *different* question (the open-visit aggregate; the close-without-a-bill case). **The timestamps' own mutability is a separate question, recorded here, not taken.**
- **`bill.closed_by`** — the bill's closer can be rewritten, **0** corpus hits for the mutation. **Feature **443** owns the comparison against `visit.server_id`; its own mutability is a separate question, recorded here, not taken.**
- **`stock_entry.reason` / `ref_order_item_id`** — rewritable in principle, **but feature **470**'s database trigger refuses **all** `UPDATE` and `DELETE` on `stock_entry`, so they are covered by a filed feature. **Not taken.**
- **`menu_item.photo_url`, `menu_item.is_prepared`, `batch.photo_url`, `batch.notes`, `batch.qty_start`** — all rewritable, **0** corpus hits for the mutation. **Recorded here so the next pass files them or discards them deliberately. None is taken.**
