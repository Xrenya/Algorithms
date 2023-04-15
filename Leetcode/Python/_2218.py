class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for coins in range(0, k + 1):
                cur_sum = 0
                for cur_coin in range(0, min(len(piles[i - 1]), coins) + 1):
                    if cur_coin > 0:
                        cur_sum += piles[i - 1][cur_coin - 1]
                    dp[i][coins] = max(dp[i][coins], dp[i - 1][coins - cur_coin] + cur_sum)
                    
        return dp[n][k]
