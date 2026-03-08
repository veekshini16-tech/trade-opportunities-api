
class SessionTracker:

    def __init__(self):
        self.sessions = {}

    def track(self, client):
        if client not in self.sessions:
            self.sessions[client] = 0

        self.sessions[client] += 1
