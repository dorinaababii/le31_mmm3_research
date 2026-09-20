# 204 — docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2-AI orchestration surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/204-docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration.md` (defer artifact; **no code today**).

Bucket: **v2-AI orchestration (architecture-reference)**. Build verdict: **`defer`** (charter §3.1 + §3.4 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce multi-stage AI-assisted operations (e.g., AI-suggested menu updates, AI-suggested reconciliation), the owner wants *a multi-stage explicit-state-transition surface with observable evidence + non-AI fallback*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant) and v1's Order.status state machine is not extensible to multi-stage AI workflows*, so that *v2 can offer AI assistance without violating §3.4 or re-architecting v1*." **PASS** (zero-pain today; v1 is small enough that single-stage transitions are sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium-high for the architectural match (the *State is a deterministic fold of events + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* primitive set is well-established in the GitHub Apache-2.0-community-adoption cluster). Apache-2.0 license is charter-compatible per §3.2 (more permissive than MIT in some senses — explicit patent grant — less permissive in others — explicit patent termination clause; both Apache-2.0 and MIT are acceptable permissive licenses per charter §3.2). **PASS**. |
| 4 | **Conflict** | None. The *State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; operator-tooling with observable evidence + non-AI fallback; governed core is operator-tooling, adapters require §3.4 review before shipping). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI orchestration (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/204-docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration-HANDOFF.md` and `features/204-docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2-AI trigger condition fires (first v2-AI PR that introduces multi-stage AI-assisted operations with explicit-state-transitions + observable-evidence + non-AI-fallback):

- `app/models/state_derivation_view.py` — possibly add a `state_derivation_view` SQLModel table (view_name, view_definition, dependencies); the *deterministic-fold-of-events* discipline from dagwell.
- `app/models/stock_entry.py` — possibly add `prepared_at + received_at + approved_at` columns to `StockEntry` (nullable for backward compatibility); the *executed != completed* discipline from dagwell.
- `app/models/order_status.py` — possibly add `transport_evidence + output_evidence + approval_evidence` columns to `Order.status`; the *completion-needs-three-evidence-types* discipline from dagwell.
- `app/policy/governed_core.py` — possibly add a `governed_core` policy / config layer that gates which AI-assisted operations are permitted; the *governed-core-without-adapters* discipline from dagwell.
- `app/state/state_derivation_engine.py` — possibly add a Python module that computes derived views from the event stream; the *deterministic-fold* primitive from dagwell.
- `app/orchestration/provider_agnostic.py` — possibly add a provider-agnostic LLM-orchestration layer (any LLM provider can be plugged in without changing the core).
- `app/bot/prep_status.py` — possibly add a Telegram-bot command for the cook to view the *prepared_at + received_at + approved_at* distinction (e.g., `/prep-status <stock_entry_id>`).
- `app/bot/order_status.py` — possibly add a Telegram-bot command for the owner to view the *three-evidence-types status* on an Order (e.g., `/order-status <order_id>`).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [x] `features/204-docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration.md` exists and is read back by the parent.
- [x] `specs/204-docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration-HANDOFF.md` (this file) exists and is read back by the parent.
- [x] The GitHub repo description is quoted verbatim: *"Provider-agnostic orchestration engine that runs agent work as a governed graph over an event-sourced, append-only ledger. State is a deterministic fold of events, never stored. executed != completed: completion needs transport + output evidence + approvals. Governed core implemented; no adapters yet."*
- [x] The Apache-2.0 permissive license is documented (parent-verified against raw JSON; subagent's MIT claim corrected).
- [x] The *State is a deterministic fold of events, never stored + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* quintuple-primitive set is documented.
- [x] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/` + INDEX.md row + parent research report file.

**Future v2-AI trigger (when the first v2-AI PR that introduces multi-stage AI-assisted operations lands):**
- [ ] The PR is read back by the parent.
- [ ] The *State is a deterministic fold of events + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* primitive set is evaluated against the PR's changes: does the change preserve *append-only posture*? Does the change add *deterministic-fold*? Does the change add *executed-but-not-completed*? Does the change add *three-evidence-types*? Does the change add *governed-core-without-adapters*?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2-AI surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `state_derivation_view` table; remove the new `prepared_at + received_at + approved_at` columns from `StockEntry`; remove the new `transport_evidence + output_evidence + approval_evidence` columns from `Order.status`; remove the new `governed_core` policy; remove the new `state_derivation_engine` module; remove the new `provider_agnostic` orchestration layer; restore the original schema.
- Migration cost: depends on the v2-AI change; the *State is a deterministic fold + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters* primitive set's design implies *additive schema* (the new `state_derivation_view` table is additive on top of the existing append-only log; the new columns on `StockEntry` and `Order.status` are additive on top of the existing schemas).
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

## 7. Handoff summary

| Field | Value |
|---|---|
| Feature ID | 204 |
| Slug | `docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration` |
| Bucket | v2-AI orchestration (architecture-reference, parking-lot defer) |
| Parent research issue | linear: blocked (workspace plan limit; see /opt/data/le31-daily-research-2026-09-20.linear-fallback.json); intended title `Research 2026-09-20 — daily` |
| Linear sub-issue | linear: blocked (workspace plan limit); intended title `Feature 204 — docentesIA-dagwell-apache-2-0-event-sourced-append-only-ledger-orchestration-engine-deterministic-fold-v2-ai-orchestration` |
| Status today | defer (parking-lot) |
| No code today | yes |
| Verifiability today | feature file + HANDOFF file + INDEX.md row + parent research report file |
| Trigger condition (future v2-AI) | first v2-AI PR that introduces multi-stage AI-assisted operations with explicit-state-transitions + observable-evidence + non-AI-fallback |
| Disable path | delete `features/204-...md` + `specs/204-...-HANDOFF.md` |
| Migration cost | additive schema only (depends on v2-AI change) |
| Retained data | none |
| Parent research report | `/opt/data/le31-daily-research-2026-09-20.md` (52nd consecutive daily-research pass) |
| Raw fetches path | `/tmp/le31-daily-2026-09-20/` (68 files; anti-fabrication canary 0/67) |
| Linear fallback path | `/opt/data/le31-daily-research-2026-09-20.linear-fallback.json` |
| License | Apache-2.0 ✓ (parent-verified; charter §3.2 compatible) |
| GitHub repo | `docentesIA/dagwell` (1star/0forks, Python, 422 KB, pushed 2026-09-16T16:11:24Z) |
| Topics (verbatim) | none (empty array; description-only signals) |
| Description (verbatim) | *"Provider-agnostic orchestration engine that runs agent work as a governed graph over an event-sourced, append-only ledger. State is a deterministic fold of events, never stored. executed != completed: completion needs transport + output evidence + approvals. Governed core implemented; no adapters yet."* |
| LE31-shape-score | 2 (description-only signals; *State is a deterministic fold + executed != completed + completion needs transport + output evidence + approvals + governed core without adapters*) |
| Companion artifacts | features 148, 173, 176, 183, 186, 187, 188, 189, 192, 193, 195, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 203 (sister-pick A), 205 (sister-pick C) (ripgrep-verified distinct) |
| Sister-picks from 2026-09-20 | feature 203 (shawn-durrani/membro v2-AI control-plane), feature 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference) |

## 8. Verification log

*(Empty — to be populated by the parent if/when the future v2-AI trigger condition fires.)*

---

**OPERATOR NOTE (2026-09-20):** Today's Linear MCP write endpoint returned a workspace plan-limit error (`You've exceeded the free issue limit for this workspace` — carry-over from 2026-09-19); per `le31-daily-research/SKILL.md` hard rule, the parent research issue + the 3 Linear sub-issues were NOT created today. The fallback JSON at `/opt/data/le31-daily-research-2026-09-20.linear-fallback.json` documents the intended issues for resync after the workspace quota resets. The feature files + HANDOFFs were written to the repo regardless, per spec hard rule *"treat the report file as the source of truth; the Linear issue is the index"*.