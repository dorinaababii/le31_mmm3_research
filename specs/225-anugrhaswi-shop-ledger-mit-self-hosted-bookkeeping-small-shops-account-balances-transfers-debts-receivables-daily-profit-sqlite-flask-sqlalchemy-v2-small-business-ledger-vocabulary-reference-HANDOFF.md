# 225 — anugrhaswi/shop-ledger v2-small-business-ledger-vocabulary-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 small-business-ledger-horizontal-expansion question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/225-anugrhaswi-shop-ledger-mit-self-hosted-bookkeeping-small-shops-account-balances-transfers-debts-receivables-daily-profit-sqlite-flask-sqlalchemy-v2-small-business-ledger-vocabulary-reference.md` (defer artifact; **no code today**).

Bucket: **v2 small-business-ledger-vocabulary-reference (self-hosted-bookkeeping + small-shops + double-entry + daily-profit + Flask + SQLAlchemy + SQLite, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a small-business-ledger horizontal-expansion surface (expansion from a single-restaurant-vertical product to a small-business-bookkeeping-horizontal product that supports multiple vertical-business-types, or expansion to a standalone-bookkeeping product, or expansion to a standalone-daily-P&L product), what is the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* vocabulary that preserves the existing v1 single-restaurant-vertical posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 148 KB with 0★/0⑂ + MIT permissive license + 9 topics + in-window-by-push-only + FRESH PUSH TODAY is shipping the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* primitive as the v2 small-business-ledger-horizontal-expansion discipline*, but struggles because *v1 has no documented small-business-ledger-horizontal-expansion primitive in the charter*, so that *v2 can introduce the small-business-bookkeeping + double-entry-accounting + daily-P&L vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no small-business-ledger-horizontal-expansion trigger; the JTBD is primitive vocabulary extension + self-hosted-bookkeeping + double-entry + daily-profit + SQLite documentation, not a build-need; **cross-section JTBD value is HIGH** — the only 2026-09-24 GitHub Search candidate with 100% topic-overlap score; the FRESH PUSH TODAY is the first in-window event for this repo in the 57-pass series). |
| 2 | **Viability** | Maintainer can read 148 KB repo description + 9-topic vocabulary + self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite octuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no small-business-ledger-horizontal-expansion surface today). Confidence: high for the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* vocabulary (0★/0⑂ + MIT permissive license + 9 topics including all 9 LE31-relevant primitives + in-window-by-push-only + FRESH PUSH TODAY + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *self-hosted-bookkeeping + small-shops + double-entry* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the small-business-bookkeeping dimension*; the *daily-profit + account-balances + transfers + debts + receivables* discipline IS the *single-tenant + ledger-modules* posture applied to the *capital-management* dimension; the *Flask + SQLAlchemy + SQLite* stack is sister-shape to LE31 v1's FastAPI + SQLModel + PostgreSQL stack). Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the small-business-bookkeeping dimension* (every bookkeeping state transition is an explicit SQLModel row; no silent transition; the *StockEntry-append-only* pattern IS the *ledger* primitive applied to the small-business-bookkeeping dimension). Charter §3.1 alignment (the *self-hosted + single-tenant + on-premise* posture IS the *explicit-state-transition + single-restaurant-vertical* discipline applied to the *bookkeeping* dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive; SQLite is on-pattern for v1 development per known-conflict note); §3.4 not triggered (no AI surface; the *self-hosted-bookkeeping* discipline is deterministic-ledger-discipline, not customer-facing AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 small-business-ledger-vocabulary-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 148 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours; 148 KB modest-repo size makes inspection immediately productive). **Cost-to-value ratio: high** (the *self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite* octuple + the 9/9 topic-overlap score + the FRESH PUSH TODAY need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/225-anugrhaswi-shop-ledger-mit-self-hosted-bookkeeping-small-shops-account-balances-transfers-debts-receivables-daily-profit-sqlite-flask-sqlalchemy-v2-small-business-ledger-vocabulary-reference-HANDOFF.md` and `features/225-anugrhaswi-shop-ledger-mit-self-hosted-bookkeeping-small-shops-account-balances-transfers-debts-receivables-daily-profit-sqlite-flask-sqlalchemy-v2-small-business-ledger-vocabulary-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + self-hosted-bookkeeping + small-shops + double-entry + daily-profit + SQLite documentation for the next v2 small-business-ledger-horizontal-expansion review moment; **cross-section JTBD value is HIGH** — the only 2026-09-24 GitHub Search candidate with 100% topic-overlap score; the FRESH PUSH TODAY is the first in-window event for this repo in the 57-pass series).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a small-business-ledger-horizontal-expansion surface to the LE31 v2 operator surface, a small-business-bookkeeping surface, a double-entry-accounting surface, or a daily-P&L surface):

- `app/bookkeeping/` — possibly add (the small-business-bookkeeping module directory; depends on the v2 change).
- `app/bookkeeping/ledger.py` — possibly add (the double-entry-accounting ledger handler; depends on the v2 change).
- `app/bookkeeping/daily_pnl.py` — possibly add (the daily-P&L-calculation handler; depends on the v2 change).
- `app/bookkeeping/balances.py` — possibly add (the account-balances query handler; depends on the v2 change).
- `app/bookkeeping/transfers.py` — possibly add (the inter-account-money-movement handler; depends on the v2 change).
- `app/bookkeeping/receivables.py` — possibly add (the receivables handler; depends on the v2 change).
- `app/models/bookkeeping_accounts.py` — possibly add (the `bookkeeping_accounts` SQLModel table; depends on the v2 change).
- `app/models/bookkeeping_transactions.py` — possibly add (the `bookkeeping_transactions` SQLModel table; double-entry ledger; depends on the v2 change).
- `app/models/bookkeeping_daily_pnl.py` — possibly add (the `bookkeeping_daily_pnl` SQLModel table; depends on the v2 change).
- `app/models/bookkeeping_receivables.py` — possibly add (the `bookkeeping_receivables` SQLModel table; depends on the v2 change).
- `tests/test_bookkeeping.py` + `tests/test_bookkeeping_ledger.py` + `tests/test_bookkeeping_daily_pnl.py` + `tests/test_bookkeeping_receivables.py` — possibly add (the integration tests for the small-business-bookkeeping + double-entry + daily-P&L + receivables surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no small-business-ledger-horizontal-expansion surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

- **No code today**, so no verification protocol applies.
- **Future v2 verification protocol** (if the trigger condition fires):
  1. **License verification** — re-fetch `https://api.github.com/repos/anugrhaswi/shop-ledger/license` to confirm `spdx_id: 'MIT'`.
  2. **Stack-shape verification** — confirm `anugrhaswi/shop-ledger` source uses Flask + SQLAlchemy + SQLite + double-entry-accounting primitives by inspecting `app/` or `src/` directory.
  3. **Bookkeeping verification** — confirm `anugrhaswi/shop-ledger` source has a `bookkeeping` module with account-balances + transfers + debts + receivables surfaces.
  4. **Daily-P&L verification** — confirm `anugrhaswi/shop-ledger` source has a `daily_pnl` module that calculates daily profit from transactions.
  5. **Integration test verification** — verify the adapted vocabulary primitives work against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack.
  6. **Telegram surface verification** (if a Telegram surface is added in v2) — verify the adapted vocabulary primitives send correct aiogram messages with no hallucinated text.
- **Anti-fabrication canary**: `grep -c 'LE31' <shop-ledger-source-file>` must return 0 — the shop-ledger source is independent of LE31 and any "verbatim" quotes must not mention LE31.

## 5. Rollback path

**Fully reversible.** The defer artifact is documentation only. Disable/delete path:
- `git rm specs/225-anugrhaswi-shop-ledger-mit-self-hosted-bookkeeping-small-shops-account-balances-transfers-debts-receivables-daily-profit-sqlite-flask-sqlalchemy-v2-small-business-ledger-vocabulary-reference-HANDOFF.md`
- `git rm features/225-anugrhaswi-shop-ledger-mit-self-hosted-bookkeeping-small-shops-account-balances-transfers-debts-receivables-daily-profit-sqlite-flask-sqlalchemy-v2-small-business-ledger-vocabulary-reference.md`
- No migration, no SQLModel schema rollback, no FastAPI route removal, no Telegram handler removal required.
- No retained data; no safe-failure-mode concern.

If a future v2 PR has already added a small-business-ledger surface based on this vocabulary reference, the rollback path includes:
- Remove the v2 surface code (depends on the v2 change).
- Remove the v2 SQLModel tables (depends on the v2 change).
- Remove the v2 FastAPI routes (depends on the v2 change).
- Remove the v2 Telegram handlers (depends on the v2 change).
- Re-run LE31 v2 test suite to confirm no regression.

## 6. Mandatory LE31 skill list

The coding agent **MUST** load and follow these skills before any future v2 implementation (none apply today):

- `le31-conventions` — the master skill for v2 development conventions; §3.1 explicit-state-transitions, §3.2 license-compatible-only, §3.4 no-customer-facing-AI.
- `le31-v1-feature-pattern` — the v1 feature template pattern that informs the v2 surface shape.
- `le31-handoff-spec` — the handoff spec that documents the slice contract.
- `le31-coding-agent-brief` — the coding-agent brief that produces the paste-in prompt from the slice contract.
- `le31-verification-protocol` — the verification protocol that defines what "done" means.
- `le31-feature-pipeline` — the feature pipeline that produces the deliverables.
- `le31-daily-research` — the daily research skill that produced this artifact.
- `le31-daily-brainstorm` — the daily brainstorm skill that produced this artifact.
- `le31-v2-feature-pattern` — the v2 feature template pattern (if it exists; otherwise this skill is not loaded).

**No skill loading required today.** The defer artifact is documentation only; the coding agent does not need to load any skill because there is no code change.

---

**Summary**: defer (parking-lot); v2 small-business-ledger-vocabulary-reference; no code today; MIT ✓ §3.2 STRICTLY-COMPATIBLE; cross-section JTBD value is HIGH (the only 2026-09-24 GitHub Search candidate with 100% topic-overlap score; FRESH PUSH TODAY); 9/9 topic-overlap score; sister-shape to features 170 + 172 + 223.