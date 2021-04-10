class RecentCounter:

    def __init__(self):
        self.array = []

    def ping(self, t: int) -> int:
        self.array.append(t)
        while self.array[0] < t - 3000:
            self.array.pop(0)
        return len(self.array)
            
