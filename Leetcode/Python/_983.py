class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        days = list(set(days))
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(i - 7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[-1])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
