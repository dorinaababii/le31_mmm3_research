# HANDOFF — Feature 175: `nhobin219-litelink-append-only-iceberg-embedded-local-first`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/175-nhobin219-litelink-append-only-iceberg-embedded-local-first.md` — defer/parking-lot (Pick C of Brainstorm 2026-09-14, parent research issue HMM-249).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | litelink `SQLite buffer → local Iceberg table → remote Iceberg table` is the §3.1 explicit-state-transitions primitive applied to data egress; every write is durable before acknowledgement; no write is lost on `SIGKILL`; no write is in-memory-only |
| 2 | Charter §3.2 (permissive license) | ✓ | Apache-2.0 |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | litelink is a deterministic append-only library; no AI integration in the description or topics |
| 4 | In-window by `pushed_at` | ✓ | pushed 2026-09-03T06:23:07Z (within 30-day window 2026-08-15..2026-09-14) |
| 5 | Ripgrep-verified unique vs features/ 1..172 | ✓ | no existing feature covers the *"SQLite → local Iceberg → remote Iceberg + no read on the hot path touches the network"* three-tier capture primitive |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 30/49/81/134/154/168/169 |
| 7 | Defer verdict (parking-lot, no code change) | ✓ | 3★ + 32-day-old repo + single in-window push + single-maintainer + no restaurant-specific code → no code adoption; the *durable-append-only-capture* primitive + the *explicit anti-pattern warning* are the values |

**Gate verdict**: **defer (parking-lot)** — 7/7 gate checks pass, but the build verdict is `defer` because LE31 v1 has no audit-log export surface (v1 is single-restaurant, the owner trusts the system). The *v2-architecture vocabulary* + the *explicit anti-pattern reference* are the brainstorm values, not the code.

## Bucket

**v2** (durable-append-only-capture + audit-log export) — the *v2-architecture vocabulary* is the value, not the code. LE31 v1 is single-restaurant, the owner trusts the system, and there is no accountant-share surface; the litelink pattern is the v2-architecture reference for any future v2 surface that asks *"how do we let the owner share the `audit_logs` chain with an external party without losing durability guarantees?"*

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that adds audit-log export to an external party — accountant, tax authority, multi-restaurant federation), the implementation would introduce:
- An `audit_export_buffer` table (`app/models/audit_export.py`): id, audit_log_id, sealed_at, status: unsealed|sealed|synced.
- An `audit_export_seal` background job (`app/jobs/audit_export_seal.py`): APScheduler job that seals the buffer at `target_seal_size` into the local Iceberg table.
- An `audit_export_sync` background job (`app/jobs/audit_export_sync.py`): APScheduler job that uploads the local Iceberg table to the remote Iceberg table on S3 (or any object store).
- An `audit_export_catalog` SQLite sidecar (`app/storage/audit_export_catalog.sqlite`): tracks the catalog state for the local + remote Iceberg tables.
- An `app/audit_export/` package: Iceberg writer (PyIceberg), S3 client (boto3), catalog manager.

This is **NOT a v1 surface** — LE31 v1 is single-restaurant, the owner trusts the system, and there is no accountant-share surface. The HANDOFF is to evaluate whether the v2 audit-log export surface is the right product-wedge for the next v2 PR.

## Verification protocol

1. `git clone https://github.com/nhobin219/litelink` (NOT to be done today — defer).
2. `curl -sS https://raw.githubusercontent.com/nhobin219/litelink/main/README.md` (parent-verified 2026-09-14; the README is the source of truth for the verbatim three-tier capture primitive + the explicit anti-pattern warning).
3. `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN" "https://api.github.com/repos/nhobin219/litelink"` for star count, fork count, license, language, pushed_at, created_at, topics (parent-verified 2026-09-14).
4. `git diff --stat` (post-trigger-fires, NOT today) to verify the audit-export changes are isolated to `app/models/audit_export.py`, `app/jobs/audit_export_seal.py`, `app/jobs/audit_export_sync.py`, `app/storage/audit_export_catalog.sqlite`, `app/audit_export/`.
5. `pytest app/audit_export/ -v` (post-trigger-fires, NOT today) to verify the three-tier capture (SQLite buffer → local Iceberg → remote Iceberg) passes the durability test suite — every write is durable before acknowledgement, no write is lost on `SIGKILL`, no read on the hot path touches the network.

## Rollback path

**None today** — no code change today, no rollback needed.

If the future v2 trigger fires and the implementation lands:
- Rollback = `alembic downgrade -1` to drop the `audit_export_buffer` table; the `audit_export_seal` + `audit_export_sync` background jobs are disabled in `app/jobs/scheduler.py`; the `audit_export_catalog.sqlite` sidecar file is removed. The existing `audit_logs` table is unchanged.

## Mandatory LE31 skill list

When (and only when) the future v2 trigger fires, the coding agent MUST load these skills before starting:

- `development` (router for all coding work)
- `le31-v1-feature-pattern` (existing LE31 v1 feature implementation pattern — applies as the LE31 v2 surface extends the v1 schema)
- `le31-handoff-spec` (HANDOFF contract reader/writer)
- `le31-coding-agent-brief` (paste-in prompt from slice contract)
- `speckit-implement` (verify tasks in order)

## Bucket project

**`le31 Research`** (parent research issue HMM-249) — the sub-issue for this feature lives in `le31 Research` (where the parent research issue lives), NOT in `le31 v1 — Core MVP`. Reason: the project `le31 v2 owner-pains` (which the original SKILL.md expected) **does not exist** in this workspace; the verified workspace contains only `le31 v1 — Core MVP`, `le31 Workflow`, and `le31 Research`. Per the verified-2026-08-28 skill note: *"For a v2-bucket pick, attach the sub-issue to `le31 Research` (where the parent research issue lives) and say so in the report."*

## Why this is a `defer`

The litelink repo is 3★, 32-day-old, with single in-window push. The single-maintainer cadence + the no-restaurant-specific-code make code adoption impractical. The *value* is the v2-architecture vocabulary + the *explicit anti-pattern reference*: the three-tier capture primitive (SQLite buffer → local Iceberg table → remote Iceberg table) is the named architectural reference for any future v2 surface that asks *"how do we let the owner share the `audit_logs` chain with an external party without losing durability guarantees?"*, and the key sentence *"no read on the hot path touches the network"* is the LE31 phone-first operator posture applied to data egress. The README motivation paragraph *"125,884 objects, 62.5% under 16 KiB, Parquet files at 2 rows each, compaction routine nothing ever scheduled, in-memory buffer a SIGKILL emptied"* is the **explicit anti-pattern reference** for any future v2 audit-log export surface — LE31 v2 audit-log export MUST NOT replicate any of these four failure modes. No build time today; the value is the v2-architecture vocabulary + the named anti-pattern warning for the future v2 audit-export surface.
