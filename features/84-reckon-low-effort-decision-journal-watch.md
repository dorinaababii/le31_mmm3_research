# Feature 84 — Reckon Low-Effort Decision Journal Watch

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-19 (Pick A, defer — no observed LE31 pain; no public Reckon repo) · **Bucket**: v2 owner-pains (watch-list)
> **One-line**: A research-only watch-list artifact that records the in-window ProductHunt launch of `Reckon` ("decision journal that helps you calibrate", 2026-08-06) as a peer signal for the **decision-shaped** cross-section primitive (one-field-per-day personal calibration surface) that complements LE31's **recap-shaped** surfaces (features 39 / 67 / 69). No code; gate verdict `defer`. Re-evaluation trigger: an in-window ≥10★ Reckon-style peer with public repo + MCP API.

## Goal

The cross-section signal is **single-field-per-day personal calibration surface + low-effort UX + append-only persistence**. LE31 already has three recap-shaped surfaces:

- **Feature 39** (`owner-daily-recap-telegram`) — owner-facing daily recap push to Telegram
- **Feature 67** (`solo-operator-shift-journal-pwa`) — operator-side shift journal PWA
- **Feature 69** (`owner-no-account-shift-recap-link`) — no-account owner recap link

All three ask "**what happened**?" The new surface implied by Reckon is "**what did you decide and why?**" — captured at the cook's fingertips during shift, persisted append-only, surfaced to the owner via the existing recap channel. This is a **decision-shaped** extension, not a competing **recap-shaped** surface.

The pattern is observed in **`Reckon`** (ProductHunt main feed 2026-08-06 — "decision journal that helps you calibrate" — solo-builder micro-SaaS in the low-effort UX lane). The peer is a solo-builder product in the LE31-adjacent lane (low-effort UX + personal calibration); the cross-section is real even though the peer is small.

## Scope

**In scope (v2 owner-pains watch-list, S effort, no code, defer until re-evaluation trigger):**

- Record the in-window PH Reckon launch (2026-08-06) as peer signal for the decision-shaped primitive.
- Cross-section mapping to LE31's existing recap-shaped surfaces (features 39 / 67 / 69).
- Re-evaluation trigger documentation: revisit when (i) an in-window ≥10★ Reckon-style peer surfaces with public repo + MCP API, OR (ii) the LE31 cook/owner explicitly asks for decision-recap, OR (iii) the daily-research picks up a `decision journal` keyword in any HN / GitHub / arXiv query.

**Out of scope (v2 owner-pains watch-list):**

- The `CookDecision` table itself (would require schema + service + bot command + recap channel wiring; not built today).
- LLM-assisted prompts in the decision surface (charter §3.2: AI may assist owner/staff with observable evidence + non-AI fallback; out of scope for this watch-list artifact).
- Decision audit trail (covered by feature 61 holdfast approval ledger).
- Decision rationale mixin (covered by feature 47 decision-rationale mixin).

## Description

**Evidence precondition:** observed (in-window PH launch Reckon 2026-08-06, solo-builder micro-SaaS, low-effort UX lane). Confidence: **low–medium** for the JTBD pull (the peer is a solo-builder PH launch with no star count and no public repo; the cross-section is real but the evidence is thin).

**Cross-validation anchors:**

- Features 39 / 67 / 69 are recap-shaped (what happened); the new surface would be decision-shaped (what did you decide).
- The "low-effort" angle maps to charter §3.1 (every new surface must minimize cognitive load on the cook — single-field-per-day fits the constraint).
- The "append-only persistence" angle maps to feature 39's `OwnerRecap` shape (a small append-only table per owner/staff member).

**Decision: defer.** The cross-section is real but the evidence is thin; file as a watch-list artifact with a clear re-evaluation trigger.

## Data model

No data model changes today. When re-elevated to build:

```
CookDecision        (id, cook_user_id, decided_at, question, answer, shift_id)
```

Append-only, never updated or deleted (per charter §3.1 stock + state invariants adapted to the decision surface). One row per shift per cook; question is a small enum (`what_changed`, `what_repeated`, `what_blocked`, free-text).

## Implementation steps (when re-elevated)

1. **Verify the LE31 schema baseline** (read the existing `OwnerRecap` table for shape).
2. **Add `CookDecision` table** in `backend/app/models/cook_decision.py` (SQLModel).
3. **One Alembic migration** adding the table.
4. **Add `/decision` handler** in `backend/app/bot/cook_bot.py` (aiogram v3) — single-field prompt, append-only insert.
5. **Wire into feature 39's recap channel** — append the latest decision to the daily recap push.
6. **Add 3 acceptance tests** in `backend/tests/test_cook_decision.py`.
7. **Commit and push** with message `Add CookDecision decision-shaped recap extension (feature 84)`.

## Telegram interaction

When re-elevated: cook bot sends a single prompt at shift end ("what changed today that you'd repeat?"); cook replies with free text; the answer is appended to `CookDecision`. Owner sees the latest decision appended to the daily recap push (feature 39's existing surface).

## Dependencies

- The existing `OwnerRecap` table (feature 39) for shape reference.
- The existing cook bot surface (feature 02 + feature 09).
- No new pip dependencies.

## Open questions

- **Q1: Is the decision-shape primitive actually observed in any LE31 owner / cook feedback?** The watch-list artifact assumes the primitive is real but observed evidence is absent. If the LE31 owner / cook has not asked for a decision-recap, the surface may not be needed.
- **Q2: Does the surface conflict with feature 61 (holdfast approval ledger) or feature 47 (decision-rationale mixin)?** Both already sketch decision surfaces. The new surface should be scoped to **single-field-per-day at most** to avoid scope overlap.
- **Q3: Is the PH Reckon launch enough peer signal, or do we need a ≥10★ Reckon-style peer with public repo before re-elevation?** The watch-list artifact says the latter.

## Why this matters

The low-effort-UX personal-calibration pattern is the canonical micro-SaaS thesis (Reckon is a solo-builder product in this lane). The cross-section with LE31 surfaces 39 / 67 / 69 is direct: all three are recap-shaped; the new surface is **decision-shaped**. Filing as a watch-list artifact with a clear re-evaluation trigger gives the cross-section durable presence in the LE31 backlog without committing to a build that no observed LE31 cook/owner pain justifies today.

**Risk of building without observed pain:** the surface could expand into a "full decision audit trail" which collides with features 61 + 47; the scope guardrail in Q2 is essential.

**Risk of NOT building:** if the LE31 cook/owner ever asks for a decision-recap surface, the watch-list artifact ensures the cross-section is already documented and the re-evaluation trigger is clear.

## Status: defer (watch-list)

This file is a **watch-list artifact (defer until re-evaluation trigger)**. No code is shipped today. The slice boundary is hard: zero source-code changes, zero migrations, zero new dependencies. The artifact lives in this file and the corresponding HANDOFF.md.

The watch should be re-evaluated when: (i) an in-window ≥10★ Reckon-style peer surfaces with public repo + MCP API, OR (ii) the LE31 cook/owner explicitly asks for decision-recap, OR (iii) the daily-research picks up a `decision journal` keyword in any HN / GitHub / arXiv query.
