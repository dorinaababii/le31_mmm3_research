# Feature 96 — neuruhai-cluster-watch

> **Day-2 update (2026-08-22).** Documents the **in-window NeuruhAI 5-pack** — 5 Apache-2.0 Python append-only ledger libraries, all pushed 2026-08-20, all created Aug 9–12. The 5-pack **doubles the AI-agent-decision-ledger cluster** (first filed as **feature 92** on 2026-08-21, 6 libraries) from 6 → 11 in 24 hours. Observed during the 2026-08-22 daily brainstorm (see `/opt/data/le31-brainstorm-2026-08-22.md`, Pick A). Bucket: **v2-AI control-plane (parking-lot, cluster research-note)** — hard defer pending cluster-maturity threshold.

## Goal

Record the **in-window NeuruhAI 5-pack** as the **day-2 update** to feature 92's AI-agent-decision-ledger cluster. The 5-pack is empirically real: 5 new libraries from one org, all Python, all Apache-2.0, all explicitly append-only-ledger-shaped, all pushed within 24 hours of each other. Cluster expansion is the freshest **CATEGORY-formation signal** of the 22-pass series — the pattern LE31 already ships (features 03, 49, 61, 81, 83) is being independently re-implemented by the Python ecosystem at a fast clip.

## Scope

**In scope:**
- Direct-repo GETs on the 5 NeuruhAI cluster members + the 1 already-counted lifecycle repo (via `$HERMES_GITHUB_TOKEN`):
  - `NeuruhAI/neuruh-lifecycle-state-ledger` (★1, pushed 2026-08-20, already in feature 92 cluster)
  - `NeuruhAI/neuruh-canonical-state-revision-ledger` (★0, pushed 2026-08-20)
  - `NeuruhAI/neuruh-authorization-consumption-ledger` (★0, pushed 2026-08-20)
  - `NeuruhAI/neuruh-canary-evaluation-ledger` (★0, pushed 2026-08-20)
  - `NeuruhAI/neuruh-evidence-ledger` (★0, pushed 2026-08-20)
- Tracking star velocity + push activity + license + Python version + dependency footprint on each NeuruhAI repo.
- Documenting the cluster convergence in the LE31 research notes (this artifact is the document).
- Cross-referencing the cluster against LE31 features 49, 61, 81, 83 (the production-grade append-only ledger implementations) + feature 92 (day-1 cluster observation).

**Out of scope (v1 / v2):**
- Importing any code from the NeuruhAI repos (the cluster is the research-note observation; LE31 already covers the architecture with features 49/61/81/83).
- Building a new append-only-decision-ledger feature for LE31 (the architecture is already shipping).
- Building any feature based on the cluster code surface.
- Charter §3.2 license check: all 5 repos are Apache-2.0 (verified via raw GitHub API responses), so import would be technically allowed — but no build implied today.

## Description

The NeuruhAI 5-pack is the **second cluster-expansion event** observed in the 22-pass daily-brainstorm series. The day-1 cluster (feature 92) was 6 libraries; today the cluster is **11 libraries** (6 original + 5 NeuruhAI new). The doubling is empirical evidence that the Python ecosystem is converging on the "AI agent decision ledger" pattern.

### Per-repo description table (verbatim from GitHub API responses)

| Repo | ★ | Description |
| --- | --- | --- |
| `NeuruhAI/neuruh-lifecycle-state-ledger` | ★1 | "Canonical append-only lifecycle state ledger binding forward transitions and rollback evidence." (already in feature 92 cluster) |
| `NeuruhAI/neuruh-canonical-state-revision-ledger` | ★0 | "Append-only, hash-chained memory of canonical-state revisions anchored to one lifecycle tip. Memory, not power." |
| `NeuruhAI/neuruh-authorization-consumption-ledger` | ★0 | "Append-only tamper-evident ledger that retires single-use deployment authorizations exactly once." |
| `NeuruhAI/neuruh-canary-evaluation-ledger` | ★0 | "Tamper-evident canary evaluation ledger with deterministic PASS/HOLD/ROLLBACK evidence." |
| `NeuruhAI/neuruh-evidence-ledger` | ★0 | "Append-only tamper-evident evidence provenance ledger for governed agent systems." |

### Cluster size trajectory (LE31 daily-brainstorm tracked)

| Date | Cluster size | Trigger |
| --- | --- | --- |
| 2026-08-21 (day-1, feature 92) | 6 libraries | daryl + PROTOCOL-C + memo + Hanish + neuruh-lifecycle + Vector |
| 2026-08-22 (day-2, this feature) | **11 libraries** (+5 in 24h) | NeuruhAI 5-pack added: canonical-state-revision + authorization-consumption + canary-evaluation + evidence-ledger (4 new) + neuruh-lifecycle-state was already counted |

### Why this matters for LE31

LE31's existing features **03** (StockEntry ledger), **49** (postledger tamper-evident hash), **61** (holdfast approval ledger), **81** (append-only immutable audit check), **83** (lifecycle citation mixin) are the **production-grade reference implementations** of the "append-only decision ledger" pattern. The cluster's doubling in 24h is empirical confirmation that:

1. The architectural pattern is forming a category in the Python ecosystem (not a niche design).
2. LE31's append-only-ledger posture is the **mature end** of a 30-day-old pattern that 11 libraries are still trying to match.
3. The cluster informs the **scoping** of feature 68 (cook-assistant-deterministic-gate) — if LE31 ever builds the v2-AI control plane, the cluster provides an off-the-shelf primitive to consume, not to build from scratch.

## Data model

No new LE31 data model. This artifact is a research-note observation, not a feature contract. The cluster does not introduce a new table or schema.

## Implementation steps

1. **No code change**. This is a research-note artifact.
2. Future-pass tracking: add the 5 NeuruhAI repos to the daily-research watch list (carry-over from 2026-08-22 brainstorm).
4. Re-evaluation: in 30 days (2026-09-22), check whether any NeuruhAI repo has crossed ≥10★ OR whether the cluster has grown to ≥15 libraries.

## Telegram interaction if any

None. This is a research-note observation; no Telegram interaction is needed.

## Dependencies

- **`$HERMES_GITHUB_TOKEN`** for daily direct-repo GETs on the 5 NeuruhAI repos.
- **GitHub `topic:append-only` search** (filtered by `pushed:2026-07-22..<date>`) for cluster discovery.
- **Cross-reference**: feature 92 (day-1 cluster observation, 6 libraries).

## Open questions

1. **Are the 5 NeuruhAI repos part of a single org-level release (e.g., a NeuruhAI "launch" of a series) or organic day-by-day authoring?** — answer this on next pass by reading the commit history + author info on each repo.
2. **Is the cluster growing because the pattern is genuinely useful, or because LLMs are recommending "build an append-only decision ledger" as boilerplate?** — distinguish by tracking star velocity (organic growth vs AI-generated-repo noise).
3. **Is there a Python ecosystem-shift trigger** (e.g., a popular LLM framework recommending decision ledgers as a best practice)? — answer by reading `references` + `topics` on the cluster members.

## Why this matters

The cluster **doubled in 24 hours** — that's a fast signal. LE31 already ships the architecture; the cluster is **external validation**, not a new build pick. The next-pass discipline is: **watch the cluster, do not build a new feature**. If the cluster exceeds 5 libraries at ≥10★ each (currently 0 at ≥10★), escalate to a `build` decision; until then, this is a parking-lot research-note.

## Distinct from existing features

- **Feature 03** (StockEntry ledger) — LE31's per-batch production append-only ledger. Distinct: feature 03 is the production implementation; this artifact is the research-note on the external cluster.
- **Feature 49** (postledger tamper-evident hash) — LE31's tamper-evident hash chain. Distinct: feature 49 is the production hash chain; this artifact observes external libraries that re-implement the same pattern.
- **Feature 61** (holdfast approval ledger) — LE31's approval-gated append-only ledger. Distinct: feature 61 is LE31's approval workflow; the cluster's `NeuruhAI/neuruh-authorization-consumption-ledger` is a related but different primitive.
- **Feature 81** (append-only immutable audit check) — LE31's audit verification. Distinct: feature 81 verifies LE31's own ledger; this artifact observes external libraries.
- **Feature 83** (lifecycle citation mixin) — LE31's lifecycle-aware citation. Distinct: feature 83 is LE31's citation primitive; `NeuruhAI/neuruh-lifecycle-state-ledger` is an external library re-implementing lifecycle binding.
- **Feature 92** (ai-agent-decision-ledger-cluster-watch) — **day-1 cluster observation, 6 libraries**. This feature (96) is the **day-2 update**, 11 libraries, specifically tracking the 5 NeuruhAI repos added in the last 24h. Distinct from feature 92 in that this feature is the update, not the original observation.

## Sources

- **GitHub `topic:append-only`** (search verified at 2026-08-22 06:44 UTC; PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
- Raw response: `/tmp/le31-brainstorm-2026-08-22/gh_topic_append-only.json` (174,888 bytes, 30 items returned).
- 5 NeuruhAI repos verified via raw GitHub API responses (item ids 1296148728 + 4 others — see raw JSON for full IDs).
- Full report: `/opt/data/le31-brainstorm-2026-08-22.md` (Pick A section, lines 71–93).
- Parent Linear issue: HMM-125 (Brainstorm 2026-08-22 — daily).
- This Linear sub-issue: HMM-126.