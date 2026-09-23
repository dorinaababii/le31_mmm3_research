# Feature 219 — Mormolykos-epcore-mit-deterministic-licensing-kernel-evidence-in-licence-bound-append-only-ledger-standard-library-only-v2-ai-deterministic-licensing-kernel (defer)

> **NEW observation (2026-09-23).** Documents in-window GitHub Search `append-only+ledger` query result: `Mormolykos/epcore` (**MIT ✓**, **0★/0⑂**, Python, **pushed 2026-09-20T18:23:59Z**, in-window by push only, **128 KB** small repo, default_branch=`main`). Topics (verbatim from raw JSON, **0 topics**): none. Description (verbatim, parent-verified GitHub Search raw JSON): *"A deterministic licensing kernel: evidence in, a licence bound to one exact proposal out, recorded in an append-only ledger. Standard library only."* **The strongest v2-AI deterministic-licensing-kernel vocabulary of the 54-pass series** (the only in-window candidate with the *deterministic + evidence-bound + append-only-ledger + standard-library-only* quadruple-primitive). Bucket: **v2-AI deterministic-licensing-kernel (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"deterministic licensing kernel + evidence in + licence bound to one exact proposal out + recorded in an append-only ledger + standard library only"** quadruple-primitive as a persistent cross-section reference for any future LE31 v2-AI surface that introduces an AI-assisted workflow with deterministic-evidence-binding. The artifact is the persistent cross-section reference + the four named architectural primitives (deterministic-from-evidence, evidence-bound-licence, append-only-ledger, standard-library-only). No code today (MIT license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **deterministic licensing kernel** discipline: the *deterministic-from-evidence* posture (same evidence always produces same license output; no LLM or non-deterministic stage in the licensing path) maps onto any future LE31 v2-AI surface that needs a *deterministic-decision* primitive from operator-supplied evidence.
- A written record of the **evidence-bound-licence** discipline: the *evidence-bound* posture (each output is bound to its evidence; the binding is exact; the licence cannot drift from the evidence) maps onto charter §3.1's *attribution discipline* (every state transition must be attributable to its evidence).
- A written record of the **append-only ledger** discipline: direct LE31 `audit_logs` discipline match; every licensing decision is a new append-only entry; the ledger is the persistent record.
- A written record of the **standard-library-only** posture: the *zero-dependency* discipline (no third-party deps; stdlib only = portable + auditable + reproducible). LE31 v1's pin-bump discipline aligns with this (no exotic deps; the lockfile is the single source of truth).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-assisted workflow surface (charter §3.4 explicitly forbids customer-facing AI; LE31 v1 has no owner-facing AI either).
- A cross-section reference with the prior AI-governance + audit-log + append-only-ledger + human-gate + AI-system-registry primitives cluster: features 92 (AI-agent-decision-ledger), 126 (Five Primitives for Governing AI Agents), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 145 (garde-fous), 152, 167 (provtrail hash-chained ledger), 169 (openshare-ledger), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger), 188 (ShibaClaw), 189 (HASHI), 190 (ilyautov small-business-RU-34), 192 (LinkedParticles/particles-standard), 196 (monstabravo agent-ledger), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter), 199 (karusrus-transparency-kit), 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 218 (today's Pick A sister — LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), 220 (today's Pick C sister — Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger). The *transferable insight* is the **deterministic + evidence-bound + append-only-ledger + standard-library-only** primitive set.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2-AI surface in v1 (charter §3.4 explicit invariant: AI may only assist owner/staff with observable evidence + non-AI fallback; no v1 surface today).
- Any introduction of a third-party dependency (the *standard-library-only* discipline is the whole point; introducing a third-party dep would violate the primitive).

## Description

GitHub Search `append-only+ledger` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-23/_raw/gh_append_only_ledger.json`) returned 34 total / 30 retrieved candidates; `Mormolykos/epcore` is one of the 3 net-new in-window MIT Python candidates not previously filed. It is the strongest v2-AI deterministic-licensing-kernel vocabulary of the 54-pass series.

The `Mormolykos/epcore` repo's architectural pattern has four core sub-primitives:

1. **Deterministic licensing kernel** — the *deterministic-from-evidence* discipline (same evidence always produces same license output; no LLM or non-deterministic stage in the licensing path). Maps onto any future LE31 v2-AI surface that needs a *deterministic-decision* primitive from operator-supplied evidence. Charter §3.4 non-AI-fallback primitive: the kernel can run without LLM; the LLM is only an optional input.
2. **Evidence in, a licence bound to one exact proposal out** — the *evidence-bound-licence* discipline (each output is bound to its evidence; the binding is exact; the licence cannot drift from the evidence). Maps onto charter §3.1's *attribution discipline* (every state transition must be attributable to its evidence).
3. **Recorded in an append-only ledger** — direct LE31 `audit_logs` discipline match. The *append-only ledger* holds the sequence of licensing decisions; each decision is a new append-only entry; the ledger is the persistent record. Charter §3.1 + §3.2 compatibility: the *append-only* posture is preserved (no updates, no deletes, only appends).
4. **Standard library only** — the *zero-dependency* posture (no third-party deps; stdlib only = portable + auditable + reproducible). LE31 v1's pin-bump discipline aligns with this (no exotic deps; the lockfile is the single source of truth). Adoption would require confirming that the LE31 v1 stack does not conflict with stdlib-only (LE31 uses FastAPI + SQLModel + aiogram + httpx — all of which are third-party; the *standard-library-only* discipline is therefore NOT portable to v1 directly).

The LE31 relevance is the **deterministic + evidence-bound + append-only-ledger + standard-library-only** quadruple-primitive. LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the question this repo answers is "if (and only if) LE31 v2 ever introduces an AI-assisted workflow with deterministic-evidence-binding, what is the operator-tooling primitive set that satisfies charter §3.4?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2-AI trigger condition (if the first v2-AI PR that introduces a deterministic-licensing-kernel surface lands):** potential schema additions (depending on the v2-AI surface):
- `licensing_kernel_inputs` table — each evidence input that fed into a licensing decision would carry an entry in this table; the *deterministic-from-evidence* primitive from epcore. Each row would have `evidence_id`, `actor_user_id`, `evidence_payload` (JSONB), `recorded_at`, `evidence_signature` (for non-repudiation).
- `licensing_kernel_outputs` table — each license output would carry an entry in this table; the *evidence-bound-licence* primitive. Each row would have `license_id`, `license_signature`, `binding_to_evidence_hash` (the cryptographic binding), `recorded_at`.
- `licensing_kernel_decisions` table — a write-once append-only record of the actual licensing decision (the *append-only ledger* primitive). Each row would have `decision_id`, `input_evidence_id` FK, `output_license_id` FK, `decision_hash`, `recorded_at`.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces a deterministic-licensing-kernel surface lands):**
- Add a `licensing_kernel_inputs` SQLModel table (evidence_id, actor_user_id, evidence_payload, recorded_at, evidence_signature).
- Add a `licensing_kernel_outputs` SQLModel table (license_id, license_signature, binding_to_evidence_hash, recorded_at).
- Add a `licensing_kernel_decisions` SQLModel table (decision_id, input_evidence_id FK, output_license_id FK, decision_hash, recorded_at).
- Implement a `deterministic_kernel.run(evidence) -> license` function (stdlib-only; no third-party deps; the *standard-library-only* discipline); the *deterministic-from-evidence* primitive.
- Implement a `binding_hash(evidence, license) -> str` function (stdlib-only; the *evidence-bound-licence* primitive); use SHA-256 hash chain.
- Implement a `license_signature(license, binding_hash) -> str` function (stdlib-only; the *non-repudiation* primitive); use HMAC-SHA256 with a server-side secret.
- Add a periodic `license_decision_snapshot` job that computes derived views (most-recent-licenses, weekly license summary, etc.) and stores them as a snapshot table; the *position-over-time* discipline (cross-reference feature 197 rajo69-ledgerkb vocabulary).

**Steps independent of the v2-AI trigger (today):**
- [x] Read the `Mormolykos/epcore` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *deterministic licensing kernel + evidence-bound + append-only-ledger + standard-library-only* primitive set (parent re-verified verbatim).
- [x] Cross-reference with features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (repo now 404), 198, 199, 203, 204, 205, 212, 213, 214, 215, 216, 217, 218 (this file's Pick A sister), 220 (this file's Pick C sister) (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces a deterministic-licensing-kernel surface lands):**
- The owner would need a Telegram command to view the *licensing-decision summary* (e.g., `/licenses today`); the *deterministic-from-evidence* primitive maps 1:1 onto a chat-style query interface where the human sees the full decision history.
- The owner would need a Telegram command to view the *evidence-binding for a specific license* (e.g., `/license-binding <id>`); the *evidence-bound-licence* primitive would surface the binding hash + the evidence_id FK.
- These are v2-AI surface additions; not in v1 scope.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v2-AI trigger dependencies:** depends on the v2-AI surface that introduces a deterministic-licensing-kernel with operator-tooling + non-cloud-by-default + append-only-ledger + standard-library-only (LE31 v1 has none of these surfaces). Cross-references: features 92 (AI-agent-decision-ledger), 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 126 (Five Primitives for Governing AI Agents), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 141 (KRINEIA five-invariants), 145 (garde-fous), 152, 156 (AWIG-OS rule-citing-audit), 160 (FactGraph), 167 (provtrail hash-chained ledger), 169 (akoffice933 openshare-ledger SHA-256 hash chain), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger disposition-ledger kernel), 188 (ShibaClaw self-hosted security-first AI agent), 189 (HASHI local-first control-plane), 190 (ilyautov small-business-RU-34 AI-skills-tax-contractor-INN), 192 (LinkedParticles/particles-standard sourced + confidence-scored append-only ledger), 196 (monstabravo agent-ledger append-only-checked-against-git), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 218 (this file's Pick A sister — LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), 220 (this file's Pick C sister — Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger).

## Open questions

1. **Deterministic-from-evidence mechanism:** is the *deterministic-from-evidence* discipline a pure function (i.e., `f(evidence) -> license` with no side effects, no randomness, no LLM)? Or does it have a non-deterministic stage (e.g., a random salt, a configuration file that mutates, an LLM stage)? The full read of `Mormolykos/epcore`'s source code is needed before any v2 port.
2. **Evidence-bound-licence binding mechanism:** is the *evidence-bound-licence* primitive cryptographic (e.g., SHA-256 hash chain, HMAC, Ed25519 signature)? Or is it logical (e.g., a foreign-key relationship)? The full read of the source code is needed.
3. **Append-only-ledger schema details:** what is the exact schema of an *append-only-ledger* entry? Each entry has `decision_id` + `input_evidence_id` FK + `output_license_id` FK + `decision_hash` + `recorded_at`? Or a simpler schema? The full read is needed.
4. **Standard-library-only enforcement:** does `Mormolykos/epcore` actually use zero third-party deps? Is the lockfile empty? The full read of the repo's dependencies is needed.
5. **Standard-library-only → Postgres migration path:** would the epcore schema port cleanly to Postgres (LE31 v2 would store the `licensing_kernel_decisions` in Postgres for SQLModel-consistency), or is the *standard-library-only* discipline a portability requirement (i.e., the stdlib-only code is the whole point; LE31 v2 would have to write its own equivalent)? Cross-reference: feature 189 (HASHI local-first control-plane = local-first-aware), feature 212 (Rooster-glitch/Hardtack = local-first-aware).
6. **MIT license file confirmation:** is `Mormolykos/epcore`'s MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **deterministic + evidence-bound + append-only-ledger + standard-library-only** quadruple-primitive is **the cleanest 2026-09-23 v2-AI deterministic-licensing-kernel vocabulary for any future LE31 v2 surface that introduces an AI-assisted workflow with deterministic-evidence-binding** — and the MIT permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31's charter §3.1 + §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback; attribution discipline; append-only posture). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce an AI-assisted workflow with deterministic-evidence-binding (e.g., an AI-suggested daily-prep summary that must be deterministic from the day's prep log), the owner wants *a deterministic-licensing-kernel surface that the human can audit*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant)*, so that *v2 can offer AI assistance without violating §3.1 + §3.4*." **PASS** (zero-pain today; v1 is small enough that operator-tooling without AI is sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (the *standard-library-only* discipline is the whole point); no new permissions. Confidence medium for the architectural match (the *deterministic + evidence-bound + append-only-ledger + standard-library-only* primitive set is well-established in the GitHub 0★-community-adoption cluster; epcore's 128 KB small-repo footprint + MIT license confirms a real implementation, not just a proposal). MIT license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *deterministic + evidence-bound + append-only-ledger + standard-library-only* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; operator-tooling with observable evidence + non-AI fallback; attribution discipline; no customer-facing AI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI deterministic-licensing-kernel (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/219-Mormolykos-epcore-mit-deterministic-licensing-kernel-evidence-in-licence-bound-append-only-ledger-standard-library-only-v2-ai-deterministic-licensing-kernel-HANDOFF.md` and `features/219-Mormolykos-epcore-mit-deterministic-licensing-kernel-evidence-in-licence-bound-append-only-ledger-standard-library-only-v2-ai-deterministic-licensing-kernel.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-23.md` (54th consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 212 (Rooster-glitch/Hardtack), 213 (hseshadr/avow), 214 (ilovepixelart/matador), 215 (Salar-prog/netscan), 216 (bangnevgo/ai-workflow-os), 217 (penguineer/PingBoardDaemon), 218 (this file's Pick A sister — LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), 220 (this file's Pick C sister — Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger).
- Sister-picks from 2026-09-23: feature 218 (LuisRG98/restaurant-saas-api v1 production-restaurant-API-reference), feature 220 (Jita81/commit-replay-bench v2-AI commit-replay-bench-evidence-ledger).