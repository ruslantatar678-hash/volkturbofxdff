import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

print(f"✅ Длина токена TELEGRAM: {len(TELEGRAM_BOT_TOKEN)}")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден! Убедись, что он добавлен в переменные окружения Render.")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Главное меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📈 Вверх"), KeyboardButton(text="📉 Вниз")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("👋 Привет! Выберите направление для сигнала:", reply_markup=menu)

@dp.message(F.text == "📈 Вверх")
async def signal_up(message: Message):
    await message.answer("🔼 Сигнал на ВВЕРХ (действует 2-5 минут)")

@dp.message(F.text == "📉 Вниз")
async def signal_down(message: Message):
    await message.answer("🔽 Сигнал на ВНИЗ (действует 2-5 минут)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
