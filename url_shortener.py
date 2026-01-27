import hashlib

url_db = {}

def shorten_url(long_url):
    short = hashlib.md5(long_url.encode()).hexdigest()[:6]
    url_db[short] = long_url
    return short

def get_original(short_url):
    return url_db.get(short_url, "❌ URL not found")

while True:
    print("\n1. Shorten URL\n2. Open URL\n3. Exit")
    ch = input("Choice: ")

    if ch == "1":
        url = input("Enter long URL: ")
        short = shorten_url(url)
        print(f"🔗 Short URL: {short}")

    elif ch == "2":
        s = input("Enter short URL: ")
        print("➡️ Redirecting to:", get_original(s))

    else:
        break
