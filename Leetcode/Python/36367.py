class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        counter = 0
        for i in range(len(nums)):
            counter += m - nums[i]
        return counter
