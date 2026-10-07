# HANDOFF — 292-berty-go-ipfs-log-v2-owner-pains-append-only-crdt-vocabulary-reference

**Status**: defer (parking-lot, vocabulary reference)
**Date**: 2026-10-07
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/292-berty-go-ipfs-log-apache-2-0-go-append-only-log-crdt-ipfs-v2-owner-pains-append-only-crdt-vocabulary-reference.md`
**LE31 feature gate verdict**: defer (vocabulary reference; no v1 pain observed; strongest v2 owner-pains append-only-CRDT cross-section pick of the 70-pass series)

## Trigger policy

This is a **defer artifact**. It does not start a build. It surfaces a dated, in-window v2 owner-pains append-only-CRDT vocabulary reference (`berty/go-ipfs-log`, Apache-2.0, 86★/34⑂, 1126 KB modest, Go, 6-topic array, in-window by `pushed_at` ONLY) for the next time the LE31 owner opens a v2 owner-pains multi-device-append-only surface window.

If the trigger condition (v2 owner-pains multi-device-append-only surface window opens) is met, the external coding agent should:

1. Read the active feature file in full.
2. Confirm the `berty/go-ipfs-log` repo is still in-window (pushed within last 7 days from the trigger date) and the description is still the same.
3. Implement the `CRDTEntry + LogReplica + SyncEvent` SQLModel tables as described in the active feature's Data model section.
4. Implement the CRDT-merge service (pure-Python; lamport-clock + replica-id deterministic sort; no external IPFS dependency).
5. Implement the content-addressing service (using `hashlib.sha256`; LE31 v1 already uses hashlib implicitly for audit-log entries).
6. Implement the libp2p sync service (Python libp2p equivalent or a Go sidecar; the v2 PR would need to specify the binding).
7. Run the v1 test suite + the new v2 multi-device-append-only test suite.
8. Surface any test failures to the owner (LE31 v1 has no multi-device-append-only today; the test suite will be green if `audit_logs + StockEntry` are single-source, but the *deterministic-merge* must be verified against a synthetic two-replica scenario).
9. Verify the v1 `audit_logs + StockEntry` SQLModel tables are untouched (the v2 `CRDTEntry` table is NEW, not a migration of v1 `audit_logs`).
10. Verify the *content-addressing by hash* discipline: every `CRDTEntry.hash` is a sha256 of `(content + prev_hash + lamport_clock + replica_id)`.

If the trigger condition is **not** met, do nothing. The defer artifact can be safely ignored until the owner opens a v2 owner-pains multi-device-append-only surface window.

## Mandatory inputs

- **Active feature**: `features/292-berty-go-ipfs-log-apache-2-0-go-append-only-log-crdt-ipfs-v2-owner-pains-append-only-crdt-vocabulary-reference.md`
- **Parent daily brainstorm report**: `/opt/data/le31-brainstorm-2026-10-07.md` (pass 70, pick C)
- **Raw fetches**: `/opt/data/le31-brainstorm-2026-10-07/gh_append_only_nd.json` (parent re-fetched the productive query) and `/opt/data/le31-brainstorm-2026-10-07/verify_berty_go-ipfs-log.json` (parent-direct-GitHub-API-GET)
- **Related picks from the 70-pass series**:
  - **Feature 287 — `noise01/endoxa`** — v2-AI governed-beliefs + append-only-ledger
  - **Feature 288 — `pete-builds/mcp-nixreview`** — v2-AI MCP-server + append-only-audit-ledger
  - **Feature 289 — `shivamk01here/LedgerLoop`** — v2-AI hash-chained-audit-ledger + exactly-once-execution
  - **Feature 284 — `S0tman/irp-capture`** — v2 owner-pains decision-rationale-ledger

## Mandatory LE31 skill list

The external coding agent **MUST** load these skills before implementing:

- `le31-conventions` — charter invariants and the seven-check feature gate
- `le31-v1-feature-pattern` — v1 feature contract shape, slicing rules, and DoD (also applies to v2 features that touch the v1 surface)
- `le31-handoff-spec` — frozen contract discipline and verification protocol
- `development` — generic coding pipeline (specify → plan → tasks → implement)
- `speckit-specify` — feature spec writer
- `speckit-plan` — implementation plan writer
- `speckit-tasks` — dependency-ordered task list writer

The external coding agent **MUST NOT**:

- Add `libp2p + IPFS` to the v1 stack without an explicit charter decision (v1 is single-Postgres; v2 is forward-looking).
- Update or delete any `CRDTEntry` or `SyncEvent` rows (append-only §3.3 invariant).
- Expose `CRDTEntry.content` publicly via IPFS without a privacy-preserving discipline (GDPR §3.7 boundary; content-hash-only or per-restaurant-encrypted).
- Use a Go sidecar for the v1 surface (v1 is Python; v2 PR would need to justify the language change).

## Frozen contract

The active feature file is the frozen contract. Do not silently change the slice, scope, or verification path. If new evidence requires a contract change, surface it to the user and patch the package before re-sending.

## Verification protocol

The external coding agent verifies:

1. Its read of the contract matches the recorded contract fields (`Goal`, `Evidence`, `Scope`, `Description`, `Data model`, `Implementation steps`, `Telegram interaction`, `Dependencies`, `Open questions`, `Why this matters`).
2. The slice does not require another skill, model, or migration outside the package.
3. The end-to-end acceptance path is executable in the configured environment.
4. The rollback or feature-removal path is present and reversible.

End-to-end acceptance path (when triggered):
- Two devices (tablet-bar-01 + kitchen-tg-bot-01) both write to `CRDTEntry` while disconnected
- The devices reconnect
- The CRDT-merge service sorts the entries by `(lamport_clock, replica_id)` deterministically
- Both devices converge to the same `CRDTEntry` set (verified by hash comparison)
- The `SyncEvent` table has 2 rows (one per direction)
- The `LogReplica` table updates `last_seen_lamport` and `last_sync_at` for both replicas

## Rollback path

- Delete the `CRDTEntry + LogReplica + SyncEvent` SQLModel tables (drop + alembic downgrade).
- Delete the `crdt_merge.py + ipfs_content_address.py + libp2p_sync.py` service files.
- The v1 `audit_logs + StockEntry` SQLModel tables are untouched (NEW tables, not a migration).
- No data is lost (the v2 `CRDTEntry` data is removed; the v1 `audit_logs + StockEntry` data is preserved).

## Sign-off gap

This is a defer artifact. The trigger condition is **the next time the LE31 owner opens a v2 owner-pains multi-device-append-only surface window** (estimated Q2 2027 based on the v2 roadmap; no current commitment).

The external coding agent must mirror back the frozen contract before implementing and stop if it cannot.

---

**LE31 charter alignment summary** (per `le31-conventions/SKILL.md`): §3.1 partial (lamport-clock + replica-id ✓; CRDT-merge OFF-§3.1 = explicit charter-decision needed for v2); §3.2 strictly-compatible (Apache-2.0 permissive + IPFS self-hosted); §3.3 ✓ (append-only `CRDTEntry + SyncEvent` + content-addressing by hash = stronger than §3.3 raw `audit_logs`); §3.4 strong alignment (operator-facing + peer-to-peer + non-AI-fallback + deterministic-merge); §3.7 partial (IPFS privacy boundary = explicit charter-decision needed).
