class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        power = [2,3,5,7,13,17,19,31]
        acc = 0
        for p in power:
            acc = 2**(p - 1) * (2**p - 1)
            if num == acc:
                return True
            elif num < acc:
                return False
        return False
