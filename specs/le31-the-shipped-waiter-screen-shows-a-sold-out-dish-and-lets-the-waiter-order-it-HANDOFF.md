# HANDOFF — Feature 475: the shipped waiter screen shows a sold-out dish and lets the waiter order it

> **Slice contract for the coding agent.** Feature: `features/475-le31-the-shipped-waiter-screen-shows-a-sold-out-dish-and-lets-the-waiter-order-it-first-party-the-charter-says-the-menu-auto-hides-it-v1-menu-availability-filter.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (executed under `node` on 2026-11-13).
> Filed by: Daily Brainstorm 2026-11-13 (daily pass), Pick B.

---

## 1. The active feature path

```
features/475-le31-the-shipped-waiter-screen-shows-a-sold-out-dish-and-lets-the-waiter-order-it-first-party-the-charter-says-the-menu-auto-hides-it-v1-menu-availability-filter.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 397 / 438 / 465 / 467 / 471, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | The shipped `index.html` executed under `node` on 2026-11-13: the menu renderer, extracted verbatim, computes `const soldOut = item.stock === 0`, adds a `sold-out` class, **renders the button with its name, price and a "0 left" tag**, and refuses only the click. `MOCK_MENU` item id 3 (`Caesar Salad`) has `stock: 0` and the file's own comment reads `// sold out`. **The dish is rendered.** |
| 2 | The defect is in LE31's own code | **PASS** | `PROJECT_CHARTER.md`, verbatim, **two P0 rows**: row 43 — *"menu hides sold-out items"*; row 44 — *"Cook can mark an item sold-out via `/sold_out`; menu auto-hides it"*, acceptance criterion *"After `/sold_out tiramisu`, **the waiter's UI no longer shows it**."* The shipped surface **shows** it. **This is the only finding in the corpus that violates a charter acceptance criterion stated in the charter's own words, in the surface the charter's acceptance test names.** |
| 3 | No filed feature owns it | **PASS** | Feature **397** owns the **server-side** sold-out state and the `/sold_out` command. Feature **438** owns `MenuItem.is_active` and the server-side filter, and its *Out of scope* says verbatim: *"Any menu-management UI. The write path is an API; **the screen is not built here**."* Feature **467** owns the fixture↔API drift check. **Nobody owns the shipped screen's render filter.** |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **397** = the server-side representation of sold-out. **438** = the server-side retirement flag (a *different* state: retired ≠ sold out, and 438's own test 2 proves they must not merge). **465** = money in the bill modal. **467** = the drift check. **475** = **the shipped screen's availability filter and its order-path guard.** |
| 5 | The demand is real | **PASS — the strongest of this pass's three** | The charter states the requirement **twice, in two separate P0 rows**, with a verbatim acceptance criterion naming the surface. The mock-up ships with a **sold-out dish already in its data** (`Caesar Salad`, `stock: 0`, commented `// sold out`), so the defect is present the moment the file is opened. **The mock-up makes zero `fetch()` calls** — so there is no live surface — but the charter's criterion is about the waiter's UI, and the waiter's UI is this file. |
| 6 | It is cheap now and expensive later | **PASS** | One predicate, one filter clause, one guard, in one file. **No schema change, no Python change, no endpoint, no migration, no fixture change.** Expensive later: a sold-out dish that stays on the menu is a **stock-out** — feature 374's derivation means the batch is short and the ledger's last line for it is `sold_out`. The guest is told to wait; the table waits; the service time grows. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — it fires on 397, 438 and 465** | **397** is about to land the server-side sold-out state and the `/sold_out` command — **it must cite 475, or 475 lands first**, or the server filter and the screen filter become two rules. **438** is about to land `is_active` and its server-side filter; **465** is about to rewrite the menu's price rendering (`item.price.toFixed(2)`) into its money helper — **475 must not fork that.** |

**Overall: `build`.**

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `index.html` | **One predicate, the render filter, and the order-path guard** | **One file. No build step** (§4.1: *"vanilla HTML + JS. No build step"*). **The price rendering is feature 465's — do not touch it.** |
| `features/397-…-sold-out-state-…md` | **One line** — name 475 as the screen-side counterpart | 397 owns the server half; 475 owns the screen half. |
| `features/438-…-menu-item-has-no-availability-flag-…md` | **One line** — record that the screen's filter is 475's, not 438's | 438's *Out of scope* already says the screen is not built there. |

**Do NOT touch:** `MOCK_MENU` (467 owns the fixture), `backend/app/models.py` (**438** owns `is_active`), `backend/app/bot/cook_bot.py` and the `/sold_out` command (**397**), the stock derivation (**374** / **471**), `MenuItem.is_prepared` (**398**), the bill modal's money (**465**), `backend/app/routers/tables.py`, any `Decimal` declaration.

## 4. The implementation, in order

1. **Add `isAvailable(item)` with exactly one definition.** It must return `true` for `item.stock === null` — the fixture uses `stock: null` for unprepared items (`Coke`, `House Wine`, `Espresso`), and **a naive `item.stock > 0` would hide every unprepared drink.** **Do not inline `item.stock > 0` anywhere else.**
2. **Filter in the renderer.** `MOCK_MENU.filter(m => m.category === cat)` must also filter on `isAvailable(m)`. **The dish must not be rendered at all** — no button, no price, no stock tag, no row.
3. **Remove the now-dead `sold-out` class branch** — a CSS class nothing emits is a lie about the surface. **Decided and recorded.**
4. **Guard the order path.** `addToOrder` must refuse an unavailable dish. **The guard belongs in `addToOrder`, not in the click handler** — the click handler is not a boundary: it is bypassed by any direct caller, and its captured `soldOut` value is stale by construction after a re-render.
5. **Make the refusal legible.** *"Caesar Salad is sold out."* — not silence. A silent refusal is indistinguishable from a broken button.
6. **Do not touch the price rendering.** `item.price.toFixed(2)` stays exactly as it is unless 465 has landed, in which case it is 465's formatter call. **Fixing the money here would fork 465's money rule.**
7. **Add the regression check** (see §6). **Write it first — it must fail on today's file.**

## 5. The four things that will go wrong if nobody tells you

1. **Hiding the dish but leaving the guard in the click handler.** The filter and the guard are **two different jobs**. The filter is what the waiter sees; the guard is what the kitchen is protected by. **A sold-out dish can reach `addToOrder` by any route that does not go through the button** — the function is a global.
2. **Writing `item.stock > 0` and hiding every unprepared drink.** The fixture's `stock: null` means *"not stock-tracked"*, not *"out of stock"*. **The naive predicate silently removes Coke, House Wine and Espresso from the menu** — a far worse defect than the one being fixed, and one the check in §6 item 4 exists to catch.
3. **Touching the money.** `item.price.toFixed(2)` is a money rendering and **feature 465 owns it**. Changing it here creates a second money rule in the same file — the exact thing 465 exists to prevent. **If 465 has landed, use its formatter; if not, leave the price exactly as it is.**
4. **Changing the fixture.** `Caesar Salad`'s `stock: 0` and its `// sold out` comment are **the shipped facts this slice reads**. Feature **467**'s *Out of scope* excludes *"any change to the mock-up's … fake-data content"*. **The fixture is the test input, not the thing under test.**

## 6. Verification protocol

Offline, no network, no database, no browser.

```bash
cd /opt/data/le31_mmm3_research_work

# 1. THE PREDICATE EXISTS AND HAS EXACTLY ONE DEFINITION.
grep -c 'function isAvailable' index.html            # must be 1
grep -c 'item\.stock > 0' index.html                 # must be 0  (no inlined copy of the rule)

# 2. THE SOLD-OUT DISH IS NOT RENDERED.  (the charter's own sentence)
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const M=eval('('+s.match(/const MOCK_MENU = \[[\s\S]*?\n\];/)[0].replace('const MOCK_MENU =','').replace(/;\$/,'')+')');
         const sold=M.filter(m=>m.stock===0);
         if(!sold.length){console.error('FAIL: no sold-out dish in the fixture');process.exit(1)}
         const render=s.match(/function renderMenu\(\)[\s\S]*?\n\}/)[0];
         if(!/isAvailable/.test(render)){console.error('FAIL: the renderer does not filter');process.exit(1)}
         console.log('PASS: the renderer filters on availability')"

# 3. THE ORDER PATH IS GUARDED, NOT JUST THE CLICK HANDLER.
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const body=s.match(/function addToOrder\(item\) \{[\s\S]*?\n\}/)[0];
         if(!/isAvailable/.test(body)){console.error('FAIL: addToOrder does not guard');process.exit(1)}
         console.log('PASS: addToOrder refuses an unavailable dish')"

# 4. "stock === null" IS AVAILABLE.  (a naive `stock > 0` would hide every unprepared drink)
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const M=eval('('+s.match(/const MOCK_MENU = \[[\s\S]*?\n\];/)[0].replace('const MOCK_MENU =','').replace(/;\$/,'')+')');
         const nullStock=M.filter(m=>m.stock===null);
         if(!nullStock.length){console.error('FAIL: fixture has no null-stock dishes');process.exit(1)}
         const body=s.match(/function isAvailable\(item\) \{[\s\S]*?\n\}/);
         if(!body){console.error('FAIL: no isAvailable');process.exit(1)}
         if(/stock\s*>\s*0/.test(body[0])){console.error('FAIL: isAvailable hides null-stock dishes');process.exit(1)}
         console.log('PASS: '+nullStock.length+' null-stock dishes remain available')"

# 5. THE CORPUS AGREES: this slice is now owned.
grep -rl 'isAvailable' features/ specs/          # must include features/475-*.md

# 6. THE ADJACENT FEATURES ARE CITED, NOT DUPLICATED.
grep -c '397' features/475-*.md                   # must be >= 1
grep -c '438' features/475-*.md                   # must be >= 1
grep -c '465' features/475-*.md                   # must be >= 1

# 7. NOTHING OUTSIDE index.html CHANGED, AND THE FIXTURE IS UNTOUCHED.
git diff --name-only <base>...HEAD -- . ':(exclude)index.html'   # must be empty
git diff <base>...HEAD -- index.html | grep -E '^[-+].*MOCK_MENU' # must be empty
```

**The negative control is mandatory.** Re-inject the defect — remove `isAvailable` from the renderer's filter, or restore `for (const item of MOCK_MENU.filter(m => m.category === cat))` — and **checks 2 and 3 must fail**. A check that cannot fail proves nothing. **Checks 2 and 4 must fail on today's file**, because today's file is exactly the defect.

## 7. Rollback path

`git revert` the single commit that touched `index.html`. The change is one predicate and one filter clause in one function.

**No schema, no database, no server-side state, no API contract, no fixture data.** Reverting restores the shipped behaviour exactly, including the defect. **Rolling back is free.**

## 8. The mandatory LE31 skill list

Read these before writing code. They are in the repo under `skills/`:

- **`skills/le31-conventions/`** — the naming, money and data-model conventions. **The `Decimal` rule is here — and this slice must not fork it.**
- **`skills/le31-frontend/`** — the frontend's conventions. **This is the relevant one.** `index.html` is vanilla HTML + JS with no build step (§4.1).
- **`skills/le31-backend/`** — the backend's structure. **Read it even though this slice touches no Python**, so you know what you are *not* changing.
- **`skills/le31-handoff-spec/`** — the slice-contract shape this file follows.
- **`skills/le31-coding-agent-brief/`** — how the paste-in prompt is produced from this contract. **Do not paste chat excerpts; use the skill.**
- **`skills/le31-v1-feature-pattern/`** — the v1 feature's shape.
- **`skills/le31-research/`** and **`skills/le31-data/`** — the research corpus and the data conventions, for the domain vocabulary.

**Also read, in the repo, before you start:**

- **`features/397-…-sold-out-state-…md`** — the server-side sold-out state this slice mirrors.
- **`features/438-…-menu-item-has-no-availability-flag-…md`** — the retirement flag; **note that 438's *Out of scope* explicitly excludes the screen.**
- **`features/465-…`** — the money in the same file.
- **`features/467-…`** — the drift check and the fixture's reconciliation.

## 9. The one thing that matters

**This is the only finding in the corpus that violates a charter acceptance criterion stated in the charter's own words — and the charter names the surface.**

*"After `/sold_out tiramisu`, the waiter's UI no longer shows it."*

Today the shipped UI **shows it**: the dish, its price, and a `0 left` tag. The only protection is a value captured in a click handler's closure at render time, which a re-render invalidates and which any direct caller of `addToOrder` bypasses.

**Ship the contract with the strongest evidence available and let the audit strengthen it.** Here the evidence is already execution-proven under `node`, and the charter row is quoted verbatim in the contract. **Ship it.**
