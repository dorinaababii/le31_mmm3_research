# 191 — eddierzhang/FullHouse-Updated FastAPI + audit-log + AI-agents-manager-decides HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI owner-assist surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/191-eddierzhang-FullHouse-Updated-mit-fastapi-audit-log-ai-agents-manager-decides-v2-ai-owner-assist.md` (defer artifact; **no code today**).

Bucket: **v2-AI (owner-assist, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces an AI-assisted operator surface, what is the charter §3.4 invariant pattern that prevents the AI from acting autonomously?'*, the maintainer wants *evidence that another independent 2026 Python repo at 7002 KB with FastAPI + audit-log + AI-agents + Docker is shipping exactly the AI-proposes-manager-decides discipline*, but struggles because *v1 has no AI-assist surface and the charter §3.4 invariant is not yet operationalized in code*, so that *v2 can introduce the AI-assisted operator surface with the explicit charter §3.4 invariant rather than inventing a new one*." **PASS** (zero-pain today; v1 has no AI-assist surface; the JTBD is primitive vocabulary extension + charter §3.4 invariant documentation, not a build-need). |
| 2 | **Viability** | Owner can read 7002 KB repo description + 6 topics? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (Python + FastAPI + audit-log already in v1 stack). Confidence: high for the architectural vocabulary validation (MIT + Python + 7002 KB substantial repo + in-window push 3-days-ago + the `audit-log + fastapi` topic pair directly maps onto LE31's `audit_logs` + FastAPI; the *AI-proposes-manager-decides* discipline is explicitly named in the description). Stack: on-pattern for v1 primitives (FastAPI + audit-log match LE31 exactly); off-pattern for v2 primitives (Anthropic + AI-agents are v2-AI surface only). Practicability of adoption: medium — the *AI-proposes-manager-decides* primitive can be extracted and re-implemented against LE31's StockEntry + audit_logs. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The `audit-log + fastapi` topic pair directly maps onto LE31's existing `audit_logs` SQLModel table + FastAPI backend (charter §3.1 alignment); §3.2 (MIT = permissive); §3.4 (the *manager decides* framing is the explicit charter §3.4 compliance pattern: AI proposes + observable evidence + non-AI fallback). Charter §3.4 explicitly validated. **PASS** (charter §3.1 + §3.2 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI owner-assist (cross-section architectural vocabulary + charter §3.4 invariant documentation); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 7002 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (7002 KB is already substantial; only the *AI-proposes-manager-decides* + description need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/191-eddierzhang-FullHouse-Updated-mit-fastapi-audit-log-ai-agents-manager-decides-v2-ai-owner-assist-HANDOFF.md` and `features/191-eddierzhang-FullHouse-Updated-mit-fastapi-audit-log-ai-agents-manager-decides-v2-ai-owner-assist.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + charter §3.4 invariant documentation for the next v2-AI owner-assist question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an AI-assisted operator surface, an *AI-proposes-manager-decides* discipline, an Anthropic integration, or an AI-agents surface):

- `app/ai/propose.py` — possibly add an *AI-proposes* module (the AI generates a proposal + a reasoning trace; depends on the v2 change).
- `app/ai/approve.py` — possibly add a *manager-decides* module (the manager sees the proposal + the reasoning trace + approves/rejects; depends on the v2 change).
- `app/ai/audit_log_extension.py` — possibly add a `proposal_id` column + a `manager_decision` column to `audit_logs` (charter §3.1 alignment via the new audit-trail entries for proposal + decision; depends on the v2 change).
- `app/ai/integrations/anthropic.py` — possibly add an Anthropic API integration (the AI provider; depends on the v2 change).
- `app/ai/integrations/mcp.py` — possibly add an MCP-server integration for the AI-agents surface (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/191-eddierzhang-FullHouse-Updated-mit-fastapi-audit-log-ai-agents-manager-decides-v2-ai-owner-assist.md` exists and is read back by the parent.
- [ ] `specs/191-eddierzhang-FullHouse-Updated-mit-fastapi-audit-log-ai-agents-manager-decides-v2-ai-owner-assist-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `FullHouse-Updated` description is quoted verbatim (7002 KB repo).
- [ ] The 0★/0⑂ + MIT + Python + in-window push 3-days-ago + `audit-log + fastapi` stack mirror with LE31 v1 + *AI-proposes-manager-decides* charter §3.4 explicit-compliance discipline is documented.
- [ ] The charter §3.4 alignment via explicit *manager decides* veto point is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an AI-assisted operator surface, an *AI-proposes-manager-decides* discipline, an Anthropic integration, or an AI-agents surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `FullHouse-Updated` architectural-vocabulary set is evaluated against the PR's changes: does the change address the *AI-proposes-manager-decides* discipline? Does the change enforce the *manager decides* veto point (charter §3.4 alignment)? Does the change preserve the *audit-log + fastapi* stack mirror with LE31 v1?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `propose.py` + `approve.py` modules; remove the new `audit_log_extension.py` schema change; remove the new Anthropic + MCP integrations; restore the original `audit_logs` + `StockEntry` schemas.
- Migration cost: depends on the v2 change; the `FullHouse-Updated` pattern's *AI-proposes-manager-decides + audit-log + fastapi* implies *additive architecture* (the new AI-assisted operator surface is additive on top of the existing v1 surfaces — FastAPI routes + aiogram handlers + `audit_logs` writer all live in one Python process today; the new AI surface adds a discrete layer with the propose-then-decide discipline).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.
