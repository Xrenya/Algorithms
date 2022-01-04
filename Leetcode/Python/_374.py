# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n + 1
        while l < r - 1:
            m = (l + r) >> 1
            output = guess(m)
            if output == 0:
                return m
            elif output == 1:
                l = m
            else:
                r = m
