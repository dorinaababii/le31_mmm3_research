# HANDOFF — Feature 494: LE31 has no machine-readable write contract, so no client other than a browser can write anything

## Active feature path

`features/494-machine-readable-write-api-for-non-form-clients.md`

**Disposition:** `build` — **a first-party gap, proved by execution, with a small and
well-specified fix** (declare request/response models; attach them to the routes;
write one contract test).

**What this slice delivers:** a new `backend/app/contracts.py` declaring the request
and response models for LE31's three state-changing writes, those models attached to
the routes that implement them, and **one contract test** that compares the API's
declared shapes against a client expectation fixture.

**What this slice explicitly does NOT deliver:** any change to the shipped
`index.html`, any change to the business semantics of a write, any new business
operation, any table or column, and any fix to the money/tax/seat-form defects that
features 465 / 466 / 481 / 484 own.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | **PASS.** Proved by execution: the backend declares **0** pydantic request-body models and exposes exactly **one** non-GET route; the shipped waiter surface contains **0** `fetch(` calls and **0** `<form>` elements. No non-browser client can write anything to LE31, because there is no body to write. |
| 2. Viability | **PASS in principle.** FastAPI request/response models are the framework's own mechanism; `response_model=` plus a body annotation makes the declaration the contract. |
| 3. Practicability / confidence | **HIGH.** The change is small, entirely within LE31's stack (FastAPI + pydantic), and the gap is verified by reading LE31's own source. |
| 4. Conflict | **No hard conflict** — but **feature 467 is the sibling finding** and must be read first. 467 owns the client's drift; this feature owns the server's contract and the standing check. Fixing one without the other leaves the problem half-solved. |
| 5. Outcome, appetite, scope | **BUILD.** The contract plus the check is the deliverable; the client's adoption is feature 467's and a later feature's job. |
| 6. Cost to operational value | **LOW** (one module, three route annotations, one test); **HIGH** — this is the first artefact in the repo that can satisfy charter §7's *"End-to-end before commit"* clause, even partially. |
| 7. Circuit breaker / reversibility | **PASS.** Additive module plus route annotations; reverting the annotations restores the previous behaviour exactly. |

## Files to touch

**Authorized in this disposition:**

- `backend/app/contracts.py` — **NEW**. The pydantic request and response models for
  the three writes, plus the documented error-status enumeration.
- `backend/app/routers/tables.py` — **the seat route's body annotation only.** Add the
  seat request model; **keep the existing 409 guard** (feature 388) and the existing
  `adults` validation (feature 466) — do not change their behaviour.
- `backend/app/routers/orders.py` / `backend/app/routers/bills.py` — **if and only if
  those files exist.** LE31's backend currently has `backend/app/routers/tables.py`
  and `backend/app/bot/cook_bot.py`; the order and bill routes may not exist yet. The
  parent verified the route list on 2026-11-17:

  ```
  @app.on_event("startup")
  @app.get("/api/health")
  @app.get("/")
  @router.get("")
  @router.post("/{table_id}/seat")
  ```

  **If the order or bill route does not exist, this feature declares the models and
  the documented contract for them, and does NOT create the routes** — creating them
  would duplicate feature 02 and feature 415's ownership.
- `backend/tests/test_contracts.py` — **NEW** (or the repo's existing test location —
  check `backend/tests/` first).

**Explicitly NOT to be touched:**

- `index.html` — **the shipped waiter surface is feature 467's.** This feature must
  not modify it. (Feature 467's own finding is that it calls no API at all; fixing
  that is *not* this slice.)
- `features/465-*.md`, `features/466-*.md`, `features/467-*.md`,
  `features/481-*.md`, `features/484-*.md` — other features' contracts.
- `backend/app/models.py` — **no schema change.**
- `backend/app/bot/cook_bot.py` — **no Telegram handler change.**

## Verification protocol reference

**Documentary verification (required):**

1. Read `features/494-machine-readable-write-api-for-non-form-clients.md` in full.
2. Read feature **467** in full before coding:
   `features/467-le31-the-waiter-surface-and-the-api-have-drifted-apart-and-nothing-can-see-it-the-mock-up-calls-no-api-and-no-test-compares-the-two.md`.
   The two features are siblings; this one must not duplicate it.
3. Read the instrument sources at
   `/tmp/le31-brainstorm-2026-11-17/gh/beingmushfiq__Baki-Bondhu.README.md` and
   `/tmp/le31-brainstorm-2026-11-17/gh/shyampandey1104__erpnext-pos-offline-pwa-hybrid-counter.README.md`
   (both MIT, both ★0, both off-stack).

**Executed verification (required):**

4. **The gap must still hold before coding.** Re-run
   `/opt/data/le31-verify-2026-10-27/.venv/bin/python /opt/data/le31-brainstorm-2026-11-17-scripts/audit_lifecycle.py`
   and confirm it still prints `BaseModel (JSON body schema) occurrences: 0` and
   `shipped index.html: <form>=0  fetch(= 0`. If either has changed, **another
   feature has landed** — re-derive before implementing.
5. **After coding**, the declared models must be discoverable **in-process** from the
   FastAPI app — not by grepping the source. Introspect the app's routes and assert
   that each write route now has a request-body model and a declared response model.
   **Grepping the source is the self-contamination bug** (the checker matches
   itself); parse the app.
6. **The contract test compares TWO artefacts.** The test must assert the API's
   declared model against a **client expectation fixture**. A test that checks only
   the API **always passes** and is a **vacuous pass** — it must be rejected.
7. **The error statuses are reachable.** Assert that a request violating a
   documented guard produces the **documented** status (409 for the seat conflict,
   400 for the `adults` validation, 422 for a body that fails its schema) and not a
   500.
8. **Negative control — mandatory.** Mutate one declared field name in
   `backend/app/contracts.py`, confirm the contract test **fails**, restore, confirm
   it **passes**, and assert no residue (no `.bak`, no stray file). A contract test
   that cannot fail proves nothing.
9. **The test must fail if the client drifts.** Change one field name **in the
   fixture only** and confirm the test **fails**. This is the direction that feature
   467 says nothing currently checks.
10. **Charter §7** — the contract test is the first executable check in the repo that
    compares two of LE31's own surfaces. It does **not** replace an end-to-end test;
    it is a first step, and the report must not claim otherwise.

## Rollback path

- Delete `backend/app/contracts.py`.
- Delete the contract test file.
- Revert the request-body annotation on the seat route (and the `response_model=`
  arguments, if any were added). Reverting the annotations restores the previous
  behaviour exactly — the route's guard and validation are untouched.
- Delete `features/494-machine-readable-write-api-for-non-form-clients.md`.
- Delete `specs/494-machine-readable-write-api-for-non-form-clients-HANDOFF.md`.
- Remove the feature-494 row from `/opt/data/INDEX.md` and from the in-repo
  `INDEX.md`.
- **No data rollback:** no table, no column, no migration.

## Mandatory LE31 skill list

Before any implementation, load and follow:

- `le31-conventions` — money invariants and charter boundaries (§3.2, §7);
- `le31-research-workflow` — source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

This feature is already `build`; it needs **no** promotion trigger. It needs an
**implementation owner**.

**The ordering constraint:** the contract must land **before or in the same pull
request as feature 415**, because 415 implements the bill-close write and its
request/response shapes are declared here. Feature 415's own text must be read
before the shapes are finalised.

**What must NOT be promoted under this feature:** a change to the shipped
`index.html`. That surface is owned by features **465** (float money), **466** (the
`adults` min), **467** (the drift) and **484** (the billed-table crash). This
feature's check will *observe* the drift; it must not *fix* it, and fixing it here
would duplicate four filed features.

**What may be promoted later, as a separate feature:** making the shipped client
actually call the contract (feature 467's job), and covering the **read** routes in
the same contract (explicitly out of scope here).
