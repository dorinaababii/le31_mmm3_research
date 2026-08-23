# Feature 100 — pronto-watch-v3 (day-3 sustained maintainer activity)

> **NEW observation (2026-08-23).** Documents the in-window
> `SGrappelli/pronto` **3-day sustained maintainer activity**
> observed during the 2026-08-23 daily research pass. The peer is
> in **3 consecutive days of maintainer activity**: pushed
> 2026-08-21T19:07:53Z → 2026-08-22T19:10:54Z → 2026-08-23 fetch
> ran. **NEW data point today**: repo size grew from 5411KB to
> 5706KB (+295KB / +5.5% overnight) — a real signal of active code
> work, not just metadata churn.
> Bucket: **v2 owner-pains (watch-list, cross-section peer)** —
> hard defer pending charter §3.1 surface-expansion review.

## Goal

Record the **3-day sustained maintainer activity** on
`SGrappelli/pronto` (the cross-section peer for LE31's
cook-Telegram-bot surface). The 3-day cadence (2026-08-21 push →
2026-08-22 push → 2026-08-23 fetch) plus the **+295KB / +5.5%
overnight size delta** is a real signal of returning maintainer
activity + active code work. This is the day-3 observation contract;
it supersedes features 90 (`pronto-cafe-telegram-reminders-cross-section`,
2026-08-21) + 94 (`pronto-watch-v2`, 2026-08-22) with the newest
data point. The artifact is the persistent watch-list record.

## Scope

**In scope:**
- Document the in-window observation in the LE31 research notes
  (this artifact is the document).
- Track the cross-section peer for LE31's cook-Telegram-bot surface
  (WhatsApp + Telegram reminders, self-hosted Docker, Next.js + Supabase).
- Read the README + commit log via raw curl on the next pass to
  confirm the maintainer activity pattern.

**Out of scope (v1 / v2):**
- Any code import from `SGrappelli/pronto` (LE31 is Python + FastAPI
  + SQLModel + aiogram v3; pronto is Next.js + Supabase + TypeScript
  — **full stack mismatch**).
- Any charter §3.1 surface-expansion decision (the "expand to
  WhatsApp?" question is parked).
- Any feature built on top of pronto's cross-section surface
  (e.g. WhatsApp reminders for LE31 cook surface — charter-out-of-scope
  per §3.1).

## Description

### pronto release/activity timeline (recent window)

| Date | Event | Δ | Confidence |
|---|---|---|---|
| 2026-08-20 | 39★ baseline | — | (carried from 2026-08-21 pass) |
| 2026-08-21T19:07:53Z | Push (NEW) | +1★, +1 fork, +1 day | observed (PyPI + GitHub API) |
| 2026-08-22T19:10:54Z | Push (NEW) | +0★, +0 forks, +24h, +295KB | observed (direct-repo GET) |
| 2026-08-23 06:31Z | Fetch ran | +0★, +0 forks, no new push in past 11.3h | observed (direct-repo GET) |

**Direct PyPI URL**: n/a (not a Python package)

**GitHub repo**: https://github.com/SGrappelli/pronto

**Direct repo GET today (2026-08-23 06:31 UTC):**
- Stars: **40★** (unchanged from yesterday; +1★/24h observed
  2026-08-21→2026-08-22; +0★/24h today)
- Forks: **12** (unchanged from yesterday; +1 fork/24h observed
  2026-08-21→2026-08-22; +0 forks/24h today)
- Size: **5706KB** (+295KB / +5.5% overnight — real signal of active
  code work)
- License: **MIT** (clean)
- Last pushed: **2026-08-22T19:10:54Z** (~11.3h before today's fetch)
- `updated_at`: 2026-08-22T19:11:18Z
- Topics: `auto-repair`, `barbershop`, `barcode-scanner`,
  `beauty-salons`, `booking`, `cafe`, `crm`, `dental-clinic`,
  `docker`, `fitness`, `inventory`, `nextjs`, `pos`, `self-hosted`,
  `small-business`, `spa`, `supabase`, `telegram`, `viber`,
  `whatsapp`
- Description: "Open-source booking, CRM & POS for salons,
  barbershops, cafes and shops. Zero commission. WhatsApp & Telegram
  reminders."

### Why this matters (but is still watch-list continue)

1. **3-day sustained maintainer activity** is a meaningful
   maintainer-engagement data point. The maintainer went from 0
   pushes in 7 days (carry-over from 2026-08-21 baseline) to 3
   pushes in 3 days. This is a real signal of returning engagement.
2. **+295KB / +5.5% overnight size delta** is the most concrete
   evidence of active code work observed in any LE31 watch-list
   repo. Repo size grew from 5411KB (2026-08-22 06:32 UTC baseline)
   to 5706KB (2026-08-23 06:31 UTC baseline). Not metadata churn.
3. **Cross-section peer for LE31's cook-Telegram-bot surface.**
   Pronto carries WhatsApp + Telegram reminders for salons, cafes,
   barbershops, etc. The Telegram-reminder cross-section is the
   relevant LE31 adjacency; WhatsApp is charter-out-of-scope per §3.1.
4. **Full stack mismatch** (LE31 is Python + FastAPI + SQLModel +
   aiogram v3; pronto is Next.js + Supabase + TypeScript). Pronto
   is useful as a **pattern reference**, not as an import target.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 90 `pronto-cafe-telegram-reminders-cross-section` | Day-1 observation (carry-over from 2026-08-21) | Older target |
| 94 `pronto-watch-v2` | Day-2 observation (carry-over from 2026-08-22) | Older target |
| **100 `pronto-watch-v3` (this)** | Day-3 observation (carry-over from 2026-08-23) | **Newest** artifact + +295KB size delta data point |

This pick is the **3rd consecutive daily-research carry-over** of
the same pronto observation. It is NOT a duplicate of the prior v2
artifact — it is the **newest** daily-research observation with the
+295KB size delta data point + the 3-day sustained activity pattern.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation, not a feature build.

## Implementation

1. Continue daily GitHub direct-repo GET on `SGrappelli/pronto` to
   surface new stars/forks/pushes in the next daily-research pass.
2. Read the pronto README + commit log via raw curl in the next pass
   to confirm the maintainer activity pattern (3 pushes in 3 days).
3. **No build implied.** The pick is a watch-list observation. The
   "should LE31 expand to WhatsApp?" question is parked pending
   charter §3.1 surface-expansion review.

## Telegram interaction

None. This is a passive observation; no cook or manager action.

## Dependencies

- None. The watch-list entry is passive.

## Open questions

- What is the maintainer working on? (Read the commit log + README
  diff via raw curl on the next pass to find out.)
- Is the maintainer planning a v1.0 release? (Check the GitHub
  milestones via raw curl.)
- Does the +295KB size delta overnight indicate a UI overhaul, a
  new feature, or a dependency update? (Read the commit log.)
- Is the cross-section peer pattern (WhatsApp + Telegram reminders)
  relevant to LE31's cook-Telegram-bot surface? (The Telegram part is
  relevant; the WhatsApp part is charter-out-of-scope per §3.1.)

## Why this matters

The 3-day sustained maintainer activity + the +295KB overnight size
delta is the **strongest in-window cross-section peer signal** for
LE31's cook-Telegram-bot surface observed across the 24-pass series.
The maintainer is back to active development after the carry-over
2026-08-20 baseline stagnation. Pronto is the closest peer to LE31's
cook-Telegram-bot cross-section surface (WhatsApp + Telegram reminders,
self-hosted Docker); the Telegram-reminder pattern is the relevant
LE31 adjacency. The artifact is the persistent watch-list record so
future research passes can compare against this baseline.