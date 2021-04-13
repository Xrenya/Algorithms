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
