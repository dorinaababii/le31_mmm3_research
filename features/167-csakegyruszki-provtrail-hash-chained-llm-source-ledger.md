# Feature 167 — csakegyruszki-provtrail-hash-chained-llm-source-ledger (defer)

> **NEW observation (2026-09-13).** Documents in-window GitHub repo `csakegyruszki/provtrail` (MIT, **0★/0⑂**, Python, **pushed 2026-09-12T10:00:09Z**, in-window by push only, **created 2026-09-11** — 2-day-old repo, 169 KB). Description (verbatim from GitHub API): *"Append-only, hash-chained ledger for recording the sources used in LLM-assisted research."* Topics: `chain-of-custody`, `claude-code`, `llm`, `mcp`, `provenance`, `python`, `research`. Has a PyPI release at https://pypi.org/project/provtrail/ (verified via parent fetch 2026-09-13). Bucket: **v2-AI architecture-reference (charter §3.4 territory; AI agent ledger primitive; Claude Code + MCP is staff-tooling, not customer-facing)** — watch-list defer. Zero build time today.

## Goal

Retain the **"append-only, hash-chained ledger for recording the sources used in LLM-assisted research"** primitive as a persistent cross-section reference for any future LE31 v2 surface that proposes an LLM-assisted recommendation visible to a customer, or the first v2 surface that records which documents the cook's Telegram bot referenced before pushing a stock recommendation. The artifact is the persistent cross-section reference + a candidate *chain-of-custody + Claude Code + MCP* vocabulary for the next v2-AI control-plane surface. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"append-only, hash-chained ledger"** primitive: every entry is *append-only* (no row is updated), the chain is *hash-chained* (each entry's hash includes the previous entry's hash), so tampering with any single entry is detectable. This is the load-bearing primitive for any future LE31 surface that records "which sources did the AI consult to suggest this?" with non-repudiation.
- A written record of the **"chain-of-custody"** sub-primitive (one of the GitHub topics): the audit chain must record the *complete provenance trail* — who/what created the entry, when, with which inputs, citing which downstream outputs.
- A written record of the **"claude-code + mcp"** tool integration: provtrail is designed to be installed as an MCP server by Claude Code (Anthropic's CLI coding agent), so any time Claude Code makes a tool call, provtrail records the source. The MCP integration is *staff-tooling* (developer workflow), not customer-facing AI — charter §3.4 does not trigger.
- A decision record: today's verdict is `defer` because LE31 v1 has no LLM-assisted surface (charter §3.4 explicitly rules out customer-facing AI; no v2 owner-facing surface has been designed yet).

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot (charter §3.1: explicit state transitions; v1 surfaces are sufficient for v1 ops).
- Any change to LE31 v1's `audit_logs` schema.
- Any new LLM-assisted surface (LE31 v1 has no LLM integration today; introducing one would require a charter §3.4 owner decision).
- Adoption of the provtrail codebase (the repo is 2 days old, 169 KB, MIT Python; the *primitive* is portable; the *codebase* is not adoptable without a full read-and-eval).
- Cross-pollination with charter §3.4 AI surface (the *LLM-assisted research sources* framing is staff-tooling, not customer-facing; if a v2 surface ever exposes LLM-assisted suggestions to a customer, this primitive becomes a hard requirement, not an option).

## Evidence / JTBD

When a future LE31 v2 surface proposes an LLM-assisted recommendation (e.g. "based on last week's sales, prep 12 pieces of cake tomorrow"), the owner wants *a primitive that records which sources the AI consulted to make that recommendation*, but struggles because *LE31 v1 has no LLM integration and no audit-trail vocabulary for AI sources*, so that *the v2 surface can answer "why did the AI suggest this?" with a chain-of-custody proof*.

- **Evidence class**: observed (the provtrail description + topics name the primitive explicitly: `chain-of-custody`, `claude-code`, `llm`, `mcp`, `provenance`).
- **Confidence**: medium-high for the primitive match (the description is direct; the hash-chained ledger discipline is well-established in audit-log research; the MCP integration is verifiable via the PyPI release); low for transferability (the cook's Telegram bot does not use Claude Code today; the integration pattern is transferable only if LE31 v2 ever adopts an LLM).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no LLM integration; the v2 surface that would *use* the primitive doesn't exist.
- **The value is naming, not direct demand**: when the first v2 LLM-assisted surface lands (if/when the owner approves §3.4), the provtrail pattern is a ready-made *named primitive* — and the *chain-of-custody + Claude Code + MCP* vocabulary slot into feature 137 (NL-to-Executable-Obligations) + feature 145 (garde-fous-frozen-mandate-append-only-agent-loop) + feature 127 (zero-shot-self-orchestration-Ledger-Based-Control) + feature 150 (Mandato MCP digitally-signed mandate) + feature 152 (LATTICE governance-first authorized AI).

## Description

GitHub `csakegyruszki/provtrail` (MIT, 0★/0⑂, Python, pushed 2026-09-12T10:00:09Z, created 2026-09-11, 169 KB) + PyPI `provtrail` (verified 2026-09-13). Description (verbatim): *"Append-only, hash-chained ledger for recording the sources used in LLM-assisted research."*

The architectural primitive has one core principle and three sub-primitives:

1. **"Append-only, hash-chained ledger"** — a *ledger* is a sequence of records; *append-only* means new records are added but old records are never modified; *hash-chained* means each entry's hash includes the previous entry's hash, so the chain is tamper-evident.
2. **"Sources used in LLM-assisted research"** — every entry records *which sources* the LLM consulted: which documents, which tools, which previous entries, which user prompts. The source list is the *audit trail of the LLM's reasoning process*.
3. **"Chain-of-custody"** (topic) — the audit chain must record the *complete provenance trail* — who/what created the entry, when, with which inputs, citing which downstream outputs. This is the *forensic* discipline: every entry must be reconstructable from its recorded inputs.

**The 1:1 mapping onto LE31 v2 architecture (if/when §3.4 surfaces):**

| provtrail primitive | LE31 v2 equivalent | Charter section | Status |
|---|---|---|---|
| Append-only ledger | (LE31 v1 already has this for `StockEntry` + `audit_logs`) | §3.1 ✓ | **Implemented (v1)** |
| Hash-chained ledger | (LE31 v1 `audit_logs` is append-only but not hash-chained; charter §3.1 says "explicit state changes" but doesn't require hash-chaining) | §3.1 + v2 hardening | **Not implemented** — would require a hash-chained schema migration |
| LLM source provenance | (LE31 v1 has no LLM integration) | §3.4 (future v2) | **Not implemented** — requires §3.4 owner decision |
| MCP integration (Claude Code) | (LE31 v1 has no Claude Code integration; the cook Telegram bot is not Claude-Code-based) | v2-AI | **Not implemented** |
| Chain-of-custody | (LE31 v1 `audit_logs` records user_id + timestamp + action but not the complete provenance trail of inputs) | §3.1 + v2 hardening | **Not implemented** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that adds an LLM-assisted surface), the v2 schema migration would need:

- `ai_source_ledger` table (append-only): `id`, `ts`, `actor_user_id`, `source_type` (enum: `document` / `tool_call` / `previous_entry` / `user_prompt`), `source_uri`, `source_hash`, `parent_entry_id`, `entry_hash`. The `entry_hash` is computed as `sha256(parent_hash + canonical_json(this_entry))` — this is the *hash-chain* discipline.
- `audit_logs` may need a `chain_head_hash` field to record the head of the chain at the time of the audit-log entry (so the audit chain and the source chain can be cross-validated).

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v2 implementation would include:
1. Create the `ai_source_ledger` SQLModel class.
2. Add the `chain_head_hash` field to `audit_logs`.
3. Wire the MCP server registration into the cook Telegram bot handler so any future Claude Code integration automatically appends to `ai_source_ledger`.
4. Add a v2 surface that exposes the chain-of-custody proof to the owner (e.g. "why did the AI suggest 12 pieces?" → shows the chain of sources).

**No existing code change today.**

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

Future v2: if the cook Telegram bot ever adopts an LLM integration (charter §3.4 owner decision required), the bot would record every LLM source consultation to `ai_source_ledger` before executing any state-changing command. The Telegram bot is a *staff-tooling* surface (the cook, not a customer), so §3.4 does not trigger.

## Dependencies

- **Charter §3.4 owner decision** for any future v2 LLM-assisted surface. Without that decision, this primitive is documentation only.
- **Charter §3.1 invariant compatibility**: ✓ (append-only hash chain is the strongest form of "explicit state changes").
- **§3.2 license compatibility**: ✓ (provtrail is MIT permissive).
- **Stack compatibility**: ✓ (Python; MCP is a JSON-RPC protocol; SQLModel can hold the schema).

## Open questions

1. **Does LE31 v2 need an LLM-assisted surface at all?** The cook Telegram bot is highly functional today with deterministic commands. The v2 question is whether the cook would benefit from "based on last week's sales, prep 12 pieces of cake tomorrow" recommendations. This is an owner decision per charter §3.4.
2. **If yes, which LLM?** Claude Code + MCP is one option; an in-process model is another; a hosted API is a third. The provtrail primitive works with any of them, but the integration effort differs.
3. **What is the retention policy for `ai_source_ledger`?** v1 retention is "indefinite" (charter §3.1: append-only); v2 retention may want a rolling-window policy (drop entries older than N days) for GDPR reasons (CNIL §3.5). This is an owner decision.

## Why this matters

The **chain-of-custody + Claude Code + MCP** vocabulary is the **v2-AI control-plane vocabulary** that LE31 needs *before* it can answer the §3.4 question. Without this vocabulary, the first LLM-assisted surface would be a black box (the AI suggests something, the cook executes it, no audit trail exists). With this vocabulary, the first LLM-assisted surface can be defended: the owner can show a regulator "here is the chain of sources the AI consulted before suggesting 12 pieces." That defensibility is the **highest-leverage vocabulary addition** the 45-pass series has surfaced for the v2-AI question.

Companion artifacts: features 137 (NL-to-Executable-Obligations), 145 (garde-fous-frozen-mandate-append-only-agent-loop), 127 (zero-shot-self-orchestration-Ledger-Based-Control), 150 (Mandato MCP digitally-signed mandate), 152 (LATTICE governance-first authorized AI), 141 (KRINEIA five-invariants append-only as proof) — all ripgrep-verified distinct from this artifact.
