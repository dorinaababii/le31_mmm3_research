# HANDOFF — Feature 344: `acc12138-x-smart-restaurant-ai-waiter-mit-llm-powered-ai-waiter-h5-qr-ordering-dual-track-intent-parsing-llm-rules-rag-real-time-admin-dashboard-flask-sqlite-ollama-qwen3-4b-chinese-v2-ai-dual-track-llm-as-residual-only-parser-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/344-acc12138-x-smart-restaurant-ai-waiter-mit-llm-powered-ai-waiter-h5-qr-ordering-dual-track-intent-parsing-llm-rules-rag-real-time-admin-dashboard-flask-sqlite-ollama-qwen3-4b-chinese-v2-ai-dual-track-llm-as-residual-only-parser-vocabulary.md` — defer/parking-lot (Pick A of Daily Brainstorm 2026-10-19).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes a *LLM-waiter-+-dual-track-intent-parsing-+-RAG-+-H5-QR-ordering-+-real-time-admin-dashboard-+-on-premise-+-Ollama-+-local-Qwen3-4B primitive*, the owner wants *evidence that this LLM-waiter-vocabulary exists in 2026 with the same dual-track-LLM-as-residual-only-parser + on-premise-Ollama-local-Qwen3-4B posture*, but struggles because *LE31 has no documented v2-AI LLM-waiter-vocabulary reference*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same dual-track-intent-parsing + LLM-as-residual-only-parser + on-premise-Ollama-Qwen3-4B + RAG-over-Chroma posture"*. |
| 2 | Viability | ✓ | The owner/staff can understand the operator-facing vocabulary (LLM-waiter + dual-track-intent-parsing + RAG + H5-QR-ordering + admin-dashboard + on-premise-Ollama-Qwen3-4B + chinese-language) without specialist help. The 0★/0⑨ with substantial maintainer activity (created 2026-09-21 + pushed 2026-10-15 = IN-WINDOW BY BOTH FIELDS, ~28-day-old repo, 50778 KB substantial) makes vocabulary viable, but code adoption is not viable (LE31 v2-AI has no LLM-waiter-as-feature surface today; v2-AI is on agent-governance + audit-ledger + chokepoint). |
| 3 | Practicability and confidence | ✓ | Fits the fixed stack: Python ✓ ON-STACK + Flask OFF-STACK (charter §3.1 review needed: LE31 v2-AI is FastAPI + Postgres, not Flask + SQLite) + SQLite OFF-STACK (LE31 v2-AI is Postgres, not SQLite) + LangChain OFF-STACK (LangChain introduces implicit-state-machines; LE31 v2-AI is explicit-state-machine per §3.1) + Ollama/local-Qwen3-4B OFF-STACK (LE31 v2-AI has no on-premise-LLM-as-feature surface today; charter §3.4 review needed) + Chroma OFF-STACK (LE31 v2-AI has no RAG-as-restaurant-context-window surface today; charter §3.7 review needed) + RAG ✓ ON-PATTERN + H5-QR-ordering OFF-STACK (LE31 v1 has the customer-QR-menu feature 11; v2-AI has no H5-QR-ordering surface yet) + SSE OFF-STACK (LE31 v1 has aiogram-driven-cook-bot; v2-AI has no SSE surface today; charter §3.4 review needed) + JWT ✓ ON-PATTERN + Docker ✓ ON-PATTERN (single-binary-deploy posture is portable) + ChartJS OFF-STACK (UI-only; OFF-§3.1 unless explicitly named in v2-AI charter). Evidence strength: medium-high for vocabulary; low for code adoption. |
| 4 | Conflict | ✓ | Does not violate any invariant. The *dual-track intent parsing (LLM + rules) + Ollama + local-Qwen3-4B + RAG-over-Chroma* primitives are §3.1 + §3.4-aligned (rules-own-canonical-intent-state-machine + non-AI-fallback-first + on-premise-LLM-as-feature). The *Ollama + local-Qwen3-4B* posture IS the §3.4 *non-AI-fallback-first* invariant. No §3.4 customer-facing AI outside the AI-waiter surface. No data rule violation (charter §3.7 PII review needed: the *Chroma RAG* posture might ingest customer-PII if RAG ever ingests customer-memo; charter-decision needed). |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI defer outcome (LLM-waiter-as-feature surface for the LE31 v2-AI). Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The vocabulary reference cost is ~30 min documentation; the LE31 v2-AI surfaces (planned agent-governance + AI-assisted) may adopt the *dual-track-intent-parsing + LLM-as-residual-only-parser + on-premise-Ollama-local-Qwen3-4B + RAG-over-Chroma* discipline; the reference is *naming*, not new build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. The handbook + HANDOFF can be reverted by `git rm` of the file. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass; build verdict `defer` because the code is not adoptable today (Flask + SQLite + LangChain + Chroma + Chinese-language stack off-LE31-v2-AI-stack + no v2-AI LLM-waiter-as-feature surface in v2-AI charter + Italian-only market scope). The vocabulary IS portable.

## Bucket

**v2-AI** (LLM-waiter-+-dual-track-intent-parsing-+-RAG-+-H5-QR-ordering-+-real-time-admin-dashboard-+-on-premise-+-Ollama-+-local-Qwen3-4B-vocabulary) — the *vocabulary* is the value, not the code. The verbatim description + topics name the 13-tuple-primitive set (LLM-powered-AI-waiter + H5-QR-ordering + dual-track intent parsing (LLM + rules) + RAG + real-time admin dashboard + Flask + SQLite + Ollama/Qwen3-4B + LangChain + SSE + JWT + ChartJS + Docker + Chinese-language) + the tech-stack (Python + Flask + SQLite + LangChain + Ollama + Qwen3-4B + RAG + SSE + JWT + ChartJS + Docker + github-actions + Chroma + openpyxl + AI-assistant + admin-dashboard + pos-system + chinese + restaurant + llm + qwen).

## Files to touch

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *dual-track-intent-parsing + LLM-as-residual-only-parser + Ollama + local-Qwen3-4B + RAG-over-Chroma* discipline lands, the files to touch are:

- `backend/alembic/versions/` — add migration for `IntentRule`, `Intent`, `MenuChroma`, `OrderItem`, `OrderEvent` tables.
- `backend/services/intent_rule_parser.py` — new file with `IntentRuleParser` class (regex + lookup-table rules; ALWAYS tried first; the §3.1 *rules-own-canonical-intent-state-machine* posture).
- `backend/services/intent_llm_parser.py` — new file with `IntentLLMParser` class using Ollama + local Qwen3-4B (charter §3.4 *non-AI-fallback-first* + §3.4 *on-premise-LLM-as-feature* posture).
- `backend/services/dual_track_intent_parser.py` — new file with `DualTrackIntentParser` class (rules first; LLM only on rule-miss; the §3.4 *LLM-as-residual-only-parser* invariant).
- `backend/services/menu_chroma.py` — new file with `MenuChroma` class (RAG over Chroma for restaurant-context-window; the §3.7 *RAG-as-restaurant-context-window* posture).
- `backend/services/order_event_sse.py` — new file with `OrderEventSse` class for SSE-fed admin dashboard (the §3.4 *observable-evidence* posture).
- `backend/llm/ollama_client.py` — new file with `OllamaClient` class (wraps Ollama + local Qwen3-4B; the §3.4 *non-AI-fallback-first* posture).
- `frontend/templates/h5-qr-menu.html` — new minimal-HTML/HTMX template for the customer-facing-H5-QR-ordering surface.
- `frontend/templates/admin-dashboard.html` — new minimal-HTML/HTMX template for the operator-facing-admin-dashboard (ChartJS rendered via minimal-HTML).
- `frontend/static/qr-menu-app.js` — new minimal-JS for the H5-QR-customer-facing-app.
- `backend/main.py` — wire the new sub-apps into the parent uvicorn app.
- `tests/test_intent_rule_parser.py` — new unit test for `IntentRuleParser`.
- `tests/test_intent_llm_parser.py` — new unit test for `IntentLLMParser`.
- `tests/test_dual_track_intent_parser.py` — new unit test for `DualTrackIntentParser` (verify rules-first; LLM-on-rule-miss).
- `tests/integration/test_order_event_sse.py` — new integration test for `OrderEventSse`.

## Verification protocol reference

When the first v2-AI PR that adopts the *dual-track-intent-parsing + LLM-as-residual-only-parser + Ollama + local-Qwen3-4B + RAG-over-Chroma* discipline lands, the verification protocol is:

1. Run `pytest tests/test_intent_rule_parser.py` and verify the `IntentRuleParser` produces a valid intent for the rule-matching inputs.
2. Run `pytest tests/test_intent_llm_parser.py` and verify the `IntentLLMParser` produces a valid intent for the rule-missing inputs.
3. Run `pytest tests/test_dual_track_intent_parser.py` and verify the `DualTrackIntentParser` ALWAYS tries rules FIRST and only fires the LLM on rule-miss.
4. Run `pytest tests/integration/test_order_event_sse.py` and verify the SSE-fed admin dashboard receives the order events correctly.
5. Run `uvicorn backend.main:app` and curl the admin-dashboard endpoint to verify the SSE-fed admin dashboard is callable.
6. Inspect the `Intent` table in Postgres and verify every intent-state-transition is recorded (the §3.3 append-only-ledger invariant).
7. Open `frontend/templates/h5-qr-menu.html` in a browser and verify the customer-facing-H5-QR-ordering surface renders the menu and accepts orders.
8. Verify Ollama + local Qwen3-4B is running locally and the `IntentLLMParser` calls it correctly.

## Rollback path

**None today.** The defer artifact is documentation only.

When the first v2-AI PR that adopts the *dual-track-intent-parsing + LLM-as-residual-only-parser + Ollama + local-Qwen3-4B + RAG-over-Chroma* discipline lands, the rollback path is:

1. `git revert <commit-sha>` to revert the migration.
2. `alembic downgrade -1` to drop the five tables.
3. Delete the files listed in "Files to touch" above.
4. Restart uvicorn.
5. Stop the Ollama + local Qwen3-4B service.

## Mandatory LE31 skill list

The external coding agent MUST load these LE31 skills before any code is written:

- `skills/le31-conventions/SKILL.md` — for all hard rules and the seven-check feature gate.
- `skills/le31-v1-feature-pattern/SKILL.md` — for the v1 feature contract shape and slicing rules.
- `skills/le31-research/SKILL.md` — for the research workflow and report shape.
- `skills/le31-feature-pipeline/SKILL.md` — for the feature pipeline (lease to coding agent).
- `skills/le31-handoff-spec/SKILL.md` — for the handoff spec (this file).
- `skills/le31-coding-agent-brief/SKILL.md` — for the paste-in brief.
- `skills/le31-backend/SKILL.md` — for the backend conventions (if applicable).
- `skills/le31-frontend/SKILL.md` — for the frontend conventions (if applicable).
- `skills/le31-data/SKILL.md` — for the data conventions (if applicable).
- `PROJECT_CHARTER.md` — for the project charter.
- `HANDOFF.md` — for the project handoff notes.

## Trigger condition

This defer artifact is documentation only. It becomes a build trigger when the **first v2-AI PR that adds an LLM-waiter-as-feature surface to the LE31 v2-AI** lands. At that point:

1. Re-run the seven-check feature gate (this artifact is `defer`; the new surface may shift it to `build` or `experiment`).
2. Decide which intent-parsing discipline (rules-only vs rules-first-LLM-fallback vs LLM-only) becomes the `DualTrackIntentParser`.
3. Decide which LLM (Ollama + local Qwen3-4B vs remote-Claude-Sonnet vs local-Llama-3-8B) becomes the `IntentLLMParser`.
4. Decide which RAG-over-Chroma corpus (menu-only vs menu + restaurant-context vs menu + dietary-restrictions) becomes the `MenuChroma`.
5. Apply charter §3.7 PII review to the *Chroma RAG* surface before any v2-AI PR.
6. Apply charter §3.7 Italian-only-market-scope review to the *Chinese-language + RAG* surface before any v2-AI PR.
7. Adopt the *dual-track intent parsing + LLM-as-residual-only-parser + Ollama + local-Qwen3-4B + RAG-over-Chroma* discipline on the chosen surface.

## Reversibility

The defer artifact is **fully reversible** (vocabulary-only). The handbook + HANDOFF can be reverted by `git rm` of the file. No code today; no migration; no rollback needed.

## Sign-off gap

None today. The defer artifact is documentation only; no v2-AI code is shipped.
