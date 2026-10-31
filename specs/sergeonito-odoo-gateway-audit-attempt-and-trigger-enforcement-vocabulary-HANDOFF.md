# HANDOFF — 413-sergeonito-odoo-gateway-audit-attempt-and-trigger-enforcement-vocabulary

**Status**: **defer** (v1, parking-lot vocabulary reference — **NOT a build**)
**Date**: 2026-10-31
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/413-sergeonito-odoo-gateway-mit-python-fastapi-postgresql-rbac-audit-log-postgres-triggers-reject-update-delete-truncate-attempted-event-before-write-outcome-after-field-names-not-values-v1-audit-attempt-and-trigger-enforcement-vocabulary.md`
**LE31 feature gate verdict**: **defer** — gate check 1 (JTBD) **FAILS**. Evidence class **INFERRED**. **This contract records a rejection. It does not authorise work.**

## Trigger policy

**This is a `defer`. A coding agent must NOT implement this.**

Per `le31-feature-pipeline` §*Hard rules*: *"If the pick fails the gate, do not write a contract; report rejection instead."* **This document exists because the rejection still needs its vocabulary attached** — and because it carries a **real, dated observation about LE31's own append-only invariant** that is worth having on the record.

**This contract may be opened by an agent in exactly one circumstance:** LE31 gains its first write that crosses a system boundary (a Telegram send, a payment call, a receipt print), **or** the owner asks for an owner-visible log of who did what. **In that case** the agent must:

1. **Re-run the seven-check gate** for the *actual* audit feature. **This document does not substitute for that gate.**
2. Read the feature file and the artifact's `ADR-0004` summary together.
3. **Resolve the blocking charter question first** (see *Sign-off gap* #2): *which database does LE31 develop against?* The trigger mechanism **cannot be specified** until that is answered, because Postgres triggers and SQLite are different guarantees.

**Until then, this document is a record.** Implementing it as written — an `AuditLog` table, a `stock_entry` trigger, an `attempted` write path — would be **scope creep against a rejected proposal**, and the trigger half would **create a dev/prod divergence** rather than remove one.

## Frozen contract

**The one thing this contract records:** *LE31's append-only ledger is enforced by convention rather than by the database, and the two mechanisms that would change that — a DB trigger, and an `attempted`-before-the-write audit event — are recorded with their dev/prod costs attached.*

**The vocabulary, with the artifact's verbatim wording** (170-line README, `/tmp/le31-daily-2026-10-31/gh/readmes/sergeonito__odoo-gateway.md`):

| Idea | Verbatim |
|---|---|
| **DB-enforced append-only** | L36 — *"PostgreSQL table, **append-only through triggers (UPDATE, DELETE, TRUNCATE rejected)**"* |
| **Attempt before write** | L36 — *"an **`attempted` event before each Odoo write and the outcome after it**"* |
| **Why** | L149 — *"a write touches two systems; **`attempted` events and `Idempotency-Key` close the gap**"* |
| **Content rule** | L36 — *"**field names, not values**"* |
| **Refusals are audited too** | L35 — *"every 403 is audited"* |
| **Triggers are explicit, not implicit** | L138-139 — *"not see triggers, renames or data moves, so those parts are **written explicitly** (as the append-only triggers in migration 0001 are)."* |

**Two ideas transfer; the rest does not.**

**1. The guarantee lives in the database.** LE31's charter says *"Never update or delete ledger events"* and enforces it by **convention** — and currently by **there being no code that would**. The artifact enforces it **mechanically**: a trigger rejects `UPDATE`, `DELETE` and `TRUNCATE`, so the guarantee **survives a bug, a bad migration, or a `psql` session**.

**2. The log records the *attempt*, not just the outcome.** When a write spans two systems there is a window in which the write **may have happened** and the outcome was **never recorded** — the process died, the network hung. Writing the `attempted` event **first** makes that gap visible: the log contains an `attempted` with **no matching outcome**, and **that incompleteness is the signal**. A log of successes alone cannot distinguish *"did not happen"* from *"happened and we lost the record"*.

**What does NOT transfer:** the Odoo integration; Entra ID / MS365 auth; the RBAC model (LE31's roles are `UserRole` on `AppUser` — feature 403 owns the allowlist); Celery; the reconciliation endpoint; the stock-snapshot tables; and **`field names, not values` as an adopted policy** (that is an owner privacy decision about a surface that does not exist).

**The distinction that must not be lost — this is the reason this is a separate concept from the ledger:**

| | `StockEntry` (exists, never written) | Audit event (does not exist) |
|---|---|---|
| **What it is** | a **business fact**: quantity moved, and why | a **record of an attempt**: something was tried |
| **Append-only?** | yes — a charter invariant | yes — the artifact's mechanism |
| **Rejects writes?** | currently **no** (nothing writes it) | n/a |
| **Consumer** | the owner's stock numbers | **nobody yet** |
| **Rows per event** | one per quantity change | possibly two per write (`attempted` + outcome) |

**Collapsing the two is the mistake this document exists to prevent.** `StockEntry` is **the truth about the restaurant**; an audit event is **a record that something was tried**. A *refused* stock write is **not** a stock movement — writing it into `StockEntry` would corrupt the ledger the owner's numbers are derived from, and `le31-conventions` is explicit: *"Current stock is derived from entries."* **Anything that is not a quantity change does not belong in `StockEntry`.**

**The live, dated observation this record carries** — LE31's append-only invariant is **vacuously** upheld today:

```bash
grep -rn "\.update(\|delete(\|session.delete" backend/app/    # → NO MATCHES
grep -rn "StockEntry" backend/app/                              # → declaration only; no construction site
```

Nothing updates anything, because **nothing implements the ledger**. **The invariant is kept by the accident that the code which would break it has not been written** — and features 03, 04, 26, 34 and 45 all plan to write stock.

## Files to touch

**None.** This feature adds nothing to the repository.

| File | Change |
|---|---|
| `features/413-…md` | **NEW** (this pass). The vocabulary record. |
| `specs/413-…-HANDOFF.md` | **NEW** (this pass). This document. |
| `backend/**` | **NO CHANGE.** No model, no column, no trigger, no endpoint, no bot command. |

**Any change to `backend/` from this slice is a defect.**

## Mandatory LE31 skill list

An agent **reading** this contract (under the trigger condition above) must load:

- `le31-conventions` — the stock invariant, the privacy invariant and the seven-check gate.
- `le31-v1-feature-pattern` — the canonical contract shape and the slicing rules.
- `le31-handoff-spec` — the frozen-contract discipline.
- `development` — the generic code pipeline, **if and only if** the gate is re-run and passes.

An agent **not** acting on the trigger condition needs **none** of these; this document is a record.

## Mandatory inputs

- **Active feature**: `features/413-sergeonito-odoo-gateway-mit-python-fastapi-postgresql-rbac-…-v1-audit-attempt-and-trigger-enforcement-vocabulary.md`
- **Parent daily research report**: `/opt/data/le31-daily-research-2026-10-31.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-31/`
  - `gh/repos/sergeonito__odoo-gateway.json` — direct `GET /repos/` (HTTP 200)
  - `gh/readmes/sergeonito__odoo-gateway.md` — README, 170 lines, raw text (fetched by the **parent**, not the delegated subagent)
- **LE31 source of truth** (read-only):
  - `backend/app/models.py:113-126` — `class StockEntry` (the ledger, **never written**)
  - `backend/app/models.py:75-81` — `class AppUser` (`role: UserRole`) — the only actor record that exists
  - `backend/app/models.py:27-32` / `:54-59` — `TableStatus` / `StockReason` — **no audit or attempt member**
  - `backend/app/config.py:20` — `database_url: str = "sqlite:///./restaurant.db"` — **the dev default that makes a trigger guarantee production-only**
  - `backend/app/bot/cook_bot.py:11, 72, 82-83` — `/sold_out` advertised, **unregistered**
  - `grep -rn "audit_log\|class Audit" backend/app/models.py` → **NO OUTPUT**
  - `grep -rn "\.update(\|delete(\|session.delete" backend/app/` → **NO MATCHES**
- **Sibling features to read but NOT merge:** 374 (`qty_remaining`), 394 (guarded state transition), 403 (role-based bot allowlist), 405 (business day), 410 (money-rule reconciliation), **411 (money-precision guard — the sibling that shares the *dev/prod divergence* theme)**, and the parent report's *Adjacent evidence* for the **idempotency gap**, which is **not** bundled here.

## Verification protocol reference

**There is no verification protocol, because there is nothing to verify.** No code, no schema, no behaviour.

**The only check an agent may perform** is a read-only confirmation that the recorded first-party state is still true:

```bash
grep -rn "\.update(\|delete(\|session.delete" backend/app/   # expect: NO MATCHES (nothing mutates anything)
grep -rn "StockEntry" backend/app/                          # expect: declaration only, no construction site
grep -rn "audit_log\|class Audit" backend/app/models.py     # expect: NO OUTPUT
grep -n "sqlite" backend/app/config.py                     # expect: the dev default is still SQLite
```

**If any of those has changed** — the ledger is now written, or an audit table exists — **this document is stale and must be re-derived**, not acted on.

## Rollback path

**Nothing to roll back.** No code, no schema, no data.

**What remains safe if the document is deleted:** every LE31 behaviour. **The vocabulary and the dated observation are the only things it holds.**

**Trigger condition for revisiting:** LE31's first write that crosses a system boundary (a Telegram send, a payment call, a receipt print), **or** the owner asks for an owner-visible log of who did what. **At that point, re-run the gate** — and **resolve the database question first**, because the trigger mechanism's answer depends on it.

## Sign-off gap

**Every question in this slice is an unmade owner decision, and this artifact made none of them:**

1. **Does LE31 need an audit trail at all, distinct from the ledger?** **Recorded default: no, not in v1.** LE31's owner-facing surfaces need the ledger, not an audit log.
2. **If yes, does it need to be enforceable by the database?** **Recorded default: undecided, and BLOCKED on a separate question** — *which database does LE31 develop against?* §3.2 says Postgres in production; the dev default is SQLite (`config.py:20`); `le31-conventions` §*Known conflicts* names *"Postgres-only versus SQLite development"* as an **unresolved charter conflict**. **A trigger-based guarantee cannot be specified until that is resolved**, because the answer differs by backend. **Recorded as a dependency on an unresolved conflict, not as a recommendation.**
3. **Would LE31 write an `attempted` event before a write?** **Recorded default: only once LE31 has a write that can half-fail.** Before that, an `attempted` event is a record of nothing.
4. **Would the audit content be *"field names, not values"*?** **Recorded default: undecided.** It is a **privacy** decision and belongs to the owner. If adopted it is a policy about a surface that does not exist yet.
5. **Is an audit log guest data or operational data?** `le31-conventions`: *"v1 guest demographics are counts, not identity or contact data."* An audit log records **actor identity** and **action** — **operational data LE31 legitimately needs** (`AppUser` exists). **Recorded default: operational data, not guest data — but this is the owner's call**, and the two rules must be stated together so the audit surface does not become a back door around the privacy invariant.

**The agent must not widen any of these.** If the trigger fires, each needs its own decision and its own gate.

## Handoff summary

LE31's most important invariant — *"never update or delete ledger events"* — is currently kept by **nothing**: not by the schema, not by a constraint, not by a test. `grep -rn "\.update(\|delete(\|session.delete" backend/app/` returns **no matches**, and `StockEntry` is **never constructed**. The append-only discipline is **vacuously** true. **The moment the first stock write lands — and features 03, 04, 26, 34 and 45 all plan to write stock — the invariant will be upheld by the discipline of whoever writes that code, and nothing will catch them if they are not careful.**

`sergeonito/odoo-gateway` (MIT, Python + FastAPI + Postgres, in-window by both dates) offers the stronger form: *"PostgreSQL table, **append-only through triggers (UPDATE, DELETE, TRUNCATE rejected)**"*. **That mechanism is not adopted**, because it is **Postgres-only** and LE31's dev database is SQLite — adopting it would create **the same dev/prod divergence feature 411 exists to remove**, in the opposite direction: editable in dev, immutable in production.

The **second** idea is the one that will matter sooner, and it is the cheap one: **write the `attempted` event before the external write and the outcome after it** — *"a write touches two systems; `attempted` events and `Idempotency-Key` close the gap."* LE31's first write across a system boundary will be a **Telegram send**. If that send fails after the database has committed, LE31 will hold **a committed order and no record that anything was attempted**, and the owner's log will show a number that does not match what the waiter saw. **Recording the attempt first closes that gap, at the cost of one extra row.**

**The expensive time to learn it is after the first lost order.**
