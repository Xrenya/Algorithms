class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        timestamps = self.map[key]
        l = 0
        r = len(timestamps) - 1
        while l <= r:
            m = l + (r - l) // 2
            if timestamps[m][0] == timestamp:
                return timestamps[m][-1]
            elif timestamps[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        if r >= 0:
            return timestamps[r][-1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
