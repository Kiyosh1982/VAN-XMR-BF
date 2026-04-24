import time
import os
import zlib
import requests

print("🔥 SCRIPT START")

# test wordlist
try:
    with open("english.txt") as f:
        WORDLIST = [w.strip() for w in f if w.strip()]
    print("✅ Wordlist:", len(WORDLIST))
except:
    print("❌ Gagal load wordlist")
    exit()

print("🚀 START LOOP")

for i in range(5):
    print("Loop ke:", i)
    time.sleep(1)

print("✅ DONE")
        print(f"✅ Wordlist loaded: {len(words)}")

        if len(words) < 1000:
            raise Exception("Wordlist tidak lengkap")

        return words

    except Exception as e:
        print("❌ ERROR wordlist:", e)
        return []
