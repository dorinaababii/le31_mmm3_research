# HANDOFF — 145-garde-fous-frozen-mandate-append-only-agent-loop

**Status**: defer (parking-lot, watch-list, architecture-reference, no build today)
**Date**: 2026-09-05
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/145-garde-fous-frozen-mandate-append-only-agent-loop.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no AI-agent loop today — charter §3.4 forbids customer-facing AI; v1 has no AI at all. The value of garde-fous today is *vocabulary*, not *implementation*).

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the garde-fous repo (GitHub `FiExplorer11020/garde-fous`, 0★/0 forks, MIT, Python, pushed 2026-08-28T13:11:17Z, in-window by push only) as a dated, in-window **architectural-vocabulary reference** for the next time LE31 proposes a v2-AI surface that needs an *agent loop that respects charter §3.1's no-silent-automation invariant*.

If the trigger condition (LE31 first proposes a v2-AI surface that needs the frozen-mandate operating-mode — most likely a v2-AI cook-facing or owner-facing assistant that *acts on `audit_logs` to make recommendations*, or a v2 surface that integrates an LLM with the LE31 operational loop) is met, the external coding agent should:

1. Load this artifact and the parent brainstorm report (`/opt/data/le31-brainstorm-2026-09-05.md`).
2. Load the garde-fous repo (parent-fetched 2026-09-05; do NOT trust any prose summary of the library — re-read the README directly from the GitHub repository before adopting, and note that the README is in French).
3. Load the companion features 68 / 126 / 127 / 134 / 135 / 137 / 141 (ripgrep-verified distinct) — garde-fous is the *operational-mode* of ledger-based control; combined with these features, the family has eight independent papers/repos that converge on append-only + frozen-mandate + proposal-then-action as the right primitive set for auditable AI-agent loops.
4. Re-run the LE31 feature gate with the garde-fous three-sub-primitive vocabulary in hand.
5. **Decide which of the three sub-primitives (frozen mandate / irreversible-actions-proposed-not-taken / state-derived-from-append-only-journal) the new v2-AI surface needs**. Use the matrix in the parent feature 145 (`Description` section) as the starting checklist.
6. **For v2-AI surfaces that consult `audit_logs`**: explicitly check `no reward-path self-reference` (KRINEIA invariant #2). Garde-fous's frozen mandate prevents the agent from self-editing its mandate to bypass this invariant.
7. **For v2-AI surfaces that propose irreversible actions**: explicitly check that the proposal is a separate `audit_logs` row from the human-confirmed action; the agent cannot directly write `StockEntry` rows.
8. **For v2-AI surfaces that maintain state**: explicitly check that the agent's view of state is reconstructed from the append-only journal, never from a mutable cache.
9. **Pilot on one surface first**. Do not try to satisfy all three sub-primitives on every v2-AI surface at once.
10. **Document the per-sub-primitive verdict** in the surface's feature contract.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/145-garde-fous-frozen-mandate-append-only-agent-loop.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-09-05.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-09-05/gh_topic_append-only.json` (garde-fous repo at index position verified by parent).
- **Garde-fous repo**: GitHub `FiExplorer11020/garde-fous` (parent-fetched 2026-09-05; description field re-verified by parent against raw JSON — French-language).
- **Companion artifacts**:
  - `features/68-cook-assistant-deterministic-gate.md` (cook-assistant deterministic gate — *the model proposes, the gate decides*)
  - `features/126-five-primitives-Governing-AI-Agents-at-Runtime.md` (Five Primitives — *runtime-witnessing primitives*)
  - `features/127-zero-shot-self-orchestration-Ledger-Based-Control.md` (Ledger-Based Control — *agent loop reads from a ledger*)
  - `features/134-echo-auditable-memory-plane-stockentry-audit.md` (ECHO — *record shape*)
  - `features/135-dreamledger-execution-settled-credit-ledger-architecture.md` (DreamLedger — *credit ledger dual*)
  - `features/137-natural-language-policies-executable-obligations-verification-harness.md` (NL-to-Executable-Obligations — *policy compilation*)
  - `features/141-krineia-five-invariants-append-only-audit-proof.md` (KRINEIA — *proof/record distinction + no reward-path self-reference*)
- **Charter §3.1 (explicit operational transitions, no silent automation)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4 (no customer-facing AI; staff-facing AI allowed with observable evidence + non-AI fallback)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 explicit transitions, §3.4 no customer-facing AI, §3.4 observable evidence + non-AI fallback).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repository verification (re-read the README directly from the repo, never trust prose summaries).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The vocabulary surfaced by this defer is:

- **Frozen mandate**: the agent's mandate is set at startup (e.g., *"recommend cook-time adjustments"*) and is never edited mid-loop. The mandate is *immutable* for the duration of the conversation.
- **Irreversible-actions-proposed-not-taken**: any action that would have a durable effect on the system is *proposed* (written to the audit log as a `proposal: <action>` row) but **not taken** without explicit human confirmation. The proposal is a `StockEntry`-style append-only row; the human-confirmed action is a second append-only row.
- **State-derived-from-append-only-journal**: the agent's view of the system state is always reconstructed from the append-only journal, never from a mutable cache. The agent has no in-memory state that is not also in the journal.

LE31 v1 doesn't have a v2-AI surface that needs this vocabulary today. The defer artifact does **not** propose an `AgentLoop` base class or `mandate` / `proposal` / `action` tables. It surfaces the *vocabulary* for future use.

## Rollback path

This is a documentation-only artifact. There is no code to roll back. If the LE31 owner decides the vocabulary is not worth carrying, the file can be deleted with no operational impact.

## Verification protocol reference

For the LE31 seven-check feature gate, see `skills/le31-conventions/SKILL.md` §"Feature gate". For GitHub repository verification, see `skills/le31-research/SKILL.md` (always re-read the README directly from the repository, never trust prose summaries — the 2026-08-28 subagent fabrication incident is the reference failure mode).