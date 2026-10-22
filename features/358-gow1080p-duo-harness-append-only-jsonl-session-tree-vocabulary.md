# Feature 358 — `gow1080p-duo-harness-append-only-jsonl-session-tree-vocabulary` (defer)

> **NEW observation (2026-10-22).** Documents in-window GitHub repo `gow1080p/duo-harness` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**), **★3/⑂2**, **161 KB**, **TypeScript OFF-STACK for LE31's Python 3.13 / FastAPI / SQLModel / aiogram v3 charter**, created **2026-10-21T05:01:35Z** and pushed **2026-10-22T06:29:56Z (today, ~1h before this pass ran)**, `archived=false`, `fork=false`, 0 open issues, default_branch=`main`). Description (verbatim from GitHub API direct-GET, **parent-verified 2026-10-22**): *"Zero-bloat, vendor-agnostic TypeScript Agent Harness (Functional Core + Append-Only JSONL Session Tree + KV Cache Compactor + Cost & Cache Tracker + MCP + Autonomous Code Reviewer)"*. Topics: **none** (`[]`). Bucket: **v2-AI (vocabulary only)** — Pick C of Daily Research 2026-10-22. Build verdict: `defer` (parking-lot; **vocabulary reference only**).

> **Bucket note:** `le31 v2-AI` **does not exist** as a Linear project (confirmed via `list_projects` 2026-10-22: the workspace has only `le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1). Per `le31-feature-pipeline/SKILL.md` line 33, the intended sub-issue attaches to **`le31 Research` P-HMM-1**. **No attachment actually occurred — the Linear write endpoint is blocked (34th consecutive day).**

## Goal

Record the **append-only session tree as a first-class structure** and the **functional-core / effects-at-the-edge** split, as durable cross-section vocabulary for the *day LE31 gains any AI surface at all*. LE31 has **no AI surface today**, so this is a parking-lot citation with an explicit dependency on a decision that has not been made. No code today.

## Scope

**In scope (defer artifact):**

- A written record of the **append-only JSONL session tree** primitive: a conversation is a tree of immutable nodes on disk, not a mutable message array.
- A written record of the **functional-core / effects-at-the-edge** split: pure logic in the core, all I/O at the boundary. This is good discipline and is *already* how FastAPI+SQLModel separates, but the explicit naming is worth keeping.
- A written record of the **cost and cache tracker** primitive — the idea that an agent harness treats token spend as a tracked, visible quantity rather than an invisible side effect. This is the one primitive with a §3.4 flavour.
- A written record of the **bounded-context-window-as-arbitrary-gate** idea, which appears in the *sibling* repo `megablue/mega-smart-context` (*"a bounded memory document, a verbatim working window and a gated archive instead of append-only history"*) and **directly contradicts** this repo's append-only posture. **Both are recorded; the disagreement is unresolved and is explicitly not resolved here.**
- A decision record: verdict is `defer` because LE31 has no AI surface for any of this to govern.

**Out of scope (defer artifact):**

- Any AI surface. **None is proposed.**
- Any MCP client or server in LE31.
- Adoption of the TypeScript codebase (off-stack).
- Any resolution of the append-only-vs-bounded-window conflict.

## Out of scope

- See "Scope" above. The defer artifact is **vocabulary-only**; no code is shipped today.

## Evidence / JTBD

**Gate check 1 (JTBD) fails as stated.** The repo's job is: *when an AI agent runs a long task, its operator wants to inspect what happened and what it cost, but struggles because agent state is opaque and spend is invisible, so that the run can be audited.* **LE31 has no agent.** There is no run to audit. This is a job for someone building an agent product; LE31 is a restaurant operations system.

- **Evidence class**: **observed** (repo exists; all fields read from `GET /repos/gow1080p/duo-harness`, not from a search index).
- **Confidence**: **high** that the description names the primitives it claims; **low** for LE31 relevance — **the lowest of today's three picks**, because it targets a product category LE31 is not in.
- **Traction caveat, recorded plainly**: ★3/⑂2 is **minimal**. This is a repo created yesterday. The pick is about the *shape*, not the project.
- **Real observed LE31 JTBD**: **zero**.

## Description

GitHub `gow1080p/duo-harness` (MIT ✓, ★3/⑂2, 161 KB, TypeScript OFF-STACK, created 2026-10-21, pushed 2026-10-22, archived=false, topics `[]`).

Six named components. Three matter to LE31, three do not:

**Matters:**

1. **Append-Only JSONL Session Tree** — a session is a tree of immutable nodes persisted as JSON Lines. Language-neutral, trivially portable to Python. **This is §3.3 applied to the conversation domain**: append-only, current state derived, never updated.
2. **Cost & Cache Tracker** — token spend and cache behaviour are tracked quantities. §3.4 requires AI assistance to come "with observable evidence"; a cost tracker is a weak but real instance of that. The stronger LE31 reading would be: if any AI surface ever exists, **its cost must be visible to the owner, not hidden in a log**.
3. **Functional Core + effects at the edge** — pure domain logic separated from I/O. LE31 already does this structurally; keeping the name prevents a future pass from re-deriving it.

**Does not matter:**

4. **KV Cache Compactor** — an infrastructure optimisation with no LE31 analogue.
5. **MCP integration** — LE31 has no AI surface to expose.
6. **Autonomous Code Reviewer** — a development-time tool, not a product feature.

**The unresolved conflict.** The sibling repo `megablue/mega-smart-context` (MIT, TypeScript, ★1, 544 KB, pushed 2026-10-21, also in-window) argues the **opposite** position: *"the model owns the context window — a bounded memory document, a verbatim working window and a gated archive instead of append-only history."* `duo-harness` keeps append-only history; `mega-smart-context` deliberately replaces it with a bounded window and a gated archive.

**This is the same unresolved disagreement already recorded between features 352 (`Idriz-hax/harbor-ledger-memory`, keyword/file-based with the document set always surfaced) and 354 (`AIDAChip-Inc/mem-plus-plus`, vector-first hybrid retrieval).** That disagreement has now been observed in a second, independent pair of repos. **It is not resolved here and must not be presented as resolved.** The tension is real and architectural: an append-only history is auditable but grows without bound; a bounded window is efficient but forgets, and forgetting is exactly what an auditor cannot tolerate.

## Data model

None shipped.

For reference, the implied shape is a **session** (immutable identifier), a **node** (parent pointer + payload + timestamp, written once), and derived **session state** computed by folding the tree. The `megablue/mega-smart-context` position would replace the fold with a **bounded document** plus an **explicitly gated archive** — where the gate, not the size limit, is the safety property.

No LE31 entity changes.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (all must hold):** (1) an **explicit owner decision** that LE31 gains any AI surface at all — this decision has not been made and this contract does not presume it; (2) the §3.4 non-AI-fallback requirement is specified for that surface; (3) the append-only-vs-bounded-window conflict above is resolved. **Condition (1) alone is unmet, and it is the load-bearing one.**

## Telegram interaction

None. Explicitly none — §3.4 permits AI only in the owner/staff assistance role with a non-AI fallback, and no such surface is being proposed.

## Dependencies

- **Blocking:** an unmade owner decision on whether LE31 gets an AI surface at all.
- **Unresolved:** the append-only-vs-bounded-context-window question, now observed in two independent repo pairs (352/354 and 356-adjacent here).
- None technical. No MCP client, no embedding model, no TypeScript adoption.

## Open questions

1. **Does LE31 ever gain an AI surface?** Unmade after 84 passes. Nothing here changes that.
2. **Append-only history or bounded window?** Genuinely open. Two repo pairs disagree. Recorded, not resolved.
3. **Is a cost tracker sufficient "observable evidence" under §3.4?** Probably not on its own — evidence should be about what the AI *did*, not what it *cost*. Recorded as a doubt rather than an answer.
4. **Would the §3.7 boundary apply** if a session tree ever stored restaurant context? Yes, and it is unmade — the same unmade boundary already recorded on features 352 and 354.

## Why this matters

Very little today, and the contract says so. Its only real value is that the append-only-vs-bounded-window conflict has now been seen **twice, independently**. That makes it a pattern rather than an anecdote, which is worth knowing *before* the decision is made — but a pattern observed from outside is still not evidence of restaurant pain, and per `le31-conventions` pitfall 2 it must not be converted into demand.

---

**Gate verdict: `defer`.** Fails check 1 (JTBD — no agent surface exists). Fails check 3 partly (the prerequisite owner decision is unmade). **No hard conflict**, but it sits directly on top of an unresolved architectural conflict. Fully reversible (161 KB, vocabulary-only). v2-AI bucket, attached to `le31 Research` in the fallback payload only — **not attached in Linear**.