# 168 — edusouzaxGV asset-ledger content-addressed append-only manifest HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 audit-trail surface becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/168-edusouzaxgv-asset-ledger-content-addressed-append-only-manifest.md` (defer artifact; **no code today**).

Bucket: **v2 architecture-reference (content-addressed identification + append-only manifest + lineage queries + drift detection + pluggable storage backends; charter §3.1 territory; v2-hardening primitive)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 audit-trail surface is introduced (e.g. *show me every StockEntry change for menu item X in the last 30 days, with the bytes that changed*), the owner wants *a primitive that answers 'where did this value come from?' with content-hash-based deduplication + lineage walk + drift detection + storage-agnostic backend*, but struggles because *LE31 v1's `audit_logs` is text-only and has no content-hash discipline*, so that *the v2 surface can answer 'is this value still the same as yesterday?' without reading the entire database*." **PASS** (zero-pain today; v1 has no audit-trail surface; the JTBD is primitive documentation, not a build-need). |
| 2 | **Viability** | Owner can read the description (1-line)? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies (asset-ledger is MIT Python); no new permissions. Confidence medium for the primitive match (description names all five sub-primitives: `provenance-tracking backup`, `content-addressed identification`, `append-only manifest`, `lineage queries`, `drift detection`, `pluggable storage backends`); low for transferability (asset-ledger is for media backup, not restaurant ops). Practicability of adoption: medium-high — the content-hash + manifest + lineage-walk discipline is portable. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The asset-ledger *content-addressed + append-only manifest* primitive *is* a v2 question, not a v1 question; it does not violate §3.1 (append-only posture is preserved — the manifest IS append-only). No §3.4 conflict (no AI integration). **PASS** (charter §3.1 invariant-compatible for v1; the primitive IS the strongest form of §3.1). |
| 5 | **Outcome, appetite, scope** | v2 architecture-reference (content-addressed + append-only manifest + lineage queries + drift detection + pluggable storage vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-line description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (1 line is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/168-edusouzaxgv-asset-ledger-content-addressed-append-only-manifest-HANDOFF.md` and `features/168-edusouzaxgv-asset-ledger-content-addressed-append-only-manifest.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section vocabulary for the next v2-hardening question moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a content-hash-based deduplication or lineage-walk surface):

- `app/models/content_manifest.py` — possibly add a SQLModel class for the content manifest (depends on the v2 change).
- `app/models/audit_log.py` — possibly add a `content_hash` field (depends on the v2 change).
- `app/services/lineage_walk.py` — possibly add a service that walks the manifest for a given content hash (depends on the v2 change).
- `app/services/drift_detector.py` — possibly add a drift-detection service that recomputes hashes on read (depends on the v2 change).
- `app/storage/` — possibly add a pluggable storage backend abstraction (depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/168-edusouzaxgv-asset-ledger-content-addressed-append-only-manifest.md` exists and is read back by the parent.
- [ ] `specs/168-edusouzaxgv-asset-ledger-content-addressed-append-only-manifest-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The asset-ledger description is quoted verbatim (1-line, all five sub-primitives).
- [ ] The 0★/0⑂ + MIT + 1-day-old + Python + 101 KB stack-shape cluster is documented.
- [ ] The *content-addressed identification + append-only manifest + lineage queries + drift detection + pluggable storage backends* primitives are documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a content-hash-based deduplication or lineage-walk surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The asset-ledger JTBD-validation set is evaluated against the PR's changes: does the change support content-hash-based deduplication? Does it support lineage-walk queries? Does it support drift detection? Does it support pluggable storage backends?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 surface (if it lands):**
- Disable: revert the PR.
- Delete: revert the PR; remove the new `content_manifest` table; remove the new `content_hash` field from `audit_logs`; remove the new `lineage_walk` service; remove the new `drift_detector` service; remove the new pluggable storage abstraction.
- Migration cost: depends on the v2 change; the asset-ledger pattern's *content-addressed + append-only manifest* implies *additive architecture* (the new layer is additive on top of the existing v1 surfaces — append-only `audit_logs` + StockEntry ledger).
- Retained data: the `audit_logs` table retains all rows (charter §3.1); the verification log is a *new* document, not a schema change.

## 6. Mandatory LE31 skill list for the external agent

The external coding agent must load:

1. `le31-conventions` — for the seven-check feature gate and the hard invariants.
2. `le31-v1-feature-pattern` — for the canonical v1 contract shape (not applicable today; the defer artifact is documentation only).
3. `le31-handoff-spec` — for the handoff discipline (the contract is frozen; do not silently change the slice).
4. `le31-conventions-coder` (in `coding-agent/skills/`) — for the LE31-specific coding conventions.
5. `le31-arch-patterns` (in `coding-agent/skills/`) — for the LE31 architectural patterns.
6. `le31-data-correctness` (in `coding-agent/skills/`) — for the LE31 data-correctness rules.
7. `le31-quality-gates` (in `coding-agent/skills/`) — for the LE31 quality gates.

The external agent must **mirror back the frozen contract** before implementing (per `le31-handoff-spec/SKILL.md` §Frozen Contract Discipline) and stop if it cannot.

## 7. Handoff summary

| Field | Value |
|---|---|
| Feature ID | 168 |
| Slug | `edusouzaxgv-asset-ledger-content-addressed-append-only-manifest` |
| Bucket | v2 architecture-reference (content-addressed identification + append-only manifest + lineage queries + drift detection + pluggable storage) |
| Decision | defer |
| Build time today | 0 hours |
| Files to touch today | 0 |
| Files to touch on trigger | `app/models/content_manifest.py` (possibly) + `app/models/audit_log.py` (possibly `content_hash` field) + `app/services/lineage_walk.py` (possibly) + `app/services/drift_detector.py` (possibly) + `app/storage/` (possibly pluggable abstraction) |
| Trigger condition | First v2 PR that adds a content-hash-based deduplication or lineage-walk surface (typically a v2 owner-facing audit-trail surface, a v2-AI surface that consults `audit_logs`, or a v2 surface that introduces a second stakeholder who needs independent verification) |
| Verification protocol | Does the change support content-hash-based deduplication? Does it support lineage-walk queries? Does it support drift detection? Does it support pluggable storage backends? |
| Rollback | Fully reversible (defer artifact is documentation only) |
| Parent research issue | HMM-237 (Research 2026-09-13 — daily) |
| Linear sub-issue | (to be created) |
| Lead source | GitHub `edusouzaxGV/asset-ledger` (MIT, 0★, Python, pushed 2026-09-12, created 2026-09-12, 101 KB) |

## 8. Sign-off gap

**No sign-off gap today** (the defer artifact is documentation only).

**Future v2 trigger sign-off gap** (when the first v2 PR that adds a content-hash-based deduplication or lineage-walk surface lands): the external agent must mirror back the frozen contract (per §6 above) and the operator must confirm the *content-addressed identification + append-only manifest + lineage queries + drift detection + pluggable storage backends* JTBD validation is the right architectural checklist (an owner decision).
