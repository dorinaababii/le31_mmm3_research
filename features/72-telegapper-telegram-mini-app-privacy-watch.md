# Feature 72 — TeleGapper Telegram Mini App Privacy Watch

> **Priority**: P3 (watch-list) · **Effort**: S (research-only, no
> code) · **Source**: daily research 2026-08-16 (Pick C, **NEW** v2-AI
> watch-list) · **Bucket**: **v2-AI** (Telegram-Mini-App privacy
> watch-list)
> **One-line**: A research-only watch-list artifact that records the
> in-window arXiv paper **TeleGapper: On the (un)reliability of
> Privacy Policies in Telegram Mini apps** (arXiv:2608.13390,
> 2026-08-13, cs.CR, Ferrari/Ceccato/Verderame). The paper's findings
> — **59.4% of Telegram Mini Apps contact an undisclosed third party;
> 78.8% rely exclusively on Telegram's default privacy policy; none
> provides a consent or opt-out mechanism** — establish a baseline
> data point that future v2-AI scope work (a hypothetical Telegram
> Mini App waiter-side surface) can reference. **LE31 v1 ships a
> chat-based bot, not a Mini App, so the impact is watch-list only.**

## Goal

The TeleGapper paper is the **first in-window arXiv paper directly
relevant to LE31's Telegram surface**. While LE31 v1 ships a
**chat-based** Telegram bot (aiogram v3), the LE31 product surface
has a natural v2-AI extension: a Telegram Mini App for the waiter
side (a mobile-native waiter app that complements the existing
web-based waiter UI from feature 02).

If LE31 ever ships a Telegram Mini App surface, the privacy-policy
obligation is **non-trivial**:

- 59.4% of existing Mini Apps contact an undisclosed third party →
  LE31 must audit its Mini App's third-party network traffic if shipped.
- 78.8% rely on Telegram's default privacy policy → LE31 must ship
  an **application-specific privacy policy** if it ships a Mini App.
- None of the surveyed Mini Apps provides a consent or opt-out
  mechanism → LE31 must ship a consent/opt-out mechanism if it ships
  a Mini App.

This slice ships **zero code**; the slice ships **one watch-list
artifact** that future v2-AI scope work can reference. The slice
boundary is hard: one Markdown file update, zero source code changes,
zero migrations, zero new dependencies.

## Scope

**In scope (v2-AI watch-list, S effort, ≤1 day, defer):**

- One source-file edit: this
  `features/72-telegapper-telegram-mini-app-privacy-watch.md` artifact
  (the watch-list record).
- The corresponding HANDOFF.md under `specs/`.
- The corresponding row in `INDEX.md` "Active feature pipeline" table.

**Out of scope (deferred to a future v2-AI scope):**

- A new LE31 Telegram Mini App surface. That is a separate v2-AI
  scope item; not this slice.
- A new LE31 privacy policy. LE31 v1 has no privacy policy today
  (charter §3.2 explicitly notes that v1 guest demographics are
  counts, not identity/contact data; no privacy policy obligation
  under GDPR Article 13 for v1 data). A Mini App surface would
  require a separate v2-AI scope decision.
- A LE31 consent / opt-out mechanism. Same as above.
- A LE31 Mini App third-party audit framework. Same as above.

## Description

**Evidence precondition:** observed (verified via the arXiv API;
TeleGapper paper arXiv:2608.13390, cs.CR, 2026-08-13T15:51:18Z,
authors Luca Ferrari, Mariano Ceccato, Luca Verderame).

**Confidence:** **high** for the empirical findings (59.4% / 78.8% /
none); **medium** for the v2-AI applicability to LE31 (LE31 v1 is a
chat-based bot, not a Mini App; the Mini App surface is a future
v2-AI extension of the waiter web UI).

**Paper abstract summary:**

> "Telegram Mini Apps are Web applications embedded within the
> Telegram client, forming an ecosystem of third-party services
> within one of the world's most widely used messaging platforms.
> Despite their growing adoption and access to Telegram-provided
> context, their privacy properties remain largely unexplored.
> [TeleGapper] assess[es] the privacy posture of Mini Apps by
> capturing runtime network traffic, identifying third-party
> communications, and comparing observed data flows against
> disclosed privacy information. We evaluate 278 working Mini Apps
> collected from tApps Center. We find that **59.4% contact at least
> one undisclosed third party**, **78.8% rely exclusively on
> Telegram's default privacy policy**, and **none provides a consent
> or opt-out mechanism**. These findings expose a substantial
> transparency and compliance gap in a widely used yet understudied
> ecosystem."

**Cross-validation anchors:**

- **`Show HN: SquadCue – local-first mission control for AI CLI
  agents`** (2026-08-11 carry-over, HN) — Telegram-as-push-channel
  for an AI/agent backend is a recognized 2026 pattern; Telegram is
  increasingly used as a surface for AI/agent applications.
- **`Show HN: Captain, AI Travel Agent`** (2026-08-14, HN) —
  Telegram-bot-for-travel pattern; not restaurant-tech but confirms
  the Telegram-bot-as-2026-architecture trend.

**Decision: defer (v2-AI watch-list).** The slice boundary is hard:
one Markdown file update, zero source code changes, zero migrations,
zero new dependencies.

## Data model

No data model changes. The slice is a pure watch-list artifact.

## Implementation steps

1. **Append a row** to `/opt/data/INDEX.md` "Active feature pipeline"
   table with date 2026-08-16, pick
   `telegapper-telegram-mini-app-privacy`, feature path
   `features/72-telegapper-telegram-mini-app-privacy-watch.md`,
   Linear sub-issue ID (TBD), status "v2-AI Watch-list (defer)".
2. **If/when a v2-AI Telegram Mini App scope is opened** in a future
   pass, reference this artifact in the scope decision to anchor the
   privacy-policy obligation.

## Telegram interaction

None today. The slice is a watch-list artifact; the hypothetical
future v2-AI Telegram Mini App surface would have its own
Telegram-interaction contract (out of scope for this slice).

## Dependencies

- The `/opt/data/INDEX.md` file — must be writable.
- Future v2-AI scope work must reference this artifact if a Telegram
  Mini App surface is proposed.

No new pip dependencies. No new system dependencies. No new external
services.

## Open questions

- **Q1: Will LE31 ever ship a Telegram Mini App surface?** Currently
  NOT in v1 charter §3.2. A Mini App surface would require a charter
  revision (analogous to the walk-in-front-desk-channel feature 56
  which is in Backlog pending charter §5 revision). **Scope this as
  a separate question, not this slice.**
- **Q2: If a Mini App is shipped, what third-party services would it
  contact?** The Mini App's network traffic would need to be audited
  against the TeleGapper framework to ensure no undisclosed third
  party. **Out of scope today.**
- **Q3: If a Mini App is shipped, should it ship its own privacy
  policy or rely on Telegram's default?** Per the 78.8% finding,
  relying on Telegram's default is the majority pattern but is also
  the compliance gap that TeleGapper flags. **LE31 should ship its
  own privacy policy if a Mini App is shipped.** **Out of scope today;
  this artifact records the data point.**

## Why this matters

The TeleGapper paper establishes a **concrete 2026-08 baseline
data point** for the Telegram-Mini-App privacy compliance gap. If
LE31 ever ships a Telegram Mini App surface (a natural extension of
the waiter web UI from feature 02), the privacy-policy obligation
must be **explicit**:

- An application-specific privacy policy (the 78.8% finding flags
  default-policy reliance as a transparency gap).
- An audit of third-party network traffic (the 59.4% finding flags
  undisclosed third-party contact as a transparency gap).
- A consent / opt-out mechanism (the "none" finding flags the absence
  of consent as a compliance gap).

This artifact records the data point so future v2-AI scope work does
not have to rediscover it.

**Risk of NOT tracking:** a future v2-AI scope decision on a Telegram
Mini App surface would lack the TeleGapper baseline and would have
to rediscover the privacy-policy obligation. **The artifact prevents
that rediscover cost.**

**Risk of over-tracking:** the artifact is a research-note; over-use
of it would be in a future scope decision (not this slice). **No
over-tracking risk today.**

## Status: v2-AI watch-list (defer)

This file is a **v2-AI watch-list artifact (defer)**. The slice
boundary is hard: one Markdown file update, zero source code changes,
zero migrations, zero new dependencies. No code change today. The
research-side subagent (Pass 17, 2026-08-16) records the
TeleGapper baseline data point for future v2-AI scope reference.
