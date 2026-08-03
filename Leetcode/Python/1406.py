class Solution:
    def stoneGameIII_DP(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = stoneValue[i] - dp[i + 1]
            if i + 2 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - dp[i + 2])
            if i + 3 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3])
            print(dp)
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
    
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache
        def dfs(index):
            if index >= len(stoneValue):
                return 0
            max_score = -float("inf")
            score = 0
            for i in range(3):
                if i + index >= len(stoneValue):
                    break
                score += stoneValue[index + i]
                max_score = max(max_score, score - dfs(index + i + 1))
            return max_score

        r = dfs(0)
        if r > 0:
            return "Alice"
        elif r < 0:
            return "Bob"
        return "Tie"
