# Feature 380 — `boethius68/KitchenLink`: zero-cloud LAN relay + all-14-EU-allergen declaration for the waiter/guest surface (defer)

> **NEW observation (2026-10-25).** Documents in-window GitHub repo `boethius68/KitchenLink` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable in principle**, but the repo is **SwiftUI + Next.js + Supabase ✗ OFF-STACK** for LE31's Python 3.13 / FastAPI / SQLModel / Postgres stack), **★0/⑂0**, **54,797 KB**, `default_branch=main`, `archived=false`, created **2026-02-21T00:00:00Z AND pushed 2026-10-24T00:00:00Z = IN-WINDOW BY `pushed_at` ONLY** (created 7 months before the 2026-09-25..2026-10-25 window start — **this is not a fresh discovery**). All field values read from a **direct `/repos/` GET** by the parent on 2026-10-25, not from search-result numbers. Description (verbatim from GitHub API): *"Smartphone-first OS for restaurants, bars, and cafes — offline-resilient QR table ordering & native POS"*.
>
> Bucket: **v1 (connectivity-boundary + allergen-declaration vocabulary)** — Pick B of Daily Brainstorm 2026-10-25. Build verdict: **`defer`** (parking-lot; **vocabulary reference only** — no code changes, no schema change).

## Goal

Retain `boethius68/KitchenLink` as an **external arrival that names two things LE31 has not named**, and turn each into a one-sentence written boundary in LE31's own documentation.

The two things:

1. **The zero-cloud fallback as an explicit, designed state.** KitchenLink's architecture diagram names a *"Local Hub Relay (POC) — Local LAN Multicast / P2P — Zero-Cloud Offline Fallback"* as a first-class component, with the guest web falling back to LAN dispatch when the cloud link drops. LE31's boundary today is binary (online / offline) and implicit.
2. **Allergen declaration as a *data* concern, not a menu-text concern.** KitchenLink's guest web carries a *"quiet inline allergen pictogram"* engine covering *"all 14 EU allergens and statutory food additives without visual clutter."* LE31's `MenuItem` model has no allergen field at all.

**The deliverable is two sentences in LE31's own documentation.** Not a feature. Not a build.

## Scope

**In scope (v1 — documentation only):**
- One sentence in the connectivity boundary: LE31's waiter/cook surfaces must have a **named** behaviour when the uplink is lost, distinct from "the request fails".
- One sentence in the data-model boundary: `MenuItem` will eventually carry a **structured allergen list**, not a free-text note — and that list will be **EU-14-shaped** because that is the regulatory set the target market uses.

## Out of scope (v1)

- Any schema change. **No `allergens` column is added in this feature.**
- Any LAN relay, multicast, P2P relay, mDNS/Bonjour discovery, or Supabase-style edge runtime. **LE31 does not adopt SwiftUI, Next.js, or Supabase.**
- A guest QR ordering surface — **already filed as Feature 11** (`11-customer-qr-menu.md`); not re-picked.
- The LAN-only ordering surface itself — **already filed as Feature 376** (`drsamonline/canteen-lan`, the 2026-10-25 daily-research pick); not re-picked. **Feature 380 is about the *allergen* half and the *named-state* half, not the LAN-ordering half.**
- EU allergen regulatory sign-off — this is a **vocabulary** reference, not legal advice. **Owner decision required before any allergen data is collected** (see Open questions).
- Any WebSocket or polling-model change — **§3.2 defers WebSockets** and Feature 375 builds on the polling model.
- Any device-topology or deployment decision — **Feature 381** owns that vocabulary.

## Description

Two independent ideas arrived from one README.

**Idea 1 — the zero-cloud fallback as a named state.** KitchenLink's architecture (quoted from the upstream README; these are facts about *that* project):

> `LAN["Local Hub Relay (POC)<br/>• Local LAN Multicast / P2P<br/>• Zero-Cloud Offline Fallback"]`

and

> *"Offline-First Resilience: If the internet or cloud connection drops, KitchenLink can fall back to local LAN order dispatching so service never halts during rush hours."*

LE31's own boundary is currently *silent on the failure mode*: `le31-conventions` says *"operational transitions are explicit user actions"* and Feature 376 (2026-10-25) names the *LAN-only venue* as a case. What neither names is what happens **on the LAN-only venue when the single kitchen tablet reboots**, or when the router drops the uplink mid-service. The vocabulary to borrow is the idea of a **named relay state** rather than a boolean.

**Idea 2 — allergens as structured data.** KitchenLink's guest web carries *"quiet inline allergen pictograms covering all 14 EU allergens and statutory food additives without visual clutter"*, and the README states the project was built *"für den europäischen Markt … mit lückenloser Auszeichnung aller 14 EU-Allergene"*.

LE31's `MenuItem` model (parent-read on 2026-10-25, `backend/app/models.py`) is:

```python
class MenuItem(SQLModel, table=True):
    id / name / category / unit_price / unit / is_prepared / photo_url
```

**There is no allergen field.** The only free-text surface is `OrderItem.notes` (per-order, not per-dish) and `Batch.notes`. LE31 also treats v1 guest data as **counts, not identity** — allergens are a *dish* attribute, not a guest attribute, so they do **not** collide with the privacy invariant.

**The cross-section value is the shape, not the code.** A dish with fourteen possible declarable allergens needs a *set*, not a string, and the EU-14 set is the right one for the target market (France/Paris per the charter's business-time convention). LE31 should learn the *shape* — a per-dish structured allergen set — and the *policy* — allergen data belongs to the menu item, never to the guest record.

## Data model

**No change.** This feature adds no table, no column, no migration.

For reference, the shape this feature is recording for a future decision (NOT to be implemented here):

```
menu_item.allergens : set of allergen codes, EU-14 vocabulary
  ["gluten","crustaceans","eggs","fish","peanuts","soy","milk",
   "nuts","celery","mustard","sesame","sulphites","lupin","molluscs"]
```

## Implementation steps

1. **`PROJECT_CHARTER.md` §3.2 (Out of scope / explicit non-goals)** — add one sentence naming the zero-cloud fallback as a distinct state LE31 must not silently conflate with a failed request. *(One sentence. Not a section.)*
2. **A short note next to the `MenuItem` model** (either a comment in `backend/app/models.py` or a line in the charter's schema-overview §4.2) recording that `MenuItem` will eventually carry a structured EU-14 allergen set, and that this is **deferred to v2** pending an owner decision.
3. **Do not touch** `backend/app/models.py` beyond a comment. **Do not add a column.**

## Telegram interaction if any

None. The allergen vocabulary is a menu-surface concern; the relay-state vocabulary is a connectivity concern. Neither touches the cook bot.

## Dependencies

- `PROJECT_CHARTER.md` (edit, one or two sentences).
- `backend/app/models.py` (optional comment only).
- **Existing `MenuItem` model** for the reference shape.

## Open questions

1. **Is LE31's target market actually EU-14?** The charter sets business time to `Europe/Paris`, which implies France — and France's declarable-allergen list is the EU-14 plus the 14th (gluten) already covered. **But LE31's *owner* may be operating a single restaurant whose actual customers need a different set.** Owner decision required. **Until then, do not collect allergen data.**
2. **Does allergen data belong on `MenuItem` or on a separate `MenuItemAllergen` table?** LE31's §4.3 discipline says *append-only, never update* for *stock*; a menu dish's allergen set is **mutable metadata**, not a ledger, so a simple set column is defensible. But it is a call that should be made once, deliberately, when the feature is actually scheduled.
3. **Does the "named zero-cloud state" belong in the charter at all**, or is it a decision for the waiter/cook UX feature (Feature 375, the 85th pass's "visibility of system status" criteria)? **Recommendation: one cross-reference sentence in the charter, full treatment deferred to the UX feature.** Do not open a new charter section for it.

## Why this matters

The 88-pass series has filed a large number of *vocabulary* references — and there is a real risk that "another reference filed" becomes a habit that stops looking. So the honest question for this one is: **does it change anything?**

Two answers, both small:

**First** — the allergen observation is the **first in 88 passes** to name a *menu-dish attribute that LE31's model cannot express at all*. Not "an approach LE31 should adopt" (there have been many of those), but **a piece of information a restaurant must be able to serve and LE31 currently has nowhere to put**. That is a different class of gap, and it is worth ten references of the "good idea, wrong shape" kind.

**Second** — the zero-cloud fallback is the **third** arrival in three consecutive passes (Features 376, 380, and the 2026-10-24 HN story *"Keeping restaurant iPads in sync without a router"*) describing the same boundary from a different side. Three independent arrivals is the threshold at which a boundary stops being an interesting idea and becomes a **named thing**. It is already named — Feature 376 named it on 2026-10-25. **Feature 380 does not rename it; it adds the missing half (what happens when the LAN relay itself fails) and the allergen observation.**

Neither of these justifies a schema change today. Both justify two sentences.
