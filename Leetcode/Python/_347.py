class HeapMax:
    def __init__(self):
        self.a = []
        self.size = 0
        
    def insert(self, v):
        self.a.append(v)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.a[i][1] > self.a[(i - 1) // 2][1]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2
            
    def remove(self):
        self.a[-1], self.a[0] = self.a[0], self.a[-1]
        last = self.a.pop()
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.a[j][1] < self.a[2 * i + 2][1]:
                j = 2 * i + 2
            if self.a[i][1] > self.a[j][1]:
                break
            else:
                self.a[i], self.a[j] = self.a[j], self.a[i]
                i = j
        return last[0]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = HeapMax()
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        for (k_, v_) in count.items():
            heap.insert((k_, v_))
        output = [0] * k
        for i in range(k):
            output[i] = heap.remove()
        return output
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1
        output = []
        for k, val in sorted(mapping.items(), key=lambda item: item[1], reverse=True)[:k]:
            output.append(k)
        return output
    
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        lst = sorted(counter.items(), key=lambda item: item[1])[-k:]
        out = [(lambda x: x[0])(x) for x in lst]
        
        return out
