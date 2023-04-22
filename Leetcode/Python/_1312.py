class Solution:
    def minInsertions(self, s: str) -> int:
        def longestPalindromeSubseq(self, s: str) -> int:
            n = len(s)
            dp = [0] * n
            dpPrev = [0] * n

            for start in range(n - 1, -1, -1):
                dp[start] = 1
                for end in range(start + 1, n):
                    if s[start] == s[end]:
                        dp[end] = dpPrev[end - 1] + 2
                    else:
                        dp[end] = max(dpPrev[end], dp[end - 1])
                dpPrev = dp[:]

            return dp[n - 1]

        return len(s) - longestPalindromeSubseq(self, s)
