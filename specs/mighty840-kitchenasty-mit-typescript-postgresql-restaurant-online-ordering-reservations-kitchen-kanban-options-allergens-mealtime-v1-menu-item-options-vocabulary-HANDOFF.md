# HANDOFF — Feature 386: menu-item **options** as a first-class concept (the second gap in LE31's `MenuItem` model) — vocabulary reference

**This is a `defer` (parking-lot) pick.** It is a **vocabulary reference**: **no code changes, no schema change, no test file.** The deliverable is **one sentence in LE31's own documentation**, plus one sentence naming what this gap is not.

**Discovery chain:** Daily Brainstorm 2026-10-26 → the parent read the README of the in-window repo `mighty840/kitchenasty` (MIT, ★58/⑂29) → its "Menu & Kitchen" section says *"**Options, allergens, and mealtime tagging per item**"* → the parent read LE31's own `backend/app/models.py` → `grep -rn -i "option|variant|modifier" backend/app/models.py` returns **no output at all**: `MenuItem` has no option concept, and `OrderItem` records only `qty` and one `unit_price`.

**Full evidence record: `features/386-mighty840-kitchenasty-mit-typescript-postgresql-restaurant-online-ordering-reservations-kitchen-kanban-options-allergens-mealtime-v1-menu-item-options-vocabulary.md`**

## Active feature path

`features/386-mighty840-kitchenasty-mit-typescript-postgresql-restaurant-online-ordering-reservations-kitchen-kanban-options-allergens-mealtime-v1-menu-item-options-vocabulary.md` — **defer** (Pick B of Daily Brainstorm 2026-10-26).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL** | *No owner, waiter or cook has reported anything about sizes, variants, or choices.* The gap is **observable in the schema** (`MenuItem` cannot express an option; `OrderItem` has no place to record one), but **the need for it is not established**. **Evidence class: INFERRED, confidence LOW** — deliberately, and the contract says so. **The observed fact is the gap, not the demand.** This is the check that separates this pick from feature 385. |
| 2 | Viability | ✗ **FAIL** | A schema change of this size (an option-group model, a value model, an order-line reference, and a pricing consequence) is **not a small change**, and it would need to land together with the price question in feature 387. **Nothing is built today.** |
| 3 | Practicability and confidence | ✗ | **Confidence in the NEED is low** (check 1). The *shape* is well-attested — two independent authors, opposite ends of the stack, one window (feature 387 is the second). **The named rabbit hole: do not let a well-evidenced shape become a presumption of need.** |
| 4 | Conflict | ✗ **FAIL** | A price-bearing option model interacts with `DerivedTip` (which derives from `subtotal_items`) and with §3.6's exact-money rule — see feature 387's second sentence. **The gap cannot be filled without deciding the price question, and that decision is not made.** |
| 5 | Outcome + appetite + scope | ✗ | Not a v1 build. **The scope of this feature is deliberately ONE SENTENCE**, precisely because the underlying question is undecided. |
| 6 | Cost to operational value | ✗ | Value is **conditional on the owner selling a dish with a choice**, which is **unknown**. Filing the vocabulary now costs one sentence and forecloses nothing; building the model now costs days and may be wrong. |
| 7 | Circuit breaker + reversibility | ✓ | **Fully reversible** — a documentation-only artifact, one file. **Stop evidence:** if a PR adds a `notes`-based price-affecting choice, **stop and re-read** — that is the silent-money-bug path this feature exists to prevent. **Review point:** whenever an options model is proposed, confirm the price question was answered first. |

**Gate verdict: `defer`** — parking-lot. **This is not a "no"**: it is a documented gap with a named trigger condition (below).

## Bucket

**v1 (menu-data vocabulary)** — Pick B of Daily Brainstorm 2026-10-26. This would be a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — the parent confirmed on 2026-10-26 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that `le31 v2 owner-pains` / `le31 v2-AI` do **not** exist. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — 39th consecutive day), the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload.

## Files to touch

**The change itself — documentation only, two sentences:**

- LE31's **menu-data boundary** — the doc where the `MenuItem` shape is stated. **Find it first; do not guess the path.** The substance: *LE31's `MenuItem` describes a product; a product's variants are not described, and an order line is currently `MenuItem × qty` at a single price. Choosing a variant is a future decision, not an implicit use of `notes`.*
- LE31's **pricing boundary** — one sentence naming what this gap is **not** (allergens — feature 10; category nesting — recorded, not picked).

**Do NOT touch (out of scope, explicitly):**

- `backend/app/models.py` — **no schema change.** No `Option`, `OptionGroup`, `Modifier`, `Variant` or `MenuItemOption` model. **The column does not exist and this feature does not add it.**
- `backend/app/services/`, `backend/app/routers/`, `backend/app/bot/` — **no code at all.**
- `PROJECT_CHARTER.md` — **no charter edit.** This feature proposes a sentence; it does not make one.
- `features/10-allergen-tracking.md` — **allergens are owned by feature 10.** The allergen half of this pick's source is a **genuine duplicate and is recorded as such, not picked.**
- `features/11-customer-qr-menu.md` — the customer-facing menu. Not re-picked.
- Any `Socket.IO` / WebSocket adoption — §3.2 defers WebSockets; feature 375 builds on the polling model. `kitchenasty`'s "real-time WebSocket updates" is **explicitly not** a proposal.
- `kitchenasty`'s reservations, analytics, coupons, Stripe integration, staff invitations — **all out of scope.**

## The load-bearing check

There is **no test file** — this is a documentation artifact. The load-bearing check is that the two sentences exist, that they are **in LE31's own documentation** rather than only in this contract, and that the naming is precise enough that a future reader cannot mistake this gap for the allergen gap or the category-nesting gap.

**The verification is a re-runnable grep:**

```bash
cd /opt/data/le31_mmm3_research_work
grep -rn "option\|variant\|modifier" --include=*.py backend/app/models.py
# expect: NO output — this is the gap being documented, not closed
grep -rn "variants are not described\|variant" --include=*.md . | grep -v "^./features/\|^./specs/"
# expect: the new sentence, in LE31's own documentation
```

**The second grep's presence is the proof the feature landed; the first grep's continued emptiness is the proof the feature did NOT overreach.** A feature that closed the gap would be a **different feature**, gated separately.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. Here the observable behaviour is that **the gap is named in a place a future implementer will actually read** — which means: the sentence must live in LE31's own menu-data boundary, not only in this contract and the HANDOFF. **If the only place the sentence appears is in `features/` and `specs/`, the feature has not landed.**

## Rollback path

Delete the two sentences. One file, no code, no data, fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants (read the *Privacy* rule: allergens are a **dish** attribute, never a guest attribute, which is why the allergen gap does not collide with LE31's counts-only guest model) and the seven-check gate
- `le31-data` — schema-shape discipline
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for §3 scope and §4 schema
- `features/10-allergen-tracking.md` — **read this first**; it is the nearest neighbour and the easiest to confuse with this feature
- `features/387-mekedron-wolt-cli-…-HANDOFF.md` — the second half of one idea

## Open questions carried into any future build

1. **Does LE31's owner sell any dish with a choice?** **Unknown, and not askable from the repo.** This single question decides whether options are a v1 gap, a v2 feature, or a non-issue. **Recorded as unknown, not as "yes".**
2. **Is the price per-option or per-item-with-surcharge?** Two different models — an option *has* a price, or an option *adjusts* the price. `kitchenasty`'s per-item tags and `wolt-cli`'s resolution model do not settle it. **Do not guess.**
3. **Is a `notes`-based price-affecting choice ever allowed?** **The recommendation is no**, and the reason is the silent money bug described in the contract: a free-text choice with a single recorded price produces a bill that is arithmetically self-consistent and semantically wrong. **This is an owner decision.**
4. **Does "mealtime tagging" (also named in the source line) matter?** A dish served only at lunch is a **menu-availability** concept, not an option concept. **Out of scope here; recorded so a later pass does not conflate the two.**
5. **Is category nesting a separate feature?** `MenuItem.category` is a plain `str` and `kitchenasty` does *"Category management with nesting"*. **Recorded, not picked.**
