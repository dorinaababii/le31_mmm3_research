# Slice Handoff — Feature 340 (BUGGIEEEEE/worklog)

> **Feature ID**: 340
> **Feature path**: `/opt/data/le31_mmm3_research_work/features/340-BUGGIEEEEE-worklog-mit-shared-append-only-work-ledger-ai-coding-agents-cross-session-persistent-goal-context-end-of-turn-saves-hooks-v2-ai-shared-append-only-work-ledger-vocab.md`
> **Decision**: defer (parking-lot, vocabulary reference)
> **Bucket**: v2-AI

## LE31 feature gate verdict (carried from feature contract)

- **Evidence precondition**: inferred (vocabulary observation, not observed LE31 user pain). Confidence: medium.
- **Seven checks**:
  1. **JTBD**: When a v2-AI agent assists the owner/staff with a multi-step workflow, the operator wants the agent's goal/decisions/constraints persisted across compaction and new sessions via a shared append-only work ledger.
  2. **Viability**: high — the worklog vocabulary is the simplest of the 3 picks today; non-technical owner/staff could interpret the worklog with minimal assistance.
  3. **Practicability and confidence**: high — Python on-stack; the Claude-Code-/Codex-specific hook implementation is NOT portable to LE31; the *end-of-turn-save-enforcement* discipline IS portable (LE31 v2-AI would use a generic AI-agent-session-end detector).
  4. **Conflict**: no hard conflict with any charter invariant; the worklog is the AI-agent-context side of the charter §3.3 audit-log-immutability primitive.
  5. **Outcome / appetite / scope**: v2-AI outcome; 0 build time today; max 4 weeks per pick if a v2-AI window opens.
  6. **Cost to operational value**: medium RICE (this is the most directly transferable of the 3 picks); still not a v1 PR candidate.
  7. **Circuit breaker / reversibility**: fully reversible (vocabulary-only artifact; no code adoption).
- **Decision**: **defer (parking-lot, vocabulary reference)**.

## Files this slice will touch (when implemented)

> Not implemented today. When a v2-AI window opens, the implementation will touch:

- `app/v2/ai/worklog/__init__.py` — new package
- `app/v2/ai/worklog/models.py` — `WorklogEntry` (append-only) + `WorklogSession` + `WorklogHook` SQLModel tables
- `app/v2/ai/worklog/router.py` — FastAPI router under `/v2/ai/worklog` with append-only POST + read-only GET endpoints
- `app/v2/ai/worklog/templates/` — HTMX templates for the operator-facing worklog-read UI
- `app/v2/ai/worklog/session_end.py` — generic AI-agent-session-end detector (NOT Claude-Code-/Codex-specific) that fires the end-of-turn save
- `app/v2/ai/worklog/tests/` — verify the worklog rejects update + delete operations + the session-end detector fires the save
- `migrations/` — alembic migration for the new tables

> **Greenfield**: no existing v1 files are touched by this slice (LE31 v1 has no AI agent surface).
> **Generic detector (not Claude-Code-specific)**: the worklog vocabulary *enforces end-of-turn-save* via hooks; the Claude-Code-/Codex-specific hook implementation is NOT portable to LE31; LE31 v2-AI would build a generic AI-agent-session-end detector.

## Verification protocol (when implemented)

1. Run `pytest app/v2/ai/worklog/tests/` and verify all tests pass.
2. Manually POST a `WorklogEntry` via the FastAPI router; verify the entry is persisted + the append-only constraint is enforced.
3. Manually attempt to PUT (update) or DELETE a `WorklogEntry`; verify the router returns HTTP 405 Method Not Allowed (or equivalent rejection).
4. Manually trigger the `session_end` detector; verify a `WorklogEntry` is appended to the worklog.
5. Verify the HTMX worklog-read UI renders the entry list + the search-by-keyword endpoint returns matching entries.
6. Verify the integration with the v2-AI surface (if the v2-AI surface is already implemented).

## Rollback path

- `git revert <commit-hash>` to remove the v2-AI worklog surface.
- `alembic downgrade -1` to drop the new tables.
- No v1 data is affected (greenfield; no migration of existing v1 data).
- All `WorklogEntry` rows are append-only per charter §3.3; they remain in the audit trail even after the rollback.

## Mandatory LE31 skill list for the external coding agent

Before starting, the external coding agent MUST load these skills:

1. **`le31-conventions`** — the global LE31 decision layer + feature gate + hard invariants.
2. **`le31-v1-feature-pattern`** — the canonical contract shape + slicing rules + definition of done.
3. **`le31-handoff-spec`** — the handoff discipline + frozen contract + verification protocol.
4. **`le31-coding-agent-brief`** — the paste-in prompt template that produces the slice prompt from this HANDOFF.
5. **`le31-research`** — the research workflow + evidence-before-recommendation discipline.
6. **`development`** — the generic code-development pipeline (specify → plan → tasks → implement).

## Trigger policy for the external coding agent

- **DO NOT start** until a v2-AI workflow window opens in the LE31 charter roadmap.
- **DO NOT start** until a future v2-AI PR proposes a cross-session-persistent-goal-context surface, an end-of-turn-save-enforcement surface for AI-agent-sessions, a shared-append-only-work-ledger for AI-agent-context, or a hook-enforced-state-save discipline for AI-agent-actions.
- **DO NOT start** until the charter §3.4 AI-sandbox-as-auditable-test review has been completed.
- **DO NOT adopt** the Claude-Code-/Codex-specific hook implementation; LE31 v2-AI would build a generic AI-agent-session-end detector.
- When triggered, mirror back the frozen contract fields before implementing; stop if the mirror-back does not match.

## External-context Linear reference

- Parent research issue: Research 2026-10-18 — daily (Linear MCP BLOCKED 29th consecutive day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-18.linear-fallback.json` documents the intended parent + 3 sub-issues).
- This feature: Feature 340 — BUGGIEEEEE/worklog (intended sub-issue in `le31 Research` P-HMM-1).

## Sign-off gap

- External agent has NOT yet been dispatched.
- Charter §3.4 review has NOT yet been completed.
- v2-AI workflow window has NOT yet opened.
- No v1 PR today.

## Cross-references

- Feature contract: `/opt/data/le31_mmm3_research_work/features/340-...md`
- Source artifact: `/opt/data/le31-daily-research-2026-10-18.md` (pick C)
- Sister-shapes: features 316/322 (the-vibey-project/vibey, referenced by name as sister-shape: `BUGGIEEEEE/worklog` uses worklog-ledger not PostgreSQL), 187/188 (traust-security/traust-ledger), 232 (lpalbou/AbstractGateway), 287/288/289 (noise01/endoxa + pete-builds/mcp-nixreview + shivamk01here/LedgerLoop), 327 (musterhq/muster), 332/333/334/338/339 (the v2-AI agent-governance cluster).