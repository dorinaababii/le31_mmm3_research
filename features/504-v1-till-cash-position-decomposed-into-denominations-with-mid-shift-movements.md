# Feature 504 — `v1-till-cash-position-decomposed-into-denominations-with-mid-shift-movements`

> **Pick A of Daily Research 2026-11-20.** **Bucket: v1.** **Verdict: `defer` — parking-lot vocabulary reference.**
>
> **Source artifact:** `kodlyft/xpos` — MIT, ★55 / ⑂47, TypeScript/Vue on Frappe+ERPNext, created 2026-02-26, pushed 2026-11-19T15:55:22Z, 9,504 KB, `default_branch=develop`, `archived=False`. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-20/gh/repo_36_kodlyft_xpos.json`; README (base64-decoded): `/tmp/le31-daily-2026-11-20/gh/readme_plain/plain_36_kodlyft_xpos.md`; source URL: https://github.com/kodlyft/xpos.
>
> **Why this pick:** one README states a till as a **counted position with a composition**, not as a number — *"Opening shift – Define opening balance with cash denomination breakdown"* — and gives the till **two named outbound movements that happen before the close**: *"Cash expenses – Record till expenses with GL account allocation"* and *"Cash deposits – Move cash from till to bank/safe accounts mid-shift"*. LE31 owns the *variance number* (feature 391) and the *close transition* (feature 426); **neither owns what the counted position is made of, nor the two mid-shift movements that change what the close must reconcile against.**
>
> **Why it is net-new:** the parent ran a targeted dedup sweep across all **1,034 feature and spec files** in the repository before selecting this pick: `denomination` → **0 files**; `cash deposit|bank drop|till to (bank|safe)` → **0 files**; `till expense` → **0 files**; `opening balance.{0,60}(breakdown|denomination|note)` → **0 files**; `cash movement` → 6 hits across 4 files, none of which is a till (feature 393 is a .NET cash-register vocabulary reference; features 391 and 426 are LE31's own shift-variance and shift-close contracts); `gift card` → 36 hits in 4 files, feature 18 owning gift cards as stored value — a different concern. **The word *denomination* appears nowhere in the corpus.** That is the strongest single piece of net-newness evidence in this pass.
>
> **Boundary with feature 391 (`le31-shift-variance-stored-no-derivation-no-payment-table`):** 391 owns **the variance number** — the difference between expected and counted at close. This pick owns **what the counted position is made of** (denominations), **what the opening position was declared to be**, and **the two mid-shift outbound movements** that happen *before* close. They are complementary: 391 needs a counted quantity to compare against; this pick specifies what that quantity is made of.
>
> **Boundary with feature 426 (`le31-shift-close-lifecycle`):** 426 owns **the close transition itself**. This pick owns **the state the close reconciles against** — a till whose cash has been deposited to the safe and had expenses taken out is not the till that was opened. Building this before 391 or 426 lands would create a third shift-family concept with no host.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **till cash position** as the reference design for any future LE31 cash-management surface:

1. the till's position is **declared at open** — not derived, but stated, as a **breakdown into denominations**;
2. the close reconciles **all payment modes** against a **tax collection summary**, not against one total;
3. the till has **two named outbound movements that occur mid-shift**, before the close:
   - a **cash deposit** — cash moves from the till to a bank/safe account,
   - a **cash expense** — cash leaves the till and is allocated to an account;
4. both movements are **first-class records**, not edits to a balance;
5. the closing reconciliation therefore runs against a position that **has been changed since it was opened**, and the variance (feature 391) is the difference after those changes.

No denomination schema, no till model, no movement ledger and no variance derivation is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the five-point mechanism summary above.
- The dedup result that establishes the mechanism is net-new to the corpus (`denomination` → 0 files).
- The explicit boundary with feature 391 (the variance number) and feature 426 (the close transition).
- The load-bearing sentence of the design, stated once: **the till's counted position is a decomposition into denominations, and the close reconciles a position that mid-shift movements have already changed.**
- The ordering constraint that this pick must follow features 391 and 426 rather than precede them.
- A future-project attachment decision: `le31 Research`, because the two host features are parked and no shift-family project exists.

## Out of scope

- No denomination model, no till model, no cash-movement ledger, no schema change.
- No change to the waiter web UI, the cook Telegram bot, the `StockEntry` ledger, or the bill lifecycle.
- No change to how the shift close is triggered or recorded — feature 426 owns that.
- No change to how the shift variance is derived — feature 391 owns that.
- No adoption of the TypeScript/Vue/Frappe/ERPNext stack.
- **No implementation of cash deposits or cash expenses.** The source's "GL account allocation" is a finance-system concept LE31 does not have; the transferable part is the *existence and naming of the two movements*, not the accounting.
- No customer-facing or public surface. A till is an operator surface.
- **No resolution of whether LE31 needs cash management at all** for a single-operator restaurant. That is a charter question and this contract does not answer it.

## Description

The source artifact's README states the shift and cash family in four consecutive bullets, verbatim:

> *"**Opening shift** – Define opening balance with cash denomination breakdown"*
> *"**Closing shift** – Reconcile all payment modes with tax collection summary"*
> *"**Cash expenses** – Record till expenses with GL account allocation"*
> *"**Cash deposits** – Move cash from till to bank/safe accounts mid-shift"*

**1. The position has a composition.** A denomination breakdown is not a nicer way to write a number — it is a *different kind of statement*. A number says "there are 200 euros in the till". A breakdown says "there are 2×€100, 4×€20, and 30×€0.50 in the till". The second is what makes a count **checkable**: a discrepancy of €7.50 is not a mystery, it is "someone took a €5 and two €1 coins", and it tells the owner what to look for. LE31's feature 391 records that the shift variance is *stored without a derivation*; a variance without a composition is a number nobody can act on.

**2. The position is declared, not derived.** "Define opening balance" — the opening is an **input the operator states**, not a value the system computes. This matters for the charter's explicit-state principle: the operator declares what the till held at 09:00, and the system does not guess.

**3. There are two outbound movements, and they are different.** A **cash deposit** moves money *from the till to a bank or safe account* — the money still belongs to the restaurant, but it is no longer in the till. A **cash expense** moves money *out of the till entirely* — for bread, for the bus, for a tip envelope. These are not the same event and they do not have the same effect on the close. Only the first changes *where* the cash is; only the second changes *how much* the restaurant has. Collapsing them into one "cash out" would lose exactly the distinction an owner needs at close.

**4. The close reconciles a changed position.** Because both movements happen **mid-shift** — the source says so explicitly — the closing reconciliation is not "open minus sales". It is "open, plus what came in, minus what went to the safe, minus what was spent, versus what is counted". This is the sentence that makes the design load-bearing.

**What LE31 does not have.** Feature 391 owns the *variance*; feature 426 owns the *close*. Neither owns the *composition of the counted position* nor the *named mid-shift movements*. This pick is about the two things that sit between the open and the close and currently have no owner.

**Why the source's own limits are recorded rather than hidden.** The README does not specify the denomination set, whether denominations are a fixed enum or free-form, how the closing count is entered, or how a deposit interacts with the reconciliation. So this contract records a **shape**, not a copyable design. A future implementation would have to specify all four, and this contract is honest that they are unspecified.

**Adjacent but not owned.** The same README also ships *"Return mode – Process returns linked to original invoices with automatic credit notes"*, *"Customer credit – Auto-detect unallocated advances and credit notes at checkout"* and *"Draft invoices – Save, retrieve, and manage multiple open orders per session"* — the last two are **feature 506**, a separate pick with its own contract, not bundled here. *"Stock receiving – Goods receipt workflow with PO matching and variance handling"* is **feature 489**'s mechanism. *"Gift cards – Sell stored-value cards anyone can spend in parts, with a liability ledger reconciled to the GL"* is a stored-value concern owned by feature 18, not a till concern. None of these is bundled.

## Data model

**None is created by this feature.** The following is a *reference shape* recorded for a future implementation, and it is deliberately not a schema:

```
CashPosition (declared at shift open)
  shift_id          the shift this position belongs to
  declared_by       who declared it
  declared_at       when it was declared
  denominations    the breakdown: denomination -> count of notes/coins

CashMovement (the two outbound movements)
  movement_id       opaque identifier
  shift_id          the shift it belongs to
  movement_type     'cash_deposit' | 'cash_expense'
  amount            exact EUR value, minor units, never a float
  occurred_at       timezone-aware instant
  destination       where the cash went (safe/bank for a deposit; a note for an expense)
```

**The load-bearing sentence, stated once, as the contract's design:** *the counted position at close is compared against a position that has been adjusted by every mid-shift movement; a movement is a new record and never an edit to the declared position or to a running balance.*

**The reference shape is deliberately incomplete**, and the gaps are named rather than guessed: the **denomination set** (a fixed euro enum, or free-form per site) is unspecified; the **closing count entry surface** is unspecified; the **allocation of an expense to an account** is unspecified — LE31 has no general ledger, so "GL account allocation" has no LE31 equivalent and the source's version of it is explicitly *not* transferred; and whether a **deposit is a till-out or a transfer between two cash locations** is unspecified. An implementer must decide all four and record the decision. A contract that guessed them would be worse than one that names them.

## Implementation

**No implementation is authorised by this feature.** It is a `defer` reference.

If a future feature is separately approved, the plausible touch points would be:

- `backend/app/models.py` — future `CashPosition` and `CashMovement` models;
- `backend/app/services/cash.py` — future derivation of the expected close position from the declared position plus the movements;
- `backend/app/routers/shifts.py` — future shift-open declaration and movement-recording routes;
- the waiter web UI — future shift-open denomination entry and cash-movement capture;
- tests — declared position is never edited; a movement never updates a balance; close reconciles against the adjusted position; a duplicate movement is rejected.

**Ordering constraint (not optional).** A future implementation must land **after** feature 391 (`le31-shift-variance-stored-no-derivation-no-payment-table`) and **after** feature 426 (`le31-shift-close-lifecycle`). Both were filed 2026-11-15/2026-11-16 and are still parked. Starting a third shift-family slice before either of its two predecessors moves is scope accumulation without appetite.

## Telegram interaction

**None.** The cook Telegram bot is not a consumer of the till position in this disposition, and no bot command is added. The source has no cook-surface cash feature either — cash is a waiter/owner matter. A future "the till is at €X" bot command would need its own owner decision and its own chat-id allowlist treatment (feature 403).

## Dependencies

**Existing LE31 features this pick depends on or is adjacent to:**

- **Feature 391** (`le31-shift-variance-stored-no-derivation-no-payment-table`) — owns the variance number. **Prerequisite.** A denomination breakdown is what makes that number actionable.
- **Feature 426** (`le31-shift-close-lifecycle`) — owns the close transition. **Prerequisite.** The movements recorded here change what the close reconciles against.
- **Feature 5** (`payment-tip-reconciliation`) — the *payment modes* half of the closing reconciliation. **Adjacent.** The source reconciles "all payment modes"; this pick owns only the cash position's composition, not the card/mobile money modes.
- **Feature 403** (`role-carrying-bot-chat-table`) — an actor is needed for "who declared the opening balance". **Adjacent.**
- **Feature 496** (`audit-ready-daily-export-with-financial-reconciliation-identities`) — a declared position and its movements are facts an export may need to state. **Adjacent, and deliberately not bundled.**
- **Feature 18** (`gift-cards`) — stored value, a liability position. **Adjacent, explicitly not bundled.**

**External dependency:** none. The source artifact is a MIT-licensed reference, not a code dependency; nothing is imported.

## Open questions

1. **Does a single-operator restaurant need denominations at all?** The owner counts one till. A denomination breakdown earns its keep when a discrepancy must be explained; if the owner never investigates a discrepancy, this is ceremony. This is the question that decides whether the pick ever leaves the parking lot.
2. **What is the denomination set** — a fixed euro enum, or free-form per site? A free-form set makes counting faster and reconciliation harder.
3. **How is the closing count entered?** A denomination breakdown at close, or only a total with an optional breakdown when there is a discrepancy? The second is much cheaper and covers most nights.
4. **Is a cash deposit a till-out or a transfer between two cash locations?** LE31 has no second cash location today. If the answer is "a safe", LE31 needs a second location concept; if it is "the bank", the movement leaves the restaurant's cash entirely and the treatment differs.
5. **What replaces "GL account allocation" for an expense?** LE31 has no general ledger. An expense needs a reason (feature 432's `StockReason` sign-coherence family is the nearest existing vocabulary), not an account.
6. **Does the cook bot need to see till movements?** If the till runs low mid-shift, that is a different question from who declared the opening balance, and the charter forbids silently acting on operational state.

## Why this matters

LE31's existing shift features record a **number** — the variance — and a **transition** — the close. Neither records **what was counted** or **what left the till in the middle of the service**. That gap is exactly where restaurant cash goes missing: a €50 that went to the safe at 21:00 and a €12 of bread bought at 19:30 are indistinguishable in a system that only remembers "expected vs counted at close".

The value of recording this now, while it is still a `defer`, is that the **composition-and-movement model is cheap to get right on paper and expensive to get wrong in code**. A till model that stores a mutable balance instead of appending movements is the same defect class the charter already forbids for `StockEntry`; a till model that computes its expected close without subtracting the deposits and expenses will report a variance that is real but misattributed, and the owner will spend the evening looking for a €300 discrepancy that is actually a safe deposit they forgot to record.

Two things this contract deliberately refuses to do. It does not start a shift-family slice ahead of features 391 and 426, because a third concept in the same family with no host is scope, not progress. And it does not pretend the source's design is more specified than it is: the denomination set, the count-entry surface, the deposit's semantics and the expense's allocation are all named as open questions rather than invented.

The honest summary is that LE31 does not need till denominations today, may never need them for a one-operator restaurant, and will need them the moment the owner starts investigating a discrepancy. The vocabulary is cheap to hold and expensive to rediscover.
