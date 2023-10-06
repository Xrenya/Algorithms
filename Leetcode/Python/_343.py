class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)

        for i in [1, 2, 3]:
            dp[i] = i

        for n in range(4, n + 1):
            output = n
            for i in range(2, n):
                output = max(output, i * dp[n - i])

            dp[n] = output

        return dp[n]
