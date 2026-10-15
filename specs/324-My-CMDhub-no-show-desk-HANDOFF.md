# HANDOFF — 324-My-CMDhub-no-show-desk

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today)
**Date**: 2026-10-15
**Active feature path**: `/opt/data/le31_mmm3_research/features/324-My-CMDhub-no-show-desk-mit-morning-no-show-desk-small-motels-tabpfn-flags-risky-bookings-local-gemma-drafts-reconfirm-message-code-checks-every-fact-fastapi-langgraph-telegram-bot-v2-ai-tabpfn-local-gemma-small-motel-no-show-forecasting-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 does not need to *use* `My-CMDhub/no-show-desk`; LE31 v1 has no AI agent; the v2-AI roadmap has no *operator-side predictive-forecasting-with-fact-verification* surface; the peer value is *v2-AI cross-section vocabulary for a future v2-AI PR that adds an AI-assisted operator-side surface*, not *adoption*.) **Note**: subagent's `pushed_at` value `2026-10-14T07:50:54Z` was corrected by parent to `2026-10-14T07:50:41Z` (13-second discrepancy, parent-verified via direct GitHub API GET).

## Trigger policy

This is a **defer artifact (parking-lot)** — a watch-list entry. It does not start a build. It surfaces the `My-CMDhub/no-show-desk` GitHub repo (MIT, **0★ / 0⑂**, **270 KB modest**, language Python ✓ ON-STACK + FastAPI + LangGraph + TabPFN + local Gemma + Telegram-bot + code-checks-every-fact, **pushed 2026-10-14T07:50:41Z AND created 2026-10-14T07:36:00Z = IN-WINDOW BY BOTH FIELDS** = 1-day-old repo) as a dated, in-window **structural-evidence peer** for LE31's potential v2-AI *operator-side predictive-forecasting-with-fact-verification* surface.

If the trigger condition (LE31 first proposes a v2-AI surface that wants *predictive-forecasting-on-historical-data-with-fact-verification* OR *local-LLM-as-edge-inference-for-drafted-messages* OR *code-checks-every-fact-before-publish* OR *Telegram-bot-glue-for-operator-side-forecast-review* primitives, OR a future owner decision questions whether LE31 v2-AI should adopt TabPFN or local-LLM as the deterministic-prediction-and-edge-inference primitives) is met, the external coding agent should:

1. Load this artifact and the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-15.md`).
2. Load the `no-show-desk` repo: `https://github.com/My-CMDhub/no-show-desk` — README + `no_show_desk/` source if available.
3. Load the companion features 232 (lpalbou/AbstractGateway — durable AI control plane) + 287 (noise01/endoxa — governed beliefs for LLM agents) + 288 (pete-builds/mcp-nixreview — advisory NixOS change-review with CVE attestation gate) + 289 (shivamk01here/LedgerLoop — Python runtime for financial AI agents with idempotent exactly-once execution) + 299 (A220man/human-approval-console — approval receipts) — all v2-AI agent-orchestrator + chokepoint + human-gate + append-only-ledger vocabulary references.
4. Re-run the LE31 feature gate with `no-show-desk`'s README in hand.
5. **Decide whether the proposed v2-AI surface benefits from `no-show-desk`'s TabPFN + local-Gemma + code-checks-every-fact framing**. If the v2-AI surface wants *predictive-forecasting-on-historical-data-with-fact-verification*, `no-show-desk` is purpose-built for that use case. If the v2-AI surface only wants the existing feature 05 waiter-tip-capture, `no-show-desk` adds no value.
6. **If `no-show-desk` is proposed for adoption**: pin to a specific version, add to `requirements-noshowdesk.txt` (do not pin to v1 yet), and add a single test forecast call against a single historical-booking from the LE31 owner-side data. Compare against the hand-written equivalent. If the test forecast adds predictive-forecasting-value, propose a v2-AI extension to feature 05 / new v2-AI surface; if not, document the comparison and defer.
7. **If `no-show-desk` is not adopted**: document the comparison and defer. No charter §3.1 change is needed because `no-show-desk` is a v2-AI-agent-runtime library, not a v1 stack change.
8. **Pilot on one historical-booking first**. Do not adopt `no-show-desk` project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Mandatory inputs

- **Active feature**: `features/324-My-CMDhub-no-show-desk-...md`
- **Parent daily-brainstorm report**: `/opt/data/le31-brainstorm-2026-10-15.md`
- **Raw fetches**: `/tmp/le31-brainstorm-2026-10-15/gh_topic_hospitality_python.json` (where `My-CMDhub/no-show-desk` is listed; parent-verified raw JSON has `stargazers_count=0`, `forks_count=0`, `license.spdx_id=MIT`, `pushed_at=2026-10-14T07:50:41Z` (parent-corrected from subagent's `2026-10-14T07:50:54Z`), `created_at=2026-10-14T07:36:00Z`, `description="Find out which guests won't turn up, days before they don't. A morning no-show desk for small motels: TabPFN flags risky bookings, local Gemma drafts a reconfirm message, code checks every fact."`, `size=270`, `topics=[fastapi, gemma, hospitality, langgraph, local-llm, no-show, tabpfn, tabular-data, telegram-bot, webgpu]`)
- **`no-show-desk` repo**: `https://github.com/My-CMDhub/no-show-desk` (parent-fetched 2026-10-15 metadata; verify-via-direct-GitHub-API-GET at `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_My-CMDhub_no-show-desk.json`)
- **Companion artifacts**:
  - `features/232-lpalbou-AbstractGateway-...md` (the first durable-AI-control-plane v2-AI reference — `no-show-desk` would extend with predictive-forecasting)
  - `features/287-noise01-endoxa-...md` (governed beliefs for LLM agents — `no-show-desk` would extend with the local-Gemma + fact-verification pattern)
  - `features/288-pete-builds-mcp-nixreview-...md` (advisory NixOS change-review with CVE/KEV attestation gate — `no-show-desk` is the hospitality analogue)
  - `features/289-shivamk01here-LedgerLoop-...md` (Python runtime for financial AI agents with hash-chained-audit-ledger — `no-show-desk` would extend with the predictive-forecasting pattern)
- **Charter §3.4 (chokepoint-governed + human-gate + non-AI-fallback + observable-evidence)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`

## Mandatory LE31 skill list

The external coding agent must load:
- `le31-conventions` — for the seven-check feature gate and the hard invariants (charter §3.4 chokepoint-governed + human-gate + non-AI-fallback + observable-evidence; §3.7 PII-on-device for local-LLM).
- `le31-feature-pipeline` — for the v2-AI bucket semantics (although per `le31-feature-pipeline/SKILL.md` line 33, the workspace does not have a `le31 v2-AI` project; v2-AI surface attaches to `le31 Research` parent).
- `le31-research` — for the source-of-truth discipline on GitHub repo verification (always verify stars/forks/licence/`created_at`/`pushed_at` from raw API JSON).

The agent must NOT load `le31-v1-feature-pattern` because this is a v2-AI surface (the v1-feature-pattern does not apply).

## Verification protocol reference

- **Read-back protocol**: parent-re-parse the raw `/tmp/le31-brainstorm-2026-10-15/gh_topic_hospitality_python.json` JSON to confirm `full_name=My-CMDhub/no-show-desk` + `stargazers_count=0` + `forks_count=0` + `license.spdx_id=MIT` + `pushed_at=2026-10-14T07:50:41Z` (parent-corrected from subagent's `07:50:54Z`) + `created_at=2026-10-14T07:36:00Z` + `description = "Find out which guests won't turn up, days before they don't. A morning no-show desk for small motels: TabPFN flags risky bookings, local Gemma drafts a reconfirm message, code checks every fact."` + `size=270` + `topics=[fastapi, gemma, hospitality, langgraph, local-llm, no-show, tabpfn, tabular-data, telegram-bot, webgpu]`.
- **GitHub canonical read**: GET `https://api.github.com/repos/My-CMDhub/no-show-desk` (HTTP 200; parent-verified 2026-10-15; raw JSON at `/tmp/le31-brainstorm-2026-10-15/verify/ghverify__parent_My-CMDhub_no-show-desk.json`).
- **Anti-fabrication canary**: `grep -lF 'My-CMDhub/no-show-desk'` across `/opt/data/le31_mmm3_research/features/*.md` = 0 matches outside this feature file (parent-verified).
- **Distinct-from-features**: ripgrep-verified `no-show-desk` against features 1–323 = only this feature 324.

## Rollback path

This defer artifact is fully reversible:
- **Delete the feature file**: `rm /opt/data/le31_mmm3_research/features/324-My-CMDhub-no-show-desk-...md`.
- **Delete the HANDOFF**: `rm /opt/data/le31_mmm3_research/specs/324-My-CMDhub-no-show-desk-...-HANDOFF.md`.
- **No code change was made today**, so no rollback of code is required.
- **No database migration was made today**, so no rollback of schema is required.
- **No pin change was made today** (LE31 pin set unchanged: fastapi==0.118.0 + sqlmodel==0.0.42 + aiogram==3.31.0 + sqlalchemy>=2.0,<2.1).
- The TabPFN + Gemma + LangGraph stack would add new pin entries (`tabpfn>=0.1.10` + `gemma-cpp>=0.1` + `langgraph>=0.0.30`) on a future v2-AI PR; today no pins are added.
