# Feature 49 — Postledger Tamper-Evident Hash Chain on `StockEntry`

> **Priority**: P2 · **Effort**: S (≤1 day) · **Source**: brainstorm 2026-08-09 (cross-section pick A) · **Bucket**: v2 (audit)
> **One-line**: Add a `prev_hash` + `row_hash` (sha256 of `prev_hash || json.dumps(stable_row)`) pair to `StockEntry`, written atomically with each row, so the cook can't quietly edit a row and the owner can prove it on a one-command replay (`verify.py` CLI or `/verify ledger [date]` cook-bot command).

## Goal

The existing `StockEntry` ledger captures *what happened* (quantity delta, time, source) and (via feature 37) *why* (the rationale on voids). What it does NOT protect against is *silent row edits* — if the cook edits a row in the database directly (or a migration goes wrong, or a backup-restore silently mutates a row), the chain of evidence is broken and the only check today is `git log` on the migration files. The append-only invariant is enforced by *convention* (no UPDATE/DELETE statements in the codebase, the `via` enum is the only way to mutate a count) but not by *cryptography*.

`shuaige121/postledger` (pushed 2026-08-08T18:22:04Z, 0★, "Double-entry bookkeeping that assumes the bookkeeper is not trustworthy. Idempotent writes, append-only journal, DB-enforced balance, **tamper-evident hash chain**. Unix CLI + MCP server + local read-only web view. Zero dependencies.") is a *double-entry bookkeeping* primitive that solves the same problem: "assumes the bookkeeper is not trustworthy" → *tamper-evident hash chain* on every row. Translated to LE31, this is the missing *proof-of-no-tampering* layer on `StockEntry` (and, in a follow-up, on any append-only entity that wants the same guarantee — feature 47's `DecisionRationaleMixin` can opt in).

Inspired by today's brainstorm: GitHub `topic:append-only` repo `shuaige121/postledger` (pushed 2026-08-08T18:22:04Z, 0★, "Double-entry bookkeeping that assumes the bookkeeper is not trustworthy. Idempotent writes, append-only journal, DB-enforced balance, tamper-evident hash chain. Unix CLI + MCP server + local read-only web view. Zero dependencies."). The repo comes from the *finance / double-entry-bookkeeping* world — completely outside hospitality — and shares the LE31 `StockEntry` *append-only ledger* primitive, but adds the *untrusted-bookkeeper* invariant. Translated to LE31, this is the missing *proof-of-no-tampering* layer that pairs with the existing append-only `StockEntry` table.

Distinct from feature 30 (`append-only-audit-redirect`) because 30 is the *redirect primitive* (route writes through one function so they can't bypass the ledger); this is *cryptographic proof-of-no-tampering* on the rows themselves. Distinct from feature 37 (`void-rationale-ledger-field`) because 37 is the per-event *rationale* field on voids; this is the *immutable* chain on every row. Distinct from feature 46 (`havemind-decision-notes`) because 46 is the *append-only decision log*; this is the *append-only stock ledger* with a stronger invariant. Distinct from feature 47 (`decision-rationale-mixin`) because 47 is the *rationale mixin*; this is the *hash chain* on the underlying rows. **None** of the four protect against silent row edits — only Pick A does.

## Evidence / JTBD

When the owner reviews the cook's nightly `StockEntry` ledger and a row looks suspicious (e.g. the count of the lamb batch jumped from 8 to 18 between 19:00 and 19:30 with no intervening `prep` event), the owner wants cryptographic proof that no row was edited, but currently the only check is `git log` on the migration files (and a developer who suspects tampering has no way to detect it without re-running the migration history), so that a `prev_hash` / `row_hash` chain on `StockEntry` makes verification a one-line replay: `verify.py` CLI replays the chain and reports "OK" or "BROKEN at row 1234 (prev_hash mismatch)".

## Scope

**In scope (v2):**
- Add two new columns to `StockEntry`:
  - `prev_hash: Optional[str] = Field(default=None, max_length=64)` — the `row_hash` of the previous row (NULL for the genesis row).
  - `row_hash: Optional[str] = Field(default=None, max_length=64)` — `sha256(prev_hash || canonical_json(stable_row_without_hash_fields))`.
- One new SQLAlchemy event listener (`before_insert`) on `StockEntry` that computes `row_hash` from the previous row's `row_hash` + the stable row JSON. The listener is the **single** way rows get a hash; no application code writes `row_hash` directly.
- One new Alembic migration: `add_prev_hash_row_hash_to_stockentry` — adds the two columns as nullable (back-fill is a separate step), creates a unique index on `row_hash` (so the chain is fast to query), and creates a SQLAlchemy event listener registration.
- One new back-fill script: `backend/scripts/backfill_stockentry_hash.py` — for every existing `StockEntry` row, in `id` order, set `prev_hash` / `row_hash` from the canonical chain. Idempotent: re-running on already-hashed rows is a no-op.
- One new CLI: `backend/scripts/verify_stockentry_chain.py <from_id?> <to_id?>` — replays the chain from the genesis row (or the given `from_id`) to the latest row (or the given `to_id`), and reports the first mismatch with the row id, the expected `row_hash`, and the recomputed `row_hash`. Returns exit code 0 on OK, 1 on BROKEN.
- One new cook-bot command: `/verify ledger [date]` (default: today) — runs the same replay and answers "OK ✓ <N> rows verified" or "✗ BROKEN at row <id> (prev_hash mismatch) — investigate".
- One new unit test: `backend/tests/test_stockentry_hash_chain.py` — covers the listener, the back-fill script, the CLI, and the bot command.
- One new short doc: `backend/app/models/stockentry_hash.md` (50 lines) — explains the algorithm, the canonical-JSON rule, and the "what to do if the chain is broken" runbook.

**Out of scope (v2):**
- No LLM dependency. The hash chain is pure Python (stdlib `hashlib` + `json`).
- No auto-correction on mismatch. A broken chain is a **detection** signal, not a **correction** action — the operator must investigate.
- No application-level UPDATE/DELETE prevention. The hash chain detects tampering; it does not prevent it. (The existing `via` enum is the prevention layer; this feature is the detection layer.)
- No retroactive hash chain on other tables. Feature 47's `DecisionRationaleMixin` can opt in via a follow-up if/when any other entity wants the same guarantee.
- No change to the `via` enum semantics. The existing `manual | void | comp | substitution` stays.
- No external hash anchoring (e.g. publishing `row_hash` to a public chain). Local-only.

## Description

The hash chain is the smallest primitive that turns "trust the cook" into "verify the cook in one command". The algorithm:

1. **Canonical JSON**: every `StockEntry` row has a `to_canonical_json()` method that returns a deterministic JSON string of the stable fields (id, menu_item_id, delta_qty, via, occurred_at, rationale, rationale_set_at, rationale_set_by_chat_id, created_at) — sorted keys, no whitespace, UTC ISO-8601 timestamps, null for unset fields. The `prev_hash` and `row_hash` fields are excluded from the canonical JSON.
2. **Genesis row**: the first `StockEntry` row (by `id`) has `prev_hash = None` and `row_hash = sha256("" || to_canonical_json(row))` = `sha256(to_canonical_json(row))` (with the empty string as the prev part).
3. **Subsequent rows**: each new row reads the previous row's `row_hash` and computes `row_hash = sha256(prev_row_hash || to_canonical_json(new_row))`.
4. **Verification**: a `verify_chain(from_id, to_id)` function iterates rows in `id` order, recomputes the hash for each row from `(prev_row_hash, canonical_json(row))`, and reports the first mismatch.

The SQLAlchemy `before_insert` listener is the only path that writes `prev_hash` / `row_hash` — application code never sets these directly. This means a developer who tries to insert a `StockEntry` via raw SQL *without* going through the listener will get a row with `row_hash = NULL`, which the chain verifier flags as broken on the first subsequent row.

## Data model

```sql
ALTER TABLE stockentry ADD COLUMN prev_hash VARCHAR(64);
ALTER TABLE stockentry ADD COLUMN row_hash VARCHAR(64);
CREATE UNIQUE INDEX ix_stockentry_row_hash ON stockentry (row_hash);
```

The two columns are nullable so the back-fill script can run incrementally. The unique index on `row_hash` is the fast-path for the verifier (most chain queries can be answered by walking the unique-index B-tree).

## Implementation steps

1. **New file**: `backend/app/models/stockentry_hash.py` — `to_canonical_json(row) -> str`, `compute_row_hash(prev_row_hash: str | None, row) -> str`, `verify_chain(session, from_id=None, to_id=None) -> VerifyResult` (a small dataclass with `ok: bool`, `broken_at_id: int | None`, `expected: str | None`, `actual: str | None`, `rows_checked: int`).
2. **New file**: `backend/app/models/stockentry_listeners.py` — `@event.listens_for(StockEntry, "before_insert")` that calls `compute_row_hash` and sets `prev_hash` / `row_hash`. Imports are inside the listener (lazy) to avoid a circular import with the model module.
3. **New file**: `backend/app/migrations/versions/2026_08_09_add_prev_hash_row_hash_to_stockentry.py` — Alembic migration that adds the two columns and the unique index, and calls `op.execute("SELECT register_stockentry_hash_listener()")` if a SQL-level listener is registered (otherwise no-op — the SQLAlchemy listener in step 2 is sufficient).
4. **New file**: `backend/scripts/backfill_stockentry_hash.py` — for each existing `StockEntry` row in `id` order, sets `prev_hash` / `row_hash` from the canonical chain. Prints progress every 1000 rows. Idempotent: re-running skips already-hashed rows.
5. **New file**: `backend/scripts/verify_stockentry_chain.py` — CLI wrapper around `verify_chain` with argparse and exit codes 0/1.
6. **New file**: `backend/app/bot/commands/verify_ledger.py` — `/verify ledger [date]` cook-bot command. Default date = today (Europe/Paris). Calls `verify_chain` and replies with the result.
7. **New file**: `backend/tests/test_stockentry_hash_chain.py` — unit tests for the listener, the back-fill script, the CLI, and the bot command. Includes a tamper test (manually edit a row's `delta_qty` in a test DB and assert the verifier reports BROKEN).
8. **New file**: `backend/app/models/stockentry_hash.md` — short doc explaining the algorithm, the canonical-JSON rule, and the runbook for "what to do if the chain is broken".
9. **Refactor**: `backend/app/models/stockentry.py` — add the two nullable columns to the SQLModel.
10. **Wire-up**: register the listener in `backend/app/main.py` on app startup (one line).
11. **Verify**: `pytest backend/tests/test_stockentry_hash_chain.py` passes; `verify_stockentry_chain.py` exits 0 on a fresh dev DB after a smoke run; `/verify ledger` returns "OK" in the cook bot.

## Telegram interaction

One new cook-bot command:
- `/verify ledger [date]` (cook-only, chat-id in `TELEGRAM_ALLOWED_USERS`). Default date = today (Europe/Paris). Replies:
  - OK case: `OK ✓ <N> rows verified (<from_id>..<to_id>)` (one line, no follow-up).
  - Broken case: `✗ BROKEN at row <id> — expected <expected_short>, got <actual_short>. Investigate.` + a follow-up message with the full `VerifyResult` JSON for the operator to forward to the developer.

No new waiter-side interaction. The verify CLI is the operator/developer path.

## Dependencies

- Existing `sqlmodel` (already a dep).
- Existing `sqlalchemy` (already a dep).
- Existing `pydantic` v2 (already a dep).
- Existing `pytest` (already a dep).
- Existing `alembic` (already a dep).
- Stdlib `hashlib` + `json` (always available).
- **No new packages.**

## Failure / recovery

- **If the chain is broken at row X**: the verifier reports the broken row id, the expected `row_hash`, and the recomputed `row_hash`. The operator reads the canonical JSON for row X and compares against the row in the DB; the diff is the *tampered field*. The operator then decides:
  1. If the row was edited by a developer (e.g. a hotfix) and the rationale is documented in `notes`, the operator can **re-hash** by running `backfill_stockentry_hash.py --from-id X` (the script will use the current row contents as the new canonical state and re-hash from X onwards). This is the *intentional re-hash* path — it is logged in the script output.
  2. If the row was edited by the cook via direct SQL (no rationale), the operator can **void** the row by writing a new `StockEntry` with negative `delta_qty`, `via = "void"`, and a rationale explaining the original-row-tampered incident. The chain now has a void row pointing at the broken row (the broken row's `row_hash` stays in history; the void row is the correction).
- **If the chain is broken at the genesis row**: the only recovery is to drop the table and re-create from a backup. The genesis row cannot be re-hashed (it has no `prev_hash` to point to). This is a **hard failure** — the operator should investigate before re-creating.
- **If the back-fill script fails partway**: re-running is idempotent. The script commits every 1000 rows in a transaction; a mid-run crash leaves the chain in a consistent state up to the last commit.

## Definition of done

- `StockEntry` has `prev_hash` and `row_hash` columns, with a unique index on `row_hash`.
- The SQLAlchemy `before_insert` listener writes both columns on every new row.
- The Alembic migration is applied to dev + staging.
- The back-fill script is run on production and exits 0 (chain is OK after back-fill).
- The `verify_stockentry_chain.py` CLI runs on production and exits 0.
- `/verify ledger` cook-bot command returns "OK" on a fresh dev DB.
- The tamper test (manually edit a row, run verifier, expect BROKEN) passes.
- The `stockentry_hash.md` doc is in the repo.
- The change is committed and pushed to `main`.

## Open questions

1. **Should the verifier also check the `prev_hash` column matches the previous row's `row_hash` column, or just recompute the chain independently?** Lean: both. The independent recompute is the *fast* path (O(N) chain walk); the cross-check against the stored `prev_hash` is the *paranoid* path (catches the case where the listener is bypassed but the chain still looks consistent). Default: both, in the order cross-check → independent recompute.
2. **Should the back-fill script be run on a maintenance window, or online?** Lean: online. The script commits every 1000 rows in a transaction; total downtime is bounded. A long back-fill on a 100k-row table would take ~10 seconds at 10k rows/sec on a modern Postgres.
3. **Should the canonical JSON include `created_at` and `occurred_at` in UTC, or in the original timezone?** Lean: UTC. The auditor reads UTC; the cook reads Europe/Paris. The canonical JSON is the auditor's view.
4. **Should the verifier be exposed as a `/verify` admin command in addition to the cook-bot command?** Lean: yes. The operator should be able to run `/verify` from their phone too. One line of code, no new permissions.
5. **Should the chain cover other append-only entities (e.g. `DecisionNote` from feature 46)?** Lean: as a follow-up, not in this feature. Feature 47's `DecisionRationaleMixin` can opt in by adding the same two columns and the same listener; the change is mechanical. Deferred to a follow-up feature if/when feature 46's `DecisionNote` is reported as needing the same guarantee.

## Why this matters

LE31's existing moat is the **per-batch append-only `StockEntry` ledger paired with a Telegram cook surface** (feature 04). Today the append-only invariant is enforced by *convention* (no UPDATE/DELETE statements in the codebase, the `via` enum is the only way to mutate a count). A restaurant operator or accountant who reviews the ledger has no cryptographic way to detect tampering — they trust the codebase.

Adding a `prev_hash` / `row_hash` chain turns that trust into *verify*. The chain is the smallest primitive that delivers both *immutability-by-convention* and *integrity-by-cryptography* on the same rows. The cost is one new column-pair + one listener + one CLI + one bot command + one test suite — about 1 day of work. The benefit is that the owner can answer "did anyone touch this row?" in one command, and the answer is *cryptographic proof*, not "I trust the dev team".

This complements feature 37 (`void-rationale-ledger-field`) which captures *why* a row was written — together, the two features give the owner *what* (the row), *why* (the rationale), and *did anyone touch it* (the hash chain). Three small primitives, one strong audit story.
