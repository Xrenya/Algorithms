class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = -1
        r = num + 1
        while l < r - 1:
            m = (l + r) >> 1
            n = m * m
            if n == num:
                return True
            elif n < num:
                l = m
            else:
                r = m
        return False
