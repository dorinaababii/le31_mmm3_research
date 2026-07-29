# Menu Digitization / OCR

The user wants the cook to **upload a photo of today's menu** (e.g. a chalkboard
or a printed sheet) and have the system extract the items. This is OCR +
structured extraction.

## Top projects

| # | Project | Repo | ⭐ | Last push | License | Stack |
|---|---|---|---|---|---|---|
| 1 | **PaddleOCR** | https://github.com/PaddlePaddle/PaddleOCR | ~50k+ | very active | Apache-2.0 | Python + PaddlePaddle / ONNX |
| 2 | **RapidOCR** | https://github.com/RapidAI/RapidOCR | ~3k+ | active | Apache-2.0 | Python wrapper over ONNXRuntime |
| 3 | **donut** (NAVER) | https://github.com/clovaai/donut | ~6k+ | 2024 | MIT | Python + PyTorch, end-to-end DocAI |
| 4 | **OCRmyPDF** | https://github.com/ocrmypdf/OCRmyPDF | ~10k+ | active | MPL-2.0 | CLI over Tesseract |
| 5 | **scan-bill** | https://github.com/muslimalfatih/scan-bill | small | dormant | — | receipt OCR reference impl |

## What each is good at

- **PaddleOCR** — best accuracy on Chinese/English scene text; the de-facto
  choice for "photo of a menu in the wild". Heavier install (~1 GB model).
- **RapidOCR** — drop-in replacement using ONNXRuntime; faster install,
  slightly lower accuracy, multi-language.
- **donut** — end-to-end transformer that takes image → structured JSON.
  No separate text-detection step. Best for *structured* docs (forms, invoices)
  but can be fine-tuned for menus. Training data is the hard part.
- **OCRmyPDF** — adds a text layer to PDFs; useful if the menu is a PDF upload.

## Recommendation for our app

**Pipeline:**
1. Cook sends photo to Telegram bot.
2. Bot downloads image, runs **RapidOCR** (lightweight, easy `pip install`).
3. Post-process with regex + a small LLM (GPT-4o-mini, Gemini Flash, or local
   Qwen-VL) to convert raw OCR text → structured `{name, price, qty, photo_url}`.
4. Bot replies with "Here's what I read — confirm or correct?" inline keyboard.
5. On confirm, items are added to today's `Menu` table and `Batch` rows are
   auto-created with `qty=1` (cook then updates qty).

**Why not pure OCR?** Menu photos are messy — handwritten prices, struck-out
items, multi-language. A small LLM call (~1 cent per photo) makes the structured
extraction reliable.

**Why not donut end-to-end?** We'd need to label a training set of restaurant
menus in our own language/style. Not worth it for a single restaurant.

## Cost & latency

- RapidOCR on a phone-photo menu: ~2-4s on CPU.
- LLM post-processing: ~3-5s via API.
- Total: ~7s, acceptable for a once-a-day workflow.

See [../features/04-menu-photo-bot.md](../features/04-menu-photo-bot.md).