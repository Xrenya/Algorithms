class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = list(accumulate(stones))
        f = [0] * n
        f[n - 1] = dp[n - 1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], dp[i] - f[i + 1])
        return f[1]
