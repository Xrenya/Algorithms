class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1_000_000_007
        dp = [0] * 26
        
        for c in s:
            idx = ord(c) - ord('a')
            dp[idx] = (sum(dp) + 1) % MOD
            
        return sum(dp) % MOD
