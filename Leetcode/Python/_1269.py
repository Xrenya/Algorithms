class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        arrLen = min(steps, arrLen)
        dp = [[0] * (steps + 1) for _ in range(arrLen)]
        dp[0][0] = 1

        for remain in range(1, steps + 1):
            for cur in range(arrLen - 1, -1, -1):
                ans = dp[cur][remain - 1]
                if cur > 0:
                    ans = (ans + dp[cur - 1][remain - 1]) % MOD

                if cur < arrLen - 1:
                    ans = (ans + dp[cur + 1][remain - 1]) % MOD

                dp[cur][remain] = ans
        return dp[0][steps]
