# Feature 484 — The billed floor card dereferences an absent `subtotal` and crashes: tapping a billed table throws instead of showing the bill

> Bucket: **v1 — Core MVP**. Verdict: **`build`**. Evidence class: **OBSERVED (executed against LE31's own shipped `index.html` under Node v22, 2026-11-15)**, confidence **high** for the defect, **medium** for how often a billed table lacks a `subtotal`.
>
> **This is a first-party finding.** The third-party sources from today's fetch were the *instruments*; the subject is LE31's own shipped waiter screen.
>
> **The single sentence this feature exists to make true:** *tapping a billed table shows the bill — it never throws.*

## Goal

Make the shipped waiter screen's floor-card click path **safe for every table**, not just the ones that happen to carry a `subtotal`.

Concretely, two things:

1. **A tap never throws.** The billed branch dereferences `t.subtotal` with no guard, so a billed table with no `subtotal` produces a `TypeError` and the handler aborts before it can show anything.
2. **The absence is reported, not invented.** When there is no amount, the screen says so. **It must not show `0.00 €`** — a missing number and a zero amount are different facts, and a waiter must not read one as the other.

## Scope

**In scope (v1):**

- **The guard on the billed-table branch** in `index.html`'s `onTableClick`.
- **A fallback message** for a billed table with no amount, which states *why* the amount is unavailable.
- **A check** that fails if the billed branch can dereference an absent value.

**Explicitly NOT in scope:**

- **The floor card's rendering of the amount.** Feature **485** owns what the amount *means* (a tax-inclusive total stored in a field named `subtotal`). **This feature owns only whether the tap crashes.**
- **The floor grid's layout.** Feature **24**.
- **The fixture/API drift check.** Feature **467**.
- **The mock-up's `T4` fixture value.** This feature does **not** add a `subtotal` to `T4` — **that would hide the defect rather than fix it.**
- **Any schema change, any migration, any Python file, any new dependency.**

## Description

### The defect, as parsed from LE31's own shipped file

`onTableClick`, verbatim from `index.html`:

```javascript
function onTableClick(t) {
  if (t.status === 'free')   openSeatModal(t);
  else if (t.status === 'billed') alert(`Table ${t.label} bill: ${t.subtotal.toFixed(2)} € (mock)`);
  else if (t.status === 'dirty') alert(`Table ${t.label} needs clearing (mock)`);
  else { /* seated / ordered → load into order view */ }
}
```

**`t.subtotal.toFixed(2)` — with no guard on `t.subtotal`.** The two neighbouring branches (`free` → open a modal; `dirty` → an alert with a fixed string) are both safe. **The `billed` branch is the only one that dereferences a value that may be absent.**

Note also that the `ordered` branch does **not** show `t.subtotal` at all, and the `seated` branch does not either — **`subtotal` is dereferenced on exactly one path, and that path is the one that can throw.**

### The measured evidence

Executed against the shipped file under Node v22 on 2026-11-15:

```text
=== PROBE A: what the floor card shows for a BILLED table ===
T4 status           : billed
T4.seats           : 6
T4.subtotal (fixture): 87
T4.party           : {"size":5,"adults":5,"children":0}
floor card renders  : 87.00 €

=== PROBE A2: the billed-table click handler ===
onTableClick for a billed table does: alert(`Table ${t.label} bill: ${t.subtotal.toFixed(2)} € (mock)`)
=> it labels the amount "bill", and the value is the field named "subtotal".
Does the code check whether subtotal includes tax?  NO
```

And the crash, executed by removing the field from a `billed` table and calling the shipped handler:

```text
=== TEST 1: clicking a billed table whose fixture has NO subtotal ===
click path source for billed: else if (t.status === 'billed') alert(`Table ${t.label} bill: ${t.subtotal.toFixed(2)} € (mock)`);
=> `t.subtotal.toFixed(2)` with NO undefined guard.

onTableClick(T4 without subtotal) -> THREW: TypeError: Cannot read properties of undefined (reading 'toFixed')
```

**The throw is real and it happens inside the handler.** The alert on the next line is never reached.

### Why the shipped path does not crash today — and why that is not a defence

**The shipped fixture happens to give `T4` a `subtotal` of `87.00`.** That is the *only* reason the shipped `billed` path does not throw on the shipped fixture. **The fixture is not a guard.**

```text
fixture rows and whether they carry subtotal:
   T1 status=free    subtotal=ABSENT
   T2 status=seated  subtotal=ABSENT
   T3 status=ordered subtotal=ABSENT     <- (the shipped T3 does carry 28.00)
   T4 status=billed  subtotal=ABSENT     <- (the shipped T4 does carry 87.00)
   T5 status=free    subtotal=ABSENT
   T6 status=dirty   subtotal=ABSENT
   P1 status=free    subtotal=ABSENT
   P2 status=seated  subtotal=ABSENT
```

**(The parenthetical above is the probe's own regex artefact, corrected by the direct-GET probe: the shipped `T3` carries `subtotal: 28.00` and the shipped `T4` carries `subtotal: 87.00`; the fixture rows `T1`, `T2`, `T5`, `T6`, `P1` and `P2` carry no `subtotal` at all.)** The point stands regardless of which rows carry the field: **`subtotal` is an optional field on a table row, and exactly one code path dereferences it unconditionally.**

### How a billed table loses its `subtotal` — the reachable paths

Three paths in the shipped file can produce a `billed` table with no `subtotal`:

1. **The bill-confirm handler's `if (t)` guard.** The handler writes `t.subtotal = subtotal + tax` **only if `t` was found**:

   ```javascript
   const t = MOCK_TABLES.find(x => x.id === state.visit.table_id);
   if (t) { t.status = 'billed'; t.subtotal = subtotal + tax; }
   ```

   **`t.status` is set inside the same guard, so `t.status = 'billed'` also only happens when `t` is found.** So a table that becomes `billed` through this path always gets a `subtotal`. **This path is safe — and it is exactly why the shipped fixture works.**

2. **The fixture.** `MOCK_TABLES` is hand-written data. `T4` is the only `billed` row and it carries `87.00`. **Any future fixture row added as `billed` without a `subtotal` crashes the screen.** This is a *maintainer* path, not a runtime one — and it is the most likely one, because adding a table to the fixture is exactly what someone does to test a new floor layout.

3. **The mock-up's own reset.** `renderFloor()` re-renders from `MOCK_TABLES`; a page reload restores the fixture. There is no persisted state, so the fixture is the whole world.

**The honest summary:** the crash is **certain to be reachable and currently masked by a hand-written fixture value.** That is a weaker statement than "the shipped path crashes today", and it is the true one. **The gate treats it as a `build` because the fix is one conditional, the failure mode is a crash in the waiter's busiest surface, and the masking value is one line of hand-written data that any edit can remove.**

### Why this is not feature 467, 485, or 465

- **467** owns the **fixture/API drift check** — *"the mock-up calls no API and no test compares the two."* **Its subject is the absence of a comparison.** This feature's subject is a **crash on a code path**. 467 may well add a check that would catch this — **if a crash is what it looks for.** Recorded as a dependency, not a duplicate.
- **485** owns **what the amount means** — a tax-inclusive total stored in a field named `subtotal`. **This feature owns only whether the tap throws.** **The two must not be merged**: 485 is a semantics contract, this one is a null-safety contract, and merging them would put a money-semantics change and a one-line guard in the same PR.
- **465** owns the browser's **money arithmetic** (floats → cents). This feature touches no arithmetic — **it adds a guard, not a computation.**

### Why no filed feature owns it

A corpus-wide grep over all **516** feature contracts and **476** HANDOFFs:

| Shape searched | Result |
|---|---|
| A feature states that the **billed-table click path** can throw | **0 hits** |
| A feature names `t.subtotal.toFixed` as a **defect** | **0 hits** |
| A feature states that a **floor-card tap** crashes | **0 hits** |
| A feature requires an **undefined/null guard** on a mock-up amount | **0 hits** |

The three hits for `TypeError` in the corpus are feature **453**'s SQLite timezone `TypeError` (a Python backend defect, unrelated) and feature **457**'s *"the cost of the defect is not a crash"* (about `DerivedTip`, unrelated). **Nobody owns this.**

### Data model

**No schema change. No new table. No migration. No Python file.**

The change is to `index.html` and is one guard plus one message:

```javascript
else if (t.status === 'billed') {
  if (t.subtotal == null) {
    alert(`Table ${t.label} was billed — amount unavailable (mock)`);
  } else {
    alert(`Table ${t.label} bill: ${t.subtotal.toFixed(2)} € (mock)`);
  }
}
```

**The exact fallback wording is the implementer's choice; the constraint is that it must state the absence and must not print a number.** A `0.00 €` fallback would be **a wrong fact presented as a true one**, which is strictly worse than a crash for a waiter deciding what to do next.

**Note the boundary with feature 485.** Once 485 lands, the field may hold a *tax-inclusive total* and may carry a tax breakdown. **This feature's guard must not assume what the field means — it must only assert that the field is present.** The two contracts are independent and can land in either order.

### Implementation steps

1. **Add the guard on the billed branch.** Use a presence check that covers both `undefined` and `null` (`== null` or an explicit `typeof` check) — **the fixture's absent property reads as `undefined`, but a future `subtotal: null` would read as `null`, and both must be safe.**
2. **Write the fallback message.** It must state that the amount is unavailable and must not print `0.00` or any other number.
3. **Do not add a `subtotal` to the fixture's `T4`.** **That is the one change that would make the check pass without fixing the defect**, and the check in step 5 is written to catch it.
4. **Check the other branches while you are there — but do not change them.** `free`, `dirty` and the `seated`/`ordered` branch are all already safe. **This slice adds no guard where none is needed.**
5. **Add the check** (see *Verification protocol*). **Write it first — it must fail on today's file.**

### Telegram interaction if any

**None.** This feature is entirely inside the waiter's browser. It adds no Telegram command, changes no bot handler, and changes nothing the cook sees.

### Dependencies

- **`index.html`** — `onTableClick`, and the `MOCK_TABLES` fixture (read-only; **not to be edited**).
- **Feature 485** — owns the meaning of the `subtotal` field. **This feature must not change what the field contains.** The two are independent; either may land first.
- **Feature 467** — owns the fixture/API drift check. **Its check may or may not detect a crash; this feature's check is specifically about the guard.**
- **Feature 474** — owns the single-visit state and the per-table order state. **The billed path is reachable through the bill-confirm handler, which acts on `state.visit`.** Recorded as a dependency, not a blocker.
- **Feature 24** — owns the floor grid's layout. **This feature must not change the card's markup**, only the click handler.

### Open questions

1. **What should the fallback say?** **Recorded default: state that the amount is unavailable.** The implementer may propose a better phrase; the constraint is that it prints no number.
2. **Should the floor card itself show something for a billed table with no amount?** **Recorded default: no — this slice touches the click handler only.** The card's rendering is feature **485**'s and feature 24's territory.
3. **Should a `billed` table without a `subtotal` be prevented at write time?** **Recorded default: no.** The bill-confirm handler always writes both fields together, so the write path is already consistent. **This is a read-path robustness fix, not a write-path constraint.**
4. **Is `t.subtotal` ever legitimately `0`?** **Recorded: yes, and `0` must still render as `0.00 €`.** This is why the guard must test for *absence*, not for falsiness — **a falsy check would silently turn a zero bill into "unavailable".** The implementer must use `== null`, **not** `!t.subtotal`.

### Why this matters

**The floor grid is the waiter's primary surface and the only one that is always visible.** A tap there is the most common interaction in the product. And a crash in that path is not a partial failure — **the handler aborts, nothing is shown, and the waiter gets no feedback at all.** The closest mental comparison is the one the corpus already recorded for the bot: *an unregistered command does not produce "unknown command"; aiogram's dispatcher drops it silently, and from the cook's side the bot hung.*

**Here the same silence has a stack trace attached.** The waiter taps a billed table and nothing happens. They tap again. Nothing happens. They conclude the table is not really billed, or that they tapped wrong, or that the app is broken — **and every one of those conclusions is wrong.**

**And the second cost is the masking.** The defect does not fire on today's fixture, so nobody will ever report it. It is latent behind one hand-written number (`87.00`) that a future edit to the fixture can remove without anyone noticing. **A crash that is one fixture edit away from firing is a crash that will fire.** The alternative to fixing it now is a check that only exists to notice, later, that a screen began throwing — **and by then it will be in front of a customer.**

**The cost of the fix is one conditional and one sentence.** The cost of not fixing it is a crash in the product's busiest surface, discovered by a waiter rather than by a test.

### Adjacent evidence

1. **The neighbouring branches are already safe** — `free` opens a modal, `dirty` alerts a fixed string. **The unsafe branch is the only one that reads a value.** Recorded as evidence that the fix is a one-branch change.
2. **The `subtotal` field is display-only and hand-written** — `T3: subtotal: 28.00`, `T4: subtotal: 87.00` — and is *not* derived from any order line. Feature **465** records that these fixture values *"are display-only fixtures"*. **This feature does not change them.**
3. **Feature 467 records that the mock-up calls no API and no test compares it to the server.** A crash in a fixture-only screen is invisible to any server-side test — **so the check in this contract must be a browser-free DOM-harness check, exactly as feature 477's is.** Recorded so the implementer does not look for a server-side test to write.
4. **Third-party corroboration — vocabulary only, no code adopted.** `mrsalt227-ui/kafe78-pos` (null licence, 0★) separates kasir / waiter / dapur / stok / laporan surfaces, and `satisfecho/pos` (★66, AGPL-3.0, licence-incompatible) describes a multi-tenant floor/table surface. **Neither was executed against LE31's code and neither is a source of implementation.** The transferable rule is LE31's own: **a user-facing surface must degrade to a message, never to an exception.**

### Verification protocol

1. **The guard exists and is presence-based.** Assert the billed branch does not dereference `t.subtotal` unconditionally.
2. **The absent case does not throw.** With a `billed` table whose `subtotal` is absent, invoking the shipped handler **must not raise** and must produce a message that **contains no number**.
3. **The present case still shows the amount.** With `subtotal: 87`, invoking the handler shows `87.00 €`.
4. **`null` is also safe.** With `subtotal: null`, invoking the handler does not throw.
5. **Zero is not "absent".** With `subtotal: 0`, invoking the handler shows `0.00 €` — **not** the unavailable message. **This check exists specifically to catch a falsy guard.**
6. **The regression test fails on today's file.** Steps 2, 4 and 5 **must fail** against the shipped `index.html` before the fix is applied. **If they pass, the test is not testing the defect.**
7. **The fixture was not "fixed" instead.** Assert the shipped `MOCK_TABLES` is unchanged by this slice — in particular, that `T4` was not given a `subtotal` it did not have.
8. **The corpus agrees.** `grep -rn "onTableClick" features/ specs/` must hit **this** contract.

## Rollback path

**Fully reversible.** The change is confined to `index.html`: one conditional and one message inside `onTableClick`.

- **Roll back by reverting the file.** No schema change, no migration, no data.
- **There is no data at risk**: the mock-up persists nothing.
- **The one thing a rollback loses** is the guard, and with it the crash returns.

## Out of scope

- What the `subtotal` field means — feature **485**.
- The browser's money arithmetic — feature **465**.
- The fixture/API drift check — feature **467**.
- The floor card's markup and the floor grid's layout — feature **24**.
- The single-visit state and the per-table order state — feature **474**.
- The bill, the money rules, the tax rate, the tip — features **05 / 408 / 410 / 415 / 420 / 457 / 480 / 481**.
- Any Python file, any endpoint, any schema change, any migration, any new dependency.
