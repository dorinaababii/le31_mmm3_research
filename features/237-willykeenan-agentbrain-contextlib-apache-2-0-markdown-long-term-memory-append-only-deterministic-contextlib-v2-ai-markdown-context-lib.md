# Feature 237 — willykeenan-agentbrain-contextlib-apache-2-0-markdown-long-term-memory-append-only-deterministic-contextlib-v2-ai-markdown-context-lib (defer)

> **NEW observation (2026-09-27).** Documents in-window GitHub Search `append-only+ledger` query result: `willykeenan/agentbrain-contextlib` (**Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, **1★/0⑂**, Python, **pushed 2026-09-26T22:57:33Z** (in-window by `pushed_at` only — *1 day before fetch time*), **created 2026-09-25T16:07:10Z** (~2-day-old repo with in-window `pushed_at`; `created_at` is OUT-OF-WINDOW by ~2 days), **repo size = 100 KB modest repo** (parent-verified via raw GitHub API JSON; subagent did not record exact size), `default_branch=main`, archived=`False`). **No topics** (parent-verified from raw JSON: `"topics": []`). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-27): *"ContextLib: a project's long-term memory as plain Markdown files you can read in Finder, on an SSD, with no database required. Append-only d..."* (description truncated in raw JSON; the full description starts with *"ContextLib: a project's long-term memory as plain Markdown files you can read in Finder, on an SSD, with no database required. Append-only d..."*). The **plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib** quadruple-primitive + the *Markdown-files-in-Finder* posture = the **strongest single v2-AI markdown-contextlib vocabulary of the 58-pass series**. Bucket: **v2-AI markdown-contextlib (parking-lot, future-v2-AI-surface-vocabulary-reference)** — watch-list entry, zero build time today.

## Goal

Retain the **plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib** quadruple-primitive as a persistent cross-section reference for any future LE31 v2-AI surface that introduces (a) **plain-Markdown-as-long-term-memory** (the long-term memory is stored as plain Markdown files, not as a database record), (b) **no-database-required** (the long-term memory does not require a database server; the memory is the file system), (c) **append-only** (memory entries are recorded once and never modified), and (d) **deterministic-contextlib** (the contextlib is deterministic, not learned). The artifact is the persistent cross-section reference + the verbatim description. No code today (Apache-2.0 license permits future code reuse; vocabulary-only artifact today; 100 KB modest-repo size is comfortably readable).

## Scope

**In scope (defer artifact):**
- A written record of the **plain-Markdown-as-long-term-memory** discipline: the *Markdown-as-memory* primitive (the long-term memory is stored as plain Markdown files, not as a database record; this is the *human-readable + diffable + portable* posture applied to the long-term-memory dimension; LE31 v1's Postgres is the database layer for transactional state but does NOT serve as the *long-term-memory layer* for AI context — the *Markdown-as-memory* layer is a v2-AI future reference).
- A written record of the **no-database-required** discipline: the *no-database-required* primitive (the long-term memory does not require a database server; the memory is the file system; this is the *file-system-as-database* posture applied to the long-term-memory dimension; LE31 v1's Postgres is the database layer for transactional state but the *no-database-required* posture is NOT directly applicable to LE31's transactional state — the *no-database-required* posture is a v2-AI vocabulary reference for any future *long-term-memory-only* surface that does not require transactional semantics).
- A written record of the **append-only** discipline: the *append-only-contextlib* primitive (memory entries are recorded once and never modified; this is the *append-only + no-mutation* posture applied to the contextlib dimension; LE31 v1's `audit_logs` is already append-only but does NOT serve as a *contextlib* — the *append-only-contextlib* layer is a v2-AI future reference).
- A written record of the **deterministic-contextlib** discipline: the *deterministic-contextlib* primitive (the contextlib is deterministic, not learned; this is the *explicit + reproducible* posture applied to the contextlib dimension; charter §3.4's *observable-evidence* requirement is operationalized by this primitive).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the cross-section reference is informative, not a v2-AI build-trigger.
- A cross-section reference with the prior v2-AI append-only-ledger + audit-log cluster: features 121 + 122 + 129 + 160 + 173 + 183 + 187 + 197 + 198 + 199 + 212 + 219 + 220 + 230 + 231 + 232 + 236 (today's Pick A — `shawn-durrani/membro` MIT 1★/0⑂ — local-first-AI-assistant-memory + append-only-fact-ledger + deterministic-extraction-walls). The *transferable insight* is the **plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib** quadruple-primitive.

**Out of scope (defer artifact):**
- Any change to LE31 v1's data model.
- Any change to the waiter web UI.
- Any change to the cook Telegram bot.
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any v2 surface in v1 (charter §3.1 + §3.2 invariant: v1 surface expansion is the next boundary; cross-section is informative, not a v2 expansion trigger).
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2 horizontal-expansion surface in v2 (charter §3.1 + §3.2 invariant: v2 surface expansion is the next boundary; this is a vocabulary reference, not a v2 expansion trigger).
- Any v2-AI markdown-contextlib implementation in v2 (the artifact is vocabulary-only; the implementation would require explicit owner/charter sign-off).
- Any no-database-required primitive in v1 (LE31 v1's Postgres is the database layer for transactional state; the *no-database-required* posture is NOT directly applicable to LE31's transactional state — the *no-database-required* posture is a v2-AI vocabulary reference for any future *long-term-memory-only* surface that does not require transactional semantics).
- Any markdown-contextlib primitive in v1 (LE31 v1 has no AI surface at all; the *markdown-contextlib* vocabulary is a v2-AI future reference).

## Description

The pick is **`willykeenan/agentbrain-contextlib`** — a Python + Apache-2.0 + plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib vocabulary artifact. Charter §3.4 NOT triggered because the artifact is operator-tooling-AI (the contextlib provides AI context for the operator's supervised AI workflows), NOT customer-facing-AI (no restaurant diner interacts with the contextlib; the diner interacts with the operator who uses the AI). The *markdown-contextlib* is a tool for the *operator/owner* who supervises the AI; charter §3.4 is satisfied because the AI runs in the *operator-tooling layer* (per charter §3.4 *"AI may assist owner/staff, with observable evidence and a non-AI fallback"*). The artifact is the persistent cross-section reference for the verbatim description + the 4 named primitives.

**Stack caveat**: Markdown is not LE31 v1's Postgres-only stack; the *plain-Markdown-as-long-term-memory* vocabulary is transferable but the serialization format may not be directly adopted. The *no-database-required* posture is **NOT** applicable to LE31 v1's transactional state (which legitimately requires a database).

## Data model

No data model changes today. The artifact is a vocabulary reference, not a code change. Future v2-AI surface that adopts the *markdown-contextlib* primitive would extend the LE31 v1 data model with appropriate new tables or files (e.g., a `contextlib_entry` table with `entry_id, entry_markdown_path, entry_content, recorded_at, parent_entry_id, append_only_hash`; a `contextlib_file` table with `file_id, file_path, file_hash, recorded_at`; or a file-system-based `~/le31-contextlib/*.md` directory tree). All future schema extensions are explicitly out-of-scope for this defer artifact.

## Implementation steps

Zero implementation today (defer artifact). If a future v2-AI PR is triggered by the trigger condition below, the implementation would:
1. Read the `willykeenan/agentbrain-contextlib` README at https://github.com/willykeenan/agentbrain-contextlib for the *plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib* quadruple-primitive.
2. Cross-reference with LE31 v1's `audit_logs` schema to identify the *delta* (the *delta* = `willykeenan/agentbrain-contextlib` introduces plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib primitives that LE31 v1's `audit_logs` does not have; LE31 v1's `audit_logs` is append-only but does NOT serve as a *contextlib* — the *contextlib* discipline is the *AI-context* layer between operator and AI assistant).
3. Apply charter §3.4 *operator-tooling-AI with observable evidence + non-AI fallback* review to the *delta* (any new v2-AI surface requires explicit owner/charter sign-off; the *markdown-contextlib* surface is operator-tooling-AI which is charter §3.4-compatible provided the non-AI fallback is preserved — i.e., the operator can read every contextlib entry as plain Markdown without using the AI to interpret it).
4. Implement the surface with the LE31 v1 + FastAPI + SQLModel + aiogram stack; the `willykeenan/agentbrain-contextlib` reference is the *vocabulary* for *plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib*, NOT for *contextlib replacement*.

## Telegram interaction

Zero new Telegram interaction today. Future v2-AI PR that adopts the *markdown-contextlib* primitive would extend the existing aiogram-bot (cook-bot per charter §3.1) with a *contextlib-status* command set that allows the operator to query contextlib status (e.g., `/contextlib list` → list of recently-recorded contextlib entries; `/contextlib show <entry_id>` → show a contextlib entry as Markdown; `/contextlib append <markdown_text>` → append a new contextlib entry). The *contextlib-status* discipline is *operator-tooling* (operator queries the contextlib status), NOT customer-facing-AI; charter §3.4 is NOT triggered.

## Dependencies

- LE31 charter §3.1 surface-expansion review (for any v2 surface adoption).
- LE31 charter §3.2 surface-expansion review (for any v2-AI surface adoption).
- LE31 charter §3.4 operator-tooling-AI-with-observable-evidence boundary (for any markdown-contextlib adoption; the *markdown-contextlib* posture is operator-tooling-AI which is charter §3.4-compatible provided the non-AI fallback is preserved).
- LE31 charter §3.2 license-compatible (Apache-2.0 permissive; future code adoption is possible).
- Features 121, 122, 129, 160, 173, 183, 187, 197, 198, 199, 212, 219, 220, 230, 231, 232, 236 (today's Pick A).
- Cross-section reference `willykeenan/agentbrain-contextlib` at https://github.com/willykeenan/agentbrain-contextlib (Apache-2.0, 1★/0⑂, Python, plain-Markdown-as-long-term-memory + no-database-required + append-only + deterministic-contextlib).

## Open questions

- Will LE31 v2-AI ever introduce a markdown-contextlib surface? If yes, `willykeenan/agentbrain-contextlib` is the vocabulary reference.
- Will LE31 v2-AI ever introduce a plain-Markdown-as-long-term-memory layer (vs the current `audit_logs` which records *state transitions* but not *long-term-memory entries*)? If yes, `willykeenan/agentbrain-contextlib` is the vocabulary reference.
- Will LE31 v2-AI ever introduce a no-database-required posture (file-system-as-database)? If yes, `willykeenan/agentbrain-contextlib` is the vocabulary reference.
- Will LE31 v2-AI ever introduce a deterministic-contextlib (the contextlib is deterministic, not learned)? If yes, `willykeenan/agentbrain-contextlib` is the vocabulary reference.
- The 1★/0⑂ is explicitly NOT offered as evidence of *LE31 needing a markdown-contextlib*; the 1★/0⑂ is for the *markdown-contextlib domain*, not for the *LE31 operational* primitive. The transferable item is the *technique* (Markdown-as-memory + no-database + append-only + deterministic-contextlib), not the *markdown-contextlib* itself.
- **Open question that may kill any future PR**: who would ever read the plain-Markdown contextlib entries? LE31 has exactly one stakeholder (the owner) who can just ask the AI what it did. The *plain-Markdown-as-long-term-memory* may be over-engineering for a single-tenant single-operator scenario.
- **Stack caveat open question**: would LE31 v2-AI adopt the Markdown serialization format directly (file-system-as-database for the contextlib) or would it adopt a Postgres-backed *contextlib* table that mimics the Markdown-as-memory discipline? The Markdown serialization is the load-bearing primitive, not the file-system-vs-database choice.

## Why this matters

The verbatim description in `willykeenan/agentbrain-contextlib` is the **canonical v2-AI markdown-contextlib vocabulary** that LE31 v1's `audit_logs` (feature/charter §3.1) and v2-AI's future contextlib surface would inherit. Specifically: (i) **plain-Markdown-as-long-term-memory** (the *Markdown-as-memory* primitive) is the *human-readable + diffable + portable* posture; (ii) **no-database-required** (the *no-database-required* primitive) is the *file-system-as-database* posture; (iii) **append-only** (the *append-only-contextlib* primitive) is the *append-only + no-mutation* posture per charter §3.1; (iv) **deterministic-contextlib** (the *deterministic-contextlib* primitive) is the *explicit + reproducible* posture per charter §3.4. When v2-AI introduces any of these 4 primitives, `willykeenan/agentbrain-contextlib` is the vocabulary reference. **HONEST DISCLOSURE**: `willykeenan/agentbrain-contextlib`'s 1★/0⑂ is for the *markdown-contextlib domain*, not for the *LE31 operational* primitive; the 1★/0⑂ is explicitly NOT offered as evidence of LE31's need for the markdown-contextlib. **STACK CAVEAT**: Markdown is not LE31 v1's Postgres-only stack; the *plain-Markdown-as-long-term-memory* vocabulary is transferable but the serialization format may not be directly adopted.