# Spec 187 — `traust-security-traust-ledger-append-only-disposition-ledger-kernel` (HANDOFF)

**Source feature:** `features/187-traust-security-traust-ledger-append-only-disposition-ledger-kernel.md`
**Parent research issue:** HMM-266 (Research 2026-09-17 — daily)
**Linear sub-issue:** HMM-269
**Filed:** 2026-09-17 by the LE31 daily-research cron (Pick C of Daily Research 2026-09-17)

---

## Active feature path

- **Repo:** `dorinaababii/le31_mmm3_research.git` (working dir: `/opt/data/le31_mmm3_research_work/`)
- **Feature spec file:** `features/187-traust-security-traust-ledger-append-only-disposition-ledger-kernel.md`
- **This HANDOFF file:** `specs/187-traust-security-traust-ledger-append-only-disposition-ledger-kernel-HANDOFF.md`

## Seven-check gate verdict

| # | Check | Status |
|---|---|---|
| 1 | Goal stated | PASS (v2 architecture-reference observation; closest reusable v2-hardening primitive of 2026-09-17) |
| 2 | Evidence / JTBD stated | PASS (GitHub API description is direct: "Append-only disposition ledger kernel for security auditing workflows") |
| 3 | Scope + Out-of-scope stated | PASS (vocabulary-only artifact; no code change; no library; no new dependency; security-audit domain OFF-LE31 acknowledged) |
| 4 | User flow described | PASS (no user-visible flow today; the v2 trigger is the introduction of an external-audit-trail surface that needs a tamper-evident append-only ledger primitive) |
| 5 | Data model described | PASS (no data model change today; the future v2 schema migration is described) |
| 6 | Dependencies + failure-recovery + DoD | PASS (AGPL/SSPL ripgrep dependency; kernel-interface inspection dependency; no recovery needed; DoD = feature spec exists + HANDOFF exists + Linear sub-issue created + parent research issue exists + push to main) |
| 7 | Open questions listed | PASS (3 open questions, all related to the two next-step questions + a vocabulary question on "disposition") |

**Gate verdict:** PASS — v2 architecture-reference defer (parking-lot). No build today.

## Files to touch

**None today.** This is a vocabulary-only artifact. The coding agent does NOT need to touch any files in `le31_mmm3_research` today.

**Read-only inspection tasks** (not file modifications):

1. The coding agent MAY ripgrep the `traust-ledger` GitHub repository (`traust-security/traust-ledger`) for any AGPL-3.0 or SSPL dependency that would contaminate the permissive Apache-2.0 license.
2. The coding agent MAY inspect the kernel interface (`__init__.py` or equivalent) to determine whether the kernel exposes a Python class (in-process integration) or a standalone service (network/IPC integration).

These are **read-only** inspections — they do NOT modify any files in `le31_mmm3_research`.

## Verification protocol reference

Per `le31-feature-pipeline/SKILL.md`, the coding agent should:

1. **Confirm no build is required today.** This is a defer/parking-lot artifact; the only verification is that the feature spec exists, the HANDOFF exists, and the Linear sub-issue is created.
2. **If the future v2 trigger condition fires**: read the `traust-ledger` GitHub repository on GitHub (`traust-security/traust-ledger`) and inspect the kernel interface + dependencies to verify the two next-step questions.
3. **Read the companion artifacts** (features 121, 122, 133, 134, 135, 141, 148, 167, 168, 169, 181, 182) to understand the existing v2 architecture-reference cluster.
4. **Pre-merge review.** Per `pre-merge-review/SKILL.md`, this is a documentation-only artifact (no code change), so the pre-merge review is light.
5. **Push to main.** `git push origin main`.
6. **Update Linear sub-issue HMM-269** to `Done` when the artifact is filed (today's cron run does this automatically).

## Rollback path

**None needed.** This is a documentation-only artifact (vocabulary observation + future-forkable-kernel note). There is no code change to roll back.

If the upstream `traust-ledger` repository disappears, changes its license, or its kernel interface becomes incompatible with LE31's stack, the next pass would file a new observation that supersedes this one (or updates the existing record). The artifact is not load-bearing for any LE31 v1 surface.

## Mandatory LE31 skill list

The coding agent MUST load and apply these skills before starting:

1. `le31-conventions` — for the LE31 charter §3.1, §3.2, §3.4 invariants that apply to v2 architecture-reference deferrals.
2. `le31-v1-feature-pattern` — for the canonical v1 feature contract shape (this HANDOFF follows that shape; the agent should re-read the spec to confirm).
3. `development` — for the spec → plan → tasks → implement pipeline (no implementation today, but the skill list applies for any future v2 surface that builds on this artifact).
4. `pre-merge-review` — for the non-author-independent-review gate (light, since no code change today).
5. `verify-before-fixing` — for the discipline of "this is a defer/parking-lot artifact; no implementation is needed; verify the artifact is correctly filed rather than starting to fix things."

## Notes for the coding agent

- **No build today.** This is a defer/parking-lot artifact. The coding agent should NOT touch any files in `le31_mmm3_research` today beyond the cron-generated files.
- **Apache-2.0 permissive license confirmed** — charter §3.2 ✓ (license tag: Apache-2.0, GitHub API response confirms). But: AGPL/SSPL dependency contamination is the open question (ripgrep required).
- **1★/4⑂ fork/derivative activity signal is noteworthy.** 4 forks on 1★ indicates active fork-based adoption by other developers (typical bookmarking behavior would result in more stars; fork-count > star-count is the kernel-primitive signature).
- **The two next-step questions are the gate to any future v2 reference usage:** (1) AGPL/SSPL dependency ripgrep; (2) kernel interface inspection (Python class vs standalone service). Until both are answered, `traust-ledger` is vocabulary-only.
- **The "disposition" word in the description** is interesting — it suggests event-outcome tracking (e.g., "this event was disposition: approved / denied / pending"). LE31's `audit_logs` doesn't have a notion of disposition today. The coding agent should consider whether the v2 schema needs an optional `disposition` field (vocabulary-only question, defer until v2 trigger).
- **The 1:1 mapping table** in the feature spec (4 kernel primitives vs LE31 v1 architecture status) is the at-a-glance gate summary. The coding agent should re-read the table before any adoption decision.
- **Future v2 trigger condition** = the introduction of an external-audit-trail primitive (e.g., tax filing, accountant verification). When that trigger fires, the v2 surface that addresses it should reference feature 187 + features 167 (provtrail) + 181 (Merkle Audit) — the three append-only-ledger kernel options for the v2-hardening cluster.