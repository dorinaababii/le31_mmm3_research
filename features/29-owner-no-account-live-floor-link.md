# Feature 29 — Owner No-Account Live-Floor Link

> **Priority**: P2 · **Effort**: M (3–5 days) · **Source**: brainstorm
> 2026-08-04 (cross-section pick B) · **Bucket**: v2 owner-pains
> **One-line**: Owner generates a signed expiring link from the existing cook
> bot (`/ownerlink`); the link opens a single-page htmx view of the floor
> (table states, last 10 orders, prep-time histogram, today's cover count,
> reorder line). No install, no account.

## Goal

Let the owner see the current state of the restaurant from any phone, at
any time, without installing an app or remembering a password. The owner is
also the operator in a small restaurant, and the off-floor decision moments
(supplier run, sick day, child pickup) are exactly when they need to know
"is everything OK?" — but today the only owner surface is the same login as
the waiter, which is the wrong friction for an off-floor glance.

Inspired by the no-account cluster that surfaced in today's GitHub
`topic:small-business` search: `Sreenivas-Sadhu-Prabhakara/slotone` ("A
private, offline appointment day-book for a one-person business. No
accounts…"), `slipbook` ("Free invoice & receipt maker, no sign-up."),
`Sreenivas-Sadhu-Prabhakara/shelftrack` ("100% offline, nothing leaves your
device."). Three repos from the same author, all built around the same
primitive: zero-install, zero-account, ephemeral-share-link, photo-in or
CSV-out. LE31's owner is the same kind of solo operator; the primitive fits.

## Scope

**In scope (v2 owner-pains):**
- New cook-bot command `/ownerlink` that returns a single signed URL of
  the form `https://<host>/owner/<token>`. The token is a `secrets`
  `token_urlsafe(32)` string, signed with the existing `SECRET_KEY`
  (charter §3.2). The token is hashed (SHA-256) and stored in a new
  `OwnerLink` row with `expires_at = now() + 12h`. The raw token is only
  in the URL; the database only stores the hash.
- New FastAPI route `GET /owner/<token>`:
  - If the hashed token matches an unexpired `OwnerLink` row, render a
    single-page Jinja2 template (`owner.html`) with htmx loaded from
    CDN.
  - If expired or unknown, return 410 Gone.
  - No login, no cookies, no session. Each request validates the signed
    token from scratch.
- The page shows:
  - Table states (`free`, `seated`, `ordered`, `billed`, `dirty`) as a
    colored grid (reuses the index.html floor mock-up, no drag-and-drop
    editor).
  - Last 10 orders with timestamps and item count.
  - Today's cover count (`SUM(party_size)` over today's `Visit`s where
    `closed_at IS NULL` or `closed_at > today_start`).
  - Prep-time histogram (last 50 served orders, time from
    `OrderItem.created_at` to `OrderItem.served_at`).
  - Reorder summary line (calls feature 26 endpoint server-side, not via
    the bot).
- New FastAPI route `POST /owner/<token>/revoke` (no body) that expires
  the link immediately and returns 204. The owner can text themselves
  `/ownerlink` to get a fresh link if they think the old one leaked.
- No writes to existing tables from the page. The page is read-only; any
  action (seating, ordering) still goes through the existing waiter UI.
- All output respects the existing privacy invariant: counts only, no
  PII, no customer identifiers, no order contents text (only item count
  per order).

**Out of scope (v2 owner-pains):**
- Push notifications (the link is on-demand only; if the page is open,
  htmx polling refreshes every 10 s).
- Owner-side actions (close visit, mark dirty) — those stay in the waiter
  UI where the role check lives.
- Multi-link rotation / per-role links — one active link per owner.
- TLS termination — assumed already in place (charter §3.2 deployment
  expects a reverse proxy with TLS).
- Customer-facing use of the same primitive — customer QR menu is
  feature 11 territory with its own token rotation; do not unify.

## Description

The owner-cook of a single small restaurant needs three things from a
surface they're going to glance at from off-floor:

1. **Zero friction to open.** No install, no signup, no login.
2. **Truth on one page.** Tables, recent orders, covers, prep times,
   reorder status. Not a dashboard, not a tabbed view.
3. **Revocable.** If the phone is lost, the link can be expired in one
   command.

The primitive that satisfies all three is a signed expiring link with a
server-rendered page. The token is a 256-bit random string, hashed for
storage, valid for 12 hours, and revocable. The page is a Jinja2 template
served from the existing FastAPI app — no SPA, no build step, no React.

The data is already in the schema:

- `Table.state` → table grid.
- `Order` + `OrderItem` → last 10 orders + item count.
- `Visit.party_size` → today's covers.
- `OrderItem.created_at` / `served_at` → prep-time histogram.
- Feature 26 query → reorder line.

The page is **read-only**. The owner can see everything but cannot change
anything from this surface. That is deliberate: the explicit-state rule
(charter §3.1) requires a confirmed waiter action for any state
transition, and the owner-link page is not a waiter surface.

The link is chat-id allowlisted (same as feature 04). Anyone who can type
`/ownerlink` in the cook bot gets a link. The chat-id allowlist is the
owner-trust boundary; the link is the access primitive.

## Data model

```
OwnerLink  (id, token_hash TEXT UNIQUE, created_at, expires_at, revoked_at NULL)
```

One new table. Token is `token_urlsafe(32)` from `secrets`; the raw token
lives in the URL only. The database stores only the SHA-256 hash.

Migration: `init_db()` creates the table if absent.

## Implementation

1. **New model** — `backend/app/models.py`: `OwnerLink` SQLModel class.
2. **New module** `backend/app/routers/owner_link.py`:
   - `GET /owner/<token>` — renders `owner.html` Jinja2 template with
     data fetched from existing SQLModel queries (no new endpoints, no
     new aggregation logic).
   - `POST /owner/<token>/revoke` — sets `revoked_at = now()`, returns
     204.
3. **New bot handler** — extend `backend/app/bot/cook_bot.py` with
   `/ownerlink` (chat-id allowlisted). Generates a fresh `token_urlsafe(32)`,
   stores its SHA-256 hash, returns the full URL.
4. **Template** — `backend/app/templates/owner.html`: single-page, htmx
   loaded from CDN (`<script src="https://unpkg.com/htmx.org@2.0.3">`),
   no other JS. Auto-refresh every 10 s via htmx `hx-trigger="every 10s"`
   on a refresh div.
5. **Wire into `app/main.py`** — include the new router.
6. **Manual verification**:
   - `cd backend && uvicorn app.main:app --reload`
   - In Telegram (cook role): `/ownerlink` → URL.
   - Open the URL on a fresh browser session (no cookies, no login).
   - Confirm table grid renders, last 10 orders show, today's cover
     count is non-zero, prep-time histogram renders, reorder line
     appears if feature 26 is enabled.
   - Close and reopen browser → still works (no session).
   - Wait 12 hours → page returns 410 Gone (or shorten the expiry in a
     test fixture).
   - POST `/owner/<token>/revoke` → page returns 410 Gone immediately.
   - Privacy test: confirm no customer names, no order-item text
     appears in the page source.

## Telegram interaction

- New cook-bot command `/ownerlink` — returns the signed URL.
- Existing cook-bot commands are unaffected. No new cook input beyond
  this one.

## Dependencies

- [08-index-mockup.md](08-index-mockup.md) — the existing floor grid
  visual is the template for the page layout.
- [26-reorder-point-on-stockentry.md](26-reorder-point-on-stockentry.md)
  — the reorder line on the page reuses the feature 26 query.
- Charter §3.1 (existing `Table.state`, `Visit`, `Order`, `OrderItem`,
  `Bill` models).
- Charter §3.2 (`SECRET_KEY` already configured in `backend/app/config.py`).

## Open questions

- Polling cadence — 10 s is a guess. If the restaurant is high-volume,
  the cook will see stale data; if low-volume, the polling is just load.
  Default: 10 s; allow per-deployment config in `config.py`.
- Multiple active links — should the cook be able to keep several
  `/ownerlink`s alive at once (e.g. for the owner's partner)? Default:
  one active link per chat-id; issuing a new one invalidates the old.
  Track via `OwnerLink` rows with `revoked_at` set on supersession.
- Audit trail — should every page view be logged? Default: no logging of
  reads; if needed, log to existing structured-log stream as `info`.
- Browser support — htmx works on every browser since IE11; no concern.

## Why this matters

LE31's charter is built around two surfaces: waiter web UI and cook
Telegram bot. The owner is supposed to be reachable through those, but the
owner's actual decision moments are *off-floor*, where neither surface is
practical. Today's research surfaced three small-business repos (slotone,
slipbook, shelftrack) all built around the same primitive — a no-account,
ephemerally-shared, photo-in / CSV-out surface for a solo operator. That
primitive is exactly what the LE31 owner needs to glance at the floor from
the supplier, the school run, or a sick day. It is a 3-5 day build that
reuses existing schema, existing FastAPI, existing role checks, and adds
one new table + one new template + one new bot command. No new dependency,
no new infra.