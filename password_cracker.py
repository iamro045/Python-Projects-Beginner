import hashlib

target_hash = hashlib.sha256("secret123".encode()).hexdigest()

wordlist = ["admin", "password", "secret123", "welcome"]

for word in wordlist:
    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
        print("🔓 Password found:", word)
        break
