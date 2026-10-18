# HANDOFF — Feature 341: `dashpilot-labs-dashpilot-mcp-mit-doordash-drive-deliveries-over-mcp-quote-dispatch-track-from-your-pos-with-ops-board-and-daily-diagnostics-check-in-v2-ai-mcp-server-for-delivery-aggregator-pos-bridge-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/341-dashpilot-labs-dashpilot-mcp-mit-doordash-drive-deliveries-over-mcp-quote-dispatch-track-from-your-pos-with-ops-board-and-daily-diagnostics-check-in-v2-ai-mcp-server-for-delivery-aggregator-pos-bridge-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-18).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *MCP-server-for-delivery-aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in primitive*, the owner wants *evidence that this delivery-aggregator-MCP-bridge-vocabulary exists in 2026 with the same MCP-as-cross-system-tooling + ops-board + daily-diagnostics-check-in posture*, but struggles because *LE31 has no documented v2-AI delivery-aggregator-MCP-bridge-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (MCP-server-for-delivery-aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in) without specialist help. The 0★/0⑨ with maintainer activity (created 2026-10-04 + pushed 2026-10-07 = IN-WINDOW BY BOTH FIELDS, ~14-day-old repo) makes vocabulary viable, but code adoption is not viable (the MCP-server-for-Delivery-Aggregator-+-POS-bridge stack is off-LE31-stack today; LE31 v2 has no delivery-aggregator surface). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + MCP OFF-STACK (charter §3.4 review needed for v2-AI) + Model-Context-Protocol OFF-STACK + DoorDash OFF-DOMAIN + delivery ✓ ON-PATTERN + POS ✓ ON-STACK + restaurant ✓ ON-STACK. Required data + permissions + infrastructure: Python 3.13 + FastAPI + SQLModel + Postgres + minimal-HTML/HTMX + FastMCP. Rabbit hole: the *MCP-server + DoorDash-Drive + ops-board + daily-diagnostics-check-in* stack is off-LE31-stack (LE31 v2 has no delivery-aggregator surface; v2 charter is owner-pains + AI-assisted, not delivery-aggregator-bridged). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* primitives are §3.4 + §3.7-aligned (MCP-as-cross-system-tooling + observable-evidence + non-AI-fallback + minimal-PII-only-aggregator-API-bridge). The *ops-board + daily-diagnostics-check-in* posture IS the §3.1 *operator-orchestrates-the-aggregator* + §3.3 *append-only-audit-* charter invariant. No §3.4 customer-facing AI. No data rule violation (charter §3.7 PII review needed for the *driver_name + driver_phone* fields). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI defer outcome (delivery-aggregator-MCP-bridge surface for the LE31 v2 owner-pains). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v2-AI surfaces (planned owner-pains + AI-assisted) may adopt the *MCP-as-cross-system-tooling* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable (MCP-server-for-Delivery-Aggregator-+-POS-bridge stack off-LE31-stack today + no v2-AI delivery-aggregator-MCP-bridge surface in v2 charter).

## Bucket

**v2-AI** (MCP-server-for-delivery-aggregator-+-POS-bridge-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 6-tuple-primitive set (MCP-server-for-Delivery-Aggregator-+-POS-bridge + quote-dispatch-track + ops-board + daily-diagnostics-check-in + DoorDash-Drive + restaurant + POS + MCP + Model-Context-Protocol + delivery) + the tech-stack (Python + MCP + Model-Context-Protocol + DoorDash + restaurant + delivery + POS).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `DeliveryAggregatorBridge`, `DeliveryQuote`, `DeliveryDispatch`, `DeliveryEvent`, `DeliveryDailyDiagnostics` tables.
- `backend/services/delivery_aggregator_bridge.py` — new file with `DeliveryAggregatorBridge` class (wraps DoorDash Drive API; supports `quote`, `dispatch`, `track`).
- `backend/services/delivery_daily_diagnostics.py` — new file with `DeliveryDailyDiagnostics` class (overnight check-in; appends to `delivery_daily_diagnostics`).
- `backend/mcp_server_delivery.py` — new file with `McpServerForDelivery` FastMCP sub-app exposing `quote_delivery`, `dispatch_delivery`, `track_delivery` as MCP tools (the §3.4 *MCP-as-cross-system-tooling* posture).
- `frontend/templates/delivery-ops-board.html` — new minimal-HTML/HTMX template for the ops board.
- `backend/main.py` — wire the new sub-app into the parent uvicorn app.
- `tests/test_delivery_aggregator_bridge.py` — new unit test for `DeliveryAggregatorBridge`.
- `tests/integration/test_mcp_delivery.py` — new integration test for `McpServerForDelivery`.
- `cron/delivery_daily_diagnostics.py` — new cron entry for the overnight check-in.

## Verification protocol reference

When the first v2-AI PR that adopts the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline lands, the verification protocol is:

1. Run `pytest tests/test_delivery_aggregator_bridge.py` and verify the `DeliveryAggregatorBridge` produces a valid quote, dispatches the delivery, and tracks the delivery state for the existing LE31 POS sales.
2. Run `pytest tests/integration/test_mcp_delivery.py` and verify the MCP-server exposes the `quote_delivery`, `dispatch_delivery`, `track_delivery` tools correctly.
3. Run `uvicorn backend.main:app` and curl the MCP-server endpoint to verify the tools are callable.
4. Open `frontend/templates/delivery-ops-board.html` in a browser and verify the ops board renders the delivery state as a navigable table.
5. Inspect the `DeliveryEvent` table in Postgres and verify every delivery-state-transition is recorded (the §3.3 append-only-ledger invariant).
6. Run the `cron/delivery_daily_diagnostics.py` overnight check-in and verify the `DeliveryDailyDiagnostics` table is populated.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the five tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.
5. Remove the `cron/delivery_daily_diagnostics.py` entry from the cron schedule.

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

This defer artifact is documentation only. It becomes a build trigger when the **first v2-AI PR that adds a delivery-aggregator-MCP-bridge surface to the LE31 v2 owner-pains** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which delivery aggregator (DoorDash Drive, Wolt, UberEats, Deliveroo) becomes the first `DeliveryAggregatorBridge`.
3. Decide which LE31 surface (cook Telegram bot? owner daily-recap?) consumes the `DeliveryEvent` append-only-ledger.
4. Apply charter §3.7 PII review to the *driver_name + driver_phone* fields before any v2-AI PR.
5. Adopt the *MCP-server-for-delivery-aggregator-+-POS-bridge + ops-board + daily-diagnostics-check-in* discipline on the chosen surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v2-AI code is shipped.