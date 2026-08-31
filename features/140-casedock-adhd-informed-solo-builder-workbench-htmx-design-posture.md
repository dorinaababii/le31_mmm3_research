# Feature 140 — casedock ADHD-informed solo-builder workbench htmx design posture (defer, parking-lot)

> **NEW observation (2026-08-30).** Documents in-window GitHub repo `gerpaick/casedock` (Apache-2.0, 2★, 6.6 MB, Python Django 6 + HTMX, **pushed today 2026-08-30T06:25:10Z**) from the 2026-08-30 daily-brainstorm pass. The repo is a *"Calm workbench for solo technical builders — ADHD-informed design"* with explicit design principles: *"Remove decisions instead of adding them; the first thing you see is an action, not information"*, *"No red badges, overdue indicators, or streaks"*, *"No time estimation, no gamification"*, *"The board never shows more than ~7–10 active cases without folding"*. Bucket: **v2 operator-UX (parking-lot)** — defer. Zero build time today.

## Goal

Retain the **casedock design posture** ("remove decisions instead of adding them") as the **operator-UX cross-section reference** for the first LE31 v2 surface where the solo owner is asked to triage, focus, or review — i.e., the surface that gives the owner a bounded working object (a **Case**: spec, decisions, execution items, private notes, source links) instead of an unbounded feed.

The artifact is the persistent design reference. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the casedock design principles (the README's "Design principles" section).
- A written record of the casedock core loop: **Capture → Triage (decided once: do now / convert to Case / set aside / waiting / archive) → Case (bounded working object) → Focus (1 main + 2 secondary per day)**.
- A decision record: today's verdict is `defer (parking-lot)` because LE31 v1 has no v2 surface where the owner is asked to triage or focus; the value of casedock today is *design posture*, not *implementation*.
- A reference for the next time LE31 proposes a v2 surface for owner-facing review/recap.

**Out of scope (defer artifact):**
- Any code dependency on casedock (it is Django 6, not FastAPI).
- Any adoption of the case-as-bounded-working-object primitive (LE31 v1 has `StockEntry` + `audit_logs`, not Cases).
- Any change to the Telegram cook-bot surface (which is hands-busy, phone-first, not a workbench).
- Any implementation of "decide once" semantics — LE31 v1 already has explicit state transitions, but the "decided items leave your head" framing is a v2 UX consideration.

## Description

GitHub `gerpaick/casedock` (Apache-2.0, 2★, 6.6 MB, Python Django 6 + HTMX, **pushed today 2026-08-30T06:25:10Z**) is described in its README as a *"personal execution layer for overloaded developers"*. The core loop:

1. **Capture** — one field, zero required fields. Global `c` shortcut from any page.
2. **Triage** — every item gets decided once: *do now / convert to Case / set aside / waiting / archive*. Decided items leave your head.
3. **Case** — a bounded working object: spec, decisions, execution items, private notes, source links. Understandable in isolation, weeks later.
4. **Focus** — 1 main + 2 secondary per day. The board surfaces the first unchecked execution item as the "just start" prompt.

The README's "Design principles" section explicitly states:

> *"casedock is ADHD-informed by design — evidence-based, not gamified:*
> *- Remove decisions instead of adding them; the first thing you see is an action, not information*
> *- No red badges, overdue indicators, or streaks — stale work is marked neutrally*
> *- No time estimation, no gamification, no "you haven't logged in" nags*
> *- The board never shows more than ~7–10 active cases without folding"*

**Cross-section with LE31**:

- **The design principle *"remove decisions instead of adding them; the first thing you see is an action, not information"* is a direct cross-section with LE31's solo-owner operator philosophy** (charter §3.4.4 "the non-technical owner") and **feature 130 DHH-restaurant paper finding #1** ("workstation prompts + self-paced rehearsal"). All three sources converge on the same lesson: the right surface for an operator is *one action*, not *a menu of options*.
- **The bounded-working-object primitive (a Case has spec, decisions, execution items, private notes, source links — "understandable in isolation, weeks later") is the *dual* of feature 134 ECHO's auditable memory plane** (2026-08-29): ECHO argues *replace* chat history with structured records ("understandable in isolation, weeks later" is ECHO's verbal mirror of casedock's Case).
- **The "decided items leave your head" principle** is the *explicit-state-transition* posture: every item gets decided once. This is exactly charter §3.1's "operational transitions are explicit user actions" — but casedock extends it to the **decision layer** (triage), not just the operational layer (StockEntry).
- **The "1 main + 2 secondary per day" focus principle** is the *explicit-bound* posture: the board never shows more than ~7–10 active cases. This is the same shape as LE31 v1's single-cook-channel design — one cook, one bot, one focused surface.

**Stack mismatch**: casedock is **Django 6 + HTMX**, not FastAPI + SQLModel. The **Apache-2.0 licence** permits adoption of design ideas, not code. The transferable item is the design posture, not the implementation.

**Sibling cross-section with feature 84 Reckon low-effort decision-journal watch** (2026-08-19):
- Feature 84 = `Reckon` (ProductHunt main feed 2026-08-06 — *"decision journal that helps you calibrate"*). Solo-builder micro-SaaS in the low-effort UX lane. **No public repo, no code.**
- Feature 140 = `casedock` (GitHub, 2026-08-30). Solo-builder workbench in the low-effort UX lane. **Real code (6.6 MB), Apache-2.0, pushed today.**
- Both share the "low-effort UX for solo operators" theme, but the **technical primitive** is different: casedock ships **code** (specifically the **case-as-bounded-working-object** primitive + the "decide once" invariant), Reckon is a PH launch without a public repo.
- **They are complementary, not duplicates.** Feature 84 validates the JTBD pull (low-effort UX + personal calibration); feature 140 surfaces the implementation primitive (Case + Decide Once).

## Data model

No schema change today. The defer artifact documents that the future v2 surface that adopts the casedock posture would:

- Introduce a **Case** entity (analogous to `StockEntry` but for the decision layer) with fields: `spec`, `decisions`, `execution_items`, `private_notes`, `source_links`.
- Introduce a **Triage** state machine: `do_now / convert_to_case / set_aside / waiting / archive` — each item gets decided exactly once.
- Adopt the "decided items leave your head" principle: triage-decided items do not appear again.

**Out of scope**: any adoption of casedock's Django + HTMX stack.

## Implementation steps

None today (defer). When LE31 first proposes a v2 surface where the solo owner is asked to triage, focus, or review:

1. **Re-run the LE31 feature gate** with this paper in hand.
2. **Decide whether the surface is a workbench** (casedock-style) **or a recap feed** (LE31 v1 owner-recap style). The two have different shapes: workbench = bounded active set; recap = chronological feed.
3. **If workbench: define the bounded working object**. The casedock Case has spec / decisions / execution items / private notes / source links. For LE31's owner surface, the Case might be a `Visit`, a `Bill`, a `Shift`, or a `Reconciliation`. Each is a bounded working object.
4. **If workbench: implement the triage state machine**. casedock's states are `do_now / convert_to_case / set_aside / waiting / archive`. For LE31's owner surface, the states would be `pending / reviewed / resolved / escalated / archived`. The "decided once" invariant is the load-bearing one.
5. **If workbench: respect the focus bound**. "1 main + 2 secondary per day" is a *very* aggressive bound; LE31's owner may need more headroom, but the principle "the board never shows more than ~7–10 active items without folding" should be preserved.
6. **Decide whether the surface is a Telegram surface** (LE31 v1 chat-based) **or a web surface** (LE31 v1 has `index.html` mockups). casedock is a web surface; the Telegram equivalent is a different problem.
7. **Pilot on one decision type first**. Do not triage all of the owner's decisions at once.

## Dependencies

- Charter §3.1 (append-only posture) — the Case primitive must remain additive over `audit_logs` (no breaking changes to v1).
- Charter §3.4 (no customer-facing AI) — surface is owner, not diner; the casedock "decide once" principle is the *opposite* of how AI suggestions work, so any v2 surface that adopts the casedock posture must add an explicit *no AI in the triage step* guardrail.
- Charter §3.4.4 (the non-technical owner) — the casedock posture is *for* the non-technical owner, not the technical one.
- Feature 130 DHH-restaurant paper — sibling cross-section: *"workstation prompts + self-paced rehearsal"*.
- Feature 134 ECHO Auditable Memory Plane — companion: ECHO = record-shape primitive; casedock Case = bounded working object that *uses* structured records.
- Feature 84 Reckon low-effort decision-journal watch — sibling cross-section: Reckon = JTBD-pull validation (PH launch, no code); casedock = implementation primitive (GitHub, real code).

## Open questions

- **Is LE31 v2 an owner-workbench or an owner-recap?** The two have different shapes. casedock is a workbench; LE31 v1 owner-recap (if any) is a feed. The decision determines whether this primitive is relevant.
- **What is the bounded working object for LE31's owner?** casedock's Case = spec/decisions/execution_items/private_notes/source_links. For LE31, the most likely Case shapes are `Visit`, `Bill`, `Shift`, `Reconciliation`.
- **Is the "decide once" invariant compatible with v1?** LE31 v1's `audit_logs` are append-only (no edits, no deletes). The "decided once" invariant is *additive* over `audit_logs`: every triage decision is a new `audit_logs` row.
- **What is the focus bound for LE31's owner?** casedock's "1 main + 2 secondary per day" is aggressive. LE31's owner may need 5–10 active items without folding. The principle (bounded active set) is the load-bearing one; the exact bound is open.
- **Is the casedock posture compatible with charter §3.4 (no customer-facing AI)?** casedock has no AI integration. The casedock posture is *explicitly anti-AI* in its triage step ("the first thing you see is an action, not information" — AI suggestions are *information*, not action). Compatible by construction, but the *guardrail* must be written into the contract: "the triage step is operator-only; no AI suggestion is shown in the triage step".

## Why this matters

The repo provides LE31 with three things it does not currently have: (i) **a real implementation primitive** (Case + Decide Once) for the "low-effort UX for solo operators" cross-section that feature 84 only validated at the JTBD level; (ii) **explicit anti-AI design principles** ("no gamification", "no streaks", "the board never shows more than ~7–10 active cases") that are the *opposite* of how AI-assisted surfaces are typically designed; (iii) **a dated reference** (pushed today 2026-08-30) for the next time LE31 proposes a v2 surface where the owner is asked to triage or focus.

The cost of *not* filing this today is the risk that the first v2 surface that asks the owner to triage or focus reinvents the "decide once" invariant from scratch, or — worse — adds AI suggestions to the triage step (charter §3.4 violation). Filed now so the v2 boundary has the implementation primitive ready when the surface is proposed.

**Fully reversible.** Filing as a parking-lot defer artifact does not commit to any schema change or any v2 work. The Apache-2.0 licence means design ideas can be adopted without attribution gymnastics; code adoption is not proposed.
