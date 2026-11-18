# Feature 495 — `v1-multi-terminal-order-capture-and-cashier-split-with-shared-queue`

> **Pick A of Daily Research 2026-11-18.** **Bucket: v1 (floor-operations vocabulary reference).** **Verdict: `defer` — parking-lot reference.**
>
> **Source artifact:** `FreeOpenSourcePOS/FloCafe` — MIT, ★192 / ⑂91, TypeScript/Electron, created 2026-05-07, pushed 2026-11-18T00:46:39Z. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-18/gh/repo_07_FreeOpenSourcePOS_FloCafe.json`; README: `/tmp/le31-daily-2026-11-18/gh/readme_07_FreeOpenSourcePOS_FloCafe.md` (37,642 bytes); source URL: https://github.com/FreeOpenSourcePOS/FloCafe.
>
> **Why this pick:** FloCafe states the capture/payment split as a single explicit line — *"Separate order capture, cashier payment, or combined counter terminals with shared LAN queue and QR ticket lookup"* — which is a compact description of a **floor-operations vocabulary LE31 does not have**. The parent ran a targeted dedup sweep across all 1,016 feature and spec files in the repository before selecting this pick: `shared LAN queue` → **0 hits**, `separate capture/cashier terminals` → **0 hits**, `multi-terminal` → **2 hits**, both incidental (feature 448's open question about bill-number allocation under a multi-terminal floor; features 474/476 mention "two terminals" in the context of a different defect). The mechanism is net-new to the corpus.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **counter-terminal vocabulary** as the reference design for a future LE31 multi-surface floor:

1. order capture and payment can be performed by **different terminals**;
2. the terminals are **separate order capture, cashier payment, or combined** roles, chosen per counter;
3. all terminals draw from **one shared queue**;
4. a **QR ticket lookup** joins a terminal to the order it is acting on;
5. the shared queue is **local** (LAN), not cloud-mediated.

No second surface, no queue, and no ticket-lookup table is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the five-point mechanism summary above.
- The explicit boundary with LE31 v1's fixed two-surface charter and with the two shipped first-party defects this mechanism would widen (features 474 and 476).
- The dedup result that establishes the mechanism is net-new to the corpus.
- A future-project attachment decision: `le31 Research`, because no v2 project exists and this pick is not v1 work today.

## Out of scope

- No second waiter surface, no tablet/handheld mode, no staff device management.
- No queue table, no queue authority, no ticket-lookup endpoint.
- No change to the waiter web UI, the cook Telegram bot, the `StockEntry` ledger, or the bill lifecycle.
- No adoption of the TypeScript/Electron stack.
- No concurrent-writer design, no ordering guarantee, no starvation policy — this feature records the vocabulary, it does not specify the mechanism's internals.

## Description

FloCafe's README states the mechanism directly:

- *"**Multi-counter ordering:** Separate order capture, cashier payment, or combined counter terminals with shared LAN queue and QR ticket lookup."*

The same README frames the surrounding posture:

- *"**Offline-first architecture:** Local SQLite storage with auto-migrating schema and fail-closed safety."*
- *"**Cash drawer management:** Cash pulse on checkout and end-of-shift cash drawer reconciliation."*
- *"**Granular roles & permissions:** Owner, Manager, Cashier, Server, and Chef roles with context-aware access policies."*

The transferable idea is the **separation of the act of ordering from the act of paying, without separating the order**. A busy counter has two people and one order; FloCafe's design admits that by giving the counter a set of terminals that share a queue and join to an order by ticket, rather than requiring one device to own the order end to end.

This matters to LE31 because the corpus already contains the two first-party defects that this mechanism would widen, and both were found by the same parent-side defect sweep:

- **Feature 474** — *"the shipped waiter screen holds one visit for the whole restaurant ... seating a second party destroys the first party's order."* The visit is the unit of ownership, and it is not per-table.
- **Feature 476** — *"the shipped waiter screen adds a dish to a line the kitchen has already served ... the quantity changes and nobody is told."* A second terminal would create a second writer against a line the cook has already acted on.

A shared queue with ticket lookup is the shape that makes those two defects fixable rather than merely tolerable: it names the **join key** (the ticket) and the **authority** (the queue) explicitly. But naming them is not the same as designing them, and the corpus does not yet justify the design.

## Data model

No schema change. The future reference shape, explicitly **not proposed today**, is:

```text
CounterTerminal (future reference)
  id, venue_id, role_kind        # order_capture | cashier_payment | combined
  shared_queue_id, active_ticket_ref

SharedQueue (future reference)
  id, venue_id, ordering_rule, enqueued_at

Ticket (future reference)
  id, queue_id, order_ref, state # queued | claimed | settled
```

Note what this shape deliberately does **not** decide: whether `Ticket` is a new entity or a projection over LE31's existing `Visit`/`Order` rows, and whether the queue is persisted or in-memory. LE31's `Visit` model is the existing authority; a future implementation would most likely extend it rather than replace it.

## Implementation

None in this feature. When a second floor surface is promoted into a scoped feature:

1. Decide the **join key**: is the ticket the order line-group id, a separate `Ticket` row, or the QR payload itself?
2. Decide the **queue authority**: one server-side queue (LE31 is server-authoritative) rather than a client-side one.
3. Decide the **claim protocol**: how a terminal claims a ticket, and what happens when a claimed ticket's terminal dies mid-order.
4. Decide the **visibility rule** for a line the kitchen has already served — feature 476's defect must be closed before a second writer exists.
5. Decide whether the **visit** becomes per-table — feature 474's defect must be closed before two people touch one visit.
6. Keep the split **explicit**: the capture action and the payment action remain separate user actions. LE31's charter forbids silently serving, closing, or reconciling an order, and a shared queue must not become a path that closes one implicitly.
7. Keep the queue out of `StockEntry` and out of the bill ledger — a queue is a work-claim, not a financial or stock event.

## Telegram interaction

None. The cook Telegram bot is not a counter terminal, and nothing here changes the cook's surface. If a future design ever routes a queue event to the cook, that is a separate feature with its own acceptance path.

## Dependencies

- Existing feature 474 — per-table order state and the one-visit-per-restaurant defect. A prerequisite, not a peer.
- Existing feature 476 — order-line quantity phase and the unserved-quantity-change defect. A prerequisite, not a peer.
- Existing feature 448 — bill numbering; its open question already names the *"busy multi-terminal floor"* as a trigger condition for a counter-row allocator.
- Existing feature 388 — table state and seat idempotency.
- Existing feature 483 — course fire filter, because a second terminal changes what "fire" means.
- Charter §3.1 — LE31 v1's two operational surfaces. This mechanism exceeds that count and therefore cannot be v1 work without an explicit charter decision.
- `le31 v2 owner-pains` and `le31 v2-AI` **do not exist** in the workspace; the sub-issue is attached to `le31 Research`.

## Open questions

1. Is a second counter terminal a real LE31 operator need, or only a vocabulary worth retaining? No operator has asked.
2. If it is needed, is the second terminal a **waiter** surface or a **cashier** surface? The charter names one owner and two staff roles; a cashier surface is a third.
3. Does the charter's two-surface count need an explicit owner decision to change, or is this a v2 item by definition?
4. Is the queue persisted (auditable, survives restart) or in-memory (lost on restart)? The cook bot's FSM has already been recorded as losing state on restart in feature 478; the same failure mode must not be copied here.
5. What is the ticket's identity — and is it the QR payload, a separate id, or the order id?
6. What happens to a ticket when the claiming terminal goes offline mid-order? Fail-closed, per LE31's posture, or fail-open with a visible warning?
7. Does the shared queue create a second concurrency surface that features 493 (bill-close idempotency key) and 400 (client-UUID idempotent sync) must be extended to cover?

## Why this matters

FloCafe is the strongest-traction permissive-licensed artifact this pass surfaced alongside OrderRestro, and it is the only one in the window that names the capture/payment split as a first-class mechanism rather than an accident of implementation. LE31's corpus has 528 feature contracts and none of them describe a floor with two people and one order.

The correct disposition is nevertheless **defer**. The mechanism is net-new and worth keeping, but LE31 v1 has a single-counter surface by design, two shipped first-party defects would have to be closed before a second writer is safe, and no operator has asked for it. Filing it now preserves the vocabulary — the join key and the queue authority, named — without pretending the demand exists.
