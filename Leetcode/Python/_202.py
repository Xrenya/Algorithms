class Solution:
    def isHappy(self, num: int) -> bool:
        def decompose(num):
            output = 0
          
            while num:
                output += (num % 10) ** 2
                num = num // 10
            return output
        
        slow = num
        fast = num
        
        while True:
            slow = decompose(slow)
            fast = decompose(decompose(fast))
            if slow == fast:
                break
            
        return slow == 1
