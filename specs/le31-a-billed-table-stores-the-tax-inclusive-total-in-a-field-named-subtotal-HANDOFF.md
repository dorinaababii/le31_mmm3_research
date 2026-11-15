# Slice contract — `le31-a-billed-table-stores-the-tax-inclusive-total-in-a-field-named-subtotal`

## Active feature path

`features/485-le31-a-billed-table-stores-the-tax-inclusive-total-in-a-field-named-subtotal-first-party-the-floor-card-hides-the-tax-split-v1-floor-card-amount-semantics.md`

## Seven-check gate verdict

**BUILD.** Evidence class: **observed**, execution-proven under Node v22 against LE31's own shipped `index.html`; confidence **high** for the defect and **medium** for its operational consequence (no operator incident was observed).

1. **JTBD:** When the owner reads a billed table's amount on the floor, they want to know what the guest paid **and** what of it was tax, but the card stores the tax-inclusive total in a field named `subtotal` and renders it under a bare `€`, so the tax split is **not recoverable from the screen**.
2. **Viability:** pass — one field rename or one extra field and one render change; nothing for staff to administer.
3. **Practicability:** pass — no schema change (the fixture is in-browser), no stack change. Rabbit holes: the fixture is **display-only and hand-written**, so the fix must decide whether the floor card stores a `{subtotal, tax, total}` triple or a single correctly-named total; and the tax rate's own home is feature **481**'s subject, so **this slice must not move the rate.**
4. **Conflict:** **none hard.** The charter's money invariant is *"never use binary floats; preserve exact EUR values and explicit tax/tip derivations"* — **a tax-inclusive total presented under a field named `subtotal`, with no tax shown, is not an explicit tax derivation.** The fix therefore *supports* the invariant. It does **not** touch the browser's float arithmetic (feature **465**), the tax rate's home (features **481 / 408 / 410**), or the tip formula (features **05 / 415 / 420 / 457 / 480**).
5. **Outcome/scope:** v1 outcome *the owner can read a billed table's amount without a lie about its name*. Cap at the field's meaning and the card's render. **Do not** fix the float arithmetic, **do not** move the tax rate, **do not** redesign the bill flow, **do not** add the tip to the card.
6. **Cost/value:** small implementation cost; the value is that the one number an owner reads about a closed table has the right meaning, and the tax split is visible rather than absorbed.
7. **Circuit breaker:** stop if the floor card is replaced (features **467 / 474 / 24** all touch `index.html` — **this is a file-level collision and a rebase is required**). Revert one file, one region; no persisted data is at risk.

## Files to touch

- `index.html` — the bill-confirm click handler's write to the table row, the floor-card renderer inside `renderFloor()`, and the `T4` fixture value.
- A focused test/probe file for the billed amount if the repository's test structure supports it.

**Do not edit** the arithmetic — the `reduce(...)`, the `* 0.10`, and the tip derivation stay exactly as they are; **this slice changes what is stored and shown, not how it is computed** (feature **465** owns the arithmetic and the rounding mode). Do not change the tax rate's value or its home (features **481 / 408 / 410**). Do not change the tip (features **480 / 457 / 05 / 415 / 420**). Do not change the billed branch's null guard (feature **484**) — the two are independent and may land in either order. Do not edit the floor grid's layout (feature **24**).

## Verification protocol reference

Follow the feature contract's `## Verification protocol`:

1. The stored field **means what it is named**: after the bill-confirm handler runs, the tax-exclusive subtotal field holds the tax-exclusive amount — **not** `subtotal + tax`.
2. The total is **stored and reachable**: the card can obtain the total the guest paid without re-deriving it from a misnamed field.
3. The card **shows the split**: the rendered card for a billed table distinguishes the items amount from the tax.
4. The card shows **no tip** — assert the tip does not appear on the card.
5. The **fixture and the code agree**: `T4`'s fixture value has the same meaning as the value the code writes.
6. `git diff -- index.html` shows **no change** to the `reduce(...)`, the `* 0.10`, or the tip derivation.

The regression test **must fail against the current file before the fix is applied** — checks 1 and 3 specifically. **If they pass, the test is not testing the defect.** The implementer must **record which direction was taken** (store the split, or store one correctly-named total) and must not change the rate or the arithmetic.

## Rollback path

Revert the `index.html` change (the bill-confirm write, the floor-card renderer, the `T4` fixture value). No schema, data, migration, or persistent state is affected. **The one thing a rollback loses is the split on the card**, and with it the misleading field name returns.

## Mandatory LE31 skill list

- `le31-conventions`
- `le31-v1-feature-pattern`
- `development`
- `speckit-specify`
- `speckit-plan`
- `speckit-tasks`
- `speckit-implement`
- `verify-before-fixing`
- `pre-merge-review`

## Linear reference

Intended as a Feature sub-issue under the 2026-11-15 research issue in project **`le31 v1 — Core MVP` (P-HMM-3)** (this is a v1 pick), label `Feature`, status `Done`. **The workspace contains only three projects — `le31 v1 — Core MVP`, `le31 Workflow`, `le31 Research` — so `le31 v2 owner-pains` and `le31 v2-AI` do not exist and must not be invented.** The parent research issue lives in `le31 Research` (P-HMM-1), and the fallback payload records both.

**Linear writes are blocked** (HTTP 400 `invalid_request` — *"You've exceeded the free issue limit for this workspace"*, requestId `a5ac4876ca6bdbbd`; 59th consecutive day). Use the fallback payload in `/opt/data/le31-daily-research-2026-11-15.linear-fallback.json` and record `linear: blocked`. **Do not claim an issue ID that was not returned by Linear.**

**Why this pick is not a duplicate:** features **480** (line 226) and **481** (line 243) both record this defect verbatim and both defer it — 480 to *"the amount question to 465's"* and 481 to *"the label question is adjacent to 460's territory"*. **Feature 465 owns the float arithmetic and feature 460 owns the table's free-text area** (a corpus grep for `subtotal`/`tax`/`floor card`/`amount` in 460 returns **zero hits**). **Neither owns this, so the deferral left a gap rather than a decision.**
