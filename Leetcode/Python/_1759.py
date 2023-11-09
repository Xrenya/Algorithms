class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        streak = 0
        MOD = 10 ** 9 + 7
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                streak += 1
            else:
                streak = 1

            count = (count + streak) % MOD
        return count 
