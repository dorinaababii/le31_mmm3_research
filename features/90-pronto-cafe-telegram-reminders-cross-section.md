# Feature 90 — pronto-cafe-telegram-reminders-cross-section

> **NEW observation (2026-08-21).** Documents the in-window
> `SGrappelli/pronto` companion-repo signal observed during the
> 2026-08-21 daily brainstorm (see
> `/opt/data/le31-brainstorm-2026-08-21.md`, Pick A).
> Bucket: **v2 owner-pains (watch-list, cross-section peer)** — hard
> defer pending charter §3.1 surface-expansion review.

## Goal

Record the **in-window Pronto cross-section peer** — the highest
mid-adoption (★39) cross-section signal seen in the 22-pass series for
LE31's cook-Telegram-bot surface. Pronto proves that a small-business
self-hosted POS uses **both WhatsApp and Telegram** for reminders. The
pattern is direct: LE31's cook bot surface (features 33, 41, 60) is
Telegram-only; Pronto chose dual-channel. The cross-section question
("should LE31 v2 expand to WhatsApp?") is a **charter-level scoping
decision** that the artifact explicitly defers.

## Scope

**In scope:**
- Daily direct-repo `GET https://api.github.com/repos/SGrappelli/pronto`
  (via `$HERMES_GITHUB_TOKEN`).
- Reading the Pronto README in the next daily-research pass to confirm
  the WhatsApp + Telegram reminders pattern.
- Tracking star velocity + push activity on `SGrappelli/pronto`.
- Documenting the cross-section pattern in the LE31 research notes.

**Out of scope (v1 / v2):**
- Importing any code from `SGrappelli/pronto` (TypeScript stack
  mismatch; LE31 is Python+FastAPI).
- Building a WhatsApp channel for LE31's cook bot (charter §3.1 says
  Telegram-only; WhatsApp expansion needs explicit charter approval).
- Building any feature based on the Pronto code surface.

## Description

### `SGrappelli/pronto`

|| Date | Stars | Pushed | License | Language |
||---|---|---|---|---|---|
|| 2026-08-21 (baseline) | 39★ | 2026-08-19 | (not checked) | TypeScript |

**Direct repo URL**: https://github.com/SGrappelli/pronto

**Verbatim description** (from GitHub API):
> Open-source booking, CRM & POS for salons, barbershops, cafes and
> shops. Zero commission. WhatsApp & Telegram reminders. Self-hosted
> via Docker.

**Why this is the cross-section peer of the pass:**

1. **Telegram + WhatsApp are the two default small-business bot channels.**
   Pronto chose both. LE31's bot is Telegram-only (charter §3.1).
2. **Self-hosted Docker is the dominant deployment shape** for
   small-business POS. Pronto is Docker; LE31 is Python+FastAPI+
   Postgres (also self-hostable).
3. **Zero-commission is the small-business pricing posture.** Pronto
   is explicit; LE31 is for one restaurant, not a SaaS, so commission
   is irrelevant.

**Cross-section peers in this 30-day window** (from the same
`topic:small-business` query):
- `lsfusion-solutions/mycompany` (★317, pushed 2026-08-19) — full
  ERP/CRM/POS, JavaScript + lsFusion stack.
- `ConsciousUniverse/simple-stock-management` (★181, pushed 2026-07-28)
  — Python stock & inventory.
- `dragotin/kraft` (★79, pushed 2026-08-19) — C++ quotes & invoices.
- `nicolettas-muggelbude/RechnungsFee` (★65, pushed 2026-08-20) —
  TypeScript offline-first invoicing.
- `djfksjd/sole-search` (★45, pushed 2026-07-30) — Python Korean
  small-business public-data agent (feature 82).
- `SGrappelli/pronto` (★39, pushed 2026-08-19) — **this pick**.
- `celerp/celerp` (★23, pushed 2026-08-21) — Python self-hosted
  desktop ERP.
- `oathdriven/icm-folder-system` (★8, pushed 2026-08-17) — plain-text
  folder-as-database.

**Why ★39 is the right mid-adoption threshold**: lower than ★45
(`djfksjd/sole-search` already filed as feature 82, deferring because
the JFKS surface is Korean-only); higher than ★23 (`celerp/celerp`,
no restaurant alignment). Pronto is the **only** in-window peer
combining: (a) ★25+ stars, (b) cafe/booking/CRM/POS, (c) WhatsApp +
Telegram reminders, (d) self-hosted Docker. The unique combination is
the cross-section.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 33 `telegram-walkin-pin` | Telegram channel for walk-in reservations | Telegram-only; Pronto adds WhatsApp |
| 41 `telegram-msg-stock-update` | Telegram message → stock update | Telegram-only; Pronto adds WhatsApp |
| 60 `restaurant-telegram-front-desk-mirror` | Telegram front-desk mirror for restaurant | Telegram-only; Pronto adds WhatsApp |
| 82 `owner-public-data-watch-bot` | Owner-relevant public-data bot | Different surface (public-data, not reminders) |

This pick is **NOT** a duplicate of any existing feature. It is a
**cross-section peer observation** that surfaces a charter-level
question ("should LE31 expand to WhatsApp?") that the existing feature
pipeline has not yet reached.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation, not a feature build.

## Implementation

1. Read the `SGrappelli/pronto` README in the next daily-research pass
   via `curl -sS` to
   `https://raw.githubusercontent.com/SGrappelli/pronto/main/README.md`
   (or whatever branch the active push targets). Confirm the WhatsApp
   + Telegram reminders pattern.
2. Continue daily direct-repo GET on Pronto to track star velocity +
   push activity.
3. If the README confirms the WhatsApp + Telegram pattern + the
   Telegram reminder surface is documented, document the pattern in
   the LE31 research notes (this artifact is the document).
4. **No build implied.** The pick is a watch-list observation. The
   "should LE31 expand to WhatsApp?" question is parked pending
   charter §3.1 surface-expansion review.

## Telegram interaction

None. This is a passive observation; no cook or manager action.

## Dependencies

- `$HERMES_GITHUB_TOKEN` for the daily direct-repo GET (already in
  `/opt/data/.env`).

## Open questions

- Does the Pronto README confirm the WhatsApp + Telegram reminders
  pattern with a documented API surface?
- Does Pronto have a public webhook or event API that LE31 could
  integrate against (e.g., for a future "Telegram bridge to Pronto
  reminders" surface)?
- Does the Pronto license permit derivative works (the README should
  confirm; many self-hosted POS are MIT, but Pronto may be AGPL or
  commercial)?
- Is the "expand to WhatsApp" question on the LE31 charter roadmap
  (charter §3.1 currently says Telegram-only)? If yes, this pick
  becomes a build candidate. If no, the pick stays parked.

## Why this matters

The Pronto cross-section peer is the **only in-window mid-adoption
(★25-50) peer** that combines: (a) small-business self-hosted POS, (b)
WhatsApp + Telegram reminders, (c) cafe/booking/CRM surface. The
pattern is direct and worth documenting. The cross-section signals
that the small-business self-hosted POS market is converging on dual-
channel bot reminders (Telegram + WhatsApp). LE31's charter §3.1
currently says Telegram-only; the "expand to WhatsApp" question is a
charter-level decision that Pronto's existence supports but does not
yet require. The artifact is filed as a watch-list entry with a clear
re-evaluation trigger so the next research pass knows what to look
for.
