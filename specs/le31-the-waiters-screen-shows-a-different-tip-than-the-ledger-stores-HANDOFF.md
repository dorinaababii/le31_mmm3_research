# HANDOFF — Feature 465: the waiter's screen shows a different tip than the ledger stores

> **Slice contract for the coding agent.** Feature: `features/465-le31-the-waiters-screen-shows-a-different-tip-than-the-ledger-stores-the-shipped-mock-up-computes-money-in-javascript-floats.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (executed under `node` on 2026-11-10).
> Filed by: Daily Brainstorm 2026-11-10 (100th daily-brainstorm pass), Pick A.

---

## 1. The active feature path

```
features/465-le31-the-waiters-screen-shows-a-different-tip-than-the-ledger-stores-the-shipped-mock-up-computes-money-in-javascript-floats.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 411 / 408 / 05 / 415 / 420 / 457 / 24 / 388, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | The mock-up's own JavaScript, run under `node` on 2026-11-10, against LE31's own `Decimal` rule: `0.10 × 3` paid `0.33` → node tip `-0.00000000000000` → `toFixed(2)` = **`-0.00`**, Decimal tip = **`0.00`**; `1.15 × 3` paid `3.45` → node tip `-0.34500000000000` → **`-0.34`**, Decimal tip = **`-0.35`**. **Three divergences measured.** |
| 2 | The defect is in LE31's own code | **PASS** | `index.html` (30,530 bytes, 720 lines, mounted at `/` by `backend/app/main.py`): `const subtotal = state.visit.items.reduce((s, x) => s + x.unit_price * x.qty, 0);` and `const tax = subtotal * 0.10;` and `const tip = paid - (subtotal + tax);` — **all IEEE-754 double arithmetic.** `PROJECT_CHARTER.md` §7, verbatim: *"Money sums use `Decimal` arithmetic. No `float(qty * price)` anywhere."* |
| 3 | No filed feature owns it | **PASS** | Sweep over **959** feature contracts + HANDOFFs: `toFixed` → **0 hits**. Feature **411** owns the **ten server-side `Decimal` fields** and explicitly notes *"the waiter surface is a static mockup with zero `fetch()` calls"* — it fixes the server, **not the browser**. |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **411** = server-side money precision (ten `Decimal` fields). **408/410** = the tax rate and the rounding mode. **05/415/420/457** = what the tip *is*. **This slice = how the browser computes and formats money.** **Four different questions.** |
| 5 | The demand is real | **PARTIAL — recorded honestly** | No operator has reported a wrong tip — **the mock-up has zero `fetch()` calls**, so there is no live surface on which the drift can mislead anyone. **Yet.** |
| 6 | It is cheap now and expensive later | **PASS** | One file, one region, one helper. **No schema change, no Python change.** Expensive later: the moment the surface is wired, the **displayed** tip and the **stored** tip come from two implementations of one rule, and a guest who paid exactly is told they underpaid. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — it DOES fire, and it is the finding** | Feature **411** is about to land a `Decimal` guard **on the server's ten fields**. It would faithfully leave the browser's arithmetic untouched. **411 must cite this feature, or this must land first, or in the same PR.** |

**Overall: `build`.** The weakest link is check 5, weak for the same mechanical reason as the other two picks of this pass: **the surface that would produce the complaint does not exist yet.** That is also the reason it is cheap.

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `index.html` | **The `money` helper + every money computation and display site** | **One file. No build step** (§4.1: *"vanilla HTML + JS. No build step"*). The fixture's money literals become **integer cents**. |
| `backend/app/config.py` | **Nothing, unless the tax rate is needed there** | The tax rate is **feature 408's** territory. **Do not add it here.** |
| `features/08-index-mockup.md` | **One line** — record the money constraint the mock-up spec did not state | So the informal spec and the contract agree. |
| `features/411-le31-money-precision-declared-not-enforced-…md` | **One line** — name this feature as its **browser-side sibling** | 411 fixes the server; this fixes the browser. **Neither blocks the other.** |
| The repo's verification tooling (**check what exists**) | **One parity check** | Node vs `Decimal`, offline. See §6. |

**Do NOT touch:** `backend/app/models.py` (feature 411 owns the money **fields**), `backend/app/routers/tables.py`, any `Decimal` declaration, the tax rate (408), the tip formula's meaning (05/415/420/457), the floor grid (feature 24), the seat modal's bounds (**feature 466**), the fixture's status values (**feature 467**).

## 4. The implementation, in order

1. **Decide and record the representation.** Recorded default: **integer minor units (cents)**, held in a `Number`. **A `Number` holding an integer count of cents is exact to 2^53 cents ≈ 90 trillion euros.** State this bound in the code comment.
2. **Add the `money` helper** — `parse`, `of`, `add`, `sub`, `mul`, `pct`, `fmt`. **One definition, one home.** `fmt` must normalise the negative zero (`(-0).toFixed(2)` is `"-0.00"`).
3. **Convert the fixture's money literals to cents** — `unit_price: 14` → `unit_price_cents: 1400`; `subtotal: 28.00` → `2800`. **A `Number` must never hold a money value, not even in the fixture** — the fixture is what the arithmetic operates on.
4. **Rewrite the three computation sites** (`subtotal`/`tax`/`total`; the bill modal's `tip`) to use the helper.
5. **Rewrite the display sites** to use `money.fmt`. **Every `toFixed(2)` on a money value must be gone.**
6. **Fix the `paid` parse** — `money.parse(...)` instead of `+value || 0`.
7. **Fix the negative zero at the source too** — the tip computation must normalise `-0` to `0` **before** the `tip < 0` branch, not only in the formatter. **See §5.2.**
8. **Record the rounding rule** in a comment next to `money.pct`, naming feature **408**. **Do not invent a tax rule.**
9. **Add the parity check** (see §6). **Write the regression test first** — it must fail on today's file.

## 5. The four things that will go wrong if nobody tells you

1. **Fixing only the formatter and leaving the arithmetic in floats.** `toFixed(2)` on a float that has already drifted gives a **drifted** two-decimal number — the `1.15 × 3` case proves it (`-0.34` vs the Decimal `-0.35`). **The arithmetic must move to integer cents; the formatter is cosmetic by comparison.**
2. **Normalising `-0` only in the formatter.** The mock-up **branches** on the sign: `tip < 0` selects *"Underpaid by X €"*. A tip of `-0.0000000000000000004` is negative, so **the waiter is told to chase a shortfall on a table where the guest paid exactly** — and `money.fmt` alone would still print `-0.00 €`. **The zero must be normalised before the branch, and in the formatter.** **Two places, not one.**
3. **Moving the tax rate into the browser.** The rate is feature **408**'s, and the charter §7 puts magic numbers in `config.py`. **This slice must round the way the server rounds, and must not become a second source of the rate.** If 408 has not landed, the placeholder is `Math.round` **and it must be marked provisional**.
4. **Editing `index.html` without knowing feature 24 and 466 are in it.** **Three features of this pass and feature 24 all touch this file.** The regions are disjoint — **the bill modal's arithmetic** (this), **the seat modal's inputs** (466), **the floor grid** (24), **the fixture's statuses** (467) — but **a rebase is required.** Say which landed first in your report.

## 6. Verification protocol

Four offline commands, plus the executed parity test:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The helper exists and has exactly ONE definition.
grep -c "^const money = {" index.html      # must be exactly 1

# 2. No money arithmetic remains in float form.
grep -c "toFixed(2)" index.html             # must be 0

# 3. Every money literal in the fixture is an integer count of cents.
grep -nE "unit_price: *[0-9]+\.[0-9]" index.html   # must be 0 hits
grep -nE "subtotal: *[0-9]+\.[0-9]" index.html     # must be 0 hits

# 4. The corpus agrees: the browser-side money rule is now owned.
grep -rl "toFixed" features/ specs/ | wc -l      # must be >= 1 (this feature)

# 5. The charter clause is named in the file.
grep -c "Decimal" index.html                     # must be >= 1
```

**The executed parity test** — run the mock-up's own `money` helper under `node` on the three diverging cases, and compare against Python `Decimal`:

| case | expected node cents | expected Decimal cents | expected `fmt` |
|---|---|---|---|
| `0.10 × 3`, paid `0.33` | `0` | `0` | `"0.00 €"` — **never `"-0.00 €"`** |
| `6.90 × 3`, paid `22.77` | `0` | `0` | `"0.00 €"` |
| `1.15 × 3`, paid `3.45` | `-35` | `-35` | `"-0.35 €"` |

**The test must fail on today's `index.html` and pass after.** The simplest form of the failing assertion today: `fmt` on a zero tip returns `"-0.00 €"`.

**The negative control** — re-introduce a float multiplication into the fixture (e.g. `unit_price: 1.15`) and confirm the parity check's **exit code flips 0 → 1**. A check that has only ever passed proves nothing.

**Record in the HANDOFF:** which rounding rule you used and where it came from; whether `money.pct` matches feature 408; and **whether the `tip < 0` branch now sees a normalised zero** (it must).

## 7. Rollback path

**Fully reversible in one step.** `git revert <the commit>` restores `index.html` byte-for-byte.

**No data is at risk** — the mock-up writes nothing (`features/08`: *"Persistence (refresh = back to mock data)"*). **No schema change, no migration, no backfill. No API change** — `main.py` continues to mount the same path.

**The rollback is visible and harmless**: the surface returns to showing `-0.00 €` and `Underpaid by 0.34 €`. Because nothing is wired, **no operator ever sees the difference.**

## 8. The mandatory LE31 skill list

Read these before writing code — **all of them**, in this order:

1. `le31-conventions` — the schema conventions and the known conflicts.
2. `le31-data` — the data-model rules (strings, enums, money, timestamps).
3. `le31-v1-feature-pattern` — the v1 feature shape.
4. `le31-frontend` — the front-end conventions.
5. `le31-handoff-spec` — the handoff format itself.
6. `le31-coding-agent-brief` — **produces the paste-in prompt from this contract. Do not paste chat excerpts.**

**And read these four feature contracts in full before you start:**

- `features/411-le31-money-precision-declared-not-enforced-decimal-12-345-is-silently-coerced-on-postgres-and-silently-stored-on-sqlite-dev-and-prod-disagree-v1-money-precision-guard.md` — **the server-side sibling.** It owns the ten `Decimal` fields and names the *absence of a `fetch()` call* as the reason the defect is inert. **You own the browser.**
- `features/408-le31-tax-rate-has-no-home-so-bill-subtotal-tax-is-a-free-floating-money-number-v1-tax-rate-and-rounding-in-config.md` — **owns the rounding rule you must match.**
- `features/457-le31-derived-tip-amount-is-not-constrained-to-its-own-formula-first-party-the-row-that-is-documented-as-computed-is-a-free-standing-number-v1-derived-tip-formula-enforcement.md` — **owns what the tip IS.** You do not change that.
- `features/24-visual-table-layout-v2.md` — **the other `index.html` editor.** Its scope: *"All changes live in `index.html` only."*

## 9. The one thing that matters

**LE31's promise is that the money it shows the owner is the money it stored.** The database at least *declares* `Decimal` (feature 411's ten fields). **The screen the waiter reads does not** — and the screen is where the decision is made. A guest who paid **exactly** is told *"Underpaid by 0.34 €"*, on a table where the arithmetic is exact to the cent.

**The error is not "the number is slightly off". It is "the system tells the waiter the guest has not paid, when they have."**
