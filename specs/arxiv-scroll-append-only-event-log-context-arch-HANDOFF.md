# arxiv-scroll-append-only-event-log-context-arch — HANDOFF

> **Slice for the research agent.** This is a passive watch-list
> observation of the in-window `arXiv:2608.21129v1` Scroll paper
> (2026-08-21, cs.CL, "Context as an Environment: Programmatic
> Context Management for Long-Horizon Agents"), not a feature
> build. The slice boundary is hard: zero source-file edits, zero
> schema changes, zero new config keys. Read this *and*
> `features/111-arxiv-scroll-append-only-event-log-context-arch.md`
> before touching any code. Do not paste chat excerpts back into
> the build.

## Frozen identifiers (do not rename)

- Feature ID: `111`
- Slug: `arxiv-scroll-append-only-event-log-context-arch`
- Contract file: `features/111-arxiv-scroll-append-only-event-log-context-arch.md`
- Bucket: **v2 owner-pains (watch-list, defer)** — academic-formalization
  of the v2 audit-search roadmap; not actionable as a build today.
- Linear parent: TBD (Research 2026-08-25 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft watch-list artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (verified in-window via arXiv API + `append-only ledger`
query; `arXiv:2608.21129v1` Scroll paper published 2026-08-21T23:39:19Z;
explicit "append-only Event Log + lossless historical ground truth +
typed namespace + eviction index" pattern).

**Confidence:** **high** for the pattern (the Scroll paper's framing
is direct and unambiguous; the LE31 feature-gate trail already has
features 30+49+81+108 mapping to the same pattern); **low** for
LE31-specific urgency (charter §3 single-tenant posture for v1; v2
audit-search extension is parked pending v2 charter review).

**Decision: watch-list defer (hard defer pending v2 charter review
of audit-search extension).** The slice boundary is hard: zero
source-file edits, zero schema changes, zero new config keys. The
watch-list tracking tests whether the Scroll pattern converges with
≥2 independent papers in the next 30 days.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-research` (this pick came from the daily research job
   on 2026-08-25).
5. `le31-feature-pipeline` (so the agent understands how this slice
   will be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/111-arxiv-scroll-append-only-event-log-context-arch.md   # NEW (this artifact)
specs/arxiv-scroll-append-only-event-log-context-arch-HANDOFF.md # NEW (this file)
INDEX.md                                                            # EDIT: append one row to "Active feature pipeline" table (watch-list defer entry)
```

Zero source-file edits outside the research artifacts. Zero schema
changes. Zero new config keys.

## Verification protocol

- **Today**: verify that this `HANDOFF.md` exists + the
  `features/111-…md` contract file exists + the `INDEX.md` row was
  added + the `Research 2026-08-25 — daily` Linear issue was created
  with the parent body + the `le31_v2_owner_pains` Linear sub-issue
  was created with the contract body and `Feature` label.
- **Tomorrow (2026-08-26)**: read the Scroll paper in full and
  cite in the next daily-research pass. Confirm:
  - Does the Scroll paper explicitly describe "append-only Event
    Log + lossless historical ground truth + typed namespace +
    eviction index"?
  - Does the paper have a public release of the reference
    implementation?
  - Does the paper's evaluation (94.8% on LongMemEval_S, 73.1%
    on BEAM_10M, 86.7% on LOCA_256K) generalize to the LE31 v2
    audit-search problem?
- **30-day rolling**: track whether ≥2 independent papers in the
  arXiv + OpenAlex feeds converge on the same "append-only Event
  Log + typed namespace" pattern.
- **Re-check threshold**: if the v2 charter review opens AND
  surfaces the audit-search extension in the next 90 days, OR if
  ≥3 independent papers converge on the same pattern, the slice
  is un-deferred and becomes a v2 charter-question prompt.
- **Drop threshold**: if the v2 charter review does not surface
  the audit-search extension by 2027-05-01 (90-day window from
  this artifact), surface in a future daily-research pass as a
  "parking-lot continue" signal.

## Rollback path

**Fully reversible.** Delete this file + the corresponding
`INDEX.md` row. Zero risk of code regression (no code changed).

## Carry-over chain (provenance)

This slice is the **first in-window academic paper** in the
26-pass daily-research series that explicitly describes the
"append-only Event Log + typed namespace + eviction index"
pattern that LE31 v2 plans to implement. There is no
carry-over chain for this slug — this is the **inaugural
entry** for the `arxiv-scroll-append-only-event-log-context-arch`
slug. Future daily-research passes may add
`arxiv-scroll-append-only-event-log-context-arch-v2` if the
pattern converges with additional independent papers.

Cross-reference (informational, not carry-over):

- **Feature 30** (`append-only-audit-redirect`) — LE31 v1 audit-redirect feature
- **Feature 49** (`decision-rationale-mixin`) — LE31 v1 decision-rationale feature
- **Feature 81** (`audit-trail-primitive`) — LE31 v1 audit-trail feature
- **Feature 104** (`aldia-ai-agent-business-engine-cross-section`) — Apache-2.0 MCP business-engine peer (cross-section, charter-pending)
- **Feature 108** (`telegram-chat-history-fuzzy-search-stockentry-audit`) — LE31 v2 audit-search cross-section (Telegram fuzzy-search for `StockEntry`-audit, AGPL-3.0 peer)
- **arXiv:2608.21138v1 EvoWiki** (2026-08-24, cs.CL) — "Incremental State Overwriting" paper; adjacent to LE31 audit-trail but Scroll is more relevant (Scroll = append-only Event Log + lossless history; EvoWiki = entity version chains + State-Overwrite Protocol)

## Stop conditions

Pause and ask the user if any of the following is true:
- The v2 charter review opens AND surfaces the audit-search
  extension (would trigger a new build pick).
- ≥3 independent papers converge on the same
  "append-only Event Log + typed namespace" pattern (would
  trigger a "pattern convergence" signal).
- The Scroll paper's reference implementation is publicly
  released with a permissive license (would re-open the
  code-import question per charter §3.2).
- Verification fails twice on the same root cause.

## Mirror-back confirmation

Before coding (or in this case, before tracking), mirror back:
slice ID (`111`), required skills (le31-conventions +
le31-v1-feature-pattern + le31-handoff-spec + le31-daily-research +
le31-feature-pipeline), verification protocol (read paper in full +
30-day pattern-convergence tracking + v2 charter-review tracking),
and rollback path (delete file + INDEX.md row). Confirm or correct
each, then begin tracking.
