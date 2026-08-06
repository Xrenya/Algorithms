class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(num):
            p = 1
            while num > 0:
                p *= num % 10
                num //= 10
                if p == 0:
                    break
            return p % t == 0
        while not check(n):
            n += 1
        return n
