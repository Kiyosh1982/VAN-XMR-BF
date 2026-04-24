import time
import requests
import os
import zlib

# ================= CONFIG =================
WORDS_1_10 = [
    "wise","gas","choice","maze","muffin",
    "gown","flame","camp","hill","deliver"
]

TELEGRAM_TOKEN = "7654735781:AAGcVIbnVux2u1gyBKTS3F9SUmIxZMqXhYg"
TELEGRAM_CHAT_ID = "5568964448"

SEND_LIMIT = 5
MAX_LOOP = 50000
# ==========================================

# ========= TELEGRAM =========
def kirim_sync(msg):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg
        }, timeout=5)
    except:
        pass

# ========= LOAD WORDLIST =========
def load_wordlist():
    print("📦 Loading wordlist (local)...")

    try:
        with open("english.txt") as f:
            words = [w.strip() for w in f if w.strip()]

        print(f"✅ Wordlist loaded: {len(words)}")

        if len(words) < 1000:
            raise Exception("Wordlist tidak lengkap")

        return words

    except Exception as e:
        print("❌ ERROR wordlist:", e)
        return []
