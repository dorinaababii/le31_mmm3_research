# Feature 145 — garde-fous frozen-mandate append-only agent-loop vocabulary (defer)

> **NEW observation (2026-09-05).** Documents in-window GitHub repository `FiExplorer11020/garde-fous` (0★/0 forks, MIT, Python, pushed **2026-08-28T13:11:17Z**, in-window by push only): *"Une boucle d'agent qui ne peut pas déraper : mandat gelé, actions irréversibles proposées, état dérivé d'un journal en écriture seule."* (An agent loop that can't slip: frozen mandate, irreversible actions proposed, state derived from an append-only journal.) French language. **First surface of this repo in the 37-pass series** (parent-verified by ripgrep against all features 1–143 + all brainstorm reports 2026-08-18..2026-09-04). Bucket: **v2 owner-pains (architecture reference)** — watch-list defer. Zero build time today.

## Goal

Retain the **frozen-mandate operating-mode** as the **architectural vocabulary** for any future LE31 v2-AI surface that needs an *agent loop that respects charter §3.1's no-silent-automation invariant*. The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the garde-fous vocabulary: frozen mandate (set at startup, never edited mid-loop) + irreversible-actions-proposed-not-taken (every potentially-durable action is *proposed* first) + state-derived-from-append-only-journal (the agent's view of state is always reconstructed from a log, never from a mutable cache).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-agent loop today (charter §3.4 forbids customer-facing AI; v1 has no AI at all); the defer surfaces the vocabulary for the next v2-AI surface that wants to build an auditable agent loop.
- A reference for the next time LE31 proposes a v2-AI surface that needs to satisfy *"the agent's mandate is set at startup, never edited mid-loop, and any irreversible action is proposed, not taken"*.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `audit_logs` schema.
- Any user-facing "AI agent loop" surface (no cook-facing AI agent today; charter §3.4 forbids customer-facing AI; staff-facing AI is allowed but not in v1).
- Adoption of the garde-fous code — LE31 has no AI agents today, so adopting the library would require an AI-agent surface that doesn't exist.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes an LLM-assisted cook-facing or owner-facing assistant that *acts on `audit_logs` to make recommendations*, the owner wants *an agent loop whose mandate is fixed at startup and cannot drift mid-conversation*, but struggles because *LLM agents routinely edit their own mandate as context changes*, so that *the assistant's recommendations are reproducible from the audit log without requiring a conversation replay*.

- **Evidence class**: inferred (no LE31 owner has asked for an AI-agent surface in 37 passes).
- **Confidence**: medium (mechanism) / low (present urgency).
- **Real observed LE31 JTBD**: none. No owner has asked *"can the assistant's recommendations be reproduced from the audit log?"* in 37 passes.
- **The value is contingency**, not direct demand: when v2-AI is considered, the vocabulary already exists.

## Description

GitHub `FiExplorer11020/garde-fous` (0★/0 forks, MIT, Python, pushed 2026-08-28T13:11:17Z, in-window by push only) — *"Une boucle d'agent qui ne peut pas déraper : mandat gelé, actions irréversibles proposées, état dérivé d'un journal en écriture seule."* (An agent loop that can't slip: frozen mandate, irreversible actions proposed, state derived from an append-only journal.)

The transferable primitive is the **frozen-mandate operating-mode**, expressed as three sub-primitives:

1. **Frozen mandate**: the agent's mandate is set at startup (e.g., *"recommend cook-time adjustments"* or *"flag stock-shortage risks"*) and is never edited mid-loop. The mandate is *immutable* for the duration of the conversation.
2. **Irreversible-actions-proposed-not-taken**: any action that would have a durable effect on the system (e.g., *"reduce the prep quantity for tomorrow"* or *"close tonight's shift"*) is *proposed* (written to the audit log as a `proposal: <action>` row) but **not taken** without explicit human confirmation. The proposal is a `StockEntry`-style append-only row; the human-confirmed action is a second append-only row.
3. **State-derived-from-append-only-journal**: the agent's view of the system state is always reconstructed from the append-only journal, never from a mutable cache. The agent has no in-memory state that is not also in the journal.

**Cross-section with LE31 charter §3.1** (explicit operational transitions):

| Charter invariant | v1 status | Garde-fous primitive |
|---|---|---|
| **Explicit operational transitions, no silent automation** (charter §3.1) | **Satisfied** — every `StockEntry` row is an explicit user action. | Garde-fous is the *AI-agent-loop version* of this invariant: every agent action is also explicit, *and* the proposal is a separate row from the action. |
| **No customer-facing AI** (charter §3.4) | **Satisfied** — v1 has no AI. | Garde-fous is the *staff-facing AI* vocabulary; it does not propose any change to the customer-facing-AI exclusion. |
| **Money: never use binary floats. Preserve exact EUR values** (charter §3.1) | **Satisfied** — `Decimal` everywhere. | Garde-fous does not address money directly; the *proposal-then-action* pattern is invariant for any action, money or otherwise. |

**Cross-section with the existing features 126 / 127 / 134 / 135 / 141 family:**

- **Feature 126 Five Primitives for Governing AI Agents at Runtime** (2026-08-28) — *runtime-witnessing primitives*. Garde-fous contributes the **mandate-immutability** primitive: the agent's mandate is one of the primitives that runtime-witnessing must verify.
- **Feature 127 Ledger-Based Control in Zero-Shot Self-Orchestration** (2026-08-28) — *ledger-based control = agent loop reads from a ledger, not a mutable cache*. Garde-fous is the *operational-mode* of ledger-based control: a frozen mandate + append-only proposals is exactly what ledger-based control looks like at the agent-loop level.
- **Feature 134 ECHO Auditable Memory Plane** (2026-09-04) — *replace append-only with structured records*. Garde-fous is the *agent-loop* discipline: structured records of proposals + actions replace silent state mutations.
- **Feature 135 DreamLedger** (2026-09-04) — *credit-ledger dual of `StockEntry`*. Garde-fous contributes the **proposal-then-action** pattern that any credit-ledger (or `StockEntry`-style ledger) can opt into for AI-agent-loop integration.
- **Feature 141 KRINEIA five invariants** (2026-09-04) — *proof/record distinction*. Garde-fous's frozen mandate is the *upstream* of KRINEIA's `no reward-path self-reference` invariant: the agent's mandate cannot be self-edited because it is frozen at startup.
- **Feature 137 NL-to-Executable-Obligations** (2026-08-29) — *policy compilation*. Garde-fous adds the *proposal-then-action* discipline that any NL-policy surface must respect: a policy is *compiled* into a proposal, not into an action.

**Cross-section with feature 68 `cook-assistant-deterministic-gate`** (2026-08-15) — *the model proposes, the deterministic gate decides*. Garde-fous is the *operational-mode* of feature 68: feature 68 says *"the gate decides"*; garde-fous says *"the gate decides, and the agent cannot bypass the gate by editing its own mandate"*.

LE31 v1 currently has no AI-agent loop; the defer surfaces the garde-fous vocabulary for future use. The value is **vocabulary**, not *implementation*.

## Data model

No schema change today. The defer artifact documents that the future garde-fous-instantiation would have:

- **Mandate table** (future): a `mandate` table that stores the agent's startup mandate as an immutable row; any subsequent mandate edit would be a new row with `supersedes_mandate_id` pointing to the prior mandate. **Not built today.**
- **Proposal table** (future): a `proposal` table that stores every agent-proposed action as an immutable row with `status: pending|confirmed|rejected|expired`; the agent cannot directly write `StockEntry` rows without a prior proposal. **Not built today.**
- **Action table** (future): a `action` table that stores every human-confirmed action as an immutable row with `proposal_id` linking to the proposal; **not built today.**

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to build this in v2, the implementation steps would be:

1. Add a `LE31_GARDE_FOUS_ENABLED` env flag (default off).
2. Add the `mandate` + `proposal` + `action` tables above.
3. Add a thin `AgentLoop` base class whose `propose(action)` returns a `proposal_id` rather than executing the action; whose `confirm(proposal_id, human_id)` writes the `action` row.
4. **Out of scope for v1**: any v2-AI surface that uses `AgentLoop`; any LLM integration; any cook-facing or owner-facing assistant.
5. **Out of scope for v1**: any mandate-edit workflow; mandates are frozen at startup forever in this defer.

## Telegram interaction if any

None. Garde-fous is an architecture-reference artifact; no cook-facing Telegram surface today. If the LE31 owner decides to build the v2-AI owner-facing assistant surface, garde-fous would be exposed *as* part of that surface, not separately.

## Dependencies

- **GitHub**: `FiExplorer11020/garde-fous` (0★/0 forks, MIT, Python, pushed 2026-08-28T13:11:17Z, in-window by push only).
- **Charter §3.1 (explicit operational transitions)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.4 (no customer-facing AI; staff-facing AI allowed with observable evidence + non-AI fallback)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Companion artifacts**: features 68 / 126 / 127 / 134 / 135 / 137 / 141 (ripgrep-verified distinct).
- **Stack**: no new dependency today; future v2-AI would require LLM integration (out of scope today).
- **Licence**: MIT — importable for reference but not proposed as a v2 dependency (LE31 has no AI agents today). README contents not read in this pass (parent relied on the GitHub Search `description` field — French-language).

## Open questions

1. **Who would invoke the frozen-mandate agent loop on a v2-AI LE31 surface?** LE31 has one stakeholder (the owner) and v1 has no AI. The vocabulary is conceptually useful but adds no operational value today. Same open question as features 121 / 141 / 144: if LE31's one stakeholder is the only one who can read the audit log, the marginal value of formal agent-loop discipline over charter §3.1's natural explicit-transition posture is **unproven**. Recommendation: revisit when LE31 v2-AI is considered.
2. **Does charter §3.1 need a `frozen-mandate` clause for v2-AI?** Today, no. A future v2-AI surface that uses `AgentLoop` would make this explicit. Recommendation: not a v1 question; revisit when v2-AI is considered.
3. **Is the proposal-then-action pattern compatible with feature 68's `cook-assistant-deterministic-gate`?** Yes, but the verification is not done — feature 68's gate is one instance of a proposal-then-action pattern; garde-fous is the *general* pattern. Recommendation: when v2-AI is considered, feature 68 should be re-stated as a *specific* proposal-then-action instance with garde-fous as the *general* vocabulary.
4. **Does the mandate-immutability invariant hold across the agent's full lifecycle, or per-conversation?** Today: per-conversation (the mandate is set at startup of each conversation). The repository's `0★` traction suggests the design has not been pressure-tested in production; not independently verified. Recommendation: do not commit to adoption without an in-restaurant pilot.

## Why this matters

LE31 charter §3.1 has been **operationalizing explicit-transition discipline** for 37 passes without ever surfacing the *frozen-mandate operating-mode* for AI-agent loops. Garde-fous is the **first primitive in the 37-pass series** that gives the agent-loop question a charter-§3.1-friendly answer: *the agent's mandate is frozen at startup, irreversible actions are proposed not taken, and state is derived from an append-only journal*. The value is not implementation today — LE31 v1 has no AI-agent loop. The value is **vocabulary**: any future v2-AI surface can now ask *"how do we build an agent loop that respects charter §3.1?"* and design with garde-fous as a primitive, instead of rediscovering the no-silent-automation tension from first principles each time. Combined with features 68 + 126 + 127 + 134 + 135 + 137 + 141, the family now has **eight independent papers/repos** that converge on append-only + frozen-mandate + proposal-then-action as the right primitive set for auditable AI-agent loops. This is the **deepest single-vocabulary cluster of the 37-pass series**.

The defer is fully reversible: if the LE31 owner decides the vocabulary is not worth carrying, the file can be deleted with no operational impact. The vocabulary is contained in the file, not in the codebase.