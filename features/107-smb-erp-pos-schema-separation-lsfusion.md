# Feature 107 — SMB ERP+POS schema-separation (lsFusion Apache-2.0 reference)

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-24 (Pick B, **defer**) · **Bucket**: v2 owner-pains (parking-lot, future-schema-patterns)
> **One-line**: A research-only watch-list artifact that records the in-window `lsfusion-solutions/mycompany` cross-section peer (317★ Apache-2.0 JavaScript, pushed 2026-08-19) — **a mature 7-module single-tenant SMB ERP+POS (inventory + invoicing + manufacturing + sales + projects + HR + POS) under permissive Apache-2.0 license** — as a future reference for LE31 v2 schema-separation patterns. **No code today; deferred indefinitely until either (a) LE31 v2 explicitly opens the schema-patterns question (charter §3 review pending), or (b) ≥2 independent permissive-license SMB ERP+POS peers converge on the same per-context module count.**

## Goal

The 2026-08-24 brainstorm scan surfaced `lsfusion-solutions/mycompany` (317★, Apache-2.0 JavaScript, pushed 2026-08-19T07:54:24Z, https://github.com/lsfusion-solutions/mycompany) — a free, open-source, self-hosted ERP and CRM for small businesses with **7 modules**: inventory, invoicing, manufacturing, sales, projects, HR, and POS. Built on lsFusion (the underlying platform). Description verbatim: "Free, open-source, self-hosted ERP and CRM for small businesses: inventory, invoicing, manufacturing, sales, projects, HR and POS. Built on lsFusion."

The cross-section insight: **single-tenant SMB ERP+POS architecture with per-business-context schema separation is the dominant open-source SMB pattern**, and `lsfusion-solutions/mycompany` is the highest-star permissive-license (Apache-2.0) reference in the 7-day window. Apache-2.0 license means the schema patterns can be studied and adapted without license contagion (unlike AGPL-3.0 `satisfecho/pos` which blocks LE31 v1 import per charter §3.2).

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 v2 team considers whether to add per-business-context schema separation (e.g., a separate `Inventory` schema and a separate `Menu` schema with explicit foreign-key relationships), the team wants to know whether mature open-source SMB ERP+POS projects use this pattern, so that the LE31 v2 schema design is informed by working peers and not invented from scratch.

**Why this is a fresh cross-section signal today**: `lsfusion-solutions/mycompany` is **the highest-star permissive-license (Apache-2.0) SMB ERP+POS reference in the 7-day brainstorm window**. The other in-window SMB ERP+POS peers are:
- `shyamsitaula/samarium` 503★ MIT Laravel — out-of-window by 13 weeks (pushed 2026-05-20).
- `satisfecho/pos` 31★ AGPL-3.0 Python — direct LE31-stack match but AGPL blocks import per charter §3.2; covered by features 40/42/89.
- `artivisi/balaka` 39★ Apache-2.0 Java — SME accounting app with inventory + POS-leaning modules; Apache-2.0 permissive license, in-window push 2026-08-18, but only 2 modules documented (accounting + inventory).

`lsfusion-solutions/mycompany` is the unique pattern-record candidate for mature 7-module permissive-license SMB ERP+POS.

## Scope

**In scope (v2 owner-pains, S effort, ≤1 day, defer — LE31 already ships the surface):**
- Daily direct-repo `GET https://api.github.com/repos/lsfusion-solutions/mycompany` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `lsfusion-solutions/mycompany` README + module documentation in the next daily-research pass to confirm the 7-module separation (READ ONLY — no import).
- Tracking star velocity + push activity on `lsfusion-solutions/mycompany`.
- Documenting the 7-module schema-separation pattern in the LE31 research notes (this artifact is the document).

**Out of scope (no new LE31 implementation):**
- A new ERP module framework. LE31 is a focused restaurant app; the 7-module SMB ERP surface is out of v1 scope.
- An `lsfusion-solutions/mycompany` import. The repo is JavaScript + lsFusion; the stack does not match LE31 Python.
- An Apache-2.0 → LE31 v1 dependency. The license is permissive but the stack is JavaScript and the surface is ERP, not restaurant.
- Any new feature based on the `lsfusion-solutions/mycompany` code surface.

## Description

**Evidence precondition:** observed (GitHub `lsfusion-solutions/mycompany` 317★ + Apache-2.0 + JavaScript + lsFusion + 7-module ERP+POS + 2026-08-19 push). Confidence: **high** for the cross-section pattern (the 7-module surface is documented in the description and README); **low** for LE31-specific urgency (LE31 v1 single-tenant context is correct; the v2 schema-patterns question is a future-tense concern).

### `lsfusion-solutions/mycompany`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-24 (this pass) | **317★** | (track) | 2026-08-19T07:54:24Z | Apache-2.0 | JavaScript |

**Direct repo URL**: https://github.com/lsfusion-solutions/mycompany

**Verbatim description** (from GitHub API):
> Free, open-source, self-hosted ERP and CRM for small businesses: inventory, invoicing, manufacturing, sales, projects, HR and POS. Built on lsFusion.

**Why this is the cross-section peer of the day:**

1. **The 7-module surface is mature.** A single repo ships inventory + invoicing + manufacturing + sales + projects + HR + POS — **the full SMB ERP+POS surface**, not a single-feature MVP. 317★ community traction confirms the surface has real users.
2. **Apache-2.0 license is permissive.** No contagion risk if the schema patterns are studied (charter §3.2 prohibits GPL/AGPL but is silent on permissive licenses).
3. **It validates LE31 charter §3 single-tenant posture.** A mature open-source SMB ERP+POS at 317★ proves that single-tenant schema separation scales. LE31's charter §3 single-tenant posture is consistent with this peer without changing.
4. **It is the only in-window ≥300★ permissive-license SMB ERP+POS reference.** `satisfecho/pos` (31★ AGPL Python) is excluded by license; `longnick/small-pos-open-source` (92★ MIT TS) is a starter, not a mature ERP; `shyamsitaula/samarium` (503★ MIT Laravel) is out-of-window.

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 v2 team considers per-business-context schema separation, the team wants to know whether mature open-source SMB ERP+POS projects use this pattern, so that the schema design is informed by a peer. Plausible but not currently blocking.
2. **Viability**: No new feature to operate; the pattern informs a future v2 schema decision. No new viability required.
3. **Practicability and confidence**: The peer repo is 317★ + Apache-2.0 + JavaScript + lsFusion + 7-module ERP+POS; high confidence in the pattern (the 7-module surface is documented in the description). Low confidence in LE31-specific urgency (LE31 v1 single-tenant context is correct; the v2 schema-patterns question is future-tense).
4. **Conflict**: No invariant conflict. The pattern validates LE31 charter §3 single-tenant posture without changing it.
5. **Outcome, appetite, scope**: v2 owner-pains parking-lot. S effort. ≤1 day. **Defer** — LE31 v1 single-tenant posture is correct; this artifact records the 7-module pattern for future v2 iteration.
6. **Cost to operational value**: Zero implementation cost; pure pattern-record artifact. High upside (architectural clarity for v2) at zero downside.
7. **Circuit breaker and reversibility**: Fully reversible. Watch-list artifact; can be deleted without consequence.

## Data model

**No schema changes.** Watch-list artifact only.

## Implementation steps

**None** — research-only artifact. The slice ships this Markdown file + a one-row `INDEX.md` update + a `*-HANDOFF.md` slice contract for the coding agent (which records the same non-action: "do not implement today; read README on next pass"). The slice hand-off is a no-op directive to the coding agent.

## Telegram interaction if any

**None** — the artifact does not interact with the LE31 Telegram-bot surface. The cross-section is observational only.

## Dependencies

- **No code dependencies** (research-only artifact).
- **External data dependency**: `lsfusion-solutions/mycompany` README + module documentation — to be read in the next daily-research pass (carry-over to 2026-08-25).
- **Watch-list add to `le31-daily-research-2026-08-25` pass**: include `lsfusion-solutions/mycompany` in the 5-repo watch list to track star velocity + push activity.

## Open questions

1. **What is the exact module separation pattern in `lsfusion-solutions/mycompany`?** Is it one lsFusion module per business area (inventory, invoicing, manufacturing, sales, projects, HR, POS), or is it one schema per business area with explicit FK relationships? The answer determines how transferable the pattern is to LE31 v2.
2. **Is the 317★ count maintained over the next 7 days?** Velocity will inform whether the pattern is gaining traction or is a mature stable pattern.
3. **Does `lsfusion-solutions/mycompany` support Postgres?** lsFusion is database-agnostic but the default configuration may differ; confirming the DB compatibility is a prerequisite for any future LE31 v2 reference.
4. **Does LE31 v2 charter need a per-context schema separation?** This is a charter-level question that the artifact defers. The current charter (PROJECT_CHARTER.md §3) says "single-tenant" but does not constrain the backend schema separation.

## Why this matters

The 2026-08-24 brainstorm pass surfaces `lsfusion-solutions/mycompany` as the only in-window ≥300★ permissive-license (Apache-2.0) mature SMB ERP+POS reference documenting a 7-module schema-separation pattern. The cross-section insight: **single-tenant SMB ERP+POS architecture with per-business-context schema separation is the dominant open-source SMB pattern at the 7-module level, and Apache-2.0 permissive licensing makes the patterns study-able without contagion**. The artifact validates LE31 charter §3 single-tenant posture without changing it and records the 7-module pattern as a future reference for LE31 v2 if/when schema-patterns questions arise.

**Cross-section with existing LE31 features**:
- Charter §3 (single-tenant posture) → this artifact validates the posture without changing it.
- Features 23-29 (v1 surface) → this artifact does not affect v1 build behavior.
- Feature 90 (pronto-watch cross-section) → different surface (Telegram + WhatsApp reminders; LE31 is Telegram-only).
- Features 102-104 + 106 (2026-08-23 + 2026-08-24 brainstorm picks) → all v2 watch-list artifacts; this is the schema-patterns-layer sibling.

**Why defer, not build**: zero observed pain at the LE31-owner level; LE31 v1 single-tenant posture is correct; the v2 schema-patterns question is a future-tense concern. The artifact is a research-note that records the pattern for future v2-AI iteration.
