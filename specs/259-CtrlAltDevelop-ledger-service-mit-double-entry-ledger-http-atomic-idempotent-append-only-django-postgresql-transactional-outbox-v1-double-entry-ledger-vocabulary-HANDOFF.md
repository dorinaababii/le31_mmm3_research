# Pick C — `CtrlAltDevelop/ledger-service` — v1 double-entry-ledger-vocabulary — HANDOFF

> **Slice contract** for the coding agent. Trigger only when the trigger condition below fires; today is **`defer (parking-lot, vocabulary reference)`**.

## Active feature path

`/opt/data/le31_mmm3_research_work/features/259-CtrlAltDevelop-ledger-service-mit-double-entry-ledger-http-atomic-idempotent-append-only-django-postgresql-transactional-outbox-v1-double-entry-ledger-vocabulary.md`

## Trigger condition

The slice is **not** a build today. It becomes a build when **any** of the following fires:
1. First v1 PR that adds a `LedgerEntry` SQLModel table (or extends the existing `StockEntry` schema with double-entry columns).
2. First v1 PR that adds an `IdempotencyKey` SQLModel table + FastAPI idempotency middleware that hashes the request body + the `Idempotency-Key` header and returns the cached response if the hash matches a prior request.
3. First v1 PR that adds a `TransactionalOutbox` SQLModel table + outbox-drain worker.
4. First v1 PR that adds a `/ledger-outbox count` / `/ledger-outbox drain` / `/ledger-outbox replay <outbox_id>` Telegram command set on the cook-bot (operator-tooling only; **Telegram-client exposure to restaurant diners requires explicit §3.4 review**).
5. First v1 PR that extends the existing `StockEntry.amount_eur` column to use Python's `decimal.Decimal` type instead of `float` (charter §3.6 hard invariant).

## Seven-check gate verdict (per `le31-conventions/SKILL.md`)

1. **Raison d'être / JTBD** — *"When the owner closes a shift, they want a clear string view of expected vs counted cash + per-payment-method breakdown + variance explanation, but struggle because the existing v1 reconciliation surface (feature 05 + 06 + 09) computes tip derived but does not enforce double-entry + idempotency + transactional-outbox on the reconciliation writes, so that the shift-close HTTP endpoint is race-safe and every ledger entry is committed in the same DB transaction as the operation that produced it."* — PASS (links to feature 05 + 06 + 09 + 74; justifies a new pain)
2. **Viability** — Owner + staff do not need to understand the implementation; they only see the close-shift + reconcile-cash UI outputs. PASS.
3. **Practicability and confidence** — MIT permissive (charter §3.2 STRICTLY-COMPATIBLE); §3.4 not triggered (no AI surface); confidence **high** for mechanism (stack-adjacent; same operational envelope), **medium** for present LE31 urgency. PASS.
4. **Conflict** — None detected. The vocabulary is operator-tooling only; §3.1 explicit-state-transitions preserved; §3.6 money primitives preserved (Decimal). PASS.
5. **Outcome, appetite, and scope** — **v1** outcome (cross-section to features 03+05+06+09+74+75+78+121+170+172). Appetite = zero today (parking-lot). PASS.
6. **Cost to operational value** — Pain frequency/severity = low today; pain is forecast for v1 release era when multiple waiters may attempt to close the same shift. Implementation cost = low-medium (~50-100 lines of SQLModel + idempotency-middleware code; 1-2 days when triggered). PASS.
7. **Circuit breaker and reversibility** — Fully reversible (vocabulary-only artifact; no code shipped today). PASS.

**Decision: defer (parking-lot, vocabulary reference).** No build today.

## Files to touch (when triggered)

- `le31/app/models/ledger.py` (new) — `LedgerEntry` + `IdempotencyKey` + `TransactionalOutbox` SQLModel tables
- `le31/app/middleware/idempotency.py` (new) — FastAPI idempotency middleware that hashes the request body + the `Idempotency-Key` header and returns the cached response if the hash matches a prior request
- `le31/app/services/ledger.py` (new) — service layer for `record_ledger_entry` + `get_idempotency_key` + `drain_outbox` + `replay_outbox_entry`
- `le31/app/workers/outbox_drain.py` (new) — outbox-drain worker that reads the `TransactionalOutbox` table and dispatches the events to downstream systems (notifications queue, billing system, external accounting system)
- `le31/app/api/v1/shifts.py` (modify) — extend the existing close-shift endpoint with `Idempotency-Key` header support + transactional-outbox write
- `le31/app/api/v1/ledger.py` (new) — HTTP endpoints: `GET /api/ledger/entries` + `GET /api/ledger/entries/<entry_id>` + `GET /api/ledger/outbox` + `POST /api/ledger/outbox/drain` + `POST /api/ledger/outbox/replay/<outbox_id>`
- `le31/app/cook_bot/handlers/ledger.py` (new) — Telegram command handlers: `/ledger-outbox count` + `/ledger-outbox drain` + `/ledger-outbox replay <outbox_id>` (operator-tooling only; NOT customer-facing)
- `le31/migrations/versions/<revision>_ledger.py` (new) — Alembic migration for the three new tables
- `skills/le31-conventions/SKILL.md` — append the *double-entry + atomic + idempotent + transactional-outbox* posture as a §3.1-aligned pattern

## Verification protocol reference

- Per `le31-v1-feature-pattern/SKILL.md` Definition of Done: the specified user completes the flow on the intended surface; resulting rows and derived values are inspected; forbidden and duplicate actions are safe; promised feedback appears; the regression gap was demonstrated where applicable; docs/status match reality; the change is committed and pushed.
- Per `le31-coding-agent-brief/SKILL.md`: the coding-agent-brief skill produces the paste-in prompt automatically from this slice contract; do not paste chat excerpts.
- Per `le31-feature-pipeline/SKILL.md`: the contract must be sufficient for the coding agent to start without asking; the commit and push to the branch named in the skill config (default: main) must be confirmed.

## Rollback path

- **Revert the Alembic migration** (`alembic downgrade -1`) to drop the three new tables
- **Revert the idempotency middleware** (remove the `le31/app/middleware/idempotency.py` file + remove the registration from `le31/app/main.py`)
- **Revert the outbox-drain worker** (remove the `le31/app/workers/outbox_drain.py` file + remove the worker registration from `le31/app/main.py`)
- **Revert the HTTP endpoints** (remove the `le31/app/api/v1/ledger.py` file + remove the import from `le31/app/api/v1/__init__.py`; revert the `le31/app/api/v1/shifts.py` modifications)
- **Revert the Telegram command handlers** (remove the `le31/app/cook_bot/handlers/ledger.py` file + remove the registration from `le31/app/cook_bot/handlers/__init__.py`)
- **No data loss** if the rollback happens BEFORE any ledger-entry or idempotency-key or outbox rows are written
- **Full data retention** if the rollback happens AFTER rows are written (the three tables are dropped but the ledger-entry rows are preserved in `audit_logs` per the *append-only* invariant)

## Mandatory LE31 skill list

- `le31-conventions` (always)
- `le31-feature-pipeline` (when handoff is triggered)
- `le31-v1-feature-pattern` (when v1 implementation triggered)
- `le31-coding-agent-brief` (when the coding agent is invoked)
- `speckit-specify` + `speckit-plan` + `speckit-tasks` + `speckit-implement` (when a full spec/plan/tasks/implement cycle is needed)
- `pre-merge-review` (mandatory before merge per the operating-principles)

## Parent research issue

[linear: blocked] (workspace plan-limit error — 12th consecutive day; verified today via `save_issue` write-probe with requestId `a4396da65c72d371`; parent fallback at `/opt/data/le31-daily-research-2026-10-01.linear-fallback.json`)