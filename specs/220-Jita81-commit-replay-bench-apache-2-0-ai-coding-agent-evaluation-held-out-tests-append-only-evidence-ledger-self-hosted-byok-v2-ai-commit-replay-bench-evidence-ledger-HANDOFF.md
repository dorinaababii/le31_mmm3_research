# 220 — Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/220-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger.md` (defer artifact; **no code today**).

Bucket: **v2-AI commit-replay-bench-evidence-ledger (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + §3.4 + `le31-conventions` Feature gate).

## 2. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2-AI trigger condition fires (first v2-AI PR that introduces a commit-replay-bench surface):

- `app/models/commit_replay_inputs.py` — possibly add a `commit_replay_inputs` SQLModel table (patch_id, agent_id, repo_id, patch_payload, recorded_at).
- `app/models/commit_replay_held_out_tests.py` — possibly add a `commit_replay_held_out_tests` SQLModel table (test_id, repo_id, test_payload, recorded_at, test_signature).
- `app/models/commit_replay_verdicts.py` — possibly add a `commit_replay_verdicts` SQLModel table (verdict_id, patch_id FK, test_id FK, verdict, score, decision_hash, recorded_at).
- `app/models/commit_replay_routing.py` — possibly add a `commit_replay_routing` SQLModel table (route_id, verdict_id FK, route_handler, route_threshold, recorded_at).
- `app/kernel/clone_repo.py` — possibly implement a `clone_repo(repo_id) -> local_repo_path` function (the *self-hosted* discipline; no managed-cloud-service dependency).
- `app/kernel/run_held_out_tests.py` — possibly implement a `run_held_out_tests(repo_path, test_id) -> verdict` function (the *commit-replay-evaluation* primitive; the *held-out-tests-grading* primitive).
- `app/kernel/verdict_signature.py` — possibly implement a `verdict_signature(verdict, test_id) -> str` function (stdlib-only; the *non-repudiation* primitive); use SHA-256 hash chain.
- `app/kernel/route_by_measured_evidence.py` — possibly implement a `route_by_measured_evidence(verdict, threshold) -> route_id` function (the *route-by-measured-evidence* primitive).
- `app/jobs/commit_replay_snapshot.py` — possibly add a periodic job that computes derived views (most-recent-patches, weekly agent-grade summary).
- `app/bot/replays_today.py` — possibly add a Telegram-bot command for the owner to view the *commit-replay-verdict summary* (e.g., `/replays today`).
- `app/bot/replay_route.py` — possibly add a Telegram-bot command for the owner to view the *routing-decision for a specific verdict* (e.g., `/replay-route <verdict_id>`).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 3. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [x] `features/220-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger.md` exists and is read back by the parent.
- [x] `specs/220-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger-HANDOFF.md` (this file) exists and is read back by the parent.
- [x] The GitHub repo description is quoted verbatim: *"Commit Replay Bench — grade an AI coding agent against a repository's own held-out tests, record every verdict in an append-only evidence ledger, route each class of change on measured evidence. Self-hosted, BYOK, Apache-2.0."*
- [x] The Apache-2.0 permissive license is documented.
- [x] The *commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK* primitive set is documented.
- [x] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/` + INDEX.md row + parent research report file.

**Future v2-AI trigger (when the first v2-AI PR that introduces a commit-replay-bench surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The *commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK* primitive set is evaluated against the PR's changes: does the change preserve *commit-replay-evaluation posture*? Does the change add *held-out-tests-grading*? Does the change add *append-only-evidence-ledger*? Does the change add *route-by-measured-evidence*? Does the change preserve *self-hosted + BYOK* posture?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 4. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2-AI surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `commit_replay_inputs` table; remove the new `commit_replay_held_out_tests` table; remove the new `commit_replay_verdicts` table; remove the new `commit_replay_routing` table; restore the original `audit_logs` schema.
- Migration cost: depends on the v2-AI change; the *commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK* primitive set's design implies *additive schema* (the new `commit_replay_*` tables are additive on top of the existing append-only log).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

## 5. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.

## 6. Handoff summary

This is the **54th-pass daily-research Pick C** (2026-09-23). Bucket: **v2-AI commit-replay-bench-evidence-ledger**. Build verdict: **`defer`** (parking-lot, vocabulary-only artifact). The cross-section reference is the artifact. No code today. The future v2-AI trigger condition is *first v2-AI PR that introduces a commit-replay-bench surface*. Sister-picks today: feature 218 (LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), feature 219 (Mormolykos/epcore v2-AI deterministic-licensing-kernel).

## 7. Trigger condition for re-evaluation

The artifact is *re-evaluable* when:
- A v2-AI PR lands that introduces a commit-replay-bench surface (commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted + BYOK).
- A v2-AI PR lands that adds an operator-tooling surface for commit-replay-verdict inspection.

When any of these trigger conditions fires, the coding agent should:
1. Re-read the GitHub repo structure of `Jita81/commit-replay-bench`.
2. Compare against LE31 v2's actual v2-AI surface (when it exists).
3. Identify the transferable architectural primitives.
4. Apply the LE31 seven-check gate from `le31-conventions/SKILL.md`.

## 8. Sign-off gap

The artifact is vocabulary-only; no end-to-end behavior is built today. The verification protocol section's "Future v2-AI trigger" checklist is the placeholder for the next coding-agent reviewer.

---

**Linear sub-issue (intended, blocked):** HMM-301 in `le31 Research` (parent: HMM-298 in `le31 Research`; `le31 v2-AI` project does NOT exist per `le31-feature-pipeline/SKILL.md` line 33, so v2-AI picks attach to `le31 Research`); fallback at `/opt/data/le31-daily-research-2026-09-23.linear-fallback.json` (Linear MCP write endpoint BLOCKED by workspace plan-limit).