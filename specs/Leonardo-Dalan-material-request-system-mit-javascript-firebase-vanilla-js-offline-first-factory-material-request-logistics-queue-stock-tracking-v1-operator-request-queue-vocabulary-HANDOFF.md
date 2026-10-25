# Leonardo-Dalan-material-request-system-mit-javascript-firebase-vanilla-js-offline-first-factory-material-request-logistics-queue-stock-tracking-v1-operator-request-queue-vocabulary — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/378-Leonardo-Dalan-material-request-system-mit-javascript-firebase-vanilla-js-offline-first-factory-material-request-logistics-queue-stock-tracking-v1-operator-request-queue-vocabulary.md`
> before touching anything. **This is a WATCH-LIST / VOCABULARY slice,
> NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise a request table, an order-queue
> state, a request-approval or cancellation flow, a pending-requests
> panel, a Firebase dependency, or offline sync.** It records **one
> structural parallel and the exact point at which the parallel
> breaks**.

## Frozen identifiers (do not rename)

- Feature ID: `378`
- Slug: `Leonardo-Dalan-material-request-system-mit-javascript-firebase-vanilla-js-offline-first-factory-material-request-logistics-queue-stock-tracking-v1-operator-request-queue-vocabulary`
- Contract file: `features/378-Leonardo-Dalan-material-request-system-mit-javascript-firebase-vanilla-js-offline-first-factory-material-request-logistics-queue-stock-tracking-v1-operator-request-queue-vocabulary.md`
- Bucket: **v1 (request-queue vocabulary)** — defer
- Linear parent: **not created — Linear MCP write endpoint blocked (38th consecutive day), requestId `a4ff44223faad34e`**
- Linear sub-issue: **not created — same blocker**. Intended payload at `/opt/data/le31-daily-research-2026-10-25.linear-fallback.json`
- Source repo: GitHub `Leonardo-Dalan/material-request-system` (MIT), ★0/⑂0, 416 KB, JavaScript, created 2026-10-20T16:21:57Z, pushed 2026-10-20T16:39:08Z
- Raw fetch: `/tmp/le31-daily-2026-10-25/pv/Leonardo-Dalan__material-request-system.json`
- Report: `/opt/data/le31-daily-research-2026-10-25.md`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: assumed — the weakest class on the scale.**
The artifact is real (direct `/repos/` GET, HTTP 200, in-window by
both `created_at` and `pushed_at`, MIT licence verified, 4 topics).
**But there is no reported pain at all** — no LE31 owner, waiter, or
cook has reported anything about requests, queues, or order states.
This is the weakest evidence class, and it is the reason this pick
carries the heaviest warning in the contract.

**Confidence: medium** for the artifact's existence and shape. **Low**
for the transferability of the flow, and the contract states the
reason: the **domain is a hard mismatch** (factory materials, not a
restaurant) and the **payload semantics diverge** (a request for a
thing vs a record of something that happened).

**Decision: defer (vocabulary reference).** Check 1 (JTBD) **fails**
on `assumed` evidence. Check **2** **fails** (factory domain, not
restaurant) and check **4** **fails** (Firebase + offline-first
conflicts with §3.2's server-authoritative posture).

**Known rabbit hole: the mapping itself.** The reference's flow
(*operator requests → logistics queue → stock tracking*) is
**superficially identical** to LE31's (*waiter creates an order →
the order queue carries it to the cook → `StockEntry` records the
movement*), and that superficial identity is the trap. **The two are
not equivalent**, and the divergence is exactly what this slice
exists to prevent someone from missing.

**The divergence, stated precisely:**

- In the reference, **the request is for a thing that does not yet
  exist in stock** — it creates an *obligation*.
- In LE31, **the order is a record of something that already
  happened** — it creates no obligation, and the `StockEntry` ledger
  records consumption and prep.

**Why the divergence bites.** An outstanding request that never
becomes an entry **is not a stock fact**. Introducing one either
(a) creates a **second representation of stock** — the exact defect
filed as **feature 374** on 2026-10-24 — or (b) creates a request
pipeline whose relationship to the append-only ledger is undefined.
Both are forbidden by §3.3.

**Circuit breaker:** if no order-state concept is ever proposed, this
remains an unused reference. **Acceptable outcome.**

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-10-25 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.
5. `le31-handoff-spec` — the frozen-contract discipline this slice follows.

If the destination repo does not ship these skills, request them
from the project owner before starting. **Do not invent LE31
conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/378-…-v1-operator-request-queue-vocabulary.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No model, enum, endpoint, or test is
added. No schema is migrated.**

## What the coding agent must NOT do

- **Do not add a `Request` model, a request table, a request enum, or a
  request endpoint.** LE31 records facts; it does not track outstanding
  obligations.
- **Do not add request-approval, request-cancellation, or a
  pending-requests panel.** The contract is the pre-written answer on
  why these are not free.
- **Do not add an `OrderStatus`/`OrderState` enum with
  `pending`/`acknowledged`/`prepared`/`served` on the strength of this
  slice.** An *order state* is a §3.4 explicit transition and is a
  legitimate future proposal — but it must be **proposed and gated on
  its own merits**, not imported from this artifact. If a PR does add
  one, it must state explicitly whether it introduces an outstanding
  request for goods (forbidden, per §3.3) or merely an order state
  (allowed, subject to §3.4).
- **Do not add Firebase, a client-side framework, or offline-sync
  machinery.** LE31 is server-authoritative (§3.2).
- **Do not add a stock valuation, cost, or margin report.** §3.3
  forbids it. The 2026-10-25 report's *Adjacent evidence* now carries
  **two independent counter-examples** (`LEO17061996/fnb-erp-django`
  computes *"giá vốn bình quân"* and a *"dashboard food cost"*;
  feature 372's `kinv` refuses with *"without stock-valuation
  busywork"*), and the 2026-10-24 report carries the matching refusal.
- **Do not edit the charter or `le31-conventions`.** The proposed
  documentation question is a **question**, not an answer.

## The mapping and its limit (the actual deliverable content)

| Reference (`material-request-system`) | LE31 equivalent | Divergence |
|---|---|---|
| operator **requests** | waiter **creates an order** | a *request for a thing* vs a *record of something that happened* |
| **logistics queue** carries it | the **order queue** carries it to the cook | LE31's carrier is the **Telegram bot** (§3.1), not a logistics queue |
| **stock tracking** reports it | **`StockEntry`** records the movement | LE31's ledger is append-only and **never valued** (§3.3) |
| *(no equivalent)* | the **owner is never a requester** | LE31's requester is the waiter; the owner observes |

**The proposed documentation question** — stated as a question, and
**unanswered**, because answering it is an owner decision:

> *Does LE31 have an explicit notion of an order's queue state
> (received → acknowledged → prepared → served), separate from the
> order's own status? If not, is that a gap or a deliberate
> simplification?*

**And the proposed vocabulary question:**

> *Is "request" a term LE31 should avoid entirely?* §3.3's ledger
> records facts; if "request" appears anywhere in LE31's vocabulary it
> may imply an outstanding obligation the system does not track.

**The Telegram asymmetry, recorded rather than left implicit.** If
LE31 ever wanted an explicit order-queue state, the natural place to
*express* it would be the waiter web UI (which polls, per §3.2), and
the natural place to *act* on it would be the cook bot — **but the bot
is not a queue-monitoring surface and must not become one.** The
queued-request vocabulary therefore has **no Telegram component**, and
adding one would be a §3.1 surface expansion.

## Trigger for the next step

The next time **any one** of these is true:

1. A PR adds an order-state or order-queue concept.
2. A proposal for a "pending requests" or "requested items" panel
   appears.
3. A proposal for a stock valuation, cost, or margin report appears.

When triggered:

1. Read the contract in full, **and feature 374** (`le31-qty-remaining-derived-not-stored`)
   — the second-representation-of-stock defect is the specific failure
   this slice's warning points at.
2. Confirm the request-vs-fact distinction is stated in the PR
   description **before** the design is discussed.
3. If trigger 3 fires, the §3.3 no-valuation rule applies unchanged and
   the two counter-examples in the 2026-10-25 report are the citation.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/378-…-v1-operator-request-queue-vocabulary.md`
      exists and was read back.
- [ ] The repo's licence, star/fork counts, size, language, topics,
      `created_at`, `pushed_at`, `archived`, `fork` and `default_branch`
      match the raw JSON at
      `/tmp/le31-daily-2026-10-25/pv/Leonardo-Dalan__material-request-system.json`.
- [ ] The description quoted in the contract
      (*"Factory material request system: operator requests, logistics queue, stock tracking and reports. Offline-first web app (vanilla JS + Firebase)"*)
      is **verbatim** from the raw file.
- [ ] The topic list `['firebase','inventory-management','manufacturing','vanilla-js']`
      matches the raw file exactly (4 topics).
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] **No source file, model, enum, endpoint, schema, dependency, or
      test was modified.** No request flow, no order-state enum, no
      pending-requests panel, no valuation report. No charter edit was
      made.

## Rollback path

Delete
`features/378-Leonardo-Dalan-material-request-system-mit-javascript-firebase-vanilla-js-offline-first-factory-material-request-logistics-queue-stock-tracking-v1-operator-request-queue-vocabulary.md`,
delete
`specs/Leonardo-Dalan-material-request-system-mit-javascript-firebase-vanilla-js-offline-first-factory-material-request-logistics-queue-stock-tracking-v1-operator-request-queue-vocabulary-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and delete the (uncreated) Linear
sub-issue if it ever exists.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- **Does LE31's order model need an explicit queue state at all?** The
  documentation question above is **unanswered**, and that is the
  point of the pick: today, LE31's order state is implied by the
  existing §3.4 transitions. If the answer is "no, the current model is
  deliberately simple", this pick's value is the **warning** about
  what an import of request-cancellation semantics would break.
- **Is "request" a term LE31 should avoid entirely?** **Wording
  decision, owner call.**
- **Should the queue-state question be answered in the charter or left
  implicit?** Leaving it implicit preserves the current simplicity;
  answering it in writing costs a paragraph and prevents the import.
  **Unmade.**
- **Was the reference's actual implementation read?** **No** — only the
  GitHub API metadata and the one-line description. **The claim that it
  "tracks stock and reports on it" rests on the description, not on
  code.** If the owner ever wants this vocabulary acted on, the repo
  (MIT, 416 KB) must be read properly first.
