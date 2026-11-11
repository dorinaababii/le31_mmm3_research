# Feature 465 — The waiter's screen shows a different tip than the ledger stores: the shipped mock-up computes money in JavaScript floats

> **Pick A of Daily Brainstorm 2026-11-10 (100th daily-brainstorm pass).** **FIRST-PARTY — the defect is in LE31's own shipped waiter surface, and it is proved by EXECUTION** (the mock-up's real JavaScript, run under `node`), not by reading.
>
> `index.html` is the shipped waiter UI. `backend/app/main.py` mounts it at `/`:
>
> ```python
> _STATIC_DIR = _REPO_ROOT / "index.html"
> if _STATIC_DIR.exists():
>     app.mount("/", StaticFiles(directory=str(_STATIC_DIR.parent), html=True), name="ui")
> ```
>
> It is 30,530 bytes / 720 lines, and it contains **the P0 tip formula**, verbatim:
>
> ```js
> const subtotal = state.visit.items.reduce((s, x) => s + x.unit_price * x.qty, 0);
> const tax = subtotal * 0.10;
> const tip = paid - (subtotal + tax);
> ```
>
> Every one of those is **IEEE-754 double arithmetic**. `x.unit_price * x.qty` is a float multiplication.
>
> **`PROJECT_CHARTER.md` §7 (Quality bar), verbatim:**
>
> > - **Money sums use `Decimal` arithmetic.** No `float(qty * price)` anywhere.
>
> **The mock-up does exactly the thing the charter forbids, in the one surface a waiter looks at.**
>
> **Executed under `node` on 2026-11-10** (the mock-up's own arithmetic, verbatim, against LE31's own `Decimal` rule):
>
> | items | paid | node `tip` | node `toFixed(2)` | `Decimal` tip | differs? |
> |---|---|---|---|---|---|
> | `0.10 × 3` | `0.33` | `-0.00000000000000` | **`-0.00`** | `0.00` | **YES** |
> | `6.90 × 3` | `22.77` | `-0.00000000000000` | **`-0.00`** | `0.00` | **YES** |
> | `1.15 × 3` | `3.45` | `-0.34500000000000` | **`-0.34`** | `-0.35` | **YES** |
>
> **A waiter is shown `Tip (derived): -0.00 €` on a table where the ledger would store `0.00`, and `Underpaid by 0.34 €` on a table where the ledger would store `0.35`.**
>
> **And the divergence is not cosmetic — it changes the DECISION.** The mock-up branches on the float:
>
> ```js
> const tip = paid - (subtotal + tax);
> ... 'Tip (derived): ' + tip.toFixed(2) + ' €'
> ... : 'Underpaid by ' + (-tip).toFixed(2) + ' €';
> ```
>
> A tip of `-0.0000000000000000004` is **negative**, so the mock-up takes the *underpaid* branch and tells the waiter the guest has not paid enough — for a table where the guest paid **exactly** the bill. The waiter is told to chase a shortfall that does not exist.
>
> **Why the corpus does not own it.** A corpus-wide sweep over 959 feature contracts and HANDOFFs returns **zero** hits for `toFixed`. Feature **411** (`le31-money-precision-declared-not-enforced…`) owns the **server-side** money precision — it names the ten `Decimal` fields on `MenuItem`, `OrderItem`, `Bill`, `DerivedTip` and `Shift`, and it explicitly observes that *"the waiter surface is a static mockup with zero `fetch()` calls"*. **It fixes the ten server fields. It does not touch the browser's own arithmetic.** The browser is a *second implementation of the money rules*, and it is the one the operator actually reads.
>
> **Bucket: v1.** Verdict: **`build`**. Evidence class: **OBSERVED** (executed under `node`). Confidence: **high** for the defect (the arithmetic is verbatim and the divergence is measured); **medium** for the demand (no operator has reported it — but the mock-up is the **only** waiter surface that exists, so there is no other surface on which the bug could have been seen).

## Goal

Make **the number the waiter reads and the number the ledger stores the same number**.

The concrete outcome: **the money arithmetic in the waiter surface is done in integer minor units (cents), never in a JavaScript `Number`**, and **the tip the mock-up displays is the tip the `DerivedTip` row would hold for the same inputs.**

**The single sentence this feature exists to make true:** *money is computed once, in the server's decimal arithmetic, and the browser displays it — it does not recompute it.*

## Scope

**In scope (v1):**

- **A money helper in `index.html`** that represents every amount as an **integer number of minor units (cents)**, with one documented add/subtract/multiply and one documented formatter. No `Number` ever holds a money value.
- **Replace every money computation in `index.html`** — `subtotal`, `tax`, `total`, `tip`, and the `reduce(...)` over the order lines — with that helper.
- **A rounding rule that is stated once.** The tax is `subtotal × 0.10`; in cents that is a **division that must round**, and the rule must be the same one the server uses. LE31's server-side rounding rule is owned by feature **408** (`le31-tax-rate-has-no-home…`) — **this slice does not define a tax rule**, it only requires that the browser's rounding match the server's, and it must cite 408's rule once 408 lands.
- **Replace the `toFixed(2)` calls** on money with the formatter, and **eliminate the `-0.00` case** (a zero tip must render `0.00 €`, never `-0.00 €`).
- **A `SEVEN-CHECK`-style assertion set** — see *Verification protocol* — that fails on today's `index.html` and passes on the fixed one.

**Explicitly NOT in scope:**

- **The server-side money fields.** That is feature **411** (and **404**'s `CHECK`/`STRICT` family). **This slice changes no Python file.**
- **The tax rate and the rounding mode.** That is feature **408** / **410** — filed. **This slice does not move the tax rate into the browser**, it only requires the browser to round the way the server rounds.
- **The tip formula's *meaning*.** `total_paid − subtotal_items − subtotal_tax` is feature **05 / 415 / 420 / 457**. **This slice does not change what the tip is** — it makes the browser compute the *same* tip the server computes.
- **Wiring the mock-up to the API.** That is a different slice (see *Dependencies*).
- **The `float` in `config.py`, `db.py` or any other backend file.**
- **Any change to `features/08-index-mockup.md`'s *visual* design**, its colour tokens, its three views, or its fake-data content.

## Description

### The defect, as observed in LE31's own shipped file on 2026-11-10

`index.html` line ~600 (the bill modal), verbatim:

```js
const subtotal = state.visit.items.reduce((s, x) => s + x.unit_price * x.qty, 0);
const tax = subtotal * 0.10;
const tip = paid - (subtotal + tax);
```

and, at the display sites:

```js
document.getElementById('t-tax').textContent     = tax.toFixed(2) + ' €';
document.getElementById('t-total').textContent   = (subtotal + tax).toFixed(2) + ' €';
document.getElementById('bill-due').textContent  = (subtotal + tax).toFixed(2) + ' €';
const paid = +document.getElementById('inp-paid').value || 0;
```

`x.unit_price` comes from the fixture as a **JavaScript number literal**:

```js
{ menu_item_id: 1, name: 'Schnitzel', qty: 1, unit_price: 14, status: 'preparing' },
```

So every money value in the browser is a `Number`, every operation is a double operation, and `toFixed(2)` is a **display** rounding applied **after** the arithmetic has already drifted.

### The three measured divergences (executed under `node`, 2026-11-10)

| case | node `tip` | node `toFixed(2)` | `Decimal` tip | what the waiter sees | what the ledger stores |
|---|---|---|---|---|---|
| `0.10 × 3`, paid `0.33` | `-0.00000000000000` | `-0.00` | `0.00` | `Tip (derived): -0.00 €` | `0.00` |
| `6.90 × 3`, paid `22.77` | `-0.00000000000000` | `-0.00` | `0.00` | `Tip (derived): -0.00 €` | `0.00` |
| `1.15 × 3`, paid `3.45` | `-0.34500000000000` | `-0.34` | `-0.35` | `Underpaid by 0.34 €` | `-0.35` |

**The third row is the one that matters.** `1.15 × 3 = 3.4499999999999997` in binary floating point; `3.45 − 3.4499999999999997 − 0.34499999999999997 = −0.34500000000000064`; `toFixed(2)` on that is `-0.34`. In `Decimal`, `Decimal("1.15") * 3 = Decimal("3.45")` exactly, and `Decimal("3.45") − Decimal("3.45") − Decimal("0.35") = Decimal("-0.35")`. **The waiter is told the guest is 1 cent short on a table where the arithmetic is exact.**

### ⭐ And the branch the divergence takes

The mock-up does not merely *display* the drifted number — it **decides on it**:

```js
const tip = paid - (subtotal + tax);
... : `Underpaid by ${(-tip).toFixed(2)} €`;
```

A tip of `-0.0000000000000000004` is **negative**. The guest paid **exactly** the bill, and the waiter is told to chase a shortfall.

### ⭐ Why the browser has a second implementation of the money rules at all

`features/08-index-mockup.md` (the informal v1 spec for this file) says, verbatim:

> **Out of scope (v1):**
> - Real backend wiring.
> - Persistence (refresh = back to mock data).

and, under *How to view*:

> When the real backend exists, the same HTML can be served by FastAPI (static files at `/`).

**The intent is that this file becomes the real waiter surface.** `main.py` already mounts it at `/`. The money arithmetic in it is therefore **not throwaway** — it is the arithmetic the waiter will read on every table — and it was written under the assumption that a mock-up may be approximate.

**This feature is the transition from "a mock-up may be approximate" to "a money rule is a money rule."** It does not wire the API (that is a separate slice). It makes the file's arithmetic *correct on its own terms*, so that when the wiring happens there is nothing to un-learn.

### ⚠️ The honest boundary: this is a mock-up, and a mock-up has no ledger

**A mock-up has no `Bill` row and no `DerivedTip` row, so there is nothing in the database for the browser's number to disagree *with* — yet.** The divergence is between the browser's arithmetic and **the charter's rule that the browser's arithmetic is supposed to implement**, which is what makes it a defect today rather than a cosmetic difference.

The moment the surface is wired, the same arithmetic produces the **displayed** value while the server produces the **stored** value, and the two are on the same table. That is the failure this slice removes in advance.

**This is the same "free today, expensive later" shape the corpus has filed repeatedly** (features 455, 458, 462): there is no live surface on which the bug can currently be *observed by a user*, so there is no report to have been made — and the fix is cheap precisely because nothing is wired yet.

## Data model

**No schema change. No Python change. No new table, no new column, no new endpoint.**

The change is **inside `index.html`**:

```js
// Money is an integer number of minor units (cents). Never a Number.
const money = {
  parse: (str) => Math.round(Number(str) * 100),        // "3.45" -> 345
  of:    (cents) => cents,                               // identity, for clarity
  add:   (a, b) => a + b,                                // integer add — exact
  sub:   (a, b) => a - b,                                // integer sub — exact
  mul:   (cents, qty) => cents * qty,                   // integer mul — exact
  pct:   (cents, rate) => Math.round(cents * rate),     // rounding stated ONCE
  fmt:   (cents) => (cents / 100).toFixed(2).replace('-0.00', '0.00') + ' €',
};
```

**Two properties this buys, and they are the whole contract:**

1. **Integer minor units make `add`/`sub`/`mul` exact.** `345 + 345 + 345` is `1035`, not `1034.9999999999999`. The `1.15 × 3` case becomes exactly `345` cents.
2. **`fmt` normalises the negative zero.** `(0).toFixed(2)` is `"0.00"`, but `(-0).toFixed(2)` is `"-0.00"` — the `replace` handles the sign bit, and a `cents === 0 ? 0 : cents` guard handles it at the source.

**The tax rounding must cite feature 408's rule.** `money.pct` above uses `Math.round` (round-half-up) as a **placeholder**; the implementer must replace it with whatever 408 specifies, and must state which rule was used. **This slice does not decide the tax rule.**

## Implementation steps

1. **Add the `money` helper** near the top of `index.html`, with the two properties above documented in a short comment that names the charter §7 clause it implements.
2. **Convert every money literal in the fixture to cents.** The fixture's `unit_price: 14` becomes `unit_price_cents: 1400`; the `subtotal: 28.00` / `87.00` fixtures become `2800` / `8700`. **A `Number` must never hold a money value** — not even in the fixture, because the fixture is what the arithmetic operates on.
3. **Rewrite the three computation sites** (`subtotal`/`tax`/`total`, and the bill-modal `tip`) to use `money.add` / `money.mul` / `money.pct` / `money.sub`.
4. **Rewrite the display sites** to use `money.fmt`. **Delete every `toFixed(2)` on a money value** — the verification asserts zero remain.
5. **Fix the `paid` parse**: `money.parse(document.getElementById('inp-paid').value)` instead of `+value || 0`.
6. **Fix the negative-zero display** so a zero tip renders `0.00 €`.
7. **Add the assertion set** below to the repo's verification tooling (see *Verification protocol*), so the rule cannot rot.
8. **Record the rounding rule used** in a one-line comment next to `money.pct`, naming feature 408.

## Telegram interaction if any

**None.** This slice touches the waiter surface only. It does not change the cook bot, and it does not change any Telegram command.

## Dependencies

- **Feature 08** (`08-index-mockup.md`) — the informal spec for `index.html`. **This slice does not rewrite feature 08**; it **adds to it** the constraint the mock-up spec did not state (that money arithmetic in the surface must be decimal-exact). The implementer should add one line to feature 08's *Scope* recording this, so the two agree.
- **Feature 411** (`le31-money-precision-declared-not-enforced…`) — the **server-side** money precision. **This slice is its browser-side sibling, not its replacement.** 411 owns the ten `Decimal` fields; this slice owns the browser's arithmetic. **Neither blocks the other.** If 411 lands first, this slice must cite it; if this slice lands first, 411 must cite it.
- **Feature 408 / 410** — the tax rate and the rounding mode. **408 owns the rule; this slice must match it.** This slice does **not** define it.
- **Feature 05 / 415 / 420 / 457** — the tip formula's meaning and the server-side tip derivation. **This slice does not change what the tip is.**
- **Feature 24** (`visual-table-layout-v2`) — an `index.html` rewrite of the floor grid, with the scope line *"All changes live in `index.html` only; no backend changes, no new endpoints."* **⚠️ THIS IS A FILE-LEVEL COLLISION**: 24 will edit the same file. **The two must not be developed in parallel against the same file without a rebase**; this slice's money helper is a **separate region** of `index.html` from 24's floor grid, and the implementer must say which lands first.
- **Feature 388** — puts `index.html` explicitly **out of scope** (*"Any waiter-UI change beyond what the API response implies (the UI is `index.html`, feature 01's scope)"*). **This slice is the first contract to own `index.html`'s money rules**, and it does not contradict 388: 388's out-of-scope note says the UI is *"feature 01's scope"*, and **feature 01 is an informal spec, not a contract** — this slice supplies the missing contract for that surface.

## Open questions

1. **Should the browser compute the tip at all, or receive it?** The charter's intent (§4.1: the waiter UI is *"vanilla HTML + JS. No build step"*) and feature 08's intent (*"the same HTML can be served by FastAPI"*) both suggest the server will eventually own the computation. **The recorded default for this slice: the browser computes in cents** — because the mock-up has no server to compute it, and because a browser that cannot compute a total cannot preview a bill at all. **But the end state is that the server sends the total and the browser renders it**; this slice makes the browser's *interim* arithmetic exact so the transition is not a second drift.
2. **Cents, or a `BigInt` of cents?** Recorded default: **integer cents** (a `Number`). A `Number` holding an integer count of cents is exact up to 2^53 cents — about **90 trillion euros** — which is far beyond any restaurant. **The implementer must state this bound.**
3. **Rounding mode for tax.** Recorded default: **follow feature 408**. If 408 has not landed, the placeholder is `Math.round` (half-up) **and the implementer must mark it as provisional**.
4. **Does `money.pct` round the tax, or the total?** Recorded default: **round the tax** (a rate applied to a base produces a tax amount; rounding the total instead gives a different cent).
5. **What about the `subtotal: 28.00` fixture values that are not derived from any line?** They are display-only fixtures; they must still be stored in cents (`2800`).
6. **Should the negative-zero fix live in `fmt` or at the source?** Recorded default: **both** — `fmt` normalises the string, and the tip computation normalises `-0` to `0` before display. **A single place is not enough** because the *branch* on `tip < 0` also sees the negative zero, and the branch must not take the "underpaid" path for an exactly-paid table.

## Why this matters

**LE31's central promise is that the money it shows the owner is the money it stored.** The charter's §7 makes the arithmetic a **rule**, not a preference: *"No `float(qty * price)` anywhere."*

**And the one place a waiter looks — the only waiter surface that exists — violates it.** Not in the database, where feature 411's ten `Decimal` fields are at least *declared* correctly, but **in the browser**, where the rule is not merely violated but is **unobservable**: a mock-up with hard-coded data is exactly where an approximate total hides, because the numbers are small and the drift is one cent.

**The cost of finding out later.** The moment the surface is wired, the *displayed* tip and the *stored* tip are two numbers produced by two implementations of one rule, and a waiter who is told the guest underpaid by a cent will chase it. The reconciliation is worse: feature 06's `spend_per_cover` and the daily report would read from the ledger, so the report and the screen would disagree in front of the owner.

**And it is free today.** The mock-up has **zero `fetch()` calls** (`grep -c "fetch(" index.html` → **0**). There is no live surface on which the drift can currently mislead a real operator, so **nobody has reported it and nobody can**. That is exactly why it must be fixed **now**, while it is a one-file change to a file nobody depends on, rather than later, when it is a cross-surface reconciliation.

**This is the same argument the corpus has already accepted for `Table.label` (455), `MenuItem.name` (458) and `AppUser.name` (462): a spoken identifier with no rule is cheap to fix before it exists and expensive after.**

## Adjacent evidence

**Third-party instruments — read in the raw fetch, no code adopted, no licence gate triggered:**

- **`AlgoVyn/bikri`** (MIT ✓, ★1 / ⑂0 = **NO traction evidence in either direction**, created 2026-10-26, pushed 2026-11-10, fetched by direct `GET /repos/` on 2026-11-10) — its `sale_lines` and its *derived-not-stored* discipline are the same shape as this slice's *computed-not-displayed* rule. **Already cited by features 453/454/455/459/461 — used as corroboration only, NOT re-picked.**
- **`smithadifd/ledger`** (MIT ✓, ★0 / ⑂0 = **NO traction evidence**, created 2026-11-02, pushed 2026-11-10, direct `GET`) — *"Current state is derived from the events and never edited."* **Already cited by feature 457 — corroboration only.**
- **`manoranjan2050/RestoPro-ERP-Web`** (MIT ✓, ★1 / ⑂0 = **NO traction evidence**, created 2026-11-04, pushed 2026-11-05, direct `GET`) — **already cited by features 443/448/459 — corroboration only.**

**⭐ THE GENUINE DUPLICATES, MARKED AND SKIPPED (not re-picked):**

- **`AlgorithmVyn/bikri` → `AlgoVyn/bikri`** — 11 corpus files cite it. **Skipped.**
- **`baba-dev/menuminute`** (MIT ✓, ★1 / ⑂0 = NO traction evidence) — 3 corpus files cite it (443, 459, 461). **Skipped.**
- **`manoranjan2050/RestoPro-ERP-Web`** — 7 corpus files cite it. **Skipped.**
- **`ferret-project/ferret`** (MIT ✓, **★18** — the highest-starred fresh permissive candidate in the 2026-11-10 pool, created 2026-10-31) — *"Find anything you own — a self-hosted home inventory with a REST API and an MCP server for Claude."* **A home-inventory app, not a restaurant system. Not adopted.** **Recorded because it is the top of the mechanical star ordering and its exclusion is a judgement, not a fact.**
- **`ahmerahdev/karobar-erp`** (MIT ✓, ★3) — multi-tenancy is **§3.2's explicit non-goal**. **Skipped on scope.**
- **`famalthtechnologies/famalth-lynx-pos`** (Apache-2.0 ✓, ★3) — 2 corpus files cite it (455, 460). **Skipped.**
- **`nikolaosmanhss-png/pantrytrack`** (MIT ✓, ★3 / ⑂3, created 2026-11-09, Python/SQLite — *"Open-source stock and food-waste tracker for small restaurants and cafes"*) — **the closest domain match in the fresh pool**, but ★3 is **no traction evidence**, and its food-waste model is **feature 432's** sign-matrix territory. **Recorded, not adopted.**
- **`salhiworks/sorrel-restaurant-starter`** (MIT ✓, ★1, created 2026-11-09) — a Next.js website starter with a Supabase backend. **Not adopted: LE31's stack is FastAPI/SQLModel/vanilla HTML (§4.1).**
- **`opensourcepos`, `NexoPOS`, `n8n`, `medusajs`, `saleor`, `strapi`, `nocodb`** — all **created before the window** (in-window by push only) and/or licence-incompatible (AGPL-3.0, BUSL-1.1, Sustainable Use License). **§3.2 blockers. No code adopted.**

**The HN family produced no signal for this pick.** 20 in-window hits across 8 queries, 0 promoted. The titles are *"Show HN: Launch HN: Tableline – a simple POS for coffee shops that works offline"*, *"Show HN: Tablet menu that works without internet"*, *"Show HN: I replaced my restaurant spreadsheet with a small web app"*, *"Ask HN: What is your approach to handling PCI compliance for small POS vendors?"*. **None of them is a product with a money-precision rule to borrow.** The family is **soft for the eighth consecutive pass.**

## Verification protocol

**All seven checks run against the FILE, offline. No network, no database.**

```bash
# 1. The helper exists and has exactly ONE definition.
grep -c "^const money = {" index.html     # must be exactly 1

# 2. No money arithmetic remains in float form.
#    Every toFixed(2) on a money value must be GONE.
grep -c "toFixed(2)" index.html            # must be 0

# 3. Every money literal in the fixture is an integer count of cents.
#    No fixture money value may have a decimal point.
grep -nE "unit_price: *[0-9]+\.[0-9]" index.html   # must be 0 hits
grep -nE "subtotal: *[0-9]+\.[0-9]" index.html     # must be 0 hits

# 4. The arithmetic is exact: re-run the three diverging cases
#    through the browser helper AND through Python Decimal, and
#    require the two to agree.
node -e '<load money from index.html; compute the 3 cases>' > /tmp/money.json
python3 verify_money_parity.py /tmp/money.json
#    -> asserts: for each case, node cents == Decimal cents, and
#                fmt(0) is "0.00 €" and never "-0.00 €"

# 5. The corpus agrees: the browser-side money rule is now owned.
grep -rl "toFixed" features/ specs/ | wc -l     # must be >= 1 (this feature)

# 6. The charter clause is named in the file.
grep -c "Decimal" index.html                    # must be >= 1 (the rule is cited)

# 7. Nothing outside index.html changed.
git diff --name-only | grep -v "^index.html$" | wc -l   # must be 0
```

**The negative control** must be run on this slice's headline assertion: re-introduce a float multiplication into the fixture (e.g. `unit_price: 1.15`), re-run checks 2–4, and require the exit code to flip **0 → 1**. A check that has only ever passed is not evidence it works.

## Rollback path

**Revert one file.** `git revert <the commit>` restores `index.html` byte-for-byte.

- **No data is at risk** — the mock-up writes nothing; there is no persistence (`features/08`: *"Persistence (refresh = back to mock data)"*).
- **No schema change, no migration, no backfill.**
- **No API change** — no endpoint's contract changes; `main.py` continues to mount the same path.
- **Fully reversible in one step.**
- **The rollback is visible and harmless**: the surface returns to showing `-0.00 €` and `Underpaid by 0.34 €`. Because nothing is wired, **no operator ever sees the difference.**
