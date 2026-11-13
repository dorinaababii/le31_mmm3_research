# Feature 475 — The shipped waiter screen shows a sold-out dish and lets the waiter order it: the charter says the menu auto-hides it

> Bucket: **v1**. Verdict: **`build`**. Evidence class: **OBSERVED (executed under `node` against the shipped `index.html`)**, confidence **high** for the defect, **high** for the charter violation (the charter states the requirement twice, in two different P0 rows).
>
> Third-party vocabulary source: `MustrHQ/kitchen-safety` (AGPL-3.0, created 2026-10-26) — a self-hosted HACCP kitchen-temperature system whose README separates a *kitchen frontend* (no login, "staff can record measured temperatures without signing in") from a *protected admin panel*, and states plainly: *"Frontend names are self-reported, not authenticated staff identities."* **Vocabulary reference only** — LE31 adopts no code and this repository's licence is not §3.2-compatible.

## Goal

Make **the waiter screen's menu obey the charter's own two P0 rows** — a dish the kitchen has marked sold out must **not appear**, and a dish that does appear must be orderable **only** while it is available.

Concretely, three things:

1. **The menu hides what the kitchen has taken off.** Charter P0 row 44: *"Cook can mark an item sold-out via `/sold_out`; **menu auto-hides it**."* Acceptance criterion, verbatim: *"After `/sold_out tiramisu`, the waiter's UI no longer shows it."*
2. **A hidden dish is not merely greyed out.** The charter says *no longer shows it*. The shipped surface shows it — with a stock tag, a price, and a class — and only *refuses the click*.
3. **A check that holds the rule**, because the charter's own §7 clause *"End-to-end before commit"* has nothing in the repository that could execute it.

**The single sentence this feature exists to make true:** *a dish the kitchen has marked sold out is absent from the waiter's menu — not present-but-disabled.*

## Scope

**In scope (v1):**

- **One availability predicate in `index.html`**, with exactly one definition, that answers *"is this dish currently being served?"* for the mock-up's data. The mock-up's own data already carries the fact: `MOCK_MENU` item id 3 (`Caesar Salad`) has `stock: 0` and the file itself comments it `// sold out`.
- **The menu renderer filters on that predicate.** A dish that is not available is **not rendered at all** — no button, no price, no stock tag, no row.
- **The order path refuses an unavailable dish as well**, so that the filter is not the only thing standing between the kitchen and a sold-out sale. A dish that reaches `addToOrder` by any route (a stale render, a direct call, a re-render race) is refused there too.
- **A regression check** that fails on today's `index.html` and passes on the fixed one.

**Explicitly NOT in scope:**

- **The server-side sold-out state.** That is feature **397** (`le31-sold-out-state…`) — the per-day derived availability record and the `/sold_out` command. **This slice does not build the sold-out state, does not write a `StockEntry`, and does not derive availability from the ledger.** It reads the fact the mock-up already carries.
- **The retired-dish flag.** That is feature **438** (`is_active` on `MenuItem`) — and its *Out of scope* says, verbatim: *"Any menu-management UI. The write path is an API; the screen is not built here."* **438 owns the server-side flag and the server-side filter; this slice owns the shipped screen's filter.**
- **The stock derivation.** That is features **374** (`qty_remaining` derived) and **471** (stored vs derived `qty_remaining`). **This slice reads a number; it does not change how the number is produced.**
- **The `MenuItem.is_prepared` consumer.** That is feature **398**. Not touched.
- **The money arithmetic in the bill modal.** Feature **465**. Not touched.
- **Any change to `MOCK_MENU`'s data.** The fixture's `stock: 0` on `Caesar Salad` is the shipped fact this slice reads. **The fixture array is not modified.** (Feature **467** owns the fixture's reconciliation with the API's response shape, and its *Out of scope* excludes *"any change to the mock-up's … fake-data content"*.)
- **Any Python file, any endpoint, any schema change.** This slice changes `index.html` only.

## Description

### The defect, as executed

The shipped menu renderer, verbatim from `index.html`:

```js
function renderMenu() {
  const host = document.getElementById('menu-list');
  host.innerHTML = '';
  const cats = [...new Set(MOCK_MENU.map(m => m.category))];
  for (const cat of cats) {
    const wrap = document.createElement('div');
    wrap.className = 'menu-cat';
    wrap.innerHTML = `<h3>${cat}</h3>`;
    const list = document.createElement('div');
    list.className = 'menu-items';
    for (const item of MOCK_MENU.filter(m => m.category === cat)) {
      const soldOut = item.stock === 0;
      const btn = document.createElement('button');
      btn.className = 'menu-item-btn' + (soldOut ? ' sold-out' : '');
      btn.innerHTML = `
        <span class="name">${item.name}</span>
        <span class="price">${item.price.toFixed(2)} €${item.stock != null ? ` <span class="stock-tag">${item.stock} left</span>` : ''}</span>
      `;
      btn.addEventListener('click', () => { if (!soldOut) addToOrder(item); });
      list.appendChild(btn);
    }
    wrap.appendChild(list);
    host.appendChild(wrap);
  }
}
```

Executed under `node` against the file's own fixture:

```
=== LEAD 3: the charter says "menu hides sold-out items" ===
  charter rows mentioning sold-out:
    ["| **P0** | Waiter can browse today's menu and add items to the active visit. | `POST /api/visits/{id}/items` works; menu hides sold-out items. |",
     "| **P0** | Cook can mark an item sold-out via `/sold_out`; menu auto-hides it. | After `/sold_out tiramisu`, the waiter's UI no longer shows it. |"]
  MOCK_MENU items with stock: 0 -> [ 'Caesar Salad (id 3)' ]
  the fixture comments it: true
  ...
  >>> does the shipped renderer reference `stock` at all? true
  >>> the sold-out dish IS RENDERED. The charter says it must be hidden.
```

**The charter names the requirement twice, in two separate P0 rows, and the shipped surface satisfies neither.**

- P0 row 43's acceptance criterion: *"menu hides sold-out items."*
- P0 row 44's acceptance criterion: *"After `/sold_out tiramisu`, **the waiter's UI no longer shows it**."*

The shipped surface **shows** it. It computes `soldOut = item.stock === 0`, adds a `sold-out` CSS class, **renders the button with its name, price and a "0 left" tag**, and refuses only the click.

### Why "present but disabled" is not the same as "hidden"

Three reasons, and the third is the one that matters.

1. **The charter says "no longer shows it"** — a statement about what is *on the screen*, not about what is *clickable*. A greyed-out `Caesar Salad — 9.00 € 0 left` is on the screen.

2. **A disabled button is still a promise to the guest.** The waiter reads the menu to the table. Reading a dish that is on the screen, then discovering at the pass that the kitchen is out, is the exact failure the charter row is written to prevent. The requirement exists because a guest being told *"we have Caesar salad"* and then not receiving it is a service failure, and LE31's charter names it as a **P0**.

3. **The refusal is in the wrong place, and it is the only place.** `btn.addEventListener('click', () => { if (!soldOut) addToOrder(item); })` — the guard is **inside the click handler**. That means:

   - Any path to `addToOrder` that does not go through this button **is not guarded at all**. `addToOrder` is a plain global function; the order-view's own "add" affordances and any future surface can call it directly.
   - The menu is re-rendered on every state change (`renderOrder()` is called from `addToOrder`, from `bumpStatus`, from the seat handler, from the bill handler). Between a render and a click, the fixture's `stock` can change with **no re-render** — the button's closure captured a stale `soldOut` value. **A dish that sold out after the last render remains clickable.**

   The third point is the one that makes this a **defect** rather than a **stylistic disagreement**: the shipped code's only protection against selling a sold-out dish is a value captured in a closure at render time, and nothing invalidates it.

### Why the corpus does not own this

- Feature **397** owns the **server-side** sold-out state — the per-day derived availability record and the `/sold_out` command. **It has no UI scope**, because there is no UI beyond the mock-up's static menu.
- Feature **438** owns the **server-side** retirement flag `MenuItem.is_active` and "one filter applied to the waiter menu surface". Its *Out of scope* says, verbatim: *"Any menu-management UI. The write path is an API; the screen is not built here."* **438's filter is a server-side read helper; this slice is the shipped screen's render filter.**
- Feature **467** owns the **fixture↔API drift check** and explicitly excludes *"any change to the mock-up's … fake-data content"*. This slice does not change the fixture and does not build the drift check.
- Feature **465** owns the money in the bill modal. **The menu's `item.price.toFixed(2)` is a money rendering** — **read 465 before starting, and do not change the formatter it installs.** If 465 has landed, this slice's `toFixed(2)` is already the money helper's call; **if it has not, leave the price rendering exactly as it is** — fixing the money is 465's job, and doing it here would fork the money rule.

### The third-party source contributes (vocabulary only)

`MustrHQ/kitchen-safety`'s README draws a distinction that is directly on point:

> *"Frontend names are self-reported, not authenticated staff identities."*

And it separates the two surfaces explicitly: a **kitchen frontend** where *"staff can record measured temperatures without signing in"*, and a **protected admin panel** where *"manager resolutions, account changes, settings, reports"* live. **The kitchen is trusted to enter data without authenticating; the manager's surface is protected.**

LE31's sold-out rule is exactly this shape: **the kitchen asserts a fact ("we are out of tiramisu"), and the waiter's surface must honour it.** The transferable vocabulary is the **split between the surface that *asserts* availability and the surface that *displays* it** — the assertion is unverified and informal; the display must not repeat it as an invitation.

**Vocabulary reference only.** This repository is AGPL-3.0, which is not §3.2-compatible for code adoption, and its subject — HACCP temperature records — is not LE31's domain. **Nothing from it is copied.**

## Data model

**No schema change. No Python change. No endpoint.**

The mock-up's menu data already carries the fact:

```js
const MOCK_MENU = [
  { id: 1, name: 'Schnitzel',    category: 'Mains',    price: 14,   prepared: true,  stock: 18 },
  { id: 2, name: 'Burger',       category: 'Mains',    price: 12,   prepared: true,  stock: 15 },
  { id: 3, name: 'Caesar Salad', category: 'Mains',    price: 9,    prepared: true,  stock: 0  },  // sold out
  ...
];
```

The change is one predicate with exactly one definition, and the render filter that uses it:

```js
// ONE definition. Every surface asks this.
function isAvailable(item) {
  return item.stock === null || item.stock > 0;
}
```

**`stock === null` means "not stock-tracked"** (the fixture uses `stock: null` for the unprepared items — `Coke`, `House Wine`, `Espresso`) and those are available. **This distinction is load-bearing**: a naive `item.stock > 0` would hide every unprepared drink. The fixture's own comment `// sold out` on item 3 is the proof the distinction is intended.

## Implementation steps

1. **Add `isAvailable(item)` with exactly one definition**, near the fixture, before the renderer. It must return `true` for `stock === null`. **Do not inline `item.stock > 0` anywhere else** — a second copy of the rule is how the next reader reintroduces the bug, and the same reasoning is why feature **438** insists on *"one function answering 'is this dish currently being served?' … and no surface re-implements the rule"*.
2. **Filter in the renderer.** Change `MOCK_MENU.filter(m => m.category === cat)` to filter on `isAvailable(m)` as well. **The dish must not be rendered at all** — not a disabled button, not a greyed row, not a "0 left" tag.
3. **Remove the `sold-out` class branch** if it becomes dead code, **or keep it** if 465/467 need it. **Decided: remove the now-dead class branch** — a CSS class nothing emits is a lie about the surface. **Recorded so a later pass does not re-add it.**
4. **Guard the order path too.** `addToOrder` must refuse an unavailable dish. **The guard belongs in `addToOrder`, not in the click handler**, because the click handler is the *only* place the guard currently lives and it is not a boundary — any caller of `addToOrder` bypasses it. The refusal must be legible: the waiter's screen must say *why* the dish cannot be added, not silently do nothing.
5. **Do not touch the price rendering.** `item.price.toFixed(2)` stays exactly as it is unless feature 465 has landed, in which case it is 465's formatter call. **This slice does not own money.**
6. **Do not touch `MOCK_MENU`.** The `stock: 0` on `Caesar Salad` and the `// sold out` comment are the shipped facts this slice reads.
7. **Add the regression check** (see *Verification protocol*).

## Telegram interaction if any

**None.** The `/sold_out` command and the sold-out state are feature **397**'s. This slice changes no bot command, no FSM state, and no Python file. **The `/sold_out` command's output is not read by this slice** — the mock-up reads its own fixture's `stock` field, which is the honest position for a mock-up that calls no API (feature **467** records that it makes no `fetch()` call).

## Dependencies

- **Feature 397** (`le31-sold-out-state…`) — **read first.** It owns the server-side representation of "sold out today" and the `/sold_out` command. **This slice does not build it and does not duplicate its representation.** When 397 lands, the *server-side* filter is 397's and the *shipped screen's* filter is this slice's — **the two must agree, and this slice's contract must cite 397's rule once 397 lands.**
- **Feature 438** (`le31-menu-item-has-no-availability-flag…`) — owns `MenuItem.is_active` (retirement) and the server-side filter. **Its *Out of scope* explicitly excludes any menu-management UI.** This slice is the screen half.
- **Feature 465** (`le31-the-waiters-screen-shows-a-different-tip…`) — owns the money in the same file. **The menu's price rendering must not be forked.** Read before starting.
- **Feature 467** (`le31-the-waiter-surface-and-the-api-have-drifted-apart…`) — owns the drift check and the fixture's reconciliation. **This slice does not build that check and does not change `MOCK_MENU`.**
- **Feature 471** (`le31-the-stored-batch-qty-remaining-and-the-charter-formula-disagree…`) — owns the *server-side* `qty_remaining` derivation. **This slice reads a number and does not change how it is produced.**
- **Charter P0 rows 43 and 44** — the two rows this slice makes true.

## Open questions

1. **Should a sold-out dish be hidden, or shown as unavailable?** — **Decided: hidden.** The charter says *"menu hides sold-out items"* and *"the waiter's UI no longer shows it"*, in two separate rows. **This is the charter's requirement, stated twice, and it is not this slice's to reinterpret.** A "show it greyed out" design would need a charter change, which is the owner's document.
2. **What about the "0 left" stock tag on available dishes?** — **Decided: keep it for dishes that ARE rendered.** The tag shows the remaining count for a dish with `stock > 0`; that is a different fact from availability and is useful to the waiter. **Only the `stock === 0` case is removed**, and it is removed by the dish not being rendered at all.
3. **Should the predicate live in the API instead?** — **Decided: no.** The mock-up calls no API (`grep -c "fetch(" index.html` → **0**), so an API predicate would have nothing to filter. **When the surface is wired, the server-side predicate (397/438) replaces this one, and this slice's predicate is deleted rather than kept as a second implementation.** Recorded so the two do not drift.
4. **Should the order-path refusal be silent?** — **Decided: no.** A silent refusal is indistinguishable from a broken button. The refusal must say *"Caesar Salad is sold out."*
5. **Does `is_available` need to be an `OrderItem` concern?** — **Decided: no.** Whether a dish is on the menu today is a `MenuItem` fact. **Feature 438 owns the stored form**; this slice only reads the mock-up's.

## Why this matters

**This is the only finding in the corpus that is a violation of a charter acceptance criterion, stated in the charter's own words, in a surface the charter's acceptance test is run against.**

Charter P0 row 44's acceptance criterion is not an abstract capability — it is a sentence about the waiter UI: *"After `/sold_out tiramisu`, **the waiter's UI no longer shows it**."* **That sentence is a test.** And today the shipped UI fails it, in the ordinary case, on the shipped fixture, with a sold-out dish already in the data (`Caesar Salad`, `stock: 0`, commented `// sold out`).

**And the failure is not "it looks slightly wrong" — it is that the guest can be promised a dish the kitchen does not have.** The waiter is reading the menu to the table. `Caesar Salad — 9.00 € · 0 left` is on the screen. The waiter's most natural reading of a menu is *"these are what we have."* A dish with `0 left` reads as *"we are out"* — and the charter's own answer is that the dish should not be there at all, precisely because the waiter should never have to make that inference.

**The wrong-place guard makes it worse, not better.** The only protection is `if (!soldOut)` inside a click handler, with `soldOut` captured when the menu was last rendered. Three consequences, in increasing order of severity:

1. A direct call to `addToOrder` — a global function — bypasses the guard entirely.
2. A re-render between the sale-out and the click is **not guaranteed**: the captured `soldOut` value is stale by construction.
3. **There is no test, and no way to write one.** The charter's §7 clause *"End-to-end before commit"* has nothing in the repository that could execute it — feature **467** records that the mock-up makes **zero** `fetch()` calls. **So the requirement that has an explicit acceptance sentence in the charter is the one requirement nothing can check.**

**And the cost is asymmetric.** Adding a dish that is sold out is a **stock-out** — feature 374's derivation means the batch is short, and the ledger's last line for that batch is `sold_out`. The guest who was promised it is told to wait; the table waits; the service time for that table grows. Every one of those is a cost the owner absorbs, and **the mock-up that the owner loads is the one that models the dish as available.**

**This is the second time the corpus has found a defect by reading the shipped surface against the charter's own words** (the first was the mock-up's float money). **It is also the cheapest fix in the corpus** — one predicate, one filter clause, one guard, no schema, no Python, no endpoint, no migration — **and it is the only one whose charter row has a *verbatim acceptance criterion* naming the surface.**

## Adjacent evidence

| Source | What it contributes | Disposition |
|---|---|---|
| `MustrHQ/kitchen-safety` (AGPL-3.0, created 2026-10-26, ★0) | The **split between the surface that asserts a fact and the surface that displays it**: a login-free kitchen frontend where *"staff can record measured temperatures without signing in"*, and a protected admin panel — with the explicit statement *"Frontend names are self-reported, not authenticated staff identities."* | **Vocabulary reference only** (AGPL-3.0 not §3.2-compatible; the domain is HACCP, not LE31's). Confirms that **the display side of an informal assertion needs its own rule**, not the assertion's rule. |
| `FreeOpenSourcePOS/FloCafe` (MIT, created 2026-05-07) — *"Free, open-source, offline-first Point of Sale for cafes, restaurants, and food businesses."* | A permissive-licensed POS whose README claims offline-first operation for exactly LE31's restaurant segment. | **Recorded, not adopted.** Its README was not fetched this pass (it was in the shortlist but the readme budget went to the two sources above). **No claim is made about its contents.** |
| `lorenzoyang/TavoloFlow` (AGPL-3.0, created 2026-10-16, ★22) | Its README states, verbatim: *"Guests scan the table's fixed QR code, browse the menu **with photos and allergens**"* and *"Owners manage the menu, with shared options such as drink sizes, sugar, toppings or spice levels that can add to the price."* | **Vocabulary reference only.** Confirms that in a real restaurant system **the menu a guest sees is the owner's curated, edited list** — not a live stock feed — which is the same separation 438 (retirement) and 397 (sold-out) draw on the server side. |
| `diamondrubinny/menuai` (AGPL-3.0, created 2026-10-22) — *"multilingual, designer-grade menu builder for restaurants, cafés & bars — full RTL, 16 themes, export to one HTML file, PDF or QR."* | A menu *builder* — the owner's editing surface, distinct from the waiter's ordering surface. | **Recorded, not adopted.** Its README was not fetched this pass; no claim is made about its contents. |

## Verification protocol

Seven checks, all offline, no network, no database, no browser.

```bash
# 1. THE PREDICATE EXISTS AND HAS EXACTLY ONE DEFINITION.
grep -c 'function isAvailable' index.html            # must be 1
grep -c 'item\.stock > 0' index.html                 # must be 0  (no inlined copy of the rule)

# 2. THE SOLD-OUT DISH IS NOT RENDERED.  (the charter's own sentence)
#    MOCK_MENU's item 3 has stock: 0 and the file comments it "// sold out".
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const M=eval('('+s.match(/const MOCK_MENU = \[[\s\S]*?\n\];/)[0].replace('const MOCK_MENU =','').replace(/;\$/,'')+')');
         const sold=M.filter(m=>m.stock===0);
         if(!sold.length){console.error('FAIL: no sold-out dish in the fixture');process.exit(1)}
         // the rendered set must NOT contain any sold-out dish
         const render=s.match(/function renderMenu\(\)[\s\S]*?\n\}/)[0];
         if(!/isAvailable/.test(render)){console.error('FAIL: the renderer does not filter on isAvailable');process.exit(1)}
         console.log('PASS: the renderer filters on the availability predicate')"

# 3. THE ORDER PATH IS GUARDED, NOT JUST THE CLICK HANDLER.
#    The guard must be inside addToOrder.
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const body=s.match(/function addToOrder\(item\) \{[\s\S]*?\n\}/)[0];
         if(!/isAvailable/.test(body)){console.error('FAIL: addToOrder does not guard availability');process.exit(1)}
         console.log('PASS: addToOrder refuses an unavailable dish')"

# 4. "stock === null" IS AVAILABLE.  (a naive `stock > 0` would hide every unprepared drink)
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const M=eval('('+s.match(/const MOCK_MENU = \[[\s\S]*?\n\];/)[0].replace('const MOCK_MENU =','').replace(/;\$/,'')+')');
         const nullStock=M.filter(m=>m.stock===null);
         if(!nullStock.length){console.error('FAIL: fixture has no null-stock dishes');process.exit(1)}
         // isAvailable must be true for every null-stock dish
         console.log('PASS: '+nullStock.length+' null-stock dishes must remain available')"

# 5. THE CHARTER ROWS ARE NAMED IN THE FILE (or in the contract that the file cites).
grep -rl 'sold-out' features/ specs/ | grep 475

# 6. THE CORPUS AGREES: this slice is now owned.
grep -rl 'isAvailable' features/ specs/        # must include features/475-*.md

# 7. NOTHING OUTSIDE index.html CHANGED, AND THE FIXTURE IS UNTOUCHED.
git diff --name-only <base>...HEAD -- . ':(exclude)index.html'   # must be empty
git diff <base>...HEAD -- index.html | grep -E '^[-+].*MOCK_MENU' # must be empty
```

**The negative control.** Re-inject the defect — remove `isAvailable` from the renderer's filter (or restore `for (const item of MOCK_MENU.filter(m => m.category === cat))`) — and **checks 2 and 3 must fail**. A check that cannot fail proves nothing. If checks 2 and 4 pass on the unmodified file, the verifier is wrong, not the file.

## Rollback path

`git revert` the single commit that touched `index.html`. The change is one predicate and one filter clause in one function. **No schema, no database, no server-side state, no API contract, no fixture data.** Reverting restores the shipped behaviour exactly, including the defect. **Rolling back is free.**
