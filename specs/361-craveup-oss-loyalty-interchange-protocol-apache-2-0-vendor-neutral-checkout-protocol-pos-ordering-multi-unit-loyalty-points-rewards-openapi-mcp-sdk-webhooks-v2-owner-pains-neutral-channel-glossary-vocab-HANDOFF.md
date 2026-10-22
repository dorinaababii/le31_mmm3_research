# HANDOFF — Feature 361 · Vendor-neutral channel protocol with glossary binding (defer, v2 owner-pains)

**Date:** 2026-10-22 · **Feature:** `features/361-craveup-oss-loyalty-interchange-protocol-...-neutral-channel-glossary-vocab.md`
**Source:** [`craveup-oss/loyalty-interchange-protocol`](https://github.com/craveup-oss/loyalty-interchange-protocol) — Apache-2.0 ✓ §3.2 · ★4/⑂0 · TypeScript off-stack · created 2026-07-15, pushed 2026-10-18
**Linear:** not attached — write endpoint blocked (34th day), `requestId a4e6a0548d28d2de`

## Why this is deferred

**Neutrality is a property of a set, not of a single member.** LE31 has one venue and therefore one integration. There is nothing to be neutral *between*. The precondition is unmade, so this is filed as parking-lot vocabulary, not scheduled work.

## Two ideas, deliberately not bundled

| Idea | Disposition | Reason |
|---|---|---|
| Vendor-neutral protocol (`openapi` + `webhooks` + `sdk` + `mcp`) | **deferred** | Cost is paid up front; benefit arrives only with the second integration. |
| Glossary binding (canonical term ↔ external vocabulary) | **retained as a cheap question** | The vocabulary problem is *already present* in LE31. Recording it costs one document. |

Bundling them into a single "deferred" note would have discarded the second. They are separated deliberately.

## Upstream references

| Ref | Detail |
|---|---|
| Repo | https://github.com/craveup-oss/loyalty-interchange-protocol |
| Licence | Apache-2.0 (verified via `GET /repos/craveup-oss/loyalty-interchange-protocol`, 2026-10-22) |
| Description | *"Open-source restaurant loyalty platform and vendor-neutral checkout protocol for POS, ordering, and multi-unit teams."* |
| Topics | 20, incl. `protocol`, `foodservice`, `qsr`, `loyalty`, `points`, `openapi`, `mcp`, `sdk`, `webhooks` |
| In-window | `pushed_at` **only** (2026-10-18); created 2026-07-15 (~3 months old) |
| Supporting, independent | [`amisonnet8/mtqg`](https://github.com/amisonnet8/mtqg) — MIT, created 2026-10-20, in-window — carries a **glossary** as a first-class axis beside decisions and rules, showing the glossary is a general pattern rather than a loyalty quirk |

**Adoption posture: vocabulary only.** TypeScript not adopted. **The loyalty/points/rewards feature set is explicitly NOT part of this pick** — that is the part being deferred. LE31 has no AI surface, so the `mcp` topic is recorded only to close the question, not to raise it.

## Slice

**None.** No API, no spec, no SDK, no webhook, no MCP server, no loyalty feature, no multi-unit work.

## Trigger conditions

Protocol work resumes when **all** hold:
1. LE31 has a **second** downstream integration or a **second** venue (load-bearing, currently unmet), **and**
2. owner-facing vocabulary has been **observed** to diverge in practice — not assumed, **and**
3. if MCP exposure is ever wanted, the §3.4 AI-surface question has an answer.

Glossary recording resumes on its own weaker trigger: **the first time a term is found to mean two different things in two different places.**

## Acceptance

None — zero code. The deliverable is the decision record itself.

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| "Vendor-neutral" becomes an excuse for premature abstraction | **high** | The trigger conditions are explicit and condition 1 is currently unmet. |
| Glossary over-engineered into a runtime `CanonicalTerm` table at one venue | medium | Open question: glossary as document, not entity, until there is more than one vocabulary to bind. |
| Whose vocabulary is canonical is decided by accident | medium | Open question 2 — an actual unmade decision with no obvious default. |

## Reversibility

**Trivially reversible.** A document. No code, no migration, no surface.