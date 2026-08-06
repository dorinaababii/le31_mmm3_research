# Feature 36 — Self-Hosted POS Watch

## Goal

Record, in a single durable artefact, the three independent self-hosted
restaurant systems that surfaced in the 2026-07-30 → 2026-08-06 daily
research window, so the operator (and the coding agent) can compare
them against LE31's charter without re-discovering them at decision
time.

## Scope

**In scope (v1 ops, no code change):**
- A single Markdown document at `features/36-self-hosted-pos-watch.md`
  (this file) that lists the three references with: stack, key
  features, GitHub URL, last-touched date, star count, and the
  one-paragraph "what LE31 can learn" note.
- A pointer row in `INDEX.md` so the next agent picks up the artefact.

**Out of scope (v1):**
- A formal benchmark or feature-by-feature matrix — too expensive for a
  30-minute artefact; can be added later if the operator asks.
- Forks of any of the three references — LE31's charter forbids
  multi-stack drift.
- Adoption of any library or framework from the three references —
  the artefact is observational only.

## Description

In the 2026-07-30 → 2026-08-06 research window, three independent
self-hosted restaurant systems were active on GitHub:

1. **[`vul-os/beepbite`](https://github.com/vul-os/beepbite)** — Go
   1.25 + React 19, self-hostable, MIT/Apache-2.0, "no platform fee".
   POS till + kitchen display + floor plan + menu management +
   inventory + purchase orders. Channel-agnostic ordering today
   (WhatsApp, QR storefront, web); Discord/Slack/email adapters planned.
   **Status: pre-1.0, under active rebuild.** Pushed every day this
   week (2026-08-01 → 2026-08-06). **What LE31 can learn**: confirms
   the self-hosted-POS niche is alive for solo operators. Different
   stack (Go) but the architecture (POS + KDS + inventory + purchase
   orders as a single self-hosted deploy) maps directly to LE31's
   charter.

2. **[`illustraton916/vanhamylly-api`](https://github.com/illustraton916/vanhamylly-api)** —
   Node.js 20 + Express + PostgreSQL 16, **production restaurant
   backend powering a real restaurant in Finland**. REST API + QR
   ordering from table + **Telegram bot as the sole admin panel** +
   **WebSocket KDS** (`/ws/kitchen`) + ESC/POS receipt + kitchen-ticket
   printing + SumUp card payments. Money is integer cents only, i18n
   via `_fi/_ua/_en` columns, three-tier auth (public/internal/staff).
   Topics: docker, express, nodejs, postgresql, restaurant,
   telegram-bot, websocket. **What LE31 can learn**: the production
   reference for "Telegram bot is the only admin panel" — direct
   validation of LE31's charter §4.1 choice of aiogram as the cook
   surface. Different stack (Node.js vs Python) but the architecture
   transfers.

3. **[`nkieu-config/branchbrew-cafe-erp`](https://github.com/nkieu-config/branchbrew-cafe-erp)** —
   NestJS + Next.js 16 + Prisma 7 + PostgreSQL + Docker ERP, 23
   backend modules, 131 REST endpoints, 41-table schema, 464
   automated tests, realtime kitchen display, **double-entry general
   ledger**, load-tested to **150 orders/sec**. Live demo at
   `branchbrew-cafe-erp.vercel.app`. **What LE31 can learn**: the
   most ambitious solo-built restaurant system seen this window. The
   double-entry general journal is a **wider** primitive than LE31's
   append-only `StockEntry` (feature 03); reading both confirms that
   LE31's narrow primitive is the right one for prepared-item stock
   and that a full general journal is unnecessary for v1.

| Reference | Stack | Production? | KDS? | Telegram? | Stock ledger? | Last touched (2026-08-06 window) |
|---|---|---|---|---|---|---|
| `vul-os/beepbite` | Go + React | No (pre-1.0) | Yes | No | Yes (purchase orders) | 2026-08-06 |
| `illustraton916/vanhamylly-api` | Node.js + Express | **Yes (real restaurant)** | Yes (WebSocket) | **Yes (admin panel)** | Integer cents, no strict ledger | 2026-08-03 |
| `nkieu-config/branchbrew-cafe-erp` | NestJS + Next.js | Yes (live demo) | Yes | No | Double-entry general journal | (carried over from 2026-08-05) |

## Data model

None. This is a documentation artefact only.

## Implementation

None. The file is this document; no code changes are required.

To keep the artefact fresh, the daily research cron should re-run the
`restaurant POS language:python` and `telegram kitchen` GitHub queries
each day and update the "Last touched" column when a reference
surfaces again. Estimated cost: ≤ 30 seconds of curl + a one-line
edit to this file.

## Telegram interaction

None.

## Dependencies

- Daily research report `/opt/data/le31-daily-research-YYYY-MM-DD.md`
  — the source for the "Last touched" column.
- LE31 charter `PROJECT_CHARTER.md` §3.1 — the scope this artefact
  measures the references against.

## Open questions

- Should this file be promoted to a full benchmark (feature-by-feature
  matrix)? Default: no, only if the operator asks.
- Should the references be forked into `research/13-peer-architecture-comparison.md`
  (already shipped 2026-08-05)? They overlap; the answer is "this file
  is the operational pointer, `research/13-peer-architecture-comparison.md`
  is the architectural analysis". Future daily runs should cross-link.
- Should `beepbite` be re-evaluated when it ships 1.0? Yes, but
  out of scope for this artefact — record it as a future daily-research
  trigger.

## Why this matters

When the operator (or the next coding agent) eventually asks "why
didn't we just fork `beepbite` / `vanhamylly-api` / `branchbrew-cafe-erp`?",
the answer should be a one-link reference rather than a re-read of
seven days of daily research reports. This file is that reference.
