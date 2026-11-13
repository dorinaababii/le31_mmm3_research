# Feature 476 — The shipped waiter screen adds a dish to a line the kitchen has already served: the quantity changes and nobody is told

> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED (executed under `node` against the shipped `index.html`)**, confidence **high** for the defect, **low** for the demand (the *frequency* of a guest adding a dish after the first was served is not evidenced and is not claimed).
>
> Third-party vocabulary source: `hekimcan206/offline-pos-sync` (MIT, created 2026-11-11) — an offline-first POS sync engine whose README names the exact class of failure: *"Two terminals edit the same ticket while offline: both tap '+1', one takes payment while the other voids the ticket, someone adds a dessert after the bill was paid"* and *"last write wins silently loses a quantity."* **Vocabulary reference only** — LE31 adopts no code from this repository.

## Goal

Make **the shipped order screen refuse to change a line the kitchen has already started on** — so that the quantity on the screen is the quantity the kitchen cooked, and a change to an order is something the kitchen is told about.

Concretely, three things:

1. **A line's quantity is only editable while the line is still `new`.** Once it has been fired to the kitchen, its quantity is a fact about what the kitchen is cooking.
2. **A change to a fired line is a new line, or a refusal** — never a silent mutation of the fired line.
3. **A check that holds the rule**, because the shipped file is the surface the charter's §7 clause *"End-to-end before commit"* is supposed to be able to exercise, and today it cannot.

**The single sentence this feature exists to make true:** *the waiter screen does not change the quantity of a dish the kitchen is already cooking, and if the guest adds that dish anyway, the kitchen finds out.*

## Scope

**In scope (v1):**

- **One editability predicate in `index.html`** with exactly one definition, answering *"may this line's quantity still be changed?"*.
- **The quantity controls on an order line are hidden or disabled for a line that is not `new`** — so the surface does not offer an action it must then refuse.
- **The order path refuses the change** — adding a dish whose existing line has already been fired must **not** silently increment the fired line. It must **add a separate line** (the kitchen then cooks one more) **or refuse and say why**. **Decided: add a separate line** — refusing would make the guest's second Schnitzel unorderable, which is a service failure of its own.
- **A regression check** that fails on today's `index.html` and passes on the fixed one.

**Explicitly NOT in scope:**

- **The server-side order-line quantity rule.** Feature **456** (`le31-order-item-qty-may-be-zero-or-negative…`) owns the server-side constraint on `order_item.qty`'s sign and size. **This slice does not add a CHECK, does not touch `backend/app/models.py`, and does not change any Python file.**
- **The server-side status↔timestamp coherence rule.** Feature **452** (`le31-an-order-line-can-be-served-and-still-say-it-is-new…`) owns it — including the scenario it quotes, *"qty=3 of it is already served"*. **452 is a server-side write-path rule; this slice is the shipped screen's rule.** They must agree, and each says so.
- **The order-line transition log and its actor.** Feature **379** owns the append-only `OrderItemTransition` table and the `by_user_id` column. **This slice does not build a transition log and does not add an actor column.**
- **The `course` field.** Out of scope by the charter's silence — recorded explicitly in features **430** and **453**. Not touched.
- **The line-level allergen field.** Feature **439** owns it. Not touched.
- **The kitchen's own screen.** LE31 has none — the cook's surface is the Telegram bot, whose `/start_today` flow is a stub. **This slice does not build a kitchen screen.**
- **The per-table order state.** That is feature **474** — the global `state.visit`. **This slice assumes 474's per-table state exists; if 474 has not landed, this slice's predicate still applies to whatever single visit the file holds.** The regions are disjoint.
- **The money arithmetic.** Feature **465**. Not touched.
- **Any schema change, endpoint, or migration.**

## Description

### The defect, as executed

The shipped order handler, verbatim from `index.html`:

```js
function addToOrder(item) {
  const existing = state.visit.items.find(x => x.menu_item_id === item.id);
  if (existing) existing.qty += 1;
  else state.visit.items.push({ menu_item_id: item.id, name: item.name, qty: 1, unit_price: item.price, status: 'new' });
  renderOrder();
}
```

**There is no check on the existing line's `status`.** The handler finds the first line with a matching `menu_item_id` and increments its quantity — whatever state that line is in.

Executed under `node` against the file's own handler:

```
=== LEAD 1: addToOrder on a line that is already SERVED ===
  the shipped handler:
    | function addToOrder(item) {
    |   const existing = state.visit.items.find(x => x.menu_item_id === item.id);
    |   if (existing) existing.qty += 1;
    |   else state.visit.items.push({ menu_item_id: item.id, name: item.name, qty: 1, unit_price: item.price, status: 'new' });
    |   renderOrder();
    | }

  before: qty=1 status=served
  after : qty=2 status=served
  >>> adding a dish to a SERVED line incremented its qty to 2.
  >>> the cook already served 1; the line now claims 2 were served.
  >>> nothing in the shipped file records that the qty changed after service,
      and the kitchen is never told.
  a PREPARING line: qty 2 -> 3
```

**Three distinct failures, one root cause.**

1. **The quantity of a served line changes.** The kitchen served one Schnitzel. The screen now says two were served. The guest has ordered one and been served one; the ticket says two.

2. **The kitchen is not told.** The shipped surface's only channel to the kitchen is the `btn-fire` handler:

   ```js
   document.getElementById('btn-fire').addEventListener('click', () => {
     state.visit.items.filter(x => x.status === 'new').forEach(x => x.status = 'preparing');
     renderOrder();
     alert('Fired all new items to kitchen. (In real app → Telegram message to cook)');
   });
   ```

   It fires only lines whose status is `new`. A line already `preparing` or `ready` is **never re-fired**, so a quantity added to it **never reaches the kitchen at all**. The kitchen is cooking one; the screen says two; nobody told them.

3. **Two lines with the same dish are indistinguishable.** `find(x => x.menu_item_id === item.id)` returns the **first** match. So once the guest orders Schnitzel, the chef plates it, it goes `served`, and the guest orders Schnitzel **again** — the second Schnitzel lands on the **served** line:

   ```
   -> the waiter taps Schnitzel again:
      qty of the SERVED line = 2
   >>> a second Schnitzel ordered AFTER the first was served lands on the
       served line, so the kitchen is told nothing and the ticket says 2 served.
   ```

   **This is the everyday case, not an edge case.** It happens the first time a guest re-orders a dish. The line says `served`, the guest has had one and ordered a second, and the kitchen — which is about to receive a ticket saying "2 × Schnitzel" — receives nothing, because the line was already fired.

### The rule that is missing

The shipped file has a status ladder, and it is the right vocabulary — but it is used only to *display* a line, never to *gate* an edit:

```js
const STATUS_FLOW = ['new', 'preparing', 'ready', 'served'];
```

Feature **452** already established the server-side rule this slice's predicate must mirror:

> *"a line's `status` and its timestamps are two views of the same fact, and they may not disagree."*

**The shipped screen's gap is the same rule one step further on:** a line's `status` and its **quantity** are also two views of the same fact — *what the kitchen is cooking* — and a fired line's quantity is a fact about the kitchen, not about the order. **The screen lets the order rewrite the kitchen's fact.**

### Why the corpus does not own this

- Feature **456** owns the **server-side** constraint on `order_item.qty` — that it may not be zero or negative. **That is a different rule**: it constrains the *value*, not *when the value may change*, and it lives in a `CHECK` constraint on a table that does not exist yet in any route. **Nothing about the shipped screen's edit rule.**
- Feature **452** owns the **server-side** status↔timestamp coherence rule and its write helper. Its *Scope* is about a **write path** and a **predicate over rows**; **the shipped screen has no write path, no timestamps and no persistence** — it mutates an in-memory array. **452 cannot cover it.**
- Feature **379** owns the **transition log and actor**. **The shipped screen's defect is not a missing actor** — it is a *missing gate*. 379 would record who fired the line; it would not stop the quantity changing afterwards. **Different mechanism.**
- Feature **430** owns the order line's **insertion time** (`added_at`), and its *Out of scope* explicitly puts `course` aside. **It does not own when a quantity may change.**
- Feature **474** owns the **per-table order state**. **This slice is about the rules *within* one party's order** — a different concern, and the file regions are disjoint (474: the `state` object and the floor/seat handlers; 476: the order-line controls and `addToOrder`).

### What the third-party source contributes (vocabulary only)

`hekimcan206/offline-pos-sync`'s README names this exact class of failure, in a system built specifically to survive it:

> *"Two terminals edit the same ticket while offline: both tap '+1', one takes payment while the other voids the ticket, someone adds a dessert after the bill was paid."*
>
> *"Last write wins silently loses a quantity or erases a paid sale."*

Its design separates three concerns that LE31's shipped screen collapses into one: **row LWW**, **field-level LWW**, and **domain rules** (ADR 0002, *"merge strategies, field registers and domain lattices"*). LE31's screen has **none** of the three. `existing.qty += 1` is a **read-modify-write with no domain rule** — the textbook last-writer-wins on the one field that must not be last-writer-wins.

The transferable vocabulary is the **domain-lattice idea**: a quantity on a fired line is not a free number that any writer may set; it is a **monotone count within a phase**. Once the kitchen owns it, only an **increment that the kitchen can see** may change it. LE31's answer for a single-screen, no-sync surface is simpler than a lattice but the same shape: **the fired quantity is the kitchen's; the order's additional quantity is a new line.**

**Vocabulary reference only.** `offline-pos-sync` is a .NET/PostgreSQL engine with a SQLite outbox, an `INSERT … ON CONFLICT (change_id) DO NOTHING` arbiter and a Toxiproxy test harness. **LE31 adopts none of it.** §3.1 requires SQLite compatibility that a .NET engine cannot provide, and LE31's v1 has one server and no outbox.

## Data model

**No schema change. No Python change. No endpoint.** The state lives in the browser, and it changes shape in exactly one way:

```js
// BEFORE — every line is mutable, whatever its status
{ menu_item_id: 1, name: 'Schnitzel', qty: 1, unit_price: 14, status: 'served' }

// AFTER — a fired line keeps its quantity; a NEW line carries the extra
{ menu_item_id: 1, name: 'Schnitzel', qty: 1, unit_price: 14, status: 'served' }   // unchanged
{ menu_item_id: 1, name: 'Schnitzel', qty: 1, unit_price: 14, status: 'new'    }   // the second one
```

**Two lines with the same `menu_item_id` is the correct outcome, not a bug.** The shipped file's `addToOrder` already has the "else push a new line" branch — it is simply never reached for a fired dish. **This slice makes it reachable.**

## Implementation steps

1. **Add `isQuantityEditable(line)` with exactly one definition.** It returns `line.status === 'new'`. **Do not inline `x.status === 'new'` in a second place** — the shipped file already has that literal inside the fire handler, and a third copy is how the two diverge.
2. **Hide or disable the quantity controls on a line that is not `new`.** The shipped order row renders, verbatim:

   ```js
   <span class="qty-controls">
     <button title="Bump status" data-act="bump">⏵</button>
     <button title="Remove" data-act="×">×</button>
   </span>
   ```

   The "Remove" button is present on **every** line, including a `served` one. **A line the kitchen has finished must not be removable from the screen either** — that is the same class of defect (a served line is the kitchen's fact) and it is fixed by the same predicate. **Decided: the remove control is hidden on a line that is not `new`, for the same reason.** Recorded so it is not lost.
3. **Change `addToOrder` to respect the phase.** The lookup must find a line that is **still editable** — not merely a line with the same `menu_item_id`:

   ```js
   const existing = state.visit.items.find(x => x.menu_item_id === item.id && isQuantityEditable(x));
   ```

   If a fired line exists with that dish, the `else` branch runs and a **new `status: 'new'` line** is pushed. **The kitchen then receives it on the next fire, because the fire handler picks up exactly the `new` lines.**
4. **Do not change the fire handler.** `state.visit.items.filter(x => x.status === 'new').forEach(x => x.status = 'preparing')` already does the right thing — with step 3 in place, a re-ordered dish is a `new` line and is fired correctly. **This slice does not touch the fire handler.**
5. **Do not touch `bumpStatus`.** The ladder is correct; it is feature **452**'s territory to make the server's ladder agree with it.
6. **Add the regression check** (see *Verification protocol*).

## Telegram interaction if any

**None.** The kitchen is told about a fired line by the shipped surface's `alert('Fired all new items to kitchen. (In real app → Telegram message to cook)')` — a placeholder, not a bot call. **This slice does not change `backend/app/bot/cook_bot.py`, does not add a command, and does not change an FSM state.** Feature **403** owns the Telegram allowlist; feature **379** owns the transition log's actor.

## Dependencies

- **Feature 452** (`le31-an-order-line-can-be-served-and-still-say-it-is-new…`) — **read first.** It owns the server-side status↔timestamp coherence rule and its predicate. **This slice's predicate must mirror 452's rule exactly**, and each contract must cite the other. **452 is a server-side write-path rule; this is a screen-side rule — different mechanisms, must not be merged.**
- **Feature 456** (`le31-order-item-qty-may-be-zero-or-negative…`) — owns the server-side constraint on `qty`'s sign and size. **This slice must not add a sign constraint to the server** — the ledger's negative delta is legitimate (a sale consumes stock), and 456's own contract makes that point about the ledger. **This slice adds no server-side rule at all.**
- **Feature 379** (`le31-order-item-transition-attribution…`) — owns the transition log and the actor column. **This slice adds no log and no actor.**
- **Feature 474** (`le31-the-shipped-waiter-screen-holds-one-visit-for-the-whole-restaurant…`) — owns the per-table order state. **This slice assumes it; the file regions are disjoint.**
- **Feature 465** (`le31-the-waiters-screen-shows-a-different-tip…`) — owns the money in the same file. **The order row's price rendering must not be forked.**
- **Feature 430** (`le31-order-item-has-no-insertion-time…`) — owns `added_at`. **This slice does not add a timestamp.**
- **Charter §7** — *"End-to-end before commit"*, and the charter's own line-level vocabulary (`OrderItem.status` with `new`/`preparing`/`ready`/`served`).

## Open questions

1. **Should adding a dish after it was fired create a new line, or refuse?** — **Decided: a new line.** Refusing would make the guest's second Schnitzel unorderable, which is a service failure of its own and puts the waiter in the position of lying to the guest. **A new line is also the only outcome the shipped fire handler already knows how to deliver** — it fires exactly the `new` lines.
2. **What about the `Remove` button on a fired line?** — **Decided: hide it on any line that is not `new`.** Same reason as the quantity: a served line is the kitchen's record. **Recorded so the implementer does not treat it as out of scope.**
3. **Should the screen's editability rule be `'new'` only, or `'new'` and `'preparing'`?** — **Decided: `'new'` only.** A `preparing` line is already in the kitchen; changing its quantity has the same defect as changing a `served` one. **Feature 452's server-side rule must be read to confirm it agrees.** Recorded so the two do not drift.
4. **Should the extra line carry a note explaining why there are two lines?** — **Decided: no.** The screen is a mock-up; the line's `status: 'new'` already distinguishes it from the fired one, and the order row shows the status pill. **A note is a server-side concern (feature 379's transition log).**
5. **Does this need the order-line status pill to be more prominent?** — **Decided: no.** That is the mock-up's visual design, and feature **467** and **465** both guard it. **Out of scope.**

## Why this matters

**The defect the third-party source names — *"someone adds a dessert after the bill was paid"* — is the first case in LE31's history where the corpus has a *named* external description of the exact failure mode, and LE31's shipped surface has that failure in its most ordinary form.**

Not as an edge case. As **the first time a guest re-orders the dish they just finished.** "Two schnitzels, please" — with one already served. In that moment the shipped screen does three wrong things at once:

1. The **served** line's quantity becomes 2 — so the screen claims two were served when one was.
2. The **kitchen is never told** — the fire handler only fires `new` lines, so the second schnitzel is on the screen and not in the kitchen.
3. **The bill is now wrong by one dish.** The bill modal sums the order lines. A line that says `qty: 2, status: 'served'` contributes two dishes to the total. **The guest is charged for a dish the kitchen never received.**

**Point 3 is the one that makes this a money defect, and it is why this slice is not a UI-polish item.** Feature **465** already found that the shipped bill modal computes money in JavaScript floats and renders *"Underpaid by 0.34 €"* where the server says `-0.35`. That is a **rounding** defect, worth fractions of a cent. **This one is a whole dish.** The meal's subtotal, tax, total and derived tip are all computed from a line whose quantity the kitchen has never seen.

**And the failure is invisible in the exact way LE31's other surface failures are invisible.** There is no error, no alert, no red state. The line reads `Schnitzel ×2  served`. It looks *finished*. The waiter sees a completed order. The kitchen sees a ticket with no second schnitzel. The guest waits for a dish that was never ordered and was charged for.

**The cost of the information decays, and LE31's own corpus says so.** Features 444, 452 and 379 each established the same principle: *a line's status, its timestamps and its quantity are three views of one fact, and they must not disagree.* **Once the disagreement exists, nothing in LE31 can reconstruct which value was right** — there is no transition log (379, unbuilt), no insertion time (430, unbuilt), and the shipped screen keeps no record at all. **The guest's second schnitzel exists only as a number on a line that says it was served.**

**This is also the cheapest remaining fix in the shipped surface.** One predicate, one changed `find` condition, one hidden control. **No schema, no Python, no endpoint, no migration, no fixture change** — and it makes the shipped screen consistent with the server-side rule feature 452 has already specified, so the two surfaces will agree when the mock-up is eventually wired.

**And it is the second of the two charter-adjacent defects in the shipped surface** (the first being 475's sold-out dish). **Together they say something the corpus has not said before about `index.html`: it is not a mock-up of a product, it is a product.** It has a menu the waiter reads to the guest, an order the kitchen is supposed to receive, and a bill the guest is charged on. **Three of its rules are wrong, and the charter's own P0 acceptance criteria name two of them.**

## Adjacent evidence

| Source | What it contributes | Disposition |
|---|---|---|
| `hekimcan206/offline-pos-sync` (MIT, created 2026-11-11, ★0) | The **named failure** — *"both tap '+1' … someone adds a dessert after the bill was paid"*, *"last write wins silently loses a quantity"*, and the three-way split of merge strategies (row LWW / field LWW / domain rules, ADR 0002 *"merge strategies, field registers and domain lattices"*). LE31's `existing.qty += 1` is a read-modify-write with **no domain rule**. | **Vocabulary reference only.** LE31 adopts no code. The transferable idea is the **domain-lattice principle**: a fired quantity is not a free number any writer may set — it is a count within a phase, and an increment that the kitchen cannot see must not land on it. |
| `lorenzoyang/TavoloFlow` (AGPL-3.0, created 2026-10-16, ★22) | Its README describes the **kitchen screen** as the place where *"the kitchen and the pass see the dishes as they arrive"*, with *"per-screen category filters"* — i.e. **the kitchen's view of a dish is a separate view with its own state**, not a projection of the waiter's screen. | **Vocabulary reference only.** Confirms the **two-views-one-fact** structure: the waiter's order and the kitchen's ticket are two surfaces over one dish. LE31's defect is that only one of them exists. |
| `Raktim94/nodedr-restaurant-pos` (AGPL-3.0, created 2026-08-03) — *"Self-hosted restaurant POS with tables, kitchen display, reservations, QR ordering, loyalty and local-network operation."* | A recent (created 2026-08-03, in-window) restaurant POS whose description names **kitchen display** as a first-class surface alongside the tables. | **Recorded, not adopted.** Its README was not fetched this pass; **no claim is made about its contents** beyond the one-line description quoted here, which came from the GitHub search response. |
| `MustrHQ/kitchen-safety` (AGPL-3.0, created 2026-10-26) | The **split between the asserting surface and the displaying surface** — a login-free kitchen frontend whose names are *"self-reported, not authenticated staff identities"*, and a protected admin panel. | **Vocabulary reference only.** Supports the argument that a quantity the kitchen owns must not be silently rewritten by the order side. |

## Verification protocol

Seven checks, all offline, no network, no database, no browser.

```bash
# 1. THE PREDICATE EXISTS AND HAS EXACTLY ONE DEFINITION.
grep -c 'function isQuantityEditable' index.html      # must be 1
grep -c "x\.status === 'new'" index.html               # must be 1  (the fire handler's own copy
                                                      #            is the only other allowed one)

# 2. A SERVED LINE'S QUANTITY DOES NOT CHANGE.
#    (the exact scenario that fails today)
node <scripts/prove_order_view.js>
#    expected: "after : qty=1 status=served"   (today it prints qty=2)

# 3. THE SECOND ORDER OF A DISH BECOMES A SEPARATE LINE.
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const M=eval('('+s.match(/const MOCK_MENU = \[[\s\S]*?\n\];/)[0].replace('const MOCK_MENU =','').replace(/;\$/,'')+')');
         const body=s.match(/function addToOrder\(item\) \{[\s\S]*?\n\}/)[0];
         if(!/isQuantityEditable/.test(body)){
           console.error('FAIL: addToOrder does not respect the phase');process.exit(1)}
         console.log('PASS: addToOrder finds only an editable line')"
#    and: after adding, the fixture must hold TWO lines with that menu_item_id,
#    one 'served' qty=1 and one 'new' qty=1.

# 4. THE FIRE HANDLER STILL PICKS UP THE NEW LINE.
grep -c "filter(x => x.status === 'new')" index.html    # must be 1 -- the fire path is unchanged

# 5. THE CORPUS AGREES: this slice is now owned.
grep -rl 'isQuantityEditable' features/ specs/          # must include features/476-*.md

# 6. THE SERVER-SIDE RULE IS CITED, NOT DUPLICATED.
grep -c '452' features/476-*.md                         # must be >= 1
grep -c '456' features/476-*.md                         # must be >= 1

# 7. NOTHING OUTSIDE index.html CHANGED.
git diff --name-only <base>...HEAD -- . ':(exclude)index.html'   # must be empty
```

**The negative control.** Re-inject the defect — restore `const existing = state.visit.items.find(x => x.menu_item_id === item.id);` — and **checks 2 and 3 must fail**. A check that cannot fail proves nothing. If check 2 passes on the unmodified file, the verifier is wrong, not the file.

**A second negative control is required for check 2 specifically:** the check must fail on today's file, because today's file is exactly the defect. **If check 2 passes before the fix, the check is vacuous.**

## Rollback path

`git revert` the single commit that touched `index.html`. The change is one predicate, one changed `find` condition, and one hidden control. **No schema, no database, no server-side state, no API contract, no fixture data.** Reverting restores the shipped behaviour exactly, including the defect. **Rolling back is free.**
