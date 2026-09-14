# Feature 175 — skrudjreal-geminka-agent-v2-ai-control-plane-watch-v3 (defer)

> **NEW observation (2026-09-14).** Documents the **6-day push-idle broken by 2026-09-12T20:30:46Z** on GitHub `SkrudjReal/geminka-agent` — **MIT, 10★/0⑂, Python, 1281 KB**, `pushed_at` 2026-09-12T20:30:46Z (in-window by `pushed_at`, 2 days ago; broken 6-day push-idle from 2026-09-06 → 2026-09-12). This is the **3rd filing** of this repo as a feature (features 95, 117-variant-now-superseded, and 175); today's filing documents the **maintainer-still-active confirmation** (the 6-day push-idle was broken, the maintainer is still working on the repo). **First surface of this 6-day-push-idle-broken observation** (parent-verified by ripgrep against all features 1–172 + all brainstorm/daily-research reports 2026-08-04..2026-09-14). Bucket: **v2-AI control-plane watch-list (defer, parking-lot)** — cross-section reference, zero build time today.

## Goal

Retain the **`SkrudjReal/geminka-agent` 6-day push-idle broken by 2026-09-12T20:30:46Z** signal as a persistent cross-section reference for the LE31 v2-AI control-plane (charter §3.4 owner/staff-assist allowed). The artifact is the persistent cross-section reference + the maintainer-still-active confirmation + the documented push-idle history (6-day push-idle broken = maintainer is not abandoning the repo). No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **`SkrudjReal/geminka-agent` push-idle history**: 2026-09-06 → 2026-09-12 = 6-day push-idle, broken by 2026-09-12T20:30:46Z push.
- A written record of the **maintainer-still-active confirmation**: the 6-day push-idle was broken, the maintainer is not abandoning the repo.
- A written record of the **MIT permissive license** confirmation (charter §3.2 compatible).
- A written record of the **Gemini-powered agent** architecture: the repo uses Gemini as the *agent brain* for a Python workflow; the question this raises for LE31 is "if v2 ever introduces AI-assisted owner-side workflows (e.g., AI-summarised daily recap, AI-assisted stock replenishment suggestions), what control-plane does the AI sit in?"
- A cross-section reference with the prior `SkrudjReal/geminka-agent` filings (features 95, 117-variant-now-superseded) and the broader v2-AI control-plane cluster (features 126 five-primitives / 127 zero-shot-self-orchestration / 128 SKILL.state / 133 HANSARD / 134 ECHO / 135 DreamLedger / 136 MemGuard / 137 NL-to-Executable-Obligations / 150 Mandato / 152 LATTICE / 156 AWIG-OS / 161 claims-ledger / 162 Partasyuk / 163 LMCP / 167 provtrail / 168 asset-ledger / 169 openshare-ledger).
- A decision record: today's verdict is `defer` because LE31 v1 has no AI-assisted owner-side workflow surface (charter §3.4 forbids customer-facing AI; staff-only AI surfaces are a v2 surface at the earliest).

**Out of scope (defer artifact):**
- Any change to the cook Telegram bot.
- Any AI-assisted owner-side workflow surface in v1.
- Any v2-AI control-plane surface in v1.
- Any adoption of the `SkrudjReal/geminka-agent` code (the repo is Python + Gemini-powered agent; charter §3.4 owner/staff-assist compatible but no v1 surface exists).

## Evidence / JTBD

When a future LE31 v2 owner wants *AI-assisted owner-side workflows* (e.g., AI-summarised daily recap, AI-assisted stock replenishment suggestions, AI-assisted menu engineering), the owner wants *a cross-section reference for the staff-only AI control-plane primitive*, but struggles because *v1 has no AI surface and charter §3.4 forbids customer-facing AI*, so that *v2 can offer staff-only AI assistance without violating §3.4*.

- **Evidence class**: inferred (no LE31 owner has asked for AI-assisted workflows in 46 passes).
- **Confidence**: high for the push-idle-broken observation (parent-verified by direct-repo GET at `/tmp/le31-daily-2026-09-14/gh_parent_repo_SkrudjReal__geminka-agent.json`).
- **Real observed LE31 JTBD**: none directly. The maintainer-still-active confirmation is a *vocabulary + contingency* signal, not a *demand* signal.
- **The value is a ready-made cross-section reference** for any future v2-AI staff-only control-plane.

## Description

GitHub `SkrudjReal/geminka-agent` (MIT, 10★/0⑂, Python, 1281 KB, pushed 2026-09-12T20:30:46Z). The architectural pattern has one core finding and four sub-primitives:

1. **6-day push-idle broken** — `pushed_at` 2026-09-12T20:30:46Z; the previous push was 2026-09-06 (carry-over from 09-13). The 6-day push-idle was broken by the 2026-09-12 push, confirming the maintainer is still actively working on the repo.
2. **MIT permissive license** — charter §3.2 compatible (idea-portability is allowed).
3. **Gemini-powered agent** — the repo uses Gemini as the *agent brain* for a Python workflow. The architectural pattern is: *Python tool-set + Gemini as the planner + a control loop that calls tools and verifies results*.
4. **Staff-only AI** — the AI is the *operator's* workflow, not the *customer's* experience. This is charter §3.4 compatible (owner/staff-assist allowed).

The LE31 relevance is the **staff-only AI control-plane** cross-section reference. The question this raises for LE31 is: "if v2 ever introduces AI-assisted owner-side workflows, what control-plane does the AI sit in?" Charter §3.4 forbids customer-facing AI but **allows AI that assists owner/staff with observable evidence and a non-AI fallback**. The Gemini-powered agent pattern is a cross-section reference for any future v2 surface that needs to ask "what is the control-plane primitive for staff-only AI workflows?"

## LE31 seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | Inferred only — no observed LE31 v1 pain (v1 has no AI surface); v2 surface doesn't exist yet. |
| 2. Viability | Mechanism is well-defined (cross-section peer-reference); viability is conditional on a v2 staff-only AI control-plane surface. |
| 3. Practicability and confidence | Confidence: high for the push-idle-broken observation (parent-verified by direct-repo GET). Stack: same-stack (Python). Charter §3.1 invariant-compatible; §3.2 MIT permissive; §3.4 owner/staff-assist compatible (Gemini is staff-only). |
| 4. Conflict | No conflict with charter §3.1, §3.2, §3.4, §3.5, or §3.7. |
| 5. Outcome, appetite, scope | v2-AI control-plane (watch-list); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. |
| 6. Cost to operational value | Zero cost today; zero value today. Future contingency value: medium (cross-section reference for any v2-AI staff-only control-plane). |
| 7. Circuit breaker and reversibility | Trivially reversible: written reference, no code. |

**Decision: defer (parking-lot).** No v1 pain; no v2 build implication today. The maintainer-still-active confirmation is a vocabulary + contingency addition, not a `build` upgrade trigger.

## Implementation steps

None today. When v2 introduces any staff-only AI control-plane surface, the *cross-section peer reference* to surface is **`SkrudjReal/geminka-agent` (MIT, 10★/0⑂, Python + Gemini-powered agent)** with the documented push-idle-broken confirmation as the *maintainer-still-active* evidence.

## Dependencies

- None today.
- Future dependencies (v2 only): a v2 staff-only AI control-plane surface (charter §3.4 owner/staff-assist allowed). None of these are in v1 scope.

## Open questions

1. **Does LE31 v2 ever introduce a staff-only AI control-plane surface?** Today: no signal. The default answer is *no* unless owner-facing AI-assist pain surfaces.
2. **Is the *Gemini-as-agent-brain* pattern transferable to LE31's owner-side workflows?** The honest answer is *probably* — the pattern is institution-agnostic. But the specific Gemini API choice is not transferable (LE31's stack is FastAPI + SQLModel + Postgres + aiogram v3; Gemini is not pinned).
3. **Is the *maintainer-still-active* confirmation a quality signal or a maintenance-burden signal?** The honest answer is *quality* — the maintainer is still pushing code after 6 days, which is a healthy activity pattern. Not a hard-close trigger.

## Why this matters

The `SkrudjReal/geminka-agent` push-idle-broken confirmation is the **strongest maintainer-still-active signal of any v2-AI control-plane watch-list repo across the 46-pass series**. For LE31 v1, the implication is *none* (v1 has no AI surface). For LE31 v2, the implication is *the Gemini-as-agent-brain pattern is the cross-section reference for any future staff-only AI control-plane*. **No build today.**

## Cross-section (vs the prior filings)

- Feature 95 (first filing of `SkrudjReal/geminka-agent`, 2026-08-29) — *upstream* of this filing (the first observation).
- Feature 117-variant-now-superseded (geminka-agent-watch-v2, 2026-09-08) — *upstream* (the second observation).
- This filing (geminka-agent-watch-v3, 2026-09-14) — *current* (the 3rd filing, push-idle-broken confirmation).

The *transferable insight* is the **Gemini-as-agent-brain + staff-only-AI control-plane** pattern — a cross-section reference for any future v2-AI staff-only control-plane.
