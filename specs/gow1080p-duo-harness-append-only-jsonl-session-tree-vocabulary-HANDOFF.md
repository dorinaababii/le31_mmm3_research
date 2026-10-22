# HANDOFF — `gow1080p-duo-harness-append-only-jsonl-session-tree-vocabulary`

> **Build verdict: `defer`.** This slice contract exists because `le31-feature-pipeline` requires one per pick. **The coding agent should not start work, and must not invent an AI surface to justify starting.** The load-bearing precondition — an explicit owner decision that LE31 gains any AI surface — is unmade after 84 passes.

## Active feature path

`features/358-gow1080p-duo-harness-append-only-jsonl-session-tree-vocabulary.md`

External source: `https://github.com/gow1080p/duo-harness` (MIT, TypeScript OFF-STACK, ★3/⑂2, 161 KB, created 2026-10-21, **pushed 2026-10-22 — today**, zero topics). All fields parent-verified 2026-10-22 from `GET /repos/...`.

## Seven-check gate verdict

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | **FAIL** — job is auditing an AI agent run; LE31 has no agent |
| 2 | Viability | pass — nothing to operate |
| 3 | Practicability & confidence | **partial fail** — the prerequisite owner decision is unmade; TypeScript off-stack |
| 4 | Conflict | **no hard conflict**, but sits atop an *unresolved* architectural conflict (below) |
| 5 | Outcome / appetite / scope | no v1 outcome served |
| 6 | Cost to operational value | none for a restaurant owner |
| 7 | Circuit breaker / reversibility | fully reversible; 161 KB |

**Decision: `defer`.** Evidence class **observed**, confidence **high** on the shape / **low** on LE31 relevance — **the lowest of today's three picks**, because it targets a product category LE31 is not in.

## The unresolved conflict — do not treat as settled

Two independent repo pairs now disagree, and **the disagreement is unresolved**:

- **Append-only history:** this pick (`duo-harness`, append-only JSONL session tree) and feature 352 (`Idriz-hax/harbor-ledger-memory`, keyword/file-based with the document set always surfaced).
- **Bounded window:** the sibling `megablue/mega-smart-context` (*"a bounded memory document, a verbatim working window and a gated archive instead of append-only history"*) and feature 354 (`AIDAChip-Inc/mem-plus-plus`, vector-first hybrid retrieval).

**The tension is real and architectural:** an append-only history is auditable but grows without bound; a bounded window is efficient but *forgets*, and forgetting is exactly what an auditor cannot tolerate.

**A future PR must not resolve this by picking one silently.** `le31-conventions` requires exposing an exact conflict rather than choosing the easiest-looking rule. Any implementation touching this area needs an explicit owner decision recorded in the charter first.

## Files to touch

**None.** Vocabulary artifact; no LE31 source file is modified.

## Verification protocol reference

None required — nothing is built.

**Hard prohibition for any future AI-surface work:** the §3.4 non-AI-fallback must be a *working* path, not a stub. A test asserting the AI path can be disabled and the operator can complete the task manually is the minimum bar. **Do not weaken that test to make a build pass.**

If an append-only session store is ever built, the mandatory tests are: (1) no code path updates or deletes a session node; (2) session state is a *fold* over the tree, never a stored mutable total; (3) if a bounded-window design is chosen instead, the **gate** — not the size limit — is asserted, and archived material remains retrievable.

## Rollback path

Delete `features/358-…md` and this file. No runtime footprint, no data, no migration.

**Note the asymmetry:** reverting an AI surface returns the system to its non-AI state, which is a *safe* default — unlike the policy-chokepoint vocabulary filed on 2026-10-21, where reverting would discard a safety property. Recorded so the two are not conflated.

## Trigger condition (all must hold)

1. **Explicit owner decision that LE31 gains any AI surface at all.** Unmade after 84 passes. This contract does not presume it.
2. §3.4 non-AI-fallback specified for that surface, with observable evidence of what the AI did.
3. The §3.7 boundary defined — what is operational knowledge (supplier prices, prep times) vs guest data (who ordered what, payment instruments) inside a memory or session store. **Unmade** on features 352, 354, and here.
4. The append-only-vs-bounded-window conflict above resolved by the owner.

**All four are unmet.** Condition (1) alone is load-bearing.

## Mandatory LE31 skill list

- `le31-conventions` — the seven-check gate; §3.4 AI-with-observable-evidence-and-fallback; §3.7 privacy boundary; the "expose conflicts, do not guess" rule that governs the unresolved tension above.
- `le31-daily-research` — provenance.
- `le31-feature-pipeline` — why this contract exists despite `defer`.
- `le31-v1-feature-pattern` — the feature-file template shape.
- `features/352-…` and `features/354-…` — **must be read** before any AI-surface discussion; they hold the other two halves of this conflict.

## Status

- **Linear sub-issue:** NOT created. Write endpoint blocked, **34th consecutive day** (HTTP 400 `invalid_request`, free-issue-limit, requestId `a4e675dd19dbdc59`).
- **Bucket:** v2-AI (vocabulary only). **`le31 v2-AI` does not exist** — confirmed via `list_projects` 2026-10-22 (workspace has only `le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1). Intended attachment: `le31 Research` (P-HMM-1) per `le31-feature-pipeline/SKILL.md` line 33. **No attachment occurred in Linear.**
- **Fallback payload:** `/opt/data/le31-daily-research-2026-10-22.linear-fallback.json`.
- **Report:** `/opt/data/le31-daily-research-2026-10-22.md`.