# 2026-09-08 — `ha-filament-ledger-end-user-deployable-append-only-integration-pattern` HANDOFF

> **Frozen build contract** for an external coding agent. Read this package alone; if you cannot start without additional context, this package is incomplete.

## 1. Active feature path

`features/155-ha-filament-ledger-end-user-deployable-append-only-integration-pattern.md` (defer artifact; **no code today**).

Bucket: **v2 owner-pains architecture-reference**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When LE31 v2 introduces an owner-facing audit-export surface, the owner wants *a deployable-integration pattern for exposing `audit_logs` (or derived `StockEntry`) as a normal user integration*, but struggles because *LE31 doesn't yet have a user-facing-deployable-integration primitive*, so that *the v2 surface can be exposed as a normal integration (not a custom build)*." **PASS** (zero-pain today; the cook Telegram bot is already a user-facing ledger surface; the JTBD is documentation-nicety, not build-need). |
| 2 | **Viability** | Owner can read 2666 B? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence high for the architectural match (the four sub-primitives — *Home Assistant custom integration* + *append-only ledger* + *instead of guesswork* + *tracks remaining filament* — map onto a *user-facing deployable integration* that exposes the ledger as a sensor panel). Stack mismatch (Home Assistant, not FastAPI) → no code adoption is possible. **PASS**. |
| 4 | **Conflict** | None. The ha-filament-ledger "append-only ledger" pattern *is* the LE31 §3.1 *current stock is derived from entries* invariant; the "instead of guesswork" pattern *is* the LE31 §3.1 *never update or delete ledger events* invariant (mutable state is the "guesswork" alternative that the pattern rejects). **PASS** (charter §3.1 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2 owner-pains architecture-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 2666 B description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (2666 B is already tight; the *instead of guesswork* rhetorical move is the key contribution). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/2026-09-08-ha-filament-ledger-end-user-deployable-append-only-integration-pattern-HANDOFF.md` and `features/155-ha-filament-ledger-end-user-deployable-append-only-integration-pattern.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2 architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that exposes `audit_logs` as a Home Assistant sensor, a Telegram bot skill, a CLI tool, or a webhook receiver):

- `app/audit/expose.py` — possibly add a new exposure surface (Home Assistant sensor, Telegram bot skill, CLI tool, webhook receiver).
- `app/audit/config.py` — possibly add a new configuration surface (the *frozen mandate* — what the integration is allowed to read/write).
- `app/state/transitions.py` — possibly add a new operational transition (user-facing-deployable-integration config).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/155-ha-filament-ledger-end-user-deployable-append-only-integration-pattern.md` exists and is read back by the parent.
- [ ] `specs/2026-09-08-ha-filament-ledger-end-user-deployable-append-only-integration-pattern-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The ha-filament-ledger description is quoted verbatim (2666 B repo).
- [ ] The 1:1 mapping onto LE31 v1/v2 architecture is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a user-facing-deployable-integration surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The ha-filament-ledger pattern is evaluated against the PR's changes: does the change preserve *append-only ledger*? Does the change preserve *instead of guesswork* discipline? Does the change expose the ledger as a *user-facing deployable integration*? Does the change use a *frozen mandate* (config flow)?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR; remove the new exposure surface.
- Delete: revert the PR; remove the new Home Assistant sensor, Telegram bot skill, CLI tool, or webhook receiver; restore the original `audit_logs` exposure.
- Migration cost: depends on the v2 change; the ha-filament-ledger pattern's *append-only* implies *no new migrations* (the new exposure surfaces are *read-only* on top of the existing append-only log).
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
| Feature ID | 155 |
| Slug | `ha-filament-ledger-end-user-deployable-append-only-integration-pattern` |
| Bucket | v2 owner-pains architecture-reference |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/audit/expose.py` (new, possibly) + `app/audit/config.py` (possibly) + `app/state/transitions.py` (possibly) |
| Trigger condition | First v2 PR that exposes `audit_logs` as a Home Assistant sensor, a Telegram bot skill, a CLI tool, or a webhook receiver |
| Verification protocol | Does the change preserve *append-only ledger*? Does it preserve *instead of guesswork* discipline? Does it expose the ledger as a *user-facing deployable integration*? Does it use a *frozen mandate* (config flow)? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | (to be created) |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `jobshimo/ha-filament-ledger` (MIT, 0★, pushed 2026-09-07T09:26:19Z) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds a user-facing-deployable-integration surface lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the ha-filament-ledger pattern is the right architectural checklist (an owner decision).

## 9. Verification log

*(Empty today. The first v2 surface that adds a user-facing-deployable-integration will append a row here with: PR number, the ha-filament-ledger pattern evaluated, the evaluation result, and the operator's sign-off.)*