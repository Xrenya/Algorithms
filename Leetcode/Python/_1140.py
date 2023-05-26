class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[-1] * (n + 1) for i in range(n + 1)] for p in range(0, 2)]

        def func(p, i, m):
            if i == n:
                return 0
            if dp[p][i][m] != -1:
                return dp[p][i][m]
            output = 1000000 if p == 1 else -1
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if p == 0:
                    output = max(output, s + func(1, i + x, max(m, x)))
                else:
                    output = min(output, func(0, i + x, max(m, x)))
            dp[p][i][m] = output
            return output

        return func(0, 0, 1)
