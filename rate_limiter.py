import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.requests = defaultdict(list)

    def allow_request(self, user):
        now = time.time()
        self.requests[user] = [
            t for t in self.requests[user] if now - t < self.window
        ]

        if len(self.requests[user]) < self.limit:
            self.requests[user].append(now)
            return True
        return False

rl = RateLimiter(3, 10)

user = "rohit"
for i in range(5):
    print("Allowed?" , rl.allow_request(user))
    time.sleep(2)
  
