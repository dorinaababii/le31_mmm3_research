# Feature 367 — `tianye1999-dsb-execution-gate-task-ledger-vocabulary` (defer)

> **NEW observation (2026-10-23).** Documents in-window GitHub repo `tianye1999/dsb` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★1/⑂0**, **7,295 KB**, **Python ✓ ON-STACK**, created **2026-10-23 AND pushed 2026-10-23 = IN-WINDOW BY BOTH FIELDS (same-day repo)**, `archived=false`, `fork=false`, 0 open issues, default_branch=`main`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-23, not from search-result numbers. Description (verbatim from GitHub API): *"DSB (逗沙包): an open-source, trust-first Android AI agent. Delegate app chores on a background virtual display, with execution gates, a task ledger and audit logs. No root, no always-on PC. Built on DeepSeek Harness (DSH), DeepSeek by default."* Topics (verbatim): `accessibility-service, ai-agent, ai-assistant, android, audit-logging, chinese, deepseek, guardrails, gui-agent, llm-agent, mobile-agent, open-source, phone-automation, privacy, scrcpy, termux, trustworthy-ai, virtual-display`. Bucket: **v2-AI (execution-gate + task-ledger + audit-log vocabulary)** — Pick A of Daily Brainstorm 2026-10-23. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

## Goal

Retain the **execution-gate + task-ledger + audit-log** vocabulary as a persistent cross-section reference, and record the observation that an independent team building an agentic system on Android arrived at the same safety triple LE31 uses for operational state — without any knowledge of LE31. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **execution-gate → task-ledger → audit-log** triple: when a system can take actions on a user's behalf, the minimum defensible record is (1) an explicit gate the human passes, (2) a ledger of what was proposed and approved, (3) a log of what actually ran. This is the same shape as LE31's §3.1 explicit-state + §3.3 append-only-ledger + audit-trail invariants.
- A written record of the **`trustworthy-ai` + `guardrails` + `privacy` topic posture** — the framing is deliberate and named, not incidental.
- A decision record recording that this is the **third pass in three days to surface the same unmade owner decision** (see "Why this matters").

**Out of scope (defer artifact):**

- Any LE31 code, schema, or agentic surface.
- Adopting the DSB codebase (Android/DeepSeek/virtual-display stack is entirely off-stack).
- Any AI feature. LE31 has no AI surface today.

## Out of scope

- See "Scope" above. This artifact is **vocabulary-only**; no v1 code is shipped.

## Evidence / JTBD

- **Evidence class**: observed. The description and topics name the primitives explicitly; all numeric fields came from the repo endpoint.
- **Confidence**: high for the vocabulary match (the triple is named in the project's own description); **low for transferability** — LE31 has no agentic surface to gate.
- **Traction caveat, recorded plainly**: ★1⑂0 is **no traction evidence in either direction.** It is a repo created and pushed on the same day as this pass. The pick is about the *shape*, not the project.
- **JTBD**: When a future LE31 surface lets a system act on the owner's behalf, the owner wants *an explicit gate plus a durable record*, but struggles because *LE31's existing gate (the §3.1 explicit user action) was designed for a human operator and has never been stress-tested against a system that proposes actions*, so that *the ledger proves what was approved versus what ran*.

## Description

`tianye1999/dsb` is a trust-first Android AI agent that delegates app chores to a background virtual display. Its safety architecture is the transferable part:

1. **Execution gates** — the agent cannot act without passing an explicit gate. This is §3.1 *operational transitions are explicit user actions* applied to an agent instead of a waiter.
2. **Task ledger** — a durable record of proposed/approved tasks. This is §3.3 *StockEntry ledger, never update or delete*, applied to agent intent rather than stock.
3. **Audit logs** — what actually executed. Distinct from the ledger: the ledger is intent, the log is outcome. LE31 currently conflates these (a StockEntry records both the delta and its cause).
4. **No always-on PC, no root** — the §3.5 self-contained posture.

The **difference worth keeping** is the ledger/log split. LE31's StockEntry is one record that carries both the quantity change and its reason. DSB separates *what was authorised* from *what happened*. If LE31 ever gains any automated actor, that split is the cheapest way to keep the ledger honest — because a divergence between authorised and actual is exactly what an audit trail exists to surface.

## Data model

None shipped. The vocabulary implies: **ProposedTask** (intent, gate-required) → **Approval** (explicit human action, timestamped, append-only) → **ExecutionLog** (what ran, append-only, may diverge from approval). LE31's current `StockEntry` merges Approval and ExecutionLog.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) an owner decision that LE31 gets any AI/agentic surface; (2) the §3.7 boundary rule for operational vs guest data; (3) a v1 PR proposing any automated actor.

## Telegram interaction if any

None today. Long-horizon note: if the gate primitive is ever adopted, the cook's Telegram bot is the natural gate surface — an inline Approve/Reject button is a §3.1-conformant explicit action and needs no new client.

## Dependencies

None. No new packages, no schema migration, no infrastructure.

## Open questions

1. **Does LE31 get any AI surface at all?** Unmade. This is the third pass to surface it (features 352, 354, and this one).
2. **Should the ledger/log split be adopted for `StockEntry` even without any AI?** Possibly, but that is a v1 data-model change with no current pain behind it — do not do it speculatively.
3. **Unresolved conflict carried forward:** features 352 and 354 disagree on retrieval strategy (vector-first hybrid vs keyword/file-based with full document surfacing). Untouched here.

## Why this matters

Because the question it raises — *should a system be able to propose an action without a human approving it?* — is the question LE31's §3.1 already answers for humans and has never answered for software. This project answers it for an agent in a hostile environment (a phone automating arbitrary apps), and does so with the same three primitives LE31 already owns. Recording the vocabulary now means that if LE31 ever gets an agentic surface, the design does not start from zero.

## Cross-section

Features 352 (`Idriz-hax/harbor-ledger-memory`), 354 (`AIDAChip-Inc/mem-plus-plus`), 90 (`pronto-cafe-telegram-reminders`). All three of 352/354/this pick bottom out on the same unmade AI-surface decision. GitHub `tianye1999/dsb` is unique vs features 1–363 (verified by ripgrep against `features/` and `specs/`). Fully reversible — documentation-only artifact.