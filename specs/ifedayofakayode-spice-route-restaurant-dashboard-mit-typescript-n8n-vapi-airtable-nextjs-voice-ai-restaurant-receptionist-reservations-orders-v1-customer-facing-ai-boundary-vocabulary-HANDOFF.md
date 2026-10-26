# ifedayofakayode-spice-route-restaurant-dashboard-mit-typescript-n8n-vapi-airtable-nextjs-voice-ai-restaurant-receptionist-reservations-orders-v1-customer-facing-ai-boundary-vocabulary — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/384-ifedayofakayode-spice-route-restaurant-dashboard-mit-typescript-n8n-vapi-airtable-nextjs-voice-ai-restaurant-receptionist-reservations-orders-v1-customer-facing-ai-boundary-vocabulary.md`
> before touching anything. **This is a WATCH-LIST / BOUNDARY
> REFERENCE slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise an AI feature, a voice surface, a
> telephony integration, a reservation model, or a third surface.** It
> proposes **one document** recording a refusal with a citation, and
> nothing else.

## Frozen identifiers (do not rename)

- Feature ID: `384`
- Slug: `ifedayofakayode-spice-route-restaurant-dashboard-mit-typescript-n8n-vapi-airtable-nextjs-voice-ai-restaurant-receptionist-reservations-orders-v1-customer-facing-ai-boundary-vocabulary`
- Contract file: `features/384-ifedayofakayode-spice-route-restaurant-dashboard-mit-typescript-n8n-vapi-airtable-nextjs-voice-ai-restaurant-receptionist-reservations-orders-v1-customer-facing-ai-boundary-vocabulary.md`
- Bucket: **v1 (boundary vocabulary — a refusal, made citable)** — defer
- Linear parent: **not created — Linear MCP write endpoint blocked (39th consecutive day), requestId `a50781689b353a4a`** (a separate write probe also failed, requestId `a5076ad3de8335ea`)
- Linear sub-issue: **not created — same blocker**. Intended payload at `/opt/data/le31-daily-research-2026-10-26.linear-fallback.json`
- Source repo: GitHub `ifedayofakayode/spice-route-restaurant-dashboard` (MIT), ★0/⑂0, 250 KB, TypeScript, created 2026-10-20T07:35:07Z, pushed 2026-10-22T08:40:59Z
- Raw fetch: `/tmp/le31-daily-2026-10-26/pv/ifedayofakayode__spice-route-restaurant-dashboard.json`
- README: `/tmp/le31-daily-2026-10-26/rd/ifedayofakayode_spice-route-restaurant-dashboard.md`
- Report: `/opt/data/le31-daily-research-2026-10-26.md`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: assumed — the weakest class on the scale.**
The artifact exists and is real (direct `/repos/` GET, HTTP 200,
in-window by both `created_at` and `pushed_at`; README read).

**But there is no reported pain at all.** Nothing in this window
indicates LE31's owner has missed calls, lost orders to unanswered
phones, or asked for any AI feature. The artifact's business premise
is **strong and plausible** (*"Restaurants are busiest exactly when
nobody has time to answer the phone"*) — **and a plausible premise
about a different product is not a pain report for LE31.**

**Confidence: high** for the artifact's existence, licence, size and
content. **None** for LE31-side demand — **no market claim is made in
either direction.**

**Decision: defer (vocabulary reference).** Check 1 (JTBD) **fails**
on `assumed` evidence. **Check 4 (conflict) fails outright and is
disqualifying on its own:** the artifact is a **customer-facing AI**
(a voice agent answering guests' calls), and §3.1 states *"AI: no
customer-facing AI. AI may assist owner/staff, with observable evidence
and a non-AI fallback."* It also adds a **third surface** (voice) to a
product whose invariant names exactly two.

**Known rabbit hole:** treating this artifact's strength as a reason to
build it. **The artifact is a good product with a sound argument, and
LE31 declines its shape, not its quality.** The other rabbit hole is
the mirror image: treating the refusal as settled and never
re-examining it. **It is settled by §3.1, and §3.1 is a charter
decision — not a preference this slice is entitled to defend on its
own.**

**Circuit breaker:** if the document is never written, this remains an
unused reference. **Acceptable outcome.** The cost of the artifact is
one file.

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
| `features/384-…-v1-customer-facing-ai-boundary-vocabulary.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No model is changed. No AI provider is integrated. No voice or
telephony code is written. No reservation model is added. No third
surface is built.**

## What the coding agent must NOT do

- **Do not build the AI receptionist**, in any form. Not a voice
  agent, not a chat agent, not a "simple" version, not a v2
  placeholder.
- **Do not integrate any AI provider** — Vapi, OpenAI, Anthropic, or
  otherwise — for any purpose. **LE31 has none today and none is
  proposed.**
- **Do not add a voice, telephony, call-recording, or transcription
  surface.**
- **Do not add a guest-facing surface of any kind.** §3.1 names two
  surfaces: the waiter web UI and the cook Telegram bot. Both are
  staff-facing.
- **Do not add a reservation or booking model.** A reservation is a
  **promise about the future**, not a record of something that already
  happened — the same *fact-vs-obligation* distinction already filed
  as feature 378. **Load feature 378 before writing anything about
  reservations, and do not answer that question a second time here.**
- **Do not port or vendor the TypeScript implementation.** MIT makes it
  legally adoptable; the shape is a §3.1 invariant violation, so
  adoption is **prohibited by the charter**, not merely discouraged.
- **Do not build the owner-facing day-view dashboard as part of this
  slice.** It is **adjacent**, not forbidden: an owner-facing view is
  a §3.1 surface-count question and would be a **separate proposal
  with its own gate**. It is recorded as *not picked*, not bundled.
- **Do not add an "AI assistant on the cook bot"** on the strength of
  this artifact. LE31 **may** do that under §3.1's carve-out — but the
  bar is *observable evidence* and *a non-AI fallback that preserves
  the function*, and **this artifact does not meet that bar** (its
  fallback is the absence of the function). **A separate, properly
  gated proposal is required.**
- **Do not edit `PROJECT_CHARTER.md`, `le31-conventions`, or any skill
  file.** The artifact **cites** §3.1; it does not **change** it.
- **Do not add a money, cost, or valuation surface.** §3.3 forbids it.

## The proposed boundary (the actual deliverable content)

**One document.** It records:

1. **What the artifact does**, concretely: an AI receptionist that
   answers every incoming call, checks table availability, takes
   reservations and orders, and logs everything; the owner sees the
   day on a dashboard. Stack: Next.js + n8n + Vapi + Airtable.
2. **Its stated premise, quoted in full** — *"Restaurants are busiest
   exactly when nobody has time to answer the phone. Every missed call
   is a booking or an order that goes to a competitor, and staff who do
   answer are pulled away from guests in the room."* — **so the pull
   toward the shape is documented, not dismissed.**
3. **The collision, stated in LE31's terms:** the artifact's customer
   is the **guest**; its fallback is *"the phone rings and nobody
   answers"*, which is the **absence of the function, not a degraded
   version of it** — and that is the disqualifying detail against
   §3.1's requirement of *a non-AI fallback*.
4. **Where LE31's own AI allowance sits**, as the contrast: AI that
   assists **owner or staff**, with **observable evidence** and a
   **non-AI fallback**. **The document must state plainly that LE31
   does not define either of those two terms today** — because that
   gap applies to LE31's *permitted* AI, not only to the forbidden
   kind, and it is the more useful half of this artifact.
5. **The three questions any future customer-facing-AI proposal must
   answer**: *what does the guest get when the model is wrong?* · *what
   is the non-AI fallback, and does it preserve the function or merely
   restore the absence?* · *what evidence is observable to the owner
   afterwards?* **A proposal that cannot answer all three fails at
   check 4 by construction.**

## Trigger for the next step

- The owner reports **missed calls**, lost orders, or asks *"can we
  stop missing phone calls?"* → **this slice is the pre-written
  answer** — and the correct response is to start from the **business
  problem** (a staff-side missed-call visibility surface is not
  forbidden), **not** from this artifact's AI shape.
- A PR adds an AI model call, a voice integration, a telephony
  provider, or any guest-facing surface → **this slice must be read
  first.**
- A PR adds an AI assistant on the cook bot or in the waiter UI →
  **this slice must be read first**, because §3.1's *observable
  evidence* and *non-AI fallback* conditions apply and are **not
  defined anywhere in LE31 today.**
- A PR adds a reservation or booking concept → **feature 378 must be
  read first** to avoid answering the fact-vs-obligation question
  twice.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/`.

**For this slice (documentation only):**

1. The document exists and states the refusal **with the artifact's
   premise quoted**, so it does not read as a dismissal.
2. `git diff --stat` shows exactly the added files — **no change under
   `backend/`**, no migration, no new dependency.
3. `grep -rniE "openai|anthropic|vapi|whisper|speech|transcri" --include=*.py backend/`
   returns **no new AI or voice integration** — i.e. **the reference
   has not leaked into the codebase.**
4. The document **does not bundle the owner dashboard** with the AI
   refusal, and does not propose a reservation model.
5. The document **states the gap in LE31's own permitted AI case**
   (undefined *observable evidence*, undefined *non-AI fallback*) —
   because that gap applies to LE31's allowed use of AI, not only to
   the forbidden kind.

**If the gate is ever re-run and a build is approved** — and it must
be, from scratch, with `reported` evidence — the acceptance path for
LE31's *permitted* AI case is: a human staff member sees the
model's output **together with the underlying facts**, can overrule
it, and can still complete the task with the model disabled. **A
model output that appears is not acceptance.**

## Rollback path

**Delete one file.** The slice adds no migration, no schema change, no
model, no integration and no runtime behaviour, so the rollback is
`rm` on the document plus the feature-contract file. **There is no
data to reconcile, nothing to unwind, and no provider account to
disconnect.**

**If a future build is ever approved**, the rollback must include:
the AI provider integration removed, the credential removed, the
model-dependent code path deleted **entirely rather than disabled by a
flag**, and — because a delivered AI output may have been acted on —
**an explicit statement of what happens to the ledger rows that were
written on the strength of an AI-assisted decision.** §3.3's
append-only rule means such rows are **never rewritten**; if they are
wrong, they are corrected by a compensating entry.

## Open questions carried into the slice

1. **Has the LE31 owner ever lost an order because a phone call went
   unanswered?** — the question this artifact exists to sharpen. **If
   yes, the pain is `reported` and §3.1 is the thing that must be
   *discussed* (not silently overridden).** Unanswered.
2. **What is LE31's non-AI fallback for a staff-facing AI assistant?**
   — §3.1's carve-out requires one and **LE31 has never specified
   what it looks like.** If the fallback is *"the model is wrong and
   the cook notices"*, that is **not** a fallback; it is an absence.
   **This is the most useful thing this artifact forces into the open,
   because it applies to LE31's permitted AI.**
3. **What counts as "observable evidence" for an AI-assisted
   decision?** — required by §3.1, undefined in LE31.
4. **Does LE31 want a missed-call surface at all** — a staff-visible
   list of unanswered calls, with **no AI**? **That question is
   legitimate, is not the artifact's question, and is deliberately not
   opened here.**
5. **Is a reservation a fact or an obligation in LE31?** — the
   distinction is filed (feature 378); the reservation case is not
   drawn. **Not decided.**
6. **Would an owner-facing day-view dashboard be a third surface?**
   — noted as adjacent, not picked, not decided.
