# 203 — shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/203-shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane.md` (defer artifact; **no code today**).

Bucket: **v2-AI control-plane (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + §3.4 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce an AI-assisted workflow (e.g., LLM-suggested documentation lookup, LLM-suggested menu translation), the owner wants *an operator-tooling surface with audit-trail and non-AI fallback*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant)*, so that *v2 can offer AI assistance without violating §3.4*." **PASS** (zero-pain today; v1 is small enough that operator-tooling without AI is sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium for the architectural match (the *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* primitive set is well-established in the GitHub 1★-community-adoption cluster; membro's 10-topic coverage including `fastapi` confirms a real implementation, not just a proposal). MIT license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; operator-tooling with observable evidence + non-AI fallback; no customer-facing AI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI control-plane (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/203-shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane-HANDOFF.md` and `features/203-shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2-AI trigger condition fires (first v2-AI PR that introduces an AI-assisted workflow with operator-tooling + non-AI-fallback + audit-trail):

- `app/models/ai_assistance_log.py` — possibly add an `ai_assistance_log` SQLModel table (interaction_id, actor_user_id, model_version, prompt, response, recorded_at, evidence_id FK, extraction_status).
- `app/models/evidence.py` — possibly add an `Evidence` SQLModel table (id, kind, url_or_path, captured_at, captured_by_user_id).
- `app/models/audit_log.py` — possibly add an optional `evidence_id` FK column to `audit_logs` (nullable; existing rows remain evidence-less).
- `app/mcp_le31_server.py` — possibly add a `mcp_le31_server` FastAPI sub-app that exposes `audit_logs` + `ai_assistance_log` as MCP tools.
- `app/policy/deterministic_extraction_wall.py` — possibly add a `deterministic_extraction_wall` policy primitive (charter §3.4: non-AI-fallback required; AI-extracted facts that fail the deterministic-extraction-wall must be flagged-for-review, not persisted to the ledger).
- `app/bot/ai_summary.py` — possibly add a Telegram-bot command for the owner to view an *AI-assistance summary* (e.g., `/ai-summary today`).
- `app/bot/ai_wall_status.py` — possibly add a Telegram-bot command for the cook to view the *AI-extraction-wall status* (e.g., `/ai-wall status`).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [x] `features/203-shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane.md` exists and is read back by the parent.
- [x] `specs/203-shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane-HANDOFF.md` (this file) exists and is read back by the parent.
- [x] The GitHub repo description is quoted verbatim: *"Local-first memory for AI assistants: append-only fact ledger behind deterministic extraction walls, immutable transcripts, provenance-carrying summaries, MCP tools. Loopback-only by default."*
- [x] The MIT permissive license is documented.
- [x] The *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* quintuple-primitive set is documented.
- [x] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/` + INDEX.md row + parent research report file.

**Future v2-AI trigger (when the first v2-AI PR that introduces an AI-assisted workflow lands):**
- [ ] The PR is read back by the parent.
- [ ] The *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* primitive set is evaluated against the PR's changes: does the change preserve *append-only posture*? Does the change add *deterministic-extraction-wall*? Does the change add *provenance-carrying*? Does the change add *MCP tools integration*? Does the change add *loopback-only by default*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2-AI surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `ai_assistance_log` table; remove the new `Evidence` table; remove the new `evidence_id` FK column from `audit_logs`; remove the new `mcp_le32_server.py` sub-app; remove the new `deterministic_extraction_wall` policy; restore the original `audit_logs` schema.
- Migration cost: depends on the v2-AI change; the *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* primitive set's design implies *additive schema* (the new `ai_assistance_log` + `Evidence` tables are additive on top of the existing append-only log).
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

## 7. Handoff summary

| Field | Value |
|---|---|
| Feature ID | 203 |
| Slug | `shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane` |
| Bucket | v2-AI control-plane (architecture-reference, parking-lot defer) |
| Parent research issue | linear: blocked (workspace plan limit; see /opt/data/le31-daily-research-2026-09-20.linear-fallback.json); intended title `Research 2026-09-20 — daily` |
| Linear sub-issue | linear: blocked (workspace plan limit); intended title `Feature 203 — shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane` |
| Status today | defer (parking-lot) |
| No code today | yes |
| Verifiability today | feature file + HANDOFF file + INDEX.md row + parent research report file |
| Trigger condition (future v2-AI) | first v2-AI PR that introduces an AI-assisted workflow with operator-tooling + non-AI-fallback + audit-trail |
| Disable path | delete `features/203-...md` + `specs/203-...-HANDOFF.md` |
| Migration cost | additive schema only (depends on v2-AI change) |
| Retained data | none |
| Parent research report | `/opt/data/le31-daily-research-2026-09-20.md` (52nd consecutive daily-research pass) |
| Raw fetches path | `/tmp/le31-daily-2026-09-20/` (68 files; anti-fabrication canary 0/67) |
| Linear fallback path | `/opt/data/le31-daily-research-2026-09-20.linear-fallback.json` |
| License | MIT ✓ (charter §3.2 compatible) |
| GitHub repo | `shawn-durrani/membro` (1star/0forks, Python, 797 KB, pushed 2026-09-17T09:34:34Z) |
| Topics (verbatim) | `ai`, `ai-memory`, `fastapi`, `llm`, `local-first`, `mcp`, `mcp-server`, `memory`, `self-hosted`, `sqlite` (10 topics) |
| Description (verbatim) | *"Local-first memory for AI assistants: append-only fact ledger behind deterministic extraction walls, immutable transcripts, provenance-carrying summaries, MCP tools. Loopback-only by default."* |
| LE31-shape-score | 3 (`fastapi` topic + description *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default*) |
| Companion artifacts | features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 204 (sister-pick B), 205 (sister-pick C) (ripgrep-verified distinct) |
| Sister-picks from 2026-09-20 | feature 204 (docentesIA/dagwell v2-AI orchestration), feature 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference) |

## 8. Verification log

*(Empty — to be populated by the parent if/when the future v2-AI trigger condition fires.)*

---

**OPERATOR NOTE (2026-09-20):** Today's Linear MCP write endpoint returned a workspace plan-limit error (`You've exceeded the free issue limit for this workspace` — carry-over from 2026-09-19); per `le31-daily-research/SKILL.md` hard rule, the parent research issue + the 3 Linear sub-issues were NOT created today. The fallback JSON at `/opt/data/le31-daily-research-2026-09-20.linear-fallback.json` documents the intended issues for resync after the workspace quota resets. The feature files + HANDOFFs were written to the repo regardless, per spec hard rule *"treat the report file as the source of truth; the Linear issue is the index"*.