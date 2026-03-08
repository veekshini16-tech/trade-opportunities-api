
import time

class RateLimiter:
    def __init__(self, limit:int, window:int):
        self.limit = limit
        self.window = window
        self.storage = {}

    def allow(self, client):
        now = time.time()
        start = now - self.window

        if client not in self.storage:
            self.storage[client] = []

        self.storage[client] = [t for t in self.storage[client] if t > start]

        if len(self.storage[client]) >= self.limit:
            return False

        self.storage[client].append(now)
        return True
