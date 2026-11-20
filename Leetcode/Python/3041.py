class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        output = 0
        for n in nums:
            dp[n + 1] = max(dp.get(n + 1, 0), dp.get(n, 0) + 1)
            dp[n] = max(dp.get(n, 0), dp.get(n - 1, 0) + 1)
            output = max(output, dp[n], dp[n + 1])
        return output
