# 227 — wwilson1017/chatty v2-owner-assist-vocabulary-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 owner-assist AI-agent-platform question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/227-wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot.md` (defer artifact; **no code today**).

Bucket: **v2 owner-assist (AI-agent-platform-for-small-business + Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces an AI-assisted owner-facing surface (an AI-agent-platform for the owner to manage Gmail/QuickBooks/Todoist/Odoo/BambooHR integrations, a GTD-todo-system, a capture-from-anywhere surface beyond feature 29, a BYO-OAuth layer, a Telegram-multi-bot deployment, or a multi-integration layer), what is the *Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration* vocabulary that preserves the existing v1 single-restaurant-vertical posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 5.8 KB with 9★/5⑂ + MIT permissive license + 10 topics + in-window-by-pushed_at-only is shipping the *Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration* primitive as the v2 owner-assist discipline*, but struggles because *v1 has no documented AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration primitive in the charter*, so that *v2 can introduce the AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no AI-agent-platform trigger; the JTBD is primitive vocabulary extension + AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration documentation, not a build-need; **cross-section JTBD value is moderate-to-high** — the only in-window 2026 *small-business AI-agent-platform with LE31-shape posture* candidate of the 57-pass brainstorm series). |
| 2 | **Viability** | Maintainer can read 5.8 KB repo description + 10-topic vocabulary + AI-agent-platform + Local-first SQLite + browser-UI + GTD todos + capture-from-anywhere + BYO-OAuth + Telegram multi-bot + multi-integration octuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no AI-agent-platform surface today). Confidence: medium for the *AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration* vocabulary (9★/5⑂ + MIT permissive license + 10 topics + in-window-by-pushed_at-only + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *AI-agent-platform-for-small-business* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the operator-assist-by-AI dimension*; the *Local-first SQLite + browser-UI + GTD-todos + capture-from-anywhere + BYO-OAuth + Telegram-multi-bot + multi-integration* discipline IS the *operator-tooling + single-tenant + embedded-database posture* applied to the deployment-formalization dimension). Stack: FastAPI + SQLModel + PostgreSQL backend = on-pattern for v1 primitives (matches v1 charter §3.2 baseline); AI-agent-platform = off-pattern for v1 (LE31 v1 has no AI surface today); Local-first SQLite = on-pattern for v1 *development* (known-conflict per `le31-conventions/SKILL.md` lines 73-75); browser-UI = on-pattern for v1 (charter §3.1 = waiter web UI); GTD-todos = off-pattern for v1 (LE31 v1 has feature 69 owner-no-account-shift-recap-link but no GTD-todo-system); capture-from-anywhere = on-pattern for v1 (feature 29 owner-no-account-live-floor-link); BYO-OAuth = off-pattern for v1 (LE31 v1 has zero third-party OAuth today); Telegram-multi-bot = off-pattern for v1 (LE31 v1 has 1 bot per charter §3.1); multi-integration = off-pattern for v1 (LE31 v1 has zero third-party integration today); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the operator-assist-by-AI dimension* (every state transition is an explicit SQLModel row; no silent transition). Charter §3.1 alignment (the *AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration* discipline IS the *explicit-state-transition* applied to the operator-assist-by-AI dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive; SQLite is on-pattern for v1 development per known-conflict note); **§3.4 NOT triggered** (chatty is *operator/business-owner-facing*, NOT customer-facing-AI; the *§3.4 customer-facing-AI hard block* does not apply because chatty is a tool for the owner/staff, not a tool that interacts with restaurant diners; the *integrations* Gmail/QuickBooks/BambooHR are operator-side, not customer-side). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 owner-assist vocabulary-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 5.8 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours with caveat: 5.8 KB small-repo size limits inspection depth — the *vocabulary* is high-value, the *code* is reference-only). **Cost-to-value ratio: moderate-to-high** (the *AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration* octuple + the *structurally-identical-to-LE31-v1-deployment-posture* signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/227-wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot-HANDOFF.md` and `features/227-wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration documentation for the next v2 owner-assist AI-agent-platform review moment; **cross-section JTBD value is moderate-to-high, the only in-window 2026 *small-business AI-agent-platform with LE31-shape posture* candidate of the 57-pass brainstorm series**).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds an AI-assisted owner-facing surface, a third-party-integration (Gmail/QuickBooks/BambooHR/Todoist/Odoo), a capture-from-anywhere surface beyond feature 29, a BYO-OAuth layer, a Telegram-multi-bot deployment, a GTD-style todo system, or a multi-integration layer):

- `app/owner_assist/` — possibly add (the AI-agent-platform owner-assist module; depends on the v2 change).
- `app/owner_assist/agent.py` — possibly add (the AI-agent execution handler; depends on the v2 change).
- `app/owner_assist/integrations/` — possibly add (the third-party-integration adapters; depends on the v2 change).
- `app/owner_assist/oauth/` — possibly add (the BYO-OAuth credential layer; depends on the v2 change).
- `app/owner_assist/todos/` — possibly add (the GTD-todo-system; depends on the v2 change).
- `app/owner_assist/capture/` — possibly add (the capture-from-anywhere handler; depends on the v2 change).
- `app/bots/` — possibly add (the Telegram-multi-bot deployment; depends on the v2 change).
- `app/models/owner_assist.py` — possibly add (the owner-assist SQLModel tables; depends on the v2 change).
- `app/models/oauth_credentials.py` — possibly add (the BYO-OAuth credential SQLModel table; depends on the v2 change).
- `tests/test_owner_assist.py` + `tests/test_integrations.py` + `tests/test_oauth.py` + `tests/test_todos.py` + `tests/test_capture.py` + `tests/test_multi_bot.py` — possibly add (the integration tests for the owner-assist + integrations + oauth + todos + capture + multi-bot surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no AI-agent-platform surface added, no GTD-todo-system added, no BYO-OAuth layer added, no Telegram-multi-bot deployment added, no multi-integration layer added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/227-wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot.md` exists and is read back by the parent.
- [ ] `specs/227-wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `wwilson1017/chatty` description is quoted verbatim (5.8 KB repo).
- [ ] The 9★/5⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + in-window-by-pushed_at-only + 10 topics + description *"A free, open-source browser-based AI agent platform; great for personal agents, professional work agents and small business owners. Agent teams ready. Local-first or deployed. Odoo, Quickbooks Online, Google Workspace and BambooHR connection built in. Agent curated CRM system included."* is documented.
- [ ] The README primitives (browser-based UI + multi-agent + multi-provider AI + heartbeat + reminders + memory + meeting recording + playbooks + commitments + usage & cost dashboard + GTD todos + capture-from-anywhere + integrations + agent orchestration + file uploads + 2FA + brandable + BYO OAuth + Local-first SQLite + one-click deploy to Railway) are documented.
- [ ] The charter §3.1 alignment via *AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration = explicit-state-transition discipline applied to operator-assist-by-AI* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive; SQLite is on-pattern for v1 development per known-conflict note) is documented.
- [ ] The charter §3.4 NOT-triggered (chatty is operator/business-owner-facing, NOT customer-facing-AI; the §3.4 customer-facing-AI hard block does not apply) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds an AI-assisted owner-facing surface, a third-party-integration (Gmail/QuickBooks/BambooHR/Todoist/Odoo), a capture-from-anywhere surface beyond feature 29, a BYO-OAuth layer, a Telegram-multi-bot deployment, a GTD-style todo system, or a multi-integration layer lands):**
- [ ] The PR is read back by the parent.
- [ ] The `wwilson1017/chatty` *AI-agent-platform + GTD-todos + BYO-OAuth + Telegram-multi-bot + multi-integration* vocabulary is evaluated against the PR's changes: does the change address the *operator-assist-by-AI* discipline? does the change preserve the *Local-first SQLite + browser-UI + GTD-todos + capture-from-anywhere + BYO-OAuth + Telegram-multi-bot + multi-integration* posture? does the change preserve the *charter §3.1 explicit-state-transition* pattern? does the change preserve the *charter §3.4 operator-tooling boundary*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

Fully reversible. Delete `specs/227-wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot-HANDOFF.md` and `features/227-wwilson1017-chatty-mit-browser-based-ai-agent-platform-local-first-sqlite-browser-ui-gtd-todos-capture-from-anywhere-byo-oauth-telegram-multi-bot.md`. The git revert path is `git revert HEAD~0 -- features/227-...md specs/227-...-HANDOFF.md` (or whichever commit introduced the files). No retained data; no safe-failure-mode concern; no operator-visible behavior change.

## 6. Mandatory LE31 skill list

The coding agent MUST load and follow these skills before starting work on this HANDOFF (per `le31-coding-agent-brief/SKILL.md`):

- `le31-conventions/SKILL.md` — the canonical seven-check feature gate + the v1/v2/v2-AI bucket taxonomy.
- `le31-daily-brainstorm/SKILL.md` — the parent context for cross-section picks + the daily-brainstorm-no-fabrication-canary.
- `le31-daily-research/SKILL.md` — the sister daily-research skill for source-family coverage.
- `le31-feature-pipeline/SKILL.md` — the immediate parent skill for this HANDOFF.
- `le31-verification-protocol/SKILL.md` — the verification protocol referenced in §4.
- `le31-coding-agent-brief/SKILL.md` — the skill that produces the paste-in prompt-in prompt automatically from this slice contract; do not paste chat excerpts.
- `le31-handoff-spec/SKILL.md` — the skill that defines this HANDOFF format.
- `le31-v1-feature-pattern/SKILL.md` — the v1 feature pattern reference.

**Do not start any code work today.** The HANDOFF is documentation-only.

## 7. Honest disclosure

- The 9★/5⑂ is explicitly NOT offered as evidence of *LE31 needing the AI-agent-platform primitive*; the 9★/5⑂ is for the *AI-agent-platform-for-small-business* domain, not for the *Local-first SQLite + browser-UI + GTD-todos + capture-from-anywhere + BYO-OAuth + Telegram-multi-bot + multi-integration* primitive. The transferable item is the *technique*, not the *code*.
- The 5.8 KB size is small; source-code inspection depth is limited; the *vocabulary* is high-value, the *code* is reference-only.
- LE31 v1 today covers 4/8 of these primitives (SQLite ✓, browser-UI ✓, capture-from-anywhere = feature 29, GTD-todo-system = NOT-YET); chatty names the **5-missing-primitive checklist** (AI-agent-platform surface + multi-integration layer + Telegram-multi-bot + BYO-OAuth + GTD-todo-system).
- Charter §3.4 NOT triggered because chatty is operator/business-owner-facing, NOT customer-facing-AI.