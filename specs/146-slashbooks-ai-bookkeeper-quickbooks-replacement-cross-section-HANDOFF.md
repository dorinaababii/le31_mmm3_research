# HANDOFF — 146-slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section

**Status**: defer (parking-lot, watch-list, cross-section competitive signal, no build today)
**Date**: 2026-09-05
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/146-slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section.md`
**LE31 feature gate verdict**: defer (LE31 v1 has no owner-facing month-end-books-reconciliation surface today; the value of slashbooks today is *JTBD validation*, not *implementation*).

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the slashbooks repo (GitHub `giltotherescue/slashbooks`, 32★/4 forks, Apache-2.0, Python, pushed 2026-08-24T22:40:20Z, in-window by push only) as a dated, in-window **JTBD-validation reference** for the next time LE31 proposes a v2 owner-facing month-end-books-reconciliation surface that addresses the *"replace outsourced bookkeeper"* JTBD.

If the trigger condition (LE31 first proposes a v2 owner-facing reconciliation surface — most likely a v2 surface that extends the existing shift-close reconciliation to month-end, or a v2 surface that introduces a chart-of-accounts mapping for the owner) is met, the external coding agent should:

1. Load this artifact and the parent brainstorm report (`/opt/data/le31-brainstorm-2026-09-05.md`).
2. Load the slashbooks repo (parent-fetched 2026-09-05; do NOT trust any prose summary of the library — re-read the README directly from the GitHub repository before adopting).
3. Load the companion features 49 / 119 / 132 / 141 / 144 (ripgrep-verified distinct) — slashbooks is the *JTBD-validation* for the *bookkeeping-surface* family.
4. Re-run the LE31 feature gate with the slashbooks JTBD framing in hand.
5. **Decide whether the new v2 surface addresses the *"replace outsourced bookkeeper"* JTBD**. Use the matrix in the parent feature 146 (`Description` section) as the starting checklist.
6. **For v2 owner-facing reconciliation surfaces**: explicitly check whether the monthly-reconciliation CSV export (the cheapest first step) is the right scope. Do not try to build an AI-agent loop first.
7. **For v2 surfaces with chart-of-accounts customization**: explicitly check whether the existing `audit_logs` + `stock_entry` + `bill` + `shift` tables provide the right substrate. The mapping is a v2 design question.
8. **Pilot on one surface first**. Do not try to satisfy the full *replace outsourced bookkeeper* JTBD at once. The CSV export is the cheapest first step (1-2 days of work; no AI integration; no new dependencies).
9. **Document the per-surface decision** in the surface's feature contract.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/146-slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section.md`
- **Parent brainstorm report**: `/opt/data/le31-brainstorm-2026-09-05.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-09-05/gh_topic_small-business.json` (slashbooks repo at index position verified by parent).
- **Slashbooks repo**: GitHub `giltotherescue/slashbooks` (parent-fetched 2026-09-05; description field re-verified by parent against raw JSON).
- **Companion artifacts**:
  - `features/49-postledger-tamper-evident-hash.md` (Postledger — *double-entry-bookkeeping "assumes the bookkeeper is not trustworthy"*)
  - `features/119-balancedesk-local-first-reconciliation-terminal-cross-section.md` (BalanceDesk — *local-first reconciliation terminal, same JTBD opposite mechanism*)
  - `features/132-sqlmodel-0-0-42-pin-track.md` (sqlmodel pin-track — *LE31's pinned SQLModel version*)
  - `features/141-krineia-five-invariants-append-only-audit-proof.md` (KRINEIA — *proof/record distinction + trust-root separation*)
  - `features/144-silphe-operator-pointer-biometric-hci-cross-section.md` (silphe — *local-only pointer-movement biometric*)
- **Charter §3.1 (Money: never use binary floats. Preserve exact EUR values and explicit tax/tip derivations)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.2 (Privacy: counts not identity)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:

- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 money discipline, §3.2 privacy, §3.4 observable evidence).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build).
- `le31-research` — for the source-of-truth discipline on GitHub repository verification (re-read the README directly from the repo, never trust prose summaries).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner.

## Frozen contract

The vocabulary surfaced by this defer is:

- **"Replace outsourced bookkeeper" JTBD framing**: the small-operator bookkeeping JTBD is real and is being addressed by credible independent maintainers in 2026 (Slashbooks 32★, BalanceDesk 1★ = two independent data points).
- **Plain-text-vs-SQL-mechanism divergence**: Slashbooks (text-ledger + AI agent) and BalanceDesk (local-first desktop) address the same JTBD with opposite mechanisms; LE31 v2 would address it with a third mechanism (SQLModel + Postgres + audit_logs per mutation).
- **JTBD-validation data point**: the 32★ + 4 forks + Apache-2.0 + in-window push is the strongest single JTBD-validation data point of the 37-pass series for the small-operator-bookkeeping surface.

LE31 v1 doesn't have a v2 owner-facing reconciliation surface today. The defer artifact does **not** propose a `monthly-reconciliation` endpoint or a `chart_of_accounts` table. It surfaces the *JTBD framing* for future use.

## Rollback path

This is a documentation-only artifact. There is no code to roll back. If the LE31 owner decides the JTBD framing is not worth carrying, the file can be deleted with no operational impact.

## Verification protocol reference

For the LE31 seven-check feature gate, see `skills/le31-conventions/SKILL.md` §"Feature gate". For GitHub repository verification, see `skills/le31-research/SKILL.md` (always re-read the README directly from the repository, never trust prose summaries — the 2026-08-28 subagent fabrication incident is the reference failure mode).