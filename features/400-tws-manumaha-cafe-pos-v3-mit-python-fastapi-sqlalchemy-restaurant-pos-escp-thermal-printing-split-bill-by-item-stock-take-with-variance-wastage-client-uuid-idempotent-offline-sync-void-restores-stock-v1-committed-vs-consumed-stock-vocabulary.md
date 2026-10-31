# Feature 400 — `tws-manumaha/cafe-pos-v3`: the **client-minted idempotency key**, the **void-restores-stock** event, and the **counted-quantity stock take with variance** — LE31's "committed vs consumed" vocabulary (defer)

> **NEW observation (2026-10-29, parent-verified).** Documents in-window GitHub repo `tws-manumaha/cafe-pos-v3` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★0/⑂0**, **66 KB**, **Python ✓ + FastAPI ✓ + SQLAlchemy ✓ on-stack**, `default_branch=main`, `archived=false`, `fork=false`, created **2026-10-28** AND pushed **2026-10-28** = **in-window by both `created_at` and `pushed_at`**). All fields parent-verified via a **direct `GET /repos/`** on 2026-10-29 (`/tmp/le31-daily-2026-10-29/parent/tws-manumaha__cafe-pos-v3__repo.json`), **never from search-result numbers**. README read in full by the parent (`/tmp/le31-daily-2026-10-29/parent/tws-manumaha__cafe-pos-v3__README.md`, 4,938 bytes; repo tree 25 files, including `app/models.py`, `app/db.py`, `app/escpos.py`, `app/security.py`, `app/seed.py`). Description (verbatim from the GitHub API): *"Cafe POS v3 — restaurant POS with ESC/POS thermal printing, split-bill by item, stock take & wastage, client_uuid idempotent offline sync."*
>
> **Why this artifact and not another.** It is the only in-window artifact that puts the **deduplication key on the client** rather than on the server, and that pairs that key with a **void that restores stock** and a **counted-quantity stock take that records variance rather than overwriting the ledger**. Those three are exactly the three things LE31's `StockEntry` cannot currently express. The README's own wording (verbatim):
>
> > *"**Full offline sync** | ✅ Offline bills carry a `client_uuid`; server sync is idempotent (no duplicates)"*
> > *"**Voids & refunds with approval** | ✅ Manager/owner only; void restores stock and reverses loyalty points"*
> > *"**Stock take & wastage** | ✅ Counted-quantity stock take with variance, and a wastage entry screen"*
> > *"**Kitchen** — a KOT is created per order; kitchen board Pending → Preparing → Ready → Served; one-tap KOT printing."*
> > *"**Inventory** — live stock, reorder levels, Out / Reorder / Low / OK, automatic draw-down per sale, stock take with variance, wastage recording, suppliers and purchase orders."*
>
> **⭐ The first-party gap this names, parent-verified against LE31's own code.** `backend/app/models.py`:
> - `StockEntry` (lines 113–126) has `id`, `batch_id`, `qty_delta`, `reason`, `ref_order_item_id`, `by_user_id`, `at: datetime`. **There is no idempotency key of any kind.** `at` is a **wall-clock timestamp**, not a monotonic event cursor.
> - `StockReason` (lines 54–60) has exactly five members — `initial`, `sale`, `waste`, `restock`, `sold_out`. **There is no reversal/void member.**
> - `grep -rn "CHECK\|check_constraint\|Constraint" backend/` → **no output**.
> - `grep -rn -i "reserved\|available\|on_hand" backend/app/` → **no output** (the only match is `__tablename__ = "table_"`).
>
> Bucket: **v1 (vocabulary + one decision, parking-lot defer)** — Pick A of Daily Research 2026-10-29. Build verdict: **`defer`** (vocabulary-only; **no code is adopted** — this is a café POS for an Indian chain with GST invoicing, loyalty points, and multi-outlet support; LE31 is one restaurant with one location and a `Decimal` EUR ledger).

## Goal

Retain, as a **written, quotable reference**, the three parts of this artifact that name capabilities LE31's own data model does not have — and turn them into **three decisions** LE31 must make before the first `StockEntry` write site is written:

1. **The idempotency key and where it is minted.** The artifact's key is **client-minted** (`client_uuid`) and travels with the bill across an offline gap. LE31's two surfaces are a waiter web UI and a cook Telegram bot — **the bot has no client**, so LE31 must decide whether the key is minted *by the surface* (before the request leaves) or *by the server* (on receipt), and then **use one namespace for both surfaces**.
2. **The void/reversal event.** The artifact's void *"restores stock and reverses loyalty points"* as an **approval-gated operation**. LE31's §3.3 forbids restoring stock by updating `Batch.qty_remaining`; a void must therefore be a **new `StockEntry`** with a **new `StockReason` member**. The name of that member, and whether the void also reverses loyalty, are decisions LE31 has not made.
3. **The counted-quantity stock take with variance.** The artifact records a physical count **as a separate fact from the derived balance**, with the difference visible. LE31's `Batch.qty_remaining` is a **single stored number**; feature **374** already argues it should not be stored at all. This artifact adds the third question 374 has not asked: **what is the vocabulary for "the count disagreed with the ledger"?**

**No code today.** This feature is a **written record** plus **three named decisions**. It changes **zero lines** of `backend/app/models.py`.

## Scope

**In scope (defer artifact):**

- A written record of the **`client_uuid`** idempotency-key pattern, with the verbatim README quotes above and the **key-minting decision** stated as a question LE31 must answer before writing the first `StockEntry` write path.
- A written record of the **void-restores-stock** pattern, and the explicit statement that under LE31's §3.3 it must be a **new `StockEntry` with a new `StockReason`**, not an update to `Batch.qty_remaining`.
- A written record of the **counted-quantity stock take with variance** pattern — a physical count as a **separate fact** from the derived balance — and its relationship to feature **374**.
- A written record of the **kitchen board state ladder** (`Pending → Preparing → Ready → Served`) as an **external reference for feature 388 / `ItemStatus`**, noting that LE31's `ItemStatus` enum (`backend/app/models.py` lines 35–40) already has exactly these five values — so the artifact **confirms** LE31's enum rather than extending it.

**Out of scope (defer artifact):**

- **Any code, table, column, endpoint, or bot command.** This feature changes **zero lines** of `backend/app/models.py` and **zero lines** of the backend.
- **Any adoption of the `cafe-pos-v3` codebase**, its multi-DB driver switch (SQLite / PostgreSQL / Microsoft SQL Server), its ESC/POS implementation, its GST invoicing, its loyalty points, its multi-outlet support, its Nginx/Let's Encrypt deployment, or its webhooks. **The transferable thing is the event vocabulary, not the POS.**
- **The `OrderItem.status` state machine itself** — feature **388** owns that.
- **The stock-deduction idempotency feature itself** — feature **382** owns that. This feature **adds the key-minting decision to 382's scope**, it does not replace 382.
- **A new Linear sub-issue in `le31 v2 owner-pains` or `le31 v2-AI`** — those projects **do not exist** in the workspace; per `le31-feature-pipeline/SKILL.md` line 33 the sub-issue attaches to **`le31 Research`** (P-HMM-1).
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.
- **The ESC/POS receipt path** — recorded in the report as adjacent; feature **391** / the receipt peers own money rendering.

## Description

### What the artifact is

A **café and small-restaurant POS** written in Python, FastAPI and SQLAlchemy, with a plain-JS front end served by Nginx. Its README is a **feature checklist** with explicit ✅ marks against a roadmap table. The three rows quoted above are marked ✅ — that is, the author claims them as **implemented**, not aspirational.

The whole system is built around a **bill lifecycle** that can be created offline and reconciled later. That is why the idempotency key is client-side: the client must be able to create the same bill twice in a flaky-connection window and have the second attempt be a no-op. LE31 has a superficially similar problem — **the cook bot can receive the same order twice over Telegram** — and a structurally *different* solution would be needed, because the bot is not a client that can be handed a UUID by a browser.

### Why the three quoted rows are the transferable parts

| Artifact row | LE31's equivalent | LE31's gap |
|---|---|---|
| *"Offline bills carry a `client_uuid`; server sync is idempotent (no duplicates)"* | a Telegram message that the cook receives twice, or a waiter re-submitting after a timeout | `StockEntry` has **no idempotency key**. There is no `client_uuid`, no `external_id`, no unique constraint of any kind on the table. |
| *"Voids & refunds with approval ✅ Manager/owner only; void restores stock and reverses loyalty points"* | a waiter cancelling an order item after it was fired | `StockReason` has **no reversal member** (`initial`, `sale`, `waste`, `restock`, `sold_out` only). §3.3 forbids fixing this by updating `Batch.qty_remaining`; the *correct* fix is a new `StockEntry`, and the *reason* it would carry does not exist yet. |
| *"Stock take & wastage ✅ Counted-quantity stock take with variance"* | the owner counting the prep batch at the start of service | `Batch.qty_remaining` is a **single stored number** (line 106). There is no concept of a **counted quantity that disagrees with the ledger**. Feature **374** asks whether that number should be stored; this artifact adds the **third** question: what does the disagreement look like in the model? |

### The vocabulary this contributes

Three words LE31 does not currently have:

1. **Idempotency key** — a value supplied by the caller that makes a repeated write a no-op rather than a second event.
2. **Reversal** — an event that *undoes* a prior event's effect, recorded **as its own entry**, never as an edit of the original.
3. **Variance** — the difference between a **counted** quantity and the **derived** quantity, recorded as a finding rather than silently reconciled.

The third is the subtle one, and it connects to the adjacent `HIZMALI/MealLoopOS` artifact recorded in the report, whose Impact Ledger module distinguishes *"separate estimates/readings"* and *"immutable plans and append-only corrections"*. **A count that disagrees with the ledger is a reportable finding, not an error to abort on** — and LE31's `StockReason` has no member that means "we counted and found a difference".

### What the artifact does *not* settle

The README says the void is *"Manager/owner only"* — a **role** rule — but LE31's permission model is a JWT/PBKDF2 layer (`backend/app/security.py`) with **no row-level or storage-layer guard** (see feature **402** for the parallel artifact that *does* enforce below the UI). So even the **approval** half of the void rule is unresolved in LE31.

## Data model

**No schema change today.** This feature records the vocabulary; it does not add columns.

The three decisions, with the shape each would take **if and when** a build is approved:

1. **Idempotency key** — a new column on `StockEntry` (e.g. `idem_key: str | None`), **unique** where not null, with the uniqueness scope decided (per `StockEntry` row, or per logical event spanning rows). A `UniqueConstraint` **would be the first constraint of any kind in LE31's schema** — `grep -rn "Constraint" backend/` currently returns nothing — so this decision carries a precedent and should be recorded with it.
2. **Reversal reason** — a new member of the `StockReason` enum (`backend/app/models.py` lines 54–60). Under §3.3 this must be a **new `StockEntry`** with `qty_delta` mirroring the original entry's `qty_delta`, and `ref_order_item_id` pointing at the entry being reversed — the enum member is the only thing that does not yet exist.
3. **Variance** — a **counting** event. Under §3.3 it is also a `StockEntry` (a `StockReason` such as a count/correction member), and the *variance* itself is **derived** (counted minus derived), never stored as its own mutable number. This is the point where features **374**, **382** and this artifact meet.

## Implementation steps

**None.** This is a `defer` artifact — vocabulary and decisions only. If the LE31 owner promotes any of the three decisions to a build, the implementation steps belong to the feature that owns the work:

- Idempotency key → **feature 382** (stock-deduction idempotency + shortfall) — extend its scope with the key-minting decision.
- Reversal reason → the feature that first writes a void/cancel path (features **03**, **09**, **15**, **17**, **30**, **45** all plan to move items through `ItemStatus`).
- Variance → **feature 374** (`qty_remaining` stored-vs-derived), extended with the counted-vs-derived question.

## Telegram interaction if any

**None today.** The artifact's kitchen board (`Pending → Preparing → Ready → Served`) is **already** LE31's `ItemStatus` enum (`backend/app/models.py` lines 35–40: `new`, `preparing`, `ready`, `served`, `cancelled`) — the artifact **confirms** the enum rather than extending it. No new bot command is proposed.

## Dependencies

- **Feature 382** — stock-deduction idempotency + shortfall (owns the idempotency work).
- **Feature 374** — `qty_remaining` stored-vs-derived (owns the stored-number question).
- **Feature 388** — table state machine (owns `OrderItem.status`).
- **Feature 391** — shift payment link and cash-variance derivation (the *money* variance; this artifact's variance is the *stock* variance — **different quantities, do not conflate**).
- **Feature 402** — database-level permission enforcement (the approval half of the void rule).
- **Charter §3.3** (append-only stock ledger) and **§3.6** (exact EUR, never float) — `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.

## Open questions

1. **Where is the idempotency key minted?** Client-side (surface-generated before the request) or server-side (on receipt)? LE31's cook bot has no client, so "client-side" means *the bot generates it*, and both surfaces must share **one key namespace** or the same order submitted through two surfaces will not collide.
2. **Does the void reverse `OrderItem.status` as well as stock, and are those one transaction or two?** The artifact treats loyalty reversal as part of the same approval. LE31 has no loyalty system, so the scope is stock + item status only — **but the atomicity question stands**.
3. **Is a variance a `StockReason` member, or a separate entity?** A member is simpler and keeps §3.3 intact; a separate entity lets a count reference a specific `Batch` and carry the counted number. **Undecided.**
4. **Is the key scoped per `StockEntry` row, or per logical event?** A single logical deduction may span multiple `StockEntry` rows (one per ingredient). **Undecided, and it is the harder question.**
5. **Does LE31 ever accept a client-supplied key at all?** If the answer is no, the whole artifact is dropped and only the void/variance halves remain. **Undecided.**

## Why this matters

Three consecutive daily-research passes have now produced independent artifacts naming **the same missing quantity** — what is *committed* but not yet *consumed* (2026-10-27 `hemeshwar09/StockGuard`, 2026-10-28 `fortikday/pantry-signal`, 2026-10-29 `bzubairy/home-kitchen-pos`). This artifact is the **first of the three that names the ledger-side machinery** rather than the quantity itself: the key that makes a repeated write a no-op, the event that undoes a prior event, and the record that says *"we counted and it disagrees"*.

LE31's backend is a **483-LOC skeleton with 3 routes** (`/api/health`, `/`, `routers/tables.py`'s `GET /api/tables` and `POST /api/tables/{id}/seat`). Every P0 in the charter's acceptance table is **specified but not built**, and `OrderItem.status` and `StockEntry` both **have no write site yet**. **That is the cheapest possible moment to decide these three things** — a vocabulary decision now costs one paragraph, and the same decision after the first production write site costs a historical audit with no ground truth. Features 03, 09, 15, 17, 30 and 45 all plan to move items through `ItemStatus`, so the window is closing.
