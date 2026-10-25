# Feature 377 — Zero-dependency, no-build-step analytics surface vocabulary: `Anatolii198/mesa-lite` (defer)

> **NEW observation (2026-10-25).** A **restaurant analytics dashboard** built in **plain HTML, CSS and vanilla JS** — *"Eight SVG chart types written from scratch — no Chart.js, no frameworks, no build step."* GitHub repo `Anatolii198/mesa-lite` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★0/⑂0**, 255 KB, **JavaScript ✗ OFF-STACK**, created **2026-10-18T10:12:36Z AND pushed 2026-10-23T19:30:22Z = IN-WINDOW BY BOTH FIELDS** (window 2026-10-18..2026-10-24), 10 topics `['admin-dashboard','analytics','charts','dark-mode','dashboard','html-template','no-dependencies','restaurant','svg-charts','vanilla-js']`, `default_branch=main`, `archived=false`, `fork=false`. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-25 (`/tmp/le31-daily-2026-10-25/pv/Anatolii198__mesa-lite.json`), not from search-result numbers. Description (verbatim from GitHub API): *"Restaurant analytics dashboard template in plain HTML, CSS and vanilla JS. Eight SVG chart types written from scratch — no Chart.js, no frameworks, no build step. Dark and light th…"* (description truncated by the GitHub API at 160 characters).
>
> **The in-window cluster this pick sits in.** Three of the 2026-10-25 window's net-new artifacts share one instinct — *ship the whole thing with no dependency tree*: this one (`mesa-lite`, no Chart.js / no frameworks / no build step), `drsamonline/canteen-lan` (feature 376, 39 KB, single-file, LAN-only), and `Leonardo-Dalan/material-request-system` (feature 378, vanilla JS + Firebase, offline-first). A fourth, `CrausalX/fork` (MIT, offline-first cashier PWA, React/Dexie/Supabase), shares the *offline* half but carries a heavy dependency tree and a third-party backend.
>
> Bucket: **v1 (owner-facing analytics surface vocabulary)** — Pick B of Daily Research 2026-10-25. Build verdict: `defer` (parking-lot; **vocabulary reference only** — no UI is built, no code changes).

## Goal

Record **"a small operator-facing dashboard does not need a dependency tree"** as prior art, with a 255 KB, no-Chart.js, no-framework, no-build-step restaurant analytics dashboard as the citation — and keep the observation **separate from the decision to change LE31's stack**, which this pick does not propose.

## Scope

**In scope (defer artifact):**

- A written record of `mesa-lite`'s shape: **plain HTML + CSS + vanilla JS**, **eight SVG chart types written from scratch**, **no Chart.js, no frameworks, no build step**, dark and light themes, 10 topics including `no-dependencies` and `svg-charts`.
- A written record of the in-window cluster that produced it (three artifacts, one instinct).
- **One proposed acceptance criterion** for LE31's *own* existing `index.html` mock-up discipline, stated in a form a test could check:
  > *When an owner-facing view is added to LE31, it must render with no build step and no client-side framework dependency — server-rendered HTML plus hand-written CSS, with charts drawn as inline SVG.*

## Out of scope

- **Any UI, template, CSS, chart, or component change.** This is a criteria document, not a redesign.
- **Adopting `mesa-lite`'s code, template, or chart implementations.** MIT makes it legally adoptable, but it is a **static HTML template with no backend**, and LE31's surfaces are server-rendered by FastAPI with data from Postgres. The transferable content is the *principle*, not the markup.
- **A new owner-facing analytics surface.** LE31 has two surfaces (§3.1: waiter web UI, cook Telegram bot). An owner dashboard is not one of them, and this pick does not propose one.
- **Any stack change.** §3.2 fixes the stack (Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres). LE31's waiter UI is already server-rendered HTML; the *absence of a client-side framework* is arguably already true. **This criterion mostly describes a decision LE31 has already made — the pick's job is to notice that and say so.**
- **Any charting library decision.** If LE31 ever needs a chart, the criterion is "hand-written SVG or a server-side path", not "adopt this repo's SVG code".
## Description

`mesa-lite` is a **restaurant analytics dashboard template** — the kind of artifact a small restaurant's owner or a freelance developer would paste into a static host and point at an export. Its pitch is unusually explicit, and the explicit part is what matters here:

> *"Restaurant analytics dashboard template in plain HTML, CSS and vanilla JS. Eight SVG chart types written from scratch — no Chart.js, no frameworks, no build step. Dark and light th…"*

**Eight chart types, written from scratch, at 255 KB.** For comparison, the chart library it declines to use is roughly the size of the entire rest of the project. The author is making a deliberate economic argument: *the dependency tree is the cost*, and for a single-page dashboard served to a restaurant owner, the tree costs more than the charts do.

**How does this land on LE31?** LE31 is a Python 3.13 / FastAPI / SQLModel / aiogram v3 / Postgres stack with a server-rendered waiter web UI. LE31's existing discipline — an `index.html` mock-up, server-rendered pages, minimal HTML/HTMX — is, **in substance, the same posture**, arrived at from a different direction: HTMX and server-rendered HTML rather than "no framework". **The pick's honest finding is that LE31's existing choice is independently corroborated by an unrelated author choosing the same shape for the same reason.**

**Why the corroboration matters more than the artifact.** LE31's stack decision is a charter decision (§3.2: *"A stack change requires an explicit charter decision"*). Charter decisions that rest only on internal argument are the ones that erode. The prior three passes have produced exactly this kind of external prior art for LE31's *other* implicit boundaries — `"Decimal money, append-only facts, no required outbound calls"` (`kitchen-erp`, 2026-10-24), `"without stock-valuation busywork"` (`kinv`, 2026-10-24), and the LAN-only exclusion (`canteen-lan`, 2026-10-25, feature 376). **This is the fourth, and the first about the *frontend* half of the stack.** A boundary corroborated by an outside party is a boundary that survives a future contributor's "why is it like this?".

**The in-window cluster is the second half of the finding.** One author choosing no dependencies is a preference. **Three authors in one 7-day window choosing no dependencies** — a LAN-only ordering board (single file, 39 KB), a restaurant dashboard (no build step, 255 KB), and a material-request system (vanilla JS + Firebase, offline-first) — is a **coherent engineering economy**, and it is one LE31 does not share. LE31's answer to that economy is "we have a dependency tree and we chose it". **This pick's job is to record that the choice is being made against a live, independently-populated alternative** — which is precisely what makes §3.2's "explicit charter decision" clause meaningful.

**What this pick is NOT.** It is not a proposal to rewrite LE31's UI stack. It is not a claim that HTMX is wrong. It is not a claim that the owner wants a dashboard. It is one recorded observation and one proposed criterion, both reversible, both with trigger conditions.

## Data model

None. No table, no column, no endpoint, no template, no migration.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (any one):**

1. **Any PR adds an owner-facing or waiter-facing view** → the no-build-step criterion must be cited in the PR description, and the PR must state whether the criterion is met or explicitly why not.
2. **Any proposal to introduce a client-side framework** (React, Vue, Svelte, Alpine, a charting library) → the criterion becomes the **pre-built counter-argument**, and the PR must address it explicitly.
3. **Any proposal to add a charting dependency for LE31** → the criterion requires an explicit statement of why hand-written or server-rendered SVG was not sufficient.

## Telegram interaction if any

None, and this is a **deliberate asymmetry, not an oversight**. The cook surface is a **Telegram bot**, whose entire client is Telegram's own client — there is no HTML, no CSS, no chart, and no build step to have. **The criterion applies to LE31's web surface only.** The "no dependency tree" question is a question about the *waiter/owner web UI* and has no analogue on the bot. Stating this asymmetry explicitly prevents the criterion from being misapplied to a surface it cannot describe.

## Dependencies

None. No new packages, no schema change, no infrastructure.

## Open questions

1. **Is this criterion redundant?** LE31's waiter UI is *already* server-rendered HTML with minimal HTMX — so the criterion may describe a decision already made, in which case the pick's value is only "an outside party reached the same conclusion independently". **That is still worth recording, but the owner should decide whether a criterion that restates existing behaviour belongs in the feature template at all.**
2. **Where should the criterion live** — the `le31-frontend` skill, the feature template, or the charter? **Owner decision.**
3. **What about charts specifically?** "No charting library" is a stronger claim than "no framework" (a chart library is a dependency, but frameworks like HTMX are also dependencies, and LE31 already accepts those). The criterion as written says *no client-side framework dependency*, which would arguably exclude HTMX. **The wording needs the owner's input** — this pick proposes a wording and flags it as provisional.
4. **Does the restaurant-operator-dashboard use case ever apply to LE31?** LE31's charter does not currently include an owner-facing reporting surface. The pick assumes it *might* (a "day's takings" view is an obvious v2 candidate) but **that is an assumption, not a finding**, and it is recorded as such.

## Why this matters

**Because LE31's frontend stack decision has so far rested on internal argument alone, and this is the first outside party to corroborate it.**

LE31's §3.2 stack commitment is deliberate and correct. But §3.2 also says a stack change requires an explicit charter decision — and a decision that has never faced an outside alternative is a decision nobody has tested. **This window produced three independent artifacts built the opposite way**, from three unrelated authors, in three different domains (venue ordering, restaurant analytics, factory material requests), all in the same 7 days. **The alternative is not hypothetical; it is being built, concurrently, at a fraction of the size.**

The pick's specific contribution is small and honest: **a 255 KB, eight-hand-written-SVG-chart restaurant dashboard is proof that "no build step" is achievable at a size a single restaurant could host themselves** — which is the size class LE31 actually operates at (one restaurant, one owner, one VPS). LE31's counter-argument is its fixed stack, and that counter-argument stands. **But the argument now has a named, dated, citable counterexample, and that is what makes it durable.**

**Fully reversible (vocabulary-only artifact).** Trigger condition: any PR adding an owner- or waiter-facing view, any proposal to add a client-side framework, or any proposal to add a charting dependency.
