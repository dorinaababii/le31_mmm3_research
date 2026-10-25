# Feature 378 — Operator-request-queue vocabulary: `Leonardo-Dalan/material-request-system` (defer)

> **NEW observation (2026-10-25).** An **operator-request → logistics-queue → stock-tracking** flow, built as **vanilla JS + Firebase, offline-first**. GitHub repo `Leonardo-Dalan/material-request-system` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★0/⑂0**, 416 KB, **JavaScript ✗ OFF-STACK**, created **2026-10-20T16:21:57Z AND pushed 2026-10-20T16:39:08Z = IN-WINDOW BY BOTH FIELDS** (window 2026-10-18..2026-10-24), 4 topics `['firebase','inventory-management','manufacturing','vanilla-js']`, `default_branch=main`, `archived=false`, `fork=false`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-25 (`/tmp/le31-daily-2026-10-25/pv/Leonardo-Dalan__material-request-system.json`), not from search-result numbers. Description (verbatim from GitHub API): *"Factory material request system: operator requests, logistics queue, stock tracking and reports. Offline-first web app (vanilla JS + Firebase)"*.
>
> Bucket: **v1 (request-queue vocabulary)** — Pick C of Daily Research 2026-10-25. Build verdict: `defer` (parking-lot; **vocabulary reference only** — no code changes, no schema change).

## Goal

Record the **operator → queue → stock** triad as vocabulary that maps onto LE31's own **waiter → order → StockEntry** triad, using an in-window artifact that states the three steps explicitly — and record the one place where the mapping **does not** hold.

**The deliverable is a named vocabulary plus one explicit non-equivalence.** Not a feature. Not a build.

## Scope

**In scope (defer artifact):**

- A written record of `material-request-system`'s three-step flow, stated in its own terms: **an operator requests** → **a logistics queue carries it** → **stock tracking reports it**.
- A written mapping onto LE31's existing triad: **waiter creates an order** → **the order queue carries it to the cook** → **`StockEntry` records the resulting stock movement**.
- **One explicit non-equivalence**, stated so a future contributor does not over-read the mapping: **the request in this reference is a request for material (a thing the operator needs), while LE31's order is a record of something that happened.** LE31's order is *not* a request for goods; the `StockEntry` ledger records consumption and prep, and §3.3 forbids valuing it. **The vocabulary overlap is in the queue mechanics, not in the semantics of the payload.**
- **One proposed documentation question** for LE31's own design docs, stated as a question and not an answer:
  > *Does LE31 have an explicit notion of an order's queue state (received → acknowledged → prepared → served), separate from the order's own status? If not, is that a gap or a deliberate simplification?*

**Out of scope (defer artifact):**

- **Any new model, column, enum, or endpoint.** No `OrderState` enum, no queue table, no `Request` table, no migration.
- **Any Firebase dependency, any client-side framework, any offline-sync machinery.** LE31 is server-authoritative (§3.2); the reference's offline-first posture is explicitly *not* being proposed.
- **Any "material request" feature.** The domain (factory materials) is a hard mismatch for a restaurant. The *flow shape* is what transfers.
- **Any change to how orders or stock work today.** LE31's §3.1/§3.3/§3.4 behaviour is untouched by this pick.

## Description

`material-request-system`'s description is a **complete three-step flow in one sentence**: *"Factory material request system: operator requests, logistics queue, stock tracking and reports."*

Read as a process, that is: **someone who needs a thing asks; something carries the ask; something records the effect on stock.** It is the shape of a great many internal systems, and it happens to be the shape of LE31's core loop described in different nouns:

| Reference (`material-request-system`) | LE31 equivalent | Notes |
|---|---|---|
| operator **requests** | waiter **creates an order** | Different payload semantics — see the non-equivalence below |
| **logistics queue** carries it | the **order queue** carries it to the cook | LE31's carrier is the Telegram bot (§3.1 cook surface), not a logistics queue |
| **stock tracking** reports it | **`StockEntry`** records the resulting movement | LE31's ledger is append-only and **never valued** (§3.3) |
| *(no equivalent)* | **the owner is never a requester** | LE31's requester is the waiter; the owner observes |

**The mapping is real and it is worth naming** because it is exactly the kind of structural parallel that a future contributor can re-derive in ten minutes — but that re-derivation is ten minutes per contributor, per session, and the risk is not wasted time. **The risk is that someone re-derives it and concludes the domains are equivalent**, and then starts building request-cancellation, request-approval, or a "pending requests" panel that LE31's invariants do not support.

**Which is why the non-equivalence is the most important line in this contract.**

In the reference, **the request is for a thing that does not yet exist in stock** — the operator wants material, and the request creates an obligation. In LE31, **the order is a record of something that already happened** — the waiter is recording what a table asked for, and the `StockEntry` records what was consumed or prepared. LE31 has no concept of an outstanding request for goods, and **§3.3 does not want one**: LE31's stock is derived from entries, and a pending request that never becomes an entry is not a stock fact. Introducing one would either (a) create a second representation of stock, which is the defect filed as feature 374, or (b) create a request pipeline whose relationship to the ledger is undefined.

**That is the pick's actual contribution: a worked example of a structural parallel that looks transferable and is not, with the reason spelled out.** The parallel is in the queue mechanics; the divergence is in the payload semantics and in what the ledger is allowed to know. **A vocabulary reference that names where a mapping breaks is more useful than one that only names where it works**, because the failure mode this pass found — a contributor importing "operator requests" into a system that records facts — is precisely the one a mapping document is supposed to prevent.

**The documented flow also has a §3.3 analogue worth recording separately:** *"stock tracking and reports."* The reference tracks stock **and reports on it**. LE31 **derives** stock from entries and **never values it** — the 2026-10-24 pass already found `kinv`'s matching refusal (*"without stock-valuation busywork"*), and the same window's `LEO17061996/fnb-erp-django` is the counter-example (*"giá vốn bình quân"* — average cost of goods — plus a *"dashboard food cost"*). **That triangulation is filed in the 2026-10-25 report's Adjacent evidence, not here; this pick owns only the request-queue vocabulary.**

## Data model

None. No table, no column, no enum, no endpoint, no migration.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (any one):**

1. **Any PR adds an order-state or order-queue concept** — e.g. an `OrderStatus` enum with `pending`/`acknowledged`/`prepared`/`served`, or a queue table. The PR must state explicitly whether it introduces an *outstanding request for goods* (which this pick shows is a §3.3 problem) or merely an *order state* (which is a §3.4 transition and is fine).
2. **Any proposal introduces a "pending requests" or "requested items" panel** — this pick is the pre-written answer: the request-vs-fact distinction must be stated before the panel is designed.
3. **Any proposal introduces a stock valuation, cost, or margin report** — §3.3 forbids it; the 2026-10-25 report's Adjacent evidence now carries two independent counter-examples, and the 2026-10-24 report carries the matching refusal.

## Telegram interaction if any

None today, and the reason is **structural rather than accidental**. The reference's "logistics queue" carries a request to whoever fulfils it; in LE31, that carrier **is** the Telegram bot (§3.1's cook surface), and the bot's delivery model is one-shot and unambiguous — a message arrives or it does not. LE31's §4.3 already requires a one-shot alert for stock events.

**The vocabulary question this pick raises has a Telegram-shaped answer, and it is recorded here rather than deferred:** if LE31 ever wanted an explicit order-queue state, the natural place to *express* it would be the waiter web UI (which polls, per §3.2) and the natural place to *act* on it would be the cook bot — **but the bot is not a queue-monitoring surface and should not become one.** The queued-request vocabulary therefore has **no Telegram component**, and adding one would be a §3.1 surface expansion.

## Dependencies

None. No new packages, no schema change, no infrastructure.

## Open questions

1. **Does LE31's order model need an explicit queue state at all?** The proposed documentation question in *Scope* is **unanswered** and is the point of the pick: today, LE31's order state is implied by the existing §3.4 transitions, and the question of whether that should become explicit is **an owner decision**. If the answer is "no, the current model is deliberately simple", then this pick's value is the *warning* about what an import of request-cancellation semantics would break.
2. **Is "request" a term LE31 should avoid entirely?** §3.3's ledger records facts. If "request" is used anywhere in LE31's vocabulary it may imply an outstanding obligation the system does not track. **Wording decision, owner call.**
3. **Should the queue-state question be answered in the charter or left implicit?** Leaving it implicit preserves the current simplicity; answering it in writing costs a paragraph and prevents the import. **Unmade.**
4. **Was the reference's actual implementation read?** No — only the GitHub API metadata and the one-line description were read. **The claim that it "tracks stock and reports on it" rests on the description, not on code.** If the owner ever wants this vocabulary acted on, the repo (MIT, 416 KB) should be read properly first.

## Why this matters

**Because a structural parallel that looks transferable and is not is the most dangerous kind of external reference — and LE31 now has a worked example of one, with the reason written down.**

The request-queue pattern is extremely common in operational software, and it is superficially identical to LE31's order flow: *someone asks, something carries it, stock is affected.* An implementer who saw only the parallel would very reasonably build request-approval, request-cancellation, or a pending-requests view — and each of those would push LE31 toward **a second representation of stock** (the exact defect filed as feature 374 on 2026-10-24) or toward a request pipeline whose relationship to the append-only ledger is undefined.

**LE31's §3.3 ledger is a record of what happened. A request is a statement of what someone wants.** Mixing the two is not a small modelling error — it is the difference between a ledger and a work queue, and LE31's product value is *a truthful stock number*, which is a ledger property and not a queue property.

So the pick's value is the **mapping plus its explicit limit**, dated and cited, in a form a future contributor can read before they start designing. That is a small artifact with a real failure mode behind it.

**Fully reversible (vocabulary-only artifact).** Trigger condition: any PR adding an order-state or order-queue concept, any proposal for a pending-requests panel, or any proposal for a stock valuation report.
