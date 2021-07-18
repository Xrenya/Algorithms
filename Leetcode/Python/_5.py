class Solution:
    def longestPalindrome(self, s):
            longest_palindrom = ''
            dp = [[0]*len(s) for _ in range(len(s))]
            for i in range(len(s)):
                dp[i][i] = 1
                longest_palindrom = s[i]

            for i in range(len(s)-1, -1, -1):
                for j in range(i+1,len(s)):  
                    if s[i] == s[j]:
                        if j-i ==1 or dp[i+1][j-1]:
                            dp[i][j] = 1
                            if len(longest_palindrom) < len(s[i:j+1]):
                                longest_palindrom = s[i:j+1]
            return longest_palindrom
