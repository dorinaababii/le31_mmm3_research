# Pick B — `Pizzylee001/Covers` — v1 restaurant-real-time-walk-in-triage-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/267-Pizzylee001-Covers-mit-nextjs-html-real-time-restaurant-occupancy-from-live-blackbird-check-ins-v1-restaurant-realtime-walk-in-triage-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v1 PR that adds a `WalkInTriage` SQLModel table (`triage_id, restaurant_id, neighborhood_id, observed_at, occupancy_pct, source_kind`).
2. First v1 PR that adds a `BlackbirdCheckIn` SQLModel table (`check_in_id, restaurant_id, check_in_payload_json, available_at`).
3. First v1 PR that adds a `NeighborhoodAggregation` SQLModel table (`aggregation_id, neighborhood_id, observed_at, occupancy_avg_json`) for the *neighborhood-aggregation* discipline.
4. First v1 PR that adds an `/api/walk-in-triage` + `/api/walk-in-triage/<triage_id>` + `/api/blackbird-check-ins` + `/api/neighborhood-aggregations` FastAPI endpoint set.
5. First v1 PR that adds a `walk-in-triage.html` minimal-HTML/HTMX template that renders *live-restaurant-occupancy + Blackbird-check-ins + real-time + neighborhood-aggregation*.
6. First v1 PR that adds an SSE/WebSocket-FastAPI-endpoint that streams *live-restaurant-occupancy* feed.
7. First v1 PR that adds a `walk-in-triage-cron` that ingests *Blackbird-check-ins* into the existing `audit_logs` schema.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v1 surface wants to **add live-restaurant-occupancy + Blackbird-check-ins + real-time + neighborhood-aggregation** to the existing FastAPI + Postgres + SQLModel stack (e.g., a v1 surface that lets a hostess answer the call 'is the restaurant busy right now?' with a real-time signal from external check-ins), the hostess wants a known-good live-restaurant-occupancy-from-external-check-ins blueprint with Next.js + Vercel + Blackbird-check-ins + neighborhood-aggregation posture, but LE31 today has no walk-in-triage + no live-restaurant-occupancy + no Blackbird-check-ins-integration, so that any future v1 extension has a documented reference."* — PASS (links to features 02 + 03 + 09 + 22 + 116 + 152 + 175 + 187 + 195 + 201 + 205 + 218 + 220 + 221 + 222 + 223 + 224 + 225 + 232 + 236 + 237 + 239 + 240 + 242 + 243 + 244 + 246 + 248 + 251 + 254 + 255 + 256 + 257 + 258 + 259 + 260 + 261 + 262 + 263 + 264 + 265 + 266; justifies a new v1 pain).
2. **Viability** — Hostess does not need to understand the implementation; they only see the *live-restaurant-occupancy + Blackbird-check-ins + real-time + neighborhood-aggregation* surface on the existing minimal-HTML/HTMX walk-in-triage page. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 N/A (no AI surface); confidence **high** for vocabulary transferability, **low** for immediate LE31 v1 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is data-display + no-AI-surface; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v1** outcome (cross-section to features 02+03+09+22+116+152+175+187+195+201+205+218+220+221+222+223+224+225+232+236+237+239+240+242+243+244+246+248+251+254+255+256+257+258+259+260+261+262+263+264+265+266). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = low-medium (~50-100 lines of SQLModel + FastAPI + minimal-HTML/HTMX + SSE/WebSocket code; 3-5 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/walk_in_triage.py` (new) — `WalkInTriage` + `BlackbirdCheckIn` + `NeighborhoodAggregation` SQLModel tables
- `le31/app/services/walk_in_triage.py` (new) — service layer for `record_walk_in_triage` + `record_blackbird_check_in` + `record_neighborhood_aggregation` + `verify_walk_in_triage`
- `le31/app/hermes/hooks/walk_in_triage_recording.py` (new) — Hermes Agent hook integration that records every Blackbird-check-in as an immutable row in `audit_logs` (operator-tooling only; **NO customer-facing AI per charter §3.4**)
- `le31/app/walk_in_triage.py` (new) — walk-in-triage primitive (FastAPI-SSE-or-WebSocket + minimal-HTML/HTMX; **no-AI-surface + operator-tooling-only per charter §3.4**)
- `le31/app/api/v1/walk_in_triage.py` (new) — HTTP endpoints: `GET /api/walk-in-triage` + `POST /api/walk-in-triage` + `GET /api/walk-in-triage/<triage_id>` + `GET /api/blackbird-check-ins` + `POST /api/blackbird-check-ins` + `GET /api/neighborhood-aggregations` + `POST /api/neighborhood-aggregations` + `GET /api/walk-in-triage/sse` (SSE live-feed)
- `le31/app/owner_dashboard/templates/walk_in_triage.html` (new) — minimal-HTML/HTMX owner-dashboard template for walk-in-triage (note: NO Next.js + Vercel; LE31 v1 uses minimal HTML + HTMX)
- `le31/migrations/versions/<revision>_walk_in_triage.py` (new) — Alembic migration for the three new tables + the `triage_id` + `triage_source` columns on `audit_logs`

## Verification protocol reference

- Run `pytest le31/tests/test_walk_in_triage.py -v` to verify the new tables + endpoints + minimal-HTML/HTMX template
- Run `pytest le31/tests/test_audit_logs_walk_in_triage_integration.py -v` to verify the audit_logs-walk_in_triage integration
- Run `pytest le31/tests/test_blackbird_check_ins_ingest.py -v` to verify the Blackbird-check-ins-ingest discipline
- Run `pytest le31/tests/test_charter_3_4_no_customer_facing_ai.py -v` to verify §3.4 no-customer-facing-AI invariant
- Run `pytest le31/tests/test_sse_live_feed.py -v` to verify the SSE live-feed discipline

## Rollback path

- Revert the SQLModel migration: `alembic downgrade -1`
- Delete the three new model files (`le31/app/models/walk_in_triage.py` + `le31/app/services/walk_in_triage.py` + `le31/app/hermes/hooks/walk_in_triage_recording.py` + `le31/app/walk_in_triage.py` + `le31/app/api/v1/walk_in_triage.py` + `le31/app/owner_dashboard/templates/walk_in_triage.html` + `le31/migrations/versions/<revision>_walk_in_triage.py`)
- Revert the `audit_logs` table changes (drop `triage_id` + `triage_source` columns)
- Restart the FastAPI server

## Mandatory LE31 skill list

- `le31-conventions` (charter §3.1 + §3.2 + §3.3 + §3.4 + §3.6 + §3.7 invariants; seven-check feature gate)
- `le31-feature-pipeline` (vocabulary-to-build pipeline + parking-lot-vs-build decision)
- `le31-handoff-spec` (slice contract format)
- `le31-coding-agent-brief` (paste-in prompt for coding agent)
- `le31-backend` (FastAPI + SQLModel + Postgres + Alembic + aiogram v3 + SSE/WebSocket)
- `le31-frontend` (minimal-HTML/HTMX + waiter-web-UI + cook-Telegram-bot)
- `le31-data` (audit_logs schema + StockEntry schema + Order.status schema)
- `le31-research` (vocabulary-reference discipline)
- `le31-v1-feature-pattern` (vocabulary-to-build-trigger patterns)

## Anti-fabrication canary

- `grep -cF 'LE31' /opt/data/le31_mmm3_research_work/features/267-...md` = 0 matches — PASS (vocabulary-only artifact; the *LE31* mentions are charter-references not file-rename literals)
- `grep -cF 'Pizzylee001/Covers' /opt/data/le31_mmm3_research_work/features/267-...md /opt/data/le31_mmm3_research_work/specs/267-...-HANDOFF.md` = 1 match each — PASS (the *Pizzylee001/Covers* references are GitHub-repo-references not LE31-imports)

## Charter compatibility

§3.1 ALIGNED (Python + FastAPI + Postgres + live-restaurant-occupancy + Blackbird-check-ins + real-time + neighborhood-aggregation = single-restaurant + single-hostess posture match; the Next.js + Vercel frontend is OFF-pattern for v1 today but the *live-restaurant-occupancy + Blackbird-check-ins + real-time + neighborhood-aggregation* discipline IS transferable to LE31 v1 + v2 + v2-AI surfaces); §3.2 STRICTLY-COMPATIBLE (MIT permissive + 2★/0⑂ + 41 KB modest + 14-day-old + pushed-11-days-ago + IN-WINDOW BY BOTH FIELDS = strongest walk-in-triage-vocabulary signal of the 3 picks); §3.3 N/A (the *real-time + walk-in-triage* discipline does not affect the *append-only-StockEntry* charter §3.3 invariant; the artifact is vocabulary-only); §3.4 N/A (no AI surface; pure data-display + no-customer-facing-AI + no-operator-facing-AI; the artifact is vocabulary-only); §3.6 N/A (no money primitive change; the *live-restaurant-occupancy + Blackbird-check-ins* discipline does not affect the *EUR-values* charter §3.6 invariant); §3.7 N/A (no privacy primitive change; the *Blackbird-check-ins* source IS public-data; no PII collected).