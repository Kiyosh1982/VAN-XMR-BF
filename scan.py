import random
import time
import zlib
import asyncio
import os
import requests
from telegram import Bot

# ================= CONFIG =================
WORDS_1_10 = ["wise", "gas", "choice", "maze", "muffin", "gown", "flame", "camp", "hill", "deliver"]

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TG_CHAT_ID")

MAX_LOOP = 5000   # bisa kamu naikkan
# ==========================================

# ================= TELEGRAM =================
bot = Bot(token=TELEGRAM_TOKEN)

async def kirim(msg):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)
    except:
        pass

# ================= LOAD WORDLIST =================
print("📥 Loading wordlist...")

url = "https://raw.githubusercontent.com/monero-project/monero/master/src/mnemonics/english.txt"
WORDLIST = requests.get(url, timeout=10).text.strip().split("\n")

if len(WORDLIST) < 1000:
    print("❌ Wordlist gagal load")
    exit()

print(f"✅ Wordlist loaded: {len(WORDLIST)} words")

# ================= CHECKSUM =================
def get_checksum(words):
    prefix = "".join(word[:3] for
