# Feature 384 — `ifedayofakayode/spice-route-restaurant-dashboard`: the customer-facing AI receptionist LE31 declines, written down so the refusal has a citation

> **NEW observation (2026-10-26).** Documents in-window GitHub repo `ifedayofakayode/spice-route-restaurant-dashboard` (**licence: `mit` ✓ §3.2 STRICTLY-COMPATIBLE — the *vocabulary-shape* is the transferable item; the *code-shape* is NOT adopted**), **★0/⑂0 — no traction evidence in either direction**, **250 KB**, `default_branch=main`, `archived=false`, `fork=false`, TypeScript **✗ off-stack**, created **2026-10-20T07:35:07Z AND pushed 2026-10-22T08:40:59Z = IN-WINDOW BY BOTH FIELDS**. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-26, not from search-result numbers. Description (verbatim from GitHub API): *"A restaurant AI calling agent that answers calls, take reservations and orders, and handles customer queries automatically."*
>
> **The README was also read** (parent, 2026-10-26, `/tmp/le31-daily-2026-10-26/rd/ifedayofakayode_spice-route-restaurant-dashboard.md`).
>
> Bucket: **v1 (boundary vocabulary — a refusal, made citable)** — Pick C of Daily Research 2026-10-26. Build verdict: **`defer`** (parking-lot; **vocabulary reference only** — no code changes, no schema change, and **no licence to copy the implementation from**).

## Goal

Retain `ifedayofakayode/spice-route-restaurant-dashboard` as the **complete, well-executed instance of the shape LE31's §3.1 invariant forbids** — so that the refusal has a **citation** rather than only a prohibition.

> **A boundary that is written down is a decision; a boundary that is merely absent is an accident.**

This artifact is the **fifth** external corroboration of an LE31 boundary in this series, and **the first about AI**. The prior four: `kitchen-erp`'s *"Decimal money, append-only facts"* (2026-10-24), `kinv`'s *"without stock-valuation busywork"* (2026-10-24), `mesa-lite`'s no-build-step criterion (2026-10-25), and `dotnet-pos-integration`'s *"a supervisor may accept a risk but cannot change a fact"* (2026-10-26, feature 382).

**The deliverable is one document** stating the boundary in the concrete terms of a real product, so that a future contributor who wants to add a phone-answering agent can be handed a specific answer.

## Scope

**In scope (v1 — documentation only):**
- One document stating **LE31's position on customer-facing AI**, in the concrete terms of the artifact: what the product does, which surface it occupies, and which LE31 invariant it collides with.
- One document recording the **shape's stated business premise** verbatim, so the *strength* of the pull toward this shape is documented and not merely asserted.
- One document recording **where LE31's own AI allowance sits** — the §3.1 carve-out that AI *may* assist owner/staff, with observable evidence and a non-AI fallback — so the refusal is a **boundary**, not a **blanket ban**.

## Out of scope

- **Any code, schema, or migration in LE31.** No voice surface, no telephony, no reservation bot, no call handling, no AI of any kind.
- **Any port or vendor of the TypeScript implementation.** The licence is MIT, so it is *legally* adoptable — **but the stack is Next.js + n8n + Vapi + Airtable, and the shape is a §3.1 invariant violation.** Adoption is not merely discouraged; it is prohibited by the charter.
- **Any third-party AI provider integration** (Vapi, OpenAI, Anthropic, or otherwise) in LE31. **No such integration exists today and none is proposed.**
- **Any AI-generated customer-facing content, in any surface.** This is the broader rule the artifact exists to make concrete.
- **Any reservation or table-booking surface.** LE31's `Visit` model (`models.py:129-140`) records a *seated party*, not a *reservation*. A reservation is a **different fact with a different lifecycle** (a booking is a promise; a visit is an event) — and adding it would be a §3.1/§3.4 question in its own right, **entirely separate from the AI question, and not opened here.**
- **Re-opening `PROJECT_CHARTER.md` §3.1.** The charter says it; this artifact **cites** it. **The charter is not edited.**
- **Any criticism of the artifact.** Its README's premise is well-argued, its scope is honestly declared (*"The demo uses a fictional restaurant, Spice Route Kitchen, and made-up customer data"*), and its engineering is competent. **The artifact is a good product. LE31 declines its shape, not its quality.**

## Description

**What the thing is.** An **AI receptionist named "Alex"** that answers every incoming phone call, checks table availability, takes reservations and food orders, and logs everything; the owner watches the whole day on a dashboard. Stack: **Next.js** (dashboard), **n8n** (automation), **Vapi** (voice), **Airtable** (database). Topics: `['airtable','automation','n8n','nextjs','restaurant','vapi','voice-ai']`.

**Its stated premise is worth quoting in full**, because the strength of the pull is the thing that must be documented:

> *"Restaurants are busiest exactly when nobody has time to answer the phone. Every missed call is a booking or an order that goes to a competitor, and staff who do answer are pulled away from guests in the room."*

**That is a genuinely strong argument, and LE31 does not dispute it.** What LE31 disputes is the *solution class*, not the problem. The README's own benefit table leads with *"No missed calls — the agent answers every call, even at peak hours."*

**Why LE31 declines it.** §3.1 of LE31's conventions states the product invariant:

> *"Product: one small restaurant and two primary operational surfaces—waiter web UI and cook Telegram bot."*

and the AI invariant:

> *"AI: no customer-facing AI. AI may assist owner/staff, with observable evidence and a non-AI fallback."*

**The artifact collides with the AI invariant head-on, and with the product invariant at the surface level:**
- Its customer is the **guest**, not the owner or staff. **The entire value proposition is a guest-facing interaction.** This is not a staff-assistance tool with a customer-facing edge — it *is* a customer-facing AI.
- It adds a **third surface** (voice/telephony) to a product whose invariant names exactly two.
- Its fallback, if the AI is unreachable, is **that the phone rings and nobody answers** — which is precisely the pre-AI state. **LE31's rule requires a non-AI fallback that *preserves the function*; this shape's fallback is *the absence of the function*.** That is the sharpest single way to state the difference, and it is recorded here as the disqualifying detail.

**Where LE31's own AI allowance sits, for contrast.** LE31's §3.1 permits AI that assists **owner or staff**, provided it has **observable evidence** and a **non-AI fallback**. That is a *narrow* carve-out with two required properties, and **it is the exact opposite of the artifact's shape**: the artifact's AI is the product; LE31's permitted AI is an assistant that a human can check and overrule. **An owner-facing anomaly summary produced by a model, shown in the Telegram bot with the underlying ledger rows visible and a manual override, is inside the allowance. An AI that answers a guest's phone call is outside it, and no amount of quality changes that.**

**The artifact's honest scope note is recorded because it is good practice:** *"The demo uses a fictional restaurant, Spice Route Kitchen, and made-up customer data. No real personal information is stored in this repository."* A product that says this about its own demo data has a better data-handling story than most. **That does not move the decision, and it is recorded so that the refusal is not mistaken for a criticism of the author.**

**One adjacency is noted and deliberately not pursued.** The artifact's **restaurant dashboard** (owner sees the whole day: reservations, orders, calls) is a *owner-facing* surface, and **an owner-facing day-view dashboard is not itself forbidden by §3.1** — but it is a **new owner surface**, which is a §3.1 surface-count question, and it would be a *separate* proposal with its own gate. **The AI part is what is refused here. The dashboard part is simply not picked, and is recorded as not-picked rather than being quietly bundled.**

## Data model

**No data model change. This artifact is a document, and it is a document about a shape LE31 does not have.**

For the record, the *shape* being documented, expressed in LE31's terms (**explicitly not proposed as a schema**):

- A **call** is a new kind of *fact* (something that happened, at a time, with a duration and an outcome). LE31 has no such model. `Visit` (`models.py:129-140`) records a seated party; `OrderItem` (`models.py:142-156`) records a line; **neither records a conversation.**
- A **reservation** is a fact about the *future*, and LE31's ledger is a record of things that **already happened**. **A booking is a promise; a `StockEntry` is a fact.** Adding reservations would raise the same "fact vs obligation" distinction that feature 378 (`Leonardo-Dalan/material-request-system`, 2026-10-25) recorded against *requests*: *"in LE31 the order is a RECORD of something that already happened — it creates NO obligation."* **That distinction is already filed; it is not re-litigated here, and no reservation model is proposed.**
- **No AI-response model, no transcript model, no prompt model, and no provider-integration config are created by this artifact.**
- **The only LE31-side fact that would exist is the observation itself** — and this artifact deliberately does not create a place to store it.

## Implementation steps

**There are no implementation steps. The deliverable is one document.**

The steps that *would* apply **if and only if** the owner ever asks for it, and which this artifact explicitly does **not** authorise:

1. **The owner's question arrives in some form.** The most likely form is *"can we stop missing phone calls?"* — which is a **real business problem** and deserves a **real answer**, and **the real answer is not necessarily no.**
2. **The answer starts from the business problem, not from the shape.** If the owner reports missing calls as a pain, the honest first step is a **staff-side** answer (a surface where a human sees missed-call information) rather than an AI that answers them. **That would be a new proposal with its own gate run from scratch.**
3. **Re-run the feature gate from scratch**, with the owner's own words as `reported` evidence. This artifact's evidence class is **`assumed`** — the weakest class on the scale — because **nothing in the window indicates LE31's owner has missed calls.**
4. **If, and only if, customer-facing AI is ever proposed, the proposal must answer the three questions the §3.1 invariant poses:** *what does the guest get when the model is wrong?* · *what is the non-AI fallback, and does it preserve the function or merely restore the absence?* · *what evidence is observable to the owner afterwards?* **A proposal that cannot answer all three fails at check 4 by construction.**
5. **Never, under any name, in v1.** §3.1's AI invariant is not a preference and this artifact does not propose changing it.

## Telegram interaction if any

**None. This artifact has no Telegram component, and the reason is structural rather than accidental.**

LE31's cook surface is a **Telegram bot**. A Telegram bot is a **staff-facing** surface — **the cook and the waiter are the users**, and the bot's inbound messages come from those staff, not from guests. **The artifact's entire value proposition is a guest-facing interaction**, and the two do not overlap.

**The one thing the artifact contributes to the Telegram surface is a negative rule, and it is worth stating because the temptation is real:** LE31's §3.1 carve-out permits AI that assists staff with observable evidence and a non-AI fallback. **A future contributor could point at this artifact and ask why LE31 will not put an AI assistant on the cook bot.** The answer is that **LE31 may** — that is precisely what the carve-out allows — and the bar it must clear is the one in the §3.1 invariant: *observable evidence* and *a non-AI fallback that preserves the function*. **The artifact does not meet that bar for a guest-facing surface, and it is not the model for a staff-facing one either, because its fallback is the absence of the function rather than a degraded version of it.**

**The bot must not become a guest-interaction surface.** A guest-facing AI on the cook bot would be a §3.1 surface expansion *and* an AI-invariant violation in one change.

## Dependencies

- **`le31-conventions`** — the seven-check gate, and the §3.1 product and AI invariants that this artifact documents against.
- **`PROJECT_CHARTER.md` §3.1** — the two-surface rule and the no-customer-facing-AI rule. **This is the load-bearing reference.**
- **`PROJECT_CHARTER.md` §3.4** — explicit operational state transitions; the reasoning that a *promise* and a *fact* are different categories.
- **`features/378-Leonardo-Dalan-material-request-system-...`** — **load it before writing anything about reservations.** It records the *fact-vs-obligation* distinction against requests; a reservation raises the same distinction and **must not be answered twice**.
- **`le31-v1-feature-pattern`** — for the shape of any future contract derived from this artifact.
- **`le31-research`** — for the rule that research evidence is **never an automatic product requirement**. **This artifact is the clearest example in the series: a well-built product, a strong business argument, and a refusal.**
- **No AI provider, no telephony provider, no third-party service.** None is needed for a document, and none is proposed.

## Open questions

1. **Has the LE31 owner ever lost an order because a phone call went unanswered?** — **the question this artifact exists to sharpen.** If yes, the pain is `reported` and the §3.1 invariant is the thing that must be *discussed* (not silently overridden). **Unanswered, and nothing in this window suggests it has been answered.**
2. **What is LE31's non-AI fallback for a staff-facing AI assistant?** — the §3.1 carve-out requires one, and **LE31 has never specified what it looks like.** If the fallback is *"the model is wrong and the cook notices"*, that is **not** a fallback; it is an absence. **This is the single most useful thing this artifact forces into the open, because it applies to LE31's *permitted* AI, not just the forbidden kind.**
3. **What counts as "observable evidence" for an AI-assisted decision?** — the §3.1 carve-out requires it and LE31 has no definition.
4. **Does LE31 want a missed-call surface at all** — a staff-visible list of unanswered calls, with no AI? **That question is legitimate, is NOT the artifact's question, and is deliberately not opened here.**
5. **Is a reservation a fact or an obligation in LE31?** — the distinction is filed (feature 378) but the reservation case is not drawn. **Not decided.**
6. **Would an owner-facing day-view dashboard be a third surface?** — noted as adjacent, not picked, not decided.

## Why this matters

**Because a refusal without a citation is indistinguishable from a refusal that has never been examined — and LE31's AI invariant deserves better than that.**

§3.1's *"no customer-facing AI"* rule is currently one line in a conventions file. It has never been tested against a real, complete, competently-built product that violates it. **This artifact is that test, and LE31 passes it honestly:** the strongest pull toward the shape is an argument LE31 can acknowledge is sound (*"Restaurants are busiest exactly when nobody has time to answer the phone"*) — and LE31 declines the **solution class** anyway, because the invariant is about *who the AI talks to*, and that is not a quality question.

**The artifact also forces LE31 to sharpen its own permitted case, which is the more valuable half.** LE31 *may* use AI to assist staff. That carve-out has two conditions — *observable evidence* and *a non-AI fallback* — and **LE31 has never said what either means.** The artifact demonstrates, by contrast, a shape whose fallback is *"the phone rings and nobody answers"* — **the absence of the function, not a degraded version of it.** That contrast is now on the record, and it is the standard LE31's own permitted AI has to clear. **A rule that has been tested against a counterexample is a rule; a rule that has only ever been read aloud is a wish.**

**And it is filed as `defer` with `assumed` evidence, which is the honest verdict.** There is no evidence anywhere in this window that LE31's owner has missed calls. The artifact documents a **shape**, and shapes are not evidence of need — the same rule this series has applied to every other pick for 88 passes. **The value of this artifact is that it is the first one whose value is entirely in the refusal.** When the next person asks for a phone-answering agent, LE31 will have a specific answer, with a specific example attached, instead of a line in a conventions file that nobody has ever had to defend.
