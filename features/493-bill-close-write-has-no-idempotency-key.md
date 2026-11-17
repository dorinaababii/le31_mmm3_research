# Feature 493 — The bill-close write has no idempotency key, so a retry is indistinguishable from a first attempt

> **Pick B of Daily Brainstorm 2026-11-17 (106th daily-brainstorm pass).**
> Bucket: **v1 — Core MVP**. Verdict: **`build`** (a vocabulary+guard reference that
> names a first-party gap; the *code* change is deferred to the feature that owns the
> bill-close write).
> Evidence class: **OBSERVED** — the source's mechanism is read verbatim from its
> in-window README; the LE31-side gap is **proved by EXECUTION** against LE31's real
> schema and by a corpus-wide grep.
>
> **Source artifact:** `shyampandey1104/erpnext-pos-offline-pwa-hybrid-counter` —
> *"ERPNext POS Offline Progressive Web App (PWA) Hybrid Counter"*.
> MIT licence, ★0, ⑂0, created **2026-10-19**, pushed **2026-11-17** — **in-window by
> BOTH `created_at` and `pushed_at`**.
> Python / Frappe-ERPNext.
> URL: https://github.com/shyampandey1104/erpnext-pos-offline-pwa-hybrid-counter
> Raw README: `/tmp/le31-brainstorm-2026-11-17/gh/shyampandey1104__erpnext-pos-offline-pwa-hybrid-counter.README.md`
> Raw repo JSON: `/tmp/le31-brainstorm-2026-11-17/gh/shyampandey1104__erpnext-pos-offline-pwa-hybrid-counter.repo.json`

## Goal

Make one sentence true that LE31 cannot currently say:

> **If LE31's bill-close write is retried — by a double tap, by a proxy retry, by a
> dropped connection — the second attempt is recognised as the same bill and does not
> bill the guest twice.**

Feature 388 already establishes this rule for the **seat** transition. This feature
establishes it for the **bill-close** transition, which is the write that **moves
money** and which LE31's schema currently gives **no protection at all**.

## Scope

**In scope (v1):**

- The **vocabulary and the rule** for an idempotent write: a caller-supplied
  **idempotency key** that the server stores and that makes a repeat of the same
  logical write return the **first** result instead of performing a second write.
- A **named, narrow application to the bill-close write** — the write that creates
  the `Bill` row, computes the `DerivedTip`, and deducts stock.
- The **precise statement of what is NOT yet owned**, so a future implementer does
  not have to re-derive it: the stock-deduction write's idempotency is already
  covered elsewhere in the corpus, and the seat write's is covered by feature 388.

**Out of scope (v1):**

- **The offline client, the IndexedDB queue, the service worker and the background
  sync.** LE31 is a single-VPS, online, server-authoritative system (charter §3.2);
  feature 373 already records this boundary in full. This feature is the **server
  half only**.
- **The stock-deduction write's idempotency** — already covered by features 400 and
  401 (see "What is already owned"). Do not re-implement.
- **The seat write's idempotency** — owned by feature **388**. Do not re-implement.
- **Any change to `Bill`, `DerivedTip`, `OrderItem` or `Visit` schemas in this
  contract.** The idempotency key's *storage* is the subject of the feature that owns
  the bill-close write (feature 415 per feature 448's cross-reference); this contract
  names the requirement and the rule, and does not perform the migration.
- **A full offline-first implementation.** Explicitly deferred — see feature 373.

## Description

### The source's mechanism, verbatim

From the in-window README:

> *"**Idempotent Background Synchronization:** Uses UUID v4 tokens to guarantee that
> no invoice is ever submitted twice, even if the connection fluctuates mid-sync."*

and, from the architecture diagram, the client→server contract:

> *"**Idempotent Ingestion Engine** … Validate Stock Balances … Submit POS Invoices &
> Update General Ledger … **Return Server Invoice Numbers**"*

and the client-side half:

> *"**Local Receipt Printing**"* and *"processes payments locally … When connectivity
> resumes, the engine queues and pushes transactions in idempotent batches with
> automated sequence reconciliation."*

Three separable pieces:
1. **the client mints a token** (UUID v4) for the logical document;
2. **the server's ingestion engine recognises a replay** by that token;
3. **the server reconciles its own assigned number back** into the client's local
   record after accepting the batch.

**Pieces 2 and 3 are the portable half.** Piece 1 is client-side and out of scope.

### LE31's own state, by execution

The parent built LE31's real schema (`SQLModel.metadata.create_all` on a throwaway
SQLite DB from `backend/app/models.py`) and inspected it. Script:
`/opt/data/le31-brainstorm-2026-11-17-scripts/audit_lifecycle.py`.

```
--- PICK B: idempotency / client dedup on writes ---
  idempotency tokens in backend: NONE
  PASS  backend has NO idempotency key on any write
  UNIQUE indexes in the real schema: [('bill', 'sqlite_autoindex_bill_1')]
```

Read that carefully — it is the whole finding:

- **No idempotency token exists anywhere in LE31's backend.** The grep for
  `idempot|dedup|Idempotency-Key|uuid4|request_id|client_token|conflict` over
  `backend/app/main.py`, `backend/app/routers/tables.py` and
  `backend/app/bot/cook_bot.py` returns **zero hits**.
- **The only UNIQUE index in the entire schema is `bill.visit_id`.**

That second fact cuts both ways, and the direction matters:

- **It partly protects the bill-close write.** `Bill.visit_id` is `unique=True`, so a
  *duplicate bill for the same visit* is rejected by the database. A retry of the
  bill-close write **cannot** create a second `Bill` row for the same visit.
- **It does NOT make the write idempotent.** A unique constraint says *"one bill per
  visit"*. It does not say *"this retry is the same bill"*. The difference is
  observable:

| | a unique constraint | idempotency |
|---|---|---|
| a duplicate write | **rejected** (an error) | **accepted, returns the first result** |
| the caller's experience | an error it must interpret | a success it can rely on |
| the `DerivedTip` row | **not written** (the write aborted) | **the same one**, not a second |
| the stock deduction | **not applied** | **not applied again** |

**A caller that retries after an ambiguous failure — the timeout case — gets an
error, not the original bill.** If the caller cannot distinguish "my first attempt
succeeded and the response was lost" from "my first attempt failed", it has no
correct recovery. A unique constraint makes the *duplicate* impossible; it does not
make the *retry* correct.

### The two-write gap, precisely

LE31 has three state-changing writes of consequence. Their idempotency status:

| write | idempotency | owner |
|---|---|---|
| **seat** (`POST /{table_id}/seat`) | owned — feature **388** (adds the `Table.status` column and a 409) | feature 388 |
| **stock deduction** | owned — features **400** / **401** (client UUID, idempotent sync) | features 400/401 |
| **bill close** (creates `Bill`, writes `DerivedTip`, deducts stock) | **NOT owned** | **this feature** |

The corpus sweep for the bill-close case specifically returns **zero** files:

```
PICK 493 — idempotent-write-endpoint-for-retryable-state-changes
    idempotency key on the BILL CLOSE write specifically -> 0 []
    idempotency key on the STOCK DEDUCTION write specifically -> 14 [...]
    an idempotency key carried by a REQUEST on any route -> 23 [...]
```

**This narrowing is deliberate and is the honest scope.** The generic "idempotency
key" concept is **well covered** in the corpus (23 files carry a request-level
idempotency key). What is **not** covered is the *application* of that concept to
the one write that moves money. Re-filing "idempotency is a good idea" would be a
duplicate; naming the **bill-close** write as the uncovered instance is not.

This is the seventh finding shape — *a covered concept, an uncovered INSTANCE* —
and the corpus-wide grep is what found it. A filename check would have found
nothing; a concept sweep for "idempotency" would have returned 23 hits and stopped.

### Why the bill-close write is the right instance

The bill close is where LE31's **three** invariants meet:

1. a `Bill` row is created (money is recorded);
2. a `DerivedTip` row is written — and feature **457** already records that this row
   *"is a free-standing number"* with no constraint tying it to its own formula;
3. stock is deducted, per the append-only `StockEntry` ledger.

A retry that partially applies is the dangerous case. If the `Bill` insert succeeds
and the stock deduction fails, the retry hits the unique constraint on
`bill.visit_id`, **errors**, and the caller is left with a bill and no deduction —
and no way to tell that from a genuine first-attempt failure. The idempotency key
is what lets the server recognise "this is the same logical bill" and **complete**
the remaining steps rather than refusing.

### The rule (the transferable part)

> **A write that moves money and can be retried carries a caller-supplied
> idempotency key. The server stores the key with the outcome. A repeat of the same
> key returns the stored outcome and performs no second write.**

Three properties, all from the source's vocabulary:

- **The key is minted by the caller**, not the server. A server-minted key cannot
  survive a lost response — the caller never learns it.
- **The key is stored with the outcome**, so the repeat is a **read**, not a
  re-execution. This is what makes it "idempotent" rather than "rejected".
- **The server reconciles its own number back**, so the client's local record and
  the server's record agree afterwards. For LE31 this is the `Bill` row's
  human-facing number (feature **448** owns the number's shape;
  `<service-day>-<sequence>`), not an auto-increment id.

## Data model

**No schema change in this contract** — see "Out of scope". The requirement this
feature places on the feature that owns the bill-close write is stated as an
**interface contract**, so that implementer can choose the storage:

```
The bill-close route SHALL accept an optional idempotency key.

  Request:  POST /api/visits/{visit_id}/bill
            Idempotency-Key: <caller-minted opaque string>
            { subtotal_items, subtotal_tax, total_due, total_paid,
              payment_method }

  First call   -> 201 { bill_id, bill_number, derived_tip, ... }
  Repeat call  -> 200 { bill_id, bill_number, derived_tip, ... }   # SAME body
  Repeat with a DIFFERENT body under the SAME key -> 409 (the key is bound to
                                                        the first body)
```

**The key is bound to the request body.** A key reused with a *different* body is a
client bug; returning the first result for a different body would silently accept a
second, different bill. `409` is the honest answer.

**Where the key is stored** is the implementing feature's choice; the corpus already
contains the two candidate shapes, and the implementer should read them rather than
invent a third:

- features **400** / **401** — a client-UUID column and a client-UUID idempotent
  sync vocabulary;
- features **259** / **412** — a transactional-outbox / idempotent-inbox shape.

## Implementation steps

This contract implements **no code**. It hands the implementing feature:

1. **The rule**, verbatim, as in "The rule" above.
2. **The narrow instance**: the bill-close write — named exactly, so the seat and
   stock-deduction writes are not re-implemented.
3. **The three properties** (caller-minted, stored-with-the-outcome,
   server-reconciles-back), each with the sentence it came from.
4. **The 409-on-key-reuse-with-a-different-body** case, which is the one that is
   easy to forget.
5. **The corpus pointers** so the implementer does not re-derive the vocabulary.

**The implementing feature should also** — and this is the part that makes the
reference worth filing — **assert the retry case in a test**: issue the same
bill-close request twice with the same key and assert that **two** `Bill` rows do
**not** exist, that exactly **one** `DerivedTip` row exists, and that exactly
**one** set of `StockEntry` rows exists. The corpus already contains this shape of
test for the seat write (feature 388's `observe_seat.py`).

## Telegram interaction if any

**None.** The bill-close write is an HTTP route. The cook bot does not close bills.

## Dependencies

- **Feature 388** — **upstream, and this feature does NOT re-implement it.** It
  establishes the *seat* write's idempotency rule and the pattern of proving a
  duplicate write by execution (`observe_seat.py`). This feature reuses the
  *pattern*, not the code.
- **Features 400 / 401** — upstream *vocabulary* for a client-UUID idempotent write
  (the stock-deduction instance, already owned).
- **Feature 415** — the feature that owns the bill-close **write** (per feature
  448's cross-reference). **This contract lands BEFORE or IN THE SAME PULL REQUEST
  as 415** — the ordering matters, because 415 implements the write and would
  otherwise implement it **without** the key.
- **Feature 448** — owns the human-facing bill number; the "server reconciles its
  own number back" property refers to that number, not to an auto-increment id.
- **Feature 457** — owns the `DerivedTip` constraint. A retried write must not
  produce a second free-standing tip number; this feature's test (one `DerivedTip`
  row) is the same concern seen from the retry side.

## Open questions

- **Should the key be mandatory or optional on the bill-close route?** Mandatory
  breaks any existing caller; optional means the safe behaviour is opt-in. This
  pass does **not** decide. The source's own clients always supply one.
- **Should the key be a header or a body field?** The corpus is split (features 400
  and 401 use a column on the row; features 259 and 412 use an inbox table). The
  implementing feature should pick one and state why.
- **What is the retention window for stored keys?** A key that expires and is then
  replayed would be re-executed. Open.
- **Does the same key mechanism need to cover the `DerivedTip` write separately?**
  It should not — the tip is written **inside** the bill-close transaction, so the
  bill-close key covers it. **Assert that in the test**, because a separate write
  path for the tip would break the single-write guarantee.
- **Is the retry the *only* concern?** The same absence of a key also means a
  **replay by an attacker** is indistinguishable from a legitimate retry. LE31 is a
  single-VPS, trusted-network system, so this is a hardening note rather than a
  threat model — but it is the reason the key is **bound to the request body**.

## Why this matters

**The interesting finding is the narrowness.** The corpus already knows about
idempotency — 23 contracts carry a request-level key, and features 400 and 401
apply it to the stock write, and feature 388 applies it to the seat write. A
concept sweep for "idempotency" would have returned 23 hits and this pass would
have filed nothing.

The uncovered instance is the write that **moves money**: the bill close creates
the `Bill`, writes the `DerivedTip` and deducts the stock. Its only protection
today is `Bill.visit_id`'s unique constraint, which prevents a *duplicate* bill and
provides **no** correct answer for a *retry*. And a retry after an ambiguous
timeout is not an exotic case — it is what a proxy, a mobile client on a flaky
network, or an impatient double-tap produces.

**The instrument matters.** This finding was produced by **executing** LE31's real
schema and reading the resulting index list, then grepping the corpus for the
*specific write* rather than for the *concept*. The same greedy concept sweep that
found 23 hits would have masked it.

**The source is a reference, not a template.** The repo is ★0, MIT, and entirely
off-stack (Python/Frappe-ERPNext against LE31's FastAPI/SQLModel), and it is an
offline-first system — a design LE31 explicitly does not have. What transfers is
the **rule** and the **three properties**, not the code. Its README's "100%
coverage" badge is **self-reported by the repository author and is NOT
independently verified**, and no test count from it is repeated as fact anywhere in
this contract.
