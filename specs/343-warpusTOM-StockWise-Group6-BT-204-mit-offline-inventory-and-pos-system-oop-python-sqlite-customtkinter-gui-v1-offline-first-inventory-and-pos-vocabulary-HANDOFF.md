# HANDOFF — Feature 343: `warpusTOM-StockWise-Group6-BT-204-mit-offline-inventory-and-pos-system-oop-python-sqlite-customtkinter-gui-v1-offline-first-inventory-and-pos-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/343-warpusTOM-StockWise-Group6-BT-204-mit-offline-inventory-and-pos-system-oop-python-sqlite-customtkinter-gui-v1-offline-first-inventory-and-pos-vocabulary.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-18).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v1 surface proposes an *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI primitive*, the owner wants *evidence that this offline-first-inventory-and-POS-vocabulary exists in 2026 with the same offline-first + OOP-Python + SQLite + CustomTkinter-GUI posture*, but struggles because *LE31 has no documented v1 offline-first-inventory-and-POS-vocabulary reference*, so that *the v1 surface can be defended with "this is what an independent maintainer shipped in 2026 with the same offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI) without specialist help. The 0★/0⑨ + 26312 KB substantial = THE LARGEST in-window brainstorm-vocabulary pick of the 80-pass series with maintainer activity (created 2026-09-27 + pushed 2026-09-27 = IN-WINDOW BY BOTH FIELDS, ~21-day-old repo) makes vocabulary viable, but code adoption is not viable (the offline-first + SQLite + CustomTkinter stack is off-§3.5 unless explicit charter-decision is made; LE31 v1 has no offline-first-inventory-and-POS surface). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + SQLite OFF-§3.5 (offline-first-SQLite charter-decision needed for v1) + CustomTkinter OFF-§3.1 (desktop-GUI charter-decision needed) + inventory-management ✓ ON-PATTERN + POS ✓ ON-STACK. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX + sqlite3 (stdlib) + customtkinter (desktop GUI). Rabbit hole: the *offline-first + SQLite + CustomTkinter* stack is off-LE31-stack (LE31 v1 is online + Postgres + minimal-HTML/HTMX; charter §3.5 review needed for any v1 PR that adopts this discipline). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* primitives are §3.5 + §3.1-aligned (offline-first + explicit-state-transitions + sync-to-central-server-when-network-available). The *offline-first + SQLite* posture IS the §3.5 *offline-first-SQLite* charter invariant (charter-decision needed). The *CustomTkinter-GUI* posture is OFF-§3.1 (charter-decision needed). No §3.4 customer-facing AI. No data rule violation. |
| 5 | Outcome + appetite + scope | ✓ | Maps to v1 polish outcome (offline-first-inventory-and-POS for the LE31 feature 03 `kitchen-stock-tracker`). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v1 surfaces (feature 03 `kitchen-stock-tracker` + feature 39 `owner-daily-recap-telegram`) may adopt the *offline-first + SQLite + sync-to-central-Postgres* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (offline-first + SQLite + CustomTkinter stack off-§3.5 unless explicit charter-decision is made + no v1 offline-first-inventory-and-POS surface in v1 charter).

## Bucket

**v1** (offline-first-inventory-and-POS-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 6-tuple-primitive set (offline-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI + inventory-management + POS) + the tech-stack (Python + SQLite + CustomTkinter + inventory-management + POS).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `Product`, `InventoryItem`, `Sale`, `InventoryEvent` tables in the central Postgres (the local SQLite is the offline-first layer; the central Postgres is the source-of-truth).
- `backend/services/offline_first_sync.py` — new file with `OfflineFirstSync` class (syncs local SQLite to central Postgres when network is available).
- `backend/services/inventory_management.py` — new file with `InventoryManagement` class (OOP Python; wraps the `InventoryItem` + `InventoryEvent` tables).
- `backend/main.py` — wire the new service into the existing feature 03 `kitchen-stock-tracker` surface.
- `frontend/templates/inventory-dashboard.html` — new minimal-HTML/HTMX template for the inventory dashboard (if §3.5 *online-first-HTML* posture is kept) OR `desktop/inventory_app.py` — new file with CustomTkinter GUI (if §3.5 *offline-first-CustomTkinter* posture is adopted).
- `tests/test_offline_first_sync.py` — new unit test for `OfflineFirstSync`.
- `tests/test_inventory_management.py` — new unit test for `InventoryManagement`.

## Verification protocol reference

When the first v1 PR that adopts the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline lands, the verification protocol is:

1. Run `pytest tests/test_offline_first_sync.py` and verify the `OfflineFirstSync` syncs local SQLite to central Postgres correctly.
2. Run `pytest tests/test_inventory_management.py` and verify the `InventoryManagement` produces valid `InventoryItem` + `InventoryEvent` records.
3. Run `uvicorn backend.main:app` and curl the inventory endpoint to verify the inventory state matches the local SQLite.
4. Open the CustomTkinter GUI (if adopted) and verify the inventory state renders correctly.
5. Disconnect the network and verify the offline-first-POS continues to record sales locally.
6. Reconnect the network and verify the local SQLite syncs to central Postgres correctly.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v1 PR that adopts the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the four tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules.
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `skills/le31-frontend/SKILL.md` — for the frontend conventions (if applicable).
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v1 PR that adds an offline-first surface to the LE31 feature 03 `kitchen-stock-tracker`** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide whether to ship CustomTkinter desktop GUI (charter §3.5 review) or minimal-HTML/HTMX web GUI (charter §3.1 aligned).
3. Decide whether to ship single-shop (LE31 v1 charter) or multi-shop (charter-decision needed).
4. Adopt the *offline-first-inventory-+-POS-system + OOP-Python + SQLite + CustomTkinter-GUI* discipline on the feature 03 `kitchen-stock-tracker` surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v1 code is shipped.