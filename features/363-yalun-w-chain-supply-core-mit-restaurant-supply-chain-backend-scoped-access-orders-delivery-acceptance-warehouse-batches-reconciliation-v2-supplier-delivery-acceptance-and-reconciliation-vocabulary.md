# Feature 363 — `yalun-w/chain-supply-core` restaurant-supply-chain-backend-+-scoped-access-+-orders-+-delivery-acceptance-+-warehouse-batches-+-reconciliation (defer)

> **NEW observation (2026-10-23).** Documents in-window GitHub Search `restaurant-pos` / `supply chain restaurant` result: `yalun-w/chain-supply-core` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★0 / 0⑂ = NO traction evidence in EITHER direction**, **786 KB = among the smallest non-trivial picks of the 85-pass series**, **Python ✓ ON-STACK**, created 2026-10-21T08:49:52Z AND pushed 2026-10-21T08:49:59Z = **IN-WINDOW BY BOTH FIELDS, and created→pushed is a 7-second gap — the repo was created and seeded in one sitting, ~2 days before this pass**). **Zero topics.** Description (verbatim, parent-verified via direct `GET /repos/` 2026-10-23): *"Restaurant supply-chain backend: scoped access, orders, delivery acceptance, warehouse batches and reconciliation. Code-only open-source extraction."* The trailing phrase **"Code-only open-source extraction"** is itself the strongest signal: this is an *extraction* of code from a larger product, not an independently-run project, which is why ★0. **Fully reversible** (vocabulary-only artifact).

## Goal

Retain `yalun-w/chain-supply-core` as a **structural-evidence peer** documenting the **delivery-acceptance-then-reconcile** ordering for supplier-side stock. The artifact is the peer-awareness record plus the named vocabulary for **acceptance-as-a-distinct-explicit-state before reconciliation**. No code today.

## Scope

**In scope (defer artifact):**
- A written record: MIT, ★0/0⑂ (recorded plainly as **no traction evidence either way**), 786 KB, Python ON-STACK, in-window by both fields, zero topics, 7-second create→push.
- A decision record: verdict is `defer`.
- A named vocabulary: **acceptance-before-reconciliation / scoped-access / batch-tracked-inbound**.
- A cross-section reference with feature 343 (`warpusTOM/StockWise_Group6_BT-204` — offline-first inventory + POS) and the §3.3 StockEntry invariant.

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any supplier, purchase-order, or warehouse data model. **LE31 v1 has no inbound-goods concept whatsoever** — its `StockEntry` ledger records prepared-item decrements, not deliveries.
- Any supplier-facing surface. §3.1's two-role discipline (waiter, cook) has no supplier role, and adding one is an owner decision.

## Description

GitHub `yalun-w/chain-supply-core` — *"Restaurant supply-chain backend: scoped access, orders, delivery acceptance, warehouse batches and reconciliation."*

**Stack match matrix:**

| `chain-supply-core` component | LE31 charter §3.1 | Match? |
|---|---|---|
| Python | Python 3.13 | ✅ exact |
| Orders | §3.3 ledger discipline | ⚠️ **different order kind** — supplier POs vs restaurant tickets |
| Delivery acceptance | §State *explicit operational transitions* | ✅ strong conceptual match |
| Warehouse batches | §3.3 *append-only* | ✅ batch-as-event is §3.3-shaped |
| Reconciliation | §3.3 *derived current state* | ✅ strong match — reconcile by derivation, not mutation |
| Scoped access | §3.4 chokepoint | ⚠️ transferable; LE31 has no multi-tenant concept |
| Zero topics, ★0 | — | ⚠️ **weak evidence of nothing** |

**The primitive worth keeping — the ordering:**

The pick's sequence is **orders → delivery acceptance → batches → reconciliation**. Acceptance is a *distinct explicit state between "ordered" and "received"*, and reconciliation happens **after** it, by derivation.

That ordering maps onto LE31's §State invariant (*operational transitions are explicit user actions*) and §3.3 (*current stock is derived from entries*) with no translation at all. It is the cleanest structural mapping of the day.

**⚠️ Why it is still `defer`, stated plainly:**
1. **The domain does not exist in LE31.** LE31 tracks what the kitchen *consumes*, not what a supplier *delivers*. There is no supplier, no purchase order, no warehouse. This pick answers a question LE31 has never been asked.
2. **★0/0⑂ and "code-only extraction"** mean there is no evidence this code runs anywhere. It is vocabulary, not validation.
3. **§3.1 role discipline.** A supplier is a third role. Adding it is an owner decision, not a research finding.

**⚠️ One genuine tension recorded:** if LE31 ever does add supplier intake, §3.3's append-only ledger and this pick's "reconciliation" could conflict — does reconciliation *correct* the ledger (forbidden by §3.3) or *derive* from it (canonical)? **This pick derives. LE31 must too. The tension is recorded so it is not resolved by accident later.**

## Data model

None today. If ever built, and only after an owner decision creates the supplier role: an `InboundDelivery` **append-only** row per delivery-acceptance event (`supplier_ref`, `accepted_at` tz-aware, `line_items`, `batch_refs`), with warehouse quantity **derived** by folding the ledger — never stored as a mutable balance. This mirrors §3.3 exactly. **Deliberately unspecified**: supplier identity storage, which brushes §3.7 (a supplier is a business contact, not a guest, but the boundary is unmade).

## Implementation steps

1. Do not implement. LE31 has no inbound-goods concept and no supplier role.
2. If the owner ever opens supplier intake, re-run the seven-check gate with §3.1's two-role discipline as an explicit gate item — a third role is a charter decision.
3. If opened, the acceptance-before-reconciliation ordering is the default to start from; it satisfies §State and §3.3 simultaneously.
4. Reconcile **by derivation only**. Any design that mutates a stored balance on reconciliation violates §3.3 and must be rejected, not negotiated.

## Telegram interaction

None. The cook's Telegram surface must not gain supplier-facing commands without an owner decision on the third role.

## Dependencies

- **Unmade:** whether LE31 gains a supplier role at all (charter-level, §3.1).
- **Unmade:** the §3.7 boundary for supplier contact data if it ever exists.
- **Unmade:** the reconciliation-derives-vs-corrects question — recorded above, resolved in favour of derivation by §3.3.

## Open questions

1. Does LE31 ever track inbound goods, or only kitchen consumption?
2. If yes, is a supplier a third role — and does §3.1's two-role discipline survive that?
3. Is "reconciliation" ever permitted to correct a ledger entry, or only to derive? (§3.3 says derive; confirm and record.)
4. Would acceptance events share the `StockEntry` ledger or sit beside it?

## Why this matters

Two of the last three passes have picked off-domain items and said so. This one is a genuinely good **structural** mapping — acceptance-before-reconciliation is the canonical §State + §3.3 shape — attached to a domain LE31 does not have. Filing it records the shape for a decision that has not been made, which is the correct outcome for a `defer`, and it is filed at true weight: ★0, no topics, an extracted codebase.