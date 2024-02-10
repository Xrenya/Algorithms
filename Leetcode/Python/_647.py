class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time complexity O(n2)
        # Space complexity O(n)
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


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time complexity O(n3)
        # Space complexity O(1)
        def is_palidrome(s, low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1

            return True
        output = 0
        for low in range(len(s)):
            for high in range(low, len(s)):
                output += is_palidrome(s, low, high)
            
        return output
