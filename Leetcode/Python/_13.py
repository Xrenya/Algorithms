class Solution:
    def romanToInt(self, x: str) -> int:
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        ans = 0
        i = 0
        while i < len(x):
            if i < len(x)-1 and d[x[i]] <  d[x[i+1]]:
                ans += d[x[i+1]] - d[x[i]]
                i += 2
            else:
                ans += d[x[i]]
                i += 1
        return ans
