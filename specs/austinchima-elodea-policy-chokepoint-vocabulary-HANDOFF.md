# austinchima-elodea-policy-chokepoint-vocabulary — HANDOFF

> **Slice for the coding agent — NOT YET ACTIVE.** This artifact is a
> `defer` (parking-lot) vocabulary reference. **Do not implement anything from
> this file today.** Read this *and* `features/351-austinchima-elodea-...md`
> before any work begins. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `351`
- Slug: `austinchima-elodea-policy-chokepoint-vocabulary`
- Contract file: `features/351-austinchima-elodea-apache-2-0-inline-policy-enforcement-proxy-for-ai-agents-opa-policies-on-mcp-tool-calls-human-approval-for-risky-actions-hash-chained-audit-log-go-v2-ai-policy-chokepoint-vocabulary.md`
- Bucket: **v2-AI** — `defer` (parking-lot, vocabulary reference only)
- Source repo: `austinchima/elodea` (Apache-2.0, ★1/⑂0, Go OFF-STACK, pushed 2026-10-18T03:52:59Z, created 2026-09-18T16:16:40Z)
- Linear parent: `le31 Research` (P-HMM-1)
- Linear sub-issue: **NOT CREATED** — Linear MCP write endpoint blocked (32nd consecutive day). Fallback JSON: `/opt/data/le31-daily-research-2026-10-21.linear-fallback.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed**
(in-window GitHub repo; verbatim description names `Inline policy enforcement
proxy`, `OPA policies on MCP tool calls`, `human approval for risky actions`,
`hash-chained audit log`).

**Confidence:** **medium-high** for the vocabulary match (all four primitives
named explicitly; the *code* is Go = off-stack, the *discipline* is portable);
**low** for present urgency (LE31 has **no AI surface at all** — nothing exists
to policy-gate).

**Decision: defer (parking-lot).** No build commitment.

**Checks that would block a `build` today:**
- **Conflict (§4) — ⚠️ the blocking one:** the **policy-as-input** posture is the
  **inverse** of LE31's charter §3.1 **rules-as-code** posture. This is the same
  tension already recorded in feature 137
  (`natural-language-policies-executable-obligations-verification-harness`).
  **Owner decision required before any implementation**: either restrict any
  policy-authoring surface to **non-operational** rules (display-only,
  approval-only) or amend the charter. **This is a hard blocker, not a
  preference.**
- **Viability (§2)**: the *on-call*-class upstream domain is off-§3.5; the
  *human-approval* gate degenerates to "the single owner clicks" in a
  single-tenant system, which may add friction without adding safety. Recorded,
  not resolved.
- **Practicability (§3)**: Go + REGO (OPA's policy language) = double
  off-stack. A Python implementation is feasible but the *policy language*
  decision is unmade.
- **Outcome and scope (§5)**: zero v1 demand; v2-AI bucket.

**Checks that pass:** Conflict on the *human-approval* and *hash-chain* postures
(these strengthen §3.4 non-AI-fallback and §3.3 audit-chain rather than
conflicting with them); Reversibility (fully reversible, vocabulary-only).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting (when this slice is ever
re-elevated from `defer` to `experiment` or `build`):

1. `le31-conventions` (project invariants + the seven-check gate; **especially
   the §3.1 rules-as-code vs policy-as-input tension**).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror the contract back).
4. `le31-daily-research` (this pick came from the daily research job on 2026-10-21).
5. `le31-feature-pipeline` (how this slice will be sequenced once re-elevated).
6. `le31-research` (for the cross-section evidence base).

If the destination repo does not yet ship these skills, request them from the
research-side Hermes instance before writing code.

## Files the slice would touch (NOT NOW — reference only)

```
features/351-austinchima-elodea-...md                 # NEW (this contract)
specs/austinchima-elodea-policy-chokepoint-vocabulary-HANDOFF.md   # NEW (this file)
INDEX.md                                              # EDIT: one row in "Active feature pipeline" (added 2026-10-21)
# --- the following exist only as a design sketch; DO NOT CREATE until re-elevated ---
agent/models/agent_tool_call.py                       # AgentToolCall + AgentToolCallApproval + AgentPolicyAuditChain
agent/services/policy_engine.py                       # declarative policy evaluator (YAML/JSON; NOT REGO)
agent/services/policy_proxy.py                        # the chokepoint: agent -> proxy -> tool executor
agent/api/agent_tool_calls.py                         # POST proposal + POST approval endpoints
cook_bot/handlers/approvals.py                        # aiogram v3 /approvals + /approve + /reject
agent/tests/test_policy_chokepoint.py                 # require_approval never executes unapproved + hash chain verifies
```

One Alembic migration when re-elevated: `CREATE TABLE agent_tool_call` +
`CREATE TABLE agent_tool_call_approval` +
`CREATE TABLE agent_policy_audit_chain` (append-only).
**Zero schema impact on `MenuItem`, `StockEntry`, `Order`, `OrderItem`, `Bill`,
`Payment`, `Visit`, `Shift`.** `agent_policy_audit_chain` is **append-only with
no update/delete code path** (charter §3.1). Zero new pip dependencies for a
Python implementation (`hashlib` is stdlib).

**Hard constraint for any future implementation**: a `policy_decision =
'require_approval'` call MUST NOT execute without a corresponding
`AgentToolCallApproval` row. This is the entire value of the primitive; a
version that logs approvals after execution is worthless.

## Verification protocol

**Today: none.** This is a `defer` artifact; there is nothing to verify. The
protocol below activates only if and when this slice is re-elevated.

1. **Obtain the owner decision on the §3.1 policy-as-input tension.** No
   implementation begins before this exists in Linear.
2. **Read back** `features/351-austinchima-elodea-...md` and confirm it matches
   the daily-research report's Pick B description.
3. **Run the approval-gate test (the critical one):** submit a tool call with
   `policy_decision='require_approval'`; assert the tool executor is **never
   invoked**; assert `executed_at` stays `NULL`; assert no approval row exists.
4. **Run the hash-chain test:** insert N entries, then verify the chain
   end-to-end; then tamper with entry *k* and assert verification **fails**.
5. **Run the append-only test:** attempt `UPDATE` and `DELETE` on
   `agent_policy_audit_chain`; both MUST raise.
6. **Run the proxy-bypass test:** assert there is no code path by which an agent
   reaches a policy-gated tool without passing through `PolicyProxy`. This is the
   structural guarantee and it must be enforced by interface design, not
   convention.
7. **Run the LE31 test suite** and confirm it still passes.
8. **Hand-test on the cook bot**: submit a `require_approval` call, then confirm
   `/approvals` lists it, `/approve <id>` executes it, `/reject <id>` does not.
9. **Observe the actual owner behaviour**: the owner must be able to understand,
   operate, and recover from the approval flow without documentation.

## Rollback path

The artifact is a Markdown file in a git repository.

- **Rollback**: `git revert <commit>` on the commit that added
  `features/351-…md` and `specs/austinchima-elodea-…-HANDOFF.md`. No runtime
  impact to roll back, because nothing was deployed.
- **Feature-removal path** (if re-elevated and later reverted): drop the three
  tables; remove `PolicyProxy` from the agent's call path; remove the
  `/approvals`, `/approve`, `/reject` handlers. **Reverting `PolicyProxy` means
  the agent calls tools directly again — which is exactly the ungoverned state
  this slice exists to prevent.** Record that in the Linear issue before
  reverting; it is a deliberate loss of a safety property, not a neutral revert.
- **Data retained on removal**: the `agent_policy_audit_chain` rows are the only
  durable output. If they are dropped, the approval history is gone permanently.
  **Recommendation: export the chain before any removal.**

## Linear sub-issue

**NOT CREATED.** The Linear MCP write endpoint has been blocked for 32
consecutive days (HTTP 400: *"You've exceeded the free issue limit for this
workspace"*). Read endpoints work; write endpoints do not.

When the block lifts, create the sub-issue as:
- **Project**: `le31 Research` (P-HMM-1) — per `le31-feature-pipeline/SKILL.md`
  line 33, because `le31 v2-AI` **does not exist** in this workspace (only
  `le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1
  exist). Do **not** invent a project.
- **Label**: `Feature`
- **Title**: `Feature 351 — elodea policy-chokepoint vocabulary (defer; §3.1 policy-as-input tension)`
- **Body**: the feature-contract summary + the file path + an explicit callout of
  the §3.1 blocker.

Full pending-issue specification: `/opt/data/le31-daily-research-2026-10-21.linear-fallback.json`.

## Sign-off gap

This package is **incomplete by design**: it records a `defer` decision with an
unresolved charter conflict, not an agreed build. The external agent must NOT
mirror this contract back as an accepted slice. When this slice is
re-elevated, the package must be regenerated with (a) the owner's §3.1 decision
recorded in Linear, (b) a fresh feature-gate verdict, and (c) a real Linear
sub-issue ID.