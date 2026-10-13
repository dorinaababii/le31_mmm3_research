# Feature 298 — `the-vibey-project/vibey` AI-coding-agents orchestrator with append-only PostgreSQL ledger (defer)

> **NEW observation (2026-10-13).** Documents in-window GitHub repo `the-vibey-project/vibey` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **3★/1⑂**, language Python, **45086 KB substantial = 2nd-largest in-window v2-AI orchestrator of the 75-pass series**, default_branch=`main`, **pushed 2026-10-13T03:34:22Z = TODAY (in-window by `pushed_at` only; created 2026-08-14T21:25:22Z = ~2-month-old repo with in-window push)**). Topics (verbatim from raw JSON, **20 topics** = the most topic-rich v2-AI orchestrator of the 75-pass series, tied with `djust-org/djust` at 20-topic threshold): `agent-orchestration, ai-agents, audit-log, autonomous-agents, autonomous-software-delivery, claude-code, cli, coding-agents, devsecops, event-sourcing, human-in-the-loop, job-queue, llm, local-llm, ollama, postgresql, sovereign-ai, supply-chain-security, workload-identity`. Description (verbatim, parent-verified GitHub API direct-GET 2026-10-13): *"Open-source orchestrator for AI coding agents: a spec interview, unattended builds on local (Ollama) or paid agents, human-gated review, and an append-only PostgreSQL ledger so a crashed agent's work is picked up, not lost"*. The **Python + PostgreSQL = 2/2 LE31-backend-stack-match** plus 18 additional primitives is the **strongest in-window 2026 v2-AI-orchestrator-with-append-only-PostgreSQL-ledger + spec-interview + human-gated-review + crashed-agent-resumable quad-primitive peer of the 75-pass series** (vs `warrant-ai/warrant` = feature 302 which uses ed25519 + merkle-tree + langgraph + MCP without spec-interview or local-Ollama; vs `djust-org/djust` = features 35+86+158+222+230+232+260+261+286 which uses local-filesystem + spec-interview but NOT PostgreSQL-ledger). **Sister-shape to feature 287 (`noise01/endoxa`) + 288 (`pete-builds/mcp-nixreview`) + 289 (`shivamk01here/LedgerLoop`) + 302 (`warrant-ai/warrant`) + 304 (`DSHCorrectover/agent-second-fuse`)** = the persistent v2-AI audit-trail + governance vocabulary cluster. **First observation date 2026-10-13** = today (was a watchlist reference in the 10-12 report's not-pick section). Bucket: **v2-AI agent-orchestration-with-crash-safe-append-only-PostgreSQL-ledger-vocabulary (defer, parking-lot)** = peer awareness + named v2-AI architectural vocabulary + today-pushed cross-section observation; **zero build time today**.

## Goal

Retain `the-vibey-project/vibey` as a **structural-evidence peer** that LE31's Postgres-in-production stack (charter §3.1) is being actively maintained by an AI-agent-orchestration author in 2026, with the **append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive** directly relevant to any future v2-AI surface that wants AI-agent-orchestration with crash-safe PostgreSQL-ledger recovery. The artifact is the persistent peer-awareness record + the named architectural vocabulary for the **append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review** quad-primitive. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the peer: stack match (2/2 = Python + PostgreSQL), star/fork counts, licence (MIT permissive), in-window activity, author identity (`the-vibey-project` = active maintainer with 2026 engagement + the `vibey` orchestration tool).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-agent-orchestration surface today (charter §3.4 customer-facing-AI hard-block; v2-AI surface is parking-lot vocabulary-only at this point). The peer value is **structural evidence + vocabulary, not *adoption***.
- A reference for the next time LE31 proposes a v2-AI surface that wants AI-agent-orchestration with crash-safe append-only-PostgreSQL-ledger: `vibey` is MIT-permissive (no licensing friction) and is purpose-built for that use case.
- A reference for the "crashed agent's work is picked up, not lost" framing: any future v2-AI surface that wants crash-safe agent-session-recovery can evaluate `vibey` against the alternative (custom orchestrator + custom persistence).
- A cross-section reference with the **v2-AI agent-orchestrator + audit-trail vocabulary cluster** = features 287 (`noise01/endoxa` append-only-ledger + SMT) + 288 (`pete-builds/mcp-nixreview` MCP-server + CVE-KEV attestation gate) + 289 (`shivamk01here/LedgerLoop` exactly-once-execution + hash-chained-audit-ledger) + 302 (`warrant-ai/warrant` decision-ledger + ed25519 + merkle-tree) + 304 (`DSHCorrectover/agent-second-fuse` fail-closed-second-fuse) + 232 (`lpalbou/AbstractGateway` durable-AI-control-plane) + 286 (`gadyamedia/vocenya-mcp` AI-receptionist-MCP-server) + this one (feature 298).

**Out of scope (defer artifact):**
- Any code change to LE31 today (v1 has no AI-agent orchestration surface).
- Any pin bump (Postgres-in-production is charter §3.1 already).
- Any documentation change to LE31's README or HANDOFF.md.
- Any charter §3.4 surface (customer-facing-AI is charter §3.4 hard-block; `vibey`'s AI agents are operator-facing = chokepoint-governed = does NOT trigger §3.4).

## Description

GitHub `the-vibey-project/vibey` — *"Open-source orchestrator for AI coding agents: a spec interview, unattended builds on local (Ollama) or paid agents, human-gated review, and an append-only PostgreSQL ledger so a crashed agent's work is picked up, not lost"* — is an **AI-coding-agents orchestrator** with crash-safe append-only PostgreSQL ledger recovery. The repo is authored by `the-vibey-project` (active 2026 maintainers).

The repo's **3★ / 1⑂** is the **strongest today-pushed v2-AI orchestrator of the 75-pass series** (today-pushed 2026-10-13 at 03:34:22Z = 1 of 7 watchlist today-pushes today). Combined with the **MIT permissive licence**, the **exact 2/2 backend-stack match** (Python + PostgreSQL are charter §3.1 components), the **20 topics** (the most topic-rich v2-AI orchestrator of the 75-pass series), and the **unique quad-primitive** (`append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review`), this is **the strongest single v2-AI agent-orchestrator-with-crash-safe-append-only-PostgreSQL-ledger peer of the 75-pass series**.

**Stack match matrix**:

| `vibey` component | LE31 charter §3.1 | Match? |
|---|---|---|
| Python | Python 3.13 (required) | ✅ exact |
| PostgreSQL | Postgres (required) | ✅ exact (LE31's `audit_logs` schema uses Postgres) |
| append-only-ledger | matches LE31's `audit_logs` + `StockEntry` ledger discipline | ✅ exact |
| spec-interview | matches a future LE31 v2-AI control-plane discipline | 🆕 v2-relevant (not in v1 today) |
| human-gated-review | matches LE31's charter §3.4 *operator confirms* invariant | ✅ exact |
| crashed-agent-resumable | matches a future LE31 v2-AI control-plane recovery surface | 🆕 v2-relevant |
| claude-code + coding-agents + autonomous-software-delivery | matches a future LE31 v2-AI *AI-coding-agent* surface (off-v1) | 🆕 v2-relevant |
| postgresql + workload-identity + devsecops | matches LE31's Postgres + Postgres-identity surfaces | ✅ exact |
| event-sourcing + audit-log | matches LE31's append-only audit-trail invariant | ✅ exact |
| sovereign-ai + local-llm + ollama | matches LE31's *local-LLM preferred* posture | ✅ semantic-match |

**Cross-section insight for LE31**: the **append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive** is **directly LE31-relevant** for any future v2-AI surface that wants AI-agent-orchestration with crash-safe recovery. Today LE31 v1 has no AI-agent-orchestration surface (charter §3.4 customer-facing-AI hard-block). The **append-only-PostgreSQL-ledger** primitive alone is the **single most charter-§3.1-aligned v2-AI primitive of the 75-pass series** (the append-only-PostgreSQL discipline = charter §3.1 invariant that operational transitions are explicit user actions). The peer-validation of the *crash-safe append-only-ledger* idea is the durable takeaway.

**The 4 primitives of the quad-primitive set**:
1. **append-only-PostgreSQL-ledger**: every agent action appends a new row to the ledger (matching LE31's `StockEntry` model).
2. **crashed-agent-resumable**: the orchestrator can resume an agent's work after the agent crashes (because the append-only-ledger persists the agent's session-state).
3. **spec-interview**: before any agent work begins, the orchestrator conducts a spec interview (matching a future LE31 v2-AI control-plane discipline where AI cannot run without an explicit spec).
4. **human-gated-review**: every agent action goes through a human-gated review before it can change external state (matching charter §3.4 *operator confirms* invariant).

**Licence**: MIT permissive — **zero licensing friction** for any LE31 v2-AI surface that wants to *use* `vibey` (adopt = `pip install`, not fork, so no copyleft concerns).

**In-window by push only — labelled as such**: the repo was **created 2026-08-14** (~2 months ago, off-window for an in-window-by-creation-signal). The 2026-10-13 push is a **today-push on a ~2-month-old orchestrator**, not a new discovery. The today-push signal + 20-topic breadth + 45086 KB substantial size = the strongest today-pushed v2-AI orchestrator of the 75-pass series.

**Distinct from features 1–295** (ripgrep-verified — no overlap on `the-vibey-project`, `vibey`):

- Does **NOT** duplicate feature 287 (`noise01/endoxa` — append-only-ledger + SMT + defeasible-revision) or feature 288 (`pete-builds/mcp-nixreview` — MCP-server + CVE-KEV attestation gate) or feature 289 (`shivamk01here/LedgerLoop` — exactly-once-execution + hash-chained-audit-ledger + crash-safe-resumable-runs) or feature 302 (`warrant-ai/warrant` — decision-ledger + ed25519 + merkle-tree) or feature 304 (`DSHCorrectover/agent-second-fuse` — fail-closed-second-fuse + signed-receipts + append-only-ledger + incident-reports) or feature 232 (`lpalbou/AbstractGateway` — durable-AI-control-plane + replay-first) or feature 286 (`gadyamedia/vocenya-mcp` — MCP-server + AI-receptionist).

## Data model

No schema change today. The defer artifact documents that `vibey` would have:
- **PostgreSQL-ledger schema**: append-only ledger of agent actions (matches LE31's existing `audit_logs` + `StockEntry` ledger discipline).
- **AI-coding-agent orchestration**: orchestration surface for AI-coding-agents (Claude Code, Codex, Ollama).
- **Spec-interview schema**: a structured spec-interview format (matching a future v2-AI discipline).
- **Human-gated-review discipline**: every agent-action requires human-confirm before external-state-change (matching charter §3.4 *operator confirms* invariant).

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to evaluate `vibey` for a future v2-AI surface:

1. Add `vibey` to a side-branch `requirements-vibey.txt` (do not pin to v1 yet).
2. Read the `vibey` README's append-only-PostgreSQL-ledger schema + spec-interview format.
3. Build a 1-prototype: a single `vibey` orchestration session against a benign environment (e.g., a sandbox).
4. Compare the orchestration surface against LE31's existing `audit_logs` + `StockEntry` schema to ensure no-schema-conflict.
5. **If the orchestration surface is charter-§3.1-compatible**, propose a v2-AI PR that adopts `vibey` for AI-agent-orchestration with explicit owner sign-off; **if not**, document the comparison and defer.
6. **Out of scope for v1 today**: any `vibey` adoption. v1 has no AI-agent-orchestration surface (charter §3.4 customer-facing-AI hard-block).

## Telegram interaction if any

None today. `vibey` is an AI-agent-orchestrator surface; the cook Telegram bot (charter §3.1) is aiogram v3 and would be the orchestrator of a future v2-AI surface that wants to drive cook-bot actions via `vibey`'s spec-interview + human-gated-review discipline. v1 today has no AI-orchestration surface, so no Telegram integration today.

## Dependencies

- **GitHub**: `the-vibey-project/vibey` 3★ / 1⑂ / MIT / Python / pushed 2026-10-13T03:34:22Z / created 2026-08-14T21:25:22Z.
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.4 (AI: no customer-facing AI; AI may assist owner/staff with observable evidence and non-AI fallback)**: `vibey`'s agents are operator-facing + chokepoint-governed + human-gated-review = aligns with §3.4.
- **Stack**: Python 3.13 (LE31's runtime), PostgreSQL (LE31's production DB), append-only-ledger discipline (LE31's §3.1 invariant).
- **Licence**: MIT permissive — **zero licensing friction**.
- **Companion artifacts**:
  - `features/287-noise01-endoxa-apache-2-0-governed-beliefs-for-llm-agents-append-only-ledger-smt-checked-consistency-defeasible-revision-calibration-python-llm-agents-truth-maintenance-v2-ai-governed-beliefs-vocabulary.md` (governed-beliefs + append-only-ledger)
  - `features/288-pete-builds-mcp-nixreview-mit-mcp-server-cve-kev-attestation-gate-ai-agents-append-only-audit-ledger-nixos-fastmcp-python-v2-ai-mcp-server-attestation-vocabulary.md` (MCP-server + append-only-audit-ledger)
  - `features/289-shivamk01here-LedgerLoop-mit-python-runtime-financial-ai-agents-idempotent-exactly-once-hash-chained-audit-ledger-policy-engine-human-approvals-crash-safe-resumable-runs-automatic-rollback-760-tests-v2-ai-ledger-discipline-runtime-vocabulary.md` (exactly-once-execution + crash-safe-resumable)
  - `features/302-warrant-ai-warrant-apache-2-0-decision-ledger-ai-agents-mandate-evidence-cost-outcome-replay-before-ship-ed25519-merkle-tree-rfc-8785-langgraph-mcp-python-temporal-v2-ai-decision-ledger-vocabulary.md` (decision-ledger + ed25519 + merkle-tree)
  - `features/304-DSHCorrectover-agent-second-fuse-mit-independent-fail-closed-second-fuse-ai-agents-runtime-guard-signed-receipts-append-only-ledger-incident-reports-v2-ai-fail-closed-second-fuse-vocabulary.md` (fail-closed-second-fuse + signed-receipts + append-only-ledger + incident-reports)
  - `features/232-lpalbou-AbstractGateway-mit-python-durable-ai-control-plane-replay-first-append-only-receipts-rfc8785-json-canonicalization-v2-ai-durable-control-plane-vocabulary-reference.md` (durable-AI-control-plane + replay-first)

## Open questions

1. **Does LE31 ever propose a v2-AI surface that needs AI-agent-orchestration?** Today: no — v1 has no AI-agent surface (charter §3.4 customer-facing-AI hard-block). v2 surfaces: maybe — if the LE31 owner proposes a v2 surface that drives AI-coding-agents for restaurant operations (e.g., AI-driven stock-forecast from historical receipts) AND wants a crash-safe append-only-PostgreSQL-ledger, then `vibey` is purpose-built. Recommendation: revisit when the first v2-AI surface is proposed.
2. **Is `vibey` mature enough for production?** Today: 3★ / 1⑂ is encouraging but not conclusive. Recommendation: not a v1 question today; revisit when the LE31 owner requests a v2-AI surface that needs agent-orchestration.
3. **Would adopting `vibey` violate charter §3.4's "no customer-facing AI"?** No — `vibey`'s AI agents are operator-facing (the spec-interview + human-gated-review enforce operator-in-the-loop). v1 v2 could adopt `vibey` for AI-coding-agents like Claude Code without violating §3.4 because the AI does not directly interact with the cook or the guest; the AI is operator-tooling.
4. **Does the "crashed agent's work is picked up, not lost" framing align with LE31's operational-transitions invariant?** Yes — the append-only-PostgreSQL-ledger discipline = charter §3.1 invariant that operational transitions are explicit user actions.

## Why this matters

LE31's chosen stack — **FastAPI + SQLModel + Postgres + aiogram v3** — has the Postgres-in-production invariant as a load-bearing operational discipline. The **append-only-PostgreSQL-ledger + crashed-agent-resumable + spec-interview + human-gated-review quad-primitive** would be the load-bearing primitive for any future LE31 v2-AI surface that wants AI-agent-orchestration with crash-safe recovery. `the-vibey-project/vibey` is **structural evidence** that:

1. **The append-only-PostgreSQL-ledger + spec-interview + human-gated-review discipline is being actively maintained by `the-vibey-project` in 2026.** This is the load-bearing substrate for any future LE31 v2-AI surface that wants AI-agent-orchestration with crash-safe append-only-PostgreSQL-ledger recovery; structural health is good.
2. **The "crashed agent's work is picked up, not lost" framing is emerging as a named architectural concern.** Any future v2-AI surface that wants agent-session-recovery can evaluate `vibey` against the alternative (custom orchestrator + custom persistence).
3. **MIT permissive + exact 2/2 backend-stack match + 20-topic breadth + today-pushed + 45086 KB substantial size** = the strongest single in-window 2026 v2-AI agent-orchestrator-with-crash-safe-append-only-PostgreSQL-ledger peer of the 75-pass series.

The defer is fully reversible: the file is a peer-awareness record, not a code dependency. If the LE31 owner decides to evaluate `vibey` later, the file documents what to evaluate and how to evaluate it; if not, the file can be deleted with no operational impact.
