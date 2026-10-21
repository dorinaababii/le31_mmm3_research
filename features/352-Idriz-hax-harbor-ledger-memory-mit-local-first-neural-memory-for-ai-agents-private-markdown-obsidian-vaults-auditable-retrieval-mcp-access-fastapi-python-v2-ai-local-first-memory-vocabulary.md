# Feature 352 — `Idriz-hax-harbor-ledger-memory-mit-local-first-neural-memory-for-ai-agents-private-markdown-obsidian-vaults-auditable-retrieval-mcp-access-fastapi-python-v2-ai-local-first-memory-vocabulary` (defer)

> **Pick C of Daily Research 2026-10-21.** Documents in-window GitHub repo `Idriz-hax/harbor-ledger-memory` (**MIT ✓ §3.2 permissive**, **★0/⑂0**, **1122 KB modest**, **Python ✓ ON-STACK** + **FastAPI ✓ ON-STACK**, **pushed 2026-10-14T10:00:20Z** = in-window by `pushed_at` (first day of the 8-day window), **created 2026-04-21T23:25:42Z** = ~5.5-month-old repo with in-window push, archived=false). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-21): *"Local-first neural memory for AI agents: private Markdown/Obsidian vaults, auditable retrieval, and MCP access."* Topics (verbatim, parent-verified, **6 topics**): `ai-agents, fastapi, information-retrieval, knowledge-graph, knowledge-management, local-first`. Bucket: **v2-AI** (parking-lot, vocabulary reference only). Build verdict: `defer`. **§3.7 posture: local-first + private vaults = no PII leaves the premises, which is the canonical LE31 privacy invariant applied to the AI-memory dimension.**

## Goal

Retain the **local-first-neural-memory + private-Markdown/Obsidian-vaults + auditable-retrieval + MCP-access + FastAPI** vocabulary as a persistent cross-section reference for the LE31 v2-AI *agent-memory* dimension, documenting the primitive an independent maintainer shipped in 2026 on the LE31 v1 stack. The artifact is a vocabulary reference + a demand signal for a future LE31 v2-AI memory surface. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **local-first + private-Markdown/Obsidian-vaults + auditable-retrieval + MCP-access** 4-tuple-primitive: an AI agent's memory lives in *private Markdown vaults* the owner controls (editable in Obsidian or any text editor), retrieval over those vaults is *auditable* (the agent can say which documents it used), and the memory is reachable by the agent *through an MCP surface* while remaining on-premise. **The transferable primitive is *memory-as-user-owned-files*:** the operator can read, edit, delete, and version-control what the agent "remembers", because the memory is a directory of Markdown rather than an opaque embedding store.
- A written record of the **Python + FastAPI + local-first** stack-shape: this is the **first `local-first` + `knowledge-management` + `knowledge-graph` + `MCP-access` agent-memory vocabulary on the exact LE31 v1 backend stack of the 82-pass series**.
- A written record of the *auditable-retrieval* posture: retrieval is not a black box; the retrieved documents are part of the observable output. This IS the canonical §3.4 *observable evidence* invariant applied to the *agent-memory-retrieval* dimension, and it is the closest §3.4 analogue to the §3.3 append-only-audit posture — instead of proving what the agent *did*, it proves what the agent *saw*.
- A written record of the *local-first* posture: nothing leaves the premises. This IS the canonical §3.7 *store only data needed for restaurant operations; v1 guest demographics are counts, not identity* invariant applied to the *agent-memory-store* dimension — an agent that reads restaurant documents must not exfiltrate them to a third-party embedding API.
- A decision record: today's verdict is `defer` because (1) LE31 has no AI surface and therefore no memory surface; (2) ★0 is not evidence of anything, in either direction; (3) the demand-signal (an independent maintainer shipped this on-stack in 2026) is the value, not the code-adoption opportunity.

**Out of scope:**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any AI surface in LE31 v1 (charter §3.4).
- Any vector-store / embedding-service dependency in LE31 v1.
- Adoption of the harbor-ledger-memory codebase (MIT permits it; the "neural memory" framing is off-domain and the ★0 signal is not adoption-grade evidence).

## Out of scope

- See the explicit out-of-scope list above. The defer artifact is **vocabulary-only**; no v1 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes *"an agent that remembers things about this restaurant, where the owner can read and edit what it remembers, and where nothing about the restaurant is sent to a third party"*, the owner wants *a primitive that proves memory-as-user-owned-Markdown-files is buildable on the LE31 stack*, but struggles because *LE31 has no precedent for an agent-memory surface and no established answer to "where does the agent's memory live?"*, so that *the v2-AI surface can be defended with "an independent MIT-licensed maintainer shipped local-first Markdown-vault agent memory on FastAPI + Python in 2026"*.

- **Evidence class**: **observed** (the verbatim description names `Local-first`, `private Markdown/Obsidian vaults`, `auditable retrieval`, `MCP access`; the 6 topics confirm `local-first`, `knowledge-management`, `knowledge-graph`, `information-retrieval`, `ai-agents`, `fastapi`).
- **Confidence**: **medium-high** for the vocabulary match (all 4 primitives named explicitly in the description; full LE31 backend-stack match); **low** for present urgency (zero owner mentions in 82 passes; ★0 provides no traction evidence).
- **Real observed LE31 JTBD**: **zero direct JTBD today.** The value is the vocabulary: when the first v2-AI memory surface is proposed, this is a ready-made *named primitive* that also happens to be the only one of the 82-pass series that satisfies the §3.7 privacy invariant *by construction* rather than by review.

## Description

GitHub `Idriz-hax/harbor-ledger-memory` (MIT ✓ §3.2, ★0/⑂0, 1122 KB modest, Python ✓ ON-STACK + FastAPI ✓ ON-STACK + ai-agent + information-retrieval + knowledge-graph + knowledge-management + local-first, pushed 2026-10-14T10:00:20Z, created 2026-04-21T23:25:42Z, archived=false). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-21): *"Local-first neural memory for AI agents: private Markdown/Obsidian vaults, auditable retrieval, and MCP access."*

The architectural primitive has sub-primitives that map onto LE31's charter invariants:

1. **Private Markdown/Obsidian vaults** — the agent's memory is a directory of Markdown files the owner can open in a text editor or Obsidian. This IS the canonical §3.1 *append-only / inspectable / file-based-persistence* posture applied to the *agent-memory* dimension: LE31's `StockEntry` ledger is inspectable because it is rows; a Markdown vault is inspectable because it is files. Sister-shape to features 126 (`five-primitives-governing-AI-agents-at-runtime`), 128 (`skill-state-scalable-long-horizon-agent-skills`), 134 (`echo-auditable-memory-plane`).
2. **Local-first** — the vault lives on the owner's own disk; no data leaves. This IS the canonical §3.7 *minimal-data / on-premise* invariant. Sister-shape to features 53 + 66 (offline-first, which are already first-external-field-validated by the 2026-08-28 *GeoJournal of Tourism and Geosites* study recorded in feature 130).
3. **Auditable retrieval** — when the agent recalls something, the retrieved source documents are part of the observable output. This IS the canonical §3.4 *observable evidence* invariant applied to the *retrieval* dimension. Sister-shape to feature 129 (`ledger-claim-to-evidence-trace-graph-audit` — the *claim-to-evidence edge* problem, solved here for the simpler *memory-to-source* case).
4. **MCP access** — the agent reaches its memory through an MCP tool surface rather than reading arbitrary paths. This IS the canonical §3.4 *chokepoint-governed* invariant applied to the *memory-read* dimension: the memory store is reachable through one controlled surface, not opened to the whole filesystem. Sister-shape to feature 334 (`pattern-mcp` — MCP server as an auditable decision ledger) and feature 351 (elodea — MCP tool calls as the policy chokepoint).
5. **FastAPI** — the memory service is an ordinary FastAPI app, not a bespoke runtime. This IS the canonical §3.1 *fixed stack* invariant verified on-stack.

The defer artifact retains the **5-tuple-primitive** (private-Markdown-vaults + local-first + auditable-retrieval + MCP-access + FastAPI-on-stack) as a persistent cross-section reference.

## Data model

N/A (defer artifact; vocabulary-only; no schema today).

When the first v2-AI memory-surface PR adopts this discipline, the shape is:

```sql
-- The vault is a set of Markdown FILES on the owner's disk. This table indexes them.
CREATE TABLE memory_document (
    id BIGSERIAL PRIMARY KEY,
    vault_relative_path TEXT NOT NULL UNIQUE,  -- e.g. 'suppliers/lamb.md'
    content_sha256 BYTEA NOT NULL,             -- integrity + change detection
    first_seen_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_modified_at TIMESTAMPTZ NOT NULL
);

-- Retrieval is AUDITABLE: every retrieval event records WHICH documents were used.
-- This is the 'what did the agent SEE' counterpart to LE31's 'what did the agent DO' audit.
CREATE TABLE memory_retrieval_event (
    id BIGSERIAL PRIMARY KEY,
    agent_surface TEXT NOT NULL,               -- which LE31 surface asked
    query_text TEXT NOT NULL,
    retrieved_document_ids BIGINT[] NOT NULL,  -- the exact source set (audit trail)
    retrieved_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    surfaced_to_operator BOOLEAN NOT NULL DEFAULT TRUE  -- always TRUE per §3.4
);

-- A memory write is an EXPLICIT event with a provenance record (charter §3.1: no silent mutation).
CREATE TABLE memory_write_event (
    id BIGSERIAL PRIMARY KEY,
    vault_relative_path TEXT NOT NULL,
    written_by TEXT NOT NULL,                  -- 'owner' or an agent-surface id
    reason TEXT NOT NULL,                      -- why the agent believed this changed
    written_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

**Stock impact**: none. **Money impact**: none. **§3.1 invariants preserved**: `memory_write_event` is append-only (never updated, never deleted); the vault files themselves are operator-owned and editable; `memory_retrieval_event.surfaced_to_operator` defaults to `TRUE` because §3.4 requires observable evidence — a retrieval that is not shown to the operator is not permitted.

## Implementation steps

**None today.** The defer artifact is documentation only.

When the first v2-AI memory-surface PR adopts this discipline:

1. Add `MemoryDocument` SQLModel table (index of the vault; the vault itself is plain files on disk, NOT a table).
2. Add `MemoryRetrievalEvent` SQLModel table (append-only; records the exact retrieved document set).
3. Add `MemoryWriteEvent` SQLModel table (append-only; provenance + reason for every agent-initiated write).
4. Add a `VaultReader` service that reads Markdown files from a configured directory (no embedding service, no third-party API call — this is the §3.7 guarantee).
5. Add `/api/memory/documents` + `/api/memory/retrievals` FastAPI endpoints.
6. Add an MCP tool surface (`memory_search`, `memory_write`) so the agent reaches the vault through one controlled chokepoint rather than raw filesystem access.
7. Add unit + integration tests asserting: no outbound network call occurs during retrieval; retrieval events always carry a non-empty `retrieved_document_ids`; write events are append-only.

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

When the first v2-AI memory-surface PR adopts this discipline, the cook-bot (aiogram v3) interaction would be:

- `/memory <query>` — the agent surfaces what it recalled, **plus the source documents it used** (§3.4 observable evidence: the operator sees the answer *and* its sources).
- `/memory show <path>` — the operator opens a specific vault file (e.g. `suppliers/lamb.md`) directly in chat, because the vault is plain Markdown and therefore readable without any agent involvement.
- `/memory forget <path>` — the operator removes a vault file; this is an ordinary file deletion plus an append-only `memory_write_event` recording the intent.

**§3.4 note**: the whole point of the Markdown-vault discipline is that **the operator can always bypass the agent**. The non-AI fallback is not a degraded mode — it is opening the file.

## Dependencies

- Python 3.13, FastAPI, SQLModel, Postgres (production) — all already LE31 v1 stack.
- aiogram v3 for the `/memory` surface.
- `pathlib` (stdlib) for vault access — **zero new pip dependencies**.
- **§3.7 guarantee requires that no embedding service or LLM API is on the retrieval path.** If a future design adds embeddings, the embedding computation MUST be local (e.g. a local model) or the §3.7 guarantee is broken. This is a hard constraint, not a preference.

## Open questions

- **Does LE31 v2-AI ever gain an agent-memory surface?** Today no — no AI surface exists. **Decision pending.**
- **What would a restaurant agent actually remember?** Recipes and substitution rules are plausible; guest identities are **prohibited** by §3.7 (counts, not identity). The boundary between "operational knowledge" and "guest data" in a vault needs an explicit rule before any vault is created. **Decision pending.**
- **Is "neural memory" (per the repo's own framing) compatible with the auditable-retrieval posture?** A dense embedding index is inherently less auditable than a Markdown file list — the source documents are auditable but the *ranking* is not. LE31's version should probably be **keyword/file-based retrieval with the document set always surfaced**, accepting worse recall for better auditability. **Decision pending; the recommendation is keyword-first.**
- **Who edits the vault?** If the owner edits `suppliers/lamb.md` in Obsidian and the agent writes to the same file, the conflict resolution is undefined. **Decision pending.**

## Why this matters

This is the **only in-window agent-memory vocabulary of the 82-pass series that satisfies the LE31 §3.7 privacy invariant *by construction***: private Markdown vaults on the owner's own disk mean restaurant documents cannot leak to a third-party embedding API, not because a reviewer approved it but because the architecture has no egress path. Given that LE31's charter §3.4 keeps AI strictly in the operator-assistance role and §3.7 keeps guest data to counts, an architecture whose default is "nothing leaves" is the only shape that survives both constraints simultaneously without an amendment.

The *auditable-retrieval* primitive is also the cleanest instance in the 82-pass series of the §3.4 observable-evidence invariant: instead of auditing what the agent *did* (the pattern in features 129, 230, 231), it audits what the agent *saw*. For a restaurant that is arguably the more important question — a wrong recommendation built on a stale supplier price is more damaging than a wrong action taken from correct information.

Why it is filed at `defer`: LE31 has no AI surface today, ★0 is not traction evidence, and the "neural memory" framing implies an embedding dependency that conflicts with the §3.7 guarantee. Filing it now means the design question ("where does the agent's memory live, and can the owner read it?") already has an on-stack, permissively-licensed answer when the first v2-AI memory surface is proposed.

Fully reversible: vocabulary-only artifact; deletion has zero runtime impact.