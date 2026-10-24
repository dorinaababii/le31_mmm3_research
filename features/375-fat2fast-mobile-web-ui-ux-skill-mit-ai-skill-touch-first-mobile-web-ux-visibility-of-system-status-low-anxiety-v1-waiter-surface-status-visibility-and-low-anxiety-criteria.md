# Feature 375 — Waiter-surface "visibility of system status" and "low anxiety" as first-class acceptance criteria (defer)

> **NEW observation (2026-10-24).** Two independent third-party sources converge on the same two dimensions, and LE31 has neither as a stated requirement. (1) GitHub repo `fat2fast/mobile-web-ui-ux-skill` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★0/⑂0**, **6,526 KB**, **JavaScript ✗ OFF-STACK** (an AI agent skill, not an application), created **2026-10-12 AND pushed 2026-10-19 = IN-WINDOW BY BOTH FIELDS**, `archived=false`, `fork=false`, 0 open issues, default_branch=`main`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-24, not from search-result numbers. Description (verbatim from GitHub API): *"AI skill to improve UI/UX for mobile websites, responsive web apps, and PWAs. Helps vibe coders and developers transform existing responsive layouts into intuitive, touch-friendly, mobile-optimized experiences with smarter navigation, usability, and mobile-first UX design."*. (2) OpenAlex work *"Diagnosing Usability Barriers and Conversion Quality Deficits: An Integrated Framework for Web Interface Evaluation"*, published **2026-10-16**, DOI `10.54878/d75ny149`, open-access status `bronze`, in the `htmx OR no-build OR single-page` query result set.
>
> Bucket: **v1 (waiter-surface usability acceptance criteria)** — Pick C of Daily Brainstorm 2026-10-24. Build verdict: `defer` (parking-lot; **vocabulary reference only** — no UI is built, no code changes).

## Goal

Turn **"visibility of system status"** and **"low anxiety"** from implicit hopes into **named, testable acceptance criteria for LE31's waiter surface** — and record the *measurement instrument* that makes them nameable.

The convergence, stated precisely and with the numbers taken from the two raw sources:

| Source | What it says | Why it matters for LE31 |
|---|---|---|
| OpenAlex, *"Diagnosing Usability Barriers and Conversion Quality Deficits"*, 2026-10-16, DOI 10.54878/d75ny149 | Across 50 evaluations of 27 websites, the **weakest** dimensions were **help and documentation (59)**, **visibility of system status (62)**, **clarity (65)** and **low anxiety (67)** — and these four form what the paper calls *"a coherent, literature-consistent profile."* The paper also reports that usability and conversion quality are *"weakly to moderately associated (r = 0.40, r² ≈ 0.16), indicating complementary rather than redundant diagnostic coverage."* | These are the four dimensions a **web app** fails at most often. LE31's waiter surface **is** a web app (§3.1: *"Mobile-responsive web UI for waiters (works on a phone or tablet)"*). The paper says which two of them matter most for an app. |
| `fat2fast/mobile-web-ui-ux-skill` (MIT, ★0) | The skill's stated thesis: *"A website can be responsive and still be frustrating on a phone"* — a desktop sidebar becomes a hard-to-navigate menu, tables are difficult to scan, forms are awkward with the on-screen keyboard, and important actions are easy to miss. It instructs the agent to *"diagnose usability problems **beyond layout and CSS overflow**"* and to *"choose patterns based on user tasks rather than blindly applying bottom navigation, cards, or bottom sheets."* | LE31's waiter surface is a **phone or tablet in a loud, hot, one-handed service situation** (§3.3 lists waiter hardware as an open question). The skill's insistence that *responsive ≠ usable* is the distinction LE31's existing UI contracts never make. |

**No UI is built today. The deliverable is two named acceptance criteria and the instrument that measures them.**

## Scope

**In scope (defer artifact):**

- A written record of the OpenAlex paper's four weakest dimensions and their measured scores, with the DOI, the publication date, the sample size, and the r/r² figure, attached.
- A written record of the `fat2fast` skill's "responsive ≠ usable" distinction and its *"diagnose beyond layout and CSS overflow"* instruction.
- **Two proposed acceptance criteria for the waiter surface**, stated in the form a test could check:
  1. **Visibility of system status** — at every moment, the waiter can tell, without reading text, *whether the last action reached the server*. Concretely: a pending/in-flight indicator, a clear post-confirmation state, and a visible failure state that does **not** silently look like success.
  2. **Low anxiety** — the surface never leaves the waiter guessing whether something went wrong, and never makes them re-check whether an action registered. Concretely: no action that can silently no-op, no ambiguous empty state, no destructive action without a visible undo path.
- A note that the paper's own **methodological caveat** is carried forward honestly: *"the deterministic modeled scoring engine produced all 50 evaluations rather than the AI pipeline, and six repeat audited sites supplied 29 of the 50 evaluations."* **The instrument is a model, not a measurement of LE31.**

**Out of scope (defer artifact):**

- **Any UI, template, CSS, or component change.** This is a criteria document, not a redesign.
- **Adopting the `fat2fast` skill into LE31's agent workflow.** It is an *AI agent skill* for vibe coders; LE31's coding agent has its own `le31-frontend` skill. **The two are not the same thing and this pick does not propose replacing one with the other.** The transferable content is the *vocabulary* ("responsive ≠ usable", "diagnose beyond overflow", "choose patterns based on user tasks").
- **A redesign of the waiter flow.** §3.1 says two surfaces; nothing here adds a third.
- **Any usability study of LE31 itself.** LE31 has no deployed user to study. Adopting a measurement instrument before there is a product to measure is backwards.
- **Accessibility work** beyond the two named criteria (the skill touches `accessib` in its description; the OpenAlex paper scores Nielsen's ten heuristics, one of which is accessibility-adjacent — but **neither source's in-scope material makes an accessibility claim this pick relies on**, and none is asserted here).

## Description

LE31's waiter surface is described in the charter in a single line: *"Mobile-responsive web UI for waiters (works on a phone or tablet)."* **That is a layout requirement, not a usability requirement.** "Mobile-responsive" constrains how the page reflows at a small viewport. It says nothing about whether the waiter, holding the phone in one hand in a loud room, can tell that the order they just sent actually went through.

That gap is not hypothetical, and LE31's own design makes it sharp. §3.2 explicitly defers **real-time WebSocket push** (*"Real-time WebSocket push (waiter UI polls; v2 can add WebSockets)"*). So the waiter surface is, by design, **polling**. A poll-based surface has an inherent ambiguity: between the moment the waiter taps "send" and the moment the next poll returns, the surface has *no new information*. A correct implementation must therefore show something in that gap — a pending state, a spinner, a queued count. **If it shows nothing, the surface is indistinguishable from a failed send.** The waiter will tap again. If the first send eventually succeeds, the order is duplicated.

**This is precisely the "visibility of system status" failure the OpenAlex paper identifies as the second-weakest dimension (62/100) in web applications, and it is exactly the "low anxiety" failure (67/100) that follows from it.** The two dimensions are not two separate problems here — they are one problem seen from two sides: the system knows something the waiter does not, and the waiter's only way to find out is to guess or to re-act.

There is a second, cheaper source in the same direction. The `fat2fast` skill's opening claim — *"A website can be responsive and still be frustrating on a phone"* — and its instruction to diagnose *"beyond layout and CSS overflow"* describe the failure mode where a team has satisfied the layout requirement and believes the usability requirement is thereby met. **LE31's charter sentence is exactly that failure mode, written down as a requirement.**

**The instrument is the more valuable half.** The OpenAlex paper does something LE31's existing UI contracts never do: it puts a **number** on the dimensions, and it establishes that the dimensions are *complementary rather than redundant* (r = 0.40, r² ≈ 0.16) — meaning a surface can score well on usability and badly on conversion quality, and fixing one does not fix the other. For a system whose entire product is "the waiter records the order correctly", that is a useful warning: a waiter UI can be *pleasant* and still *lose orders*.

**The honest caveat, carried forward:** the paper's scores come from a deterministic scoring engine, not from human raters, and 29 of its 50 evaluations came from just six sites. The instrument is a model. **It is adopted as a checklist to think with, not as a benchmark to score against.**

## Data model

None. No table, no column, no endpoint, no template. The criteria are written against LE31's **existing** surfaces and require no data model change: the waiter UI already knows whether its last request succeeded (HTTP status) and whether a request is in flight (client state). The gap is that the surface may not be *showing* it.

## Implementation steps

None. `defer` — parking-lot criteria reference.

**Trigger condition (any one):**

1. Any PR touches a waiter-UI template or the waiter API's request path → these two criteria must be cited in the PR description, and the PR must state which of the two it addresses (or explicitly why neither).
2. The owner answers charter §3.3's open question 4 (*"Waiter hardware — tablet, phone, or laptop?"*) → the answer determines whether the criteria are stated for a phone (one-handed, thumb-reachable, high ambient noise) or a tablet, and the criteria document should be updated to match before any UI work.
3. A future feature introduces a waiter-facing action that can silently fail (a send, a void, a transfer) → **the "visibility of system status" criterion is a precondition for that feature, not a follow-up to it.**

## Telegram interaction if any

None today, and this is a **deliberate asymmetry, not an oversight**: the cook surface is a Telegram bot, which already has an unambiguous delivery model (a message arrives, or it does not) and an existing §4.3 requirement to send a one-shot alert. The waiter surface is a web app, and a web app is the surface where "did that go through?" is genuinely hard. **The criteria apply to the web surface only.** The cook bot's "visibility of system status" is a different and easier problem, already partly specified in §4.3.

## Dependencies

None. No new packages, no schema change, no infrastructure.

## Open questions

1. **Should the two criteria become a required section in the LE31 feature template itself** (so every future UI feature states its status-visibility behaviour)? That is a process change to `le31-feature-pipeline`, not a code change, and it is a cheap and probably-correct adoption. **Unmade owner decision.**
2. **Is "low anxiety" too soft to be a criterion?** It is a *felt* property; the two proposed operationalisations (no silent no-op; visible undo) are checkable, which is what makes the criterion usable. Whether the operationalisation is right is unmade.
3. **What is LE31's actual waiter hardware?** Charter §3.3 question 4, still open, defaults to tablet. The criteria are stated for a phone-or-tablet; the phone case is the harder one and is the one §3.1's "works on a phone or tablet" implies.
4. **Would a no-op action ever be acceptable?** If the answer is ever yes, criterion 2 needs restating, because "no action that can silently no-op" would be false. Not decided.

## Why this matters

Because LE31's charter names the *width* of its waiter UI and says nothing about the *trust* an operator has in it, and the two source families in this pick independently say those are the dimensions web applications fail at most.

The specific risk this pass found: §3.2 defers WebSockets, so the waiter UI polls; a poll-based surface has an unavoidable in-flight window; and **LE31's charter does not say what the waiter sees during that window.** If nothing is shown, then under a flaky kitchen wifi — precisely the environment LE31 targets — a successful order is indistinguishable from a failed one, and the rational response to an indistinguishable state is to tap again. **The failure mode is duplicate orders, and it is a design omission rather than a bug.** No one has to write bad code for it to happen; the code only has to omit one thing.

That is a cheap thing to get right and an expensive thing to discover from a user complaint. The cost of naming the criterion now is two sentences in a feature template. The cost of not naming it is a support ticket that reads "the waiter sent the order twice".

The second reason, and the one that generalises: **the instrument**. LE31 has never had a way to talk about waiter-UI quality other than "make it responsive". The OpenAlex paper supplies both a vocabulary and a set of numbers, and — this is the part worth keeping — an honest statement of its own limits. A criterion that came with a measurement attached is worth more than a principle that came from intuition, because it can be argued with.

## Cross-section

Features 11 (`customer-qr-menu`), 34 (`stockout-prep-board-snapshot` — a wall the cook reads *"in two seconds between tickets"*, the closest thing LE31 has to a glanceability requirement), 45 (`print-fallback-floor-sheet` — a *print* fallback, i.e. LE31's existing answer to "the surface is unavailable"), 65 (`cook-photo-stock-list-pwa`), 67 (`solo-operator-shift-journal-pwa`), 130 (`dhh-kitchen-accessible-operator-ux-visual-replayable` — the closest existing neighbour: a kitchen operator-UX reference), 214 (`ilovepixelart/matador` — no-SPA no-build frontend architecture), 353 (`FreeOpenSourcePOS/FloCafe` — offline-first floor POS), 355 (`Haroon-World/RestaurantPOS` — Android phone + Bluetooth ESC/POS). GitHub `fat2fast/mobile-web-ui-ux-skill` is **unique** vs all 402 pre-existing feature files + 378 HANDOFFs (verified by ripgrep against `features/`, `specs/` and `INDEX.md` for `mobile-web-ui-ux`, `fat2fast` — 0 hits). The OpenAlex work is **not** in LE31's corpus (no `features/` file cites DOI `10.54878/d75ny149`; verified by ripgrep for `d75ny149` and for the title fragment). Fully reversible (vocabulary-only). **Note the honest overlap: feature 130 is an existing operator-UX reference; this pick is not the first to touch operator UX, but it is the first to attach a measurement instrument and a numeric score to the claim.**
