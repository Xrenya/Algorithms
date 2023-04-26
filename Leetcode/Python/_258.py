class Solution:
    def addDigits(self, num: int) -> int:
        def summator(num):
            acc = 0
            while num:
                acc += num % 10
                num = num // 10
            return acc
        
        while num > 9:
            num = summator(num)
            
        return num
            
            
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
