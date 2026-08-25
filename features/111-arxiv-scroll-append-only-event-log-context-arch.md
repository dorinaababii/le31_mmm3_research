# Feature 111 — arXiv Scroll append-only event-log context-arch watch

> **NEW observation (2026-08-25).** Documents the in-window
> `arXiv:2608.21129v1` Scroll paper (2026-08-21, cs.CL, "Context as
> an Environment: Programmatic Context Management for Long-Horizon
> Agents") which explicitly names "**append-only Event Log** +
> sandboxed persistent Python kernel + typed namespace across model
> calls + lossless historical ground truth + eviction index tied to
> exact Event Log addresses" = direct adjacency to LE31 features
> 30+49+81 v2 audit-trail extension. The Scroll paper is the
> **academic-formalization** of the v2 audit-search surface for
> `StockEntry`-via-Telegram trail (already covered by feature 108
> from 2026-08-24). Combined with feature 108 + features 30/49/81,
> Scroll provides academic backing for the LE31 v2 audit-search
> roadmap.
> Bucket: **v2 owner-pains (watch-list, defer)** — Scroll is the
> academic-formalization of the v2 audit-search roadmap but is not
> actionable as a build today. Cross-section peer for features
> 30+49+81+108 v2 extension.

## Goal

Track the in-window `arXiv:2608.21129v1` Scroll paper as
**academic backing for the LE31 v2 audit-search roadmap**. The
Scroll paper's "append-only Event Log + lossless historical ground
truth + typed namespace + eviction index tied to Event Log
addresses" framing is a stronger formulation of the LE31 v2
audit-search surface for `StockEntry`-via-Telegram trail (covered
by feature 108 from 2026-08-24). Watch-list continue (defer until
the v2 charter review surfaces the audit-search extension).

## Scope

**In scope:**
- Read the Scroll paper in full + cite in the next daily-research
  pass.
- Track whether ≥2 independent papers in the next 30 days converge
  on the same "append-only Event Log + typed namespace" pattern.
- Cross-reference Scroll against features 30+49+81+108 v2
  extension in the LE31 feature-gate trail.
- Add a row to `/opt/data/INDEX.md` "Active feature pipeline" table
  with date, pick, feature path, Linear ID, status (Backlog,
  watch-list defer, v2 owner-pains).

**Out of scope:**
- Any code change to the LE31 backend (Scroll is academic-formalization
  of an already-watched pattern).
- Any schema change, migration, or config key change.
- Any new pip dependency (Scroll does not propose new dependencies).
- Any charter change (charter §3 single-tenant posture remains
  correct for v1; v2 multi-context decomposition is parked).

## Description

### Paper overview

| Field | Value |
|---|---|
| arXiv ID | `2608.21129v1` |
| Title | "Context as an Environment: Programmatic Context Management for Long-Horizon Agents" |
| Authors | (carry-over — not parsed in today's fetch) |
| Category | cs.CL (Computation and Language) |
| Submitted | 2026-08-21T23:39:19Z (carry-over) |
| URL | https://arxiv.org/abs/2608.21129 |

### Key claims (verbatim from arXiv abstract)

> "LLM agents increasingly take on long-running tasks whose history
> grows far beyond a single model context window. Existing approaches
> compress earlier interactions or extract selected information into
> fixed memory representations, committing to what to preserve before
> future needs are known. We present Scroll, a context manager that
> treats each agent session as an executable Session Environment. The
> environment is backed by an **append-only Event Log** and a
> sandboxed, persistent Python kernel. The kernel maintains a **typed
> namespace across model calls**, allowing tool outputs, retrieved
> history, and derived state to be bound to variables rather than
> serialized into the prompt at each call. Model-written code
> searches, materializes, and transforms session state through exec;
> only explicitly printed projections enter the model's working view
> for the next call. Context management thus becomes a programming
> task that inherits the improving coding abilities of LLMs, while
> the **Event Log preserves lossless historical ground truth**. As
> the working view approaches its budget, stale spans are evicted
> but remain recoverable: an **eviction index keeps compact landmarks
> tied to exact Event Log addresses, so that the agent navigates
> directly to evicted regions instead of searching the full log**."

### LE31 adjacency analysis

The Scroll paper's pattern maps directly to LE31's existing
feature contracts:

| Scroll pattern | LE31 feature | Status |
|---|---|---|
| "append-only Event Log" | Feature 30 (append-only-audit-redirect), Feature 81 (audit-trail primitive) | Active in v1 |
| "sandboxed, persistent Python kernel" | (no direct LE31 feature; relates to v2 owner-pains audit-search) | v2 parking-lot |
| "typed namespace across model calls" | Feature 49 (decision-rationale mixin) | v1 active |
| "lossless historical ground truth" | Feature 81 (audit-trail primitive) | v1 active |
| "eviction index tied to exact Event Log addresses" | Feature 108 (Telegram chat-history fuzzy-search `StockEntry`-audit) | v2 parking-lot |
| "agent navigates directly to evicted regions instead of searching the full log" | Feature 108 | v2 parking-lot |

The Scroll pattern is **academic-formalization** of the LE31 v2
audit-search roadmap. It does not propose new dependencies or
new code — it provides a vocabulary for the pattern that LE31 v2
already plans to implement.

### Why this paper matters (but is still a watch-list defer)

1. **Direct adjacency to LE31 features 30+49+81+108.** The
   Scroll pattern (append-only Event Log + lossless historical
   ground truth + typed namespace + eviction index) maps to
   four existing LE31 features (30, 49, 81, 108). This is the
   strongest academic backing for the v2 audit-search roadmap
   observed in the 26-pass series.
2. **Long-context evidence for v2 audit-search.** Scroll's
   results (94.8% on LongMemEval_S, 73.1% on BEAM_10M, 86.7%
   on LOCA_256K) demonstrate that the append-only Event Log
   pattern works for long-horizon agents. LE31 v2 audit-search
   for `StockEntry`-via-Telegram trail is a long-horizon
   problem (history grows beyond the model context window);
   Scroll's results are directly relevant.
3. **Informs LE31 v2 audit-search implementation.** The
   pattern (append-only log + typed namespace + eviction
   index + model-written code to navigate) is a
   more-formalized version of the v2 audit-search surface
   already covered by feature 108 (Telegram chat-history
   fuzzy-search `StockEntry`-audit, AGPL-3.0 peer blocks
   code-import but indexing pattern is reusable).
4. **No new dependency, no schema change.** Scroll does not
   propose new dependencies; the pattern is implemented in
   the agent's prompt + Python kernel. The LE31 v2
   audit-search can adopt the pattern without new pip deps.
5. **Watch-list defer.** The Scroll paper is academic; not
   actionable as a build today. Watch-list continue until the
   v2 charter review surfaces the audit-search extension.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 30 `append-only-audit-redirect` | Append-only audit-redirect (LE31 v1) | LE31 feature, not academic |
| 49 `decision-rationale-mixin` | Decision-rationale mixin (LE31 v1) | LE31 feature, not academic |
| 81 `audit-trail-primitive` | Audit-trail primitive (LE31 v1) | LE31 feature, not academic |
| 104 `aldia-ai-agent-business-engine-cross-section` | ALdia peer (Apache-2.0 MCP business engine) | Different peer, MCP framing |
| 108 `telegram-chat-history-fuzzy-search-stockentry-audit` | Telegram fuzzy-search for `StockEntry`-audit (LE31 v2 cross-section) | LE31 feature, not academic |
| **111 `arXiv-scroll-append-only-event-log-context-arch` (this)** | Scroll paper academic-backing for v2 audit-search roadmap | **Academic-formalization** of features 30+49+81+108 |

This pick is **academic backing** for the LE31 v2 audit-search
roadmap. It is NOT a duplicate of features 30/49/81/104/108 — it
is the **first academic paper** in the 26-pass series that
explicitly describes the append-only Event Log + typed namespace
+ eviction index pattern that LE31 v2 plan to implement.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation + a watch-list artifact; no schema change.

## Implementation

1. Read the Scroll paper in full in the next daily-research pass
   (2026-08-26) and cite in the report.
2. Track whether ≥2 independent papers in the next 30 days
   converge on the same "append-only Event Log + typed namespace"
   pattern. If yes, surface in a future daily-research pass as
   a "pattern convergence" signal.
3. Cross-reference Scroll against features 30+49+81+108 v2
   extension in the LE31 feature-gate trail when the v2 charter
   review opens.
4. **No build today.** The pick is a watch-list defer. The
   "should LE31 v2 adopt the Scroll pattern for audit-search?"
   question is parked pending the v2 charter review.

## Telegram interaction

None. This is a passive watch-list observation; no LE31
cook/manager action.

## Dependencies

- None. The Scroll pattern is academic-formalization; no new
  dependencies.

## Open questions

- Does the v2 charter review surface the audit-search extension
  in the next 90 days? (If yes, Scroll becomes a
  charter-question prompt.)
- Do ≥2 independent papers in the next 30 days converge on the
  same "append-only Event Log + typed namespace" pattern? (If
  yes, surface as a "pattern convergence" signal.)
- Does feature 108 (Telegram chat-history fuzzy-search
  `StockEntry`-audit) reach build-candidate status in the next 30
  days? (If yes, Scroll becomes a v2 charter-question prompt.)
- Does the Scroll paper have a public release of the reference
  implementation? (If yes, evaluate for code-import per charter
  §3.2.)

## Why this matters

The `arXiv:2608.21129v1` Scroll paper is the **first academic
paper** in the 26-pass daily-research series that explicitly
describes the "append-only Event Log + typed namespace + lossless
historical ground truth + eviction index" pattern that LE31 v2
plans to implement. The Scroll pattern is the
**academic-formalization** of the LE31 v2 audit-search roadmap
already covered by features 30+49+81+108. Combined with feature
108, Scroll provides academic backing for the LE31 v2
audit-search roadmap. The paper's results (94.8% on LongMemEval_S,
73.1% on BEAM_10M, 86.7% on LOCA_256K) demonstrate that the
pattern works for long-horizon agents. **The Scroll paper is the
strongest academic backing for the v2 audit-search roadmap
observed in the 26-pass series.**
