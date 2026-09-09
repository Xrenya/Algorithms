class Solution:
    def countCommas(self, n: int) -> int:
        p = 1000
        output = 0
        while p <= n:
            output += n - p + 1
            p *= 1000
        return output
