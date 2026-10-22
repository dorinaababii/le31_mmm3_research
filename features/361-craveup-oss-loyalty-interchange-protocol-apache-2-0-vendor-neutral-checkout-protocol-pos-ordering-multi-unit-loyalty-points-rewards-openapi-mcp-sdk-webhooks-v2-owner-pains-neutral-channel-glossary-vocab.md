# Feature 361 — `craveup-oss-loyalty-interchange-protocol-apache-2-0-vendor-neutral-checkout-protocol-pos-ordering-multi-unit-loyalty-points-rewards-openapi-mcp-sdk-webhooks-v2-owner-pains-neutral-channel-glossary-vocab` (defer)

> **Pick C of Daily Brainstorm 2026-10-22 (pass 83).** Documents in-window GitHub repo `craveup-oss/loyalty-interchange-protocol` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**), **★4/⑂0**, **TypeScript OFF-STACK**, **created 2026-07-15, pushed 2026-10-18** — in-window by `pushed_at` only; the repo is ~3 months old. 20 topics including `api + foodservice + loyalty + points + qsr + mcp + openapi + openapi + protocol + sdk + self-hosted + webhooks`. Bucket: **v2 owner-pains**. Verdict: **`defer`** (parking-lot).

## Goal

Record the **vendor-neutral protocol** idea and, more importantly, the **glossary** idea: that LE31's own channel surface should carry an explicit, versioned mapping from each downstream system's local vocabulary onto one canonical internal identifier. Defer the protocol; the glossary is the durable insight.

## Scope

**In scope (defer artifact):**

- A written record of the **vendor-neutral protocol** shape: a published, documented interface (`openapi` + `webhooks` + `sdk` + `mcp`) that any POS or ordering system can implement or consume, so LE31 is not written against one vendor's semantics.
- A written record of the **glossary binding** idea, supported independently by `amisonnet8/mtqg` (*"memo & rules, todo, Q&A & bugs, glossary: a project journal in your git repo, for humans and AI agents"*, MIT, created 2026-10-20, in-window) — which carries a glossary as a first-class axis alongside decisions and rules.
- A decision record explaining why the protocol is deferred: **neutrality is a property of a set, not of a single member.** With one integration there is nothing to be neutral between.
- An inventory of LE31's own vocabulary that would need canonical terms — table, cover, turn, ticket, prep station, mise en place — recorded as a **question**, not an answer.

**Out of scope (defer artifact):**

- Any published API, OpenAPI spec, SDK, or webhook surface.
- Any MCP server in LE31. **LE31 has no AI surface, and none is proposed.**
- Loyalty, points, rewards, or any customer-engagement feature. The upstream repo is a loyalty platform; **that is the part being deferred, not the protocol idea.**
- Multi-unit or multi-tenant support.
- Adopting the TypeScript codebase (off-stack).

## Evidence / JTBD

**Gate check 1 (JTBD) fails as stated, and this is the reason for the defer.** The repo's job is: *when a restaurant chain runs several POS and ordering systems across units, they want loyalty and checkout data to flow between them without rewriting per vendor, but are stuck integrating each vendor's semantics individually.* LE31 serves **a single owner with a single venue**. There is no integration set, so the job does not exist yet.

- **Evidence class**: **observed** (repo exists; all fields read from `GET /repos/craveup-oss/loyalty-interchange-protocol` on 2026-10-22, parent-verified, **not** from a search index).
- **Confidence**: **high** that the protocol framing is what the repo advertises — the description and the `protocol`/`vendor-neutral` topics are explicit. **Low** for adoption feasibility: ★4, self-hosted, ~3 months old, no evidence of multi-vendor deployments.
- **Traction caveat, recorded plainly**: ★4/⑂0. This is a small project. The idea is worth keeping because it is *structurally* right for LE31's direction, not because this repo is significant.
- **Real observed LE31 JTBD**: **zero** today. The nearest real one is the glossary — LE31's owner vocabulary is currently implicit in the UI copy and the operator's head.

## Description

Two separable ideas from one repo:

**The protocol idea.** Publish LE31's channel surface as a documented, versioned, vendor-neutral contract, so that a future multi-vendor world does not require LE31 to be rewritten. The repo's topic set (`openapi`, `sdk`, `webhooks`, `protocol`, `mcp`) is the shape. This is genuinely good architecture and LE31 should eventually want it.

**The glossary idea.** Every downstream system names things differently. The **same repo's** vocabulary, and LE31's, do not line up; nor does a franchise's franchisee's, nor a cook's. The cross-section move is to bind them explicitly: one canonical internal identifier per concept, with a documented mapping from each external vocabulary, versioned so the mapping can evolve without breaking consumers. `mtqg`'s glossary axis supports this as a general pattern rather than a loyalty-specific quirk.

**Why the protocol defers and the glossary does not.** The protocol's cost is paid up front and its benefit arrives only with the second integration — so it is a bet on a future LE31. The glossary's cost is small, and the vocabulary problem is *already present* in LE31: the owner says "table 4", the UI says something else, the cook says something else again. Recording the vocabulary question today costs one document. That is why this contract keeps the glossary and drops the protocol.

## Data model

None shipped.

For reference, the implied shape is a `CanonicalTerm` (one internal identifier, e.g. `table`) with many `ExternalMapping` rows, each `(external_vocabulary, external_term, canonical_term_id, mapping_version)`. A change to the mapping is a new version, not an in-place edit — the same append-only discipline as §3.3, applied to vocabulary.

No LE31 entity changes.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) LE31 has a **second** downstream integration or a second venue, making neutrality meaningful; (2) the owner-facing vocabulary has been observed to diverge in practice, not merely assumed to; (3) §3.4's AI-surface question has an answer, if MCP exposure is ever wanted. **Condition (1) is unmet and is load-bearing.**

The glossary half has a weaker, independent trigger: record the vocabulary the first time a term is found to mean two different things in two different places.

## Telegram interaction

None. Explicitly none — §3.4 permits AI only in the owner/staff assistance role with a non-AI fallback, and no surface is proposed here.

## Dependencies

- **Blocking:** a second integration or venue. Unmade.
- **Unresolved:** whether the glossary belongs in the domain model or in a docs artifact. A runtime `CanonicalTerm` table is over-engineering at one venue; a written glossary is not. Genuinely open.

## Open questions

1. **Does LE31 ever serve more than one venue?** Unmade, and the entire defer hinges on it.
2. **Whose vocabulary is canonical?** The owner's, the cook's, or the POS vendor's? This is a real decision with no obvious default.
3. **Is `mcp` exposure relevant without an AI surface?** Almost certainly not yet. Recorded to close the question, not to raise it.
4. **Would the §3.7 boundary apply** if external vocabulary ever entered LE31? Yes, and it is unmade — the same unmade boundary already recorded on features 352, 354, and 358.

## Why this matters

Little today, and this contract is honest about that. Its value is that it separates two ideas that arrived bundled: one (the protocol) is deferred on an honest precondition, and the other (the glossary) is preserved as a cheap question worth revisiting the first time a term means two things in two places. Bundling them into one "deferred" note would have discarded the second.

---

**Gate verdict: `defer`.** Fails check 1 (JTBD — LE31 has one venue and therefore no integration set to be neutral between). Fails check 3 (the precondition is unmade). **No hard conflict.** Fully reversible and zero-cost: it is a document. v2 owner-pains bucket. Attached to `le31 Research` P-HMM-1 in the fallback payload only — **not attached in Linear** (write endpoint blocked, 34th consecutive day).