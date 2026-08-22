# Feature 97 — stratum-watch

> **NEW observation (2026-08-22).** Documents the **in-window `mazze93/stratum` repo** — the **first in-window cluster-style repo with a human "control room" UI on top of an append-only event log**. Every other in-window append-only library (including the NeuruhAI 5-pack, daryl, PROTOCOL-C, memo, Hanish, etc.) is a pure ledger primitive (events + hashes, no UI). Stratum is the **first to surface a UI / control-room layer** on top of an append-only event log. Observed during the 2026-08-22 daily brainstorm (see `/opt/data/le31-brainstorm-2026-08-22.md`, Pick B). Bucket: **v2-AI control-plane (parking-lot, single-repo research-note)** — hard defer pending ★10★ threshold.

## Goal

Record the **first in-window cluster-style repo with a human "control room" UI on top of an append-only event log** — `mazze93/stratum` is the freshest cross-section signal of the 22-pass series for LE31's v2-AI deterministic-gate control plane (feature 68 cook-assistant-deterministic-gate). The combination of (a) "epistemic" / evidence-gated trust + (b) "deterministic projection" + (c) "human control room" maps directly to LE31's v2-AI control plane shape.

## Scope

**In scope:**
- Daily direct-repo GET on `https://api.github.com/repos/mazze93/stratum` (via `$HERMES_GITHUB_TOKEN`).
- Tracking star velocity + push activity + license + Python/TS version + dependency footprint on stratum.
- Reading the stratum README in the next daily-research pass to confirm the "evidence-gated trust" + "Tessera projection" + "human control room" patterns.
- Cross-referencing stratum against LE31 features 49 (postledger tamper-evident hash), 61 (holdfast approval ledger), 63 (second-opinion verifier role), 68 (cook-assistant deterministic gate), 81 (append-only immutable audit check).

**Out of scope (v1 / v2):**
- Importing any code from stratum (TypeScript stack mismatch; LE31 is Python+FastAPI).
- Building a feature based on the stratum code surface (★2 is below the build threshold).
- Charter §3.2 license check: MIT license means stratum is technically importable, but no build implied.

## Description

The stratum repo's description (verbatim from GitHub): "Epistemic decision ledger: append-only event log with evidence-gated trust, deterministic Tessera projection, and a human control room. TypeScript + Cloudflare Workers."

| Field | Value |
| --- | --- |
| Repo | [mazze93/stratum](https://github.com/mazze93/stratum) |
| Stars | ★2 |
| Forks | 0 |
| Watchers | 2 |
| License | MIT |
| Language | HTML (TypeScript — package.json present) |
| Created | 2026-08-15T22:00:14Z (7 days before fetch) |
| Updated | 2026-08-22T03:13:06Z (~3.5h before fetch) |
| Pushed | 2026-08-22T03:13:06Z (~3.5h before fetch) |
| Size | small (under 50KB) |
| Topics | append-only |

### Why this is a fresh cross-section signal

The stratum pattern is **unique** in the in-window cluster: every other in-window append-only library is a **pure ledger primitive** — they emit events, verify hashes, and stop there. Stratum is the **first to surface a UI / control-room primitive** on top of the ledger. The three primitives (`epistemic / evidence-gated trust`, `deterministic Tessera projection`, `human control room`) are exactly the primitives LE31 v2-AI control plane needs:

1. **`epistemic / evidence-gated trust`** — events are valid only when supported by evidence (links to sources, evidence receipts, etc.).
2. **`deterministic Tessera projection`** — the ledger is projected into a view layer via a deterministic function (same inputs → same outputs).
3. **`human control room`** — humans can see, audit, and intervene on the ledger events.

LE31 v2-AI cook-assistant-deterministic-gate (feature 68) is exactly the **"human control room over an append-only ledger"** pattern. Stratum is the **first cluster member that hints at this pattern at the library level**.

### Why parking-lot (not build)

(a) **★2 is below the build threshold** — cluster-maturity threshold is ≥10★ (currently 0 in cluster at ≥10★); (b) **TypeScript stack mismatch** — Stratum is TypeScript on Cloudflare Workers; LE31 is Python+FastAPI+aiogram+Postgres; (c) **MIT license = future consumption candidate, not code-fork candidate**; (d) **the architecture is novel** — no second in-window repo has the same pattern, so there's no empirical validation yet; (e) **LE31 already covers the architectural pattern** — features 49/61/63/68/81 are the production implementations.

## Data model

No new LE31 data model. This artifact is a research-note observation. The stratum library does not introduce a new LE31 table or schema.

## Implementation steps

1. **No code change**. This is a research-note artifact.
2. Future-pass tracking: add `mazze93/stratum` to the daily-research watch list.
3. Read stratum README in the next daily-research pass to confirm the "evidence-gated trust" + "Tessera projection" + "human control room" patterns.
4. Re-evaluation: in 30 days (2026-09-22), check whether stratum has crossed ≥10★.

## Telegram interaction if any

None. This is a research-note observation; no Telegram interaction is needed.

## Dependencies

- **`$HERMES_GITHUB_TOKEN`** for daily direct-repo GET on `mazze93/stratum`.
- **GitHub `topic:append-only` search** (filtered by `pushed:2026-07-22..<date>`) for stratum discovery.
- **Cross-reference**: features 49, 61, 63, 68, 81 (production-grade append-only ledger implementations).

## Open questions

1. **What is "Tessera projection"?** — read the README + source code on next pass to confirm.
2. **What is "evidence-gated trust"** — same. Likely a verification pattern but the exact shape is unclear from the description alone.
3. **What is the "human control room" UI?** — TypeScript on Cloudflare Workers suggests a serverless UI; the exact UX is unclear.

## Why this matters

The pattern "append-only ledger + evidence-gated trust + deterministic projection + human control room" is the **shape of LE31's v2-AI control plane** if LE31 ever builds feature 68 (cook-assistant-deterministic-gate). Stratum is the **first cluster member that hints at this shape at the library level**. The cross-section is direct: feature 68 is exactly the LE31 instantiation of this pattern. Stratum is the **research-note that informs the scoping of feature 68**.

## Distinct from existing features

- **Feature 49** (postledger tamper-evident hash) — LE31's tamper-evident hash chain. Distinct: feature 49 is the production hash chain; stratum is a research-note on an external library that re-implements the pattern with a UI.
- **Feature 61** (holdfast approval ledger) — LE31's approval-gated append-only ledger. Distinct: feature 61 is LE31's approval workflow; stratum's "human control room" is a related but different primitive (control-room over the ledger, not approval within the ledger).
- **Feature 63** (second-opinion verifier role) — LE31's verifier role. Distinct: feature 63 is the LE31 role; stratum's "evidence-gated trust" is an external primitive that re-implements the verifier-role concept.
- **Feature 68** (cook-assistant-deterministic-gate) — LE31's v2-AI control plane slice. Distinct: feature 68 is a slice contract; stratum is a research-note on an external library that informs feature 68's scoping.
- **Feature 81** (append-only immutable audit check) — LE31's audit verification. Distinct: feature 81 verifies LE31's own ledger; stratum's "Tessera projection" is an external projection of a different ledger.
- **Feature 92** (ai-agent-decision-ledger-cluster-watch) — **day-1 cluster observation, 6 libraries, all pure ledger primitives**. Distinct: feature 92 is the day-1 cluster; this feature (97) is a **single new cluster member that adds a UI/control-room layer** (a new shape vs feature 92's primitives).

## Sources

- **GitHub `topic:append-only`** (search verified at 2026-08-22 06:44 UTC; PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
- Raw response: `/tmp/le31-brainstorm-2026-08-22/gh_topic_append-only.json` (174,888 bytes, 30 items returned).
- Stratum verified via raw GitHub API response (item id 1296148728).
- Full report: `/opt/data/le31-brainstorm-2026-08-22.md` (Pick B section, lines 95–107).
- Parent Linear issue: HMM-125 (Brainstorm 2026-08-22 — daily).
- This Linear sub-issue: HMM-127.