# Feature 148 — coxswain-graphs-harness-owns-consequence-architecture-pattern (defer)

> **NEW observation (2026-09-07).** Documents in-window GitHub repo `ppfenning/coxswain-graphs` (MIT, **0★/0⑂**, Python, **pushed 2026-09-06T21:17:39Z**, in-window by push only, 619 B repo). Description (verbatim): *"Graphs own sequence and write nothing; one harness owns every consequence — the gate, the worktree, the checks, the append-only ledger."* The **inverse** of feature 129 LEDGER (which adds a typed-edge layer over an existing append-only log): feature 129 says *add typed edges on top of the log*; coxswain-graphs says *the log is the only thing that holds consequence* and *graphs own sequence*. The **tightest one-sentence architectural statement of the 39-pass series** (619 B is a README that *fits in a tweet*). Bucket: **v1 architecture-reference** — watch-list defer. Zero build time today.

## Goal

Retain the **"graphs own sequence and write nothing; one harness owns every consequence"** architectural pattern as a persistent cross-section reference for the LE31 v1 architecture review. The artifact is the persistent cross-section reference + a candidate *architectural axiom* for the next v1 architecture-review moment. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the coxswain-graphs architectural pattern: *graphs own sequence / one harness owns every consequence / append-only ledger* + the *gate / worktree / checks / ledger* sub-primitive set.
- A written record of the **inverse relationship with feature 129 LEDGER** (which adds typed edges over the log) — the two patterns are *complementary, not competing*.
- A decision record: today's verdict is `defer` because the LE31 v1 codebase already implements the pattern implicitly (the single FastAPI process *is* the harness, the `audit_logs` *is* the ledger, the operational state transitions *are* the gate); the defer surfaces the pattern as a *named architecture*, not a code change.
- A cross-section reference with prior picks: features 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146, 147.

**Out of scope (defer artifact):**
- Any change to the FastAPI process structure.
- Any change to the `audit_logs` schema.
- Any change to the operational-transition machinery.
- Any new architectural pattern (the coxswain-graphs pattern is a *naming* of the existing LE31 architecture, not a new pattern).
- Adoption of the coxswain-graphs code (the repo is a 619 B README, not an importable library).

## Evidence / JTBD

When a future LE31 maintainer reads the codebase, the owner wants *a one-sentence statement of the architecture*, but struggles because *the architecture is implicit in the code*, so that *the next maintainer can verify the architecture hasn't drifted*.

- **Evidence class**: observed (the coxswain-graphs README is a *one-sentence architectural statement* that matches the LE31 v1 architecture).
- **Confidence**: high for the architectural match (the four sub-primitives — gate / worktree / checks / append-only ledger — map onto LE31's operational-transition gate, FastAPI request handling, validation pipeline, and audit_logs respectively).
- **Real observed LE31 JTBD**: zero-pain today; the codebase is small enough that the architecture is implicit.
- **The value is naming, not direct demand**: when the architecture *is* reviewed (e.g. before a v2 surface lands), the coxswain-graphs pattern is a ready-made *named* architecture.

## Description

GitHub `ppfenning/coxswain-graphs` (MIT, 0★/0⑂, Python, pushed 2026-09-06T21:17:39Z, in-window by push only, 619 B). Description (verbatim): *"Graphs own sequence and write nothing; one harness owns every consequence — the gate, the worktree, the checks, the append-only ledger."*

The architectural pattern has two clauses and four sub-primitives:

1. **"Graphs own sequence and write nothing"** — *sequence* (ordering) is the only thing graphs hold; graphs do not hold *state* (state is derived from the append-only log).
2. **"One harness owns every consequence"** — there is one (and only one) subsystem that owns *consequences* (the *side effects*: ledger writes, state transitions, external API calls).
3. **Sub-primitives of the harness**:
   - **the gate** — the entry point that *adjudicates* whether an action is allowed.
   - **the worktree** — the *isolation boundary* where the action is performed.
   - **the checks** — the *validation pipeline* that confirms the action is complete.
   - **the append-only ledger** — the *commit* primitive that records the action's consequence.

**The 1:1 mapping onto LE31 v1 architecture:**

| Coxswain-graphs primitive | LE31 v1 equivalent | Charter section |
|---|---|---|
| graphs own sequence | FastAPI request ordering (request → handler → audit_logs row); the order of events in `audit_logs` is the sequence | §3.1 (every prepared-item quantity change is a new `StockEntry`) |
| graphs write nothing | `audit_logs` is the only authoritative source; derived state (current stock, open orders, shift variance) is computed from `audit_logs` | §3.1 (current stock is derived from entries) |
| one harness owns every consequence | The single FastAPI process owns *all* side effects: `StockEntry` writes, `audit_logs` writes, `Bill` derivations, `Shift` close, aiogram sends | §3.1 (do not silently send, serve, close, or reconcile an order) |
| the gate | FastAPI route handler + dependency-injection validation (e.g. the `Order` transition is gated by an explicit user action) | §3.1 (operational transitions are explicit user actions) |
| the worktree | The SQLModel session — the boundary within which the action is performed | (implicit) |
| the checks | Pydantic validation + SQLModel constraints + the `audit_logs` write confirms the action is recorded | §3.1 (operational transitions are explicit user actions) |
| the append-only ledger | `audit_logs` table (every mutation is a new row, never an update or delete) | §3.1 (Never update or delete ledger events) |

**The inverse relationship with feature 129 LEDGER (claim-to-evidence-trace-graph-audit):**

- **Feature 129** says: *add typed edges on top of the append-only log* — a *graph layer* over the *log layer* — so the owner can *trace* a derived figure back to the rows that produced it.
- **Coxswain-graphs** says: *the log is the only thing that holds consequence*; the *graph* is just the *sequence* of log entries.
- **These are complementary, not competing**: feature 129's typed edges are *over* the log; coxswain-graphs's "graph" is the *sequence* of log entries. Feature 129 adds a *query-time* layer; coxswain-graphs is a *commit-time* discipline.
- **LE31 v1 already implements both**: the `audit_logs` is the commit-time log; the future feature 129 implementation would be the query-time graph layer.

**What coxswain-graphs does NOT transfer:**

- The repo is a 619 B README, not an importable library. There is no "adopt the coxswain-graphs library" option.
- The author is a *research maintainer* (no production deployment evidence in the repo).
- The "gate / worktree / checks / ledger" sub-primitives are the *AI-coding-agent* flavor (the repo is for AI agent loops, not restaurant ops); the LE31 transferability is *architectural, not implementation*.

**Cross-section with prior picks:**

- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. The coxswain-graphs *append-only ledger* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Coxswain-graphs *does not query*; it commits. Feature 122 supplies the query-time measurement; coxswain-graphs is the *what was queried* substrate.
- **Feature 125 auditable-continual-learning-three-axis** — the *commit-time gate* axis. Coxswain-graphs's *the gate* is the *commit-time gate* primitive.
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Coxswain-graphs is the *commit discipline*; feature 127 is the *control mode*.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Coxswain-graphs's *graph* is the *commit-time sequence*; feature 129's *graph* is the *query-time typed edges*. Inverse relationship (see above).
- **Feature 133 hansard-runtime-witnessing** — the *who witnessed* axis. Coxswain-graphs's *the gate* is the *who witnessed the action* witness; feature 133 is the *runtime* witness.
- **Feature 134 echo-record-shape** — the *record shape* axis. Coxswain-graphs's *append-only ledger* is the *commit*; feature 134 is the *record shape* of the commit.
- **Feature 135 dreamledger-execution-settled-credit-ledger** — the *credit ledger* dual. Coxswain-graphs is the *state ledger*; feature 135 is the *credit ledger*.
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* axis. Coxswain-graphs's *the gate* is the *runtime* check; feature 137's obligations would be *compiled into* the gate.
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Coxswain-graphs is the *informal* statement of feature 138's 9-node model.
- **Feature 139 stale-constraints-budgeted-verification-failures** — the *stale-constraint* problem. Coxswain-graphs's *the checks* are the *verification budget*; the *stale constraint* is the *what the checks might miss*.
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Coxswain-graphs's *append-only ledger* is the *record*; feature 141's invariants are the *proof*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** — the *frozen mandate* primitive. Coxswain-graphs's *one harness* is the *frozen mandate*; the mandate is what the harness holds fixed.
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** — the *JTBD framing*. Coxswain-graphs is the *architecture*; feature 146 is the *JTBD that the architecture serves*.
- **Feature 147 reliability-lives-in-institution-not-cognition-2609-03192v1** — the *experimental test* of the architecture. Coxswain-graphs is the *informal* statement; feature 147 is the *experimental* test.

The 15 picks (this one + 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146, 147) form the **deepest single-vocabulary cluster in the 39-pass series** for the *append-only-ledger + one-harness-owns-consequence* architectural pattern. **All 15 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the coxswain-graphs architectural pattern to `specs/2026-09-07-coxswain-graphs-harness-owns-consequence-architecture-pattern-HANDOFF.md`** as a named architecture for the LE31 v1 codebase — already done in the HANDOFF.md.
2. **Wait for the first v1 architecture-review moment** — trigger condition: first v1 PR that adds a new subsystem, refactors the FastAPI process structure, or splits the harness into multiple processes.
3. **On trigger, evaluate the change against the coxswain-graphs pattern** — does the change preserve *one harness owns every consequence*? Does it preserve *graphs own sequence and write nothing*? The pattern is the *what to verify*, not the *what to implement*.

## Telegram interaction if any

**None.** The defer artifact is documentation only; no operator surface changes.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.

## Open questions

1. **Is the coxswain-graphs pattern specific to AI-coding agents?** The repo's context is AI agent loops (the worktree is the git worktree, the checks are the CI checks, the ledger is the audit log of agent actions). The LE31 transferability is *architectural, not implementation*; the *names* match (gate / worktree / checks / ledger) but the *substances* differ (LE31's worktree is a SQLModel session, not a git worktree). The transferability is *real but partial*.
2. **Is the inverse relationship with feature 129 LEDGER the right framing?** The two patterns are *both about graphs and append-only ledgers* but at *different layers* (commit-time vs. query-time). The framing is *the graph at commit time is the sequence*; *the graph at query time is the typed edges*. This is a single-pass synthesis; a more careful read of feature 129 may reveal additional nuances.
3. **Should the coxswain-graphs pattern be added to the LE31 charter §3.1 explicitly?** Owner decision required. The pattern is *implied* by the existing §3.1 wording; making it *explicit* is a documentation change, not a code change. Recommend: no, the §3.1 wording is already canonical; adding the coxswain-graphs pattern is *redundant*.

## Why this matters

**Coxswain-graphs is the *tightest one-sentence architectural statement* of the 39-pass series.** 619 B is a README that *fits in a tweet*; the pattern is *commit-time discipline* (one harness owns every consequence) + *commit-time sequence* (graphs own sequence and write nothing) + *commit-time sub-primitives* (the gate, the worktree, the checks, the append-only ledger). The LE31 v1 codebase already implements the pattern implicitly; the defer surfaces the pattern as a *named architecture* for the next maintainer.

**The inverse relationship with feature 129 LEDGER is the architectural complementarity**: feature 129 is the *query-time graph* (typed edges); coxswain-graphs is the *commit-time graph* (sequence). The two together are the *full* LE31 architectural story: *commit-time sequence* + *query-time typed edges* + *one harness owns every consequence*. The cluster (15 picks, this one + 14 prior) is the persistent cross-section reference for the next v1 architecture-review moment.
