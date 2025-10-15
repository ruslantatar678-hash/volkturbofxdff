# Forex Signal Bot

Простой телеграм-бот для генерации сигналов на рынке Forex.

## 🚀 Локальный запуск

1. Скопируй `.env.example` в `.env` и добавь свои ключи.
2. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запусти бота:
   ```bash
   python bot.py
   ```

## 🌐 Деплой на Render
- Используй Dockerfile
- В переменных окружения укажи TELEGRAM_BOT_TOKEN и ALPHAVANTAGE_API_KEY
