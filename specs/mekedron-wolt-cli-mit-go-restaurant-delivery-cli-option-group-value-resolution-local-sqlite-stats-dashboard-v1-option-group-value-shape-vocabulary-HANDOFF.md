# HANDOFF — Feature 387: the option group/value shape (second independent arrival) and the listed-price vs charged-price distinction LE31 has never written down — vocabulary reference

**This is a `defer` (parking-lot) pick.** It is a **vocabulary reference**: **no code changes, no schema change, no test file.** The deliverable is **two sentences in LE31's own documentation**.

**This pick has two halves, and they are not equally owned:**

1. **The option group/value shape** — feature 386 owns that gap. **This feature adds one pointer sentence and does NOT re-argue it.**
2. **The listed-price vs charged-price distinction** — **this is the new half, and it is LE31's own.** LE31's `OrderItem.unit_price` is a snapshot of `MenuItem.unit_price`, and `DerivedTip` derives from `subtotal_items`, which derives from those `unit_price` values. **The charter and schema never say whether `unit_price` is the price the venue *lists* or the price actually *charged*.** They are the same number today only because LE31 has no options. **That is the sentence worth writing.**

**Discovery chain:** Daily Brainstorm 2026-10-26 → the parent read the README of the in-window repo `mekedron/wolt-cli` (MIT, ★36/⑂7) → its feature list names *"**option matrix inspection and option resolution by name** (`--option "Drink=Cola"`)"* and its worked cart example shows `--option "<drink-group-id>=<drink-value-id>"` → the parent read LE31's own `backend/app/models.py` → `OrderItem` carries `qty` and one `unit_price` and **nowhere to record a choice**, while `DerivedTip` derives from `subtotal_items`, which derives from those `unit_price` values.

**Full evidence record: `features/387-mekedron-wolt-cli-mit-go-restaurant-delivery-cli-option-group-value-resolution-local-sqlite-stats-dashboard-v1-option-group-value-shape-vocabulary.md`**

## Active feature path

`features/387-mekedron-wolt-cli-mit-go-restaurant-delivery-cli-option-group-value-resolution-local-sqlite-stats-dashboard-v1-option-group-value-shape-vocabulary.md` — **defer** (Pick C of Daily Brainstorm 2026-10-26).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL** | *No owner has reported a pricing or options problem.* **Evidence class: INFERRED, confidence LOW** — deliberately, and the contract says so. **The one nuance worth stating precisely:** the price-provenance half is **not** a demand claim — it is a **definitional gap in LE31's own model**, and definitional gaps can be closed by a sentence regardless of demand. **That is why this feature is filed at all.** |
| 2 | Viability | ✗ **FAIL** | A price-bearing option model is **not** a small change, and it cannot land without the price question being answered first. **Nothing is built today.** |
| 3 | Practicability and confidence | ✗ | **Confidence in the NEED is low** (check 1). The *shape* is well-attested — two independent authors, opposite ends of the stack, one window. **The named rabbit hole: a well-evidenced shape is not a presumption of need, and a definitional gap is not a demand signal.** |
| 4 | Conflict | ✗ **FAIL** | The price half reaches directly into `DerivedTip` and §3.6's exact-money rule. **The distinction has two defensible readings and LE31 has picked neither on purpose.** |
| 5 | Outcome + appetite + scope | ✗ | Not a v1 build. **The scope of this feature is deliberately TWO SENTENCES.** |
| 6 | Cost to operational value | ✓ (narrowly) | Value today: one sentence prevents a future **silent** mis-pricing. Value in six months if deferred: the ambiguity is resolved **by accident**, by whichever code path happens to be written first. **The cost of writing it down is one sentence — the cheapest item in the pass.** |
| 7 | Circuit breaker + reversibility | ✓ | **Fully reversible** — a documentation-only artifact, one file. **Stop evidence:** if a PR introduces a price-bearing choice **without** deciding the price provenance first, **stop and re-read** — that is the silent-money-bug path. **Review point:** whenever an options model is proposed, confirm the price-provenance sentence was answered first. |

**Gate verdict: `defer`** — parking-lot. **The half that is genuinely LE31's own is the price-provenance sentence**; the options-shape half is a pointer to feature 386.

## Bucket

**v1 (menu-data + price-provenance vocabulary)** — Pick C of Daily Brainstorm 2026-10-26. This would be a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — the parent confirmed on 2026-10-26 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that `le31 v2 owner-pains` / `le31 v2-AI` do **not** exist. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — 39th consecutive day), the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload.

## Files to touch

**The change itself — documentation only, two sentences:**

- LE31's **menu-data boundary** — **one sentence**: the option shape is the convergent external shape (a **group** and a **value**), with a pointer to feature 386 as the owner of that gap. **Do not re-argue the gap — one reference, one line.**
- LE31's **pricing boundary** — **one sentence**: LE31's `unit_price` is a snapshot; the charter does not yet say whether it is the **listed** price of the product or the **charged** price of the product-as-ordered, and the two differ by exactly the option set; `DerivedTip` derives from `subtotal_items`, which derives from `unit_price` — so the distinction is **not academic**.

**Do NOT touch (out of scope, explicitly):**

- `backend/app/models.py` — **no schema change.** No `Option`/`OptionGroup`/`Modifier`/`Variant`, no `OrderItemOption`, no `Cart`/`CartItem`. **LE31 has no cart and this feature does not propose one.**
- `backend/app/services/`, `backend/app/routers/`, `backend/app/bot/` — **no code at all.**
- `PROJECT_CHARTER.md` — **no charter edit.**
- `DerivedTip`, `Bill`, `Shift` — **no schema change.** They are named as *dependents* of the price question, not as things to change.
- Any Wolt / delivery-platform integration — **explicitly not proposed.** `wolt-cli` is an unofficial community client and is **not affiliated with Wolt**; LE31 is a venue-side system, not a consumer ordering client. **The overlap is the menu vocabulary, not the business.**
- Any local-SQLite dashboard — §3.2's server-authoritative Postgres posture.
- Any CLI or terminal surface — §3.1's two surfaces (waiter web UI, cook Telegram bot).
- `kitchenasty`'s code, `wolt-cli`'s code — **MIT makes both legally adoptable; neither is adopted.** Go and TypeScript are both off-stack, and the transferable content is a **naming convention**, not an implementation.

## The load-bearing check

There is **no test file** — this is a documentation artifact. The load-bearing check is that the two sentences exist, in LE31's **own** documentation, and that the price sentence names `DerivedTip`'s dependence explicitly enough that a future implementer cannot read it as academic.

**The verification is a re-runnable grep:**

```bash
cd /opt/data/le31_mmm3_research_work
grep -rn "listed price\|charged price\|unit_price" --include=*.md . | grep -v "^./features/\|^./specs/"
# expect: the new price-provenance sentence, naming DerivedTip's dependence
grep -n "unit_price" backend/app/models.py
# expect: the two existing declarations (MenuItem.unit_price, OrderItem.unit_price) — UNCHANGED
```

**The second grep must show the declarations unchanged.** A feature that changed them would be a **different feature**, gated separately. The value of this feature is that it makes the ambiguity *visible* before someone resolves it by accident.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. Here the observable behaviour is that **the ambiguity is named in a place a future implementer will actually read** — which means the sentence must live in LE31's own pricing boundary, not only in this contract and the HANDOFF. **If the only place it appears is in `features/` and `specs/`, the feature has not landed.**

## Rollback path

Delete the two sentences. One file, no code, no data, fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants (read the *Money* rule: exact arithmetic, `Decimal` never float) and the seven-check gate
- `le31-data` — schema-shape discipline; **exact-arithmetic-over-a-wrong-quantity is still wrong**
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth for §3.6 (money) and §4 schema
- `features/386-mighty840-kitchenasty-…-HANDOFF.md` — **read this first**; it owns the options half of this idea
- `features/387-…-HANDOFF.md` — this document

## Open questions carried into any future build

1. **Is LE31's `unit_price` the listed price or the charged price?** **Currently indistinguishable** — and that is precisely the point. The question becomes answerable only when options exist. **Recorded as a question, not answered.**
2. **Does the owner sell any dish with a choice?** Unknown; feature 386 records the same unknown. **Do not resolve this feature's question by assuming the answer.**
3. **Should a cart exist in LE31?** The reference has one. **LE31 does not, and this feature does not propose one** — a cart is a §3.1 surface question and a §3.4 explicit-transition question, and neither is settled. **Recorded as out of scope, deliberately.**
4. **Do LE31's future customers arrive through a delivery platform?** The reference's whole domain is "a consumer ordering from Wolt". **The overlap is the menu vocabulary, not the business.** Recorded so a later pass does not treat this as a delivery-integration opportunity.
5. **Do the two features 386/387 need to land together?** If an options model is ever built, **yes** — the shape and the price question are one decision, not two. **Neither lands alone.**
