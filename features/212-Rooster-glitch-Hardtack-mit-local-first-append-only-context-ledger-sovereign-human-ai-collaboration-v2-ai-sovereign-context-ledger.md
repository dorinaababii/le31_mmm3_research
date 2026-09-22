# Feature 212 — Rooster-glitch-Hardtack-mit-local-first-append-only-context-ledger-sovereign-human-ai-collaboration-v2-ai-sovereign-context-ledger (defer)

> **NEW observation (2026-09-22).** Documents in-window GitHub Search `append-only+ledger` query result: `Rooster-glitch/Hardtack` (**MIT ✓**, **0★/0⑂**, Python, **pushed 2026-09-21T11:23:43Z**, in-window by push only, **34 KB** small repo, default_branch=`main`). Topics (verbatim from raw JSON, **0 topics**): none. Description (verbatim, parent-verified GitHub Search raw JSON): *"Local-first, append-only context ledger for sovereign human-AI collaboration."* **The strongest v2-AI sovereign-context-ledger vocabulary of the 53-pass series** (the only in-window candidate with the *local-first + append-only context ledger + sovereign human-AI collaboration* triple-primitive). Bucket: **v2-AI sovereign-context-ledger (defer, parking-lot)** — watch-list entry, zero build time today.

## Goal

Retain the **"local-first + append-only context ledger + sovereign human-AI collaboration"** triple-primitive as a persistent cross-section reference for any future LE31 v2-AI surface that introduces an AI-assisted workflow with operator-ownership + non-cloud-by-default + append-only-context. The artifact is the persistent cross-section reference + the three named architectural primitives (local-first, append-only context ledger, sovereign human-AI collaboration). No code today (MIT license permits future code reuse; vocabulary-only artifact today).

## Scope

**In scope (defer artifact):**
- A written record of the **local-first** discipline: the *no-cloud-by-default* posture; data lives on the operator's machine; cloud is opt-in only = textbook charter §3.4 compliance.
- A written record of the **append-only context ledger** discipline: every context update is a new append-only entry; the ledger is the persistent record; views are derived, not stored.
- A written record of the **sovereign human-AI collaboration** discipline: the human owns the context; the AI is a guest that reads + writes under explicit user control = the *user-data-sovereignty* principle.
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-assisted workflow surface (charter §3.4 explicitly forbids customer-facing AI; LE31 v1 has no owner-facing AI either).
- A cross-section reference with the prior AI-governance + audit-log + append-only-ledger + human-gate + AI-system-registry primitives cluster: features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404), 198, 199, 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 213 (this file's Pick B sister — hseshadr/avow v2-AI signed-evidence-receipts), 214 (this file's Pick C sister — ilovepixelart/matador v1 frontend-architecture-reference). The *transferable insight* is the **local-first + append-only context ledger + sovereign human-AI collaboration** triple-primitive set.

**Out of scope (defer artifact):**
- Any change to the `audit_logs` schema.
- Any change to the `StockEntry` schema.
- Any change to the cook Telegram bot authorization flow.
- Any customer-facing AI surface in v1 (charter §3.4 explicit invariant: NO customer-facing AI).
- Any owner-facing AI surface in v1 (LE31 v1 has no AI surface at all).
- Any v2-AI surface in v1 (charter §3.4 explicit invariant: AI may only assist owner/staff with observable evidence + non-AI fallback; no v1 surface today).
- Any local-first SQLite migration (LE31 uses Postgres; Hardtack may use sqlite per its small size + local-first posture).

## Description

GitHub Search `append-only+ledger` query (parent re-fetched live, see `/tmp/le31-daily-2026-09-22/gh/append_only_ledger_10cb2e.json`) returned 35 total / 35 retrieved candidates; `Rooster-glitch/Hardtack` is one of the 3 net-new in-window MIT Python candidates not previously filed. It is the strongest v2-AI sovereign-context-ledger vocabulary of the 53-pass series.

The `Rooster-glitch/Hardtack` repo's architectural pattern has three core sub-primitives:

1. **Local-first** — direct LE31 charter §3.4 compliance match. The *local-first* discipline (no cloud by default; data lives on operator's machine) maps onto any future LE31 v2 surface that needs to commit AI-assisted decisions with operator-tooling + non-cloud-by-default posture. The *local-first* pattern is the *data-sovereignty* posture: the operator owns the data; the AI doesn't exfiltrate or co-own.
2. **Append-only context ledger** — direct LE31 `audit_logs` discipline match. The *append-only context ledger* is the same architectural primitive as LE31's `audit_logs` schema (every state change is a new append-only entry; current state is derived). The *context-ledger* framing is the *context-as-append-only* discipline: the AI's working context (the visible-to-AI record of past decisions) is itself an append-only log.
3. **Sovereign human-AI collaboration** — the *operator-owns-the-context* discipline (the human owns the context; the AI is a guest that reads + writes under explicit user control) maps onto charter §3.4 (operator-tooling without customer-cloud) AND charter §3.1 (every state transition must be attributable). The *sovereign* qualifier is the *user-data-sovereignty* principle: the human owns the data; the AI doesn't exfiltrate or co-own.

The LE31 relevance is the **local-first + append-only context ledger + sovereign human-AI collaboration** triple-primitive. LE31 v1 has no AI surface at all (charter §3.4 explicit invariant); the question this repo answers is "if (and only if) LE31 v2 ever introduces an AI-assisted workflow, what is the operator-ownership + non-cloud-by-default + append-only-context primitive set that satisfies charter §3.4?"

## Data model

**No change to LE31 v1's data model today.** The defer artifact is documentation only.

**Future v2-AI trigger condition (if the first v2-AI PR that introduces an AI-assisted workflow lands):** potential schema additions (depending on the v2-AI surface):
- `ai_context_log` table — each AI context update would carry an entry in this table; the *append-only context ledger* primitive from Hardtack. Each row would have `context_id`, `actor_user_id` (always the human for sovereign primitives; the AI cannot write directly), `context_payload` (JSONB), `recorded_at`, `source` (`human` | `ai-proposed` | `ai-confirmed-by-human`).
- `ai_context_sovereignty_policy` table — a config / policy primitive that gates which actors can write to the `ai_context_log` (the sovereign principle = the human is the only primary writer; AI proposes via `ai-proposed` and is upgraded to `ai-confirmed-by-human` only on human approval).
- `local_first_storage_root` config — a config primitive that pins where the `ai_context_log` lives (LE31 v2 could store in a local SQLite file alongside the Postgres for v1-data, with an opt-in cloud-replication policy).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change.

## Implementation

**Today (defer artifact):** No code change. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces an AI-assisted workflow lands):**
- Add an `ai_context_log` SQLModel table (context_id, actor_user_id, context_payload, recorded_at, source).
- Add an `ai_context_sovereignty_policy` SQLModel table (policy_id, allowed_sources, default_actor_constraint, requires_human_approval_for).
- Optionally add a `local_first_storage_root` config primitive that gates the storage location of the `ai_context_log` (charter §3.4: no-cloud-by-default posture).
- Add a periodic `ai_context_snapshot` job that computes derived views (most-recent-AI-proposals, weekly context summary, etc.) and stores them as a snapshot table; the *position-over-time* discipline (cross-reference feature 197 rajo69-ledgerkb vocabulary).

**Steps independent of the v2-AI trigger (today):**
- [x] Read the `Rooster-glitch/Hardtack` GitHub repo structure (parent re-verified the description, license, stars/forks, pushed_at, size_kb against raw JSON).
- [x] Confirm MIT permissive license (parent re-verified `license.spdx_id = "MIT"`).
- [x] Confirm the description's *local-first + append-only context ledger + sovereign human-AI collaboration* triple-primitive vocabulary (parent re-verified verbatim).
- [x] Cross-reference with features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (repo now 404), 198, 199, 203, 204, 205, 213 (this file's Pick B sister), 214 (this file's Pick C sister) (ripgrep-verified distinct).

## Telegram interaction

**Today (defer artifact):** No Telegram interaction. The artifact is documentation only.

**Future v2-AI trigger (when the first v2-AI PR that introduces an AI-assisted workflow lands):**
- The owner would need a Telegram command to view the *AI-context-log summary* (e.g., `/ai-context today`); the *sovereign human-AI collaboration* primitive maps 1:1 onto a chat-style query interface where the human sees the AI's full proposal history.
- The owner would need a Telegram command to *approve an AI-proposed context update* (e.g., `/ai-context-approve <id>`); the *sovereign* primitive would surface `ai-proposed` entries and require explicit human approval to upgrade to `ai-confirmed-by-human`.
- These are v2-AI surface additions; not in v1 scope.

## Dependencies

- **None today.** The defer artifact is documentation only.
- **Future v2-AI trigger dependencies:** depends on the v2-AI surface that introduces an AI-assisted workflow with operator-ownership + non-cloud-by-default + append-only-context (LE31 v1 has none of these surfaces). Cross-references: features 121 (Field-Tier Minimization), 122 (Trace Integrity CAIT), 126 (Five Primitives for Governing AI Agents), 127 (Zero-Shot Self-Orchestration), 128 (SKILL.state), 133 (HANSARD), 134 (ECHO), 137 (NL-to-Executable-Obligations), 141 (KRINEIA five-invariants), 145 (garde-fous), 152, 156 (AWIG-OS rule-citing-audit), 160 (FactGraph), 167 (provtrail hash-chained ledger), 169 (akoffice933 openshare-ledger SHA-256 hash chain), 175 (geminka-agent), 183 (n0-public agent-safety), 187 (traust-ledger disposition-ledger kernel), 188 (ShibaClaw self-hosted security-first AI agent), 189 (HASHI local-first control-plane), 190 (ilyautov small-business-RU-34 AI-skills-tax-contractor-INN), 192 (LinkedParticles/particles-standard sourced + confidence-scored append-only ledger), 196 (monstabravo agent-ledger append-only-checked-against-git), 197 (rajo69-ledgerkb — repo now 404, vocabulary-only), 198 (aidankaras-arbiter postgresql point-in-time), 199 (karusrus-transparency-kit EU AI Act Article 50), 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 213 (this file's Pick B sister — hseshadr/avow v2-AI signed-evidence-receipts), 214 (this file's Pick C sister — ilovepixelart/matador v1 frontend-architecture-reference).

## Open questions

1. **Local-first storage substrate:** Hardtack is 34 KB (very small repo); is the *local-first* posture implemented via a local SQLite file, a local JSON-Lines append-only file, or a local Postgres? The full read of Hardtack's schema is needed before any v2 port.
2. **Sovereign enforcement details:** how does Hardtack enforce *sovereign human-AI collaboration* (is the AI banned from writing directly? does the AI always propose + the human confirms? is there a per-request authorization step?). The full read of Hardtack's authorization model is needed before any v2 port.
3. **Append-only context ledger schema details:** what is the exact schema of an *append-only context ledger* entry (does each entry have `context_id` + `actor_user_id` + `context_payload` + `recorded_at` + `source`? or a richer schema with `prev_hash` + `signature`?). The full read of Hardtack's schema is needed before any v2 port.
4. **Local-first → Postgres migration path:** would the Hardtack schema port cleanly to Postgres (LE31 v2 would store the `ai_context_log` in Postgres for SQLModel-consistency), or is the *local-first* discipline sqlite/JSON-Lines-specific (i.e., the file-based portability is the whole point)? Cross-reference: feature 189 (HASHI local-first control-plane = local-first-aware),
6. **MIT license file confirmation:** is Hardtack's MIT license file in the standard `LICENSE` location, or is it a custom-license file? Adoption requires confirmation that the license terms are charter-compatible (charter §3.2).

## Why this matters

The **local-first + append-only context ledger + sovereign human-AI collaboration** triple-primitive is the **cleanest 2026-09-22 v2-AI sovereign-context-ledger vocabulary for any future LE31 v2 surface that introduces an AI-assisted workflow** — and the MIT permissive license confirms it's a *practiced discipline*, not just a theoretical one. The vocabulary is fully transferable to LE31's charter §3.4 compliance pattern (operator-tooling with observable evidence + non-AI fallback; no cloud-exfiltration risk; user-data-sovereignty). The artifact is informational only today; the value is vocabulary + a future-forkable-kernel note.

## LE31 seven-check gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 owner wants to introduce an AI-assisted workflow (e.g., LLM-suggested menu translation, LLM-suggested owner-question-answering), the owner wants *a sovereign-context-ledger surface that the human owns and the AI cannot exfiltrate*, but struggles because *v1 has no AI surface at all (charter §3.4 explicit invariant)*, so that *v2 can offer AI assistance without violating §3.4*." **PASS** (zero-pain today; v1 is small enough that operator-tooling without AI is sufficient; the JTBD is documentation-nicety, not a build-need). |
| 2 | **Viability** | Owner can read the 1-paragraph description? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies; no new permissions. Confidence medium for the architectural match (the *local-first + append-only context ledger + sovereign human-AI collaboration* primitive set is well-established in the GitHub 0★-community-adoption cluster; Hardtack's 34 KB small-repo footprint + MIT license confirms a real implementation, not just a proposal). MIT license is charter-compatible per §3.2. **PASS**. |
| 4 | **Conflict** | None. The *local-first + append-only context ledger + sovereign human-AI collaboration* primitive set is charter §3.1 + §3.4 invariant-compatible (append-only posture preserved; operator-tooling with observable evidence + non-AI fallback; user-data-sovereignty; no customer-facing AI). **PASS** (charter §3.1 + §3.4 invariant-compatible). |
| 5 | **Outcome, appetite, scope** | v2-AI sovereign-context-ledger (architecture-reference); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 1-paragraph description + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (small artifact is already tight). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/212-Rooster-glitch-Hardtack-mit-local-first-append-only-context-ledger-sovereign-human-ai-collaboration-v2-ai-sovereign-context-ledger-HANDOFF.md` and `features/212-Rooster-glitch-Hardtack-mit-local-first-append-only-context-ledger-sovereign-human-ai-collaboration-v2-ai-sovereign-context-ledger.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section reference for the next v2-AI architecture-review moment).

## Cross-references

- Parent research issue: `/opt/data/le31-daily-research-2026-09-22.md` (53rd consecutive daily-research pass).
- Companion artifacts (ripgrep-verified distinct): features 92, 126, 127, 128, 133, 134, 137, 145, 152, 167, 169, 175, 183, 187, 188, 189, 190, 192, 196, 197 (rajo69/ledgerkb — repo now 404, vocabulary-only), 198, 199, 203 (shawn-durrani/membro v2-AI control-plane), 204 (docentesIA/dagwell v2-AI orchestration), 205 (Mark007-R/Restaurant-Intelligence-Platform v1 restaurant-vertical reference), 213 (this file's Pick B sister), 214 (this file's Pick C sister).
- Sister-picks from 2026-09-22: feature 213 (hseshadr/avow v2-AI signed-evidence-receipts), feature 214 (ilovepixelart/matador v1 frontend-architecture-reference).