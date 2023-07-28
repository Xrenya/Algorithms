class HeapMin:
    def __init__(self):
        self.a = []
        self.size = 0
        
    def insert(self, v):
        self.a.append(v)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.a[i] < self.a[(i - 1) // 2]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2
        
            
    def remove(self):
        self.a[-1], self.a[0] = self.a[0], self.a[-1]
        last = self.a.pop()
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.a[j] > self.a[2 * i + 2]:
                j = 2 * i + 2
            if self.a[i] < self.a[j]:
                break
            else:
                self.a[i], self.a[j] = self.a[j], self.a[i]
                i = j
        return last
    
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = HeapMin()
        self.k = k
        for v in nums:
            self.heap.insert(v)
        while self.heap.size > self.k:
            self.heap.remove()

    def add(self, val: int) -> int:
        self.heap.insert(val)
        if self.heap.size > self.k:
            last = self.heap.remove()
        return self.heap.a[0]
        

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)            

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums) 
                
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
