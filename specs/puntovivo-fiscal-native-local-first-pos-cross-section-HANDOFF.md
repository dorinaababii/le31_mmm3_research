# puntovivo-fiscal-native-local-first-pos-cross-section — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/131-puntovivo-fiscal-native-local-first-pos-cross-section.md`
> before touching anything. **This is a WATCH-LIST / PARKING-LOT
> slice, NOT a build slice.** There is no code deliverable.
>
> **This is the weakest of the three picks in the 2026-08-28 pass and
> is filed at its true weight.** 2★, created off-window, stack
> entirely disjoint from LE31, and **no LE31 owner has raised fiscal
> compliance in any of 29 passes.** Do not treat it as equivalent to
> the two paper-backed picks in the same pass.

## Frozen identifiers (do not rename)

- Feature ID: `131`
- Slug: `puntovivo-fiscal-native-local-first-pos-cross-section`
- Contract file: `features/131-puntovivo-fiscal-native-local-first-pos-cross-section.md`
- Bucket: **v2 owner-pains (parking-lot)** — defer
- Linear parent: **HMM-169** (Brainstorm 2026-08-28 — daily)
- Linear sub-issue: **HMM-172** (Feature)
- Source repo: `johnny4young/puntovivo`
- Stats at observation: **2★ / 1 fork, MIT, TypeScript**, created
  **2026-01-30** (off-window), pushed **2026-08-27** (in-window by
  push only)
- Raw fetch: `/tmp/le31-brainstorm-2026-08-28/gh_search_restaurant_language_python_stars_3E1.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: observed, but thin.** The repo exists and its
description and topic list were read verbatim from the raw GitHub
search JSON by the parent agent. **The README was not fetched** —
"fiscal-native" is the author's own claim, not a verified property.

**Confidence: medium** that the repo is what its description says;
**low** for any LE31 relevance; **low** for present urgency.

**Decision: defer (parking-lot).** No check fails, but the pick is
weak on four independent axes and each is recorded rather than
smoothed over:

1. **No demand signal.** 29 passes, zero owner mentions of fiscal
   compliance. 2★ is **not** evidence of demand and is not offered as
   such.
2. **Off-window creation** (2026-01-30, ~7 months before the window).
   In-window by push only.
3. **Stack entirely disjoint.** Electron + React + Fastify + tRPC +
   SQLite vs FastAPI + SQLModel + htmx. MIT permits import; the stack
   forbids it in practice.
4. **Value is contingent and external.** It becomes useful only if a
   legal requirement appears — binary, outside LE31's control, not a
   gradually-maturing need.

**Known rabbit hole:** researching Colombian tax law, or worse,
inferring Swiss obligations from a Colombian implementation. **This
repo is authority on nothing.** If the question ever matters, start
with Swiss law.

**Circuit breaker / hard expiry:** if neither re-evaluation trigger
fires within 90 days (**by 2026-11-26**), retire this artifact.
Contingent-value parking-lot entries must not accumulate indefinitely.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-brainstorm` — this pick came from the 2026-08-28 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.

If the destination repo does not ship these skills, request them from
the project owner before starting. **Do not invent LE31 conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/131-puntovivo-fiscal-native-local-first-pos-cross-section.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written.**

## What the coding agent must NOT do

- **Do not import any code from `puntovivo`.** MIT permits it; the
  stack makes it meaningless. No dependency is proposed.
- **Do not build a fiscal module, receipt model, or e-invoicing
  surface.** No schema change of any kind.
- **Do not assume anything about Swiss fiscal or receipt-retention
  law.** It has **not** been verified. Flag the question; do not
  answer it.
- **Do not build an Electron or desktop surface for LE31.** That
  question belongs to feature 119's cross-platform consideration, not
  here.
- **Do not present 2★ as evidence of demand.**
- **Do not inflate this pick to match features 129 and 130.** They are
  paper-backed; this is a repo description.

## The durable content (two observations, and that is all)

1. **Three independent local-first POS/back-office projects surfaced
   in three consecutive days** — `Ritchalison/BalanceDesk`
   (2026-08-26, feature 119), `MehfoozurRehman/restopilot-command`
   (2026-08-27, logged under 119), and `johnny4young/puntovivo`
   (2026-08-28, this one). **All three are desktop-shaped — the
   opposite of LE31's server + Telegram + htmx posture.** The trend is
   interesting as a *divergent-approach* observation, not as something
   to copy. **The trend is the signal; the repo is the data point.**
   Three points is also not a trend with confidence — worth watching,
   not worth concluding.

2. **If a statutory record-immutability requirement ever reaches LE31,
   charter §3.1's append-only `StockEntry` + `audit_logs`-per-mutation
   discipline is already most of the answer.** LE31 would be well
   positioned rather than exposed. That is a useful fact about a
   decision already made, and it is cheap to have written down.

The only new dimension puntovivo adds over the two prior data points
is **statutory fiscal compliance as a first-class data-model concern**
(`dian` = Colombia's national tax authority, plus
`electronic-invoicing` and the phrase "fiscal-native"). Everything
else about it — local-first, offline-first, SQLite-in-a-folder,
small-business retail — is already recorded elsewhere.

## Watch-list instructions

- Daily `GET https://api.github.com/repos/johnny4young/puntovivo` via
  `$HERMES_GITHUB_TOKEN`. Track stars, forks, `pushed_at`.
- **Re-evaluation triggers** (either one):
  - the repo crosses **≥10★**, or
  - **any** owner conversation touches receipts, tax filing, or
    statutory record retention.
- **The second trigger is the only one that actually matters.** Star
  growth on a 2★ hobby repo tells LE31 nothing about whether a Swiss
  restaurant has a receipt-retention obligation.

## Trigger for the next step

When an owner conversation touches receipts, tax, or record retention:

1. **Establish what Swiss law requires. Start there, not here.** This
   repo is a Colombian implementation of Colombian rules.
2. Then check whether LE31's existing append-only model already
   satisfies it. **It plausibly does** — see durable observation 2.
3. Only then consider whether any new modelling is needed.
4. Run `le31-conventions` on that feature independently. This artifact
   pre-authorises nothing.

## Search-hygiene note for future passes

This **TypeScript** repo surfaced under a `language:python` query.
GitHub matched repository text rather than honouring the filter's
intent. **The `language:` qualifier does not guarantee the language of
returned repos** — future passes must check the `language` field on
each result rather than trusting the query.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/131-puntovivo-fiscal-native-local-first-pos-cross-section.md`
      exists and was read back.
- [ ] Stars (2), forks (1), licence (MIT), language (TypeScript),
      `created_at` (2026-01-30), `pushed_at` (2026-08-27) and the full
      topic list match the raw JSON at
      `/tmp/le31-brainstorm-2026-08-28/gh_search_restaurant_language_python_stars_3E1.json`.
- [ ] The description is quoted **verbatim** from the raw JSON.
- [ ] The contract states plainly that creation is **off-window** and
      that in-window status is **by push only**.
- [ ] The contract states plainly that **no owner has raised fiscal
      compliance** and that **Swiss requirements are unverified**.
- [ ] The 90-day expiry date (**2026-11-26**) is recorded.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-172 exists with label `Feature` and parent HMM-169.
- [ ] No source file, schema, or test was modified. **No puntovivo
      code exists anywhere in the repo.**

## Rollback path

Delete
`features/131-puntovivo-fiscal-native-local-first-pos-cross-section.md`,
delete
`specs/puntovivo-fiscal-native-local-first-pos-cross-section-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-172.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- **Does Switzerland impose a receipt-retention or record-immutability
  obligation on a restaurant of LE31's size?** Unverified. The whole
  artifact hinges on this and it has not been asked.
- Has any LE31 owner ever raised fiscal compliance? **No — not in 29
  passes.** Strongest argument the pick is premature.
- Is "fiscal-native" a real architectural property or repo-description
  marketing? **Unknown; README not fetched.**
- Is the three-repo local-first-desktop pattern meaningful, or three
  unrelated hobby projects in a popular template stack? **Not
  concludable from three points.**
