class HeapMax:
    def __init__(self):
        self.a = []
        self.size = 0
        
    def insert(self, v):
        self.a.append(v)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.a[i] > self.a[(i - 1) // 2]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2
            
    def remove(self):
        self.a[0], self.a[-1] = self.a[-1], self.a[0]
        last = self.a.pop()
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.a[j] < self.a[2 * i + 2]:
                j = 2 * i + 2
            if self.a[i] > self.a[j]:
                break
            else:
                self.a[i], self.a[j] = self.a[j], self.a[i]
                i = j5 
        
        return last
    
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = HeapMax()
        for n in nums:
            heap.insert(n)
            
        for _ in range(k):
            v = heap.remove()
            
        return v


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:                    
        n = len(nums)
        def partition(l, r, pivot):
            pivot_elem=nums[pivot]
            nums[r],nums[pivot]=nums[pivot],nums[r]
            
            index=l
            for i in range(l, r):
                if nums[i]<pivot_elem:
                    nums[i],nums[index]=nums[index],nums[i]
                    index+=1
            
            nums[index],nums[r]=nums[r],nums[index]
            return index
        def quick_select(l,r,kth_index):
            if l==r:
                return nums[l]
            
            pivot_index=partition(l,r,l)
            
            if pivot_index==kth_index:
                return nums[pivot_index]
            
            if kth_index>pivot_index:
                return quick_select(pivot_index+1, r, kth_index)
            else:
                return quick_select(l,pivot_index-1, kth_index)
        
        return quick_select(0, n - 1, n - k)
