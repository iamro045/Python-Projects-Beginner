import threading
import requests

urls = [
    "https://example.com/file1",
    "https://example.com/file2"
]

def download(url):
    r = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"⬇️ Downloaded {filename}")

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
