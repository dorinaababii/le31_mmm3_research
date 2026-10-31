# Feature 401 — `bzubairy/home-kitchen-pos`: **"low-stock warnings that count what pending orders still need"** — the pending-order reservation, the third artifact in three passes to name it (defer)

> **NEW observation (2026-10-29, parent-verified).** Documents in-window GitHub repo `bzubairy/home-kitchen-pos` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★0/⑂0**, **1,231 KB**, **TypeScript ✗ off-stack** — Next.js + Supabase + Vercel, `archived=false`, `fork=false`, created **2026-10-28** AND pushed **2026-10-28** = **in-window by both `created_at` and `pushed_at`**). All fields parent-verified via a **direct `GET /repos/`** on 2026-10-29 (`/tmp/le31-daily-2026-10-29/parent/bzubairy__home-kitchen-pos__repo.json`), **never from search-result numbers**. README read in full by the parent (`/tmp/le31-daily-2026-10-29/parent/bzubairy__home-kitchen-pos__README.md`, 10,826 bytes; repo tree 123 files). Description (verbatim from the GitHub API): *"Free, phone-first POS for small home food businesses: orders, recipe-based stock, expenses, profit."*
>
> **Why this artifact and not another.** Its README states the whole idea in **one line** — and that line names the exact quantity LE31 cannot express. Verbatim:
>
> > *"**Automatic stock:** recipes per menu item, so delivering an order deducts its ingredients and packaging"*
> > *"**low-stock warnings that count what pending orders still need**"*
> > *"**stock history for every ingredient**"*
> > *"**Orders:** one-tap order entry with live totals; statuses: New → Pending → Preparing → Delivered"*
> > *"**Restocking and expenses:** restocking adds stock, updates the cost and records the expense in one step"*
>
> **⭐ This is the third artifact in three consecutive passes to name this quantity**, from three unrelated domains and three unrelated stacks:
> - 2026-10-27 — `hemeshwar09/StockGuard` (Python, FastAPI + PostgreSQL): the **guarded conditional transition** (`UPDATE ... WHERE status = 'ACTIVE'`) plus DB-level `CHECK` constraints that *"refuse to commit an oversold state"*.
> - 2026-10-28 — `fortikday/pantry-signal` (Python, MIT): the **three-quantity triad** — *"On hand"*, *"Reserved"*, *"Available"* — where *"Reserved: ingredients required by queued orders not yet prepared or cancelled"*.
> - 2026-10-29 — `bzubairy/home-kitchen-pos` (TypeScript, Supabase): the **pending-order reservation as a product rule** — a stock warning that *subtracts what queued orders will consume*.
>
> **The first-party gap, parent-verified against LE31's own code.** `backend/app/models.py`:
> - `Batch.qty_remaining: int` (line 106) — a **single stored number**.
> - `StockEntry` (lines 113–126) — `qty_delta`, `reason`, `ref_order_item_id`, `by_user_id`, `at: datetime`. **`at` is a wall-clock timestamp, not a monotonic event cursor.**
> - `StockReason` (lines 54–60) — `initial`, `sale`, `waste`, `restock`, `sold_out`. **No `reserve`, no `release`.**
> - `grep -rn -i "reserved\|available\|on_hand" backend/app/` → **no output** (the only match is `__tablename__ = "table_"`).
> - `grep -rn "CHECK\|check_constraint\|Constraint" backend/` → **no output**.
>
> Bucket: **v1 (vocabulary only, parking-lot defer)** — Pick B of Daily Research 2026-10-29. Build verdict: **`defer`** (vocabulary-only; **no code is adopted** — this is a two-person home kitchen in Pakistan using WhatsApp/Foodpanda intake and Supabase; LE31 is one restaurant with a waiter web UI, a cook Telegram bot and a `Decimal` EUR ledger).

## Goal

Retain, as a **written, quotable reference**, the **pending-order reservation rule**, and record the **one decision** it forces on LE31:

> **Is "committed" a stored number or a derivation?**

Under LE31's §3.3 (*"every prepared-item quantity change is a new `StockEntry` … current stock is derived from entries"*), the answer **must** be *a derivation* — and that is the whole point of recording this artifact, because **the artifact itself stores a balance**. LE31's rule and the artifact's implementation point in opposite directions, and **only the rule transfers**.

The concrete deliverable is a written statement of the derivation:

> **Available = (derived on-hand from `StockEntry`) − (quantity that open `OrderItem`s will consume)**

…together with the **vocabulary** the artifact supplies for it (*pending*, *reserved*, *committed*, *available*), and the statement that **"committed" is computed over `StockEntry` + open `OrderItem`s, never stored as a column.**

**No code today.** This feature is a **written record** plus **one named decision**. It changes **zero lines** of `backend/app/models.py`.

## Scope

**In scope (defer artifact):**

- A written record of the **pending-order reservation rule**, with the verbatim README quotes above.
- A written record of the **derivation** (on-hand minus open-order consumption) as the LE31-compatible form of the rule, and the explicit statement that **it is a view/derivation, not a column**.
- A written record of the **vocabulary** the artifact supplies — *pending order*, *committed*, *available* — and the decision to use **"committed"** rather than "reserved" in LE31's vocabulary (with the reason: *reserved* collides with the 2026-10-28 `pantry-signal` triad's own "Reserved" concept, which was a *quantity*, while "committed" is unambiguously a *relation between an order and stock*).
- A written record of the **`recipes per menu item` → `deducts its ingredients`** rule as the **explosion** step that turns a menu-item sale into ingredient-level `StockEntry` rows.

**Out of scope (defer artifact):**

- **Any code, table, column, endpoint, view, or bot command.** This feature changes **zero lines** of `backend/app/models.py` and **zero lines** of the backend.
- **Any adoption of the `home-kitchen-pos` codebase**, its Supabase schema, its WhatsApp/Foodpanda/Instagram intake channels, its customer website and checkout, its PWA packaging, its receipt-image sharing, or its customer-record model. **The transferable thing is the rule, not the app.**
- **Any adoption of its storage model.** The artifact keeps *"stock history for every ingredient"* alongside a current balance — a **stored-balance** model that **violates LE31's §3.3**. **This is the single most important thing this feature does *not* adopt.**
- **The `MenuItem` availability / sold-out state** — feature **397** owns it.
- **The non-prepared-item sale path** — feature **398** owns it.
- **Recipe explosion into `StockEntry` rows** — features **03**, **15** and **385** own the ingredient model; this artifact is a *reference for the rule*, not a proposal for the schema.
- **A new Linear sub-issue in `le31 v2 owner-pains` or `le31 v2-AI`** — those projects **do not exist**; per `le31-feature-pipeline/SKILL.md` line 33 the sub-issue attaches to **`le31 Research`** (P-HMM-1).
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### What the artifact is

A **free, phone-first POS for a two-person home food business**, installed as an installable web app on iPhone and Android, with a separate customer ordering website. Everything runs on free tiers (Supabase + Vercel) with *"no app store and no monthly fees"*. Its README documents a real deployment — *"Built for a two-person home kitchen in Pakistan"* — with blurred screenshots of *"Messy Bitess"*, the actual kitchen it was built for.

Its order model is a **four-state ladder**: *"statuses: New → Pending → Preparing → Delivered"*. The stock model is **recipe-driven**: every menu item has a recipe, and delivering an order deducts the ingredient quantities the recipe implies.

### The one rule that matters

> *"low-stock warnings that **count what pending orders still need**"*

This is the artifact's entire stock-reservation contribution, and it is stated as a **product rule about a warning**, not as a storage decision. The owner does not need a "reserved" column; they need the **warning to not lie**. If three tiramisu are pending and five are on hand, the honest answer to "how much can I still sell?" is **two**, not five.

That is precisely the distinction LE31's single `Batch.qty_remaining` cannot express — and precisely the distinction the 2026-10-28 `pantry-signal` triad named with *"Reserved: ingredients required by queued orders not yet prepared or cancelled"*.

### ⭐ The divergence that must be recorded, not copied

The artifact's implementation is **not** §3.3-compatible:

| | `bzubairy/home-kitchen-pos` | LE31 §3.3 |
|---|---|---|
| Current stock | a **stored balance** per ingredient | **derived** from `StockEntry` rows |
| History | *"stock history for every ingredient"* — a separate table | the `StockEntry` ledger **is** the history |
| Restock | *"restocking adds stock, updates the cost and records the expense in one step"* | a **new `StockEntry`** with `reason=restock`; the balance is derived |
| Consumption | *"delivering an order deducts its ingredients and packaging"* | a **new `StockEntry`** per ingredient, `qty_delta` negative, `reason=sale` |

**LE31's model is stricter, and the artifact's rule survives that strictness** — because *"count what pending orders still need"* is a **derivation over `StockEntry` plus open `OrderItem`s**, not a stored column. The rule is *more* compatible with §3.3 than the artifact's implementation is. **That asymmetry is the reason this feature exists as a vocabulary record rather than a template.**

### The vocabulary this contributes

One term and one derivation:

- **Committed** — the quantity that open (not-yet-served, not-yet-cancelled) `OrderItem`s will consume, computed by exploding their recipes to ingredients.
- **Available** — on-hand minus committed. **A derived quantity, never a column.**

And a supporting concept:

- **Recipe explosion** — a menu-item sale becomes N ingredient-level `StockEntry` rows, one per ingredient, each with the same `ref_order_item_id`. **This is what makes the derivation possible at all** — you cannot compute "what pending orders need" without knowing how a menu item maps to ingredients.

### What the artifact does *not* settle

The artifact does not say what happens when a pending order is **cancelled** — does the commitment disappear, or must it be released by a compensating entry? Under LE31's §3.3 the answer would be **a new `StockEntry`**, but LE31's `StockReason` has no `reserve`/`release` member, so the *shape* of that release is undecided here (see feature **400**, which records the parallel reversal question).

## Data model

**No schema change today.** This feature records the vocabulary; it does not add columns.

The derivation, stated so it can be implemented later without re-deriving it:

```
on_hand(batch)      = SUM(StockEntry.qty_delta WHERE batch_id = B)      -- per §3.3
committed(batch)    = Σ over open OrderItems of qty(recipe explosion)     -- derived, not stored
available(batch)    = on_hand(batch) − committed(batch)
```

Two things this makes explicit:

1. **`Batch.qty_remaining` is redundant** if `available` is computed — which is a **further argument for feature 374** (stored-vs-derived). This artifact is *evidence for 374*, not a rival to it.
2. **"Committed" requires a recipe→ingredient mapping to exist.** LE31's `MenuItem` has `is_prepared: bool = True` (line 92) and `Batch` exists per prepared item (line 96) — so the mapping is *partially* present for prepared items. **The unprepared path is feature 398's business.**

## Implementation steps

**None.** This is a `defer` artifact — vocabulary and one decision only. If the owner promotes it, the implementation belongs to the features that own the work:

- The **derivation** (on-hand / committed / available) → **feature 374** (`qty_remaining` stored-vs-derived) and **feature 385** (batch provenance).
- The **recipe explosion** into ingredient-level `StockEntry` rows → features **03**, **15**, **385**.
- The **`reserved`/`release` `StockReason` members** → the feature that first writes a cancellation path (features **03**, **09**, **15**, **17**, **30**, **45**).

## Telegram interaction if any

**None today.** The artifact's order ladder is `New → Pending → Preparing → Delivered`; LE31's `ItemStatus` (`backend/app/models.py` lines 35–40) is `new`, `preparing`, `ready`, `served`, `cancelled` — **the same five concepts, different names**, and LE31's names are already right for a kitchen that *prepares* rather than *delivers*. The one thing the artifact contributes that LE31's cook bot does **not** have is the **warning**: *"low-stock warnings that count what pending orders still need"* is a **notification to the cook**, and LE31's two surfaces (waiter web UI, cook Telegram bot) have **no notification surface at all** — features **90**/**94** already track Telegram-reminder peers. **Recorded, not proposed.**

## Dependencies

- **Feature 374** — `qty_remaining` stored-vs-derived (owns the stored-number decision).
- **Feature 382** — stock-deduction idempotency + shortfall (owns the write-path correctness).
- **Feature 385** — batch provenance (owns the recipe→ingredient mapping).
- **Feature 397** — menu availability / sold-out state (a *different* concept from *committed*: a sold-out item is unavailable **now**, a committed item is unavailable **because of a queued order**).
- **Feature 398** — non-prepared-item sale semantics (the unprepared path has no recipe to explode).
- **Feature 400** — the same window's parallel artifact (records the idempotency key and the reversal event).
- **Charter §3.3** (append-only stock ledger) — `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.

## Open questions

1. **Is "committed" computed over `OrderItem`s in `ItemStatus` states `new`/`preparing`/`ready`, or only `new`?** An item that is `ready` has (presumably) already had its ingredients deducted — so committing only for `new`/`preparing` may be the correct rule, but **LE31 has no write site for `OrderItem.status` today**, so the rule cannot be pinned down against real behaviour.
2. **When is the deduction written — at order entry, at fire, at prepare, or at serve?** The artifact deducts at *"delivering"*. LE31's §3.2 surfaces imply the cook bot fires the item. **The deduction point determines the meaning of "committed" and is undecided.**
3. **Does a cancelled `OrderItem` release its commitment automatically, or by a compensating `StockEntry`?** §3.3 says the latter, but the `StockReason` member does not exist (see feature **400**).
4. **Is `available` exposed anywhere, or only used inside the low-stock warning?** If it is only used in a warning, it may not need a persisted form at all — a **query-time derivation** may be sufficient. **Undecided.**
5. **Does the artifact's *"stock history for every ingredient"* suggest anything LE31 should keep?** LE31's `StockEntry` **is** the history. **The answer is "no"** — and recording that no is the point of this feature.

## Why this matters

Three consecutive daily-research passes have produced three independent artifacts — from a stock-service (Python/FastAPI/Postgres), a local restaurant prototype (Python/MIT), and a home-kitchen POS (TypeScript/Supabase) — that all converge on the same missing quantity: **what is committed but not yet consumed**. That is no longer a coincidence, and it is now the **third** consecutive pass in which the same gap appears. LE31's `Batch.qty_remaining` is a **single stored number** that cannot express it, and LE31's `StockReason` has no member that means *"held for an order"*.

This matters **now** because LE31's backend is a **483-LOC skeleton with 3 routes**, and no feature has yet written a `StockEntry`. The order-status ladder, the recipe explosion, and the commitment release all have to be decided **together** by whoever writes the first stock write site, and each is cheap to decide now and expensive to change later.
