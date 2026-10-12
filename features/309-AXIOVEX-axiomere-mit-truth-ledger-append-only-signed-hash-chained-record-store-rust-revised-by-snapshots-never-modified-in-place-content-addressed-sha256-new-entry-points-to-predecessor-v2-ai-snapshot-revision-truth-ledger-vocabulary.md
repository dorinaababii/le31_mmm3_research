# Feature 309 — `AXIOVEX-axiomere-mit-truth-ledger-append-only-signed-hash-chained-record-store-rust-revised-by-snapshots-never-modified-in-place-content-addressed-sha256-new-entry-points-to-predecessor-v2-ai-snapshot-revision-truth-ledger-vocabulary` (defer)

> **NEW observation (2026-10-12).** Documents in-window GitHub repo `AXIOVEX/axiomere` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, Rust core + Python SDK via PyO3, **pushed 2026-10-12 = TODAY**, in-window by `pushed_at` only, **23 KB tiny + 8 KB Python SDK = smallest v2-AI pick of the 74-pass series**). Description (verbatim from GitHub Search API, parent-verified 2026-10-12 via direct re-parse of `gsearch5.json`): *"Axiomere — a truth ledger: an append-only, signed, hash-chained record store (Rust) where records are revised by new snapshots and never modified in place. The records are content-addressed by SHA-256 and every revision creates a new entry pointing to its predecessor."* Topics (verbatim, parent-verified, 8 topics): **`append-only, audit-trail, ed25519, immutable, ledger, merkle-tree, provenance, rust`**. The **`axiomere-python` sister-shape** (MIT, 0★/0⑂, 8 KB tiny, topics: `append-only, immutable, provenance, pyo3, python, truth-ledger`) is a PyO3 wrapper for the Rust core. Bucket: **v2-AI (snapshot-revision-truth-ledger-vocabulary)** — Pick B of Daily Research 2026-10-12. Build verdict: `defer` (parking-lot). Zero build time today.

## Goal

Retain the **`append-only + signed + hash-chained + record-store + revised-by-snapshots + never-modified-in-place + content-addressed-by-SHA-256 + new-entry-points-to-predecessor + truth-ledger + audit-trail + ed25519 + merkle-tree + provenance + Rust`** 14-dimensional primitive as a persistent cross-section reference for the LE31 v2-AI *truth-ledger-with-snapshot-revision-semantics* wedge, and document the **snapshot-revision-vocabulary** validation that an independent maintainer arrived at in 2026 without reading the LE31 charter. The artifact is a persistent cross-section reference + a demand-signal for the LE31 v2-AI product wedge. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **`revised-by-snapshots + never-modified-in-place`** double-primitive: a *snapshot* is a new record that supersedes an old record; the old record is preserved (never modified in place); the new record points to the old record via the *content-addressed-by-SHA-256* hash. The *snapshot-revision* discipline is the **strongest v2-AI audit-trail-event-sourcing vocabulary of the 74-pass series**. This is the §3.1 *explicit-state-transition* charter invariant applied to the *audit-trail-record-revision* dimension, where the *snapshot-revision* is the §3.1 *append-only-ledger* discipline with the *revision* extension.
- A written record of the **`content-addressed-by-SHA-256 + new-entry-points-to-predecessor`** double-primitive: every record is identified by its content hash (SHA-256), not by an external ID; every revision creates a new entry that points to its predecessor. The *content-addressed-by-SHA-256* primitive is the §3.1 *content-addressed-storage* primitive; the *new-entry-points-to-predecessor* is the *linked-list-of-content-addressed-records* pattern, which is a portable linked-list + content-addressing pattern.
- A written record of the **`append-only + signed + hash-chained + record-store + truth-ledger + audit-trail + ed25519 + merkle-tree + provenance + Rust + immutable`** 11-dimensional sub-primitive: the *append-only* is §3.1-aligned; the *signed* is the *cryptographic-signature* primitive; the *hash-chained* is the *hash-chain* primitive (each entry's hash includes the previous entry's hash); the *record-store* is the *generic-record-store* framing; the *truth-ledger* is the *truth-claim* primitive (a ledger that records truth claims, not just data); the *audit-trail* is the *audit-trail* primitive; the *ed25519* is the *cryptographic-signature-algorithm* primitive; the *merkle-tree* is the *merkle-tree* primitive (enables efficient proofs of inclusion); the *provenance* is the *provenance* primitive (records where the data came from); the *Rust* is the *implementation-language* primitive; the *immutable* is the *immutable-data* primitive (records can never be modified once written).
- A decision record: today's verdict is `defer` because (1) LE31 v1 has no v2-AI surface requirement; (2) the *snapshot-revision-truth-ledger-vocabulary* is the value, not the code (the 23 KB tiny + 0★/0⑂ is the smallest v2-AI pick of the 74-pass series, but the *snapshot-revision* discipline is the §3.1 *append-only-ledger-with-revision* primitive); (3) the *demand-signal* is the value, not the code-adoption opportunity.

**Out of scope (defer artifact):**

- Any change to LE31 v1's waiter web UI (HTMX) or cook Telegram bot (aiogram v3).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema (the §3.1 *append-only-ledger* primitive is already implemented; the *snapshot-revision* extension is OFF the v1 charter).
- Adoption of the AXIOVEX/axiomere codebase (0★/0⑂ with 23 KB tiny + 8 KB Python SDK; the Rust core + Python SDK is portable to LE31 stack via PyO3, but the 0★/0⑂ is a low community-traction signal).
- Cross-pollination with the v2-AI snapshot-revision primitive in v1 (LE31 v1 has no v2-AI surface).
- Cross-pollination with the v2-AI audit-trail-event-sourcing primitive in v1 (LE31 v1 has no event-sourcing surface).

## Out of scope

- See "Scope" section above for the explicit defer-artifact out-of-scope list. The defer artifact is **vocabulary-only**; no v1/v2 code is shipped today.

## Evidence / JTBD

When a future LE31 v2-AI surface proposes "the truth-ledger-with-snapshot-revision-semantics + content-addressed-by-SHA-256 + new-entry-points-to-predecessor primitive" (e.g., a v2 surface that introduces an AI-assisted owner-side workflow like "the owner asks the AI assistant to revise a daily-recap; the AI assistant proposes a revised version; the original version is preserved as a snapshot; the revised version creates a new entry pointing to the original via the SHA-256 content hash; the owner can review the revision history via the linked-list-of-content-addressed-records"), the owner wants *a primitive that proves the demand for this shape exists in 2026*, but struggles because *LE31 has no documented evidence that "append-only + signed + hash-chained + revised-by-snapshots + content-addressed-by-SHA-256 + new-entry-points-to-predecessor" is a real demand signal*, so that *the v2-AI surface can be defended with "this is what an independent maintainer shipped in 2026 with the same snapshot-revision + content-addressed-by-SHA-256 framing"*.

- **Evidence class**: observed (the description names the 14-dimensional primitive set explicitly: `append-only + signed + hash-chained + record-store + revised-by-snapshots + never-modified-in-place + content-addressed-by-SHA-256 + new-entry-points-to-predecessor + truth-ledger + audit-trail + ed25519 + merkle-tree + provenance + Rust`).
- **Confidence**: medium for the vocabulary match (the verbatim description names the 14-primitive set); low for transferability (LE31 v1 has no v2-AI surface; the 23 KB tiny repo is the smallest v2-AI pick of the 74-pass series; the Rust core requires PyO3 wrapper for Python integration; the 0★/0⑂ is a low community-traction signal).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant + aiogram + HTMX + Postgres with no AI agent); the value is the *snapshot-revision-truth-ledger-vocabulary* — when the first v2 PR that adds a v2-AI surface with audit-trail-revision semantics lands, the AXIOVEX/axiomere pattern is a ready-made *named primitive*.

## Description

GitHub `AXIOVEX/axiomere` (MIT, 0★/0⑂, Rust core + Python SDK via PyO3, pushed 2026-10-12 = TODAY, 23 KB tiny + 8 KB Python SDK). Description (verbatim, parent-verified GitHub Search API re-parse 2026-10-12): *"Axiomere — a truth ledger: an append-only, signed, hash-chained record store (Rust) where records are revised by new snapshots and never modified in place. The records are content-addressed by SHA-256 and every revision creates a new entry pointing to its predecessor."* Topics (verbatim, parent-verified GitHub Search API, 8 topics): **`append-only, audit-trail, ed25519, immutable, ledger, merkle-tree, provenance, rust`**.

The architectural primitive has 4 sub-primitives that map 1:1 onto the LE31 v2-AI surface:

1. **`Append-only + never-modified-in-place`** — the *append-only* discipline means new records are appended; the *never-modified-in-place* discipline means existing records are never modified. The *append-only + never-modified-in-place* double-primitive is §3.1-aligned. The *never-modified-in-place* is the *strict-append-only* primitive (vs *relaxed-append-only* which allows back-dating).
2. **`Content-addressed-by-SHA-256 + new-entry-points-to-predecessor`** — every record is identified by its content hash (SHA-256), not by an external ID; every revision creates a new entry that points to its predecessor via the *content-addressed-by-SHA-256* hash. The *content-addressed-by-SHA-256* primitive is the §3.1 *content-addressed-storage* primitive; the *new-entry-points-to-predecessor* is the *linked-list-of-content-addressed-records* pattern, which is a portable linked-list + content-addressing pattern.
3. **`Revised-by-snapshots`** — when a record needs to be revised, a new *snapshot* record is created that supersedes the old record; the old record is preserved (never modified in place); the new record points to the old record via the *content-addressed-by-SHA-256* hash. The *revised-by-snapshots* discipline is the **strongest v2-AI audit-trail-event-sourcing vocabulary of the 74-pass series** (no other in-window candidate uses the snapshot-revision pattern).
4. **`Signed + hash-chained + ed25519 + merkle-tree + provenance + truth-ledger + audit-trail + immutable + Rust`** — the cryptographic-verifiability surface. The *signed* is the *cryptographic-signature* primitive (every record is signed); the *hash-chained* is the *hash-chain* primitive (each entry's hash includes the previous entry's hash, forming a tamper-evident chain); the *ed25519* is the *cryptographic-signature-algorithm* primitive; the *merkle-tree* is the *merkle-tree* primitive (enables efficient proofs of inclusion); the *provenance* is the *provenance* primitive (records where the data came from); the *truth-ledger* is the *truth-claim* primitive (a ledger that records truth claims, not just data); the *audit-trail* is the *audit-trail* primitive; the *immutable* is the *immutable-data* primitive; the *Rust* is the *implementation-language* primitive.

**The 1:1 mapping onto LE31 surface:**

| Axiomere primitive | LE31 equivalent | Charter section | Status |
|---|---|---|---|
| Append-only + never-modified-in-place | `StockEntry` + `audit_logs` schema (append-only atomic) | §3.1 ✓ | **Implemented (v1, partial)** |
| Content-addressed-by-SHA-256 | (LE31 v1 uses UUIDs, not SHA-256; the SHA-256 primitive is a v2 extension) | §3.1 | **Not implemented (v2-AI surface)** |
| Revised-by-snapshots | (LE31 v1 has no revision; the *snapshot-revision* discipline is a v2-AI extension) | §3.1 + v2-AI | **Not implemented (v2-AI surface)** |
| Signed + hash-chained + ed25519 | (LE31 v1 has no cryptographic-signature on `audit_logs`; the *signed-records* discipline is a v2-AI extension) | §3.1 + v2-AI | **Not implemented (v2-AI surface)** |
| Merkle-tree | (LE31 v1 has no merkle-tree; the *merkle-tree* discipline is a v2-AI extension) | v2-AI | **Not implemented (v2-AI surface)** |
| Provenance + truth-ledger + audit-trail | (LE31 v1 has no provenance/truth-claim/audit-trail-vocabulary; the *truth-ledger* discipline is a v2-AI extension) | v2-AI | **Not implemented (v2-AI surface)** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface that requires truth-ledger-with-snapshot-revision semantics), the implementation would add:

1. A `signature` column on the existing `audit_logs` table (Alembic migration) for v2-AI receipts (a str column that stores the SHA-256 content hash + ed25519 signature of the receipt payload).
2. A `predecessor_hash` column on the existing `audit_logs` table (Alembic migration) for v2-AI snapshot revisions (a str column that stores the SHA-256 content hash of the predecessor record, nullable for genesis records).
3. A new `SnapshotRevision` table (Alembic migration) with columns: `id` (UUID), `predecessor_id` (UUID FK to `audit_logs` nullable for genesis), `content_hash` (str SHA-256), `signature` (str ed25519), `revised_at` (timezone-aware datetime), `revised_by` (str), `revision_reason` (str).
4. A `content_addressed_storage` table (Alembic migration) with columns: `id` (UUID), `content_hash` (str SHA-256 unique), `content_type` (str), `content_payload` (JSON), `created_at` (timezone-aware datetime), `created_by` (str).
5. A `GET /v2/snapshot-revisions/{entity_type}/{entity_id}` endpoint that returns the snapshot-revision history for the given entity (linked list of content-addressed records).
6. A `POST /v2/snapshot-revisions/{entity_type}/{entity_id}/revise` endpoint that creates a new snapshot revision (charter §3.1 *explicit-state-transition* primitive applied to audit-trail-record-revision; requires explicit owner confirmation per charter §3.4 *human-gate* invariant).
7. A `GET /v2/content-addressed/{content_hash}` endpoint that returns the content-addressed record for the given SHA-256 content hash.

The HANDOFF is to evaluate whether the v2-AI surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

## Telegram interaction

**No new Telegram interaction today.** The defer artifact is documentation only.

If the future v2-AI trigger condition fires (first v2 PR that introduces a v2-AI surface with truth-ledger-with-snapshot-revision semantics), the implementation would add a single Telegram message type:

- `snapshot_revision_request` (sent to the owner): *"A snapshot revision is proposed: {entity_type} {entity_id}. Reply /confirm to create the revision, /reject to discard, /view to see the predecessor."* The owner confirms or rejects via Telegram inline keyboard. The confirmation creates a new `SnapshotRevision` record with `predecessor_id = <predecessor_uuid>` + `content_hash = sha256(new_content)` + `signature = ed25519(new_content)`.

## Dependencies

- **Existing LE31 v1 primitives** (no change): `audit_logs` schema (append-only atomic) + `StockEntry` schema (append-only atomic). Both are already implemented in LE31 v1.
- **No new dependencies** are required for the defer artifact.
- **Future v2-AI surface** (if trigger fires): would require the `signature` column + `predecessor_hash` column on `audit_logs` (Alembic migration) + new `SnapshotRevision` table + new `content_addressed_storage` table + 3 new FastAPI endpoints. The aiogram v3 bot would require 1 new handler type (`snapshot_revision_request`).

## Open questions

- **Will the future v2-AI surface ever need a truth-ledger-with-snapshot-revision semantics?** The LE31 v1 `audit_logs` schema is already an append-only ledger. The *snapshot-revision* discipline is an extension of the *append-only-ledger* primitive that allows revisions while preserving the revision history. Sister-shape to features 187+188+232+287-289+299-304 (the persistent v2-AI audit-trail vocabulary cluster) but with the unique *snapshot-revision* framing.
- **Is the Rust core + Python SDK via PyO3 portable to LE31 stack?** The PyO3 wrapper pattern is a well-known Rust-Python interop mechanism; the `axiomere-python` 8 KB sister-shape is the PyO3 wrapper. The PyO3 pattern is portable to LE31 stack but adds a build-time dependency (Rust toolchain + maturin). Recommend evaluating the PyO3 build complexity in a future v2 polish pass.
- **Is the SHA-256 content-addressing portable to LE31's UUID-based schema?** The LE31 v1 schema uses UUIDs as primary keys (charter §3.1 *UUID-primary-key* discipline). The SHA-256 content-addressing is a v2 extension that adds a `content_hash` column alongside the UUID primary key. The two primitives are not mutually exclusive (the UUID identifies the record in the database; the SHA-256 identifies the record by its content).

## Why this matters

The **`append-only + signed + hash-chained + record-store + revised-by-snapshots + never-modified-in-place + content-addressed-by-SHA-256 + new-entry-points-to-predecessor + truth-ledger + audit-trail + ed25519 + merkle-tree + provenance + Rust`** 14-dimensional primitive is the **canonical v2-AI snapshot-revision-truth-ledger-vocabulary** of the 74-pass series. The *revised-by-snapshots* discipline is the **strongest v2-AI audit-trail-event-sourcing vocabulary of the 74-pass series** (no other in-window candidate uses the snapshot-revision pattern; sister-shape `Bastardki11er/tally` uses append-only-history without snapshots; sister-shape `warrant-ai/warrant` uses ed25519 + merkle-tree without snapshots; sister-shape `farooqarahim/glassbox` uses Ed25519 + ML-DSA-65 without snapshots).

When the first v2 PR that adds a v2-AI surface with audit-trail-revision semantics lands, the AXIOVEX/axiomere pattern is a ready-made *named primitive* for the *snapshot-revision + content-addressed-by-SHA-256 + new-entry-points-to-predecessor* vocabulary. The defer artifact is a parking-lot reference, not a build candidate.
