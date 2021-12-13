class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = [0] * n
        l = 0
        r = n - 1
        for i in range(n-1, -1, -1):
            left = nums[l]**2
            right = nums[r]**2
            if left < right:
                array[i] = right
                r -= 1
            else:
                array[i] = left
                l += 1
        return array
                
            
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arrayQueue = collections.deque()
        size = len(nums)
        l = 0
        r = size - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                arrayQueue.appendleft(nums[l]*nums[l])
                l += 1
            else:
                arrayQueue.appendleft(nums[r]*nums[r])
                r -= 1
        return arrayQueue
    
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arrayQueue = collections.deque()
        size = len(nums)
        l = 0
        r = size - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                arrayQueue.appendleft(nums[l]**2)
                l += 1
            else:
                arrayQueue.appendleft(nums[r]**2)
                r -= 1
        return arrayQueue
    
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        index = len(nums) - 1
        output = [None] * len(nums)
        while l <= r:
            left = nums[l]**2
            right = nums[r]**2
            if left < right:
                output[index] = right
                r -= 1
            else:
                output[index] = left
                l += 1
            index -= 1
        return output
