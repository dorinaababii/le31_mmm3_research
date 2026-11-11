# Feature 467 — The waiter surface and the API have drifted apart, and nothing can see it: the mock-up calls no API and no test compares the two

> **Pick C of Daily Brainstorm 2026-11-10 (100th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own shipped waiter surface, and it is proved by EXECUTION and by PARSING the shipped files**, not by reading.
>
> `index.html` is the shipped waiter UI. `backend/app/main.py` mounts it at `/`:
>
> ```python
> _STATIC_DIR = _REPO_ROOT / "index.html"
> if _STATIC_DIR.exists():
>     app.mount("/", StaticFiles(directory=str(_STATIC_DIR.parent), html=True), name="ui")
> ```
>
> **It never calls the API.**
>
> ```
> $ grep -c "fetch(" index.html
> 0
> ```
>
> **And the data it renders is a hard-coded JavaScript array whose shape the API cannot produce.** Parsed out of the shipped file on 2026-11-10:
>
> ```js
> { id: 1, label: 'T1', section: 'main', seats: 4, status: 'free' },
> { id: 2, label: 'T2', section: 'main', seats: 4, status: 'seated', party: { size: 4, adults: 3, children: 1 }, server: 'AB' },
> { id: 3, label: 'T3', section: 'main', seats: 4, status: 'ordered', party: { size: 2, adults: 2, children: 0 }, server: 'AC', subtotal: 28.00 },
> { id: 4, label: 'T4', section: 'main', seats: 6, status: 'billed',  party: { size: 5, adults: 5, children: 0 }, server: 'AB', subtotal: 87.00 },
> { id: 5, label: 'T5', section: 'main', seats: 2, status: 'free' },
> { id: 6, label: 'T6', section: 'main', seats: 4, status: 'dirty' },
> ```
>
> **Three of those six statuses — `ordered`, `billed`, `dirty` — cannot be produced by the shipped API.** `backend/app/routers/tables.py`:
>
> ```python
> def _table_status(table_id: int, session: Session) -> str:
>     visit = session.exec(
>         select(Visit).where(Visit.table_id == table_id, Visit.closed_at == None)
>     ).first()
>     if not visit:
>         return TableStatus.free.value
>     return TableStatus.seated.value  # could be 'ordered' / 'billed' with more checks
> ```
>
> **The API's own comment says the other three states are not implemented.** The mock-up ships all three.
>
> **And the drift is invisible, because nothing compares the two.** `PROJECT_CHARTER.md` §7 says:
>
> > - **End-to-end before commit.** Don't commit a feature that "compiles but doesn't work in the UI".
>
> **There is no mechanism in the repo that could execute that clause.** The charter requires an end-to-end check before commit; the repo has no test that renders the UI, no test that fetches from the API, and no check that the mock-up's fixture matches the API's response shape.
>
> **Bucket: v1.** Verdict: **`build`**. Evidence class: **OBSERVED** (parsed from the shipped files; the API's comment quoted verbatim). Confidence: **high** for the defect (six fixture statuses against two producible ones, zero `fetch()` calls, zero UI tests in a 959-file corpus); **medium** for the demand (no operator has reported it — but the mock-up is the **only** waiter surface that exists).

## Goal

Make **the waiter surface and the API unable to drift apart silently** — so that the moment the surface is wired, the two agree about what a table looks like, and every drift between them is caught by a check that runs before a commit.

The concrete outcome:

1. **A machine-checkable description of the API's response shapes** exists, and the mock-up's fixture is checked against it — so a status the API cannot return is a **failing check**, not a surprise on the floor.
2. **The mock-up's fixture states which statuses the API can currently produce**, and the ones it cannot are either removed or explicitly marked as not-yet-implemented.
3. **A drift check exists at all** — because today there is none, and the charter requires one.

**The single sentence this feature exists to make true:** *the waiter surface's data comes from the API's contract, and a check fails the moment the two disagree.*

## Scope

**In scope (v1):**

- **A drift check** that compares the mock-up's fixture against the API's actual response shape and **fails** when they disagree. The check must be runnable offline, with **no network call** and **no database**.
- **A machine-readable record of the API's current response shape** — the fields `GET /api/tables` returns, and the **complete set of `TableStatus` values the API can actually return** (`free`, `seated`, and whatever 388 adds).
- **The mock-up's fixture is brought into agreement with that record**, or its impossible states are explicitly marked as *"a state the API does not implement yet"* so the drift is **declared rather than accidental**.
- **A note in the mock-up itself** stating that its data is a fixture and not API output — so the next reader knows the file is a *preview* and not a *client*.
- **An assertion set** that fails on today's repo and passes on the fixed one.

**Explicitly NOT in scope:**

- **Wiring the mock-up to the API.** That is a separate, larger slice — the surface would become a real client, with polling, error states, and loading states. **This slice does not add a `fetch()` call.**
- **Adding the missing table states to the API.** `ordered`, `billed` and `dirty` as real transitions are feature **388**'s territory (and **388 explicitly puts `ordered`/`billed`/`dirty` out of scope**: *"The full five-state machine (`ordered`, `billed`, `dirty`) as transitions … The other three states exist as enum values and are not wired."*). **This slice does not change the API.**
- **The `Table.status` column.** That is feature **388** — filed.
- **Any change to the mock-up's visual design**, its three views, its colour tokens, or its fake-data content beyond the status reconciliation.
- **A browser test framework, a headless browser, or a CI pipeline.** The drift check must be a **plain script** that runs offline — the repo has no such infrastructure today and adding one is a different slice.

## Description

### What is actually in the repo today

| artefact | state on 2026-11-10 |
|---|---|
| `index.html` | 30,530 bytes, 720 lines, **0 `fetch()` calls** — a static fixture |
| `backend/app/main.py` | mounts `index.html` at `/` — the fixture **is** the shipped surface |
| `backend/app/routers/tables.py` | **one** router, `GET /api/tables` + `POST /api/tables/{id}/seat` |
| `GET /api/tables` response | `{id, label, section, seats, x, y, status}` — `status` ∈ {`free`, `seated`} |
| the mock-up's fixture | `{id, label, section, seats, status, party?, server?, subtotal?}` — `status` ∈ {`free`, `seated`, `ordered`, `billed`, `dirty`} |
| UI tests in the corpus | **0** — a sweep of 959 feature contracts and HANDOFFs finds no UI-rendering or fixture-comparison check |

**The fields do not match either.** The API returns `x` and `y` (the floor-map coordinates, which feature **460** and feature **24** both care about); the fixture has **no `x`/`y`**. The fixture has `party`, `server` and `subtotal`; the API's `GET /api/tables` returns **none of them**. **The mock-up is not a client of the API and does not pretend to be one — and nothing says so.**

### ⭐ The drift is already three states wide

| status | in the mock-up's fixture | producible by the API? |
|---|---|---|
| `free` | T1, T5, P1, P2 | **yes** |
| `seated` | T2, P2 | **yes** |
| `ordered` | T3 | **NO** — the API's own comment says *"could be 'ordered' / 'billed' with more checks"* |
| `billed` | T4 | **NO** — same |
| `dirty` | T6 | **NO** — same |

**And the CSS has a rule for each of them** (`.table-card.status-ordered`, `.status-billed`, `.status-dirty`) — the mock-up was *designed* for the five-state machine the API does not implement.

### ⭐ Why this is a defect and not a mock-up being a mock-up

`features/08-index-mockup.md` says, verbatim:

> **Out of scope (v1):**
> - Real backend wiring.
> - Persistence (refresh = back to mock data).

and, under *How to view*:

> When the real backend exists, the same HTML can be served by FastAPI (static files at `/`).

**That last sentence is the problem.** The file is *already* served by FastAPI — `main.py` does exactly that today. **The condition "when the real backend exists" is already half-met**: the backend exists, the file is mounted, and the file still ignores it.

**The intent is that this file becomes the real waiter surface.** Under that intent, a fixture that contains three states the API cannot produce is not a mock-up's harmless simplification — **it is a specification of behaviour the API has not agreed to implement.** When the wiring happens, either the surface must lose three states (and the floor map becomes a two-colour grid) or the API must grow three transitions (and feature 388's *Out of scope* says it will not).

**Nobody has to decide yet. But somebody has to notice, and today nothing does.**

### ⭐ And the charter's own quality bar is unenforceable

`PROJECT_CHARTER.md` §7:

> - **End-to-end before commit.** Don't commit a feature that "compiles but doesn't work in the UI".

**There is no mechanism in the repository that can execute this clause.** There is no UI test, no fixture check, no response-shape assertion, no CI config. A feature can land, pass every manual check, and be "working in the UI" **against a fixture that the API does not produce** — which is exactly what has happened, silently, for the three missing statuses.

**This is the seventh finding shape the corpus has filed — *a covered concept, an uncovered instance* — applied to the surface itself.** The corpus owns the *table states* (388), the *money* (411, 415, 457), the *party rules* (414, 423), and the *mock-up* (feature 08, informally). **Nobody owns the relationship between them.**

### The cost of leaving it

**Today: zero, and that is the trap.** The mock-up is a fixture; a fixture is allowed to be a fiction.

**The day the surface is wired** — one afternoon of work — the drift becomes **runtime**, and it will be found by the owner, on a Saturday, on the floor:

- The UI polls `GET /api/tables`, receives `status: "free"` or `status: "seated"` **only**, and the tables the fixture showed as `ordered` / `billed` / `dirty` **render in the free colour**. A table that was just billed looks free. **A waiter seats a second party on a table that already has a bill.**
- Or, the wiring is written *to match the fixture* — and then the API must grow three transitions **that feature 388 explicitly declined to build.**

**Either way the decision is forced by an accident.** This slice makes it a decision.

**And the drift check is the part that keeps paying.** Once it exists, **every** future divergence between the surface and the API is a failing check instead of a floor incident — including the ones nobody has thought of yet, and including the **three that already exist**.

## Data model

**No schema change. No Python change to the API's behaviour. No new table, no new column, no new endpoint.**

Two artefacts:

**1. A machine-readable record of the API's response shape** — small, checked in, and **derived from the API rather than hand-written**, so it cannot itself drift:

```
api-contracts/tables.json
  {
    "GET /api/tables": {
      "item": {
        "id": "int", "label": "str", "section": "str",
        "seats": "int", "x": "int", "y": "int",
        "status": { "enum": ["free", "seated"],
                    "note": "TableStatus members the API can currently return" }
      }
    }
  }
```

**The `status` enum in that file is the load-bearing part.** It must list **only** the states the API can actually produce, and the drift check must fail when the API's own `_table_status()` can return a value that is not in it — **and vice versa**.

**2. A drift check** — a plain script, offline, no network, no database:

```
scripts/check-surface-drift.py
  - parse index.html's fixture
  - parse api-contracts/tables.json
  - assert: every fixture status is in the contract's enum
  - assert: every fixture field is in the contract's item
  - assert: every contract field is either present in the fixture or
            explicitly listed as "not yet rendered by the surface"
  - assert: the API's source contains no TableStatus member that the
            contract's enum does not list
  - exit 1 on any mismatch
```

**Two design decisions the implementer must record:**

- **Is the contract file hand-written or generated?** Recorded default: **hand-written but verified against the API's source by the check** — the check asserts the contract's `status` enum matches the set of `TableStatus` members that appear as `return TableStatus.<member>` in the router. **A generated contract needs a build step the repo does not have.** The implementer must state which.
- **What happens to the three impossible states?** Recorded default: **keep them in the fixture, and mark them** — the fixture grows a `notYetImplemented: true` marker on `T3`, `T4` and `T6`, and the check treats a marked state as *declared* rather than *accidental*. **The alternative — deleting them — makes the mock-up visibly poorer and pre-empts feature 388's decision.** The implementer must state which, and **deleting them is not forbidden**, only recorded.

## Implementation steps

1. **Write `api-contracts/tables.json`** — the response shape of `GET /api/tables`, with the `status` enum containing **only** `free` and `seated`, and a `note` naming the two missing states and the feature that owns them (388).
2. **Write `scripts/check-surface-drift.py`** — the five assertions above. It must **exit 1** on today's repo, because the fixture carries three states the contract does not list and omits two fields (`x`, `y`) the contract does list.
3. **Mark the fixture's impossible states** (or remove them, per the recorded decision). **Marking is the default.**
4. **Add a header comment to `index.html`** stating, in one line, that its data is a fixture and not API output, and that `scripts/check-surface-drift.py` is what keeps the two in agreement.
5. **Add the drift check to the repo's verification tooling** so it runs with the other checks — **and record that it must run before every commit that touches `index.html` or `backend/app/routers/tables.py`.**
6. **Add the assertion set** below.

## Telegram interaction if any

**None.** This slice touches the waiter surface and a check script. It does not change the cook bot, and it does not change any Telegram command.

## Dependencies

- **Feature 08** (`08-index-mockup.md`) — the informal spec for `index.html`. It says *"Real backend wiring"* is out of scope for the mock-up, and *"When the real backend exists, the same HTML can be served by FastAPI"*. **This slice is the first contract to make the *drift* between the two a checked property.** It does not rewrite feature 08; it adds one constraint to it.
- **Feature 388** (`le31-table-state-machine…`) — owns `Table.status` and the seat guard. **388's *Out of scope* says the other three states are *"not wired"* and *"the UI is `index.html`, feature 01's scope"*.** **⚠️ THIS IS THE DEPENDENCY THAT MATTERS MOST**: if 388 lands and starts returning `ordered`/`billed`/`dirty`, **this slice's contract file must be updated in the same PR** — otherwise the drift check fails the moment 388 lands, and a check that fails on correct code trains people to disable it. **The check must therefore read the API's *source*, not only the contract file**, so that 388's landing is detected as a *contract* change rather than a false drift.
- **Feature 01** (`01-table-management.md`) — the informal spec that 388 calls *"feature 01's scope"* for the UI. **Informal, not a contract.** This slice supplies the missing contract for that surface.
- **Feature 24** (`visual-table-layout-v2`) — an `index.html` rewrite of the floor grid, scope line *"All changes live in `index.html` only"*. **⚠️ FILE-LEVEL COLLISION** with this slice and with picks 465/466. **Different regions**; the implementer must say which lands first.
- **Features 465 and 466** (this pass's picks A and B) — **⚠️ FILE-LEVEL COLLISION**: all three edit `index.html`. **465** edits the bill modal's arithmetic, **466** edits the seat modal's inputs, **this slice** edits the fixture and adds the contract file. **The three regions are disjoint, but a rebase is required.**
- **Feature 460** — owns `Table.section` (the floor map's grouping). The mock-up's fixture uses `section: 'main'` and `section: 'patio'`; **460 owns the canonicalisation rule for that field**. **The drift check should not duplicate 460's rule** — it checks the *shape*, not the *values*.
- **Feature 14** (`split-bills.md`) — the mock-up's bill modal computes one total. **Not in scope here.**

## Open questions

1. **Hand-written contract file, or generated?** Recorded default: **hand-written, but verified against the API's source by the check.** The implementer must record the choice.
2. **Keep the three impossible states (marked) or delete them?** Recorded default: **keep and mark.** Deleting them is not forbidden, only recorded — but it removes the visual evidence that the five-state design was intended, and feature 388 may yet build them.
3. **Where does the drift check live?** Recorded default: **`scripts/check-surface-drift.py`** at the repo root, alongside whatever check tooling exists. **The repo has no canonical test command** — the implementer must say how the check is invoked, and the answer must be one a human will actually run.
4. **Should the check be extended to cover the other mock-up data (the menu fixture, the visit fixture)?** Recorded default: **no for this slice** — one surface, one check. The check's shape is designed so extending it is a matter of adding a contract entry.
5. **What about `x` and `y`, which the API returns and the fixture omits?** Recorded default: **the contract lists them and the check requires the fixture to declare them as "not yet rendered"** — so the omission is **declared**, not silent. **The floor map is feature 24's and 460's territory.**
6. **Should this slice also add the first end-to-end UI check the charter §7 implies?** Recorded default: **no.** The charter's clause is about a feature being "working in the UI", which needs a rendered browser. **This slice is the cheap half — a shape check, not a rendering check** — and the expensive half is a separate slice. **Saying so is part of the contract, so nobody assumes §7 is now satisfied.**

## Why this matters

**LE31 is a system whose owner makes every decision on a phone, standing up, holding a tray.** The floor view's colour *is* the state of the table. If a table that has been billed renders as free, the next waiter seats a second party on it — and the bill for the first party is now attached to a table with a second visit on it, which is the exact state feature **454** filed (a visit closed with order lines and no bill) arriving by a completely different road.

**But the real cost of this defect is not today's bug. It is that LE31 has no instrument.** The charter asks for end-to-end verification before commit and **the repository contains nothing that could perform it.** That is the state of a project that has been running for months of daily passes: **every pass has been adding rules to the corpus and checks to the contracts, and no pass has added a check that would catch the surface and the API disagreeing about what a table is.**

**This is the same lesson the 99th pass recorded about the concept sweep** — *"a pass that searches for concepts will find nothing and will not know it has failed"* — applied to the repository rather than to the analysis. **A repo with no drift check cannot know it has drifted.**

**And it is cheap now for the same reason it is urgent later.** The drift check is a script and a small JSON file — a day's work. Once the surface is wired, the *same* check is the only thing standing between a schema change and a floor incident, and by then it must also handle real network calls, real latency and real error states. **Cheap now, expensive later, and the cheap version is already going to be needed.**

## Adjacent evidence

**Third-party instruments — read in the raw fetch, no code adopted:**

- **`AlgoVyn/bikri`** (MIT ✓, ★1 / ⑂0 = **NO traction evidence**, created 2026-10-26, pushed 2026-11-10, direct `GET /repos/` on 2026-11-10) — its `sale_lines` table and its *derived-not-stored* discipline are the same shape as this slice's *contract-not-assumed* rule. **Already cited by 11 corpus files — corroboration only, NOT re-picked.**
- **`huv0310-arch/verdict-ledger`** (MIT ✓, ★0 / ⑂0 = **NO traction evidence**, created 2026-11-06, pushed 2026-11-09, direct `GET`) — *"Every memory knows its sources."* **Already cited by feature 457 — corroboration only.**
- **`farulivan/roomflow`** (MIT ✓, ★1, created 2026-10-20) — a staff-facing dashboard. **Adjacent in shape; recorded, not adopted.**
- **`nikolaosmanhss-png/pantrytrack`** (MIT ✓, ★3 / ⑂3, created 2026-11-09) — the closest domain match in the fresh pool. **Recorded, not adopted: ★3 is no traction evidence and its territory is feature 432's.**

**⭐ THE GENUINE DUPLICATES, MARKED AND SKIPPED (not re-picked):**

- **`baba-dev/menuminute`** (MIT ✓, ★1 / ⑂0) — 3 corpus files cite it. **Skipped.**
- **`manoranjan2050/RestoPro-ERP-Web`** (MIT ✓, ★1 / ⑂0) — 7 corpus files cite it. **Skipped.**
- **`ahmerahdev/karobar-erp`** (MIT ✓, ★3) — multi-tenancy is **§3.2's explicit non-goal**. **Skipped on scope.**
- **`famalthtechnologies/famalth-lynx-pos`** (Apache-2.0 ✓, ★3) — 2 corpus files cite it. **Skipped.**
- **`ferret-project/ferret`** (MIT ✓, ★18 — the top of the mechanical star ordering) — a home-inventory app. **Not adopted.**
- **`salhiworks/sorrel-restaurant-starter`** (MIT ✓, ★1) — wrong stack (§4.1). **Not adopted.**
- **`opensourcepos`, `NexoPOS`, `n8n`, `medusajs`, `saleor`, `strapi`, `nocodb`, `directus`, `appsmith`** — **created before the window** (in-window by push only) and/or licence-incompatible (AGPL-3.0, BUSL-1.1, Sustainable Use License). **§3.2 blockers. No code adopted.**

**The HN family produced no signal for this pick** — 20 in-window hits, 0 promoted. The nearest titles are *"Show HN: Launch HN: Tableline – a simple POS for coffee shops that works offline"* and *"Show HN: Tablet menu that works without internet"* — **products, not instruments; the family is soft for the eighth consecutive pass.**

**The OpenAlex family produced no signal for this pick** — 7/7 HTTP 200, `meta.count` = 17,675 / 99 / 162 / 9 / 30,696 / 12,702 / **0** (the nonsense control, proving the filter is live), all **distinct** and none near corpus scale. **0 papers promoted.** Abstracts were carried as **raw `abstract_inverted_index` dumps only** and **never paraphrased**.

## Verification protocol

**All checks run offline. No network, no database, no browser.**

```bash
# 1. The contract file exists and is parseable.
python3 -c "import json;d=json.load(open('api-contracts/tables.json'));print(d)"

# 2. The contract's status enum matches what the API's SOURCE can return.
#    (not what the contract says — what the router returns)
python3 scripts/check-surface-drift.py --check-enum-only
#    -> asserts: {m for m in re.findall(r'TableStatus\.(\w+)', router_source)}
#                == set(contract['...']['status']['enum'])

# 3. The fixture's statuses are all producible.
python3 scripts/check-surface-drift.py
#    -> asserts: every fixture status is in the contract enum,
#                OR is explicitly marked not-yet-implemented

# 4. The fixture's fields match the contract's fields.
#    -> asserts: no undeclared fixture field; every contract field is
#                present or declared as not-yet-rendered

# 5. The corpus agrees: the surface-vs-API relationship is now owned.
grep -rl "check-surface-drift\|api-contracts" features/ specs/ | wc -l   # must be >= 1

# 6. The mock-up says what it is.
grep -c "fixture" index.html      # must be >= 1 (the one-line disclaimer)

# 7. Nothing but the named files changed.
git diff --name-only | grep -vE "^(index.html|api-contracts/.*|scripts/.*)$" | wc -l
```

**The negative control** must be run on check 3: add a fourth impossible status (`status: 'refunded'`) to the fixture and require the exit code to flip **0 → 1**. A check that has only ever passed is not evidence it works.

**⚠️ A note on the check's failure mode.** The check must **not** compare the fixture against a *snapshot* of the contract taken by hand — it must compare against the **API's source**. Otherwise, when feature 388 lands and the API starts returning `ordered`, the check will still pass while the two have genuinely diverged again. **A drift check that reads a hand-written file is a snapshot check, and it is the failure mode this feature exists to prevent.**

## Rollback path

**Revert one commit.** `git revert <the commit>`.

- **No data is at risk** — the mock-up writes nothing.
- **No schema change, no migration, no backfill.**
- **No API change** — `backend/app/routers/tables.py` is untouched; check 2 reads it, never writes it.
- **Fully reversible in one step.**
- **The rollback is visible and harmless**: the fixture's three impossible states come back and the drift check is gone. Because nothing is wired, **no operator ever sees the difference.**
- **The one thing to note in the rollback**: after reverting, the repo is back to having **no drift check at all** — which is the state this feature was filed to end. **Say so in the revert message.**
