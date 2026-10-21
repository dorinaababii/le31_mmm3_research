# Feature 354 — `AIDAChip-Inc-mem-plus-plus-append-only-zero-llm-ingest-memory-vocabulary` (defer)

> **NEW observation (2026-10-21).** Documents in-window GitHub repo `AIDAChip-Inc/mem-plus-plus` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★9/⑂2**, **15,415 KB moderate**, **Python ✓ ON-STACK** (matches LE31 v1's Python 3.13 charter), **created 2026-09-03T21:34:57Z AND pushed 2026-10-20T01:08:02Z = IN-WINDOW BY BOTH FIELDS** (~7-week-old repo with an in-window push), `archived=false`, `fork=false`, 0 open issues, default_branch=`main`). Description (verbatim from GitHub API direct-GET, parent-verified 2026-10-21): *"Non-destructive, long-term organizational memory for AI agents. Preserve dated records, search with hybrid retrieval, and query history. PostgreSQL/pgvector, local ONNX embeddings, zero LLM calls at ingestion."* Topics (verbatim, parent-verified, **19 topics**): `agent-memory, ai-agents, append-only, hybrid-search, information-retrieval, llm-agents, llm-memory, long-term-memory, onnx, organizational-memory, pgvector, postgresql, python, rag, retrieval, retrieval-augmented-generation, semantic-search, temporal-search, vector-search`. Bucket: **v2-AI (append-only organisational-memory + hybrid/temporal retrieval + zero-LLM-at-ingestion vocabulary)** — Pick B of Daily Brainstorm 2026-10-21. Build verdict: `defer` (parking-lot; **vocabulary reference only**; Apache-2.0 permits code-shape reuse but the §3.7 boundary is unmade).

## Goal

Retain the **append-only dated records + hybrid (vector + keyword) retrieval + temporal search + zero LLM calls at ingestion + local ONNX embeddings** vocabulary as a persistent cross-section reference for the LE31 v2-AI *retrieval and audit* wedge. The upstream repo is an AI-agent memory system; LE31 has **no AI surface at all**. The transferable contribution is narrow and specific: **an ingestion path that requires no model call**, which is the strongest available reading of §3.4 (AI in operator-assistance only, never in the business kernel). No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **zero-LLM-calls-at-ingestion + local-ONNX-embeddings** primitive: a retrieval store where writing a record requires no model inference, only a local embedding. IS the canonical §3.4 *deterministic kernel + zero inference* invariant applied to the *v2-AI retrieval* dimension — the write path is as deterministic as the read path.
- A written record of the **append-only + non-destructive + dated records + temporal-search** posture: records are never edited, only superseded, and "what did this look like last Tuesday" is a first-class query. IS the canonical §3.3 *append-only, derived-not-persisted* invariant extended to the *retrieval* dimension — the same posture LE31 v1 already applies to StockEntry, generalised to text.
- A written record of the **hybrid retrieval (vector + keyword)** posture and its relationship to feature 352 (`Idriz-hax/harbor-ledger-memory`, filed today by the research cron). The two picks are direct cross-section siblings and disagree in an instructive way — see Open questions.
- A decision record: today's verdict is `defer` because (1) LE31 has no AI surface to attach memory to; (2) **the §3.7 boundary is unmade** — what counts as operational knowledge vs guest data inside a memory store; (3) an upstream "memory" framing implies an embedding dependency that would need to be re-specified as keyword/file-based to preserve auditability (see Why this matters).

**Out of scope (defer artifact):**

- Any adoption of pgvector, ONNX, or any embedding model.
- Any change to LE31 v1's StockEntry ledger.
- Any AI surface. LE31's first AI surface, if any, is a v2-AI decision that has not been made.
- Treating this repo's output as an operator-facing recommendation engine.

## Out of scope

- See "Scope" above. Vocabulary-only; no code today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "let the operator ask what happened last Tuesday", the owner wants *a retrieval shape whose write path never calls a model*, but struggles because *every agent-memory reference they can find puts an LLM in the ingestion path, which is exactly the §3.4 shape the charter forbids in the business path*.

- **Evidence class**: observed (verbatim description + 19 verbatim topics name `zero LLM calls at ingestion`, `append-only`, `temporal-search`, `hybrid-search`, `onnx`, `pgvector` explicitly; all counts and timestamps parent-verified by direct `/repos/` GET).
- **Confidence**: medium-high for the vocabulary match. **low** for present urgency — zero owner mentions across 83 brainstorm + 82 research passes, and LE31 has no AI surface to attach this to.
- **Traction caveat, recorded plainly**: ★9/⑂2 is minimal traction. It is recorded as a demand signal of the *shape*, not of adoption. Noted so a future reviewer does not mistake ★9 for validation.

## Description

GitHub `AIDAChip-Inc/mem-plus-plus` (Apache-2.0 ✓, ★9/⑂2, 15,415 KB, Python ✓ ON-STACK, created 2026-09-03, pushed 2026-10-20, archived=false).

Sub-primitives that map onto LE31:

1. **Zero LLM calls at ingestion** — writing a record requires no model inference. IS the canonical §3.4 *deterministic kernel + zero inference* invariant. **This is the pick's single most valuable idea**, because it is the shape that lets a retrieval store coexist with §3.4 without an exemption.
2. **Local ONNX embeddings** — the embedding runs locally, not via an API. Preserves the §3.7 *no-egress* property structurally rather than by review: restaurant documents never leave the owner's machine because there is no network call to make.
3. **Append-only + non-destructive + dated records** — IS the canonical §3.3 *append-only* invariant, generalised from numeric StockEntry rows to text records.
4. **Temporal search** — "what did this look like at time T" as a first-class query. This is the retrieval-side analogue of LE31 v1's append-only StockEntry and is the most directly reusable idea for the audit dimension.
5. **Hybrid retrieval (vector + keyword)** — semantic recall **plus** exact-match recall. The keyword half is the auditable half: a keyword hit is explainable, a vector hit is not.

## Data model

None shipped. The implied shape: a **Record** table (append-only, `id`, `recorded_at`, `content`, `superseded_by` nullable) plus a **temporal index** and a **keyword index**, with embeddings as a *derived, rebuildable* projection rather than the source of truth. The rebuildability point is the important one: if embeddings can always be recomputed from the append-only records, then a bad embedding run is recoverable and the audit trail survives. That is §3.3 applied properly.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) an owner decision exists on whether LE31 gets any AI surface at all; (2) the §3.7 boundary rule is written down — what may enter a memory store and what may not; (3) the retrieval store is specified as keyword-first with embeddings as a rebuildable projection.

## Telegram interaction if any

None today. Worth recording for a future spec: if a retrieval surface ever reaches the cook or waiter role, it must be an answer the operator can act on without trusting an opaque similarity score — which argues for **keyword-first answers with the embedding as a fallback hint**, never the reverse.

## Dependencies

- LE31 charter §3.3 (append-only, derived-not-persisted), §3.4 (deterministic kernel, no inference in the business path), §3.7 (guest data as counts not identity; no egress).
- Sister features: **352** (`Idriz-hax/harbor-ledger-memory`, filed 2026-10-21 by the research cron — the direct cross-section sibling), 351 (`austinchima/elodea`), 129/230/231 (the audit-what-the-agent-did cluster).
- LE31 v1's Postgres + SQLModel stack (which the upstream's PostgreSQL choice aligns with).

## Open questions

1. **§3.7 boundary unmade.** What counts as operational knowledge (supplier prices, prep times, staff notes) versus guest data (who ordered what, payment instruments) in a memory store? An unmade rule means no store can be created safely. **Owner decision required before any implementation.**
2. **Vector-first vs keyword-first.** Feature 352 argues keyword/file-based retrieval with the document set always surfaced (worse recall, better auditability). This repo argues hybrid with embeddings primary. **These two picks disagree**, and the disagreement is unresolved.
3. **Embedding rebuildability.** If embeddings are a derived projection over append-only records, a bad embedding run is recoverable. Is that true of the upstream? Unverified — would need a code read before adoption.
4. **Does "organizational memory" imply multi-tenant?** LE31 is single-restaurant by charter. Upstream framing may assume otherwise.

## Why this matters

It supplies the **narrowest, cleanest §3.4-compatible retrieval shape found in 83 passes**: a store where *writing* a record costs no model call, embeddings run locally so there is no egress path by construction, and the source of truth is an append-only dated log with embeddings as a rebuildable projection. That combination is the one that can survive a §3.7 review without a charter amendment — which is exactly the property feature 352 was filed for and could not prove from its description alone.

Its second contribution is the **recorded disagreement with feature 352** (vector-first vs keyword-first). Filing both, and naming the conflict, is more useful than filing one and letting the other be rediscovered in six months. The owner does not need to resolve this today; they need to know it is unresolved.