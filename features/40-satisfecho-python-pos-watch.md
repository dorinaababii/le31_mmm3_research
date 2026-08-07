# Feature 40 — `satisfecho/pos` Python POS Watch

> **Priority**: P2 · **Effort**: XS (≤ 30 min) · **Source**: daily research 2026-08-07
> (Pick A) · **Bucket**: v1 ops tracking
> **One-line**: A tracking artefact that documents the
> [`satisfecho/pos`](https://github.com/satisfecho/pos) peer (22★, Python FastAPI
> + SQLModel + PostgreSQL + Angular + Redis + WebSocket, self-hosted multi-tenant
> POS with kitchen display + Stripe+Revolut payment, pushed 2026-08-02) on the
> LE31 charter dimensions, so the operator's build-vs-fork decision is made
> from evidence rather than from novelty.

## Goal

Keep the operator's due-diligence dossier current. Yesterday's `feature 36 —
self-hosted-pos-watch` named three in-window self-hosted POS references
(`vul-os/beepbite`, `illustraton916/vanhamylly-api`, `nkieu-config/branchbrew-cafe-erp`).
Today adds a fourth — `satisfecho/pos` — and prioritises it because it is the
**highest-starred in-window Python POS peer** that uses the **same stack as
LE31** (Python, FastAPI, SQLModel, PostgreSQL, WebSocket). Without this
tracking artefact, the operator has to re-discover the peer and re-derive the
comparison.

## Scope

**In scope (v1 ops tracking):**
- A single Markdown file (`features/40-satisfecho-python-pos-watch.md`, this
  document) that compares `satisfecho/pos` to LE31 on the charter dimensions.
- A one-row append to `INDEX.md`'s daily research log row (already done as
  HMM-44) and to the active feature pipeline table (already done as HMM-45).
- A pointer reference back to the existing `features/36-self-hosted-pos-watch.md`
  for the prior three-reference comparison.

**Out of scope (v1 ops tracking):**
- Re-implementing or forking `satisfecho/pos` — forking would inherit opinionated
  multi-tenancy, Stripe+Revolut, and an Angular frontend that LE31 explicitly
  does not want (charter §3 single-restaurant; charter §4 stack is FastAPI +
  SQLModel + aiogram — no Angular).
- Building a new feature. This is a documentation artefact; no code change.
- Evaluating the `satisfecho/pos` source code in depth. The README + topic tags
  are sufficient for the comparison.

## Description

`satisfecho/pos` is the highest-starred in-window Python POS peer. It is
self-hosted, multi-tenant, with a Stripe+Revolut payment integration, a
docker-compose deploy story, kitchen display, and a WebSocket transport. The
GitHub topics nailed by the project's README are the exact same as LE31's
charter stack:

| GitHub topic | LE31 charter match |
|---|---|
| `fastapi` | ✅ charter §4.1 — FastAPI |
| `sqlmodel` | ✅ charter §4.1 — SQLModel |
| `kitchen-display-system` | ✅ charter §3.1 — kitchen surface |
| `postgresql` | ✅ charter §4.1 — Postgres in production |
| `python` | ✅ charter §4.1 — Python 3.13 |
| `websocket` | ✅ adjacent to feature 23 (SSE cook channel) |
| `self-hosted` | ✅ charter §3 — single-restaurant self-host |
| `point-of-sale` / `restaurant-pos` | ✅ charter §3 — restaurant ops |
| `stripe` | ⚠️ out of v1 (charter §3 — no real money in v1) |
| `docker` | ✅ charter §4.1 — Docker |
| `multi-tenant` / `saas` | ❌ charter §3 — single-restaurant, not multi-tenant |
| `angular` / `typescript` | ❌ charter §4 — FastAPI + minimal HTML/HTMX, no Angular |
| `redis` | adjacent to v2 polish (charter §4.1 — Postgres in production) |

The match is strong on the **server-side stack** (Python + FastAPI + SQLModel
+ Postgres + WebSocket + Docker + Kitchen Display + Self-hosted) and **diverges
on the product surface** (multi-tenant SaaS, Stripe+Revolut, Angular frontend,
Redis). LE31 explicitly chooses the single-restaurant self-host path with a
minimal HTML/HTMX frontend, no real money in v1, and a Telegram-driven cook
surface (not a WebSocket KDS by default — feature 23 is the v1 polish).

The operator's reading of this artefact should be: "the LE31 stack is a real
production-shaped stack — `satisfecho/pos` is the proof — and the LE31 product
shape is intentionally different from this peer, so a fork is not warranted."

## Data model

None. No schema changes. No new tables. No new columns.

## Implementation

1. Read this file (you are doing it).
2. Read `satisfecho/pos` README at
   [https://github.com/satisfecho/pos](https://github.com/satisfecho/pos) — 30 min.
3. Read the existing `features/36-self-hosted-pos-watch.md` for the prior
   three-peer comparison.
4. Tick the box in `INDEX.md`'s active feature pipeline table (already added
   as HMM-45).
5. Commit: `git add features/40-satisfecho-python-pos-watch.md INDEX.md && git commit -m "Feature 40: satisfecho Python POS watch (tracking artefact)"`.

## Telegram interaction

None. This is a documentation artefact. No bot command, no Telegram surface.

## Dependencies

- `features/36-self-hosted-pos-watch.md` — the prior three-peer comparison; this
  feature's tracking artefact is a complement, not a replacement.
- The `satisfecho/pos` README at
  [https://github.com/satisfecho/pos](https://github.com/satisfecho/pos) — the
  source of the comparison rows.

## Open questions

- Should `satisfecho/pos` be added as a row to the existing `feature 36`
  comparison table, or kept in a separate `feature 40` file? Decision: separate
  file. The peer is the first Python stack-match to LE31, and the operator
  should be able to read the comparison in isolation. The daily-research
  report already cross-references both.
- Should the operator be encouraged to clone `satisfecho/pos` and read the
  source? Decision: not for v1; the topics + README are sufficient. Recording
  the URL and the topics as the comparison artefact is the right size for a
  ≤ 30 min tracking pick.

## Why this matters

`satisfecho/pos` is the first in-window Python POS peer that is both stack-
aligned (Python + FastAPI + SQLModel + Postgres + WebSocket + Docker) and
substantially production-shaped (22★, multi-tenant, Stripe+Revolut, kitchen
display, self-hosted). The operator's build-vs-fork decision needs this peer
visible, with the stack-match and product-divergence made explicit, so the
decision is made from evidence rather than from the LE31 founder's instincts
about the gap. The companion feature 42 (`self-hosted-pos-watch-3`)
synonymously updates the prior three-peer comparison table with two new in-
window rows.
