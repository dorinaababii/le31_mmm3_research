# Feature 104 — ALdia AI-Agent Business Engine Cross-Section (Watch-list, Charter-pending)

> **Priority**: P3 (watch-list, charter-pending) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-23 (Pick C, **defer**) · **Bucket**: v2-AI (audit-trail primitive) + v2 owner-pains (audit surface)
> **One-line**: A research-only watch-list artifact that records the in-window `jonalemndi2/ALdia` cross-section peer (1★ Apache-2.0 Python, pushed 2026-08-22) — an **open-source business engine for AI agents with immutable audit trail**. The pattern is **inverse-validation** of LE31 charter §3.4 (no customer-facing AI): ALdia assumes AI-agent-facing API; LE31 says human-staff-facing. The cross-section signal: **LE31 should ship the human-calls + agent-calls variants of the same audit-trail primitive**. **No code today; deferred indefinitely pending explicit charter §3.4 review.**

## Goal

The 2026-08-23 brainstorm scan surfaced `jonalemndi2/ALdia` (1★, Apache-2.0, Python, pushed 2026-08-22T18:57:06Z, https://github.com/jonalemndi2/ALdia) — "Open-source business engine for AI agents (invoicing, payments, inventory, immutable audit trail, self-hosted)." The cross-section insight: **the audit-trail primitive should accept both human-calls and AI-agent-calls** so the same primitive can serve v1 (human staff/waiter) and v2-AI (cook-assistant orchestrator).

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2-AI passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 v2 team considers whether the audit-trail primitive (feature 49 + 81) should accept AI-agent calls (in addition to human staff calls), the team wants to know whether a commercially-viable peer exists, so that LE31 can adopt the same primitive API surface without rewriting the audit chain.

**Why this is a fresh cross-section signal today**: `jonalemndi2/ALdia` is the **first in-window repo to explicitly expose an "open-source business engine for AI agents" with an immutable audit trail**. The prior LE31 audit-trail primitives (feature 49 postledger-tamper-evident-hash, feature 81 append-only-immutable-audit-check) are v2 owner-pains primitives that assume human-calls; ALdia is the operational layer that assumes AI-agent-calls.

## Scope

**In scope (v2-AI + v2 owner-pains, S effort, ≤1 day, defer — charter §3.4 review pending):**
- Daily direct-repo `GET https://api.github.com/repos/jonalemndi2/ALdia` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `jonalemndi2/ALdia` README + commit history in the next daily-research pass to confirm the AI-agent-facing API + immutable-audit-trail architecture (READ ONLY — no import).
- Tracking star velocity + push activity on `jonalemndi2/ALdia`.
- Documenting the AI-agent-facing audit-trail pattern in the LE31 research notes (this artifact is the document).
- **Explicit charter §3.4 review input**: the artifact flags the charter tension for the next charter review.

**Out of scope (no new LE31 implementation):**
- An `jonalemndi2/ALdia` import. The repo is 1★ + Apache-2.0 + Python + unproven.
- A new audit-trail API primitive. Feature 49 + 81 already ship the primitive; this artifact is the agent-calls variant input.
- Any new feature based on the `ALdia` code surface.
- A charter §3.4 change. The artifact flags the tension but does not modify the charter.

## Description

**Evidence precondition:** observed (GitHub `jonalemndi2/ALdia` 1★ + Apache-2.0 + Python + immutable-audit-trail + 2026-08-22 push + clear description cross-section with LE31 features 49 + 81). Confidence: **medium** for the architectural pattern (description is explicit; pattern is reverse-validates the LE31 primitive); **low** for LE31-specific urgency (charter §3.4 binding constraint + 1★ = no observed market validation).

### `jonalemndi2/ALdia`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-23 (this pass) | **1★** | (track) | 2026-08-22T18:57:06Z | Apache-2.0 | Python |

**Direct repo URL**: https://github.com/jonalemndi2/ALdia

**Verbatim description** (from GitHub API):
> Open-source business engine for AI agents (invoicing, payments, inventory, immutable audit trail, self-hosted).

**Why this is the cross-section peer of the day:**

1. **The architectural pattern is inverse-validation of LE31 charter §3.4.** ALdia assumes the audit-trail primitive accepts **AI-agent calls** (the agent records invoice/payment/inventory events directly). LE31 charter §3.4 says no customer-facing AI; v2-AI cook-assistant is owner/staff-facing only. The two designs converge on the **same audit-trail primitive** but diverge on **who calls the API**. The cross-section signal: **LE31 should ship the human-calls + agent-calls variants of the same primitive** so the audit chain is consistent regardless of caller.
2. **The pattern alignment with features 49 + 81 is direct.** Both features already ship the immutable-audit primitive (postledger-tamper-evident-hash + append-only-immutable-audit-check); the missing piece is the API contract that accepts AI-agent calls. ALdia shows that the API contract is the standard small-business CRUD surface (invoicing, payments, inventory) wrapped in an audit-trail envelope.
3. **The pattern is distinct from the NeuruhAI cluster (`96-neuruhai-cluster-watch`).** The NeuruhAI cluster ships the **agent-decision-ledger** primitive (5 sibling repos for AI-agent state revision + outcome calibration + lifecycle + evidence + authorization-consumption). ALdia ships the **business-engine primitive** (invoicing + payments + inventory + immutable audit). Different primitive level; complementary cross-section.

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 v2 team considers whether the audit-trail primitive should accept AI-agent calls (in addition to human staff calls), the team wants to know whether a commercially-viable peer exists, so that LE31 can adopt the same primitive API surface without rewriting the audit chain. Plausible but charter §3.4 is the binding constraint today.
2. **Viability**: If the AI-agent-facing API is approved, the primitive is already implemented (features 49 + 81). No new viability required.
3. **Practicability and confidence**: The peer repo is 1★ + Apache-2.0 + Python + immutable-audit; architecture is straightforward (CRUD + audit-trail envelope); high confidence in the pattern. Low confidence in LE31-specific urgency (1★ + charter tension).
4. **Conflict**: **Flagged** — inverse-validation of charter §3.4. Not a hard conflict (the audit-trail primitive is the same) but requires explicit charter confirmation before adoption. The artifact records the tension for the next charter review.
5. **Outcome, appetite, scope**: v2-AI + v2 owner-pains watch-list. S effort. ≤1 day. **Defer** — charter-pending.
6. **Cost to operational value**: Zero implementation cost; pure pattern-record artifact. High upside (v2-AI API surface) at zero downside IF charter §3.4 is revisited.
7. **Circuit breaker and reversibility**: Fully reversible. Watch-list artifact; can be deleted without consequence.

## Data model

**No schema changes.** Watch-list artifact only.

## Implementation steps

**None** — research-only artifact. The slice ships this Markdown file + a one-row `INDEX.md` update + a `*-HANDOFF.md` slice contract for the coding agent (which records the same non-action: "do not implement today; read the ALdia README on next pass; surface as feature 49 + 81 v2 extension input when ≥5★ validation OR 2+ independent repos converge on the agent-calls API pattern AND charter §3.4 is explicitly revisited"). The slice hand-off is a no-op directive to the coding agent.

## Telegram interaction if any

**None** — the artifact does not interact with the LE31 Telegram-bot surface. The cross-section is observational only.

## Dependencies

- **No code dependencies** (research-only artifact).
- **External data dependency**: `jonalemndi2/ALdia` README + commit history — to be read in the next daily-research pass (carry-over to 2026-08-24).
- **Watch-list add to `le31-daily-research-2026-08-24` pass**: include `jonalemndi2/ALdia` in the 5-repo watch list to track star velocity + push activity.
- **Charter §3.4 review input**: this artifact flags the AI-agent-facing API tension for the next charter review.
- **Feature 49 (postledger-tamper-evident-hash) + Feature 81 (append-only-immutable-audit-check) v2 extension**: this artifact is the agent-calls variant input.

## Open questions

1. **What is the exact API surface of `jonalemndi2/ALdia`?** The description says "business engine" but does not specify the API contract. The next daily-research pass should read the README to confirm whether the audit-trail API is structured REST, gRPC, or something else.
2. **Does `jonalemndi2/ALdia` enforce human/agent caller distinction?** If the audit chain differentiates human-calls from agent-calls in the entry metadata, the cross-section to LE31 charter §3.4 is direct (LE31 can audit-trail both, with a metadata flag for compliance review). If not, the cross-section is weaker.
3. **Is the immutable-audit-trail a per-record hash chain, a Merkle tree, or a CRDT?** The answer determines how transferable the implementation is to LE31's existing audit-trail primitives.
4. **Does charter §3.4 require explicit revision?** This is a charter-level question. The artifact flags the tension but does not modify the charter. The next charter review should consider whether the AI-agent-facing API surface is acceptable as a **non-customer-facing** layer (i.e., the AI agent is the orchestrator, not the customer).

## Why this matters

The 2026-08-23 brainstorm pass surfaces `jonalemndi2/ALdia` as the first in-window peer to explicitly expose an "open-source business engine for AI agents" with an immutable audit trail. The pattern is inverse-validation of LE31 charter §3.4 (no customer-facing AI): ALdia assumes AI-agent-facing API; LE31 says human-staff-facing. The cross-section signal: **LE31 should ship the human-calls + agent-calls variants of the same audit-trail primitive** so the audit chain is consistent regardless of caller. The artifact flags the charter tension for the next charter review, without changing today's roadmap.

**Cross-section with existing LE31 features**:
- Feature 49 (postledger-tamper-evident-hash) → the existing primitive; this artifact is the agent-calls variant input.
- Feature 81 (append-only-immutable-audit-check) → the existing primitive; this artifact is the operational layer input.
- Features 38 (cook-voice-note-to-stockentry) + 41 (telegram-msg-stock-update) → human-calls variants of the inventory primitive.
- Features 68 (cook-assistant-deterministic-gate) + 92 (ai-agent-decision-ledger-cluster-watch) → v2-AI control plane; this artifact is the audit-trail API surface input.

**Why defer, not build**: 1★ = no observed market validation; charter §3.4 binding constraint; inverse-validation only (not direct validation). The artifact is a research-note that records the pattern + the charter tension for future v2-AI iteration.

**Charter tension explicit**: this is the first brainstorm pick that **explicitly flags a charter tension** rather than a hard charter violation. The artifact invites the next charter review to revisit §3.4 with the option of allowing AI-agent-facing audit-trail APIs as a non-customer-facing layer.
