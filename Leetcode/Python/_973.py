class HeapMin:
    def __init__(self):
        self.a = []
        self.size = 0

    def push(self, n):
        self.a.append(n)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.a[i][0] < self.a[(i - 1) // 2][0]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    def pop(self):
        self.a[-1], self.a[0] = self.a[0], self.a[-1]
        min_n = self.a.pop()[1]
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.a[j][0] > self.a[2 * i + 2][0]:
                j = 2 * i + 2
            if self.a[i] < self.a[j]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
        return min_n
    
            
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = HeapMin()
        for p in points:
            d = sqrt(p[0]**2 + p[1]**2)
            heap.push((d, p))
            
        output = []
        for _ in range(k):
            output.append(heap.pop())
        return output

        
