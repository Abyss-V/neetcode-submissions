class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        r = timestamp
        while r >= 0:
            if r not in self.timestamp[key]:
                r -= 1
            else:
                return self.timestamp[key][r]
        return ""
