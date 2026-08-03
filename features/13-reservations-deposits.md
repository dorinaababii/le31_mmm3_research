# Feature 13 — Reservations & No-Show Deposits

> **Priority**: P2 · **Effort**: M (5–10 days) · **Source**: owner-pains
> research — "I lose money when guests book, occupy a prime table, and never show."
> **One-line**: Bookings with optional deposit hold; SMS/email reminders;
> manager sees risky reservations and can charge a no-show fee.

## Goal

Let the restaurant take reservations — including optional deposits to deter
no-shows — without standing up a separate booking system.

## Scope

**In scope (v1 of this feature):**
- Public booking page `/book` — guest picks date, time, party size, leaves name + phone.
- Manager view: today's / week's reservations in a list.
- Reservation status: `pending`, `confirmed`, `seated`, `completed`, `no_show`, `cancelled`.
- Optional deposit hold via Stripe (no full charge — just a pre-auth).
- Auto-reminder: SMS 24h before, SMS 2h before (via Twilio).
- Walk-in support: "add a walk-in to the waitlist" → manager sees queue.

**Out of scope:**
- Deposits via bank transfer / cash app (Stripe only).
- Integration with OpenTable, SevenRooms, Resy (each requires a partnership contract).
- Table preferences ("window seat please") — free-text note only.
- Group bookings > 8 people — they call in.

## Description

Guest visits the booking page on the restaurant's website (or scans a QR at
the door). Picks date, time, party size. Leaves name + phone. Optionally
adds a card for a deposit hold (e.g. €10/person).

Manager sees the day's reservations on a single page; can confirm / reject.
Cook sees "upcoming reservations" in the pre-shift brief (feature 12).

24h before: SMS reminder with a "Cancel" link.
2h before: SMS reminder with a "We're ready!" message.
If guest doesn't show 15 min after the booking → manager can mark `no_show`
and (if deposit was held) charge the deposit via Stripe.

## Data model

```
Reservation
  id              PK
  guest_name      TEXT
  guest_phone     TEXT
  guest_email     TEXT NULL
  party_size      INT
  booked_at       DATETIME (the booking moment)
  reserved_for    DATETIME (when they want to come)
  status          Enum (pending|confirmed|seated|completed|no_show|cancelled)
  notes           TEXT NULL
  table_id        FK NULL (assigned when seated)
  deposit_cents   INT NULL
  stripe_pi_id    TEXT NULL  (Stripe PaymentIntent id)
  reminder_24h_sent   BOOLEAN
  reminder_2h_sent    BOOLEAN

WaitlistEntry
  id              PK
  guest_name      TEXT
  guest_phone     TEXT
  party_size      INT
  arrived_at      DATETIME
  quoted_wait_min INT
  seated_at       DATETIME NULL
  cancelled_at    DATETIME NULL
```

## Implementation

1. **Booking page** `/book` — FastAPI route, single HTML form.
2. **Manager page** `/admin/reservations` — list + actions (confirm, reject, no-show).
3. **Stripe integration** — `stripe` Python lib; PaymentIntent with `capture_method='manual'`.
4. **Reminder job** — APScheduler or cron; runs every 5 min, finds reservations
   due for reminder, sends via Twilio SMS.
5. **Waitlist** — simple addition to the manager page; manual entry.

## Stripe & SMS deps

- `stripe>=10.0` Python package
- Twilio account (pay-as-you-go SMS, ~€0.05/SMS in EU)
- For EU GDPR: reservation data retention policy (90 days default)

## Telegram integration

```
Manager: /reservations
Bot:     Today's reservations (Fri 24 Jul):

         18:00 · 2 guests · Marie Dupont · ✅ confirmed · deposit €20
         19:00 · 4 guests · Paul Bernard · ⏳ pending
         19:30 · 6 guests · Wedding Dupont · ✅ confirmed · Table 8
         20:30 · 2 guests · Walk-in suggestion · seated

         Upcoming waitlist:
         • 19:15 — Sarah (4) — quoted 20 min
```

```
Bot:     ⚠ Reservation 19:00 (Paul Bernard, 4 guests) is 15 min late.
         Mark no-show? [Yes — charge €20] [No — still coming] [Cancel]
```

## Dependencies

- [12-pre-shift-briefing.md](12-pre-shift-briefing.md) — integrates brief content.
- New: Stripe account, Twilio account.

## Open questions

- Should reservations come via the customer QR menu page or a separate `/book` page? (Both — link from menu page.)
- What if the guest cancels 1h before? Full refund or fee? (Default: full refund; configurable.)
- Should we offer a "leave a review after" flow? (Punted to v2.)
- SMS or WhatsApp for reminders? (SMS default; WhatsApp would need a separate business API.)

## Why this matters

In the owner-pains research, no-shows ranked **#1 with "very common" frequency**.
For restaurants where a single no-show on a Saturday night can lose €100+,
a €10/person deposit hold recovers the cost in 2 weekends.

The catch: this is the first feature that introduces **real money flow** (Stripe)
and a **paid external service** (Twilio). It also creates GDPR obligations
(name + phone + email storage, retention, deletion). Worth building carefully.