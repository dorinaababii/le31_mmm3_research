# Feature 494 — LE31 has no machine-readable write contract, so no client other than a browser can write anything

> **Pick C of Daily Brainstorm 2026-11-17 (106th daily-brainstorm pass).**
> Bucket: **v1 — Core MVP**. Verdict: **`build`** (a first-party gap, proved by
> execution; the code change is small and the contract is the deliverable).
> Evidence class: **OBSERVED** — LE31's own backend and shipped surface, read and
> executed on 2026-11-17. The third-party sources are the *instrument*; the subject
> is LE31's own code.
>
> **Source artifact (instrument, not subject):** `beingmushfiq/Baki-Bondhu` — MIT,
> ★0, created 2026-10-24, pushed 2026-11-16, **in-window by both fields**.
> URL: https://github.com/beingmushfiq/Baki-Bondhu
> Raw README: `/tmp/le31-brainstorm-2026-11-17/gh/beingmushfiq__Baki-Bondhu.README.md`
>
> **Corroborating source (also in-window):** `shyampandey1104/erpnext-pos-offline-pwa-hybrid-counter`
> — MIT, ★0, created 2026-10-19, pushed 2026-11-17. Its *"Batch Sync Engine"* posts
> a **structured batch** to `POST /api/method/pos_pwa.sync_batch` — i.e. a
> machine-readable write contract that a non-browser client can speak.

## Goal

Make one sentence true that LE31 cannot currently say:

> **Any client can write to LE31 — a kiosk, a scanner, a voice client, a test, a
> queue — by speaking one documented, machine-readable contract, and there is a
> check that proves the shipped surfaces still speak it.**

Today LE31's API has **no write contract at all** beyond a single route, and the
shipped waiter surface does not use the API. This feature names the missing
contract and the missing check.

## Scope

**In scope (v1):**

- **A documented machine-readable write contract** for LE31's state-changing
  operations: a JSON **request body** schema and a JSON **response** schema, per
  route, with the shapes named and the error statuses enumerated.
- **The three write operations** the contract must cover, taken from LE31's own
  charter rows and existing features — the **seat**, the **order line**, and the
  **bill close** — each expressed as a request/response pair.
- **A contract check** that the API's declared shapes and the shipped client's
  expectations cannot drift apart silently.

**Out of scope (v1):**

- **Changing the shipped `index.html` waiter surface.** That surface's drift from
  the API is owned by feature **467**; this feature does not modify it.
- **Fixing the money or the tax defects** in the shipped surface (features 465,
  481) or the seat-form guard (466) or the billed-table crash (484).
- **A new route's semantics.** This feature defines the *shape* of the contract for
  routes that already exist or are already owned by other features; it does not
  invent new business operations.
- **Any new table, column, or migration.**
- **A public API, an API key, a rate limiter, or multi-tenancy.** LE31 is a
  single-VPS, trusted-network system (charter §3.2).
- **Adopting any third-party codebase.** See "Reference discipline".

## Description

### What LE31's API actually is, today

From the parent's execution against LE31's real code
(`/opt/data/le31-brainstorm-2026-11-17-scripts/audit_lifecycle.py`):

```
--- PICK A: input paths (ANY non-form input surface?) ---
  BaseModel (JSON body schema) occurrences: 0
  routes:
      @app.on_event("startup")
      @app.get("/api/health")
      @app.get("/")
      @router.get("")
      @router.post("/{table_id}/seat")
  shipped index.html: <form>=0  fetch(= 0  <input>=4
  voice/audio tokens in index.html: NONE
```

And the proof that `index.html` is the **shipped** surface — not a mock-up — is one
line of LE31's own `backend/app/main.py`:

```python
_STATIC_DIR = _REPO_ROOT / "index.html"
if _STATIC_DIR.exists():
    app.mount("/", StaticFiles(directory=str(_STATIC_DIR.parent), html=True), name="ui")
```

Three facts, each load-bearing:

1. **`BaseModel` occurrences: 0.** FastAPI's request-body schema is a pydantic
   model. LE31 declares **none**. Every write route therefore takes its input from
   **path/query parameters** only.
2. **One non-GET route exists:** `POST /{table_id}/seat`. Its entire input is the
   **table id in the path**. There is no body to carry a party size, an item, or an
   amount.
3. **The shipped surface calls nothing:** `index.html` contains **0** `fetch(`
   calls, **0** `<form>` elements and **4** `<input>` elements. Every button
   mutates a local JavaScript `state` object; **not one of them reaches the API.**

**The consequence, stated plainly: LE31's API cannot accept a bill, and LE31's
waiter screen cannot send one.** The two halves exist and do not meet.

### Why this is a first-party finding and not a reference

Feature **467** already files *"the waiter surface and the API have drifted apart
and nothing can see it"*. **This is not a duplicate.** The two findings are
adjacent but distinct, and the distinction is the point:

| | feature 467 | **this feature** |
|---|---|---|
| the defect | the **client** does not call the API | the **server** has no write contract to call |
| the subject | `index.html`'s behaviour | the **API's shape** |
| the fix | make the client call the API | give the API a body the client can send |
| the risk of fixing only one | a client that calls an API with no body schema cannot send a bill | a correct client with no contract is still blocked |

**Fixing 467 without this feature produces a client that cannot express a bill.**
And fixing this feature without 467 leaves a contract nothing checks against.

The corpus sweep confirms the gap is not owned:

```
PICK 494 — machine-readable-write-api-for-non-form-clients
    a JSON write endpoint / request body schema in LE31 -> 2
       (feature 221 — a READ-ONLY reference: "one route that takes a datetime
        string and returns a list of open restaurants"; feature 221's own text
        says "No existing file changes today" and names no write route)
    a client other than the browser calling the API -> 6
       (features 123, 200, 228, 286 — all third-party references or goldens,
        none of them a LE31 write contract)
    the two surfaces are compared by a contract test -> 0 []
```

**Zero files own "a contract test that compares LE31's two surfaces".** Feature 467
owns the *drift*; it does not own a *check*. And the corpus has **23** contracts
mentioning an idempotency key and **33** mentioning an API — but not one of them
states the write contract LE31's own charter requires.

### What the contract must contain

For each of the three writes, a **request body** and a **response body**:

| write | request body (minimum) | response | current owner |
|---|---|---|---|
| **seat a party** | `party_size`, `adults`, `children` | `visit_id`, `table_id`, `status` | feature 388 owns the guard; feature 466 owns the `adults` min |
| **add an order line** | `menu_item_id`, `qty`, `course?`, `notes?` | `order_item_id`, `status`, `fired_at?` | feature 02 owns the write; feature 483 owns the course-fire filter |
| **close a bill** | `subtotal_items`, `subtotal_tax`, `total_due`, `total_paid`, `payment_method` | `bill_id`, `bill_number`, `derived_tip` | feature 415 owns the write; feature 448 owns the number; feature 493 owns the idempotency key |

**The three names in the middle column are the interesting part.** LE31's writes are
**already specified** — in six different feature contracts, by six different passes.
What has never existed is the single place where their **wire shapes** are stated
together, so a client (or a test) has one thing to read.

And the error statuses must be enumerated, because they are already implied by the
guards:

- **409** — the transition is refused (feature 388's seat conflict; feature 493's
  idempotency-key reuse with a different body);
- **400** — the request is invalid (feature 466's `adults < 1`; feature 484's
  absent amount);
- **422** — the body failed its schema (FastAPI's default; **never observed**
  today, because there is no body to fail).

### The check

**A contract test** that compares the API's declared shapes against the shipped
client's expectations — **zero files in the corpus own this** (the sweep above
returns 0). The shape of the check:

- For each write route, the test asserts the route's **declared request model**
  exists, and that its **field names and types** are the ones the contract
  documents.
- The test asserts the **response model** exists and carries the documented fields
  — including `bill_number` (feature 448) and `derived_tip` (feature 457).
- The test asserts the **error statuses** are reachable — i.e. that a request
  violating a documented guard produces the documented status, not a 500.

**The test must compare two artefacts, not one.** A test that only asserts the API's
own models would pass forever while the client drifts — which is precisely the
failure mode feature 467 documents. The test's other side is a **fixture of the
client's expectations**, and the fixture is what makes the check meaningful.

This is the fourth instrument — *read the SHIPPED surface against the SHIPPED API* —
and it is what this feature generalises: feature 467 applied it once (2026-11-16)
and found the drift. **This feature makes it a standing check.**

## Data model

**No schema change, no migration.** This feature produces:

1. **One module** — `backend/app/contracts.py` (or equivalent) — declaring the
   request and response models, imported by the routers that implement them.
   FastAPI's `response_model=` and the request-body annotation make the declaration
   **the** contract, so it cannot drift from the implementation by construction.
2. **One documented contract** — the three request/response pairs above, with the
   error statuses — living beside the models so that a client author reads one
   place.
3. **One contract test** comparing the API's declared models against a **client
   expectation fixture**.

**Why pydantic models and not a hand-written doc.** A hand-written document drifts
from the code on the first refactor and nobody notices — that is feature 467's
failure mode, one level up. A declared model that the route *uses* cannot drift
from the route's behaviour; it can only drift from the *client*, and the contract
test is what catches that half.

## Implementation steps

1. **Declare the three request models** as pydantic models in a new module, with
   the field names and types from the table above. Every field that an existing
   feature's guard inspects is **declared**, so the schema and the guard are read
   together.
2. **Attach them to the routes.** Each write route takes its body from the declared
   model. **The seat route keeps its 409 guard** (feature 388); the bill-close route
   gains the body feature 415 already needs.
3. **Declare the response models** — including `bill_number` (feature 448) and
   `derived_tip` (feature 457) — and set `response_model=` on the routes.
4. **Enumerate the error statuses** in the contract: 400, 409, 422. Assert in the
   test that each documented status is **reachable** and that a guard violation
   produces the documented one.
5. **Write the client expectation fixture** — a small, explicit record of what a
   client expects to send and to receive, per write.
6. **Write the contract test:** for each write route, compare the route's declared
   model (introspected **in-process** from the FastAPI app, not by grepping the
   source) against the fixture. **Both sides must be compared** — a test that only
   checks the API would be a vacuous pass.
7. **Make the check runnable in CI** — the repo's own charter §7 requires
   *"End-to-end before commit"*, and feature 467 records that **nothing in the
   repository can execute it today**. This test is one of the first things that can.

**A negative control is required.** The test's own assertion must be proven
load-bearing: mutate the API's declared model (change one field name), confirm the
test **fails**, restore, confirm it **passes** again, and assert no residue. A
contract test that cannot fail proves nothing — and a contract test that only
checks one side always passes.

## Telegram interaction if any

**None.** The contract covers HTTP routes. The cook bot's Telegram surface is not
an HTTP client of these routes and is out of scope.

## Dependencies

- **Feature 467** — the **sibling** finding, and the reason this feature's check
  exists. It owns the *client's* drift; this feature owns the *server's* contract
  and the standing check. **Neither may land without the other being considered** —
  467 without this feature has no contract to call; this feature without 467 has
  nothing to check against.
- **Feature 388** — the seat route's 409 guard; the contract must name that status.
- **Feature 415** — owns the bill-close **write**; the request/response shapes
  above are taken from its scope. **This contract lands BEFORE or IN THE SAME PULL
  REQUEST as 415**, for the same reason as feature 493's ordering rule.
- **Feature 448** — owns `bill_number`; the bill-close response model must carry
  it.
- **Feature 457** — owns the `DerivedTip` constraint; the bill-close response model
  must carry `derived_tip`.
- **Feature 493** — owns the idempotency key on the bill-close write; the contract
  must name the 409 that a key-reuse produces.
- **Feature 466** — owns the `adults >= 1` guard; the contract must name that 400.
- **Charter §7** — *"End-to-end before commit"*; the contract test is one of the
  first executable things in the repository that can satisfy it.

## Open questions

- **Does the contract live in code (pydantic models), in a document, or both?**
  This contract argues for code-first with a document generated from it. The
  implementing feature may prefer a hand-written document plus a test that checks
  the two agree — which is the same shape, one step looser. **Not decided here.**
- **Does the seat route keep its path parameter, or move the table id into the
  body?** Moving it would break the existing client. Keeping it means the contract
  is "path parameter + body", which is fine but must be stated per route. Open.
- **Is a `bill_number` on the bill-close response in scope, given feature 448 has
  not yet landed?** If 448 has not landed, the field is absent and the contract
  says so — the contract must track the **current** shape, not the intended one.
- **Should the contract cover reads too?** This feature covers writes. The reads
  (`GET /api/tables`) have their own shape and their own drift risk (feature 467
  notes the fixture ships three statuses the API cannot produce). Open.

## Why this matters

**The finding is not subtle, and that is the point.** LE31's backend has **zero**
request-body models and **one** non-GET route. LE31's shipped waiter screen has
**zero** API calls. Two halves, no meeting point. A reader who has only seen the
feature corpus would not guess this: 525 feature contracts and 487 HANDOFFs
describe the seat, the order line, the bill close, the tip, the bill number and the
tax rule — **six write operations' worth of business rules, and not one line of
wire format.**

**This is the seventh finding shape again — a covered concept, an uncovered
INSTANCE — applied to the wire.** The corpus covers "the API" (33 files), "the
surface" (feature 467), "the drift" (feature 467). What no file owns is **the
contract itself**, and the check that keeps it true.

**The three third-party sources were the instrument, not the subject.** The
offline-PWA counter's `sync_batch` endpoint is a machine-readable write contract
that a non-browser client speaks; the voice-ledger app's flows are all client→server
structured calls. Neither is a LE31 codebase (both are off-stack, ★0, and README-only
evidence, and their self-reported metrics are **not independently verified**). They
showed the *shape* a write contract has. **The defect is in LE31's own code, and
it was proved by reading and executing LE31's own backend and its own shipped
`index.html`.**

**And the payoff is bigger than the contract.** Feature 467 observed that LE31's
own charter §7 clause *"End-to-end before commit"* has **nothing in the repository
that could execute it**. A contract test that compares two artefacts is the
smallest thing that could. It is not the end-to-end test — but it is the first
artefact in the repository that would **notice** if the two sides stopped agreeing.

## Reference discipline

Both third-party artifacts are cited above as **instruments** and are subject to
the charter §3.2 rules:

- `beingmushfiq/Baki-Bondhu` — **MIT** (permissive), ★0, created 2026-10-24, pushed
  2026-11-16. Kotlin / Jetpack Compose / Room / Firebase — **off-stack**. The
  *vocabulary-shape* is adopted; the **code-shape is NOT adopted**, and no line of
  it is copied.
- `shyampandey1104/erpnext-pos-offline-pwa-hybrid-counter` — **MIT** (permissive),
  ★0, created 2026-10-19, pushed 2026-11-17. Python / Frappe-ERPNext — **off-stack**
  (LE31 is FastAPI + SQLModel + Postgres). The *vocabulary-shape* is adopted; the
  **code-shape is NOT adopted**.
