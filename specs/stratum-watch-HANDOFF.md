# stratum-watch — HANDOFF

> **Slice for the research agent.** This is a passive single-repo research-note observation of `mazze93/stratum` — the **first in-window cluster-style repo with a human "control room" UI on top of an append-only event log**. The slice boundary is hard: zero source-file edits, zero schema changes, zero new config keys. Read this *and* `features/97-stratum-watch.md` before touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `97`
- Slug: `stratum-watch`
- Contract file: `features/97-stratum-watch.md`
- Bucket: **v2-AI control-plane (parking-lot, single-repo research-note)** — hard defer pending ★10★ threshold
- Linear parent: **HMM-125** (Brainstorm 2026-08-22 — daily, created in this cron)
- Linear sub-issue: **HMM-127** (Feature label, project `le31 v1 — Core MVP` per le31-feature-pipeline SKILL.md nonexistent-`le31 v2-AI` correction)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed** (verified in-window via GitHub `topic:append-only` search at 2026-08-22 06:44 UTC with PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`; 1 stratum repo identified).

**Confidence:** **medium-low** for the build implication (★2 is below the build threshold; TypeScript stack mismatch; no second in-window repo with the same pattern); **high** for the architectural pattern (the combination of "epistemic / evidence-gated trust + deterministic projection + human control room" is unique in window).

**Decision: parking-lot; hard defer pending ★10★ threshold.** Stratum is the **first cluster-style repo with a UI/control-room layer** — every other in-window append-only library is a pure ledger primitive. The re-evaluation trigger is **stratum star velocity** (≥10★ in next 30 days) OR a second in-window repo with the same UI/control-room pattern appears.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-22).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/97-stratum-watch.md             # NEW (this artifact)
specs/stratum-watch-HANDOFF.md           # NEW (this file)
INDEX.md                                  # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back** `features/97-stratum-watch.md` and confirm it matches the daily-brainstorm report's "stratum-watch" pick description (Pick B section).
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-22), pick slug (`stratum-watch`), feature path (`features/97-stratum-watch.md`), and Linear sub-issue ID (HMM-127).
3. **On the next daily-research pass**:
   a. Direct-repo GET on `mazze93/stratum` via `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN"`:
      - `https://api.github.com/repos/mazze93/stratum`
   b. Read the README via `curl -sS https://raw.githubusercontent.com/mazze93/stratum/main/README.md` to confirm the "evidence-gated trust" + "Tessera projection" + "human control room" primitives.
   c. Track star velocity + push activity + license + TypeScript version + Cloudflare Workers runtime on the repo.
   d. Update the "Why this matters" section of `features/97-stratum-watch.md` with the README-confirmed primitives.
4. **No build implied.** The pick is a single-repo research-note observation. The re-evaluation trigger is **stratum star velocity** (≥10★ in next 30 days) OR a second in-window repo with the same UI/control-room pattern appears — not a build decision.

## Linear sub-issue

Create a Linear sub-issue in project **`le31 v1 — Core MVP`** (per le31-feature-pipeline SKILL.md nonexistent-`le31 v2-AI` correction — the canonical v2-AI control-plane bucket does not exist) with label `Feature`.

- Title: `Feature 97 — stratum-watch`.
- Body: the contract from `features/97-stratum-watch.md` (or a short summary + the file path).
- Parent: **HMM-125** (Brainstorm 2026-08-22 — daily).
- Status: `Backlog`.

## Rollback path

Delete `features/97-stratum-watch.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

Stratum is the **first cluster member that hints at LE31 v2-AI cook-assistant control plane** (feature 68) at the library level. The combination of (a) "epistemic / evidence-gated trust" + (b) "deterministic Tessera projection" + (c) "human control room" maps directly to the shape of LE31 v2-AI control plane if LE31 ever builds feature 68. Stratum is the **research-note that informs the scoping of feature 68**. Filed as a parking-lot research-note with a clear re-evaluation trigger: stratum star velocity (≥10★ in next 30 days).

## Carry-over history

This is the **NEW observation** (2026-08-22); no prior artifact exists. Combines:

- The `mazze93/stratum` in-window repo (★2, MIT, HTML/TypeScript, pushed 2026-08-22).
- The 22-pass observation that all other in-window append-only libraries are pure ledger primitives (no UI).
- The v2-AI control-plane pattern (carry-over from features 49, 61, 63, 68, 81) — stratum is the **first cluster member with a UI primitive** that informs feature 68's scoping.
- The cross-section with feature 92's day-1 cluster (6 pure-ledger-primitive libraries) — stratum is the **first new shape** beyond those primitives.

## Sources

- **GitHub `topic:append-only`** (search verified at 2026-08-22 06:44 UTC; PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
- Raw response: `/tmp/le31-brainstorm-2026-08-22/gh_topic_append-only.json` (174,888 bytes; stratum item id 1296148728).
- Full report: `/opt/data/le31-brainstorm-2026-08-22.md` (Pick B section, lines 95–107).
- Linear parent: HMM-125 (Brainstorm 2026-08-22 — daily, status Done).
- Linear sub-issue: HMM-127 (Feature label, status Backlog, parent HMM-125).