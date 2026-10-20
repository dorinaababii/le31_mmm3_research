# HANDOFF — 319-ganon3264-focus-mit-llm-as-roleplay-frontend-local-llm-session-state-htmx-self-hosted-fastapi-python

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-20
**Active feature path**: `/opt/data/le31_mmm3_research/features/319-ganon3264-focus-mit-llm-as-roleplay-frontend-local-llm-session-state-htmx-self-hosted-fastapi-python-v2-ai-local-llm-self-hosted-fastapi-htmx-session-state-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v2-AI roadmap is unspecified; the peer value is *local-LLM-+-FastAPI-+-HTMX-+-session-state-+-self-hosted vocabulary for a future v2-AI PR that adds a self-hosted-LLM-frontend-with-session-state-+-operator-only-access surface*, not *adoption*; the *roleplay* domain is OFF-§3.4 customer-facing-AI and would require §3.4 review if ever surfaced to restaurant diners; only the *vocabulary* is portable, NOT the *roleplay-domain-shape*.)

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `ganon3264/focus` GitHub repo (MIT, **★9 / 0⑂ = the 3rd-highest in-window 2026 star count of any net-new v2-AI Python+FastAPI+HTMX+local-LLM+self-hosted pick of the 81-pass research series**; **WEAK SIGNAL DISCLOSURE**: 9★/0⑂ is on the lower-end of in-window pick star counts and is NOT offered as evidence of restaurant need; the transferable item is the *local-LLM-+-FastAPI-+-HTMX-+-session-state* vocabulary, not the *roleplay* itself; language Python ✓ ON-STACK, **pushed 2026-10-18T20:04:18Z AND created 2026-07-19T00:13:30Z = IN-WINDOW BY BOTH FIELDS**, by `ganon3264`) as a dated, in-window **structural-evidence peer** for LE31's v2-AI self-hosted-LLM-frontend-with-session-state-+-operator-only-access substrate.

If the trigger condition (LE31 first proposes a v2-AI surface that wants *self-hosted-LLM-frontend-with-session-state-+-operator-only-access* primitives, OR a future v2-AI owner decision questions whether the self-hosted-LLM-+-FastAPI-+-HTMX-+-session-state approach is healthy in 2026) is met, the external coding agent should:

1. Load this artifact and the parent daily-research report (`/opt/data/le31-daily-research-2026-10-20.md`).
2. Load the `focus` repo: `https://github.com/ganon3264/focus` — README + the LLM-integration + the session-state-store if available.
3. Load the companion features 297 (`yevheniidehtiar/hyper-admin` Pydantic-native FastAPI admin + HTMX) + 317 (`borhanst/fastapi-admin-kit` zero-config-FastAPI-admin-panel-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first) + 318 (`Matthew-Selvam/Open-Dispatch` one-API-+-10-social-platforms-+-self-hosted-+-Buffer/Hootsuite-alternative-+-FastAPI-+-HTMX-+-Telegram-as-channel) + 325 (`AlexisLD-DEV/qramen` QR-code-table-ordering-PWA) + 343 (`warpusTOM/StockWise_Group6_BT-204` offline-first-inventory-+-POS-vocabulary) + 345 (`alissonlittig/vitrine-erp` multi-store-desktop-POS-+-ERP) — these are the persistent *self-hosted-+-FastAPI-+-HTMX-+-Python* sister-cluster.
4. Re-run the LE31 feature gate with `focus`'s README in hand.
5. **Decide whether the proposed v2-AI surface benefits from `focus`'s local-LLM-+-FastAPI-+-HTMX-+-session-state-+-self-hosted framing**. If the v2-AI surface wants *self-hosted-LLM-frontend-with-session-state-+-operator-only-access*, `focus`'s *vocabulary* (FastAPI + HTMX + local-LLM + session-state + self-hosted) IS purpose-built for that use case. **The *roleplay* domain is OFF-§3.4 customer-facing-AI**; any v2-AI PR adopting the `focus` vocabulary MUST verify the surface stays operator-tooling-AI not customer-facing-AI per §3.4.
6. **If `focus`'s vocabulary is proposed for adoption**: verify the underlying local-LLM-runtime is portable (LE31 v1 has no AI-runtime; v2-AI roadmap is unspecified; the *vocabulary* IS adoptable IF the local-LLM-runtime IS portable; Ollama + Qwen2.5-7B is the canonical v2-AI local-LLM-runtime choice), add to a side-branch `requirements-focus.txt` (do not pin to main yet), and build a single-operator prototype: register one LLM-inference-runtime (e.g., Ollama with a small model like Qwen2.5-7B) with the frontend; verify that the session-state + chat-history work end-to-end for a single menu-engineering suggestion. Compare against the LE31 v1 *manual-handling-of-every-action* discipline. **Verify the surface stays operator-tooling-AI not customer-facing-AI** per §3.4 (the prototype should be served only to authenticated operators, not to restaurant diners). If the local-LLM-+-FastAPI-+-HTMX-+-session-state-+-self-hosted discipline is meaningfully stronger AND the §3.4 verification passes, propose a v2-AI surface adoption; if not, document the comparison and defer.
7. **If `focus`'s vocabulary is not adopted**: document the comparison and defer. No charter §3.1 change is needed because the *local-LLM + FastAPI + HTMX + session-state + self-hosted* posture is a v2-AI surface, not a stack change (charter §3.1 doesn't specify LLM-inference-runtime; the v2-AI roadmap has not adopted one yet).
8. **Pilot on one action first**. Do not adopt `focus`'s vocabulary project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/319-ganon3264-focus-mit-llm-as-roleplay-frontend-local-llm-session-state-htmx-self-hosted-fastapi-python-v2-ai-local-llm-self-hosted-fastapi-htmx-session-state-vocabulary.md`
- **Parent daily-research report**: `/opt/data/le31-daily-research-2026-10-20.md`
- **Raw fetches**: `/tmp/le31-daily-2026-10-20/github_search/g4.json` (parent-verified raw JSON has `full_name=ganon3264/focus` + `stargazers_count=9` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-18T20:04:18Z` + `created_at=2026-07-19T00:13:30Z` + `description="A roleplaying frontend for use with LLMs."` + `size=4883` + `topics=[chatbot, fastapi, fastapi-backend, htmx, llm, llm-frontend, local-llm, roleplay, roleplay-ai, roleplay-chat, self-hosted, sillytavern-alternative]` = **12 topics = 11/12 LE31-relevant** (the OFF-§3.4 `roleplay`/`roleplay-ai`/`roleplay-chat`/`sillytavern-alternative` keywords are off-domain; the *vocabulary* (FastAPI + HTMX + local-LLM + self-hosted + chatbot) IS portable)
- **`focus` repo**: `https://github.com/ganon3264/focus` (parent-fetched 2026-10-20 metadata)
- **Companion artifacts**:
  - `features/297-yevheniidehtiar-hyper-admin-Pydantic-native FastAPI admin.md` (Pydantic-native FastAPI admin)
  - `features/317-borhanst-fastapi-admin-kit-zero-config-FastAPI-admin-panel-with-auto-CRUD-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first-vocabulary.md` (zero-config-FastAPI-admin-panel-+-RBAC-+-audit-logs-+-Tailwind/HTMX-+-SQLModel-first)
  - `features/318-Matthew-Selvam-Open-Dispatch-one-API-to-dispatch-content-to-10-social-platforms-+-self-hosted-+-Buffer/Hootsuite-alternative-+-FastAPI-+-HTMX-+-Python-+-Telegram-+-YouTube-+-TikTok-vocabulary.md` (one-API-+-10-social-platforms-+-self-hosted-+-Buffer/Hootsuite-alternative-+-FastAPI-+-HTMX-+-Telegram-as-channel)
  - `features/325-AlexisLD-DEV-qramen-QR-code-table-ordering-PWA.md` (QR-code-table-ordering-PWA)
  - `features/343-warpusTOM-StockWise_Group6_BT-204-offline-first-inventory-+-POS-vocabulary.md` (offline-first-inventory-+-POS-vocabulary)
  - `features/345-alissonlittig-vitrine-erp-multi-store-desktop-POS-+-ERP-vocabulary.md` (multi-store-desktop-POS-+-ERP-vocabulary)
- **Charter §3.1 (Python 3.13 + FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`
- **Charter §3.4 (chokepoint + human-gate + boundary-guard + router + non-AI-fallback + observable-evidence)**: `focus`'s *local-LLM + self-hosted + operator-only-access* posture IS canonical §3.4 *chokepoint-governed + operator-only-access + observable-evidence + non-AI-fallback* charter invariant applied to the *v2-AI operator-tooling-AI* dimension; the *roleplay* domain IS OFF-§3.4 customer-facing-AI and would require §3.4 review if ever surfaced to restaurant diners.
- **Charter §3.7 (privacy-first)**: `focus`'s *self-hosted + local-LLM + no-third-party-LLM-call* posture IS canonical §3.7 *self-hosted-privacy* invariant — no PII leaves the operator's VPS.

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.1 stack, §3.2 open-source dependency whitelist, §3.3 append-only ledger, §3.4 chokepoint + human-gate + non-AI-fallback, §3.7 privacy-first).
- `le31-v1-feature-pattern` — for the canonical contract shape (only relevant if the defer is promoted to build; note: this is a v2-AI pick, not a v1 pick, so the v1 pattern is informative but not directly applicable).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-feature-pipeline` until the defer is promoted to build by the LE31 owner (and note: `le31 v2-AI` project does NOT exist per `le31-feature-pipeline/SKILL.md` line 33; sub-issue would be attached to `le31 Research` P-HMM-1 as parent).

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-daily-2026-10-20/github_search/g4.json` JSON to confirm `full_name=ganon3264/focus` + `stargazers_count=9` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-18T20:04:18Z` + `created_at=2026-07-19T00:13:30Z` + `description` = `"A roleplaying frontend for use with LLMs."` + `size=4883` + `topics=[chatbot, fastapi, fastapi-backend, htmx, llm, llm-frontend, local-llm, roleplay, roleplay-ai, roleplay-chat, self-hosted, sillytavern-alternative]` = **12 topics = 11/12 LE31-relevant**.
- **GitHub canonical read**: GET `https://api.github.com/repos/ganon3264/focus` (HTTP 200; parent-verified 2026-10-20).
- **Anti-fabrication canary**: `grep -lF 'ganon3264/focus'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `ganon3264`, `focus` against features 1–318 = only this feature 319.
- **WEAK SIGNAL DISCLOSURE protocol**: feature-file states explicitly that 9★/0⑂ is on the lower-end of in-window pick star counts and is NOT offered as evidence of restaurant need; the transferable item is the *local-LLM-+-FastAPI-+-HTMX-+-session-state* vocabulary, not the *roleplay* itself.

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/319-ganon3264-focus-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/319-ganon3264-focus-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).
