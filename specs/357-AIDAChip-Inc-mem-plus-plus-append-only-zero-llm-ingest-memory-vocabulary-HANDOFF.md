# HANDOFF — Feature 354: `AIDAChip-Inc-mem-plus-plus-append-only-zero-llm-ingest-memory-vocabulary`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/354-AIDAChip-Inc-mem-plus-plus-append-only-zero-llm-ingest-memory-vocabulary.md` — defer/parking-lot (Pick B of Daily Brainstorm 2026-10-21).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ | When a future LE31 v2-AI surface proposes "let the operator ask what happened last Tuesday", the owner wants *a retrieval shape whose write path never calls a model*, but struggles because *every agent-memory reference puts an LLM in the ingestion path — exactly the §3.4 shape the charter forbids in the business path*. |
| 2 | Viability | ✓ | "Dated records you can search without calling a model" is comprehensible without specialist help. **Apache-2.0 ✓ §3.2 STRICTLY-COMPATIBLE**, ★9/⑂2. **Traction caveat recorded plainly: ★9/⑂2 is minimal traction and is NOT evidence of adoption; it is recorded as a demand signal for the shape, not for the project.** |
| 3 | Practicability and confidence | ✓ | **Python ✓ ON-STACK + PostgreSQL ✓ ON-STACK** (LE31 v1 is Python 3.13 / SQLModel / Postgres) — this is the most stack-aligned pick of the pass apart from the two v1 phone/POS ones. pgvector and ONNX are NOT in the LE31 stack and would be additions. Evidence strength: medium-high for the vocabulary; **low for present urgency**. |
| 4 | Conflict | ✓ | Does not violate any invariant as a *retrieval* store. **⚠️ BLOCKER RECORDED: the §3.7 boundary is UNMADE — what counts as operational knowledge (supplier prices, prep times) versus guest data (who ordered what, payment instruments) inside a memory store is undefined.** Until that rule exists, no store can be created safely. **⚠️ SECOND CONFLICT RECORDED: this pick argues vector-first hybrid retrieval; feature 352 (`Idriz-hax/harbor-ledger-memory`, filed the same day by the research cron) argues keyword/file-based with the document set always surfaced. The two disagree and the disagreement is unresolved.** |
| 5 | Outcome + appetite + scope | ✓ | Maps to v2-AI defer outcome. Maximum time worth spending: 1 hour for documentation + HANDOFF. Today: 0 build time. |
| 6 | Cost to operational value | ✓ | The value is (a) naming the **zero-LLM-at-ingest** shape as the §3.4-compatible retrieval posture, and (b) **recording the vector-first vs keyword-first disagreement with feature 352** so the owner knows it is unresolved rather than rediscovering it later. No build. |
| 7 | Circuit breaker + reversibility | ✓ | No code today; no rollback needed. Documentation-only revert via `git rm`. |

**Gate verdict**: **`defer` (parking-lot)** — 7/7 gate checks pass. Build verdict `defer` because: (1) **LE31 has no AI surface at all** — there is nothing to attach memory to; (2) the §3.7 boundary rule is unmade and is a hard blocker; (3) the vector-first vs keyword-first question conflicts with a sibling pick filed the same day.

## Bucket

**v2-AI (append-only organisational-memory + hybrid/temporal retrieval + zero-LLM-at-ingestion + local-ONNX-embeddings vocabulary)** — Pick B of Daily Brainstorm 2026-10-21.

## Files to touch

**None today.** The defer artifact is documentation only, and no file should be created until BOTH blockers clear.

When (1) an owner decision exists on whether LE31 gets any AI surface, (2) the §3.7 boundary rule is written, and (3) the vector-first vs keyword-first conflict is resolved, the files to touch are expected to be:

- `backend/alembic/versions/` — migration adding an append-only `record` table (`id`, `recorded_at`, `content`, `superseded_by` nullable). **Append-only: no UPDATE path, enforced at the DB level**, matching the existing StockEntry discipline.
- `backend/alembic/versions/` — migration adding `temporal_idx` / keyword index. Embeddings, if kept at all, are a **rebuildable projection**, never the source of truth — so a bad embedding run is recoverable and the audit trail survives.
- `backend/services/record_service.py` — append-only write path. **Must require zero model inference** (§3.4).
- `backend/services/retrieval_service.py` — keyword-first retrieval. **If the owner chooses vector-primary instead, this decision must be re-reviewed against §3.7 before implementation, not after.**
- `tests/test_record_service.py` — **must include a test asserting no network/model call occurs on the write path.** That test is the point of the feature.

**Explicitly NOT to be created before the blockers clear:** any embedding model dependency, any pgvector extension migration, any LLM client in the write path.

## Verification protocol reference

See `/opt/data/le31_mmm3_research_work/skills/le31-v1-feature-pattern/SKILL.md` for the canonical verification protocol, and `PROJECT_CHARTER.md` §3.4 and §3.7 for the two invariants this feature is gated on.

## Rollback path

`git rm features/354-AIDAChip-Inc-mem-plus-plus-append-only-zero-llm-ingest-memory-vocabulary.md specs/357-AIDAChip-Inc-mem-plus-plus-append-only-zero-llm-ingest-memory-vocabulary-HANDOFF.md` — documentation-only single revert.

## Mandatory LE31 skill list

When the blockers clear and a v2-AI retrieval PR lands, the coding agent must load these skills before starting:

- `le31-conventions` — for the canonical §3.3 / §3.4 / §3.7 charter-invariant review. **§3.7 is the load-bearing one here.**
- `le31-v1-feature-pattern` — for the canonical v1 feature pattern and the append-only-StockEntry discipline this extends.
- `le31-backend` — for the canonical FastAPI + SQLModel + Postgres + Alembic + append-only-ledger pattern.
- `le31-handoff-spec` — for the canonical HANDOFF-spec format.
- `le31-coding-agent-brief` — for the canonical paste-in-prompt format.

**Read `features/352-Idriz-hax-harbor-ledger-memory-local-first-memory-vocabulary.md` alongside this one.** The two picks are direct cross-section siblings filed on the same day and they disagree about whether retrieval should be vector-first or keyword-first. Implementing either without reading the other is the specific failure mode this note exists to prevent.