class Power(object):
    def __init__(self):
        self.max_power = 15
        self.nums = 1
    
    def __iter__(self):
        for i in range(self.max_power + 1):
            yield self.nums
            self.nums *= 4


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = Power()
        for num in power:
            if n == num:
                return True
        return False


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 4 != 0:
                return False
            n //= 4
        return True
