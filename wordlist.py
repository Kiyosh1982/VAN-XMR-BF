WORDLIST = []

with open("english.txt") as f:
    WORDLIST = [w.strip() for w in f if w.strip()]
