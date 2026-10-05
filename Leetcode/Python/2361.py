class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        n = len(regular)
        dp = [[0] * (n + 1) for _ in range(2)]
        
        dp[0][0] = 0
        dp[1][0] = expressCost
        
        for i in range(1, n + 1):
            dp[0][i] = min(dp[0][i-1] + regular[i - 1], dp[1][i-1] + regular[i - 1])
            dp[1][i] = min(dp[0][i-1] + expressCost + express[i - 1], dp[1][i-1] + express[i - 1])
            
        return [min(dp[0][i], dp[1][i]) for i in range(1, n + 1)]
