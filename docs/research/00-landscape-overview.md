# Restaurant Software Landscape — Broad Survey

Research compiled July 2026 via the GitHub REST API and direct README fetches.
Stars and last-push dates reflect what was returned at fetch time.

## TL;DR

There is **no single open-source project** that fits the user's exact spec:
*Telegram-driven kitchen, finite stock of prepared items, table-side ordering with
guest demographics, and tip derived from `total_paid − items_consumed`*.

The closest open-source projects cluster into three groups:

| Group | Best projects | Why not perfect fit |
|---|---|---|
| **Full-stack POS** | [TastyIgniter](https://github.com/tastyigniter/TastyIgniter), [URY](https://github.com/ury-erp/ury), [RestoPOS](https://github.com/faizaldevs/RestoPOS) | Big, PHP-heavy, built for multi-location; too heavy for one small restaurant |
| **POS + KDS bundles** | [URY Mosaic](https://github.com/ury-erp/mosaic) (KDS), [evan361425/flutter-pos-system](https://github.com/evan361425/flutter-pos-system) (mobile POS) | Flutter version has good demographics; Mosaic is tightly coupled to ERPNext |
| **Adjacent tools** | [Nishiki](https://github.com/nishiki-tech/nishiki-frontend) (food inventory), [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) / [RapidOCR](https://github.com/RapidAI/RapidOCR) (OCR), [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) / [aiogram](https://github.com/aiogram/aiogram) (bots) | Each does one thing well; need to compose |

The recommended path is to **build a thin Python/FastAPI app + Telegram bot that
composes a few existing libraries**, rather than fork any of the heavy POS
projects. See `docs/research/09-recommended-stack.md` for the architecture sketch.

---

## Category indexes

- [01 — POS Systems](./01-pos-systems.md)
- [02 — Kitchen Display Systems (KDS)](./02-kitchen-display.md)
- [03 — Inventory & Finite-Stock Tracking](./03-inventory-stock.md)
- [04 — Menu Digitization / OCR](./04-menu-ocr.md)
- [05 — Telegram Bot Frameworks for Operational Workflows](./05-telegram-bots.md)
- [06 — Payments, Tips & Reconciliation](./06-payments-tips.md)
- [07 — Guest / Table Analytics](./07-guest-analytics.md)
- [08 — Deep-Dive: Top 5 Projects to Fork/Extend](./08-deep-dive-top-5.md)
- [09 — Recommended Stack & Architecture](./09-recommended-stack.md)

---

## Method

- GitHub REST API used (rate-limited; some calls needed retry after 30s).
- Browser tools unavailable on this machine; verification done via
  `raw.githubusercontent.com` README fetches.
- All URLs and stars in the per-category files were verified against
  fetched content, not generated.

## Confidence & gaps

- **High confidence**: project names, repo URLs, license, primary language, last-push date.
- **Medium confidence**: feature lists (READMEs are marketing-leaning; real source-of-truth is the code).
- **Low confidence**: live demo URLs, install complexity (some require Docker + Frappe + Node + Postgres, others are one-binary).