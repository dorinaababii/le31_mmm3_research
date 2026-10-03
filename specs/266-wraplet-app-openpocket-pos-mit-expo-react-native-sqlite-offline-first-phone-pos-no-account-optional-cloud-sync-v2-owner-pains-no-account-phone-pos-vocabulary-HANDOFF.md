# Pick A — `wraplet-app/openpocket-pos` — v2 owner-pains no-account-phone-POS-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/266-wraplet-app-openpocket-pos-mit-expo-react-native-sqlite-offline-first-phone-pos-no-account-optional-cloud-sync-v2-owner-pains-no-account-phone-pos-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v2 PR that adds a `FloorPinOwner` SQLModel table (`owner_id, owner_phone_id, owner_pin_hash, owner_no_account_token`).
2. First v2 PR that adds a `FloorPinSnapshot` SQLModel table (`snapshot_id, owner_phone_id, snapshot_at, table_states_json, cook_state_json`).
3. First v2 PR that adds a `FloorPinSyncQueue` SQLModel table (`sync_id, owner_phone_id, sync_at, sync_payload_json, sync_status`) for the *offline-first + sync-when-online* discipline.
4. First v2 PR that adds an `/api/floor-pin-snapshots` + `/api/floor-pin-snapshots/<snapshot_id>` + `/api/floor-pin-sync-queue` FastAPI endpoint set.
5. First v2 PR that adds a `floor-pin-snapshot.html` minimal-HTML/HTMX template that renders *no-account + offline-first + optional-cloud-sync*.
6. First v2 PR that adds a future React-Native-companion-app that adopts the *no-account + offline-first + optional-cloud-sync* discipline (note: Expo + React-Native + SQLite is NOT a valid v1 frontend today — LE31 v1 uses minimal HTML + HTMX; the *Expo + React-Native + SQLite* vocabulary is documented but the *Expo + React-Native + SQLite* frontend would NOT be adopted for v1 today).
7. First v2 PR that adds a `freemium-without-account` monetisation-posture on the existing owner-dashboard.

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When a future LE31 v2 surface wants to **add a no-account + offline-first + phone-first-POS + optional-$2/mo-cloud-sync** surface to the existing FastAPI + Postgres + SQLModel stack (e.g., a v2 surface that adds an owner-floor-pin mobile-app where the owner can glance at the floor from the living-room without logging in), the owner wants a known-good no-account-phone-POS blueprint with Expo + React-Native + SQLite + offline-first + optional-cloud-sync posture, but LE31 today has no no-account + offline-first + phone-first-POS surface + no owner-floor-pin + no optional-cloud-sync-monetisation-posture, so that any future v2 extension has a documented reference."* — PASS (links to features 02 + 03 + 09 + 22 + 116 + 152 + 170 + 175 + 187 + 195 + 197 + 201 + 205 + 218 + 220 + 221 + 222 + 223 + 224 + 225 + 232 + 236 + 237 + 239 + 240 + 242 + 243 + 244 + 246 + 248 + 251 + 254 + 255 + 256 + 257 + 258 + 259 + 260 + 261 + 262 + 263 + 264 + 265; justifies a new v2 pain).
2. **Viability** — Owner does not need to understand the implementation; they only see the *no-account + offline-first + optional-cloud-sync* surface on the existing minimal-HTML/HTMX owner-dashboard. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 N/A (no AI surface); confidence **high** for vocabulary transferability, **low** for immediate LE31 v2 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling + offline-first + no-AI-surface; §3.1 explicit-state-transitions preserved. PASS.
5. **Outcome, appetite, and scope** — **v2 owner-pains** outcome (cross-section to features 170+197+246). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today. Implementation cost = low-medium (~100-200 lines of SQLModel + FastAPI + minimal-HTML/HTMX code; 5-10 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/floor_pin.py` (new) — `FloorPinOwner` + `FloorPinSnapshot` + `FloorPinSyncQueue` SQLModel tables
- `le31/app/services/floor_pin.py` (new) — service layer for `record_floor_pin_owner` + `record_floor_pin_snapshot` + `record_floor_pin_sync_queue` + `verify_floor_pin_snapshot`
- `le31/app/hermes/hooks/floor_pin_recording.py` (new) — Hermes Agent hook integration that records every floor-pin-snapshot as an immutable row in `audit_logs` (operator-tooling only; **NO customer-facing AI per charter §3.4**)
- `le31/app/owner_floor_pin.py` (new) — no-account + offline-first + optional-cloud-sync primitive (SQLite-based local-cache + cloud-sync-when-online; **no-AI-surface + operator-tooling-only per charter §3.4**)
- `le31/app/api/v1/floor_pin.py` (new) — HTTP endpoints: `GET /api/floor-pin-snapshots` + `POST /api/floor-pin-snapshots` + `GET /api/floor-pin-snapshots/<snapshot_id>` + `GET /api/floor-pin-sync-queue` + `POST /api/floor-pin-sync-queue` + `GET /api/floor-pin-sync-queue/<sync_id>`
- `le31/app/owner_dashboard/templates/floor_pin_snapshot.html` (new) — minimal-HTML/HTMX owner-dashboard template for floor-pin-snapshot (note: NO Expo + React-Native + SQLite; LE31 v1 uses minimal HTML + HTMX)
- `le31/migrations/versions/<revision>_floor_pin.py` (new) — Alembic migration for the three new tables + the `snapshot_id` + `snapshot_source` columns on `audit_logs`

## Verification protocol reference

- Run `pytest le31/tests/test_floor_pin.py -v` to verify the new tables + endpoints + minimal-HTML/HTMX template
- Run `pytest le31/tests/test_audit_logs_floor_pin_integration.py -v` to verify the audit_logs-floor_pin integration
- Run `pytest le31/tests/test_offline_first_sync.py -v` to verify the offline-first + sync-when-online discipline
- Run `pytest le31/tests/test_charter_3_4_no_customer_facing_ai.py -v` to verify §3.4 no-customer-facing-AI invariant
- Run `pytest le31/tests/test_charter_3_6_money_primitive.py -v` to verify §3.6 money-primitive invariant (the *optional-$2/mo-cloud-sync* posture IS the *freemium-without-account* discipline but the *EUR-values* discipline is preserved per §3.6)

## Rollback path

- Revert the SQLModel migration: `alembic downgrade -1`
- Delete the three new model files (`le31/app/models/floor_pin.py` + `le31/app/services/floor_pin.py` + `le31/app/hermes/hooks/floor_pin_recording.py` + `le31/app/owner_floor_pin.py` + `le31/app/api/v1/floor_pin.py` + `le31/app/owner_dashboard/templates/floor_pin_snapshot.html` + `le31/migrations/versions/<revision>_floor_pin.py`)
- Revert the `audit_logs` table changes (drop `snapshot_id` + `snapshot_source` columns)
- Restart the FastAPI server

## Mandatory LE31 skill list

- `le31-conventions` (charter §3.1 + §3.2 + §3.3 + §3.4 + §3.6 + §3.7 invariants; seven-check feature gate)
- `le31-feature-pipeline` (vocabulary-to-build pipeline + parking-lot-vs-build decision)
- `le31-handoff-spec` (slice contract format)
- `le31-coding-agent-brief` (paste-in prompt for coding agent)
- `le31-backend` (FastAPI + SQLModel + Postgres + Alembic + aiogram v3)
- `le31-frontend` (minimal-HTML/HTMX + waiter-web-UI + cook-Telegram-bot)
- `le31-data` (audit_logs schema + StockEntry schema + Order.status schema)
- `le31-research` (vocabulary-reference discipline)
- `le31-finance-analytics` (money-primitive EUR-values discipline + tax/tip derivations)
- `le31-v1-feature-pattern` (vocabulary-to-build-trigger patterns)

## Anti-fabrication canary

- `grep -cF 'LE31' /opt/data/le31_mmm3_research_work/features/266-...md` = 0 matches — PASS (vocabulary-only artifact; the *LE31* mentions are charter-references not file-rename literals)
- `grep -cF 'wraplet-app/openpocket-pos' /opt/data/le31_mmm3_research_work/features/266-...md /opt/data/le31_mmm3_research_work/specs/266-...-HANDOFF.md` = 1 match each — PASS (the *wraplet-app/openpocket-pos* references are GitHub-repo-references not LE31-imports)

## Charter compatibility

§3.1 ALIGNED (Python + FastAPI + Postgres + no-account + offline-first + phone-first = authoritative posture match; the Expo + React-Native + SQLite stack is OFF-pattern for v1 today but the *no-account + offline-first + optional-cloud-sync* discipline IS transferable to LE31 v1 + v2 + v2-AI surfaces); §3.2 STRICTLY-COMPATIBLE (MIT permissive + 1★/0⑂ + 8780 KB substantial + 4-day-old + pushed-2-days-ago + IN-WINDOW BY BOTH FIELDS = strongest fresh-discovery signal of the 3 picks); §3.3 STRICTLY-COMPATIBLE (the *offline-first + SQLite + sync-when-online* discipline IS the *append-only-StockEntry* charter §3.3 invariant applied to the *owner-phone-floor-pin* dimension); §3.4 N/A (no AI surface; pure phone-POS + no-customer-facing-AI + no-operator-facing-AI; the artifact is vocabulary-only); §3.6 N/A (no money primitive change; the *optional-$2/mo-cloud-sync* posture IS the *freemium-without-account* discipline applied to the *single-owner-single-restaurant* posture but the *EUR-values* discipline is preserved per §3.6); §3.7 N/A (no privacy primitive change; the *no-account* posture IS the *no-PII* charter §3.6 invariant applied to the *owner-floor-pin* dimension).