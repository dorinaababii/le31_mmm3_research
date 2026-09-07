# 2026-09-07 — `personal-agent-blueprint-telegram-chokepoint-architecture-pattern` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/149-personal-agent-blueprint-telegram-chokepoint-architecture-pattern.md` (defer artifact; **no code today**).

Bucket: **v1 architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 maintainer reads the cook Telegram bot, the owner wants *to know which subsystem owns the audit_logs row*, but struggles because *the codebase doesn't name the chokepoint*, so that *any future change to the bot can be evaluated against the chokepoint's invariants*." **PASS** (zero-pain today; the codebase is small; the chokepoint is implicit; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 76 B? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the architectural match (the four sub-primitives — multi-channel listeners / append-only event stream / authorization chokepoint / hash-chained audit ledger — map onto LE31's aiogram handler, audit_logs, cook's confirmation transition, and audit_logs respectively). **PASS**. |
| 4 | **Conflict** | None. The personal-agent-blueprint "append-only event stream" *is* the LE31 §3.1 *audit_logs* invariant; the "authorization chokepoint" *is* the LE31 §3.1 *operational transitions are explicit user actions* invariant. The "hash-chained audit ledger" is a *future* enhancement, not v1 (LE31 v1's `audit_logs` is *not* hash-chained today; the hash-chain is a v2 surface, not v1). **PASS** (charter §3.1 invariant-compatible; charter §3.2 not violated because hash-chaining is for audit, not for operations). |
| 5 | **Outcome, appetite, scope** | v1 architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 76 B description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (76 B is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-07-personal-agent-blueprint-telegram-chokepoint-architecture-pattern-HANDOFF.md` and `features/149-personal-agent-blueprint-telegram-chokepoint-architecture-pattern.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v1 architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v1 trigger condition fires (first v1 PR that touches the cook Telegram bot, the owner's approval flow, or the operational transitions):

- `app/bot/cook.py` — possibly add a new Telegram handler (depends on the v1 change).
- `app/state/transitions.py` — possibly add a new operational transition (depends on the v1 change).
- `app/audit/log.py` — possibly add a new audit event type (depends on the v1 change).

**Future v2 surface (NOT v1) — if the owner decides hash-chaining is worth the implementation cost:**
- `models/audit_log.py` — add a `previous_hash` column.
- `app/audit/log.py` — compute the hash on every `audit_logs` insert.
- `app/audit/verify.py` — **NEW** (verification query that detects chain breaks).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/149-personal-agent-blueprint-telegram-chokepoint-architecture-pattern.md` exists and is read back by the parent.
- [ ] `specs/2026-09-07-personal-agent-blueprint-telegram-chokepoint-architecture-pattern-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The personal-agent-blueprint description is quoted verbatim (76 B repo).
- [ ] The 1:1 mapping onto LE31 v1 architecture is documented.
- [ ] The "authorization chokepoint" is named as a discrete subsystem.
- [ ] The "hash-chained audit ledger" is documented as a *future* v2 surface, not v1.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v1 trigger (when the first v1 PR that touches the cook Telegram bot, the owner's approval flow, or the operational transitions):**
- [ ] The PR is read back by the parent.
- [ ] The chokepoint pattern is evaluated against the PR's changes: does the change preserve the chokepoint's authority? Does it introduce a *bypass* (a code path that performs the action without going through the chokepoint)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

**Future v2 trigger (if hash-chaining is added):**
- [ ] The hash function (sha256) is added to the dependencies.
- [ ] The `previous_hash` column is added to `audit_logs` with a migration.
- [ ] The verification query is added.
- [ ] A test verifies that tampering with one row invalidates the chain.
- [ ] The migration is reversible (charter §3.1: never update or delete ledger events; the `previous_hash` column is *additive* — it does not modify existing rows).

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v1 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new handler / transition / event type.
- Migration cost: depends on the v1 change; the chokepoint pattern's "authorization chokepoint" implies *no new migrations* (the chokepoint is a *naming*, not a new schema).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

**Future v2 surface (if hash-chaining is added):**
- Disable: set `audit_logs.hash_chain_enabled = false`; the hash computation is skipped.
- Delete: remove the `previous_hash` column; the column is *additive* (does not modify existing rows), so the migration is *reversible* (drop the column; existing rows are unchanged).
- Migration cost: low (one column add + one index on `previous_hash` if needed for verification queries).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `previous_hash` is *additive* (existing rows are unchanged).

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
| Feature ID | 149 |
| Slug | `personal-agent-blueprint-telegram-chokepoint-architecture-pattern` |
| Bucket | v1 architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on v1 trigger | `app/bot/cook.py` (possibly) + `app/state/transitions.py` (possibly) + `app/audit/log.py` (possibly) |
| Files to touch on v2 trigger (if hash-chaining) | `models/audit_log.py` + `app/audit/log.py` + `app/audit/verify.py` (NEW) |
| v1 trigger condition | First v1 PR that touches the cook Telegram bot, the owner's approval flow, or the operational transitions |
| v2 trigger condition | Owner decides hash-chaining is worth the implementation cost (charter §3.2 owner decision) |
| Verification protocol | v1: does the change preserve the chokepoint's authority? v2: tampering with one row invalidates the chain? |
| Rollback | Fully reversible (defer artifact is documentation only; v2 hash-chaining is *additive* — drop the column to revert) |
| Parent research issue | HMM-204 (Research 2026-09-07 — daily) |
| Linear sub-issue | HMM-207 (to be created) |
| Lead source | GitHub `arielhalevy123/personal-agent-blueprint` (MIT, 0★, pushed 2026-09-06T09:41:50Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v1 trigger sign-off gap** (when the first v1 PR that touches the cook Telegram bot lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the chokepoint pattern is the right architectural checklist (an owner decision).

**Future v2 trigger sign-off gap** (if hash-chaining is proposed): the operator must decide whether the LE31 threat model (accidental corruption, not malicious tampering) justifies the implementation cost (an owner decision per charter §3.2).

## 9. Verification log

*(Empty today. The first v1 surface that touches the cook Telegram bot will append a row here with: PR number, the chokepoint pattern evaluated, the evaluation result, and the operator's sign-off. The first v2 surface that adds hash-chaining will append a row here with: PR number, the hash function used, the verification query result, and the operator's sign-off.)*
