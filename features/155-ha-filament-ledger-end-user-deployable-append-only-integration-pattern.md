# Feature 155 — ha-filament-ledger-end-user-deployable-append-only-integration-pattern (defer)

> **NEW observation (2026-09-08).** Documents in-window GitHub repo `jobshimo/ha-filament-ledger` (MIT, **0★/0⑂**, Python, **pushed 2026-09-07T09:26:19Z**, in-window by push only, 2666 B description). Description (verbatim): *"Home Assistant custom integration that tracks remaining filament with an append-only ledger instead of guesswork."* Topics: `home-assistant`, `home-assistant-integration`, `3d-printing`, `filament`, `bambulab`, `ams`, `hacs`. The **only end-user deployable integration** in the 30-repos append-only-ledger cluster today: a real *user-facing* ledger subsystem (Home Assistant sensor panel showing remaining filament) vs. the abstract frameworks in features 153 (sausageos) and 154 (chronology-protocol). Bucket: **v2 owner-pains architecture-reference** — watch-list defer. Zero build time today.

## Goal

Retain the **"Home Assistant custom integration that tracks remaining filament with an append-only ledger instead of guesswork"** end-user-deployable-integration pattern as a persistent cross-section reference for the LE31 v2 architecture review. The artifact is the persistent cross-section reference + a candidate *named user-facing-deployable-integration primitive* for any future v2 surface that wants to expose `audit_logs` (or a derived view of `StockEntry`) as a directly-deployable integration. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the ha-filament-ledger end-user-deployable-integration pattern: *Home Assistant custom integration* + *append-only ledger* + *instead of guesswork* + *tracks remaining filament*.
- A written record of the **"instead of guesswork"** discipline: the alternative to an append-only ledger is *mutable state* (a counter that decrements), which is the exact mutation model charter §3.1 forbids.
- A written record of the **user-facing deployable integration** primitive: a *normal user integration* (Home Assistant custom component) that exposes the ledger as a sensor panel.
- A decision record: today's verdict is `defer` because the LE31 v1 cook Telegram bot *is* already a user-facing ledger surface; the ha-filament-ledger pattern is recorded as the *user-facing-deployable-integration* primitive for any future v2 surface that wants to expose `audit_logs` (or derived `StockEntry`) as a directly-deployable integration.
- A cross-section reference with prior picks: features 121, 122, 125, 127, 129, 133, 134, 135, 137, 138, 139, 141, 145, 146, 147, 148, 149, 153, 154 = the 19-pick append-only-ledger + production-ERP + cryptographic-verifiability cluster.

**Out of scope (defer artifact):**
- Any change to the cook Telegram bot.
- Any new Home Assistant integration (LE31 v1 is a FastAPI + SQLModel + Postgres + aiogram stack; Home Assistant is a separate ecosystem).
- Any change to the `audit_logs` schema.
- Any new user-facing surface (the v1 cook Telegram bot is the only user-facing surface).
- Adoption of the ha-filament-ledger code (the repo is 2666 B + a Home Assistant custom component; the stack is Home Assistant, not FastAPI → no code adoption is possible).

## Evidence / JTBD

When LE31 v2 introduces an owner-facing audit-export surface, the owner wants *a deployable-integration pattern for exposing `audit_logs` (or derived `StockEntry`) as a normal user integration*, but struggles because *LE31 doesn't yet have a user-facing-deployable-integration primitive*, so that *the v2 surface can be exposed as a normal integration (not a custom build)*.

- **Evidence class**: observed (the ha-filament-ledger README is a *user-facing deployable integration* that uses an append-only ledger to track a specific subsystem; the "instead of guesswork" discipline is the *opposite* of mutable state and the *same* as charter §3.1).
- **Confidence**: high for the architectural match (the four sub-primitives — *Home Assistant custom integration* + *append-only ledger* + *instead of guesswork* + *tracks remaining filament* — map onto a *user-facing deployable integration* that exposes the ledger as a sensor panel).
- **Real observed LE31 JTBD**: zero-pain today; the cook Telegram bot is already a user-facing ledger surface.
- **The value is naming, not direct demand**: when the v2 surface *is* introduced (if/when the owner wants to expose `audit_logs` or `StockEntry` as a deployable integration), the ha-filament-ledger pattern is a ready-made *named user-facing-deployable-integration primitive*.

## Description

GitHub `jobshimo/ha-filament-ledger` (MIT, 0★/0⑂, Python, pushed 2026-09-07T09:26:19Z, in-window by push only, 2666 B description). Description (verbatim): *"Home Assistant custom integration that tracks remaining filament with an append-only ledger instead of guesswork."*

The architectural pattern has one core principle and four sub-primitives:

1. **"Home Assistant custom integration"** — the deployment surface is a *Home Assistant custom component* (HACS-installable, YAML-configurable, Lovelace-card-renderable). Home Assistant is a *popular open-source home-automation platform*; the custom integration is a *normal user-deployable artifact* (not a custom build).
2. **"Append-only ledger"** — the data structure is an *append-only ledger* (every filament-loading event is a new ledger row; the current remaining filament is *derived* from the ledger, not stored as a mutable counter).
3. **"Instead of guesswork"** — the *alternative* to an append-only ledger is *mutable state* (a counter that decrements as filament is consumed). The "guesswork" framing is the author's name for *mutable state*: the alternative is *guessing* the current state, which is brittle (a counter reset, a missed decrement, a race condition all corrupt the state). The append-only ledger *eliminates the guesswork* by being *the only source of truth*.
4. **"Tracks remaining filament"** — the user-facing primitive is a *sensor panel* that shows the current remaining filament (in grams or meters). The sensor is *derived* from the ledger, never stored as a mutable value.

**The 1:1 mapping onto LE31 v1/v2 architecture:**

| Ha-filament-ledger primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Home Assistant custom integration | The cook Telegram bot (aiogram v3) is the *user-facing deployable surface* in v1 | §3.1 (operational transitions are explicit user actions) | **Implemented in v1** — the cook Telegram bot is the user-facing surface |
| append-only ledger | `StockEntry` table (every prepared-item quantity change is a new row) | §3.1 (Never update or delete ledger events) | **Implemented in v1** — `StockEntry` is append-only |
| instead of guesswork (no mutable state) | The v1 codebase does not use mutable state for stock; the current stock is *derived* from `StockEntry` | §3.1 (current stock is derived from entries) | **Implemented in v1** — current stock is derived, not stored as a mutable counter |
| sensor panel (tracks remaining filament) | The cook Telegram bot's view of the prepped-item queue is the *sensor panel* in v1 | §3.1 (the cook's view of the order queue is the user-facing surface) | **Implemented in v1** — the cook Telegram bot shows the order queue |

**The "instead of guesswork" discipline:**

The ha-filament-ledger pattern's contribution is the *naming* of the *no-mutable-state* discipline. The author calls it *"instead of guesswork"* — the alternative to an append-only ledger is *guessing* the current state. This is a *rhetorical* move: instead of describing the discipline as *append-only ledger* (technical), the author describes it as *instead of guesswork* (functional). The rhetorical move is valuable because it *names the alternative* (mutable state = guesswork), which makes the discipline *more persuasive* in product conversations.

LE31 charter §3.1 already covers this discipline (*never update or delete ledger events; current stock is derived from entries*). The ha-filament-ledger pattern's contribution is the *naming* of the alternative as *guesswork* — a rhetorical move that makes the discipline more accessible to non-technical stakeholders (e.g. the owner of a small restaurant).

**What ha-filament-ledger does NOT transfer:**

- The repo is 2666 B + a Home Assistant custom component; the stack is *Home Assistant* (a home-automation platform), not FastAPI → no code adoption is possible.
- The author is a *maintainer with a small but credible footprint* (created 2026-08-02, in-window push 2026-09-07; 0★/0⑂ traction but the topics are credible: `3d-printing`, `filament`, `bambulab`, `ams`, `hacs` — all real Home Assistant ecosystem primitives).
- The "user-facing deployable integration" primitive is a *future v2 surface*, not v1. Introducing it today would be a *v1 surface expansion* that requires an owner decision per charter §3.2.
- The Home Assistant ecosystem is *orthogonal* to LE31's stack (FastAPI + SQLModel + Postgres + aiogram). The *pattern* is portable (any user-facing-deployable-integration that uses an append-only ledger is the same shape); the *code* is not adoptable.

**Cross-section with prior picks:**

- **Feature 121 ledger-commitment-field-tier-minimization** — the *what is committed* axis. Ha-filament-ledger's *append-only ledger* is the commit primitive; feature 121's *canonical digest* is the commitment that makes the commit verifiable.
- **Feature 122 trace-integrity-cait-acceptance-criterion** — the *what is queried* axis. Ha-filament-ledger's *sensor panel* is the *query-time* primitive (a query can read the current state from the ledger); feature 122 supplies the query-time measurement.
- **Feature 125 auditable-continual-learning-three-axis** — the *commit-time gate* axis. Ha-filament-ledger's *instead of guesswork* is the *commit-time gate* (every filament-loading event is gated by an explicit user action — the HACS config flow).
- **Feature 127 ledger-based-control-zero-shot-self-orchestration** — the *operational mode of ledger-based control*. Ha-filament-ledger's *sensor panel* is the *query-time view* of the ledger; feature 127's *proposal-then-action* is the *commit-time* discipline.
- **Feature 129 ledger-claim-to-evidence-trace-graph-audit** — the *explanation-time* axis. Ha-filament-ledger's *sensor panel* is the *explanation-time* primitive (a query can explain why the current state is what it is, by reading the ledger); feature 129's *graph* is the *typed edges* that make the explanation queryable.
- **Feature 133 hansard-runtime-witnessing** — the *who witnessed* axis. Ha-filament-ledger's *append-only ledger* is the *witness* (every event is witnessed by the ledger); feature 133 supplies the runtime witness.
- **Feature 134 echo-record-shape** — the *record shape* axis. Ha-filament-ledger's *append-only ledger* is the *commit*; feature 134 is the *record shape* of the commit.
- **Feature 135 dreamledger-execution-settled-credit-ledger** — the *credit ledger* dual. Ha-filament-ledger is the *state ledger* (filament quantity); feature 135 is the *credit ledger* (AI agent actions).
- **Feature 137 natural-language-policies-executable-obligations** — the *policy compilation* axis. Ha-filament-ledger's *Home Assistant custom integration* is the *policy-as-deployable-integration* posture (the policy is exposed as a normal user integration, not a custom build).
- **Feature 138 institutional-continuity-infrastructure-formal-model** — the *formal model* of institutional continuity. Ha-filament-ledger is the *informal* statement of feature 138's 9-node model (the Home Assistant config flow is the *source* node; the append-only ledger is the *admitted meaning* + *runtime authority* + *consequence* nodes; the sensor panel is the *independent observation* + *reconciliation* + *examination* nodes).
- **Feature 139 stale-constraints-budgeted-verification-failures** — the *stale-constraint* problem. Ha-filament-ledger's *instead of guesswork* is the *what handles the stale constraint* (the ledger is the source of truth, the sensor panel is the derived view; the stale constraint is the *mutable counter alternative*).
- **Feature 141 krineia-five-invariants** — the *proof/record distinction*. Ha-filament-ledger's *append-only ledger* is the *record*; feature 141's invariants are the *proof*.
- **Feature 145 garde-fous-frozen-mandate-append-only-agent-loop** — the *frozen mandate* primitive. Ha-filament-ledger's *Home Assistant config flow* is the *frozen mandate* (the config is frozen at integration install time); the mandate is what the integration holds fixed.
- **Feature 146 slashbooks-ai-bookkeeper-quickbooks-replacement-cross-section** — the *JTBD framing*. Ha-filament-ledger is the *user-facing-deployable-integration JTBD*; feature 146 is the *bookkeeping JTBD*.
- **Feature 147 reliability-lives-in-institution-not-cognition-2609-03192v1** — the *experimental test* of the architecture. Ha-filament-ledger is the *informal* statement; feature 147 is the *experimental* test of the operational invariants.
- **Feature 148 coxswain-graphs-harness-owns-consequence-architecture-pattern** — the *one harness owns every consequence* pattern. Ha-filament-ledger's *Home Assistant custom integration* is the *one harness* (one integration owns the consequence of the filament quantity); feature 148 is the *one place where consequence is owned*.
- **Feature 149 personal-agent-blueprint-telegram-chokepoint-architecture-pattern** — the *authorization chokepoint* pattern. Ha-filament-ledger's *Home Assistant config flow* is the *chokepoint* (the config flow is the one place where the user authorizes the integration); feature 149's *chokepoint* is the *enforcement of the authorization*.
- **Feature 153 sausageos-production-erp-append-only-stock-fefo-versioned-recipes** — the *production-ERP primitive set*. Ha-filament-ledger is the *user-facing-deployable-integration* primitive; feature 153 is the *production-ERP* primitive set.
- **Feature 154 chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive** — the *cryptographic-verifiability* primitive. Ha-filament-ledger is the *user-facing-deployable-integration* primitive; feature 154 is the *cryptographic-verifiability* primitive.

The 20 picks (this one + 19 prior) form the **deepest single-vocabulary cluster in the 40-pass series** for the *append-only-ledger + user-facing-deployable-integration + production-ERP + cryptographic-verifiability* architectural pattern. **All 20 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The v2 surface would require:

- A new *deployable-integration* surface (e.g. a Home Assistant custom component, a Telegram bot skill, a CLI tool, a webhook receiver).
- A new *exposed view* of `audit_logs` (or derived `StockEntry`) as a sensor / metric / event stream.
- A new *configuration surface* (the *frozen mandate* — what the integration is allowed to read/write).

None of these are v1; all are v2 surfaces that would require an *owner decision* per charter §3.2.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the ha-filament-ledger user-facing-deployable-integration pattern to `specs/2026-09-08-ha-filament-ledger-end-user-deployable-append-only-integration-pattern-HANDOFF.md`** as a named v2 primitive for the LE31 codebase — already done in the HANDOFF.md.
2. **Wait for the first v2 surface that requires a user-facing-deployable-integration** — trigger conditions: (a) first v2 PR that exposes `audit_logs` as a Home Assistant sensor; (b) first v2 PR that exposes `audit_logs` as a Telegram bot skill; (c) first v2 PR that exposes `audit_logs` as a webhook receiver; (d) first v2 PR that adds a CLI tool to query the ledger.
3. **On trigger, evaluate the change against the ha-filament-ledger pattern** — does the change preserve *append-only ledger*? Does the change preserve *instead of guesswork* discipline? Does the change expose the ledger as a *user-facing deployable integration*? Does the change use a *frozen mandate* (config flow)?
4. **Future v2 surface (NOT v1)**: the user-facing-deployable-integration primitive is a candidate v2 surface. Owner decision required: which deployable-integration surfaces, if any, should be added in v2?

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2 surface** (if the owner decides to add a user-facing-deployable-integration) would: (a) expose `audit_logs` (or a derived view of `StockEntry`) as a sensor / metric / event stream; (b) provide a configuration surface (the *frozen mandate*); (c) use a Home Assistant custom component, a Telegram bot skill, a CLI tool, or a webhook receiver as the deployment surface. This is a *v2 surface*, not v1.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2 surface dependencies** (if a user-facing-deployable-integration is added): a deployment surface (Home Assistant, Telegram bot skill, CLI tool, webhook receiver), a configuration surface (the *frozen mandate*), an exposure surface (sensor / metric / event stream). All future; no v1 dependency.

## Open questions

1. **Which user-facing-deployable-integration surface, if any, should LE31 v2 add?** Owner decision required. The most operationally valuable is probably a *Telegram bot skill* (the cook already uses Telegram; a bot skill would expose `audit_logs` directly in the cook's workflow); the most technically valuable is probably a *webhook receiver* (a generic surface that any external system can subscribe to). The cost in v1 today is *none* (the cook Telegram bot is already a user-facing surface; a *deployable-integration* is a *v2 expansion* of the surface).
2. **Is the ha-filament-ledger 36-day-old 0★/0⑂ repo a credible user-facing-deployable-integration data point?** Charter §3.2: stars are popularity proxy, not gate. The *pattern* is the value, not the maintainer's track record. The 2666 B description is tight; the topic tags are credible (`3d-printing`, `filament`, `bambulab`, `ams`, `hacs` — all real Home Assistant ecosystem primitives). **The pattern is transferable; the codebase is not adoptable**.
3. **Is the ha-filament-ledger Home Assistant stack a blocking factor?** Stack mismatch (Home Assistant vs FastAPI) is the primary reason for the *no code adoption* decision. The *pattern* is portable; the *code* is not. If LE31 ever needs the ha-filament-ledger primitives in code, they would be *re-implemented* on the LE31 stack (FastAPI + SQLModel + Postgres + aiogram), not imported from ha-filament-ledger.
4. **Should the LE31 v1 codebase add a *user-facing-deployable-integration* surface today?** Charter §3.2: only data needed for restaurant operations. The owner of a small restaurant uses the cook Telegram bot; the owner does not need a Home Assistant custom component today. Recommend: no, defer to v2 if/when the owner asks for a deployable-integration surface.

## Why this matters

**Ha-filament-ledger is the only end-user deployable append-only-ledger integration in the 30-repos cluster today.** The pattern's contribution is the *naming* of the *no-mutable-state* discipline as *"instead of guesswork"* — a rhetorical move that makes the discipline more accessible to non-technical stakeholders. The 2666 B README is a *ready-made* user-facing-deployable-integration pattern; the 36-day-old 0★ repo is a small-maintainer's first attempt at the pattern.

**The cluster (20 picks, this one + 19 prior) is the persistent cross-section reference for the next v2 architecture-review moment.** All 20 are `defer`; no code change today. The cluster is the *what the LE31 architecture is*, named across 20 different sources, and ready to be referenced when the first v2 user-facing-deployable-integration surface lands (Home Assistant sensor, Telegram bot skill, CLI tool, or webhook receiver).

**The most operationally valuable future v2 surface is a Telegram bot skill**: exposing `audit_logs` (or a derived view of `StockEntry`) as a Telegram bot skill would close the *user-facing-deployable-integration gap* (today, the cook Telegram bot is the only user-facing surface; a *bot skill* would allow other systems to subscribe to the audit log without a custom build). Owner decision required; not v1.