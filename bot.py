import os
import sys
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from utils import get_forex_signal

# Загружаем переменные из .env (для локальных запусков)
load_dotenv()

# Проверяем токены
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

if not TELEGRAM_BOT_TOKEN:
    print("❌ ERROR: TELEGRAM_BOT_TOKEN is not set! Set it in Render Dashboard → Environment.", flush=True)
    sys.exit(1)

print("✅ Длина токена TELEGRAM:", len(TELEGRAM_BOT_TOKEN), flush=True)

# --- Бот ---
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_command(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📈 Сигнал на 2 мин", callback_data="signal_2")],
        [InlineKeyboardButton(text="📉 Сигнал на 5 мин", callback_data="signal_5")]
    ])
    await message.answer("Выберите период анализа:", reply_markup=kb)

@dp.callback_query()
async def callbacks(call: types.CallbackQuery):
    if call.data.startswith("signal_"):
        period = int(call.data.split("_")[1])
        await call.message.answer("🔍 Анализирую рынок...")
        signal = await get_forex_signal(period)
        await call.message.answer(f"📊 Сигнал ({period} мин): {signal}")

async def main():
    print("🚀 Bot started successfully!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

