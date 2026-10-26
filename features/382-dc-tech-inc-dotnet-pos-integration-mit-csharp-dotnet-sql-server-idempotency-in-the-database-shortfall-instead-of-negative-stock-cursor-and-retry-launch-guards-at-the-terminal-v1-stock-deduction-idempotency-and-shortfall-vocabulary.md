# Feature 382 — `dc-tech-inc/dotnet-pos-integration`: LE31's `StockEntry` has no idempotency guard, and an outside author wrote down the missing rule

> **NEW observation (2026-10-26).** Documents in-window GitHub repo `dc-tech-inc/dotnet-pos-integration` (**licence: `mit` ✓ §3.2 STRICTLY-COMPATIBLE — the *vocabulary-shape* is the transferable item; the *code-shape* is NOT adopted**), **★0/⑂0 — no traction evidence in either direction**, **97 KB**, `default_branch=main`, `archived=false`, `fork=false`, 4 open issues, C#/.NET 10 + SQL Server **✗ off-stack**, created **2026-10-22T15:51:29Z AND pushed 2026-10-22T20:19:34Z = IN-WINDOW BY BOTH FIELDS**. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-26, not from search-result numbers. Description (verbatim from GitHub API): *"Point-of-sale to stock integration worker in C#/.NET and SQL Server: launch guards at the terminal (drawer, keylock, scan, quantity, repeat) with audited supervisor override, idempotent sales ingestion, reconciliation, retry, PowerShell tooling"*.
>
> **The README and the file tree were also read** (parent, 2026-10-26, `/tmp/le31-daily-2026-10-26/rd/`). The repo ships **six ADRs** under `docs/adr/`: `0001-idempotency-in-the-database`, `0002-shortfall-instead-of-negative-stock`, `0003-dapper-and-plain-sql`, `0004-pull-with-a-cursor-and-retry`, `0005-powershell-tooling-with-a-mockable-sql-seam`, `0006-launch-guards-at-the-terminal`. **This is the first artifact in the 88-pass series that is a reference implementation of a LE31 gap, rather than merely a shape that rhymes with one.**
>
> Bucket: **v1 (stock-ledger semantics vocabulary)** — Pick A of Daily Research 2026-10-26. Build verdict: **`defer`** (parking-lot; **vocabulary reference only** — no code changes, no schema change, and **no licence to copy the implementation from**).

## Goal

Retain `dc-tech-inc/dotnet-pos-integration` as the external arrival that answers a question LE31's own codebase has never answered:

> **What happens in LE31 when the same business event writes `StockEntry` twice?**

**And, second and separately:**

> **What does LE31 do when a sale asks for more stock than exists?**

**The deliverable is one document.** It records the two questions, the two candidate answers, and the fact that **LE31 currently has neither**.

**The parent-verified gap this artifact names.** `backend/app/models.py:113-126` defines `StockEntry` as an append-only ledger with columns `id, batch_id, qty_delta, reason, ref_order_item_id, by_user_id, at`. Parent-verified on 2026-10-26 by grep across the entire backend (9 Python files):

- `grep -rniE "idempot|dedup|duplicate" --include=*.py backend/` → **0 matches**. **Nothing prevents the same business event from appending two rows.**
- `grep -rniE "shortfall|negative" --include=*.py backend/` → **1 match**, and it is only a sign convention: `qty_delta: int  # positive = added, negative = consumed` (`models.py:122`).
- `grep -rniE "reconcil" --include=*.py backend/` → **1 match**, and it is only a docstring on an unrelated model: `class Shift(SQLModel, table=True): """For end-of-shift cash reconciliation."""` (`models.py:181-182`).

**So `ref_order_item_id` exists and is nullable and unconstrained. There is no uniqueness guarantee on it, no shortfall concept, and no reconciliation routine.** That is the gap. This artifact is the reference for closing it, not the authority to close it.

## Scope

**In scope (v1 — documentation only):**
- One document recording the **"idempotency lives in the database, in the same transaction as the stock change"** rule as stated in ADR-0001, including the specific anti-pattern it names: *"There is no 'have I seen this?' read in application code, so there is no check-then-act race."*
- One document recording the **"stock never goes negative; the difference is recorded as shortfall"** rule as stated in ADR-0002, including its `CHECK (OnHand >= 0)` backing and its deliberate *"There is no back-order or automatic correction."*
- One document recording that **the third external answer to LE31's open oversell-policy question now exists**, and how it differs from the two already filed.
- A cross-section note naming the ADRs that are **NOT** in scope for v1 and why (ADR-0004 cursor/retry presumes an external system to poll; ADR-0006 launch guards presume a POS-terminal device model LE31 does not have).

## Out of scope

- **Any code, schema, or migration in LE31.** This is a vocabulary artifact. No `StockEntry` column, no new table, no Alembic migration, no unique index, no `Shortfall` enum, no reconciliation job.
- **Any port or vendor of the C#/.NET implementation.** The licence is MIT, so it is *legally* adoptable — **but adopting it would be a §3.2 stack change** (C#/.NET + SQL Server inside a Python 3.13 / FastAPI / SQLModel / Postgres product) requiring an explicit charter decision. **The transferable content is the RULE, not the implementation.**
- **ADR-0006 (launch guards at the terminal).** It presumes a cash drawer sensor, a keylock, a barcode scanner and a per-terminal session model — an OMG UnifiedPOS device vocabulary. **LE31 has no POS terminal and no hardware of any kind.** This ADR is recorded as *read and declined*, not as a backlog item.
- **ADR-0004 (pull with a cursor and retry).** It presumes a remote system to poll. **LE31's waiter writes to LE31's own database in the same request** — there is no remote system to reconcile against, and no cursor to keep.
- **ADR-0003 (Dapper and plain SQL) and ADR-0005 (PowerShell tooling).** These are stack-specific choices with no transferable content.
- **Re-litigating the oversell-policy question as a build.** Feature 373 (`ramaraihan12/warung-pos`) already recorded it as an **unmade owner decision**. This artifact adds a **third candidate answer** to that open question; it does not make the decision.
- **Any charter, `le31-conventions`, or `PROJECT_CHARTER.md` edit.** The artifact **proposes** the questions; it does not **answer** them.
- **Any money, cost, or valuation surface.** §3.3 forbids it, and ADR-0002's `Shortfall` is a *quantity* difference, not a value.

## Description

**The repo is explicitly not a product.** Its README states: *"Built and maintained by DCtech. as an engineering reference. The POS is **fictional** (`PosIntegration.FakePos`), every SKU and sale is generated, and nothing here is derived from a real POS product, a client or an employer's system."*

**What it is, and why it matters to LE31**, is a worked argument about the seam where a POS and a stock system meet. The README enumerates the failure modes:

> - the POS delivers at least once, so the same sale can arrive twice;
> - the POS fails (503, timeouts) in the middle of a page;
> - a sale can ask for more than the shelf holds, or for an item the stock system has never heard of;
> - weeks later nobody can say whether the two systems still agree;
> - an operator rings up a wrong sale (the same basket twice, a typed code, 100 instead of 10), and once the POS has committed it no back-office check can undo it.

**Every one of these maps onto a LE31 situation that LE31 has not written down**, except the first three, which map onto situations LE31 arguably has *because* it has no idempotency guard:

| ADR | Rule (condensed from the ADR's own *Decision* paragraph) | LE31 today |
|---|---|---|
| 0001 | `ProcessedSale` has the sale id as **primary key**; the insert happens **first, inside the same transaction** that updates stock and writes the movements; a second delivery fails the insert, rolls back, and returns `Duplicate` | **No guard.** `ref_order_item_id` is nullable and unconstrained. |
| 0002 | Each line books **`min(OnHand, quantity)`**; the remainder, and any unknown SKU, is stored as **`Shortfall`** on the movement; `CHECK (OnHand >= 0)`; **no back-order, no automatic correction** | **No policy.** `qty_delta` may go arbitrarily negative. |
| 0004 | Read pages after a **stored cursor**; retry transient failures (5xx/408/429/deadlock) up to five times with backoff and jitter; permanent errors **fail fast**; invalid sales are **rejected and logged, not retried** | **Not applicable.** LE31 has no remote system to poll. |
| 0006 | A `LaunchGuardPipeline` evaluates a sale *attempt* against terminal state; **"a supervisor may accept a risk but cannot change a fact"** | **Not applicable** (no POS terminal), **but the rule is portable vocabulary.** |

**ADR-0001's most valuable sentence for LE31 is the negative one.** The ADR does not say *"check whether we have seen this sale before"*. It says the reason it does not is that *"there is no 'have I seen this?' read in application code, so there is no check-then-act race."* **That is a statement about where the guarantee must live, and LE31's `StockEntry` currently has no guarantee living anywhere.**

**ADR-0002's distinction is the one that makes this a *third* answer rather than a duplicate.** LE31 has already filed one external answer to the oversell question — feature 373 (`ramaraihan12/warung-pos`, 2026-10-24): *"A sale is never refused for lack of stock, because the customer already has the goods… both sales are kept, the stock reads -1, and the owner sees the product in an Attention list."* ADR-0002 takes the **opposite** position on the sign and adds a third element:

- `warung-pos` → keep the sale, **let the stock go negative**, surface it.
- `dc-tech-inc` → keep the sale, **refuse to let the stock go negative**, and record **the difference** as an explicit `Shortfall` on the movement.

**Both keep the sale. They differ on what the ledger says.** Parent-verified that this is *not* already covered: `grep -rn "shortfall" features/*.md` returns only unrelated matches for *prep shortfalls* in feature 52; no existing feature or spec contains `min(OnHand`, a never-negative rule, or a shortfall concept.

**ADR-0006's transferable sentence** — *"the rule for 'can release' is that a supervisor may accept a risk but cannot change a fact"* — is **the same distinction LE31's §3.4 explicit-transition principle already makes**, stated in one line by an outside author. It is the **fourth external corroboration of an LE31 boundary** in this series, after `kitchen-erp`'s *"Decimal money, append-only facts"* (2026-10-24), `kinv`'s *"without stock-valuation busywork"* (2026-10-24), and `mesa-lite`'s no-build-step criterion (2026-10-25). **A boundary that is written down is a decision; a boundary that is merely absent is an accident.**

## Data model

**No data model change. This artifact is a document.**

For the record, the *shape* of the rules being documented, expressed in LE31's own terms (**not proposed as a schema — this is what the artifact records, so that a future proposal can cite it**):

- The ADR-0001 rule, in LE31 terms: **a uniqueness guarantee on a business-event key, enforced by the database, inside the same transaction that appends the `StockEntry` row.** LE31's candidate key would be `ref_order_item_id` — which already exists on `StockEntry` (`models.py:124`) and is currently nullable and unconstrained. **Whether `ref_order_item_id` becomes non-null and unique is an owner decision this artifact does not make.**
- The ADR-0002 rule, in LE31 terms: **a quantity cap derived from the current derived stock, with the uncapped remainder recorded as a separate, visible value on the ledger entry.** LE31's stock is *derived* (`SUM(qty_delta) WHERE batch_id = X`, per the `StockEntry` docstring at `models.py:116-117`), so a `min(OnHand, qty)` rule would be computed against that derived sum, not a stored number. **Whether the remainder is a new column, a new `StockReason`, or a new ledger event is not decided here.**
- **No `Shortfall` model, enum, table, or field is created by this artifact.**
- **No uniqueness constraint, index, or migration is created by this artifact.**

## Implementation steps

**There are no implementation steps. The deliverable is one document.**

The steps that *would* apply **if and only if** the owner later approves a build, and which this artifact explicitly does **not** authorise:

1. **Owner answers the two questions.** The narrow, answerable questions are: *"If the same order is submitted twice — a double-tap, a retry, two waiters on the same ticket — should LE31 record one `StockEntry` or two?"* and *"When a sale asks for more than exists, should the ledger record a negative quantity, or should it record the difference separately?"* **Until an owner answers, no code is written.**
2. **Re-run the feature gate** with the owner's answer as `reported` evidence. This artifact's evidence class is **`inferred`** — the gap is real and parent-verified *inside LE31's own codebase*, but **an internal gap is not a reported pain**, and check 1 requires the latter.
3. **Scope to ADR-0001 alone** if a build is ever approved. **ADR-0001, ADR-0002, ADR-0004 and ADR-0006 are four separate decisions with four separate justifications.** Bundling them is the failure mode this artifact warns about.
4. **If ADR-0001 is approved, the acceptance path is observable:** submit the same order twice, then inspect the ledger and confirm exactly one `StockEntry` row exists for it — and confirm the second submission produced *no* row and *no* partial write.
5. **If ADR-0002 is approved**, the acceptance path is: attempt a sale exceeding available stock, then inspect the ledger and confirm the quantity never went negative and the difference is visible as a distinct value.

## Telegram interaction if any

**None. This artifact has no Telegram component, and the reason is structural rather than accidental.**

LE31's cook surface is a **Telegram bot** (`backend/app/bot/cook_bot.py`, aiogram v3). A Telegram bot's inbound messages arrive via a **webhook served by Telegram's servers** — so an operator pressing a button twice produces **two separate inbound updates**, and Telegram does not deduplicate them for LE31.

**This is precisely the ADR-0001 condition, arriving through a different door.** The ADR's failure mode — *"the same sale can arrive twice"* — is not a remote-POS edge case in LE31's case; it is the **normal** double-tap on a kitchen tablet. **This does not license a build.** It is recorded because it makes the question concrete and in-scope for LE31 specifically, rather than borrowed from a POS integration that LE31 does not have.

**The Telegram bot must not become a deduplication surface.** Dedup belongs in the database (§3.3, append-only ledger) and in the write path, not in the bot's handler layer — a bot-level guard would be a second representation of a fact that the ledger already owns.

## Dependencies

- **The LE31 owner** — the two questions must be answered by a person, not inferred from a repository.
- **`le31-conventions`** — the seven-check gate; and the §3.3 stock invariant and §3.4 explicit-transition invariant that this artifact documents against.
- **`le31-v1-feature-pattern`** — for the shape of any future contract derived from this artifact.
- **Existing feature 373** (`features/373-ramaraihan12-warung-pos-...`) — **load it before writing anything about oversell.** It holds the open owner decision and the first external answer.
- **Existing features 49 and 52** — they add unique indexes to `StockEntry` (`ix_stockentry_row_hash`, `ix_stockentry_anchor_hash`) but for **hash-chain integrity**, not for **business-event deduplication**. **A future ADR-0001 implementation must not collide with them, and must not reuse `row_hash` as the dedup key** — a hash-chain row hash and a business-event id are different things.
- **Existing features 259, 269, 303** — these cover the **HTTP idempotency-key** primitive (`IdempotencyKey` table, `idempotency_key + request_hash + response_payload`). **Pick A is not that.** Those are *endpoint-level* idempotency for a client-retryable request; ADR-0001 is *ledger-write-level* idempotency keyed by a business event, enforced inside the stock transaction. **A future proposal must state which one it is.**
- **`PROJECT_CHARTER.md` §3.2** — the stack decision (Python 3.13 / FastAPI / SQLModel / aiogram v3 / Postgres). **Adopting the C#/.NET implementation would violate it.**
- **`PROJECT_CHARTER.md` §3.3** — the stock invariant (every prepared-item quantity change is a new `StockEntry`; never update or delete ledger events; current stock is derived).

## Open questions

1. **Should the same business event append one `StockEntry` or two?** — **the question this artifact exists to put on the table. Unanswered.**
2. **Should a sale that exceeds available stock record a negative quantity, or record the difference separately?** — a **third** external answer now exists (`min(OnHand, qty)` + explicit shortfall); the owner has still not chosen between it and feature 373's *"never refuse, record the negative, surface it"*.
3. **Is `ref_order_item_id` the right key for idempotency, or is a dedicated business-event id needed?** — `ref_order_item_id` is nullable today, so it cannot serve as a primary dedup key without a schema change. **Not decided here.**
4. **Does the guarantee belong on the `StockEntry` row, or on a separate ledger event?** — ADR-0001 puts the uniqueness on a `ProcessedSale`-style row *in the same transaction*; LE31's §3.3 says ledger events are never deleted, so a "processed" marker row would itself be an append-only event with its own lifetime question.
5. **Does an oversell need an owner-visible surface?** — feature 373 noted that LE31 has `features/15-inventory-variance.md` and `features/34-stockout-prep-board-snapshot.md` but **no "something is wrong and the owner should look" surface**. ADR-0002's `Shortfall` is *per-movement* and *for investigation*, which is not the same as an attention list. **Open.**
6. **Is the "supervisor may accept a risk but cannot change a fact" rule applicable to LE31 at all?** — LE31 has no supervisor role today. The rule is recorded as vocabulary; its LE31 analogue (if any) is not proposed.

## Why this matters

**Because LE31 has a real, parent-verified gap, and this is the first artifact that closes the *thinking* about it without pretending the gap has been reported.**

The distinction matters. LE31's backend contains **no idempotency mechanism of any kind** — parent-verified by grep across all 9 Python files, with zero matches for `idempot`, `dedup`, or `duplicate`. `StockEntry` carries a `ref_order_item_id` that nothing constrains. A `StockEntry` ledger whose whole value proposition is *"current stock is derived from entries"* can be silently wrong if the same event is written twice, and **LE31 has no way today to detect that**.

**But check 1 of the feature gate is not satisfied by an internal gap.** Check 1 asks for a *reported* or *observed* pain — something an owner, waiter, or cook has actually hit. This artifact's evidence class is **`inferred`**: the gap is real and observable in the code, but **no one has reported it**. That is exactly the classification the gate exists to enforce, and exactly why the verdict is `defer` and not `build`.

**What the artifact buys is the decision, pre-stated.** The next time an owner asks *"what happens if the waiter taps send twice?"*, LE31 will not be inventing an answer from scratch — it will have a **documented, externally-authored, test-backed candidate answer** ready to put in front of them, complete with the trade-off named (*"a supervisor may accept a risk but cannot change a fact"*), the anti-pattern named (*"no check-then-act race"*), and the deliberately-excluded options named (*"no back-order or automatic correction"*).

**And the artifact's scope discipline is itself the deliverable.** This pass found a repo that is MIT-licensed, complete, tested, and directly on-topic — and filed it as **vocabulary only**, refusing to port 97 KB of C# into a Python product, refusing to bundle four ADRs into one slice, and refusing to answer an owner decision on the owner's behalf. **A stack boundary that survives is one that has been tested against an outside alternative.** This is the fifth such corroboration in the 88-pass series, and the first about the *ledger-write* half of LE31's data model.
