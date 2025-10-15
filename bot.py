# --- проверка переменных окружения (вставить в самом верху bot.py) ---
import os, sys
from dotenv import load_dotenv

load_dotenv()  # для локальной разработки; в Render не обязателен

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# Выдаём короткое информативное сообщение и выходим, если чего-то нет
if not TELEGRAM_BOT_TOKEN:
    print("❌ ERROR: TELEGRAM_BOT_TOKEN is not set! Set it in Render Dashboard → Environment.", flush=True)
    sys.exit(1)

if not ALPHAVANTAGE_API_KEY:
    print("❌ ERROR: ALPHAVANTAGE_API_KEY is not set! Set it in Render Dashboard → Environment.", flush=True)
    sys.exit(1)

# Для отладки можно напечатать длину токена (не сам токен):
print("✅ TELEGRAM token length:", len(TELEGRAM_BOT_TOKEN), flush=True)
# -------------------------------------------------------------------
