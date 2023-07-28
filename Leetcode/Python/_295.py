class HeapMin:
    def __init__(self):
        self.a = []
        self.size = 0

    def push(self, n):
        self.a.append(n)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.a[i] < self.a[(i - 1) // 2]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    def pop(self):
        self.a[-1], self.a[0] = self.a[0], self.a[-1]
        min_n = self.a.pop()
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.a[j] > self.a[2 * i + 2]:
                j = 2 * i + 2
            if self.a[i] < self.a[j]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
        return min_n

    def pushpop(self, n):
        if self.size == 0:
            return n
        self.push(n)
        return self.pop()


class MedianFinder:

    def __init__(self):
        self.size = 0
        self.large = HeapMin()
        self.small = HeapMin()

    def addNum(self, num: int) -> None:
        print("addNum", self.small.a, self.large.a)
        if self.large.size == self.small.size:
            self.large.push(-self.small.pushpop(-num))
        else:
            self.small.push(-self.large.pushpop(num))
        print("addNum", self.small.a, self.large.a)


    def findMedian(self) -> float:
        if self.large.size == self.small.size:
            return (self.large.a[0] - self.small.a[0]) / 2
        else:
            return self.large.a[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
