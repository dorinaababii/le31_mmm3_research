# neuruhai-cluster-watch — HANDOFF

> **Slice for the research agent.** This is a passive cluster research-note observation of the **in-window NeuruhAI 5-pack** — 5 Apache-2.0 Python append-only ledger libraries, all pushed 2026-08-20, all created Aug 9–12. The slice boundary is hard: zero source-file edits, zero schema changes, zero new config keys. Read this *and* `features/96-neuruhai-cluster-watch.md` before touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `96`
- Slug: `neuruhai-cluster-watch`
- Contract file: `features/96-neuruhai-cluster-watch.md`
- Bucket: **v2-AI control-plane (parking-lot, cluster research-note)** — hard defer pending cluster-maturity threshold
- Linear parent: **HMM-125** (Brainstorm 2026-08-22 — daily, created in this cron)
- Linear sub-issue: **HMM-126** (Feature label, project `le31 v1 — Core MVP` per le31-feature-pipeline SKILL.md nonexistent-`le31 v2-AI` correction)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed** (verified in-window via GitHub `topic:append-only` search at 2026-08-22 06:44 UTC with PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`; 5 NeuruhAI repos identified).

**Confidence:** **high** for the cluster pattern (5 new libraries in 24h, all Apache-2.0 Python, all explicitly append-only-ledger-shaped); **low** for the build implication (LE31 already covers the architecture with features 03/49/61/81/83; the cluster is external validation, not a new build).

**Decision: parking-lot; hard defer pending cluster-maturity threshold.** The 5-pack is the **day-2 update** to feature 92's day-1 cluster observation. The cluster grew from 6 → 11 in 24h. The re-evaluation trigger is **cluster maturity** (≥5 libraries at ≥10★ each, currently 0 at ≥10★) — not a build decision.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-22).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/96-neuruhai-cluster-watch.md           # NEW (this artifact)
specs/neuruhai-cluster-watch-HANDOFF.md         # NEW (this file)
INDEX.md                                         # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back** `features/96-neuruhai-cluster-watch.md` and confirm it matches the daily-brainstorm report's "neuruhai-cluster-watch" pick description (Pick A section).
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-22), pick slug (`neuruhai-cluster-watch`), feature path (`features/96-neuruhai-cluster-watch.md`), and Linear sub-issue ID (HMM-126).
3. **On the next daily-research pass**:
   a. Direct-repo GETs on all 5 NeuruhAI repos via `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN"`:
      - `https://api.github.com/repos/NeuruhAI/neuruh-lifecycle-state-ledger`
      - `https://api.github.com/repos/NeuruhAI/neuruh-canonical-state-revision-ledger`
      - `https://api.github.com/repos/NeuruhAI/neuruh-authorization-consumption-ledger`
      - `https://api.github.com/repos/NeuruhAI/neuruh-canary-evaluation-ledger`
      - `https://api.github.com/repos/NeuruhAI/neuruh-evidence-ledger`
   b. Track star velocity + push activity + license + Python version + dependency footprint on each repo.
   c. Continue tracking feature 92's day-1 cluster members (daryl, PROTOCOL-C, memo, Hanish, Vector) for the rolling 6+ → 11 → ? trajectory.
4. **No build implied.** The pick is a cluster-watch observation. The re-evaluation trigger is **cluster maturity** (≥5 libraries at ≥10★ each, currently 0 at ≥10★) — not a build decision.

## Linear sub-issue

Create a Linear sub-issue in project **`le31 v1 — Core MVP`** (per le31-feature-pipeline SKILL.md nonexistent-`le31 v2-AI` correction — the canonical v2-AI control-plane bucket does not exist) with label `Feature`.

- Title: `Feature 96 — neuruhai-cluster-watch`.
- Body: the contract from `features/96-neuruhai-cluster-watch.md` (or a short summary + the file path).
- Parent: **HMM-125** (Brainstorm 2026-08-22 — daily).
- Status: `Backlog`.

## Rollback path

Delete `features/96-neuruhai-cluster-watch.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

The 5-pack **doubled the cluster from 6 → 11 in 24 hours** — that's a category-formation signal that's hard to ignore. LE31 already covers the architecture with features 03/49/61/81/83 (production implementations) and feature 92 (day-1 cluster observation). This artifact (96) is the day-2 update that records the 5-pack specifically. The cluster informs the **scoping of feature 68** (cook-assistant-deterministic-gate) — if LE31 ever builds the v2-AI control plane, the cluster provides an off-the-shelf primitive to consume, not to build from scratch. Filed as a parking-lot research-note with a clear re-evaluation trigger: cluster maturity threshold (≥5 libraries at ≥10★ each).

## Carry-over history

This is the **day-2 observation** (2026-08-22); supersedes feature 92's day-1 cluster list (2026-08-21). Combines:

- The 5 new NeuruhAI repos (canonical-state-revision + authorization-consumption + canary-evaluation + evidence-ledger + the already-counted lifecycle-state).
- The day-1 cluster (feature 92: daryl, PROTOCOL-C, memo, Hanish, Vector) — still tracked.
- The 22-pass observation that LE31 features 03/49/61/81/83 are the production-grade reference implementations.
- The v2-AI control-plane pattern (carry-over from features 49, 61, 68, 81, 83, 92).

## Sources

- **GitHub `topic:append-only`** (search verified at 2026-08-22 06:44 UTC; PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
- Raw response: `/tmp/le31-brainstorm-2026-08-22/gh_topic_append-only.json` (174,888 bytes).
- Full report: `/opt/data/le31-brainstorm-2026-08-22.md` (Pick A section, lines 71–93).
- Linear parent: HMM-125 (Brainstorm 2026-08-22 — daily, status Done).
- Linear sub-issue: HMM-126 (Feature label, status Backlog, parent HMM-125).