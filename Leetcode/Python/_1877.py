class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        pair = -float("inf")
        while l < r:
            pair = max(pair, nums[l] + nums[r])
            l += 1
            r -= 1
        return pair
