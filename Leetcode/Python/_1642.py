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
    
    
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = HeapMin()
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb < 0:
                continue
            heap.push(climb)
            if heap.size <= ladders:
                continue
            bricks -= heap.pop()
            if bricks < 0:
                return i
        return len(heights) - 1


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        allocation = []
        n = len(heights)
        for i in range(n - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(allocation, climb)
            if len(allocation) <= ladders:
                continue
            bricks -= heapq.heappop(allocation)
            if bricks < 0:
                return i
        return n - 1
