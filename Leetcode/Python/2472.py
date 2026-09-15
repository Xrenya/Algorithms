class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pali = [[False] * n for _ in range(n)]

        for l in range(1, n + 1):
            for left in range(n - l + 1):
                right = left + l - 1
                pali[left][right] = s[left] == s[right] and (l <= 2 or pali[left + 1][right - 1])

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k + 1):
                if pali[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]
