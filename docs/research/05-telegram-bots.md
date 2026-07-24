# Telegram Bot Frameworks for Operational Workflows

The user wants the cook to drive the kitchen side of the system via Telegram.
We need to choose the bot framework + decide what to build on top.

## Top frameworks

| # | Project | Repo | ⭐ | Last push | License | Stack |
|---|---|---|---|---|---|---|
| 1 | **python-telegram-bot** | https://github.com/python-telegram-bot/python-telegram-bot | ~29k | 2026-07-24 | GPLv3 / LGPLv3 (v13-) | Python, asyncio |
| 2 | **aiogram** | https://github.com/aiogram/aiogram | ~5k | active | MIT | Python, asyncio, type-hinted |
| 3 | **python-telegram-bot** v20+ | (same repo) | — | — | LGPLv3 | modernized asyncio |
| 4 | **telebot** (pyTelegramBotAPI) | https://github.com/eternnoir/pyTelegramBotAPI | ~7k | active | LGPL | sync + async |

## python-telegram-bot (PTB) — pros / cons

- **Pros**: largest community, most StackOverflow answers, lots of extensions
  (job-queue, persistence, conversation handlers), well-documented.
- **Cons**: GPL license (v20+ LGPL — fine for our closed internal bot).
- **ConversationHandler**: a state machine per user — perfect for "upload menu
  photo → confirm items → set quantities" workflow.

## aiogram — pros / cons

- **Pros**: very clean async API, type hints, MIT license, FSM (finite-state
  machine) for multi-step flows is elegant. Lower boilerplate.
- **Cons**: smaller community than PTB; docs OK but fewer SO answers.

## Which to pick

For this project: **aiogram**. Reasons:
1. **MIT license** = no copyleft contagion into our codebase.
2. **FSM + Router pattern** maps cleanly onto our workflow (photo → OCR →
   confirm → set stock).
3. Type hints → easy to keep the bot layer readable.
4. We can integrate `python-telegram-bot` only if a specific extension is needed.

## Operations patterns to copy from existing bots

- **Inline keyboards for confirm/cancel** instead of typing commands.
- **One bot, many roles**: same bot, different behaviour per `user_id`
  (cook vs manager). Persist role in DB.
- **Conversation timeouts**: 10 minutes idle → drop the FSM state.
- **Webhook > polling** for production (single HTTP endpoint); polling OK for dev.

## Bot command surface (proposed)

**Cook**:
- `/start_today` — begin shift; bot asks for menu photo
- (send photo) — OCR → confirm items → set quantities per item
- `/stock` — current batch quantities + alerts
- `/sold_out <item>` — mark an item out for the rest of the day
- `/eod` — end-of-day report: sold vs leftover
- `/leftover <item> <qty>` — record waste for tomorrow's prep estimate

**Manager**:
- `/demand_forecast` — based on last 14 days, suggest tomorrow's prep
- `/sales_today` / `/sales_week`
- `/export_csv` — daily takings + tips

**Waiter**:
- `/my_tables` — list of tables I'm serving
- `/add <table> <item> [qty]` — quick line add
- `/bill <table>` — print + send bill to kitchen/payment

See [../features/04-menu-photo-bot.md](../features/04-menu-photo-bot.md).