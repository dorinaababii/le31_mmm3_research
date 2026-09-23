# 219 — Mormolykos-epcore-mit-deterministic-licensing-kernel-evidence-in-licence-bound-append-only-ledger-standard-library-only-v2-ai-deterministic-licensing-kernel HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/219-Mormolykos-epcore-mit-deterministic-licensing-kernel-evidence-in-licence-bound-append-only-ledger-standard-library-only-v2-ai-deterministic-licensing-kernel.md` (defer artifact; **no code today**).

Bucket: **v2-AI deterministic-licensing-kernel (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + §3.4 + `le31-conventions` Feature gate).

## 2. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2-AI trigger condition fires (first v2-AI PR that introduces a deterministic-licensing-kernel surface):

- `app/models/licensing_kernel_inputs.py` — possibly add a `licensing_kernel_inputs` SQLModel table (evidence_id, actor_user_id, evidence_payload, recorded_at, evidence_signature).
- `app/models/licensing_kernel_outputs.py` — possibly add a `licensing_kernel_outputs` SQLModel table (license_id, license_signature, binding_to_evidence_hash, recorded_at).
- `app/models/licensing_kernel_decisions.py` — possibly add a `licensing_kernel_decisions` SQLModel table (decision_id, input_evidence_id FK, output_license_id FK, decision_hash, recorded_at).
- `app/kernel/deterministic_kernel.py` — possibly implement a `deterministic_kernel.run(evidence) -> license` function (stdlib-only; no third-party deps; the *standard-library-only* discipline).
- `app/kernel/binding_hash.py` — possibly implement a `binding_hash(evidence, license) -> str` function (stdlib-only; SHA-256 hash chain).
- `app/kernel/license_signature.py` — possibly implement a `license_signature(license, binding_hash) -> str` function (stdlib-only; HMAC-SHA256 with server-side secret).
- `app/jobs/license_decision_snapshot.py` — possibly add a periodic job that computes derived views (most-recent-licenses, weekly license summary).
- `app/bot/licenses_today.py` — possibly add a Telegram-bot command for the owner to view the *licensing-decision summary* (e.g., `/licenses today`).
- `app/bot/license_binding.py` — possibly add a Telegram-bot command for the owner to view the *evidence-binding for a specific license* (e.g., `/license-binding <id>`).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 3. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [x] `features/219-Mormolykos-epcore-mit-deterministic-licensing-kernel-evidence-in-licence-bound-append-only-ledger-standard-library-only-v2-ai-deterministic-licensing-kernel.md` exists and is read back by the parent.
- [x] `specs/219-Mormolykos-epcore-mit-deterministic-licensing-kernel-evidence-in-licence-bound-append-only-ledger-standard-library-only-v2-ai-deterministic-licensing-kernel-HANDOFF.md` (this file) exists and is read back by the parent.
- [x] The GitHub repo description is quoted verbatim: *"A deterministic licensing kernel: evidence in, a licence bound to one exact proposal out, recorded in an append-only ledger. Standard library only."*
- [x] The MIT permissive license is documented.
- [x] The *deterministic + evidence-bound + append-only-ledger + standard-library-only* primitive set is documented.
- [x] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/` + INDEX.md row + parent research report file.

**Future v2-AI trigger (when the first v2-AI PR that introduces a deterministic-licensing-kernel surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The *deterministic + evidence-bound + append-only-ledger + standard-library-only* primitive set is evaluated against the PR's changes: does the change preserve *deterministic-from-evidence posture*? Does the change add *evidence-bound-licence*? Does the change add *append-only-ledger*? Does the change use *standard-library-only*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 4. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2-AI surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `licensing_kernel_inputs` table; remove the new `licensing_kernel_outputs` table; remove the new `licensing_kernel_decisions` table; restore the original `audit_logs` schema.
- Migration cost: depends on the v2-AI change; the *deterministic + evidence-bound + append-only-ledger + standard-library-only* primitive set's design implies *additive schema* (the new `licensing_kernel_*` tables are additive on top of the existing append-only log).
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

This is the **54th-pass daily-research Pick B** (2026-09-23). Bucket: **v2-AI deterministic-licensing-kernel**. Build verdict: **`defer`** (parking-lot, vocabulary-only artifact). The cross-section reference is the artifact. No code today. The future v2-AI trigger condition is *first v2-AI PR that introduces a deterministic-licensing-kernel surface*. Sister-picks today: feature 218 (LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), feature 220 (Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger).

## 7. Trigger condition for re-evaluation

The artifact is *re-evaluable* when:
- A v2-AI PR lands that introduces a deterministic-licensing-kernel surface (deterministic-from-evidence + evidence-bound-licence + append-only-ledger + standard-library-only).
- A v2-AI PR lands that adds an operator-tooling surface for evidence-binding inspection.

When any of these trigger conditions fires, the coding agent should:
1. Re-read the GitHub repo structure of `Mormolykos/epcore`.
2. Compare against LE31 v2's actual v2-AI surface (when it exists).
3. Identify the transferable architectural primitives.
4. Apply the LE31 seven-check gate from `le31-conventions/SKILL.md`.

## 8. Sign-off gap

The artifact is vocabulary-only; no end-to-end behavior is built today. The verification protocol section's "Future v2-AI trigger" checklist is the placeholder for the next coding-agent reviewer.

---

**Linear sub-issue (intended, blocked):** HMM-300 in `le31 Research` (parent: HMM-298 in `le31 Research`; `le31 v2-AI` project does NOT exist per `le31-feature-pipeline/SKILL.md` line 33, so v2-AI picks attach to `le31 Research`); fallback at `/opt/data/le31-daily-research-2026-09-23.linear-fallback.json` (Linear MCP write endpoint BLOCKED by workspace plan-limit).