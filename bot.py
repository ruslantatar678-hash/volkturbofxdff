import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import get_forex_signal

if __name__ == "__main__": 
    import asyncio
    from aiogram import Bot, Dispatcher
    from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

    from utils import get_forex_signal

    async def main():
        dp = Dispatcher()
        bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))

        @dp.message(commands=["start"])
        async def start_command(message: Message):
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="📈 Сигнал на 2 мин", callback_data="signal_2")],
                [InlineKeyboardButton(text="📉 Сигнал на 5 мин", callback_data="signal_5")]
            ])
            await message.answer("Выберите период анализа:", reply_markup=kb)

        @dp.callback_query()
        async def callbacks(call):
            if call.data.startswith("signal_"):
                period = int(call.data.split("_")[1])
                await call.message.answer("🔍 Анализирую рынок...")
                signal = await get_forex_signal(period)
                await call.message.answer(f"📊 Сигнал ({period} мин): {signal}")

        print("🚀 Bot started successfully!")
        await dp.start_polling(bot)

    asyncio.run(main())
