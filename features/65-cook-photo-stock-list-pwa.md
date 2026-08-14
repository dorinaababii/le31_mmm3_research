# Feature 65 — Cook Photo Stock-List PWA

> **Priority**: P2 · **Effort**: M (≤1 week) · **Source**: brainstorm
> 2026-08-14 (cross-section pick B) · **Bucket**: **v2 owner-pains
> (cook-UX)** — same bucket as feature 04 (`menu-photo-bot`) but a
> different JTBD (stock entry, not menu item parsing).
> **One-line**: add a **photo-first stock-entry surface** on the cook's
> phone via the existing Telegram cook bot — distinct from the
> existing menu-photo-bot (feature 04, dish recognition). The new
> flow is: cook opens the Telegram cook bot, taps `/stock-snap`,
> takes a photo of a product on the receiving shelf, optionally adds
> a low-effort text annotation ("flour 25kg — bag 1 of 4"), confirms,
> and the entry lands as a new `StockEntry` row in the existing
> append-only ledger.

## Goal

`Sreenivas-Sadhu-Prabhakara/shelftrack` (HTML PWA, MIT, created
2026-07-15, re-pushed 2026-08-14) is the cross-section anchor. The
repo is a *photo-first stock list* for a tiny shop — snap a product,
set a reorder level, see what's running low at a glance, export to
CSV. 100% offline, nothing leaves the device.

LE31's existing `StockEntry` flow (feature 03, kitchen stock
tracker) requires manual text entry. During a Friday-night service,
the cook has **one hand free and one phone in the other** — manual
text entry is fragile. The shelftrack pattern (snap → reorder level
→ low alert → CSV) maps cleanly to LE31's cook bot:

| shelftrack step | LE31 adaptation |
|---|---|
| snap a product photo | Telegram photo upload from cook bot |
| set a reorder level | `/stock-snap` → optional low-effort annotation ("flour 25kg — bag 1 of 4") |
| see what's running low | existing low-alert channel (cook bot) |
| export to CSV | existing owner-daily-recap (feature 39) export |

The result is **photo-first stock entry** — a pattern that
complements the existing menu-photo-bot (feature 04, dish
recognition) without competing with it (feature 04 parses
*menu items* from photos; feature 65 logs *stock entries*
from photos). Both surfaces use Telegram photo upload; both
land data in the existing append-only ledger; both respect
the charter §Privacy invariant (photos are stored on
operator-controlled storage, not third-party).

## Scope

**In scope (v2 owner-pains M effort, ≤1 week):**

- `bot/cook_bot.py` extension: add `/stock-snap` command and
  photo handler. State machine: `awaiting_photo` →
  `awaiting_annotation` (optional) → `awaiting_confirm` →
  write `StockEntry` row.
- `bot/keyboards.py` extension: add inline confirmation
  keyboard ("Confirm" / "Edit annotation" / "Cancel").
- `backend/app/services/stock_entry.py` extension: add
  `create_stock_entry_from_photo(product_photo_file_id: str,
  annotation: str | None, prep_station: str, qty: Decimal,
  unit: str, actor_id: int)` helper.
- One Alembic migration: add `photo_file_id TEXT NULL` column
  to `stock_entry` table. Nullable = backwards-compatible;
  append-only invariant intact (no UPDATE/DELETE).
- New `backend/app/services/media.py`: ≤100 LOC, aiogram
  `get_file` → local storage under
  `var/stock_photos/YYYY-MM-DD/<uuid>.<ext>`. Path stored
  alongside the `photo_file_id` (Telegram's file id) for
  retrieval.
- `backend/tests/test_cook_stock_snap.py`: 4 fixtures —
  snap with annotation, snap without annotation, low-alert
  trigger, ledger hash integrity.
- `bot/README.md` extension: short section on the
  `/stock-snap` command and the photo retention policy.

**Out of scope (v2 v1):**

- Object recognition on the photo. The photo is *evidence* of
  the receiving event; the operator types the product name
  (or picks from a list of recent products) in the annotation
  step. A future pick could add OCR or a multimodal model
  for *suggested* product names (with operator confirmation),
  but that is a separate feature.
- Photo storage retention enforcement. The slice ships the
  storage path; a separate feature adds the retention policy
  (≤90 days default, configurable).
- Multi-photo per entry. v1 ships one photo per entry; a
  future pick could attach a photo gallery (front + back of
  a delivery, multiple angles of a stock shelf).
- Client-side PWA. The cook-side surface stays on Telegram
  (the existing cook bot); a PWA variant is a separate
  feature that requires an operator-side web surface
  (LE31's waiter UI is the candidate, not the cook side).

## Description

`Sreenivas-Sadhu-Prabhakara/shelftrack` is the **pattern**, not
the file (LE31 is server-side Python/FastAPI/aiogram, not a
client-side HTML PWA). The pattern: snap → reorder level →
low alert → CSV. LE31's adaptation is server-side Telegram
photo upload that lands in the existing append-only `StockEntry`
ledger.

The **cross-validation anchors** are:

- `Sreenivas-Sadhu-Prabhakara/slotone` (JS, MIT, re-pushed
  2026-08-14) — same author, *private offline appointment
  day-book for a one-person business*. Corroborates the
  low-effort single-operator offline-first pattern.
- `gaganjainse/ClinicLedger` (Kotlin, 1★, 2026-07-15) — *offline-first
  voice-assisted clinic ledger for Indian practitioners*.
  Different surface (clinic not restaurant), different
  language (Kotlin not Python), but the **photo-first stock-entry**
  + **offline-resilient** + **single small business** pattern
  overlap is tight.
- `MahyarMozafar/demo-kitchenware` (HTML+seller-panel,
  carry-over from 2026-08-12/13 daily-research) — same
  Telegram-to-inventory pattern, but the demo is the *seller
  panel*, not the cook surface. Cross-section reading only.

The **first surfaced** reference: `Sreenivas-Sadhu-Prabhakara/shelftrack`
appeared in 2026-08-04 brainstorm (HMM-24) as a reference; the
2026-08-14 re-push after 30 days of stable development is what
elevates it to brainstorm-grade. The repo is now mature enough
to point at as a *production pattern*, not a *fresh idea*.

## Data model

One Alembic migration:

```sql
ALTER TABLE stock_entry
  ADD COLUMN photo_file_id TEXT NULL;
```

Nullable = backwards-compatible (existing `StockEntry` rows
have `NULL`); the column is the Telegram `file_id` string. The
local-storage path is in `var/stock_photos/YYYY-MM-DD/<uuid>.<ext>`.

Append-only invariant intact: no UPDATE/DELETE on the column.
A future "photo retention policy" feature (out of scope) can
delete the *local file* without touching the ledger row.

```sql
-- (Carry-over from feature 03 + 37; the new column is additive.)
CREATE TABLE stock_entry (
    id              BIGSERIAL PRIMARY KEY,
    ingredient_id   BIGINT NOT NULL REFERENCES ingredient(id),
    qty_delta       NUMERIC(12, 4) NOT NULL,
    unit            TEXT NOT NULL,
    actor_id        BIGINT NOT NULL REFERENCES user_account(id),
    prep_station    TEXT NOT NULL,
    rationale       TEXT,                  -- feature 37
    photo_file_id   TEXT,                  -- feature 65 (NEW)
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## Implementation steps

1. Add Alembic migration `XXXX_add_stock_entry_photo_file_id.py`.
2. Extend `backend/app/models/stock_entry.py` (SQLModel):
   add `photo_file_id: str | None = None` field.
3. Create `backend/app/services/media.py`: aiogram `get_file`
   → local storage under `var/stock_photos/YYYY-MM-DD/`. Path
   in env var `LE31_MEDIA_ROOT`, default `./var/stock_photos`.
4. Extend `backend/app/services/stock_entry.py`:
   `create_stock_entry_from_photo(photo_file_id, annotation,
   prep_station, qty, unit, actor_id)` helper that writes
   the `StockEntry` row + saves the local file.
5. Extend `bot/cook_bot.py`:
   - Register `/stock-snap` command (cook-only).
   - State machine: `awaiting_photo` → `awaiting_annotation` →
     `awaiting_confirm` → `create_stock_entry_from_photo`.
   - Inline confirmation keyboard ("Confirm" / "Edit annotation"
     / "Cancel").
6. Extend `bot/keyboards.py`: add the confirmation keyboard.
7. Add `backend/tests/test_cook_stock_snap.py` (4 fixtures).
8. Add `bot/README.md` section on the `/stock-snap` command.
9. Validate: run the full `backend/tests/` suite; the new
   fixtures must pass and the existing `test_stock_entry.py`
   (feature 03) and `test_void_rationale.py` (feature 37)
   must pass unchanged.

## Telegram interaction if any

- `/stock-snap` (cook-only). Bot replies: "Send a photo of the
  product." User uploads photo. Bot replies: "Add a short
  annotation? (or tap Skip)". User replies with annotation
  text or taps Skip. Bot replies with confirmation keyboard:
  "Confirm — flour 25kg bag 1 of 4" / "Edit annotation" /
  "Cancel". User taps Confirm. Bot writes the `StockEntry`
  row + replies: "Logged: +25 kg flour, photo attached."
- The existing low-alert path (cook bot, `feature 03`) emits
  the same "running low" Telegram message it does today;
  no change.
- The existing owner-daily-recap Telegram (feature 39)
  surfaces the new entry in the same shape as today's
  text-only entries; the photo is included as a thumbnail
  inline.
- No owner-facing commands added; the owner views the photo
  via the existing daily-recap inline thumbnail.

## Dependencies

- **Feature 03** (`kitchen-stock-tracker`) — the `StockEntry`
  model + write path that this slice extends.
- **Feature 04** (`menu-photo-bot`) — the existing Telegram
  photo-handler pattern that this slice reuses.
- **Feature 37** (`void-rationale-ledger-field`) — the
  `rationale` column that this slice reuses for the
  annotation text.
- **Feature 39** (`owner-daily-recap-telegram`) — the recap
  channel that surfaces the new entry.
- **aiogram v3** — `get_file` + photo upload handlers, already
  in use.
- **No new pip dependency**.

## Open questions

- Photo storage retention policy. Recommendation: ≤90 days
  default, configurable via `LE31_MEDIA_RETENTION_DAYS` env
  var. A separate feature adds the cron-based cleanup; not
  in scope for this slice.
- Photo file size cap. Recommendation: 5 MB (Telegram's
  bot API limit is 20 MB; 5 MB keeps the local storage
  footprint reasonable). Configurable via
  `LE31_MEDIA_MAX_BYTES` env var.
- Should the photo be **required** or **optional** for a
  stock entry? Recommendation: optional in v1 (the annotation
  is enough). A future "evidence-required" mode (gated on a
  charter revision) could make the photo required; not in
  scope here.
- Object-recognition on the photo. Recommendation: out of
  scope for v1; a future pick adds multimodal model
  suggestion with operator confirmation (gated on a charter
  revision authorising a multimodal model provider).

## Why this matters

`Sreenivas-Sadhu-Prabhakara/shelftrack` first surfaced in
2026-08-04 brainstorm (HMM-24) as a reference, but the
2026-08-14 re-push after 30 days of stable development is
what elevates it to brainstorm-grade. The shelftrack pattern
(snap → reorder level → low alert → CSV) maps cleanly to
LE31's cook bot, and the resulting **photo-first stock-entry
surface** is exactly the kitchen-side UX improvement the
operator notices during service.

The LE31 differentiator (per-batch append-only `StockEntry`
ledger paired with a Telegram cook surface) is **strengthened**
by this slice — the photo is *evidence* of the receiving
event, stored alongside the existing append-only row, with
the local file path derivable from the `photo_file_id`.
The cook can update stock during service with **one hand +
one photo** — the most-asked-for kitchen UX improvement in
the daily-research carries.

This is a **build candidate**, not an experiment. The slice
boundary is hard: one Telegram command + one Alembic
migration + one service helper + 4 test fixtures. If the
build validates, a follow-up pick adds the photo retention
policy and the optional object-recognition suggestion.

## Evidence (recorded)

- **Cross-section anchor 1**: `Sreenivas-Sadhu-Prabhakara/shelftrack`
  (0★, HTML PWA, MIT, created 2026-07-15, re-pushed 2026-08-14).
  *Photo-first stock list for a tiny shop — snap a product, set
  a reorder level, see what's running low at a glance, and
  export to CSV. 100% offline, nothing leaves your device.*
  Topics: `inventory, offline, privacy, pwa, small-business,
  stock-management`. Read at
  `/tmp/le31-brainstorm-2026-08-14/gh_topic_small_business.json`.
- **Cross-section anchor 2**: `Sreenivas-Sadhu-Prabhakara/slotone`
  (0★, JS, MIT, re-pushed 2026-08-14) — *private offline
  appointment day-book for a one-person business*. Same author,
  same low-effort single-operator offline-first pattern.
- **Cross-section anchor 3**: `gaganjainse/ClinicLedger` (1★,
  Kotlin, 2026-07-15) — *offline-first voice-assisted clinic
  ledger*. Different surface, different language, but the
  offline-first + ledger-as-source-of-truth + single small
  business pattern overlap is tight.
- **Carry-over**: `MahyarMozafar/demo-kitchenware` (HTML+
  seller-panel, 2026-08-12/13 daily-research) — same
  Telegram-to-inventory pattern, seller-panel variant.
- **In-repo dependency**: feature 03's `StockEntry` model;
  feature 04's Telegram photo-handler pattern; feature 37's
  `rationale` column; feature 39's owner-daily-recap export.
- **First surfaced**: `shelftrack` appeared in 2026-08-04
  brainstorm (HMM-24) as a reference; not promoted to a pick
  at the time. Today's re-push elevates it.
