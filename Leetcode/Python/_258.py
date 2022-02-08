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
            
            
