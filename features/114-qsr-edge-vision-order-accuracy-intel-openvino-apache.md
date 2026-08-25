# Feature 114 — QSR edge-vision order-accuracy Intel OpenVINO Apache reference

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no code) · **Source**: brainstorm 2026-08-25 (Pick C, **defer**) · **Bucket**: v2 owner-pains (parking-lot, future-vision-surface-reference)
> **One-line**: A research-only watch-list artifact that records the in-window `intel-retail/order-accuracy` cross-section peer (2★ / 15 forks Apache-2.0 Python, pushed **2026-08-25 today**) — **an Intel-authored Quick Service Restaurant (QSR) reference implementation for edge object detection + order accuracy (GStreamer + OpenVINO)** — as a future reference for LE31 v2 computer-vision surface (plate-accuracy, kitchen-display visual verification, stock-shelf visual verification). **No code today; deferred indefinitely until either (a) LE31 v2 explicitly opens the computer-vision surface question (charter §3.5 AI non-customer-facing rule applies — vision must be gated on deterministic stock-state transitions, not free-form LLM calls), or (b) the `intel-retail/order-accuracy` peer gains a community-traction signal (>=100★ or >=3 independent QSR-edge-vision reference implementations with similar positioning).**

## Goal

The 2026-08-25 brainstorm scan surfaced `intel-retail/order-accuracy` (2★ / 15 forks Apache-2.0 Python, pushed **2026-08-25T05:00:26Z (today, freshest push in the pass)**, https://github.com/intel-retail/order-accuracy). Description verbatim: *"The Order Accuracy Pipeline System is an open-source reference implementation for building and deploying video analytics pipelines for retail order accuracy in Quick Service Restaurant (QSR) use cases. It leverages Intel® hardware and software, GStreamer, and OpenVINO™ to enable scalable, real-time object detection and classification at the edge."*

The cross-section insight: **LE31's v2 computer-vision surface (plate-accuracy, kitchen-display visual verification, stock-shelf visual verification) has a vendor-grade (Intel-authored) QSR-anchored Apache-2.0 permissive reference for edge object detection + order accuracy**. The 1:7.5 star-to-fork ratio signals real consumption, not just stargazers. Different domain (vision/edge) than LE31's text/cook-bot stack, but the architectural pattern (GStreamer + OpenVINO + edge deployment + QSR-anchored + Apache-2.0 permissive) is a useful reference.

The slice ships **zero code**; the slice ships **one watch-list artifact** that future v2 passes can reference. The slice boundary is hard: one Markdown file update, zero source code changes, zero migrations, zero new dependencies.

## Evidence / JTBD

When the LE31 v2 team considers adding any computer-vision surface (plate-accuracy, kitchen-display visual verification, stock-shelf visual verification), the team wants to know whether a vendor-grade (Intel-authored) QSR-anchored reference implementation documents the edge-vision architecture, so that the computer-vision design is informed by a working peer and not invented from scratch.

**Why this is a fresh cross-section signal today**: `intel-retail/order-accuracy` is the **freshest in-window push** (2026-08-25 today) and the **only in-window Intel-authored QSR reference implementation** for edge object detection + order accuracy. The other in-window restaurant-tech vision-adjacent peers are:
- `arushahmd/restaurant-voice-ai` 1★ MIT Python — voice-ordering, not edge-vision (covered by feature 113).
- `Eigensu/RestoBuzz` 1★ MIT Python — WhatsApp bulk-messaging, not edge-vision (mention-only).
- `nematjon555/telegram-restaurant-delivery-bot` 0★ Python — Telegram delivery bot, not edge-vision (covered by feature 110).

None of the above ship an edge-vision + QSR-anchored architecture. `intel-retail/order-accuracy` is the unique pattern-record candidate.

## Scope

**In scope (v2 owner-pains, S effort, ≤1 day, defer — LE31 v1 doesn't ship a computer-vision surface):**
- Daily direct-repo `GET https://api.github.com/repos/intel-retail/order-accuracy` (via `$HERMES_GITHUB_TOKEN`) to track stars + push activity.
- Reading the `intel-retail/order-accuracy` README + architecture documentation in the next daily-research pass to confirm the GStreamer + OpenVINO + edge deployment pattern (READ ONLY — no import).
- Tracking star velocity + push activity on `intel-retail/order-accuracy`.
- Documenting the QSR edge-vision architecture pattern in the LE31 research notes (this artifact is the document).

**Out of scope (no new LE31 implementation):**
- A new computer-vision surface. LE31 v1 doesn't ship one; the v2 extension is a future-tense concern.
- An `intel-retail/order-accuracy` import. Apache-2.0 permissive license means code-borrow is permitted, but no borrow is needed today; the architectural pattern is informational only.
- A GStreamer / OpenVINO / Intel-hardware dependency. Adding these would expand LE31's dependency surface dramatically; the artifact is informational only.
- Any new feature based on the `intel-retail/order-accuracy` code surface.
- Any schema changes; any new dependencies; any source-file edits outside this artifact.

## Description

**Evidence precondition:** observed (GitHub `intel-retail/order-accuracy` 2★ / 15 forks + Apache-2.0 + Python + GStreamer + OpenVINO + Intel hardware + QSR-anchored + in-window push on **2026-08-25 today**). Confidence: **high** for the cross-section pattern (the GStreamer + OpenVINO + edge deployment architecture is documented in the repo description); **low** for LE31-specific urgency (LE31 v1 doesn't ship a computer-vision surface; the v2 extension is a future-tense concern; charter §3.5 AI non-customer-facing rule applies — vision must be gated on deterministic stock-state transitions, not free-form LLM calls).

### `intel-retail/order-accuracy`

| Date | Stars | Forks | Pushed | License | Language |
|---|---|---|---|---|---|
| 2026-08-25 (this pass) | **2★** | 15 | **2026-08-25T05:00:26Z (today)** | Apache-2.0 | Python |

**Direct repo URL**: https://github.com/intel-retail/order-accuracy

**Verbatim description** (from GitHub API):
> The Order Accuracy Pipeline System is an open-source reference implementation for building and deploying video analytics pipelines for retail order accuracy in Quick Service Restaurant (QSR) use cases. It leverages Intel® hardware and software, GStreamer, and OpenVINO™ to enable scalable, real-time object detection and classification at the edge.

**Why this is the cross-section peer of the day:**

1. **Intel-authored QSR reference implementation.** Vendor-grade reference (Intel as the authoring org) rather than hobby project. The QSR anchoring is direct — same domain as LE31 (restaurant), different sub-domain (QSR vs full-service).
2. **GStreamer + OpenVINO + edge deployment architecture.** The edge-vision pipeline (GStreamer for video capture + OpenVINO for Intel-hardware-accelerated inference) is well-documented and Intel-credible. Apache-2.0 permissive means the architecture pattern is reusable without license concerns.
3. **Star-to-fork ratio of 1:7.5 signals real consumption.** 2★ / 15 forks (1:7.5) vs typical 1:0.5–1:2 — the fork count is unusually high relative to stars, suggesting real production consumption rather than just stargazing.
4. **Freshest in-window push today.** Pushed at 2026-08-25T05:00:26Z (today, ~2 hours before this brainstorm pass started). Freshest single in-window signal of the day.
5. **Cross-section to LE31 v2 computer-vision surface is direct.** When LE31 v2 considers plate-accuracy, kitchen-display visual verification, or stock-shelf visual verification, the QSR edge-vision architecture is a direct reference. Charter §3.5 AI non-customer-facing rule applies — vision must be gated on deterministic stock-state transitions, not free-form LLM calls (e.g., vision surfaces must trigger an explicit user-action prompt before any `StockEntry` write).

**Seven-check gate verdict:**
1. **Raison d'être / JTBD**: When the LE31 v2 team considers adding a computer-vision surface (plate-accuracy, kitchen-display visual verification, stock-shelf visual verification), the team wants to know whether a vendor-grade QSR-anchored peer documents the edge-vision architecture, so that the computer-vision design is informed by a working peer. Plausible but not currently blocking.
2. **Viability**: No new feature to operate; the pattern informs a future v2 surface decision. No new viability required. **Note**: charter §3.5 (AI non-customer-facing) applies — vision must be gated on deterministic stock-state transitions, not free-form LLM calls.
3. **Practicability and confidence**: The peer repo is 2★ / 15 forks + Apache-2.0 + Python + GStreamer + OpenVINO + Intel hardware + QSR-anchored; high confidence in the architectural pattern (the GStreamer + OpenVINO + edge deployment architecture is documented in the repo description). Low confidence in LE31-specific urgency (no owner signal of "I want plate-accuracy / kitchen-display visual verification" today).
4. **Conflict**: No invariant conflict. The pattern is informational and does not change LE31 v1 behavior. **Note**: charter §3.5 (AI non-customer-facing) is preserved by the deterministic-state-machine gating pattern.
5. **Outcome, appetite, scope**: v2 owner-pains parking-lot. S effort. ≤1 day. **Defer** — LE31 v1 doesn't ship a computer-vision surface; this artifact records the QSR edge-vision architecture for future v2 iteration.
6. **Cost to operational value**: Zero implementation cost; pure pattern-record artifact. High upside (computer-vision surface for v2) at zero downside.
7. **Circuit breaker and reversibility**: Fully reversible. Watch-list artifact; can be deleted without consequence.

## Data model

**No schema changes.** Watch-list artifact only.

## Implementation steps

**None** — research-only artifact. The slice ships this Markdown file + a one-row `INDEX.md` update + a `*-HANDOFF.md` slice contract for the coding agent (which records the same non-action: "do not implement today; read `intel-retail/order-accuracy` README on next pass"). The slice hand-off is a no-op directive to the coding agent.

## Telegram interaction if any

**None today.** The artifact does not interact with the LE31 Telegram-bot surface. The cross-section is observational only. **If/when the slice is un-deferred** (v2 owner-pains extension), the computer-vision surface would be a **kitchen-display visual verification** (cook-bot visible `StockEntry` confirmation) gated on deterministic stock-state transitions, not free-form LLM calls — preserving charter §3.1 + §3.5.

## Dependencies

- **No code dependencies** (research-only artifact).
- **External data dependency**: `intel-retail/order-accuracy` README + architecture documentation — to be read in the next daily-research pass (carry-over to 2026-08-26).
- **Watch-list add to `le31-daily-research-2026-08-26` pass**: include `intel-retail/order-accuracy` in the 5-repo watch list to track star velocity + push activity + Intel-credibility signals.

## Open questions

1. **What is the exact GStreamer + OpenVINO pipeline structure in `intel-retail/order-accuracy`?** Is it a single-stage pipeline (capture → inference) or multi-stage (capture → preprocess → inference → postprocess)? The answer determines how transferable the pattern is to LE31 v2.
2. **Is the 2★ / 15-fork count maintained over the next 7 days?** The 1:7.5 ratio is the actionable signal; velocity at this ratio or higher is the gate. Star-only velocity without fork increase would be a weaker signal.
3. **Does `intel-retail/order-accuracy` require Intel-specific hardware?** The peer is positioned for Intel hardware + OpenVINO; LE31 v1 deployment on a single VPS + systemd unit (per charter §4.1) doesn't have Intel hardware. The answer informs whether the pattern is portable to LE31 v2 deployment context.
4. **Does the LE31 owner actually want a computer-vision surface?** This is a charter-level question that the artifact defers. The current charter (PROJECT_CHARTER.md §3) does not mention a computer-vision surface; features 30 + 49 + 81 + 108 + 111 + 112 v2 extension would need explicit charter approval.

## Why this matters

The 2026-08-25 brainstorm pass surfaces `intel-retail/order-accuracy` as the **freshest in-window push** and the **only in-window Intel-authored QSR reference implementation** for edge object detection + order accuracy. The cross-section insight: **LE31's v2 computer-vision surface (plate-accuracy, kitchen-display visual verification, stock-shelf visual verification) has a vendor-grade QSR-anchored Apache-2.0 permissive reference for edge object detection + order accuracy**. Apache-2.0 permissive license means any spec or pattern is reusable without license concerns for future v2 owner-pains extension.

**Cross-section with existing LE31 features**:
- Features 30 + 49 + 81 + 108 + 111 + 112 (audit-trail + audit-search + audit-trail-open-standard-alignment siblings) → this artifact (feature 114) is the audit-vision-verification sibling (vision as the next audit-layer primitive).
- Features 41 + 65 (cook-bot message-input surfaces) → these are the `StockEntry`-via-message sources; vision surfaces would be the `StockEntry`-via-vision input source.
- Features 67 + 68 + 90 + 113 (solo-operator + deterministic-gate + cook-assistant + voice-ordering siblings) → this artifact (feature 114) is the deterministic-gate-vision sibling.

**Why defer, not build**: zero observed pain at the LE31-owner level (no signal that the owner wants a computer-vision surface today); LE31 v1 doesn't ship one; the v2 extension is a future-tense concern; charter §3.5 AI non-customer-facing rule applies — vision must be gated on deterministic stock-state transitions, not free-form LLM calls. The artifact is a research-note that records the QSR edge-vision architecture for future v2 iteration.