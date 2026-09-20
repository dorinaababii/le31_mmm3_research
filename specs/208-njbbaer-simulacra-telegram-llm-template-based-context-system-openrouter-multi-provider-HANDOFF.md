# 208 — njbbaer/simulacra telegram-llm-template-based-context-system + OpenRouter-multi-provider + AI-but-operator-only HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 owner-assist + template-based-context + OpenRouter-multi-provider + AI-but-operator-only question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/208-njbbaer-simulacra-telegram-llm-template-based-context-system-openrouter-multi-provider.md` (defer artifact; **no code today**).

Bucket: **v2 owner-assist (Telegram-LLM + template-based-context + multi-provider-abstraction + AI-but-operator-only primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces an LLM-assisted surface, a template-based-context pattern, a multi-provider-LLM-abstraction layer, or an AI-but-operator-only surface, what is the template-based-context + OpenRouter-multi-provider + AI-but-operator-only primitive that preserves the existing v1 no-LLM-surface + pure-transactional-cook-bot posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 1556 KB with MIT license + in-window-by-push-only + 4★/1⑂ + 6 topics including ai + llm + openrouter + python + telegram + telegram-bot is shipping the template-based-context + multi-provider-abstraction + AI-but-operator-only primitive as the v2 owner-assist discipline*, but struggles because *v1 has no documented LLM-surface primitive in the charter*, so that *v2 can introduce the LLM-assisted-surface + template-based-context + multi-provider-abstraction vocabulary with the explicit charter §3.4 observable-evidence + non-AI-fallback discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no LLM-surface trigger; the JTBD is primitive vocabulary extension + template-based-context documentation, not a build-need). |
| 2 | **Viability** | Owner can read 1556 KB repo description + 6-topic vocabulary + template-based-context + OpenRouter-multi-provider + AI-but-operator-only topic set? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v2 (the template-based-context vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the OpenRouter integration or the LLM-provider code; LE31 v1 has no LLM surface today). Confidence: medium for the template-based-context + OpenRouter-multi-provider + AI-but-operator-only vocabulary (MIT + Python + 1556 KB substantial + in-window-by-push-only + 4★/1⑂ + 6 topics + explicit template-based-context description + OpenRouter multi-provider topic = §3.2 STRICTLY-COMPATIBLE + §3.4 territory-future-review; the template-based-context discipline IS the *charter §3.4 observable-evidence + non-AI-fallback* pattern by construction). Stack: FastAPI + PostgreSQL backend = on-pattern for v2 primitives; OpenRouter integration = off-pattern for v1 (LE31 v1 has no LLM surface); LLM-provider libraries (openai + anthropic + google-generativeai) = off-pattern for v1; MIT license = on-pattern for code adoption. Practicability of adoption: high for vocabulary + architecture-reference adoption (MIT §3.2 STRICTLY-COMPATIBLE); low for code reuse (LE31 would re-implement against its own stack, not import OpenRouter or LLM-provider code). **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The template-based-context primitive IS the *charter §3.4 observable-evidence + non-AI-fallback* pattern by construction (the template is the evidence; the deterministic-template-renderer is the non-AI-fallback). The template-constrains-structure discipline ensures the LLM cannot *invent* context (the template constrains the structure); the LLM can only *fill* context (the renderer applies LLM-generated values to the templated slots). Charter §3.1 alignment (template-constrains-structure = explicit-structure discipline); §3.2 STRICTLY-COMPATIBLE (MIT license); §3.4 territory-future-review (the *template-based-context-system* primitive IS the *observable-evidence + non-AI-fallback* pattern by construction, but the LLM-assisted-interpretation step requires future §3.4 review before adoption). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 owner-assist (Telegram-LLM + template-based-context + OpenRouter-multi-provider + AI-but-operator-only vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1556 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (1556 KB is substantial; only the *template-based-context + OpenRouter-multi-provider + AI-but-operator-only* vocabulary + the in-window-by-push-only signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/208-njbbaer-simulacra-telegram-llm-template-based-context-system-openrouter-multi-provider-HANDOFF.md` and `features/208-njbbaer-simulacra-telegram-llm-template-based-context-system-openrouter-multi-provider.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + template-based-context + OpenRouter-multi-provider + AI-but-operator-only documentation for the next v2 owner-assist-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a template-based-context-bot to the LE31 operator surface, a multi-provider-LLM-abstraction layer to the LE31 v2 architecture, or a deterministic-template-renderer for any LLM-assisted workflow):

- `app/bot/templates/` — possibly add (the template directory; each bot gets its own template file with placeholders; depends on the v2 change).
- `app/bot/renderer.py` — possibly add (the deterministic-template-renderer that fills the placeholders with runtime-data; depends on the v2 change).
- `app/llm/openrouter.py` — possibly add (the OpenRouter multi-provider-LLM-abstraction layer; depends on the v2 change).
- `app/llm/providers/` — possibly add (the individual LLM provider implementations: OpenAI, Anthropic, Google, local-LLM; depends on the v2 change).
- `app/bot/llm_assist.py` — possibly add (the LLM-assisted-bot handler that calls the renderer + the LLM provider; depends on the v2 change; **charter §3.4 future-review required**).
- `tests/test_template_renderer.py` + `tests/test_openrouter_provider.py` + `tests/test_llm_assist_bot.py` — possibly add (the integration tests for the template-based-context + OpenRouter-multi-provider + LLM-assisted-bot surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no LLM surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/208-njbbaer-simulacra-telegram-llm-template-based-context-system-openrouter-multi-provider.md` exists and is read back by the parent.
- [ ] `specs/208-njbbaer-simulacra-telegram-llm-template-based-context-system-openrouter-multi-provider-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `njbbaer/simulacra` description is quoted verbatim (1556 KB repo).
- [ ] The 4★/1⑂ + MIT license (§3.2 STRICTLY-COMPATIBLE for code adoption) + Python + in-window-by-push-only + 6 topics (ai + llm + openrouter + python + telegram + telegram-bot) is documented.
- [ ] The charter §3.1 alignment via *template-constrains-structure = explicit-structure discipline* is documented.
- [ ] The charter §3.4 territory-future-review is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a template-based-context-bot to the LE31 operator surface, a multi-provider-LLM-abstraction layer to the LE31 v2 architecture, or a deterministic-template-renderer for any LLM-assisted workflow lands):**
- [ ] The PR is read back by the parent.
- [ ] The `njbbaer/simulacra` template-based-context + OpenRouter-multi-provider + AI-but-operator-only vocabulary is evaluated against the PR's changes: does the change address the *template-constrains-structure* discipline? does the change preserve the *OpenRouter-multi-provider-abstraction* primitive? does the change preserve the *AI-but-operator-only* posture? does the change preserve the *charter §3.4 observable-evidence + non-AI-fallback* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the `app/bot/templates/` template directory; remove the `app/bot/renderer.py` deterministic-template-renderer; remove the `app/llm/openrouter.py` OpenRouter integration; remove the `app/llm/providers/` LLM-provider implementations; remove the `app/bot/llm_assist.py` LLM-assisted-bot handler; restore the original `app/bot/cook.py` Telegram handler.
- Migration cost: depends on the v2 change; the template-based-context vocabulary is *additive architecture* (the templates are *new* files; the renderer is *new* code; the OpenRouter integration is *new* code; the LLM-provider implementations are *new* code; the LLM-assisted-bot is *new* code, not a schema change).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the `StockEntry` table retains all rows; the new `bot_template` table is *new* data, not a schema change; the new `bot_context` table is *new* data, not a schema change; the verification log is a *new* document, not a schema change.

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
