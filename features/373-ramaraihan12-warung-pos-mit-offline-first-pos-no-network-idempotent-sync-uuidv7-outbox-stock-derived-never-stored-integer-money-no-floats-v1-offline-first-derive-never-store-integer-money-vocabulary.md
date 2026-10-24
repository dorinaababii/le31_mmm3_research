# Feature 373 — `ramaraihan12/warung-pos` offline-first POS: derive-never-store stock, integer money, idempotent outbox sync (defer)

> **NEW observation (2026-10-24).** Documents in-window GitHub repo `ramaraihan12/warung-pos` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★0/⑂0**, **575 KB**, **TypeScript ✗ OFF-STACK** (Next.js 16 / React 19 / Drizzle / Postgres 17 / Dexie — LE31 is FastAPI + SQLModel + SQLite/Postgres), created **2026-10-24T03:04:02Z AND pushed 2026-10-24T03:04:09Z = IN-WINDOW BY BOTH FIELDS**, `archived=false`, `fork=false`, 0 open issues, default_branch=`main`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-24, not from search-result numbers. Description (verbatim from GitHub API): *"Offline-first point of sale for a small shop: sells with no network, syncs idempotently when back online. Next.js, Drizzle, Postgres, Dexie"*. Bucket: **v1 (offline-first + derive-never-store + integer-money vocabulary)** — Pick A of Daily Brainstorm 2026-10-24. Build verdict: `defer` (parking-lot; **vocabulary reference only**).
>
> ⚠️ **THIS PICK IS THE ONE THAT FOUND A FIRST-PARTY DEFECT.** See **Feature 374** — this repo's README states the invariants that LE31's own `backend/app/models.py` currently violates. This feature is the *reference*; Feature 374 is the *defect it exposed*. Do not treat this file as the fix.

## Goal

Retain `ramaraihan12/warung-pos` as the **external arrival that states three of LE31's hardest invariants in one README** — and, more narrowly, as the artifact that made the parent look at LE31's own schema for the first time in 87 passes and find a contradiction between §4.3 and `models.py`.

The three arrivals, quoted from the upstream README (the README text is a third-party document; the sentences below are extracted facts about *that project*, not claims about LE31):

| Upstream README statement | LE31 invariant | Charter |
|---|---|---|
| *"Stock is never a stored number. It is the sum of `stock_movements` (receiving positive, sales negative), computed on the server."* | current stock derived from the append-only ledger, never stored | §4.3 / conventions *Stock* |
| *"Money is integer rupiah everywhere (`integer` columns, no floats, a guard that throws on a fractional value)."* | exact EUR, never binary floats; a **guard** that rejects a fractional value | §3.6 / conventions *Money* |
| *"A sale is never refused for lack of stock, because the customer already has the goods."* | an oversell is recorded, not refused | (LE31 has no stated policy — this is the gap) |

**No code today. The deliverable is the reference, and the pointer to Feature 374.**

## Scope

**In scope (defer artifact):**

- A written record of the three statements above, with the source repo and its verbatim README text attached.
- A written record of the **fourth** arrival, which is the genuinely new one and the one that changed LE31's own file: *"Stock is never a stored number."* LE31's charter says the same thing in §4.3 — **and LE31's schema says the opposite.** This reference is what made that visible. See Feature 374.
- A written record of the **integer-money-with-a-guard** pattern. LE31's §3.6 says "exact EUR, never binary floats" and the codebase does use `Decimal` throughout `models.py` (verified: `unit_price`, `subtotal_items`, `subtotal_tax`, `total_due`, `total_paid`, `amount`, `opening_float`, `counted_cash`, `variance` are all `Decimal = Field(max_digits=10, decimal_places=2)`). **The gap is not the type — it is the guard.** LE31 has no runtime check that rejects a fractional value on write; `Decimal` with `decimal_places=2` will *round* a third decimal place rather than raise. Upstream's "a guard that throws on a fractional value" is a strictly stronger property than "the column is declared `Decimal`". **This is the one genuinely actionable idea in this pick, and it is cheap.**
- A decision record noting that this is the **third** independent external project (after `jdmacleod/kitchen-erp`, feature 370, and `Donkie/Spoolman`, feature 371) to arrive at LE31's money/stock invariant set — and the **first** to state it as a *negative* ("never stored") and to pair it with a *runtime guard*.

**Out of scope (defer artifact):**

- Any LE31 code, schema, or migration. (The one exception is Feature 374, which is a **separate feature** with its own contract; this file does not authorise it.)
- Adopting the warung-pos codebase. It is **TypeScript, off-stack** — LE31 is FastAPI + SQLModel. The *offline-first outbox* pattern is portable; the code is not.
- QRIS / Indonesian payment rails, multi-user cashier roles, Postgres 17, Next.js 16, Playwright, Better Auth, Drizzle, Dexie, Vitest — all off-stack or out of scope.
- Barcode scanning, receipts on 58 mm thermal paper, email reminders. §3.2 excludes customer-facing receipts and payment-gateway integration.
- **A full offline-first implementation of LE31.** This is the honest boundary. LE31 is a **single-VPS, online, server-authoritative** system (§3.2: one VPS + systemd unit; the waiter UI polls; §3.2 explicitly defers WebSockets). An outbox with device-side UUIDs is a substantial architectural change, not a feature. See "Why this matters" for why it is nevertheless worth filing.

## Description

`ramaraihan12/warung-pos` is a 575 KB self-hosted POS for an Indonesian *warung* (small shop) whose stated design goal is *"keeps selling when the internet drops and syncs when it comes back."* It is brand new (created 2026-10-24, ★0, 0 issues) and unproven. **The project is not the artifact — the README is.** What makes it worth a pass is that its README states its invariants unusually precisely, and three of those statements are LE31's invariants stated by a stranger.

The transferable content, in the order it mattered:

1. **"Stock is never a stored number."** Upstream keeps `stock_movements` and computes the sum on the server. LE31's §4.3 prescribes the same shape — and LE31's `backend/app/models.py` line 106 declares `qty_remaining: int` as a **persisted column on `Batch`**, with no derivation site anywhere in the codebase. **The parent verified this on 2026-10-24:** `grep -rn qty_remaining` across the repository returns exactly one code hit (the column declaration) plus documentation and feature-contract text; `backend/app/services/` **does not exist**; and features 26, 34, 371 and 372 all describe `qty_remaining` as derived, which it is not. This is a first-party defect and it is filed as **Feature 374**, separately, because it is a code change and not a vocabulary reference.

2. **"Money is integer rupiah everywhere (`integer` columns, no floats, a guard that throws on a fractional value)."** Note the last clause. Upstream does not merely *declare* an integer money type; it **guards the write path** so a fractional value cannot enter. LE31's `Decimal` fields are correct in type but will silently round at two decimal places. The guard is the transferable part, and it is a small, high-value addition.

3. **"A sale is never refused for lack of stock, because the customer already has the goods."** Upstream's stated policy: a sale is never blocked by insufficient stock; both sales are kept, the stock reads **-1**, and the owner sees the product in an **Attention list**. LE31 has **no stated policy** on oversell — and §4.3's `sold_out` marking is a *kitchen prep* concept (the cook ran out), not a *theft/concurrency* concept (two waiters sold the last one). These are different things and LE31 conflates neither — it simply has not decided. **The upstream policy is worth filing as a candidate answer to a question LE31 has never asked.**

4. **The clock-check detail** — *"compares the device clock with the server clock at the moment a batch is sent, not at the moment of sale, because an offline sale always arrives late and that gap says nothing about the clock."* This is a genuinely sharp observation about clock-skew detection, and it is the kind of thing that is hard to re-derive. LE31 is not offline-first, so it has no analogue today. Recorded for the day it needs one.

5. **The concurrency case is stated concretely**: *"If two offline devices sell the last egg tray, both sales are kept, stock reads -1, and the owner sees the product in an Attention list."* LE31's single-VPS, online model makes a true concurrent oversell much less likely (one server serialises writes), but not impossible — two waiters can still sell the last portion within one request window. **The "Attention list" surface, however, is a real gap in LE31: `features/15-inventory-variance.md` and `features/34-stockout-prep-board-snapshot.md` exist, but there is no "something is wrong and the owner should look" surface in the waiter UI.** That is a separate question and is not actioned here.

## Data model

None shipped. The vocabulary implies, for LE31's own future consideration: an **outbox table** (client-generated id + payload + attempt count), a **client clock vs server clock** comparison, and a **derived** on-hand quantity. **None of this is proposed for LE31 v1**, and no table is added by this feature. LE31's `StockEntry` remains the only ledger.

The one data-model-adjacent item that *is* proposed (in Feature 374, not here): the removal of a persisted `Batch.qty_remaining` column in favour of a derived read.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (any one):**

1. A PR touches any money-bearing write path → the §3.6 exact-`Decimal` rule and the **missing fractional-value guard** (this pick's actionable residue) must be cited in the PR description.
2. The owner ever asks about oversell, concurrent sale of the last portion, or an "attention"/anomaly list → the upstream policy above is the pre-agreed candidate answer.
3. The owner ever asks for the waiter UI to work with no network → this reference is the starting point, and the scope should be re-derived from scratch (an offline-first LE31 is a v2-scale architectural decision, not a feature).

## Telegram interaction if any

None today. Long-horizon note: if the cook bot is ever asked for a stock check, the upstream "Attention list" framing maps onto LE31's existing `/sold_out` and `/leftover` commands; but the *anomaly* surface (a sale that drove stock negative) belongs to the **owner/manager** role, not the cook, and §3.1 names exactly two roles. **Adding a third surface for anomalies would conflict with §3.1** — the anomaly should be a line in an existing manager command (e.g. the end-of-day recap, feature 39) rather than a new surface.

## Dependencies

None. No new packages, no schema migration, no infrastructure. The upstream stack is entirely off-stack (TypeScript/Next.js/Drizzle/Dexie); the *patterns* are portable, the *code* is not.

## Open questions

1. **Should LE31 add a fractional-value guard on money writes?** The reference says yes. This is the one unmade decision this pick proposes. Cost is small (one Pydantic validator on the `Decimal` fields, or a SQL check constraint). **Unmade owner decision.**
2. **What is LE31's oversell policy?** Never asked, never written down. Upstream's answer is "never refuse, record the negative, surface it". **Unmade owner decision.**
3. **Should "attention"/anomaly reporting exist in v1 at all?** It would ride on the existing end-of-day recap rather than adding a surface. **Unmade owner decision.**

## Why this matters

Because it did something no previous LE31 pass has done: **it made the parent look at LE31's own code, and the code was wrong.**

Eighty-seven passes of "external arrival at LE31's invariant set" have all been filed as *vocabulary references* — as evidence that LE31's rules are the right rules, quoted back at LE31. That is worth something, but it is a weak form of value: it changes nothing. This reference changed something. The parent, reading this README for a brainstorm pick, noticed that a stranger's project stated *"Stock is never a stored number"* and then went and checked whether LE31's own schema obeyed the same rule — **and found that it does not.** That check costs one `grep` and about ninety seconds. It was never run in 86 prior passes, because every prior pass was reading *external* descriptions and never *internal* code.

The honest framing of the lesson: **external references are only useful if you let them make you look at your own code.** A third-party README that agrees with your rules is a curiosity; a third-party README that makes you find a place where your code does not obey your rules is an audit. This pick is the first one in the series that was an audit.

The narrower, still-valuable residue: the **fractional-value guard**. LE31's money fields are correctly typed `Decimal` but will round a third decimal place instead of rejecting it. The reference's "a guard that throws on a fractional value" is the stronger property, and it is a small change.

## Cross-section

Features 259 (`CtrlAltDevelop/ledger-service` — transactional outbox, idempotent, double-entry), 302 (`mhmd2042/cafe-pos` — offline café POS, **integer minor units**), 353 (`FreeOpenSourcePOS/FloCafe` — offline-first floor POS), 266 (`wraplet-app/openpocket-pos` — no-account phone POS, optional cloud sync), 370 (`jdmacleod/kitchen-erp` — "Decimal money, append-only facts"), 371 (`Donkie/Spoolman` — on-hand derived from movements, never stored), 372 (`hitaishi2222/kinv` — expiry without valuation). GitHub `ramaraihan12/warung-pos` is **unique** vs all 402 pre-existing feature files + 378 HANDOFFs (verified by ripgrep against `features/`, `specs/` and `INDEX.md` for `warung-pos`, `warungpos`, `ramaraihan` — 0 hits). Fully reversible (vocabulary-only). **Notably, the four prior "arrival" references (370/371/372 and 259) never once looked at LE31's own `models.py` — this is the first arrival to be used as an audit instrument.**
