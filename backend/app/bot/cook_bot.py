"""Telegram bot stub (aiogram v3).

Implements the cook-side workflow from `docs/features/04-menu-photo-bot.md`.
The full FSM flow is described below — the actual handlers will be added
once the OCR + LLM pipeline is wired up.

Bot commands (from `docs/research/05-telegram-bots.md`):

  /start_today     begin shift; bot asks for menu photo
  /stock           current batch quantities + alerts
  /sold_out <item> mark an item out for the rest of the day
  /eod             end-of-day report: sold vs leftover
  /leftover <item> <qty>   record waste for tomorrow's prep estimate
  /forecast        demand estimate for tomorrow

State machine (FSM):

  idle
    └── /start_today ──► awaiting_photo
                          └── (photo received) ──► ocr_running
                                                     └── ocr_done ──► awaiting_confirm
                                                                      └── (confirm) ──► awaiting_quantities
                                                                                          └── (done) ──► idle
"""

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from ..config import settings


class CookFlow(StatesGroup):
    """FSM states for the cook's morning menu setup."""
    idle              = State()
    awaiting_photo    = State()
    ocr_running       = State()
    awaiting_confirm  = State()
    awaiting_quantities = State()


async def cmd_start_today(message: Message, state: FSMContext) -> None:
    """`/start_today` handler — ask the cook for the menu photo."""
    await state.set_state(CookFlow.awaiting_photo)
    await message.answer(
        "Good morning! Send me a photo of today's menu and I'll set up the stock."
    )


async def on_photo(message: Message, state: FSMContext) -> None:
    """Receive a photo, kick off OCR, transition to awaiting_confirm."""
    current = await state.get_state()
    if current != CookFlow.awaiting_photo.state:
        return  # ignore photos sent outside the flow
    await state.set_state(CookFlow.ocr_running)
    # TODO: download photo, run RapidOCR + LLM, populate parsed items.
    # For now, just acknowledge.
    await message.answer(
        "Photo received — OCR pipeline not yet wired up. "
        "See docs/features/04-menu-photo-bot.md for the next step."
    )
    await state.set_state(CookFlow.idle)


async def cmd_help(message: Message) -> None:
    await message.answer(
        "Cook commands:\n"
        "/start_today — begin shift, upload menu photo\n"
        "/stock — current batches\n"
        "/sold_out <item> — mark item sold out\n"
        "/eod — end-of-day summary\n"
        "/leftover <item> <qty> — log waste\n"
        "/forecast — tomorrow's prep estimate\n"
    )


def build_dp() -> Dispatcher:
    """Build the aiogram Dispatcher with our handlers."""
    dp = Dispatcher()
    dp.message.register(cmd_start_today, Command("start_today"))
    dp.message.register(cmd_help, Command("help"))
    # Photo handler is registered loosely (no command filter) but checks FSM state.
    # TODO: register on_photo when the FSM is in awaiting_photo state.
    return dp


async def run_bot() -> None:
    """Entry point. Run via: `python -m app.bot.run` (when implemented)."""
    if not settings.telegram_bot_token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set in .env")
    bot = Bot(token=settings.telegram_bot_token)
    dp = build_dp()
    # TODO: filter incoming messages to allowed user IDs.
    await dp.start_polling(bot)