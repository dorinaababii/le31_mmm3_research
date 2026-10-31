# Feature 413 — `sergeonito/odoo-gateway`: an `attempted` audit event *before* the write, and DB-level triggers that make the ledger append-only in the database itself — vocabulary for LE31's StockEntry immutability

> **Pick C of Daily Research 2026-10-31 (93rd pass).** **VOCABULARY ONLY — `defer`.** The artifact is a real, on-stack FastAPI + Postgres implementation of two mechanisms LE31's charter *asserts* but does not enforce: **an append-only audit table enforced by database triggers**, and **an `attempted` event written *before* the external write, with the outcome written after**.
>
> `sergeonito/odoo-gateway` (MIT, ★0/0⑂, **Python**, 344 KB, created 2026-10-26, pushed 2026-10-27 — **in-window by both `created_at` and `pushed_at`**; all fields parent-verified via direct `GET /repos/` at `/tmp/le31-daily-2026-10-31/gh/repos/sergeonito__odoo-gateway.json`; topics `audit-log, celery, entra-id, fastapi, odoo, postgresql, rbac`).
>
> Its README states, verbatim:
>
> > L36 — *"| Audit | PostgreSQL table, **append-only through triggers (UPDATE, DELETE, TRUNCATE rejected)**; an **`attempted` event before each Odoo write and the outcome after it**; **field names, not values** |"*
> >
> > L35 — *"| RBAC | Roles `viewer` / `operator` / `admin` → permissions; routes depend on permissions only; **every 403 is audited** |"*
> >
> > L149 — *"- [ADR-0004](docs/adr/0004-audit-after-the-call.md): a write touches two systems; **`attempted` events and `Idempotency-Key` close the gap**"*
> >
> > L138-139 — *"not see triggers, renames or data moves, so those parts are **written explicitly** (as the append-only triggers in migration 0001 are)."*
>
> **Bucket: v1.** MIT ✓ §3.2 strictly-compatible; Python + FastAPI + Postgres **on-stack**. **Vocabulary-only — `defer`.** Evidence class: **INFERRED** (no LE31 owner has asked for an audit trail; **and LE31's `StockEntry` ledger is never written at all today**).
>
> **⚠️ Gate check 1 FAILS.** No reported owner pain for an audit surface. The evidence class is **INFERRED**.
>
> **⚠️ Gate check 4 note — a genuine architectural tension, surfaced and not resolved.** The artifact's triggers are **Postgres-only** (§3.2's production database), but **LE31's dev database is SQLite** (`backend/app/config.py:20`: `database_url: str = "sqlite:///./restaurant.db"`). **SQLite has no `CREATE TRIGGER` equivalent in the ORM layer and no equivalent enforcement of `UPDATE`/`DELETE` rejection** — so a trigger-based append-only guarantee would be **enforced in production and absent in development**, exactly the dev/prod divergence that feature 411 exists to remove. **This is why the artifact's mechanism is vocabulary, not a proposal.** LE31's charter invariant (*"Never update or delete ledger events"*) is currently upheld **vacuously** — `grep -rn "\.update(\|delete(\|session.delete" backend/app/` returns **no matches**: nothing updates anything, because nothing implements the ledger at all.

## Goal

**Record two vocabulary ideas from an on-stack artifact that LE31's charter already asserts but does not enforce**, and state plainly — for each — **what it would take in LE31 and why it is not being done now**.

**The single sentence this feature exists to make true:** *LE31's append-only ledger is enforced by convention rather than by the database, and the two mechanisms that would change that — a DB trigger, and an `attempted`-before-the-write audit event — are recorded with their dev/prod costs attached.*

**This feature produces no code and changes no behaviour.** It is a **parking-lot** entry with the vocabulary written down.

## Scope

**In scope (v1):**

- **A written vocabulary** for: a database-enforced append-only table; an `attempted` event written *before* an external write and an outcome event written *after*; and *"field names, not values"* as an audit-content rule.
- **An explicit statement of what each would cost in LE31**, including the **SQLite/Postgres divergence** that makes the trigger mechanism a production-only guarantee.
- **A mapping onto LE31's own `StockEntry`**, with the vocabulary of "ledger event" kept distinct from "audit event".

**Out of scope (v1):**

- **Any migration, trigger, table, column, endpoint or bot command.** This feature **adds nothing to `backend/`**. It is a **document**.
- **Any `AuditLog` model.** LE31 has none — `grep -rn "audit_log\|class Audit" backend/app/models.py` → **no output**.
- **Any change to `StockEntry`.** Its append-only discipline is a **charter invariant** (`le31-conventions`: *"Never update or delete ledger events"*), and this feature does not weaken it, strengthen it, or reimplement it.
- **The `Idempotency-Key` mechanism.** LE31 has no idempotency anywhere. **This is a real first-party gap and it is recorded in the parent report's *Adjacent evidence* — but it is a different gap and it is not bundled here.** Bundling three gaps into one feature is exactly the scope creep `le31-conventions` §*Hard invariants* warns about (*"build exactly the accepted outcome"*).
- **The Odoo integration itself.** LE31 talks to no ERP and needs no ERP.
- **Entra ID / MS365 authentication, RBAC, Celery, the reconciliation endpoint, the stock-snapshot tables.** None of that transfers.
- **`field names, not values` as an implemented policy for LE31.** It is a **privacy-shaped** idea — record *that* a field changed, not *what* it changed to. It is **recorded** here because LE31's privacy invariant is *"store only data needed for restaurant operations"*, but **adopting it is an owner decision about the audit surface, and no audit surface exists to apply it to.**

## Description

### What the artifact demonstrates, precisely

`sergeonito/odoo-gateway` is a small (344 KB) FastAPI gateway in front of Odoo. Two mechanisms in it bear on LE31, and **both are about making a promise the database can keep, rather than the application promising it.**

**1. The append-only guarantee lives in the database.**

> L36 — *"PostgreSQL table, **append-only through triggers (UPDATE, DELETE, TRUNCATE rejected)**"*

This is the *stronger* form of LE31's invariant. LE31's charter says *"Never update or delete ledger events"* — and enforces it by **convention and by there being no code that would**. The artifact enforces it **mechanically**: a trigger on the table rejects `UPDATE`, `DELETE` and `TRUNCATE` outright, so **the guarantee survives a bug, a bad migration, or a `psql` session**.

**2. The audit log records the *attempt*, not just the outcome.**

> L36 — *"an **`attempted` event before each Odoo write and the outcome after it**"*
>
> L149 — *"a write touches two systems; **`attempted` events and `Idempotency-Key` close the gap**"*
>
> L83 — *"A recorded walk through the same commands, 80 seconds: reads, **a refused write and its audit event**, `Idempotency-Key` replay, the audit pair, Odoo down"*

The reasoning is the transferable part. When a write spans **two systems** (LE31's database *and* an external call), there is a window in which the write may have happened and the outcome was never recorded — the process died, the network hung. **Writing the `attempted` event first means the gap is visible**: the audit log contains an `attempted` with **no matching outcome**, and that incompleteness is the signal. **A log that only records successes cannot distinguish "did not happen" from "happened and we lost the record".**

**3. A small content rule worth noting.**

> L36 — *"**field names, not values**"*

An audit event records *which* field was touched, not the value. That keeps an audit log from becoming a second copy of the business data — which is exactly LE31's privacy shape.

### Why this is `defer` and not `build`

1. **No owner pain.** Evidence class **INFERRED**. No LE31 owner has asked for an audit surface, and **an audit surface has no consumer**: the owner-facing surfaces LE31 has planned (end-of-day recap, stock board) would consume the ledger, not a separate audit log.
2. **There is nothing to audit yet.** `StockEntry` is **never constructed** anywhere in `backend/` — the grep for `StockEntry` outside `models.py` returns **no hits**. `OrderItem` is likewise never constructed. **There are no operational transitions happening, so there is nothing whose attempts need recording.** The invariant is upheld *vacuously*: `grep -rn "\.update(\|delete(\|session.delete" backend/app/` → **no matches**.
3. **The trigger mechanism is production-only.** SQLite — LE31's dev database — does not give this guarantee. Adopting it would create **the same dev/prod divergence that feature 411 exists to remove**, in the opposite direction: in dev the ledger would be *editable*, in production it would not. **A ledger that behaves differently in the environment where the tests run is worse than one that behaves the same way and is merely conventional.**
4. **The `attempted`/outcome pairing assumes a two-system write.** LE31 writes to **one** database and calls **no** external service. The gap the artifact closes does not exist in LE31 — **yet**. It will exist the moment LE31 sends a Telegram message or calls a payment provider, and **that is the moment this becomes relevant.**

**The trigger condition for revisiting this:** LE31's first write that crosses a system boundary (a Telegram send, a payment call, a receipt print), **or** the owner asks for an owner-visible log of who did what. At that point the `attempted`/outcome pairing is the vocabulary to reach for — and the trigger idea needs a **SQLite-aware** answer rather than a copy of the artifact's.

## Data model

**No new table. No new column. No schema change. No code.**

This feature's "data model" section records **what a future audit surface would need** and, more importantly, **how it differs from LE31's ledger**:

```
A future audit surface would need at minimum:

  occurred_at     -> when the attempt happened
  actor_id        -> who attempted it (AppUser.id exists today)
  action          -> what was attempted
  outcome         -> succeeded / refused / failed / unknown
  field_names     -> WHICH fields were touched (not their values)

None of these exist today, and no table should be created for them yet.
```

**The distinction that must not be lost, and is the reason this is a separate concept from the ledger:**

| | `StockEntry` (exists, never written) | Audit event (does not exist) |
|---|---|---|
| **What it is** | a **business fact**: quantity moved, and why | a **record of an attempt**: something was tried |
| **Append-only?** | yes — a charter invariant | yes — the artifact's mechanism |
| **Rejects writes?** | currently no (nothing writes it) | currently n/a |
| **Consumer** | the owner's stock numbers | nobody yet |
| **Rows per event** | one per quantity change | possibly two per write (`attempted` + outcome) |

**Collapsing these two is the mistake this document exists to prevent.** `StockEntry` is **the truth about the restaurant**; an audit event is **a record that something was tried**. A refused stock write is *not* a stock movement, and writing it into `StockEntry` would corrupt the ledger that the owner's numbers are derived from — and `le31-conventions` is explicit: *"Current stock is derived from entries."* **Anything that is not a quantity change does not belong in `StockEntry`.**

## Implementation steps

**There is no implementation.** This is a `defer` — a parking-lot vocabulary artifact. Per `le31-feature-pipeline` §*Hard rules*: *"If the pick fails the gate, do not write a contract; report rejection instead."* **This handoff exists as a record of the rejection, with the vocabulary attached**, and it must state plainly that **a coding agent must not implement it**.

**What a future agent may do with this document:** if LE31 ever gains a write that crosses a system boundary, **read this document and the artifact's ADR-0004 together**, and **re-run the seven-check gate for the actual audit feature**.

**What a future agent must not do:** create an `AuditLog` table; add a Postgres trigger to `stock_entry`; reuse `StockEntry` to record refusals or attempts; add `Idempotency-Key` headers to LE31's routes; add an `AuditLog` write path; or copy the artifact's RBAC, Entra ID, Celery or Odoo integration.

## Telegram interaction if any

**None.** This feature touches no bot command.

**One observation is recorded because it bears on a *future* decision:** LE31's cook bot has **no** handler for `/sold_out` — advertised in the bot's own docstring (`cook_bot.py:11`) and in `/help`'s output (`cook_bot.py:72`), but **with no handler function and no registration** (`cook_bot.py:82-83` register only `/start_today` and `/help`). **A bot that marks an item sold out is a write to an external surface** (the waiter's menu), and once it exists, LE31 **will** have a write that crosses a system boundary — **which is precisely the situation this vocabulary is for.** Recorded, not proposed.

## Dependencies

**Read-only references. This feature depends on nothing to build, because it builds nothing.**

- **The artifact's README** — `/tmp/le31-daily-2026-10-31/gh/readmes/sergeonito__odoo-gateway.md` (170 lines, fetched by the parent on 2026-10-31; **not** via the delegated subagent, which saved only 3 READMEs).
- **The artifact's direct repo metadata** — `/tmp/le31-daily-2026-10-31/gh/repos/sergeonito__odoo-gateway.json` (HTTP 200).
- **LE31 first-party state to read but NOT change:**
  - `backend/app/models.py:113-126` — `class StockEntry` (the ledger, never written)
  - `backend/app/models.py:75-81` — `class AppUser` (`role: UserRole`) — the only actor record that exists
  - `backend/app/config.py:20` — the SQLite dev default that makes the trigger mechanism production-only
  - `backend/app/bot/cook_bot.py:11, 72, 82-83` — `/sold_out` advertised, unregistered
- **Sibling features to read but NOT merge:** 374 (`qty_remaining`), 394 (guarded state transition), 403 (role-based bot allowlist), 405 (business day), 410 (money-rule reconciliation), 411 (money-precision guard — the sibling that shares the **dev/prod divergence** theme), and the parent report's *Adjacent evidence* for the **idempotency gap**, which is **not** bundled here.
- **`le31-conventions`** — the stock invariant, the privacy invariant and the seven-check gate.
- **`le31-handoff-spec`** — the frozen-contract discipline (used here to *record a rejection*, not to authorise work).

## Open questions

**All owner decisions. None is decided here, and none is decided by this artifact.**

1. **Does LE31 need an audit trail at all, distinct from the ledger?** **Recorded default: no, not in v1.** LE31's owner-facing surfaces need the ledger, not an audit log.
2. **If yes, does it need to be enforceable by the database?** **Recorded default: undecided, and the decision is blocked on a separate one** — *which database does LE31 develop against?* §3.2 says Postgres in production; the dev default is SQLite; `le31-conventions` §*Known conflicts* names *"Postgres-only versus SQLite development"* as an unresolved charter conflict. **A trigger-based guarantee cannot be specified until that is resolved**, because the answer differs by backend. **This is recorded as a dependency on an unresolved charter conflict, not as a recommendation.**
3. **If yes, would LE31 write an `attempted` event before a write?** **Recorded default: only once LE31 has a write that can half-fail** (an external call). **Before that, an `attempted` event is a record of nothing.**
4. **Would the audit content be *"field names, not values"*?** **Recorded default: undecided.** It is a **privacy** decision and it belongs to the owner. If adopted, it is a policy about a surface that does not exist yet.
5. **Is the *audit log* subject to the same privacy rule as guest data?** `le31-conventions`: *"v1 guest demographics are counts, not identity or contact data."* An audit log records **actor identity** and **action** — **which is operational data LE31 legitimately needs** (`AppUser` exists), but the two rules must be stated together so the audit surface does not become a back door around the privacy invariant. **Recorded default: an audit log is operational data, not guest data — but this is the owner's call.**

## Why this matters

Because LE31's most important invariant — *"never update or delete ledger events"* — is currently kept by **nothing**. Not by the schema, not by a constraint, not by a test. **It is kept by the accident that the code that would break it has not been written.**

`grep -rn "\.update(\|delete(\|session.delete" backend/app/` returns **no matches**. The append-only discipline is **vacuously** true. The moment the first stock write lands — and features 03, 04, 26, 34 and 45 all plan to write stock — the invariant will be upheld by **the discipline of whoever writes that code**, and there will be **no mechanism** to catch them if they are not careful.

That is the right time to have the answer ready, and the wrong time to guess it. The artifact's answer — **triggers, not convention** — is stronger than LE31's current arrangement, but **only on the database LE31 uses in production**, and LE31's charter conflict about which database that development targets is still unresolved. **So the artifact is not adopted; it is recorded, with its cost attached**, so that when the owner resolves the database question the ledger-enforcement question is already on the table with a real answer attached to it.

And the second idea is the one that will matter sooner: **the `attempted`-before-the-write pattern.** LE31's first write that crosses a system boundary will be a Telegram send. If that send fails after the database has committed, LE31 will have **a committed order and no record that anything was attempted** — and the owner's log will show a number that does not match what the waiter saw. **Recording the attempt first closes that gap.** The idea costs one extra row. **The expensive time to learn it is after the first lost order.**
