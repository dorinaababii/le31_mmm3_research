# Feature 141 — KRINEIA five-invariants framework for append-only audit proofs (defer)

> **NEW observation (2026-09-04).** Documents in-window OpenAlex papers `W7203539524` / `W7203537535` (sibling IDs = v1 + v2 of the same Zenodo deposit) *Append-Only as Proof: A Formal Account of Governance Sovereignty in AI Audit Systems* by Reuben Bowlby, DOIs `10.5281/zenodo.21957892` / `10.5281/zenodo.21957891`, 2026-08-15, cited 0×, type `preprint`. **First surface of this paper in the 34-pass series** (parent-verified by ripgrep against all features 1–140 + all brainstorm reports 2026-08-18..30). The paper formalizes the **proof/record distinction** and identifies **five KRINEIA invariants** for an audit log to constitute a governance proof: append-only, no reward-path self-reference, minimal operators, external analysis only, trust-root separation. Bucket: **v2 owner-pains (architecture reference)** — watch-list defer. Zero build time today.

## Goal

Retain the **proof/record distinction** + **five KRINEIA invariants** as the **architectural vocabulary** for the first LE31 v2 surface that needs to ask *which invariants does this surface need to preserve?* before designing. The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the KRINEIA framework: proof/record distinction + five named invariants.
- A decision record: today's verdict is `defer` because LE31 v1 has no v2 surface that needs to ask this question today; the v1 answer is "yes, all five, by charter §3.1 + §3.4 + Postgres transactional constraints".
- A reference for the next time LE31 proposes a v2 surface that wants to verify *governance proof* not just *operational record*.
- The empirical observation: the paper's instantiation in a production multi-agent system with 42,961+ audit bus entries and detection of the **A4 phantom delivery probe class**.

**Out of scope (defer artifact):**
- Any change to the `StockEntry` schema.
- Any change to the `audit_logs` schema.
- Any user-facing "governance proof" surface (no owner-facing query today).
- The paper's production multi-agent system context — LE31 has no AI agents and §3.4 forbids customer-facing AI; the *framework* transfers, the *production instance* does not.

## Description

OpenAlex `W7203539524` / Zenodo `10.5281/zenodo.21957892` — *Append-Only as Proof: A Formal Account of Governance Sovereignty in AI Audit Systems* — formalizes the distinction between **records** (mutable documentation of claims) and **proofs** (tamper-evident, independently observable witnesses) in AI audit systems. The paper identifies **five necessary invariants — the KRINEIA invariants — for an audit log to constitute a governance proof**:

1. **append-only** — no row is updated or deleted; corrections are new rows.
2. **no reward-path self-reference** — an AI agent that scores its own reward cannot read the log it generates to score itself; this is a *consumption* invariant, not a *storage* invariant.
3. **minimal operators** — the set of roles that can write rows is the smallest set that satisfies the operational requirement; new roles require explicit additions.
4. **external analysis only** — the analyst of the log is not the producer; reading-as-auditor is distinct from reading-as-operator.
5. **trust-root separation** — the trust root that signs rows (Postgres permissions, HSM, etc.) is not the same identity as the trust root that reads them (operator, owner, AI).

The paper proves each is **individually necessary** and all five are **jointly sufficient**. It then shows that all current major AI governance frameworks (NIST AI RMF, EU AI Act Article 18, ISO 42001 clause 9.1) specify *records* rather than *proofs* and are therefore structurally incapable of distinguishing genuine governance from governance theater. The paper instantiates the framework in a production multi-agent system with 42,961+ audit bus entries and demonstrates detection of the **A4 phantom delivery probe class** (an event that should have produced a row but didn't).

**Cross-section with LE31 charter §3.1** (append-only posture):

| KRINEIA invariant | LE31 charter §3.1 / §3.4 / v1 status | Evidence |
|---|---|---|
| **append-only** | **Satisfied** by charter §3.1: *"every prepared-item quantity change is a new `StockEntry`. Never update or delete ledger events."* | Direct match. Both `StockEntry` and `audit_logs` are append-only by design. |
| **no reward-path self-reference** | **Trivially satisfied** because LE31 has no AI inference that reads its own log to score a reward (§3.4 forbids customer-facing AI; v1 has no AI at all). | For any **future v2-AI surface** that proposes an LLM consult `audit_logs` while generating a recommendation, this invariant is the **load-bearing one** and must be checked. |
| **minimal operators** | **Satisfied** — the existing operator set is small (`waiter` / `cook` / `owner`); no role can mutate rows outside its allowed set. | Charter §3.2 + Postgres FK constraints enforce this. |
| **external analysis only** | **Partially satisfied** — LE31's waiter / cook / owner are independent observers of the same `StockEntry` *within* a single restaurant. | Would need a *reviewer-impersonating* check (the owner opening last night's `audit_logs` *as if* they were an auditor, not *as* the owner) before the v2 owner-facing history surface can claim full compliance. |
| **trust-root separation** | **Satisfied implicitly** via Postgres transactional constraints + `actor_user_id` + `actor_role` provenance fields. | Maps onto a future concern if LE31 ever signs logs with an external HSM rather than DB-level permissions. |

**Cross-section with prior picks:**

- **Feature 121 Field-Tier Minimization** (2026-08-27) — *what is committed is canonical even if later reclassified*. KRINEIA is the *formal envelope* around feature 121's principle: feature 121 says the commitment persists; KRINEIA says the *consumption* of the commitment is also invariant-gated.
- **Feature 122 Trace Integrity CAIT** (2026-08-27) — *what is queried is the right answer*. KRINEIA is the *upstream* of feature 122's measurement: feature 122 measures the answer; KRINEIA verifies the *invariants* that produced the answer.
- **Feature 129 LEDGER Claim-to-Evidence Trace Graphs** (2026-08-28) — *what's the typed edge from a derived figure back to the rows that produced it?*. KRINEIA is the *vocabulary layer* of feature 129: feature 129 names the edges; KRINEIA names the invariants the edges must preserve.
- **Feature 133 HANSARD Runtime Witnessing** (2026-08-29) — *runtime witnessing as architectural primitive*. KRINEIA's `no reward-path self-reference` is the formal cousin of HANSARD's "the record is produced by the suspects" framing.
- **Feature 134 ECHO Auditable Memory Plane** (2026-08-29) — *replace append-only with structured records*. KRINEIA's proof/record distinction gives ECHO a precise name for what its structured records are: ECHO records are proofs, not records.
- **Feature 135 DreamLedger** (2026-08-29) — *credit-ledger dual of `StockEntry`*. KRINEIA's five invariants are the *enforcement layer* that DreamLedger's credit ledger would need to be a proof.
- **Feature 136 MemGuard** (2026-08-29) — *verifier signals as lifecycle metadata*. KRINEIA's `external analysis only` is the formal cousin of MemGuard's persistent verifier signals.
- **Feature 137 NL-to-Executable-Obligations** (2026-08-29) — *policy compilation*. KRINEIA's `minimal operators` is the invariant that policy compilation must preserve.
- **Feature 138 ICI Institutional Continuity** (2026-08-30) — *nine-node continuity model*. KRINEIA's proof/record distinction is the *enforcement mechanism* for ICI's source → consequence → examination join.

LE31 v1 currently has no v2 surface that asks "is this a governance proof or just a record?" — the answer for v1 is **"proof, by all five KRINEIA invariants, by charter §3.1 + §3.4 + Postgres transactional constraints"**. The value of KRINEIA today is **vocabulary**, not *implementation*. The paper provides LE31 with the terms (`proof/record`, `append-only`, `no reward-path self-reference`, `minimal operators`, `external analysis only`, `trust-root separation`) to use when the next v2 surface is proposed.

## Data model

No schema change today. The defer artifact documents that the future KRINEIA-instantiation would have:

- **Storage layer**: existing `StockEntry` + `audit_logs` tables — no change (already append-only by charter §3.1).
- **Invariant assertions** (future): a thin per-mutation check function that verifies the five invariants at write time and returns `(invariant_id, pass/fail, evidence_link)` for each. **Not built today.**
- **Reading-mode flag** (future): a flag on the read path that distinguishes `operator-read` (operator-as-actor) from `auditor-read` (reviewer-as-auditor) so that the `external analysis only` invariant is *enforced* not just *respected*. **Not built today.**
- **Trust-root registry** (future): a record of which identity signs rows (DB user + connection) and which identities can read them; checked at query time. **Not built today.**

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to build this in v2, the implementation steps would be:

1. Add a `LE31_KRINEIA_VERIFY` env flag (default off).
2. Implement the five-invariant check function against existing `StockEntry` + `audit_logs`.
3. Add a CLI command `le31 krineia-check` that runs the check on the live database and returns a per-invariant verdict with evidence links.
4. Add a one-page operator-facing report at `/owner/audit/krineia` that displays the five-invariant verdict with the most-recent-N audit_logs as evidence.
5. **Out of scope for v1**: the AI-agents-of-the-production-multi-agent-system context; the A4 phantom-delivery-probe detection model; any consumer-facing surface.

## Telegram interaction if any

None. KRINEIA is an architecture-reference artifact; no operator-facing Telegram surface today. If the LE31 owner decides to build the v2 owner-facing history surface (features 108 / 134 sibling), KRINEIA's five-invariant check would be exposed *as* part of that surface, not separately.

## Dependencies

- **arXiv / OpenAlex**: paper `W7203539524` / DOI `10.5281/zenodo.21957892` / author Reuben Bowlby / 2026-08-15.
- **Sibling deposit**: `W7203537535` / DOI `10.5281/zenodo.21957891` (v2 of the same deposit).
- **Charter §3.1 (append-only ledger)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.4 (no customer-facing AI)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Companion artifacts**: features 121 / 122 / 129 / 133 / 134 / 135 / 136 / 137 / 138 (ripgrep-verified distinct).
- **Stack**: none — vocabulary only.
- **Licence**: Zenodo deposit; paper itself is open-access on Zenodo. KRINEIA is the paper's name for the invariant set; the paper's "production multi-agent system" is *not* MIT-licensed and is not proposed for adoption (LE31 has no AI agents).

## Open questions

1. **Who would invoke the five-invariant check on a v2 LE31 surface?** LE31 has one stakeholder (the owner). The check is conceptually useful but adds no operational value if the owner is the only one who would read it. Same open question as feature 121 (Field-Tier Minimization): if LE31's one stakeholder is the only one who can read the audit log, the marginal value of formal invariant-gating over charter §3.1's natural append-only posture is **unproven**. Recommendation: revisit when LE31 v2 has a second stakeholder (a second owner, a reviewer, an auditor).
2. **Does charter §3.1 need a `trust-root separation` clause?** Today, trust-root separation is implicit (Postgres permissions). A future v2 surface that uses an external HSM would make this explicit. Recommendation: not a v1 question; revisit when HSM is considered.
3. **Is the `no reward-path self-reference` invariant satisfied vacuously or structurally?** Today: vacuously (no AI). When v2-AI is considered: structurally (charter §3.4 forbids customer-facing AI; staff-facing AI is allowed but would need explicit non-self-reference enforcement). Recommendation: capture in any future v2-AI spec.
4. **Does the A4 phantom-delivery probe class have a LE31 analogue?** Possibly: a `StockEntry` row that records an item was served when no waiter action took place. **Not evaluated.** Recommendation: not a v1 question; revisit when v2 audit-trail surface (feature 108 sibling) is considered.

## Why this matters

LE31 charter §3.1 has been **operationalizing append-only discipline** for 34 passes without ever naming what discipline it is. KRINEIA is the **first formal framework in the 34-pass series** that gives the operational discipline a name (proof, not record) and a checklist (five named invariants). The value is not implementation today — LE31 v1 already meets all five invariants vacuously or structurally. The value is **vocabulary**: any future v2 surface can now ask *"which of the five KRINEIA invariants does this surface need to preserve?"* and design accordingly, instead of rediscovering the principles from first principles each time. This is the **highest-leverage vocabulary addition of the 34-pass series**.

The defer is fully reversible: if the LE31 owner decides the vocabulary is not worth carrying, the file can be deleted with no operational impact. The vocabulary is contained in the file, not in the codebase.