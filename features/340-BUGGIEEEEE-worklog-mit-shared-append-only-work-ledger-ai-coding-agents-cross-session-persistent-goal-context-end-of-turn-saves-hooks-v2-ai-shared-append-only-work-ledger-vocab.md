# Feature 340 — BUGGIEEEEE/worklog (v2-AI shared-append-only-work-ledger-for-AI-coding-agents-+-cross-session-persistent-goal-context-+-end-of-turn-save-enforcement-via-hooks)

> **Bucket**: v2-AI (parking-lot, vocabulary reference)
> **GitHub**: https://github.com/BUGGIEEEEE/worklog
> **License**: MIT
> **Status (as of 2026-10-18)**: ★3 / ⑂1; 4508 KB modest; pushed 2026-10-16T04:42:54Z (in-window by `pushed_at`); created 2026-10-06T09:42:04Z (~12 days old); default_branch=master; archived=False
> **Topics (verbatim, 0)**: `[]` (no GitHub topics; empty array)
> **Description (verbatim)**: *Shared append-only work ledger for AI coding agents (Claude Code, Codex): keeps goal/decisions/constraints across compaction and new sessions, enforces end-of-turn saves with hooks.*
> **Cross-section**: features 187/188 (traust-security/traust-ledger, the persistent AI-agent-audit-ledger vocabulary reference), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 316/322 (the-vibey-project/vibey, referenced by name as sister-shape: `BUGGIEEEEE/worklog` uses worklog-ledger not PostgreSQL), 327 (musterhq/muster), 332/333/334/338/339 (the v2-AI agent-governance cluster)
> **Decision**: defer (parking-lot, vocabulary reference)
> **Parent research issue**: Research 2026-10-18 — daily (Linear MCP blocked; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-18.linear-fallback.json`)
> **Slice handoff**: `/opt/data/le31_mmm3_research_work/specs/340-BUGGIEEEEE-worklog-mit-shared-append-only-work-ledger-ai-coding-agents-cross-session-persistent-goal-context-end-of-turn-saves-hooks-HANDOFF.md`

## Goal

When a future v2-AI LE31 workflow introduces AI-assisted features for the owner/staff, the system wants every AI coding agent to write its **goal/decisions/constraints** to a **shared append-only work ledger** at **end-of-turn**, so that the context is preserved across compaction and new sessions, but today AI agents lose their context on session boundaries and on compaction, so that the operator cannot reconstruct what the agent was trying to do or why it made specific decisions.

## Evidence / JTBD

**Inferred** (vocabulary observation, not observed LE31 user pain). The pain is *possible* in any future v2-AI workflow window but is not *directly observed* in any LE31 v1 user flow today.

When a v2-AI agent assists the owner/staff with a multi-step workflow, the operator wants every agent action to be **bounded by acceptance criteria** (Pick A: haiplane), **governed by a persona-charter** (Pick B: barony), and **logged in a shared append-only work ledger** (Pick C: worklog), but struggles because today AI agents operate without explicit acceptance gates, without persona-charters, and without cross-session-persistent-context, so that the workflow audit trail is incomplete and the operator cannot reconstruct what the agent did or why.

Confidence: **medium** (the maintainer is shipping real code = the primitive is working for at least one user; the worklog is the simplest of the 3 picks today; the vocabularies are transferable to a Python+FastAPI+Postgres+SQLModel+aiogram v3 stack with a charter §3.4 review).

## Scope

- v2-AI only: applies to a future v2-AI workflow window (operator + staff tooling, not customer-facing).
- The transferable vocabulary is the **shared-append-only-work-ledger + cross-session-persistent-goal-context + end-of-turn-save-enforcement-via-hooks** triple-primitive.
- The Python stack is portable to LE31 v2-AI with a charter §3.4 review (AI-sandbox-as-auditable-test + non-AI-fallback + observable-evidence).
- No v1 PR today; no v1 build today; no quota-filling.

## Out of scope

- v1 product surface (waiter web UI + cook Telegram bot). LE31 v1 has no AI agent surface.
- Any customer-facing AI per charter §3.4 (the worklog vocabulary is operator-tooling only).
- Any runtime import of worklog as a dependency (the worklog codebase is the vocabulary reference, not the code dependency).
- Any LE31-specific schema migration or model change (worklog is vocabulary-only; the v2-AI surface is greenfield).
- The "end-of-turn-save-enforcement-via-hooks" implementation is specific to Claude Code + Codex hooks; LE31 v2-AI would adopt the *end-of-turn-save-enforcement* discipline without necessarily adopting the *Claude Code / Codex hooks* implementation (LE31 v2-AI would use a generic AI-agent-session-end detector).

## Description

The worklog vocabulary is the **shared-append-only-work-ledger-for-AI-coding-agents** triple-primitive:

1. **Shared append-only work ledger** — the worklog is a single shared file (typically `.worklog/worklog.md` or `.worklog/worklog.jsonl`) that every AI coding agent writes to. The ledger is append-only; entries cannot be edited or deleted. This is the **append-only-as-shared-state** discipline applied to AI-agent-context.
2. **Cross-session-persistent-goal-context** — the worklog preserves the agent's goal + decisions + constraints across compaction (when the LLM context window is summarized to fit) and across new sessions (when a new agent session starts). The worklog is the persistent context that survives compaction and new sessions. This is the **worklog-as-cross-session-memory** discipline.
3. **End-of-turn-save-enforcement-via-hooks** — the worklog enforces an end-of-turn save via hooks. When an AI coding agent (Claude Code, Codex) ends a turn, a hook fires that requires the agent to write its current goal + decisions + constraints to the worklog before the turn can complete. This is the **hook-enforced-end-of-turn-save** discipline.

The Python stack + the 3★ for a 4508 KB modest repo = a real working primitive that at least one user is depending on (Claude Code + Codex users).

## Data model

No LE31 schema change today. The worklog vocabulary is operator-tooling infrastructure that would be introduced in a future v2-AI window. The data model for a future worklog-style v2-AI work-ledger surface would be:

- `WorklogEntry` — id, session_id, agent_id, goal (TEXT), decisions (JSONB), constraints (JSONB), created_at, turn_index (append-only per charter §3.3)
- `WorklogSession` — id, agent_id, started_at, ended_at, parent_session_id (nullable, for compaction-and-restart), last_turn_index
- `WorklogHook` — id, agent_id, hook_type, hook_config (JSONB), enabled, created_at (the hook configuration that enforces the end-of-turn save)

The `WorklogEntry` is the **charter §3.3 audit-log-immutability** primitive applied to AI-agent-cross-session-context.

## Implementation steps

Not implemented today (parking-lot). When a v2-AI window opens, the implementation would be:

1. Add a `worklog_entries` SQLModel table with the schema above (append-only).
2. Add a FastAPI router under `/v2/ai/worklog` with append-only endpoints + read-only endpoints.
3. Add an HTMX template for the operator-facing worklog-read UI.
4. Add a generic AI-agent-session-end detector (not Claude-Code-specific) that fires the end-of-turn save.
5. Add an integration test that verifies the worklog rejects update + delete operations + the session-end detector fires the save.

## Telegram interaction

If a future v2-AI operator workflow adopts worklog vocabulary, the operator Telegram bot would gain:
- `/worklog` — show the most recent worklog entries
- `/worklog_session <session_id>` — show a specific session's worklog
- `/worklog_search <query>` — search the worklog for a keyword

The `/worklog_search` command enables the operator to **search the agent's cross-session context** without reading every worklog entry.

## Dependencies

- A future v2-AI window opening (no v1 PR today).
- Charter §3.4 review (AI-sandbox-as-auditable-test + non-AI-fallback + observable-evidence).
- The worklog codebase is the vocabulary reference; no runtime dependency on the worklog project itself.
- The generic AI-agent-session-end detector is a greenfield implementation; LE31 v2-AI would build this on Postgres + a periodic background task that watches the AI-agent session lifecycle.

## Open questions

- Is the LE31 v2-AI workflow window opening in 2026-Q4 or later? (parent has no visibility into the charter roadmap).
- Does a future v2-AI workflow actually need a shared-append-only-work-ledger, or is the existing v1 `audit_logs` append-only ledger sufficient for operator-side audit? (likely yes for any multi-agent workflow + any cross-session context need).
- Should the worklog vocabulary be combined with the haiplane vocabulary (Pick A) for acceptance-criteria-and-named-commit-on-shared-worklog, or should they be adopted independently? (likely independently first, then combined).
- How does worklog's append-only ledger interact with charter §3.3 audit-log-immutability? (they reinforce each other; the worklog is the AI-agent-context side of the audit-log-immutability primitive).
- How does worklog's cross-session-persistent-goal-context interact with the existing v1 `audit_logs`? (the worklog is the AI-agent-side; the audit_logs is the user-action side; they are complementary).

## Why this matters

The worklog vocabulary is the **canonical shared-append-only-work-ledger + cross-session-persistent-goal-context + end-of-turn-save-enforcement-via-hooks discipline** of the 79-pass series. It is the simplest of the 3 picks today and the one most directly transferable to LE31 v2-AI. The worklog is the **only of today's 3 picks** that directly addresses the AI-agent-context-loss-on-compaction problem, which is the dominant AI-agent-operational-pain of any multi-step workflow.

When a v2-AI window opens, the worklog vocabulary becomes the actionable cross-session-persistent-goal-context reference for any LE31 v2-AI workflow that needs to preserve AI-agent-context across compaction and new sessions.

Charter §3.4 alignment is strong: worklog enforces end-of-turn-save via hooks (chokepoint-governed) + requires goal/decisions/constraints to be human-readable (human-gate) + anchors every entry in an append-only ledger (observable-evidence) + has a non-AI-fallback (the operator can read the worklog without an AI agent).

Sister-shape cross-section: features 316/322 (the-vibey-project/vibey, referenced by name as sister-shape: `BUGGIEEEEE/worklog` uses worklog-ledger not PostgreSQL), 187/188 (traust-security/traust-ledger), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 327 (musterhq/muster), 332/333/334/338/339 (the v2-AI agent-governance cluster).

## Trigger condition

Re-evaluate when:
1. A v2-AI workflow window opens in the LE31 charter roadmap.
2. A future v2-AI PR proposes a cross-session-persistent-goal-context surface.
3. A future v2-AI PR proposes an end-of-turn-save-enforcement surface for AI-agent-sessions.
4. A future v2-AI PR proposes a shared-append-only-work-ledger for AI-agent-context.
5. A future v2-AI PR proposes a hook-enforced-state-save discipline for AI-agent-actions.

At that point, the worklog vocabulary becomes actionable for the LE31 v2-AI surface.