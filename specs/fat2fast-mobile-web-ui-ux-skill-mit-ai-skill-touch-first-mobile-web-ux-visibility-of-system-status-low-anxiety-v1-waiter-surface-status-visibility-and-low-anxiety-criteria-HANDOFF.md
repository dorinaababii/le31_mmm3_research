# HANDOFF — Feature 375: waiter-surface "visibility of system status" and "low anxiety" criteria

**Upstream sources (two, independent):**

1. GitHub [`fat2fast/mobile-web-ui-ux-skill`](https://github.com/fat2fast/mobile-web-ui-ux-skill) — MIT, ★0/⑂0, 6,526 KB, JavaScript, created 2026-10-12, pushed 2026-10-19 (**in-window by both fields**), `archived=false`, `fork=false`, 0 open issues, default_branch=`main`. All fields read from a direct `GET /repos/` by the parent on 2026-10-24.
2. OpenAlex — *"Diagnosing Usability Barriers and Conversion Quality Deficits: An Integrated Framework for Web Interface Evaluation"*, published 2026-10-16, DOI `10.54878/d75ny149`, OA status `bronze`, from the `htmx OR no-build OR single-page` query result set. Abstract reconstructed **parent-side from the raw `abstract_inverted_index`** in `/tmp/le31-brainstorm-2026-10-24/openalex/03-htmx-or-no-build-or-single-page.json`.

**Full evidence record: `features/375-fat2fast-mobile-web-ui-ux-skill-mit-ai-skill-touch-first-mobile-web-ux-visibility-of-system-status-low-anxiety-v1-waiter-surface-status-visibility-and-low-anxiety-criteria.md`**

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/375-fat2fast-mobile-web-ui-ux-skill-mit-ai-skill-touch-first-mobile-web-ux-visibility-of-system-status-low-anxiety-v1-waiter-surface-status-visibility-and-low-anxiety-criteria.md` — defer/parking-lot (Pick C of Daily Brainstorm 2026-10-24).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL** | No owner pain is reported about the waiter UI. Evidence class **inferred**. **BUT the failure mode is concrete and derived from LE31's own design, not asserted: §3.2 defers WebSockets ("waiter UI polls"), so the surface has an unavoidable in-flight window in which a sent order and a failed order look identical.** A failing check 1 is what makes this a defer — the criterion is named and ready, but nobody has asked for it. |
| 2 | Viability | ✓ | MIT ✓ §3.2 STRICTLY-COMPATIBLE for the GitHub source. The OpenAlex source is an open-access *article*, not code — no licence question for a citation. **Traction caveat: ★0⑂0, 0 open issues; the GitHub artifact is an AI agent skill, not an application, and its README makes no claim of measured effect.** The article's own caveat is carried forward in the contract. |
| 3 | Practicability and confidence | ✓ | The criteria are checkable against LE31's *existing* surfaces and need no data model change: the waiter UI already knows whether its last request succeeded (HTTP status) and whether a request is in flight (client state). Evidence strength: **medium** — the vocabulary and the instrument are external and real; the *application to LE31* is a parent-side inference. |
| 4 | Conflict | ✓ | No invariant is violated. **But adopting the substance WOULD conflict:** the `fat2fast` artifact is an *AI agent skill* for vibe coders, and LE31 already has its own `le31-frontend` skill. **Replacing one with the other is not proposed.** The two proposed acceptance criteria are additive to the existing feature template, not a replacement of it. |
| 5 | Outcome + appetite + scope | ✓ | Maps to the v1 defer outcome. Maximum time worth spending: **30 min documentation**. **Today: 0 build time.** |
| 6 | Cost to operational value | ✓ | The value is naming two dimensions a web app fails at most, with a measurement instrument attached. ~30 min of documentation; no build, no training, no maintenance. |
| 7 | Circuit breaker + reversibility | ✓ | No code; no rollback needed. Revert by `git rm`. |

**Gate verdict: `defer` (parking-lot)** — check 1 fails on evidence class, with a concrete but *unreported* failure mode.

## Bucket

**v1 (waiter-surface usability acceptance criteria)** — Pick C of Daily Brainstorm 2026-10-24. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming. Because the **parent research issue for this pass also failed to create**, the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload, and that is the only project that exists for the write.

## Files to touch

**None today.** Documentation-only.

**The one process change this pick proposes (owner decision, not a code change):**

- `skills/le31-feature-pipeline/SKILL.md` — the feature template could gain a required line for waiter-facing features: *"How does the operator know this action reached the server? What is shown while it is in flight? What is shown if it fails?"* **This is a template change, it affects every future feature contract, and the parent has not decided it. It is recorded as an open question, not proposed as done.**

**If a future UI feature is built, the expected files (for reference — none are in scope today):**

- `backend/app/templates/*.html` (waiter surface) — the pending/in-flight and failure states.
- `backend/app/routers/tables.py` — the waiter API's request path, to confirm the status the UI would surface.
- `tests/test_waiter_surface_*.py` — a test that a failed request does not render as success.

**Do NOT:** add a third surface, add a WebSocket, redesign the waiter flow, or import the `fat2fast` skill into LE31's agent workflow.

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. For this `defer` reference the observable behaviour is **that the two criteria are stated in a form a test could check, and that the instrument is cited with its own caveat attached** — a reader must be able to tell the difference between "the paper measured this on 27 websites" and "this is a criterion LE31 has adopted".

The **load-bearing verification** for this pick is that the abstract was reconstructed **parent-side from the raw `abstract_inverted_index`**, not taken from any prose summary. It can be re-run:

```bash
python3 - <<'PY'
import json
d=json.load(open('/tmp/le31-brainstorm-2026-10-24/openalex/03-htmx-or-no-build-or-single-page.json'))
for r in d['results']:
    if 'Diagnosing Usability Barriers' in (r.get('title') or ''):
        pos={}
        for w,idxs in (r.get('abstract_inverted_index') or {}).items():
            for i in idxs: pos[i]=w
        print(r['publication_date'], r['doi'])
        print(' '.join(pos[k] for k in sorted(pos))[:1500])
PY
```

**Note: the raw files live under `/tmp/` and are therefore ephemeral.** If this HANDOFF's abstract is ever questioned and `/tmp/le31-brainstorm-2026-10-24/` has been cleared, the DOI `10.54878/d75ny149` is the durable handle. **The parent reconstructed the abstract from the raw index on 2026-10-24; the numbers quoted in the feature contract (59 / 62 / 65 / 67, r = 0.40, r² ≈ 0.16, 50 evaluations across 27 sites, 29 of 50 from six sites) are taken from that reconstruction and should be re-checked against the DOI if anyone relies on them.**

**The fabrication canary for this pick:** `grep -cF 'LE31' /tmp/le31-brainstorm-2026-10-24/openalex/*.json` returns 0 for every file — no third-party source mentions LE31, and the numbers above are LE31's own application of the paper, not quotes from it.

## Rollback path

`git rm features/375-*.md specs/fat2fast-mobile-web-ui-ux-skill-*-HANDOFF.md`. Documentation-only, no migration, no data. Fully reversible.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate
- `le31-frontend` — the existing frontend patterns (**read this before assuming the `fat2fast` skill has anything to add**)
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — §3.1 (the two surfaces), §3.2 (WebSockets deferred → polling), §3.3 question 4 (waiter hardware still open)

## Open questions carried into any future build

1. **Should the two criteria become a required section in the LE31 feature template itself?** That is a process change to `le31-feature-pipeline`, affecting every future contract. Cheap and probably correct. **Unmade owner decision.**
2. **Is "low anxiety" too soft to be a criterion?** It is a *felt* property; the two proposed operationalisations (no silent no-op; visible undo) are checkable, which is what makes it usable. Whether the operationalisation is the right one is unmade.
3. **What is LE31's actual waiter hardware?** Charter §3.3 question 4, still open, defaults to tablet. The phone case is the harder one and is the one §3.1's "works on a phone or tablet" implies. **The criteria should be stated for the actual hardware before any UI work.**
4. **Would a no-op action ever be acceptable?** If yes, criterion 2 ("no action that can silently no-op") needs restating, because it would be false. Not decided.
5. **Should the `fat2fast` skill be read by LE31's coding agent at all?** The parent did not propose it, and `le31-frontend` already exists. **Unmade, and the recommendation is no.**
