# Feature 316 — `the-vibey-project-vibey-mit-ai-coding-agents-orchestrator-append-only-postgresql-ledger-crash-safe-resumable-v2-ai-agent-orchestration-vocabulary` (defer)

> **NEW observation (2026-10-15).** Documents 10-13 daily-research PICK C carry-over (was promised in 2026-10-13 report's INDEX-narrative truth but the actual feature file was never written; today's pass closes the INDEX-vs-on-disk gap). GitHub `the-vibey-project/vibey` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **3★/1⑂**, language Python ✓ ON-STACK, **pushed 2026-10-13T03:34:22Z = TODAY-PUSHED when first reported** (today-pushed AGAIN on 2026-10-15 = 2nd-day in-window push), **created 2026-08-14T...** = ~2-month-old repo with in-window push, **45086 KB substantial = 2nd-largest in-window v2-AI orchestrator of the 75-pass series**, `default_branch=main`, archived=`False`). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-15): *"Open-source orchestrator for AI coding agents: a spec interview, unattended builds on local (Ollama) or paid agents, human-gated review, and an append-only PostgreSQL ledger so a crashed agent's work is picked up, not lost."* Topics (verbatim, parent-verified, **20 topics**): `agent-orchestration, ai-agents, audit-log, autonomous-agents, autonomous-software-delivery, claude-code, cli, coding-agents, devsecops, event-sourcing, human-in-the-loop, job-queue, local-llm, ollama, postgresql, sovereign-ai, supply-chain-security, workload-identity` (listed 17 in 20-entry array). Bucket: **v2-AI (agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger-vocabulary)** — Pick C of Daily Research 2026-10-13 carry-over. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`open-source-orchestrator-for-AI-coding-agents + spec-interview + unattended-builds-on-local-Ollama-or-paid-agents + human-gated-review + append-only-PostgreSQL-ledger + crashed-agent's-work-is-picked-up-not-lost + 20-topic topic-array`** 7-tuple-primitive as a persistent cross-section reference for the LE31 v2-AI *agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger* wedge, and document the **stack-shape validation** that an independent maintainer arrived at in 2026 (~2-month-old repo). The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`open-source-orchestrator-for-AI-coding-agents + spec-interview + unattended-builds-on-local-Ollama-or-paid-agents + human-gated-review + append-only-PostgreSQL-ledger + crashed-agent's-work-is-picked-up-not-lost + 20-topic topic-array`** 7-tuple-primitive.
- A written record of the **Python + PostgreSQL = 2/2 LE31-backend-stack-match** = the strongest in-window 2026 v2-AI agent-orchestrator-with-crash-safe-append-only-PostgreSQL-ledger peer of the 75-pass series.
- A written record of the **20 topics = most topic-rich v2-AI orchestrator of the 75-pass series (tied with `djust-org/djust` at 20-topic threshold)**.
- A written record of the **append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive** = the unique append-only-PostgreSQL-ledger + crashed-agent-resumable v2-AI orchestrator primitive.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Adoption of `the-vibey-project/vibey` codebase (single-author 3★ v2-AI polish surface; LE31 v1 has no AI-orchestration surface today; v2-AI is undefined per charter §3.4).
- Cross-pollination with the v1 charter §3.4 customer-facing-AI posture (the *AI-coding-agents-orchestrator* surface is operator-tooling, not customer-facing; the *human-gated-review* posture IS the §3.4 invariant).

## Description

GitHub `the-vibey-project/vibey` (MIT, 3★/1⑂, Python, pushed 2026-10-13T03:34:22Z (10-13) + 2026-10-15 (today-pushed again, 2nd-day in-window), created ~2026-08-14 = ~2-month-old repo with in-window push, 45086 KB substantial, default_branch=`main`, archived=`False`).

The architectural primitive has multiple sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **Open-source orchestrator for AI coding agents** — the *AI-agent-orchestrator primitive* for the *coding-agents* dimension.
2. **A spec interview** — the *spec-interview primitive* that captures the user's intent before any agent action.
3. **Unattended builds on local (Ollama) or paid agents** — the *local-first + paid-fallback* primitive for AI-coding-agents.
4. **Human-gated review** — the *human-gate primitive* that requires an explicit user-action before any agent action is committed.
5. **Append-only PostgreSQL ledger** — the *append-only-PostgreSQL-ledger primitive* that records every agent action as an immutable append-only ledger entry.
6. **Crashed agent's work is picked up, not lost** — the *crash-safe-resumable primitive* that recovers crashed-agent partial work from the append-only PostgreSQL ledger.
7. **20 topics** = the most topic-rich v2-AI orchestrator of the 75-pass series including `agent-orchestration + ai-agents + audit-log + autonomous-agents + autonomous-software-delivery + claude-code + cli + coding-agents + devsecops + event-sourcing + human-in-the-loop + job-queue + llm + local-llm + ollama + postgresql + sovereign-ai + supply-chain-security + workload-identity`.

**The 1:1 mapping onto LE31 surface:**

| vibey-primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| open-source-orchestrator-for-AI-coding-agents | (LE31 v1 has no AI-orchestrator surface; the Hermes framework that runs the daily-research cron is an *orchestrator*) | §3.4 ✓ (cross-section) | **Not implemented** — v2-AI polish surface |
| spec-interview | (LE31 v1 has no spec-interview surface) | n/a | **Not implemented** — v2-AI polish surface |
| unattended-builds-on-local-Ollama-or-paid-agents | (LE31 v1 uses Hermes framework not Ollama) | n/a | **Not implemented** — v2-AI polish surface |
| human-gated-review | (LE31 v1 has explicit-state-transitions but no AI-human-gate) | §3.1 + §3.4 ✓ | **Not implemented** — v2-AI polish surface |
| append-only-PostgreSQL-ledger | (LE31 v1 has append-only `StockEntry` + `audit_logs` SQLModel tables) | §3.1 ✓ | **Implemented (v1)** — the *append-only* invariant is already in v1's SQLModel schema |
| crashed-agent-resumable | (LE31 v1 has no AI-orchestrator surface) | n/a | **Not implemented** — v2-AI polish surface |
| Python + PostgreSQL | (LE31 v1 uses Python + Postgres) | §3.1 ✓ | **Implemented (v1)** — the *stack-match* is on-§3.1 |
| 20 topics | (n/a — measure of topic-coverage not stack-shape) | n/a | Sister-shape |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2-AI PR that introduces a v2-AI agent-orchestrator surface for the LE31 single-restaurant Swiss kitchen), the implementation would add:

1. A new `AIAgentSession` SQLModel table (Alembic migration) with columns: `id` (UUID), `session_kind` (str enum: `prep-scheduling`, `menu-pricing`, `recipe-scaling`), `state` (str enum: `spec-interview`, `attended-build`, `human-gated-review`, `completed`, `crashed`), `created_at`, `updated_at`.
2. A new `AIAgentAction` SQLModel table (Alembic migration) with columns: `id` (UUID), `session_id` (UUID FK), `action_type` (str), `input_payload` (JSON), `output_payload` (JSON), `created_at` (timezone-aware).
3. A new `AIAgentSpecInterview` SQLModel table (Alembic migration) with columns: `id` (UUID), `session_id` (UUID FK), `question` (str), `answer` (str), `created_at`.
4. An Alembic migration that adds the new tables.
5. A `AIAgentOrchestrator` service that orchestrates AI-coding-agents via spec-interview + unattended-build + human-gated-review + append-only-PostgreSQL-ledger + crash-safe-resumable discipline.
6. A `AIAgentSpecInterviewService` service that captures the user's intent before any agent action.
8. An `AIAgentLedgerReplayer` service that replays the append-only-PostgreSQL-ledger for crashed-agent recovery.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires:

**For v2-AI agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger surface** (if approved):
1. Add new `AIAgentSession` SQLModel table (Alembic migration).
2. Add new `AIAgentAction` SQLModel table (Alembic migration).
3. Add new `AIAgentSpecInterview` SQLModel table (Alembic migration).
4. Add Alembic migration for the new tables.
5. Add a `AIAgentOrchestrator` service that orchestrates AI-coding-agents via the 5 primitives.
6. Add a `AIAgentSpecInterviewService` service that captures the user's intent.
7. Add an `AIAgentLedgerReplayer` service that replays the ledger for crashed-agent recovery.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

If the future v2-AI trigger fires, the v2-AI agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger surface would add **a v2-AI cook-Telegram-orchestrator primitive** (e.g., the cook Telegram bot subscribes to AIAgentAction events and receives formatted orchestrator-status messages). The cook-Telegram-orchestrator primitive would be a sister-shape to feature 39 (owner-daily-recap-telegram) + feature 16 (supplier-orders-bot) + feature 53/66 (offline-first).

## Dependencies

- **Stack**: Python 3.13, FastAPI, SQLModel, Postgres, aiogram v3 (LE31 v1 stack; `the-vibey-project/vibey` stack is Python + PostgreSQL + Ollama + Claude-Code which is on-§3.1).
- **External**: Ollama + Claude-Code (v2-AI polish; not required for v1).
- **Internal**: §3.1 (Python+Postgres+append-only-ledger on-§3.1); §3.2 (MIT permissive on-§3.2); §3.4 (operator-tooling + human-gate + non-AI-fallback on-§3.4).
- **Trigger dependency**: future v2-AI PR that adds an AI-orchestrator surface with crash-safe append-only-PostgreSQL-ledger recovery.

## Open questions

- **Q1**: When (if ever) will LE31 introduce a v2-AI agent-orchestrator surface? The v1 charter explicitly uses waiter web UI + cook Telegram bot + owner-daily-recap; the AI-orchestrator primitive is a v2-AI polish surface.
- **Q2**: If the v2-AI agent-orchestrator surface lands, will it use `the-vibey-project/vibey` or `djust-org/djust` = features 35+86+158+222+230+232+260+261+286 or hand-rolled? The `the-vibey-project/vibey` approach is the *append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review* primitive.
- **Q3**: Will the *append-only-PostgreSQL-ledger* posture align with LE31 v1's existing `audit_logs` schema? The *append-only-PostgreSQL-ledger* posture IS the *every-agent-action-is-an-append-only-audit-log-entry* invariant applied to the *AI-orchestrator* dimension.
- **Q4**: How will the *crashed-agent-resumable* posture interact with LE31 v1's existing schema? The *crashed-agent-resumable* posture IS the *crashed-agent's-partial-work-survives-across-agent-session-boundaries* invariant applied to the *AI-orchestrator* dimension.

## Why this matters

The **`open-source-orchestrator-for-AI-coding-agents + spec-interview + unattended-builds-on-local-Ollama-or-paid-agents + human-gated-review + append-only-PostgreSQL-ledger + crashed-agent's-work-is-picked-up-not-lost + 20-topic topic-array`** 7-tuple-primitive is the **strongest direct LE31 v2-AI agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger peer of the 75-pass series** for three reasons:

1. **The Python + PostgreSQL = 2/2 LE31-backend-stack-match is the canonical v2-AI orchestrator stack**: when LE31 v2-AI introduces an agent-orchestrator surface (e.g., a v2-AI surface that orchestrates AI-coding-agents for prep-scheduling or menu-pricing), the Python + PostgreSQL substrate is the existing v1 stack.
2. **The append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive is the unique v2-AI orchestrator discipline of the 75-pass series**: sister-shape `djust-org/djust` uses local-filesystem + `BUGGIEEEEE/worklog` uses worklog-ledger not PostgreSQL + `warrant-ai/warrant` uses decision-ledger not PostgreSQL.
3. **The 20-topic topic-array is the most topic-rich v2-AI orchestrator of the 75-pass series**: the *agent-orchestration + ai-agents + audit-log + autonomous-agents + autonomous-software-delivery + claude-code + cli + coding-agents + devsecops + event-sourcing + human-in-the-loop + job-queue + llm + local-llm + ollama + postgresql + sovereign-ai + supply-chain-security + workload-identity* nonuple-primitive is the strongest v2-AI orchestrator topic-coverage of the cluster.

Sister-shape to features 35+86+158+222+230+232+260+261+286 (`djust-org/djust` AI-coding-agent-orchestrator family) + 287 (`noise01/endoxa` governed-beliefs + SMT) + 288 (`pete-builds/mcp-nixreview` MCP-server-+-CVE-attestation) + 289 (`shivamk01here/LedgerLoop` financial-AI-agent-runtime + exactly-once-execution). The `the-vibey-project/vibey` pattern is the **strongest direct append-only-PostgreSQL-ledger + crashed-agent-resumable v2-AI orchestrator primitive** of the cluster.

The trigger condition for this defer artifact to become a build is: first v2-AI PR that adds a v2-AI agent-orchestrator-with-crash-safe-append-only-PostgreSQL-ledger recovery surface.

**Fully reversible** (vocabulary-only artifact). No code today.

---

## Cross-section references

- `features/35-djust-org-djust-…md` + 86 + 158 + 222 + 230 + 232 + 260 + 261 + 286 — `djust-org/djust` AI-coding-agent-orchestrator family (sister-shape)
- `features/287-noise01-endoxa-…md` — governed-beliefs + SMT (sister-shape)
- `features/288-pete-builds-mcp-nixreview-…md` — MCP-server + CVE-attestation (sister-shape)
- `features/289-shivamk01here-LedgerLoop-…md` — financial-AI-agent-runtime + exactly-once-execution (sister-shape)
- `features/302-warrant-ai-warrant-…md` — decision-ledger (sister-shape)

---

**Parent research issue**: [linear: blocked] (parent fallback at `/opt/data/le31-daily-research-2026-10-15.linear-fallback.json`). Original Daily Research issue: 2026-10-13 PICK C carry-over.