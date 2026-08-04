# Feature 28 — Shelf-Threshold Receiving Bot

> **Priority**: P1 · **Effort**: S–M (2–4 days) · **Source**: brainstorm 2026-08-04
> (cross-section pick A) · **Bucket**: v2 owner-pains
> **One-line**: Cook sends one photo of the morning delivery via the existing
> Telegram bot; OCR diffs quantities against the most recent `/expected`; the
> delta is written as a `StockEntry`, and a one-line reorder summary is
> returned.

## Goal

Close the inventory receiving stage without leaving the operator surface the
cook already runs. When the morning delivery arrives, the cook should be able
to take one photo, send it to the same Telegram bot they already use for
feature 04 (menu photo bot), and have the receiving quantities logged as
`StockEntry` rows plus a reorder line if any item is now at or below its
threshold.

Inspired by `Sreenivas-Sadhu-Prabhakara/shelftrack` (pushed **today**,
2026-08-04, GitHub `topic:small-business`): *"Photo-first stock list for a
tiny shop — snap a product, set a reorder level, see what's running low at a
glance, and export to CSV. 100% offline, nothing leaves your device."* The
exact same primitive applied to a small restaurant's receiving stage.

## Scope

**In scope (v2 owner-pains):**
- New cook-bot command `/expected <supplier> <item1>=<qty1> <item2>=<qty2>...`
  that records the expected delivery for the named supplier (one row per
  `(supplier, menu_item, expected_at)` tuple).
- New cook-bot command `/received` that accepts one photo. The bot runs OCR
  on the photo (reuse the OCR primitive from feature 04; if the item has no
  existing OCR adapter, the command returns "send expected list first" and
  aborts).
- For each `(supplier, item)` the bot diffs OCR'd `qty` against the recorded
  `expected_qty` and writes one `StockEntry` row with `qty_delta = ocr_qty −
  expected_qty` (can be negative if a delivery was short). The `StockEntry`
  `reason` field is set to `receiving:<supplier>` for audit traceability.
- After writing the deltas, the bot replies with a one-line reorder summary:
  "3 items need reorder: tiramisu, panna cotta, focaccia" — reusing the
  threshold query from feature 26 (`reorder_point` / `par_level`).
- All cook-bot commands are chat-id allowlisted, same as feature 04.
- One new table `ExpectedDelivery` (see Data Model). One new file
  `backend/app/bot/cook_bot_receiving.py`. Reuses the existing OCR adapter.

**Out of scope (v2 owner-pains):**
- Multi-supplier auto-reorder or supplier integrations — feature 16 territory.
- Voice-driven receiving — `rishirevuri/Koe` (today's research signal) is
  adjacent; deferred to v2-AI.
- Per-line item images — one photo per delivery is enough for v1 of this
  contract; item-level photos are feature 04 territory.
- Reconciling receiving against invoices or POs — feature 16.

## Description

The current `Batch` + `StockEntry` model (charter §3.1) tracks cooked and
sold quantities but does not record *receiving*. The owner-cook manually
types "we got 10kg of flour" into a notes file or remembers it. The first
question after the kitchen closes is therefore "are we going to be short
tomorrow?" — which is exactly the question feature 26's threshold query
answers, but the underlying stock count includes no receiving event.

This contract closes the loop with the smallest possible change:

1. Cook types `/expected butcher 4 ribeye=2 1kg=1` (or similar) at the start
   of the day. The bot stores one row per `(supplier, item, expected_at)`
   tuple.
2. When the delivery arrives, cook sends one photo of the whole delivery
   slip (or pile) to the bot with the command `/received`.
3. The bot OCRs the visible quantities and matches them against the most
   recent unfulfilled `ExpectedDelivery` for the same supplier. Each matched
   `(item, ocr_qty, expected_qty)` produces a single `StockEntry` with
   `qty_delta = ocr_qty − expected_qty`. The supplier name is recorded in the
   `StockEntry.reason` field so the audit trail is intact.
4. The bot then runs the feature 26 reorder query against the resulting
   stock and replies with the one-line reorder summary.

The `StockEntry` ledger remains append-only (a receiving is a `StockEntry`,
not an update to existing rows). The explicit-state rule is preserved (the
cook's `/received` photo is an explicit action — no auto-OCR on inbound
messages).

If OCR fails or yields zero matches, the bot replies "could not read items;
please retype quantities" and writes nothing. The cook can then type the
quantities manually with `/received_typed ribeye=2 1kg=1` (a v2-AI fallback
out of this contract — for v1 of this contract, manual retype is acceptable
and documented in the cook-bot help).

## Data model

```
ExpectedDelivery  (id, supplier_name, menu_item_id, expected_qty,
                   expected_at, fulfilled_at NULL)
StockEntry        (existing) — append-only; this contract writes new rows
                   with reason='receiving:<supplier_name>'
Batch             (existing) — unchanged
MenuItem          (existing) — unchanged; reorder_point from feature 26
```

One new nullable column on `StockEntry`:

```
StockEntry.reason TEXT NULL DEFAULT NULL
```

(Backfill: existing rows keep `reason = NULL`; new rows from this contract
set `reason = 'receiving:<supplier_name>'`.)

Migration: `init_db()` adds the column if absent.

## Implementation

1. **Schema migration** — extend `backend/app/models.py` `StockEntry` with
   `reason: Optional[str]`. New `ExpectedDelivery` SQLModel class.
2. **New module** `backend/app/bot/cook_bot_receiving.py`:
   - `/expected <supplier> <item>=<qty> ...` handler. Parses arguments,
     looks up `MenuItem` by fuzzy name match, inserts one
     `ExpectedDelivery` row per pair, replies "expected 2 ribeye, 1 kg of
     1kg-pack from butcher".
   - `/received` handler. Accepts a photo, downloads it, passes the bytes
     to the existing OCR adapter (from feature 04). For each OCR'd
     `(item_name, qty)` line, look up the most recent unfulfilled
     `ExpectedDelivery` for the same supplier (inferred from the prior
     `/expected` call's chat context, defaulting to "today's supplier" if
     only one supplier is unfulfilled today). If no match, log a warning
     and skip. For each match, write one `StockEntry` with `qty_delta =
     ocr_qty − expected_qty` and `reason = 'receiving:<supplier>'`. Mark
     the `ExpectedDelivery.fulfilled_at = now()`. After writing, run the
     feature 26 reorder query and reply with the one-line summary.
   - On OCR failure, reply "could not read items; please retype
     quantities" and write nothing.
3. **Wire into `app/main.py`** — `cook_bot_receiving` registers its
   handlers on the existing aiogram `Dispatcher`.
4. **Manual verification**:
   - `cd backend && uvicorn app.main:app --reload`
   - In Telegram (cook role):
     - `/expected butcher ribeye=2 1kg=1`
     - `/start_today` (existing) and create two `MenuItem` rows named
       "ribeye" and "1kg-pack" with `reorder_point = 2`.
     - Send a photo of a slip reading "ribeye 2 / 1kg-pack 1" with the
       caption `/received`.
     - Bot replies "received: 2 ribeye, 1 1kg-pack from butcher. 0 items
       need reorder."
     - Sell 5 ribeye → `/reorder` (from feature 26) now shows "ribeye".
   - Repeat with a short delivery ("ribeye 1" instead of "ribeye 2") and
     confirm `StockEntry.reason = 'receiving:butcher'` and `qty_delta =
     −1`.
   - Repeat with an OCR failure (deliberately blurry photo) and confirm
     no `StockEntry` is written.

## Telegram interaction

- New command `/expected <supplier> <item>=<qty> ...` — records expected
  delivery.
- New command `/received` (followed by a photo) — runs OCR, writes
  `StockEntry` rows, returns reorder summary.
- **No new client, no new screen.** All interaction stays inside the
  existing cook-bot surface the cook already runs.

## Dependencies

- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — `StockEntry`
  ledger is the destination; append-only invariant preserved.
- [04-menu-photo-bot.md](04-menu-photo-bot.md) — OCR primitive.
- [26-reorder-point-on-stockentry.md](26-reorder-point-on-stockentry.md) —
  reorder summary query and the `reorder_point` / `par_level` columns.
- [16-supplier-orders.md](16-supplier-orders.md) — upstream of this contract
  on the v2 roadmap; this is the *receiving* signal, feature 16 is the
  *ordering* action.

## Open questions

- Should the bot prompt the cook to confirm before writing the `StockEntry`
  rows? Pro: safety against OCR mistakes. Con: extra round-trip. Default:
  confirm via an inline button after OCR; cook taps "Looks good" or
  "Cancel". Add as a v1.1 polish if it's cheap.
- Multi-supplier in one delivery — is it realistic that one slip covers
  two suppliers? Default: no; one photo per supplier.
- OCR adapter — feature 04's OCR is menu-photo specific. This contract
  needs the same adapter for delivery slips, which may have a different
  layout. If the existing adapter yields < 50 % accuracy on delivery slips,
  fall back to a typed-quantities command path (see above).
- Should the bot send a daily end-of-day summary including receiving totals?
  Default: yes, piggy-back on the existing feature 26 `/end_of_day`
  extension. Single one-line addition.

## Why this matters

The killer pattern (append-only `StockEntry` ledger) currently has a blind
spot: the receiving stage. Without it, the ledger is truth-only-after-cooking,
which means the owner-cook has to remember or write down "we got 10kg of
flour" by hand. This contract turns the photo the cook is already taking
for feature 04 into a receiving event in the same ledger, using the same
surface. It is the smallest, safest step that closes the loop the operator
asked for in the research.

Externally primed by `Sreenivas-Sadhu-Prabhakara/shelftrack` (pushed
**today**): photo-first, threshold-driven, single-operator, offline, nothing
leaves your device. The LE31 cook bot is exactly the same shape; this
contract reuses feature 04's OCR primitive, feature 26's threshold query,
and the existing `StockEntry` append-only invariant. No new dependencies.