# 167 — csakegyruszki provtrail hash-chained LLM source ledger HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/167-csakegyruszki-provtrail-hash-chained-llm-source-ledger.md` (defer artifact; **no code today**).

Bucket: **v2-AI architecture-reference (chain-of-custody + Claude Code + MCP primitive; charter §3.4 territory; staff-tooling, not customer-facing)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 surface proposes an LLM-assisted recommendation (e.g. *prep 12 pieces of cake tomorrow*), the owner wants *a chain-of-custody primitive that records which sources the AI consulted to make that recommendation*, but struggles because *LE31 v1 has no LLM integration and no audit-trail vocabulary for AI sources*, so that *the v2 surface can answer 'why did the AI suggest this?' with a chain-of-custody proof*." **PASS** (zero-pain today; v1 has no LLM integration; the JTBD is primitive documentation, not a build-need). |
| 2 | **Viability** | Owner can read the description (1-line)? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (provtrail is MIT Python + MCP JSON-RPC); no new permissions. Confidence medium-high for the primitive match (description + 7 topics align with chain-of-custody + Claude Code + MCP); low for transferability (LE31 v1 has no Claude Code integration). Practicability of adoption: medium-high — the chain-of-custody discipline is portable; the MCP integration is verifiable. §3.4 conflict: **provtrail is staff-tooling (Claude Code developer workflow), not customer-facing** — §3.4 not triggered. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The provtrail *chain-of-custody + hash-chained LLM source ledger* primitive *is* a v2 question, not a v1 question; it does not violate §3.1 (append-only posture is preserved — the chain is append-only hash-chained). §3.4 conflict is contingent on whether the LLM-assisted surface is staff-tooling (Claude Code developer workflow) or customer-facing (none currently planned); the *primitive itself* is staff-tooling. **PASS** (charter §3.1 invariant-compatible for v1; §3.4 contingent on future surface design). |
| 5 | **Outcome, appetite, scope** | v2-AI architecture-reference (chain-of-custody + Claude Code + MCP vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-line description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (1 line is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/167-csakegyruszki-provtrail-hash-chained-llm-source-ledger-HANDOFF.md` and `features/167-csakegyruszki-provtrail-hash-chained-llm-source-ledger.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section vocabulary for the next v2-AI question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an LLM-assisted surface — staff-tooling or customer-facing):

- `app/models/ai_source_ledger.py` — possibly add a SQLModel class for the AI source ledger (depends on the v2 change).
- `app/models/audit_log.py` — possibly add a `chain_head_hash` field (depends on the v2 change).
- `app/services/llm_provenance.py` — possibly add a chain-of-custody service that appends to `ai_source_ledger` on every LLM tool call (depends on the v2 change).
- `app/telegram/cook_bot.py` — possibly wire the MCP server registration so the cook Telegram bot records LLM sources (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/167-csakegyruszki-provtrail-hash-chained-llm-source-ledger.md` exists and is read back by the parent.
- [ ] `specs/167-csakegyruszki-provtrail-hash-chained-llm-source-ledger-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The provtrail description is quoted verbatim (1-line + 7 GitHub topics).
- [ ] The 0★/0⑂ + MIT + 2-day-old + Python + 169 KB stack-shape cluster is documented.
- [ ] The *chain-of-custody + Claude Code + MCP* primitives are documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an LLM-assisted surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The provtrail JTBD-validation set is evaluated against the PR's changes: does the change record which sources the AI consulted? Does the change preserve *append-only hash-chained* discipline? Does the change preserve *staff-tooling, not customer-facing* posture (charter §3.4)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `ai_source_ledger` table; remove the new `chain_head_hash` field from `audit_logs`; remove the new `llm_provenance` service; remove the MCP server registration from the cook Telegram bot.
- Migration cost: depends on the v2 change; the provtrail pattern's *chain-of-custody + Claude Code + MCP* implies *additive architecture* (the new layer is additive on top of the existing v1 surfaces — `audit_logs` append-only + StockEntry ledger).
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
| Feature ID | 167 |
| Slug | `csakegyruszki-provtrail-hash-chained-llm-source-ledger` |
| Bucket | v2-AI architecture-reference (chain-of-custody + Claude Code + MCP) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/ai_source_ledger.py` (possibly) + `app/models/audit_log.py` (possibly `chain_head_hash` field) + `app/services/llm_provenance.py` (possibly) + `app/telegram/cook_bot.py` (possibly MCP registration) |
| Trigger condition | First v2 PR that adds an LLM-assisted surface (staff-tooling OR customer-facing, the latter requires charter §3.4 owner decision) |
| Verification protocol | Does the change record which sources the AI consulted? Does it preserve *append-only hash-chained* discipline? Does it preserve *staff-tooling, not customer-facing* posture (charter §3.4)? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-237 (Research 2026-09-13 — daily) |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `csakegyruszki/provtrail` (MIT, 0★, Python, pushed 2026-09-12T10:00:09Z, created 2026-09-11) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds an LLM-assisted surface lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the *chain-of-custody + Claude Code + MCP* + *staff-tooling, not customer-facing* (charter §3.4) JTBD validation is the right architectural checklist (an owner decision).
