# dc-tech-inc-dotnet-pos-integration-mit-csharp-dotnet-sql-server-idempotency-in-the-database-shortfall-instead-of-negative-stock-cursor-and-retry-launch-guards-at-the-terminal-v1-stock-deduction-idempotency-and-shortfall-vocabulary — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/382-dc-tech-inc-dotnet-pos-integration-mit-csharp-dotnet-sql-server-idempotency-in-the-database-shortfall-instead-of-negative-stock-cursor-and-retry-launch-guards-at-the-terminal-v1-stock-deduction-idempotency-and-shortfall-vocabulary.md`
> before touching anything. **This is a WATCH-LIST / DATA-SEMANTICS
> REFERENCE slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise an idempotency mechanism, a unique
> constraint, a `Shortfall` field, a reconciliation job, or any schema
> change.** It proposes **one document** recording two questions LE31
> has never answered, and nothing else.

## Frozen identifiers (do not rename)

- Feature ID: `382`
- Slug: `dc-tech-inc-dotnet-pos-integration-mit-csharp-dotnet-sql-server-idempotency-in-the-database-shortfall-instead-of-negative-stock-cursor-and-retry-launch-guards-at-the-terminal-v1-stock-deduction-idempotency-and-shortfall-vocabulary`
- Contract file: `features/382-dc-tech-inc-dotnet-pos-integration-mit-csharp-dotnet-sql-server-idempotency-in-the-database-shortfall-instead-of-negative-stock-cursor-and-retry-launch-guards-at-the-terminal-v1-stock-deduction-idempotency-and-shortfall-vocabulary.md`
- Bucket: **v1 (stock-ledger semantics vocabulary)** — defer
- Linear parent: **not created — Linear MCP write endpoint blocked (39th consecutive day), requestId `a50781689b353a4a`** (a separate write probe also failed, requestId `a5076ad3de8335ea`)
- Linear sub-issue: **not created — same blocker**. Intended payload at `/opt/data/le31-daily-research-2026-10-26.linear-fallback.json`
- Source repo: GitHub `dc-tech-inc/dotnet-pos-integration` (MIT), ★0/⑂0, 97 KB, C#/.NET 10 + SQL Server, created 2026-10-22T15:51:29Z, pushed 2026-10-22T20:19:34Z, 4 open issues
- Raw fetch: `/tmp/le31-daily-2026-10-26/pv/dc-tech-inc__dotnet-pos-integration.json`
- README + file tree: `/tmp/le31-daily-2026-10-26/rd/dc-tech-inc_dotnet-pos-integration.md`
- Report: `/opt/data/le31-daily-research-2026-10-26.md`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** The artifact exists and is real
(direct `/repos/` GET, HTTP 200, in-window by both `created_at` and
`pushed_at`; README and file tree read, not just the description).

**And the gap it names is parent-verified inside LE31's own
codebase.** `backend/app/models.py:113-126` defines `StockEntry` with
`ref_order_item_id` (nullable, unconstrained). Parent-verified by grep
across all 9 Python files in `backend/` on 2026-10-26:

- `grep -rniE "idempot|dedup|duplicate" --include=*.py backend/` → **0 matches**
- `grep -rniE "shortfall|negative" --include=*.py backend/` → **1 match**, and it is only a sign convention on `qty_delta` (`models.py:122`)
- `grep -rniE "reconcil" --include=*.py backend/` → **1 match**, and it is only a docstring on the unrelated `Shift` model (`models.py:181-182`)

**So the gap is real and observable in the code. But it is NOT a
reported pain.** No LE31 owner, waiter, or cook has said "the same
order got written twice" or "we sold more stock than we had". An
internal gap is not a `reported` or `observed` pain, and check 1
requires one.

**Confidence: high** for the artifact's existence, licence, size, and
content (direct API read, README and all six ADRs read verbatim).
**High** for the LE31-side gap (three greps over the whole backend,
reproducible). **Low-to-none** for the *prevalence* of the failure in
LE31's actual usage — **no claim is made about how often it happens**,
because no evidence either way exists.

**Decision: defer (vocabulary reference).** Check 1 (JTBD) **fails**:
the pain is real in the code but has never been reported by a user.
Checks **3** and **4** also fail: C#/.NET + SQL Server is off-stack
(§3.2), and a dedup key plus a `Shortfall` concept are **new data
model** requiring an explicit charter decision.

**Known rabbit hole:** treating "LE31 has no idempotency guard" as
"LE31 should build an idempotency guard today". **The gap is real;
the build is not authorised.** The missing thing is not code — it is
the **owner's answer** to two questions.

**Circuit breaker:** if the document is never written and the owner is
never asked, this remains an unused reference. **Acceptable outcome.**
The cost of the artifact is one file.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-10-26 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.
5. `le31-handoff-spec` — the frozen-contract discipline this slice follows.

If the destination repo does not ship these skills, request them
from the project owner before starting. **Do not invent LE31
conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/382-…-v1-stock-deduction-idempotency-and-shortfall-vocabulary.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No model is changed. No UI is built. No Alembic revision is
written. No unique index is created. No `Shortfall` field, enum, or
table is added.**

## What the coding agent must NOT do

- **Do not add an idempotency mechanism.** No `ProcessedSale` table, no
  unique index on `ref_order_item_id`, no application-level
  check-then-act, no `Duplicate` return path. **The ADR explicitly
  rejects the application-level check — "there is no 'have I seen
  this?' read in application code, so there is no check-then-act race" —
  so a naive `if not seen: insert` would reproduce the exact defect
  the ADR warns about.**
- **Do not add a `Shortfall` field, enum, model, or ledger event.**
- **Do not write a reconciliation routine or a reconciliation job.**
- **Do not make `ref_order_item_id` non-null, unique, or indexed.**
- **Do not change `StockEntry`'s schema in any way.**
- **Do not port, vendor, or translate the C#/.NET implementation.** The
  licence is MIT and the code is legally adoptable — **but adopting it
  would be a §3.2 stack change** (C#/.NET + SQL Server inside a Python
  3.13 / FastAPI / SQLModel / Postgres product) and needs an explicit
  charter decision.
- **Do not implement ADR-0004 (cursor + retry).** It presumes a remote
  system to poll. **LE31's waiter writes to LE31's own database in the
  same request.** There is nothing to poll.
- **Do not implement ADR-0006 (launch guards at the terminal).** It
  presumes a cash drawer, a keylock, a barcode scanner and a
  per-terminal session model — **OMG UnifiedPOS device vocabulary.**
  LE31 has no POS terminal and no hardware of any kind.
- **Do not implement ADR-0003 (Dapper / plain SQL) or ADR-0005
  (PowerShell tooling).** Stack-specific, no transferable content.
- **Do not add deduplication to the Telegram bot layer.** A bot-level
  guard would be a second representation of a fact the ledger owns
  (§3.3). **Dedup belongs in the database and the write path.**
- **Do not re-litigate the oversell question as a build.** Feature 373
  already holds it as an open owner decision. This artifact adds a
  third candidate answer, nothing more.
- **Do not edit `PROJECT_CHARTER.md`, `le31-conventions`, or any other
  skill file.** The artifact **proposes** the questions; it does not
  **answer** them.
- **Do not confuse this with the HTTP idempotency-key work.** Features
  259, 269 and 303 cover endpoint-level idempotency for client-retryable
  requests. **ADR-0001 is ledger-write-level idempotency keyed by a
  business event, enforced inside the stock transaction.** Any future
  proposal must state which one it is.
- **Do not reuse `row_hash` as the dedup key.** Features 49 and 52
  create unique indexes on `row_hash` and `anchor_hash` for **hash-chain
  integrity**. A hash-chain row hash and a business-event id are
  different things, and a future implementation must not collide with
  them.

## The proposed boundary (the actual deliverable content)

**One document.** It records:

1. **The question:** *"What happens in LE31 when the same business event
   writes `StockEntry` twice?"* — with the parent-verified evidence
   that **nothing in LE31 prevents it today**, and the three greps that
   establish it, quoted so the next reader can reproduce it.
2. **The second question:** *"What does LE31 do when a sale asks for more
   stock than exists?"* — with the three external answers now on the
   table (`warung-pos`: keep the negative and surface it; `dc-tech-inc`:
   never go negative, record the difference; `fnb-erp-django`: compute
   weighted-quantity deduction and average cost of goods, which §3.3
   forbids).
3. **The candidate answers**, in the ADR's own words, including the
   anti-patterns it names: *"no check-then-act race"*, *"no back-order or
   automatic correction"*, and *"a supervisor may accept a risk but cannot
   change a fact"*.
4. **The ADRs that are out of scope** (0004, 0006) and the one-line
   reason each does not apply to LE31.

**The document must NOT answer the questions.** It puts them on the
table with a candidate answer each, and leaves the decision with the
owner.

## Trigger for the next step

- The owner asks what happens when the same order is submitted twice,
  when a waiter double-taps send, or when two waiters touch the same
  ticket → **this slice is the pre-written answer.**
- A PR touches `backend/app/models.py` `StockEntry`, or adds a write
  path that appends `StockEntry` rows → **this slice must be read
  first**, because that PR is the moment the question becomes live.
- A PR adds a unique constraint or an idempotency key → **this slice
  must be read first**, to check it is ledger-level and not
  endpoint-level, and to check it does not collide with features 49/52.
- The owner answers either question → **the feature gate is re-run from
  scratch** with the owner's words as `reported` evidence, and only
  ADR-0001 alone would be in scope for a first build.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/`.

**For this slice (documentation only):**

1. The document exists and names the two questions **as questions**.
2. The document contains **no schema, no field, no table, no index,
   and no migration** — verified by `git diff --stat` showing exactly
   one added file (this handoff) plus the contract file.
3. `grep -rniE "idempot|dedup|Shortfall" --include=*.py backend/`
   still returns **0 matches for `idempot`/`dedup`** — i.e. **the
   reference has not leaked into the codebase.**
4. The document **cites** the three greps that establish the gap, so a
   future reader can reproduce it.
5. The document **does not answer the oversell question** on the owner's
   behalf — the two candidate answers are presented side by side with
   the decision left open.

**If the gate is ever re-run and a build is approved, the acceptance
path for ADR-0001 alone is:** submit the same order twice, then inspect
the ledger and confirm **exactly one** `StockEntry` row exists for it,
that the second submission produced **no** row and **no** partial
write, and that the bot/web surface reported the duplicate to the
user. **A router response is not acceptance.**

## Rollback path

**Delete one file.** The slice adds no migration, no schema change, no
model, and no runtime behaviour, so the rollback is `rm` on the
document plus the feature-contract file. **There is no data to
reconcile and no state to unwind.**

**If a future build is ever approved**, the rollback path must be
written *before* the migration and must include: the new table or
column dropped, the uniqueness guarantee removed, and — because
`StockEntry` is append-only under §3.3 — **an explicit statement that
existing ledger rows are never rewritten to "fix" a duplicate.** A
duplicate written after the fact stays in the ledger; it is corrected
by a compensating entry, never by an edit.

## Open questions carried into the slice

1. **Should the same business event append one `StockEntry` or two?**
   — the load-bearing question. **Unanswered.**
2. **Should an oversell record a negative quantity, or record the
   difference separately?** — three external answers on the table;
   the owner has chosen none.
3. **Is `ref_order_item_id` the right dedup key, or is a dedicated
   business-event id needed?** — `ref_order_item_id` is nullable today.
4. **Does the guarantee live on the `StockEntry` row, or on a separate
   append-only ledger event?** — §3.3 says ledger events are never
   deleted, so a "processed" marker row has its own lifetime question.
5. **Does an oversell need an owner-visible surface?** — feature 373
   noted LE31 has no "something is wrong and the owner should look"
   surface. `Shortfall` is per-movement, which is not the same thing.
6. **Is "a supervisor may accept a risk but cannot change a fact"
   applicable to LE31 at all?** — LE31 has no supervisor role. Recorded
   as vocabulary; no LE31 analogue is proposed.
