# Feature 364 — `NexoForger/seat-and-serve` Frappe/ERPNext-restaurant-POS-+-KDS-+-kiosk-+-ordering-app (defer)

> **NEW observation (2026-10-23).** Documents in-window GitHub Search `restaurant-pos` result: `NexoForger/seat-and-serve` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★2 / 0⑂**, **1928 KB modest**, **Python ✓ ON-STACK**, created 2026-10-01T10:22:51Z AND pushed 2026-10-22T16:45:09Z = **IN-WINDOW BY BOTH FIELDS** (~3-week-old repo with an in-window push). **Zero topics.** Description (verbatim, parent-verified via direct `GET /repos/` 2026-10-23): *"S&S (Seat & Serve) Frappe and ERPNext restaurant POS, KDS, kiosk, and ordering app"*. **Fully reversible** (vocabulary-only artifact).

## Goal

Retain `NexoForger/seat-and-serve` as a **structural-evidence peer** documenting the **four-surface-single-backend** shape (POS + KDS + kiosk + ordering on one framework) and, more usefully, the fact that it is built on **Frappe/ERPNext rather than FastAPI+SQLModel**. No code today.

## Scope

**In scope (defer artifact):**
- A written record: MIT, ★2/0⑂, 1928 KB, Python ON-STACK but **framework OFF-STACK**, in-window by both fields, zero topics.
- A decision record: verdict is `defer`, with the reason stated precisely — this is an **ERP-platform adoption** question, not a shape question.
- A named vocabulary: **four-surfaces-one-backend / framework-vs-shape / kiosk-as-a-role**.
- A cross-section reference with feature 325 (`AlexisLD-DEV/qramen` — QR-code table ordering PWA) and feature 323 (`KitchenQ`).

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any ERPNext or Frappe evaluation. **A stack change requires an explicit charter decision** (§3.1) and nothing in this pass constitutes one.
- Any kiosk surface. A kiosk is a **fourth client**; §3.1's two-role discipline already constrains clients (see the recorded tension below).

## Description

GitHub `NexoForger/seat-and-serve` — *"S&S (Seat & Serve) Frappe and ERPNext restaurant POS, KDS, kiosk, and ordering app"*.

**Stack match matrix:**

| `seat-and-serve` component | LE31 charter §3.1 | Match? |
|---|---|---|
| Python | Python 3.13 | ✅ language matches |
| Frappe / ERPNext framework | FastAPI + SQLModel + Postgres | ❌ **OFF-STACK — and not a small gap** |
| Postgres (implied by ERPNext) | Postgres in production | ✅ data store matches |
| POS / KDS / ordering shapes | waiter UI + cook Telegram bot | ⚠️ shape overlaps; **surface count does not** |
| Kiosk | — | ❌ **no LE31 analogue** |

**The useful reading is the negative one.** ERPNext gives a restaurant POS, KDS, kiosk and ordering app **for free inside an existing ERP**. That is a real and widely-taken approach to this problem, and it is worth having on file precisely because LE31 is *not* taking it. The question it raises is the one worth naming: **does LE31 want a business system, or the smallest useful ops system?** §3.1 answers this already — "two primary operational surfaces" and a fixed stack — but this pick is the concrete counterfactual.

**⚠️ Tensions recorded:**
1. **Framework vs shape.** The *shapes* (POS, KDS, ordering) are portable vocabulary. The *framework* (Frappe/ERPNext) is the actual decision and it is squarely against §3.1. Adopting it would be a rewrite, not an integration. **This pick therefore contributes shape, not code.**
2. **Surface count.** POS + KDS + kiosk + ordering = four clients. LE31 has two (waiter web UI, cook Telegram bot), and feature 355 already recorded that adding a native phone app would make three and that §3.1's two-role discipline argues against it. **A kiosk is the fourth. The tension compounds and is recorded rather than resolved.**
3. **★2/0⑂ with zero topics** — minimal evidence either way. The pick is about the shape, not the project's adoption.

## Data model

None today, and deliberately so. ERPNext's data model (Company, Item, Supplier, Warehouse, Stock Ledger Entry, Journal Entry) is a **double-entry ERP model**, which is categorically different from LE31's §3.3 single append-only `StockEntry` ledger with derived current stock. Mapping one onto the other is the whole cost of adoption, and it is not a mapping anyone should attempt from a research pass. **Recorded, not designed.**

## Implementation steps

1. Do not implement, and do not evaluate ERPNext, from this artifact.
2. If the owner ever reopens the §3.1 stack decision, this pick is the named counterfactual to weigh against the smallest-useful-ops-system principle — **and that decision would be a charter amendment, taken deliberately, with its own research pass.**
3. If LE31 ever adds a kiosk, re-read this artifact together with feature 355's surface-count tension rather than treating each as a standalone addition.

## Telegram interaction

None. Frappe/ERPNext kiosk surfaces have no Telegram component, and LE31's cook surface is aiogram v3 by charter (§3.1).

## Dependencies

- **Unmade:** whether the §3.1 stack decision is ever reopened. It is currently settled and this pass does not unsettle it.
- **Unmade:** whether LE31 ever gains surfaces beyond the two charter roles. Feature 355 (client 3) and this pick (client 4) both push on an unmade decision.
- **Procurement note:** a kiosk implies dedicated hardware in the restaurant. None exists.

## Open questions

1. Would a business system (ERP) ever be preferable to the smallest useful ops system for a single restaurant? (Answered by §3.1 today: no. Recorded so the answer is visible, not assumed.)
2. What is LE31's maximum client count, and is that a charter number or an accident of history?
3. Is a KDS a *surface* or a *view of the existing cook surface*? This is genuinely unresolved and determines whether feature 323's cluster is one surface or four.

## Why this matters

The strongest thing this pick contributes is a **named counterfactual**. LE31 has spent 85 passes accumulating peers that confirm its direction; far fewer record a serious alternative that LE31 deliberately rejects. The ERP-monolith route is the most credible such alternative in the restaurant-software space, and having it on file — with its cost (a rewrite, a different data model, a surface-count problem) stated plainly — is more useful than another confirming shape.