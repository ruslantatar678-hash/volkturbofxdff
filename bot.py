import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import get_forex_signal

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def start_menu(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📈 Сигнал на 2 мин", callback_data="signal_2")],
        [InlineKeyboardButton(text="📉 Сигнал на 5 мин", callback_data="signal_5")]
    ])
    await message.answer("Выберите период для анализа:", reply_markup=kb)

@dp.message(commands=["start"])
async def start_command(message: types.Message):
    await start_menu(message)

@dp.callback_query()
async def callbacks(call: types.CallbackQuery):
    if call.data.startswith("signal_"):
        period = int(call.data.split("_")[1])
        await call.message.answer("🔍 Анализирую рынок...")
        signal = await get_forex_signal(period)
        await call.message.answer(f"📊 Сигнал ({period} мин): {signal}")
        await start_menu(call.message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
