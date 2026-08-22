# Feature 92 — ai-agent-decision-ledger-cluster-watch

> **NEW observation (2026-08-21).** Documents the **AI-agent decision
> ledger cluster** — 6+ in-window Python libraries, all converged on
> the same pattern in 30 days (2026-07-22 → 2026-08-21). Observed
> during the 2026-08-21 daily brainstorm (see
> `/opt/data/le31-brainstorm-2026-08-21.md`, Pick C).
> Bucket: **v2-AI control-plane (parking-lot, cluster research-note)**
> — hard defer pending cluster-maturity threshold.

## Goal

Record the **in-window Python AI-agent-decision-ledger cluster** —
6+ libraries, all building "AI agents need append-only decision
ledgers" primitives, all in 30 days. The cluster is empirically
real; the highest is ★3 (zero are at feature-ready scale). The
pick is filed as a **cluster research-note** (not a feature
contract) because the build implication is "watch the cluster",
not "import a library" or "build a new feature".

## Scope

**In scope:**
- Daily direct-repo GETs on the 6 cluster members (via
  `$HERMES_GITHUB_TOKEN`).
- Tracking star velocity + push activity + license + Python
  version + dependency footprint on each cluster member.
- Documenting the cluster convergence in the LE31 research notes.
- Cross-referencing the cluster against LE31 features 49, 61, 81, 83
  (the production-grade append-only ledger implementations).

**Out of scope (v1 / v2):**
- Importing any code from the cluster (the cluster is the
  research-note observation; LE31 already covers the architecture
  with features 49/61/81/83).
- Building a new append-only-decision-ledger feature for LE31 (the
  architecture is already shipping).
- Building any feature based on the cluster code surface.

## Description

### The 6 in-window Python cluster members

| Repo | Stars | Pushed | License | One-line |
|---|---|---|---|---|
| `daryl-labs-ai/daryl` | 3★ | 2026-08-21 | (not checked) | "The trust layer for AI agents — cryptographic proof of every decision" |
| `AetherAI3/PROTOCOL-C` | 2★ | 2026-08-19 | (not checked) | "Tamper-evident, forward-secret data commitments for Python — sign any decision with a one-shot key, audit it forever. Pure stdlib, zero deps" |
| `Lulzx/memo` | 1★ | 2026-07-27 | (not checked) | "Permanent memory for agents. One log file, one projection, 150 lines of Python" |
| `JosephOIbrahim/Hanish` | 1★ | 2026-08-19 | (not checked) | "A scoreboard for the future. Write predictions down, watch what happens, keep score forever — a domain-blind calibration substrate with append-only ledger" |
| `NeuruhAI/neuruh-lifecycle-state-ledger` | 1★ | 2026-08-20 | (not checked) | "Canonical append-only lifecycle state ledger binding forward transitions and rollback evidence" |
| `mrpandafr/Vector` | 0★ | 2026-07-24 | (not checked) | "A memory model in 7 lines. Time is a node. Every link knows its speaker. Nothing can be deleted. MIT" |

**Direct repo URLs** (in priority order):
- https://github.com/daryl-labs-ai/daryl (★3, highest)
- https://github.com/AetherAI3/PROTOCOL-C (★2)
- https://github.com/Lulzx/memo (★1)
- https://github.com/JosephOIbrahim/Hanish (★1)
- https://github.com/NeuruhAI/neuruh-lifecycle-state-ledger (★1)
- https://github.com/mrpandafr/Vector (★0)

### Why this is a fresh cross-section signal

The cluster is the **first time the brainstorm pass observed 6+
Python libraries in 30 days all converging on the exact same
pattern**. The category is **forming**:

1. **The "append-only ledger" + "AI agent" + "decision audit"** primitive
   is becoming a category. LE31's `StockEntry` ledger (feature 03) is
   the **production-grade reference implementation**.
2. **The 6 new libraries are "DIY" implementations** of the same
   primitive LE31 already ships. The cluster confirms LE31's architecture
   is converging with the Python ecosystem.
3. **The cluster is Python-native** — 5/6 are MIT-licensed Python
   libraries. The pip-installable "AI agent decision ledger" is
   becoming a commodity primitive in Python.

### Why parking-lot (not build)

(a) **No buildable feature surfaces** — the cluster is a research-
note, not a feature contract.
(b) **LE31 already covers the architecture** — features 49, 61, 81, 83
are the production implementation; the cluster is external validation.
(c) **No observed LE31-owner pain** — the append-only ledger is
shipping, not a question.
(d) **Charter §3.2 — no GPL/AGPL imports** — the cluster libs are MIT
(none checked yet, but README scan suggests MIT for at least some),
but the build implication is "watch the cluster", not "import a
library".
(e) **Cost-to-value**: the cluster tells us the **direction** of the
Python ecosystem, not the **next slice**.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 49 `postledger-tamper-evident-hash` | Audit-grade `prev_hash`/`row_hash` chain on `StockEntry` | Production implementation; cluster is external validation |
| 61 `holdfast-approval-ledger` | AI-proposes / human-publishes decision ledger | Production implementation; cluster is external validation |
| 81 `append-only-immutable-audit-check` | Chain verification primitive | Production implementation; cluster is external validation |
| 83 `lifecycle-citation-mixin` | Explicit `lifecycle_state` + `superseded_by_id` chain on `StockEntry` | Production implementation; cluster is external validation |

This pick is **NOT** a duplicate of any existing feature. It is a
**cluster research-note** that validates the architectural pattern
already shipped in features 49/61/81/83.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation, not a feature build.

## Implementation

1. Read the top-3 cluster members' READMEs in the next daily-research
   pass to confirm the architectural pattern:
   - `curl -sS https://raw.githubusercontent.com/daryl-labs-ai/daryl/main/README.md`
   - `curl -sS https://raw.githubusercontent.com/AetherAI3/PROTOCOL-C/main/README.md`
   - `curl -sS https://raw.githubusercontent.com/Lulzx/memo/main/README.md`
2. Continue daily direct-repo GETs on all 6 cluster members to
   track star velocity + push activity.
3. **No build implied.** The pick is a cluster-watch observation.
   The re-evaluation trigger is **cluster maturity** (≥5 libraries
   at ≥10★ each, currently 3 at ≥3★) — not a build decision.

## Telegram interaction

None. This is a passive observation; no cook or manager action.

## Dependencies

- `$HERMES_GITHUB_TOKEN` for the daily direct-repo GETs (already in
  `/opt/data/.env`).

## Open questions

- Do the cluster members overlap in their primitive surface (i.e., do
  they all expose the same `append(record) → row_hash` interface)?
- Do any of the cluster members mature to ≥10★ in the next 30 days?
  (Currently 3 at ≥3★; threshold is 5 at ≥10★.)
- Does the cluster's architectural pattern inform the **scoping** of
  feature 68 (cook-assistant-deterministic-gate)? Specifically, which
  deterministic-gate primitive is the right one to use?

## Why this matters

The cluster is the **first category-formation signal** of the 22-pass
series. Six libraries in 30 days, all building the same primitive,
is not noise — it's a pattern. The cluster validates LE31's existing
architectural posture (append-only ledger as the production-grade
implementation) and surfaces new questions about which cluster member
(if any) LE31 should consume when the v2-AI cook-assistant surface
(feature 68) is being scoped. The artifact is filed as a parking-lot
research-note with a clear re-evaluation trigger: cluster maturity
threshold (≥5 libraries at ≥10★ each).
