# Feature 164 — muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route (defer)

> **NEW observation (2026-09-09).** Documents in-window GitHub repo `Muredsa/UXYS` (MIT, **1★/0⑂**, **pushed 2026-09-04T17:08Z** — in-window, language Python, license MIT, no topics). Description (verbatim from GitHub API): *"Intent-first UX analysis skill for AI agents — model user intents, shortest sufficient route."* **The *"shortest sufficient route"* primitive is the *static-analysis* dual of feature 68 (`cook-assistant-deterministic-gate`)** — both argue that a v2 operator-UX surface should expose *one* action at a time, not a menu, but they reach it from opposite directions (UXYS = analysis-time; feature 68 = runtime). Bucket: **v2 operator-UX architecture-reference** — parking-lot defer. Zero build time today.

## Goal

Retain the **"intent-first UX analysis skill — model user intents, shortest sufficient route"** primitive as a persistent cross-section reference for any future v2 surface that introduces an owner/operator-facing review or recap. The artifact is the persistent cross-section reference + a candidate *static-analysis* discipline for the next v2 operator-UX surface. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"intent-first UX"** discipline: the operator-UX surface is analyzed from the operator's *intent* (what is the operator trying to do?), not from the *features* (what does the application offer?). This is the *opposite posture* of a multi-option KDS / POS surface.
- A written record of the **"shortest sufficient route"** primitive: at every operator-facing moment, the surface should expose the *smallest sufficient action set* — not a menu, not a list, not a navigation. This is the operator-UX dual of charter §3.1 *"explicit state transitions"* + *"explicit user actions"* invariants.
- A written record of the **"model user intents"** primitive: the analysis step is to *model* the operator's intents (a small set of high-confidence intents), then surface the action that serves the *most-confident* intent first. This is the *static-analysis* analog of feature 68's *runtime* deterministic gate.
- A decision record: today's verdict is `defer` because LE31 v1 has no operator-UX surface (the waiter web UI is a minimum-viable feature surface, not a *designed* operator-UX surface); the *"shortest sufficient route"* primitive is a future v2 surface, not v1.

**Out of scope (defer artifact):**
- Any change to the waiter web UI (charter §3.1: explicit state transitions; the v1 surface is sufficient for v1 ops).
- Any change to the cook Telegram bot (charter §3.1: explicit state transitions; the v1 surface is sufficient for v1 ops).
- Any new operator-UX surface (LE31 v1 has no designed operator-UX surface today; introducing one would require an owner decision per charter §3.2).
- Adoption of the UXYS codebase (the repo is a 1★ MIT Python skill; the *primitive* is portable; the *codebase* is not adoptable without a full read-and-eval).
- Cross-pollination with charter §3.4 AI surface (the *"intent-first UX analysis skill for AI agents"* framing suggests AI surface integration; charter §3.4 explicitly rules out customer-facing AI; owner-facing AI is allowed with observable evidence).

## Evidence / JTBD

When a future LE31 v2 operator-facing review or recap surface is introduced, the operator wants *a static-analysis tool that surfaces the smallest sufficient action set at every moment*, but struggles because *the v1 waiter web UI shows all menu items at every moment*, so that *the v2 surface can be audited for operator-UX quality*.

- **Evidence class**: observed (the UXYS description names the *"shortest sufficient route"* primitive explicitly).
- **Confidence**: high for the primitive match (the *shortest sufficient route* is the operator-UX dual of charter §3.1's *"explicit state transitions"* + *"explicit user actions"*); low for transferability (the UXYS README has not been read; the skill-format is documentation-only and the underlying prompt logic is unknown).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no designed operator-UX surface (the v1 waiter web UI is functional, not designed for low-effort operator-UX).
- **The value is naming, not direct demand**: when the first v2 operator-UX surface lands, the *"shortest sufficient route"* primitive is a ready-made *named design discipline*.

## Description

The `Muredsa/UXYS` repo (MIT, 1★, Python, pushed 2026-09-04T17:08Z) is a *"skill"* — a packaged instruction-set for an AI agent. The skill is designed to *analyse* a user interface from an *"intent-first"* posture: it asks *"what is the user trying to do?"* first, then surfaces the *smallest sufficient action set* that serves the most-confident intent.

The architectural primitive UXYS proposes has three components:

1. **Intent-first UX** — the analysis is anchored on the operator's *intent*, not on the application's *features*. This is the *opposite posture* of a feature-list UI (which anchors on the application's features and asks the operator to find the right one).
2. **Shortest sufficient route** — at every moment, the surface should expose the *smallest sufficient action set*. Not a menu (which has *N* options). Not a list (which has *N* items). Not a navigation (which has *N* routes). The surface has *1* action visible at a time.
3. **Model user intents** — the analysis step is to *model* the operator's intents. A small set of high-confidence intents (e.g. *"I want to take an order"*, *"I want to check stock"*, *"I want to close a shift"*). The skill surfaces the action that serves the most-confident intent first.

**The 1:1 mapping onto LE31 v1 architecture:**

| UXYS primitive | LE31 v1 equivalent | Charter section | Status |
|---|---|---|---|
| Intent-first UX | (LE31 v1 surfaces are not designed with intent-first posture; the waiter web UI shows the menu, the cook Telegram bot shows the order queue) | (future v2 surface) | **Not implemented** — would require a redesign of the waiter web UI + cook Telegram bot |
| Shortest sufficient route | (LE31 v1 surfaces are not designed with shortest-sufficient-route posture; the waiter web UI shows all menu categories) | (future v2 surface) | **Not implemented** |
| Model user intents | (LE31 v1 has no intent-modeling; the cook Telegram bot responds to commands, the waiter web UI shows forms) | (future v2 surface) | **Not implemented** |
| Skill-format primitive | (LE31 v1 has no skill-format primitives) | (future v2 surface; charter §3.4 if AI-influenced) | **Not implemented** |

**Cross-section with prior picks (LE31 cluster of 26 defer picks, this is pick #28 = +1):**

- **Feature 68 cook-assistant-deterministic-gate** — the *runtime* deterministic-gate. UXYS is the *static-analysis* dual of feature 68. **UXYS is the *audit* discipline; feature 68 is the *enforcement* discipline.**
- **Feature 84 reckon-low-effort-decision-journal-watch** — the *low-effort decision-journal* primitive. UXYS is the *low-effort operator-UX* primitive; feature 84 is the *low-effort decision-journal* primitive. **UXYS is the *audit* discipline; feature 84 is the *capture* discipline.**
- **Feature 130 dhh-kitchen-accessible-operator-ux-visual-replayable** — the *accessible visual-replayable* operator-UX. UXYS is the *intent-first* operator-UX; feature 130 is the *accessible visual-replayable* operator-UX. **UXYS is the *intent-anchored* posture; feature 130 is the *accessibility-anchored* posture.**
- **Feature 140 casedock-adhd-informed-solo-builder-workbench-htmx-design-posture** — the *"remove decisions instead of adding them"* posture. UXYS is the *"smallest sufficient action set"* posture; feature 140 is the *"remove decisions"* posture. **UXYS is the *shortest-route* discipline; feature 140 is the *no-decisions* discipline.**
- **Feature 144 silphe-operator-pointer-biometric-hci-cross-section** — the *low-effort pointer-biometric* HCI. UXYS is the *intent-first* HCI; feature 144 is the *low-effort* HCI. **UXYS is the *intent-anchored* posture; feature 144 is the *effort-minimizing* posture.**
- **Feature 156 awig-os-rule-citing-audit-bali-village-constitution-architectural-precedent** — the *every-act-cites-the-rule* primitive. UXYS is the *smallest-action* primitive; feature 156 is the *rule-citing* primitive. **UXYS is the *what-to-show* discipline; feature 156 is the *what-cites-what* discipline.**

The 28 picks form the **deepest single-vocabulary cluster in the 42-pass series** for the *append-only-ledger + audit-trail-schema + owner-pains + operator-UX* architectural pattern. **All 28 are `defer`; no code change today.**

## Data model

**No data model change.** The defer artifact is documentation only. The *"shortest sufficient route"* primitive is a future v2 operator-UX surface and would require (optionally):
- A *user-intent model* (a small set of high-confidence intents: take order, check stock, close shift, etc.).
- A *smallest-sufficient-action-set* derivation query (compute the action set for the current intent).
- A *smallest-sufficient-action-set* audit tool (the UXYS skill is the audit tool; no code adoption required).

None of these are v1; all are v2 surfaces that would require an *owner decision* per charter §3.2.

## Implementation steps

**No code today.** The defer artifact is the persistent cross-section reference:

1. **Add the *"shortest sufficient route"* primitive to `specs/2026-09-09-muredsa-uxys-intent-first-ux-analysis-shortest-sufficient-route-HANDOFF.md`** as a named design discipline for any future v2 operator-UX surface — already done in the HANDOFF.md.
2. **Wait for the first v2 surface that introduces an operator-UX review or recap** — trigger conditions: (a) first v2 PR that adds an operator-UX surface; (b) first v2 PR that adds a user-intent model; (c) first v2 PR that redesigns the waiter web UI for intent-first posture.
3. **On trigger, evaluate the change against the *"shortest sufficient route"* primitive** — does the change expose the smallest sufficient action set at every moment? Does the change anchor on operator intent (not application features)? The primitive is the *what to verify*, not the *what to implement*.

## Telegram interaction if any

**None today.** The defer artifact is documentation only; no operator surface changes.

The **future v2 surface** (if the owner decides to redesign the waiter web UI or cook Telegram bot for intent-first posture) would: (a) add a user-intent model; (b) compute the smallest sufficient action set at every moment; (c) audit the surface with the UXYS skill. This is a *v2 surface*, not v1.

## Dependencies

- **GitHub access** — public, no dependency.
- **No LE31 code dependency** — defer artifact is documentation only.
- **Future v2 dependencies** (if *"shortest sufficient route"* is adopted): a user-intent model; a smallest-sufficient-action-set derivation query; an audit tool. All future; no v1 dependency.

## Open questions

1. **Is the UXYS 1★ repo a credible production-traction data point?** Charter §3.2: stars are popularity proxy, not gate. The repo is by `Muredsa` (single author); the README has not been read; the underlying prompt logic is unknown. The *primitive* is the value; the *production traction* is not.
2. **Should the LE31 v1 waiter web UI be redesigned for intent-first posture today?** Charter §3.2: only changes needed for restaurant operations. The owner of a small restaurant has not asked for an operator-UX redesign; the v2 surface that needs the redesign is a future surface. Recommend: defer to v2 if/when the owner asks for an operator-UX redesign.
3. **Does the UXYS overlap with feature 140 casedock?** Partially: UXYS is the *"smallest action set"* posture; casedock is the *"remove decisions"* posture. Both argue *less is more* for operator-UX. **UXYS is the *smallest-action* discipline; casedock is the *no-decisions* discipline.** The clusters overlap on *less is more*; UXYS adds the *intent-modeling* step which casedock does not.
4. **Does the UXYS overlap with feature 130 DHH-kitchen?** Partially: UXYS is the *intent-first* posture; feature 130 is the *accessible visual-replayable* posture. Both argue for *better* operator-UX. **UXYS is the *intent-anchored* discipline; feature 130 is the *accessibility-anchored* discipline.** The clusters are complementary, not duplicate.
5. **Does the UXYS overlap with charter §3.4?** Yes (partial): UXYS is a *"skill for AI agents"* — the framing suggests AI surface integration. Charter §3.4 explicitly rules out customer-facing AI; owner-facing AI is allowed with observable evidence. UXYS is a *static-analysis skill*, not a customer-facing surface; **owner decision required if any AI-influenced operator-UX surface is scoped.**

## Why this matters

**UXYS is the freshest *"intent-first operator-UX"* primitive of the 42-pass series.** The *"shortest sufficient route"* framing is the operator-UX dual of charter §3.1's *"explicit state transitions"* + *"explicit user actions"* invariants — applied not to the data model but to the operator-facing surface. The 1★ MIT Python skill is the smallest portable artifact of the 42-pass series for this primitive.

**The cluster (28 picks, this one + 27 prior) is the persistent cross-section reference for the next v2 owner-pains + operator-UX moment.** All 28 are `defer`; no code change today. The cluster is the *what the LE31 v2 owner-pains + operator-UX architecture is*, named across 28 different sources, and ready to be referenced when the first v2 operator-UX surface lands.

**The most operationally valuable future v2 surface is waiter web UI redesign for intent-first posture**: introducing a waiter web UI that anchors on the operator's intent (take order, check stock, close shift) rather than the application's features (menu items, categories, navigation), and exposes the *smallest sufficient action set* at every moment, would close the *low-effort operator-UX gap* (today, the waiter must scan the menu to find the right action). Owner decision required; not v1.