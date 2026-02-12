import time
from collections import deque

class SlidingWindowRateLimiter:
    def __init__(self, max_requests, window_size):
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests = deque()

    def allow_request(self):
        current_time = time.time()

        # Remove expired timestamps
        while self.requests and current_time - self.requests[0] > self.window_size:
            self.requests.popleft()

        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        return False


rl = SlidingWindowRateLimiter(3, 10)

for i in range(6):
    print("Allowed:", rl.allow_request())
    time.sleep(2)
