import time

class TTLCache:
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl):
        expiry = time.time() + ttl
        self.cache[key] = (value, expiry)

    def get(self, key):
        if key not in self.cache:
            return None

        value, expiry = self.cache[key]

        if time.time() > expiry:
            del self.cache[key]
            return None

        return value


cache = TTLCache()
cache.set("user_1", "Rohit", 5)

print("Initial:", cache.get("user_1"))
time.sleep(6)
print("After expiry:", cache.get("user_1"))
