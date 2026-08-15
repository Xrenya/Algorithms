class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        zeros = True

        for i in range(len(nums)):
            total ^= nums[i]
            if nums[i] > 0:
                zeros = False
        
        if total > 0:
            return len(nums)
        return len(nums) - 1 if zeros is False else 0
