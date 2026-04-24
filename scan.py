import random
import time
import zlib
import asyncio
import requests
from telegram import Bot

# ================= CONFIG =================
WORDS_1_10 = ["wise", "gas", "choice", "maze", "muffin", "gown", "flame", "camp", "hill", "deliver"]

TELEGRAM_TOKEN = "7654735781:AAGcVIbnVux2u1gyBKTS3F9SUmIxZMqXhYg"
TELEGRAM_CHAT_ID = "5568964448"

MAX_LOOP = 5000
# ==========================================

print("🔥 SCRIPT START")

# ================= TELEGRAM =================
bot = Bot(token=TELEGRAM_TOKEN)

async def kirim(msg):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)
    except Exception as e:
        print("Telegram error:", e)

# ================= LOAD WORDLIST =================
print("📥 Loading wordlist...")

url = "https://raw.githubusercontent.com/monero-project/monero/master/src/mnemonics/english.txt"

WORDLIST = []

for i in range(3):  # retry 3x
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            WORDLIST = r.text.strip().split("\n")
            break
    except:
        pass

print("Wordlist length:", len(WORDLIST))

if len(WORDLIST) < 1000:
    print("❌ Wordlist gagal load (fallback aktif)")
    
    WORDLIST = [
        "abbey","ability","ablaze","abnormal","abort","abrasive","absorb",
        "abyss","academy","acquire","across","adapt","addicted","adept",
        "adjust","adopt","adorable","adrenalin","adult","advance","adverb",
        "adverse","advert","advice","hidden","wall","gold","secret"
    ]

    print("⚠️ Pakai fallback wordlist:", len(WORDLIST))

# ================= CHECKSUM =================
def get_checksum(words):
    prefix = "".join(word[:3] for word in words)
    crc = zlib.crc32(prefix.encode()) & 0xffffffff
    return WORDLIST[crc % len(WORDLIST)]

# ================= SCAN =================
print("\n🚀 START SCANNING")

start = time.time()
found = 0

for i in range(MAX_LOOP):
    w11 = random.choice(WORDLIST)

    first_11 = WORDS_1_10 + [w11]
    w12 = get_checksum(first_11)

    seed = " ".join(first_11 + [w12])

    # 🎯 FILTER (sementara dibuat gampang dulu buat test)
    if True:
        found += 1

        msg = f"""
🎯 Candidate Found

Seed:
{seed}

Loop: {i}
Time: {time.strftime("%H:%M:%S")}
"""

        print(msg)
        asyncio.run(kirim(msg))

print("\n✅ DONE")
print(f"Checked: {MAX_LOOP}")
print(f"Found: {found}")
print(f"Time: {time.time()-start:.2f}s")
