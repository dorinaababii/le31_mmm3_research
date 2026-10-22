# Feature 356 — `hrekokovgmmek-lab-research-ledger-append-only-preregistration-vocabulary` (defer)

> **NEW observation (2026-10-22).** Documents in-window GitHub repo `hrekokovgmmek-lab/research-ledger` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**), **★1/⑂0**, **15 KB (smallest non-trivial pick of the 84-pass series)**, **Python ✓ ON-STACK**, created **2026-10-21T16:22:43Z** and pushed **2026-10-21T16:23:03Z** — a ~1-minute initial push, i.e. the repo was created and seeded in one sitting, `archived=false`, `fork=false`, 0 open issues, default_branch=`main`). Description (verbatim from GitHub API direct-GET, **parent-verified 2026-10-22**): *"An append-only log of results and decisions, and preregistrations that freeze code and data and let the outcome be read once."* Topics (verbatim, parent-verified, **6 topics**): `backtesting, preregistration, python, quant, reproducibility, research-tools`. Bucket: **v2 (vocabulary only)** — Pick A of Daily Research 2026-10-22. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Record the **append-only log of decisions + preregistration-that-freezes-values** vocabulary as a durable cross-section reference, and document the one primitive that is genuinely *stronger* than LE31's current §3.3 invariant — **immutability by pre-commitment**, i.e. a value that is fixed *before* the outcome is known cannot be edited afterwards even by an operator with database access. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **append-only decision log** primitive: decisions are entries, not mutable rows.
- A written record of the **preregistration / freeze** primitive, which is the actual novel element: *"preregistrations that freeze code and data and let the outcome be read once."* This is **stronger than append-only**. Append-only says *never update or delete*; preregistration says *this value was committed before the outcome existed, and the commitment is checkable*.
- A written record of the **read-once outcome** primitive: the result is written once and thereafter only read.
- A decision record: verdict is `defer` because the job-to-be-done is **scientific preregistration**, which has no restaurant analogue, and because LE31's §3.3 already encodes the weaker principle.

**Out of scope (defer artifact):**

- Any change to LE31 v1's `StockEntry` ledger or its derivation of current stock.
- Any preregistration mechanism on menu prices or stock counts.
- Adoption of the codebase, despite MIT and despite it being Python and only 15 KB.
- Any claim that LE31 needs this. It does not today.

## Out of scope

- See "Scope" above. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

**Gate check 1 (JTBD) fails as written.** The repo's job is: *when a researcher is about to run an experiment, they want to commit to a method in advance, but struggle because hindsight bias makes results unfalsifiable, so that the outcome can be read once and believed.* **That is not an LE31 job.** LE31's owner reads prep counts and stock levels; there is no outcome to protect from hindsight.

- **Evidence class**: **observed** (repo exists; every field above read from `GET /repos/hrekokovgmmek-lab/research-ledger`, not from a search index).
- **Confidence**: **high** that the description means what it says (it is unusually explicit); **low** for any LE31 relevance.
- **Traction caveat, recorded plainly**: ★1/⑂0 is **no traction evidence in either direction** — not adoption, not failure. This is a 15 KB repo created and pushed within one minute on 2026-10-21. The pick is about the *shape*, not the project.
- **Real observed LE31 JTBD**: **zero**. Filed as a citation for a future §3.3 strengthening conversation, not as a capability gap.

## Description

GitHub `hrekokovgmmek-lab/research-ledger` (MIT ✓, ★1/⑂0, 15 KB, Python ✓ ON-STACK, created and pushed 2026-10-21, archived=false).

Three primitives, in increasing order of relevance to LE31:

1. **Append-only log of results and decisions** — *already an LE31 invariant.* §3.3 states every prepared-item quantity change is a new `StockEntry`, never an update or a delete, and current stock is derived. This primitive adds nothing.
2. **Preregistration that freezes code and data** — **the novel one.** The value is fixed and committed *before* the outcome is known. In LE31 terms this would be a charter-level claim, not an implementation detail: it means a `MenuItem.price_eur` could be pinned at a service time and the pin could be proven to predate the sale. LE31 makes no such guarantee today.
3. **Read-once outcome** — the result is written once and thereafter only read. This is close to, but not the same as, LE31's *explicit state transition* invariant (§3.4): read-once is about a **record**, explicit-transition is about a **workflow**.

The distinction matters: LE31's ledger is append-only by *convention and code discipline*; `research-ledger`'s is append-only by *pre-commitment that is externally checkable*. The second is a stronger claim, and adopting it would be a **strengthening** of §3.3 rather than a violation of it.

## Data model

None shipped.

For reference, the implied shape is a two-table split: an **append-only entry log** (decision or result, timestamped, immutable) and a **freeze record** (the preregistered value plus the commit point that makes it checkable). The interesting property is that the freeze record must be verifiable *without* trusting the log that follows it — otherwise "frozen before the outcome" is an assertion rather than a fact.

No LE31 entity changes. **Explicitly: `StockEntry` is untouched.**

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) LE31 needs a value that must provably predate an event — realistic candidates are a price locked at order-open time, or a stock count frozen at service start; (2) the owner has decided such a guarantee is worth the storage and the audit surface; (3) §3.3 is amended to state *why* pre-commitment, not merely append-only, is the invariant.

## Telegram interaction

None. No user-facing surface.

## Dependencies

None. No new runtime dependency. No migration. No AI capability required.

## Open questions

1. **Is pre-commitment ever actually needed?** LE31 v1 has no falsifiability problem. This is the entire reason for `defer`.
2. **If it were needed, what verifies the freeze?** A pre-commitment claim that cannot be independently checked is worse than no claim, because it invites reliance on an unbacked guarantee.
3. **Would this touch §3.7?** A freeze record could capture a price and a timestamp. Both are operational data, not guest data, so probably not — but this has not been reviewed.

## Why this matters

Small, honest value. LE31's §3.3 append-only invariant is one of the few places where the charter is *already* stricter than most restaurant software, and `research-ledger` names the one step beyond it. Recording it costs 15 KB of disk and prevents a future pass from rediscovering the idea. **It does not justify any build time today, and this contract does not claim otherwise.**

---

**Gate verdict: `defer`.** Fails check 1 (JTBD). No hard conflict — if anything it strengthens §3.3. Fully reversible (vocabulary-only artifact; deletion costs nothing). 3/3 checks answered, decision recorded.