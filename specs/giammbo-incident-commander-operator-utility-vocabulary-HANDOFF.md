# giammbo-incident-commander-operator-utility-vocabulary — HANDOFF

> **Slice for the coding agent — NOT YET ACTIVE.** This artifact is a
> `defer` (parking-lot) vocabulary reference. **Do not implement anything from
> this file today.** Read this *and* `features/350-giammbo-incident-commander-...md`
> before any work begins. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `350`
- Slug: `giammbo-incident-commander-operator-utility-vocabulary`
- Contract file: `features/350-giammbo-incident-commander-apache-2-0-self-hosted-incident-management-one-click-declaration-configurable-lifecycle-timeline-postmortems-fastapi-htmx-python-v2-owner-pains-operator-utility-vocabulary.md`
- Bucket: **v2 owner-pains** — `defer` (parking-lot, vocabulary reference only)
- Source repo: `giammbo/incident-commander` (Apache-2.0, ★5/⑂1, pushed 2026-10-20T13:19:22Z, created 2026-04-30T03:14:02Z)
- Linear parent: `le31 Research` (P-HMM-1)
- Linear sub-issue: **NOT CREATED** — Linear MCP write endpoint blocked (32nd consecutive day). Fallback JSON: `/opt/data/le31-daily-research-2026-10-21.linear-fallback.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed**
(in-window GitHub repo, verbatim description names `one-click declaration`,
`configurable lifecycle & timeline`, `postmortems (auto-generated post-incident review)`, `self-hosted`; 6/6 topics LE31-relevant).

**Confidence:** **medium-high** for the vocabulary match (full LE31 backend-stack
match: Python + FastAPI + HTMX), **low** for present urgency (zero owner mentions
in 82 passes).

**Decision: defer (parking-lot).** No build commitment. No owner has raised an
incident-management need in 82 passes; LE31's charter §3.5 scopes a single
restaurant, not an on-call rotation.

**Checks that would block a `build` today:**
- **Viability (§2)**: the *on-call* / *devops* / *escalation* posture is OFF-§3.5
  (LE31 = single restaurant, two surfaces, one owner). A v1 incident surface
  would need an explicit charter decision, not just a build.
- **Outcome and scope (§5)**: zero v1 demand. This is a v2 owner-pains bucket item.
- **Cost to operational value (§6)**: no pain frequency, no money/time avoided —
  there is no incident to prevent yet.

**Checks that pass:** Practicability (full LE31 stack match, zero new
dependencies), Conflict (Apache-2.0 permissive; §3.4 NOT triggered — no AI
involved at all in this surface), Reversibility (fully reversible,
vocabulary-only).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting (when this slice is ever
re-elevated from `defer` to `experiment` or `build`):

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror the contract back).
4. `le31-daily-research` (this pick came from the daily research job on 2026-10-21).
5. `le31-feature-pipeline` (how this slice will be sequenced once re-elevated).
6. `le31-research` (for the cross-section evidence base).

If the destination repo does not yet ship these skills, request them from the
research-side Hermes instance before writing code.

## Files the slice would touch (NOT NOW — reference only)

```
features/350-giammbo-incident-commander-...md          # NEW (this contract)
specs/giammbo-incident-commander-operator-utility-vocabulary-HANDOFF.md   # NEW (this file)
INDEX.md                                              # EDIT: one row in "Active feature pipeline" (added 2026-10-21)
# --- the following exist only as a design sketch; DO NOT CREATE until re-elevated ---
agent/models/incident.py                              # Incident + IncidentTransition SQLModel tables
agent/models/incident_lifecycle.py                    # data-driven lifecycle definition loader
agent/api/incidents.py                                # POST /api/incidents (one-click) + POST transitions
agent/views/incident_views.py                         # incident_timeline + incident_postmortem SQL views
templates/incident.html                               # minimal-HTML/HTMX declaration + timeline + postmortem export
cook_bot/handlers/incident.py                         # aiogram v3 /incident + /stage + /timeline
agent/tests/test_incident.py                          # append-only invariant + one-click declaration tests
```

One Alembic migration when re-elevated: `CREATE TABLE incident` +
`CREATE TABLE incident_transition` (append-only, no update/delete paths).
**Zero schema impact on `MenuItem`, `StockEntry`, `Order`, `OrderItem`, `Bill`,
`Payment`, `Visit`, `Shift`.** `incident_timeline` and `incident_postmortem` are
**SQL views, not tables** (charter §3.1: derived state is never persisted).
Zero new pip dependencies.

## Verification protocol

**Today: none.** This is a `defer` artifact; there is nothing to verify. The
protocol below activates only if and when this slice is re-elevated.

1. **Re-run the seven-check gate** before any implementation. Confirm nothing in
   the owner's stated priorities has changed the demand picture.
2. **Read back** `features/350-giammbo-incident-commander-...md` and confirm it
   matches the daily-research report's Pick A description.
3. **Run the append-only invariant test**: attempt to `UPDATE` and `DELETE` a
   row in `incident_transition`; both MUST raise. This is the charter §3.1
   invariant and the whole reason the timeline is a view.
4. **Run the derivation test**: `incident_timeline` and `incident_postmortem`
   MUST reflect a transition inserted directly into `incident_transition` with no
   other code path. If they do not, they are incorrectly cached.
5. **Run the one-click test**: `/incident <reason>` on the cook bot MUST create
   exactly one `incident` row and zero `incident_transition` rows (declaration is
   not a transition).
6. **Run the explicit-transition test**: the bot MUST refuse to advance a stage
   that is not the next valid stage in the configured lifecycle.
7. **Run the LE31 test suite** and confirm it still passes.
8. **Hand-test on the cook bot**: trigger `/incident`, `/stage`, `/timeline` in a
   test chat; verify each reply renders within the 4096-char Telegram limit.
9. **Observe the actual waiter/cook/owner behaviour** that changed — per
   `le31-conventions`, "tests pass" is not the same as "the user completed the
   flow on the intended surface".

## Rollback path

The artifact is a Markdown file in a git repository.

- **Rollback**: `git revert <commit>` on the commit that added
  `features/350-…md` and `specs/giammbo-incident-commander-…-HANDOFF.md`.
  There is no runtime impact to roll back, because nothing was deployed.
- **Feature-removal path** (if re-elevated and later reverted): drop the two
  tables (`DROP TABLE incident_transition; DROP TABLE incident;`) and the two
  views; remove the `/incident`, `/stage`, `/timeline` bot handlers; remove the
  `incident.html` template. **No LE31 business data is lost** — incident rows
  are operational metadata, not stock, money, or order records.
- **Data retained on removal**: none required. Nothing in `MenuItem`,
  `StockEntry`, `Order`, `OrderItem`, `Bill`, `Payment`, `Visit`, or `Shift`
  references `incident`.

## Linear sub-issue

**NOT CREATED.** The Linear MCP write endpoint has been blocked for 32
consecutive days (HTTP 400: *"You've exceeded the free issue limit for this
workspace"*). Read endpoints work; write endpoints do not.

When the block lifts, create the sub-issue as:
- **Project**: `le31 Research` (P-HMM-1) — per `le31-feature-pipeline/SKILL.md`
  line 33, because `le31 v2 owner-pains` **does not exist** in this workspace
  (only `le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research`
  P-HMM-1 exist). Do **not** invent a project.
- **Label**: `Feature`
- **Title**: `Feature 350 — incident-commander operator-utility vocabulary (defer)`
- **Body**: the feature-contract summary + the file path.

Full pending-issue specification: `/opt/data/le31-daily-research-2026-10-21.linear-fallback.json`.

## Sign-off gap

This package is **incomplete by design**: it records a `defer` decision, not an
agreed build. The external agent must NOT mirror this contract back as an
accepted slice. When this slice is re-elevated, the package must be regenerated
with (a) a fresh feature-gate verdict, (b) the owner decision that unblocked it,
and (c) a real Linear sub-issue ID.