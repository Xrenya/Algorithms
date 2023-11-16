class MovingAverage:

    def __init__(self, size: int):
        self.q = deque([])
        self.size = size
        self.val = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.val += val
        while self.q and len(self.q) > self.size:
            self.val -= self.q.popleft()
        return self.val / min(len(self.q), self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
