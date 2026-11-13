# Feature 474 — The shipped waiter screen holds one visit for the whole restaurant: seating a second party destroys the first party's order

> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED (executed under `node` against the shipped `index.html`)**, confidence **high** for the defect, **low** for the demand (the *frequency* of two parties being seated at once in production is not evidenced and is not claimed).
>
> Third-party vocabulary source: `hekimcan206/offline-pos-sync` (MIT, created 2026-11-11) — an offline-first POS sync engine whose README states, verbatim: *"Two terminals edit the same ticket while offline: both tap '+1', one takes payment while the other voids the ticket…"* and *"last write wins silently loses a quantity or erases a paid sale."* LE31's shipped surface has the same shape with a **stronger** failure: the second party's seat **destroys** the first party's order rather than merging it. **Vocabulary reference only** — LE31 is not a .NET/PostgreSQL system and adopts no code from this repository.

## Goal

Make **the waiter screen able to hold more than one party at once** — so that the screen the owner loads can represent the floor it claims to represent.

Concretely, three things:

1. **The order screen is per-table, not global.** Every table with an open party keeps its own order, and the waiter can move between them.
2. **No order is ever silently destroyed.** A party's lines live with the party; changing which table the screen is showing must not discard another table's lines.
3. **A check that holds the rule**, because — as the corpus has now established twice — a rule applied only in the application is a rule the next code path forgets.

**The single sentence this feature exists to make true:** *the waiter screen shows one party at a time, and every other seated party's order is still there when the waiter comes back to it.*

## Scope

**In scope (v1):**

- **Replace the single global `state.visit` with a per-table collection** of open parties in `index.html`. The shape is a map keyed by table id, each entry holding the party, the server and the order lines.
- **A "switch to this table" action** on the floor grid: tapping a table that has an open party loads *that* party's order into the order view instead of starting an empty one.
- **A seat guard in the UI** that refuses to seat a party at a table that is not `free` — the UI's own copy of the rule feature **388** puts on the API. The UI must not be the one surface that allows it. (388 owns the **API** guard and explicitly puts waiter-UI changes out of its own scope; this slice owns the **UI** guard.)
- **The bill and close paths operate on the selected party's entry**, and the bill record names the **table id** and a **visit identity** so two bills on the same table are distinguishable.
- **A regression check** that fails on today's `index.html` and passes on the fixed one.

**Explicitly NOT in scope:**

- **The money arithmetic in the browser.** That is feature **465** — filed, and it owns the `toFixed(2)`/`float` problem in the bill modal. **This slice does not change any money rule and must not touch feature 465's helper.**
- **The seat form's validation.** That is feature **466** — filed, and it owns the `Adults` input's `min="0"`. **This slice does not change the seat form's inputs.**
- **The fixture/API drift check.** That is feature **467** — filed, and it owns the check that compares the fixture's statuses against the API's response shape. **This slice does not build that check.**
- **The API's stored `Table.status` column and the API's seat guard.** That is feature **388** — filed. **This slice adds no Python file and changes no endpoint.** It adds the UI-side guard so the two surfaces agree in the meantime, before 388's API guard exists.
- **Wiring the mock-up to the API.** That is a separate, larger slice. **This slice does not add a `fetch()` call.**
- **Any change to the mock-up's visual design**, its three views, or its colour tokens.
- **Any change to `features/01-table-management.md`'s *contract* semantics.** Feature 01 is an informal spec; this slice adds a **contract** beside it, and does not rewrite it.

## Description

### The defect, as executed

`index.html` declares exactly one visit, for the whole restaurant:

```js
let state = {
  visit: { table_id: 3, table_label: 'T3', party: { size: 2, adults: 2, children: 0 }, server: 'AC',
           items: [
             { menu_item_id: 1, name: 'Schnitzel', qty: 1, unit_price: 14, status: 'preparing' },
             { menu_item_id: 4, name: 'Fries',     qty: 1, unit_price:  4, status: 'ready' },
             { menu_item_id: 5, name: 'Coke',      qty: 1, unit_price:  3, status: 'new' },
           ] },
  bills: [],
};
```

And the seat handler **replaces** it:

```js
// Switch to order view pre-loaded with this table
state.visit = { table_id: t.id, table_label: t.label, party: t.party, server: 'AB', items: [] };
```

Executed under `node` against the file's own fixture and the file's own handler body:

```
=== SCENARIO: table 3 is already seated and has 3 items on its order ===
  BEFORE seating anyone else, state.visit is table T3 with 3 items:
      Schnitzel x1  status=preparing
      Fries x1  status=ready
      Coke x1  status=new

  the shipped handler ran: state.visit = { table_id: 1, table_label: T1, items: [] }
  AFTER  seating table T1, state.visit is table T1 with 0 items:

  the FIRST party's order (table Schnitzel x1, Fries x1, Coke x1) is now:
  >>> table T3 still shows status=ordered on the floor map, but its order is GONE

=== and can the first party be billed? ===
  state.visit is now table T1; its subtotal is 0
  the shipped bill handler would alert("No items to bill.") for the FIRST table.
  >>> the first party's bill is unreachable through the shipped UI.
```

**The floor map lies.** Table T3 still renders as `ordered` with its party of 2. The waiter sees a live table and a "bill" button that produces *"No items to bill."*

### The mock-up's own fixture describes a state the code cannot hold

`MOCK_TABLES` in the same file holds **three tables simultaneously occupied**:

```
  table 1 T1 status=free    party=none
  table 2 T2 status=seated  party={"size":4,"adults":3,"children":1}
  table 3 T3 status=ordered party={"size":2,"adults":2,"children":0}
  table 4 T4 status=billed  party={"size":5,"adults":5,"children":0}
  table 5 T5 status=free    party=none
  table 6 T6 status=dirty   party=none
  table 7 P1 status=free    party=none
  table 8 P2 status=seated  party={"size":6,"adults":4,"children":2}
```

**T2, T3 and P2 are all occupied at the same time** — three parties, three order lists. The shipped `state` holds **one** order list. The fixture is a picture of a restaurant the code cannot represent.

And the informal spec agrees with the fixture, not with the code. `features/01-table-management.md`'s own sketch:

```
│   [T1 🟢]  [T2 🟡 party 4]  [T3 🔴 bill] │
│   [T4 ⚫ dirty]  [T5 🟢]  [T6 🟠 ord.] │
```

**Four tables in four different states, three of them occupied.** The sketch is the requirement; `index.html` is the implementation; they disagree.

### Why the corpus does not own this

- Feature **388** owns the **API-side** seat guard and the stored `Table.status` column. Its own *Out of scope* says, verbatim: *"Any waiter-UI change beyond what the API response implies (the UI is `index.html`, feature 01's scope; this slice does not restyle it)."* **388 does not own the UI's state model.**
- Feature **465** quotes `state.visit.items.reduce(...)` — but only as the **site of the float arithmetic**. Its *Scope* is exclusively money: *"This slice changes no Python file"*, and its *Out of scope* excludes *"any change to `index.html`'s visual design … or its fake-data content"*. **465 does not own the fact that `state.visit` is one object for the whole restaurant.**
- Feature **467** owns the **fixture↔API drift check** — a check, not a state model. Its *Out of scope* excludes *"any change to the mock-up's visual design … or its fake-data content beyond the status reconciliation."*
- Feature **01** is an **informal spec**: it has no `## Out of scope` heading, no gate verdict, no verification protocol, and no owner for the UI's state model. **Three separate filed features defer the waiter UI to feature 01's scope, and feature 01 is not a contract.**
- A corpus-wide sweep over 28 candidate concepts returns **`COVERED (2)`** for *"shipped UI: ONE global visit for the whole restaurant"* — and both hits are 465 and its HANDOFF, which quote the string **as the site of a float**. The sweep matched the **token**, not the **concept**.

### What the third-party source contributes (vocabulary only)

`hekimcan206/offline-pos-sync`'s README names the failure mode this is an instance of, in a system built to survive it:

> *"Last write wins silently loses a quantity or erases a paid sale."*

Its own design splits the concern three ways — **row LWW**, **field-level LWW**, and **domain rules** — and its ADR 0002 is titled *"merge strategies, field registers and domain lattices"*. LE31's shipped surface implements **none** of the three: it has one global slot and no merge at all.

The transferable vocabulary is the **three-way split of "how do two versions of the same thing get combined"** — LE31 needs a fourth answer for a surface that cannot hold two versions at once: **keep both, keyed by table**. The *code* of `offline-pos-sync` (a .NET sync engine with a SQLite outbox, an `INSERT … ON CONFLICT (change_id) DO NOTHING` arbiter and a Toxiproxy test harness) is **not** adopted: LE31's v1 has a single server, no outbox, and §3.1 requires SQLite compatibility that a .NET engine cannot provide.

## Data model

**No schema change. No Python change.** The state lives in the browser:

```js
// BEFORE — one visit for the whole restaurant
let state = {
  visit: { table_id: 3, table_label: 'T3', party: {...}, server: 'AC', items: [...] },
  bills: [],
};

// AFTER — one open party per table, plus which one the screen is showing
let state = {
  visits: {
    // keyed by TABLE id
    3: { table_id: 3, table_label: 'T3', party: { size: 2, adults: 2, children: 0 },
         server: 'AC', items: [ /* per-line objects, as today */ ] },
  },
  active_table_id: 3,          // which party the order view is showing
  bills: [],                   // each bill record gains table_id + a visit key
};
```

**The bill record changes shape** (see *Implementation steps* step 6) — but the change is in the browser's in-memory array only, not in the database.

## Implementation steps

1. **Replace `state.visit` with `state.visits` + `state.active_table_id`.** Every read of `state.visit` becomes a lookup of the active entry. **Do not leave a `state.visit` alias behind** — a second name for the same concept is how the next reader reintroduces the bug.
2. **Seed `state.visits` from the fixture.** The fixture has T2, T3 and P2 occupied; the shipped `state` has one. **The fixture's three occupied tables must each get an entry**, or the mock-up will still show a floor the code cannot hold. (Do **not** change the fixture's data — feature **467** owns the fixture's reconciliation and its *Out of scope* says *"any change to the mock-up's visual design … or its fake-data content"*. **Adding the two missing entries to `state` is not changing the fixture** — the fixture array `MOCK_TABLES` is untouched.)
3. **Add the switch-to-table action.** Tapping a table on the floor grid that has an entry in `state.visits` sets `active_table_id` and renders that party's order. Tapping a `free` table opens the seat modal. Tapping an occupied table **must not** open the seat modal — see step 4.
4. **Add the UI-side seat guard.** The seat handler must check the target table's status before applying `t.status = 'seated'`. If the table is not `free`, the handler **refuses**, says so, and **switches to the existing party** instead. This is the UI's copy of feature **388**'s API rule; **388 owns the API guard**, this owns the UI one, and **neither may be implemented by editing the other's file region**.
5. **Route every order mutation through the active entry.** Add/remove/change-status on a line must address `state.visits[state.active_table_id].items`, never a global array.
6. **Give the bill record an identity.** A pushed bill becomes `{ table_id, table_label, visit_key, subtotal, tax, paid, tip, method }`. **`table_label` alone is not an identity**: two separate visits on the same table produce two records that are byte-identical apart from their position in the array. `visit_key` must be distinct per visit — a monotonic counter held in the state is sufficient for a mock-up.
7. **Make close and bill operate on the active entry only**, and remove that entry from `state.visits` when the visit closes (the bill path already clears `state.visit.items = []`).
8. **Add the regression check** (see *Verification protocol*).

## Telegram interaction if any

**None.** The waiter surface is a web UI; this slice touches no bot command and no FSM state. The cook bot (`backend/app/bot/cook_bot.py`) is untouched.

## Dependencies

- **Feature 388** (`le31-table-state-machine…`) — **read first.** It adds the stored `Table.status` column and the **API-side** seat guard. This slice adds the **UI-side** guard. **The two regions are disjoint: 388 changes `backend/app/models.py` and `backend/app/routers/tables.py`; this slice changes `index.html` only.** A rebase is required; each contract says which lands first.
- **Feature 465** (`le31-the-waiters-screen-shows-a-different-tip…`) — **read first.** It owns the money helper in the same file. This slice **must not** touch the money helper, the `toFixed(2)` calls, or the tip arithmetic. **The regions are disjoint** (465: the bill modal's arithmetic; this: the state object and the seat/floor handlers) — **but both edit `index.html`, so a rebase is required.**
- **Feature 466** (`le31-the-seat-form-accepts-a-party-the-api-will-refuse…`) — owns the `Adults` input's `min="0"`. **This slice does not change any input's attributes.**
- **Feature 467** (`le31-the-waiter-surface-and-the-api-have-drifted-apart…`) — owns the drift check and the fixture's status reconciliation. **This slice does not build the drift check and does not change `MOCK_TABLES`.**
- **`features/01-table-management.md`** — the informal spec whose own sketch shows three occupied tables. **This slice does not rewrite it; it adds a contract beside it.**
- **Charter §7** — *"End-to-end before commit"*. This slice is the first thing in the corpus that makes the charter's own UI acceptance criterion checkable, because it adds a check to the file the charter's P0 row 42 is judged against (*"UI shows table card turning yellow"*).

## Open questions

1. **Should the UI's guard duplicate 388's API guard, or wait for it?** — **Decided: implement it now.** 388's guard does not exist yet, and the UI is the surface the owner actually loads. The UI guard must return the **same refusal semantics** 388 specifies (refuse, and show the party that is already there) so that when 388 lands the two do not disagree. **Recorded here so a later pass does not re-litigate it.** If 388 lands first, **delete this slice's duplicate and keep only the UI's message formatting** — do not keep two independent refusal texts.
2. **Should the fixture's three occupied tables each carry a visible order list?** — **Decided: yes, but only where the fixture already implies one.** The shipped `state` had exactly one party's lines; that party's table is T3. **T2 and P2 get empty item lists** — a table can be seated without having ordered yet, which is the normal case. **The point of the change is that the three entries EXIST**, not that all three have items.
3. **Should `bills` be keyed by table id instead of an array?** — **Decided: no, keep the array** but give each record a `table_id` and a `visit_key`. A keyed structure is a larger refactor of a file three other features edit. **Recorded.**
4. **Does the mock-up need a *server* per visit?** — **Decided: keep `server: 'AC'` / `'AB'` as-is.** The server field is a display string in the mock-up and feature **451** owns the real actor semantics on the API side. **This slice does not make the mock-up's server real.**
5. **Is a floor-grid interaction (tap an occupied table to switch) enough, or is a tab/list needed?** — **Decided: the floor-grid tap is enough.** The file's own design is a grid of table cards; adding a second navigation surface is scope creep. **Recorded.**

## Why this matters

**The mock-up is what the owner loads, and the charter's P0 acceptance criterion is judged against it.**

Charter P0 row 42 reads, verbatim: *"Waiter can seat a party at any free table … `POST /api/tables/{id}/seat` works; **UI shows table card turning yellow**."* The UI is therefore **load-bearing for the charter's own acceptance test** — and it is the one artefact in the repository that can demonstrate the product working.

The defect is that the shipped UI **cannot represent the restaurant the charter describes**. A restaurant has, by construction, more than one table occupied at once — that is what a restaurant *is*. The mock-up's own fixture says so. The spec's own sketch says so. The code says otherwise.

**And the failure is silent and unrecoverable.** There is no error, no alert, no red tile. The floor map continues to show the first table as occupied. The waiter comes back to a table that looks live and finds *"No items to bill."* Worse — the lines are **gone**, not merely hidden: `state.visit = { ... items: [] }` replaces the whole object, so the first party's Schnitzel, Fries and Coke no longer exist anywhere in the program. **There is no audit, no undo, and no second screen to check.**

**The cost of the information decays.** Today the defect is a missing data structure. After the first real service — after the first bill is closed and the first shift reconciled — **reconstructing whose order was lost requires a manual audit of live service history with no ground truth**, because the lines were never stored anywhere. That is the same asymmetry feature 388's contract names, and it is why this must land before the product is used rather than after.

**This is the third time the corpus has found a defect by reading the shipped surface against the shipped API**, and the first time the defect is not a *value* but a *shape*. 465 found money computed in floats. 466 found a form that permits a value the API refuses. 467 found two surfaces that can drift with nothing to see it. **This one is more fundamental than all three: the surface's data model cannot hold the domain.** A float is a wrong number; a missing `Table.status` is a missing column; **a single global visit is a missing collection — and every downstream feature that assumes "the current order" (feature 02's order taking, feature 05's bill, feature 09's kitchen board) inherits the assumption that there is only ever one.**

**It is also the cheapest fix in the corpus.** One data-structure change in one file, no schema, no Python, no endpoint, no migration — and it removes a whole class of "the waiter was looking at the wrong table" confusion that no other slice can remove, because the other slices all assume the surface can show a party.

## Adjacent evidence

| Source | What it contributes | Disposition |
|---|---|---|
| `hekimcan206/offline-pos-sync` (MIT, created 2026-11-11, ★0) | The vocabulary of merging two versions of the same ticket: **row LWW**, **field-level LWW**, **domain rules** (ADR 0002 *"merge strategies, field registers and domain lattices"*). Its README names the exact failure: *"last write wins silently loses a quantity or erases a paid sale."* | **Vocabulary reference only.** LE31 adopts no code. The transferable idea is the **three-way split of "how do two versions combine"** — LE31's answer for a surface that cannot hold two versions is **keep both, keyed by table**. |
| `lorenzoyang/TavoloFlow` (AGPL-3.0, created 2026-10-16, ★22) | A working restaurant app whose README describes the **same four surfaces** — Floor, Kitchen, Pass, and the bill — and whose **own floor holds many open tables at once**; the README's *"One table, start to finish"* walkthrough is one visit *among* the floor's. | **Vocabulary reference only** (AGPL-3.0 is not §3.2-compatible for code adoption). Confirms that **a floor of concurrently-open tables is the normal shape**, not an edge case. |
| `MustrHQ/kitchen-safety` (AGPL-3.0, created 2026-10-26) | Its README separates the **kitchen frontend** (no login) from the **protected admin panel**, and states plainly: *"Frontend names are self-reported, not authenticated staff identities."* | **Vocabulary reference only.** Confirms that a **surface's identity model is a separate, deliberate decision** — which is the argument for making this surface's *party* model a decision too, rather than an accident of one object literal. |
| `hekimcan206/offline-pos-sync` — *"a restaurant whose internet drops never loses a ticket"* | The **promise** an operator surface makes about a ticket. LE31's shipped surface makes no such promise and breaks it in the ordinary case (no internet required). | Framing. |

## Verification protocol

Seven checks, all offline, no network, no database. **Checks 1–4 run under `node`; check 5 runs as a Python script; 6 and 7 are corpus greps.**

```bash
# 1. THE STATE OBJECT IS PER-TABLE.  There is no single global visit left.
grep -c 'state\.visit\b' index.html          # must be 0
grep -c 'state\.visits' index.html           # must be >= 1
node -e "const s=require('fs').readFileSync('index.html','utf8');
         if(/\bstate\.visit\b/.test(s)) {console.error('FAIL: a global state.visit survives'); process.exit(1)}
         if(!/state\.visits/.test(s)) {console.error('FAIL: no state.visits'); process.exit(1)}
         console.log('PASS: the state is per-table')"

# 2. SEATING A SECOND PARTY DOES NOT DESTROY THE FIRST PARTY'S ORDER.
#    (the same scenario that fails today)
node <scripts/prove_global_visit.js>          # must print "the FIRST party's order is GONE: NO"
node -e "..."                                  # assert the first party's lines are still readable

# 3. THE UI REFUSES TO SEAT AT A TABLE THAT IS NOT FREE.
#    Executed against the shipped handler body, with the shipped fixture:
#    table 4 is 'billed' in MOCK_TABLES.
node <scripts/prove_ui_regions.js>            # must print a REFUSAL, not a silent seat

# 4. THE FIXTURE'S CONCURRENTLY OCCUPIED TABLES EACH HAVE AN ENTRY IN state.visits.
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const occ=(s.match(/status:\s*'(seated|ordered|billed)'/g)||[]).map(x=>x.match(/'(.*)'/)[1]);
         ... require every occupied table id to be a key of state.visits ..."

# 5. TWO BILLS ON THE SAME TABLE ARE DISTINGUISHABLE.
node -e "..."        # bill twice on one table -> the two records differ in visit_key

# 6. THE CORPUS AGREES: this slice is now owned.
grep -rl 'state\.visits' features/ specs/     # must include features/474-*.md
grep -rlF 'one visit for the whole restaurant' features/ specs/

# 7. NOTHING OUTSIDE index.html CHANGED.
git diff --name-only <base>...HEAD -- . ':(exclude)index.html'   # must be empty
```

**The negative control.** Re-inject the defect — replace `state.visits` with a single `state.visit` — and **checks 1 and 2 must fail**. A check that cannot fail proves nothing. If checks 1–4 pass on the unmodified file, the verifier is wrong, not the file.

## Rollback path

`git revert` the single commit that touched `index.html`. The file is self-contained: the `state` object, the floor-grid handler, the seat handler, the order renderer, the bill handler and the close handler. **Reverting restores the shipped behaviour exactly, including the defect** — no data migration, no schema, no server-side state, no database rows, no API contract. **Rolling back is free, which is why this slice is safe to land before 388, 465, 466 and 467.**
