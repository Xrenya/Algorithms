class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(1, len(dp)):
            dp[i] = min(dp[max(0, i - 1)] + cost[i - 1], dp[max(0, i - 2)] + cost[i - 1])

        return min(dp[-1], dp[-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(cost)):
            first, second = second, min(first + cost[i], second + cost[i])

        return min(first, second)
