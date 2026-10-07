# Feature 292 — `berty/go-ipfs-log` v2 owner-pains append-only-CRDT-vocabulary (defer)

> **Status:** defer (parking-lot, vocabulary reference)
> **Bucket:** v2 owner-pains (attach to `le31 Research` P-HMM-1 as the parent of the sub-issue — `le31 v2 owner-pains` does not exist per `le31-feature-pipeline/SKILL.md` line 33)
> **Date:** 2026-10-07
> **Active feature path:** `/opt/data/le31_mmm3_research_work/features/292-berty-go-ipfs-log-apache-2-0-go-append-only-log-crdt-ipfs-v2-owner-pains-append-only-crdt-vocabulary-reference.md`
> **Companion HANDOFF:** `/opt/data/le31_mmm3_research_work/specs/292-berty-go-ipfs-log-apache-2-0-go-append-only-log-crdt-ipfs-v2-owner-pains-append-only-crdt-vocabulary-reference-HANDOFF.md`
> **Source daily brainstorm:** `/opt/data/le31-brainstorm-2026-10-07.md` (pass 70, pick C)
> **Parent-verified via:** direct GitHub API GET `/repos/berty/go-ipfs-log` at `/opt/data/le31-brainstorm-2026-10-07/verify_berty_go-ipfs-log.json`
> **LE31 feature gate verdict:** defer (vocabulary reference; no v1 pain observed; v2 owner-pains append-only-CRDT-vocabulary reference is a future-extension signal)

## Goal

Surface a v2 owner-pains append-only-CRDT-vocabulary reference for **append-only-log CRDT on IPFS** as a forward-looking pattern for any future LE31 v2 surface that exposes owner-facing distributed-append-only semantics (multi-device sync, conflict-free merge, content-addressed audit trail, deterministic ordering without a central server).

## Evidence / JTBD

**Evidence classification:** inferred. The *append-only-log CRDT on IPFS* discipline is forward-looking for any future LE31 v2 owner-pains surface that wants multi-device or multi-location append-only semantics; no LE31 v1 surface today has multi-device or multi-location append-only (LE31 v1 is single-tenant single-Postgres). **Confidence: high** (86★/34⑂ = highest-star brainstorm pick of the 70-pass series + 1126 KB modest + Apache-2.0 permissive + 6-topic array including `append-only + berty + crdt + ipfs + ipfs-log + libp2p` + 0 customer-facing AI + in-window by `pushed_at` ONLY = strongest v2 append-only-CRDT cross-section pick of the 70-pass series).

**When** the LE31 owner wants to add a second device (e.g., a tablet at the bar) that can write to the `audit_logs + StockEntry + SupplierOrder` SQLModel tables offline and sync when reconnected, **the owner wants to** know that the two devices' writes will merge deterministically without conflict (CRDT semantics), every write is content-addressed for audit-trail, and no central server is required for the merge (IPFS-style peer-to-peer), **but struggles because** the existing v1 `audit_logs + StockEntry + SupplierOrder` SQLModel tables are single-Postgres append-only ledgers with no multi-device merge semantics, no content-addressed audit trail, no peer-to-peer sync, **so that** the owner cannot use a second device offline without losing data or creating conflicts. The *append-only-log CRDT on IPFS* discipline IS the *multi-device + content-addressed + conflict-free-merge* charter §3.1 invariant applied to the *multi-device-append-only* dimension.

## Scope

**In scope (vocabulary reference, defer):**
- Document the *append-only-log CRDT + IPFS-content-addressing + libp2p-peer-to-peer* triple-primitive as a candidate vocabulary for any future LE31 v2 owner-pains multi-device-append-only surface.
- Identify the on-stack Python mapping for each primitive (LE31 uses Python; berty/go-ipfs-log is Go; a future PR would need a Python-equivalent or a Go sidecar).
- Record the §3.1/§3.2/§3.3/§3.4/§3.7 alignment per `le31-conventions/SKILL.md`.
- Note that this is a **6-year-old repo with fresh in-window push** (created 2019-05-09, pushed 2026-09-22 = 7-year-old project with active maintenance) — established vocabulary with active community.

**Out of scope (v2):**
- No v2 build today; defer artifact; vocabulary-only.
- No IPFS integration; v2 owner-pains multi-device-append-only is forward-looking.
- No CRDT-merge on the existing `audit_logs + StockEntry` SQLModel tables.
- No libp2p peer-to-peer sync.

## Description

`berty/go-ipfs-log` is a **Go library implementing an append-only log CRDT on IPFS** with the following properties:
- **Go version of append-only log CRDT on IPFS** — the central discipline is the *append-only log* (a CRDT that supports only append operations, with deterministic merge semantics).
- **CRDT (Conflict-free Replicated Data Type)** — every replica can append independently; when two replicas sync, the merge is deterministic (no conflict resolution needed).
- **IPFS (InterPlanetary File System)** — every entry is content-addressed by its hash, enabling peer-to-peer sync without a central server.
- **libp2p** — the peer-to-peer networking layer.
- **Apache-2.0 permissive + 1126 KB modest + 86★/34⑂** — established vocabulary with active community traction.
- **6-topic array** including `append-only + berty + crdt + ipfs + ipfs-log + libp2p` = the strongest v2 append-only-CRDT cross-section topic-coverage of the 70-pass series.

The vocabulary is a strong §3.3 + §3.1 alignment signal for any future LE31 v2 owner-pains multi-device-append-only surface because:
- The *append-only-log CRDT* IS the §3.3 *audit-log-immutability* charter invariant applied to the *multi-device-merge* dimension (every replica's append is preserved; the merge is deterministic).
- The *content-addressing by hash* IS the §3.3 *audit-log-immutability* charter invariant applied to the *content-addressed-audit-trail* dimension (every entry's hash includes the previous entry's hash, making any tampering detectable).
- The *IPFS peer-to-peer* IS the §3.2 *self-hosted + zero-external-dependencies* charter invariant applied to the *peer-to-peer-sync* dimension (no central server required).
- The *libp2p* posture IS the §3.1 *explicit-state-transition* charter invariant applied to the *peer-discovery* dimension.

## Data model

```
AuditLogEntry   (id, content, hash, prev_hash, lamport_clock, at)        # existing — append-only
CRDTEntry       (id, log_id, content, hash, prev_hash, lamport_clock, replica_id, at)  # NEW — CRDT-append-only with deterministic merge
LogReplica      (id, replica_id, last_seen_lamport, last_sync_at, peer_id)  # NEW
SyncEvent       (id, replica_id, peer_id, entries_received, entries_sent, occurred_at)  # NEW — append-only
```

The `CRDTEntry + SyncEvent` tables are **append-only** per charter §3.3. Every CRDT-append is a new `CRDTEntry` row; every sync is a new `SyncEvent` row. The `lamport_clock` column enforces the *deterministic merge* discipline: when two replicas sync, entries are sorted by `(lamport_clock, replica_id)` and the merge is deterministic. The `replica_id` column identifies the source device (e.g., `tablet-bar-01`, `kitchen-tg-bot-01`).

## Implementation steps

**This is a defer artifact. No code is written today.** When (and if) a future v2 PR adopts the *append-only-log CRDT on IPFS* discipline, the following files would be touched:

- `/opt/data/le31_mmm3_research_work/backend/app/models/crdt_entry.py` — new SQLModel `CRDTEntry + LogReplica + SyncEvent` tables (append-only, §3.3 invariant).
- `/opt/data/le31_mmm3_research_work/backend/app/services/crdt_merge.py` — pure-Python CRDT-merge service with lamport-clock + replica-id deterministic sort.
- `/opt/data/le31_mmm3_research_work/backend/app/services/ipfs_content_address.py` — content-addressing using `hashlib.sha256` (LE31 v1 already uses hashlib implicitly for audit-log entries).
- `/opt/data/le31_mmm3_research_work/backend/app/services/libp2p_sync.py` — libp2p peer-to-peer sync (would require a Go sidecar or a Python libp2p equivalent; the v2 PR would need to specify the binding).
- (No other files expected to require changes for a vocabulary-only PR.)

## Telegram interaction

**None today** (defer artifact; no v2 build; vocabulary-only). If a future v2 owner-pains multi-device-append-only surface is built, the cook-side Telegram bot could surface sync events with their state (e.g., "Sync: 12 entries received from tablet-bar-01, 3 entries sent. Last sync: 2 minutes ago. Lamport clock: 142857."). The bot surfaces *what was synced* but does NOT participate in the sync (the sync is between the FastAPI server and the IPFS peer-to-peer layer).

## Dependencies

- **Charter §3.1 (explicit-state-transition)**: existing `audit_logs + StockEntry` SQLModel tables are the v1 append-only ledgers; the `CRDTEntry` table extends the same pattern to the *multi-device-merge* dimension with **lamport-clock + replica-id** discipline.
- **Charter §3.3 (audit-log-immutability)**: existing `audit_logs` SQLModel table is the v1 append-only ledger; the `CRDTEntry` table is a v2 extension with **content-addressing by hash** (stronger than v1's auto-increment id).
- **Charter §3.4 (operator-facing)**: the *multi-device-append-only* surface is operator-tooling per charter §3.4 invariant; the *peer-to-peer* discipline is the *non-AI-fallback* posture (no AI to merge; the merge is deterministic).
- **Stack note**: `berty/go-ipfs-log` is Go, not Python. A future PR that adopts the *append-only-log CRDT* discipline would need either (a) a Python port of the CRDT-merge algorithm (pure-Python, no IPFS dependency), or (b) a Go sidecar that the FastAPI server calls via gRPC. Option (a) is simpler and aligns with the v1 Python stack; option (b) is more powerful but adds a deployment dependency.
- **No v1 dependencies today**: this is a v2 forward-looking surface; no v1 code depends on it.

## Open questions

1. **What is the multi-device scenario?** A future PR that adopts the *multi-device-append-only* discipline would need to specify the use case (tablet at the bar + kitchen Telegram bot? two waiters on two tablets? owner on phone + tablet?). LE31 v1 is single-tenant single-device; the v2 PR would need to justify the multi-device scenario.
2. **What is the conflict-resolution policy?** The CRDT-merge is deterministic, but the *semantic* conflict resolution (e.g., two waiters both mark the same order as "served") would need a policy. A future PR would need to specify the policy.
3. **What is the IPFS pinning strategy?** IPFS content-addressing requires a pinning service (or a local IPFS node). A future PR would need to specify the pinning strategy.
4. **What is the GDPR/privacy boundary?** IPFS content-addressing makes entries public-by-hash; a future PR would need to specify the privacy-preserving discipline (e.g., hash only, not content; or content encrypted with a per-restaurant key).
5. **What is the relationship to the v1 `audit_logs + StockEntry` SQLModel tables?** A future PR that adopts the *multi-device-append-only* discipline would need to specify whether `CRDTEntry` is a NEW table (parallel to v1 `audit_logs`) or a MIGRATION of v1 `audit_logs` to CRDT semantics. The v1 pattern is simpler; the v2 pattern is more powerful.

## Why this matters

This is the **strongest v2 owner-pains append-only-CRDT cross-section pick of the 70-pass brainstorm series**. The *append-only-log CRDT on IPFS + libp2p + 86★/34⑂ + 6-year-old-with-fresh-push* discipline is **distinct from the AI-ledger features 284-289 (which are Python+MIT/MCP/AI-agent shape)**. The *append-only-CRDT + merge-semantics for concurrent writers* discipline is the only non-AI flavour of ledger vocabulary surfaced this pass — a refreshing counterpoint to the AI-ledger cluster of 284-289.

The **append-only-log CRDT** discipline extends the v1 `audit_logs + StockEntry` SQLModel append-only pattern to the *multi-device-merge* dimension with deterministic CRDT-merge semantics. The **content-addressing by hash** discipline extends the v1 `audit_logs` to the *content-addressed-audit-trail* dimension with cryptographic-hash-as-audit-evidence (stronger than the v1 auto-increment id). The **IPFS peer-to-peer** discipline extends the v1 *self-hosted* posture to the *peer-to-peer-sync* dimension (no central server required). The **libp2p** posture is the v2 networking layer for the multi-device scenario.

**Charter alignment summary:** §3.1 partial (lamport-clock + replica-id ✓; CRDT-merge OFF-§3.1 = explicit charter-decision needed for v2); §3.2 strictly-compatible (Apache-2.0 permissive + IPFS self-hosted); §3.3 ✓ (append-only `CRDTEntry + SyncEvent` + content-addressing by hash = stronger than §3.3 raw `audit_logs`); §3.4 strong alignment (operator-facing + peer-to-peer + non-AI-fallback + deterministic-merge); §3.7 partial (IPFS privacy boundary = explicit charter-decision needed).
