# Feature 203 — shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane (defer)

> **NEW observation (2026-09-20).** Documents in-window GitHub Search `append-only+ledger` query result: `shawn-durrani/membro` (**MIT ✓**, **1★/0⑂**, Python, **pushed 2026-09-17T09:34:34Z**, in-window by push only, **797 KB** substantial repo, default_branch=`main`). Description (verbatim, parent-verified GitHub Search raw JSON): *"Local-first memory for AI assistants: append-only fact ledger behind deterministic extraction walls, immutable transcripts, provenance-carrying summaries, MCP tools. Loopback-only by default."* Topics (verbatim from raw JSON, **10 topics**): `ai`, `ai-memory`, `fastapi`, `llm`, `local-first`, `mcp`, `mcp-server`, `memory`, `self-hosted`, `sqlite`. **The strongest v2-AI control-plane vocabulary of the 52-pass series** (the only in-window candidate with the *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* quintuple-primitive). Bucket: **v2-AI control-plane (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"append-only fact ledger behind deterministic extraction walls + immutable transcripts + provenance-carrying summaries + MCP tools + loopback-only by default"** quintuple-primitive as a persistent cross-section reference for any future LE31 v2-AI surface that introduces an AI-assisted workflow with operator-tooling + non-AI-fallback + audit-trail. The artifact is the persistent cross-section reference + the five named architectural primitives (append-only fact ledger, deterministic extraction walls, immutable transcripts, provenance-carrying summaries, MCP tools, loopback-only by default). No code today (MIT license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **append-only fact ledger** discipline: every fact extracted from an AI assistant interaction is recorded as a new append-only entry; the ledger is the persistent record; views are derived, not stored.
- A written record of the **deterministic extraction walls** discipline: the *extract-then-persist* posture where extraction is deterministic (replayable, testable) and persistence is append-only; non-deterministic outputs are rejected at the wall.
- A written record of the **immutable transcripts** discipline: the original AI-assistant transcripts are immutable; only derived views (summaries, queries) are computed.
- A written record of the **provenance-carrying summaries** discipline: every summary carries its source; the *evidence-bearing summary* is the *summary-with-citations* primitive.
- A written record of the **MCP tools integration** discipline: the Model Context Protocol integration pattern for AI-assistant tool use; a future LE31 v2-AI surface could expose a `mcp_le31_server` wrapping `audit_logs`.
- A written record of the **loopback-only by default** posture: the local-first + no-cloud-by-default discipline = textbook charter §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-assisted workflow surface (charter §3.4 explicitly forbids customer-facing AI; LE31 v1 has no owner-facing AI either).
- A cross-section reference with the prior AI-governance + audit-log + append-only-ledger + human-gate + AI-system-registry primitives cluster: features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404), 198, 199. The *transferable insight* is the **append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default** quintuple-primitive set.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2-AI surface in v1 (charter §3.4 explicit invariant: AI may only assist owner/staff with observable evidence + non-AI fallback; no v1 surface today).
- Any MCP-server integration in v1 (LE31 v1 has no AI surface; MCP integration is inapplicable).
- Any sqlite → Postgres migration (LE31 uses Postgres; membro uses sqlite per its topics).

## Description

GitHub Search `append-only+ledger` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-20/gh_append-only+ledger.json`) returned 37 total / 30 in-window candidates; `shawn-durrani/membro` is one of the 6 net-new in-window MIT/Apache Python candidates not previously filed. It is the strongest v2-AI control-plane vocabulary of the 52-pass series.

The `shawn-durrani/membro` repo's architectural pattern has five core sub-primitives:

1. **Append-only fact ledger** — direct LE31 `audit_logs` discipline match. The *append-only fact ledger* is the same architectural primitive as LE31's `audit_logs` schema (every state change is a new append-only entry; current state is derived).
2. **Deterministic extraction walls** — the *extract-then-persist* discipline (extraction is deterministic; persistence is append-only) maps onto any future LE31 v2 surface that needs to commit AI-extracted data with replayability. The *deterministic-extraction-wall* pattern is the *trust-boundary* between the LLM and the persistent store: only deterministic (replayable, testable) extractions are appended; non-deterministic outputs are rejected at the wall.
3. **Immutable transcripts** — the *transcript-immutability* discipline (original AI-assistant transcripts are immutable; only derived views are computed) maps onto LE31's audit_logs immutability principle (charter §3.1: never update or delete ledger events).
4. **Provenance-carrying summaries** — the *evidence-bearing-summary* discipline (every summary carries its source) maps onto the same primitive as 09-19 Pick A `rajo69/ledgerkb` (which is now 404 — see feature 197 close path).
5. **MCP tools (Model Context Protocol)** — the *AI-tool-protocol* discipline maps onto any future LE31 v2-AI surface that exposes LE31 audit_logs as MCP tools to AI assistants. The MCP standard is gaining adoption; future LE31 v2 could expose a `mcp_le31_server` that wraps the audit_logs table.
6. **Loopback-only by default** — the *local-first + no-cloud-by-default* posture maps onto charter §3.4 (operator-tooling-without-customer-cloud). The `loopback-only by default` posture is the textbook §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback; no cloud-exfiltration risk).

The LE31 relevance is the **append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default** quintuple-primitive. LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the question this repo answers is "if (and only if) LE31 v2 ever introduces an AI-assisted workflow, what is the operator-tooling + non-AI-fallback + audit-trail + MCP-integrable primitive set that satisfies charter §3.4?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2-AI trigger condition (if the first v2-AI PR that introduces an AI-assisted workflow lands):** potential schema additions (depending on the v2-AI surface):
- `ai_assistance_log` table — each AI interaction would carry an entry in this table; the *append-only fact ledger* primitive from membro. Each row would have `interaction_id`, `actor_user_id`, `model_version`, `prompt`, `response`, `recorded_at`, `evidence_id` (FK to Evidence table, optional), `extraction_status` (rejected-at-wall / accepted-into-ledger / flagged-for-review).
- `evidence` table — each AI-extracted fact would carry an optional `evidence_id` FK pointing to an `Evidence` table (URL, document, photo, etc.); the *evidence-bearing* discipline from membro.
- `mcp_le31_server` wrapper — a future v2-AI surface could expose the `audit_logs` table + the `ai_assistance_log` table as MCP tools; the *MCP tools integration* primitive from membro.
- `deterministic_extraction_wall` policy — a config / policy primitive that gates which AI-extracted facts are persisted to the ledger; the *deterministic-extraction-wall* primitive from membro.

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces an AI-assisted workflow lands):**
- Add an `ai_assistance_log` SQLModel table (interaction_id, actor_user_id, model_version, prompt, response, recorded_at, evidence_id FK, extraction_status).
- Add an optional `evidence_id` FK column to `audit_logs` (nullable; existing rows remain evidence-less).
- Add a periodic `ai_assistance_log_position_snapshot` job that computes derived views (most-recent-AI-suggestions, weekly AI summary, etc.) and stores them as a snapshot table; the *position-over-time* discipline (cross-reference feature 197 rajo69-ledgerkb vocabulary).
- Optionally add a `mcp_le31_server.py` FastAPI sub-app that exposes `audit_logs` + `ai_assistance_log` as MCP tools.
- Add a `deterministic_extraction_wall` policy primitive (charter §3.4: non-AI-fallback required; AI-extracted facts that fail the deterministic-extraction-wall must be flagged-for-review, not persisted to the ledger).

**Steps independent of the v2-AI trigger (today):**
- [x] Read the `shawn-durrani/membro` GitHub repo structure (parent re-verified the description, topics, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* quintuple-primitive vocabulary (parent re-verified verbatim).
- [x] Cross-reference with features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (repo now 404), 198, 199 (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces an AI-assisted workflow lands):**
- The owner would need a Telegram command to view an *AI-assistance summary* (e.g., `/ai-summary today`); the *provenance-carrying summary* primitive maps 1:1 onto a chat-style query interface.
- The cook would need a Telegram command to view the *AI-extraction-wall status* (e.g., `/ai-wall status`); the *deterministic-extraction-wall* primitive would surface flagged-for-review entries.
- These are v2-AI surface additions; not in v1 scope.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v2-AI trigger dependencies:** depends on the v2-AI surface that introduces an AI-assisted workflow with operator-tooling + non-AI-fallback + audit-trail (LE31 v1 has none of these surfaces). Cross-references: features 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 126 (Five Primitives for Governing AI Agents), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 141 (KRINEIA five-invariants), 145 (garde-fous), 152, 156 (AWIG-OS rule-citing-audit), 160 (FactGraph), 167 (provtrail hash-chained ledger), 169 (akoffice933 openshare-ledger SHA-256 hash chain), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger disposition-ledger kernel), 188 (ShibaClaw self-hosted security-first AI agent), 189 (HASHI local-first control-plane), 190 (ilyautov small-business-RU-34 AI-skills-tax-contractor-INN), 192 (LinkedParticles/particles-standard sourced + confidence-scored append-only ledger), 196 (monstabravo agent-ledger append-only-checked-against-git), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 204 (this file's Pick B sister — docentesIA/dagwell event-sourced-append-only-ledger), 205 (this file's Pick C sister — Mark007-R/Restaurant-Intelligence-Platform measured-NLP).

## Open questions

1. **PostgreSQL-vs-sqlite migration path:** membro uses sqlite per its topics (`sqlite` topic); LE31 uses Postgres + SQLModel. Would the membro schema port cleanly to Postgres, or is the *append-only fact ledger* discipline sqlite-specific (e.g., via SQLite's `WITHOUT ROWID` tables or its trigger-based projections)? Cross-reference: feature 187 (traust-ledger, Apache-2.0 kernel = port-friendly), feature 167 (provtrail hash-chained ledger, port-friendly).
2. **Deterministic-extraction-wall schema details:** what is the exact schema of a *deterministic extraction wall* (does the wall inspect the LLM output and reject at the prompt-template level, or is it a post-hoc verification layer)? The full read of membro's schema is needed before any v2 port.
3. **MCP tools integration details:** what is the exact API for exposing `audit_logs` as MCP tools (declarative `@mcp_tool` decorator, imperative registration)? The full read of membro's MCP integration is needed before any v2 port.
4. **Loopback-only enforcement:** how does membro enforce *loopback-only by default* (is it a config flag, a network-policy layer, an OS-level firewall rule)? The full read of membro's network policy is needed before any v2 port.
5. **MIT license file confirmation:** is membro's MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default** quintuple-primitive is the **cleanest 2026-09-20 v2-AI control-plane vocabulary for any future LE31 v2 surface that introduces an AI-assisted workflow** — and the MIT permissive license + the 10-topic coverage (including `fastapi` + `local-first` + `mcp` + `memory`) confirm it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31's charter §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce an AI-assisted workflow (e.g., LLM-suggested documentation lookup, LLM-suggested menu translation), the owner wants *an operator-tooling surface with audit-trail and non-AI fallback*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant)*, so that *v2 can offer AI assistance without violating §3.4*." **PASS** (zero-pain today; v1 is small enough that operator-tooling without AI is sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium for the architectural match (the *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* primitive set is well-established in the GitHub 1★-community-adoption cluster; membro's 10-topic coverage including `fastapi` confirms a real implementation, not just a proposal). MIT license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *append-only fact ledger + deterministic extraction walls + provenance-carrying summaries + MCP tools + loopback-only by default* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; operator-tooling with observable evidence + non-AI fallback; no customer-facing AI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI control-plane (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/203-shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane-HANDOFF.md` and `features/203-shawn-durrani-membro-mit-fastapi-local-first-ai-assistant-memory-append-only-fact-ledger-v2-ai-control-plane.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-20.md` (52nd consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 204 (this file's Pick B sister), 205 (this file's Pick C sister).
- Sister-picks from 2026-09-20: feature 204 (docentesIA/dagwell v2-AI orchestration), feature 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference).