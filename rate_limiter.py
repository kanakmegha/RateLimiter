import time
import threading
from collections import defaultdict, deque

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)
        self.lock = threading.Lock()

    def allow_request(self, key: str):
        now = time.time()

        with self.lock:
            window = self.requests[key]

            # Remove expired requests
            while window and window[0] <= now - self.window_seconds:
                window.popleft()

            if len(window) >= self.max_requests:
                return False, len(window)

            window.append(now)
            return True, len(window)
