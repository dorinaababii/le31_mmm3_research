# Feature 390 — `Pantry`'s recipe-consumption snapshot: the order line records what was deducted, not what the recipe says today

> **Pick C of Daily Research 2026-10-27 (89th pass).** Documents in-window GitHub repo `bhargavkalita47/Pantry` (**licence `null` → §3.2 STRICTLY-INCOMPATIBLE — the *vocabulary-shape* is transferable, the *code-shape* is NOT adopted**), **★0/⑂0 — no traction evidence in either direction**, **53 KB**, JavaScript / Node 24 ✗ off-stack, created **2026-10-26T10:23:50Z AND pushed 2026-10-26T12:30:38Z = IN-WINDOW BY BOTH FIELDS** (a **same-day** repo), 1 topic `['inventory-management']`, `default_branch=main`, `archived=false`, `fork=false`, 0 open issues. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-27, not from search-result numbers. Description (verbatim from GitHub API): *"Recipe-based restaurant inventory: ingredient tracking, menu recipes, automatic order deductions and a stock ledger. SQLite locally, with an optional hosted backend."*
>
> **The README was read** (parent, 2026-10-27, `/tmp/le31-daily-2026-10-27/gh/readmes/bhargavkalita47__Pantry.md`). Two claims are recorded below: *"Orders retain recipe-consumption snapshots, so later recipe edits do not change cancellation quantities."* and *"Operation IDs prevent duplicate deductions when retrying a request."*
>
> Bucket: **v1**. Verdict: **`defer`** — vocabulary only, and **blocked behind feature 359**.

## Goal

Record in LE31's vocabulary the distinction between **what was deducted at the time of a sale** and **what the recipe says today** — a distinction LE31 does not currently have, because LE31 does not yet have recipes at all.

The concrete outcome: **one sentence in the feature tree stating that an order line must record the quantities actually deducted, not a live reference to the current recipe.**

## Scope

**In scope (v1):**

- **One document** recording `Pantry`'s two engineering decisions verbatim, with source URL, and the LE31-side vocabulary each one names.
- **An explicit statement of the dependency**: this pick is **blocked behind feature 359** (recipe-linked depletion), because LE31 has **no recipe or ingredient concept at all** today.
- **An explicit statement that this is not a duplicate of feature 359** — and the grep that proves it.

**Explicitly NOT in scope:**

- **Any `Recipe`, `RecipeComponent`, `Ingredient` or `Depletion` model.** Feature 359's subject, and 359 is itself an `experiment`.
- **Any schema, code or dependency change.** This feature changes **no file in `backend/`.**
- **Any change to `MenuItem`.** `MenuItem` (models.py line 84) has no recipe link and this pick does not add one.
- **Any cancellation, void, comp or refund flow.** The pick names the *problem* a snapshot would solve; it does not build the cancellation that would need to consume it.
- **Adopting `Pantry`'s code.** Licence `null` — §3.2 strictly-incompatible. The transferable item is a **sentence**, not a module.

## Description

### What `Pantry` actually is

A **recipe-based inventory and ordering** app for restaurants and cafés: *"Connect each menu item to its ingredients. Confirming an order deducts the combined quantities, blocks shortages and records stock movements. For example, three lattes consume 54 g of coffee and 600 ml of milk."* It runs three ways — a browser-local demo (one sample café per visitor), local development (SQLite, one restaurant on one machine) and an optional hosted workspace (server API + Supabase). It requires Node.js 24. The source lives in a `Pantry_GitHub_Source/` subdirectory.

**There is no traction claim here and none is made.** ★0, 0 open issues, a single topic, a same-day repository.

### The two claims worth taking

**Claim 1 — the snapshot (the reason this pick exists).**

> *"Orders retain recipe-consumption snapshots, so later recipe edits do not change cancellation quantities."*

Underneath it, in the same Engineering-decisions section:

> *"SQLite and cloud modes use revision-guarded writes to commit inventory, orders and movements together. Operation IDs prevent duplicate deductions when retrying a request. **Orders retain recipe-consumption snapshots, so later recipe edits do not change cancellation quantities.** Stock and money use integer units."*

Read precisely, this is a **point-in-time** claim: the order line stores **the quantities that were actually deducted**, and the recipe is a **live document that may change afterwards**. The two are different things, and conflating them means a cancellation computed "from the current recipe" reverses a *different* set of quantities than the sale deducted.

**That is a second, independent instance of the exact shape LE31 is already bleeding on.** Feature 385 (`OrderItem.batch_id`) is the same class of defect: an event that should have been recorded as a *fact at the time* is instead reconstructible only from a *later-mutable source*. Feature 385's version is batch provenance; this is consumption provenance. **Both are "the event forgot to write down what it saw."**

**Claim 2 — the operation id (recorded, not the reason for the pick).**

> *"Operation IDs prevent duplicate deductions when retrying a request."*

This is the **third independent arrival** at the idempotency gap (after `dc-tech-inc/dotnet-pos-integration`'s ADR-0001 on 2026-10-26 and `adil-alzhan-dev/kumo-qr-ordering`'s *"each order carries a key"* in this window). It is recorded here as evidence for the **convergence**, and it is **not** filed as a feature — feature 382 owns the ledger-write idempotency rule, and feature 388 owns the order-state validation rule. **Three arrivals, three passes, one agreed hazard: a retried state-changing request must not create a second state.** The convergence is the finding; the pick is the snapshot.

### Why this is not a duplicate of feature 359

Feature 359 (`dollyzn/react-menu`, recipe-linked depletion) is the closest neighbour, and it was checked directly:

```
grep -n -i "snapshot\|cancel\|reverse\|restore\|revert" features/359-*.md
# -> NO OUTPUT
```

**Feature 359 specifies the depletion. It says nothing about what happens to an already-deducted order line when the recipe later changes.** The two features are adjacent, not overlapping: 359 answers *"what gets deducted when a line is confirmed?"*; this one answers *"what does the order line remember afterwards?"*

**And a second check was run, because "Pantry" appears in the feature tree and a false positive would have meant silently skipping a real pick.** The only match is **feature 370** (`jdmacleod/kitchen-erp`), and it is **incidental** — that feature concerns a *different project* whose **domain** is a household pantry (and it says so: *"its domain is a household pantry, not a restaurant floor"*). **It is not a prior `Pantry` pick.**

### Why LE31 cannot act on this yet

LE31 has **no recipe concept whatsoever**:

```
grep -rn -i "recipe\|ingredient\|bom" backend/app/
# -> NO OUTPUT
```

`MenuItem` (models.py line 84) declares `id, name, category, unit_price, unit, is_prepared, photo_url` — **no recipe link, no ingredient list**. `Batch` (line 96) is *"a concrete prepared quantity of a MenuItem for a specific day"* — a **prepared output**, not a **recipe**. Those are different concepts: LE31 tracks *what was made*, not *what it was made from*.

So the snapshot sentence has **no subject in LE31 yet**. It becomes meaningful only once feature 359 (or something like it) introduces recipe-linked depletion. **Filing a vocabulary note now is correct; filing a feature now would be premature.**

## Data model

**No data-model change. None.**

The *content* of the documentation is:

1. The snapshot sentence — *"the order line records the quantities actually deducted, not a live reference to the current recipe."*
2. The operation-id sentence — *"a retried deduction must not deduct twice."*
3. The dependency statement on feature 359, and the greps that establish it.
4. The point-in-time vocabulary: **recipe** (mutable, live) vs **consumption** (immutable, recorded).

**If and when feature 359 lands**, the shape this pick anticipates is: the depletion record carries the *quantities*, and those quantities are **copied onto the order line** (or the depletion is referenced immutably) — so a later recipe edit cannot change them. **This pick does not specify that shape in detail** — feature 359's contract should, and this note is the reminder.

## Implementation steps

1. **`features/390-…md`** — this file. It is the deliverable.
2. **Do not** add a `docs/` folder, a `research/` entry, or a `PROJECT_CHARTER.md` edit for this feature. The mapping lives here, in the feature tree.
3. **Do not** create a `backend/` change of any kind. `git diff --stat backend/` must be **empty** after this feature.
4. **Do not** add `Pantry` as a dependency, a submodule, or a vendored directory. The repository is **read as a text**.
5. **Do not** edit feature 359. If feature 359's author wants to adopt the snapshot sentence, that is a change to 359, made by 359's owner, with its own review. **This feature points at 359; it does not edit 359.**

## Telegram interaction if any

**None.** No command, no message, no change to the cook bot.

## Dependencies

- **`features/359-dollyzn-react-menu-…`** — **the hard dependency.** This pick is blocked behind it. 359 is an `experiment`, not a build.
- `features/385-le31-order-item-batch-provenance-…` — **the sibling finding.** Same class: an event that must write down what it saw. Read it — the framing transfers, the domain does not.
- `features/382-dc-tech-inc-dotnet-pos-integration-…` — the ledger-write idempotency rule; the reason `Pantry`'s operation-id claim is recorded and **not** filed.
- `features/388-le31-table-state-machine-first-party-…` — the order-state validation rule; the third leg of the convergence.
- `PROJECT_CHARTER.md` §3.3 — stock is **derived** from ledger entries, never stored. A snapshot is *how the derivation inputs stay true over time*.
- `PROJECT_CHARTER.md` §3.6 — exact EUR arithmetic and integer quantities; `Pantry`'s *"Stock and money use integer units"* is the same commitment from another direction.
- `PROJECT_CHARTER.md` §3.2 — the non-goals that keep this pick small (no procurement, no cost accounting, no per-item modifiers).

## Open questions

1. **Where does the snapshot live — on the order line, or on the depletion record?** `Pantry` says *"orders retain recipe-consumption snapshots"* — on the order. But LE31's §3.3 model derives everything from `StockEntry` rows, so a snapshot could equally be *implied* by the ledger entries that already exist. **Not decided here** — it is feature 359's decision, and it must be made there, not retrofitted here.
2. **Is a snapshot needed at all if the depletion is already a ledger row?** If every deduction writes its own `StockEntry` with the quantities, then the "snapshot" may already exist implicitly — and the real gap would only be for ingredients that are **not** modelled as ledger entries (i.e. everything, today). **This question is why the pick is `defer` and not `build`: it is not yet known that a new concept is needed rather than an existing one being read correctly.**
3. **Should LE31 record a revision number on recipes?** `Pantry` mentions *"revision-guarded writes"* — a mechanism for concurrent recipe edits, not just a snapshot. **Out of scope**, and §3.2 keeps single-location single-chef operations simple. Recorded only.
4. **Does a cancellation flow exist in LE31 v1 at all?** Feature 05/14 (the bill) and a void/comp path are separate features. If there is no cancellation, there is no consumer for the snapshot, and the pick is even further from actionable. **Not verified this pass** — noted as an open question rather than asserted.

## Why this matters

**Because "the recipe today" and "what was actually deducted" are different facts, and LE31's own ledger rule means the difference compounds silently.**

§3.3 says stock is **derived** from ledger entries — never stored. That rule is right, and it is also what makes a snapshot necessary: if the derivation inputs are re-read from a mutable source at any later point, then the derivation is only as stable as the *most recently edited* recipe. A cook who corrects a recipe's quantity after service would, under a naive implementation, change what an earlier sale means.

**Nothing about that failure is visible.** The stock number would still be right (the ledger entries did not change); only the *meaning* of an old order line would drift, and only for orders that are later cancelled or reconciled. LE31 would have no way to detect it, because there is nothing to compare against — the snapshot would have to have been written at the time.

**The uncomfortable part is that LE31 has already been bitten by this shape once.** Feature 385 found that `OrderItem` records no batch provenance — the same "the event forgot to write down what it saw" shape, found a day ago, in the same class of field. **Two features in two passes about two different fields, one pattern.** The generalisation worth carrying forward: **any fact that an event observed at write time must be written down at write time, because every source it could later be reconstructed from is mutable.** That is a sentence worth LE31 having, and it is worth having *before* the recipe feature is built rather than after.

**Why `defer` rather than `build`.** Three reasons, and they are honest rather than diplomatic. **First**, the subject does not exist: LE31 has no recipe concept, so there is nothing to snapshot and no code to add. **Second**, the premise is unproven: if the depletion already writes one ledger row per deduction, the snapshot may be *implicit* and this pick would be recommending a concept that is not needed. **Third**, it is blocked behind feature 359, which is itself an `experiment` — stacking a vocabulary note on top of an experiment is how a chain of dependencies forms with nobody owning the root.

**Why it is filed at all, then.** Because the *pattern* is worth having in the vocabulary **before** the feature that would need it is written, and because it is the third independent arrival at the duplicate-event family — which, taken together with the other two, is the strongest convergence signal this research series has produced. Three strangers, three stacks, three countries, one hazard: **a retried or re-derived state change must not silently become a second state.** LE31 has now been told three times, from outside, by people who had to solve it to ship.
