# Feature 168 — edusouzaxgv-asset-ledger-content-addressed-append-only-manifest (defer)

> **NEW observation (2026-09-13).** Documents in-window GitHub repo `edusouzaxGV/asset-ledger` (MIT, **0★/0⑂**, Python, **pushed 2026-09-12**, in-window by push only, **created 2026-09-12** — 1-day-old repo, 101 KB). Description (verbatim from GitHub API): *"Provenance-tracking backup for generated media. Content-addressed identification, append-only manifest, lineage queries and drift detection. Pluggable storage backends."* Topics: `[]` (none declared). Bucket: **v2 architecture-reference (charter §3.1 territory; content-addressed + append-only + lineage + pluggable storage pattern; off-domain for restaurant v1)** — watch-list defer. Zero build time today.

## Goal

Retain the **"provenance-tracking backup for generated media with content-addressed identification + append-only manifest + lineage queries + drift detection + pluggable storage backends"** primitive as a persistent cross-section reference for any future LE31 v2 surface that needs to ask "where did this value come from?" — typically a v2 owner-facing audit-trail surface, a v2-AI surface that consults `audit_logs`, or a v2 surface that introduces a second stakeholder who needs independent verification of stock changes. The artifact is the persistent cross-section reference + a candidate *immutable-then-derivable* design discipline for the next v2-hardening primitive. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"content-addressed identification"** primitive: every asset gets a *content hash* (e.g. SHA-256) computed from its bytes; the hash IS the identifier. Two assets with identical bytes have identical identifiers; two assets with different bytes have different identifiers. This is the load-bearing primitive for any future LE31 surface that needs to deduplicate or verify "is this the same value as yesterday?".
- A written record of the **"append-only manifest"** primitive: a *manifest* is a list of (content hash, timestamp, metadata) tuples; *append-only* means new entries are added but old entries are never modified; the manifest is the *index* over the content-addressed store.
- A written record of the **"lineage queries"** primitive: given a content hash, walk the manifest to find all the times the hash appeared, all the metadata associated with each appearance, and all the downstream assets that referenced it. This is the *audit query* primitive.
- A written record of the **"drift detection"** primitive: when an asset's bytes change but its hash changes too, drift detection notices the discrepancy. This is the *tamper-evident* primitive: the manifest says the hash is X, but the file's bytes hash to Y, so the file was tampered with.
- A written record of the **"pluggable storage backends"** discipline: the manifest doesn't care where the bytes live (local disk, S3, GCS, IPFS); the same manifest works against any backend. This is the *storage-agnostic* discipline — the LE31 owner can switch backends without rewriting the audit surface.
- A decision record: today's verdict is `defer` because LE31 v1 has no second stakeholder (single owner, single restaurant), no v2 audit-export surface, and no AI integration. The *content-addressed + append-only manifest* pattern is a v2-hardening primitive that doesn't have a v1 trigger.

**Out of scope (defer artifact):**
- Any change to LE31 v1's `StockEntry` ledger (charter §3.1: explicit state changes; v1 ledger is sufficient for v1 ops).
- Any change to LE31 v1's `audit_logs` schema.
- Any new owner-facing audit-trail surface (LE31 v1 has no designed audit-trail surface; introducing one would require a charter decision).
- Adoption of the asset-ledger codebase (the repo is 1 day old, 101 KB, MIT Python; the *primitive* is portable; the *codebase* is not adoptable without a full read-and-eval).
- Cross-pollination with cross-section features 121 / 122 / 129 / 133 / 134 / 135 / 141 / 167 (this primitive is the *manifest* layer; the others are *audit-chain* layers — different primitives, same family).

## Evidence / JTBD

When a future LE31 v2 owner-facing audit-trail surface is introduced (e.g. "show me every StockEntry change for menu item X in the last 30 days, with the bytes that changed"), the owner wants *a primitive that answers "where did this value come from?" with content-hash-based deduplication + lineage walk + drift detection + storage-agnostic backend*, but struggles because *LE31 v1's `audit_logs` is text-only and has no content-hash discipline*, so that *the v2 surface can answer "is this value still the same as yesterday?" without reading the entire database*.

- **Evidence class**: observed (the asset-ledger description names all five sub-primitives: `provenance-tracking backup`, `content-addressed identification`, `append-only manifest`, `lineage queries`, `drift detection`, `pluggable storage backends`).
- **Confidence**: medium for the primitive match (the description is direct; the five primitives are well-established in content-addressed storage research); low for transferability (the asset-ledger is for media backup, not restaurant ops; the *primitive* is portable, the *use case* is not).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no designed audit-trail surface; the v2 surface that would *use* the primitive doesn't exist.
- **The value is naming, not direct demand**: when the first v2 audit-trail surface lands (if/when the owner asks for content-hash-based deduplication), the asset-ledger pattern is a ready-made *named primitive* — and the *content-addressed + append-only manifest + lineage queries + drift detection + pluggable storage* vocabulary slot into features 121 (Field-Tier Minimization, *what is committed*) / 122 (Trace Integrity CAIT, *what is queried*) / 129 (LEDGER Trace Graph, *what edges*) / 133 (HANSARD, *who witnessed*) / 134 (ECHO, *record shape*) / 135 (DreamLedger, credit ledger dual) / 141 (KRINEIA, *append-only as proof*) / 167 (Pick A today).

## Description

GitHub `edusouzaxGV/asset-ledger` (MIT, 0★/0⑂, Python, pushed 2026-09-12, created 2026-09-12, 101 KB). Description (verbatim): *"Provenance-tracking backup for generated media. Content-addressed identification, append-only manifest, lineage queries and drift detection. Pluggable storage backends."*

The architectural primitive has five components:

1. **Content-addressed identification** — every asset (file, image, document) gets a content hash computed from its bytes (typically SHA-256). The hash IS the identifier: `sha256(bytes)`. Two assets with identical bytes have identical identifiers; two assets with different bytes have different identifiers.
2. **Append-only manifest** — the manifest is a list of `(content_hash, timestamp, metadata)` tuples, stored in an append-only log (no entry is ever modified or deleted; only new entries are added).
3. **Lineage queries** — given a content hash, walk the manifest to find: (a) all the times the hash was added; (b) all the metadata at each appearance; (c) all the downstream assets that referenced the hash in their own metadata; (d) the full provenance tree back to the original source.
4. **Drift detection** — when reading an asset from storage, recompute its content hash and compare to the manifest's recorded hash. If they differ, the asset was tampered with (or the storage backend is corrupted); raise a drift alarm.
5. **Pluggable storage backends** — the manifest doesn't care where the bytes live (local disk, S3, GCS, IPFS, in-memory); the same manifest works against any storage layer that exposes `read(hash) → bytes`.

**The 1:1 mapping onto LE31 v2 architecture (if/when audit-trail surfaces are designed):**

| asset-ledger primitive | LE31 v2 equivalent | Charter section | Status |
|---|---|---|---|
| Content-addressed identification | (LE31 v1 has no content-hash discipline on `audit_logs`; each row has its own primary key, not a content-derived identifier) | §3.1 + v2 hardening | **Not implemented** |
| Append-only manifest | (LE31 v1's `audit_logs` is append-only; this primitive is partially implemented) | §3.1 ✓ | **Implemented (v1, partial)** — `audit_logs` is append-only but not hash-indexed |
| Lineage queries | (LE31 v1 has no lineage walk; queries are SQL on `audit_logs`) | v2 hardening | **Not implemented** |
| Drift detection | (LE31 v1 has no drift detection; `audit_logs` is text-based and assumes the database is trustworthy) | v2 hardening | **Not implemented** |
| Pluggable storage backends | (LE31 v1 uses Postgres as the only backend) | v2 hardening | **Not implemented** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that adds a content-hash-based deduplication or lineage-walk surface), the v2 schema migration would need:

- `content_manifest` table (append-only): `id`, `content_hash` (SHA-256 hex), `ts`, `actor_user_id`, `metadata_json`, `parent_hash`, `entry_hash` (computed as `sha256(parent_hash + canonical_json(this_row))`).
- `content_storage` (any backend; manifest doesn't care): `content_hash → bytes`.
- `audit_logs.content_hash` field: nullable foreign key to `content_manifest.content_hash` — when an audit-log entry references a StockEntry, the audit-log row can record the content hash of the StockEntry at the time of the change.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v2 implementation would include:
1. Create the `content_manifest` SQLModel class.
2. Add the `content_hash` field to `audit_logs`.
3. Wire the content-hash computation into the StockEntry write path (so every `StockEntry` write also appends to `content_manifest`).
4. Add a v2 surface that exposes lineage queries (e.g. "show me all the StockEntries that referenced this ingredient batch").
5. Add drift detection on read (any time a `StockEntry` is read, recompute its hash and compare to `content_manifest`).

**No existing code change today.**

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

Future v2: if the owner-facing audit-trail surface is built, it would likely be exposed through a Telegram command (`/audit <menu_item_id>` → reply with the lineage walk + drift status). But the cook's daily ops surface is unaffected.

## Dependencies

- **Charter §3.1 invariant compatibility**: ✓ (append-only manifest IS the strongest form of "explicit state changes" — every entry is immutable and hash-indexed).
- **§3.2 license compatibility**: ✓ (asset-ledger is MIT permissive).
- **Stack compatibility**: ✓ (Python + SQLModel can hold the schema; the *pluggable storage backend* discipline maps onto LE31's existing Postgres-backed storage).
- **First v2 surface that needs provenance over `audit_logs` rows**: trigger condition.

## Open questions

1. **Does LE31 v2 need content-hash discipline?** v1 has not surfaced a JTBD for it. The v2 question is whether the owner would ever need to verify "is this StockEntry still the same as yesterday?" — currently the SQL query "select * from stock_entry where id = X" is sufficient.
2. **What is the retention policy for `content_manifest`?** v1 retention is "indefinite" (charter §3.1); v2 retention may want a rolling-window policy.
3. **What is the storage backend?** v2 should design for pluggability from day 1, but v1 only needs Postgres.

## Why this matters

The **content-addressed identification + append-only manifest + lineage queries + drift detection + pluggable storage backends** vocabulary is the **v2-hardening primitive** for any future LE31 surface that needs to ask "where did this value come from?" without re-implementing storage. Without this vocabulary, the first audit-trail surface would have to re-invent content-hashing, manifest storage, and lineage walks from scratch. With this vocabulary, the v2 surface can adopt the asset-ledger pattern directly: content-hash the StockEntry, append to the manifest, walk the lineage on read, raise drift alarms on tamper, and use whatever storage backend the LE31 owner prefers.

Companion artifacts: features 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 129 (LEDGER Trace Graph), 133 (HANSARD), 134 (ECHO), 135 (DreamLedger), 141 (KRINEIA), 167 (Pick A today) — all ripgrep-verified distinct from this artifact.
