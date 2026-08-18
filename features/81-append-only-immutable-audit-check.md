# Feature 81 — Append-Only Immutable Audit Check

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: brainstorm 2026-08-18 (cross-section pick A) · **Bucket**: v2 owner-pains
> **One-line**: A new `/audit-check` cook-bot command (and matching `verify.py` CLI) that walks the `StockEntry` ledger, recomputes the sha256 hash chain, and reports any drift to the owner in plain language.

## Goal

The existing `StockEntry` ledger is intended to be append-only and (once feature 49 ships) hash-chained. The owner must be able to **verify the chain integrity on demand** without trusting the application code or the database admin. The cross-section pattern is observed in `SFHAJJI/lex-corpus-lu-legilux` (5★, 491747KB, in-window push 2026-08-15T19:39:33Z, "Every consolidated version of Luxembourg law as verbatim publisher files + dated JSON metadata, append-only, sha256-hashed. The tree is the legislative history") — public immutable records require a public verification surface so external auditors can confirm integrity.

## Scope

**In scope (v2 owner-pains):**
- A new `/audit-check` command on the existing cook bot (aiogram v3) that recomputes the sha256 chain (per feature 49) over `StockEntry` rows in chronological order and reports: chain intact / chain drifted at row N / chain missing rows.
- A matching `verify.py` CLI (same primitive as feature 49's `verify.py`) for server-side cron + ad-hoc audit use.
- Plain-language report: "ledger intact through 2026-08-18 12:42 UTC, 4521 rows verified" / "ledger drifted at row 4521, expected row_hash `<x>`, got row_hash `<y>`, via='void', qty=-2.0".
- Optional: a `/audit-check <from> <to>` date-range form.

**Out of scope (v2 owner-pains):**
- The hash chain itself (covered by feature 49; audit-check assumes feature 49 is shipped).
- Owner-facing audit dashboard UI (v3 territory; defer).
- Cross-ledger comparison (covered by feature 31; defer).
- Cryptographic signature over the chain root (v3 territory; defer).

## Description

Once feature 49 ships, every `StockEntry` row carries a `(prev_hash, row_hash)` pair with `row_hash = sha256(prev_hash || json.dumps(stable_row, sort_keys=True))`. The audit-check walks the chain from the genesis row (hash = `"0" * 64`) to the latest row, recomputes each `row_hash` from `prev_hash` + stable-row JSON, and compares to the stored `row_hash`. Any mismatch is a chain drift and is reported with the row id, the expected vs actual hash, the `via` enum, and the qty delta.

The cook-bot command is exposed on the cook bot's existing chat surface (the cook bot already authenticates via Telegram bot token + cook user id). The owner is given the same command via a separate `/audit-check` handler bound to the owner chat id (already enumerated in `OwnerLink` / feature 29's `owner_chat_id` column).

The `verify.py` CLI lives at `agent/verify.py` and accepts `--from <iso> --to <iso>` args, returning JSON on stdout suitable for piping into a cron alert.

## Data model

No schema change. Reads the existing `StockEntry` table (which, post-feature-49, has `prev_hash` + `row_hash` columns).

```python
# Pseudo-schema (after feature 49 ships)
class StockEntry(SQLModel, table=True):
    id: int (primary key)
    at: datetime (UTC)
    menu_item_id: int (FK)
    qty: Decimal (EUR for stock-in, negative for stock-out)
    via: str (enum: receive | cook | void | adjust | count | ...)
    rationale: str | None (feature 37)
    actor_user_id: int
    prev_hash: str (64 hex chars)
    row_hash: str (64 hex chars)
```

## Implementation steps

1. **Prerequisite**: ship feature 49 (Postledger Tamper-Evident Hash Chain on `StockEntry`).
2. Add `agent/verify.py` with a `verify_ledger(from_: datetime | None, to: datetime | None) -> VerifyReport` function that walks the chain.
3. Add `verify_ledger` to a new `agent/services/audit.py` module (so the cook-bot command and the CLI share it).
4. Add `cook_bot/handlers/audit_check.py` aiogram v3 handler bound to `/audit-check` (cook + owner chat ids).
5. Add `cook_bot/handlers/audit_check.py` for owner chat id (separate registration on the owner bot or the cook bot's owner-handler list — depends on feature 29 wiring).
6. Add `agent/cli/verify.py` argparse CLI: `--from <iso> --to <iso> --json`.
7. Write 5 acceptance tests in `agent/tests/test_audit_check.py`:
   - empty ledger → "no rows, chain at genesis, intact"
   - 100-row ledger with intact chain → "intact through row 100"
   - ledger with one corrupted row_hash → drift report at correct row id
   - ledger with missing row (skip) → drift report at the gap
   - ledger with from/to date range filter → only rows in range are walked
8. Run all tests; commit + push.

## Telegram interaction if any

- `/audit-check` (cook + owner) — returns the plain-language audit report inline as a Telegram message (max 4096 chars; truncate + "..." for very long reports).
- `/audit-check 2026-08-01 2026-08-18` — same with date range.

## Dependencies

- **[feature 49] Postledger Tamper-Evident Hash Chain on `StockEntry`** — audit-check assumes the chain exists. **This is the hard prerequisite** — without feature 49, audit-check has nothing to verify.
- **[feature 30] Append-Only Audit Redirect** — adjacent but not a prerequisite. Audit-check is the *verification* surface; feature 30 is the *write* surface.
- **[feature 31] Peer-Ledger Compare** — adjacent but not a prerequisite. Peer-ledger compare is cross-instance; audit-check is single-instance.
- **[feature 29] Owner No-Account Live-Floor Link** — adjacent but not a prerequisite. Audit-check is exposed on the owner chat id (whatever mechanism feature 29 establishes); if feature 29 is not shipped, the owner chat id can be derived from the existing `User` table.
- `agent/services/audit.py` — new module.
- `cook_bot/handlers/audit_check.py` — new aiogram v3 handler.
- `agent/verify.py` (or `agent/cli/verify.py`) — new CLI entrypoint.

## Open questions

- Should the audit-check also verify the **row order** (chronological invariant) or only the hash chain? Row order verification is cheaper and catches a different class of attack (reordering). Recommend yes.
- Should the audit-check report include the **last 5 chain-check timestamps** (when the owner last verified, when the cron last verified)? Useful for audit trail. Recommend yes if cheap.
- Should the audit-check trigger a Telegram alert on **chain drift** even if the owner didn't request it? Charter §3.2 "explicit operational state" suggests no — drift is reported on demand, not pushed. Confirm with charter.

## Why this matters

The owner cannot run a restaurant on a ledger they cannot verify. Without audit-check, the owner must trust the application code, the database admin, and the migration history to keep the `StockEntry` ledger intact. With audit-check + feature 49, the owner gets cryptographic proof that the chain is intact on demand, in plain language, on the surface they already use (Telegram). The cross-section pattern (public immutable records with public verification surface) is observed in the in-window Luxembourg law corpus repo at 5★ + 491747KB + in-window push 2026-08-15 — the strongest append-only cross-section signal since `holdfast` (feature 61) and `postledger` (feature 49).

## Distinct from existing features

- **Feature 30 (Append-Only Audit Redirect)** writes the `OwnerAuditEvent` row with the SHA-256 hash chain (`prev_hash → this_hash`). Audit-check **verifies** an existing chain; feature 30 **writes** the chain.
- **Feature 31 (Peer-Ledger Compare)** compares two ledger instances. Audit-check **verifies a single ledger instance**; feature 31 cross-checks between instances.
- **Feature 49 (Postledger Tamper-Evident Hash Chain on StockEntry)** adds the `(prev_hash, row_hash)` pair to `StockEntry`. Audit-check **reads** the chain that feature 49 writes; audit-check is the verification surface for feature 49's storage surface.

## Cross-section evidence

- **Anchor**: [SFHAJJI/lex-corpus-lu-legilux](https://github.com/SFHAJJI/lex-corpus-lu-legilux) — 5★, 491747KB, pushed 2026-08-15T19:39:33Z, "Every consolidated version of Luxembourg law as verbatim publisher files + dated JSON metadata, append-only, sha256-hashed. The tree is the legislative history."
- **Adjacent (carry-overs)**: `dallascrilley/holdfast` (feature 61, 2026-08-12), `shuaige121/postledger` (feature 49, 2026-08-09), `nradawg/segment-seam-chain` (feature 73, 2026-08-16), `SNAPKITTYWEST/worm-engines` (2★, Zig append-only ledger fabric, in-window 2026-07-30), `sirrobot01/appendstore` (1★, Go append-only KV store, in-window 2026-08-02).
- **Academic backdrop**: `arXiv:2608.16178v1` "Agent-Native Telemetry: Verifiable State-Delta Evidence Ledger" (Jun He, cs.DC/cs.AI, 2026-08-17T06:50:12Z) + `arXiv:2608.16032v1` "Proof-of-Execution Memory: HMAC-chained ledger for LLM agent safety" (Rahman/Kim, cs.CR, 2026-08-17T02:54:04Z) — both 2026-08 academic papers on the append-only + hash-chain pattern.

## Re-evaluation trigger

- Feature 49 ships → audit-check becomes build-candidate.
- A ≥10★ in-window peer surfaces with an immutable-record verification surface pattern → escalates to `build` evidence.
- Charter §3.2 is revised to allow proactive drift alerts → expand scope to include cron-driven drift push.

## Status

**defer** — gate verdict from brainstorm 2026-08-18 (HMM-99). Prerequisite feature 49 not shipped. No observed owner pain in window. Re-evaluate when feature 49 ships.
