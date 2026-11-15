# Feature 483 — The "Fire mains" button fires every `new` line, not the mains: the kitchen receives courses the guest has not ordered

> Bucket: **v1 — Core MVP**. Verdict: **`build`**. Evidence class: **OBSERVED (parsed and executed against LE31's own shipped `index.html` under Node v22, 2026-11-15)**, confidence **high** for the defect, **medium** for the operational consequence (no operator incident was observed).
>
> **This is a first-party finding.** The third-party sources from today's fetch (`satisfecho/pos`, `leandromerov/restaurant-pos-order-system`, `mrsalt227-ui/kafe78-pos`, `Farouk1901/merkevo-waiter`, `rawaerp/jordan-restaurant-pos-benchmark`, `rawaerp/jordan-jofotara-pos-integration-guide`, `shyampandey1104/python-cloud-kitchen-pos`, `prithvihouse/restaurant-pos-research`, `FranciscoM-uv/sistema-restaurante`, `AiwithFahad/burger-club-zavique-voice-ordering`, `Sholu021/KitchenIQ`) were the *instruments*; the subject is LE31's own shipped waiter screen.
>
> **The single sentence this feature exists to make true:** *the button labelled "Fire mains" fires the mains.*

## Goal

Make the shipped waiter screen's kitchen-fire control send **only the courses it says it sends**.

Concretely, three things:

1. **A "Fire mains" control fires mains, not everything.** Today it fires every line whose status is `new`, whatever the guest ordered.
2. **The screen offers the distinction its own spec asked for** — `features/02-order-taking.md` sketches **two** buttons, `[Fire mains] [Fire all]`, and the shipped screen has **one**.
3. **A check that holds the rule** — the same shape as the other shipped-surface checks.

**The charter row this touches, verbatim** (`PROJECT_CHARTER.md`):

> | **P0** | Waiter can take an order, adjust quantities, and fire courses to the kitchen. |

The acceptance criterion names **courses**. The shipped control cannot distinguish one.

## Scope

**In scope (v1):**

- **The `btn-fire` handler's filter** in `index.html` — it must select the lines the button's label claims.
- **The button set** — restore the second control (`Fire all`) that `features/02-order-taking.md` specifies, or record a decision to keep one.
- **A check** that fails if the "mains" control fires a line outside the mains set.

**Explicitly NOT in scope:**

- **A course/sequencing model.** Feature **430** records verbatim: *"`OrderItem.course` is free text"* and *"the charter never mentions 'course' at all — sequencing is out of scope by the charter's silence, and is deliberately not picked."* **This slice does not introduce `course`, does not create a `Course` table, and does not model starters/mains/desserts as an ordering dimension.**
- **The bill, the money arithmetic, the tax rate, the tip.** Features **465 / 481 / 480 / 408 / 410 / 05 / 415 / 420 / 457**.
- **`addToOrder` and the order-line quantity phase.** Feature **476**.
- **The sold-out menu filter.** Feature **475**.
- **The single-visit-per-restaurant state.** Feature **474**.
- **The seat form.** Feature **466**.
- **The floor grid.** Feature **24**.
- **The mock-up/API drift check.** Feature **467**.
- **Any schema change, any migration, any Python file, any new dependency.**

## Description

### The defect, as parsed from LE31's own shipped file

The button, verbatim from `index.html`:

```html
<button class="btn" id="btn-fire">Fire mains</button>
```

And its handler, verbatim:

```javascript
document.getElementById('btn-fire').addEventListener('click', () => {
  state.visit.items.filter(x => x.status === 'new').forEach(x => x.status = 'preparing');
  renderOrder();
  alert('Fired all new items to kitchen. (In real app → Telegram message to cook)');
});
```

**The handler filters on `x.status === 'new'` and on nothing else.** There is no category test, no course test, no item-type test. The button is labelled `Fire mains` and it fires **everything that is new**.

### The measured evidence

Executed against the shipped file under Node v22 on 2026-11-15:

```text
=== FACT 1: "Fire mains" has no main/course filter ===
button label in HTML: Fire mains
handler body:
   document.getElementById('btn-fire').addEventListener('click', () => {
     state.visit.items.filter(x => x.status === 'new').forEach(x => x.status = 'preparing');
     renderOrder();
     alert('Fired all new items to kitchen. (In real app → Telegram message to cook)');
   });
does index.html reference `course` at all? -> NO (zero occurrences)
MOCK_MENU categories present: Mains, Sides, Drinks, Desserts
=> a "Mains" filter would be possible via category, but the handler filters on STATUS only.
=> every line with status "new" is fired, whatever its category.
```

**The word `course` appears zero times in all 31,096 bytes of `index.html`** — despite `PROJECT_CHARTER.md` naming "fire courses" as the P0 capability, and despite `features/02-order-taking.md` naming the "fire course" trigger.

**And the category data needed for the filter is already in the fixture.** `MOCK_MENU` carries `category` values `Mains`, `Sides`, `Drinks`, `Desserts` — the screen already groups the menu by category in `renderMenu()` (`[...new Set(MOCK_MENU.map(m => m.category))]`). **The category is available; the order line just does not carry it forward.**

### The order line does not carry a category

`state.visit.items` entries are created in exactly two places:

```javascript
// addToOrder
state.visit.items.push({ menu_item_id: item.id, name: item.name, qty: 1, unit_price: item.price, status: 'new' });
// the fixture
{ menu_item_id: 1, name: 'Schnitzel', qty: 1, unit_price: 14, status: 'preparing' }
```

**There is no `category` field on an order line.** The filter must therefore join the line to `MOCK_MENU` by `menu_item_id` — which is exactly the key the line already carries. **This is the implementer's central design decision, and it is recorded below.**

### The spec that asked for two buttons

`features/02-order-taking.md` — LE31's own informal spec for order taking — contains, verbatim:

> - Send "fire course" trigger (e.g. send all mains now, hold desserts).

and its mock-up sketch shows, verbatim:

```
│  Wine      5€  │ [Fire mains] [Fire all]   │
│                │ [Bill] [Close visit]      │
```

**The spec asked for two controls and named the behaviour. The screen shipped one, and the one it shipped does the other one's job.**

### Why this is not a duplicate of feature 476

Feature **476** (`le31-the-shipped-waiter-screen-adds-a-dish-to-a-line-the-kitchen-has-already-served…`) uses the `btn-fire` handler as the *place where the kitchen would be told*, in order to show that a quantity change on a served line **never reaches the kitchen**. Its subject is **the quantity changing after the line was served**. Its HANDOFF explicitly says: *"Do NOT touch: … the `btn-fire` handler"*.

**This feature's subject is the opposite: which lines the handler selects.** 476 owns *"a changed quantity is not fired";* this feature owns *"an unchanged, newly-added drink is fired by a button called Fire mains."* **They are complementary and must not be merged.**

### Why no filed feature owns it

A corpus-wide grep over all **516** feature contracts and **476** HANDOFFs, printing the matching line for every hit:

| Shape searched | Result |
|---|---|
| A feature names `Fire mains` **as a defect** | **0 hits.** The three matches are feature 476's *Do NOT touch* note, feature 02's **own informal spec** (a sketch, not a contract — it has no `## Out of scope`, no gate verdict, no verification protocol), and feature 344's unrelated AI-waiter vocabulary. |
| A feature states that the fire control ignores **category** | **0 hits** |
| A feature states that the screen **cannot distinguish courses** | **0 hits** |
| A feature states that `index.html` contains **zero** occurrences of `course` | **0 hits** |

**The corpus knew the spec asked for two buttons, because the spec is a file in the corpus — but nobody read the spec against the screen.** That is the same failure mode feature **431** documents: *"the corpus already knows this gap exists and has never filed it."*

### Data model

**No schema change. No new table. No migration. No Python file.**

The change is to `index.html` and is of one of two shapes:

| Direction | What changes | When it is right |
|---|---|---|
| **Filter by category** (recorded default) | The mains control selects lines whose `menu_item_id` resolves to a `MOCK_MENU` entry with `category === 'Mains'`. A second `Fire all` control keeps the old behaviour. | **When "mains" means the `Mains` category.** The fixture's categories are `Mains` / `Sides` / `Drinks` / `Desserts`, and the spec's own words are *"send all mains now, hold desserts"* — **category-shaped.** |
| **Do not filter; rename the button** | The button is renamed `Fire all` and the spec is corrected to match. | **When course separation is not a v1 requirement.** Cheapest, but it makes the screen's *capability* smaller than the charter's P0 row. |

**Recorded default: filter by category, and restore the second button.** The evidence is that the fixture's category vocabulary already exists and the spec already names the exact behaviour (*"send all mains now, hold desserts"*). **The implementer must state which direction was taken and why.**

**What this slice must NOT do under either direction:** introduce `course` as a field, create a `Course` table, add a course/sequencing model, or change the charter's silence about sequencing (feature **430**'s recorded decision).

### Implementation steps

1. **Decide and record the direction** — filter by category, or rename the button and correct the spec. **Recorded default: filter by category.** Record the decision in a comment at the handler.
2. **Resolve the line's category.** The order line carries `menu_item_id`, not `category`. **Two options, and the contract names the preferred one:** (preferred) look the category up from `MOCK_MENU` by `menu_item_id` at fire time — no state shape change, and the lookup is the same one `renderMenu()` already does; (acceptable) add a `category` field to the order line at creation time — but then **every** place a line is created must set it, including the fixture, and the field can drift from `MOCK_MENU`.
3. **Make the filter explicit and named.** A named helper (e.g. `function isMain(line) { … }`) so the rule is in one place and a test can call it.
4. **Decide and record the second button's fate.** `features/02-order-taking.md` sketches `[Fire mains] [Fire all]`. **Recorded default: add `Fire all`, keeping the old behaviour available**, because the old behaviour is what the waiter gets today and removing it would remove a capability without being asked to.
5. **Correct the alert text.** It currently reads *"Fired all new items to kitchen."* **After the change it must say what it actually did** — the alert is the only feedback the waiter gets, and a wrong alert is a false confirmation.
6. **Add the check** (see *Verification protocol*). **Write it first — it must fail on today's file.**

### Telegram interaction if any

**None.** This feature is entirely inside the waiter's browser. It **does not** add a Telegram command, does not change any bot handler, and does not change what the cook receives.

**The relationship to the cook surface is the point, though:** the shipped `btn-fire` alert says *"(In real app → Telegram message to cook)"*. **When the Telegram message is built, it must carry the same selection the button made** — otherwise the cook receives the drinks anyway and this slice has fixed the waiter's screen while leaving the kitchen's reality unchanged. **That mapping is feature 02's and the kitchen-display feature's work; this slice must record it, not implement it.**

### Dependencies

- **`index.html`** — the `btn-fire` handler, the `btn-fire` button, the `MOCK_MENU` fixture (read-only for the category lookup), and `state.visit.items`.
- **Feature 476** — owns `addToOrder` and the quantity phase. **It explicitly says *"Do NOT touch: … the `btn-fire` handler."* **This feature touches exactly that handler — so the two must be sequenced, not developed in parallel against the same file.** Their regions are disjoint in *intent* but 476's fix changes what a `new` line means.
- **Feature 474** — owns the single-visit state. **The fire control acts on `state.visit.items`, so this feature's test is only meaningful once 474's per-table order state lands.** Recorded as a dependency, not a blocker for the contract.
- **Feature 467** — owns the fixture/API drift check. **This slice changes the fixture's *use*, not the fixture's *contents*.**
- **Feature 430** — owns the decision that `OrderItem.course` is out of scope by the charter's silence. **This feature must not reopen it.**
- **Feature 02** (`features/02-order-taking.md`) — the informal spec this feature is reconciled against. **It is not a contract and this feature does not restructure it** beyond correcting the button set.

### Open questions

1. **Does "mains" mean the `Mains` category, or a course sequence?** **Recorded default: the `Mains` category.** The fixture's vocabulary and the spec's wording (*"hold desserts"*) both point that way, and a course model is out of scope by feature 430's recorded decision. **The implementer must state which was used.**
2. **Should `Fire all` be added, or should `Fire mains` be renamed?** **Recorded default: add `Fire all`.** The old behaviour is a capability the waiter has today.
3. **What about `Sides`?** A European service fires the main *and* its sides together. **Recorded default: `Fire mains` fires the `Mains` category only; `Fire all` fires everything.** The implementer may argue for `Mains` + `Sides` and must record the argument if they do.
4. **Does the kitchen message mirror the button's selection?** **Recorded: yes, and it is not implemented here.** This slice must record the mapping so feature 02's Telegram implementation inherits it.

### Why this matters

**The kitchen is a physical place with a finite amount of attention. Sending it a course the guest has not ordered is not a cosmetic error — it is prep work, plate space, and a conversation with the cook.**

And the specific thing that makes this defect worth a contract rather than a one-line fix is that **LE31's own spec already said the right thing, and the screen ignored it.** `features/02-order-taking.md` names the trigger, describes the behaviour in a sentence, and draws two buttons. **The implementation shipped one button doing the other one's job.** A reader of the shipped file alone would never know the distinction was supposed to exist — which is exactly how a spec-only distinction dies: quietly, in a mock-up that is the only artefact the owner loads.

**The cost of leaving it is not zero, and it is not hypothetical either.** The mock-up makes zero `fetch()` calls, so **no live surface exists on which this can currently misfire** — the honest statement is that the defect is certain and its frequency is unobserved. But the mock-up **is** the artefact feature 474 identifies as *"the one artefact in the repository that can demonstrate the product working"*, and the charter's P0 acceptance criterion for order taking is judged against it. **The screen the owner loads teaches the wrong thing about what the product does.**

**And the second cost is the drift.** The moment a second button exists, the filter rule must live in one named place. A rule that lives inline in a click handler is a rule the next handler will not copy — and the next handler is the Telegram one.

### Adjacent evidence

1. **`btn-fire` is the only channel to the kitchen in the shipped screen, and it has no notion of *which* channel.** Feature **476** already recorded this handler as the place where the kitchen would be told. **Its subject is the quantity phase, not the selection.** Recorded here; **not** merged.
2. **The screen renders a `Bot (cook)` tab whose fixture shows `/sold_out tiramisu` working** while the shipped dispatcher routes only two commands. Feature **468** owns the help-text correspondence; **this feature does not touch the bot.**
3. **`MOCK_MENU` already groups by category in `renderMenu()`.** The category vocabulary is not new; it is simply not carried onto an order line. Recorded as evidence that the fix is small.
4. **Third-party corroboration — vocabulary only, no code adopted.** `satisfecho/pos` (★66, AGPL-3.0, licence-incompatible) and `leandromerov/restaurant-pos-order-system` (MIT, 0★) both describe kitchen-display systems that separate what is sent to the kitchen from what is ordered. **Neither was executed against LE31's flow and neither is a source of implementation.** The transferable rule is LE31's own: **an operational trigger must select exactly what it claims to select.**

### Verification protocol

1. **The filter is named and callable.** A named helper exists and returns the mains set for a given `state.visit.items`.
2. **The mains control fires mains only.** With a fixture containing one `Mains`, one `Sides`, one `Drinks` and one `Desserts` line, all `status: 'new'`, invoking the mains control transitions **only the `Mains` line** to `preparing`.
3. **`Fire all` still fires everything.** With the same fixture, invoking it transitions all four.
4. **The alert tells the truth.** The alert text names what was fired and must not say "all new items" when only mains were fired.
5. **A category-less line is handled.** A line whose `menu_item_id` does not resolve in `MOCK_MENU` must **not** be fired by the mains control and **must not** throw. **The implementer must decide and record what `Fire all` does with it.**
6. **The regression test fails on today's file.** Steps 2 and 4 **must fail** against the shipped `index.html` before the fix is applied. **If they pass, the test is not testing the defect.**
7. **The corpus agrees.** `grep -rn "Fire mains" features/ specs/` must hit **this** contract.

## Rollback path

**Fully reversible.** The change is confined to `index.html`: one handler, one button, one helper.

- **Roll back by reverting the file.** No schema change, no migration, no data.
- **There is no data at risk**: the mock-up persists nothing, and no persisted state changes.
- **The one thing a rollback loses** is the filter rule. Reverting restores the unfired-everything behaviour and the drift returns with it.

## Out of scope

- A course or sequencing model, `OrderItem.course`, or any course table — feature **430**'s recorded charter-silence decision.
- The Telegram message to the cook and how it is selected — feature **02** and the kitchen-display work.
- `addToOrder` and the order-line quantity phase — feature **476**.
- The sold-out menu filter — feature **475**.
- The single-visit state — feature **474**.
- The seat form — feature **466**.
- The floor grid — feature **24**.
- The fixture/API drift check — feature **467**.
- The bill, the money arithmetic, the tax rate, the tip — features **465 / 481 / 480 / 408 / 410 / 05 / 415 / 420 / 457**.
- Any Python file, any endpoint, any schema change, any migration, any new dependency.
