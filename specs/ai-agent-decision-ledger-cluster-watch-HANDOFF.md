# ai-agent-decision-ledger-cluster-watch — HANDOFF

> **Slice for the research agent.** This is a passive cluster
> research-note observation of 6+ in-window Python AI-agent-decision-
> ledger libraries. The slice boundary is hard: zero source-file
> edits, zero schema changes, zero new config keys. Read this *and*
> `features/92-ai-agent-decision-ledger-cluster-watch.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `92`
- Slug: `ai-agent-decision-ledger-cluster-watch`
- Contract file: `features/92-ai-agent-decision-ledger-cluster-watch.md`
- Bucket: **v2-AI control-plane (parking-lot, cluster research-note)**
  — hard defer pending cluster-maturity threshold
- Linear parent: **TBD** (Brainstorm 2026-08-21 — daily, created in
  this cron)
- Linear sub-issue: **TBD** (create as a draft parking-lot artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via direct repo GETs on 6+ Python
libraries, all building "AI agent decision ledger" primitives, all
in 30 days, 2026-07-22 → 2026-08-21).

**Confidence:** **high** for the cluster pattern (6+ libraries in 30
days = category formation); **low** for the build implication (LE31
already covers the architecture with features 49/61/81/83; the
cluster is external validation, not a new build).

**Decision: parking-lot; hard defer pending cluster-maturity
threshold.** The cluster README reads (top-3) are the next
research-side action. The re-evaluation trigger is **cluster
maturity** (≥5 libraries at ≥10★ each, currently 3 at ≥3★) — not a
build decision.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job on 2026-08-21).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/92-ai-agent-decision-ledger-cluster-watch.md   # NEW (this artifact)
specs/ai-agent-decision-ledger-cluster-watch-HANDOFF.md # NEW (this file)
INDEX.md                                                  # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back**
   `features/92-ai-agent-decision-ledger-cluster-watch.md` and
   confirm it matches the daily-brainstorm report's
   "ai-agent-decision-ledger-cluster-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline"
   table and confirm the date (2026-08-21), pick slug
   (`ai-agent-decision-ledger-cluster-watch`), feature path
   (`features/92-ai-agent-decision-ledger-cluster-watch.md`), and
   Linear sub-issue ID.
3. **On the next daily-research pass**:
   a. Read the top-3 cluster members' READMEs via `curl -sS`:
      - `https://raw.githubusercontent.com/daryl-labs-ai/daryl/main/README.md`
      - `https://raw.githubusercontent.com/AetherAI3/PROTOCOL-C/main/README.md`
      - `https://raw.githubusercontent.com/Lulzx/memo/main/README.md`
   b. Continue daily direct-repo GETs on all 6 cluster members to
      track star velocity + push activity.
   c. Compare cluster architectural patterns against LE31 features
      49/61/81/83 (the production-grade append-only ledger
      implementations).
4. **No build implied.** The pick is a cluster-watch observation.
   The re-evaluation trigger is **cluster maturity** (≥5 libraries
   at ≥10★ each, currently 3 at ≥3★) — not a build decision.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v2-AI` (the v2-AI
control-plane bucket) with label `Feature`.

- Title: `Feature 92 — ai-agent-decision-ledger-cluster-watch`.
- Body: the contract from
  `features/92-ai-agent-decision-ledger-cluster-watch.md` (or a short
  summary + the file path).
- Parent: **TBD** (Brainstorm 2026-08-21 — daily, the Linear index
  issue created in this cron).
- Status: `Backlog`.

## Rollback path

Delete `features/92-ai-agent-decision-ledger-cluster-watch.md` and this
HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other
code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

The cluster is the **first category-formation signal** of the 22-pass
series. Six libraries in 30 days, all building the same primitive,
is not noise — it's a pattern. The cluster validates LE31's existing
architectural posture (append-only ledger as the production-grade
implementation) and surfaces new questions about which cluster member
(if any) LE31 should consume when the v2-AI cook-assistant surface
(feature 68) is being scoped. The artifact is filed as a parking-lot
research-note with a clear re-evaluation trigger: cluster maturity
threshold (≥5 libraries at ≥10★ each).

## Carry-over history

This is the **NEW observation** (2026-08-21); no prior artifact
exists. Combines:

- The 6+ in-window Python AI-agent-decision-ledger libraries
  (`daryl-labs-ai/daryl`, `AetherAI3/PROTOCOL-C`, `Lulzx/memo`,
  `JosephOIbrahim/Hanish`, `NeuruhAI/neuruh-lifecycle-state-ledger`,
  `mrpandafr/Vector`).
- The 22-pass observation that LE31 features 49/61/81/83 already
  cover the architectural pattern the cluster is forming around.
- The v2-AI watch-list pattern (carry-over from features 84/85/86)
  that LE31's strategic posture is converging with the Python
  ecosystem.
