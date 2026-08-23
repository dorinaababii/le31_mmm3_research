# Feature 102 — Nightmux stdlib-only Telegram-Agent Bridge (Watch-list)

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-23 (Pick A, **defer**) · **Bucket**: v2-AI (chat-driven operational control)
> **One-line**: A research-only watch-list artifact that records the in-window `mmr710/nightmux` cross-section peer (22★ MIT Python) — a **Python-stdlib-only + no-relay-server Telegram-agent bridge**. The pattern informs LE31 v2 cook-assistant (feature 68) architectural decomposition: **the Telegram-transport layer should be attack-surface-minimal**; the deterministic-gate orchestrator is the only attack surface. **No code today; deferred indefinitely until either (a) the peer crosses ≥50★ and validates the pattern as a market, or (b) ≥2 independent peers converge on the stdlib-only constraint.**

## Goal

The 2026-08-23 brainstorm scan surfaced `mmr710/nightmux` (22★, MIT, Python, pushed 2026-08-18T18:22:03Z, https://github.com/mmr710/nightmux) — a chat-driven agent-orchestrator surface that runs Claude Code / Codex / terminal agents from Telegram using **Python stdlib only** and **no relay server**. The cross-section insight: the Telegram-transport layer can be made attack-surface-minimal without sacrificing orchestrator capability, which informs the LE31 v2 cook-assistant (feature 68) architectural decomposition.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2-AI passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 v2 team considers whether the Telegram-transport layer should be attack-surface-minimal, the team wants to know whether a pure-stdlib bridge is technically viable, so that the orchestrator (deterministic gate) becomes the only attack surface.

**Why this is a fresh cross-section signal today**: `mmr710/nightmux` is the **only in-window high-star (≥20★) Telegram-agent-bridge peer with the pure-stdlib constraint**. The 6-repo cluster behind feature 78 (telegram-agent-control-plane-watch) does not enforce this constraint; `SGrappelli/pronto` (40★ MIT TS, features 90/94/100) uses WhatsApp + Telegram and is a different surface; `Mftrferdinand/Zeline` (75★ MIT Python, also in feature 78 cluster) is agentic-AI-framework-shaped, not stdlib-only-constrained.

## Scope

**In scope (v2-AI, S effort, ≤1 day, defer — LE31 already ships the surface):**
- Daily direct-repo `GET https://api.github.com/repos/mmr710/nightmux` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `mmr710/nightmux` README + commit history in the next daily-research pass to confirm the stdlib-only + no-relay architecture (READ ONLY — no import).
- Tracking star velocity + push activity on `mmr710/nightmux`.
- Documenting the stdlib-only architectural pattern in the LE31 research notes (this artifact is the document).

**Out of scope (no new LE31 implementation):**
- A new Telegram-bot framework. LE31 uses aiogram v3 and the surface is already shipped.
- A stdlib-only rewrite of the LE31 cook-bot transport. LE31's aiogram v3 + FastAPI backend is the correct stack today; rewriting to stdlib-only would lose aiogram's webhook + middleware ecosystem.
- An `mmr710/nightmux` import. The repo is a CLI/agent-orchestrator surface, not a restaurant-ops surface.
- Any new feature based on the `nightmux` code surface.

## Description

**Evidence precondition:** observed (GitHub `mmr710/nightmux` 22★ + MIT + Python stdlib only + no-relay-server + 2026-08-18 push + clear description cross-section with LE31 v2 cook-assistant transport). Confidence: **medium** for the cross-section pattern (the constraint is documented in the repo description); **low** for LE31-specific pain (LE31 already has the transport; the v2 architectural decomposition is a future-tense concern).

### `mmr710/nightmux`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-23 (this pass) | **22★** | (track) | 2026-08-18T18:22:03Z | MIT | Python |

**Direct repo URL**: https://github.com/mmr710/nightmux

**Verbatim description** (from GitHub API):
> Your night crew, on Telegram — run Claude Code / Codex / terminal agents from Telegram. Python stdlib only, no relay server.

**Why this is the cross-section peer of the day:**

1. **The constraint is novel.** Among the 6-repo Telegram-agent-cluster (feature 78) + the WhatsApp+Telegram Pronto surface (features 90/94/100) + the v2-AI agentic framework cluster (`Mftrferdinand/Zeline` 75★), `mmr710/nightmux` is the **only in-window peer that enforces "Python stdlib only" + "no relay server"**. The constraint maps directly to the LE31 v2 cook-assistant architectural decomposition: **transport = thin (≤200 lines of aiogram)**, **orchestrator = deterministic-gate (feature 68)**, **per-domain decision module = thin**.
2. **It is the only high-star (≥20★) Telegram-agent peer not in the feature 78 / 90 / 94 / 100 watch list.** Distinct by repo, distinct by author (`mmr710` is not `Mftrferdinand` / `SGrappelli` / `BosTheCoder` etc.), distinct by constraint.
3. **Stack match is direct**: Python + Telegram + chat-driven orchestrator. LE31 is Python + aiogram + chat-driven orchestrator. The stack match is exact; the architectural pattern is transferable.

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 v2 team revisits the cook-assistant architecture, the team wants to know whether a pure-stdlib transport is technically viable, so that the orchestrator becomes the only attack surface. Plausible but not currently blocking.
2. **Viability**: No new feature to operate; the pattern informs existing features (58/61/68). No new viability required.
3. **Practicability and confidence**: The peer repo is 22★ + MIT + Python stdlib only; architecture is straightforward; high confidence in the pattern (constraint is documented, repo is real, no relay-server means no remote attack surface). Low confidence in LE31-specific urgency (LE31 already has the transport; the v2 architectural decomposition is future-tense).
4. **Conflict**: No invariant conflict. The pattern strengthens the existing feature 58/61/63/68 line.
5. **Outcome, appetite, scope**: v2-AI watch-list. S effort. ≤1 day. **Defer** — LE31 already ships the surface; this artifact records the stdlib-only pattern.
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
- **External data dependency**: `mmr710/nightmux` README + commit history — to be read in the next daily-research pass (carry-over to 2026-08-24).
- **Watch-list add to `le31-daily-research-2026-08-24` pass**: include `mmr710/nightmux` in the 5-repo watch list to track star velocity + push activity.

## Open questions

1. **What is the architectural decomposition of `mmr710/nightmux`?** The repo description says "Python stdlib only, no relay server"; the next daily-research pass should confirm whether the implementation actually uses only `http.client` + `urllib.parse` + `asyncio` (or whether it uses `telegram`/`telethon` for the bot API). The answer determines how transferable the constraint is to LE31.
2. **Is the 22★ count maintained over the next 7 days?** Velocity will inform whether the pattern is gaining traction or is a single-maintainer hobby project.
3. **Does `mmr710/nightmux` expose a deterministic gate?** If yes, the cross-section to feature 68 (cook-assistant-deterministic-gate) is direct. If no, the cross-section is only on the transport-layer (and is less actionable for LE31 v2 cook-assistant).
4. **Does LE31 v2 charter need a transport-layer attack-surface policy?** This is a charter-level question that the artifact defers. The current charter (PROJECT_CHARTER.md §3.1) says "waiter web UI + cook Telegram bot"; it does not constrain the transport-layer stack.

## Why this matters

The 2026-08-23 brainstorm pass surfaces `mmr710/nightmux` as the only in-window high-star Telegram-agent-bridge peer with the pure-stdlib + no-relay constraint. The pattern informs LE31 v2 cook-assistant (feature 68) architectural decomposition: **the Telegram-transport layer should be attack-surface-minimal** so the orchestrator (deterministic gate) becomes the only attack surface. Today the LE31 cook-bot transport uses aiogram v3 + FastAPI backend; the artifact records that the stdlib-only constraint is technically viable for future v2 iteration, without changing the v1 roadmap.

**Cross-section with existing LE31 features**:
- Features 58/61/63/68 (cook-Telegram-bot operational-control surface) → this artifact strengthens the architectural pattern.
- Feature 78 (telegram-agent-control-plane-watch) → cluster anchor; this artifact is the constraint-driven sibling.
- Features 90/94/100 (`SGrappelli/pronto` WhatsApp+Telegram POS) → different surface (WhatsApp + Telegram; LE31 is Telegram-only).

**Why defer, not build**: zero observed pain at the LE31-owner level; LE31 already ships the transport; the stdlib-only architectural decomposition is a future-tense concern. The artifact is a research-note that records the pattern for future v2-AI iteration.
