# Feature 41 — Telegram Text-Message Stock Update

> **Priority**: P1 · **Effort**: S (≤ 1 day) · **Source**: daily research 2026-08-07
> (Pick B) · **Bucket**: v1 polish on feature 04 / feature 03
> **One-line**: Extend the existing cook Telegram bot (feature 04) with a
> thin text-command parser that accepts free-form `<N> <item> <action>` messages
> (e.g. `5 lamb pour`, `3 focaccia done`, `2 burger 86`) and writes the matching
> `StockEntry` row through the existing `StockEntry` write API, so the cook can
> update kitchen state + inventory without OCR, without a photo, and without
> remembering the exact `/kitchen_done <ticket_id>` command. Validated by the in-
> window peer `Walid-Amr/My-n8n-workflow` (pushed 2026-08-06, n8n + Google
> Sheets + Telegram "Your kitchen team sends one Telegram message. Your
> inventory updates itself").

## Goal

Make the cook Telegram bot fully usable for stock updates **before the OCR
photo pipeline (feature 04 v1) ships**. The cook's morning flow today is
"send a photo → confirm OCR → start batches." The cook's afternoon flow is
"see a ticket → run the kitchen." In between, the cook frequently needs to
update stock ("3 lamb pour," "2 burger 86") without leaving Telegram. The
existing `/kitchen_done <ticket_id>` command forces the cook to switch to a
menu-style keyboard; a free-form text command is faster and matches the
external-peer pattern.

This feature is a v1 polish on feature 04 (cooking Telegram bot) and feature
03 (kitchen stock tracker). It does not replace either; it adds a text-input
alternative to the existing structured inputs.

## Scope

**In scope (v1 polish):**
- A new aiogram v3 message handler in the existing
  `backend/app/bot/cook_bot.py` that fires on every plain-text Telegram
  message that does NOT match an existing command (`/start`, `/kitchen_done`,
  `/menu`, etc.) AND matches the regex `^(\d+)\s+(\S+)\s+(pour|done|restock|86|cancel|comp|void)$/i`.
- A small `item_alias` table (1-column CSV at `data/item_alias.csv` or a
  SQLModel table, TBD) keyed on the alias string, mapping to the existing
  `MenuItem.slug` column. Example: `lamb` → `lamb-ragu`, `focaccia` →
  `focaccia-rosmarino`. If the alias does not resolve, the bot replies with
  a list of the 5 closest item names from the existing `MenuItem` table.
- The matched action is interpreted against the existing `StockEntry`
  write API:
  - `pour` → `qty_delta = +N` (new batch line; the cook is taking a prep
    step in the kitchen and recording the production).
  - `done` → `qty_delta = -N` (the cook is selling N from current stock;
    linked to the most-recent open `OrderItem` if one exists, else just a
    decrement on the `current_stock` derivation).
  - `restock` → `qty_delta = +N` (new batch line; the cook is marking a
    restock event).
  - `86` → `qty_delta = 0` with `note = "86'd by <cook_name>"` and a
    `rationale` populated with the parse-time text (the cook is removing
    the item from the daily menu).
  - `cancel` / `comp` / `void` → `qty_delta = +N` (reverse, with
    `rationale` populated; the cook is restoring stock for a cancelled
    sale).
- The bot replies with the canonical confirmation message:
  ```
  ✅ <cooked> <action> — `<item_slug>` × <N> at <HH:MM> Paris. Stock now: <derived> <unit>.
  ```
- Defence: the regex rejects anything that is not `<N> <token> <action>`.
  No LLM, no fuzzy matching, no aliases resolved from multilingual input.
  Hard scope: regex + alias table only.

**Out of scope (v1):**
- Multilingual aliases (charter §3.6 — single menu language, decided at
  install time).
- Free-form NLU ("I just put 5 lamb on the stove" → pour 5 lamb). This is a
  v2-AI candidate; explicit out of v1 by the same charter §3.2 rule that
  forbids AI on any customer-facing surface.
- Voice input. Cross-references `feature 38 — cook-voice-note-to-stockentry`
  (filed 2026-08-06) which is a separate v2-AI polish.
- Quantity rationale prompted interactively. The `86` / `cancel` / `comp`
  / `void` actions populate the `rationale` field from the matched text
  directly; no follow-up prompt. A follow-up prompt is recorded as a v2
  polish (cross-references `feature 37 — void-rationale-ledger-field`).

## Description

**External validation of the pattern.** Today's daily research surfaced
[`Walid-Amr/My-n8n-workflow`](https://github.com/Walid-Amr/My-n8n-workflow)
(pushed 2026-08-06, n8n + Google Sheets + Telegram Bot API, 1★). The README
is explicit:

> Triggered by a simple Telegram message (e.g. `5 Done`).
> - Telegram Trigger — listens for staff messages
> - Code node (Python) — parses the message into Order Number and Status
> - Switch — routes the order down a Done or Cancel path
> - Update row (Sheet1) — updates the order's status
> - Get row (Sheet1) — retrieves full order details, including ingredients used
> - Parallel branches — one per ingredient (e.g. bread, cheese, burger), each
>   deducting the used quantity from its stock sheet in real time

This is the same UX pattern LE31's cook bot already supports for the
`/kitchen_done <ticket_id>` command, but exposed as a free-form text input.
The external implementation is heavier (n8n + Google Sheets + Python Code
node + Switch), but the user-facing pattern is identical: a single Telegram
message → kitchen state + inventory both update. The implicit conclusion is
that the text-message path is what ships first in the wild, not the OCR
photo pipeline.

**Internal motivation.** The cook's first day of LE31 use may not have the
photo OCR pipeline fully wired yet (feature 04 is a v1 polish with a
non-trivial OCR + LLM setup). The text-message path is a fallback that is
useful even after feature 04 ships: the cook prefers typing `5 lamb pour`
to opening the camera, taking a photo, and waiting for OCR.

## Data model

**No new tables**, by charter §3.1 (no silent duplication of stock state).
**One new column** is needed on the existing `StockEntry` table:

```python
# backend/app/models.py (additive)
# Add `rationale: str | None = Field(default=None, max_length=500)` to the
# existing StockEntry model. Migration adds a nullable `rationale` column.
```

This is the same column that `feature 37 — void-rationale-ledger-field`
introduces for voids. Coordinate the migration; if feature 37 is already
merged, this feature reuses the column. If feature 37 is not yet merged,
this feature ships alongside it or defers until feature 37 is in. Open
question for the coding agent: confirm the merge order with the operator.

The `item_alias` resolution is **not** a new table. It is a small CSV
file at `data/item_alias.csv` with two columns (`alias, menu_item_slug`)
and a flat-file loader. CSV gives the operator a trivial path to add new
aliases without a database migration. Migration to a SQLModel table is
recorded as a v2 polish.

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**
- New handler: `bot.on_message(F.text.regexp(r"^(\d+)\s+(\S+)\s+(pour|done|restock|86|cancel|comp|void)$/i"))`.
- The handler reads `(N, item_alias, action)` from the regex match.
- The handler resolves `item_alias` → `MenuItem.slug` via the CSV file.
  - If resolution fails, the bot replies with a list of the 5 closest
    `MenuItem.name` rows and the alias short-list (so the cook can pick the
    next attempt).
- The handler writes the canonical `StockEntry` row through the existing
  `StockEntry` write API (the same one used by `/kitchen_done` and the
  existing `/menu` photo bot flow).
- The handler replies with the canonical confirmation message above.

**API (FastAPI):**
- No new HTTP routes. The text-message path is a bot-only input.
- The existing `StockEntry` write API is unchanged.

**Web UI:**
- No changes. The cook screen continues to be read-only via the SSE
  cook-channel (feature 23 + feature 35).

## Implementation

1. Read this file (you are doing it).
2. Read `Walid-Amr/My-n8n-workflow` README at
   [https://github.com/Walid-Amr/My-n8n-workflow](https://github.com/Walid-Amr/My-n8n-workflow)
   — 15 min.
3. Read `features/04-menu-photo-bot.md` and `features/03-kitchen-stock-tracker.md`
   to confirm the existing `StockEntry` write API.
4. Confirm the `rationale` column migration is in place (either via
   `feature 37` or this feature ships the migration).
5. Create `data/item_alias.csv` with at least 5 entries (lamb, focaccia,
   burger, tiramisu, panna-cotta) so the first deployment isn't empty.
6. Add the new aiogram v3 handler to `backend/app/bot/cook_bot.py`.
7. Add a `register_stock_message_handler()` function that
   `bot.message.register(...)` calls at startup.
8. Manual verification (see Verification protocol in the slice handoff).
9. Commit: `git add backend/app/bot/cook_bot.py data/item_alias.csv backend/app/models.py INDEX.md && git commit -m "Feature 41: Telegram text-message stock update (regex + item_alias)"`.

## Telegram interaction

The new surface is a text-message handler. The interaction is:

- **Cook**: `5 lamb pour`
- **Bot**: `✅ 5 lamb pour — lamb-ragu × 5 at 14:32 Paris. Stock now: 12 portions.`

- **Cook**: `2 burger 86`
- **Bot**: `🚫 2 burger 86'd — burger × 2 at 14:33 Paris. Rationale: "2 burger 86". Removed from today's menu.`

- **Cook**: `5 mystery thing done` (alias not resolved)
- **Bot**: `❓ "mystery thing" didn't match any menu item. Did you mean: ?`
  - (Inline keyboard with the 5 closest `MenuItem.name` rows + `Cancel`)

The handler is `<N> <alias> <action>` only. Anything else is ignored.

## Dependencies

- `features/04-menu-photo-bot.md` — the existing aiogram v3 framework and
  webhook that this feature extends.
- `features/03-kitchen-stock-tracker.md` — the existing `StockEntry` write
  API that this feature reuses.
- `features/37-void-rationale-ledger-field.md` — the `rationale` column
  on `StockEntry` that this feature writes to. Coordinate merge order.
- `features/23-sse-cook-channel.md` — the cook screen that sees the
  resulting `StockEntry` events in real time.
- `Walid-Amr/My-n8n-workflow` — the external validation of the pattern.

## Open questions

- `86` action: should it write a `qty_delta = 0` row with `rationale`,
  or should it be a separate `Item86` event that the cook screen consumes?
  Decision: `qty_delta = 0` row with `rationale` for v1 — consistent with
  the `StockEntry` append-only invariant. A separate `Item86` event is
  recorded as a v2 polish.
- Should the `item_alias.csv` also live in the database for operator
  recovery? Decision: CSV for v1 (no migration needed). Database-backed
  aliases is a v2 polish.
- Should the bot ask for a reason when the cook types `void` / `cancel` /
  `comp`? Decision: no for v1 — the parsed text is the rationale. A
  follow-up prompt is a v2 polish.
- Coordinate merge order with `feature 37 — void-rationale-ledger-field`.
  If feature 37 is already merged, this feature reuses the column. If
  feature 37 is not yet merged, this feature ships the migration (as
  either an additive nullable column or a feature 37 PR first).

## Why this matters

The cook's first day of LE31 use may not have the photo OCR pipeline
(feature 04) fully wired. Even after feature 04 ships, the cook prefers
typing `5 lamb pour` to opening the camera, taking a photo, and waiting
for OCR. The text-message path is a lighter, faster input that
**external evidence** (today's `Walid-Amr/My-n8n-workflow` peer) shows
is what ships first in the wild. The cost is ≤ 1 day of work and ≤ 100
LOC of pure Python; the value is a cook bot usable before feature 04
ships AND faster than feature 04 after it ships. The append-only
`StockEntry` invariant is preserved (no UPDATE / no DELETE on the
ledger).
