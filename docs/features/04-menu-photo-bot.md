# Feature 04 — Menu Photo Bot (Telegram → OCR → Stock Setup)

## Goal

Each morning, the cook sends a photo of today's menu (chalkboard, printed sheet,
or handwritten list) to a Telegram bot. The bot extracts items + prices, asks
the cook to confirm or correct, then creates the day's `Batch` rows with
starting quantities.

## Scope

**In scope (v1):**
- Photo upload to Telegram bot.
- OCR (RapidOCR or PaddleOCR, language TBD).
- LLM post-processing to extract `{name, price}` pairs from raw OCR text.
- Inline keyboard for cook to confirm/edit/delete items.
- Per-item quantity prompts to create batches.
- Photo stored on disk + URL saved to `batch.photo_url`.

**Out of scope (v1):**
- Multi-photo menus (cook sends one photo, repeats if needed).
- Auto-language detection (cook sets language in `/start`).
- Voice input.

## Description

**Flow:**

1. Cook sends `/start_today` to the bot.
2. Bot replies: "Send me a photo of today's menu."
3. Cook sends photo.
4. Bot downloads, runs OCR (RapidOCR) → raw text.
5. Bot sends raw text + photo to LLM (GPT-4o-mini or local) with prompt:
   "Extract menu items from this text. Output JSON array of `{name, price}`."
6. Bot replies with extracted items as inline buttons:
   - `[✓ Schnitzel — 14€]  [✎]  [✗]`
   - `[✓ Burger — 12€]  [✎]  [✗]`
   - `[✓ Tiramisu — 6€]  [✎]  [✗]`
   - `[+ Add item manually]`
   - `[✓ Confirm all]`
7. Cook edits/deletes/adds until happy, taps **Confirm all**.
8. Bot walks through each item: "How many `Schnitzel` did you prep today?"
   (cook replies `20` or taps a quick-pick button).
9. For each item, a `Batch` is created with `qty_remaining = qty_start`,
   `prepared_at = now()`, `photo_url = <saved photo>`.
10. Bot replies: "Today's menu is live. Stock: 20 Schnitzel, 15 Burger, 8 Tiramisu."

## Tech stack

- **aiogram** for the bot framework (MIT, async, FSM).
- **RapidOCR** (`pip install rapidocr-onnxruntime`) — multi-language, no GPU needed.
- **OpenAI-compatible LLM API** for structured extraction (GPT-4o-mini, Gemini
  Flash, or local Qwen2.5-VL via Ollama). Pluggable.
- **Pillow** for any image preprocessing (rotate, contrast, crop).

## Failure modes & fallback

- **OCR returns garbage**: ask cook to retake the photo (better lighting,
  flatter angle).
- **LLM hallucinates**: cook sees the raw item list before confirming;
  always editable.
- **Network down**: bot queues the photo and processes later. Or cook can
  use a web fallback at `/admin/menu/upload`.

## Data flow

```
photo (jpg)
   ↓
bot receives via Telegram API
   ↓
download to /var/data/menu_photos/2026-07-24/091234.jpg
   ↓
RapidOCR → raw text
   ↓
LLM:  raw text + photo  →  JSON [{name, price}, ...]
   ↓
aiogram inline keyboard → cook confirms
   ↓
per-item quantity prompts
   ↓
INSERT INTO menu_item + batch + stock_entry
```

## Dependencies

- [03-kitchen-stock-tracker.md](03-kitchen-stock-tracker.md) — creates Batches.
- [../research/04-menu-ocr.md](../research/04-menu-ocr.md) — OCR options.
- [../research/05-telegram-bots.md](../research/05-telegram-bots.md) — aiogram.

## Open questions

- **Language** of menus? Drives OCR engine choice.
- **LLM provider**: hosted (OpenAI, Anthropic, Gemini) vs local (Ollama).
  Local is private but requires GPU.
- **Cost**: ~$0.01 per photo via GPT-4o-mini. If 365 photos/year, ~$3.65/year. Trivial.
- **Photo retention**: keep on disk forever? (Privacy / GDPR: menus are not
  personal data, so OK.)
- **Multi-shift**: cook takes a break, new cook continues setup. Need
  idempotency (don't double-create today's menu).

## Why this matters

This is the **primary onboarding path**. Without it, the system has zero value
on day 1 because there's no menu. Making it one photo + 60 seconds of taps
removes the biggest adoption barrier.