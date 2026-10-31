# Feature 407 — Review before write: the undo boundary ends exactly at the commit

> **Pick C of Daily Research 2026-10-30 (92nd pass).** **Reference artifact, vocabulary-only.** **Verdict: `defer`** (v1 parking lot). **No code is adopted.**
>
> **Source artifact**: `YuryFilipovich/Penny` — **Apache-2.0 ✓ §3.2 strictly-compatible**, **★8/⑂0 recorded explicitly as NO traction evidence in EITHER direction** (the highest star count of the 27-repo shortlist, and still trivially low), **303 KB**, **TypeScript / Svelte 5 / Node — OFF-STACK** (LE31 is Python 3.13 + FastAPI + SQLModel + aiogram v3), **created 2026-10-24 AND pushed 2026-10-27 = IN-WINDOW BY BOTH FIELDS**, 0 topics, `archived=false`, `fork=false`, default_branch `main`. **All fields parent-verified via direct `GET /repos/`** (`/tmp/le31-daily-2026-10-30/gh/repo_YuryFilipovich__Penny.json`, HTTP 200), **never from search-result numbers**. Description (verbatim from the GitHub API): *"Self-hosted receipt review for Grocy: extract grocery PDFs, correct products…"*.
>
> **Bucket: v1** (vocabulary reference against a v1-owned surface). **Evidence class: INFERRED, confidence LOW** — no LE31 owner has asked for undo/redo; the *gap* is observed, the *demand* is not.
>
> **⭐ The transferable idea is a boundary, stated exactly: the review buffer and the write are separated by a line that undo does not cross.** From the artifact's own README:
>
> > *"A person reviews every field before anything is written to Grocy."*
>
> > *"The UI supports undo and redo during review. **Confirming a stock purchase is a real Grocy write and cannot be undone through Penny.**"*
>
> > *"**Importing stock cannot be undone with this toolbar.**"*
>
> And the artifact is equally explicit about what it **does not** keep:
>
> > *"**Penny has no saved-receipt page, autosaved drafts, PDF storage, browser receipt database, or disk import journal.** The PDF, extracted products, corrections, and undo/redo history exist only in the open page's memory. Refresh, closing the page, or starting a new review discards them."*

## Goal

Retain the **review-before-write** discipline as a persistent cross-section reference for LE31, and record the two halves that make it work:

1. **The buffer is a real, user-visible state** — a person sees the proposed data beside the source and edits it, and nothing is durable while they do.
2. **The commit is a distinct, named act** — and **undo stops at it.** The moment the write happens, the write is history; before it, the write does not exist.

**No LE31 code changes today.** The recorded question is: *when the `/start_today` confirm flow is built, what is the shape of the confirmation buffer, and where exactly does its undo boundary sit?*

## Scope

**In scope (defer artifact, v1 vocabulary reference):**

- **A written record** of the **review-before-write + undo-boundary** discipline, quoted from the artifact.
- **A written record of LE31's current posture** against that discipline:
  - `ItemStatus` = `new / preparing / ready / served / cancelled` — **there is no draft state.** `grep -n 'class ItemStatus' -A6 backend/app/models.py` confirms it.
  - `backend/app/routers/` contains **only `tables.py`** — **there is no bill router, no order router, and no confirm endpoint.** No LE31 order is ever staged for review.
  - The **one LE31 surface that already specifies a machine-proposes-human-confirms flow** is the charter's P0: *"Cook can upload a menu photo via Telegram, **confirm parsed items**, set per-item prep quantities, and the system creates batches."* — feature 04 (`/start_today`) and feature 65 (cook photo stock-list PWA).
- **A named trigger** (below).

**Out of scope (defer artifact):**

- **Any draft state, any undo/redo stack, any review buffer, any confirm endpoint.** Nothing is built.
- **Any change to the order-taking path.** LE31's waiter takes an order and it *is* the order; there is no document-review step and **one must not be invented**.
- **AI document extraction.** The artifact's input is a **PDF receipt** and the extraction is done by an LLM. LE31's §3.4 forbids customer-facing AI and requires a non-AI fallback; the **`/start_today` photo flow is explicitly specified as *cook-initiated* with the cook confirming**, and feature 04 already owns it. **This artifact does not propose AI extraction, does not propose a review of AI output, and does not change who initiates.**
- **A receipt/PDF import surface.** LE31 has no supplier-purchase domain in v1 (§3.2).
- **Adopting the artifact's stack.** Svelte 5 + Node + Tesseract-adjacent tooling is off-stack. **Only the discipline transfers.**
- **A durable review store.** The artifact deliberately keeps **nothing** durable in the buffer. **LE31 must not copy that** — a LE31 review buffer that vanishes on refresh would be useless on a phone in a dining room — so **the discipline transfers and the storage decision does not.**

## Description

### What the artifact does, and the two halves worth keeping

`Penny` turns grocery receipt PDFs into a reviewable product list, then imports confirmed purchases into Grocy. The pipeline is: **upload → machine extracts → person reviews every field → person confirms → write happens.**

The interesting part is not the extraction. It is **where the artifact draws its lines.**

**Line 1 — the buffer is real and bounded.**

> *"The PDF, extracted products, corrections, and undo/redo history exist only in the open page's memory. Refresh, closing the page, or starting a new review discards them."*

The buffer is a **genuine intermediate state** with its own lifetime, and the artifact is **honest about that lifetime** rather than pretending it is a saved draft. **It is a transaction, not a document.**

**Line 2 — undo stops at the commit.**

> *"The UI supports undo and redo during review. **Confirming a stock purchase is a real Grocy write and cannot be undone through Penny.**"*
>
> *"**Importing stock cannot be undone with this toolbar.**"*

This is the sharpest line in the artifact, and it is sharp because it is **asymmetric on purpose**. Undo is cheap inside the buffer because nothing has happened yet. Undo is *not* offered after the commit because a stock write is **history** — and LE31's charter §3.3 says the same thing about `StockEntry`: *"Never UPDATE or DELETE."*

**So the artifact and LE31's own ledger invariant agree, and they agree for the same reason: a committed stock movement is not a value, it is an event.** The artifact's own words — *"a real Grocy write"* — are the same sentence as LE31's §3.3.

**Line 3 (a secondary but useful detail) — the source stays visible beside the extraction.**

> *"The original PDF stays visible during the scanning animation and beside the editable table, with page navigation and zoom."*

The operator compares the machine's reading against the thing being read. **That is the whole value of a review step** — it is not "approve the AI", it is "check the AI against the source". A review surface that hides the source is a rubber stamp.

### Why this fails the LE31 v1 gate today — stated plainly

**The pain the artifact solves is not a LE31 pain.** `Penny` solves *"a machine read a document and I need to check its reading before it becomes inventory"*. LE31 has **no document-reading pipeline**. The waiter's order is typed by a human; the cook's `/start_today` photo flow is **cook-initiated and cook-confirmed** by the charter's own P0 wording.

**Three further reasons the v1 build is not ready:**

1. **There is no draft state to review.** `ItemStatus` has five members and none of them is a draft. `OrderItem` is created as an order line, not as a proposal.
2. **There is no staging path to review.** `backend/app/routers/` contains **only `tables.py`**. No order is ever assembled-then-confirmed; a `POST /api/orders` would create the order directly. **There is nothing between "the waiter decides" and "the order exists".**
3. **Undo/redo against what?** LE31's `StockEntry` ledger is append-only by rule (§3.3). **An undo of a stock movement is a reversal event, not an undo** — and LE31 already has a vocabulary for that (feature 400's reversal / `StockReason` member, feature 382's idempotency). **Copying "undo" into LE31's stock path would be a category error**: it would put a mutable-buffer affordance next to an append-only ledger.

### The one genuinely portable piece — and it points at a surface LE31 already owns

**The `/start_today` confirm flow.** The charter's P0 already says the cook *"uploads a menu photo via Telegram, **confirms parsed items**, sets per-item prep quantities, and the system creates batches"*. That is **exactly `Penny`'s shape**: machine proposes, human confirms, the write happens on confirmation, and the per-item quantities are the human's to set.

**What the artifact adds to that flow, specifically:**

- **The confirmation is a distinct, named act** — not an implicit side effect of the upload. In `Penny`, confirming is a separate button with a separate consequence.
- **The buffer's lifetime is bounded and stated.** For LE31, the buffer should live in the **Telegram conversation** (the cook's phone), not in a browser — and therefore it is **bounded by the conversation**, which is a *different* lifetime from `Penny`'s page. **The discipline transfers; the lifetime is LE31's to decide.**
- **The source stays visible.** In Telegram that means the photo remains visible alongside the parsed items — **which Telegram gives for free**, because the photo *is* the message.

**Recorded, not proposed** — the confirm flow is **feature 04's** to build, and this artifact is the vocabulary it should build against.

## Data model

**None. No table, no column, no enum member.** This is a vocabulary record.

The artifact's own concepts, recorded for reference only: a *review session* (in-memory), an *extracted product* (name, quantity, unit, line price, store, receipt date, currency, expiration date, storage location, product group), optional *source coordinates* (`{ page, x, y, width, height }`, one-based pages, normalised 0–1 from the upright page's top-left), and a *confirm* that performs a **real, non-undoable** write into Grocy's stock history.

**Not adopted**: the review session is in-memory in the artifact and **LE31 must not copy that** (see *Out of scope*). The source-coordinate geometry is a **PDF-rendering** concern and has no analogue in LE31.

**One recorded LE31-relevant consequence**: the artifact states that *"New rows have no default unit"* — *"the unit is never guessed"* — which is the **same rule as feature 392** (LE31's `MenuItem.unit` and the `OrderItem` unit ambiguity). **Corroboration, not a new pick** — feature 392 already owns it.

## Implementation steps

**None. This artifact builds nothing.** The implementation steps are the steps a future implementer takes **at the trigger**, recorded so the reference is complete:

1. **When the `/start_today` confirm flow is implemented** (the trigger), read this artifact alongside **feature 04** (menu-photo bot), **feature 65** (cook photo stock-list PWA) and **feature 397** (the `sold_out` state, which is the *other* half of the confirm surface).
2. **Decide, in writing:** (a) **what is the buffer's lifetime** — the Telegram conversation, a persisted draft, or both? (b) **is "confirm" a distinct command or the act of sending the next message?** (c) **does the confirmation screen show the source photo beside the parsed items?** — the artifact says it must, and in Telegram this is free.
3. **Do not add an undo stack to the stock path.** A committed `StockEntry` is an event (§3.3). **If a correction is needed after the confirm, it is a reversal event**, using the existing `StockReason` vocabulary (feature 400 / feature 382), **not** an undo.
4. **If the buffer is persisted**, the persistence must be **append-only or explicitly a draft table** — **not** a mutable "current draft" row. Feature 374's derive-never-store discipline applies to *quantities*; a draft row is a different kind of value, and **the decision must be made explicitly** rather than by default.
5. **If no decision can be made,** close this artifact and leave the current posture (upload → parse → confirm in one turn) as-is. **That is a valid outcome** — the artifact is a reference, not a commitment.

## Telegram interaction if any

**None today.** This artifact adds no command and changes no command.

**The trigger surface is the Telegram bot**, and this is stated explicitly so the reference is complete rather than implied: the confirm flow belongs to `/start_today` (feature 04). If promoted, the shape would be **one extra state in an existing conversation** — the cook's proposed items, awaiting the cook — and **not** a new command family.

**Explicitly NOT proposed**: `/undo`, `/redo`, `/draft`, or any command that reverses a committed stock movement. **The cook's correction path is the reversal vocabulary (feature 400), and this artifact must not drag a generic undo into it.**

## Dependencies

- **No new package. No code.**
- **Feature 04** (menu-photo bot, `/start_today`) — **the trigger surface.** Owns the cook-initiated parse-and-confirm flow.
- **Feature 65** (cook photo stock-list PWA) — the same photo input on the waiter/PWA side.
- **Feature 397** (`sold_out` state) — the *other* half of the confirm surface; **feature 397 already notes that feature 34's rule depends on it being correct first.** **Do not merge.**
- **Feature 400** (`void restores stock` / reversal `StockReason`) — owns the **committed** correction path. **This artifact is explicitly NOT that.** Review-buffer undo vs. committed reversal are different concepts and **must not be merged**.
- **Feature 382** (stock-deduction idempotency) — owns the write's idempotency; relevant because a confirm that is retried must not double-write.
- **Feature 392** (menu-item unit meaning) — **corroborates** the artifact's *"the unit is never guessed"* rule. **Already owned; not re-picked.**
- **Not** feature 45 (print fallback) and **not** feature 04's OCR specifics — unrelated.

## Open questions

1. **What is the buffer's lifetime in Telegram?** The cook's phone may lose connectivity mid-confirmation. Does the parsed proposal survive a restart, or is it discarded? **The artifact's answer — discard — is wrong for LE31** and **must not be copied**; the right answer is LE31's to decide, and it is a **persistence decision** with a §3.3 interaction.
2. **Is "confirm" a distinct Telegram action or a message?** aiogram v3 supports both a dedicated button and a typed command. **The artifact's model is an explicit button**, which is a stronger signal of intent — **worth considering, not decided here.**
3. **Does the cook see the source photo beside the parsed items?** **Recommended yes** (the artifact's line 3) and cheap in Telegram. **Recorded as a recommendation, not a decision.**
4. **Is a persisted draft table acceptable under §3.3?** §3.3 governs *stock events*, not drafts. **A draft table is likely fine** — but the decision must be **made explicitly**, not inherited by default.
5. **Does this concept extend to the waiter UI?** **No.** LE31's waiter takes an order and it is the order. **Adding a review step to ordering is out of scope and is not proposed.** Recorded so a future reader does not generalise it.

## Why this matters

**Because it names a boundary that LE31's own charter implies but never draws — and the boundary is exactly where LE31's hardest rules live.** §3.3 says a stock change is a new `StockEntry` and is never updated or deleted. That is a **commit boundary**. But LE31 has **no defined pre-commit state at all**: there is no "proposed", no "pending", no buffer. **The transition from "not yet happened" to "happened" is unlabelled**, and the only reason it has not caused trouble is that **nothing yet sits on the other side of it** — there is no `/start_today` implementation, no bill router, only `tables.py`.

**The asymmetry that argues for `defer` over `build`.** The cost of getting this wrong later is real but bounded: an implementer will draw the boundary somehow, and the plausible wrong answer (*"the parse is confirmed by being sent"*) is quiet. But the cost of building it now is **worse**: LE31 would add a draft concept, a persistence decision and a buffer lifetime **before the surface it serves exists** — and would likely build the wrong lifetime, because the surface (Telegram, mobile, flaky connectivity) has properties the artifact's browser page does not.

**Why the artifact mattered, precisely.** It did not tell LE31 anything about receipts. It told LE31 that **undo is a property of the buffer, not of the data** — that the correct place to stop an undo is the moment the data becomes history — and that **the source must stay visible beside the extraction**. The second is the one that generalises: a confirm step where the operator cannot compare against the source is a **rubber stamp**, not a review. That rule applies to the `/start_today` photo flow, to the `86` stock count, and to every future machine-proposes surface LE31 builds.

**And it corroborates a rule LE31 already has, from an unrelated direction.** *"New rows have no default unit"* is LE31's feature 392's rule — **the unit is never guessed** — arriving independently from a grocery-receipt tool. Two arrivals at the same rule from different domains is **weak but real evidence** that the rule is worth keeping, and it is recorded as corroboration rather than as a new pick.

**The honest counterweight.** Every reason to file this is a reason LE31 v1 **cannot use it yet**: there is no document to review, no draft to buffer, and no order to stage. That is why the verdict is `defer` — and it is why the artifact is filed **with a trigger attached to a surface LE31 already owns** (`/start_today`), so that the next implementer inherits the boundary *and* the precondition, rather than inheriting an idea and reinventing the lifetime.
