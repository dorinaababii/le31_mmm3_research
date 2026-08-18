# append-only-immutable-audit-check — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/81-append-only-immutable-audit-check.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `81`
- Slug: `append-only-immutable-audit-check`
- Contract file: `features/81-append-only-immutable-audit-check.md`
- Bucket: **v2 owner-pains** — defer (watch-list)
- Linear parent: `HMM-99` (Brainstorm 2026-08-18 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft audit-check artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (in-window GitHub `topic:append-only` cluster — `SFHAJJI/lex-corpus-lu-legilux` 5★, 491747KB, in-window push 2026-08-15T19:39:33Z, "Every consolidated version of Luxembourg law as verbatim publisher files + dated JSON metadata, append-only, sha256-hashed").

**Confidence:** **medium** for the JTBD pull (the immutable-record-with-verification-surface pattern is well-established in legal / financial / compliance domains; the LE31 surface is the restaurant private ledger), **medium** for the stack match (the anchor peer is a static corpus, not a runtime library — the cross-section is the **verification protocol**, not the code).

**Decision: defer.** The hard prerequisite is **feature 49 (Postledger Tamper-Evident Hash Chain on StockEntry)** — without feature 49, audit-check has nothing to verify. The hard blocker for immediate build is also charter §3.2 "Money: never use binary floats" — the row_hash computation must use exact JSON serialization (sort_keys=True, no floats).

**Failed checks:**
- **Practicability**: prerequisite feature 49 has not shipped. Audit-check is meaningless without the chain.
- **Cost-to-value**: no observed owner pain in window. The owner has not asked "is my ledger intact?" yet.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-18).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after feature 49 ships).
6. `le31-research` (for the cross-section evidence base).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice will touch (when re-elevated to build)

```
features/81-append-only-immutable-audit-check.md         # NEW (this artifact)
specs/append-only-immutable-audit-check-HANDOFF.md      # NEW (this file)
INDEX.md                                                  # EDIT: append one row to "Active feature pipeline" table
agent/services/audit.py                                   # NEW (verify_ledger function)
cook_bot/handlers/audit_check.py                          # NEW (aiogram v3 /audit-check handler)
agent/verify.py (or agent/cli/verify.py)                 # NEW (CLI entrypoint)
agent/tests/test_audit_check.py                           # NEW (5 acceptance tests)
```

Zero schema impact (assumes feature 49 has shipped and the `prev_hash`/`row_hash` columns exist). Zero new pip dependencies. Zero new config keys.

## Verification protocol

After the artifact ships (post-feature-49):

1. **Read back** `features/81-append-only-immutable-audit-check.md` and confirm it matches the daily-brainstorm report's "81-append-only-immutable-audit-check" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-18), pick slug, feature path, and Linear sub-issue ID.
3. **Run the 5 acceptance tests** in `agent/tests/test_audit_check.py`:
   - empty ledger → "no rows, chain at genesis, intact"
   - 100-row ledger with intact chain → "intact through row 100"
   - ledger with one corrupted row_hash → drift report at correct row id
   - ledger with missing row (skip) → drift report at the gap
   - ledger with from/to date range filter → only rows in range are walked
4. **Run the LE31 test suite** (`pytest` or equivalent) and confirm it still passes.
5. **Hand-test on the cook bot**: trigger `/audit-check` in a test chat; verify the plain-language report renders correctly within the 4096-char Telegram limit.
6. **On a future daily-brainstorm pass**: re-query the GitHub `topic:append-only` cluster for new in-window peers with immutable-record verification patterns. If a new ≥10★ peer surfaces, escalate evidence and re-evaluate.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`.

- Title: `Feature 81 — append-only-immutable-audit-check`.
- Body: short summary + the file path to `features/81-append-only-immutable-audit-check.md` (≤1500 chars).
- Parent: `HMM-99` (Brainstorm 2026-08-18 — daily).
- Status: `Backlog` (defer until feature 49 ships).

## Rollback path

Delete `features/81-append-only-immutable-audit-check.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. Remove `agent/services/audit.py`, `cook_bot/handlers/audit_check.py`, `agent/verify.py`, and `agent/tests/test_audit_check.py`. No data migration to revert (audit-check is a read-only surface).

## Why this matters (for the coding agent)

The owner cannot run a restaurant on a ledger they cannot verify. Without audit-check + feature 49, the owner must trust the application code, the database admin, and the migration history to keep the `StockEntry` ledger intact. With audit-check + feature 49, the owner gets cryptographic proof that the chain is intact on demand, in plain language, on the surface they already use (Telegram). The cross-section pattern (public immutable records with public verification surface) is observed in the in-window Luxembourg law corpus repo at 5★ + 491747KB + in-window push 2026-08-15 — the strongest append-only cross-section signal since `holdfast` (feature 61) and `postledger` (feature 49). Two 2026-08-17 arXiv papers (`2608.16178v1` "Agent-Native Telemetry: Verifiable State-Delta Evidence Ledger" + `2608.16032v1` "Proof-of-Execution Memory: HMAC-chained ledger") confirm the academic backdrop.

**Status: defer.** Re-evaluate when (a) feature 49 ships, OR (b) an in-window ≥10★ peer with an immutable-record verification surface pattern surfaces.
