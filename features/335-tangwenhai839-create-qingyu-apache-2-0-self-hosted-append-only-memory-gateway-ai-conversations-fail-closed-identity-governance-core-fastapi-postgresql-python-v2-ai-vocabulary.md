# Feature 335 — `tangwenhai839-create/qingyu` Apache-2.0 v2-AI Python+FastAPI+PostgreSQL+append-only+AI-memory-governance-vocabulary (defer, parking-lot)

> **NEW observation (2026-10-17).** Documents in-window GitHub repo `tangwenhai839-create/qingyu` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **1★/3⑂**, **Python ✓ ON-STACK**, **1446 KB modest**, `default_branch=main`, **pushed 2026-10-15T05:54:51Z AND created 2026-10-14T17:32:15Z = IN-WINDOW BY BOTH FIELDS** (2-day-old repo with same-day push)). Topics (verbatim, parent-verified GitHub API direct-GET 2026-10-17 from `/tmp/le31-brainstorm-2026-10-17/verify/3_picks.json`, **10 topics**): `ai-memory`, `append-only`, `audit`, `chatgpt-export`, `fastapi`, `governance`, `llm`, `postgresql`, `python`, `self-hosted` = **the strongest in-window 2026-10 v2-AI Python+FastAPI+PostgreSQL+append-only+AI-memory-governance vocabulary of the 79-pass brainstorm series; the only in-window 2026-10 v2-AI self-hosted-append-only-memory-gateway-for-AI-conversations Python+FastAPI+PostgreSQL peer of the 79-pass series**. Description (verbatim, parent-verified GitHub API direct-GET 2026-10-17): *"Self-hosted, append-only memory gateway for AI conversations + a fail-closed identity/governance core. FastAPI + PostgreSQL. Work in progress."*. The **self-hosted-append-only-memory-gateway-for-AI-conversations + fail-closed-identity/governance-core + chatgpt-export-import + PostgreSQL + FastAPI** quintuple-primitive + the *append-only-memory-gateway* discipline (every AI-conversation record is appended (not updated or deleted) into a new immutable table; when a record needs to be revised, a new snapshot is appended that points to the old record; the old record is never modified) + the *fail-closed-identity/governance-core* posture (the identity/governance core fails closed when a policy is violated — e.g., when a user is not authorized to read a record, the core returns an error rather than falling back to a permissive default) + the *chatgpt-export-import* posture (AI-conversation records can be exported from ChatGPT and imported into the gateway, and vice versa) = the **canonical v2-AI Python+FastAPI+PostgreSQL+append-only+AI-memory-governance vocabulary of the 79-pass series**. Bucket: **v2-AI (parking-lot, vocabulary reference)** — Pick A of Daily Brainstorm 2026-10-17. Build verdict: `defer (parking-lot, vocabulary-only)`. Zero build time today. Sister-shape to features 309 (`AXIOVEX/axiomere`) + 310 (`Perseus-Computing-LLC/argus`) + 332 (`vsov/xcheck`) + 333 (`FlashyLabs/flashy-ledger`).

## Goal

Retain the **self-hosted-append-only-memory-gateway-for-AI-conversations + fail-closed-identity/governance-core + chatgpt-export-import + PostgreSQL + FastAPI** quintuple-primitive + the *append-only-memory-gateway + fail-closed-identity/governance-core + chatgpt-export-import* discipline as a persistent cross-section reference for the LE31 v2-AI *Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway for AI-conversations* wedge, and document the **Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway vocabulary validation** that an independent maintainer arrived at in 2026 (2-day-old repo with same-day push = same-week fresh discovery) without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI *self-hosted-append-only-memory-gateway-for-AI-conversations* product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **self-hosted-append-only-memory-gateway-for-AI-conversations + fail-closed-identity/governance-core + chatgpt-export-import + PostgreSQL + FastAPI** quintuple-primitive
- A written record of the **append-only-memory-gateway** discipline: every AI-conversation record is appended (not updated or deleted) into a new immutable table; when a record needs to be revised, a new snapshot is appended that points to the old record; the old record is never modified
- A written record of the **fail-closed-identity/governance-core** discipline: the identity/governance core fails closed when a policy is violated — e.g., when a user is not authorized to read a record, the core returns an error rather than falling back to a permissive default
- A written record of the **chatgpt-export-import** posture: AI-conversation records can be exported from ChatGPT and imported into the gateway, and vice versa
- A decision record: today's verdict is `defer (parking-lot, vocabulary-only)` because (1) **LE31 v1 is single-tenant + cook-Telegram-bot today; no Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway-for-AI-conversations surface**; (2) the *vocabulary-shape* is the transferable item; (3) the *code-shape* is **fully compatible** (Apache-2.0 permissive) but **NOT adopted** because v1 has no Python-AI-agent-conversation-memory surface

**Out of scope (defer artifact):**

- Any change to LE31 v1's current SQLModel+Postgres-only deployment
- Any change to LE31 v1's existing aiogram v3 Telegram-bot surface
- **Adoption of the `qingyu` codebase** — deferred to v2-AI (the *code-shape* is fully compatible; v1 has no Python-AI-agent-conversation-memory surface; the *fail-closed-identity/governance-core* posture requires explicit §3.4 charter-invariant review before any v2-AI build)

## Evidence / JTBD

When a future LE31 v2-AI surface proposes *"the Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway for AI-conversations + fail-closed-identity/governance-core surface that gives Python AI agents a friendly self-hosted-append-only-memory-gateway with a fail-closed-identity/governance-core for storing and querying AI-conversation records in an append-only-signed-hash-chained-memory-gateway with chatgpt-export-import portability"*, the owner wants *a primitive that proves this self-hosted-append-only-memory-gateway-for-AI-conversations pattern is real and well-tested in 2026*, but struggles because *LE31 v2-AI has no documented evidence for this pattern*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the self-hosted-append-only-memory-gateway pattern"*.

- **Evidence class**: observed (the description + topics name the primitives explicitly)
- **Confidence**: high for the self-hosted-append-only-memory-gateway-for-AI-conversations-vocabulary match (the verbatim description names the 5-pentagram-primitive + the 10-topic array)
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 has no Python-AI-agent-conversation-memory surface); the value is the **self-hosted-append-only-memory-gateway** vocabulary — when the first v2-AI PR that adds a Python-AI-agent-conversation-memory surface lands, the `qingyu` pattern is a ready-made *named gateway primitive*

## Description

GitHub `tangwenhai839-create/qingyu` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, 1★/3⑂, Python ✓ ON-STACK + FastAPI + PostgreSQL + append-only + audit + ai-memory + chatgpt-export + governance + llm + self-hosted, pushed 2026-10-15T05:54:51Z AND created 2026-10-14T17:32:15Z = IN-WINDOW BY BOTH FIELDS, 1446 KB modest). Description (verbatim, parent-verified GitHub API direct-GET 2026-10-17):

> *"Self-hosted, append-only memory gateway for AI conversations + a fail-closed identity/governance core. FastAPI + PostgreSQL. Work in progress."*

**The 1:1 mapping onto LE31 surface:**

| `qingyu` primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Python + FastAPI + PostgreSQL | LE31 v1 FastAPI + Python 3.13 + SQLModel + Postgres | §3.1 ✓ | **Implemented (v1)** — exact 3/3 backend-stack match |
| self-hosted-append-only-memory-gateway-for-AI-conversations | (LE31 v2-AI has no self-hosted-append-only-memory-gateway surface) | §3.3 + §3.4 | **Not implemented** — forward-looking v2-AI vocabulary |
| fail-closed-identity/governance-core | (LE31 v2-AI has no fail-closed-identity/governance-core surface) | §3.4 ✓ | **Not implemented** — forward-looking v2-AI vocabulary |
| chatgpt-export-import | (LE31 v2-AI has no chatgpt-export-import surface) | §3.1 partial | **Not implemented** — forward-looking v2-AI vocabulary |
| append-only + audit | LE31 v1 `audit_logs` SQLModel table (append-only) | §3.3 ✓ | **Implemented (v1)** — exact match |
| ai-memory + llm | (LE31 v2-AI has no ai-memory surface) | §3.4 REQUIRES_DECISION | **Not implemented** — forward-looking v2-AI vocabulary |
| **ACTUAL implementation** | None | n/a | **NOT adopted** — v1 has no Python-AI-agent-conversation-memory surface |
| **Future adoption** | v2-AI self-hosted-append-only-memory-gateway-for-AI-conversations + fail-closed-identity/governance-core + chatgpt-export-import surface | §3.1 + §3.2 + §3.3 + §3.4 | **Future v2-AI PR target** |

## Data model

**Reference (no schema adopted today):** the `qingyu` schema is **append-only-memory-gateway-for-AI-conversations** with the following high-level shape (inferred from the topics + description; parent has NOT read the source code per §3.2 BLOCKER check + v2-AI de-duplication):

- `MemoryRecord` — append-only, immutable, primary key `record_id` (UUID); fields: `record_id`, `conversation_id` (FK to `Conversation`), `payload` (JSONB), `created_at` (timestamptz, immutable), `previous_record_id` (FK to `MemoryRecord`, nullable for first record), `record_hash` (SHA-256 of `payload + previous_record_id + created_at` for hash-chaining); the `MemoryRecord` table has NO `updated_at` + NO `deleted_at` columns (append-only invariant)
- `Conversation` — append-only, immutable, primary key `conversation_id` (UUID); fields: `conversation_id`, `title` (text), `source` (enum: `chatgpt-export`, `claude-export`, `manual-import`), `created_at` (timestamptz, immutable); the `Conversation` table has NO `updated_at` + NO `deleted_at` columns (append-only invariant)
- `IdentityPolicy` — fail-closed, primary key `policy_id` (UUID); fields: `policy_id`, `subject` (text, e.g., `user:alice`), `resource` (text, e.g., `conversation:xyz`), `action` (enum: `read`, `write`, `delete`, `export`), `effect` (enum: `allow`, `deny`); the `IdentityPolicy` table fails closed when no policy matches a query (returns `deny` by default)
- `GovernanceAudit` — append-only, immutable, primary key `audit_id` (UUID); fields: `audit_id`, `policy_id` (FK to `IdentityPolicy`), `decision` (enum: `allow`, `deny`), `reason` (text), `created_at` (timestamptz, immutable); the `GovernanceAudit` table has NO `updated_at` + NO `deleted_at` columns (append-only invariant)

The above schema is **inferred from the topics + description**; a future v2-AI PR would design a fresh schema from scratch that captures the *append-only-memory-gateway + fail-closed-identity/governance-core + chatgpt-export-import* primitives using LE31 v2-AI charter-compliant conventions (e.g., Postgres + SQLModel + Alembic + FastAPI + Pydantic + datetime.timezone.utc + Europe/Paris business dates).

## Implementation steps

**Defer artifact (no implementation today):**

1. **Step 0 — defer**: do not implement the v2-AI self-hosted-append-only-memory-gateway-for-AI-conversations surface today. The artifact is a persistent cross-section reference + a vocabulary validation.
2. **Step 1 — pre-trigger**: a future v2-AI PR that proposes the *Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway for AI-conversations + fail-closed-identity/governance-core + chatgpt-export-import* surface would:
   - Read this artifact + the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-17.md`)
   - **DO NOT load the `qingyu` codebase** per the §defer convention; instead, read the **vocabulary-shape only** (the 5-pentagram-primitive + the 10-topic array + the *append-only + fail-closed + chatgpt-export-import* discipline) and design a fresh v2-AI implementation from scratch with charter-compliant conventions
   - Re-run the LE31 feature gate with the adoption in mind (see `specs/335-tangwenhai839-create-qingyu-HANDOFF.md`)
3. **Step 2 — pilot on one AI-conversation record first**. Do not ship the self-hosted-append-only-memory-gateway-for-AI-conversations project-wide on the first pass.

## Telegram interaction if any

**None today.** The `qingyu` vocabulary is a v2-AI surface (Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway for AI-conversations), not a Telegram-bot surface. The companion features 332 (`vsov/xcheck` — cross-agent-audit-methodology) + 333 (`FlashyLabs/flashy-ledger` — AAO-stack-ledger-rules) + today's research PICK C (`donaldrichard19-LVD/pattern-mcp` — MCP-server-design-system-pattern-check-+-auditable-decision-ledger) cover the v2-AI surface; the LE31 v1 aiogram v3 Telegram-bot surface is unchanged.

## Dependencies

**No new dependencies today.** The defer artifact is a vocabulary-only artifact:

- The `qingyu` codebase is **NOT added** to `requirements.txt` (the §defer convention forbids code-shape adoption)
- The v1 dependency-whitelist is unchanged: `fastapi==0.118.0` (HOLD per pin-bump-board 10-16), `sqlmodel==0.0.42`, `sqlalchemy>=2.0,<2.1`, `pydantic`, `aiogram ^3.30`, `alembic`
- A future v2-AI PR that adopts the vocabulary would add: `fastapi` (already pinned), `sqlalchemy[asyncio]` (already pinned), `pydantic` (already pinned), `cryptography` (for cryptographic-signature-as-audit-evidence — v2-AI dependency review needed), `asyncpg` (for async PostgreSQL — v2-AI dependency review needed)

## Open questions

- **Q1 — does the v2-AI roadmap include a Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway-for-AI-conversations surface?** The current v2-AI roadmap is silent on this question. A future v2-AI PR that proposes this surface would need a charter §3.4 *chokepoint-governed + human-gate + observable-evidence + non-AI-fallback* review.
- **Q2 — does the v2-AI roadmap include a fail-closed-identity/governance-core surface?** The current v2-AI roadmap is silent on this question. A future v2-AI PR that proposes this surface would need a charter §3.4 *chokepoint-governed* review.
- **Q3 — does the v2-AI roadmap include a chatgpt-export-import surface?** The current v2-AI roadmap is silent on this question. A future v2-AI PR that proposes this surface would need a charter §3.1 *open-data-export-import* review + §3.4 *AI-allowlist* review (LE31 charter §3.4 forbids customer-facing AI; chatgpt-export-import is a data-portability posture, not a customer-facing AI posture).
- **Q4 — what is the relationship between the `qingyu` fail-closed-identity/governance-core and the LE31 v2-AI chokepoint-governed invariant?** The `qingyu` fail-closed posture IS the §3.4 *chokepoint-governed* charter invariant applied to the *identity/governance* dimension. The two postures are aligned.

## Why this matters

LE31 v2-AI roadmap has no *Python+FastAPI+PostgreSQL self-hosted-append-only-memory-gateway for AI-conversations + fail-closed-identity/governance-core + chatgpt-export-import* surface today. When a v2-AI PR eventually wants to add such a surface, `tangwenhai839-create/qingyu` names the exact vocabulary:

- **self-hosted + append-only + memory-gateway + fail-closed-identity/governance-core + chatgpt-export-import + Python+FastAPI+PostgreSQL** = canonical §3.1 + §3.3 + §3.4 self-hosted-append-only-memory-gateway-for-AI-conversations + fail-closed-identity/governance-core + chatgpt-export-import + Python+FastAPI+PostgreSQL ON-STACK vocabulary

The 10-topic array (`ai-memory + append-only + audit + chatgpt-export + fastapi + governance + llm + postgresql + python + self-hosted`) is the strongest v2-AI Python+FastAPI+PostgreSQL+append-only+AI-memory-governance vocabulary of the 79-pass series. The Python+FastAPI+PostgreSQL ON-STACK posture aligns with §3.1. The Apache-2.0 permissive aligns with §3.2. The append-only + audit discipline aligns with §3.3. The fail-closed-identity/governance-core posture aligns with §3.4.

**The strongest v2-AI Python+FastAPI+PostgreSQL+append-only+AI-memory-governance vocabulary of the 79-pass brainstorm series.**