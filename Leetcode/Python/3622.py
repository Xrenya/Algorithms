class Solution:
    def checkDivisibility(self, n: int) -> bool:
        acc = 0
        m = 1
        cn = n
        while cn:
            acc += cn % 10
            m *= cn % 10
            cn //= 10

        return n % (m + acc) == 0
