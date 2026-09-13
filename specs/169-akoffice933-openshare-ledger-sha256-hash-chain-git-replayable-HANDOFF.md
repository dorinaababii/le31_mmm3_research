# 169 — akoffice933 openshare-ledger SHA-256 hash chain git-replayable HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 external-auditor or offline-mode surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/169-akoffice933-openshare-ledger-sha256-hash-chain-git-replayable.md` (defer artifact; **no code today**).

Bucket: **v2 architecture-reference (SHA-256 hash chain + replayable from git; charter §3.1 territory; v2-hardening primitive for independent-verifiability without a third-party timestamping service)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 surface introduces an external auditor (EU compliance audit per §3.1, French tax authority inspection, or a regulatory inspection) OR the first v2 surface that operates without internet access, the auditor wants *a primitive that records every state change in a SHA-256 hash chain, replayable from git*, but struggles because *LE31 v1's `audit_logs` is text-only and depends on the auditor trusting the database*, so that *the v2 surface can be independently verified by any auditor with read access to the git repository*." **PASS** (zero-pain today; v1 has no external-auditor surface; the JTBD is primitive documentation, not a build-need). |
| 2 | **Viability** | Owner can read the description (1-line)? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (openshare-ledger is MIT Python; SHA-256 is in the Python stdlib); no new permissions. Confidence medium-high for the primitive match (description + 10 topics align with `ai`, `auditability`, `contribution-tracking`, `data-provenance`, `evaluation`, `hash-chain`, `machine-learning`, `open-models`, `open-source`, `provenance`); low for transferability (openshare-ledger is for community-AI training attribution, not restaurant ops). Practicability of adoption: medium-high — the SHA-256 + git-replay discipline is well-established in software supply-chain security research (Sigstore, in-toto, SLSA). **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The openshare-ledger *SHA-256 hash chain + replayable from git* primitive *is* a v2 question, not a v1 question; it does not violate §3.1 (append-only posture is preserved — the chain IS append-only SHA-256 hash-chained). No §3.4 conflict (the primitive itself has no AI integration; the *use case* is community-AI training attribution, but the primitive works for any append-only audit chain). **PASS** (charter §3.1 invariant-compatible for v1; the primitive IS the strongest form of §3.1). |
| 5 | **Outcome, appetite, scope** | v2 architecture-reference (SHA-256 hash chain + replayable from git + decentralized-replay vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-line description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (1 line is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/169-akoffice933-openshare-ledger-sha256-hash-chain-git-replayable-HANDOFF.md` and `features/169-akoffice933-openshare-ledger-sha256-hash-chain-git-replayable.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section vocabulary for the next v2-hardening question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a SHA-256 hash chain over `audit_logs` + an external-auditor or offline-mode surface):

- `app/models/audit_log.py` — possibly add `entry_hash` and `parent_hash` fields (depends on the v2 change).
- `app/services/chain_compute.py` — possibly add a service that computes the SHA-256 hash chain on every `audit_logs` insert (depends on the v2 change).
- `app/git_hooks/pre-commit` — possibly add a git pre-commit hook that writes `audit_chain.json` so the chain is replayable from git alone (depends on the v2 change).
- `app/services/chain_walk.py` — possibly add a chain-walk query primitive that walks the SHA-256 chain between two entries (depends on the v2 change).
- `app/services/audit_export.py` — possibly add an audit-export surface for external auditors (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/169-akoffice933-openshare-ledger-sha256-hash-chain-git-replayable.md` exists and is read back by the parent.
- [ ] `specs/169-akoffice933-openshare-ledger-sha256-hash-chain-git-replayable-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The openshare-ledger description is quoted verbatim (1-line, all 10 topics).
- [ ] The 0★/0⑂ + MIT + 1-day-old + Python + 70 KB stack-shape cluster is documented.
- [ ] The *SHA-256 hash chain + replayable from git + decentralized-replay* primitives are documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a SHA-256 hash chain over `audit_logs` + an external-auditor or offline-mode surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The openshare-ledger JTBD-validation set is evaluated against the PR's changes: does the change add SHA-256 entry_hash + parent_hash to `audit_logs`? Is the chain replayable from git alone (no third-party timestamping service)? Is the chain-walk query primitive supported?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; drop the `entry_hash` and `parent_hash` fields from `audit_logs`; remove the new `chain_compute` service; remove the new git pre-commit hook; remove the new `chain_walk` service; remove the new `audit_export` surface.
- Migration cost: depends on the v2 change; the openshare-ledger pattern's *SHA-256 hash chain + replayable from git* implies *additive architecture* (the new fields are additive on top of the existing v1 surfaces — append-only `audit_logs` + StockEntry ledger).
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
| Feature ID | 169 |
| Slug | `akoffice933-openshare-ledger-sha256-hash-chain-git-replayable` |
| Bucket | v2 architecture-reference (SHA-256 hash chain + replayable from git + decentralized-replay) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/audit_log.py` (possibly `entry_hash` + `parent_hash` fields) + `app/services/chain_compute.py` (possibly) + `app/git_hooks/pre-commit` (possibly) + `app/services/chain_walk.py` (possibly) + `app/services/audit_export.py` (possibly) |
| Trigger condition | First v2 PR that adds a SHA-256 hash chain over `audit_logs` + an external-auditor or offline-mode surface |
| Verification protocol | Does the change add SHA-256 entry_hash + parent_hash to `audit_logs`? Is the chain replayable from git alone (no third-party timestamping service)? Is the chain-walk query primitive supported? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-237 (Research 2026-09-13 — daily) |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `akoffice933-maker/openshare-ledger` (MIT, 0★, Python, pushed 2026-09-12, created 2026-09-12, 70 KB) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds a SHA-256 hash chain over `audit_logs` + an external-auditor or offline-mode surface lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the *SHA-256 hash chain + replayable from git + decentralized-replay* JTBD validation is the right architectural checklist (an owner decision).
