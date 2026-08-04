# Feature 30 — Append-Only Audit Redirect

> **Priority**: P2 · **Effort**: S (1–2 days) · **Source**: brainstorm
> 2026-08-04 (cross-section pick C) · **Bucket**: v2 owner-pains
> **One-line**: Every state transition on `Visit`, `Order`, `OrderItem`,
> `Bill`, and `StockEntry` also writes an append-only `OwnerAuditEvent`
> row with a SHA-256 hash chain (`prev_hash → this_hash`). Owner gets a
> green/red chain-validity badge via `/audit` and the no-account link
> from feature 29.

## Goal

Turn the existing append-only `StockEntry` ledger into a self-checking
audit chain so the owner can tell in one line whether any of the
operational data was edited out-of-band (manual SQL, restored backup,
errant ORM update). The chain is built with only stdlib `hashlib` — no
new dependency — and the audit table is itself append-only, so the new
table reinforces the invariant it monitors.

Externally primed by today's research: HN `append-only-ledger` returned
**0 hits** in the 30-day window (recorded honestly), but GitHub
`topic:append-only` surfaced multiple repos and the OpenAlex query for
`creativity+product+restaurant` returned "Digital innovation strategy: A
framework for diagnosing and improving digital product and service
innovation" (in window) which independently surfaces the audit-chain
pattern as an industry pattern.

## Scope

**In scope (v2 owner-pains):**
- New SQLModel table `OwnerAuditEvent` with columns:
  `(id, event_type, source_table, source_id, payload_json, prev_hash,
   this_hash, created_at)`.
- A SQLAlchemy event listener (or `session.flush` hook) that, on commit
  of a write to `Visit`, `Order`, `OrderItem`, `Bill`, or `StockEntry`,
  computes the SHA-256 of the previous event's `this_hash` concatenated
  with the current event payload, and inserts one `OwnerAuditEvent`
  row.
- The first event in a chain has `prev_hash = NULL` and `this_hash =
  SHA-256(payload_json)`.
- New cook-bot command `/audit [days]` (default 7, max 30) that returns
  a single line:
  - `audit OK: 142 events, chain valid (last event 14:23)` (green check)
  - `audit BROKEN: chain break at event 87 (2026-08-04 11:42) — reason:
    expected prev_hash=abc, got def` (red cross, plus the offending
    event id and timestamp)
- The `/audit` command also appears on the feature 29 no-account link
  page as a small badge in the header.
- `verify_chain()` function in `backend/app/audit.py` that walks the
  table in id order and confirms each `prev_hash == previous this_hash`.
  The function is O(N) but runs in < 100 ms for 30 days of data.
- One new file `backend/app/audit.py`; one new file
  `backend/app/bot/cook_bot_audit.py`.

**Out of scope (v2 owner-pains):**
- Cryptographic signing with the restaurant's public key — the chain
  detects *tampering*, not *authentication*. Hash collisions on
  intentional forgery are out of scope.
- Replay / restore tooling — if the chain breaks, the cook manually
  inspects the offending event and decides whether to truncate or
  reset. There is no automated "fix" tool.
- Cross-process / cross-replica consistency — single Postgres instance
  (charter §3.2); multi-replica is v2-AI territory.
- Audit of any table other than the five listed (`MenuItem`,
  `MenuCategory`, `Table`, `Batch`, `User`, etc. are excluded by design;
  the chain is for *operational state*, not *reference data*).
- Streaming live audit events to the owner — `/audit` is on-demand; live
  streaming is feature 23 SSE territory.

## Description

The append-only `StockEntry` ledger is the killer pattern. But "append-only"
is a convention enforced by code review, not by the database itself: a
well-meaning operator who runs `UPDATE stockentry SET qty_delta = 10 WHERE
id = 42` will not see an error, and the ledger will quietly lose its
invariance. Worse, the only way to detect this today is to read every
`Bill` row and reconcile against `OrderItem` by hand — a job that no
small-restaurant owner actually does.

This contract adds a second append-only table — `OwnerAuditEvent` —
where every write to one of five operational tables is also recorded as
a hash-chained event. The chain makes tampering detectable in O(N) with
`hashlib` alone. The detection is a single Telegram reply (`/audit`) or a
single badge on the feature 29 page.

The chain is built as follows:

- For event N, `prev_hash = event[N-1].this_hash`.
- For event 0, `prev_hash = NULL`.
- `this_hash = SHA-256(canonical_json(payload) || prev_hash)`.
- `canonical_json` is a stable representation: keys sorted, no
  whitespace, UTC ISO-8601 timestamps, no float ambiguity (decimal
  money stays as string).

The `verify_chain()` function walks the table in `id` order and
confirms each `prev_hash` matches the previous row's `this_hash`. It also
confirms the `this_hash` matches `SHA-256(canonical_json(payload) ||
prev_hash)` for the row's own payload — so any row whose payload was
edited out-of-band is detected.

The hook is implemented as a SQLAlchemy `after_flush` listener that
queues up the audit events for each modified operational row, then
inserts them in a single commit alongside the original write. The
audit table is in the same database as the operational tables; a backup
restore is therefore reflected in both — restoring a backup that
overwrote more recent writes will produce a chain break at the
restore-point event, which is exactly what the owner needs to see.

## Data model

```
OwnerAuditEvent  (id, event_type TEXT, source_table TEXT, source_id BIGINT,
                  payload_json TEXT NOT NULL, prev_hash TEXT NULL,
                  this_hash TEXT NOT NULL, created_at TIMESTAMPTZ NOT NULL
                  DEFAULT now())
```

One new table. Index on `(source_table, source_id)` for fast lookup;
unique index on `id` (default). No other indexes — the chain is read in
id order and is small.

Migration: `init_db()` creates the table if absent.

## Implementation

1. **New model** — `backend/app/models.py`: `OwnerAuditEvent` SQLModel
   class.
2. **New module** `backend/app/audit.py`:
   - `canonical_json(payload: dict) -> str` — stable JSON encoder.
   - `compute_hash(payload_json: str, prev_hash: str | None) -> str` —
     `hashlib.sha256(payload_json.encode() + (prev_hash or "").encode()).hexdigest()`.
   - `make_event(session, source_row, event_type) -> OwnerAuditEvent` —
     builds the payload, looks up the previous event's `this_hash`,
     inserts a new `OwnerAuditEvent` row.
   - `verify_chain(session) -> AuditResult` — walks the table in id
     order, returns `(ok: bool, breaks: list[BreakInfo])`.
3. **SQLAlchemy hook** — extend `backend/app/db.py` with an
   `after_flush` listener on the operational models (`Visit`, `Order`,
   `OrderItem`, `Bill`, `StockEntry`). On every INSERT / UPDATE /
   DELETE of one of those models, queue a corresponding
   `OwnerAuditEvent` write into the same session.
4. **New bot handler** — extend `backend/app/bot/cook_bot.py` with
   `/audit [days]` (chat-id allowlisted). Calls `verify_chain()` over
   the requested window, returns the single-line summary.
5. **Feature 29 page badge** — extend
   `backend/app/templates/owner.html` to call `verify_chain()` server-
   side once per render and show a small green/red badge in the
   header.
6. **Manual verification**:
   - `cd backend && uvicorn app.main:app --reload`
   - In Telegram (cook role): `/audit 7` → "audit OK: 142 events,
     chain valid".
   - Open psql: `UPDATE stockentry SET qty_delta = 999 WHERE id = 1;`.
   - `/audit 7` → "audit BROKEN: chain break at event 87 (…): expected
     prev_hash=abc, got def".
   - Roll back: `UPDATE stockentry SET qty_delta = <original> WHERE id =
     1;`. The chain is *still* broken because `payload_json` of the
     audit event has not changed — the chain detects payload edits too.
   - This is correct behaviour: tampering is detected regardless of
     whether the original row is restored.

## Telegram interaction

- New cook-bot command `/audit [days]` — single-line reply.
- Existing cook-bot commands are unaffected.

## Dependencies

- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — the
  existing `StockEntry` ledger this contract audits.
- [05-payment-tip-reconciliation.md](05-payment-tip-reconciliation.md) —
  `Bill` is one of the audited tables; this contract preserves the
  tip-derivation invariant.
- [26-reorder-point-on-stockentry.md](26-reorder-point-on-stockentry.md)
  — ROP only reads; audit reads the same `StockEntry` rows but does not
  depend on the reorder columns.
- [29-owner-no-account-live-floor-link.md](29-owner-no-account-live-floor-link.md)
  — page shows the audit badge.
- Charter §3.1 (operational state model) and §3.2 (`SECRET_KEY`,
  Postgres).

## Open questions

- Should the chain include `MenuItem` / `Table` writes? Default: no —
  reference data is not part of operational truth. Revisit if a
  MenuItem edit could cause a financial discrepancy (e.g. price change
  on a sold item). If yes, add `MenuItem` to the audited set.
- Should `verify_chain()` also confirm that no audit row itself was
  UPDATEd or DELETEd? Default: no — the append-only convention is
  enforced by code review. A v2-AI follow-on could add a Postgres
  trigger that prevents UPDATE/DELETE on `OwnerAuditEvent`.
- Hash function — SHA-256 is the stdlib default. If the restaurant
  needs cryptographic signing (e.g. for insurance), swap to
  `hashlib.sha3_256` in one line. No API change.
- Audit retention — chain is unbounded; after 1 year of operation, the
  table is ~50k rows. Index is small. No archival needed in v1.

## Why this matters

The killer pattern is the append-only `StockEntry` ledger. The
owner-cook's recurring complaint in the research is "the till doesn't
match the software" — a margin loss of 1–3 % that the owner cannot
trace. This contract turns the ledger from a passive record into an
*active* integrity check: one Telegram reply tells the owner whether
the chain is intact. If it is broken, the offending event id and
timestamp are named; the owner knows exactly where to look. The
implementation is stdlib-only, fits inside the existing FastAPI +
SQLModel session lifecycle, and reinforces the append-only invariant
by example (the audit table is itself append-only).