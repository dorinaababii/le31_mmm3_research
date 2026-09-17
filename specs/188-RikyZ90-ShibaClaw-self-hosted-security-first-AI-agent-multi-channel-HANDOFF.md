# 188 — RikyZ90/ShibaClaw self-hosted security-first AI agent multi-channel HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI control-plane surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/188-RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel.md` (defer artifact; **no code today**).

Bucket: **v2-AI (operator-AI control-plane, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces an AI-assisted operator surface, what architectural primitives does LE31 adopt?'*, the maintainer wants *evidence that another independent 2026 single-maintainer Python repo at 81★ is shipping exactly the primitives that LE31 v2 would need — self-hosted, security-first, 28-provider abstraction, 11-channel-delivery, 3-level-memory, MCP-server integration — without re-architecting the v1 StockEntry + audit_logs*, but struggles because *v1 has no AI agent surface and the no-cloud posture means any future AI agent must be explicitly security-first + multi-channel + 3-level-memory + MCP-integrated*, so that *v2 can introduce the AI-assist primitives with the cluster's vocabulary rather than inventing a new one*." **PASS** (zero-pain today; v1 has no AI-agent surface; the JTBD is primitive vocabulary extension, not a build-need). |
| 2 | **Viability** | Owner can read 55279 KB repo description + 10 topics? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the architectural vocabulary validation (81★/9⑂ is the new high-water mark for any v2-AI peer in 2026; Apache-2.0 + Python + 181-day-old + first in-window push today confirms real maintainer with sustained engagement; the topic set maps 1:1 onto charter §3.1 + §3.2 + §3.4). Stack: on-pattern (Python matches LE31; LiteLLM/MCP are v2-AI surface primitives, not v1 stack primitives). Practicability of adoption: medium — the *self-hosted + security-first + 3-level-memory + multi-channel-delivery + MCP* primitives can be extracted and re-implemented against LE31's StockEntry + audit_logs. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The ShibaClaw *self-hosted + security-first* posture is explicitly §3.1-aligned; §3.2 (Apache-2.0 = permissive); §3.4 (ShibaClaw is an operator-facing AI agent, not customer-facing — *security-first* posture explicitly excludes guest/user-facing surfaces). Charter §3.4 compatible. **PASS** (charter §3.1 + §3.2 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI control-plane (cross-section architectural vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 55279 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (55279 KB is already substantial; only the *self-hosted + security-first + 3-level-memory + multi-channel + MCP* topic set + description need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/188-RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel-HANDOFF.md` and `features/188-RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + charter §3.1 + §3.2 + §3.4 triple-invariant validation for the next v2-AI control-plane question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an AI-agent surface, a self-hosted + security-first AI-agent control plane, a 3-level-memory subsystem, a multi-channel-delivery subsystem, or an MCP-server integration):

- `app/ai/control_plane.py` — possibly add an AI-agent control plane as a discrete subsystem (depends on the v2 change).
- `app/ai/memory/` — possibly add a 3-level-memory subsystem (level-1 = audit_logs, level-2 = StockEntry, level-3 = notes; depends on the v2 change).
- `app/ai/providers/` — possibly add a 28-provider abstraction layer (depends on the v2 change).
- `app/ai/channels/` — possibly add a multi-channel-delivery subsystem (Telegram + web + voice + email + SMS + ...; depends on the v2 change).
- `app/ai/security/` — possibly add an explicit security-first posture (threat-model documentation, sandbox boundary, supply-chain audit; depends on the v2 change).
- `app/ai/mcp/` — possibly add an MCP-server integration (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/188-RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel.md` exists and is read back by the parent.
- [ ] `specs/188-RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The ShibaClaw description is quoted verbatim (55279 KB repo).
- [ ] The 81★/9⑂ + Apache-2.0 + 181-day-old + Python + first-in-window-push-today + *self-hosted + security-first + 3-level-memory + multi-channel + MCP* topic set is documented.
- [ ] The charter §3.1 + §3.2 + §3.4 triple-invariant validation is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an AI-agent surface, a self-hosted + security-first AI-agent control plane, a 3-level-memory subsystem, a multi-channel-delivery subsystem, or an MCP-server integration lands):**
- [ ] The PR is read back by the parent.
- [ ] The ShibaClaw architectural-vocabulary set is evaluated against the PR's changes: does the change address the *self-hosted + security-first + 3-level-memory + multi-channel + MCP* vocabulary? Does the change address the charter §3.1 + §3.2 + §3.4 triple-invariant? Does the change preserve the *no-cloud + permissive-license + non-customer-facing-AI* posture?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new AI-agent control plane; remove the new 3-level-memory subsystem; remove the new 28-provider abstraction layer; remove the new multi-channel-delivery subsystem; remove the new explicit security-first posture; remove the new MCP-server integration; restore the original `audit_logs` + `StockEntry` + `notes` schemas.
- Migration cost: depends on the v2 change; the ShibaClaw pattern's *self-hosted + security-first + 3-level-memory + multi-channel + MCP* implies *additive architecture* (the new control plane is additive on top of the existing v1 surfaces — FastAPI routes + aiogram handlers + `audit_logs` writer all live in one Python process today; the new control plane adds a discrete subsystem layer).
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
| Active feature path | `features/188-RikyZ90-ShibaClaw-self-hosted-security-first-AI-agent-multi-channel.md` |
| Bucket | v2-AI (operator-AI control-plane, parking-lot defer) |
| Build verdict | **`defer`** (charter §3.1 + `le31-conventions` Feature gate) |
| Parent research issue | HMM-270 (Brainstorm 2026-09-17 — daily) |
| GitHub URL | https://github.com/RikyZ90/ShibaClaw |
| License | Apache-2.0 ✓ |
| Stars / forks | 81★ / 9⑂ (highest in-window star count of any 2026-09-17 net-new candidate) |
| Pushed at / created at | 2026-09-17T04:55:23Z / 2026-03-20T00:26:05Z |
| Files to touch today | NONE (defer artifact, documentation only) |
| Verification protocol | `le31-verification-protocol/SKILL.md` + `le31-conventions` §Definition of done |
| Rollback path | Delete `features/188-...md` + `specs/188-...-HANDOFF.md` (trivially reversible) |
| Mandatory skills | le31-conventions + le31-v1-feature-pattern + le31-handoff-spec + le31-conventions-coder + le31-arch-patterns + le31-data-correctness + le31-quality-gates |

**Mirror-back required**: the external agent must echo this frozen contract (Section 1 + 2 + 3 + 4 + 5 + 6) back before implementing and stop if it cannot.
