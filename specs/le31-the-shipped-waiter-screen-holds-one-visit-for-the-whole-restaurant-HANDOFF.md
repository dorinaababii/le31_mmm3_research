# HANDOFF — Feature 474: the shipped waiter screen holds one visit for the whole restaurant

> **Slice contract for the coding agent.** Feature: `features/474-le31-the-shipped-waiter-screen-holds-one-visit-for-the-whole-restaurant-first-party-seating-a-second-party-destroys-the-first-partys-order-v1-per-table-order-state.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (executed under `node` on 2026-11-13).
> Filed by: Daily Brainstorm 2026-11-13 (daily pass), Pick A.

---

## 1. The active feature path

```
features/474-le31-the-shipped-waiter-screen-holds-one-visit-for-the-whole-restaurant-first-party-seating-a-second-party-destroys-the-first-partys-order-v1-per-table-order-state.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 388 / 465 / 466 / 467 / 01, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | The shipped `index.html` (30,530 bytes, 719 lines, mounted at `/` by `backend/app/main.py`) executed under `node` on 2026-11-13: the seat handler `state.visit = { table_id: t.id, ..., items: [] }` was run against the file's own `MOCK_TABLES` fixture and the file's own `state` literal. **Table T3's three lines (Schnitzel / Fries / Coke) were gone after a second party was seated; the floor map still showed T3 as `ordered`; the bill handler would have alerted "No items to bill."** |
| 2 | The defect is in LE31's own code | **PASS** | `index.html` declares exactly one visit for the whole restaurant: `let state = { visit: {...}, bills: [] };` — one object, one table. The fixture beside it holds **three** concurrently occupied tables (T2 `seated`, T3 `ordered`, P2 `seated`). **The shipped fixture describes a floor the shipped code cannot represent.** `features/01-table-management.md`'s own sketch shows the same: `[T2 🟡 party 4]  [T3 🔴 bill]` and `[T6 🟠 ord.]` — three occupied tables. |
| 3 | No filed feature owns it | **PASS** | Feature **388** owns the **API-side** seat guard and the stored `Table.status`; its *Out of scope* says verbatim: *"Any waiter-UI change beyond what the API response implies (the UI is `index.html`, feature 01's scope)."* Feature **465** quotes `state.visit.items.reduce(...)` **only as the site of the float arithmetic**; its *Scope* is *"This slice changes no Python file"*. Feature **467** owns the fixture↔API drift **check**. Feature **01** is an **informal spec** — no `## Out of scope`, no gate verdict, no verification protocol. **Three filed features defer the waiter UI to feature 01's scope, and feature 01 is not a contract.** |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **388** = the API's stored status + the API's seat guard. **465** = the browser's money arithmetic. **466** = the seat form's `Adults` input bound. **467** = the fixture↔API drift check. **474** = **the screen's state model** — whether the screen can hold more than one party. **Four different questions; the file regions are disjoint.** |
| 5 | The demand is real | **PARTIAL — recorded honestly** | No operator has reported a lost order — **the mock-up makes zero `fetch()` calls**, so there is no live surface on which this could misfire. **Yet the mock-up's own fixture puts three parties on the floor at once**, so the defect is visible the moment anyone opens the file and seats a second table. |
| 6 | It is cheap now and expensive later | **PASS** | One file, one data structure, no schema change, no Python change, no endpoint. Expensive later: **the first party's lines are overwritten, not hidden** — `state.visit = {...}` replaces the whole object, so the Schnitzel, Fries and Coke no longer exist anywhere in the program. Reconstructing them later requires a manual audit of live service history with no ground truth. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — it fires, on features 465 / 466 / 467 and 388** | **465** is about to land a money helper in the same file and would faithfully leave the state model untouched; **466** is about to change the seat modal's inputs — the same handler 474 changes; **467** is about to add the drift check, which would compare a fixture against an API while the screen still holds one visit; **388** is about to add the API's seat guard. **All four must cite 474, or 474 lands first.** |

**Overall: `build`.** The weakest link is check 5, weak for the same mechanical reason as the other two picks of this pass: **the surface that would produce the complaint does not exist yet.** That is also the reason it is cheap.

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `index.html` | **The `state` object, the floor-grid handler, the seat handler, the order renderer, the bill handler, the close handler** | **One file. No build step** (§4.1: *"vanilla HTML + JS. No build step"*). The regions are disjoint from 465 / 466 / 467 but the file is shared. |
| `features/01-table-management.md` | **Nothing, or one pointer line** | It is an **informal spec**. 474 adds a contract **beside** it. **Do not rewrite the spec's semantics.** |
| `features/465-…`, `features/466-…`, `features/467-…`, `features/388-…` | **One line each** — name 474 as the sibling slice in the same file | 465/466/467 share `index.html`; 388 owns the API half of the seat rule. |

**Do NOT touch:** `backend/app/models.py` (**388** owns `Table.status`), `backend/app/routers/tables.py` (**388** owns the API guard, **451** owns the actor, **436** owns the active-visit write guard), any `Decimal` declaration, the tax rate (**408**), the money helper and the bill modal's arithmetic (**465**), the seat modal's input attributes (**466**), `MOCK_TABLES` (**467** owns the fixture's reconciliation), the fixture's status values, `backend/app/bot/cook_bot.py`.

## 4. The implementation, in order

1. **Replace `state.visit` with `state.visits` + `state.active_table_id`.** `state.visits` is a map keyed by **table id**. **Do not leave a `state.visit` alias behind** — a second name for the same concept is how the next reader reintroduces the bug.
2. **Seed `state.visits` from the fixture.** T2, T3 and P2 are occupied in `MOCK_TABLES`; **each needs an entry**, or the mock-up still shows a floor the code cannot hold. **T3 keeps the three lines the shipped `state` literal carries; T2 and P2 get empty item lists** — a table can be seated without having ordered. **Do not modify `MOCK_TABLES`** (467 owns it).
3. **Add the switch-to-table action.** Tapping a table with an entry in `state.visits` sets `active_table_id` and renders that party's order. Tapping a `free` table opens the seat modal.
4. **Add the UI-side seat guard.** The seat handler must check the target table's status before `t.status = 'seated'`. If the table is not `free`, **refuse, say so, and switch to the existing party**. **This is the UI's copy of feature 388's API rule** — the two must use the same refusal semantics, and **388 owns the API side; this owns the UI side.**
5. **Route every order mutation through the active entry.** Add / remove / change-status must address `state.visits[state.active_table_id].items`.
6. **Give the bill record an identity.** `state.bills.push({ table_id, table_label, visit_key, subtotal, tax, paid, tip, method })`. **`table_label` alone is not an identity** — two visits on the same table produce two byte-identical records. `visit_key` is a monotonic counter in the state.
7. **Make close and bill operate on the active entry**, and delete that entry from `state.visits` when the visit closes.
8. **Add the regression check** (see §6). **Write it first — it must fail on today's file.**

## 5. The four things that will go wrong if nobody tells you

1. **Fixing the seat guard but not the state.** A guard on the seat handler stops the *second* party from being seated — but the screen still holds one party, so the waiter still cannot see table T2's order while table T3 is open. **Both halves are the same slice.** The guard is the visible half; the state is the load-bearing half.
2. **Leaving `state.visit` as an alias.** `state.visits` plus a `state.visit` alias is the same bug with two names. Every read of `state.visit` must be converted; `grep -c 'state\.visit\b' index.html` must return **0**.
3. **Seeding `state.visits` from only the party the old `state` literal carried.** If you add T3 but not T2 and P2, the mock-up still shows two occupied tables with no order for them — **the fixture and the state still disagree**, which is the defect in a smaller form.
4. **Editing `index.html` without knowing 465, 466 and 467 are in it.** **Four features of this corpus and feature 24 all touch this file.** The regions are disjoint — **the state object and the floor/seat handlers** (this), **the bill modal's arithmetic** (465), **the seat modal's inputs** (466), **the fixture's statuses** (467), **the floor grid** (24) — **but a rebase is required.** Say which landed first in your report.

## 6. Verification protocol

Offline, no network, no database, no browser.

```bash
cd /opt/data/le31_mmm3_research_work

# 1. THE STATE OBJECT IS PER-TABLE.  There is no single global visit left.
grep -c 'state\.visit\b' index.html          # must be 0
grep -c 'state\.visits' index.html           # must be >= 1

# 2. SEATING A SECOND PARTY DOES NOT DESTROY THE FIRST PARTY'S ORDER.
node /opt/data/le31-brainstorm-2026-11-13-scripts/prove_global_visit.js
#    expected: "the FIRST party's order ... is GONE: NO"
#    today's file prints "is GONE" with no NO -- the check must fail on it

# 3. THE UI REFUSES TO SEAT AT A TABLE THAT IS NOT FREE.
node /opt/data/le31-brainstorm-2026-11-13-scripts/prove_ui_regions.js
#    expected: a REFUSAL, not a silent seat (table 4 is 'billed' in MOCK_TABLES)

# 4. THE FIXTURE'S CONCURRENTLY OCCUPIED TABLES EACH HAVE AN ENTRY IN state.visits.
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const t=(s.match(/const MOCK_TABLES = \[[\s\S]*?\n\];/)[0]);
         const occ=[...t.matchAll(/id:\s*(\d+),\s*label:\s*'([^']+)',[\s\S]{0,200}?status:\s*'(seated|ordered|billed)'/g)]
                    .map(m=>({id:+m[1],label:m[2],status:m[3]}));
         const keys=[...s.matchAll(/state\.visits\s*=\s*\{([\s\S]*?)\n\};/g)].map(m=>m[1]);
         if(!keys.length){console.error('FAIL: no state.visits');process.exit(1)}
         const missing=occ.filter(o=>!new RegExp('(^|[^0-9])'+o.id+'\s*:').test(keys[0]));
         if(missing.length){console.error('FAIL: occupied tables with no entry: '+JSON.stringify(missing));process.exit(1)}
         console.log('PASS: '+occ.length+' occupied tables each have an entry')"

# 5. TWO BILLS ON THE SAME TABLE ARE DISTINGUISHABLE.
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const m=s.match(/state\.bills\.push\(([^\n]*)\)/);
         if(!/visit_key/.test(m[1])){console.error('FAIL: the bill record has no visit_key');process.exit(1)}
         console.log('PASS: the bill record carries a visit identity')"

# 6. THE CORPUS AGREES: this slice is now owned.
grep -rl 'state\.visits' features/ specs/      # must include features/474-*.md

# 7. NOTHING OUTSIDE index.html CHANGED.
git diff --name-only <base>...HEAD -- . ':(exclude)index.html'   # must be empty
```

**The negative control is mandatory.** Re-inject the defect — replace `state.visits` with a single `state.visit` — and **checks 1, 2 and 4 must fail**. A check that cannot fail proves nothing. **Check 2 in particular must fail on today's file**, because today's file is exactly the defect.

## 7. Rollback path

`git revert` the single commit that touched `index.html`. The file is self-contained: the `state` object, the floor-grid handler, the seat handler, the order renderer, the bill handler and the close handler.

**No data migration. No schema. No server-side state. No database rows. No API contract.** Reverting restores the shipped behaviour exactly, including the defect. **Rolling back is free, which is why this slice is safe to land before 388, 465, 466 and 467.**

## 8. The mandatory LE31 skill list

Read these before writing code. They are in the repo under `skills/`:

- **`skills/le31-conventions/`** — the naming, money and data-model conventions. **The `Decimal` rule and the no-float rule are here.**
- **`skills/le31-backend/`** — the backend's structure, routing and database conventions. **Read it even though this slice touches no Python**, so you know what you are *not* changing.
- **`skills/le31-frontend/`** — the frontend's conventions. **This is the relevant one.** `index.html` is vanilla HTML + JS with no build step (§4.1).
- **`skills/le31-handoff-spec/`** — the slice-contract shape this file follows.
- **`skills/le31-coding-agent-brief/`** — how the paste-in prompt is produced from this contract. **Do not paste chat excerpts; use the skill.**
- **`skills/le31-v1-feature-pattern/`** — the v1 feature's shape, for context on how a contract in this corpus is written.
- **`skills/le31-research/`** and **`skills/le31-data/`** — the research corpus and the data conventions, if you need the domain vocabulary.

**Also read, in the repo, before you start:**

- **`features/388-…-table-state-machine-…md`** — the API-side seat rule this slice mirrors.
- **`features/465-…`, `features/466-…`, `features/467-…`** — the three shipped-surface slices already in `index.html`.
- **`features/01-table-management.md`** — the informal spec whose own sketch shows three occupied tables.

## 9. The one thing that matters

**The shipped mock-up is the surface the charter's P0 acceptance criteria are judged against, and it holds one party for the whole restaurant.** Seating a second party **overwrites** the first party's order — the lines are destroyed, not hidden — while the floor map still shows the first table as occupied.

**A contract may be written with a placeholder, never with a gap: ship the contract with the strongest evidence available, and let the audit strengthen it.** Here the evidence is already execution-proven under `node`, against the file's own fixture and the file's own handler body. **Ship it.**
