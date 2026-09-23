# Feature 220 — Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger (defer)

> **NEW observation (2026-09-23).** Documents in-window GitHub Search `append-only+ledger` query result: `Jita81/commit-replay-bench` (**Apache-2.0 ✓**, **0★/0⑂**, Python, **pushed 2026-09-23T05:51:17Z = TODAY**, in-window by push only, **5066 KB** substantial repo, default_branch=`main`). Topics (verbatim from raw JSON, **0 topics**): none. Description (verbatim, parent-verified GitHub Search raw JSON, full text via direct-GET): *"Commit Replay Bench — grade an AI coding agent against a repository's own held-out tests, record every verdict in an append-only evidence ledger, route each class of change on measured evidence. Self-hosted, BYOK, Apache-2.0."* **The strongest v2-AI commit-replay-bench-evidence-ledger vocabulary of the 54-pass series** (the only in-window candidate combining `Commit Replay Bench + AI-coding-agent-evaluation + held-out-tests + append-only evidence ledger + route-by-measured-evidence + self-hosted + BYOK` pushed on 2026-09-23). Bucket: **v2-AI commit-replay-bench-evidence-ledger (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"Commit Replay Bench + grade an AI coding agent against a repository's own held-out tests + record every verdict in an append-only evidence ledger + route each class of change on measured evidence + Self-hosted + BYOK + Apache-2.0"** quintuple-primitive as a persistent cross-section reference for any future LE31 v2-AI surface that introduces an AI-assisted workflow with measurable-evidence-binding + audit-trail + operator-controlled-keys. The artifact is the persistent cross-section reference + the five named architectural primitives (commit-replay-evaluation, held-out-tests-grading, append-only-evidence-ledger, route-by-measured-evidence, self-hosted-BYOK). No code today (Apache-2.0 license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **Commit Replay Bench + grade an AI coding agent against a repository's own held-out tests** discipline: the *commit-replay-evaluation* posture (a coding agent's patch is replayed against the repo's own hidden tests; the patch passes or fails based on the held-out test outcome). Maps onto charter §3.4's *observable-evidence* primitive for v2-AI workflows: every AI-produced code change is graded against measurable evidence (tests), not vibes.
- A written record of the **record every verdict in an append-only evidence ledger** discipline: direct LE31 `audit_logs` discipline match; every grading verdict is a new append-only entry; the ledger is the persistent proof.
- A written record of the **route each class of change on measured evidence** discipline: the *route-by-measured-evidence* posture (different change-classes are routed to different handlers based on the evidence-quality signal from the grading ledger). Maps onto charter §3.1's *explicit-state-transition* discipline: every state change (route-decision) is preceded by a measured-evidence gate.
- A written record of the **Self-hosted + BYOK (Bring Your Own Key)** discipline: the *local-first + non-cloud-by-default + operator-controlled-keys* posture is textbook §3.4 compliance (operator-tooling with observable evidence + non-AI fallback + no cloud-exfiltration risk + operator owns the API keys). The *self-hosted* discipline is the *no-managed-cloud-service-by-default* primitive.
- A written record of the **Apache-2.0** permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-assisted workflow surface (charter §3.4 explicitly forbids customer-facing AI; LE31 v1 has no owner-facing AI either).
- A cross-section reference with the prior AI-governance + audit-log + append-only-ledger + human-gate + AI-system-registry primitives cluster: features 92 (AI-agent-decision-ledger), 126 (Five Primitives for Governing AI Agents), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 145 (garde-fous), 152, 167 (provtrail hash-chained ledger), 169 (openshare-ledger), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger), 188 (ShibaClaw), 189 (HASHI), 190 (ilyautov small-business-RU-34), 192 (LinkedParticles/particles-standard), 196 (monstabravo agent-ledger), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter), 199 (karusrus-transparency-kit), 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 218 (today's Pick A sister — LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), 219 (today's Pick B sister — Mormolykos/epcore v2-AI deterministic-licensing-kernel). The *transferable insight* is the **commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK** primitive set.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2-AI surface in v1 (charter §3.4 explicit invariant: AI may only assist owner/staff with observable evidence + non-AI fallback; no v1 surface today).
- Any introduction of a managed-cloud-service dependency (the *self-hosted + BYOK* discipline is the whole point; introducing a managed-cloud-service dep would violate the primitive).
- Any mandatory integration with a specific LLM provider (the *BYOK* discipline means the operator brings their own keys; no LLM provider lock-in).

## Description

GitHub Search `append-only+ledger` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-23/_raw/gh_append_only_ledger.json`) returned 34 total / 30 retrieved candidates; `Jita81/commit-replay-bench` is one of the 3 net-new in-window Apache-2.0 Python candidates not previously filed. It is the strongest v2-AI commit-replay-bench-evidence-ledger vocabulary of the 54-pass series.

The `Jita81/commit-replay-bench` repo's architectural pattern has five core sub-primitives:

1. **Commit Replay Bench + grade an AI coding agent against a repository's own held-out tests** — the *commit-replay-evaluation* discipline (a coding agent's patch is replayed against the repo's own hidden tests; the patch passes or fails based on the held-out test outcome). This maps onto charter §3.4's *observable-evidence* primitive for v2-AI workflows: every AI-produced code change is graded against measurable evidence (tests), not vibes. Charter §3.4 operator-tooling primitive: the bench is owner/staff-tooling (the agent being graded), not customer-facing.
2. **Record every verdict in an append-only evidence ledger** — direct LE31 `audit_logs` discipline match. The *append-only evidence ledger* holds the sequence of grading verdicts; each verdict is a new append-only entry; the ledger is the persistent proof. Charter §3.1 + §3.2 compatibility: the *append-only* posture is preserved (no updates, no deletes, only appends).
3. **Route each class of change on measured evidence** — the *route-by-measured-evidence* discipline (different change-classes are routed to different handlers based on the evidence-quality signal from the grading ledger). Maps onto charter §3.1's *explicit-state-transition* discipline: every state change (route-decision) is preceded by a measured-evidence gate.
4. **Self-hosted + BYOK (Bring Your Own Key)** — the *local-first + non-cloud-by-default + operator-controlled-keys* posture is textbook §3.4 compliance (operator-tooling with observable evidence + non-AI fallback + no cloud-exfiltration risk + operator owns the API keys). The *self-hosted* discipline is the *no-managed-cloud-service-by-default* primitive.
5. **Apache-2.0** permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption).

The LE31 relevance is the **commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK** quintuple-primitive. LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the question this repo answers is "if (and only if) LE31 v2 ever introduces an AI-assisted workflow with measurable-evidence-binding + audit-trail + operator-controlled-keys, what is the operator-tooling primitive set that satisfies charter §3.4?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2-AI trigger condition (if the first v2-AI PR that introduces a commit-replay-bench surface lands):** potential schema additions (depending on the v2-AI surface):
- `commit_replay_inputs` table — each AI-coding-agent's patch that was graded would carry an entry in this table; the *commit-replay-evaluation* primitive from commit-replay-bench. Each row would have `patch_id`, `agent_id`, `repo_id`, `patch_payload` (JSONB), `recorded_at`.
- `commit_replay_held_out_tests` table — each held-out test that was used to grade the patch would carry an entry in this table; the *held-out-tests-grading* primitive. Each row would have `test_id`, `repo_id`, `test_payload` (the hidden test), `recorded_at`, `test_signature` (for non-repudiation).
- `commit_replay_verdicts` table — each grading verdict (pass/fail + score) would carry an entry in this table; the *append-only evidence ledger* primitive. Each row would have `verdict_id`, `patch_id` FK, `test_id` FK, `verdict` (`pass` | `fail` | `inconclusive`), `score` (0.0 to 1.0), `decision_hash`, `recorded_at`.
- `commit_replay_routing` table — each route-decision based on the measured-evidence would carry an entry in this table; the *route-by-measured-evidence* primitive. Each row would have `route_id`, `verdict_id` FK, `route_handler` (the destination handler), `route_threshold`, `recorded_at`.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces a commit-replay-bench surface lands):**
- Add a `commit_replay_inputs` SQLModel table (patch_id, agent_id, repo_id, patch_payload, recorded_at).
- Add a `commit_replay_held_out_tests` SQLModel table (test_id, repo_id, test_payload, recorded_at, test_signature).
- Add a `commit_replay_verdicts` SQLModel table (verdict_id, patch_id FK, test_id FK, verdict, score, decision_hash, recorded_at).
- Add a `commit_replay_routing` SQLModel table (route_id, verdict_id FK, route_handler, route_threshold, recorded_at).
- Implement a `clone_repo(repo_id) -> local_repo_path` function (stdlib-only or third-party git CLI; the *self-hosted* discipline; no managed-cloud-service dependency).
- Implement a `run_held_out_tests(repo_path, test_id) -> verdict` function (the *commit-replay-evaluation* primitive; the *held-out-tests-grading* primitive).
- Implement a `verdict_signature(verdict, test_id) -> str` function (stdlib-only; the *non-repudiation* primitive); use SHA-256 hash chain.
- Implement a `route_by_measured_evidence(verdict, threshold) -> route_id` function (the *route-by-measured-evidence* primitive; the *explicit-state-transition* discipline).
- Add a periodic `commit_replay_snapshot` job that computes derived views (most-recent-patches, weekly agent-grade summary, etc.) and stores them as a snapshot table.

**Steps independent of the v2-AI trigger (today):**
- [x] Read the `Jita81/commit-replay-bench` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm Apache-2.0 permissive license (parent re-verified `license.spdx_id = "Apache-2.0"`).
- [x] Confirm the description's *Commit Replay Bench + AI-coding-agent-evaluation + held-out-tests + append-only evidence ledger + route-by-measured-evidence + self-hosted + BYOK* primitive set (parent re-verified verbatim via direct-GET).
- [x] Cross-reference with features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (repo now 404), 198, 199, 203, 204, 205, 212, 213, 214, 215, 216, 217, 218 (this file's Pick A sister), 219 (this file's Pick B sister) (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces a commit-replay-bench surface lands):**
- The owner would need a Telegram command to view the *commit-replay-verdict summary* (e.g., `/replays today`); the *commit-replay-evaluation* primitive maps 1:1 onto a chat-style query interface where the human sees the full grading history.
- The owner would need a Telegram command to view the *routing-decision for a specific verdict* (e.g., `/replay-route <verdict_id>`); the *route-by-measured-evidence* primitive would surface the route_handler + the verdict + the threshold.
- These are v2-AI surface additions; not in v1 scope.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v2-AI trigger dependencies:** depends on the v2-AI surface that introduces a commit-replay-bench with operator-tooling + non-cloud-by-default + append-only-evidence-ledger + measured-evidence-routing + BYOK (LE31 v1 has none of these surfaces). Cross-references: features 92 (AI-agent-decision-ledger), 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 126 (Five Primitives for Governing AI Agents), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 141 (KRINEIA five-invariants), 145 (garde-fous), 152, 156 (AWIG-OS rule-citing-audit), 160 (FactGraph), 167 (provtrail hash-chained ledger), 169 (akoffice933 openshare-ledger SHA-256 hash chain), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger disposition-ledger kernel), 188 (ShibaClaw self-hosted security-first AI agent), 189 (HASHI local-first control-plane), 190 (ilyautov small-business-RU-34 AI-skills-tax-contractor-INN), 192 (LinkedParticles/particles-standard sourced + confidence-scored append-only ledger), 196 (monstabravo agent-ledger append-only-checked-against-git), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 218 (this file's Pick A sister — LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), 219 (this file's Pick B sister — Mormolykos/epcore v2-AI deterministic-licensing-kernel).

## Open questions

1. **Commit-replay-evaluation mechanism:** does the bench clone the repo + apply the patch + run the held-out tests? Or does it use a different protocol (e.g., a remote API, a containerized sandbox, a local-only mode)? The full read of `Jita81/commit-replay-bench`'s source code is needed before any v2 port.
2. **Append-only-evidence-ledger schema details:** what is the exact schema of an *append-only-evidence-ledger* entry? Each entry has `verdict_id` + `patch_id` FK + `test_id` FK + `verdict` + `score` + `decision_hash` + `recorded_at`? Or a richer schema? The full read is needed.
3. **Route-by-measured-evidence mechanism:** does the bench route based on a classifier (e.g., a small ML model)? A threshold (e.g., `score >= 0.8`)? A heuristic (e.g., a hand-crafted rule)? The full read of the routing logic is needed.
4. **Self-hosted + BYOK posture:** does the bench expose a CLI? A web UI? A Docker image? Does it integrate with multiple LLM providers (OpenRouter, OpenAI, Anthropic, local-LLM-via-Ollama)? The full read of the surface is needed.
5. **Apache-2.0 license file confirmation:** is `Jita81/commit-replay-bench`'s Apache-2.0 license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).
6. **LE31 v1 → v2 migration path:** would the bench port cleanly to LE31 v2's stack (Python 3.13 + FastAPI + SQLModel + Postgres + aiogram v3)? Or would LE31 v2 have to write its own equivalent? Cross-reference: feature 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), feature 198 (aidankaras/arbiter postgresql point-in-time).

## Why this matters

The **commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK** quintuple-primitive is **the cleanest 2026-09-23 v2-AI commit-replay-bench vocabulary for any future LE31 v2 surface that introduces an AI-assisted workflow with measurable-evidence-binding + audit-trail + operator-controlled-keys** — and the Apache-2.0 permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31's charter §3.1 + §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback; explicit-state-transition; append-only posture; non-cloud-by-default). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce an AI-assisted workflow with measurable-evidence-binding (e.g., an AI-suggested stock-replenishment that must be graded against measurable evidence — past prep history, current stock, supplier availability), the owner wants *a commit-replay-bench surface that the human can audit*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant)*, so that *v2 can offer AI assistance without violating §3.1 + §3.4*." **PASS** (zero-pain today; v1 is small enough that operator-tooling without AI is sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure (the *self-hosted* discipline is the whole point); no new stack dependencies (the *BYOK* discipline means operator brings their own keys; no managed-cloud-service dependency); no new permissions. Confidence medium for the architectural match (the *commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK* primitive set is well-established in the GitHub 0★-community-adoption cluster; commit-replay-bench's 5066 KB substantial-repo footprint + Apache-2.0 license confirms a real implementation, not just a proposal). Apache-2.0 license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *commit-replay-evaluation + held-out-tests-grading + append-only-evidence-ledger + route-by-measured-evidence + self-hosted-BYOK* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; operator-tooling with observable evidence + non-AI fallback; explicit-state-transition discipline; non-cloud-by-default; no customer-facing AI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI commit-replay-bench-evidence-ledger (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/220-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger-HANDOFF.md` and `features/220-Jita81-commit-replay-bench-apache-2-0-ai-coding-agent-evaluation-held-out-tests-append-only-evidence-ledger-self-hosted-byok-v2-ai-commit-replay-bench-evidence-ledger.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-23.md` (54th consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 218 (this file's Pick A sister — LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), 219 (this file's Pick B sister — Mormolykos/epcore v2-AI deterministic-licensing-kernel).
- Sister-picks from 2026-09-23: feature 218 (LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), feature 219 (Mormolykos/epcore v2-AI deterministic-licensing-kernel).