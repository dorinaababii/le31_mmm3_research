# cook-photo-stock-list-pwa — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/65-cook-photo-stock-list-pwa.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `65`
- Slug: `cook-photo-stock-list-pwa`
- Contract file: `features/65-cook-photo-stock-list-pwa.md`
- Bucket: **v2 owner-pains (cook-UX)** (same bucket as feature 04,
  different JTBD — stock entry, not menu item parsing)
- Linear parent: `HMM-77` (Brainstorm 2026-08-14 — daily)
- Linear sub-issue: `HMM-80` (see `le31 v1 — Core MVP` project,
  label `Feature`; matches the v2 owner-pains sub-issue convention
  used by features 58/61/62/63)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (`Sreenivas-Sadhu-Prabhakara/shelftrack` HTML PWA
MIT, created 2026-07-15, re-pushed 2026-08-14, the strongest
in-window cross-section anchor for the photo-first stock-entry
pattern; corroborating `Sreenivas-Sadhu-Prabhakara/slotone` JS
MIT re-pushed 2026-08-14 same author; `gaganjainse/ClinicLedger`
Kotlin 1★ 2026-07-15 corroborating offline-first + ledger-as-source
pattern). Confidence: **medium-high**.

**Decision: build candidate (v2 owner-pains M effort, ≤1 week).**
The slice is medium-sized; it touches the Telegram bot state
machine, the `StockEntry` model, and a new media-storage helper.
Circuit breaker: remove the `/stock-snap` command registration;
the existing `StockEntry` text-entry path remains unchanged.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2 owner-pains, the slicing
   discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-brainstorm` (this pick came from the daily
   brainstorm job on 2026-08-14).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request
them from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/alembic/versions/XXXX_add_stock_entry_photo_file_id.py   # NEW migration
backend/app/models/stock_entry.py                               # EDIT: add photo_file_id field (nullable)
backend/app/services/media.py                                   # NEW: aiogram get_file → local storage (≤100 LOC)
backend/app/services/stock_entry.py                             # EDIT: create_stock_entry_from_photo helper (≤60 LOC)
bot/cook_bot.py                                                 # EDIT: /stock-snap command + photo handler state machine (≤120 LOC)
bot/keyboards.py                                                # EDIT: confirmation keyboard (≤30 LOC)
backend/tests/test_cook_stock_snap.py                           # NEW: 4 fixtures
bot/README.md                                                   # note /stock-snap command + photo retention policy
```

No new pip dependencies. aiogram v3's `get_file` and photo
handler are already in use; the local storage path uses stdlib
`pathlib` + `aiofiles` (already a soft transitive dep).

## Endpoints and bot commands added

- `/stock-snap` (cook-only). State machine:
  `awaiting_photo` → `awaiting_annotation` (optional) →
  `awaiting_confirm` → write `StockEntry` row.
- Inline confirmation keyboard: "Confirm" / "Edit annotation"
  / "Cancel".
- No new REST endpoints; the `StockEntry` write path goes
  through the existing `backend/app/services/stock_entry.py`
  helper.

## Media storage path

`backend/app/services/media.py` saves Telegram photo uploads
under `var/stock_photos/YYYY-MM-DD/<uuid>.<ext>`. The path is
configurable via the `LE31_MEDIA_ROOT` env var, default
`./var/stock_photos`. The Telegram `file_id` is stored in the
`stock_entry.photo_file_id` column for retrieval.

Photo retention policy (≤90 days default) is **out of scope**
for v1 of this slice; a separate feature adds the cron-based
cleanup.

## Schema (additive migration)

```sql
-- XXXX_add_stock_entry_photo_file_id.py
ALTER TABLE stock_entry
  ADD COLUMN photo_file_id TEXT NULL;
```

Nullable = backwards-compatible. Existing `StockEntry` rows
have `NULL`; the append-only invariant is intact (no
UPDATE/DELETE).

## Stock entry helper (spec for the coding agent)

```python
# backend/app/services/stock_entry.py extension (≤60 LOC)

async def create_stock_entry_from_photo(
    *,
    photo_file_id: str,
    annotation: str | None,
    prep_station: str,
    qty: Decimal,
    unit: str,
    ingredient_id: int,
    actor_id: int,
) -> StockEntry:
    """Create a StockEntry from a Telegram photo upload.

    Side effect: saves the photo file locally under
    var/stock_photos/YYYY-MM-DD/<uuid>.<ext>.
    """
    # 1. Save photo locally
    local_path = await media.save_telegram_photo(photo_file_id)
    # 2. Write the ledger row (append-only; one row, never updated)
    entry = StockEntry(
        ingredient_id=ingredient_id,
        qty_delta=qty,
        unit=unit,
        actor_id=actor_id,
        prep_station=prep_station,
        rationale=annotation,         # reuse feature 37's rationale column
        photo_file_id=photo_file_id,  # NEW; nullable
        created_at=datetime.now(UTC),
    )
    session.add(entry)
    await session.flush()
    # 3. Trigger low-alert if qty drops below reorder point (feature 26)
    await stock_alert.maybe_emit_low_alert(entry)
    return entry
```

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent
MUST:

1. Write all 4 test fixtures; `pytest backend/tests/test_cook_stock_snap.py`
   must pass.
2. With `/stock-snap` flow: confirm the cook bot receives
   the photo, the annotation prompt appears, the confirmation
   keyboard renders, and the `StockEntry` row lands with the
   `photo_file_id` populated.
3. With `/stock-snap` flow + low stock: confirm the existing
   low-alert Telegram message is emitted (no change to feature
   03's behavior).
4. With `pytest backend/tests/test_stock_entry.py` (feature 03's
   suite): the existing text-entry path must pass unchanged;
   the new `photo_file_id` column must accept `NULL`.
5. Confirm the photo file is saved under `var/stock_photos/YYYY-MM-DD/`
   and the path is reachable from `photo_file_id` via the
   media helper.
6. Confirm ledger hash integrity: the existing
   `pytest backend/tests/test_postledger_hash.py` (feature 49's
   suite) must pass unchanged.

## Rollback / feature-removal path

1. Remove the `/stock-snap` command registration from `bot/cook_bot.py`.
2. Remove the `create_stock_entry_from_photo` helper from
   `backend/app/services/stock_entry.py`.
3. Drop the Alembic migration:
   `ALTER TABLE stock_entry DROP COLUMN photo_file_id;`
4. Delete `backend/app/services/media.py` and the test file.

Estimated rollback cost: ≤30 minutes.

## Files for the coding agent to verify against

```
features/65-cook-photo-stock-list-pwa.md
specs/cook-photo-stock-list-pwa-HANDOFF.md                (this file)
features/03-kitchen-stock-tracker.md                      (parent: StockEntry model)
features/04-menu-photo-bot.md                            (sibling: Telegram photo handler pattern)
features/37-void-rationale-ledger-field.md                (sibling: rationale column)
features/39-owner-daily-recap-telegram.md                 (downstream: recap surface)
features/26-reorder-point-on-stockentry.md                (downstream: low-alert trigger)
skills/le31-conventions/SKILL.md
skills/le31-v1-feature-pattern/SKILL.md
skills/le31-handoff-spec/SKILL.md
PROJECT_CHARTER.md
```
