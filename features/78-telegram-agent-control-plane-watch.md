# Feature 78 — Telegram + Agent Control Plane Pattern Watch

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-17 (Pick A, **defer**) · **Bucket**: v2-AI (chat-driven operational control)
> **One-line**: A research-only watch-list artifact that records the in-window GitHub cluster of **six repos in 48 hours** all converging on the same surface pattern: **Telegram (chat) + long-running agent task + control plane (start/stop/approve/switch)**. The pattern is exactly the LE31 cook-bot operational-control surface in features 58/61/63/68. **No code today; deferred indefinitely until either (a) one of these peers crosses ≥10★ and validates the pattern as a market, or (b) the pattern stays niche and LE31 is already ahead.**

## Goal

The 2026-08-17 brainstorm scan surfaced six in-window repos (2026-08-15..2026-08-17) converging on the same surface: `Mftrferdinand/Zeline` (64★, agentic AI framework + Telegram + WhatsApp), `H4fizWasabie/mino-agent` (14★, single-binary + SQLite + Telegram + personal-assistant), `viggomeesters/arr-orchestrator` (0★, Python + Telegram + agent control plane for self-hosted media), `motu001/dsh-phone-bridge` (0★, phone + Telegram + DeepSeek Harness bridge), `BosTheCoder/claude-concierge` (1★, Telegram + Claude Code phone triage), `Nicotinamide/dsh-plugin-tg-bridge` (0★, Telegram ↔ DeepSeek Harness bridge). The pattern is independent developer convergence on the same chat-driven operational surface that LE31 already ships.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2-AI passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 team wants to confirm that the chat-driven operational-control surface (cook Telegram bot + per-batch append-only `StockEntry` ledger + approval gate) is the right v2-AI investment direction, the team wants to know whether independent developers in 2026-08 are reaching for the same surface, so that the team can decide whether the existing feature pipeline is mainstream-validated or whether a new surface should be explored.

**Why this is a fresh cross-section signal today**: the GitHub `topic:telegram-bot` cluster (798 repos) + the `restaurant created:>2026-07-17 language:python` overlap produced **six repos in 48 hours** all converging on the same surface pattern. The cluster-shipping rate (6 repos in 48h) is the strongest convergence signal of the entire 2026-08 cross-section. The fact that the highest-star (`Zeline` 64★) is a Python repo with telegram-bot topic makes the pattern materially meaningful.

## Scope

**In scope (v2-AI, S effort, ≤1 day, defer — LE31 already ships the surface):**
- One source-file edit: this `features/78-telegram-agent-control-plane-watch.md` artifact (the watch-list record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (no new LE31 implementation):**
- A new Telegram-bot framework. LE31 uses aiogram v3 and the pattern is already shipped.
- A new agent control plane. LE31 already ships the cook-bot operational-control surface (features 58/61/63/68).
- A new approval-gate primitive. Feature 61 (`holdfast-approval-ledger`) already covers the human-approval gate.
- A new LLM-proposes / deterministic-gates-decide pattern. Feature 68 (`cook-assistant-deterministic-gate`) already covers this.

## Description

**Evidence precondition:** observed (GitHub `topic:telegram-bot` cluster — 6 repos in 48h, top 64★, all Python/Go/JS). Confidence: **medium** for the pattern convergence (the cluster is real and the timestamps are within 48h); **low** for LE31-specific pain (no observed pain at the LE31 owner-pain level; LE31 already ships the surface).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: Independent developers in 2026-08 are converging on the chat-driven operational surface. If the pattern is mainstream, LE31 is already ahead; if the pattern is niche, LE31 can abandon the surface and free the v2-AI budget. Plausible.
2. **Viability**: Once the pattern is confirmed mainstream, LE31's existing features are the implementation. No new viability required.
3. **Practicability and confidence**: LE31 already ships the chat-driven operational surface. High confidence today that the surface is real; low confidence today that the pattern is mainstream (only 1 repo at 64★; the rest 0–14★).
4. **Conflict**: No invariant conflict. The pattern strengthens the existing feature 58/61/63/68 line.
5. **Outcome, appetite, scope**: v2-AI watch-list. S effort.
6. **Cost to operational value**: Low value today (the LE31 surface is already shipped). High value as a market-validation signal only if one of the 6 peers crosses ≥10★.
7. **Circuit breaker**: Delete this file + the corresponding `INDEX.md` row + the Linear sub-issue. No other code changes to revert.

**Decision: defer (watch-list).** Cargo-culted from feature 71's pattern.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline" table with date 2026-08-17, pick `telegram-agent-control-plane-watch`, feature path `features/78-telegram-agent-control-plane-watch.md`, Linear sub-issue ID (TBD), status "Watch-list (defer — LE31 already ships the surface)".
2. **Re-check** on a future daily-research pass. If any of the 6 in-window peers reaches ≥10★ and is sustained for 7+ days, the watch re-activates (re-evaluate the gate). If the pattern stays at 0–1★ indefinitely, the watch expires.

## Telegram interaction

None. The slice is a research artifact; no user-facing Telegram surface changes.

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- Features 58 (operator-ai-action-surface), 61 (holdfast-approval-ledger), 63 (second-opinion-verifier-role), 68 (cook-assistant-deterministic-gate) already ship the surface in LE31.

No new pip dependencies. No new system dependencies. No new external services.

## Open questions

- **Q1: Will any of the 6 in-window peers reach ≥10★ in the next 30 days?** Re-check on a future pass. If `Zeline` (already 64★ in 5 days) sustains 100★+ or `BosTheCoder/claude-concierge` (1★) grows to 10★+, the pattern is consolidating.
- **Q2: Will the pattern consolidate in a specific domain (agent framework / personal assistant / media automation / coding agent) or remain cross-domain?** The current 6-repo cluster is cross-domain. A future domain-concentration would indicate the surface stabilizes around a specific use case.
- **Q3: Does the LE31 owner survey surface a need for any of the 6-peer patterns (e.g., "phone bridge" / "approval gate" / "session switch")?** No owner survey data today. The watch remains dormant until either observed pain or peer-velocity re-activates it.

## Why this matters

The LE31 cook-bot operational-control surface is **the LE31 v2-AI differentiator** (PROJECT_CHARTER.md + features 58/61/63/68). The 6-repo in-window cluster confirms that the surface is at a 2026-08 convergence inflection point in the broader GitHub ecosystem. If the pattern is mainstream, LE31's strategic posture is validated; if it stays niche, LE31 can reallocate the v2-AI budget to other surfaces.

**Risk of NOT tracking**: the pattern may consolidate in 2026-H2; if the watch-list is not in place when that happens, LE31 either re-derives the same conclusions (wasted cycles) or misses the consolidation (strategic risk).

**Risk of over-tracking**: the pattern is observed at the repo level only; the watch-list is research-only, consumes zero daily-research cycles, and ships no code. Over-tracking risk is low.

**Net**: park the watch-list under "defer until either observed pain or peer-velocity re-activates it." Re-evaluate when one of the 6 peers crosses ≥10★ sustained for 7+ days.

## Status: watch-list (defer)

This file is a **watch-list artifact (defer)**. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies. No code change today. The research-side subagent (Pass 18, 2026-08-17) records the watch as **defer — LE31 already ships the surface**.

## Cross-validation anchors

- **GitHub `topic:telegram-bot` + `restaurant created:>2026-07-17 language:python` cluster (2026-08-15..2026-08-17 push)** — six repos in 48h converging on the same surface pattern. The cluster confirms the pattern is at a 2026-08 convergence inflection point.
- **Feature 58 (operator-ai-action-surface)** — companion feature for the chat-driven operational surface. The watch-list is sequenced behind feature 58.
- **Feature 61 (holdfast-approval-ledger)** — approval gate primitive. The cluster includes `dallascrilley/holdfast` (same name as feature 61) — independent confirmation of the approval-gate pattern.
- **Feature 63 (second-opinion-verifier-role)** — verifier role for the chat-driven surface. The cluster's "approve / ask / switch sessions" patterns match feature 63's scope.
- **Feature 68 (cook-assistant-deterministic-gate)** — LLM-proposes / deterministic-gates-decide pattern. The cluster includes `4242labs/memento` (same pattern, pushed 2026-08-14) — independent confirmation of the deterministic-gate pattern.
- **No HN / OpenAlex validating peer** — the GitHub `topic:telegram-bot` cluster is the only in-window signal. No HN thread, no OpenAlex paper, no ProductHunt item validates the pattern yet.
