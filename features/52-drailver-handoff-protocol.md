# Feature 52 — Drailver Shift-Handoff Protocol

> **Priority**: P2 · **Effort**: S (≤1 day) · **Source**: brainstorm 2026-08-10 (cross-section pick A) · **Bucket**: v2 owner-pains
> **One-line**: Add an explicit, append-only, hash-chained **shift-change protocol log** to `StockEntry` (triggered by `/shift close <cook_id>` from the outgoing cook and `/shift open <cook_id>` from the incoming cook) so that the morning cook can confirm receipt of yesterday's context (voids-with-rationales, 86's, top movers, prep shortfalls) with one tap, and the owner can verify the shift chain on demand with `/verify shifts` — a per-shift companion to feature 49's per-row hash chain.

## Goal

The existing `StockEntry` ledger captures *what happened* (quantity delta, time, source, rationale). What it does NOT capture is **shift boundaries** — the moment when cook A hands the kitchen to cook B (or the night cook hands to the morning cook) and the verbal handoff happens. Today this is a paper clipboard + a verbal "the lamb was 86'd at 21:30". The result is that the morning cook arrives with no in-app record of what happened overnight, the operator has no way to audit whether a shift was actually closed, and the hash chain (feature 49) gives per-row proof but no *semantic* grouping by shift.

`Dawil/draiver` (pushed 2026-08-10T06:34:01Z, 0★, "externalize a ticket's valuable context (spec, decisions, gotchas) into a durable, append-only, hash-chained log; CLI + web board for the agent/human ticket protocol") is the *agent/human ticket protocol + hash-chained log* primitive from the agent-runtime world. Translated to LE31, this is the missing **shift-boundary ritual** that pairs with the existing `StockEntry` ledger. Distinct from feature 46 (`havemind-decision-notes`) because 46 is a *decision log*; this is an *operational shift log*. Distinct from feature 47 (`decision-rationale-mixin`) because 47 is a per-row *rationale*; this is a *shift-scoped* protocol that fires at a transition. Distinct from feature 49 (`postledger-tamper-evident-hash`) because 49 is per-row hash proof; this is *per-shift* hash proof that anchors the row chain to a human-acknowledged boundary. **All four together** give the operator *what* (the row), *why* (the rationale), *did anyone touch it* (the row hash), and *who was on shift* (the shift anchor).

## Evidence / JTBD

When the night cook ends the shift and the morning cook arrives at 06:30, the morning cook wants to know *what happened* (voids, 86's, prep shortfalls, top movers, top complaints) without having to scroll through 200 `StockEntry` rows, but currently the only record is a verbal handoff and an optional paper clipboard, so that a `/shift open` command on the cook bot auto-surfaces yesterday's shift-close recap (anchored to the previous shift's `prev_anchor_hash`), and the morning cook can confirm receipt with one tap ("✓ acknowledged"). The owner can then run `/verify shifts` to check that every shift was actually acknowledged by an incoming cook and not just closed by the outgoing one.

## Scope

**In scope (v2):**
- Add three new columns to `StockEntry` (reuses the existing table; one Alembic migration):
  - `is_shift_anchor: bool = Field(default=False)` — marks the row as a shift-anchor (one per `/shift close` and one per `/shift open` acknowledgement).
  - `prev_anchor_hash: Optional[str] = Field(default=None, max_length=64)` — the `anchor_hash` of the previous shift's anchor row (NULL for the first anchor).
  - `anchor_hash: Optional[str] = Field(default=None, max_length=64)` — `sha256(prev_anchor_hash || canonical_json(shift_metadata))` where `shift_metadata = {kind: "shift_close" | "shift_open", cook_id, acknowledged_by_cook_id, void_count, void_total_qty, void_top_reasons, eighty_six_count, top_movers, prep_shortfalls, occurred_at}`.
- One new Alembic migration: `add_shift_anchor_columns_to_stockentry` — adds the three columns (nullable), creates a partial unique index `ix_stockentry_anchor_hash WHERE is_shift_anchor = true` (so the chain is fast to query and only one row per anchor), and adds a CHECK constraint enforcing `is_shift_anchor = false OR (prev_anchor_hash IS NOT NULL AND anchor_hash IS NOT NULL)` for all rows after the first.
- Two new cook-bot commands:
  - `/shift close [cook_id]` — outgoing cook. The bot computes the shift metadata from the last `/shift open` (or genesis) to now, writes a `StockEntry` with `is_shift_anchor=true`, `via="shift_close"`, and the shift metadata in the `rationale` field. The bot replies with a one-line recap (void count, 86 count, top-3 movers, prep shortfalls) and the new anchor's hash.
  - `/shift open <cook_id>` — incoming cook. The bot writes a `StockEntry` with `is_shift_anchor=true`, `via="shift_open"`, `acknowledged_by_cook_id=<cook_id>`, and `prev_anchor_hash=<previous anchor hash>`. The bot replies with the previous shift's recap (so the incoming cook sees the context immediately). Cook-only, chat-id in `TELEGRAM_ALLOWED_USERS`.
- One new cook-bot command: `/verify shifts [from_date] [to_date]` — runs the chain verifier on the anchor rows in the date range. Replies "OK ✓ <N> shift anchors verified" or "✗ BROKEN at anchor row <id>".
- One new CLI: `backend/scripts/verify_shift_anchors.py [from_date] [to_date]` — same logic, exit code 0 on OK, 1 on BROKEN.
- One new unit test: `backend/tests/test_shift_anchor_chain.py` — covers the listener (anchor rows get `anchor_hash` written automatically), the bot commands (close/open round-trip), the verifier (chain OK + tamper detection), and the migration.
- One new short doc: `backend/app/models/shift_anchor.md` (50 lines) — explains the algorithm, the canonical-JSON rule, and the "what to do if the shift chain is broken" runbook.

**Out of scope (v2):**
- No LLM dependency. The shift metadata is computed from `StockEntry` queries (pure Python; no embeddings, no model calls).
- No auto-close on shift boundaries. The cook explicitly runs `/shift close` — the LE31 state invariant is preserved.
- No owner-facing UI for the shift chain. The owner runs `/verify shifts` from the cook bot (the owner is one of the `TELEGRAM_ALLOWED_USERS` chat-ids) or the CLI directly.
- No retroactive shift anchors on existing data. The migration is additive; pre-existing `StockEntry` rows have `is_shift_anchor=false` and `prev_anchor_hash=NULL` (no chain proof until the first `/shift close` runs).
- No external hash anchoring (e.g. publishing `anchor_hash` to a public chain). Local-only.
- No automatic conflict resolution on simultaneous `/shift open` and `/shift close` (two cooks trying to close at once). The unique partial index serializes the writes; the second one gets a 409 from Postgres and the bot replies "another shift is in progress; please retry".
- No shift-anchor on tables other than `StockEntry`. Feature 47's `DecisionRationaleMixin` can opt in via a follow-up if/when any other entity wants the same guarantee.

## Description

The shift-anchor is the smallest primitive that turns *verbal handoff* into *in-app ritual*. The algorithm:

1. **Canonical JSON for anchor metadata**: every `StockEntry` row that has `is_shift_anchor=true` has a `to_anchor_canonical_json()` method that returns a deterministic JSON string of `{kind, cook_id, acknowledged_by_cook_id, void_count, void_total_qty, eighty_six_count, top_movers, prep_shortfalls, occurred_at, rationale}` — sorted keys, no whitespace, UTC ISO-8601 timestamps, null for unset fields. The `prev_anchor_hash`, `anchor_hash`, and the standard `row_hash` (from feature 49) fields are excluded from the canonical JSON.

2. **Genesis anchor**: the first `/shift close` (no prior anchor exists) writes an anchor row with `prev_anchor_hash = None` and `anchor_hash = sha256("" || to_anchor_canonical_json(row))`. Subsequent anchors use `prev_anchor_hash = <previous anchor's anchor_hash>`.

3. **Per-row hash chain (feature 49 reuse)**: the existing SQLAlchemy `before_insert` listener from feature 49 still fires on every `StockEntry` insert, including anchor rows. The anchor row therefore has *both* `row_hash` (per-row, from feature 49) and `anchor_hash` (per-shift, from this feature). The two hashes are independent — feature 49 proves "no row was edited"; this feature proves "every shift was closed and acknowledged".

4. **Verification**: a `verify_shift_anchors(from_date, to_date)` function iterates anchor rows in `id` order (or in `occurred_at` order, with a fallback to `id` for ties), recomputes `anchor_hash` for each anchor from `(prev_anchor_hash, anchor_canonical_json(row))`, and reports the first mismatch with the anchor row id, the expected `anchor_hash`, and the recomputed `anchor_hash`. Returns a `VerifyResult` dataclass with `ok: bool`, `broken_at_id: int | None`, `expected: str | None`, `actual: str | None`, `anchors_checked: int`.

The `before_insert` listener is the only path that writes `prev_anchor_hash` / `anchor_hash` — application code never sets these directly. This means a developer who tries to insert a shift anchor via raw SQL *without* going through the listener will get a row with `anchor_hash = NULL`, which the chain verifier flags as broken on the first subsequent anchor.

## Data model

```sql
ALTER TABLE stockentry ADD COLUMN is_shift_anchor BOOLEAN NOT NULL DEFAULT FALSE;
ALTER TABLE stockentry ADD COLUMN prev_anchor_hash VARCHAR(64);
ALTER TABLE stockentry ADD COLUMN anchor_hash VARCHAR(64);
CREATE UNIQUE INDEX ix_stockentry_anchor_hash ON stockentry (anchor_hash) WHERE is_shift_anchor = true;
ALTER TABLE stockentry ADD CONSTRAINT ck_stockentry_anchor_hash CHECK (
    NOT is_shift_anchor OR (prev_anchor_hash IS NOT NULL AND anchor_hash IS NOT NULL)
);
```

The three columns are nullable / default-false so the migration is non-blocking on existing rows. The partial unique index makes the chain fast to query (`SELECT * FROM stockentry WHERE is_shift_anchor = true ORDER BY id` walks the unique-index B-tree). The CHECK constraint catches the "anchor with NULL hash" misconfiguration at insert time.

## Implementation steps

1. **New file**: `backend/app/models/shift_anchor.py` — `to_anchor_canonical_json(row) -> str`, `compute_anchor_hash(prev_anchor_hash: str | None, row) -> str`, `verify_shift_anchors(session, from_date=None, to_date=None) -> VerifyResult` (a small dataclass with `ok: bool`, `broken_at_id: int | None`, `expected: str | None`, `actual: str | None`, `anchors_checked: int`).
2. **New file**: `backend/app/models/shift_anchor_listener.py` — `@event.listens_for(StockEntry, "before_insert")` that fires only when `is_shift_anchor=true` and calls `compute_anchor_hash`. Coexists with feature 49's row-hash listener; both fire on every insert.
3. **New file**: `backend/app/models/shift_metadata.py` — `compute_shift_metadata(session, from_dt: datetime, to_dt: datetime) -> dict` — queries the `StockEntry` rows in the range and returns `{kind, cook_id, void_count, void_total_qty, void_top_reasons, eighty_six_count, top_movers, prep_shortfalls}`. Pure Python; one SQL query for voids, one for 86's, one for top movers.
4. **New file**: `backend/app/migrations/versions/2026_08_10_add_shift_anchor_columns_to_stockentry.py` — Alembic migration that adds the three columns, the partial unique index, and the CHECK constraint. Also calls `op.execute("SELECT register_shift_anchor_listener()")` if a SQL-level listener is registered (otherwise no-op — the SQLAlchemy listener in step 2 is sufficient).
5. **New file**: `backend/app/bot/commands/shift_close.py` — `/shift close [cook_id]` cook-bot command. Cook-only, chat-id in `TELEGRAM_ALLOWED_USERS`. Calls `compute_shift_metadata`, writes the anchor row, replies with the recap and the new anchor's hash.
6. **New file**: `backend/app/bot/commands/shift_open.py` — `/shift open <cook_id>` cook-bot command. Cook-only. Reads the previous anchor's `anchor_hash`, writes the new anchor with `prev_anchor_hash=<previous>`, replies with the previous shift's recap.
7. **New file**: `backend/app/bot/commands/verify_shifts.py` — `/verify shifts [from_date] [to_date]` cook-bot command. Default range = last 7 days. Calls `verify_shift_anchors` and replies with the result.
8. **New file**: `backend/scripts/verify_shift_anchors.py` — CLI wrapper around `verify_shift_anchors` with argparse and exit codes 0/1.
9. **New file**: `backend/tests/test_shift_anchor_chain.py` — unit tests for the listener, the metadata computation, the bot commands (close/open round-trip), the verifier (chain OK + tamper detection), and the migration.
10. **New file**: `backend/app/models/shift_anchor.md` — short doc explaining the algorithm, the canonical-JSON rule, and the runbook for "what to do if the shift chain is broken".
11. **Refactor**: `backend/app/models/stockentry.py` — add the three new columns to the SQLModel.
12. **Wire-up**: register the new listener in `backend/app/main.py` on app startup (one line, alongside feature 49's row-hash listener).
13. **Verify**: `pytest backend/tests/test_shift_anchor_chain.py` passes; `verify_shift_anchors.py` exits 0 on a fresh dev DB after a round-trip close/open smoke run; `/shift close`, `/shift open`, `/verify shifts` all return expected output in the cook bot.

## Telegram interaction

Three new cook-bot commands (cook-only, chat-id in `TELEGRAM_ALLOWED_USERS`):

- **`/shift close [cook_id]`** — outgoing cook. Default `cook_id` = the chat-id of the sender (single-cook mode). The bot computes the shift metadata, writes the anchor row, and replies:
  - Recap: `Shift closed ✓ (anchor <row_id>, hash <hash_short>)\n  Voids: <N> (<total_qty>)\n  86'd: <N>\n  Top movers: <item1> (+<qty>), <item2> (+<qty>), <item3> (+<qty>)\n  Prep shortfalls: <item1>, <item2>`
  - One Telegram message, one-line summary at top for the cook to acknowledge in a glance.

- **`/shift open <cook_id>`** — incoming cook. Reads the previous anchor's `anchor_hash`, writes the new anchor, and replies with the *previous* shift's recap (so the incoming cook sees the overnight context immediately):
  - Same recap shape as `/shift close`, but the message ends with `\n  Previous shift acknowledged by you — anchor <row_id> (hash <hash_short>)`.

- **`/verify shifts [from_date] [to_date]`** — cook or owner. Default range = last 7 days. Calls `verify_shift_anchors` and replies:
  - OK case: `OK ✓ <N> shift anchors verified (<from_date>..<to_date>)` (one line, no follow-up).
  - Broken case: `✗ BROKEN at anchor row <id> — expected <expected_short>, got <actual_short>. Investigate.` + a follow-up message with the full `VerifyResult` JSON for the operator to forward to the developer.

No new waiter-side interaction. The verify CLI is the operator/developer path.

## Dependencies

- Existing `sqlmodel` (already a dep).
- Existing `sqlalchemy` (already a dep).
- Existing `pydantic` v2 (already a dep).
- Existing `pytest` (already a dep).
- Existing `alembic` (already a dep).
- Stdlib `hashlib` + `json` (always available).
- **Reuses feature 49's `compute_row_hash` / `verify_chain` primitives** (already filed; the row-hash chain is independent but coexists on the same rows).
- **No new packages.**

## Failure / recovery

- **If the shift chain is broken at anchor row X**: the verifier reports the broken anchor id, the expected `anchor_hash`, and the recomputed `anchor_hash`. The operator reads the canonical JSON for anchor X and compares against the row in the DB; the diff is the *tampered field*. The operator then decides:
  1. If the anchor was edited by a developer (e.g. a hotfix to fix a wrong cook-id) and the rationale is documented in `notes`, the operator can **re-hash** by writing a new `/shift close` with the corrected metadata. The new anchor chains to the broken anchor's `prev_anchor_hash` (the chain is now `... → broken_X → corrected_X'`). The verifier reports the chain is OK from `corrected_X'` onwards.
  2. If the anchor was edited by the cook via direct SQL (no rationale), the operator can **void** the row by writing a new `StockEntry` with `is_shift_anchor=false`, negative `delta_qty=0`, `via="void"`, and a rationale explaining the original-anchor-tampered incident. The chain now has a void row pointing at the broken anchor (the broken anchor's `anchor_hash` stays in history; the void row is the correction marker).
- **If the shift chain is broken at the genesis anchor**: the only recovery is to drop the table and re-create from a backup. The genesis anchor cannot be re-hashed (it has no `prev_anchor_hash` to point to). This is a **hard failure** — the operator should investigate before re-creating.
- **If two cooks try to close at the same time**: the partial unique index on `anchor_hash` serializes the writes; the second one gets a 409 from Postgres and the bot replies `another shift is in progress; please retry`. The operator can wait 1 second and retry.
- **If the migration fails partway**: `alembic downgrade -1` rolls back the three columns and the index. No data loss.

## Definition of done

- `StockEntry` has `is_shift_anchor`, `prev_anchor_hash`, and `anchor_hash` columns, with a partial unique index on `anchor_hash`.
- The SQLAlchemy `before_insert` listener writes both `prev_anchor_hash` and `anchor_hash` on every anchor row (and feature 49's listener writes `row_hash` on every row).
- The Alembic migration is applied to dev + staging.
- `/shift close`, `/shift open`, and `/verify shifts` cook-bot commands return expected output in the cook bot.
- The `verify_shift_anchors.py` CLI runs on dev and exits 0 after a round-trip close/open smoke run.
- The tamper test (manually edit an anchor row's `void_count` in a test DB, run verifier, expect BROKEN) passes.
- The `shift_anchor.md` doc is in the repo.
- The change is committed and pushed to `main`.

## Open questions

1. **Should the recap also surface today's prep board (from feature 43) and the owner's daily recap (from feature 39)?** Lean: yes, but as a separate feature. Feature 52's recap is *shift-scoped* (the time range between two anchors); feature 39's recap is *day-scoped* (Europe/Paris business day). They could share metadata helpers but should not be merged.
2. **Should `/shift open` require the *previous* cook's chat-id to have closed the shift, or can the incoming cook open an unclosed shift?** Lean: incoming cook can open an unclosed shift (the previous cook forgot to close). The chain records the gap as a "missing close" in the recap, and the verifier reports OK (the chain is consistent; missing closes are an operational problem, not a chain problem).
3. **Should the recap include the rationale on each void (from feature 37)?** Lean: yes — that's the whole point. The recap says "Voids: 2 (lamb -8: 'spoiled from morning batch'; fish -3: 'wrong prep count')". Cook-bot message size limits are ~4 KB per message; a 5-void recap with full rationales fits in 4 KB comfortably.
4. **Should the chain also be exposed as an SSE event for the owner's web UI?** Lean: as a follow-up, not in this feature. The owner can run `/verify shifts` from their phone; the web UI is a v3-AI feature.
5. **Should the listener also write `anchor_hash` retroactively when `is_shift_anchor` is flipped to `true` on an existing row?** Lean: no — the listener only fires on `before_insert`, not on `before_update`. If a developer manually flips `is_shift_anchor=true` on an existing row, the chain verifier flags it as broken (no `anchor_hash`). The developer must write a new anchor row instead.

## Why this matters

LE31's existing moat is the **per-batch append-only `StockEntry` ledger paired with a Telegram cook surface** (feature 03 + 04). Today's three audit features (37 = rationale, 47 = rationale mixin, 49 = hash chain) all strengthen the *what* and *why* of each row. Feature 52 adds the **who** and **when** at a *shift* level — turning the ledger from a stream of rows into a *narrative of shifts*. The cost is one Alembic migration + three new bot commands + one CLI + one test suite — about 1 day of work, mostly reusing feature 49's primitives.

The operational value is concrete: the morning cook arrives at 06:30, runs `/shift open`, and immediately sees "Yesterday: 2 voids (lamb -8 spoiled, fish -3 wrong prep count), 1 eighty-six (lamb at 21:30), top movers were lasagna +12, soup +9, salad +7. No prep shortfalls. Previous shift acknowledged by you — anchor 4521." That's the entire verbal handoff, in-app, in one Telegram message, and it's anchored to the previous shift's `anchor_hash` so the operator can prove it was actually read by the incoming cook.

This complements feature 49 (`postledger-tamper-evident-hash`) which captures *per-row* tamper evidence; feature 47 (`decision-rationale-mixin`) which captures *per-event* rationale; feature 46 (`havemind-decision-notes`) which captures *per-decision* rationale. Together, the four features give the operator *what* (the row), *why* (the rationale), *did anyone touch it* (the row hash), *who was on shift* (the shift anchor), and *was the handoff acknowledged* (the shift hash). Five small primitives, one strong operational story.
