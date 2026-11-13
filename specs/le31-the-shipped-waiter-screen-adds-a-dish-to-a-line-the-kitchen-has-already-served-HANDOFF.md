# HANDOFF — Feature 476: the shipped waiter screen adds a dish to a line the kitchen has already served

> **Slice contract for the coding agent.** Feature: `features/476-le31-the-shipped-waiter-screen-adds-a-dish-to-a-line-the-kitchen-has-already-served-first-party-the-quantity-changes-and-nobody-is-told-v1-order-line-quantity-phase.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (executed under `node` on 2026-11-13).
> Filed by: Daily Brainstorm 2026-11-13 (daily pass), Pick C.

---

## 1. The active feature path

```
features/476-le31-the-shipped-waiter-screen-adds-a-dish-to-a-line-the-kitchen-has-already-served-first-party-the-quantity-changes-and-nobody-is-told-v1-order-line-quantity-phase.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 452 / 456 / 379 / 474 / 465, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | The shipped `index.html` executed under `node` on 2026-11-13: `addToOrder`, extracted verbatim, was run against a line with `qty: 1, status: 'served'` — **the qty became 2 and the status stayed `served`**. A `preparing` line went `2 → 3`. Re-ordering a dish whose line was already served **landed on the served line** (the file's `find` returns the first match). |
| 2 | The defect is in LE31's own code | **PASS** | `function addToOrder(item) { const existing = state.visit.items.find(x => x.menu_item_id === item.id); if (existing) existing.qty += 1; ... }` — **no check on the existing line's `status`.** The shipped fire handler is `state.visit.items.filter(x => x.status === 'new').forEach(x => x.status = 'preparing')` — so a line already fired is **never re-fired**, and the kitchen is never told. The shipped bill modal sums the order lines, so **the bill is charged for a dish the kitchen never received.** |
| 3 | No filed feature owns it | **PASS** | **456** owns the **server-side** `CHECK` on `order_item.qty`'s sign and size — a different rule (the *value*, not *when it may change*), in a table no route writes. **452** owns the **server-side** status↔timestamp coherence rule and its write helper — the shipped screen has no write path, no timestamps and no persistence. **379** owns the transition log and the actor column — the shipped defect is a missing *gate*, not a missing actor. **430** owns `added_at`. **474** owns the per-table state. **Nobody owns the screen's phase rule.** |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **452** = server-side status ↔ timestamps. **456** = server-side qty sign/size. **379** = the transition log and its actor. **474** = the per-table state model. **476** = **when a quantity may change on the shipped screen**. **Different questions; the file regions are disjoint.** |
| 5 | The demand is real | **PARTIAL — recorded honestly** | No operator has reported a wrong quantity — **the mock-up makes zero `fetch()` calls**, so there is no live surface on which this could misfire. **But this is not an edge case: it is the first time a guest re-orders the dish they just finished.** "Two schnitzels, please", with one already served. **The third-party source names the failure exactly** — *"someone adds a dessert after the bill was paid"*. |
| 6 | It is cheap now and expensive later | **PASS** | One predicate, one changed `find` condition, one hidden control, in one file. **No schema change, no Python change, no endpoint, no migration.** Expensive later: the disagreement between "what was served" and "what the order says" **cannot be reconstructed** — there is no transition log (379, unbuilt), no insertion time (430, unbuilt), and the shipped screen keeps no record at all. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — it fires on 452 and 456** | **452** is about to land the server-side write helper that sets a status and its timestamp together. **It would faithfully leave the screen's edit gate absent**, and the two rules would then disagree. **452 must cite 476, or 476 lands first, or in the same PR.** **456** owns the qty constraint and must not be duplicated here. |

**Overall: `build`.** The weakest link is check 5, weak for the same mechanical reason as the other two picks of this pass: **the surface that would produce the complaint does not exist yet.** That is also the reason it is cheap.

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `index.html` | **One predicate, the `addToOrder` lookup, and the order-row's controls** | **One file. No build step** (§4.1: *"vanilla HTML + JS. No build step"*). **The money rendering is feature 465's — do not touch it.** |
| `features/452-…-an-order-line-can-be-served-and-still-say-it-is-new-…md` | **One line** — name 476 as the screen-side sibling | 452 is the server-side rule; 476 is the screen's. **Each must cite the other.** |
| `features/456-…-order-item-qty-may-be-zero-or-negative-…md` | **One line** — record that 476 adds no server-side constraint | 456 owns the sign/size rule; **456's own contract makes the point that a negative *ledger* delta is legitimate.** |

**Do NOT touch:** `backend/app/models.py` (**456** owns the qty constraint, **452** the status/timestamp rule, **379** the transition log, **430** the insertion time), `backend/app/routers/tables.py`, `backend/app/bot/cook_bot.py` (**403** owns the allowlist), the `btn-fire` handler, `bumpStatus`, `MOCK_MENU`, the bill modal's money (**465**), any `Decimal` declaration.

## 4. The implementation, in order

1. **Add `isQuantityEditable(line)` with exactly one definition.** It returns `line.status === 'new'`. **Do not inline `x.status === 'new'` in a second place** — the fire handler already holds that literal, and a third copy is how the two diverge.
2. **Hide or disable the quantity and remove controls on a line that is not `new`.** The shipped order row renders a `Remove` button on **every** line, including a `served` one. **A line the kitchen has finished must not be removable from the screen either** — same class of defect, same predicate, **decided and recorded so it is not lost.**
3. **Change `addToOrder` to respect the phase.** The lookup must find a line that is **still editable**:

   ```js
   const existing = state.visit.items.find(x => x.menu_item_id === item.id && isQuantityEditable(x));
   ```

   If a fired line exists with that dish, the `else` branch runs and a **new `status: 'new'` line** is pushed. **Two lines with the same `menu_item_id` is the correct outcome, not a bug.**
4. **Do not change the fire handler.** `filter(x => x.status === 'new')` already does the right thing — with step 3 in place, a re-ordered dish is a `new` line and **is** fired correctly. **This is why step 3 is the whole fix.**
5. **Do not touch `bumpStatus`.** The ladder is correct; making the server's ladder agree with it is feature **452**'s job.
6. **Do not touch the price rendering** (465).
7. **Add the regression check** (see §6). **Write it first — it must fail on today's file.**

## 5. The four things that will go wrong if nobody tells you

1. **Refusing the second order instead of adding a line.** Refusing makes the guest's second Schnitzel unorderable — a service failure of its own, and it puts the waiter in the position of lying to the guest. **A new line is correct, and it is the only outcome the shipped fire handler already knows how to deliver.**
2. **Changing the `find` to search from the end, or to prefer the *latest* line.** That would still land the increment on whichever line happens to be found. **The predicate must gate the match, not reorder the search.**
3. **Adding a server-side rule to fix a screen-side defect.** This slice changes **no Python file**. The natural mistake is to "also fix" `addToOrder`'s server-side counterpart — **there isn't one; the order-taking route does not exist (feature 02 owns it).** Adding a constraint to `order_item.qty` here would duplicate **456** and would risk the ledger's legitimate negative deltas.
4. **Editing `index.html` without knowing 465, 474, 475, 466 and 467 are in it.** **Several features of this corpus and feature 24 all touch this file.** The regions are disjoint — **the order row's controls and `addToOrder`** (this), **the state object and the floor/seat handlers** (474), **the menu renderer** (475), **the bill modal's arithmetic** (465), **the seat modal's inputs** (466), **the fixture's statuses** (467), **the floor grid** (24) — **but a rebase is required.** Say which landed first in your report.

## 6. Verification protocol

Offline, no network, no database, no browser.

```bash
cd /opt/data/le31_mmm3_research_work

# 1. THE PREDICATE EXISTS AND HAS EXACTLY ONE DEFINITION.
grep -c 'function isQuantityEditable' index.html      # must be 1
grep -c "x\.status === 'new'" index.html               # must be 1 -- the fire handler's own copy
                                                      #            is the only other allowed one

# 2. A SERVED LINE'S QUANTITY DOES NOT CHANGE.  (the exact scenario that fails today)
node /opt/data/le31-brainstorm-2026-11-13-scripts/prove_order_view.js
#    expected: "after : qty=1 status=served"
#    today's file prints "after : qty=2 status=served" -- the check must fail on it

# 3. THE SECOND ORDER OF A DISH BECOMES A SEPARATE LINE.
node -e "const s=require('fs').readFileSync('index.html','utf8');
         const body=s.match(/function addToOrder\(item\) \{[\s\S]*?\n\}/)[0];
         if(!/isQuantityEditable/.test(body)){
           console.error('FAIL: addToOrder does not respect the phase');process.exit(1)}
         console.log('PASS: addToOrder finds only an editable line')"
#    and: after adding, the fixture must hold TWO lines with that menu_item_id --
#    one 'served' qty=1 and one 'new' qty=1.

# 4. THE FIRE HANDLER STILL PICKS UP THE NEW LINE.
grep -c "filter(x => x.status === 'new')" index.html    # must be 1 -- the fire path is unchanged

# 5. THE CORPUS AGREES: this slice is now owned.
grep -rl 'isQuantityEditable' features/ specs/          # must include features/476-*.md

# 6. THE SERVER-SIDE RULES ARE CITED, NOT DUPLICATED.
grep -c '452' features/476-*.md                         # must be >= 1
grep -c '456' features/476-*.md                         # must be >= 1

# 7. NOTHING OUTSIDE index.html CHANGED.
git diff --name-only <base>...HEAD -- . ':(exclude)index.html'   # must be empty
```

**Two negative controls are required for this slice.**

1. **Re-inject the defect** — restore `const existing = state.visit.items.find(x => x.menu_item_id === item.id);` — and **checks 2 and 3 must fail**.
2. **Check 2 must fail on today's file**, because today's file is exactly the defect. **If check 2 passes before the fix, the check is vacuous** — and a vacuous check is worse than no check, because it reports green on a defect.

## 7. Rollback path

`git revert` the single commit that touched `index.html`. The change is one predicate, one changed `find` condition, and one hidden control.

**No schema, no database, no server-side state, no API contract, no fixture data.** Reverting restores the shipped behaviour exactly, including the defect. **Rolling back is free.**

## 8. The mandatory LE31 skill list

Read these before writing code. They are in the repo under `skills/`:

- **`skills/le31-conventions/`** — the naming, money and data-model conventions. **The `Decimal` rule is here — and this slice must not fork it.**
- **`skills/le31-frontend/`** — the frontend's conventions. **This is the relevant one.** `index.html` is vanilla HTML + JS with no build step (§4.1).
- **`skills/le31-backend/`** — the backend's structure. **Read it even though this slice touches no Python**, so you know what you are *not* changing — and so you do not "also fix" the server side.
- **`skills/le31-handoff-spec/`** — the slice-contract shape this file follows.
- **`skills/le31-coding-agent-brief/`** — how the paste-in prompt is produced from this contract. **Do not paste chat excerpts; use the skill.**
- **`skills/le31-v1-feature-pattern/`** — the v1 feature's shape.
- **`skills/le31-research/`** and **`skills/le31-data/`** — the research corpus and the data conventions, for the domain vocabulary.

**Also read, in the repo, before you start:**

- **`features/452-…-an-order-line-can-be-served-and-still-say-it-is-new-…md`** — the server-side rule this slice mirrors.
- **`features/456-…-order-item-qty-may-be-zero-or-negative-…md`** — the server-side qty rule this slice must not duplicate.
- **`features/379-…-order-item-transition-attribution-…md`** — the transition log and actor.
- **`features/474-…`** — the per-table state this slice assumes.

## 9. The one thing that matters

**This is not an edge case. It is the first time a guest re-orders the dish they just finished.**

"Schnitzel, please" — twice, with one already served. In that moment the shipped screen increments the **served** line's quantity, **never tells the kitchen** (the fire handler only fires `new` lines), and **charges the guest for a dish that was never ordered and never received** — because the bill modal sums the order lines.

**The third-party source names the failure in one sentence:** *"someone adds a dessert after the bill was paid."*

**Ship the contract with the strongest evidence available and let the audit strengthen it.** Here the evidence is already execution-proven under `node`, against the file's own handler body. **Ship it.**
