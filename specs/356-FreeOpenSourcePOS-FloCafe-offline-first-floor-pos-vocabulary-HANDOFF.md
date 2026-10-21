# HANDOFF — Feature 353: `FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary`

**Upstream source repo: [`FreeOpenSourcePOS/FloCafe`](https://github.com/FreeOpenSourcePOS/FloCafe)** — see `features/353-FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/353-FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-21).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes "a kitchen display the cook can read at a glance", the owner wants *proof the shape is real and actively maintained in 2026*, but struggles because *LE31 has no documented reference for an offline-first POS with kitchen-display + thermal printing + inventory + billing*, so that *the v1 surface can be defended with a named primitive rather than an assertion*. |
| 2 | Viability | ✓ | The owner/staff can understand an offline-first POS with a kitchen display and thermal receipt printing without specialist help. **MIT ✓ §3.2 STRICTLY-COMPATIBLE (code-shape adoptable)**, ★148/⑂63, 28 MB, 20/20 LE31-relevant topics. Viability is high for the vocabulary; **traction caveat recorded in the feature: ★148/⑂63 is real API data but is NOT evidence of restaurant-industry adoption and no owner mention exists in 83 passes.** |
| 3 | Practicability and confidence | ✓ | TypeScript/Electron is **OFF-STACK** for LE31's Python 3.13 / FastAPI / SQLModel / Postgres charter, so the *code* is not practically adoptable; the *vocabulary* is fully portable. Required data + permissions + infrastructure: none today. Evidence strength: medium-high for the vocabulary match, low for present urgency. |
| 4 | Conflict | ✓ | Does not violate any invariant. Offline-first / self-hosted are §3.4 + §3.5-aligned. **⚠️ One unresolved tension surfaced by this pick and recorded rather than resolved: FloCafe pairs billing with a mutable inventory concept, whereas LE31 v1's StockEntry ledger is append-only with no mutable inventory row.** The *inventory-count vs append-only-ledger* reconciliation is an unmade owner decision, not an implementation detail. **Billing additionally triggers a §3.7 review** (money, possibly guest identity). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 defer outcome. Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The value is *naming* a primitive LE31 will need when the first kitchen-display PR lands, plus naming the **dual-surface pairing** with feature 355. Roughly 30 min of documentation; no build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The feature + HANDOFF can be reverted by `git rm`. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass. Build verdict `defer` because: (1) LE31 v1 today is HTMX-waiter + aiogram-cook-bot + append-only StockEntry and has **no kitchen-display surface at all**; (2) TypeScript/Electron is off-stack; (3) the append-only-vs-inventory and offline-sync questions are unmade.

## Bucket

**v1 (offline-first-floor-POS + kitchen-display + receipt/thermal-printer + inventory + billing + self-hosted vocabulary)** — Pick A of Daily Brainstorm 2026-10-21. The *vocabulary* is the value; the code is off-stack.

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts a kitchen-display or receipt-printing surface lands, the files to touch are expected to be:

- `backend/alembic/versions/` — migration adding a `kitchen_display_state` **view** (projection over order state, per feature 347's primitive), not a table.
- `backend/services/kitchen_display_service.py` — new service projecting orders into cook-readable state.
- `backend/services/print_service.py` — new service emitting ESC/POS bytes as a **pure function of an order**, never blocking on the device (composes with feature 348's device-queue shape).
- `backend/main.py` — wire any new sub-app into the parent uvicorn app.
- `frontend/templates/kitchen-display.html` — minimal-HTML/HTMX cook screen.
- `tests/test_kitchen_display_service.py` — unit tests for the projection.
- **Only if the inventory question is answered first:** `backend/services/stock_reconciliation_service.py` — this file should NOT exist until the append-only-vs-mutable-inventory decision is made.

## Verification protocol reference

See `/opt/data/le31_mmm3_research_work/skills/le31-v1-feature-pattern/SKILL.md` for the canonical v1 verification protocol.

## Rollback path

`git rm features/353-FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary.md specs/356-FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary-HANDOFF.md` — documentation-only single revert.

## Mandatory LE31 skill list

When the first v1 PR that adopts a kitchen-display or receipt-printing surface lands, the coding agent must load these skills before starting:

- `le31-conventions` — for the canonical §3.1 / §3.3 / §3.4 / §3.5 / §3.7 charter-invariant review.
- `le31-v1-feature-pattern` — for the canonical v1 feature pattern (HTMX-waiter + aiogram-cook-bot + append-only-StockEntry + Postgres + FastAPI + SQLModel).
- `le31-backend` — for the canonical FastAPI + SQLModel + Postgres + Alembic + append-only-ledger pattern.
- `le31-frontend` — for the canonical minimal-HTML/HTMX + minimal-JS pattern.
- `le31-handoff-spec` — for the canonical HANDOFF-spec format.
- `le31-coding-agent-brief` — for the canonical paste-in-prompt format.

**Read `features/355-Haroon-World-RestaurantPOS-Android-phone-bluetooth-escpos-vocabulary.md` alongside this one** — the two are a deliberate pair (desktop kitchen display vs phone-as-printer over one deterministic kernel), and a PR that implements one without reading the other will likely fork the business logic per surface.