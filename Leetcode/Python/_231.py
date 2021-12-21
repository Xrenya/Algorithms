import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        base = math.floor(math.log(n, 2))
        return 2**base == n
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        num = 2
        if n == 1:
            return True
        elif n == 2:
            return True
        while num < n:
            num *= 2
            if num == n:
                return True
        return False
      
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt = 0
        while n:
            if n & 0x1:
                cnt += 1
            if cnt > 1:
                return False
            n >>= 1
        if cnt == 1:
            return True
