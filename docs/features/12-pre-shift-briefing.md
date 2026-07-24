# Feature 12 — Pre-Shift Briefing (Manager → Staff)

> **Priority**: P2 · **Effort**: XS–S (1–3 days) · **Source**: owner-pains
> research — "Every shift I repeat today's specials, sold-out items, allergy
> warnings, reservations, staffing notes. Then someone says they never heard it."
> **One-line**: Manager sends a brief via Telegram each shift; staff acknowledge
> with one tap; non-acknowledgement is escalated.

## Goal

Replace the verbal pre-shift huddle with a persistent, searchable, ack-tracked
record that every staff member reads (or is reminded to read) at the start of
their shift.

## Scope

**In scope (v1 of this feature):**
- Manager types `/brief` (or sends a freeform message) into the cook's bot
  (or a new manager bot).
- Bot auto-attaches today's context: sold-out items, today's specials,
  upcoming reservations, 86'd items.
- Sends to all on-shift staff via Telegram.
- Each staff taps ✅ to acknowledge; taps 💬 to ask a follow-up question.
- Unacknowledged briefs at shift start → manager sees who hasn't read.
- Briefs archived in DB; searchable later.

**Out of scope:**
- Full HR / scheduling (separate feature).
- Multi-language briefs (cook writes in their language).
- Voice notes / video briefs (text only).

## Description

Each shift begins (e.g. 11:00, 18:00). Manager (or cook) runs `/brief` in
Telegram. Bot gathers today's data from the DB:
- Items currently sold out (so staff don't promise them).
- Today's specials (manager-entered or auto-detected from yesterday's specials).
- Allergen alerts (e.g. "we ran out of oat milk yesterday — check before selling
  the lactose-free dessert").
- Upcoming reservations in the next 2 hours.
- Yesterday's stats: covers, top items, tips (motivation).

Bot sends a formatted message to all staff in the on-shift group/chat.
Staff reply with ✅ (acknowledge) or ❓ (ask).

## Data model

```
ShiftBriefing
  id              PK
  shift_id        FK (which shift this belongs to)
  sent_by         FK (manager user)
  sent_at         DATETIME
  content         TEXT     (manager's freeform + auto-context concatenated)
  expires_at      DATETIME (when this brief becomes stale)

BriefingAck
  briefing_id     FK
  user_id         FK
  acked_at        DATETIME
  reaction        TEXT     ('ack' | 'question' | 'disagree')
  note            TEXT     (optional freeform follow-up)
```

## Implementation

1. **New table** `ShiftBriefing` + `BriefingAck`.
2. **Bot command** `/brief` in the manager-side aiogram dispatcher.
3. **Auto-context builder** — small Python module that queries the DB for
   today's sold-out items, upcoming reservations, etc.
4. **Ack handler** — `aiogram` callback query handler for inline buttons.
5. **Reminder job** — 30 min before shift, send to non-acknowledgers.

## Telegram interaction

```
Manager: /brief
Bot:     📋 Pre-shift briefing for Friday 24 Jul, 18:00:

         === TODAY'S MENU ===
         ✅ Most items available
         🚫 Sold out: Tiramisu, Caesar Salad (until next prep)
         ⭐ Today's specials: None set — add via /specials

         === ALLERGEN ALERTS ===
         ⚠ Oat milk is OUT — lactose-free dessert unavailable
         ⚠ Gluten-free breadcrumbs low stock

         === UPCOMING ===
         📅 19:30 — Reservation for 6 (name: Dupont) — Table 8
         📅 20:00 — Reservation for 2 — Table 2

         === YESTERDAY ===
         📊 38 covers, €742 sales, €68 tips (9.2%)
         🏆 Top: Schnitzel (12), Burger (9)

         [Acknowledge ✅]  [Question ❓]

         Manager message: "Welcome back. Tonight we'll be busier than usual — wedding next door. Pace the mains."

Waiter (AB): ✅
Bot:     Thanks AB. Acknowledged at 17:58.

Waiter (AC): ❓ "Is the oat milk expected back tonight?"
Bot:     Your question was forwarded to the manager.
```

## Dependencies

- [04-menu-photo-bot.md](04-menu-photo-bot.md) — uses the same bot dispatcher.
- [06-guest-demographics.md](06-guest-demographics.md) — reservations feature
  must exist for "upcoming reservations" to work.

## Open questions

- One bot for all roles, or separate manager / cook / waiter bots?
- Should briefs auto-include yesterday's stats, or opt-in?
- Should non-acknowledgement escalate to manager automatically after 30 min?

## Why this matters

This is **the cheapest feature in the entire backlog**. Half a day of work
for a tangible improvement in operational discipline. Per the owner-pains
research: "common" frequency but very high impact for managers of 2-5 person teams.