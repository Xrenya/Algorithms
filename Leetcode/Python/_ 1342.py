class Solution:
    def numberOfSteps (self, num: int) -> int:
        # Do a bitwise opertaion instead of math calculations
        # 14 -> 1110: step = 0
        # >>= 1 bitwise shift to left 111 -> 7 : step += 1
        # >>= 1 bitwise shift to left 11 -> 3 : step += 2
        # >>= 1 bitwise shift to left 1 -> 1 : step += 2
        # >>= 1 bitwise shift to left 0 -> 0 : step += 2
        
        steps = num == 0
        while num > 0:
            steps += 1 + (num & 1)
            num >>= 1
        return steps - 1
      
class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps
        
