# 192 — LinkedParticles/particles-standard sourced + confidence-scored append-only ledger HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI agent-memory surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/192-LinkedParticles-particles-standard-apache-sourced-confidence-scored-append-only-ledger-agent-memory.md` (defer artifact; **no code today**).

Bucket: **v2-AI (agent-memory architecture-reference, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces an agent-memory subsystem, what is the primitive pattern for sourced + confidence-scored statements?'*, the maintainer wants *evidence that another independent 2026 Python repo at 7★ Apache-2.0 with 933 KB substantial content has shipped exactly the append-only ledger + sourced + confidence-scored triple-primitive as a named specification*, but struggles because *v1 has no agent-memory surface and the charter §3.4 invariant is not yet operationalized in code*, so that *v2 can introduce the agent-memory surface with the explicit charter §3.4 invariant rather than inventing a new one*." **PASS** (zero-pain today; v1 has no agent-memory surface; the JTBD is primitive vocabulary extension + charter §3.4 invariant documentation, not a build-need). |
| 2 | **Viability** | Owner can read 933 KB repo description + 6 topics? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (Python is the LE31 v1 backend). Confidence: medium-high for the architectural vocabulary validation (Apache-2.0 + Python + 7★/1⑂ community adoption + 933 KB substantial + in-window push 5-days-ago + the *append-only ledger + sourced + confidence-scored* triple-primitive is explicitly named in the description). Stack: on-pattern for v1 primitives (Python + append-only ledger are v1 stack); off-pattern for v2 primitives (JSON-LD + JSON Schema + knowledge-graph are v2-AI surface primitives, not v1 stack primitives). Practicability of adoption: medium — the *append-only ledger + sourced + confidence-scored* primitives can be extracted and re-implemented against LE31's StockEntry + audit_logs. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *append-only ledger* primitive is explicitly §3.1-aligned (LE31's existing `StockEntry` + `audit_logs` SQLModel tables are already append-only); the *sourced* primitive operationalizes the §3.1 actor-attribution invariant (LE31's `audit_logs.actor_user_id` column is the v1 implementation of the *sourced* primitive); §3.2 (Apache-2.0 = permissive); §3.4 (the *confidence-scored* primitive IS the observable-evidence + non-AI-fallback §3.4 invariant). Charter §3.4 explicitly validated. **PASS** (charter §3.1 + §3.2 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI agent-memory architecture-reference (cross-section architectural vocabulary + charter §3.4 invariant documentation); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 933 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (933 KB is already substantial; only the *append-only ledger + sourced + confidence-scored* + description need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/192-LinkedParticles-particles-standard-apache-sourced-confidence-scored-append-only-ledger-agent-memory-HANDOFF.md` and `features/192-LinkedParticles-particles-standard-apache-sourced-confidence-scored-append-only-ledger-agent-memory.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + charter §3.4 invariant documentation for the next v2-AI agent-memory question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an agent-memory subsystem, a *sourced-statements* schema, a *confidence-score* column on `audit_logs`, or a charter §3.4 invariant validation layer):

- `app/ai/memory/ledger.py` — possibly add an *append-only ledger* module for agent-memory (depends on the v2 change).
- `app/ai/memory/source.py` — possibly add a *sourced-statements* module (every agent-memory entry cites its source; depends on the v2 change).
- `app/ai/memory/confidence.py` — possibly add a *confidence-score* module (every agent-memory entry carries a deterministic confidence score; depends on the v2 change).
- `app/audit_logs_extension.py` — possibly add a `confidence_score` column to `audit_logs` (charter §3.4 alignment via the confidence-score invariant; depends on the v2 change).
- `app/ai/memory/vintage.py` — possibly add a *vintage-archive* module (deterministic re-derivation + assertion; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/192-LinkedParticles-particles-standard-apache-sourced-confidence-scored-append-only-ledger-agent-memory.md` exists and is read back by the parent.
- [ ] `specs/192-LinkedParticles-particles-standard-apache-sourced-confidence-scored-append-only-ledger-agent-memory-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `particles-standard` description is quoted verbatim (933 KB repo).
- [ ] The 7★/1⑂ + Apache-2.0 + Python + in-window push 5-days-ago + `agent-memory + ai-memory + epistemics + json-ld + jsonschema + knowledge-graph` topic set + *append-only ledger + sourced + confidence-scored* triple-primitive vocabulary is documented.
- [ ] The charter §3.4 alignment via explicit *confidence-score* observable-evidence metric is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an agent-memory subsystem, a *sourced-statements* schema, a *confidence-score* column on `audit_logs`, or a charter §3.4 invariant validation layer lands):**
- [ ] The PR is read back by the parent.
- [ ] The `particles-standard` architectural-vocabulary set is evaluated against the PR's changes: does the change address the *append-only ledger + sourced + confidence-scored* triple-primitive? Does the change enforce the *confidence-score* observable-evidence invariant (charter §3.4 alignment)? Does the change preserve the *sourced-statements* source-citation invariant?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `ledger.py` + `source.py` + `confidence.py` modules; remove the new `confidence_score` column on `audit_logs`; remove the new `vintage.py` module; restore the original `audit_logs` + `StockEntry` schemas.
- Migration cost: depends on the v2 change; the `particles-standard` pattern's *append-only ledger + sourced + confidence-scored* implies *additive architecture* (the new agent-memory subsystem is additive on top of the existing v1 surfaces — FastAPI routes + aiogram handlers + `audit_logs` writer all live in one Python process today; the new agent-memory subsystem adds a discrete layer with the sourced + confidence-scored discipline).
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
