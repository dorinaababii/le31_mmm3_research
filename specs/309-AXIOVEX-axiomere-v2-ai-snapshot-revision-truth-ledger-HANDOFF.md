# 309-AXIOVEX-axiomere — HANDOFF

> **Slice for the coding agent.** Read this *and* `features/309-AXIOVEX-axiomere-mit-truth-ledger-append-only-signed-hash-chained-record-store-rust-revised-by-snapshots-never-modified-in-place-content-addressed-sha256-new-entry-points-to-predecessor-v2-ai-snapshot-revision-truth-ledger-vocabulary.md` before touching any code. Do not paste chat excerpts back into the build.
>
> **Defer artifact (no code today).** This is a parking-lot vocabulary reference. There is no build candidate. The HANDOFF documents what the trigger condition would be and what the slice would look like if the trigger fires.

## Frozen identifiers (do not rename)

- Feature ID: `309`
- Slug: `AXIOVEX-axiomere-v2-ai-snapshot-revision-truth-ledger`
- Contract file: `features/309-AXIOVEX-axiomere-mit-truth-ledger-append-only-signed-hash-chained-record-store-rust-revised-by-snapshots-never-modified-in-place-content-addressed-sha256-new-entry-points-to-predecessor-v2-ai-snapshot-revision-truth-ledger-vocabulary.md`
- Bucket: **v2-AI (snapshot-revision-truth-ledger-vocabulary)** — build verdict `defer`
- Linear parent (intake only — Linear is currently BLOCKED): **intended** `Research 2026-10-12 — daily` (parent fallback at `/opt/data/le31-daily-research-2026-10-12.linear-fallback.json`)
- Linear sub-issue (intake only): **intended** `Research 2026-10-12 / Pick B — v2-AI snapshot-revision-truth-ledger-vocabulary (AXIOVEX/axiomere)` with label `Feature`, project `le31 Research` (per `le31-feature-pipeline/SKILL.md` line 33 — `le31 v2-AI` does NOT exist; use `le31 Research` for v2-AI bucket picks); state `Triage`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed** (verified in-window by parent re-parse of `gsearch5.json` raw JSON; the description names the 14-primitive set explicitly: `append-only + signed + hash-chained + record-store + revised-by-snapshots + never-modified-in-place + content-addressed-by-SHA-256 + new-entry-points-to-predecessor + truth-ledger + audit-trail + ed25519 + merkle-tree + provenance + Rust`).

**Confidence:** **medium** for the vocabulary match (the verbatim description names the 14-primitive set); **low** for transferability (LE31 v1 has no v2-AI surface; the 23 KB tiny repo is the smallest v2-AI pick of the 74-pass series; the Rust core requires PyO3 wrapper for Python integration; the 0★/0⑂ is a low community-traction signal).

**Decision: defer (parking-lot, vocabulary reference).** Sister-shape to features 187+188+232+287-289+299-304 (the persistent v2-AI audit-trail vocabulary cluster) but with the unique *revised-by-snapshots + content-addressed-by-SHA-256 + new-entry-points-to-predecessor* framing. No build today; the *snapshot-revision-truth-ledger-vocabulary* is a persistent cross-section reference for any future v2-AI surface that requires audit-trail-revision semantics.

## Trigger condition (when to un-defer)

This slice un-defers if AND ONLY IF all of the following are true:

1. The first v2 PR that introduces a v2-AI surface that requires **truth-ledger-with-snapshot-revision semantics** lands (e.g., a v2 surface that introduces an AI-assisted owner-side workflow where the AI assistant proposes a revision to a daily-recap; the original version is preserved as a snapshot; the revised version creates a new entry pointing to the original via the SHA-256 content hash).
2. The proposed surface requires *content-addressed-by-SHA-256* (every record identified by its content hash, not by an external ID).
3. The proposed surface requires *new-entry-points-to-predecessor* (every revision creates a new entry that points to its predecessor via the content hash).
4. Charter §3.1 *explicit-state-transition* invariant can be maintained (every snapshot revision is an explicit operator-confirmed action, not an autonomous agent action).

If the trigger condition is met, follow the slice plan below.

## Slice plan (if trigger fires)

### Files to touch

1. **New** `app/db/migrations/2026_XX_XX_add_signature_to_audit_logs.py` (Alembic migration): add the `signature` column to `audit_logs`.
2. **New** `app/db/migrations/2026_XX_XX_add_predecessor_hash_to_audit_logs.py` (Alembic migration): add the `predecessor_hash` column to `audit_logs`.
3. **New** `app/db/migrations/2026_XX_XX_add_snapshot_revision.py` (Alembic migration): add the `SnapshotRevision` table.
4. **New** `app/db/migrations/2026_XX_XX_add_content_addressed_storage.py` (Alembic migration): add the `content_addressed_storage` table.
5. **New** `app/api/snapshot_revisions.py`: implement `GET /v2/snapshot-revisions/{entity_type}/{entity_id}` + `POST /v2/snapshot-revisions/{entity_type}/{entity_id}/revise`.
6. **New** `app/api/content_addressed.py`: implement `GET /v2/content-addressed/{content_hash}`.
7. **New** `app/bot/handlers/snapshot_revision.py`: implement the `snapshot_revision_request` Telegram handler.
8. **Update** `app/db/__init__.py`: register the new SQLModel classes.
9. **Update** `app/main.py`: include the new routers.

### Schema additions (Alembic migrations)

1. `audit_logs.signature` column: `str` (SHA-256 content hash + ed25519 signature of the audit-log payload). Nullable for legacy rows.
2. `audit_logs.predecessor_hash` column: `str` (SHA-256 content hash of the predecessor record). Nullable for genesis records. Index on `predecessor_hash` for efficient linked-list traversal.
3. `SnapshotRevision` table: `id` (UUID PK), `predecessor_id` (UUID FK to `audit_logs` nullable for genesis), `content_hash` (str SHA-256 unique), `signature` (str ed25519), `revised_at` (DateTime TZ), `revised_by` (str), `revision_reason` (str). Index on `(predecessor_id, revised_at)`.
4. `content_addressed_storage` table: `id` (UUID PK), `content_hash` (str SHA-256 unique), `content_type` (str), `content_payload` (JSON), `created_at` (DateTime TZ), `created_by` (str). Unique index on `content_hash`.

### Verification protocol

Per `le31-daily-research/SKILL.md` + `le31-conventions/SKILL.md` + `le31-v1-feature-pattern/SKILL.md`:

1. Run `pytest app/tests/test_snapshot_revision.py` (new test file). Confirm 100% pass.
2. Run `pytest app/tests/test_content_addressed.py` (new test file). Confirm 100% pass.
3. Manually exercise the end-to-end acceptance path: log in as owner → open the v2 surface → propose a snapshot revision → confirm via Telegram → verify the new `SnapshotRevision` record is created with `predecessor_id` + `content_hash` + `signature` populated.
4. Inspect the `SnapshotRevision` table to confirm the linked-list-of-content-addressed-records is correctly formed.
5. Inspect the `content_addressed_storage` table to confirm the SHA-256 content hash is unique per content.
6. Confirm charter §3.1 invariant is maintained: every snapshot revision is an explicit operator-confirmed action, not an autonomous agent action.

### Rollback path

1. Revert the Alembic migrations: `alembic downgrade -1` (4x).
2. Delete the new files: `app/api/snapshot_revisions.py` + `app/api/content_addressed.py` + `app/bot/handlers/snapshot_revision.py`.
3. Revert the `app/main.py` + `app/db/__init__.py` updates.
4. Verify: `pytest` passes with no test errors.
5. The snapshot-revision is vocabulary-only; the rollback is safe (no data loss beyond the dropped tables).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job on 2026-10-12).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after it ships).
6. `le31-research` (so the agent understands the research methodology that produced this pick).
7. `le31-coding-agent-brief` (so the agent uses the standard brief shape).

## Handoff summary

This is a **defer / parking-lot / vocabulary reference**. No build today. The slice un-defers only when the trigger condition is met. Until then, the artifact is documentation only.

**Sign-off gap:** none. The defer artifact is complete. The trigger condition is explicit. The slice plan is explicit. The verification protocol is explicit. The rollback path is explicit.

---

## Sign-off

- [x] Feature gate verdict is recorded (defer).
- [x] Feature contract (`features/309-...md`) is linked.
- [x] Mandatory LE31 skill list is named.
- [x] Trigger condition is explicit.
- [x] Verification protocol and rollback path are present (for the un-defer scenario).
- [x] Status matches the Linear fallback JSON.
