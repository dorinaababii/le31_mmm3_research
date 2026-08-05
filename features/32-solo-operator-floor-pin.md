# Feature 32 — Solo Operator Floor PIN

> **Priority**: P1 · **Effort**: S (≤3 days) · **Source**: brainstorm 2026-08-05
> (cross-section pick A) · **Bucket**: v1 owner-pains
> **One-line**: Owner issues a 4-digit PIN at boot; opening `/pin/<code>` on any
> phone lands a stripped-down live view (floor + prep alerts + last 5 voids)
> with no login, no email, no app install.

## Goal

Give the LE31 owner — who has no IT department, no second device, and who is
the same person who runs the floor — a single-tap way to glance at the room
after stepping away from the office for a break, a supplier run, or a sick
day. The current "owner on shift" surface is the full web app, which is too
heavy for a 5-second glance. The owner should not need to remember a URL, an
email, or a password; they should only need a 4-digit PIN.

Inspired by HN solo-founder SaaS Show HN cluster (objectIDs 44767231 *match
traffic sources to paying customers*, 44742032 *PassiveCraft*, 44479824
*SaaS boilerplates*, 44571534 *TikTok app via trained model*) — five threads
in the 30-day window that share the recurring UX primitive of a *minimal
glanceable surface for the solo owner, bypassing the full dashboard*.
Translated to LE31, the owner already has the no-account live floor link
(feature 29, `owner-no-account-live-floor-link`) for waiters on shift; this is
the next layer *down* — a 4-digit PIN the owner carries in their head, that
does not even require the link exchange.

## Scope

**In scope (v1 owner-pains):**
- A new config field `OWNER_PIN_HASH` in `backend/app/config.py` — bcrypt of
  a 4-digit numeric PIN, set at first boot from a random secret; rotatable
  via a manager-only CLI (`python -m app.cli rotate_owner_pin`).
- A new route `GET /pin/<code>` in a new router `backend/app/routers/owner_pin.py`.
  The route: (a) bcrypt-verifies `<code>` against `OWNER_PIN_HASH`, (b) on
  success sets a short-lived signed cookie (`owner_pin_session`, 12 h TTL), (c)
  renders the new `templates/owner_pin.html` page.
- A new template `backend/app/templates/owner_pin.html` — stripped-down live
  view: floor states (free / seated / needs-bill), today's prep alerts
  (low stock + sold-out), the last 5 voids. Subscribes to the existing
  `CookChannel` SSE stream for live updates. `Ctrl+P` print-stylesheet
  included for thermal-printer use (shared with feature 34's prep board).
- A new `GET /api/owner_pin/state` endpoint that returns the JSON payload
  consumed by the template. Reads from existing tables only.
- One new file `backend/app/cli.py` with `rotate_owner_pin` subcommand.
- All cook/manager UI surfaces unchanged.
- No new identity is created; the PIN is a bearer secret (rotating the hash
  invalidates all live sessions).

**Out of scope (v1 owner-pains):**
- Per-user PIN (per role) — single owner PIN only in v1; per-role expansion
  belongs to v2.
- PIN on the cook bot — Telegram chat-id allowlist stays the cook/host gate.
- Customer-facing PIN — explicitly out: the privacy invariant holds (no
  customer identity is created).
- Push notifications or email alerts from this route — passive glance only.
- QR-coded PIN URL — same primitive can be added later without redesign.

## Description

The route is intentionally minimal:

```
GET /pin/<code>
  ├─ if not bcrypt(code) → 401 + generic "wrong pin" page (constant-time)
  └─ else set owner_pin_session cookie (signed, 12 h TTL)
       └─ render owner_pin.html
            ├─ floor: read /api/tables (existing)
            ├─ alerts: read /api/stock/alerts (existing feature 26)
            ├─ voids: read last 5 from /api/bills?voided=true (existing)
            └─ subscribe CookChannel SSE (existing feature 23) for live updates
```

The template is server-rendered (Jinja2) with one `<script>` block that opens
the SSE connection; HTMX handles the auto-refresh of the floor grid. The
print-stylesheet is shared with feature 34's prep board (same CSS class
names) so the two pages can be printed on the same thermal printer
hardware.

## Data model

No new tables. Reuses:

```
app_user (existing) — owner user row, role='manager'
MenuItem (existing)
Batch (existing) — for prep alerts
StockEntry (existing) — append-only ledger, drives alerts
Table_ (existing) — for floor grid
Visit (existing) — for needs-bill state
Bill (existing) — for voids
```

New config field only:

```
config.py:
  OWNER_PIN_HASH = bcrypt("0000" generated at first boot)   # default
  OWNER_PIN_TTL_HOURS = 12                                   # cookie TTL
```

## Implementation

1. **Add config**: `OWNER_PIN_HASH` (bcrypt-hashed), `OWNER_PIN_TTL_HOURS`
   to `backend/app/config.py`. On first boot, generate a random 4-digit
   PIN, bcrypt it, log to stdout, and write the hash to `.env`.
2. **Create router**: `backend/app/routers/owner_pin.py` with two routes:
   - `GET /pin/<code>` — verifies PIN, sets cookie, renders template.
   - `GET /api/owner_pin/state` — returns the JSON the template renders.
3. **Create template**: `backend/app/templates/owner_pin.html` — minimal
   Jinja2 page. Reuses `templates/_floor_grid.html` partial. Subscribes to
   `CookChannel` SSE. Print-stylesheet in `static/css/print-prep.css`
   (shared with feature 34).
4. **CLI**: `backend/app/cli.py` with `rotate_owner_pin` subcommand. On
   rotation, generates a new random 4-digit PIN, re-bcrypts, and writes to
   `.env`. Logs the new PIN to stdout exactly once.
5. **Mount router** in `backend/app/main.py`:
   `app.include_router(owner_pin.router)`.
6. **Cookie signing**: reuses the existing `SECRET_KEY` config field. The
   cookie payload is `{"role": "owner_pin", "iat": <ts>}`; signature is
   `HMAC-SHA256(SECRET_KEY, payload)`. Reuse the existing cookie helper in
   `backend/app/auth.py` if available; otherwise add a small
   `backend/app/auth.py` helper.
7. **Wire-up verification**: spin up `uvicorn app.main:app --reload`,
   generate a PIN via CLI, hit `GET /pin/<code>` with `curl -L -c cookies`,
   confirm `owner_pin_session` cookie set, then `curl -b cookies
   /api/owner_pin/state` confirms JSON shape. Confirm `/pin/0000` returns
   401 with constant-time response (~250 ms regardless of validity).

## Telegram interaction

**None.** This feature is web-only. The existing cook bot Telegram channel
is unchanged; the PIN is orthogonal to the chat-id allowlist.

## Dependencies

- **Hard**:
  - [feature 23 — sse-cook-channel](23-sse-cook-channel.md) — SSE stream.
  - [feature 26 — reorder-point-on-stockentry](26-reorder-point-on-stockentry.md) — drives the prep-alert panel.
  - [feature 29 — owner-no-account-live-floor-link](29-owner-no-account-live-floor-link.md) — sits beside, not in place of.
- **Soft**:
  - [feature 34 — stockout-prep-board-snapshot](34-stockout-prep-board-snapshot.md) — shares the print-stylesheet.

## Open questions

1. **Constant-time PIN verification**: bcrypt is ~250 ms; for 4-digit codes
   the timing channel is small but not zero. Mitigation: optional fixed-delay
   wrapper in the route handler. Resolve at code-review.
2. **Rate limiting**: brute-force risk for 4-digit PIN. Mitigation: in-memory
   rate limit (`slowapi` or one-liner) at `/pin/<code>` (max 5 attempts / 5
   min / IP). Decide whether to ship the rate limit in v1 of this feature or
   defer to v2 hardening.
3. **Cookie `Secure` / `HttpOnly` flags**: required in prod (HTTPS), harmless
   in dev (HTTP). Resolve by gating on `config.ENV == "prod"`.
4. **Owner rotation on staff turnover**: rotating the PIN is the
   operational lever; document in `backend/README.md`.
5. **Does the owner need a *different* view from the manager?** The pick
   assumes yes (glanceable vs full admin); confirm before code.

## Why this matters

Removes the most-cited friction point in any solo-operator pilot: "I can't
glance at the room without logging into a full web app." Same operational
value as feature 29, but at a deeper cost layer — the owner doesn't need a
URL, just a 4-digit number they can recall in 5 seconds. ~150 lines + a
bcrypt hash; reuses every primitive that already exists (SSE, alerts,
floor grid). Trivial to roll back (remove the route + template). All three
LE31 invariants preserved: append-only ledger untouched, no new identity,
money never crosses the route.

Inspired by the same HN signal as feature 29 (solo-founder SaaS cluster),
but at a lower layer (PIN vs signed-link) — co-existence is intentional and
documented.
