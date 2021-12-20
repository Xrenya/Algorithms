class Solution:
    # Constant space
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(second, first + nums[i])
        return second
      
class Solution:
    # dp with linear space 
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(2, n + 2):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
        return dp[-1]
