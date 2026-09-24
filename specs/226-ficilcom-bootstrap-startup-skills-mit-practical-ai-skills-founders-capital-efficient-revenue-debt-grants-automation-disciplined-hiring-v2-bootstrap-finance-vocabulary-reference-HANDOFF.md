# 226 — ficilcom/bootstrap-startup-skills v2-bootstrap-finance-vocabulary-reference HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 bootstrap-finance operator-tooling question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/226-ficilcom-bootstrap-startup-skills-mit-practical-ai-skills-founders-capital-efficient-revenue-debt-grants-automation-disciplined-hiring-v2-bootstrap-finance-vocabulary-reference.md` (defer artifact; **no code today**).

Bucket: **v2 bootstrap-finance-vocabulary-reference (AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring + small-business + startup, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate; **§3.4 NOT triggered** because the *claude-code* AI posture is *operator-tooling-AI not customer-facing-AI*).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a bootstrap-finance operator-tooling surface (expansion from a single-restaurant-vertical product to a founder-facing-financial-discipline product that supports multiple vertical-business-types, or expansion to a standalone-revenue-debt-grants-tracking product, or expansion to a standalone-automation-as-force-multiplier product), what is the *AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring* vocabulary that preserves the existing v1 single-restaurant-vertical posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 649 KB with 2★/0⑂ + MIT permissive license + 9 topics + in-window-by-both-fields is shipping the *AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring* primitive as the v2 bootstrap-finance operator-tooling discipline*, but struggles because *v1 has no documented bootstrap-finance operator-tooling primitive in the charter*, so that *v2 can introduce the bootstrap-finance + AI-agents-as-operator + solo-operator-discipline vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no bootstrap-finance operator-tooling trigger; the JTBD is primitive vocabulary extension + AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring documentation, not a build-need; **cross-section JTBD value is MEDIUM** — the only 2026-09-24 GitHub Search candidate that pins all of `agent-skills + ai-agents + bootstrapping + finance + founders + small-business` simultaneously; the *claude-code* AI posture is *operator-tooling-AI not customer-facing-AI* = §3.4 NOT triggered). |
| 2 | **Viability** | Maintainer can read 649 KB repo description + 9-topic vocabulary + AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring octuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no bootstrap-finance operator-tooling surface today). Confidence: medium for the *AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring* vocabulary (2★/0⑂ + MIT permissive license + 9 topics including 6 LE31-relevant primitives + in-window-by-both-fields + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *AI-skills-as-operator-tooling* posture IS the *charter §3.1 explicit-state-transition discipline applied to the operator-tooling-AI dimension*; the *bootstrapping + capital-efficient* discipline IS the *small-business-capital-discipline* posture; the *finance + revenue + debt + grants* discipline IS the *bootstrap-finance-modules* vocabulary). Stack: FastAPI + SQLModel + PostgreSQL backend = on-pattern for v1 primitives (matches v1 charter §3.2 baseline); bootstrap-finance = off-pattern for v1 (LE31 v1 has no finance module today); AI-skills = off-pattern for v1 (LE31 v1 has no AI surface today); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the bootstrap-finance operator-tooling dimension* (every financial state transition is an explicit SQLModel row; no silent transition). Charter §3.1 alignment (the *AI-skills-as-operator-tooling* posture IS the *explicit-state-transition + single-tenant* discipline applied to the *founder-facing-financial-discipline* dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive); **§3.4 NOT triggered** (the *claude-code* AI posture is *operator-tooling-AI not customer-facing-AI*; the AI runs in the developer's IDE not in the customer's chat; the *claude-code* topic explicitly names the *developer-coding-agent* primitive which is on-pattern for LE31 v1's *no-AI-surface* discipline). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 bootstrap-finance-vocabulary-reference; **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 649 KB repo + add cross-section to existing `HANDOFF.md` (1 hour) + future source-code-inspection follow-up (1-2 hours; 649 KB small-repo size makes inspection feasible). **Cost-to-value ratio: medium** (the *AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring* octuple + the 6/9 topic-overlap score + the in-window-by-both-fields signal need to be referenced; the cross-section JTBD value is moderate because LE31 v1 has no finance module today). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/226-ficilcom-bootstrap-startup-skills-mit-practical-ai-skills-founders-capital-efficient-revenue-debt-grants-automation-disciplined-hiring-v2-bootstrap-finance-vocabulary-reference-HANDOFF.md` and `features/226-ficilcom-bootstrap-startup-skills-mit-practical-ai-skills-founders-capital-efficient-revenue-debt-grants-automation-disciplined-hiring-v2-bootstrap-finance-vocabulary-reference.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + AI-skills + bootstrapping + finance + founders + automation + disciplined-hiring documentation for the next v2 bootstrap-finance operator-tooling review moment; **cross-section JTBD value is MEDIUM** — the only 2026-09-24 GitHub Search candidate that pins all of `agent-skills + ai-agents + bootstrapping + finance + founders + small-business` simultaneously; **§3.4 NOT triggered** because the *claude-code* AI posture is *operator-tooling-AI not customer-facing-AI*).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a bootstrap-finance operator-tooling surface to the LE31 v2 operator surface, a founder-facing-financial-discipline surface, a revenue-debt-grants surface, an automation-as-force-multiplier surface, or a disciplined-hiring surface):

- `app/finance_modules/` — possibly add (the bootstrap-finance module directory; depends on the v2 change).
- `app/finance_modules/revenue.py` — possibly add (the income-tracking handler; depends on the v2 change).
- `app/finance_modules/debt.py` — possibly add (the payable-tracking handler; depends on the v2 change).
- `app/finance_modules/grants.py` — possibly add (the grants-tracking handler; depends on the v2 change).
- `app/finance_modules/automation.py` — possibly add (the founder-automation handler; depends on the v2 change).
- `app/models/finance_revenue.py` — possibly add (the `finance_revenue` SQLModel table; depends on the v2 change).
- `app/models/finance_debt.py` — possibly add (the `finance_debt` SQLModel table; depends on the v2 change).
- `app/models/finance_grants.py` — possibly add (the `finance_grants` SQLModel table; depends on the v2 change).
- `app/models/finance_automation.py` — possibly add (the `finance_automation` SQLModel table; depends on the v2 change).
- `tests/test_finance_modules.py` + `tests/test_finance_revenue.py` + `tests/test_finance_debt.py` + `tests/test_finance_grants.py` — possibly add (the integration tests for the bootstrap-finance + revenue + debt + grants surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no bootstrap-finance operator-tooling surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

- **No code today**, so no verification protocol applies.
- **Future v2 verification protocol** (if the trigger condition fires):
  1. **License verification** — re-fetch `https://api.github.com/repos/ficilcom/bootstrap-startup-skills/license` to confirm `spdx_id: 'MIT'`.
  2. **Stack-shape verification** — confirm `ficilcom/bootstrap-startup-skills` source uses Claude Code skills + AI-agents primitives by inspecting `app/` or `src/` directory.
  3. **Bootstrap-finance verification** — confirm `ficilcom/bootstrap-startup-skills` source has finance + revenue + debt + grants modules.
  4. **Automation verification** — confirm `ficilcom/bootstrap-startup-skills` source has automation + disciplined-hiring modules.
  5. **§3.4 verification** — confirm any AI surface in `ficilcom/bootstrap-startup-skills` source is *operator-tooling-AI* not *customer-facing-AI*. **This is the load-bearing charter-compliance check** for any future v2 surface that imports `bootstrap-startup-skills` vocabulary.
  6. **Integration test verification** — verify the adapted vocabulary primitives work against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack.
  7. **Telegram surface verification** (if a Telegram surface is added in v2) — verify the adapted vocabulary primitives send correct aiogram messages with no hallucinated text.
- **Anti-fabrication canary**: `grep -c 'LE31' <bootstrap-startup-skills-source-file>` must return 0 — the bootstrap-startup-skills source is independent of LE31 and any "verbatim" quotes must not mention LE31.

## 5. Rollback path

**Fully reversible.** The defer artifact is documentation only. Disable/delete path:
- `git rm specs/226-ficilcom-bootstrap-startup-skills-mit-practical-ai-skills-founders-capital-efficient-revenue-debt-grants-automation-disciplined-hiring-v2-bootstrap-finance-vocabulary-reference-HANDOFF.md`
- `git rm features/226-ficilcom-bootstrap-startup-skills-mit-practical-ai-skills-founders-capital-efficient-revenue-debt-grants-automation-disciplined-hiring-v2-bootstrap-finance-vocabulary-reference.md`
- No migration, no SQLModel schema rollback, no FastAPI route removal, no Telegram handler removal required.
- No retained data; no safe-failure-mode concern.

If a future v2 PR has already added a bootstrap-finance operator-tooling surface based on this vocabulary reference, the rollback path includes:
- Remove the v2 surface code (depends on the v2 change).
- Remove the v2 SQLModel tables (depends on the v2 change).
- Remove the v2 FastAPI routes (depends on the v2 change).
- Remove the v2 Telegram handlers (depends on the v2 change).
- Re-run LE31 v2 test suite to confirm no regression.

## 6. Mandatory LE31 skill list

The coding agent **MUST** load and follow these skills before any future v2 implementation (none apply today):

- `le31-conventions` — the master skill for v2 development conventions; §3.1 explicit-state-transitions, §3.2 license-compatible-only, **§3.4 no-customer-facing-AI** (the load-bearing §3.4 check for any v2 surface that imports bootstrap-startup-skills vocabulary).
- `le31-v1-feature-pattern` — the v1 feature template pattern that informs the v2 surface shape.
- `le31-handoff-spec` — the handoff spec that documents the slice contract.
- `le31-coding-agent-brief` — the coding-agent brief that produces the paste-in prompt from the slice contract.
- `le31-verification-protocol` — the verification protocol that defines what "done" means.
- `le31-feature-pipeline` — the feature pipeline that produces the deliverables.
- `le31-daily-research` — the daily research skill that produced this artifact.
- `le31-daily-brainstorm` — the daily brainstorm skill that produced this artifact.
- `le31-v2-feature-pattern` — the v2 feature template pattern (if it exists; otherwise this skill is not loaded).

**No skill loading required today.** The defer artifact is documentation only; the coding agent does not need to load any skill because there is no code change.

---

**Summary**: defer (parking-lot); v2 bootstrap-finance-vocabulary-reference; no code today; MIT ✓ §3.2 STRICTLY-COMPATIBLE; **§3.4 NOT triggered** because the *claude-code* AI posture is *operator-tooling-AI not customer-facing-AI*; cross-section JTBD value is MEDIUM (the only 2026-09-24 GitHub Search candidate that pins all of `agent-skills + ai-agents + bootstrapping + finance + founders + small-business` simultaneously); 6/9 topic-overlap score; sister-shape to features 102 + 178 + 220.