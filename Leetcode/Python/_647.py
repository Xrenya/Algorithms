class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            cnt += 1
            
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                        cnt += 1
        return cnt
                    
