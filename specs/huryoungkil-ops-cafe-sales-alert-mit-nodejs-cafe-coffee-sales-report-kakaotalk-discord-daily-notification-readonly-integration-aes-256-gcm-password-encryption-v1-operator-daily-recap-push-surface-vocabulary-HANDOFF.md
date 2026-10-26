# huryoungkil-ops-cafe-sales-alert-mit-nodejs-cafe-coffee-sales-report-kakaotalk-discord-daily-notification-readonly-integration-aes-256-gcm-password-encryption-v1-operator-daily-recap-push-surface-vocabulary — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/383-huryoungkil-ops-cafe-sales-alert-mit-nodejs-cafe-coffee-sales-report-kakaotalk-discord-daily-notification-readonly-integration-aes-256-gcm-password-encryption-v1-operator-daily-recap-push-surface-vocabulary.md`
> before touching anything. **This is a WATCH-LIST / COST-AND-SECURITY
> REFERENCE slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise a scheduled job, a notification
> model, a report renderer, a credential store, or a third surface.**
> It proposes **one document** recording a cost figure and a
> credential-handling rule set, and nothing else.

## Frozen identifiers (do not rename)

- Feature ID: `383`
- Slug: `huryoungkil-ops-cafe-sales-alert-mit-nodejs-cafe-coffee-sales-report-kakaotalk-discord-daily-notification-readonly-integration-aes-256-gcm-password-encryption-v1-operator-daily-recap-push-surface-vocabulary`
- Contract file: `features/383-huryoungkil-ops-cafe-sales-alert-mit-nodejs-cafe-coffee-sales-report-kakaotalk-discord-daily-notification-readonly-integration-aes-256-gcm-password-encryption-v1-operator-daily-recap-push-surface-vocabulary.md`
- Bucket: **v1 (operator-recap surface vocabulary)** — defer
- Linear parent: **not created — Linear MCP write endpoint blocked (39th consecutive day), requestId `a50781689b353a4a`** (a separate write probe also failed, requestId `a5076ad3de8335ea`)
- Linear sub-issue: **not created — same blocker**. Intended payload at `/opt/data/le31-daily-research-2026-10-26.linear-fallback.json`
- Source repo: GitHub `huryoungkil-ops/cafe-sales-alert` (MIT), ★0/⑂0, 5,351 KB, Node.js/JavaScript, created 2026-10-25T12:30:10Z, pushed 2026-10-25T13:51:34Z (same-day repo)
- Raw fetch: `/tmp/le31-daily-2026-10-26/pv/huryoungkil-ops__cafe-sales-alert.json`
- README: `/tmp/le31-daily-2026-10-26/rd/huryoungkil-ops_cafe-sales-alert.md`
- Report: `/opt/data/le31-daily-research-2026-10-26.md`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** The artifact exists and is real
(direct `/repos/` GET, HTTP 200, in-window by both `created_at` and
`pushed_at`; README read).

**And it carries the only frequency-quantified operator cost claim in
the 88-pass series:** *"A day takes 3 minutes, so a year takes about
18 hours"* — for an **unattended** venue.

**But that number is not LE31's number.** It is **self-reported by the
author, unvalidated**, and it describes a venue whose only recurring
task is reading one number. **LE31's owner has a richer surface**
(visits, orders, stock) and a correspondingly richer potential recap —
so 18 hours is a **floor-shaped anecdote, not a forecast for LE31.**
It is recorded as `inferred`, not `observed`.

**Confidence: high** for the artifact's existence, licence, size and
content (direct API read; README read; the security rules are quoted
from the repo's own text). **Medium** for the *shape* being
transferable — the push-notification recap surface is a real pattern.
**Low** for the frequency claim's applicability to LE31.

**Decision: defer (vocabulary reference).** Check 1 (JTBD) **fails**:
no LE31 owner has reported pain about a daily recap. Check **5** also
fails — an owner-facing recurring-report surface is a §3.1 surface
question. Check **3** also fails — Node.js/SQLite is off-stack.

**Known rabbit hole:** treating "18 hours a year" as LE31's
opportunity size. **It is not.** The claim is from an unattended
coffee machine; LE31 is a staffed restaurant with two surfaces and a
cooking operation. **The number is quotable as an order-of-magnitude
illustration of how recurring operator chores accumulate, and as
nothing more.**

**Circuit breaker:** if the document is never written and the owner is
never asked, this remains an unused reference. **Acceptable outcome.**
The cost of the artifact is one file.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-10-26 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.
5. `le31-handoff-spec` — the frozen-contract discipline this slice follows.

If the destination repo does not ship these skills, request them
from the project owner before starting. **Do not invent LE31
conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/383-…-v1-operator-daily-recap-push-surface-vocabulary.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No scheduled job is written. No notification model is added.
No report renderer is written. No credential store is written. No
KakaoTalk or Discord integration is written.**

## What the coding agent must NOT do

- **Do not add a scheduled job, a cron entry, a scheduler, or a
  background worker** of any kind.
- **Do not add a notification, delivery, report, or schedule model.**
- **Do not add a credential, secret, or vendor-account model.** LE31
  has **no third-party vendor system to connect to.** A credential
  table for a system that does not exist is a schema change with no
  referent.
- **Do not port or vendor the Node.js implementation.** MIT makes it
  legally adoptable; adopting it would be a §3.2 stack change
  (Node.js + SQLite inside a Python 3.13 / FastAPI / SQLModel / Postgres
  product) requiring an explicit charter decision.
- **Do not add a KakaoTalk, Discord, or any other chat integration.**
  LE31's chat surface is Telegram.
- **Do not build an SVG→PNG renderer, a charting path, or a headless
  browser.** LE31 has no such toolchain. The transferable idea is
  *"the recap is a picture, not a wall of text"* — a rendering
  decision for whichever surface eventually ships it, **not decided
  here.**
- **Do not add a third surface.** §3.1 names two: the waiter web UI and
  the cook Telegram bot. An owner-facing recap surface is a §3.1
  surface-count question. **`features/39-owner-daily-recap-telegram.md`
  already proposes putting the recap on the *existing* bot** — reuse
  it; do not create a parallel one.
- **Do not re-open or rewrite `features/39-owner-daily-recap-telegram.md`.**
  This artifact is **evidence for** it, not a replacement for it.
- **Do not add a stock valuation, cost, or margin surface.** §3.3
  forbids it. "Yesterday's sales" is a turnover figure LE31 already has
  via `Bill`/`DerivedTip` — **no cost or margin is in scope.**
- **Do not add a scheduled push without defining what happens when
  nobody opens it.** If a push is ever approved, the unanswered-message
  behaviour must be specified first.
- **Do not edit `PROJECT_CHARTER.md` or any skill file.**

## The proposed boundary (the actual deliverable content)

**One document.** It records:

1. **The cost arithmetic**, quoted with its caveat attached every time
   it appears: *"3 minutes a day → ~18 hours a year"*, for an
   unattended venue, self-reported and unvalidated, **not** LE31's
   number.
2. **The credential-handling rule set**, in the repo's own terms:
   - **read-only by construction** — *"there is no code that changes
     menus, prices, or machine settings"*;
   - **encrypted at rest** with AES-256-GCM, **key held apart from the
     database**;
   - **credentials verified by an actual login** before being stored,
     and stored only if they work;
   - **stop on authentication failure** and notify, rather than
     retrying into an account lockout;
   - **rate-limited login attempts** (≤ 6 per person per hour);
   - **no email, phone, or real name collected**;
   - **immediate full deletion** on account closure.
3. **The push-vs-pull question**, stated as an open question with the
   artifact's position (push) and LE31's existing proposal's position
   (pull) recorded side by side.
4. **The image-vs-message question**, recorded with its reason
   (a chart, deltas and a Top-5 table that does not require scrolling),
   and explicitly **not** answered.

**The document must NOT decide anything for the owner.** It supplies a
quotable figure and a quotable rule set.

## Trigger for the next step

- The owner asks "how do I see yesterday's numbers without opening the
  app?" or mentions spending time on daily checks → **this slice is
  the pre-written evidence**, and the 18-hour figure is the first thing
  to put on the table (with its caveat).
- A PR adds a scheduled job, a notification model, or a report
  renderer → **this slice must be read first.**
- A PR proposes a third owner-facing surface → **this slice must be
  read first** to confirm the recap rides the existing bot.
- A PR proposes any third-party integration (payment terminal,
  accounting package, or otherwise) → **this slice's credential rules
  are the standard that integration must meet.**
- The owner confirms the frequency → **the feature gate is re-run from
  scratch** with the owner's words as `reported` evidence, and the
  scope is `features/39-owner-daily-recap-telegram.md`.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/`.

**For this slice (documentation only):**

1. The document exists and carries the caveat **every time** the
   18-hour figure appears.
2. `git diff --stat` shows exactly the added files — **no change under
   `backend/`**, no migration, no new dependency.
3. `grep -rn "schedule\|cron\|apscheduler" --include=*.py backend/`
   returns **no new scheduler** — i.e. **the reference has not leaked
   into the codebase.**
4. The document **does not add a surface**: it references
   `features/39-owner-daily-recap-telegram.md` as the proposal it
   supports, and does not propose a parallel one.
5. The document presents the credential rules as **rules**, and does
   not introduce a credential model or a vendor integration.

**If the gate is ever re-run and a build is approved**, the acceptance
path is: the owner receives the recap **without having asked for it**,
at the configured time, and the underlying figures it shows can be
checked against LE31's own `Bill`/`DerivedTip` rows. **A rendered card
that appears is not acceptance** — the figures must be traceable.

## Rollback path

**Delete one file.** The slice adds no migration, no schema change, no
model, no scheduled job and no runtime behaviour, so the rollback is
`rm` on the document plus the feature-contract file. **There is no
data to reconcile, nothing to unwind, and no external system to
disconnect.**

**If a future build is ever approved**, the rollback must include:
the scheduler entry removed, the notification model dropped, and —
because any delivered recap is **derived** from `Bill`/`DerivedTip` —
**an explicit statement that no ledger row is deleted or rewritten to
remove a delivered report.** The report is a view; the facts stay.

## Open questions carried into the slice

1. **How long does the LE31 owner actually spend on this?** — the
   load-bearing question. The artifact supplies an 18-hours-per-year
   anecdote from an unattended venue. **Unanswered.**
2. **Push or pull?** — a scheduled delivery the owner never requests,
   or a bot command the owner asks for? **Unresolved.**
3. **Should the recap be an image or a message?** — the artifact
   renders a card; LE31 has no rendering toolchain today.
4. **Should a push notification be recorded at all?** — a delivery is
   a fact about a message, not about the business. Recording it may be
   unnecessary; not recording it may lose the audit trail.
5. **Does an owner-facing recap count against §3.1's two surfaces?**
   — `features/39-owner-daily-recap-telegram.md` keeps it on the
   existing bot, which holds the count at two. **This artifact does
   not reopen that.**
6. **What is LE31's equivalent of "stop polling on auth failure"?** —
   the nearest analogues are a bot token or a payment provider
   failing; the rule would be *stop and tell the owner*, not retry
   into a lockout. **Not specified here.**
