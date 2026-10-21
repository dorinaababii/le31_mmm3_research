# HANDOFF — Feature 355: `Haroon-World-RestaurantPOS-Android-phone-bluetooth-escpos-vocabulary`

**Upstream source repo: [`Haroon-World/RestaurantPOS_Android`](https://github.com/Haroon-World/RestaurantPOS_Android)** — see `features/355-Haroon-World-RestaurantPOS-Android-phone-bluetooth-escpos-vocabulary.md` for the full evidence record.

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/355-Haroon-World-RestaurantPOS-Android-phone-bluetooth-escpos-vocabulary.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-21).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface asks "what happens when the tablet dies mid-service", the owner wants *a proven shape where the operator device degrades to a printer and the transaction still commits*, but struggles because *LE31's HTMX waiter UI and aiogram cook bot both assume a working screen and a reachable network*. |
| 2 | Viability | ✓ | "Phone is the till, it prints over Bluetooth, it works with no network" is comprehensible without specialist help. **MIT ✓ §3.2 STRICTLY-COMPATIBLE**, 129 KB, **Python ✓ ON-STACK**. **Traction caveat recorded plainly: ★1/⑂0 is NOT evidence of adoption and NOT evidence of failure** — it is a hobby-shaped repo that names a real shape; the pick is about the shape. |
| 3 | Practicability and confidence | ✓ | **Python ✓ ON-STACK + SQLite (local-tier analogue of the v1 Postgres)** + ESC/POS (protocol is not copyrightable, fully reusable). Kivy/Buildozer are **NOT** in the LE31 stack and would be additions. Evidence strength: medium-high for the vocabulary; **very low for urgency**. |
| 4 | Conflict | ✓ | Does not violate any invariant. Phone-first + deterministic-kernel + hardware-as-output are §3.1/§3.4/§3.5-aligned. **⚠️ TENSION RECORDED: LE31 v1's cook is already a Telegram bot (aiogram v3). A native phone app for the waiter creates a THIRD client alongside the HTMX waiter and the Telegram cook. The §3.1 two-role surface discipline argues against adding a third client without an owner decision.** Unmade; recorded, not resolved. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 defer outcome. Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | Two contributions: (a) the **mobile half of the dual-surface pair with feature 353**; (b) the **strongest local-authoritative data point on file** for the offline-sync question that features 347, 348, 349 and 353 all brush against without naming. Roughly 30 min of documentation; no build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. Documentation-only revert via `git rm`. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass. Build verdict `defer` because: (1) HTMX is the charter's waiter surface and nothing argues for revisiting it; (2) Bluetooth ESC/POS requires a physical printer, which is procurement before engineering; (3) the third-client tension is unresolved; (4) ★1/⑂0 gives no traction evidence either way.

## Bucket

**v1 (phone-first POS + Bluetooth ESC/POS thermal printing + offline SQLite + single-language-Python-app vocabulary)** — Pick C of Daily Brainstorm 2026-10-21. The *ESC/POS byte protocol* is the reusable part (not copyrightable); the app is the reference.

## Files to touch

**None today.** The defer artifact is documentation only.

When the first PR that proposes printer output of any kind lands, the files to touch are expected to be:

- `backend/services/print_service.py` — **shared with feature 353's HANDOFF, and deliberately the same file.** ESC/POS emission is a **pure function of an order**: it produces bytes, never blocks on a device, and knows nothing about Bluetooth or USB. The transport is a separate concern.
- `backend/services/device_queue.py` — new device queue, composing with feature 348's *ESC/POS-byte-emit-to-device-queue* primitive.
- `backend/alembic/versions/` — only if local-authoritative offline is chosen: a local SQLite tier. **Do not create this until the offline-sync question (feature 353, Open question 2) is answered.**
- `tests/test_print_service.py` — must assert that `print_service` performs **no I/O** and returns bytes.
- **NOT to be created today:** any Kivy/Buildozer/Android packaging, any Bluetooth driver code, any third-client surface.

## Verification protocol reference

See `/opt/data/le31_mmm3_research_work/skills/le31-v1-feature-pattern/SKILL.md` for the canonical v1 verification protocol.

## Rollback path

`git rm features/355-Haroon-World-RestaurantPOS-Android-phone-bluetooth-escpos-vocabulary.md specs/358-Haroon-World-RestaurantPOS-Android-phone-bluetooth-escpos-vocabulary-HANDOFF.md` — documentation-only single revert.

## Mandatory LE31 skill list

When the first PR that proposes printer output lands, the coding agent must load these skills before starting:

- `le31-conventions` — for the canonical §3.1 / §3.4 / §3.5 charter-invariant review.
- `le31-v1-feature-pattern` — for the canonical v1 feature pattern (HTMX-waiter + aiogram-cook-bot + append-only-StockEntry + Postgres + FastAPI + SQLModel).
- `le31-backend` — for the canonical FastAPI + SQLModel + Postgres + Alembic + append-only-ledger pattern.
- `le31-frontend` — for the canonical minimal-HTML/HTMX + minimal-JS pattern.
- `le31-handoff-spec` — for the canonical HANDOFF-spec format.
- `le31-coding-agent-brief` — for the canonical paste-in-prompt format.

**Read `features/353-FreeOpenSourcePOS-FloCafe-offline-first-floor-pos-vocabulary.md` alongside this one.** The two are a deliberate pair (desktop kitchen display vs phone-as-printer over one deterministic kernel). The shared `print_service.py` boundary in this HANDOFF is only correct if both are read; implementing one alone will fork the business logic per surface, which is the exact failure mode the pair exists to prevent.