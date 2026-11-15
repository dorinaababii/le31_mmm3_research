# Feature 485 — A billed table stores the tax-inclusive total in a field named `subtotal`: the floor card hides the tax split

> Bucket: **v1 — Core MVP**. Verdict: **`build`**. Evidence class: **OBSERVED (executed against LE31's own shipped `index.html` under Node v22, 2026-11-15)**, confidence **high** for the defect, **medium** for its operational consequence.
>
> **This is a first-party finding, and the corpus already knows about it: two filed features record this defect verbatim and both defer it to features that do not own it.**
>
> **The single sentence this feature exists to make true:** *the number on a billed table's card says what it is, and the tax split is visible.*

## Goal

Make the shipped waiter screen's floor card **name and show what it is displaying**.

Concretely, two things:

1. **The field means what it says.** Today the bill-confirm handler writes a **tax-inclusive** total into a field named `subtotal`, and the card renders it under a bare `€` with no tax breakdown. **The tax split is not recoverable from the screen.**
2. **The card shows the split.** A bill is items + tax (+ tip). The card shows one number; the screen knows the other two.

**The charter invariant this touches, verbatim** (`PROJECT_CHARTER.md` §3.6, money):

> Money: never use binary floats. Preserve exact EUR values and **explicit tax/tip derivations**.

**A tax-inclusive total presented under a field named `subtotal`, with no tax shown, is not an explicit tax derivation.** The fix therefore *supports* the invariant.

## Scope

**In scope (v1):**

- **The meaning of the billed table's amount** in `index.html` — what is stored and what it is called.
- **The floor card's rendering of a billed table's amount** — so the tax split is visible.
- **A check** that fails if a tax-inclusive amount is stored under a tax-exclusive name.

**Explicitly NOT in scope:**

- **The browser's money arithmetic.** Feature **465** owns the float→cents conversion and the rounding mode. **This slice must not touch the arithmetic; it must change what is *stored* and what is *shown*.**
- **The tax rate and where it lives.** Features **481 / 408 / 410**. **This slice must not move the rate and must not change the rate's value.**
- **The tip.** Features **05 / 415 / 420 / 457 / 480**.
- **The server-side bill, `Bill.subtotal_tax`, `DerivedTip`.** Features **408 / 415 / 457**.
- **The billed-table click path's null guard.** Feature **484**. **The two are independent and may land in either order.**
- **The mock-up's `T4` fixture value** beyond what the new shape requires.
- **Any schema change, any migration, any Python file, any new dependency.**

## Description

### The defect, as parsed from LE31's own shipped file

The bill-confirm handler, verbatim:

```javascript
document.getElementById('btn-bill-confirm').addEventListener('click', () => {
  const subtotal = state.visit.items.reduce((s, x) => s + x.unit_price * x.qty, 0);
  const tax = subtotal * 0.10;
  const paid = +document.getElementById('inp-paid').value || 0;
  const tip = paid - (subtotal + tax);
  const method = document.getElementById('inp-method').value;
  if (tip < 0) { alert('Cannot close: underpaid.'); return; }
  state.bills.push({ table: state.visit.table_label, subtotal, tax, paid, tip, method });
  // Mark table billed in mock
  const t = MOCK_TABLES.find(x => x.id === state.visit.table_id);
  if (t) { t.status = 'billed'; t.subtotal = subtotal + tax; }
  ...
});
```

**`t.subtotal = subtotal + tax;`**

**A tax-exclusive subtotal is replaced by a tax-inclusive total — and it is stored in a field named `subtotal`.** After this line, `t.subtotal` no longer means what `subtotal` means everywhere else in the same file.

And the floor card, verbatim:

```javascript
<div class="bill">${t.subtotal != null ? t.subtotal.toFixed(2) + ' €' : (t.status === 'free' ? 'Tap to seat' : '')}</div>
```

**One number, a bare `€`, no tax line, no items line.** The card cannot tell the owner what was paid for the food and what was paid for the tax.

### The measured evidence

Executed against the shipped file under Node v22 on 2026-11-15:

```text
=== PROBE A3: what the bill-confirm handler WRITES into t.subtotal ===
source line: `if (t) { t.status = 'billed'; t.subtotal = subtotal + tax; }`
=> a TAX-EXCLUSIVE subtotal is replaced by a TAX-INCLUSIVE total, stored in a field named "subtotal".
   The floor card then renders that tax-inclusive number next to no tax breakdown.

=== FACT 4: bill-confirm writes subtotal+tax into the field named subtotal ===
   if (t) { t.status = 'billed'; t.subtotal = subtotal + tax; }
   the floor card renders it with no tax breakdown:
      ${t.subtotal != null ? t.subtotal.toFixed(2) + ' €' : (t.status === 'free' ? 'Tap to seat' : '')}
```

**The same file uses `subtotal` to mean a tax-exclusive amount in at least four other places** — `renderOrder()` computes it, the bill modal computes it, the tip derivation subtracts it, and `state.bills.push({ …, subtotal, tax, … })` records it. **The `state.bills` record is the proof that the file already knows the difference: it stores `subtotal` and `tax` separately.** The table row is the one place the two are fused.

### The consequence, precisely

**The bill record and the floor card disagree about what they recorded.**

| Surface | What it stores | Tax visible? |
|---|---|---|
| `state.bills` entry | `{ subtotal, tax, paid, tip, method }` — **two separate fields** | yes, in the object |
| The table row | `t.subtotal` = **`subtotal + tax`** — one fused field | **no** |

**So the screen already holds the tax split — in the bill record — and throws it away on the table row.** The fix is not to *compute* anything new; **it is to keep what the screen already knows.**

### Why the corpus knows this and still has not fixed it

This is the unusual part, and it is the strongest evidence that the gap is real.

**Feature 480** (`le31-the-bill-modal-shows-the-waiter-one-tip-and-records-another…`) records it in its *Adjacent work (recorded, NOT picked)* section, verbatim:

> 3. **The floor card's amount is unlabelled** — `t.subtotal = subtotal + tax;` stores the **total due** in a field named `subtotal`, and the floor card renders it under the bare label `€`. Recorded here; **not** picked — the label question is adjacent to **460**'s territory and the amount question to **465**'s.

**Feature 481** (`le31-the-waiter-screen-computes-tax-from-a-literal…`) records the same thing, verbatim:

> 1. **The floor card stores the total due in a field named `subtotal`** — `t.subtotal = subtotal + tax;` — and renders it under a bare `€` label. The *amount* question is feature **465**'s; the *label* question is adjacent to feature **460**'s territory. **Not picked.**

**Both deferrals point at features that do not own this:**

- **465** (`le31-the-waiters-screen-shows-a-different-tip-than-the-ledger-stores…`) owns the **money arithmetic** — the float→cents conversion and the rounding mode. Its own text says: *"Replace every money computation in `index.html`"* and *"This slice does not define a tax rule."* **It is about how the number is computed, not about what the stored field is called or whether the tax is shown.**
- **460** (`le31-a-tables-area-is-free-text-main-main-and-main-are-three-areas.md`) owns the **table's `section`/area being free text** — `main`, `main`, `patio` are three areas because the value is unnormalised. **A corpus grep for `subtotal`, `tax`, `floor card` or `amount` in feature 460 returns zero hits.** The "label question" that 480 and 481 deferred to it is a **different label entirely** — a table's area, not a table's amount.

**So: two filed features identified the defect, wrote it down accurately, and pointed it at two features that do not own it. Nobody picked it up.** This is the exact failure mode feature **431** documents: *"the corpus already knows this gap exists and has never filed it."*

**A deferral to a non-owner is a gap, not a decision.**

### Why no filed feature owns it

A corpus-wide grep over all **516** feature contracts and **476** HANDOFFs:

| Shape searched | Result |
|---|---|
| A feature **owns** "the floor card stores the total due in a field named `subtotal`" | **0 hits.** The two matches are 480's and 481's deferral notes, each ending *"Not picked."* |
| A feature requires the floor card to show a **tax breakdown** | **0 hits** |
| A feature requires the card's amount to be **labelled** | **0 hits** |
| A feature owns the **bill record vs the table row disagreeing** | **0 hits** |
| A feature owns "a tax-inclusive total is stored under a tax-exclusive name" | **0 hits** |

### Data model

**No schema change. No new table. No migration. No Python file.**

The change is to `index.html` and is of one of two shapes:

| Direction | What changes | When it is right |
|---|---|---|
| **Store the split** (recorded default) | The table row gains `subtotal`, `tax` and `total` (or the existing field is renamed to `total` and two fields are added), and the card renders the split. | **When the card should show what it is showing.** The screen already computes all three values at bill time — `subtotal`, `tax`, and `subtotal + tax` — and already stores the first two in `state.bills`. |
| **Store one correctly-named total** | The field is renamed `total` (or `amount`) and the card labels it `Total (incl. tax)`. | **When the card should show one number.** Cheapest, and honest about the name — **but the tax split stays invisible.** |

**Recorded default: store the split.** The evidence is that the screen already computes and already records the split in `state.bills`; **the change is to stop discarding it on the table row.** The implementer may choose the cheaper direction and must record why.

**What this slice must NOT do:** change the arithmetic, change the rate, change the tip, or add a server-side field.

### Implementation steps

1. **Decide and record the direction** — store the split, or store one correctly-named total. **Recorded default: store the split.** Record the decision in a comment at the write site.
2. **Stop writing a fused amount into a tax-exclusive name.** Whatever the shape, the field a reader meets must mean what its name says. **If the split is stored, `t.subtotal` must be the tax-exclusive subtotal and a separate field must carry the total.**
3. **Render the split on the card.** The card currently renders one string. **The rendered card must let the waiter tell the items amount from the tax.** **The tip is explicitly out of scope** — the card's job is the bill's composition, and the tip is features 480/457's.
4. **Make the fixture agree.** `T4` carries `subtotal: 87.00` in the shipped fixture. **Whatever the new shape is, `T4` must carry it — and the fixture value must mean the same thing the code writes.** A fixture value with a different meaning from the code's would be a second instance of this very defect.
5. **Do not touch the arithmetic.** The values written must be the ones the bill-confirm handler already computed: `subtotal`, `tax`, and `subtotal + tax`.
6. **Add the check** (see *Verification protocol*). **Write it first — it must fail on today's file.**

### Telegram interaction if any

**None.** This feature is entirely inside the waiter's browser. It adds no Telegram command and changes no bot handler.

**One consequence to record:** the bill summary the cook or owner would see is not built by this screen. **The card's split is the waiter's view.** If an owner-facing recap is later built from the same fixture, it must carry the same split — recorded, not implemented here.

### Dependencies

- **`index.html`** — the bill-confirm handler, the floor-card renderer in `renderFloor()`, and the `MOCK_TABLES` fixture.
- **Feature 465** — owns the money arithmetic (floats → cents) and the rounding mode. **This slice must not change the arithmetic and must not define a rounding rule.** It writes whatever values 465's arithmetic produces.
- **Feature 481 / 408 / 410** — own the tax rate and its home. **This slice must not move the rate or change its value.**
- **Feature 480** — owns the duplicated tip derivation and the bill modal's single-derivation site. **This slice must not change the tip formula.**
- **Feature 484** — owns the billed branch's null guard. **The two are independent: 484 guards the read, 485 decides what the field means and shows.** Either may land first.
- **Feature 467** — owns the fixture/API drift check and may mark `T3`/`T4`/`T6` with `notYetImplemented: true`. **This feature's fixture change must not collide with that marking.**
- **Feature 474** — owns the per-table order state; the bill-confirm handler acts on `state.visit`.
- **Features 24 / 466 / 475 / 476** — also edit `index.html`. **File-level collision; a rebase is required.**

### Open questions

1. **Store the split, or store one correctly-named total?** **Recorded default: store the split.** The screen already computes and records it elsewhere.
2. **Should the card show the tip too?** **Recorded default: no.** The card's job is the bill's composition; the tip is features 480/457's, and adding it would widen the scope into a money rule this slice does not own.
3. **Is the card's `€` label a "label question" that belongs to feature 460?** **Recorded: no.** Feature 460 owns the *table area*'s free text. **The amount's label is unowned, and this contract owns it.**
4. **Should `T4`'s fixture value be the tax-inclusive `87.00` or a split?** **Recorded: whatever the code writes.** A fixture value that means something different from the code's write is a second instance of the defect.
5. **Does the floor card's amount change if the tip is added later?** **Recorded default: no — the card shows items + tax = total.** The tip is a separate derivation with its own features.

### Why this matters

**The bill is the one number a restaurant cannot get wrong in front of a guest, and this is the one surface where it is displayed without its composition.**

The specific harm is not that the number is *wrong* — the number is arithmetically correct as a total. The harm is that **it is labelled as something it is not.** A card showing `87.00 €` under a field called `subtotal`, with no tax line, tells the owner that 87.00 euros of food was sold. **If the tax is 10%, then 8.70 of that 87.00 was tax, and the owner — who is deciding tomorrow's prep quantities and prices from this screen — reads 87.00 as revenue.**

**That is the failure mode that generalises: a derived value that is stored under a name that misdescribes it is indistinguishable from a fact.** Feature **457** states the discipline for exactly this case, and it is worth quoting verbatim because it is the rule this feature applies:

> **The name is the promise, and the schema is the place where a promise has to be kept.**

**And the reason to do it now, rather than when someone notices, is that the screen already knows the answer.** The bill record on the same page holds `subtotal` and `tax` separately. The fix is not new computation — it is **stopping discarding the split on the way to the card.** Every additional surface that reads the table row will inherit the fused value, so the cost of leaving it grows with every surface.

**The honest cost of doing nothing is low today and rising.** The mock-up makes zero `fetch()` calls, so **no live surface exists on which this can currently mislead anyone.** The defect is certain and its consequence is unobserved. That is why this is a narrow `build` and not a redesign — **and it is also why it should not be left for the pass that finds it in production.**

### Adjacent evidence

1. **The screen already records the split.** `state.bills.push({ table, subtotal, tax, paid, tip, method })` — **two separate fields on the same page, one fused field on the table row.** This is the strongest evidence that the fix is small and that the fusion is an oversight rather than a design.
2. **The same file uses `subtotal` to mean a tax-exclusive amount in at least four other places.** The naming is consistent everywhere *except* the table row.
3. **Two filed features record this defect verbatim and both defer it to features that do not own it** (480 line 226, 481 line 243). **The gap is documented, accurate, and unfiled.**
4. **Feature 465 records that the fixture's `subtotal: 28.00` / `87.00` values are *"display-only fixtures"* that *"are not derived from any line"* and must still be stored in cents.** That is a **fact about the fixture**, not about the card's semantics — **it is adjacent evidence, and 465 owns it.**
5. **Third-party corroboration — vocabulary only, no code adopted.** `satisfecho/pos` (★66, AGPL-3.0, licence-incompatible) and `leandromerov/restaurant-pos-order-system` (MIT, 0★) both show a bill composed of items, tax and tip. **Neither was executed against LE31's code and neither is a source of implementation.** The transferable rule is LE31's own: **a displayed money value must name what it contains.**

### Verification protocol

1. **The stored field means what it is named.** After the bill-confirm handler runs, a table's tax-exclusive subtotal field holds the tax-exclusive amount — **not** `subtotal + tax`.
2. **The total is stored and reachable.** The card can obtain the total the guest paid without re-deriving it from a misnamed field.
3. **The card shows the split.** The rendered card for a billed table distinguishes the items amount from the tax.
4. **The card shows no tip.** Assert the tip does not appear on the card — the tip is out of scope.
5. **The fixture and the code agree.** `T4`'s fixture value has the same meaning as the value the code writes for a billed table.
6. **The arithmetic was not touched.** `git diff -- index.html` shows no change to the `reduce(...)`, the `* 0.10`, or the tip derivation — **this slice changes what is stored and shown, not how it is computed.**
7. **The regression test fails on today's file.** Checks 1 and 3 **must fail** against the shipped `index.html` before the fix is applied. **If they pass, the test is not testing the defect.**
8. **The corpus agrees.** `grep -rn "t.subtotal = subtotal + tax" features/ specs/` must hit **this** contract.

## Rollback path

**Fully reversible.** The change is confined to `index.html`: the bill-confirm handler's write, the floor-card renderer, and the `T4` fixture value.

- **Roll back by reverting the file.** No schema change, no migration, no data.
- **There is no data at risk**: the mock-up persists nothing, and `state.bills` — the record that already holds the split — is not changed.
- **The one thing a rollback loses** is the split on the card, and with it the misleading field name returns.

## Out of scope

- The browser's money arithmetic, the float→cents conversion, the rounding mode — feature **465**.
- The tax rate and its home — features **481 / 408 / 410**.
- The tip formula and the duplicated tip derivation — features **480 / 457 / 05 / 415 / 420**.
- The billed branch's null guard — feature **484**.
- The fixture/API drift check and the `notYetImplemented` marking — feature **467**.
- The floor grid's layout — feature **24**.
- The seat form, the sold-out filter, the order-line quantity phase, the single-visit state — features **466 / 475 / 476 / 474**.
- The server-side bill, `Bill.subtotal_tax`, `DerivedTip` — features **408 / 415 / 457**.
- Any Python file, any endpoint, any schema change, any migration, any new dependency.
