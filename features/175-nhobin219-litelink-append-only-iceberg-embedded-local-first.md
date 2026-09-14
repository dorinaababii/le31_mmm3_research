# Feature 175 — `nhobin219-litelink-append-only-iceberg-embedded-local-first` (defer)

> **NEW observation (2026-09-14).** Documents in-window GitHub repo `nhobin219/litelink` (**Apache-2.0**, **3★/0⑂**, Python, **pushed 2026-09-03T06:23:07Z**, in-window by `pushed_at`, 2.2 MB, **created 2026-08-12T21:58:42Z** — 32-day-old repo, single in-window push). Description (verbatim from GitHub API, parent-verified direct-GET 2026-09-14): *"Durable append-only capture into Iceberg tables; embedded and local-first."* Topics (verbatim from raw JSON, parent-verified): `append-only, data-capture, durability, embedded-database, iceberg, lakehouse, parquet, python, sqlite, streaming`. README motivation paragraph (verbatim, parent-verified 2026-09-14): *"It exists because doing this by hand goes wrong the same way every time: one production capture system had 125,884 objects, 62.5% of them under 16 KiB, Parquet files at 2 rows each, a compaction routine nothing ever scheduled, and an in-memory buffer a `SIGKILL` emptied."* README key sentence (verbatim): *"no read on the hot path touches the network."* Bucket: **v2 (durable-append-only-capture + Iceberg export primitive for owner-side audit-log sharing; v2 surface, not v1 — LE31 v1 is single-restaurant, no accountant-share surface)** — pick C of Brainstorm 2026-09-14 (parent research issue HMM-249). Build verdict: `defer` (parking-lot). Zero build time today. The 32-day-old repo with single in-window push is the demand-signal, not the code.

## Goal

Retain the **`SQLite buffer → local Iceberg table → remote Iceberg table`** three-tier capture primitive as a persistent cross-section reference for the LE31 v2 *durable-append-only-capture + audit-log export* surface, and document the **explicit anti-pattern reference** that an independent maintainer documented in 2026 — *"125,884 objects, 62.5% under 16 KiB, Parquet files at 2 rows each, compaction routine nothing ever scheduled, in-memory buffer a SIGKILL emptied"* is the explicit list of things the LE31 `audit_logs` table should NOT do when v2 introduces export. The artifact is the persistent cross-section reference + the named *durable-append-only-capture* primitive + the *explicit anti-pattern* warning. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **`SQLite buffer → local Iceberg table → remote Iceberg table`** three-tier capture primitive: (1) hot-path writes go to a local SQLite buffer that is durable on commit (unsealed rows only); (2) at `target_seal_size`, the buffer is sealed into a local Iceberg table (Parquet files + Iceberg metadata); (3) the local Iceberg table is synced to a remote Iceberg table on S3 (or any object store). Reads span all three tiers; the catalog is a SQLite file rather than a service. Sister-shape to features 30 (`append-only-audit-redirect`) + 49 (`postledger-tamper-evident-hash`) + 81 (`append-only-immutable-audit-check`).
- A written record of the **`no read on the hot path touches the network`** key sentence: the hot-path (the operator-facing surface, the cook-Telegram-bot, the owner-daily-recap) reads from the local SQLite buffer + local Iceberg table only; network reads are deferred to the remote-Iceberg-table tier, which is read by background processes or accountant-facing surfaces. This is the **LE31 phone-first operator posture applied to data egress**: the operator-facing surface never blocks on a network call. Sister-shape to feature 23 (`sse-cook-channel`) + feature 35 (`sse-replay-buffer`).
- A written record of the **`append-only + durability + streaming + parquet + iceberg`** topic tag set: the capture primitive is explicitly append-only (no mutable fields), explicitly durable (commits to SQLite before acknowledging the write), explicitly streaming (no bulk-load step), and explicitly Parquet+Iceberg (columnar format + table-format metadata). This is the §3.1 explicit-state-transitions primitive applied to data egress. Sister-shape to feature 30 + 49 + 81.
- A written record of the **explicit anti-pattern warning** from the README motivation paragraph: *"125,884 objects, 62.5% under 16 KiB, Parquet files at 2 rows each, compaction routine nothing ever scheduled, in-memory buffer a SIGKILL emptied"* — this is the **negative reference** for any future LE31 v2 surface that proposes an in-memory audit buffer, or a "write-and-forget" audit pattern without a compaction routine, or a Parquet-output-without-Iceberg-metadata pattern. LE31 v2 audit-log export MUST NOT replicate any of these four failure modes.
- A decision record: today's verdict is `defer` because (1) the repo is 3★ with single in-window push (32-day-old); (2) LE31 v1 has no audit-log export surface (v1 is single-restaurant, the owner trusts the system); (3) the *durable-append-only-capture* primitive is the brainstorm value, not the code.

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot (charter §3.1: explicit state transitions; v1 surfaces are sufficient for v1 ops).
- Any change to LE31 v1's `StockEntry` schema or `audit_logs` schema.
- Any change to LE31 v1's owner-side surfaces (owner-daily-recap-telegram, owner-recap-persona-voice, owner-no-account-live-floor-link).
- Adoption of the litelink codebase (single maintainer; Apache-2.0 permissive but the codebase is a generic append-only library, not restaurant-specific).
- Cross-pollination with charter §3.4 (litelink is a deterministic append-only library; no AI integration in the description or topics).

## Evidence / JTBD

When a future LE31 v2 surface proposes "the audit-log export surface for an external accountant or tax authority" (e.g., a v2 surface that introduces "share the audit-log hash-chain with my accountant" or a v2 surface that introduces multi-restaurant federation), the owner wants *a primitive that proves the demand for a durable-append-only-capture + Iceberg export surface exists in 2026*, but struggles because *LE31 has no documented evidence that "no read on the hot path touches the network + SQLite → local Iceberg → remote Iceberg" is a real architectural pattern*, so that *the v2 surface can be defended with "this is what an independent maintainer shipped in 2026 with the durable-append-only-capture primitive."*

- **Evidence class**: observed (the litelink description + topics + README name the primitives explicitly: `append-only, data-capture, durability, embedded-database, iceberg, lakehouse, parquet, python, sqlite, streaming`; `Durable append-only capture into Iceberg tables; embedded and local-first`; `no read on the hot path touches the network`).
- **Confidence**: medium-high for the demand signal (the description is direct; the topic tags are LE31-aligned; the 3★ floor is the highest of any append-only cluster candidate in the 46-pass series); low for transferability (LE31's stack is FastAPI+SSE+Postgres+aiogram, litelink is a standalone Python library with SQLite + Iceberg; LE31 v1 has no audit-log export surface at all).
- **Real observed LE31 JTBD**: zero direct JTBD today (LE31 v1 is single-restaurant, the owner trusts the system; no accountant-share surface); the value is the *v2-architecture vocabulary* — when the first v2 PR that adds any "share the audit-log with an external party" surface lands, the litelink *durable-append-only-capture* primitive is the named architectural reference.
- **The value is vocabulary + anti-pattern, not direct demand**: when the first v2 PR that adds an audit-log export surface (if/when the owner approves the v2 audit-export surface) lands, the litelink pattern is a ready-made *named primitive* and the `SQLite → local Iceberg → remote Iceberg + no read on the hot path touches the network + append-only + durability + Parquet + streaming` vocabulary slots into features 30 (`append-only-audit-redirect`) + 49 (`postledger-tamper-evident-hash`) + 81 (`append-only-immutable-audit-check`) + 134 (`echo-auditable-memory-plane-stockentry-audit`) + 154 (`chronology-protocol-post-quantum-opentimestamps-anchored-audit-log-primitive`) + 168 (`edusouzaxgv-asset-ledger-content-addressed-append-only-manifest`) + 169 (`akoffice933-openshare-ledger-sha256-hash-chain-git-replayable`).

## Description

GitHub `nhobin219/litelink` (Apache-2.0, 3★/0⑂, Python, pushed 2026-09-03T06:23:07Z, created 2026-08-12T21:58:42Z, 2.2 MB). Description (verbatim, parent-verified GitHub API direct-GET 2026-09-14): *"Durable append-only capture into Iceberg tables; embedded and local-first."*

The architectural primitive has one core principle and three sub-primitives that map 1:1 onto the LE31 v2 *audit-log export* surface:

1. **"SQLite buffer (durable on commit, unsealed rows only)"** — the hot-path writes go to a local SQLite buffer that is durable on commit. The buffer holds *unsealed rows only* — once the buffer reaches `target_seal_size`, the rows are sealed into the local Iceberg table and removed from the buffer. This is the §3.1 explicit-state-transitions primitive applied to data egress: every write is durable before acknowledgement; no write is lost on `SIGKILL`; no write is in-memory-only. Sister-shape to feature 30 (`append-only-audit-redirect`) + feature 49 (`postledger-tamper-evident-hash`).
2. **"Local Iceberg table (a rolling window, reads land here)"** — the local Iceberg table holds the rolling-window history (the last N days, or the last N GB). The operator-facing surface reads from the local Iceberg table (not from the remote Iceberg table), because *"no read on the hot path touches the network."* This is the LE31 phone-first operator posture applied to data egress: the operator-facing surface never blocks on a network call. Sister-shape to feature 23 (`sse-cook-channel`) + feature 35 (`sse-replay-buffer`).
3. **"Remote Iceberg table (full history, on S3)"** — the remote Iceberg table holds the full history, on S3 (or any object store). The sync step uploads data files and registers them into the archive. Every other machine (an accountant-facing surface, a tax-authority-facing surface, a multi-restaurant federation surface) reads from the archive using any Iceberg engine and nothing from litelink. Sister-shape to feature 134 (`echo-auditable-memory-plane-stockentry-audit`) + feature 168 (`edusouzaxgv-asset-ledger-content-addressed-append-only-manifest`).

**The 1:1 mapping onto LE31 v2 surface:**

| litelink primitive | LE31 v2 equivalent | Charter section | Status |
|---|---|---|---|
| SQLite buffer (durable on commit) | `audit_logs` table (PostgreSQL, durable on commit) | §3.1 ✓ | **Implemented (v1)** |
| Local Iceberg table (rolling window) | (LE31 v1 has no Iceberg export surface) | v2 | **Not implemented** — v2 surface |
| Remote Iceberg table (full history, on S3) | (LE31 v1 has no S3 archive surface) | v2 | **Not implemented** — v2 surface |
| No read on the hot path touches the network | Phone-first operator web UI + local SSE channel | §3.1, §3.2 ✓ | **Implemented (v1)** |
| Append-only + durability + streaming | `audit_logs` table (append-only, durable, transactional) | §3.1 ✓ | **Implemented (v1)** |
| Parquet + Iceberg (columnar format + table-format metadata) | (LE31 v1 has no columnar export) | v2 | **Not implemented** — v2 surface |
| Embedded + local-first | SQLite as canonical store + no cloud by default | §3.1, §3.2 ✓ | **Implemented (v1)** |
| Apache-2.0 license | (LE31 is independent) | §3.2 ✓ | **Compatible (idea-portability)** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that adds audit-log export to an external party), the implementation would introduce:
- An `audit_export_buffer` table (LE31-side equivalent of the SQLite buffer; PostgreSQL with durability guarantees).
- An `audit_export_seal` background job that seals the buffer at `target_seal_size` into the local Iceberg table.
- An `audit_export_sync` background job that uploads the local Iceberg table to the remote Iceberg table on S3 (or any object store).
- An `audit_export_catalog` SQLite file that tracks the catalog state for the local + remote Iceberg tables.

This is **NOT a v1 surface** — LE31 v1 is single-restaurant, the owner trusts the system, and there is no accountant-share surface. The HANDOFF is to evaluate whether the v2 audit-log export surface is the right product-wedge for the next v2 PR.

## Implementation steps

**None today.** The defer artifact is documentation only.

If the future v2 trigger fires:
1. Add the `audit_export_buffer` table via Alembic migration.
2. Implement the `audit_export_seal` background job using APScheduler (already in LE31 stack).
3. Configure the `audit_export_sync` background job to upload to S3 (or any object store) using `boto3` (or any S3-compatible client).
4. Implement the `audit_export_catalog` SQLite file as a sidecar to the main LE31 Postgres database.
5. Add the operator-facing dashboard surface that reads from the local Iceberg table (NOT from the remote Iceberg table) — the operator-facing surface never blocks on a network call.
6. Add the accountant-facing export surface that reads from the remote Iceberg table — the accountant-facing surface is the only surface that touches the network.
7. New feature file at `features/NNN-audit-log-export-accountant-share-with-Iceberg.md` (NOT this defer artifact).

## Telegram interaction if any

None today. The defer artifact is documentation only.

If the future v2 audit-log export surface is approved, the owner-side Telegram bot could surface a *"your audit-log export is ready"* notification when the `audit_export_sync` background job completes. The notification would link to the operator-facing dashboard where the owner can verify the export before sharing. Sister-shape to feature 39 (`owner-daily-recap-telegram`) + feature 57 (`owner-recap-persona-voice`) + feature 82 (`owner-public-data-watch-bot`).

## Dependencies

- None today (defer artifact is documentation only).
- If the v2 audit-log export surface is approved: PyIceberg (Apache Iceberg Python client); boto3 (or any S3-compatible client); APScheduler (already in LE31 stack); the existing `audit_logs` table (already implemented); SQLite as a sidecar for the catalog (already in LE31 stack via SQLModel/Alembic).

## Open questions

- Does the owner approve a v2 audit-log export surface for an external accountant or tax authority? (Currently no — v1 is single-restaurant, the owner trusts the system, no accountant-share surface.)
- Does the owner approve a v2 multi-restaurant federation surface that uses the remote Iceberg table for cross-restaurant audit sharing? (Currently no — v1 is single-restaurant.)
- Does the owner approve Iceberg + S3 as the v2 audit-export stack, or does the owner prefer a different stack (e.g., a custom Parquet-on-S3 stack without Iceberg metadata, or a hash-chain stack per feature 49 `postledger-tamper-evident-hash`)? (Currently unspecified — the v2 audit-export stack design is open.)

## Why this matters

The litelink repo is the **v2-architecture vocabulary reference** for the LE31 v2 audit-log export surface. The three-tier capture primitive (SQLite buffer → local Iceberg table → remote Iceberg table) is the **named architectural reference** for any future v2 surface that asks *"how do we let the owner share the `audit_logs` chain with an external party without losing durability guarantees?"* The key sentence *"no read on the hot path touches the network"* is the **LE31 phone-first operator posture applied to data egress**: the operator-facing surface never blocks on a network call. The README motivation paragraph *"125,884 objects, 62.5% under 16 KiB, Parquet files at 2 rows each, compaction routine nothing ever scheduled, in-memory buffer a SIGKILL emptied"* is the **explicit anti-pattern reference** for any future LE31 v2 surface that proposes an in-memory audit buffer, or a "write-and-forget" audit pattern without a compaction routine, or a Parquet-output-without-Iceberg-metadata pattern — LE31 v2 audit-log export MUST NOT replicate any of these four failure modes. No code today; the value is the v2-architecture vocabulary + the named anti-pattern warning for the future v2 audit-export surface.
