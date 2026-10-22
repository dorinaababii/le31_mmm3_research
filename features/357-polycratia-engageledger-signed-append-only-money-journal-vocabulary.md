# Feature 357 — `polycratia-engageledger-signed-append-only-money-journal-vocabulary` (defer)

> **NEW observation (2026-10-22).** Documents in-window GitHub repo `polycratia/engageledger` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**), **★1/⑂0**, **9 KB (smallest pick of the 84-pass series)**, **Go OFF-STACK for LE31's Python 3.13 charter**, created **2026-10-19T13:37:48Z**, pushed **2026-10-21T15:17:07Z** (in-window by push), `archived=false`, `fork=false`, 0 open issues, default_branch=`main`). Description (verbatim from GitHub API direct-GET, **parent-verified 2026-10-22**): *"Keep the money terms of a contracting engagement as a signed append-only journal: price moves only by change orders signed by both parties, acceptance is a business-day clock stopped only by a rejection that names a criterion, and invoices are computed from the journal."* Topics: **none** (`[]`). Bucket: **v2 (vocabulary only)** — Pick B of Daily Research 2026-10-22. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Record the **money-as-derived-from-an-append-only-journal** vocabulary and the specific pairing of **a business-day acceptance clock** with **derived invoices**, and flag explicitly that this pick **overlaps existing feature 54** (`corner-mart-pos-double-entry`) rather than pretending it is new. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **signed append-only money journal** primitive: price is not a mutable field, it is a position derived from a sequence of signed change orders.
- A written record of the **acceptance-clock-with-named-rejection** primitive — the one genuinely interesting idea here: *"acceptance is a business-day clock stopped only by a rejection that names a criterion."* A rejection is only actionable if it says **which criterion failed**. A rejection that says "rejected" carries no information.
- A written record that **invoices are computed from the journal**, never stored independently. This is the direct analogue of §3.3's *current stock is derived from entries* — and it is **why this pick is filed as `defer` rather than `build`**: LE31 already decided this principle.
- An explicit overlap note against feature 54.

**Out of scope (defer artifact):**

- Any B2B invoicing capability. **This is a declared non-goal for LE31.**
- Any signature, counterparty, or contract model.
- Adoption of the Go codebase (off-stack, and 9 KB — there is nothing to adopt).
- Any change to LE31's EUR handling (§3.6, no binary floats).

## Out of scope

- See "Scope" above. The defer artifact is **vocabulary-only**; no code is shipped today.

## Evidence / JTBD

**Gate check 1 (JTBD) fails as written.** The repo's job is: *when two parties are contracting, each wants the agreed price to be unchangeable except by mutual signed consent, but struggles because a mutable price field makes disputes unresolvable, so that the final invoice can be reconstructed from the record.* **LE31 has no counterparty, no contract, and no invoice.** It serves one restaurant. There is no second party to sign anything.

- **Evidence class**: **observed** (repo exists; fields read from `GET /repos/polycratia/engageledger`, not from a search index).
- **Confidence**: **high** that the description means what it says; **low** for LE31 relevance.
- **Traction caveat, recorded plainly**: ★1/⑂0 is **no traction evidence in either direction**. The series high remains ★148 (`FreeOpenSourcePOS/FloCafe`, 2026-10-21). This is a 9 KB repo with **zero topics** — filed for one named idea, not for the project.
- **Real observed LE31 JTBD**: **zero**. The closest LE31 analogue is stock, not money, and §3.3 already covers it.

## Description

GitHub `polycratia/engageledger` (MIT ✓, ★1/⑂0, 9 KB, Go OFF-STACK, created 2026-10-19, pushed 2026-10-21, archived=false, topics `[]`).

Four primitives, only two of which are worth LE31's attention:

1. **Price moves only by change orders signed by both parties** — no counterparty in LE31. Not applicable.
2. **Acceptance is a business-day clock stopped only by a rejection that names a criterion** — **the one transferable idea.** LE31 persists timezone-aware instants and renders business dates in `Europe/Paris` (§3.7). This repo suggests the missing half: not just *when* a business day elapsed, but the rule that a clock can only be stopped by an event that carries a **reason code**. A rejection without a named criterion is indistinguishable from a stall.
3. **Invoices computed from the journal** — **already LE31's position.** §3.3: current stock is derived from `StockEntry` entries and never stored as a mutable total. Adopting this adds a citation, not a capability.
4. **A signed append-only journal as the single source of truth** — already §3.3, modulo the "signed" part, which is about tamper-evidence and is already covered by feature 49 `postledger-tamper-evident-hash`.

**Overlap declaration:** item 3 and item 4 are both already covered by feature 54 (`corner-mart-pos-double-entry`) and feature 49 (`postledger-tamper-evident-hash`). This pick contributes **one** new idea — item 2 — against two already-filed ones. That ratio is the reason for `defer`.

## Data model

None shipped.

For reference, the implied shape is a **journal of signed entries** (the only persisted monetary truth), **change orders** as a distinct signed entry type, and an **acceptance state machine** whose transitions are all clock-stops carrying a mandatory criterion. The transferable fragment is the mandatory `rejection_criterion` on any state transition that halts a business-day clock.

No LE31 entity changes.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition:** (1) LE31 ever needs a business-day SLA that can be halted (a supplier delivery window, an order-quote validity period); **and** (2) feature 54's double-entry work has defined how a rejection reason is represented. **Both** must hold. A single surface needs only the reason-code field, which is a small design question, not a feature.

## Telegram interaction

None today. If the trigger ever fires, the cook-facing analogue would be a Telegram prompt that **requires** a category before allowing a hold — never a bare "reject" button. Recorded here so the constraint is not rediscovered later.

## Dependencies

None. No new runtime dependency. No Go adoption. No signature library.

## Open questions

1. **Does the mandatory-criterion rule apply to LE31 at all?** Only if LE31 grows a clock that can be halted. It has none today.
2. **Would adding a mandatory reason code to a Telegram interaction violate §3.4** (operational transitions are explicit user actions)? No — requiring more explicitness is aligned with it, but it does add friction to the cook's hands-busy surface, which is a real cost against §3.5.
3. **Overlap with feature 54** — should this contract be merged into 54 rather than standing alone? Probably yes at some point; left separate because it is a distinct external citation.

## Why this matters

Honestly, marginally. One idea — *a clock may only be stopped by a rejection that names a criterion* — and two ideas LE31 already has. The reason to keep the file rather than discard it is that the reason-code rule is a genuine refinement to how LE31 thinks about explicit transitions, and it arrived attached to a working example. **This does not justify build time, and the contract does not pretend otherwise.**

---

**Gate verdict: `defer`.** Fails check 1 (JTBD — no counterparty exists in LE31's product) and partially fails check 5 (scope — two of four primitives duplicate feature 54 and feature 49). No hard conflict. Fully reversible (9 KB, vocabulary-only).