# Feature 42 — `self-hosted-pos-watch-3` (Update Slide)

> **Priority**: P2 · **Effort**: XS (≤ 30 min) · **Source**: daily research 2026-08-07
> (Pick C) · **Bucket**: v1 ops tracking (update slide onto `feature 36`)
> **One-line**: Two new in-window self-hosted POS references surface today
> (`satisfecho/pos` 22★, Python; `Ing-JuanDavid/restaurant-backend-POS` pushed
> 2026-08-07, Python FastAPI + SQLModel + PostgreSQL). Append them to the
> existing `feature 36` comparison table so the operator's due-diligence dossier
> stays current.

## Goal

Update the existing `feature 36 — self-hosted-pos-watch` (filed 2026-08-06) to
include two new in-window self-hosted POS references that surfaced in today's
window. The operator's due-diligence dossier should not require re-reading the
prior three-peer comparison + today's two new peers + today's
`satisfecho-python-pos-watch` in isolation; instead, the dossier should be
**one feature file that identifies all five in-window references** and makes
the LE31 stack-vs-shape divergence explicit.

This feature is a tracking artefact — no code change. It is filed as a
**separate feature file** rather than a patch to `feature 36` because:

1. The added peers are the first Python stack-matches to LE31 (yesterday's
   three peers were Go, Node.js, and NestJS/TypeScript). The structural
   finding is new.
2. Numbering is 42 (continuing the daily-research counter), so the file
   trails `feature 41` in the active pipeline table.

## Scope

**In scope (v1 ops tracking):**
- A single Markdown file (`features/42-self-hosted-pos-watch-3.md`, this
  document) that complements `feature 36` with the two new peers.
- A one-row append to `INDEX.md`'s active feature pipeline table (already
  done as HMM-47).

**Out of scope (v1 ops tracking):**
- Re-implementing or forking any of the listed peers.
- Building a new feature. This is a documentation artefact.
- A full evaluation of either new peer. The README + topic tags are
  sufficient for the comparison.

## Description

Yesterday's `feature 36` enumerated three in-window self-hosted POS
references:

| Peer | Stack | Pushed | Stars | Topic tags |
|---|---|---|---|---|
| `vul-os/beepbite` | Go + React | 2026-08-06 (carry-over, day 6) | 1★ | `golang`, `kds`, `offline-first`, `multi-currency`, `restaurant`, `self-hosted` |
| `illustraton916/vanhamylly-api` | Node.js + Express + PostgreSQL | 2026-08-03 (carry-over) | 0★ | `docker`, `express`, `nodejs`, `postgresql`, `restaurant`, `telegram-bot`, `websocket` |
| `nkieu-config/branchbrew-cafe-erp` | NestJS + TypeScript + PostgreSQL | 2026-08-05 (carry-over) | 0★ | `docker`, `double-entry-accounting`, `erp`, `event-driven-architecture`, `inventory-management`, `monorepo`, `nestjs`, `nextjs`, `point-of-sale`, `postgresql`, `prisma`, `transactional-outbox`, `typescript`, `websockets` |

Today adds two more:

| Peer | Stack | Pushed | Stars | Topic tags |
|---|---|---|---|---|
| `satisfecho/pos` | Python + FastAPI + SQLModel + PostgreSQL + Angular + Redis + WebSocket | 2026-08-02 | 22★ | `fastapi`, `sqlmodel`, `kitchen-display-system`, `postgresql`, `python`, `websocket`, `self-hosted`, `point-of-sale`, `restaurant-pos`, `stripe`, `docker`, `multi-tenant`, `redis` |
| `Ing-JuanDavid/restaurant-backend-POS` | Python + FastAPI + SQLModel + PostgreSQL | 2026-08-07 (today) | 0★ | (no topics; structure: `app/`, `alembic/`, `alembic.ini`, `.gitignore`) |

**Structural findings**:

- **Five self-hosted restaurant systems in a 7-day window.** This is the
  strongest convergence signal yet. The operator's "is LE31 alone in the
  niche?" question is now answerable: no, five peers are active in the
  same week. LE31's positioning is the **single-small-restaurant self-hosted
  Python stack with a Telegram cook surface** — that combination is unique
  among the five.
- **First Python stack-matches surfaced.** Yesterday's three peers were
  Go, Node.js, and NestJS/TypeScript — none matched LE31's Python stack.
  Today's two new peers are Python; one is the exact stack match
  (FastAPI + SQLModel + PostgreSQL).
- **First in-window peer with high star count.** `satisfecho/pos` at 22★
  is the first in-window peer with non-trivial adoption. The other four
  peers are 0–1★.
- **No new evidence on the append-only `StockEntry` ledger pattern.**
  None of the five peers implements a true append-only `StockEntry` ledger
  for prepared items. The killer pattern remains a defensible
  differentiator (same as previous 9 daily reports).

## Data model

None. No schema changes. No new tables. No new columns.

## Implementation

1. Read this file (you are doing it).
2. Read the existing `features/36-self-hosted-pos-watch.md` for the prior
   three-peer comparison.
3. Read the `satisfecho/pos` README at
   [https://github.com/satisfecho/pos](https://github.com/satisfecho/pos)
   — 30 min.
4. Browse the `Ing-JuanDavid/restaurant-backend-POS` repository at
   [https://github.com/Ing-JuanDavid/restaurant-backend-POS](https://github.com/Ing-JuanDavid/restaurant-backend-POS)
   — 10 min (no README on `main`; skim the `app/` directory structure).
5. Tick the box in `INDEX.md`'s active feature pipeline table (already
   added as HMM-47).
6. Commit: `git add features/42-self-hosted-pos-watch-3.md INDEX.md && git commit -m "Feature 42: self-hosted POS watch 3 (tracking artefact; 5 in-window peers)"`.

## Telegram interaction

None. This is a documentation artefact. No bot command, no Telegram
surface.

## Dependencies

- `features/36-self-hosted-pos-watch.md` — the prior three-peer
  comparison; this feature's tracking artefact is a complement, not a
  replacement.
- `features/40-satisfecho-python-pos-watch.md` — the in-depth comparison
  of `satisfecho/pos` on the LE31 charter dimensions. This feature
  provides the five-peer context; feature 40 provides the single-peer
  depth.

## Open questions

- Should the existing `feature 36` comparison table be **extended** to
  five rows, or **superseded** by this `feature 42`? Decision: keep
  both. `feature 36` documents the prior three; `feature 42` documents
  the new two and the structural finding. The two files together make
  the dossier complete.
- Will the operator want a 6th peer in tomorrow's window? Unknown — the
  convergence signal is strong, so the active feature pipeline should
  expect 1–2 new self-hosted peers per week. The `feature 36 / 42` /
  `feature 40` trio is the operator's current reading list.

## Why this matters

The operator's "is the LE31 niche crowded?" question is now answerable:
**yes, five self-hosted restaurant systems are active in the same week.**
LE31's positioning is the **single-small-restaurant self-hosted Python
stack with a Telegram cook surface** — that combination is unique among
the five. The convergence signal is strong enough that the operator
should be on a quarterly cadence for re-reading the comparison, not a
weekly one. This feature is the operator's evidence-based answer to the
"is LE31 alone?" question.
